---
title: "LLM Routing Pool"
details: "An orchestration pattern where a single router (typically a learned classifier or a small LLM) selects one model from a pool of heterogeneous LLMs to handle a query. Routing is one-shot per query: the same query is sent to one model, the response is returned, and the loop ends. The simplest case is cost/quality routing (cheap model for easy queries, expensive model for hard ones). The pattern is the one-shot ancestor of the multi-turn, multi-role evolved coordinator."
tags:
  - concepts
  - llm
  - orchestration
  - routing
sources:
  - Raw/trinity-coordinator-arxiv.md
  - Papers/trinity-evolved-llm-coordinator.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# LLM Routing Pool

**Source:** [[Raw/trinity-coordinator-arxiv]], [[Papers/trinity-evolved-llm-coordinator]]
**Category:** Orchestration Pattern
**Status:** Production-validated across many vendor routers (OpenRouter, LiteLLM, Together, etc.)

## Overview

An orchestration pattern where a **single router** selects one model from a pool of heterogeneous LLMs to handle a query. Routing is **one-shot per query**: the same query is sent to one model, the response is returned, and the loop ends. The simplest case is cost/quality routing (cheap model for easy queries, expensive model for hard ones). The pattern is the one-shot ancestor of the multi-turn, multi-role evolved coordinator.

## Anatomy

1. **Heterogeneous pool.** A set of LLM endpoints (possibly closed APIs, possibly open-weight servers, possibly a mix) with different cost, latency, and capability profiles.
2. **Router.** A learned classifier (e.g., a small BERT-style model on the query embedding) or a small LLM that emits a single decision: which model to invoke.
3. **One-shot dispatch.** The selected model serves the query and returns. The router does not see the response and does not iterate.

## Common Variants

- **Cost/quality router:** pick the cheapest model that has a non-trivial probability of succeeding on the query.
- **Capability router:** pick the model that has the highest benchmark score on the query's domain.
- **Latency router:** pick the model with the lowest expected latency under current load.
- **Priority router:** pick the model with the highest priority tier under a quota system.

## Comparison with the Evolved Coordinator

| Property | LLM routing pool | Evolved coordinator |
|---|---|---|
| Per-query turns | 1 | N (multi-turn) |
| Distinct actions per turn | 1 (model choice) | 2 (model + role) |
| Agent sees prior turns? | No | Yes (full transcript) |
| Action space | \|pool\| | \|pool\| × \|roles\| |
| Training signal | Per-query feedback (or supervised) | Multi-turn trajectory reward |
| Typical optimizer | Supervised (cross-entropy) | sep-CMA-ES / RL |
| Termination | External (response received) | Internal (verifier-accept) or external (turn budget) |

The evolved coordinator generalizes the routing pool by:

- **Closing the loop** — the next dispatch sees the prior turns' responses.
- **Adding a role dimension** — the same agent can be invoked in different capacities.
- **Optimizing the multi-turn trajectory** — the reward signal is the trajectory quality, not the per-query routing decision.

## When to Use This Pattern

**Fits when:**
- Queries are independent (no cross-query reasoning).
- The pool is heterogeneous (different models excel at different queries).
- Per-query latency must be bounded (no multi-turn overhead).
- The router's decision space is small (one model out of a handful).

**Does not fit when:**
- Queries benefit from multi-turn internal reasoning (decomposition, verification, refinement).
- The pool is homogeneous (no real differentiation to exploit).
- The decision space is rich (free-form routing, tool composition, etc.).

## Related

- [[Papers/trinity-evolved-llm-coordinator]] — the canonical evolved-coordinator paper
- [[Concepts/evolved-llm-coordinator]] — the multi-turn multi-role generalization
- [[Concepts/role-based-llm-delegation]] — the role dimension that the routing pool can be extended with
- [[Concepts/bundled-model-router]] — the SDK/integration-side counterpart (string-ID resolution)
- [[Concepts/coordinator-worker-task-dag-orchestration]] — a more structured orchestrator variant
