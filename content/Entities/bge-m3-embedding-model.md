---
title: "BGE-M3 Embedding Model"

details: "BGE-M3 is BAAI General Embedding v3, a dense text embedding model designed for multilingual, multi-functional, and multi-granularity retrieval. The 'M3' stands for the three properties: Multi-Linguality (100+ languages), Multi-Functionality (dense, lexical, multi-vector retrieval in one model), and Multi-Granularity (short sentences up to 8K-token passages). In Zero-Mem, BGE-M3 is the dense access signal that complements BM25 lexical scoring — both are used for indexing, seeding, and scoring only, never to generate or rewrite memory content. The dense embeddings power the query-entity alignment step (matching query-extracted entities to observed graph entities) and the dense context priors that feed into the Personalized PageRank reset vector."
tags:
  - entities
  - embedding
  - rag
created: 2026-08-05
updated: 2026-08-05
type: entity
source: "[[Raw/arxiv-zero-mem-2026-08-05]]"
sources:
  - "Raw/arxiv-zero-mem-2026-08-05"
---

# BGE-M3 Embedding Model

**Source:** [[Raw/arxiv-zero-mem-2026-08-05]] — Xiao et al., 2026
**Category:** Tool (embedding model)
**Publisher:** BAAI (Beijing Academy of Artificial Intelligence)

## Overview

BGE-M3 (BAAI General Embedding v3) is a dense text embedding model from BAAI designed for multilingual, multi-functional, and multi-granularity retrieval. The name marks its three distinguishing properties: **M**ulti-Linguality (100+ languages), **M**ulti-Functionality (dense, lexical, and multi-vector retrieval fused in a single model), and **M**ulti-Granularity (short sentences up to ~8K-token passages). It is widely used as a drop-in dense encoder for retrieval pipelines that also need lexical and multi-vector signals.

In Zero-Mem, BGE-M3 is the dense access signal that complements BM25 lexical scoring. Both are used for indexing, seeding, and scoring only — never to generate or rewrite memory content, which keeps them on the correct side of the zero-token memory regime.

## Key Details

| Property | Value |
|----------|-------|
| **Publisher** | BAAI (Beijing Academy of Artificial Intelligence) |
| **Variants** | `BAAI/bge-m3` (HuggingFace), plus GGUF / ONNX community ports for CPU and edge inference |
| **Max input length** | 8,192 tokens |
| **Output dimension** | 1,024 (default dense vector) |
| **Functions** | Dense retrieval, lexical (sparse) retrieval, multi-vector (ColBERT-style) retrieval — all from the same model |
| **Languages** | 100+ |

## Role in Zero-Mem

Two specific uses in the paper's pipeline:

1. **Query-entity alignment.** The graph view aligns each query-extracted entity ê with the most similar observed graph entity e by cosine similarity: `η0(e | q) = cos(e, ê)`, with e = `argmax(e' ∈ Ve) cos(e', ê)`. This requires a dense encoder; BM25 alone cannot do semantic alignment.
2. **Dense context priors.** The propagated entity activations are combined with dense context match scores `sim(q, z)` to form the Personalized PageRank reset vector `rq`. Without dense priors, the graph would depend on observed co-occurrence only and miss purely semantic matches.

The dense signals support indexing, seeding, and scoring. They never generate or rewrite memory content — that distinction is what keeps BGE-M3 within the zero-token regime. An embedding model is an encoder, not a generator, and is therefore permitted even though it is a neural model.

## Why BGE-M3 Specifically

- **Multi-granularity** matches the hierarchical trace units (turn / window / episode / local span) cleanly — the same model can embed all four granularities.
- **Multi-functionality** lets a single checkpoint serve both the dense cosine step and a lexical sparse signal, simplifying the stack.
- **Multilingual** matters for agent memory systems that cross language boundaries (the paper's authors are based in China, and the model has 100+ language coverage).

A functionally equivalent alternative would be `BAAI/bge-large-en-v1.5` for English-only, or `intfloat/e5-large-v2` for a different dense baseline. The choice of BGE-M3 is not load-bearing for the paper's argument — any reasonable dense encoder that supports multi-granularity inputs would work.

## How It Differs from a Generation Model

BGE-M3 is an *encoder*. Given an input text, it returns a fixed-size vector. It does not produce text, and it does not have an instruction-following capability. This is why its use does not break the zero-token regime: the regime forbids LLM calls (and LLM input/output tokens) outside the final reader, and an embedding model is not an LLM by the standard definition.

The line can blur with generative embedding models that also produce text (e.g. some LLM-based retrievers that generate pseudo-queries). If a system uses such a model to produce text as part of memory operation, it has left the zero-token regime, even if the model is technically an "embedding model".

## Related Concepts

- [[Concepts/zero-token-memory-operations]] — the operating regime BGE-M3 supports without violating
- [[Concepts/dual-view-evidence-retrieval]] — the retrieval design that uses BGE-M3 for the dense context priors
- [[Concepts/provenance-preserving-memory-substrate]] — the substrate BGE-M3 indexes without rewriting
- [[Concepts/agent-memory-layer-patterns]] — the broader memory landscape BGE-M3 typically appears in

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- Paper: [[Papers/zero-mem-zero-token-agent-memory]]
- arXiv: https://arxiv.org/html/2607.29377v1
- Model card: https://huggingface.co/BAAI/bge-m3
