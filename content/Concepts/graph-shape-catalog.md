---
title: "Five Graph Shapes"
details: "Graph engineering catalog of five shapes that cover a surprising amount of real multi-agent work: Fork/Join (research, audits, scans), Escalation Ladder (easy cases get cheap checks, hard cases escalate), Tournament (judges pick winner among candidates), Map→Reduce→Verify→Synthesize (decision-grade research), and Bounded Discovery Loop (search until stop condition)."
tags:
  - concepts
  - agent
  - orchestration
  - architecture-pattern
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Five Graph Shapes

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

The article argues you do not need a library of fifty patterns. Five graph shapes cover a surprising amount of real multi-agent work.

## Core Content

### 1. Fork / Join

```
        A
     ↙  ↓  ↘
    B   C   D
     ↘  ↓  ↙
        E
```

Use it for **research, audits, batch analysis, competitive scans**.

### 2. Escalation Ladder

```
cheap check
    ↓ uncertain?
medium check
    ↓ still uncertain?
strong model / human
```

Use it when most cases are easy but a few deserve expensive reasoning.

### 3. Tournament

```
candidate 1 ─┐
candidate 2 ─┼→ judges → winner
candidate 3 ─┘
```

Use it for **copy, designs, plans, code approaches, hypotheses**.

### 4. Map → Reduce → Verify → Synthesize

```
many workers
     ↓
normalize + dedupe
     ↓
attack weak findings
     ↓
final answer
```

Use it for **decision-grade research and large-scale review**.

### 5. Bounded Discovery Loop

```
search
 ↓
new findings?
 ↓ yes
verify → add to seen → search again

stop after:
- no new findings for N rounds
- max spend
- max time
```

Use it when you do not know how large the problem is before starting.

> The budget is part of the topology. Without a stopping rule, a loop is not architecture. It is a leak.

## Key Insights

1. **Five shapes, not fifty** — the article argues this minimal set covers most real workloads.
2. **The Bounded Discovery Loop is the one that needs an explicit stop condition** — without one, the loop is a leak.
3. **Shape selection is part of the spec** — the graph spec template (principle 13) explicitly names the chosen shape.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/graph-spec-template|Graph Spec Template]] — shape selection is one of the spec fields
- [[Concepts/coordinator-worker-task-dag-orchestration|Coordinator-Worker Task DAG Orchestration]] — fork/join under another name
- [[Concepts/escalation-ladder|Escalation Ladder]] — specific page if it exists; otherwise the shape description here stands
- [[Concepts/bounded-discovery-loop|Bounded Discovery Loop]] — same idea

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
