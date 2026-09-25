---
title: "Typed-decisions benchmark — Ollaya 400-state suite"
details: "Ollaya's internal evaluation suite for decision-model accuracy: argmax against the majority label across 400 typed-decisions states, used to rank laya, decider, nli and gliclass."
tags:
  - concept
  - benchmark
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/ollaya-library-laya-2026-09-26.md
  - .Raw/ollaya-library-decider-2026-09-26.md
  - .Raw/ollaya-library-nli-2026-09-26.md
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Typed-decisions benchmark — Ollaya 400-state suite

**Category:** Technical Reference (Benchmark)
**Status:** Active research area

## Overview

The **typed-decisions benchmark** is Ollaya's internal evaluation suite: 400 typed-decisions states, scored as **argmax against the majority label**. Ollaya publishes a single accuracy number per model tag from this benchmark and uses it to compare encoder and decoder decision models head-to-head.

## Core Content

### Results table (from Ollaya library pages, 2026-09-26)

| Model | Architecture | Params | Typed-decisions accuracy |
| --- | --- | --- | --- |
| `laya:typed-decisions` (fine-tuned) | Encoder (ModernBERT-large) | 421M | **0.766** |
| `decider:2b` | Decoder (Qwen3.5-2B) | 1.9B | 0.591 |
| `nli` (DeBERTa-v3-large) | Encoder (NLI) | 435M | 0.548 |
| `decider:0.8b` | Decoder (Qwen3.5-0.8B) | 0.75B | 0.506 |
| `nli:modernbert-large` | Encoder (NLI) | 396M | 0.515 |
| `gliclass` | Encoder (label scorer) | 439M | 0.477 |
| `laya:en` (base, zero-shot) | Encoder (ModernBERT-large) | 421M | 0.361 |

### Caveat from Ollaya

> "The labels have low annotator agreement, so compare the numbers to each other rather than reading them as absolutes."

In other words, the absolute accuracy is not a clean ground-truth score; what the benchmark does well is **rank-ordering** the families against each other.

### What this benchmark does NOT measure

- It does not score **calibration** (ECE) — that's reported separately per model card.
- It does not score **latency** under load — that's also a separate column.
- It does not exercise long contexts (states are short).

### Where typed-decisions fits in the literature

This is Ollaya's own benchmark, not a public shared eval. For comparison, TypeSafe Jev 1.13 publishes 0.727 on the same suite (per the laya page), and Ollaya's laya:typed-decisions surpasses it at 0.766.

## Key Insights

1. **Fine-tuning matters more than backbone size.** `laya:typed-decisions` (encoder, 421M, fine-tuned) beats `decider:2b` (decoder, 1.9B, zero-shot) by 0.175 absolute.
2. **Within zero-shot models, decoder beats encoder** for raw accuracy: `decider:2b` 0.591 > `nli` 0.548 > `gliclass` 0.477 > `laya:en` 0.361.
3. **Annotator agreement is the limiting factor** on interpreting the absolute numbers — the benchmark is best used for relative comparisons inside Ollaya's catalog.

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — what's being benchmarked
- [[Concepts/encoder-vs-decoder-decision-architectures]] — the architecture split the benchmark highlights
- [[Concepts/calibration-for-decision-models]] — a separate axis the benchmark doesn't measure

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
