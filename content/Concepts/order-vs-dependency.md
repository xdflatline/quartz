---
title: "Order vs Dependency"
details: "Graph engineering principle that confuses order with dependency, the most common waste in a multi-agent workflow. The diagnostic question is not 'what comes next?' but 'what information must exist before this can start?' Fake dependencies are exposed immediately by that question."
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

# Order vs Dependency

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

The first of the 14 graph-engineering principles. The most common waste in a multi-agent workflow is confusing **order** with **dependency** — running tasks sequentially because they were listed sequentially, when the later task does not actually consume anything produced by the earlier one.

## Core Content

### The Diagnostic

> The important question is not: "What comes next?" It is: **"What information must exist before this can start?"**

If task B never consumes anything produced by task A, then A → B is not a real dependency. It is just waiting.

### Canonical Example

A 4-step workflow (inspect pricing → inspect customer reviews → inspect product documentation → write market brief) is usually run sequentially. But the first three are independent; they only need to finish before step four.

```
            pricing ──────┐
                          │
reviews ──────────────────┼──→ market brief
                          │
      docs ───────────────┘
```

That drawing contains more engineering information than the numbered list.

## Key Insights

1. **Sequential numbering is a smell, not a specification** — a numbered list tells you an order, not a dependency structure.
2. **The diagnostic is one question** — name the data that must exist, or admit the edge is fake.
3. **Removing fake dependencies is the free win** — they cost latency and budget for zero information gain.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/dependency-test-edge|Dependency Test for Edges]] — the next-level diagnostic
- [[Concepts/critical-path-latency|Critical Path Latency]] — once you remove fake dependencies, the critical path shortens

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
