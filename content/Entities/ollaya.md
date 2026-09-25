---
title: "Ollaya"
details: "Local-first runtime for open decision models: serves laya, decider, nli and gliclass over an Ollama-compatible /api/decide endpoint, with sha256-pinned weights and Rust-runtime ONNX parity."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-search-index-2026-09-26.md
  - .Raw/ollaya-library-laya-2026-09-26.md
  - .Raw/ollaya-library-decider-2026-09-26.md
  - .Raw/ollaya-library-nli-2026-09-26.md
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Ollaya

**Category:** Platform
**Website:** https://ollaya.dev

## Overview

Ollaya is a local-first runtime that ships four families of **decision models** — models that read an input state together with typed questions and return calibrated answers (`choice`, `score`, `noul`) in a single forward pass, never generating text. It exposes them through a local HTTP API (`/api/decide`) that mirrors the TypeSafe / Jev API surface, so existing TypeSafe clients can point at Ollaya by switching the base URL. It also ships a CLI (`ollaya run <model> --preset <name>`) and a Modelfile format with a `CALIBRATION` layer for refitting probability temperatures.

The platform is the **integration layer** that makes heterogeneous third-party models (encoder NLI, decoder LM, instruction-tuned classifier, fine-tuned typed-decision model) behave the same way to callers. All four families share the same question schema, answer shape, and routing metadata; only the underlying model weights and scoring strategy differ.

## Key Details

### Model catalog (as of 2026-09-26)

| Model | Author | Backbone | Params | License | Approach |
| --- | --- | --- | --- | --- | --- |
| `laya` (4 tags) | Convai Innovations | ModernBERT-large / mmBERT-base | 322M / 421M | Apache-2.0 | Encoder, fine-tuned typed decisions + multilingual router |
| `decider` (3 tags) | Mapika | Qwen3.5-0.8B / 2B | 0.75B / 1.9B | Apache-2.0 | Decoder, reads option-letter logits |
| `nli` (3 tags) | Moritz Laurer | DeBERTa-v3-large / ModernBERT-large | 396M / 435M | MIT / Apache-2.0 | Encoder, zero-shot NLI entailment |
| `gliclass` (2 tags) | Knowledgator | DeBERTa-v3-large | 439M | Apache-2.0 | Encoder, instruction-following zero-shot |

### Typed-decisions accuracy (400-state benchmark, argmax vs majority label)

| Model | Accuracy |
| --- | --- |
| `decider:2b` | 0.591 |
| `nli` (DeBERTa-v3-large) | 0.548 |
| `gliclass` | 0.477 |
| `decider:0.8b` | 0.506 |
| `nli:modernbert-large` | 0.515 |
| `laya:en` (base, zero-shot) | 0.361 |
| `laya:typed-decisions` (fine-tuned) | 0.766 |

(Numbers from the model library pages; "labels have low annotator agreement, so compare numbers to each other rather than reading them as absolutes" — Ollaya.)

### Runtime architecture

- **Local HTTP server** on port 11435, exposing `/api/decide`. Model selection via `model: "<name>"` in the request body.
- **CLI** with presets (e.g. `--preset triage`).
- **Weights** are downloaded from each author's Hugging Face repo at a pinned commit, verified by sha256; Ollaya hosts only the small ONNX graph locally. This avoids re-hosting model weights.
- **Rust runtime** reproduces the Python reference exactly: same token ids, same answer-slot positions, same decision on every test question, on CPU and CUDA.
- **fp16 / fp32 graphs** are carried in the same weights file; fp16 is used on CUDA GPUs by default, fp32 on CPU. `-fp16` / `-fp32` tags pin the precision.

### API surface

A request body has the shape:

```json
{
  "model": "<name>",
  "state": "<input text or JSON>",
  "questions": {
    "<name>": {
      "type": "choice | score | noul",
      "instructions": "...",
      "criteria": { "...": "..." }
    }
  }
}
```

Responses include `answers`, `model` (which checkpoint answered), `routing` (router decisions), `usage`, and timing fields (`total_duration`, `load_duration`, `eval_duration`).

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — what a "decision model" is
- [[Concepts/encoder-vs-decoder-decision-architectures]] — the architectural split across the four families
- [[Concepts/onnx-decision-runtime-parity]] — Ollaya's reproducibility story
- [[Concepts/typed-decisions-benchmark-ollaya]] — the 400-state benchmark tying the families together
- [[Concepts/calibration-for-decision-models]] — temperature refitting via `CALIBRATION` in Modelfile
- [[Concepts/language-routing-in-decision-models]] — `laya:latest` router behavior

## References

- Raw: [[Raw/ollaya-search-index-2026-09-26]]
- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
- Website: https://ollaya.dev
