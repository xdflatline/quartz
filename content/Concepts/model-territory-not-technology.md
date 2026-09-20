---
title: "Model the Territory, Not the Technology (MMA Belief 2)"
details: "Second core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: data models must reflect the business reality (real-world entities, attributes, relationships, events) first, with the technology implementation (tables, streams, graphs) as a downstream choice. The principle inverts the common engineering instinct to start from the storage engine and contort the model to fit it; it parallels Kent's 1978 map-vs-territory framing for the modern data stack."
tags:
  - concept
  - knowledge-management
  - architecture-pattern
created: 2026-09-14
updated: 2026-09-14
type: concept
sources:
  - "[[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]"
---

# Model the Territory, Not the Technology (MMA Belief 2)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 2
**Category:** Architecture Pattern (modeling principle)
**Status:** Proposed best practice (re-articulation of a classical principle)

---

## Overview

Reis's second MMA belief is the simple inversion of a common engineering failure mode: **model the business reality first, choose the technology second**. Tables, streams, graphs, documents, knowledge graphs, property graphs, vector stores — all of these are *implementation details* of a model that has, at its core, real-world entities, attributes, relationships, and events.

The principle is older than MMA. It is the same move William Kent makes in *Data and Reality* (1978) when he argues that the language and the computer system are both maps, not the territory. Reis's contribution is to re-state the principle for a contemporary stack (Lakehouse, streaming, semantic layers, agent-facing ontologies) where the temptation to anchor on the engine is stronger than ever.

## Core Content

### The inversion Reis is targeting

| Default engineering instinct | MMA belief |
|------------------------------|------------|
| Start with warehouse / lakehouse schema | Start with business entities, attributes, relationships, events |
| "Snowflake vs. BigQuery vs. Databricks" decides structure | Technology chosen to serve the model, not the other way around |
| Schema = the model | Schema = one possible rendering of the model |
| Tables, streams, graphs treated as different disciplines | Treated as different *implementation* of the same model |

### The four primitives Reis names

- **Entities** — the things in the business (a customer, a contract, a shipment)
- **Attributes** — properties of entities
- **Relationships** — connections (customer *has* contracts; contract *contains* line items)
- **Events** — things that happen (a payment cleared; a shipment was delivered)

These four primitives are storage-engine-agnostic. They render into tables, streams, property graphs, RDF triples, or LLM-context documents without changing the underlying model.

### Connection to Kent's framing

The "territory" in MMA is Reis's business reality — the real-world entities and events. The "maps" are the storage representations. Reis is not re-inventing Kent; he is extending the map/territory distinction to the modern data stack and insisting it remain primary.

## Key Insights

1. **Technology is downstream of the model.** Choose storage engine to serve the model, not to dictate it.
2. **The same model has many renderings.** Tables, streams, graphs, documents, ontologies — pick by use case.
3. **Starting from the engine distorts the model.** Anchoring on warehouse features (cluster keys, partitioning, sort orders) too early produces models that don't fit the business.
4. **The principle scales to AI consumption.** Agents need the territory too; exposing engine-specific shapes (warehouse table views) is a leaky abstraction.

## Related Concepts

- [[Concepts/map-vs-territory-data-modeling]] — the 1978 philosophical underpinning (Kent)
- [[Concepts/data-model-as-tool-not-theory]] — the engineering corollary: engines are tools
- [[Concepts/intent-driven-data-modeling]] — the "what is the model for" question that drives territory-first modeling
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
