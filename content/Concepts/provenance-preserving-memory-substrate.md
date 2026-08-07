---
title: "Provenance-Preserving Memory Substrate"

details: "A provenance-preserving memory substrate is one in which no step generates an intermediate representation of the past. Traces are stored verbatim, and every retrieval structure (graph, hierarchy, dense index) is derived from them without rewriting or summarizing their content. Each derived unit carries a back-pointer to its original trace unit (source identifier, session time, boundary identifier, speaker, tool observation, timestamp), so retrieved evidence is always traceable to the observed interaction. This is the substrate that makes the zero-token operating regime possible: if no step rewrites the past, there is no opportunity for omission, merging, or hallucinated detail. It is also what enables deterministic calibration — every filter and rank operation can reason about provenance, boundary, and compatibility with the query without consulting an LLM."
tags:
  - concepts
created: 2026-08-05
updated: 2026-08-05
type: concept
sources:
  - "Raw/arxiv-zero-mem-2026-08-05"
---

# Provenance-Preserving Memory Substrate

**Source:** [[Raw/arxiv-zero-mem-2026-08-05]] — Xiao et al., 2026 ([arXiv:2607.29377](https://arxiv.org/html/2607.29377v1))
**Category:** Architecture Pattern
**Status:** Proposed best practice (foundational to Zero-Mem's empirical result)

## Overview

A memory architecture in which the original interaction traces are the source of record, and every retrieval structure (graph, hierarchy, dense index) is *derived* from them without rewriting or summarizing their content. Each derived unit carries a back-pointer to its original trace — source identifier, session time, boundary identifier, speaker, tool observation, timestamp — so retrieved evidence is always traceable to the observed interaction.

The substrate is the foundation that makes the zero-token operating regime possible. If no step rewrites the past, there is no opportunity for omission, merging, or hallucinated detail. It is also what enables deterministic calibration: every filter and rank operation can reason about provenance, boundary, and compatibility with the query without consulting an LLM.

## What the Substrate Preserves

| Property | Why it matters |
|----------|----------------|
| **Original text** | Retrieved evidence can be quoted verbatim in the final answer or directly inspected by the reader |
| **Source identifier** | Every unit can be traced back to a specific trace position (turn id, message id, document id) |
| **Session time** | Temporal reasoning can use the actual occurrence time, not a derived "approximate" timestamp |
| **Boundary identifier** | Session boundaries (and any other operational boundaries) are preserved as first-class metadata |
| **Speaker / role** | User, assistant, tool, and system messages stay distinguishable — no narrative voice collapse |
| **Tool observations** | Tool outputs are stored as observed, not rewritten into natural-language summaries |
| **Entity mentions as observed** | The graph records that entity e was detected in context di, not that "e is related to di" via a generated relation |

## What the Substrate Excludes

| Excluded | Why |
|----------|-----|
| **LLM-generated summaries** | Summarization can drop, merge, or invent details. The substrate has no place to put them — traces are the source. |
| **LLM-generated triples** | The graph records observed co-occurrence, not inferred relations. `subject–relation–object` extraction by an LLM is a no-go. |
| **LLM-generated embeddings of summaries** | Only the original trace text is embedded. If a summary is later generated, it cannot be embedded as if it were a trace. |
| **Rewrites by the reader's LLM** | The reader can paraphrase retrieved evidence in its answer, but the substrate cannot be mutated by the reader. |
| **Provenance loss on derived units** | Every unit carries a back-pointer. A derived unit without a back-pointer is a bug. |

## How the Substrate is Built (Zero-Mem's Case)

### Trace Storage

Each interaction trace si contains user messages, assistant responses or actions, tool observations, timestamps, speakers, and session metadata. The history H = (s1, ..., sT) is the source of record.

### Entity–Context Graph

Apply non-generative NER (e.g. spaCy) to each context unit. Construct the observed entity–context graph G = (Vd ∪ Ve, Ede ∪ Edd):

- Vd = context nodes (one per context unit)
- Ve = entity nodes (one per distinct detected entity)
- Ede = entity–context co-occurrence edges, weighted by normalized occurrence frequency
- Edd = adjacency edges between neighboring context units

Edge weights come from observed co-occurrence counts. They are not LLM-extracted relations.

### Hierarchical Trace Units

Organize the same trace units at four granularities, all preserving the same back-pointers:

- **Turns** = atomic utterances
- **Windows** = short-range context (a few turns)
- **Episodes** = adjacent windows grouped by semantic continuity and available boundaries
- **Local spans** = immediate neighborhood of a candidate turn

The hierarchy is derived, not generated. Episodes come from observable semantic continuity and boundary metadata (e.g. session markers, time gaps), not from an LLM deciding where one event ends and the next begins.

### Lexical and Dense Access Signals

BM25 (lexical statistics) and BGE-M3 (dense embeddings) are computed over the original trace units. The encoders are non-generative and do not count against the LLM budget. They are used for indexing, seeding, and scoring only.

## The Back-Pointer Discipline

Every retrieval structure must be able to answer two questions for any node, edge, or unit it exposes:

1. **Which trace did this come from?** A specific source identifier (turn id, message id, document id).
2. **What part of that trace?** A position, span, or character range.

If either answer is "we don't know", the unit is not provenance-preserving and must be discarded or rebuilt. The discipline is what enables the deterministic calibration in Zero-Mem: Filter(C(q), φ(q)) can drop any unit that fails a provenance or boundary check, because every unit carries the metadata needed to make that check.

## Why This Substrate Matters

- **Zero-token operation.** Without generated intermediates, the memory pipeline never needs an LLM. The reader is the only LLM call.
- **Traceable answers.** Every claim the reader makes can be checked against the source traces. If a claim is not supported, the deterministic answer calibration can drop or replace it.
- **Robust to model drift.** Generated memory depends on the generator's behavior — change the generator and the memory changes. Provenance-preserving memory does not.
- **Reproducibility.** Two runs over the same history produce the same evidence set, because no step is stochastic.
- **Auditability.** Every retrieved unit can be inspected as the original text, with all its context. There is no abstraction layer to reverse-engineer.

## When to Use This Substrate

- **Long-term agent memory** where the user can come back days later and ask "what did I say about X last month" — exact retrieval matters.
- **Compliance-sensitive domains** where every retrieved claim must be traceable to an observed interaction (legal, medical, financial).
- **Multi-session conversations** where the same entity reappears in distant sessions and disambiguation between sessions matters.
- **High-stakes QA** where hallucinated memory is more dangerous than incomplete memory.

A provenance-preserving substrate is overkill when:

- The memory is ephemeral (single-session chatbot) — no need to preserve provenance.
- The reader's context window fits the whole history — no memory system needed.
- The system tolerates generated abstractions (e.g. ambient summarization for UI display) — but then it is not provenance-preserving and should not claim to be.

## Related Concepts

- [[Concepts/zero-token-memory-operations]] — the operating regime this substrate enables
- [[Concepts/dual-view-evidence-retrieval]] — the retrieval design that operates over this substrate
- [[Concepts/ai-content-provenance]] — the broader concept of provenance in AI-generated content
- [[Concepts/observational-memory-pattern]] — a different non-generative memory pattern that *does* generate intermediate notes
- [[Concepts/agent-memory-layer-patterns]] — broader agent memory landscape

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- Paper: [[Papers/zero-mem-zero-token-agent-memory]]
- arXiv: https://arxiv.org/html/2607.29377v1
