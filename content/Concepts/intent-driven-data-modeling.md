---
title: "Intent-Driven Data Modeling (MMA Belief 3)"
details: "Third core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: data models must explicitly encode the model's purpose, distinguishing Operational Intent (how the business acts — write paths, transactions, workflows) from Analytical Intent (how the business learns — read paths, aggregates, ML features). A model without declared intent is technical debt in waiting; intent dictates grain, freshness, identity, and acceptable trade-offs."
tags:
  - knowledge-management
  - architecture-pattern
created: 2026-09-14
updated: 2026-09-14
type: concept
sources:
  - "[[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]"
---

# Intent-Driven Data Modeling (MMA Belief 3)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 3
**Category:** Architecture Pattern (modeling principle)
**Status:** Proposed best practice

---

## Overview

Reis's third MMA belief states that **data is not static — it has a job to do**. Every model must explicitly encode its purpose, and Reis separates purpose into two kinds: **Operational Intent** (how the business acts on the data — recording, updating, transacting, triggering workflows) and **Analytical Intent** (how the business learns from the data — querying, aggregating, training models, producing insights). A model without declared intent is technical debt in waiting, because the trade-offs that need to be made (grain, freshness, denormalization, identity strategy) cannot be made coherently without knowing what the model is for.

The principle is a synthesis of long-standing practice — Kimball's grain-first methodology, Inmon's atomic-data-then-derive hierarchy, Data Vault's hub/link/satellite separation — reframed as a first-principles statement: name the intent, then let the structure follow.

## Core Content

### The two intents

| Dimension | Operational Intent | Analytical Intent |
|-----------|---------------------|---------------------|
| **Primary action** | Write, update, transact, trigger | Read, aggregate, analyze, learn |
| **Optimization target** | Throughput, consistency, latency to act | Query cost, freshness, feature availability |
| **Identity strategy** | Stable natural keys, referential integrity | Often surrogate keys, conformed dimensions |
| **Grain preference** | One row per business event | Many rows per event at multiple grains |
| **Time handling** | Point-in-time state, current truth | Slowly changing dimensions, event time, snapshots |
| **Typical user** | Application, workflow, service | Analyst, data scientist, agent |

### What "explicit intent" changes

- **Grain decisions become principled.** Without declared intent, grain is implicit and often accidental. With declared intent, grain is a design decision.
- **Identity choices become justifiable.** Surrogate vs. natural keys is no longer a stylistic preference — it follows from whether the model is recording transactions or aggregating history.
- **Time semantics get specified.** Operational intent implies current-state semantics; analytical intent requires event time and slow-change handling (see [[Concepts/time-as-first-class-modeling-axis]]).
- **Denormalization becomes intentional.** Denormalization is no longer "wrong" or "right" — it is justified or not by the declared intent.

### Why Reis calls intentless models "technical debt in waiting"

A model built without intent looks fine at creation. As soon as it needs to support a second use case (a real-time dashboard, an ML feature pipeline, an agent that needs to reason over history), the implicit choices made for use case #1 block use case #2. Retrofitting intent is more expensive than declaring it upfront.

## Key Insights

1. **Every model has an intent; few models declare it.** Declaring intent is the first modeling act.
2. **Operational and analytical intents drive opposite trade-offs.** Treating them as one design question produces broken models for both.
3. **Intent dictates grain, identity, time, and denormalization.** All four are downstream of the declared purpose.
4. **A third "agentic intent" is implicit in MMA Belief 7.** The Agentic Era adds a third axis: how AI agents will consume the model (see [[Concepts/agentic-ready-data-modeling]]).

## Related Concepts

- [[Concepts/unified-modeling-discipline-mma]] — operational and analytical are unified by fundamentals, distinct in intent
- [[Concepts/model-territory-not-technology]] — intent is part of the territory
- [[Concepts/time-as-first-class-modeling-axis]] — temporal handling follows from intent
- [[Concepts/agentic-ready-data-modeling]] — the emerging third intent
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
