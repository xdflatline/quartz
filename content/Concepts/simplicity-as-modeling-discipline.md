---
title: "Simplicity as a Modeling Discipline (MMA Belief 6)"
details: "Sixth core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: simplicity is a discipline, not a side effect. Complexity is the default state of entropy; a good model actively fights entropy to deliver clarity. Simplicity is not achieved by removing necessary detail, but by organizing detail so that the complex becomes intuitive. Reis's framing resists the common misinterpretation that simplicity means \"fewer fields\" or \"fewer tables.\""
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

# Simplicity as a Modeling Discipline (MMA Belief 6)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 6
**Category:** Architecture Pattern (design principle)
**Status:** Proposed best practice

---

## Overview

Reis's sixth MMA belief reframes **simplicity as a discipline**, not an outcome. The strong claim is that complexity is the default state of entropy — every additional field, join, edge case, and downstream consumer pushes the model toward disorder. A good model *actively* fights this entropy to deliver clarity. Crucially, Reis distinguishes simplification from removal: simplification is not "fewer fields" or "fewer tables" but the **organization of necessary detail so the complex becomes intuitive**.

This is a more demanding position than the usual "keep it simple" advice. It treats simplicity as something that has to be continually maintained, not a property achieved once at design time.

## Core Content

### Reis's specific framing

> "Complexity is the default state of entropy; a good model fights entropy to deliver clarity. We do not simplify by removing necessary detail, but by organizing it so that the complex becomes intuitive."

This separates two failure modes that are often confused:

| Failure mode | Symptom | Reis's response |
|--------------|---------|-----------------|
| Over-simplification | Detail removed; model can't answer necessary questions | Wrong kind of simple |
| Disorderly complexity | All detail present but unorganized; model is hard to learn | The default entropy state |
| Disciplined simplicity | All necessary detail present; structure makes it learnable | The MMA target |

### What "disciplined simplicity" looks like in practice

- **Naming is deliberate.** Fields, tables, and relationships are named for the business concept they represent, not for the source system or pipeline that produced them.
- **Grain is explicit.** Every entity has a declared grain; downstream readers do not have to reverse-engineer it (see [[Concepts/intent-driven-data-modeling]]).
- **Time is explicit.** Temporal axes are modeled, not left implicit (see [[Concepts/time-as-first-class-modeling-axis]]).
- **Semantics is explicit.** Meaning is captured separately from schema (see [[Concepts/semantics-as-universal-interface]]).
- **Boundaries are clear.** Bounded contexts, namespaces, ownership, and lifecycle are visible in the model.

Each of these is an act of organization — fighting entropy — not removal.

### Why simplicity is a discipline (not a design-time choice)

Reis uses the word "discipline" deliberately: simplicity is maintained, not achieved. Every new field added, every new consumer onboarded, every schema change is an opportunity for entropy to grow. Disciplined simplicity means continuous refactoring and naming hygiene, not a one-time simplification effort.

## Key Insights

1. **Complexity is the default.** Without active effort, models grow disorderly. The instinct to blame complexity on "the business" mistakes entropy for design.
2. **Simplicity is not removal.** Removing necessary detail makes the model wrong; organizing it makes it learnable.
3. **Discipline means maintenance.** Simplicity is a property of the model's lifecycle, not of its creation event (see [[Concepts/modeling-as-continuous-lifecycle]]).
4. **Intuitiveness is the success criterion.** A model is simple when a new analyst or agent can learn it without tribal knowledge.

## Related Concepts

- [[Concepts/model-territory-not-technology]] — disciplined simplicity is a property of the territory-level model, not the engine-rendered schema
- [[Concepts/intent-driven-data-modeling]] — declared intent is itself a simplification device
- [[Concepts/modeling-as-continuous-lifecycle]] — the temporal frame in which discipline is exercised
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
