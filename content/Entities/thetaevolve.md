---
title: "ThetaEvolve"

details: "ThetaEvolve extends the [[Concepts/evolutionary-search-for-harnesses]] family by adding an RL signal on top of pure selection and in-context learning as a third update mechanism. Designed for test-time learning on open problems where the search space is large and the reward is sparse."
tags:
  - entities
  - harness
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2511.23473
---

# ThetaEvolve

**Source:** Wang et al., "ThetaEvolve: Test-time Learning on Open Problems," arXiv:2511.23473, 2025.

## Overview

Combines **evolutionary search** with **reinforcement learning** and **in-context learning** for test-time learning on open problems. Extends the [[Concepts/evolutionary-search-for-harnesses]] family with an RL signal on top of pure selection.

## Why the RL Component

Pure selection can plateau when the fitness signal is sparse. RL provides a denser gradient — even small wins produce reward updates. Combined with evolutionary diversity, the loop can explore widely while still being driven by a consistent objective.

## Related

- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Entities/alphaevolve]] — the parent
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
