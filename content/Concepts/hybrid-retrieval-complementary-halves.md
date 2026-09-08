---
title: "Hybrid Retrieval as Complementary Halves"
details: "Architectural thesis for agent memory: vector search and knowledge graphs are not competing single-index solutions but complementary halves of the retrieval problem. Vector search handles paraphrase, synonyms, and fuzzy conceptual recall; knowledge graphs handle entities, multi-hop chains, contradictions, and time. A purely vector-based system fails on the bread-and-butter queries of agent memory (exact names, 'who / why,' recency); a purely graph-based system fails on cold start, extraction cost, and free-form fuzz. The production answer is hybrid: run semantic, keyword (BM25), graph, and temporal searches in parallel on every recall, fuse the rankings with reciprocal-rank fusion, and rerank survivors with a cross-encoder."
tags:
  - concepts
  - memory
  - agent
  - rag
  - architecture-pattern
created: 2026-09-08
updated: 2026-09-08
type: concept
sources:
  - "Raw/hindsight-vectorize-knowledge-graphs-vs-vector-search-2026-08-24"
---

# Hybrid Retrieval as Complementary Halves

**Source:** [[Raw/hindsight-vectorize-knowledge-graphs-vs-vector-search-2026-08-24]] — Hindsight / Vectorize blog, 2026-08-24
**Category:** Architecture Pattern
**Status:** Vendor-blessed framing, validated against [[Concepts/hindsight-memory-architecture]] TEMPR implementation

## Overview

The recurring "vector DB vs. knowledge graph" debate for agent memory rests on a false dichotomy: vector search and graphs solve **different halves** of the retrieval problem, and neither half covers the other's queries. The thesis this concept captures is that production-grade agent memory runs **all four** retrieval strategies in parallel on every recall and lets a fusion step decide which one was right for that query:

1. **Semantic** (vector similarity over embeddings) — paraphrase, synonyms, fuzzy conceptual recall
2. **Keyword** (BM25 full-text) — exact names, codes, identifiers, SKUs
3. **Graph** (traversal over precomputed entity / co-occurrence / causal links) — multi-hop "who / why," relationships, contradictions
4. **Temporal** (time-bounded retrieval with spreading activation over events) — "when," "last Tuesday," "before the migration"

The four run concurrently, are merged with **reciprocal-rank fusion (RRF)**, and the survivors are reranked with a **cross-encoder** so the final list orders by actual relevance rather than by whichever strategy shouted loudest.

This is the explicit framing the Hindsight team uses to defend their TEMPR architecture ([[Concepts/hindsight-memory-architecture]] already documents the mechanics). The framing here is the *thesis behind the mechanics* — and it generalises to any agent-memory system, not just Hindsight.

## Why pure vector search breaks for agent memory

A vector index stores **chunks, not entities**. Its superpower — fuzzy semantic matching — is also its predictable failure mode on four query classes that dominate agent memory:

| Failure mode | What the user asks | What vector search returns | Why |
|---|---|---|---|
| **Exact-match slippage** | "What does `HTTP 502` mean in our logs?" | Thematically related chunks about HTTP errors | Embeddings blur the exact token |
| **No entity notion** | "Who else worked with Alice on Project Atlas?" | Chunks that mention Alice, Project Atlas, *separately* | Chunks are islands; no shared node links them |
| **No chain traversal** | "Why did Alice leave, and what happened next?" | A flat cosine-ranked pile | Cosine similarity ranks, it does not traverse paths |
| **No clock** | "What was I working on last Tuesday?" | Whatever embedding happens to be close, regardless of date | Memories are timeless in cosine space |

A common rebuttal is "add BM25 alongside the vector index to fix exact matches." That fix is real but narrow: BM25 closes the exact-token gap and **nothing else**. It still has no notion of entities, no multi-hop, no contradiction handling, and no temporal bound.

## Why pure knowledge graphs break for agent memory

A knowledge graph is a **data model, not a free lunch**. To be useful, something must build it:

