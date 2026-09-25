---
title: "decider — Mapika decoder decision model on Qwen3.5"
details: "Apache-2.0 family of decoder decision models by Mapika, built on Qwen3.5-0.8B and Qwen3.5-2B, that read option-letter logits in a single forward pass per question."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-decider-2026-09-26.md
---

# decider

**Category:** Tool / Model family
**Repository:** https://huggingface.co/Mapika
**Website:** https://ollaya.dev/library/decider

## Overview

decider is a family of **decoder-based decision models** by Mapika, built on Qwen3.5. It is the only decoder (generative-backbone) family in the Ollaya catalog, and it is currently the most accurate open decision model Ollaya ships. For each question, it lays out the context, the question, and lettered options (A, B, C, ...) in the prompt, then reads the next-token logits at an answer slot for those option letters. It never actually generates text — every question is one forward pass that inspects logits, then the system maps the highest-logit letter back to a label.

## Key Details

### Model tags

| Tag | Base | Params | Typed-decisions accuracy |
| --- | --- | --- | --- |
| `decider:latest`, `decider:2b` | Qwen3.5-2B | 1.9B | **0.591** |
| `decider:0.8b` | Qwen3.5-0.8B | 0.75B | 0.506 |

### Performance

- **RTX 4090, end to end:** ~155 ms on `0.8b`, ~190 ms on `2b` for a five-question request (median). Significantly slower than the encoder models (Laya: 8–10 ms for the same workload) but still faster than hosted TypeSafe Jev (236–276 ms).
- **Cost:** grows with options × context length.
- **Memory:** on 24 GB GPU, `2b` handles states up to ~8k tokens before spilling.

### How it works

- Weights are Mapika's own `model.safetensors`, downloaded from Hugging Face, pinned to a commit and verified by sha256. Ollaya hosts only the ONNX graph (8 MB). BF16 weights are widened to fp32 on load.
- The Rust runtime matches the Python reference exactly: identical token ids and answer-slot positions, same decision on every test question, on CPU and CUDA.

### Limits

- `2b` needs ~8 GB at fp32. Both models are slow on CPU.
- Score criteria must be a list, not an object — matches TypeSafe's API.

### Licensing

Apache-2.0.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — decider is the canonical decoder path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — 0.591 vs encoder siblings
- [[Concepts/onnx-decision-runtime-parity]] — same Rust-runtime parity guarantee as laya

## References

- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- HF org: https://huggingface.co/Mapika
- Ollaya page: https://ollaya.dev/library/decider
