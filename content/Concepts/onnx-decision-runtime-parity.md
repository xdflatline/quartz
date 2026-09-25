---
title: "ONNX decision-runtime parity (sha256-pinned weights, Rust vs Python reference)"
details: "Ollaya's reproducibility strategy: ONNX graphs hosted locally, weights downloaded from the author's Hugging Face repo pinned to a commit and verified by sha256, with a Rust runtime that matches the Python reference exactly on CPU and CUDA."
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

# ONNX decision-runtime parity (sha256-pinned weights, Rust vs Python reference)

**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Ollaya commits to **bit-exact parity** with each model's Python reference implementation. The pattern is the same for all four families: ship only the small ONNX graph locally (~5–8 MB), download the weights from the author's Hugging Face repo at a pinned commit, verify by sha256, and run inference through a Rust runtime that reproduces the Python reference exactly on both CPU and CUDA.

## Core Content

### Three-step reproducibility recipe

1. **Pin weights to a commit on Hugging Face**, downloaded as `model.safetensors` from the author's own repository (Convai Innovations, Mapika, Moritz Laurer, Knowledgator). Ollaya does not re-host weights.
2. **Ship only the ONNX graph** — small (8 MB for decider, ~5 MB for nli), easy to audit, and never carries the weights.
3. **Rust runtime parity** — for every test question, the Rust runtime produces the same token ids, the same answer-slot positions, and the same decision as the Python reference, on CPU and CUDA.

### Documented parity evidence (laya)

Across 2,383 questions per checkpoint (`en`, `multilingual`, `typed-decisions`), the ONNX export chose the **same answer** as the PyTorch fp32 reference **100% of the time**, with a maximum probability difference of 1.1 × 10⁻⁴.

The fp16 graph (used on CUDA GPUs by default) can differ from fp32 on near-ties, so Ollaya exposes `-fp16` and `-fp32` tags to pin precision.

### Why this matters for decision models

Decision models are used as **judges** — routing, triage, escalation, content moderation. If the runtime is not bit-exact with the reference, the same input state can yield a different top answer, and consumers cannot trust the model to behave like the published benchmark. Parity turns a decision model from "approximately matches the paper" into "is the paper."

### Precision handling

- One weights file carries both fp16 and fp32 graphs.
- CUDA GPUs default to fp16; CPU uses fp32.
- `-fp16` / `-fp32` tags pin precision explicitly (e.g. `laya:en-fp32`).
- `decider` widens BF16 to fp32 on load (the underlying Qwen3.5 base is BF16).

## Key Insights

1. **Don't re-host weights** — pin to the author's HF commit and verify by sha256. Avoids license confusion and version drift.
2. **The ONNX graph is auditable in minutes** — at 5–8 MB, a maintainer can read the graph and verify the operator set.
3. **Parity is a published claim, not a hope** — Ollaya publishes the 2,383-question parity audit on laya and commits to the same standard across all four families.

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — what parity is preserving
- [[Concepts/encoder-vs-decoder-decision-architectures]] — parity applies uniformly to both paths

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
