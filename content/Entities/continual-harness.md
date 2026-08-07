---
title: "Continual Harness paper"
detail: "Karten et al. 2026. Online adaptation for self-improving foundation agents in a long-horizon gameplay setting. Combines harness updating with co-learning a policy model by distilling a strong teacher model's labels on low-reward trajectories."
details: "Continual Harness is a narrower and cleaner SIA-like experiment: a single task domain (long-horizon gameplay), a single model, but with cleaner attribution. The setup demonstrates that harness updates and weight updates can co-exist in a stable loop when the task is well-scoped."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2605.09998
---

# Continual Harness paper

**Source:** Karten et al., "Continual Harness: Online Adaptation for Self-Improving Foundation Agents," arXiv:2605.09998, 2026.

## Overview

A narrower, cleaner SIA-like experiment: long-horizon gameplay, single model, with **cleaner attribution** than SIA. Combines harness updates with **co-learning a policy model** by distilling a strong teacher model's labels on low-reward trajectories.

## Why It Matters

- The setup is narrower than SIA (single task domain, single model)
- But the attribution is cleaner: the gains can be traced to specific updates
- It demonstrates that harness updates and weight updates **can co-exist in a stable loop** when the task is well-scoped

## Related

- [[Entities/sia-paper]] — the broader-scope sibling
- [[Concepts/joint-harness-weight-optimization]] — the concept
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
