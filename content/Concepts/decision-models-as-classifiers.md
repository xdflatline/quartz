---
title: "Decision models as classifiers (state + typed questions → calibrated answers)"
details: "Architecture pattern where a model reads an input state together with a set of typed questions and returns a calibrated answer for each question in a single forward pass, never generating text."
tags:
  - concept
  - llm
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/ollaya-search-index-2026-09-26.md
  - .Raw/ollaya-library-laya-2026-09-26.md
  - .Raw/ollaya-library-decider-2026-09-26.md
  - .Raw/ollaya-library-nli-2026-09-26.md
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Decision models as classifiers (state + typed questions → calibrated answers)

**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A **decision model** is a model that does not generate free-form text. It takes an input **state** (a message, an email, a ticket, a JSON object) together with a set of **typed questions** and returns a calibrated answer for each question in a single forward pass. This pattern — popularized by TypeSafe / Jev and now shipped by Ollaya across four open-model families — is the answer-classification analog of using a generative LLM as a judge.

## Core Content

### Question types

| Type | `criteria` | Answer fields |
| --- | --- | --- |
| `choice` | Object of option → description, or list of labels; 2–255 options | `choice`, `confidence`, `probabilities` |
| `score` | Ordered list of 2–10 levels | `score` (expected level), `confidence`, `legend`, `probabilities` |
| `noul` | Optional `{"true": "...", "false": "..."}` | `noul`: probability the statement holds |

`confidence` is the normalized top probability: `(K · pmax − 1) / (K − 1)` for K options — 0 when every option is equally likely, 1 when one option has all the probability.

### Why a single forward pass matters

In generative-LLM-as-judge, each question costs a full generation (possibly hundreds of tokens), and the model's calibration is whatever the LM happens to emit. In a decision model, every question is one forward pass; the output is a structured probability distribution over options, not free text; and calibration is a property the model can be trained or refit for.

### Cost pattern across model families

- **nli**: per option cost — N sequence pairs for N options, all batched into one forward pass.
- **gliclass**: per question cost — one sequence regardless of option count, options as label markers.
- **laya (encoder)**: per question cost — single sequence; supports 125–250 options depending on tag.
- **decider (decoder)**: per question cost — single forward pass through the LM, cost grows with options × context.

## Key Insights

1. The pattern decouples **scoring** from **generation** — useful when the consumer wants structured, calibrated answers and does not need a free-form explanation.
2. Calibration is a first-class concern: temperature fitting, refit `CALIBRATION` layers, and ECE are part of the design surface, not afterthoughts.
3. The four Ollaya families demonstrate that **encoder** and **decoder** backbones can both serve the pattern — the difference is latency, cost scaling, and accuracy on fine-tuned vs zero-shot workflows.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — splits the four families
- [[Concepts/typed-decisions-benchmark-ollaya]] — the benchmark that frames "how accurate is this pattern"
- [[Concepts/calibration-for-decision-models]] — the calibration dimension
- [[Concepts/onnx-decision-runtime-parity]] — the reproducibility dimension

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
