---
title: "Darwin Gödel Machine (DGM)"
detail: "Zhang et al. 2025. An LLM-based coding agent that is allowed to modify its own harness codebase. Code editing uses two tools: bash (<bash_command>) and editor (view/create/edit <file_path>). New agents are evaluated; only high-performing ones are added to the pool."
details: "DGM is harness evolution under a fixed model. The parent-selection rule — probability ∝ performance / (1 + number_of_children) — is the single design choice that keeps the population diverse. In experiments with Claude 3.5 Sonnet, DGM-discovered agents reach SWE-bench Verified 20% → 50% and Polyglot 14.2% → 30.7% from a simple initial harness."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2505.22954
---

# Darwin Gödel Machine (DGM)

**Source:** Zhang et al., "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents," arXiv:2505.22954, 2025.

## Overview

An LLM-based coding agent that is allowed to **modify its own harness codebase**. The "Darwin" is evolutionary search; the "Gödel" is self-reference — the system modifying itself.

## Procedure

1. Start with one coding agent in the pool
2. Pick a parent with probability ∝ performance / (1 + number_of_children)
3. The selected parent examines its own benchmark log and proposes improvements to its own harness codebase
4. Code editing uses two tools: `bash` (`<bash_command>`) and `editor` (`view/create/edit <file_path>`)
5. New agents are evaluated; only sufficiently high-performing ones are added to the pool
6. Repeat until some stop criterion

## Results

| Benchmark | Simple initial harness | DGM-discovered |
|-----------|------------------------|----------------|
| SWE-bench Verified | ~20% | up to 50% |
| Polyglot | 14.2% | 30.7% |

Base LLM: `Claude 3.5 Sonnet`. The initial harness was intentionally simple; DGM reaches strong results by editing the harness code, not the underlying model.

## Related

- [[Concepts/darwin-godel-machine]] — the concept
- [[Entities/hyperagents]] — the meta-agent follow-up
- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
