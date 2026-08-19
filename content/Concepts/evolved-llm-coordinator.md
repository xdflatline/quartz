---
title: "Evolved LLM Coordinator"
details: "A coordination architecture where a small language model (an SLM, ~0.6B parameters) acts as the control surface for orchestrating a pool of larger, heterogeneous LLMs over multi-turn interactions. The SLM is paired with a tiny linear head (~10K parameters) that emits two logits (agent selection and role assignment). The head is trained with a derivative-free optimizer (separable CMA-ES) rather than gradient-based RL, on the reward signal of the closed-loop multi-turn trajectories. The resulting policy is *evolved* in the ES sense, not gradient-descented."
tags:
  - concepts
  - llm
  - agent
  - orchestration
sources:
  - Raw/trinity-coordinator-arxiv.md
  - Papers/trinity-evolved-llm-coordinator.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# Evolved LLM Coordinator

**Source:** [[Raw/trinity-coordinator-arxiv]], [[Papers/trinity-evolved-llm-coordinator]]
**Category:** Architecture Pattern
**Status:** Production-validated (Sakana AI's TRINITY, ICLR 2026)

## Overview

A coordination architecture where a **small language model (SLM)** acts as the control surface for orchestrating a pool of larger, heterogeneous LLMs over multi-turn interactions. The SLM is paired with a tiny linear head (~10K parameters) that emits two logits — one for agent selection, one for role assignment — at each turn. The head is trained with a **derivative-free optimizer** (separable CMA-ES) rather than gradient-based RL, on the reward signal of the closed-loop multi-turn trajectories. The resulting policy is *evolved* in the evolutionary-strategy sense, not gradient-descented.

## Anatomy

1. **SLM backbone (~0.6B parameters).** A small language model reads the full multi-turn transcript at every turn and produces a hidden state.
2. **Lightweight head (~10K parameters).** A linear layer operating in parallel to the LM head, reading the penultimate-token hidden state and producing two logits:
   - Agent logits (over the LLM pool)
   - Role logits (over the coordination roles)
3. **Singular-value fine-tuning.** The SLM's per-layer singular values are scaled cheaply (LoRA-like axis) to fit the coordination task without retraining the full backbone.
4. **Multi-turn loop.** Each turn, the head selects an LLM + role, the chosen LLM produces a response, and the response is appended to the transcript. The loop terminates on a verifier-accept signal or after a fixed turn budget.

![Coordinator parameterization — a lightweight head operates in parallel to the base model's LM head and takes the hidden state corresponding to the penultimate output token as its sole input.](/assets/trinity-coordinator/fig02-parameterization.svg)

*Figure 2: Parametrization of the TRINITY coordinator.*

## Why Evolution, Not Gradients?

The paper identifies three properties of the coordination-training regime that **invert** the usual RL/supervision calculus:

- **High dimensionality, weak coupling.** Each of the ~10K head parameters has only a tiny influence on the scalar reward, making per-parameter gradients low-SNR.
- **Budget-tight.** Each evaluation step requires running the coordinated agents for inference; 1.5k–40k evaluations is the realistic budget.
- **Closed-loop, non-differentiable.** The agent pool is end-to-end non-differentiable (closed APIs, mixed architectures).

In this regime, the paper proves that **separable CMA-ES** dominates REINFORCE, imitation learning, and random search by exploiting **block-ε-separability** in the objective. The evolved selection distribution shows meaningful adaptation (concentration on high-performing agents) while REINFORCE stays nearly uniform.

## Hidden States as the Coordination Substrate

A central hypothesis: the hidden states of a small LM contain sufficient semantic signal for a tiny head to coordinate multiple LLMs effectively. The paper verifies this empirically:

- **Linear and RBF SVMs** on penultimate-token hidden states reach **100% accuracy** on task-type classification; 71–78% on agent-selection classification.
- **PCA, LDA, UMAP, t-SNE** all show clear clustering by task type and by agent selection.

![Task type separability in extracted hidden states. Both are based on penultimate-token hidden states processed by the SLM on the input sequence, and the labels are from the task metadata.](/assets/trinity-coordinator/fig05-task-separability.png)

*Figure 5: Task type separability in extracted hidden states.*

## When to Use This Pattern

**Fits when:**
- The agent pool is heterogeneous (different architectures, closed APIs, mixed open/closed weights).
- The decision per turn is small (a discrete choice over a few dozen agents × a handful of roles).
- The reward is delayed and sparse (multi-turn trajectory quality).
- Training budget is constrained (1.5k–40k evaluations realistic).
- The downstream agents are non-differentiable or too expensive to fine-tune.

**Does not fit when:**
- The agent pool is homogeneous (a single model with no real differentiation to exploit).
- The decision space is rich (natural-language decomposition, free-form tool calls) — in that case, a full reasoning LLM likely outperforms a small head.
- The reward is dense and per-step (RL with per-token rewards will outperform ES).
- Training budget is unbounded (gradient methods on a large policy network will overtake).

## Comparisons

- **vs. [[Concepts/llm-routing-pool|LLM routing pool]]:** A standard router picks one agent per query, one-shot. The evolved coordinator runs multi-turn and assigns roles, so the same agent can be invoked multiple times in different roles.
- **vs. majority voting / self-consistency:** These are parallel aggregation of redundant outputs. The evolved coordinator is *sequential*, with role-specialized invocations building on each other's outputs.
- **vs. MoA / multi-agent debate:** The coordinator is opaque (a small head) rather than a prompted LLM, so the policy is acquired by search rather than written by hand. This trades interpretability for a much smaller parameter footprint (~10K vs 7B+).

## Origins

This is the architecture introduced in TRINITY (Xu, Sun, et al., Sakana AI, arXiv 2512.04695, ICLR 2026). The conceptual lineage includes model-routing papers, mixture-of-experts routers, and CMA-ES literature, but the specific combination of SLM + tiny head + sep-CMA-ES is novel to TRINITY.

## Related

- [[Papers/trinity-evolved-llm-coordinator]] — the canonical paper
- [[Concepts/separable-cma-es-lm-coordination]] — the optimizer choice
- [[Concepts/role-based-llm-delegation]] — the Thinker/Worker/Verifier split
- [[Concepts/llm-routing-pool]] — the simpler one-shot ancestor
- [[Concepts/coordinator-worker-task-dag-orchestration]] — DAG-based orchestrator (different style)
- [[Entities/sakana-ai]] — the research lab behind TRINITY
