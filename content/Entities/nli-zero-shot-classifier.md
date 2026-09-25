---
title: "nli — Moritz Laurer zero-shot NLI decision model family"
details: "Zero-shot NLI classifiers by Moritz Laurer (DeBERTa-v3-large + ModernBERT-large) that score each option as a hypothesis against the state; the most accurate encoder on Ollaya's typed-decisions benchmark."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-nli-2026-09-26.md
---

# nli

**Category:** Tool / Model family
**Repository:** https://huggingface.co/MoritzLaurer
**Website:** https://ollaya.dev/library/nli

## Overview

The nli family ports Moritz Laurer's well-known zero-shot NLI classifiers into Ollaya as decision models. For each option, Ollaya turns it into a hypothesis ("This text is about X") and asks the model whether the state entails it; choice / score questions take the most-entailed option and yes/no (`noul`) questions take the probability that the statement is entailed. It is the highest-accuracy **encoder** model in Ollaya's catalog on typed-decisions (0.548), beating `gliclass` (0.477) and `laya:en` (0.361), and is the recommended fallback for `noul` questions when other models are weakly calibrated.

## Key Details

### Model tags

| Tag | Backbone | Params | License | Typed-decisions accuracy |
| --- | --- | --- | --- | --- |
| `nli:latest`, `nli:deberta-v3-large` | DeBERTa-v3-large | 435M | MIT | **0.548** |
| `nli:modernbert-large` | ModernBERT-large | 396M | Apache-2.0 | 0.515 |

### How it works

- **One sequence pair per option** (state as premise, option as hypothesis), so cost grows with the number of options. A 20-option question runs 20 sequences.
- All sequences in a request share one batched forward pass.
- Hypothesis templates are drawn from each model's recommended phrasing and live in the model's `decision` layer.
- Weights are the authors' own `model.safetensors`, pinned to a commit and verified by sha256. Ollaya hosts only the ~5 MB ONNX graph.
- Rust runtime reproduces the Python reference exactly: same token ids, same decision on every test question, on CPU and CUDA.

### Limits

- **Uncalibrated.** Zero-shot entailment models, not trained decision models — probabilities are not calibrated. Fit a `CALIBRATION` layer before relying on thresholds.
- **English-first.** Works best on English text.
- **Training data licenses.** Part of DeBERTa's training data carries non-commercial licenses; the author publishes a `-c` variant trained on commercially-usable data only, which Ollaya does not ship yet.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — nli is the canonical zero-shot NLI path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — 0.548 vs encoder siblings
- [[Concepts/calibration-for-decision-models]] — the calibration caveat is loudest for nli

## References

- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- HF author org: https://huggingface.co/MoritzLaurer
- Ollaya page: https://ollaya.dev/library/nli
