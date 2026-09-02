---
title: "Parallelism Width Budget"
details: "Graph engineering principle: parallelism reduces wall-clock time but not total work, and wide graphs create new costs (duplicated research, conflicting outputs, rate limits, merge pressure, verification load, context at the final stage). Set an explicit width budget; optimize for useful independent coverage per dollar, not agent count."
tags:
  - concepts
  - agent
  - orchestration
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Parallelism Width Budget

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

Parallelism is the obvious win, but it is not free. Every extra worker has a reconciliation cost. The principle: set an explicit width budget and optimize for **useful independent coverage per dollar**, not for the number of agents.

## Core Content

### The Hidden Costs of Width

Wide graphs create new costs the linear case did not have:

- more duplicated research
- more conflicting outputs
- more rate limits
- more merge pressure
- more verification
- more context at the final stage

Parallelism reduces **wall-clock time**. It does not magically reduce the amount of work.

### The Width Budget Rule

> **Add width only when the extra worker increases coverage more than it increases reconciliation cost.**

Think of it like memory allocation. You would not launch 500 database queries just because the database technically accepts connections. Do not launch 500 agents just because your runtime technically can.

### What Good vs Bad Width Looks Like

- **Good** — Five researchers on five genuinely different angles. Each adds independent coverage.
- **Bad** — Fifty researchers searching the same topic with slightly different prompts. That is noise generation, not coverage.

### The Unit to Optimize

> The unit you should optimize is not "number of agents." It is **useful independent coverage per dollar**.

## Key Insights

1. **Width is a budget, not a default** — every extra worker has a reconciliation cost.
2. **Diminishing returns are real** — five agents can be excellent; fifty on the same topic is usually noise.
3. **The metric is coverage-per-dollar** — not agent count, not total work.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/critical-path-latency|Critical Path Latency]] — what width actually buys you
- [[Concepts/fan-out-efficiency|Fan-out Efficiency]] — the observability metric that surfaces this
- [[Concepts/deterministic-reduce-before-synthesis|Deterministic Reduce Before Synthesis]] — the merge pressure relief
- [[Concepts/parallel-subagent-process-manager|Parallel Subagent Process Manager]] — runtime fan-out implementations

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
