---
title: "ArangoDB"
details: "ArangoDB is a native multi-model database (graph, document, and key-value in one engine) where [[Entities/joerg-schad]] was CTO before joining Pinecone. Notable in this wiki because ArangoDB was an early site of GraphRAG work — graph-based retrieval predating the current wave of GraphRAG papers by several years — and because ArangoDB also built its own in-house vector store, foreshadowing today's graph+vector hybrid designs now codified by Pinecone Nexus. Useful prior art when assessing [[Concepts/multi-modal-context-composition]] (graph + vector + structured in one container)."
tags:
  - entities
  - rag
  - knowledge-management
created: 2026-09-05
updated: 2026-09-05
type: entity
sources:
  - "Raw/sedaily-episode-1951-pinecone-nexus-2026"
---

# ArangoDB

**Source:** [[Raw/sedaily-episode-1951-pinecone-nexus-2026]]
**Category:** Vendor / Multi-model Database
**Notable prior employee:** [[Entities/joerg-schad]] (CTO)

## Overview

**ArangoDB** is a native multi-model database — graph, document, and key-value stores in one engine, queried through a single SQL-like language (AQL). Relevant to this wiki for two reasons:

1. **Schad was CTO there** before joining Pinecone, so ArangoDB's engineering culture directly informed Nexus.
2. **ArangoDB was an early site of GraphRAG** — graph-based retrieval for RAG-style use cases — and built its own in-house vector store, several years before the current GraphRAG wave. This is direct prior art for the [[Concepts/multi-modal-context-composition]] pattern (graph + vector + structured in one container).

## Why ArangoDB is in this wiki

- **Early GraphRAG origin point.** When evaluating "is GraphRAG new?", ArangoDB's pre-2023 internal work is the most-cited counter-example.
- **Multi-model precedent.** A single engine serving graph + document + KV is the database-side analog of Nexus's vector + structured + KG + metadata + permissions composition. The concepts scale up; the same composition pattern that works at the query layer also works at the context-construction layer.
- **Connection to Pinecone.** Schad's move from ArangoDB to Pinecone is not a coincidence — it's the same engineer applying the multi-model idea to the LLM context layer.

## Related Pages

- [[Entities/joerg-schad]] — was CTO at ArangoDB before Pinecone.
- [[Entities/pinecone]] — his current employer; Nexus applies the multi-model idea at the context layer.
- [[Concepts/multi-modal-context-composition]] — the pattern ArangoDB foreshadowed at the storage layer.