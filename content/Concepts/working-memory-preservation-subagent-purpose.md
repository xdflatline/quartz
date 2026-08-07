---
title: "Working-Memory Preservation as Subagent Purpose"
details: "A reframing of the design rationale for subagents (Rahul Garg, Thoughtworks, 2026): subagents exist primarily to protect the orchestrator's working memory by isolating disposable reasoning in worker contexts, not to save time through parallelism. The reframe changes what 'good' subagent design optimizes for — not raw speed or token cost, but the cleanliness of the orchestrator's context across the rest of the session."
tags:
  - concepts
  - agent
  - context-engineering
  - orchestration
created: 2026-08-07
updated: 2026-08-07
type: concept
source: "[[Raw/martinfowler-orchestrators-tax-2026-07-16]]"
---

# Working-Memory Preservation as Subagent Purpose

**Source:** [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
**Category:** Architecture Pattern
**Status:** Proposed best practice (single authored source, July 2026)

---

## Overview

A reframe of *why subagents exist*. The conventional case is parallelism: split a task into N parts, run them in parallel, finish faster. The reframing argues that the *real* value of a subagent is **isolation** — keeping the orchestrator's working memory clean by parking disposable reasoning (exploration, repeated file reads, failed approaches, intermediate JSONL transcripts) in the worker context so it never makes the trip back to the main thread.

This is a distinction, not a contradiction: subagents can do both. The argument is that, when design choices trade one off against the other, **isolation should win.**

## Core Content

### The conventional case vs. the reframe

| View | What subagents optimize for | What "good" looks like |
|---|---|---|
| Conventional | Wall-clock time on a fixed task | N parallel workers finish in T/N + dispatch overhead |
| Reframed | Quality of the orchestrator's working memory over the full session | The main thread ends the session with clean context, full of the trade-offs and decisions it will need later |

### Why the reframe matters

The conventional view optimizes for *one* moment in the session: the moment the subagent returns its result. The reframed view optimizes for the *whole* session after. A subagent that returns its result fast but pollutes the orchestrator's context with 50K tokens of intermediate reasoning is a net loss, because every later turn now has to compete with that noise.

> "This is what subagents are actually for. Not that they save time, but that they let you offload reasoning the orchestrator doesn't need to hold onto, so it has less to carry and less competing for its attention."

### Practical implications

- **Subagent design is interface design.** A subagent that returns its full raw transcript is a bad subagent, not because the transcript is wrong but because the interface is wrong. A good subagent returns a *summary* the orchestrator can act on, plus explicit pointers if the orchestrator needs to go deeper.
- **The orchestrator must respect the isolation.** Polling a background agent "to see how it's going" defeats the design. If you can answer from what is already known, answer from what is already known.
- **Cognitive locality (the partition rule) follows from the reframe.** If subagents exist to protect the orchestrator's working memory, the question of which tasks belong in which subagent is no longer "how do I parallelize?" — it is "which tasks share a mental model and should not be split?"
- **The orchestrator is unique in the system.** It is the only part that accumulates understanding across a long session. Subagents are meant to be disposable. Designing them to be load-bearing pieces of the main thread's memory is a category error.

### What this is not

- **Not "subagents are bad".** The post is explicitly pro-subagent. It is pro-subagent-under-discipline, anti-subagent-as-default.
- **Not "tokens don't matter".** Tokens still matter; they are just the *one-time* cost. The post is about the cost that compounds.
- **Not "parallelism is useless".** Parallelism is useful. It is just ordinary — the isolation is the actual win.
- **Not measured.** The author is explicit that this is a "working belief" from one incident, not a measurement. The trustworthy part of the data is narrower: the transcript-poll cost was real, the timings were real, and the status-check path was an avoidable cost. The broader claim (that isolation is *the* reason subagents are valuable) is a hypothesis, not a benchmark.

## Key Insights

1. **The reframe changes what you measure.** If you only measure wall-clock time and token spend, you will keep building subagents that look fine in the metrics but degrade the session. The metric that matters is "how clean is the orchestrator's context at minute N?"
2. **Subagent interfaces are the design lever.** A well-designed subagent returns a small, structured summary. A poorly-designed one returns a transcript dump. The post's "do not poll background agents for status" rule is, in effect, a rule about not reading the transcript dump.
3. **The orchestrator's uniqueness justifies the reframe.** Most of what the orchestrator holds (design rationale, trade-off history, architectural constraints) cannot be regenerated by reading the code. Subagents can be told to re-orient. The orchestrator cannot — it has to keep its context clean precisely *because* its contents are not reproducible.
4. **This reframe aligns with harness engineering.** The author cites Birgitta Böckeler's harness-engineering framing: a feedforward guide (the CLAUDE.md rule) meets a feedback signal (the orchestrator's self-critique, plus a human review), with a human steering the update. What the post describes — using subagents deliberately to protect what the orchestrator carries forward — is "a fourth kind of harness: the orchestration process itself."

## Related Concepts

- [[Concepts/orchestrators-tax]] — the framing that motivates the reframe
- [[Concepts/cognitive-locality]] — the partition rule that follows from the reframe
- [[Concepts/scratchpad-context-window-management]] — same reframe at smaller scale (one agent, large tool outputs)
- [[Concepts/context-as-evolving-playbook]] — related: context that survives the session boundary lives in an external document
- [[Concepts/agentic-harness-architecture]] — the broader pattern the reframe is one component of
- Birgitta Böckeler, "Harness Engineering" (cited in the post's acknowledgments as the source of the feedforward-guide-meets-feedback-signal framing)

## References

- Raw Article: [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
- Original: https://martinfowler.com/articles/orchestrator-tax.html
- Author: [[Entities/rahul-garg]] (Thoughtworks), 16 July 2026
