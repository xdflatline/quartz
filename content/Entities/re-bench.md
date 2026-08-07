---
title: "RE-Bench"

details: "Each environment = (scoring function, starting solution, reference solution); each can be run with 8 or fewer H100 GPUs. Examples: optimize a kernel, run a scaling-law experiment, fix an embedding, fine-tune GPT-2 for QA. The most important finding: agents beat humans at 2-hour budgets; humans exceed agents at 8-hour and 32-hour settings."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2411.15114
---

# RE-Bench

**Source:** Wijk et al., "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts," ICML 2025.

## Overview

Frontier AI R&D capabilities of language model agents **against human experts**. 7 open-ended ML research-engineering environments; 71 8-hour attempts by 61 distinct human experts.

## The Environments

Each environment = (scoring function, starting solution, reference solution); each can be run with 8 or fewer H100 GPUs.

Examples:
- Optimize a kernel
- Run a scaling-law experiment
- Fix an embedding
- Fine-tune GPT-2 for QA

## Human vs Agent

- Human experts: non-zero score in 82% of 8-hour attempts; 24% matched or exceeded strong reference solutions
- Best AI agents: 4× higher than humans at 2-hour budget
- **Humans had better returns to longer budgets and exceeded agents at 8-hour and 32-hour settings**

The budget-scaling result is the most important finding in this benchmark — it is direct evidence for the "long-term success" bottleneck in [[Concepts/open-rsi-bottlenecks]].

## Related

- [[Concepts/ai-research-engineering-benchmarks]] — the reference suite
- [[Concepts/open-rsi-bottlenecks]] — bottleneck 6 (long-term success) is what RE-Bench measures
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
