---
title: "Semantics as the Universal Interface (MMA Belief 5)"
details: "Fifth core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: meaning (semantics) is the universal interface of data modeling. Meaning makes models durable across technology changes, enables interoperability between systems, and is the only thing that allows humans and AI agents to communicate without hallucination. Semantics is positioned as the bedrock of organizational memory and as the missing layer between physical schema and reasoning."
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

# Semantics as the Universal Interface (MMA Belief 5)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 5
**Category:** Architecture Pattern (interoperability layer)
**Status:** Proposed best practice (with strong community reinforcement in the comments)

---

## Overview

Reis's fifth MMA belief names **semantics** — meaning — as the *universal interface* of data modeling. The claim is that meaning is what makes models durable across technology changes, what enables interoperability between systems, and what allows humans and AI agents to communicate without hallucination. Semantics is treated as the bedrock of organizational memory: without it, every system re-interprets the same data in its own way, and no system can reason reliably.

The belief is the connective tissue of the Agentic Era argument: if AI agents are going to consume data, they need a stable semantic layer to anchor on. Reis is explicit that this is not just "add a glossary" — semantics must be machine-consumable, versioned, and independent of any one application's interpretation.

## Core Content

### Reis's three claims for semantics

| Claim | What it implies |
|-------|-----------------|
| **Meaning makes models durable** | Schema changes; semantics survive. A field renamed in the warehouse still means the same thing if its semantic definition is preserved. |
| **Meaning enables interoperability** | Systems can exchange data correctly when they share semantics, not just structure. Two systems with identical schemas but no shared semantics produce silent corruption. |
| **Meaning is the only thing that allows humans and AI to communicate without hallucination** | LLMs and AI agents reason over meaning; without a semantic layer, they confabulate. With a semantic layer, they can ground their reasoning. |

### What Reis means by "semantics" in practice

Reis does not pin a specific formalism, but the belief is consistent with:

- **Glossaries and business vocabularies** — terms and definitions shared across the org
- **Ontologies** — formal specifications of entities, attributes, and relationships (RDF, OWL, SKOS)
- **Taxonomies and controlled vocabularies** — structured hierarchies of terms
- **Semantic layer / metrics layer** — tools (Cube, dbt semantic layer, LookML) that decouple metric definitions from physical tables
- **Metadata catalogs** (DataHub, Atlas, Unity Catalog) — when they capture meaning, not just structure

The unifying requirement is that semantics is **independent of any one database schema or application code** — a point reinforced explicitly in the comment by Larry Burns (see below).

### Larry Burns's reinforcement (comment, Aug 25, 2026)

> "Now, in the age of Agentic AI, semantic data (or metadata as we might call it) must exist independently of both the database schema and the application code, so that it can be consumed mechanically."

Burns extends Reis's claim: semantics must be *physically decoupled* from both schema and code. The modeling tool should be able to generate both the persistence schema **and** the ontology document from a single modeling exercise. This is the operational form of Belief 5.

## Key Insights

1. **Semantics is a first-class deliverable.** Not a documentation afterthought, not a glossary sheet — a modeled artifact with versioning and governance.
2. **Semantics must be machine-consumable.** Glossaries that only humans read are insufficient for AI agents.
3. **Semantics must be independent of schema and code.** Burns's extension: a modeling exercise should generate both persistence and ontology.
4. **Without semantics, AI agents hallucinate.** The Agentic Era makes this practical rather than theoretical.
5. **Interoperability is a semantic problem, not a structural one.** Systems that share semantics but not structure interoperate better than systems that share structure but not semantics.

## Related Concepts

- [[Concepts/agentic-ready-data-modeling]] — the use case that makes semantics non-optional
- [[Concepts/three-worlds-ontology-amorphous]] — Kent's framing of the language layer that semantics formalizes
- [[Concepts/ontology-llm-data-modernization]] — modern LLM-driven ontology construction is the operational form
- [[Concepts/intent-driven-data-modeling]] — intent is one axis of meaning
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
