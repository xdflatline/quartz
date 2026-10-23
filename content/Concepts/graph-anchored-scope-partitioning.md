---
title: "Graph-Anchored Scope Partitioning"
details: "Work-partitioning pattern in which a job is decomposed into a scope document and then distributed across agents by anchoring each agent's scope to a region of the codebase knowledge graph — for example, assigning agents to folders. Scope boundaries therefore coincide with the codebase's own structural boundaries, so parallel agents overlap less and handoffs fall on natural seams."
tags:
  - concept
  - orchestration
  - multi-agent
  - context-engineering
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# Graph-Anchored Scope Partitioning

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Orchestration / Work Partitioning
**Status:** Production-validated (per [[Entities/blitzy]])

---

## Overview

When a fleet of agents works a codebase in parallel, two things decide whether the result is coherent: whether their scopes overlap, and whether the seams between scopes land somewhere sensible. Both are usually left to chance, because the coordinator hands out tasks as a work list and the agents discover their mutual boundaries by running into each other.

This pattern derives scope **from the codebase's structure itself**. The graph's shape determines the partition:

1. Produce a **scope document** — the decomposed description of the job.
2. Break the scope into units.
3. Assign each unit to an agent, anchored on the graph: if the graph is folder-structured, agents get folders and their scope is limited to them.
4. Work items become graph nodes, so they are claimable and their dependencies order execution.

The stated benefit is the coupling: "What that does is it couples us to the graph. Whatever we do has to be on the graph, which is a trade-off."

## Why structural seams beat task-list seams

- **Overlap is designed out, not detected.** Two agents assigned to different folders cannot collide on the same file by construction.
- **Handoffs fall on real boundaries.** Module boundaries, ownership boundaries, and layering boundaries are where context naturally changes.
- **The graph can enforce it.** Because a unit of work is a node with a subgraph, "what may this agent touch" is answerable from the graph.

## Scope as a claim, not an assignment

A subtle but important consequence: because work items are graph nodes, an agent can *find* its work by querying the graph rather than being handed it. Claim-based assignment scales better than push-based assignment when the graph is the shared state — and it removes the coordinator as a scheduling chokepoint.

## Related Concepts

- [[Concepts/graph-anchored-agent-swarm-coordination]]
- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/coordinator-worker-task-dag-orchestration]]
- [[Concepts/parallelism-width-budget]]
- [[Concepts/subagent-context-isolation]]
- [[Concepts/builder-reviewer-task-granularity]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
