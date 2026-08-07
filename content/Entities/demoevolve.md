---
title: "DemoEvolve"

details: "DemoEvolve addresses a known failure mode of pure self-rollout loops: the archive fills with the model's own patterns, leaving the harness unable to discover strategies outside its prior distribution. By seeding the archive with human expert demonstrations, DemoEvolve expands the search space without abandoning the LLM-driven mutation operator."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2605.24539
---

# DemoEvolve

**Source:** Che et al., "DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations," arXiv:2605.24539, 2026.

## Overview

Augments the self-rollout archive with **human expert demonstrations** as reference experience for harness-level diagnosis and editing.

## Why Demonstrations

Pure self-rollout loops have a known failure mode: the archive fills with the model's own patterns, and the harness can no longer discover strategies outside its prior distribution. Seeding the archive with human expert demonstrations **expands the search space** without abandoning the LLM-driven mutation operator.

## When to Use

- When the loop's own rollouts are too homogeneous
- When domain expertise is available but expensive to elicit
- When the failure modes include "stuck in the model's prior distribution"

## Related

- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Entities/shinkaevolve]] — sibling sample-efficiency work
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
