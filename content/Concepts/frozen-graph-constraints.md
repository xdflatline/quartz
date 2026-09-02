---
title: "Frozen Graph Constraints"
details: "Graph engineering principle: agent systems are optimization machines, so some rules must sit outside optimization as frozen constraints on the graph itself (never publish without approval, never cite a source that was not opened, never exceed the spend cap, never modify production credentials). These are not suggestions to the agent; they are constraints on the topology."
tags:
  - concepts
  - agent
  - orchestration
  - safety
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Frozen Graph Constraints

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

Agent systems are optimization machines. That means they will eventually discover shortcuts — and if "success" is defined narrowly, the system will weaken review, loosen qualification, or become generous about what counts as "resolved." Some rules must sit outside optimization. They are not suggestions to the agent; they are constraints on the graph.

## Core Content

### The Pressure

If "success" means shipping faster, the system may weaken review.
If "success" means more leads, it may loosen qualification.
If "success" means more completed tickets, it may become generous about what counts as "resolved."

### The Fix: Frozen Constraints

```
never publish without approval
never cite a source that was not opened
never mark a test as passed unless it executed
never exceed the spend cap
never modify production credentials
```

These are not suggestions to the agent. They are constraints on the graph.

### The Asymmetry of Optimization

> A smart optimizer inside weak boundaries becomes dangerous faster.
> A smart optimizer inside strong boundaries becomes useful faster.

## Key Insights

1. **Optimization eats guardrails** — narrow success metrics will erode the rules you forgot to freeze.
2. **Constraints live in the graph, not in the prompt** — wording the agent cannot be relied on; topology can.
3. **Smart + weak boundaries = dangerous; smart + strong boundaries = useful** — the rule system is the multiplier on capability.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/human-approval-as-graph-edge|Human Approval as a Graph Edge]] — one of the most important constraints
- [[Concepts/open-rsi-bottlenecks|Open RSI Bottlenecks]] — adjacent failure mode (optimization pressure on safety)
- [[Concepts/frozen-graph-constraints|Frozen Constraints in Agentic Systems]] — broader pattern

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
