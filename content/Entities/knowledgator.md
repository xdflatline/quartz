---
title: "Knowledgator"
details: "Organization behind GLiClass, the instruction-following zero-shot classifier that scores all options in a single sequence; published as `gliclass` in Ollaya under Apache-2.0."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Knowledgator

**Category:** Company / Organization
**Repository:** https://huggingface.co/knowledgator

## Overview

Knowledgator is the author organization behind **GLiClass**, the instruction-following zero-shot classifier that Ollaya ships as `gliclass`. Their approach is to score all options in a single sequence by treating them as label markers around the task prompt and the input state, so cost barely grows with option count. Backbone is DeBERTa-v3-large (439M).

## Key Details

- Published models: GLiClass large (Apache-2.0). HF: https://huggingface.co/knowledgator.
- Accuracy on Ollaya's typed-decisions benchmark: 0.477 (DeBERTa-v3-large backbone).
- Strength: many-option questions where `nli`'s per-option cost would be too high.
- Weakness: `noul` questions without explicit `true` / `false` criteria are confidently wrong.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — Knowledgator ships the single-sequence encoder path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — 0.477 vs siblings

## References

- Raw: [[Raw/ollaya-library-gliclass-2026-09-26]]
- HF org: https://huggingface.co/knowledgator
