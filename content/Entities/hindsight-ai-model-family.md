---
title: "Hindsight reranker and embedding models (hs-rerank-1, hs-embed-1)"
details: "Hindsight's two retrieval models for agent memory: hs-rerank-1 (114M, MIT, built on mmBERT-small) orders memories by relevance and can drop irrelevant documents; hs-embed-1 (112M, MIT) produces 384-dimension vectors. Both cover eight languages, ship int8 ONNX exports, run viably on CPU, and are benchmarked against open rerankers up to 278M and embedders up to 118M respectively."
tags:
  - entity
  - memory
  - embedding
  - inference
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Hindsight reranker and embedding models (hs-rerank-1, hs-embed-1)

**Category:** Model family (open weights)
**Vendor:** [[Entities/vectorize]] / Hindsight
**Status:** Released 2026-11; MIT license

## Overview

The retrieval half of the [[Concepts/purpose-built-memory-model-stack|memory model stack]]. Where `hs-decide-1-flash` judges, these two encode and order: one decides which memories are relevant, the other decides which memories are near each other in meaning.

## hs-rerank-1

- **Function:** orders documents by relevance to a query; can also drop irrelevant documents (the same pruning operation recall applies — see [[Concepts/recall-time-prune-and-dedup]]).
- **Parameters:** 114M
- **Base:** `jhu-clsp/mmBERT-small`
- **License:** MIT
- **Context:** 8,192 tokens
- **Benchmarks:** compared against open rerankers up to 278M parameters on seven benchmarks — English (NanoBEIR, BRIGHT), multilingual (MIRACL plus 26 tasks in eight languages) and memory (KnowMeBench, MemBench, ConvoMem). Metric is nDCG@10.
- **Speed:** median time to rerank 50 memories on two CPU threads.

## hs-embed-1

- **Function:** turns text into 384-dimension vectors.
- **Parameters:** 112M
- **Base:** `hotchpotch/bekko-embedding-v1-a25m`
- **License:** MIT
- **Context:** 8,192 tokens
- **Benchmarks:** compared against open embedders up to 118M parameters on twelve benchmarks — English and multilingual retrieval, long conversations (BEAM), long documents (LongEmbed) and memory retrieval (LMEB). The vendor notes the fair comparison is with multilingual models; English-only models are listed because they are common defaults.
- **Speed:** median time per query on two CPU threads.

## Deployment

- Both run 15M- and 13M-parameter transformers per pass (most of their weights are the vocabulary table), so they are fast on CPU.
- Both ship **int8 ONNX** exports and serve on Text Embeddings Inference as-is.
- Self-hosted Hindsight can run them locally inside the API process:

```bash
export HINDSIGHT_API_RERANKER_PROVIDER=local
export HINDSIGHT_API_RERANKER_LOCAL_MODEL=hindsight-ai/hs-rerank-1
export HINDSIGHT_API_EMBEDDINGS_PROVIDER=local
export HINDSIGHT_API_EMBEDDINGS_LOCAL_MODEL=hindsight-ai/hs-embed-1
```

- Hosted, they are available through [[Entities/hindsight-inference]] at `POST /v1/rerank` and `POST /v1/embeddings`.
- **Migration constraint:** a bank's stored vectors must be re-embedded to switch embedding models — the embedding model is part of the bank's persisted state, not a swappable request parameter.

## Language coverage

English, Spanish, French, German, Portuguese, Japanese, Korean and Chinese — the same eight languages as the decision model.

## Related

- [[Concepts/purpose-built-memory-model-stack]] — the pattern these models instantiate
- [[Entities/hs-decide-1-flash]] — the judgment model in the same release
- [[Entities/hindsight-inference]] — hosted endpoints
- [[Entities/bge-m3-embedding-model]] — a general-purpose multilingual embedder, for comparison

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Weights: https://huggingface.co/hindsight-ai
- Benchmarks: https://benchmarks.hindsight.vectorize.io/models
