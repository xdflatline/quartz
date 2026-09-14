---
title: "Mixed Model Arts — Reis (2026)"
details: "Research synthesis of Joe Reis's Mixed Model Arts (MMA) framing for data modeling (Practical Data Modeling Substack, Aug 19, 2026). Nine core beliefs (modeling is one discipline; model the territory not the technology; intent drives structure; time is non-negotiable; semantics are the universal interface; simplicity is a discipline; designed for humans engineered for agents; modeling is a lifecycle; avoid dogma be pragmatic) together form a unified discipline that re-frames data modeling as first-principles work spanning OLTP, OLAP, and AI-agent consumption. Closely related to William Kent's 1978 framing (map vs. territory, models as tools, three-worlds ontology) and to modern ontology/LLM-driven data modernization work."
tags:
  - knowledge-management
  - survey
created: 2026-09-14
updated: 2026-09-14
type: research
sources:
  - "[[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]"
---

# Mixed Model Arts — Reis (2026)

**Updated:** 2026-09-14
**Source:** [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]] — Joe Reis, *The Mixed Model Arts Manifesto*, *Practical Data Modeling* (Substack), 2026-08-19

---

## Overview

This research index organises Joe Reis's **Mixed Model Arts (MMA)** framing of data modeling as published in the *Practical Data Modeling* Substack on 2026-08-19. The manifesto is the foundational text of Reis's forthcoming book and uses mixed martial arts as a deliberate framing metaphor: just as MMA in the 1990s settled centuries of "my style beats your style" arguments by unifying all styles around fundamentals and adapting to context, data modeling is positioned as having its own MMA moment — ending the Kimball/Inmon, normalized/denormalized, and application/analytical tribalisms.

MMA articulates nine core beliefs (below) that together constitute a unified discipline of data modeling spanning OLTP, OLAP, and AI-agent consumption. The framing is closely related to William Kent's 1978 work in *Data and Reality* (see [[Research/data-modeling-philosophy-kent-1978]]); Reis's contribution is to re-state Kent's principles for a contemporary stack (Lakehouse, streaming, semantic layers, agent-facing ontologies) and to make the unification a non-negotiable requirement of the Agentic Era.

## Concepts

### Foundational / methodological

- [[Concepts/unified-modeling-discipline-mma]] — modeling is one discipline, not two (OLTP vs. OLAP, app vs. analytics); same fundamentals (entities, relationships, identity, grain, time, semantics) everywhere
- [[Concepts/model-territory-not-technology]] — model the business reality first; tables, streams, graphs are implementation details
- [[Concepts/intent-driven-data-modeling]] — models must explicitly encode Operational Intent (how the business acts) and Analytical Intent (how it learns)
- [[Concepts/pragmatic-anti-dogma-modeling]] — reject methodology tribalism; understand the full toolkit, pick by context

### Primitives / properties

- [[Concepts/time-as-first-class-modeling-axis]] — every fact needs explicit temporal metadata (event time, valid time, transaction time); state is an illusion, change is the reality
- [[Concepts/semantics-as-universal-interface]] — meaning is the universal interface; makes models durable, enables interoperability, anchors AI-agent reasoning
- [[Concepts/simplicity-as-modeling-discipline]] — complexity is the default entropy; simplicity is discipline, not removal — organize detail so the complex becomes intuitive

### Consumer-facing

- [[Concepts/agentic-ready-data-modeling]] — designed for humans *and* engineered for AI agents; agents are a new first-class consumer of the model
- [[Concepts/modeling-as-continuous-lifecycle]] — no model is "finished"; modeling is a continuous lifecycle, not a phase

### Pre-existing garden concepts MMA resonates with

- [[Concepts/map-vs-territory-data-modeling]] — Kent's 1978 framing (see [[Research/data-modeling-philosophy-kent-1978]]); MMA Belief 2 is a direct restatement for the modern stack
- [[Concepts/three-worlds-ontology-amorphous]] — Kent's ontological framing; MMA Belief 5 (semantics as universal interface) is the operational form
- [[Concepts/data-model-as-tool-not-theory]] — Kent's tools-vs-theories distinction; MMA Belief 9 (pragmatic anti-dogma) is the same pragmatism applied to methodology selection
- [[Concepts/ontology-llm-data-modernization]] — modern LLM-driven ontology construction is the operational form of MMA Belief 5

## Tools & Projects

### People

- [[Entities/joe-reis]] — author; co-author of *Fundamentals of Data Engineering* (O'Reilly, 2022) with Matt Housley
- [[Entities/larry-burns]] — commenter who extended Belief 5 with the requirement that semantics live independently of schema and code

### Publications

- [[Entities/practical-data-modeling]] — Reis's Substack newsletter (>20,000 subscribers as of Aug 2026)
- [[Entities/mixed-model-arts-manifesto]] — the Aug 2026 manifesto itself, as a referenced document

## Raw Sources

- [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]] — full text of the manifesto plus the two most consequential comments (Larry Burns on semantics independence; Guy Kerem on emerging ontologies)

