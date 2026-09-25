---
title: "Ollaya Library — decider (Mapika on Qwen3.5)"
details: "Full library-page snapshot of the decider decoder decision-model family built on Qwen3.5: usage, speed, how it works, and limits."
tags:
  - raw
  - llm
created: 2026-09-26
updated: 2026-09-26
type: raw
source: https://ollaya.dev/library/decider
---

**Source:** Ollaya (`https://ollaya.dev/library/decider`)
**Date Retrieved:** 2026-09-26
**Type:** Model library page

---

# decider

decider is a family of open decision models by [Mapika](https://huggingface.co/Mapika), built on Qwen3.5 base models and released under Apache-2.0. For each question it lays out the context, the question and lettered options, then reads the model's next-token logits for the option letters at an answer slot. It never generates text; every question is one forward pass.

## Models

| Tag | Base | Params | Typed-decisions accuracy |
| --- | --- | --- | --- |
| `decider:latest`, `decider:2b` | Qwen3.5-2B | 1.9B | **0.591** |
| `decider:0.8b` | Qwen3.5-0.8B | 0.75B | 0.506 |

Accuracy is argmax against the majority label on all 400 typed-decisions states. For comparison, `nli` scores 0.548, `gliclass` 0.477, `laya:en` 0.361. The labels have low annotator agreement, so compare numbers to each other rather than reading them as absolutes.

## Usage

```shell
ollaya run decider --preset triage "My order never arrived and support ignores me. Refund me today or I'm switching to your competitor."
```

The same `/api/decide` endpoint shape applies, with `model: "decider"` (or `decider:0.8b` / `decider:2b`).

## Speed

- **RTX 4090, end to end:** a five-question request with a short state takes ~155 ms on `0.8b` and ~190 ms on `2b` at the median. Slower than encoder models (Laya: 8–10 ms) but still faster than hosted Jev (236–276 ms).
- **State length:** cost grows with the number of options times the context length.
- **Memory:** on a 24 GB GPU, `2b` handles states up to about 8k tokens. Longer states spill out of GPU memory and become very slow.

## How it works

- **Weights.** They come from Mapika's own `model.safetensors`, downloaded from Hugging Face, pinned to a commit and verified by sha256. Ollaya hosts only the ONNX graph (8 MB). BF16 weights are widened to fp32 when the model loads.
- **Parity.** Ollaya's Rust runtime matches the Python reference exactly: identical token ids and answer-slot positions, same decision on every test question, on CPU and CUDA.

## Limits

- **Memory.** `2b` needs about 8 GB at fp32. Both models are slow on the CPU.
- **Score criteria.** Criteria given as an object instead of a list are rejected (matches TypeSafe's API).
