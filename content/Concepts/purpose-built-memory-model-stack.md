---
title: "Purpose-built memory model stack (decide, rerank, embed)"
details: "Agent memory gets its own small-model suite rather than borrowing general-purpose infrastructure: a 0.8B decision model for typed judgments, a 114M reranker, and a 112M embedding model, all multilingual across eight languages and viable on CPU. The pattern is task-shaped weights — models trained on memory judgments beat larger general models on memory benchmarks while trailing them on general decision benchmarks."
tags:
  - concept
  - memory
  - embedding
  - local-llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Purpose-built memory model stack (decide, rerank, embed)

**Category:** Model Architecture / Infrastructure Pattern
**Status:** Open weights released 2026-11 (Apache 2.0 / MIT)

## Overview

Agent memory has been assembled from general-purpose parts: a chat LLM for every judgment, a document reranker for relevance, a document embedding model for similarity. Each of those parts is trained for a different workload. The pattern here is to ship a **three-model stack shaped to memory operations** instead.

## The stack

| Role | Model | Params | Base | License | Context |
|---|---|---|---|---|---|
| Judgment | `hs-decide-1-flash` | 0.8B | `Qwen/Qwen3.5-0.8B` | Apache 2.0 | 65,536 |
| Rerank | `hs-rerank-1` | 114M | `jhu-clsp/mmBERT-small` | MIT | 8,192 |
| Embed | `hs-embed-1` | 112M | `hotchpotch/bekko-embedding-v1-a25m` | MIT | 8,192 |

- **Decision** answers typed questions in one pass and serves on vLLM with a plugin in its repository's `serving/` folder.
- **Rerank** orders documents by relevance and carries a pruning mode ("drop irrelevant documents") that is the same operation recall uses.
- **Embed** produces 384-dimension vectors.

## Properties the pattern depends on

- **Multilingual by default.** All three work in English, Spanish, French, German, Portuguese, Japanese, Korean and Chinese — eight languages, which is a memory-locality property, not a nice-to-have.
- **CPU-viable.** The reranker and embedder run 15M- and 13M-parameter transformers per pass (most weights are the vocabulary table), ship int8 ONNX exports, and serve on Text Embeddings Inference as-is. The reranker benchmarks 50 memories on two CPU threads.
- **Non-generative pricing.** None of the three generates text, so billing is input tokens only — the structural reason the economics in [[Concepts/decision-model-cost-leverage]] work.
- **Interchangeable interface.** The decision model accepts the same System One requests as TypeSafe's Jev, so swapping is a model-name change.

## The specialization trade

The vendor's own benchmark table is unusually candid: `hs-decide-1-flash` leads on **memory judgments** — whether a new memory changes a page (79.5 vs 56.0–72.0) and whether a refresh would change anything (89.4 vs 45.0–78.3) — but trails on **general decision benchmarks**:

| Benchmark | `hs-decide-1-flash` | Best comparison |
|---|---|---|
| Mean over 8 benchmarks | 75.6 | 74.5 / 73.4 / 66.6 |
| Decision Index | 36.1 | 53.8 (StartLux) |
| Dialogue inference | 75.8 | 83.0 (StartLux) / 88.0 (`d3-lite`) |

This is the signature of task-shaped training: the model is excellent exactly where it will be used and mediocre where it will not. It is a deliberate scope choice, and a warning against reading a single benchmark mean as a general capability score.

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]] — what the decision model does in the pipeline
- [[Concepts/decision-model-cost-leverage]] — why non-generative pricing matters
- [[Concepts/recall-time-prune-and-dedup]] — the operations that need a good reranker and embedder
- [[Concepts/encoder-vs-decoder-decision-architectures]] — where this model sits in the architecture space
- [[Concepts/onnx-decision-runtime-parity]] — the CPU/ONNX deployment concern

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Entities: [[Entities/hs-decide-1-flash]], [[Entities/hindsight-ai-model-family]], [[Entities/hindsight-inference]]
- Weights: https://huggingface.co/hindsight-ai
