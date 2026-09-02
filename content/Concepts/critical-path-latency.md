---
title: "Critical Path Latency"
details: "Graph engineering principle that latency is determined by the longest unavoidable path from start to finish, not the total number of steps. A 40-node graph can finish faster than a 7-node chain if its critical path is shorter. Do not count boxes; look for the longest dependency chain."
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

# Critical Path Latency

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Fundamental (imported from project management; applies as-is to agent graphs)

## Overview

The metric that actually determines how fast a multi-agent graph finishes is the **critical path** — the longest chain of dependent tasks from start to finish. Not the total number of nodes. Not the sum of all task durations. The longest unavoidable path.

## Core Content

### The Distinction

A linear workflow adds durations:
```
8s + 12s + 6s + 10s + 9s ≈ 45s
```

If four of those tasks are independent, the system may only need to wait for the slowest one before merging. Suddenly the important number is not the sum. It is the critical path.

### The Diagnostic

> Do not count boxes. Look for the longest unavoidable path from start to finish. That path determines latency.

Everything else is an optimization opportunity.

### The Counterintuitive Consequence

This is why a 40-node graph can finish faster than a 7-node chain. The graph is bigger. The critical path is shorter.

## Key Insights

1. **Latency ≠ work total** — the question is the longest dependency, not the sum.
2. **Wide graphs win when they shorten the critical path** — width has no value when it sits on the critical path.
3. **Optimize the chain, not the diagram** — the path that determines latency is what to attack.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/order-vs-dependency|Order vs Dependency]] — removing fake dependencies shortens the critical path
- [[Concepts/parallelism-width-budget|Parallelism Width Budget]] — what width actually buys
- [[Concepts/graph-shaped-observability|Graph-Shaped Observability]] — critical-path latency is the first metric to track
- [[Concepts/critical-path-latency|Critical Path]] (planning) — broader concept this borrows from

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
