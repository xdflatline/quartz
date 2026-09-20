---
title: "Time as a First-Class Modeling Axis (MMA Belief 4)"
details: "Fourth core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: time is non-negotiable in data modeling. State is treated as an illusion; change is the reality. If a model cannot answer \"when\" and \"in what order\" for a fact, it cannot answer \"why.\" Time must be modeled explicitly — through event time, valid time, slowly changing dimensions, bitemporal tables, or equivalent constructs — rather than left implicit in a current-state snapshot."
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

# Time as a First-Class Modeling Axis (MMA Belief 4)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 4
**Category:** Architecture Pattern (modeling primitive)
**Status:** Fundamental (re-articulated for MMA)

---

## Overview

Reis's fourth MMA belief makes **time a non-negotiable, first-class axis** of every data model. The claim is stronger than the familiar "use slowly changing dimensions" advice: state is treated as an illusion, change is the reality, and a model that cannot answer "when" and "in what order" for any fact it stores cannot answer "why" — because causality requires temporal order.

The principle has direct analogues in database theory (bitemporal modeling, valid time vs. transaction time, event sourcing) but Reis frames it for a mixed-discipline audience that has historically separated "current state" (OLTP) from "history" (analytical warehouse) — and therefore routinely loses or distorts time in one of the two.

## Core Content

### Reis's strong claim

> "Everything is temporal. State is an illusion; change is the reality. Ignoring time creates chaos; modeling time creates coherence. If you cannot answer 'when' and 'in what order,' you cannot understand 'why.'"

This is not just a recommendation to add a `created_at` column. It is a statement that **every fact needs explicit temporal metadata**, and that the answers to "why did X happen?" presuppose the answers to "when did X happen, and what came before?"

### Time dimensions the model must distinguish

| Time dimension | What it answers | Typical implementation |
|----------------|-----------------|------------------------|
| **Event time** | When did the fact occur in the real world? | `event_timestamp` recorded by source |
| **Valid time** | When was the fact true in the real world? | Bitemporal valid_from / valid_to |
| **Transaction time** | When did the system learn the fact? | `recorded_at`, audit columns |
| **Processing time** | When did the pipeline handle the fact? | Watermarks, pipeline timestamps |

A model that conflates these (e.g., storing event time as a transaction-time column) silently destroys the answer to "why."

### What modeling time correctly enables

- **Causality.** "Why did churn spike in Q3?" requires knowing which events preceded which.
- **Reconstruction.** Point-in-time reconstruction of any entity's state at any moment.
- **Correction.** Retroactive corrections without overwriting history.
- **Auditability.** Who knew what, when.
- **Agent reasoning.** AI agents that need to reason over history, not just current state (see [[Concepts/agentic-ready-data-modeling]]).

### What ignoring time breaks

- **Hindsight.** "What did we know on 2025-03-15?" is unanswerable.
- **Reproducibility.** ML training data with implicit time leaks the future into the past.
- **Reconciliation.** Two systems disagree because they recorded different times.
- **Causality.** Without ordering, correlation and causation are indistinguishable.

## Key Insights

1. **State is a derived view, not a primitive.** Current state is the most recent event; it is not the underlying reality.
2. **Conflating event time, valid time, and transaction time is the most common silent data-modeling bug.** The model "works" until someone asks a temporal question.
3. **AI agents need history, not just state.** Without temporal modeling, an agent can only reason about the current snapshot.
4. **Modeling time is not optional.** Reis's word — "non-negotiable" — is deliberate.

## Related Concepts

- [[Concepts/intent-driven-data-modeling]] — operational vs. analytical intent drives which time dimensions matter most
- [[Concepts/agentic-ready-data-modeling]] — temporal modeling is a prerequisite for agent reasoning
- [[Concepts/semantics-as-universal-interface]] — semantics and time are the two durable axes
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
