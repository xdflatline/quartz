---
title: "Dynamic Reward Curriculum for RL Fine-Tuning"
details: "Training methodology from Liu et al. (Time-R1, arXiv:2505.13508v2, 2025-06-03) for cold-start-resistant RL fine-tuning of LLMs: stratify the training data by difficulty, then progressively tighten the reward function's decay coefficient across three phases (easy-only strict → full-task lenient → full-task progressively-strictened). Ablation shows the dynamic curriculum produces both higher accuracy and ~2x more concise reasoning outputs than a static, strict reward. The pattern generalizes to any task where rule-based verifiable rewards admit continuous-distance scoring."
tags:
  - llm
  - training
  - architecture-pattern
created: 2026-09-14
updated: 2026-09-14
type: concept
sources:
  - "[[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]"
---

# Dynamic Reward Curriculum for RL Fine-Tuning

**Source:** Liu, Han, Yu, Li, You, *Time-R1* (UIUC, arXiv:2505.13508v2, 2025-06-03) ([[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]), Section 3.3.3
**Category:** Architecture Pattern (RL training methodology)
**Status:** Production-validated (empirically validated in the paper; ablation shows measurable gains)

---

## Overview

The dynamic reward curriculum is the training methodology Liu et al. designed to overcome the cold-start problem in RL fine-tuning of LLMs. It stratifies the training data by difficulty (using an initial checkpoint's error distribution), then runs three sequential phases that progressively tighten the reward function's decay coefficient $\alpha$. Compared to a static, strict reward, the dynamic curriculum produces both **higher task accuracy** and **~2× more concise reasoning outputs** (~130 tokens vs ~250 tokens), indicating the curriculum fosters more focused reasoning, not just more.

## Core Content

### The mechanism: exponential-decay date reward

The base accuracy reward for date prediction is an exponential decay on month-distance:

$$R_{\text{acc}} = R_{\text{date}}(t_p, t_{gt}, \alpha) = e^{(-\alpha \cdot \Delta m(t_p, t_{gt}))}$$

The decay coefficient $\alpha$ controls strictness: larger $\alpha$ means more severe penalties for off-by-X-months errors. $\alpha = 0.1$ is "strict" (1-month error costs ~10% reward); $\alpha = 0.07$ is "lenient" (1-month error costs ~7% reward).

### The three-phase curriculum

**Difficulty stratification.** Run the initial Qwen2.5-3B-Instruct checkpoint on Timestamp Inference across the entire training set. Samples where $|\Delta m| \leq 3$ months are "easy"; the rest are "normal/hard."

**Phase 1 — Foundational logic and format learning.**

- Tasks: Timestamp Inference only, easy samples only
- Decay: fixed $\alpha = \alpha_{\text{target}} = 0.1$ (strict)
- Goal: learn task logic, response format, foundation

**Phase 2 — Exploration on full task suite.**

- Tasks: all 4 Stage 1 subtasks, full dataset (easy + normal/hard)
- Decay: easy → $\alpha = 0.1$ (strict); normal/hard → $\alpha = \alpha_{\text{start}} = 0.07$ (lenient)
- Goal: explore diverse reasoning pathways on hard examples without excessive penalty for initial inaccuracies

**Phase 3 — Transition to strict evaluation.**

- Tasks: all 4 Stage 1 subtasks, full dataset
- Decay: easy → $\alpha = 0.1$ (fixed); normal/hard → linear transition from $\alpha_{\text{start}} = 0.07$ to $\alpha_{\text{target}} = 0.1$ over $s_{\text{transition}} = 50$ steps, then fixed at $\alpha_{\text{target}} = 0.1$

The transition formula:

$$\alpha_{\text{transition}}(s) = \alpha_{\text{start}} + (\alpha_{\text{target}} - \alpha_{\text{start}}) \cdot \min(1.0, s / s_{\text{transition}})$$

For **all test evaluations**, $\alpha = 0.1$ is fixed for comparable measurement.

### Ablation evidence

| Metric | Time-R1-Fixed-Reward (static, strict) | Time-R1 (dynamic curriculum) |
|--------|----------------------------------------|-------------------------------|
| Stage 1 Overall Avg. | 0.6259 | **0.6476** |
| Stage 1 Completion | plateau ~0.70 | continues to **0.7555** |
| Avg response length (tokens) | ~250 | ~130 |

The fixed-reward ablation not only underperforms but **plateaus** on the Completion subtask, while the curriculum-trained model continues to improve. This is the signature of the dynamic curriculum's value: it prevents convergence to a suboptimal policy and yields both higher accuracy and more efficient reasoning.

### Task-specific reward extensions

The dynamic curriculum sits on top of several task-specific reward designs that should generalize:

- **Inconsistency penalty** $P_{\text{incon}}$ for Time-Difference Estimation and Event Ordering: penalizes discrepancies between explicit answer and dates inferred as intermediate steps
- **Diversity penalty** $P_{\text{div}}$ for Event Ordering: penalizes trivial solutions (all dates identical, or sequential dates with trivial order)
- **Length and repetition penalties** $P_{\text{len\_rep}}$: penalize outputs exceeding 900 tokens or containing repetitive phrases / insufficient n-gram diversity
- **Format adherence** $R_{\text{ans\_fmt}}$: bonus for valid output format (prerequisite for accuracy scoring)

These together form a rule-based reward $R(x, y) = R_{\text{acc}} + R_{\text{format}} - P_{\text{penalty}}$ with range $[-0.8, 1.1]$ — a fully rule-based, verifiable reward (RLVR-style) with no learned reward model.

## Key Insights

1. **Curriculum on rewards, not just data.** Traditional curriculum learning orders examples by difficulty. Liu et al. additionally order the reward function's strictness by difficulty — easy examples get strict evaluation from the start; hard examples get lenient first, strict later.
2. **Leniency enables exploration.** Strict rewards on cold-start hard examples produce excessive negative gradients that converge the policy to a suboptimal "safe" mode.
3. **Conciseness emerges as a side effect.** The dynamic curriculum produces ~2× shorter outputs without an explicit length reward dominating — the model learns a more focused reasoning pattern.
4. **Rule-based + verifiable reward suffices.** No learned reward model is needed; the reward is a closed-form function of (prediction, ground-truth). This generalizes to any task admitting continuous-distance or verifiable rewards.
5. **Cold-start is not unique to RLHF.** Any RL fine-tuning of a base model on a narrow task faces the same problem; the dynamic curriculum pattern should transfer.

## Related Concepts

- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — the higher-level curriculum within which this reward design operates
- [[Concepts/reinforcement-learning-grpo]] — the underlying RL algorithm
- [[Concepts/temporal-reasoning-evaluation-benchmarks]] — uses the same reward function for evaluation

## Related Entities

- [[Entities/time-r1]] — model trained with this reward design
- [[Entities/time-bench]] — training data (difficulty-stratified)

## References

- Raw Article: [[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]
- Paper: https://arxiv.org/abs/2505.13508v2
- Code: https://github.com/ulab-uiuc/Time-R1
