---
title: "Expert pruning and healing (usage-based cut, distillation recovery)"
details: "Mixture-of-Experts compression pattern: train at high sparsity with a large expert pool, then mid-training delete the least-used experts and recover the lost capability by distilling from a larger sibling model. Inkling 2 Mini started at 8-of-384 routing, pruned two-thirds of its experts to the 128 most used per layer, and healed on 1T distilled tokens to land at 26.4B total / 3.4B active parameters."
tags:
  - concept
  - training
  - local-llm
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Expert pruning and healing (usage-based cut, distillation recovery)

**Category:** Model Compression / Training Pattern
**Status:** Used to produce Inkling 2 Mini (2026-11)

## Overview

A Mixture-of-Experts model can be trained with far more parameters than it needs to serve, then compressed by deleting parts of it. The pattern's two halves are a **usage-based cut** and a **distillation recovery** — prune what the router does not use, then train the survivors to cover the work of what was deleted.

## The sequence

1. **Train wide and sparse.** Inkling 2 Mini started with sparsity 48 — **8 experts chosen out of 384** per routing decision.
2. **Prune mid-training by usage.** At a single point during midtraining, two-thirds of the experts were removed, keeping the **128 most used in each layer**. The basis is router usage, not weight magnitude: the claim is about which experts the model actually routes to, not which weights look smallest.
3. **Heal by distillation.** The pruned model trained on **1T tokens distilled from a larger internal Inkling model**, teaching the remaining experts to take over the deleted experts' work. This recovered the performance the model had before pruning.
4. **Post-train.** SFT on a data mix similar to Inkling 2 Small, then RL over **2.2T tokens in 2,000 steps**, including on-policy distillation for alignment.

## Result

- **26.4B total parameters, 3.4B active.** (The 5.4B "weight activations per token" figure accounts for repeated reads through the looped layers.)
- Small enough in memory to run on consumer hardware — the point of the exercise, per the authors: "to cut the total parameter count of the model, allowing it to run faster and on local hardware."

## Why prune rather than simply train smaller

- **Train-wide-then-prune keeps the quality of a larger search space** for most of training, then pays the memory cost only at deployment.
- **Router usage is a better signal than magnitude** for MoE: an expert that is rarely selected contributes little to outputs even if its weights are not small.
- **Healing is what makes an aggressive cut safe.** Without the distillation stage, deleting two-thirds of the experts would leave a capability hole rather than a smaller model.

## Costs and caveats

- **Extra training compute.** Pruning plus 1T healing tokens is additional work on top of the base run.
- **A larger teacher is required.** The recovery depends on access to a bigger internal model to distill from; this is not a standalone recipe for a lab without one.
- **The saving is memory, not per-token compute.** The active path is already sparse before pruning; what changes is how many parameters must be stored.
- **Benchmark attribution is aggregate.** The vendor reports the finished model, not an ablation isolating pruning, healing and looping.

## Related Concepts

- [[Concepts/native-low-precision-training]] — the other half of the ~20GB footprint
- [[Concepts/looped-transformer-architecture]] — how depth is recovered without parameters
- [[Concepts/local-agent-model-economics]] — the deployment case for the smaller footprint
- [[Concepts/llm-quantization-reference]] — size/quality trade-offs at inference rather than training time

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Research: [[Research/looped-transformers-and-local-frontier]]
- Model card: https://thinkingmachines.ai/model-card/inkling-2-mini/
