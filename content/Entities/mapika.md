---
title: "Mapika"
details: "Organization behind the decider decoder decision-model family on Hugging Face (Apache-2.0), built on Qwen3.5 base models."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-decider-2026-09-26.md
---

# Mapika

**Category:** Company / Organization
**Repository:** https://huggingface.co/Mapika

## Overview

Mapika is the author organization behind the **decider** decision-model family. They publish decoder-based decision models under Apache-2.0, built on Qwen3.5 (`Qwen3.5-0.8B` and `Qwen3.5-2B`). Decider is the only decoder (generative-backbone) family in the Ollaya catalog and is currently the most accurate open decision model Ollaya ships (0.591 on the typed-decisions benchmark for the 2B variant).

## Key Details

- Published models: `decider` 0.8B and 2B (Apache-2.0). HF: https://huggingface.co/Mapika.
- Approach: prompt the Qwen3.5 base with context + question + lettered options, read the next-token logits at an answer slot for option letters, never generate.
- Ollaya runtime widens BF16 weights to fp32 on load; the ONNX graph is only ~8 MB and the weights are pinned to a Hugging Face commit, verified by sha256.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — Mapika ships the decoder path
- [[Concepts/typed-decisions-benchmark-ollaya]] — `decider:2b` is the most accurate non-fine-tuned model

## References

- Raw: [[Raw/ollaya-library-decider-2026-09-26]]
- HF org: https://huggingface.co/Mapika
