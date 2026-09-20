---
title: "Modeling as a Continuous Lifecycle (MMA Belief 8)"
details: "Eighth core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: no model is \"finished.\" Modeling is not a phase that ends at deployment; it is a continuous practice of iterating, refactoring, and evolving the model alongside the business. The model is treated as living infrastructure that must be kept aligned with reality — analogous to how code is maintained, not delivered."
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

# Modeling as a Continuous Lifecycle (MMA Belief 8)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 8
**Category:** Architecture Pattern (process / lifecycle)
**Status:** Proposed best practice

---

## Overview

Reis's eighth MMA belief reframes modeling from a project phase to a **continuous lifecycle**. No model is "finished" — models iterate, refactor, and evolve alongside the business they represent. The implication is operational: modeling is ongoing work, on par with code maintenance, not a deliverable produced once and handed off.

This is the operational companion to Reis's territorial claim ([[Concepts/model-territory-not-technology]]). If reality changes (and reality always changes), and if the model must reflect reality (it must), then the model must change too — and the organization must be structured to make that change cheap and continuous.

## Core Content

### Reis's specific framing

> "No model is 'finished.' We iterate, refactor, and evolve in real-time alongside the business. Modeling is not a phase; it is a continuous practice of aligning systems with reality."

The framing inverts the waterfall intuition:

| Waterfall assumption | MMA position |
|----------------------|--------------|
| Model is delivered once | Model is continuously evolved |
| Change is an exception | Change is the default |
| Refactoring is overhead | Refactoring is the work |
| Modeler hands off to engineering | Modeler stays engaged across the model lifecycle |
| "Done" is a project state | "Done" is a momentary snapshot |

### What lifecycle modeling looks like in practice

- **Versioned schemas** with explicit migration and deprecation paths
- **Semantic versioning of the model** (major / minor / patch) tied to consumer-visible changes
- **Continuous review** — regular modeling sessions where the model is examined against current reality
- **Refactoring budget** — time allocated for non-functional improvements, not only new features
- **Ownership that persists** — modelers are not reassigned after delivery; they stay engaged with the models they own
- **Feedback loops** from consumers (analysts, applications, agents) back to modelers, treated as first-class inputs

### Why "lifecycle" is a stronger claim than "iteration"

Iteration implies discrete cycles (sprint, quarter, year). Lifecycle implies that modeling has no terminal state. The distinction matters because:

- **Sponsorship.** A lifecycle practice needs permanent sponsorship and budget, not project funding.
- **Tooling.** Lifecycle requires tooling for migration, deprecation, semantic versioning, lineage, and impact analysis — not just schema design.
- **Skills.** Lifecycle modeling requires skills in refactoring, deprecation, and negotiation that are different from greenfield design.
- **Metrics.** Lifecycle is measured by health (drift, age, coverage) over time, not by delivery dates.

### Connection to other MMA beliefs

- [[Concepts/simplicity-as-modeling-discipline]] — discipline is the verb that maintains simplicity over time
- [[Concepts/intent-driven-data-modeling]] — declared intent survives refactors when it is explicit
- [[Concepts/semantics-as-universal-interface]] — semantics is durable across schema changes, making lifecycle refactoring safer
- [[Concepts/agentic-ready-data-modeling]] — agents need the model to remain accurate as it evolves; versioning is part of the API

## Key Insights

1. **Models are never done.** The "delivered" state is a momentary snapshot, not a terminal state.
2. **Modeling is a verb, not a noun.** The work is the practice, not the artifact.
3. **Refactoring is the job.** Continuous refactoring against reality is the central maintenance activity.
4. **Lifecycle modeling needs permanent ownership.** Project-based model ownership produces stale models.
5. **Tooling matters.** Lifecycle requires migration tools, semantic versioning, lineage, and impact analysis — not just an ER diagram editor.

## Related Concepts

- [[Concepts/simplicity-as-modeling-discipline]] — the daily practice that keeps a model simple
- [[Concepts/model-territory-not-technology]] — the territory changes; the model must follow
- [[Concepts/intent-driven-data-modeling]] — declared intent survives refactors
- [[Concepts/semantics-as-universal-interface]] — semantics is the durable substrate
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
