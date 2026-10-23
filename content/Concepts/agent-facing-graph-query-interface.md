---
title: "Agent-Facing Graph Query Interface"
details: "Interface pattern where a coding agent is given the schema of its knowledge substrate alongside the tools to query and update it, so the agent formulates its own traversals and semantic searches rather than calling a fixed API surface. Schema exposure — what can be retrieved, what can be written back, how the graph updates on change — is what makes the graph an instrument the agent reasons against rather than a read-only index."
tags:
  - concept
  - agent
  - coding-agent
  - tooling
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Agent-Facing Graph Query Interface

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Tool Design / Interface Pattern
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

When a large codebase is represented as a graph, the agent needs a way in. The design question is whether the agent receives a fixed set of pre-baked operations ("find callers of X", "list files in module Y") or a schema it can reason over and compose its own queries against.

This pattern takes the second route: the agent is given the **schema** of the graph, the **kinds of queries it can make**, the **tools it can call**, and — critically — **what it can write back** when it finds an inconsistency, plus how the graph updates when something changes. The agent then writes its own traversals.

The stated claim is that this is the difference that matters at inference time: *"Giving the agent access to the schema as well as access to the kinds of queries it can make and tools it can call, that's what makes all the difference at inference time."*

## The interface surface

| Capability | What the agent gets |
|---|---|
| Traversal | Graph query language; the agent composes its own traversals rather than calling named operations |
| Semantic search | Embeddings of node summaries, searchable alongside structural traversal |
| Schema | The graph's structure — nodes, edges, types — so the agent knows what kinds of facts are retrievable |
| Write-back | Permission to record findings and inconsistencies it discovers |
| Lifecycle | How the graph changes when code changes; how to update it |
| Node creation | Ability to add new nodes (e.g. attaching a task or a claim to a location in the code) |

## Why query formulation is the agent's job

Fixed operations are the friendlier API but the weaker one. An agent that must pick from a menu of pre-baked queries will pick the nearest menu item and accept the loss, or burn tokens on a sequence of near-miss calls. An agent that understands the schema can ask the question the codebase's shape actually poses — "where do all the authentication patterns live" rather than "grep for auth".

This also makes the graph *writable* by the agent, which is what allows findings to be persisted at the node where they apply, rather than in a side notes file.

## Relationship to retrieval

This pattern sits between two positions usually treated as alternatives:

- **Deterministic search** (grep, symbol lookup) — precise but blind to runtime semantics and to "present but unused" code.
- **Semantic vector search** — fuzzy but loses structural grounding and cannot answer "which of these seventeen candidates is the live one".

Graph traversal over a code-shaped schema, combined with semantic search over the same nodes, answers both: structure narrows the field, meaning disambiguates within it.

## Related Concepts

- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/single-graph-contextualization]]
- [[Concepts/capability-first-tool-design]]
- [[Concepts/coding-agent-tool-taxonomy]]
- [[Concepts/tool-calling-llm]]
- [[Concepts/retrieval-subagent-architecture]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
