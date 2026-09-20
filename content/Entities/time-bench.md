---
title: "Time-Bench"
details: "Large-scale multi-task temporal reasoning dataset released alongside Time-R1 (Liu et al., arXiv:2505.13508v2, 2025-06-03). >200,000 examples derived from 10 years of New York Times news (2014–2023) with explicit temporal annotations across four Stage 1 subtasks (timestamp inference, time-difference estimation, event ordering, masked time entity completion). Augmented with synthetic data for future-event training and held-out real news for evaluation. CC BY 4.0."
tags:
  - entity
  - benchmark
  - training
created: 2026-09-14
updated: 2026-09-14
type: entity
sources:
  - "[[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]"
---

# Time-Bench

**Category:** Project (dataset)
**Repository:** https://github.com/ulab-uiuc/Time-R1
**License:** CC BY 4.0

---

## Overview

Time-Bench is the large-scale multi-task temporal reasoning dataset released alongside the Time-R1 paper (Liu et al., UIUC, arXiv:2505.13508v2, 2025-06-03). It contains over 200,000 examples derived from 10 years of New York Times news data, with explicit temporal annotations covering four fundamental Stage 1 subtasks: timestamp inference, time-difference estimation, event ordering, and masked time entity completion. The benchmark enables evaluation of LLM temporal reasoning and the construction of trained temporal models.

## Key Details

- **Source corpus:** New York Times (NYT) news articles spanning January 2016 to December 2023 (>200,000 articles) for Stage 1 training; 7,000 real articles January–July 2024 for Stage 2 training
- **Synthetic augmentation:** ~half-volume synthetic data for August 2024 – February 2025, generated using DeepSeek-V3 from May–July 2024 news (used for Stage 2 training to avoid test-set leakage)
- **Held-out test set:** real news events from August 2024 – February 2025 (for Stage 2 evaluation and Stage 3 AvgMaxSim against real events)

### Four Stage 1 subtasks

1. **Timestamp Inference** — infer `YYYY-MM` date for an event from its headline + abstract
2. **Time-Difference Estimation** — infer dates of two events and the temporal gap in months
3. **Event Ordering** — infer dates of three events and produce correct chronological permutation
4. **Masked Time Entity Completion** — fill in masked `<Year>` or `<Month>` token in event description

### Evaluation metrics

- **Stage 1 / Stage 2:** Average Total Score $R(x, y) = R_{\text{acc}} + R_{\text{format}} - P_{\text{penalty}}$, range $[-0.8, 1.1]$; uses dynamic decay $\alpha$ during training, fixed $\alpha = 0.1$ for testing
- **Stage 3 (Creative Generation):** **AvgMaxSim** — mean over generated items of max cosine similarity (using all-MiniLM-L6-v2 384-d embeddings) to real news items in the target month
  $$\text{AvgMaxSim}_m = \frac{1}{N_g} \sum_{i=1}^{N_g} \max_{\mathbf{B}_r \in \mathcal{D}_{\text{real},m}} \text{sim}(\mathbf{A}_{g,i}, \mathbf{B}_r)$$

## Related Concepts

- [[Concepts/temporal-reasoning-evaluation-benchmarks]] — the broader pattern
- [[Concepts/post-knowledge-cutoff-temporal-prediction]] — the operational problem the synthetic data addresses
- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — the training pipeline

## Related Entities

- [[Entities/time-r1]] — the model trained on this dataset
- [[Entities/ulab-uiuc]] — the research group that built it

## References

- Raw Article: [[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]
- Paper: https://arxiv.org/abs/2505.13508v2
- Code & data: https://github.com/ulab-uiuc/Time-R1
