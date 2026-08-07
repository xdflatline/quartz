---
title: "Research Index: Cognitive Locality & the Orchestrator's Tax"
details: "Synthesis of the 2026 Thoughtworks / Martin Fowler thread on subagent design: the real cost of multi-agent work is not parallelism vs. token spend but context pollution in the orchestrator's working memory. Covers the cognitive-locality partition rule, the orchestrator's-tax framing, working-memory preservation as the actual purpose of subagents, the four standing rules (CLAUDE.md), and the design discipline of not encoding decision procedures as process. Adjacent to the broader AI Agent Memory & Orchestration index."
tags:
  - research
  - agent
  - multi-agent
  - orchestration
  - context-engineering
created: 2026-08-07
updated: 2026-08-07
type: research
sources:
  - "[[Raw/martinfowler-orchestrators-tax-2026-07-16]]"
---

# Research Index: Cognitive Locality & the Orchestrator's Tax

**Updated:** 2026-08-07
**Source:** [[Raw/martinfowler-orchestrators-tax-2026-07-16]] ([[Entities/rahul-garg]], Thoughtworks, 16 July 2026; published on Martin Fowler's site)

---

## Overview

This index collects the conceptual thread introduced by [[Entities/rahul-garg]]'s 16 July 2026 post, *The Orchestrator's Tax*, on Martin Fowler's site. The post argues that in long-running multi-agent work, the scarce resource is not tokens but the **quality of the orchestrator's working memory** — and that the conventional case for subagents (parallelism, speed) misses the dominant cost (context pollution, which compounds across the rest of the session).

The thread has three load-bearing pieces:

1. **[[Concepts/cognitive-locality]]** — a partition rule: keep tasks that share a mental model under one agent; split work by *knowledge required*, not by *task granularity*.
2. **[[Concepts/orchestrators-tax]]** — a framing: tokens are spent once, context pollution taxes every later turn; a bigger context window does not fix it.
3. **[[Concepts/working-memory-preservation-subagent-purpose]]** — a reframe of subagent purpose: subagents exist primarily to protect the orchestrator's working memory, not to save time.

The thread also produces four standing rules (encoded in the author's `CLAUDE.md`) and a discipline about when to add a rule at all.

## Concepts

### The core trio (this thread)

- [[Concepts/cognitive-locality]] — partition work by the knowledge each task requires, not by task granularity
- [[Concepts/orchestrators-tax]] — context pollution is the dominant cost in long-running multi-agent work; tokens are one-time, context compounds
- [[Concepts/working-memory-preservation-subagent-purpose]] — subagents exist to protect the orchestrator's working memory, not primarily to parallelize

### Standing rules and the design discipline

The four rules (each is operationalized from one of the three core concepts):

1. **Prefer 2-4 agents per wave** — operationalizes [[Concepts/cognitive-locality]]: above 5, ask whether tasks sharing files or conventions ought to be merged.
2. **Do not poll background agents for status when the answer can be given from what is already known** — operationalizes [[Concepts/orchestrators-tax]]: do not fetch a full transcript to answer a lightweight question.
3. **Do not allow repository-wide git operations inside concurrent agent prompts** — operationalizes [[Concepts/orchestrators-tax]]: the orchestrator's context cannot recover from the structural risk of multiple writers on one tree.
4. **Treat overlapping file ownership as a consolidation signal, not a cue to spawn more agents** — operationalizes [[Concepts/cognitive-locality]] from the failure side.

The design discipline that produced the rules is itself a concept worth preserving:

- **State the missing fact; do not encode decision procedures as process.** Before adding a line to a standing instruction file, ask whether a reasonably competent orchestrator would make the right decision once it knew the one missing fact. If yes, state the fact. If the fix starts specifying approvals, checkpoints, or mandatory steps, that is usually a sign you are encoding process where a small clarification would have done the job.

### Adjacent concepts in the wiki

- [[Concepts/coordinator-worker-task-dag-orchestration]] — the DAG pattern where the tax is paid; cognitive locality applies to the *partition* of its tasks
- [[Concepts/scratchpad-context-window-management]] — same problem (context pollution) at smaller scale (large tool outputs in a single agent)
- [[Concepts/context-as-evolving-playbook]] — the related "context that survives across sessions lives in an external document" thread (Rahul cites his own *Context Anchoring* piece in the post's Related Work)
- [[Concepts/agentic-harness-architecture]] — the broader pattern the standing rules belong to
- [[Concepts/agent-memory-layer-patterns]] — memory-tiering patterns, useful for comparing the orchestrator's working memory with a structured external memory layer
- [[Concepts/multi-agent-orchestration-patterns]] — the broader survey this thread extends

## Entities

- [[Entities/rahul-garg]] — author of the post; Principal Engineer at [[Entities/thoughtworks]]
- [[Entities/thoughtworks]] — Rahul's employer; the same employer as [[Entities/martin-fowler-site]]'s principal
- [[Entities/martin-fowler-site]] — the publication that hosted the post

## Raw Sources

- [[Raw/martinfowler-orchestrators-tax-2026-07-16]] — *The Orchestrator's Tax* by [[Entities/rahul-garg]], 16 July 2026
- (Related, cited in the post's acknowledgments but not yet in the wiki: Birgitta Böckeler, *Harness Engineering*)

## Key Threads/Sources Table

| Source | Topic | Date | Key Items |
|---|---|---|---|
| [martinfowler.com — The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html) | Multi-agent subagent design; context pollution | 2026-07-16 | Coins "cognitive locality"; proposes 4 standing rules; reframes subagent purpose as working-memory preservation |
| (Referenced in post) Birgitta Böckeler, *Harness Engineering* | Harness engineering | 2026 | Named the loop the author was running (feedforward guide + feedback signal + human review) |
| (Referenced in post) Rahul Garg, *Context Anchoring* | Cross-session context survival | earlier | Argues decision context should be externalized to a living document |

## Cross-Cutting Themes

### 1. The orchestrator is the unique component

Across the three core concepts: the orchestrator is the only part of a multi-agent system that accumulates understanding across a long session. It carries design rationale, architectural constraints, and trade-off history. Subagents are meant to be disposable; their exploration, repeated file reads, failed approaches, and noisy intermediate reasoning should *never* return to the main thread. This is the architectural justification for every rule in the post: every rule is a way of protecting the orchestrator's working memory.

### 2. Tokens vs. context is the central distinction

The post separates two costs that are usually lumped together: token cost (one-time, paid and done) and context pollution (compounds, taxes every later turn). A session can be cheap in tokens and still collapse because of context pollution. A bigger context window does not fix pollution — pollution is an attention problem, not a space problem. This is the empirical hook the post builds everything else on.

### 3. Partition by knowledge, not by task

The cognitive-locality rule says: two agents reading the same architecture to do different tasks is a failure of partition, not a failure of delegation. The duplicated orientation produces *similar* intermediate reasoning, which means *similar* intermediate context the orchestrator has to filter. The cost is not the duplicate reads; it is the duplicate noise the orchestrator then carries.

### 4. Subagent design is interface design

A subagent that returns its full raw transcript is a bad subagent, not because the transcript is wrong but because the interface is wrong. The "do not poll background agents for status" rule is, in effect, a rule about not reading the transcript dump. The post's reframe — subagents exist to protect the orchestrator's working memory — changes what "good" subagent design optimizes for: not raw speed or token cost, but the cleanliness of the orchestrator's context across the rest of the session.

### 5. Standing-rule discipline is itself a cost

Every line in `CLAUDE.md` is paid on every future session. The post's heuristic for when to add a line: if a rule specifies a decision procedure (approvals, checkpoints, mandatory steps), you are probably encoding process. State the missing fact and let the orchestrator decide. The author calls this a heuristic, not a law; it is the meta-rule that produced the four concrete rules.

## Open Questions (carried forward from the post)

- **Measurement.** The author did not have per-call token accounting; the ranking of which cost was largest is the orchestrator grading its own mistake, not a measurement. The trustworthy part is narrower: the transcript dumps were real, the timings were real, the status-check path was an avoidable cost. Open question: how do we measure context pollution properly?
- **Model portability.** The thresholds (2-4 agents per wave, 5 as consolidation signal) are calibrated against Claude Sonnet 5. A different model, a different task profile, a different orchestrator would reasonably need a different balance. Open question: how do the rules generalize across models?
- **Process vs. fact.** The post proposes a heuristic for when to add a standing rule (state the fact; do not encode decision procedures) but flags it as "I don't know yet whether that heuristic survives harder cases." Open question: where is the line between a useful fact and an over-specified procedure?

## Next Research Directions

- [ ] **Benchmark the four rules.** Build a small harness that runs an N-task refactor under varying wave sizes (1, 2, 3, 4, 5, 6 agents) and measures *orchestrator context quality* at the end of the session (signal: length of the "what was decided and why" tail of the conversation; coherence of subsequent prompts). Compare against the post's hypothesized sweet spot of 2-4.
- [ ] **Compare to scratchpad at the subagent level.** The AURA [[Concepts/scratchpad-context-window-management]] pattern parks large tool outputs; the orchestrator's-tax pattern implicitly parks large subagent transcripts. Test whether a subagent-side scratchpad (return summary by default, expose exploration tools on demand) measurably reduces orchestrator context pollution.
- [ ] **Add the post's claims to the [[Research/ai-agent-memory-orchestration]] index as a cross-cutting thread.** The two indices should be siblings; the orchestrator's tax is a within-session analog of the cross-session memory-layer work.
- [ ] **Compare cognitive locality to map-reduce partition locality.** The principle has a structural analog in distributed systems (send computation to the data that shares locality; don't shuffle between nodes). Investigate whether a single theoretical frame (something about "mental model = data" and "agent = compute node") covers both, and whether other agent-orchestration patterns (router, sequential handoff, debate) have natural locality rules of their own.
- [ ] **Wait for the post to draw critique.** Single-authored, single-incident — explicitly framed as "exploratory work, built from one real incident, with more open questions than settled answers." Add a "Reception" section to this index once a counter-argument or independent measurement is published.

## References

- Primary: [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
- Author: [[Entities/rahul-garg]] (Thoughtworks), 16 July 2026
- Host: [[Entities/martin-fowler-site]]
- Adjacent index: [[Research/ai-agent-memory-orchestration]]
