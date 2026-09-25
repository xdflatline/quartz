---
title: "laya — Convai Innovations decision model family"
details: "Open Apache-2.0 family of encoder-based decision models by Convai Innovations, with multilingual routing, fine-tuned typed-decisions variant, and ONNX parity."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-laya-2026-09-26.md
---

# laya

**Category:** Tool / Model family
**Repository:** https://huggingface.co/convaiinnovations/laya
**Website:** https://ollaya.dev/library/laya

## Overview

laya is a family of **encoder-based decision models** by Convai Innovations. Unlike a generative LLM, a decision model reads an input _state_ together with a set of typed questions and returns calibrated answers for every question in a single forward pass — it never generates text. laya is the only family in the Ollaya catalog that ships a **fine-tuned typed-decisions variant** (`laya:typed-decisions`, 0.766 on the 400-state benchmark) and the only one with **multilingual coverage** beyond English (`laya:multilingual`, 100+ languages via mmBERT-base).

## Key Details

### Model tags

| Tag | Backbone | Params | Context | Languages |
| --- | --- | --- | --- | --- |
| `laya:latest` | router | — | 512 / 1024 | auto (en / multilingual) |
| `laya:en` | ModernBERT-large | 421M | 512 | English |
| `laya:multilingual` | mmBERT-base | 322M | 1024 | 100+ |
| `laya:typed-decisions` | ModernBERT-large | 421M | 1024 | English (fine-tuned) |

### Performance

| Variant | Latency, 1 question | Latency, 10 batched | Calibration error (ECE) |
| --- | --- | --- | --- |
| Laya (English, T4) | 39.5 ms | 158.6 ms | 0.081 after temperature fitting |
| Laya multilingual (T4) | 32.8 ms | 72.3 ms | — |
| laya (RTX 4090, fp16) | — | — | 16.3 ms (`en`) / 9.1 ms (`multilingual`) for 5-question request |

### ONNX export

Across 2,383 questions per checkpoint, the ONNX export chose the same answer as the PyTorch fp32 reference 100% of the time, with a maximum probability difference of 1.1 × 10⁻⁴.

### Limitations

- Base `en` / `multilingual` are near chance zero-shot on typed-decisions (0.362) — use `laya:typed-decisions` for those workflows.
- Choice with > ~20 options is weak (0.425 on Banking77 vs 0.870 for Jev).
- Raw checkpoints are over-confident; `laya:multilingual` ships without refit temperatures. Refit calibration on your own labelled data and bake it in via `CALIBRATION` in a Modelfile.

### Licensing

Apache-2.0. Weights are downloaded from Hugging Face, pinned to a commit, verified by sha256; Ollaya does not re-host the weights.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — laya is the canonical encoder path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — the benchmark that distinguishes `en` from `typed-decisions`
- [[Concepts/language-routing-in-decision-models]] — `laya:latest` is the only Ollaya router
- [[Concepts/calibration-for-decision-models]] — temperature refitting matters for laya
- [[Concepts/onnx-decision-runtime-parity]] — laya is the documented parity case study

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- HF model card: https://huggingface.co/convaiinnovations/laya
- Ollaya page: https://ollaya.dev/library/laya
