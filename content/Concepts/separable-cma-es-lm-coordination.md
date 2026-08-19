---
title: "Separable CMA-ES for LM Coordination"
details: "A training regime that uses separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES) — black-box optimization with diagonal covariance — to learn the parameters of a lightweight decision head on top of a frozen-or-near-frozen LLM. The strategy dominates gradient-based RL, imitation learning, and random search when the parameter space is high-dimensional (~10K), each parameter has only tiny individual influence on the scalar reward (low SNR), and the per-evaluation budget is tight (closed-loop multi-turn trajectories make each evaluation expensive)."
tags:
  - concepts
  - llm
  - optimization
  - training
sources:
  - Raw/trinity-coordinator-arxiv.md
  - Papers/trinity-evolved-llm-coordinator.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# Separable CMA-ES for LM Coordination

**Source:** [[Raw/trinity-coordinator-arxiv]], [[Papers/trinity-evolved-llm-coordinator]]
**Category:** Optimization Method
**Status:** Production-validated (TRINITY, ICLR 2026)

## Overview

A training regime that uses **separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES)** — black-box optimization with diagonal covariance — to learn the parameters of a lightweight decision head on top of a frozen-or-near-frozen LLM. The strategy dominates gradient-based RL, imitation learning, and random search when:

- The parameter space is high-dimensional (~10K head parameters).
- Each parameter has only a tiny individual influence on the scalar reward (low SNR).
- The per-evaluation budget is tight (closed-loop multi-turn trajectories make each evaluation expensive).

## Why "Separable"?

Full CMA-ES learns a dense covariance matrix over the parameter space, scaling as O(n²). **Sep-CMA-ES** assumes the covariance is diagonal, so it only learns per-axis step sizes — reducing memory and variance-estimate noise to O(n). This makes the algorithm tractable for ~10K-dim problems and dramatically more sample-efficient under tight budgets.

## The Budget-Constrained Regime

The paper defines the regime crisply:

- **Dimensionality:** ~10K parameters (the head, plus singular-value scales of the SLM's layers).
- **Budget:** 1.5k–40k evaluations (each = a full multi-turn trajectory through the agent pool).
- **Reward:** Sparse, terminal — based on the final output's correctness against a ground-truth benchmark.

This is the regime where, in the paper's theoretical analysis, **block-ε-separability** of the objective gives sep-CMA-ES its advantage over both random search and reinforcement learning.

## Block-ε-Separability

Informally, an objective is block-ε-separable if the parameters can be partitioned into a small number of blocks, and the contributions of different blocks to the reward are (approximately) independent. The TRINITY paper proves that, in this regime:

- **Random search** with fitness averaging sees noise-shrinking proportional to 1/B (B = batch size), but per-parameter signal stays buried in noise.
- **ep-CMA-ES** amortizes per-axis variance estimates across iterations and exploits the block structure, yielding per-iteration gain that scales with the block-ε separability index and the budget.
- **REINFORCE**'s per-parameter gradient estimator has variance depending on the baseline; in this regime the baseline cannot reduce variance enough to match the ES signal.

The paper provides an explicit head-to-head ratio showing sep-CMA-ES beats random search when the per-iteration gain outweighs the population size cost.

## Empirical Comparison

The optimizer choice visibly shapes the learned agent-selection distribution:

| Optimizer | Selection distribution after training |
|---|---|
| **sep-CMA-ES** | Concentrates on a small, high-performing subset of the agent pool |
| **REINFORCE** | Stays nearly uniform (ineffective policy improvement) |
| **Random search** | Collapses to unipolar choices (over-selects a single agent or role) |
| **Supervised fine-tuning** | Competitive single-turn performance, but does not scale to multi-turn (label generation is prohibitive) |

![LLM selection distribution evolves as the coordinator learning progresses. Left: Distribution evolution from sep-CMA-ES. Right: Distribution evolution from REINFORCE. The sep-CMA-ES trajectory concentrates on a small, high-performing subset of the agent pool. The REINFORCE trajectory remains nearly uniform.](/assets/trinity-coordinator/fig06-es-vs-rl-distribution.svg)

*Figure 6: sep-CMA-ES (left) vs REINFORCE (right) — selection-distribution evolution.*

## When to Use sep-CMA-ES

**Fits when:**
- The objective is black-box and non-differentiable (closed APIs, mixed agent architectures).
- The dimensionality is high but the per-parameter influence is weak.
- The evaluation budget is tight (each evaluation is expensive).
- The objective is *approximately* separable into a few blocks (parameters cluster into a small number of behaviourally independent groups).

**Does not fit when:**
- The objective is differentiable end-to-end (gradient descent is strictly better).
- The dimensionality is low (full CMA-ES is fine and more expressive).
- The reward is dense and per-step (RL with per-step rewards wins).
- The objective is non-separable (the diagonal-covariance assumption hurts).

## Related

- [[Papers/trinity-evolved-llm-coordinator]] — the canonical paper
- [[Concepts/evolved-llm-coordinator]] — the architecture that uses sep-CMA-ES
- [[Concepts/evolutionary-search-for-harnesses]] — a related application of ES to agent harnesses
- [[Concepts/meta-agent-workflow-search]] — another evolutionary-search-of-policy pattern
