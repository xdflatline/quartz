---
title: "The Orchestrator's Tax"
details: "A framing for the real cost of multi-agent work, coined by Rahul Garg (Thoughtworks, 2026): the orchestrator's working memory, not tokens, is the scarce resource. A token bill is paid once; context pollution taxes every later turn in the session. The post proposes four standing rules (encoded in CLAUDE.md) to keep the orchestrator's context clean: prefer 2-4 agents per wave, do not poll background agents for status, do not allow repo-wide git operations inside concurrent prompts, and treat overlapping file ownership as a consolidation signal."
tags:
  - concepts
  - orchestration
  - context-engineering
  - multi-agent
created: 2026-08-07
updated: 2026-08-07
type: concept
source: "[[Raw/martinfowler-orchestrators-tax-2026-07-16]]"
---

# The Orchestrator's Tax

**Source:** [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
**Category:** Architecture Constraint
**Status:** Proposed best practice (single authored source, July 2026)

---

## Overview

The **orchestrator's tax** is the framing that, in long-running multi-agent sessions, the real cost is not parallelism vs. token spend — it is the **quality of the orchestrator's working memory**. Tokens are spent once and forgotten. Context pollution taxes every later turn. A bigger context window does not fix it: it just gives the noise more room to pile up before anyone notices.

Coined by [[Entities/rahul-garg]] (Thoughtworks, 16 July 2026) in [[Raw/martinfowler-orchestrators-tax-2026-07-16]], the term names the cost that subagent-skeptics keep rediscovering without a word for it: every token in the orchestrator's context is competing for its attention, and the real value of a subagent is what it keeps *out* of that context, not how fast it runs.

## Core Content

### The two costs the post separates

| Cost | Behavior | When it matters |
|---|---|---|
| **Token cost** | One-time, paid and done | Budgeting, total cost of ownership |
| **Context pollution** | Compounds — taxes every later turn | Long-running sessions, multi-step work |

The author argues context pollution is the cost that survives across the session, and that it is what makes subagent design *hard*. Token cost is a billing problem; context pollution is a quality-of-reasoning problem.

> "For years we optimized software systems around CPU, memory, and throughput. The first wave of LLM tooling taught us to watch tokens. This session made me suspect there's a third thing worth watching in long-running agent workflows: the quality of the orchestrator's own working memory, the one resource that, once polluted, keeps charging rent for the rest of the session."

### The incident that surfaced the framing

Four concurrent subagents on a .NET response-pipeline refactor. Wall-clock time looked fine (~12 min vs. ~25 min serialized). The surprising cost was *not* duplicated orientation or unsafe git operations — it was the orchestrator polling background agents and pulling back **the full raw transcript** of one of them (tens of thousands of tokens of JSONL, intermediate reasoning, tool output) on each status check. That transcript stayed in the orchestrator's context and shaped every later turn.

The author flags an important caveat: he did not have per-call token accounting, so the ranking of which cost was largest is the orchestrator grading its own mistake, not a measurement. The trustworthy part is narrower — the transcript dumps were real, the timings were real, and the status-check path clearly introduced a large avoidable cost.

### The four standing rules

The author turned the incident into four rules in `CLAUDE.md`, each answering the same question: *does this piece of information, or this way the work is split, earn a place in the orchestrator's context?*

1. **Prefer 2-4 agents in one wave.** If the orchestrator wants five or more, it should first ask whether tasks sharing files or conventions ought to be merged. (This is the rule that operationalizes [[Concepts/cognitive-locality]].)
2. **Do not poll background agents for status when the answer can be given from what is already known.** Do not fetch a full transcript to answer a lightweight question.
3. **Do not allow repository-wide git operations inside concurrent agent prompts.** (One agent ran `git stash` / `git stash pop` while siblings wrote elsewhere in the same tree. Nothing broke; the risk was structural.)
4. **Treat overlapping file ownership as a consolidation signal, not a cue to spawn more agents.** (This is [[Concepts/cognitive-locality]] again, stated from the failure side.)

None of these prescribe behavior; each gives the orchestrator something to check before acting. The author calls the pattern "the smallest set of rules that addressed the failures I'd seen", and warns that the file is "a sample, not a template" — calibrated against Claude Sonnet 5 and his own workflow.

### Why "the next mistake would have been more governance"

A follow-on incident: skills active in the main thread do not propagate to spawned subagents unless the orchestrator passes them along explicitly. The author's first reaction was to add a confirm-before-spawn gate (list which agents, list which skills, wait for approval). He rejected it: it would have added a round-trip to every similar session, and approval-fatigue is a known failure mode. The narrower fix was to make the orchestrator state, before spawning, which active skills are relevant to each agent's task and point the subagent at the skill file to load.

The general lesson: **before adding a line to a standing instruction file, ask whether a reasonably competent orchestrator would make the right decision once it knew the one missing fact.** If yes, state the fact. If the fix starts specifying a decision procedure (approvals, checkpoints, mandatory steps), that is usually a sign you are encoding process where a small clarification would have done the job.

### Where this leaves the author

A small flywheel, with a human in the middle: session exposes a gap → someone notices it felt wrong → stop the work long enough to inspect → decide if the problem is real or noise → judge what deserves a standing rule → next session tells you whether the rule helped or created different waste.

The thresholds (2-4 agents per wave, 5 as consolidation signal) are *calibrated*, not universal. A different model, a different task profile, a different orchestrator would reasonably need a different balance.

## Key Insights

1. **Tokens vs. context is the central distinction.** The post argues that watching tokens alone misses the dominant cost in long-running work. A session can be cheap in tokens and still collapse because of context pollution.
2. **A bigger context window does not fix pollution.** Pollution is not a space problem; it is an attention problem. A larger window just delays the moment the model notices the noise.
3. **The orchestrator is unique in the system.** It is the only part that accumulates understanding across a long session (design decisions, architectural constraints, trade-offs already discussed). Subagents are meant to be disposable; their exploration, failed approaches, and noisy intermediate reasoning should never make the trip back to the main thread.
4. **Standing-rule discipline is a cost in itself.** Every line in `CLAUDE.md` is paid on every future session. The post's heuristic: if a rule specifies a decision procedure, you are probably encoding process. State the missing fact and let the orchestrator decide.
5. **Self-critique is a real signal but a noisy one.** The orchestrator grading its own session is useful evidence (it surfaced the transcript-poll issue here) but it cannot be the ground truth — it is the agent judging its own choices. The post explicitly downgrades the ranking of which cost was largest to "the orchestrator's account, not a measured fact."

## Related Concepts

- [[Concepts/cognitive-locality]] — the partitioning rule that operationalizes the orchestrator's tax
- [[Concepts/coordinator-worker-task-dag-orchestration]] — the DAG pattern where the tax is paid
- [[Concepts/scratchpad-context-window-management]] — same problem, different scale (tool outputs, not subagent transcripts)
- [[Concepts/context-as-evolving-playbook]] — the related "context as a living document" thread Rahul cites in Related Work
- [[Concepts/agentic-harness-architecture]] — the broader pattern; the standing rules are one of its artifacts
- Birgitta Böckeler, "Harness Engineering" (cited in the post's acknowledgments as the source of the feedforward-guide-meets-feedback-signal framing)

## References

- Raw Article: [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
- Original: https://martinfowler.com/articles/orchestrator-tax.html
- Author: [[Entities/rahul-garg]] (Thoughtworks), 16 July 2026
- Related work cited in the post: Birgitta Böckeler, "Harness Engineering" (Medium, 2026) and "Context Anchoring" by the same author
