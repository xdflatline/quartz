---
title: "Time-R1"
details: "Open-weight 3B-parameter LLM from UIUC's ULab (Liu, Han, Yu, Li, You; arXiv:2505.13508v2, 2025-06-03) trained with a three-stage GRPO + dynamic-reward curriculum on temporal reasoning tasks (comprehension → future prediction → creative scenario generation). Despite being 200x smaller, matches or exceeds DeepSeek-R1-671B on future event prediction (Stage 2 avg 0.7780 vs 0.7503) and on creative future scenario generation (Stage 3 AvgMaxSim 48.90% vs 48.81%). CC BY 4.0; checkpoints and Time-Bench dataset released on GitHub and Hugging Face."
tags:
  - entity
  - llm
  - training
  - benchmark
created: 2026-09-14
updated: 2026-09-14
type: entity
sources:
  - "[[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]"
---

# Time-R1

**Category:** Tool (model)
**Repository:** https://github.com/ulab-uiuc/Time-R1
**Hugging Face:** https://huggingface.co/collections/ulab-ai/time-r1-682626aea47cb2b876285a16
**License:** CC BY 4.0

---

## Overview

Time-R1 is a 3B-parameter LLM (built on Qwen2.5-3B-Instruct) trained to endow a small model with **comprehensive temporal reasoning** — understanding, prediction, and creative generation — via a three-stage reinforcement learning curriculum driven by a dynamic, rule-based reward system using GRPO. The model is the headline contribution of Liu et al. (UIUC, arXiv:2505.13508v2, 2025-06-03) and is the first demonstration that a moderate-sized LLM can match or exceed SOTA models >200× its size on future event prediction and creative scenario generation tasks.

## Key Details

- **Base model:** Qwen2.5-3B-Instruct
- **Training algorithm:** GRPO (Group Relative Policy Optimization)
- **Framework:** veRL
- **Compute:** 4 × NVIDIA A6000 GPUs
- **Key hyperparameters:** KL coefficient $\beta = 0.001$, $K = 5$ rollout responses per prompt
- **Checkpoints released:** $\theta_1$ (Stage 1 — comprehension), $\theta_2$ (Stage 2 — prediction; used for Stage 3 inference)

### Three-stage architecture

| Stage | Task | Training | Output checkpoint |
|-------|------|----------|-------------------|
| **1 — Comprehension** | Timestamp inference, time-difference estimation, event ordering, masked time entity completion | RL on pre-cutoff NYT data (Jan 2016 – Dec 2023) | $\theta_1$ |
| **2 — Prediction** | Future event time prediction (Aug 2024 – Feb 2025) | RL on real Jan–Jul 2024 + synthetic Aug 2024 – Feb 2025 | $\theta_2$ |
| **3 — Generation** | Creative future scenario generation (8 themes × multiple months) | Inference only (no fine-tuning) | (uses $\theta_2$) |

### Headline results (from main paper)

| Benchmark | Time-R1 (3B) | Best baseline | Margin |
|-----------|--------------|---------------|--------|
| Stage 1 Overall Avg. | **0.6476** | DeepSeek-R1-671B: 0.6916 | -0.044 (within striking distance) |
| Stage 1 Completion | **0.7555** | DeepSeek-R1-671B: 0.7493 | +0.006 (best) |
| Stage 2 Future Event Prediction | **0.7780** | DeepSeek-R1-671B: 0.7503 | +0.028 |
| Stage 3 AvgMaxSim (Creative Generation) | **48.90%** | DeepSeek-V3-671B: 48.81% | +0.09 pts |

### Key findings from the paper

- **Small beats large on temporal tasks.** A 3B model with specialized RL outperforms 671B generalist models on future prediction and creative generation.
- **Dynamic reward curriculum is essential.** The fixed-reward ablation (Time-R1-Fixed-Reward) underperforms the full model and produces ~2× more verbose outputs (~250 vs ~130 tokens).
- **Staged curriculum beats direct training.** Stage 2 only (Time-R1-S2-Direct) reaches 0.7331; with Stage 1 first, reaches 0.7780. Stage 1's foundational comprehension is crucial.
- **Transfer to generation without generation training.** Stage 3 success comes purely from inference on $\theta_2$ — the temporal understanding from Stages 1+2 transfers.
- **Reasoning process matters, not length.** The dynamic-reward model is both more accurate and more concise, indicating a more focused reasoning pattern.

## Related Concepts

- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — the architecture
- [[Concepts/dynamic-reward-curriculum-rl-finetuning]] — the reward design
- [[Concepts/post-knowledge-cutoff-temporal-prediction]] — the operational problem
- [[Concepts/temporal-reasoning-evaluation-benchmarks]] — the evaluation methodology
- [[Concepts/time-as-first-class-modeling-axis]] — Reis (MMA) on why temporal modeling is foundational
- [[Concepts/reinforcement-learning-grpo]] — the underlying algorithm

## Related Entities

- [[Entities/time-bench]] — released dataset
- [[Entities/ulab-uiuc]] — research group
- [[Entities/qwen]] — base model (Qwen2.5-3B-Instruct)
- DeepSeek-R1 (671B) — outranked baseline on Stage 2 prediction
- DeepSeek-V3 (671B) — outranked baseline on Stage 3 generation

## References

- Raw Article: [[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]
- Paper: https://arxiv.org/abs/2505.13508v2
- Code: https://github.com/ulab-uiuc/Time-R1
- HF Collection: https://huggingface.co/collections/ulab-ai/time-r1-682626aea47cb2b876285a16
