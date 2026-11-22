---
title: "Native low-precision training (train and deploy in one numeric format)"
details: "Training the model end to end in the low-precision format it will be served in, rather than quantizing afterwards. Inkling 2 Mini's expert layers ran NVFP4 on every forward pass from pretraining through RL, with the final four layers in MXFP8, and the released weights ship in exactly those formats — eliminating conversion loss and putting a 26.4B-parameter MoE into a ~20GB footprint."
tags:
  - concept
  - quantization
  - training
  - local-llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Native low-precision training (train and deploy in one numeric format)

**Category:** Training / Quantization Pattern
**Status:** Production in Inkling 2 Mini (2026-11)

## Overview

Most small-model deployment is a two-step pipeline: train in BF16/FP16, then quantize to 4-bit for serving. The quantized model is an approximation of the trained one, and post-training quantization (PTQ) trades quality for size at the end of the process.

The alternative shown here is to **train in the deployment precision**. Inkling 2 Mini used **NVFP4 in the expert layers on all forward passes from pretraining through reinforcement learning**, with the **final four layers run in MXFP8**. The released weights are the same: 20 layers in NVFP4, 4 layers in MXFP8.

Because serving precision equals training precision, there is **no conversion loss from quantization** — the deployed model is the model that was trained, not a compressed copy of it.

## What makes it practical

- **Kernel support.** The approach relies on a dedicated 4-bit kernel and hardware acceleration on NVIDIA GB300 during training — it is a hardware-co-designed technique, not a flag.
- **Selective higher precision.** The last four layers stay at 8-bit, which limits the accuracy cost of forcing the whole network to 4 bits.
- **Footprint outcome.** Total memory footprint is **~20GB**, enough to run on a 32GB-or-more Mac via Ollama, a 48GB MacBook Pro offline, or an NVIDIA DGX Spark.
- **Format breadth is preserved.** GGUF builds for llama.cpp/Unsloth are still published, so the native-format weights are not the only distribution channel.

## Why it matters beyond one model

1. **Removes the PTQ quality cliff.** The usual "Q4 loses a point or two" trade disappears when the model never existed at higher precision.
2. **Makes the memory footprint a training-time decision.** Parameter count and precision are chosen together against a deployment target (a laptop, a desktop AI box), instead of discovered at packaging time.
3. **Shifts the ecosystem cost.** Native 4-bit training is only as portable as its kernels; a model trained this way is most efficient on the hardware generation it was co-designed with, and other backends fall back to GGUF conversions.
4. **Complements QAT rather than replacing it.** [[Concepts/quantization-aware-training-qat|QAT]] simulates low precision while training in higher precision; this pattern actually trains in the low precision. Both avoid the pure-PTQ cliff, with different hardware coupling.

## Boundaries and risks

- **Hardware coupling.** The efficiency claim is strongest on GB300-class training hardware and NVFP4-capable inference targets.
- **Precision is not the only lever.** The ~20GB footprint is the product of 26.4B total parameters after expert pruning, not of 4-bit weights alone ([[Concepts/expert-pruning-and-healing]]).
- **Quality attribution is entangled.** The vendor reports benchmark results for the finished model; it does not isolate how much of the quality comes from native 4-bit training versus the healing/distillation stage.

## Related Concepts

- [[Concepts/quantization-aware-training-qat]] — simulated low precision during training
- [[Concepts/llm-quantization-reference]] — PTQ levels and sizing, the baseline this pattern departs from
- [[Concepts/mobile-quantization-schema-wna8o8]] — deployment-side precision schema for mobile
- [[Concepts/expert-pruning-and-healing]] — the parameter-count half of the footprint story
- [[Concepts/local-agent-model-economics]] — what the footprint buys

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- End-to-end 4-bit training article: https://thinkingmachines.ai/blog/end-to-end-4-bit-training/
- Research: [[Research/looped-transformers-and-local-frontier]]
