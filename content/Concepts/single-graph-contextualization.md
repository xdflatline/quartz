---
title: "Single-Graph Contextualization"
details: "Context-engineering pattern that avoids maintaining several parallel knowledge graphs — commits, files, folders, tasks, pattern learnings — by applying each source's learnings directly to the nodes of a single graph whose shape mirrors the codebase. Every datum is contextualised by where it lives in the code, so agents retrieve one coherent structure instead of reconciling multiple views."
tags:
  - concept
  - context-engineering
  - architecture-pattern
  - agent
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Single-Graph Contextualization

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Context Engineering Pattern
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

Most agent memory and retrieval systems accumulate several parallel stores — a commit-history graph, a file-structure graph, a folder graph, a task list, a separate notes or memory file system. Each is individually reasonable. Together they create a reconciliation problem: an agent must decide which store answers its question, and the stores disagree about scope, naming, and recency.

Single-graph contextualization replaces the set with **one graph whose shape mirrors the codebase's own structure**, into which every other source's learnings are folded as attributes or attached nodes. The stated benefit is not efficiency but *legibility*: "You don't have multiple graphs that you're trying to deal with. You have all the information contextualized."

## The failure it prevents

Each additional graph multiplies the retrieval decision an agent must make:

- *Where does the answer live?* The commit graph, the code graph, or the notes?
- *Which is authoritative for this file?*
- *Are these two mentions of the same subsystem the same thing?*

A second, subtler failure: a graph whose shape does not match the codebase's shape forces the agent to translate between shapes on every query. Matching the shape means a folder-scoped question is a folder-scoped traversal.

## The mechanism

1. Build one graph whose nodes and edges mirror the codebase's structure — files, modules, folders, features, dependencies.
2. For each additional knowledge source (commit history, `AGENTS.md`, `skills.md`, generated docs), identify which nodes it is relevant to and apply its learnings **to those nodes**.
3. Do not maintain a separate graph for that source. The source is consumed; its residue lives in the code-shaped graph.

Commit history is the worked example: relevant commits are processed and their learnings applied to the corresponding graph nodes, so "this is how we do it here" is a property of a place in the code, not a searchable anecdote in a parallel timeline.

## Recency weighting

The pattern carries a recency rule: when a codebase has migrated from an old pattern to a new one, the old pattern may still be visible in comments or history. The agent that applies patterns weighs recency, so "I have this, but don't do that" is honoured. This is a property of the *attribute on the node*, not a separate rule engine.

## Related Concepts

- [[Concepts/codebase-knowledge-graph-context-substrate]] — the substrate this pattern populates
- [[Concepts/agent-facing-graph-query-interface]]
- [[Concepts/graph-anchored-agent-swarm-coordination]] — the same single graph also serves as the coordination surface
- [[Concepts/provenance-preserving-memory-substrate]]
- [[Concepts/knowledge-page-as-projected-view]]
- [[Concepts/context-as-materialized-view]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
