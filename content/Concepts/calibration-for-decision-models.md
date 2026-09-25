---
title: "Calibration for decision models (ECE, temperature fitting, CALIBRATION layer)"
details: "Decision-model calibration as a first-class concern: expected calibration error (ECE), temperature refitting on labeled data, and Ollaya's `CALIBRATION` Modelfile directive for baking calibration into a model tag."
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

# Calibration for decision models (ECE, temperature fitting, CALIBRATION layer)

**Category:** Architecture Constraint
**Status:** Production-validated

## Overview

Unlike generative LLMs whose outputs are usually graded for **accuracy**, decision models are graded for **calibration** — does a `noul: 0.91` actually mean the statement holds 91% of the time? Every family in Ollaya's catalog ships with a calibration caveat: zero-shot models are uncalibrated out of the box, and even the fine-tuned encoder (laya) is over-confident unless its temperatures are refit on labeled data. Calibration is exposed as a first-class operation in Ollaya via the `CALIBRATION` Modelfile directive.

## Core Content

### Reported calibration errors

| Model | ECE | Notes |
| --- | --- | --- |
| laya (English, after temperature fitting) | **0.081** | Tesla T4, 10 questions batched |
| laya multilingual | — | Ships without refit temperatures |
| TypeSafe Jev (third-party) | 0.246 | Listed for comparison on laya page |

For comparison, Jev's published ECE of 0.246 vs Laya's 0.081 is roughly 3× worse — the gap is the largest single-axis advantage of the laya family.

### Why raw checkpoints are over-confident

- **Zero-shot NLI models (nli, gliclass)** — never trained to produce calibrated probabilities; the entailment logits are reused as probabilities, which they are not.
- **Encoder fine-tuned on a typed task (laya)** — trained with cross-entropy, which is well-known to produce over-confident outputs on out-of-distribution data.
- **Decoder (decider)** — the option-letter logits are read directly, with no calibration step.

### The fix: temperature fitting + `CALIBRATION`

Temperature fitting rescales the logits by a single scalar τ so that the resulting softmax matches empirical accuracy on a labeled calibration set. ECE drops sharply with even a small labeled set (laya's published 0.081 is "after temperature fitting" — implies a baseline without fitting is much higher).

In Ollaya, this is exposed as a Modelfile directive:

```
CALIBRATION <path-or-spec>
```

…which bakes the fitted temperatures into the model tag so consumers always get calibrated probabilities without re-fitting on every call.

### When you need to fit your own

Per Ollaya's library pages:

- For **laya:en** — base temperatures are over-confident; refit on your labeled data for production thresholds.
- For **laya:multilingual** — ships without refit temperatures; fit before using thresholds.
- For **nli** — explicitly uncalibrated ("these are zero-shot entailment models, not trained decision models"); fit on your data.
- For **gliclass** — explicitly uncalibrated; fit before relying on thresholds.
- For **decider** — no calibration guidance published; option-letter logits are read raw.

## Key Insights

1. **Calibration is the under-discussed axis of decision-model quality.** Accuracy gets the headlines (0.591, 0.548, etc.); calibration is what determines whether `noul: 0.91` is meaningful for a threshold-based workflow.
2. **Temperature fitting on a small labeled set is cheap and high-leverage** — laya's ECE drops from "very over-confident" to 0.081 with this single operation.
3. **`CALIBRATION` belongs in the model definition**, not in the consumer code. A Modelfile directive makes calibration reproducible across deployments and removes the temptation for each caller to re-implement temperature fitting.

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — what calibration is a property of
- [[Concepts/typed-decisions-benchmark-ollaya]] — calibration is a separate axis from this benchmark
- [[Concepts/encoder-vs-decoder-decision-architectures]] — calibration applies to both paths

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
