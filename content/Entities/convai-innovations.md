---
title: "Convai Innovations"
details: "Organization behind the laya decision-model family (Apache-2.0) — publishes encoder-based decision models with English and multilingual variants on Hugging Face."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-laya-2026-09-26.md
---

# Convai Innovations

**Category:** Company / Organization
**Repository:** https://huggingface.co/convaiinnovations

## Overview

Convai Innovations is the author organization behind the **laya** decision-model family. They publish encoder-based decision models under Apache-2.0, with both English (ModernBERT-large) and multilingual (mmBERT-base, 100+ languages) variants, plus a fine-tuned English variant (`laya:typed-decisions`) that is the highest-accuracy model on Ollaya's typed-decisions benchmark at 0.766.

## Key Details

- Published models: `laya` (Apache-2.0). HF model card: https://huggingface.co/convaiinnovations/laya.
- Approach: encoder-only (ModernBERT-large / mmBERT-base) trained as a typed-decision model rather than a generative LM.
- Calibration: base checkpoints ship with temperature fitting on the English variant (ECE 0.081 after fitting); `laya:multilingual` ships without refit temperatures.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — Convai ships the encoder path
- [[Concepts/typed-decisions-benchmark-ollaya]] — `laya:typed-decisions` tops the benchmark
- [[Concepts/calibration-for-decision-models]] — temperature fitting is part of the laya story

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
- HF org: https://huggingface.co/convaiinnovations
