---
title: "Role-Based LLM Delegation"
details: "A multi-LLM orchestration pattern where, at each turn, the coordinator assigns the selected LLM not just *which* agent to invoke but also *which role* it should play. Common role sets include Thinker / Worker / Verifier (decompose, execute, validate), Planner / Executor / Critic, or any small finite set of role-specialized prompts. The role is injected as a system prompt prefix before the request is sent to the chosen LLM. The same physical model can be invoked multiple times across a trajectory in different roles, so the role set decouples the decision of *which agent* from the decision of *what kind of step is next*."
tags:
  - concepts
  - llm
  - agent
  - orchestration
  - multi-agent
sources:
  - Raw/trinity-coordinator-arxiv.md
  - Papers/trinity-evolved-llm-coordinator.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# Role-Based LLM Delegation

**Source:** [[Raw/trinity-coordinator-arxiv]], [[Papers/trinity-evolved-llm-coordinator]]
**Category:** Coordination Pattern
**Status:** Production-validated (TRINITY, ICLR 2026)

## Overview

A multi-LLM orchestration pattern where, at each turn, the coordinator assigns the selected LLM not just *which* agent to invoke but also *which role* it should play. The role is injected as a system-prompt prefix before the request is sent to the chosen agent. The same physical model can be invoked multiple times across a trajectory in different roles, so the role set decouples **which agent** from **what kind of step is next**.

## The Three-Role Baseline (TRINITY)

The TRINITY paper uses a three-role split:

- **Thinker (T):** Devises high-level strategies and decomposes the task into sub-questions.
- **Worker (W):** Performs concrete problem-solving steps on a single sub-question.
- **Verifier (V):** Evaluates the current solution's soundness and completeness; an accept-and-stop signal terminates the loop.

The same model (e.g., GPT-5) can be selected as a Thinker on turn 1 and a Verifier on turn 3 — the role changes the prompt, not the model. The verifier's accept signal is also what gives the loop a natural stopping condition (separate from a fixed-turn budget).

![Overview of the cyclical coordination architecture. In each turn, the full conversation transcript is passed to a compact coordinator model. A lightweight head selects an LLM and assigns it one of three roles: Thinker (T), Worker (W), or Verifier (V). A message processing module injects a role-specific prompt before the request is sent to the chosen LLM.](/assets/trinity-coordinator/fig01-overview.svg)

*Figure 1: TRINITY's coordination loop — the head emits both an agent choice and a role choice at each turn.*

## Worked Example

To solve a complex depreciation problem, TRINITY's evolved coordinator invokes:

- **Turn 1** — *Thinker* (e.g., GPT-5): "Decompose the depreciation problem into stages."
- **Turn 2** — *Worker* (e.g., Claude-Sonnet-4): "Compute the depreciation for each stage per the decomposition."
- **Turn 3** — *Verifier* (e.g., GPT-5 again, different role): "Validate the answer and identify edge cases."

The same model (GPT-5) appears in turns 1 and 3 with different role prompts, producing different behaviours. The loop terminates when the Verifier accepts.

## Why Decouple Agent and Role?

The decoupling buys two things:

1. **Expressive coverage with a small action space.** A 7-agent pool × 3 roles = 21 distinct actions per turn, but the head only emits two `(L, R)` logits — neither dimension explodes.
2. **Mixed strategy across the trajectory.** The same agent can be invoked in different roles at different turns, so the policy can compose agent strengths with role-specific prompts without needing separate physical models for each role.

## Other Role Sets in the Literature

| Role set | Typical use |
|---|---|
| Thinker / Worker / Verifier | Decompose–execute–validate; TRINITY |
| Planner / Executor / Critic | Long-horizon planning; agentic harnesses |
| Generator / Reviewer / Refiner | Iterative refinement; self-consistency variants |
| Proposer / Discounter / Aggregator | Multi-agent debate |

Common to all: the role set is **small (3–4)**, **fixed**, and **prompt-distinguished** rather than model-distinguished.

## When to Use This Pattern

**Fits when:**
- The task is multi-step and benefits from explicit decomposition.
- The agent pool is heterogeneous (different models excel at different steps).
- Termination is non-trivial and benefits from a verifier-accept signal.
- The action space at each turn should stay small (a discrete choice over (agent, role) is more tractable than free-form routing).

**Does not fit when:**
- The task is single-step or atomic (no decomposition needed).
- The agent pool is homogeneous (role differentiation is moot).
- Termination is naturally external (e.g., a fixed test set).

## Related

- [[Papers/trinity-evolved-llm-coordinator]] — the canonical paper
- [[Concepts/evolved-llm-coordinator]] — the architecture that uses this pattern
- [[Concepts/llm-routing-pool]] — the simpler one-shot ancestor (no role, no multi-turn)
- [[Concepts/coordinator-worker-task-dag-orchestration]] — DAG-based variant (more structured)
- [[Concepts/agent-collusion-pattern]] — a different multi-agent pathology worth distinguishing
