---
title: "MLE-bench"

details: "Uses Kaggle public leaderboards as human baselines. Best setup in the paper: o1-preview with AIDE scaffolding reached at least Kaggle bronze-medal level in 16.9% of competitions. Includes resource-scaling and contamination analyses."
tags:
  - entities
  - benchmark
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2410.07095
---

# MLE-bench

**Source:** Chan et al., "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering," arXiv:2410.07095, 2024.

## Overview

75 ML-engineering competitions curated from Kaggle. Tests training models, preparing datasets, running experiments, and submitting predictions to grading scripts. Uses Kaggle public leaderboards as human baselines.

## SOTA

Best setup in the paper: `o1-preview` with **AIDE scaffolding** reached at least Kaggle bronze-medal level in 16.9% of competitions.

## Includes

- Resource-scaling analyses
- Contamination analyses (do the LLMs have prior knowledge of the competition data?)

## Related

- [[Concepts/ai-research-engineering-benchmarks]] — the reference suite
- [[Entities/re-bench]] — the harder R&D sibling
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
