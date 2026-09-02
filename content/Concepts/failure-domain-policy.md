---
title: "Failure Domain Policy"
details: "Graph engineering principle: each node must live inside an explicit failure domain with a stated policy (retry, fallback, structured failure, quorum, critical). The wrong answer is 'everything dies together.' A 10-worker graph that survives 1 failure with 9/10 disclosed is resilient; one that hides missing work is silently incomplete."
tags:
  - concepts
  - agent
  - orchestration
  - resilience
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Failure Domain Policy

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

A real graph assumes nodes will fail — not because the system is bad, but because distributed work always fails somewhere. The architecture question is **how much of the graph should die with it**. The wrong answer is "everything."

## Core Content

### The Assumption

Distributed work always fails somewhere:
- a request times out
- a source disappears
- a tool returns malformed data
- a model ignores the requested format
- a worker gets rate-limited

### The Per-Node Policy

Each node should live inside a failure domain with an explicit policy:

```
ON FAILURE:
1. retry once
2. retry with fallback model/tool
3. return structured failure
4. continue if quorum is still sufficient
5. block only if this node is critical
```

A graph with ten researchers can still produce a valid report if one fails. But the final output should know that only 9/10 completed.

### The Distinction

> That is the distinction between **resilience** and **silent incompleteness**.

**Never hide missing work. Degrade visibly.**

## Key Insights

1. **Failure is not a bug, it is a topology concern** — design the failure domain before the graph runs.
2. **Resilience is per-node, not per-graph** — the question is which nodes can fail without killing the run.
3. **Quorum-based design** — a 10-worker system with quorum=7 produces valid output as long as 7 complete, and the report should say so.
4. **Silent incompleteness is worse than visible failure** — hiding missing work is the anti-pattern.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/idempotency-for-ai-agents|Idempotency for AI Agents]] — adjacent safety pattern
- [[Concepts/durable-checkpoint-record-and-replay|Durable Checkpoint Record-and-Replay]] — implementation support
- [[Concepts/observational-memory-pattern|Observational Memory Pattern]] — observability that makes failure visible
- [[Concepts/node-failure-rate|Node Failure Rate]] — metric that triggers review of failure domains

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
