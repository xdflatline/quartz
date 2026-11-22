---
title: "Thinking Machines Lab"
details: "AI research lab that releases the Inkling family of open-weights models. Its 2026 releases centre on looped transformer architectures, native 4-bit training, expert pruning with distillation healing, and publish-alongside monitorability research; it also operates Tinker for hosted inference and fine-tuning."
tags:
  - entity
  - llm
  - local-llm
  - tooling
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Thinking Machines Lab

**Category:** AI research lab / model vendor
**Status:** Active (2026)

## Overview

Thinking Machines Lab develops and releases the **Inkling** family of open-weights models. The 2026 releases — Inkling 2 Small and [[Entities/inkling-2-mini|Inkling 2 Mini]] — are distinguished less by scale than by three architectural bets:

1. **Looped transformers** — reusing middle-layer weights across multiple passes per token to buy serial reasoning without parameters ([[Concepts/looped-transformer-architecture]]).
2. **Native low-precision training** — training and deploying in NVFP4/MXFP8 so there is no post-hoc quantization loss ([[Concepts/native-low-precision-training]]).
3. **Publish-alongside oversight research** — shipping a variable-loop research model and monitorability analysis with the production model rather than after it ([[Concepts/latent-reasoning-and-cot-monitorability]]).

## Products and surfaces

- **Inkling 2 Mini** — 26.4B/3.4B MoE, ~20GB, open weights.
- **Tinker** — hosted inference, fine-tuning and playground ([[Entities/tinker]]).
- **Research models** — `TML-d24-varloop-research`, trained for 1–5 loop passes, released to study looping and monitorability.
- **Weights hosting** — Hugging Face organization `thinkingmachines`.

## Collaborations

- **NDIF (National Deep Inference Fabric)** — making looped models accessible to interpretability researchers.
- **Goodfire** — early access for mechanistic interpretability of looped models.
- **Stanford Hazy Research / Scaling Intelligence** — early access for the Intelligence-per-Watt evaluation.
- **NVIDIA** — NVFP4 kernels and hardware acceleration on GB300; DGX Spark deployment.

## Related

- [[Entities/inkling-2-mini]] — the flagship small model
- [[Entities/tinker]] — hosted platform
- [[Research/looped-transformers-and-local-frontier]] — synthesis of the release

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Site: https://thinkingmachines.ai/
- Blog: https://thinkingmachines.ai/news/inkling-2-mini/
- Hugging Face: https://huggingface.co/thinkingmachines
