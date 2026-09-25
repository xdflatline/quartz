---
title: "gliclass — Knowledgator GLiClass zero-shot classifier"
details: "Instruction-following zero-shot classifier by Knowledgator (DeBERTa-v3-large); scores all options in a single sequence, so cost barely grows with option count."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# gliclass

**Category:** Tool / Model family
**Repository:** https://huggingface.co/knowledgator
**Website:** https://ollaya.dev/library/gliclass

## Overview

gliclass is Ollaya's port of Knowledgator's GLiClass — an instruction-following zero-shot classifier. Unlike nli (one sequence pair per option) or decider (a whole LM forward pass), gliclass writes all options as **labels inside a single sequence**, with the question's instructions as the task prompt and the state as the input text. The model scores all the labels in one forward pass, so cost barely grows with the number of options. It lands at 0.477 on Ollaya's typed-decisions benchmark — below `nli` (0.548) but above `laya:en` base (0.361) — and is the recommended encoder when option count is large and `nli`'s per-option cost is too high.

## Key Details

### Model tags

| Tag | Backbone | Params | License | Typed-decisions accuracy |
| --- | --- | --- | --- | --- |
| `gliclass:latest`, `gliclass:large` | DeBERTa-v3-large | 439M | Apache-2.0 | 0.477 |

### How it works

- **One sequence per question.** Label markers go first, then the task prompt, then the state, up to 1,024 tokens.
- The graph pools every label's span and scores it against the text.
- The mapping of `choice`, `score`, `noul` onto labels is Ollaya's, chosen by testing on typed-decisions.
- Weights are Knowledgator's own `model.safetensors`, pinned to a commit and verified by sha256.
- Rust runtime matches the Python reference exactly on CPU and CUDA.

### Limits

- **`noul` without `criteria` is its weakest point.** A yes/no question without true/false descriptions is scored as a single label with a sigmoid and can be confidently wrong. Give `noul` questions both `true` and `false` descriptions, or use `nli` for them.
- A question with more options than fit in 1,024 tokens is rejected with `TOO_MANY_OPTIONS`.
- Uncalibrated — fit a `CALIBRATION` layer before relying on thresholds.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — gliclass is the single-sequence encoder path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — 0.477 vs siblings
- [[Concepts/calibration-for-decision-models]] — calibration caveat
- [[Concepts/onnx-decision-runtime-parity]] — same Rust-runtime parity guarantee

## References

- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
- HF org: https://huggingface.co/knowledgator
- Ollaya page: https://ollaya.dev/library/gliclass
