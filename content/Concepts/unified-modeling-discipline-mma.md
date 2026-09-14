---
title: "Unified Modeling Discipline (MMA Belief 1)"
details: "First core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: data modeling is a single continuous discipline, not two (application vs. analytics, OLTP vs. OLAP). The same fundamentals — entities, relationships, identity, grain, time, semantics — apply across contexts; the differences are implementation details, not different physics. Direct rebuttal of Kimball vs. Inmon, normalized vs. denormalized, and app-vs-warehouse silos."
tags:
  - knowledge-management
  - architecture-pattern
created: 2026-09-14
updated: 2026-09-14
type: concept
sources:
  - "[[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]"
---

# Unified Modeling Discipline (MMA Belief 1)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 1
**Category:** Architecture Pattern (organizational / methodological)
**Status:** Proposed best practice

---

## Overview

The first of Reis's nine MMA core beliefs states that data modeling is **one discipline**, not two (or many). The artificial wall between application development and analytics, OLTP and OLAP, code and warehouse, is treated as a liability rather than a useful specialization. Different contexts share the same underlying physics — entities, relationships, identity, grain, time, semantics — and the implementation differences (tables vs. streams vs. graphs) are downstream choices.

The position is a direct rejection of the most durable methodological tribalisms in data: Kimball vs. Inmon (dimensional vs. corporate information factory), normalized vs. denormalized (3NF vs. star schema), and the hand-off culture where "developers throw data over the wall to analysts and data scientists."

## Core Content

### What Reis claims is unified

| Dimension | Traditional split | MMA position |
|-----------|-------------------|--------------|
| Organizational | Application dev vs. analytics | One practice, multiple contexts |
| Workload | OLTP vs. OLAP | One physics; different access patterns |
| Storage | Code model vs. warehouse model | Model the reality; technology follows |
| Methodology | Kimball, Inmon, ODF, Data Vault, etc. | First principles + pragmatic selection |

### The fundamentals Reis lists as universal

- **Entities** — discrete things in the domain
- **Relationships** — connections between entities
- **Identity** — stable keys across time and context
- **Grain** — what one row / record represents
- **Time** — every fact's temporal context (see [[Concepts/time-as-first-class-modeling-axis]])
- **Semantics** — meaning shared across humans and machines (see [[Concepts/semantics-as-universal-interface]])

### Why Reis frames this as a "house divided" problem

> "Developers throw data over the wall to analysts and data scientists. Established modeling practices are dust in the wind, forgotten to the void of time. Convenience outlasts expertise. The same ideas are reinvented in isolation, often for no good reason."
> — Reis, Manifesto

The diagnosis is sociological: split communities re-invent each other's solutions and create a hand-off tax. The prescription is institutional — practitioners trained across both sides, fluent in the shared fundamentals.

## Key Insights

1. **Silos are liabilities, not specializations.** A practitioner who only models OLTP or only models warehouses is missing half the discipline.
2. **The fundamentals don't change with context.** Entities, relationships, identity, grain, time, and semantics are the load-bearing primitives everywhere.
3. **Methodology wars are downstream.** Kimball, Inmon, Data Vault, ODF are all valid *tools* — evaluated by problem fit, not by tribal allegiance (see [[Concepts/pragmatic-anti-dogma-modeling]]).
4. **Unification is necessary for AI-agent modeling.** When the same data must serve both human analysts and agentic reasoning, single-discipline fluency is non-negotiable.

## Related Concepts

- [[Concepts/model-territory-not-technology]] — the implementation-independence corollary
- [[Concepts/pragmatic-anti-dogma-modeling]] — the methodology-war conclusion
- [[Concepts/unified-modeling-discipline-mma]] — self
- [[Entities/mixed-model-arts-manifesto]] — source document

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
