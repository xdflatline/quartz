---
title: "Three-Worlds Ontology and the Amorphousness of Information"
details: "William Kent's claim that the world of data modeling comprises three nested layers — reality itself, the natural language used to describe it, and the computer data model — and that the inner layers are maps of maps rather than faithful copies. Reality, at bottom, is amorphous, disordered, contradictory, and view-dependent; this is why no adequate formal modelling system exists."
tags:
  - knowledge-management
  - architecture-pattern
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "[[Raw/bkent-data-reality-excerpts-2026-09-13]]"
---

# Three-Worlds Ontology and the Amorphousness of Information

**Source:** William Kent, *Data and Reality* (1978/1998), Chapter 12: Philosophy ([[Raw/bkent-data-reality-excerpts-2026-09-13]])
**Category:** Architecture Constraint (philosophical / ontological)
**Status:** Fundamental

---

## Overview

Kent's **three-worlds ontology** is implicit in the Preface and explicit in Chapter 12. There are three worlds, not one, and they are not isomorphic:

1. **The world of reality** — actual people, events, attributes, relationships as they exist independently of any description.
2. **The world of language** — the constructs (entities, categories, names, relationships, attributes) we use to *talk* about reality, including natural language and any modelling vocabulary.
3. **The world of the computer** — formal data structures (records, hierarchies, relations, objects) we impose to *process* information about reality.

Each layer is a map of the previous one. Crucially, **reality itself is amorphous** — disordered, contradictory, non-rational, non-objective — so the isomorphism Kent worries about is not just a technical difficulty but an ontological impossibility.

## Core Content

### The amorphousness hypothesis

> "This book projects a philosophy that life and reality are at bottom amorphous, disordered, contradictory, inconsistent, non-rational, and non-objective. Science and much of western philosophy have in the past presented us with the illusion that things are otherwise. Rational views of the universe are idealized models which only approximate reality. The approximations are useful. The models are successful often enough in predicting the behavior of things that they provide a useful foundation for science and technology. But they are ultimately only approximations of reality, and non-unique at that."

This is Kent's hypothesis by example rather than proof: information in its "real" essence is too amorphous, ambiguous, subjective, slippery, and elusive to be pinned down by the deterministic processes embodied in a computer.

### The contradiction we live with

Kent holds both that:

- (a) reality is not singular or objective at the bottom, and
- (b) for narrow purposes and within small communities, shared views are high enough that reality *appears* stable and objective.

This is not a contradiction to be resolved but a duality to be operated within. The reconciliation rate is a function of scope and purpose (see [[Concepts/reconciliation-by-scope-and-purpose]]).

### Why this matters for modelling

If the underlying territory is amorphous, the work of modelling cannot be to discover the right structure. It can only be to:

- choose a representation that supports the narrow purpose at hand,
- be explicit about which phenomena it captures and which it flattens or omits,
- recognise that "learning" a data model is largely a *conditioning* of perception, not a discovery of truth.

### Senses as a worked example

Kent uses sensory biology to make the case vivid. Our notion of opaque objects, sharp boundaries, day/night, distinct things vs. flux, depends on which frequencies our eyes detect. A creature sensing the world through smell, electrical fields, or infrared would have a categorically different "real" world — and would model it categorically differently.

## Key Insights

1. **The three-worlds framing implies no data model can ever be the territory** — at best it is a map of a map of a map.
2. **Reality being amorphous is a hypothesis, not an axiom** — Kent offers it by accumulated example, and explicitly disclaims proof.
3. **Useful approximation ≠ faithfulness.** Science succeeds because its rational models "approximate" reality "often enough"; this is a practical sufficiency, not an ontological claim.
4. **Brain-style determines "natural" model.** People who think visually, verbally, or in networks will find different models natural — and the field's tribal allegiances may reflect cognitive style more than objective merit.
5. **"Identity" is unsettled even for humans.** Kent cites Lewis Thomas (the human as symbiotic colony), sociobiology (the gene as the unit of selection), and primate language research to show that "person" is not obviously a well-defined category — undermining the assumption that even basic categories are well-founded.

## Related Concepts

- [[Concepts/map-vs-territory-data-modeling]] — the analogy that grounds the three-worlds claim
- [[Concepts/data-model-as-tool-not-theory]] — what follows if reality is amorphous
- [[Concepts/reconciliation-by-scope-and-purpose]] — the practical mode of operating in an amorphous reality
- [[Concepts/linguistic-relativity-of-modeling]] — the language layer's role

## Related Entities

- [[Entities/william-kent]]
- [[Entities/data-and-reality]]

## References

- Raw Article: [[Raw/bkent-data-reality-excerpts-2026-09-13]]
- Original: https://bkent.net/Doc/darxrp.htm#Chapter12