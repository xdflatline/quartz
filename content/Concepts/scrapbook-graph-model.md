---
title: "Scrapbook Graph Model"
details: "A graph data model for agent memory in which each memory unit is a 'scrapbook page' and entities (people, places, concepts, classification labels) are 'stickers' anchored to that page. Stickers do not touch each other — there are no entity-to-entity edges. Two memories connect through their shared stickers, through precomputed semantic-neighbor links between memory units, or through explicit causal edges (causes, caused_by, enables, prevents). History is preserved by adding new pages rather than rewriting edges, so contradictions (Alice worked at Acme, then Stark Industries) coexist as time-bounded facts rather than collapsing into a contradictory present-tense edge. Distinct from a traditional knowledge graph (Neo4j-style), which maps direct relationships between entities and loses history when data changes."
tags:
  - concepts
  - memory
  - agent
  - knowledge-graph
  - architecture-pattern
created: 2026-09-08
updated: 2026-09-08
type: concept
sources:
  - "Concepts/hindsight-knowledge-pages-feature"
---

# Scrapbook Graph Model

**Source:** Hindsight FAQ — [How is Hindsight's graph different from a traditional knowledge graph?](https://hindsight.vectorize.io/faq#how-is-hindsights-graph-different-from-a-traditional-knowledge-graph)
**Category:** Architecture Pattern / Data Model
**Status:** Production data model in Hindsight (2026-09)

## Overview

A scrapbook graph is a graph data model in which **memory units are nodes and entities are stickers anchored to those nodes**. There are no edges between entities. Two memories are related when they share a sticker, when a precomputed semantic-neighbor link connects them, or when an explicit causal edge (`causes`, `caused_by`, `enables`, `prevents`) sits between them.

This is the data model used by Hindsight for the graph that powers its `recall` retrieval, and it is the substrate that [[Concepts/knowledge-page-as-projected-view]] pages render over.

## The metaphor

The Hindsight team describes the model with a scrapbook analogy:

```
Traditional knowledge graph:        Hindsight scrapbook:

    [Toronto] ──IS_IN──> [Canada]   Scrapbook page: "Math Class"
                                       [Alice]   [Acme]   [pedagogy:scaffolding]
```

- A **traditional graph** (Neo4j, RDF, property graphs generally) is a **map**. It shows how entities connect directly via labeled edges, mapping rigid structural facts about the world. `[Alice] —WORKS_AT→ [Acme]` is a present-tense claim that must be rewritten when Alice changes jobs.
- A **scrapbook graph** is a **scrapbook**. Each page is a single memory. On that page sit stickers for every entity present in that specific moment. The stickers do not touch each other — they just live on the same page together. Two memories that share a sticker are connected *through the sticker*, not through each other.

## Structural rules

|  | Traditional graph | Scrapbook graph |
|---|---|---|
| Primary nodes | Entities | Memory units |
| Entity representation | First-class nodes with attributes | "Stickers" anchored to memory units |
| Edges between entities | Yes (labeled, directed, attributed) | No — entities do not have direct arrows |
| Edges between memory units | Sometimes | Yes (semantic neighbors, causal links) |
| Handling change over time | Must rewrite the edge | Add a new memory page; old page still accurate |
| Source of contradictions | Edge rewrites collapse history | Pages coexist; query layer reconciles |
| Typical query primitive | Traverse direct edges | Anchor on an entity sticker, expand to its pages |

## How two memories connect

In the scrapbook model, recall starts with semantic search (finding memories relevant to the query as seed pages) and then expands from those seeds through **three parallel signals**:

### 1. Shared entities

If Memory A and Memory B both anchor to the same entity sticker — like `[pedagogy:scaffolding]` — Hindsight traverses `Memory A → [pedagogy:scaffolding] → Memory B`. This is the "scrapbook pages with the same stickers" case. It is the analog of a graph's two-hop traversal, but the intermediate hop is the sticker, not another memory.

### 2. Semantic links between memories

When a new memory is retained, Hindsight **precomputes links to its nearest neighbors in embedding space**. Semantically related pages connect directly without needing a shared sticker. This is the analog of a co-citation graph in document retrieval, but precomputed at retain time rather than computed at query time.

### 3. Causal links between memories

Hindsight also extracts explicit causal relationships — `causes`, `caused_by`, `enables`, `prevents` — between memories. Cause-and-effect chains are first-class edges rather than something the model has to infer. A recall query can ask for "what caused this memory?" or "what did this memory cause?" and traverse the explicit edge.

The semantic layer picks the starting points; the graph fills in the connections through whichever of those three signals is strongest for each candidate.

## Why no entity-to-entity edges?

Three properties drive the choice:

1. **History is preserved, not collapsed.** When Alice changes jobs, the model sees time-bounded facts — `Alice worked at Acme last year, Stark Industries now` — rather than a contradictory present-tense edge. The consuming LLM does not have to reconcile or guess.
2. **Connections come from recorded links, not inference.** When recall surfaces two related memories, it is because they share an entity, a precomputed semantic neighbor, or an explicit causal edge. The link appears in the retrieved context; the model does not have to invent one.
3. **Convergent evidence accumulates.** Multiple memories anchoring to the same sticker reinforce each other instead of competing, giving the model corroborated claims rather than singular unsupported ones.

A traditional graph requires explicit edge maintenance whenever the world changes. The scrapbook model requires only that new memory pages be retained — the graph heals itself by accretion.

## Handling change over time

Traditional graphs struggle with change. If Alice leaves Acme to work at Stark Industries, you must manually delete or rewrite the old `[WORKS_AT]` arrow. If you do not, the graph contradicts reality by stating she works at both places simultaneously. Traditional graphs are built for the absolute present; they lose history when data changes.

The scrapbook model handles change **by adding new pages, not by rewriting old ones**:

```
Scrapbook page: "Tuesday Call"
  [Alice]   [Acme]   [pedagogy:scaffolding]

Scrapbook page: "Friday Call"
  [Alice]   [Stark Industries]   [pedagogy:scaffolding]
```

Both pages are accurate at the time they were made. The graph tracks how the world evolves without complex database maintenance. A query about Alice's employer can return both memories with their timestamps and let the consumer pick the most recent — or return both and let a reconciliation layer decide.

## Where the stickers come from

Sticker creation is a mix of AI automation and developer control:

- **Open-world automation (default):** Hindsight's LLM pipeline automatically detects and extracts standard entities — people, places, dates — from raw text and turns them into stickers.
- **Developer control via `entity_labels`:** A custom schema can be defined using entity labels, forcing the LLM to categorize memories with a strict predefined vocabulary. Instead of letting the AI invent random descriptors, the developer chooses the exact names and parameters — for example, forcing a `pedagogy` key to only choose from `scaffolding`, `direct_instruction`, or `socratic_questioning`. To lock the bank to *only* configured labels, set `entities_allow_free_form: false` — the LLM then skips free-form named entities entirely and emits only entries that match the schema.

This dual control (open-world by default, schema-locked when needed) is what makes the scrapbook model both flexible and governable.

## Working pattern

For a memory system that wants to adopt the scrapbook model:

1. **Pick the memory unit as the primary node.** Do not start from entities — start from observations, facts, or memory units. Entities are anchored *to* memory units, not the other way around.
2. **Make stickers idempotent.** If "Alice," "Alice Chen," and "she" should be the same sticker, resolve them at retain time, not at query time. The whole model assumes sticker identity is stable; unresolved aliases corrupt the shared-sticker expansion signal.
3. **Precompute semantic-neighbor links at retain time.** The cost of precomputing is amortized over many queries; the cost of computing at query time is paid on every retrieval.
4. **Extract causal links explicitly when they matter.** If your domain has chains ("this decision caused that outcome"), make `causes` / `caused_by` first-class rather than expecting the LLM to infer them at query time.
5. **Treat reconciliation as a layer above the graph, not inside it.** The graph preserves contradictions faithfully (multiple pages with overlapping stickers). Reconciliation is the job of the observation layer or the page renderer, not the graph itself.

## Anti-patterns

- **Adding entity-to-entity edges "for convenience."** The moment you write `Alice —WORKS_AT→ Acme`, you have re-introduced the traditional-graph failure mode (present-tense edge, history loss on rewrite).
- **Skipping the semantic-neighbor precomputation.** Without it, every query pays an embedding-similarity cost; with it, the cost is paid once at retain time.
- **Trying to make stickers do the work of edges.** Stickers are a many-to-many anchor; they encode co-occurrence, not directionality. If you need direction (`Alice —EMPLOYS→ Bob`), it belongs as a causal edge or a separate entity-label, not as a sticker topology.
- **Forgetting that the scrapbook preserves contradictions.** If your downstream consumer expects a single reconciled view, you need an observation layer or page renderer to do that — the graph itself will not.
- **Using traditional graph query primitives directly.** Cypher-style traversal over entity-to-entity edges is the wrong tool. The right primitives are: anchor-on-sticker → expand-to-pages → score-by-shared-sticker-count-or-semantic-link-weight.

## Related Concepts

- [[Concepts/knowledge-page-as-projected-view]] — pages render over this graph's memory units; the page renders the reconciled truth the graph preserves faithfully
- [[Concepts/hybrid-retrieval-complementary-halves]] — the broader retrieval thesis (vector + graph + keyword + temporal); the scrapbook graph is the graph in that quartet
- [[Concepts/hindsight-memory-architecture]] — the TEMPR + observation consolidation architecture that uses this graph as its retrieval substrate
- [[Concepts/hindsight-knowledge-pages-feature]] — the product feature that surfaces this graph as browsable pages
- [[Concepts/structured-graph-state]] — the broader class of structured-state patterns in agent systems

## References

- FAQ source: https://hindsight.vectorize.io/faq#how-is-hindsights-graph-different-from-a-traditional-knowledge-graph
- Developer docs: https://hindsight.vectorize.io/developer/retrieval
