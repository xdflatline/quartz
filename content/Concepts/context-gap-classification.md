---
title: "Context gap classification"
details: "A taxonomy of gap types produced by Step 4 of the ontology + LLM agentic loop: identity-resolution gaps, entity-grain gaps, and semantic-collision gaps. Each type has a different owner, a different cost profile, and a different action template."
tags:
  - knowledge-management
  - llm
  - architecture-pattern
created: 2026-08-07
updated: 2026-08-07
type: concept
sources:
  - "[[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]]"
---

# Context gap classification

**Source:** [Thoughtworks blog post (2026-07-22)](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) ([[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]])
**Category:** Architecture Pattern
**Status:** Proposed best practice (illustrative taxonomy from a single industry blog)

---

## Overview

When the ontology + LLM agentic loop surfaces use-case-agnostic gaps in Step 2, those gaps are usually heterogeneous: they look like the same kind of artifact (a mismatch between two ontologies) but resolve into genuinely different problems with different owners, costs, and dependencies. Step 4 of the loop reinterprets each agnostic gap against a specific use case and classifies it; Step 5 then turns the classification into an action. Classifying the gap up front replaces a quarter of reactive rework with a plan.

## Core Content

### The taxonomy (from the churn-forecasting example)

The article classifies the three gaps the example surfaces:

| # | Gap (agnostic) | Type | What it means for the churn use case | Action template |
|---|----------------|------|----------------------------------------|------------------|
| 1 | `EmailAddress` is shared across both billing and support ontologies | **Identity-resolution** | Email is the join key that stitches billing and support histories to one customer. It is the reconciliation the model depends on. | Define the shared attribute as the resolved identity key and curate the join. Internal reconciliation, fast. |
| 2 | `Account` (billing) and `Customer` (support) may be the same real-world entity | **Entity-grain** | Whether they are the same business entity determines both the target of prediction and the underlying data model. | SME decision on the customer grain, then a modeling change to the curated entity. Low engineering cost, but it needs human judgment before code. |
| 3 | `BillingStatus` and `TicketStatus` share the type `Status` | **Semantic-collision** | A shared type does not mean shared meaning. `Status = closed` is a healthy outcome for a ticket and a churn signal for billing. Collapsing them would corrupt the label. | Disambiguate the shared type into distinct, context-qualified concepts. |

### What makes classification useful

The three gap types differ on the dimensions that determine plan quality:

- **Owner** — identity-resolution is internal; entity-grain needs an SME; semantic-collision may need both business and modeling owners.
- **Cost** — reconciliation is cheap; a grain decision can trigger downstream model changes; disambiguation is bounded but may touch labels in production.
- **Dependency order** — the join (Gap 1) is a prerequisite for any churn model; the grain decision (Gap 2) is a prerequisite for the entity the join produces; the label disambiguation (Gap 3) is a prerequisite for the label the model trains on.

Classifying the gap maps directly to a *plan* with a sequence, an owner per step, and an estimate — not just a punch list of "mismatches to fix."

### When the loop re-runs

After Step 5 mutates the curated context (resolving the email key, unifying Account/Customer, disambiguating Status), Step 6 re-runs the diff. The churn gaps are now closed. If a source changed or a new gap surfaced, the loop continues from the new state. The classification is therefore a per-cycle artifact, not a one-time deliverable.

## Key Insights

1. **A gap's classification, not its existence, drives the plan.** Surfacing a mismatch is the easy part; deciding what kind of mismatch it is — and therefore who owns the fix and what the fix costs — is the leverage.
2. **Three gap types recur in the example** (identity-resolution, entity-grain, semantic-collision). They are not exhaustive, but they are a useful starter taxonomy when bootstrapping a similar loop on a new data landscape.
3. **Semantic collision is the silent killer.** A shared type with opposite implications corrupts any model that uses the label naively. The "fix" is not to merge the values; it is to disambiguate the *concepts* so the labels stay distinct.
4. **Identity-resolution is the cheap win.** It usually unblocks the model and unlocks the other gaps; it should be sequenced first.

## Related Concepts

- [[Concepts/ontology-llm-data-modernization]] — the six-step loop this taxonomy lives inside

## References

- Raw Article: [[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]]
- Original: [https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization)
- Author: Zichuan Xiong, Thoughtworks (2026-07-22)
