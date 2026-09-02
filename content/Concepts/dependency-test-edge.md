---
title: "Dependency Test for Edges"
details: "Graph engineering principle: for every arrow in a workflow, ask 'What exact data crosses this arrow?' If the answer is not nameable in one sentence, the edge is suspicious. Status, completion, or 'so the next agent knows it is done' are not real dependencies."
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

# Dependency Test for Edges

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

A diagnostic for every edge in a multi-agent graph: name the data that crosses the arrow. If you cannot answer in one sentence, the edge is suspicious. The goal is not to maximize parallelism — the goal is to **remove fake synchronization**.

## Core Content

### The Test

> **What exact data crosses this arrow?**

### Examples

| Edge | What crosses? | Verdict |
|------|---------------|---------|
| `review file A → review file B` | Nothing | **Delete the edge** |
| `extract invoices → calculate total` | Invoice values | Keep |
| `generate three headlines → choose the strongest` | Three candidate headlines | Keep |

### Bad vs Good Answer

**Bad:** "The next agent should know the previous agent finished." → That is status, not dependency.

**Good:** "The reviewer receives the researcher's claim, source URL, and evidence excerpt."

Now the edge has meaning.

### The Goal, Restated

> The goal is not to maximize parallelism. The goal is to remove **fake synchronization**.

## Key Insights

1. **Status is not data** — completion signals do not justify an edge.
2. **Edges with no payload are edges with no purpose** — delete them.
3. **Naming the payload is the design** — if you cannot name it, you have not designed the edge.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/order-vs-dependency|Order vs Dependency]] — the upstream diagnostic
- [[Concepts/structured-graph-state|Structured Graph State]] — once the edge has a payload, that payload should be a typed object
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — same idea for tool calls

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
