---
title: "UIUC ULab"
details: "Research group at the University of Illinois at Urbana-Champaign led by Jiaxuan You, focused on LLM reasoning, agentic systems, graph learning, and data mining. Notable outputs include Time-R1 (2025), a 3B-parameter LLM trained for comprehensive temporal reasoning via a three-stage GRPO + dynamic-reward curriculum that outperforms models 200x its size on future event prediction and creative scenario generation. Code, models, and the Time-Bench dataset are released openly under CC BY 4.0."
tags:
  - knowledge-management
created: 2026-09-14
updated: 2026-09-14
type: entity
sources:
  - "[[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]"
---

# UIUC ULab

**Category:** Project (research group)
**Website:** https://github.com/ulab-uiuc

---

## Overview

UIUC ULab is a research group at the University of Illinois at Urbana-Champaign led by **Jiaxuan You** (Siebel School of Computing and Data Science). The group's work spans LLM reasoning, agentic systems, graph learning, and data mining, with a notable recent focus on **training-time specialization for temporal reasoning** — the bet that a small model with carefully designed RL fine-tuning can outperform generalist large models on temporally-grounded tasks.

## Key Details

- **Lead:** Jiaxuan You (UIUC Siebel School of Computing and Data Science)
- **Notable members on Time-R1:** Zijia Liu, Peixuan Han, Haofei Yu, Haoru Li
- **GitHub org:** https://github.com/ulab-uiuc
- **Hugging Face org:** https://huggingface.co/ulab-ai

### Representative output

**Time-R1** (arXiv:2505.13508v2, 2025-06-03) — a 3B LLM trained with a three-stage GRPO + dynamic-reward curriculum for comprehensive temporal reasoning. The paper's central claim is that thoughtful RL specialization can beat scale: Time-R1 (3B) outperforms DeepSeek-R1-671B on future event prediction (0.7780 vs 0.7503) and on creative scenario generation (48.90% vs 48.81% AvgMaxSim).

## Related Concepts

- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — the architecture ULab developed
- [[Concepts/dynamic-reward-curriculum-rl-finetuning]] — the reward design pattern
- [[Concepts/post-knowledge-cutoff-temporal-prediction]] — the operational problem ULab attacked
- [[Concepts/temporal-reasoning-evaluation-benchmarks]] — the evaluation methodology

## Related Entities

- [[Entities/time-r1]] — flagship model
- [[Entities/time-bench]] — released dataset
- Jiaxuan You — group lead, Siebel School of Computing and Data Science, UIUC

## References

- Raw Article: [[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]
- Paper: https://arxiv.org/abs/2505.13508v2
- Code: https://github.com/ulab-uiuc/Time-R1
