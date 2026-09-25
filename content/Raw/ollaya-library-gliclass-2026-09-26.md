---
title: "Ollaya Library — gliclass (Knowledgator)"
details: "Full library-page snapshot of the gliclass zero-shot classifier family (DeBERTa-v3-large) by Knowledgator: usage, scoring, and limits."
tags:
  - raw
  - llm
created: 2026-09-26
updated: 2026-09-26
type: raw
source: https://ollaya.dev/library/gliclass
---

**Source:** Ollaya (`https://ollaya.dev/library/gliclass`)
**Date Retrieved:** 2026-09-26
**Type:** Model library page

---

# gliclass

GLiClass is an instruction-following zero-shot classifier by [Knowledgator](https://huggingface.co/knowledgator). Ollaya writes a question's options as labels and its instructions as the task prompt, and the model scores all the labels in a single pass. The cost therefore barely grows with the number of options.

## Models

| Tag | Backbone | Params | License | Typed-decisions accuracy |
| --- | --- | --- | --- | --- |
| `gliclass:latest`, `gliclass:large` | DeBERTa-v3-large | 439M | Apache-2.0 | 0.477 |

For comparison, `nli` scores 0.548 and `laya:en` 0.361 on the same 400-state typed-decisions benchmark.

## Usage

```shell
ollaya run gliclass --preset triage "I was charged twice for my subscription this month and want a refund."
```

The same `/api/decide` endpoint shape applies, with `model: "gliclass"`.

## How it works

- **One sequence per question.** Label markers go first, then the task prompt, then the state, up to 1,024 tokens.
- **Scoring.** The graph pools every label's span and scores it against the text.
- **Mapping to question types.** The mapping of `choice`, `score`, `noul` onto labels is Ollaya's, chosen by testing on typed-decisions.
- **Weights.** Knowledgator's own `model.safetensors`, downloaded from Hugging Face, pinned to a commit and verified by sha256.
- **Parity.** Ollaya's Rust runtime matches the Python reference exactly on CPU and CUDA.

## Limits

- **Yes/no questions without criteria are its weakest point.** Such a question is scored as one label with a sigmoid and can be confidently wrong. Give `noul` questions `criteria` with both `true` and `false` descriptions, or use `nli` for them.
- **Option count.** A question with more options than fit in 1,024 tokens is rejected with `TOO_MANY_OPTIONS`.
- **Uncalibrated.** The model is not calibrated. Fit a `CALIBRATION` layer before relying on thresholds.
