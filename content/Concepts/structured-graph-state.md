---
title: "Structured Graph State"
details: "Graph engineering principle that nodes must exchange explicit typed state objects, not chat transcripts. Structured state gives replaceability (swap workers without rewriting downstream), inspectability (see exactly what entered/left a node), and determinism around the model (fuzzy inside, strict at the interface)."
tags:
  - concepts
  - agent
  - orchestration
  - schema
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Structured Graph State

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

Principle that nodes must exchange explicit typed state objects rather than passing chat transcripts or large prompt blobs. The model can be fuzzy inside the box; the interface around the box stays strict. "The agent can improvise. The graph should not."

## Core Content

### The Failure Mode

Once people discover parallel agents, they usually make the next mistake: every agent receives a huge prompt and returns a huge blob of text. That works in a demo. It collapses in a real graph.

### The Fix: Explicit State Objects

```
ResearchFinding {
  claim
  evidence
  source
  confidence
  timestamp
}
```

The next node is not reading a conversation. It is reading an object.

### Three Benefits

1. **Replaceability** — swap one worker for another without rewriting everything downstream.
2. **Inspectability** — see exactly what entered and left a node.
3. **Determinism around the model** — the model stays fuzzy inside the box; the interface around the box stays strict.

## Key Insights

1. **State ≠ chat** — chat is a serialization, not a contract. Nodes need objects.
2. **Strict outside, fuzzy inside** — the discipline is the interface, not the model behavior.
3. **Replaceability is the unlock** — structured state is what makes worker swaps safe.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/standard-json-schema-tool-contracts|Standard JSON Schema Tool Contracts]] — same idea applied to tool calls
- [[Concepts/dependency-test-edge|Dependency Test for Edges]] — what crosses the edge is now a structured type, not a blob
- [[Concepts/observational-memory-pattern|Observational Memory Pattern]] — adjacent pattern: structured memory, not chat history

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
