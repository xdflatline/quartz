---
title: "Ontology + LLM agentic loop for data modernization"
details: "A six-step agentic workflow for enterprise data modernization that pairs per-source ontologies with LLM-driven semantic analysis. The loop builds a reconciled, version-controlled semantic baseline and continuously classifies context gaps against new use cases."
tags:
  - llm
  - agent
  - knowledge-management
  - architecture-pattern
created: 2026-08-07
updated: 2026-08-07
type: concept
sources:
  - "[[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]]"
---

# Ontology + LLM agentic loop for data modernization

**Source:** [Thoughtworks blog post (2026-07-22)](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) ([[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]])
**Category:** Architecture Pattern
**Status:** Proposed best practice (industry blog, illustrative example, not yet a published standard)

---

## Overview

The ontology + LLM agentic loop is a six-step workflow for closing the "context gap" in enterprise data modernization programs. The premise is that modernization stalls not at delivery but at *discovery*: the months spent trying to understand what scattered, tacit enterprise data actually means. The pattern pairs a human-readable **ontology** (schema of meaning) with an **LLM agent** that reads, reconciles, and reasons over source systems. The output is a living, version-controlled semantic asset that subsequent use cases and agents reuse rather than rediscover.

## Core Content

### Why neither works alone

- **Ontology without AI**: explicit, auditable, verifiable — but months of manual analysis per source.
- **LLM without ontology**: fast and reads source systems naturally — but inferences are ungrounded and hard to verify at enterprise scale.
- **Combined**: ontology supplies the structure that makes the LLM's outputs explainable and consistent; the LLM supplies the scale that makes ontology construction tractable.

### The six-step agentic loop

| # | Step | What happens | Key artifact |
|---|------|--------------|--------------|
| 1 | Build ontological context per source | An agent reads schema, data types, foreign keys, sample values, and documentation. It infers a candidate ontology and flags low-confidence guesses for SME confirmation. | Per-source ontology (machine-readable, auditable) |
| 2 | Curate context across sources, then reconcile | Ontologies from multiple sources are merged; use-case-agnostic gaps (duplicate entities, conflicting definitions, overlapping concepts) are surfaced. | Reconciled, curated ontology |
| 3 | Compare design context against curated context | The use case's own intent is expressed as a design ontology and matched against the curated context. | Design ontology + diff |
| 4 | Identify the gaps | Each previously agnostic gap is reinterpreted for the use case: identity-resolution, semantic-collision, grain, etc. | Classified gap list |
| 5 | Take actions | Different gap types resolve into different plans (reconciliation rule, SME grain decision, semantic disambiguation) with different costs, owners, and dependency orders. | Action plan |
| 6 | Update source context and loop | The reconciled context is mutated by the actions and becomes the new baseline. The next use case and next agent inherit it rather than rediscover it. | New baseline ontology |

### Walkthrough: customer churn

The article's worked example uses two source systems (billing, support) and a churn-forecasting use case. The three use-case-agnostic gaps surface in Step 2:

1. `EmailAddress` is shared across both ontologies.
2. `Account` (billing) and `Customer` (support) may be the same real-world entity.
3. `BillingStatus` and `TicketStatus` both have type `Status`.

Reinterpreted for the churn use case in Step 4, the three gaps become:

| Gap | Type | What it means for churn | Action (Step 5) |
|-----|------|--------------------------|-----------------|
| EmailAddress shared | Identity-resolution | Email is the join key stitching billing and support histories to one customer | Define email as the resolved identity key and curate the join |
| Account vs. Customer | Entity-grain | Whether they are the same business entity determines both prediction target and data model | SME grain decision → modeling change to the curated Customer |
| BillingStatus vs. TicketStatus | Semantic-collision | `Status = closed` is healthy for a ticket but a churn signal for billing | Disambiguate the shared type into context-qualified concepts |

### Operating model: context as a service

The loop's defining property is that **context is a service at the landscape level**, not a document or a one-time snapshot. Each completed use case mutates the curated context, which becomes the new baseline for the next. Source systems change, definitions drift, and the actions from Step 5 themselves alter the landscape — so the loop is continuous by construction, not by accident.

### Human-in-the-loop boundaries

- The LLM identifies and classifies potential gaps.
- Business owners and domain experts validate entity definitions, resolve semantic conflicts, and approve changes that affect enterprise-wide data models.
- Governance does not get automated away; only the mechanical analysis does.

## Key Insights

1. **The "context gap" is the bottleneck**, not delivery. Most data-modernization programs lose months and credibility in discovery, not in building. Pairing ontology with an LLM targets exactly that middle.
2. **An ontology is a graph schema, not a slide deck.** Its value comes from being machine-readable, auditable, and version-controlled — the same properties you want from any infrastructure artifact.
3. **Use-case-agnostic gaps exist regardless of any specific use case.** Surfacing them once, in the reconciled baseline, pays off across every subsequent use case.
4. **Gaps have types** (identity-resolution, entity-grain, semantic-collision). Different types need different owners, different cost profiles, and different dependency orders; classifying them up front replaces a quarter of rework with a plan.
5. **The loop is the artifact.** A single run finds gaps; a loop converts the reconciled context into a reusable asset and amortizes the cost of building it.

## Related Concepts

- [[Concepts/context-gap-classification]] — the taxonomy of gap types the loop produces in Step 4
- [[Entities/thoughtworks]] — the company publishing the pattern
- [[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]] — full source article

## References

- Raw Article: [[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]]
- Original: [https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization)
- Author: Zichuan Xiong, Thoughtworks (2026-07-22)
