---
title: "Procedural Graph Representation"
details: "A directed, attributed graph data structure that organizes procedural knowledge as (procedure, relation, procedure) triplets, with each edge carrying textual condition, guidance, and pitfalls attributes. Where a knowledge graph answers what-is questions with (entity, relation, entity), a Procedural Graph answers what-to-do questions with (procedure, relation, procedure). Nodes abstract tool actions, reasoning steps, or task statuses; edges encode admissible transitions; attributes describe when the transition fires, how to proceed, and what to avoid. The graph sits outside model weights — inspectable, retrievable per-step, editable without retraining."
tags: [concepts, agent, llm, graph-engineering, knowledge-representation]
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - .Raw/arxiv-procedural-graphs-2026-09-08.md
  - .Papers/procedural-graphs-2026-09-08.md
---

# Procedural Graph Representation

**Source:** [[Raw/arxiv-procedural-graphs-2026-09-08]] · [[Papers/procedural-graphs-2026-09-08]]
**Category:** Knowledge Representation
**Status:** Active research area (introduced Lu et al. 2026)

## Overview

A **Procedural Graph (PG)** is a directed, attributed graph that externalizes an agent's procedural knowledge — *what to do, in what order, under which conditions* — into a graph object that lives outside model weights. The representation is the *what-to-do* counterpart to a knowledge graph: where a KG triples factual claims as (entity, relation, entity), a PG triples action paths as (procedure, relation, procedure). Edges carry not just relation labels but three action-time textual fields (condition, guidance, pitfalls) that a guidance model can read to produce situational advice at inference time.

## Core Content

### Formal Definition

$$\mathcal{G} = (\mathcal{V}, \mathcal{R}, \mathcal{E}, \Phi), \qquad \mathcal{E} \subseteq \mathcal{V} \times \mathcal{R} \times \mathcal{V}$$

- $\mathcal{V}$ — abstract nodes; each node is one of: tool action, skill, internal reasoning step, task status
- $\mathcal{R}$ — relation vocabulary; finite, domain-defined. In the PG paper: `LEADS_TO`, `TRIGGERS`, `PROVIDES_INPUT_FOR`, `CONVERGES_TO`
- $\mathcal{E}$ — directed attributed triplets $(u, r, v)$ meaning "$v$ is admissible after $u$ under relation $r$"
- $\Phi(e)$ — attribute map: in the reference implementation, three named textual fields per edge

### Edge Attribute Schema

The paper's canonical schema is three fields per edge, all natural-language strings:

| Field | Purpose | Example (financial-planning edge) |
|-------|---------|-----------------------------------|
| `condition` | When the transition applies | "projected runway falls below the safety buffer" |
| `guidance` | How to proceed on this transition | "submit the request early to allow for the financing delivery delay" |
| `pitfalls` | What to avoid | "do not stack a second request while one is pending" |

Any field can be `null` if the field does not apply (e.g., unconditional transitions have null conditions). Attribute updates are performed as *delete-then-add* on the edge, giving the same edit interface for topology and attributes.

### Knowledge Graph vs Procedural Graph

| | Knowledge Graph | Procedural Graph |
|---|---|---|
| Triple form | (entity, relation, entity) | (procedure, relation, procedure) |
| Question answered | *what is* | *what to do next* |
| Edge content | relation label | relation + condition + guidance + pitfalls |
| Use site | retrieval for facts | generation of action-time advice |
| Construction | (typically) extracted from text corpora | (typically) learned from execution feedback |

This contrast is the paper's central framing: existing procedural memory (MemoryBank, ExpeL, AutoGuide, AWM, KnowAgent) flattens procedure into text or sequences, leaving transitions implicit. The PG makes them explicit, inspectable, and editable.

### Compactness in Practice

The PG paper reports graph sizes for each benchmark used in main experiments. Most are strikingly small — the procedure graph is a human-auditable artifact, not a knowledge-base-scale object:

| Benchmark | Nodes | Triplets |
|-----------|-------|----------|
| HotpotQA | 9 | 9 |
| MultiChallenge | 7 | 7 |
| GDPval | 15 | 22 |
| ALFWorld | 11 | 27 |
| τ-bench | 17 | 18 |
| BFCL v3 | 131 | 265 |
| EnterpriseArena | 11 | 13 |

BFCL v3 is the only outlier, mirroring its large function-calling catalog. Compactness is a property, not an accident: the relation vocabulary is constrained (four relations in the experiments) and node types are the tools plus reasoning primitives.

## Key Insights

1. **Procedural knowledge is structured, not flat.** The KG-vs-PG framing exposes a category error in many prior memory baselines: they store procedure as text or as a flat summary, then expect the solver LLM to reconstruct ordering and admissibility at runtime. A PG makes those reconstructions a graph query.
2. **Edges carry *action-time* affordances.** `condition`/`guidance`/`pitfalls` are the three fields an actor needs to make a decision; a KG's plain relation label does not suffice. This is the difference between *what connects to what* and *what to do given the connection*.
3. **The graph is outside model weights.** PG lives as a data object that can be inspected, versioned, diffed, shared across agents, and edited without retraining. This shifts procedural knowledge from a model property to a system property.
4. **Topology and attributes share one edit interface.** An attribute change is a delete-then-add of the edge. This keeps the evolution loop simple — one refiner prompt produces JSON edits that work for both structural and textual mutation.
5. **Compact graphs generalize.** Despite having at most 17 nodes outside BFCL v3, the PG outperforms every baseline on every benchmark it was tested on. Small explicit structure beats large flat memory here.

## Related Concepts

- [[Concepts/graph-engineering-discipline]] — broader discipline of designing multi-agent topology; PG is one graph-engineering choice for *procedural* knowledge
- [[Concepts/graph-based-workflow-engine]] — typed graph workflows (Mastra/LangGraph); hard-pre-determined graphs, not learned or evolvable
- [[Concepts/graph-shape-catalog]] — five canonical shapes (Fork/Join, Escalation Ladder, Tournament, Map→Reduce→Verify, Bounded Discovery Loop); PG sits closer to "Bounded Discovery Loop"
- [[Concepts/structured-graph-state]] — explicit state objects for graph execution; PG's nodes abstract state transitions
- [[Concepts/deterministic-reduce-before-synthesis]] — PG is a soft analog: deterministic selection of relevant edges before the LLM synthesis step
- [[Concepts/generative-pg-guidance]] — how the graph is consumed at inference
- [[Concepts/pg-self-evolution-loop]] — how the graph is updated offline
- [[Concepts/localized-subgraph-vs-full-graph-guidance]] — empirical finding that localized subgraph > full-graph

## References

- Raw: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Paper: [[Papers/procedural-graphs-2026-09-08]]
- Original: https://arxiv.org/html/2609.09153v1