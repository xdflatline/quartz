---
title: "hs-decide-1-flash"
details: "Hindsight's 0.8B open-weight decision model (Apache 2.0), built on Qwen3.5-0.8B, that answers typed judgments about memories and facts in a single pass — a choice with per-option probabilities, a point on a scale, or the likelihood a statement holds. Serves the same System One request shape as TypeSafe's Jev, takes 167 ms at the median per request, and costs $0.02 per million input tokens through Hindsight Inference."
tags:
  - entity
  - llm
  - memory
  - inference
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# hs-decide-1-flash

**Category:** Model (open weights)
**Vendor:** [[Entities/vectorize]] / Hindsight
**Status:** Released 2026-11 with Hindsight Inference; Apache 2.0

## Overview

`hs-decide-1-flash` is a 0.8B-parameter decision model trained on the judgments Hindsight makes while operating a memory bank. It does not generate text: it takes a state plus a typed question and returns a structured answer.

## Specifications

- **Parameters:** 0.8B
- **Base model:** `Qwen/Qwen3.5-0.8B`
- **License:** Apache 2.0
- **Context:** 65,536 tokens
- **Output types:** choice with a probability per option, a score on a scale, or a likelihood that a statement holds
- **Languages:** English, Spanish, French, German, Portuguese, Japanese, Korean, Chinese
- **Serving:** vLLM with the plugin in the model repository's `serving/` folder

## Interface compatibility

It accepts the same **System One** requests as TypeSafe's Jev, so an application written for one runs on the other by changing the model name. Through [[Entities/hindsight-inference]] it is a drop-in for the System One API at `POST /v1/systemone` ($0.02 per million input tokens). The same model can also be used through the Cohere-Rerank-compatible `/v1/rerank` endpoint to rerank **and** drop irrelevant documents ($0.02 per million input tokens).

## Where it is used

Inside Hindsight 1.2 it is consulted at four points — recall pruning/deduplication, reflect evidence trimming and sufficiency, consolidation triage, and knowledge-page change-impact. See [[Concepts/decision-model-as-memory-judge]] for the pattern and its instances.

## Reported performance

- **167 ms** median per request, **350 ms** at p90 — versus 1–7 s median for the LLM call it replaces.
- **All-Hindsight quality mean:** 75.6 across eight benchmarks, against 74.5 (`StartLux-Decision 0.8B Instant`), 73.4 (`d3-lite`), 66.6 (`decider-0.8b`).
- **Memory-specific judgments:** 79.5 on whether a new memory changes a page (others 56.0–72.0); 89.4 on skipping refreshes that would change nothing (others 45.0–78.3).
- **General decision benchmarks trail:** Decision Index 36.1 vs 53.8; dialogue inference 75.8 vs 83.0–88.0.

These are vendor-run figures; see the boundaries section of [[Research/decision-gated-agent-memory]].

## Related

- [[Concepts/purpose-built-memory-model-stack]] — the stack this model leads
- [[Concepts/decision-models-as-classifiers]] — the general pattern and question types
- [[Entities/hindsight-ai-model-family]] — the reranker and embedder released alongside
- [[Entities/hindsight-inference]] — hosted API

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Weights: https://huggingface.co/hindsight-ai/hs-decide-1-flash
- Benchmarks: https://benchmarks.hindsight.vectorize.io/models/decision
