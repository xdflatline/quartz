---
title: "Zero-Token Memory Operations"
detail: "An operating regime for agent memory in which every step outside final question answering uses zero LLM calls and zero LLM input or output tokens, isolating the LLM cost to the reader."
details: "Zero-token memory operations (formalized in Zero-Mem, Xiao et al., 2026) define an operating regime in which memory construction, organization, routing, retrieval, evidence closure, pre-reader evidence calibration, and post-reader answer calibration all run without invoking an LLM. Only the final reader — the LLM that produces the answer from the evidence set R(q) — may use an LLM. Encoder computation (BM25, dense embeddings) and final-QA inference are accounted for separately. The regime separates memory-operation cost from final-reader cost, which is a useful architectural split: the memory pipeline can be optimized deterministically (no token budget, no rate limits, no model drift) while the reader is the only component exposed to LLM cost and variability. The empirical result motivating the regime: on LoCoMo and HotpotQA, Zero-Mem achieves the best F1 and BLEU-1 of eight compared systems while consuming 0 LLM tokens for memory operations and reducing memory-operation latency by 57.6% versus the fastest LLM-using baseline (LightMem)."
tags:
  - concepts
created: 2026-08-05
updated: 2026-08-05
type: concept
sources:
  - "Raw/arxiv-zero-mem-2026-08-05"
---

# Zero-Token Memory Operations

**Source:** [[Raw/arxiv-zero-mem-2026-08-05]] — Xiao et al., 2026 ([arXiv:2607.29377](https://arxiv.org/html/2607.29377v1))
**Category:** Architecture Constraint
**Status:** Active research area (empirically validated by Zero-Mem on LoCoMo + HotpotQA)

## Overview

An operating regime for agent memory in which every step outside final question answering uses zero LLM calls and zero LLM input or output tokens. The only LLM-dependent stage is the reader that maps the evidence set R(q) to the answer. Encoder inference (BM25, dense embeddings), memory organization, retrieval, fusion, closure, and calibration are all non-generative. The regime is a budget rule, not a single architecture: any system that confines its LLM calls to the final reader qualifies, regardless of which retrieval or graph algorithms it uses internally.

## The Definition

A memory system operates in the zero-token regime if, for every query q and history H:

1. Construction, organization, routing, retrieval, closure, and both pre-reader evidence calibration and post-reader answer calibration invoke no LLM.
2. No step outside the final reader consumes LLM input or output tokens.
3. Encoder computation (lexical statistics, dense embeddings) and final-QA inference are accounted for separately and are not part of the memory-operation cost.

The split is useful because it lets a system optimize two budgets independently: a deterministic budget (CPU/GPU cycles for non-generative operations) and an LLM budget (input/output tokens, model latency, model cost).

## Why It Matters

- **Cost isolation.** Memory operations can be scaled horizontally without LLM rate limits or per-token pricing. The reader is the only component exposed to LLM economics.
- **Reproducibility.** Non-generative steps are deterministic given the same input. Two runs of the same memory pipeline over the same history produce the same evidence set, which is not true for any pipeline that uses an LLM intermediate.
- **Provenance.** Because no step generates an intermediate representation of the past, retrieved evidence remains traceable to the original interaction traces. There is no abstraction layer that can drop, merge, or invent details.
- **Latency floor.** Removing LLM calls removes the dominant memory-operation latency. Zero-Mem reports 0.22 s per query and a 57.6% reduction versus the fastest LLM-using baseline (LightMem).

## What the Regime Excludes

| Excluded from memory operations | What it must NOT do |
|---------------------------------|---------------------|
| LLM-generated summaries | No abstractive compression of past interactions |
| LLM-generated graph triples | No `subject–relation–object` extraction via an LLM |
| LLM-generated embeddings | Wait — embeddings are allowed. Embedders are encoders, not generators. The LLM budget is for LLMs, not for any neural model. |
| LLM-mediated retrieval reranking | No call to an LLM to re-rank the candidate evidence |
| LLM-mediated answer correction | No call to an LLM to fix a malformed final answer (use deterministic calibration instead) |

## What the Regime Includes

- Non-generative NER (e.g. spaCy) for entity extraction.
- BM25 and dense encoders (e.g. BGE-M3) for indexing and scoring.
- Graph algorithms: Personalized PageRank, BFS, community detection.
- Hierarchical descent: episode → window → turn → local span.
- Score normalization, fusion, deduplication.
- Deterministic calibration: filter by hard constraints (provenance, boundary), rank by compatibility signals, replace scalar answers only with a unique type-compatible evidence candidate.

## Comparison With Other Memory Regimes

| System | Memory-op LLM calls | Tokens for memory ops | Notes |
|--------|---------------------|------------------------|-------|
| Mem0 / Mem0g | Yes (add/update/delete/no-op) | Large | LLM tool calls for memory updates |
| A-Mem | Yes (Zettelkasten note generation) | Large | LLM produces structured notes |
| LightMem | Yes (small LM consolidation) | Moderate | Small LM shifts the cost but does not eliminate it |
| SimpleMem | Yes (semantic compression + intent planning) | Moderate–Large | Intent-aware retrieval planning is generative |
| CompassMem | Yes (event-graph construction) | Moderate | Event-centric graph built with LLM extraction |
| GAM | Yes (JIT task-specific context) | Large | Online deep research uses LLM |
| **Zero-Mem** | **No** | **0** | Final reader is the only LLM call |

## How to Adopt the Regime

1. **Pick a non-generative access signal.** BM25 + a dense encoder is the canonical pair. The encoder is not an LLM and does not count against the budget.
2. **Build non-generative retrieval structures.** Two complementary views is a good default: a relational view (entity–context graph) and a temporal view (turn / window / episode / local). Each has distinct failure modes the other covers.
3. **Route between views deterministically.** A lightweight profile φ(q) = {subject, keywords, answer-type, temporal-cues, boundary} is enough to choose which view is primary. Globally shared primary-view weight ρ around 0.6 is a sensible default.
4. **Calibrate deterministically.** Filter on hard constraints (provenance, boundary), then rank by compatibility (subject, temporal, answer-type). For answer forms admitting deterministic checks, replace a scalar answer only with a unique type-compatible candidate.
5. **Reserve the LLM for the reader.** A single final-QA call over the evidence set is the only LLM invocation in the whole pipeline.

## Failure Modes Without the Regime

The paper's central critique of generated memory is that omissions, merges, and blurred temporal updates weaken traceability to the original interaction. Systems that summarize or graph-construct with an LLM can lose:

- Specific named entities (merged with similar entities by the LLM)
- Exact dates, numbers, and quoted expressions (smoothed over by the LLM)
- Temporal ordering across sessions (compressed into a single "summary" block)
- Speaker attribution (collapsed into a single narrative voice)

The zero-token regime forces all of these to be preserved as part of the original trace, which is then the source of record.

## Related Concepts

- [[Concepts/dual-view-evidence-retrieval]] — the retrieval design that operationalizes the regime in Zero-Mem
- [[Concepts/provenance-preserving-memory-substrate]] — the trace-as-source-of-record substrate that makes the regime possible
- [[Concepts/deterministic-first-architecture]] — the broader design philosophy: deterministic code first, LLM as a small upgrade
- [[Concepts/observational-memory-pattern]] — a different non-generative memory pattern using two background agents, not zero
- [[Concepts/agent-memory-layer-patterns]] — the broader landscape of agent memory systems

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- Paper: [[Papers/zero-mem-zero-token-agent-memory]]
- arXiv: https://arxiv.org/html/2607.29377v1