## Key Threads / Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]] | Mixed Model Arts manifesto | 2026-08-19 | 9 core beliefs; MMA metaphor; closing mission |
| Larry Burns comment | Semantics independence | 2026-08-25 | Semantic data must live outside schema and code; modeling tools should generate both persistence and ontology |
| Guy Kerem comment | Emerging interoperable ontologies | 2026-08-24 | Demand-driven standard ontologies: open question |
| [[Raw/bkent-data-reality-excerpts-2026-09-13]] | Kent's 1978 framing | 1978/1998 | Map vs. territory; tools vs. theories; linguistic relativity (see [[Research/data-modeling-philosophy-kent-1978]]) |

## Cross-Cutting Themes

### 1. The Agentic Era is the forcing function for unification

MMA's argument is that the methodological wars of the last forty years (Kimball vs. Inmon, normalized vs. denormalized, app vs. warehouse) were tolerable when humans were the only consumers. With AI agents reasoning, planning, and acting over data, the seams between modeling traditions become bugs: agents cannot reconcile two divergent models of the same reality. Reis's "modeling is one discipline" (Belief 1) is therefore not merely philosophical — it is a hard requirement of agentic consumption.

### 2. The Kent-Reis continuity

Reis does not claim to invent the underlying philosophy; he re-articulates Kent's 1978 framing for the 2026 stack. Belief 2 ("model the territory, not the technology") is the map-vs-territory principle applied to Lakehouse/streaming/semantic-layer choices. Belief 9 ("avoid dogma, be pragmatic") is the tools-vs-theories distinction applied to methodology selection. The MMA framing is best read as a modern re-statement, not an original claim.

### 3. Semantics is the load-bearing concept

If MMA has a single load-bearing belief, it is Belief 5 (semantics as the universal interface). This is the belief that connects the others:

- Belief 1 (unification) needs shared semantics across communities
- Belief 3 (intent) needs semantics to express intent
- Belief 4 (time) needs semantics to disambiguate event vs. valid vs. transaction time
- Belief 7 (agentic-ready) needs machine-consumable semantics for agent reasoning
- Belief 8 (lifecycle) needs versioned semantics that survive schema changes

Burns's comment makes the operational demand explicit: semantics must be *physically decoupled* from schema and code, and modeling tools should generate both artifacts from a single modeling exercise.

### 4. Modeling is operational engineering, not design-time work

Belief 8 (lifecycle) and Belief 6 (simplicity as discipline) reframe modeling as an *ongoing practice*. The implication is organizational: modeling needs permanent ownership, refactoring budget, and tooling for migration and impact analysis. This aligns with the [[Concepts/modeling-as-continuous-lifecycle]] principle and rejects the project-handoff pattern.

### 5. Intent is the bridge between business reality and structure

Belief 3 (intent drives structure) is the operational form of Belief 2 (model the territory). Once the territory is known, the next modeling act is to declare what the model is for. Operational intent and analytical intent make different demands on grain, identity, and time; declaring them upfront prevents the most common modeling failures. The Agentic Era implicitly adds a third intent (how agents will reason over the model) that Reis does not name but that Belief 7 makes necessary.

## Next Research Directions

- [ ] **Survey Reis's other published chapters** (Feb 2026 "Ch 1 - The Era of the Mixed Model Artist"; Nov 2025 "Semantics, Ontology, Taxonomy, and Metadata") for the longer-form treatment of Beliefs 1, 5, 7 — and ingest them when relevant
- [ ] **Compare MMA Beliefs 1–9 with Kent's Chapter 12 framing** (Philosophy, Tools, Points of View) — Kent's text is the closest historical antecedent and the comparison would sharpen the contribution claim
- [ ] **Survey modern semantic-layer tools** (Cube, dbt Semantic Layer, LookML, AtScale) for how they operationalize MMA Belief 5 — and whether they actually decouple semantics from schema, as Burns demands
- [ ] **Test Burns's hypothesis** (comment, Aug 25, 2026): can a single modeling exercise generate both persistence schemas and ontology documents? Survey existing tools (e.g., LinkML, GenSQL, ontology-extraction from ER) for partial implementations
- [ ] **Track the open question Guy Kerem raises** (comment, Aug 24, 2026): does the Agentic Era produce de facto standard ontologies, or does the long tail persist? Revisit in 12–18 months
- [ ] **Connect MMA to [[Concepts/ontology-llm-data-modernization]]** — Reis's MMA Belief 5 and the LLM-driven ontology construction work are converging on the same operational problem from different directions
- [ ] **Cross-reference Reis's *Fundamentals of Data Engineering* (2022)** for the data-engineering-cycle framework, which is the prior foundation MMA builds on

## References

- [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
- Related: [[Research/data-modeling-philosophy-kent-1978]] (Kent 1978, the philosophical antecedent)
