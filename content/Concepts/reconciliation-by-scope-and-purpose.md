---
title: "Reconciliation by Scope and Purpose"
details: "William Kent's claim that the degree to which people can share a common view of reality is a function of two variables — scope (the number of people whose views must be reconciled) and purpose (the breadth of the question). Narrow purpose and few people reconcile easily; broad purpose and many people expose the underlying disagreements. This is why information systems fail as scope and purpose grow."
tags:
  - knowledge-management
  - architecture-pattern
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "[[Raw/bkent-data-reality-excerpts-2026-09-13]]"
---

# Reconciliation by Scope and Purpose

**Source:** William Kent, *Data and Reality* (1978/1998), Chapter 12: "A View of Reality" ([[Raw/bkent-data-reality-excerpts-2026-09-13]])
**Category:** Architecture Constraint (socio-technical)
**Status:** Fundamental

---

## Overview

Kent observes that no two people share a view of reality that is identical in every detail — at most, views overlap. The probability of **reconciling** views to a workable degree is a function of two variables:

- **Scope** — the number of people whose views have to be reconciled.
- **Purpose** — the breadth of the question for which reconciliation is needed.

For narrow purposes among few people, reconciliation is near-total and reality *appears* objective. For broad purposes across many people, reconciliation degrades and discrepancies in fundamental assumptions become exposed.

This is not a bug. It is an inevitable outcome of natural selection that small communities of survivors share basic assumptions; it is also the reason that technology, which fosters interaction among greater numbers of people and integrates processes into monoliths serving wider purposes, increasingly exposes conceptual disagreements that were previously invisible.

## Core Content

### The two variables

| Variable | Definition | Effect on reconciliation |
|----------|------------|--------------------------|
| **Scope** | The number of people whose views must be reconciled | More people → lower reconciliation |
| **Purpose** | The breadth of the question being served | Broader purpose → lower reconciliation |

### Working examples Kent gives

- **Absolute truth and beauty:** reconciliation nil.
- **Survival, buying food, asking a policeman for help:** reconciliation is high (we don't need to share metaphysical views to transact).
- **Inventory records for a single warehouse:** reconciliation is high enough to make the system workable for management decision-makers.
- **Personnel, production, planning, sales, customer data for a multi-national:** reconciliation is lower — broader purpose, more stakeholders, more disagreement about what "employee" or "customer" actually means.

### Implications for information systems

The same data model rarely survives an increase in scope and purpose. The warehouse model works for one warehouse; the multi-national model breaks across divisions precisely because the implicit assumptions about "what we mean by an employee" no longer hold.

This is the practical face of the **map-vs-territory** problem (see [[Concepts/map-vs-territory-data-modeling]]): as scope and purpose grow, the discrepancies between maps become operationally significant.

### Modifying viewpoints

> "If an involved party holds multiple viewpoints, he may agree to use a particular one to serve the purpose at hand. Or he may be persuaded to modify his view, to serve that purpose."

Reconciliation need not be the discovery of a single shared view. It is sufficient that, *for the purpose at hand*, the parties have negligible differences in the relevant portion of their world view. One party may set aside an alternative viewpoint; another may revise their view; both moves are legitimate.

## Key Insights

1. **Reconciliation is a function of two variables, not a property of "truth".** Data models succeed when scope and purpose are bounded; they break when either grows.
2. **Reality appearing objective is itself a consequence of narrow scope and purpose.** This is not metaphysical but practical — a feature of small communities and narrow questions.
3. **Technology increases both scope and purpose** — and therefore exposes latent conceptual disagreements. This is why "the question is becoming more relevant today" (Kent, 1978).
4. **Viewpoint modification is a legitimate reconciliation mechanism** — setting aside alternative viewpoints, or revising one's own, can substitute for discovering a single shared view.
5. **Systems designs should declare their scope and purpose.** When they don't, the implicit narrowness gets exposed when scope or purpose inevitably grows.

## Related Concepts

- [[Concepts/map-vs-territory-data-modeling]] — why reconciliation is necessary in the first place
- [[Concepts/three-worlds-ontology-amorphous]] — the ontological reason reconciliation is partial
- [[Concepts/data-model-as-tool-not-theory]] — tools have economic, not theoretical, justification
- [[Concepts/linguistic-relativity-of-modeling]] — one source of latent disagreement

## Related Entities

- [[Entities/william-kent]]
- [[Entities/data-and-reality]]

## References

- Raw Article: [[Raw/bkent-data-reality-excerpts-2026-09-13]]
- Original: https://bkent.net/Doc/darxrp.htm#A%20View%20of%20Reality