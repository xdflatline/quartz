---
title: "PaperBench"

details: "The hardest known coding-agent benchmark as of 2026. Best model at the time (Claude 3.5 Sonnet, ~21%) does not outperform ML PhDs. Each replication task is decomposed into smaller, individually gradable sub-tasks. Includes PaperBench, PaperBench Code-Dev (lighter version), and JudgeEval."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2504.01848
---

# PaperBench

**Source:** Starace et al., "PaperBench: Evaluating AI's Ability to Replicate AI Research," ICML 2025.

## Overview

Replicate 20 ICML 2024 Spotlight and Oral papers from scratch. Each task involves understanding paper contributions, developing a codebase, and successfully executing experiments. 8,316 rubrics co-developed with the paper authors.

## Scale

- 20 full paper replications
- 8,316 rubrics (fine-grained scoring criteria)
- Includes PaperBench (full), PaperBench Code-Dev (lighter), and JudgeEval

## SOTA

Best model at the time (Claude 3.5 Sonnet, ~21%) does not outperform ML PhDs.

## Related

- [[Concepts/ai-research-engineering-benchmarks]] — the reference suite
- [[Concepts/open-rsi-bottlenecks]] — bottleneck 1 (weak evaluators) is what PaperBench tries to address
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
