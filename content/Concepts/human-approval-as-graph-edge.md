---
title: "Human Approval as a Graph Edge"
details: "Graph engineering principle that human approval is a graph edge, not a node. The publishing/irreversible node should be unreachable until approval exists in the graph, not 'instructed in the prompt' or 'usually waited for.' The stronger the consequence, the more approval belongs in architecture, not in wording."
tags:
  - concepts
  - agent
  - orchestration
  - human-in-the-loop
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Human Approval as a Graph Edge

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

The most important shift in how multi-agent systems model humans. Most people model the human as another node (`AI → human → AI`). That is too vague. The human is granting **permission for state to cross a boundary** — which makes approval an edge condition, not a node.

## Core Content

### The Common Mistake

```
AI → human → AI
```

That is too vague. The human is often not "doing work." The human is granting permission for state to cross a boundary.

### The Correct Topology

```
draft campaign
      ↓
quality checks
      ↓
[ HUMAN APPROVAL ]
      ↓
publish
```

The publishing node should literally be unreachable until approval exists. Not:

> "The model was instructed to ask first."
>
> "The agent usually waits."

The graph should make the unsafe transition **impossible**.

### When This Matters Most

Irreversible actions:

- sending money
- deploying code
- emailing customers
- deleting data
- changing permissions
- publishing externally

> The stronger the consequence, the more the approval belongs in architecture rather than prompt wording.

## Key Insights

1. **Approval is an edge, not a node** — the human is a gate on a transition, not a worker.
2. **Architecture > wording for irreversible actions** — "instruct the model to ask" is not enough.
3. **The unsafe transition should be unreachable** — the publish node should not exist in the graph without the approval edge.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/hitl-approval-gates-for-tool-calls|HITL Approval Gates for Tool Calls]] — runtime implementation
- [[Concepts/frozen-graph-constraints|Frozen Graph Constraints]] — what the human-protected transition is protecting
- [[Concepts/agent-turf-war-escalation|Agent Turf War Escalation]] — failure mode that this design constrains
- [[Concepts/human-approval-as-graph-edge|Human-in-the-Loop Approval Gates]] — broader HITL pattern

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
