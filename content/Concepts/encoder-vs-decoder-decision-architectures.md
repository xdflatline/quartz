---
title: "Encoder vs decoder decision-model architectures (Ollaya)"
details: "Architectural split across the four Ollaya decision-model families: encoder path (laya, nli, gliclass) vs decoder path (decider on Qwen3.5), and how each shapes cost, latency, and fine-tuning potential."
tags:
  - concept
  - llm
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/ollaya-library-laya-2026-09-26.md
  - .Raw/ollaya-library-decider-2026-09-26.md
  - .Raw/ollaya-library-nli-2026-09-26.md
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Encoder vs decoder decision-model architectures (Ollaya)

**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Ollaya's four families cluster into two architectural camps. **laya**, **nli**, and **gliclass** are encoder-only (no generation) — they score their inputs with classification heads over BERT-style backbones. **decider** is decoder-only — it sits on top of Qwen3.5 and reads the next-token logits at an answer slot, but never actually generates tokens. The split drives cost scaling, latency, option-handling, and fine-tuning potential.

## Core Content

### Encoder path

| Family | Backbone | Params | Mechanism | Per-question cost |
| --- | --- | --- | --- | --- |
| laya (en) | ModernBERT-large | 421M | Fine-tuned typed-decision classifier | One sequence |
| laya (multilingual) | mmBERT-base | 322M | Same, multilingual | One sequence |
| nli (deberta) | DeBERTa-v3-large | 435M | Zero-shot NLI entailment | N sequence pairs, batched |
| nli (modernbert) | ModernBERT-large | 396M | Same, smaller backbone | N sequence pairs, batched |
| gliclass | DeBERTa-v3-large | 439M | Instruction-following label scorer | One sequence (all options as labels) |

Latencies at fp16 on RTX 4090, 5-question request: laya:en 16.3 ms, laya:multilingual 9.1 ms. nli / gliclass are in the same range.

### Decoder path

| Family | Backbone | Params | Mechanism | Per-question cost |
| --- | --- | --- | --- | --- |
| decider:2b | Qwen3.5-2B | 1.9B | Read option-letter logits at answer slot | One LM forward pass; cost grows with options × context |
| decider:0.8b | Qwen3.5-0.8B | 0.75B | Same | Same |

Latencies at fp16 on RTX 4090, 5-question request: decider:0.8b ~155 ms, decider:2b ~190 ms. Roughly 10× slower than the encoder path.

### Where each path wins

- **Encoder (laya, nli, gliclass)** — low latency, low cost per call, and either multilingual support (laya:multilingual via mmBERT) or large-option support (gliclass, single sequence with all labels). nli is the highest-accuracy zero-shot encoder (0.548 on typed-decisions).
- **Decoder (decider)** — higher raw accuracy on the typed-decisions benchmark (0.591 at 2B) and the only path that benefits from a generative backbone's broad pretraining (Qwen3.5). Costs more and is slower.

### Fine-tuning potential

- **laya:typed-decisions** is fine-tuned from ModernBERT-large on typed-decisions data and reaches **0.766** — the highest score in the catalog.
- The other three families are zero-shot or near-zero-shot at their current checkpoints.

## Key Insights

1. Encoder decision models are 10× faster than decoder decision models on identical workloads, at the cost of upper-bound accuracy.
2. Fine-tuning an encoder (laya:typed-decisions) closes and surpasses the decoder's accuracy advantage: 0.766 vs 0.591.
3. Decoder decision models inherit a generative backbone's world knowledge and broad language coverage, but the cost of a single forward pass through a 2B-parameter LM dominates the latency budget.

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — the pattern being implemented
- [[Concepts/typed-decisions-benchmark-ollaya]] — the numbers behind the architectural split
- [[Concepts/onnx-decision-runtime-parity]] — runtime cost is the same per-family regardless of architecture

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
