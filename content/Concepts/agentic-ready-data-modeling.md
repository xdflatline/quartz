---
title: "Agentic-Ready Data Modeling (MMA Belief 7)"
details: "Seventh core belief of Joe Reis's Mixed Model Arts (MMA) Manifesto: data models must be designed for both human cognition and AI-agent reasoning. The era of humans-only consumption is over. Models must provide the semantic, temporal, and identity context that autonomous agents need to take reliable action — not just the documentation that human analysts need to interpret dashboards. Practical implications: explicit semantics, stable identity, durable time semantics, and agent-consumable metadata."
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

# Agentic-Ready Data Modeling (MMA Belief 7)

**Source:** Joe Reis, *The Mixed Model Arts Manifesto* ([[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]), Belief 7
**Category:** Architecture Pattern (consumer-facing design principle)
**Status:** Proposed best practice (with strong commentary reinforcement)

---

## Overview

Reis's seventh MMA belief states that data models must be **designed for humans *and* engineered for agents**. The era of humans-only consumption — where the only consumer of the data model is an analyst staring at a dashboard — is over. Models must now also serve AI agents that reason, plan, and act autonomously over data. The principle is the Agentic Era's central data-modeling requirement: a model that a human can interpret but an agent cannot reason over is no longer fit for purpose.

The belief directly motivates the rest of MMA: semantics must be explicit (Belief 5), time must be modeled (Belief 4), intent must be declared (Belief 3), and identity must be stable — because agents need all of these to take autonomous, reliable action.

## Core Content

### What changes when agents consume the model

| Property | Human-only model | Agentic-ready model |
|----------|------------------|---------------------|
| Naming | Readable to analysts | Readable **and** unambiguous to a reasoning engine |
| Semantics | In tribal knowledge, code comments, or implicit | Machine-consumable, versioned, decoupled from schema (see [[Concepts/semantics-as-universal-interface]]) |
| Identity | Often contextual or pipeline-assigned | Stable, cross-system, durable |
| Time | Often implicit current-state | Explicit event time, valid time, transaction time (see [[Concepts/time-as-first-class-modeling-axis]]) |
| Documentation | Runbooks, wikis | Structured metadata that agents can retrieve |
| Granularity | Whatever the dashboard needs | Whatever the agent's plan requires, including edge cases |

### The autonomy loop the model must support

A modern AI agent over data typically does:

1. **Discover** — find the relevant entities, tables, and fields
2. **Interpret** — understand what the fields mean and how they relate
3. **Plan** — compose queries or write actions that achieve an intent
4. **Act** — execute, retrieve, or update
5. **Verify** — check that the action was correct against declared intent

Each step requires the model to expose structured information. A model that requires tribal knowledge to interpret is a model the agent cannot use reliably.

### What "engineered for agents" means in practice

- **Semantic layer exposed via API.** Not buried in a wiki.
- **Stable entity identity across systems.** Agents cannot reconcile keys the way humans can.
- **Explicit intent per dataset.** Agents need to know whether a dataset is operational, analytical, or both.
- **Temporal queries first-class.** "What was true at time T?" must be answerable, not just "what is true now?"
- **Failure semantics declared.** What does a null mean? What does a missing row mean? Agents cannot infer this.
- **Audit trail.** Every agent action recorded for human review.

### Connection to other MMA beliefs

- [[Concepts/semantics-as-universal-interface]] is the substrate
- [[Concepts/time-as-first-class-modeling-axis]] is the prerequisite for temporal reasoning
- [[Concepts/intent-driven-data-modeling]] is what the agent is trying to satisfy
- [[Concepts/unified-modeling-discipline-mma]] is the prerequisite — the agent cannot afford to deal with two divergent modeling traditions

## Key Insights

1. **Agents are a new first-class consumer.** Not a downstream side effect of dashboards and pipelines — a consumer in their own right, with different needs.
2. **Human-readable is not the same as agent-readable.** Documentation that only humans can parse is insufficient.
3. **Agent failures are model failures.** When an agent hallucinates or misfires over a dataset, the cause is often missing semantic or temporal context — not the agent's reasoning.
4. **The Agentic Era is the forcing function for MMA.** Reis is explicit that without agent consumers, the unification of modeling traditions would be optional; with them, it is necessary.

## Related Concepts

- [[Concepts/semantics-as-universal-interface]] — the substrate for agent consumption
- [[Concepts/time-as-first-class-modeling-axis]] — temporal reasoning prerequisite
- [[Concepts/intent-driven-data-modeling]] — declared intent as an agent input
- [[Concepts/unified-modeling-discipline-mma]] — unification is needed because agents cannot tolerate silos
- [[Entities/mixed-model-arts-manifesto]] — source

## Related Entities

- [[Entities/joe-reis]]
- [[Entities/mixed-model-arts-manifesto]]

## References

- Raw Article: [[Raw/reis-mixed-model-arts-manifesto-2026-08-19]]
- Original: https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
