---
title: "Cognitive Locality"
details: "An agent-orchestration design principle coined by Rahul Garg (Thoughtworks, 2026): partition work by the knowledge or mental model each task requires, not by task granularity. Tasks that need the same mental model should stay together; splitting them just forces multiple agents to rebuild the same understanding from scratch. The principle reframes why subagents exist — not primarily for parallelism, but to keep the orchestrator's working memory clean by isolating each mental model in a single agent."
tags:
  - concepts
  - multi-agent
  - orchestration
  - context-engineering
created: 2026-08-07
updated: 2026-08-07
type: concept
source: "[[Raw/martinfowler-orchestrators-tax-2026-07-16]]"
---

# Cognitive Locality

**Source:** [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
**Category:** Architecture Pattern
**Status:** Proposed best practice (single authored source, July 2026)

---

## Overview

A design principle for multi-agent orchestration: **partition work by the knowledge or mental model each task requires, not by task granularity alone.** When two agents need to understand the same architecture, the same testing conventions, and the same surrounding code, splitting the work between them forces each to pay the orientation cost independently. Cognitive locality says: keep tasks that share a mental model under one agent, even if it means a single agent does more work.

The principle was coined by [[Entities/rahul-garg]] in the post [[Raw/martinfowler-orchestrators-tax-2026-07-16]] to explain an incident where two of four concurrent subagents on a .NET refactor were independently reconstructing the same mental model of the response pipeline. The duplication was not the orchestration failure — the wrong partition was.

## Core Content

### The definition

> "Tasks that need the same mental model should usually stay together. Splitting them just forces multiple agents to rebuild the same understanding from scratch." — Rahul Garg, 2026

Cognitive locality is a *partitioning* rule, not a parallelism rule. It interacts with, but is distinct from, the [[Concepts/coordinator-worker-task-dag-orchestration]] pattern: the DAG decides what tasks to run, cognitive locality decides which tasks belong to the same agent.

### The reframing

The principle reframes what subagents are for. The conventional case for subagents is speed (run N tasks in parallel). The cognitive-locality view is that the real benefit of subagents is **isolation** — keeping noisy intermediate reasoning out of the orchestrator's context and returning only what the orchestrator still needs. Parallelism is a side effect.

> "Get the isolation right, keep things local by cognitive locality, and subagents become the tool that protects the orchestrator's working memory, not just a cost you tolerate for parallelism."

### When to apply

| Signal | Implication |
|---|---|
| Two subagents touch overlapping files, services, or modules | Merge into one agent. Mental model overlap is a consolidation signal. |
| Subagent outputs repeat long preambles ("first, I read the codebase to understand...") | Each agent rebuilt an orientation the others already had. Bad partition. |
| A subagent's task can be described without naming any shared code | Safe to parallelize. Mental model does not overlap. |
| Tasks share a domain vocabulary (e.g. "response pipeline", "billing", "kubernetes cluster") | Single agent. Domain vocabulary = shared mental model. |

### When NOT to apply

- **Independent concerns with no shared code.** A docs-research agent and a test-runner agent have no shared mental model; parallelize freely.
- **Long-running, single-purpose work.** If a single task will take hours, splitting by mental model does not help — the issue is duration, not partition. (The Orchestrator's Tax rules suggest capping the wave at 2-4 agents regardless.)
- **Read-only exploration with no shared artifact.** Two agents reading different parts of an API spec can run in parallel; the orchestrator will fuse the results.

## Key Insights

1. **The failure mode is duplicated orientation, not duplicated work.** When two agents pay the same orientation cost, they produce *similar* intermediate reasoning, which means *similar* intermediate context the orchestrator has to filter. The cost is not the duplicate reads; it is the duplicate noise the orchestrator then carries.
2. **Mental model ≠ task.** The same task ("refactor the response pipeline") can be one agent's job or four. What changes is not what the agent does but what it must understand. Cognitive locality partitions by the *understanding* required, not by the *action* required.
3. **It is a partition rule, not a parallelism rule.** Cognitive locality can be satisfied by *serial* execution. The win is in the orchestrator's context, not in the wall clock.
4. **The principle generalizes outside multi-agent work.** Any context-engineering approach that has to decide "what goes in the main thread" is implicitly applying cognitive locality: group the things that need to be understood together, separate the things that do not.
5. **The name borrows from locality of reference in memory hierarchies.** Just as a CPU cache exploits spatial and temporal locality to avoid round-trips to main memory, an orchestrator's working memory exploits cognitive locality to avoid round-trips through orientation context. The cache analogy is in the post's text.

## Related Concepts

- [[Concepts/orchestrators-tax]] — the framing that motivates cognitive locality (context pollution in the orchestrator)
- [[Concepts/coordinator-worker-task-dag-orchestration]] — the DAG pattern that cognitive locality applies to (decides *what* runs; locality decides *who* runs it)
- [[Concepts/scratchpad-context-window-management]] — same problem, different scale: scratchpad parks large tool outputs to keep them out of the active context
- [[Concepts/agentic-harness-architecture]] — the broader pattern; cognitive locality is one of the standing rules
- [[Concepts/multi-agent-orchestration-patterns]] — the broader survey of multi-agent designs
- [[Concepts/agent-memory-layer-patterns]] — memory-tiering patterns; cognitive locality is the partition that decides which tier each task needs

## References

- Raw Article: [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
- Original: https://martinfowler.com/articles/orchestrator-tax.html
- Author: [[Entities/rahul-garg]] (Thoughtworks), 16 July 2026