- **Extraction** — usually an LLM step over raw text, with all the usual precision/recall tradeoffs
- **Entity resolution** — collapsing "Alice," "Alice Chen," and "she" to one node is a genuinely hard problem (see the Hindsight team's [entity-resolution post](https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory))
- **Edge maintenance** — facts change, and a stale edge is worse than no edge
- **Cold start** — a brand-new graph is empty; first-recall lean on other signals

The graph also has no idea what to do with free-form fuzzy queries ("that thing about the meeting where we argued about pricing"). It excels at structure and falls flat at fuzz.

## The "agent memory is not document RAG" trinity

The reason this thesis lands hardest for *agent* memory specifically — and the part that generic "vector DB vs. graph" debates miss — is three properties that distinguish agent memory from document RAG:

1. **Recurring entities** — the same users, projects, preferences appear again and again. Documents don't recur; users do.
2. **Facts that change** — someone's role, a decision, a status. Yesterday's truth is today's contradiction, and a graph can model the timeline; a vector index cannot.
3. **Time-sensitivity** — "last week," "before the migration," "what changed since." Cosine similarity is timeless; agent memory is not.

These three are precisely the queries pure vector search handles worst and a graph handles best. So "just install a vector database" is the wrong default for agent memory — not because embeddings are useless, but because they only cover the conceptual-similarity slice.

## Division of labor (at a glance)

|  | Vector search | Knowledge graph |
|---|---|---|
| **Best at** | Meaning, paraphrase, synonyms, fuzzy conceptual recall | Entities, relationships, multi-hop "who / why," change over time |
| **Struggles with** | Multi-hop chains, entity relationships, contradictions, time (exact terms are BM25's job) | Cold start, extraction cost, entity-resolution errors, free-form fuzz |
| **Setup cost** | Embed on write — cheap and immediate | Extract, resolve entities, maintain edges |
| **Example it wins** | "Where does Alice work?" | "Why did Alice leave, and who else was on her team?" |

Neither column is the winner, because neither column covers the other's row.

## How it differs from GraphRAG

GraphRAG-style systems build a knowledge graph over a **static document corpus** to answer questions about those documents. The agent-memory case flips the inputs:

|  | GraphRAG | Agent memory |
|---|---|---|
| **Source** | Indexed corpus of documents | Live observations about recurring entities (users, projects, decisions) |
| **Update cadence** | Indexed once, queried many | Updated continuously as new turns arrive |
| **Retrieval context** | Frozen archive | Mid-session, against current conversation state |
| **Contradiction handling** | Rarely a concern | Central — facts change constantly |
| **Time-sensitivity** | Low | High — "last week," "before the migration" |

The underlying idea (structure knowledge as a graph) is shared. The workload (write-heavy, entity-centric, constantly changing) is what makes agent memory its own problem — and why the graph rides **alongside** vector, keyword, and temporal search rather than replacing them.

## Working pattern

For an agent-memory system, the practical takeaway:

1. **Default to hybrid.** Run semantic, keyword, graph, and temporal searches in parallel on every recall. Do not pick one strategy per query in advance.
2. **Fuse, don't substitute.** Reciprocal-rank fusion (RRF) merges the four ranked lists into one. A cross-encoder reranks the survivors so the final ordering reflects true relevance rather than strategy confidence.
3. **Reach for the graph when the question is about entities or connections** — "who," "why," "how are these related," anything ≥1 hop.
4. **Reach for vectors when the question is about meaning** — the user phrases it differently than the memory was written.
5. **Keep the graph in the same database when possible.** Hindsight stores its graph in PostgreSQL alongside its vector and full-text indexes; spinning up Neo4j as a separate service is rarely worth the operational tax for agent-memory workloads.
6. **Budget for entity resolution.** It is the hardest part of building the graph and the most consequential for recall quality.

## Anti-patterns

- **"Just install a vector database" as the agent-memory default** — passes the demo, fails the first hard question about an entity that recurs or a fact that changed.
- **Picking a single retrieval strategy per query type up front** — defeats the fusion's whole point. Let the fusion step decide per-query.
- **Treating the knowledge graph as a replacement for the vector index** — they cover different halves; replacement loses the half the other handles.
- **Standing up Neo4j as a separate service for a workload that fits inside Postgres** — operational tax rarely earns its keep.
- **Skipping entity resolution** — without it, "Alice," "Alice Chen," and "she" remain three nodes and the graph can't answer "who works with Alice."

## Related Concepts

- [[Concepts/hindsight-memory-architecture]] — TEMPR mechanics: the concrete implementation of this thesis
- [[Concepts/hindsight-memory-system]] — Same retrieval architecture under the higher-level Hindsight framework
- [[Concepts/dual-view-evidence-retrieval]] — Zero-Mem's specific dual-view (graph + hierarchy) routing; complementary example of multi-strategy fusion
- [[Concepts/hybrid-local-search-pattern]] — QMD-style local hybrid (semantic + keyword, on-device); narrower scope (two strategies, single-user knowledge base)
- [[Concepts/agent-memory-layer-patterns]] — Broader memory-architecture landscape: constraints / decisions / heuristics tiers

## References

- Raw Article: [[Raw/hindsight-vectorize-knowledge-graphs-vs-vector-search-2026-08-24]]
- Original: https://hindsight.vectorize.io/blog/2026/08/24/knowledge-graphs-vs-vector-search-agent-memory
- Cited: [Entity resolution in agent memory](https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory)
- Cited: [How the 4-way parallel hybrid search works](https://hindsight.vectorize.io/blog/2026/03/27/parallel-hybrid-search)
- Cited: [The case against external vector DBs for agent memory](https://hindsight.vectorize.io/blog/2026/05/12/case-against-external-vector-dbs-agent-memory)
