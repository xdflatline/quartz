---
title: "Research Index: Ontology + LLM for data modernization"
details: "Synthesis of a single Thoughtworks blog post (Zichuan Xiong, 2026-07-22) introducing a six-step agentic loop that combines per-source ontologies with LLM-driven semantic analysis to close the context gap in enterprise data modernization. Anchors the ontology-llm-data-modernization and context-gap-classification concepts."
tags:
  - llm
  - agent
  - knowledge-management
  - index
created: 2026-08-07
updated: 2026-08-07
type: research
sources:
  - "[[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]]"
---

# Research Index: Ontology + LLM for data modernization

**Updated:** 2026-08-07
**Source:** [Thoughtworks Insights blog — Closing the context gap: An ontology + LLM approach to data modernization](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) (2026-07-22, Zichuan Xiong)

---

## Overview

This index synthesizes a single-source research thread on using LLMs together with ontologies to accelerate enterprise data modernization. The original framing is that the bottleneck is not delivery but *discovery*: the months spent trying to understand what scattered, tacit enterprise data actually means. The proposed remedy is a six-step agentic loop that pairs a human-readable ontology with an LLM agent and a human-in-the-loop governance boundary. The pattern is illustrated with a customer-churn use case over two source systems (billing, support) and surfaces a small but useful taxonomy of gap types (identity-resolution, entity-grain, semantic-collision).

## Concepts

### Agent Architecture
- [[Concepts/ontology-llm-data-modernization]] — the six-step agentic loop and the "context as a service" operating model.
- [[Concepts/context-gap-classification]] — the gap-type taxonomy produced in Step 4: identity-resolution, entity-grain, semantic-collision.

### Knowledge Management
- Ontology as a graph schema (schema layer of a knowledge graph) — implicit in both concept pages, surfaced as a recurring framing in the source.
- Per-source ontologies reconciled into a curated baseline — the "context as a service" loop's central abstraction.

## Tools & Projects

### Companies & Publications
- [[Entities/thoughtworks]] — the consultancy publishing the source article; relevant for its broader legacy-modernization, data-strategy, and AI-in-the-enterprise body of work.

## Raw Sources

- [[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]] — verbatim Zichuan Xiong (2026-07-22) blog post on the ontology + LLM agentic loop, including the full six-step walkthrough and the churn-forecasting worked example.

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [Thoughtworks Insights — Xiong](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) | Ontology + LLM for data modernization | 2026-07-22 | Six-step agentic loop, ontology as graph schema, "context as a service," gap classification taxonomy, churn-forecasting worked example |

## Cross-Cutting Themes

### Data Strategy
1. **Discovery is the bottleneck, not delivery.** Most modernization programs lose months in understanding what data means, not in building. The ontology + LLM loop targets that middle.
2. **Context must be a service, not a document.** A reconciled, version-controlled semantic asset that every future project and AI agent can reuse is more durable than design docs that drift.
3. **Use-case-agnostic gaps exist regardless of any specific use case.** Surfacing them once, in the reconciled baseline, pays off across every subsequent use case.

### Agent Architecture
1. **Ontology grounds LLM reasoning; LLM scales ontology construction.** Each covers the other's weakness: ontology without AI is months of manual analysis; LLM without ontology is fast but untrustworthy.
2. **Gaps have types, not just locations.** Identity-resolution, entity-grain, and semantic-collision are different problems with different owners, costs, and dependency orders; classifying them up front is the leverage.
3. **The loop is the artifact.** A single run finds gaps; a loop amortizes the cost of building the reconciled context across every subsequent use case.

### Governance
1. **The agent identifies and classifies gaps; humans own definitions, conflicts, and changes.** AI augments mechanical analysis; governance boundaries do not get automated away.

## Next Research Directions

- [ ] Evaluate whether the six-step loop generalizes beyond data modernization — e.g., to API contract reconciliation, feature-store curation, or cross-team data product discovery.
- [ ] Prototype the gap-classification taxonomy (identity-resolution, entity-grain, semantic-collision) on a different domain to test whether the three types are exhaustive or domain-specific.
- [ ] Compare the "context as a service" framing with knowledge-graph / data-mesh / data-product operational models — where do they overlap, and where do they diverge on ownership and lifecycle?
- [ ] Investigate tooling that operationalizes the loop: schema-mining agents, ontology diff/version-control, and SME-in-the-loop confirmation surfaces.

## References

- Source article: [Thoughtworks Insights](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) ([[Raw/thoughtworks-ontology-llm-data-modernization-2026-07-22]])
- Related publications (linked from the source): [Technical debt bottleneck](https://www.thoughtworks.com/insights/blog/technology-strategy/the-top-5-signs-of-a-technical-debt-bottleneck) · [Path to production for enterprise AI](https://www.thoughtworks.com/insights/articles/Path-to-production-for-enterprise-AI) · [AI-assisted migration lessons](https://www.thoughtworks.com/insights/articles/ai-assisted-migration-lessons) · [Future of software engineering podcast](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/what-does-future-software-engineering-look-like)
