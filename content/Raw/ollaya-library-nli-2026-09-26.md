---
title: "Ollaya Library — nli (Moritz Laurer)"
details: "Full library-page snapshot of the nli zero-shot NLI family (DeBERTa-v3-large and ModernBERT-large) by Moritz Laurer: usage, how it works, and limits."
tags:
  - raw
  - llm
created: 2026-09-26
updated: 2026-09-26
type: raw
source: https://ollaya.dev/library/nli
---

**Source:** Ollaya (`https://ollaya.dev/library/nli`)
**Date Retrieved:** 2026-09-26
**Type:** Model library page

---

# nli

Zero-shot NLI classifiers by [Moritz Laurer](https://huggingface.co/MoritzLaurer). Ollaya turns every option of a question into a hypothesis and asks the model whether the state entails it. Choice and score questions take the most-entailed option; a yes/no question takes the probability that its statement is entailed.

## Models

| Tag | Backbone | Params | License | Typed-decisions accuracy |
| --- | --- | --- | --- | --- |
| `nli:latest`, `nli:deberta-v3-large` | DeBERTa-v3-large | 435M | MIT | **0.548** |
| `nli:modernbert-large` | ModernBERT-large | 396M | Apache-2.0 | 0.515 |

Accuracy is argmax against the majority label on all 400 typed-decisions states. For comparison, `laya:en` 0.361, `gliclass` 0.477. Labels have low annotator agreement, so compare numbers to each other rather than as absolutes.

## Usage

```shell
ollaya run nli --preset triage "I was charged twice for my subscription this month and want a refund."
```

Point any TypeSafe client at `http://localhost:11435` and set the model to `nli`.

## How it works

- **One sequence pair per option.** Each option is a premise–hypothesis pair (state, then option hypothesis), so cost grows with the number of options. A 20-option question runs 20 sequences.
- **Batching.** All sequences in a request share one batched forward pass.
- **Hypothesis templates.** Come from each model's recommended phrasing and live in the model's `decision` layer.
- **Weights.** Authors' own `model.safetensors`, downloaded from Hugging Face, pinned to a commit and verified by sha256. Ollaya hosts only the ONNX graph (~5 MB).
- **Parity.** Ollaya's Rust runtime reproduces the Python reference exactly: same token ids and same decision on every test question, on CPU and CUDA.

## Limits

- **Uncalibrated.** Zero-shot entailment models, not trained decision models. Probabilities are not calibrated — fit a `CALIBRATION` layer on your own data before relying on thresholds.
- **English.** Work best on English text.
- **Training data licenses.** Part of the DeBERTa model's training data carries non-commercial licenses. The author publishes a `-c` variant trained on commercially-usable data only; Ollaya does not ship it yet.
