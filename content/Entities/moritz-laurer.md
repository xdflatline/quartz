---
title: "Moritz Laurer"
details: "Researcher behind the DeBERTa-v3-large and ModernBERT-large zero-shot NLI classifiers that Ollaya ships as the nli family; trained on NLI data with hypothesis-template recommendations."
tags:
  - entity
  - llm
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/ollaya-library-nli-2026-09-26.md
---

# Moritz Laurer

**Category:** Person / Researcher
**Repository:** https://huggingface.co/MoritzLaurer

## Overview

Moritz Laurer is the author of the zero-shot NLI classifiers that Ollaya ships as the `nli` family. His DeBERTa-v3-large variant (`nli:deberta-v3-large`, MIT) scores 0.548 on Ollaya's typed-decisions benchmark — the highest-accuracy **encoder** model in the catalog — and his ModernBERT-large variant (`nli:modernbert-large`, Apache-2.0) is the only NLI option Ollaya ships without non-commercial training-data license concerns.

## Key Details

- Published models: zero-shot NLI classifiers (DeBERTa-v3-large, ModernBERT-large). HF: https://huggingface.co/MoritzLaurer.
- Approach: treat each option as a hypothesis and score entailment against the state; choice / score questions take the most-entailed option, yes/no (`noul`) questions take the entailment probability.
- Hypothesis templates come from Laurer's recommended phrasing for each backbone.
- Note: part of DeBERTa's training data carries non-commercial licenses; Laurer publishes a `-c` variant trained on commercially-usable data only, which Ollaya does not ship yet.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — Laurer's classifiers are the canonical zero-shot NLI path
- [[Concepts/decision-models-as-classifiers]] — what "decision model" means
- [[Concepts/typed-decisions-benchmark-ollaya]] — 0.548 vs siblings
- [[Concepts/calibration-for-decision-models]] — calibration caveat

## References

- Raw: [[Raw/ollaya-library-nli-2026-09-26]]
- HF author org: https://huggingface.co/MoritzLaurer
