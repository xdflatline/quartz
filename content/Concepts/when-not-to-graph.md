---
title: "When Not to Graph"
details: "Graph engineering principle: graphs are powerful enough that people overuse them. Use a single agent when the task is small, steps are genuinely sequential, you are still exploring the problem, the cost of coordination exceeds the work, you need one coherent perspective, or the human wants to steer every step. A graph buys width, isolation, and control flow — not taste or truth."
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

# When Not to Graph

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

The 14th and final graph-engineering principle, and the one that prevents the discipline from becoming a religion. Graphs are powerful enough that people start using them everywhere. Do not.

## Core Content

### When to Use a Single Agent

Use a single agent when:

- the task is small
- each step genuinely depends on the previous one
- you are still exploring the problem
- the cost of coordination exceeds the work
- you need one coherent perspective, not broad coverage
- the human wants to steer every intermediate step

### What a Graph Buys — and What It Does Not

> A graph buys **width, isolation, and control flow**.
> It does not automatically buy taste.
> It does not automatically buy truth.
> It does not automatically make a weak task definition better.

Sometimes one good agent with the right tools is the correct architecture.

### The Reframe

> The point is not to graph everything. The point is to recognize when a line is artificially limiting work that was never sequential in the first place.

## Key Insights

1. **Discipline includes refusal** — the most senior graph engineer is the one who says "no graph here."
2. **Coordination has a cost** — a single agent with the right tools beats a 7-node graph for a small task.
3. **Graphs do not fix bad task definitions** — if you do not know what you want, no topology will help.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/agent-first-pipeline-architecture|Agent-First Pipeline Architecture]] — single-agent alternative
- [[Concepts/sdlc-as-context-engineering|SDLC as Context Engineering]] — sometimes the workflow is a single context, not a graph
- [[Concepts/capabilities-first-system-design|Capabilities-First System Design]] — the design order, not the topology

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
