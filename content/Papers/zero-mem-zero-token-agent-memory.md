---
title: "Zero-Mem: Zero-Token Memory Operations for LLM Agents"
detail: "Provenance-preserving agent memory where every operation outside final question answering invokes no LLM and consumes no LLM tokens."
details: "Zero-Mem (Xiao et al., 2026) reformulates agent memory as structured evidence selection over original interaction traces rather than generated abstractions. It builds two non-generative views — an entity–context graph (co-occurrence + adjacency) and a temporal hierarchy (turns, windows, episodes, local spans) — and uses BM25 + BGE-M3 only for indexing and scoring. A lightweight query profile routes between relational and local views, retrieval is fused, evidence closure adds relational bridges and local neighbors, and deterministic calibration filters and re-ranks without invoking an LLM. Only the final-QA reader uses an LLM. The paper defines an operating regime called zero-token memory operations: construction, organization, routing, retrieval, closure, and both pre- and post-reader calibration incur zero LLM calls and zero LLM input or output tokens. Encoder computation is accounted for separately. On LoCoMo and HotpotQA (56K–448K tokens), Zero-Mem beats GAM, A-Mem, Mem0, MemoryOS, LightMem, SimpleMem, and CompassMem on F1 and BLEU-1 while consuming 0 LLM tokens for memory operations and reducing memory-operation latency by 57.6% versus LightMem."
tags: [research]
source: https://arxiv.org/html/2607.29377v1
created: 2026-08-05
updated: 2026-08-05
type: article
---

**Authors:** Yilin Xiao, Zhehan Zhu, Yujing Zhang, Jin Chen, Zijin Hong, Luyao Zhuang, Qinggang Zhang, Shengyuan Chen, Xiaocao Ouyang, Lingfei Ren, Xiao Huang
**Published:** 2026 (arXiv preprint, code to be released after peer review)
**Link:** https://arxiv.org/html/2607.29377v1
**Code (pending):** https://github.com/TheMoon0815/Zero-mem

---

## Overview

Zero-Mem challenges the dominant assumption in agent memory design — that an LLM must mediate between raw interaction history and the final reader. Existing systems like Mem0, A-Mem, LightMem, and SimpleMem all retain at least one generative step (summarization, reflection, structured extraction, intent-aware planning) that adds recurring token and time cost and obscures original evidence through omission or merging. Zero-Mem asks a sharper question: can structured memory access be entirely non-generative, with the LLM reserved for final question answering?

The answer is yes. By treating the original interaction traces as the source of record and deriving two non-generative, complementary views over them, Zero-Mem achieves competitive performance on long-memory and long-context benchmarks while reducing memory-operation latency by 57.6% versus the fastest baseline (LightMem) and consuming zero LLM tokens for memory operations.

## Core Contributions

1. **Zero-token agent memory regime** — formal operating regime in which every step outside final QA uses zero LLM calls and zero LLM input or output tokens, separating memory-operation cost from final-reader inference.
2. **Provenance-preserving framework** — coordinates a relational view (entity–context graph) and a temporally ordered view (turns / windows / episodes / local spans) to perform structured evidence selection directly over original interaction traces.
3. **Empirical validation** — beats all seven memory-based baselines on LoCoMo and HotpotQA under identical final-QA readers and context budgets, while consuming zero LLM tokens for memory operations.

## Architecture

Zero-Mem is built from four components, all of which run without LLM calls:

| Component | Function | Key Mechanisms |
|-----------|----------|----------------|
| **Provenance-preserving Token-Free Memory Substrate** | Build non-generative retrieval structures over raw traces | NER-based entity–context graph (e.g. spaCy), hierarchical trace units (turn / window / episode / local), BM25 + BGE-M3 indexing |
| **Query-Conditioned Evidence Routing** | Coordinate graph vs. hierarchy based on query structure | Profile φ(q) = {subject, keywords, answer-type, temporal-cues, boundary}; deterministic routing to {relational, local} |
| **Dual-View Evidence Retrieval and Closure** | Retrieve and supplement from both views | Personalized PageRank on graph, coarse-to-fine hierarchical descent, query-wise score normalization, fusion with coefficient ρ, closure adds Ng + Nh |
| **Deterministic Evidence Calibration** | Filter and re-rank without an LLM | Hard-constraint filter on provenance and boundary, then rank by subject / temporal / answer-type compatibility; scalar answers can be replaced only by a unique type-compatible candidate |

### Memory Substrate Details

**Relational trace graph.** G = (Vd ∪ Ve, Ede ∪ Edd). Vd are context nodes, Ve are entity nodes. Ede carries entity–context co-occurrence edges weighted by normalized occurrence frequency. Edd carries adjacency edges between neighboring context units. Edges are observed, not generated — no LLM-extracted triples or inferred relations.

**Hierarchical trace units.** T(H) = Uturn ∪ Uwindow ∪ Uepisode ∪ Ulocal. Turns preserve atomic utterances; windows retain short-range context; episodes group adjacent windows into coherent event regions by semantic continuity and available temporal or session boundaries; local spans preserve the immediate neighborhood of a candidate turn. All units inherit provenance from raw traces.

**Access signals.** BM25 (lexical) + BGE-M3 (dense) for indexing, seeding, and scoring only. They never generate or rewrite memory content.

### Query-Conditioned Evidence Routing

φ(q) = {subject, keywords, answer-type, temporal-cues, boundary} is built from query + metadata without gold answers. Route(q) ∈ {relational, local} chooses graph priority or hierarchy priority based on question form, temporal/aggregation requirements, and subject-anchor availability. Both views are always executed; routing controls their relative fusion weights. Globally shared primary-view weight ρ = 0.6.

### Dual-View Evidence Retrieval

**Graph view.** Align each query-extracted entity ê with the most similar observed graph entity e via cosine similarity. Propagate activation through co-occurrence (Eq. 9 in the paper), combine with dense context priors into a reset vector rq, then run Personalized PageRank with damping γ = 0.6. PageRank values on context nodes form the graph ranking. Exact lexical/phrase matches refine for names, dates, values, titles, quoted expressions.

**Hierarchical view.** Coarse-to-fine: Uepisode → Uwindow → Uturn → Ulocal. Each unit is scored by semantic relevance plus structural compatibility (subject consistency, temporal validity, boundary consistency, expected answer type, lexical/phrase support). Local spans are added when a selected turn depends on nearby information.

### Dual-View Evidence Closure

Per-view score normalization handles the absent / spread / degenerate cases. Fusion: S_fuse(d) = ρ · Ŝ_primary(d) + (1 − ρ) · Ŝ_secondary(d). Closure: C(q) = Dedup(M(q) ∪ Ng(M(q)) ∪ Nh(M(q))) — adds graph-ranked contexts with relational/bridging support (Ng) and neighboring turns or local spans (Nh). Duplicates merged by unit identifier or source provenance.

### Deterministic Evidence Calibration

R(q) = Rank_{φ(q)}(Filter(C(q), φ(q))). Hard constraints filter; compatibility signals rank. The reader produces a0 from R(q). For answer forms admitting deterministic checks, A(q) = Extract(R(q), φ_type(q)) collects evidence-local candidates and a = Calibrate(a0, q, A(q), R(q), φ(q)) preserves a0 when supported, or applies evidence-preserving normalization, extractive shortening, or item-wise list pruning. A scalar answer is replaced only by a unique type-compatible candidate in A(q).

## Methodology (Experiments)

- **Datasets.** LoCoMo (single-hop, multi-hop, temporal, open-domain) and HotpotQA curated memory variant (56K, 224K, 448K tokens).
- **Baselines.** Memory-free: LONG-LLM, RAG. Memory-based: A-Mem, Mem0, MemoryOS, LightMem, SimpleMem, CompassMem, GAM.
- **Readers.** GPT-4o-mini (closed) and Qwen2.5-14B-Instruct (open), held constant across all methods.
- **Settings.** γ = 0.6, ρ = 0.6, top-5 retrieved items, NVIDIA RTX 4090 GPUs.
- **Metrics.** F1, BLEU-1, memory-operation time and LLM tokens.

## Results

### LoCoMo (Average F1 / BLEU-1)

Zero-Mem achieves the best average F1 and BLEU-1 under both readers. Versus GAM (the strongest baseline):

| Reader | Δ F1 | Δ BLEU-1 |
|--------|------|----------|
| GPT-4o-mini | +5.40 | +5.45 |
| Qwen2.5-14B | +4.87 | +4.86 |

With Qwen2.5-14B, Zero-Mem ranks first on every question type and metric. The gap is largest on temporal and open-domain questions, where LONG-LLM and RAG degrade sharply — indicating that long context alone is insufficient for state- and boundary-sensitive recall.

### HotpotQA

Highest F1 across all readers and context lengths (56K / 224K / 448K tokens), including the 448K setting. Average improvement of 5.52 F1 points over the strongest baseline.

### Efficiency

| Method | Memory-op tokens | Total time | Time / query |
|--------|------------------|------------|--------------|
| GAM | (uses LLMs) | — | — |
| LightMem | > 870,000 | — | fastest baseline |
| SimpleMem | (uses LLMs) | — | — |
| **Zero-Mem** | **0** | **334.77 s** | **0.22 s** |

Zero-Mem improves F1 by 10.0% and BLEU-1 by 11.5% versus GAM (the second-best on both metrics) and reduces memory-operation latency by 57.6% versus LightMem. The zero-token regime is therefore not slower despite removing generation.

### Ablations (HotpotQA 56K, GPT-4o-mini)

| Variant | F1 | BLEU-1 |
|---------|-----|--------|
| Full model | 72.07 | 69.66 |
| Graph only | 62.50 | 59.90 |
| Hierarchy only | 54.88 | 51.40 |
| No evidence closure | 67.90 | 65.43 |
| No evidence calibration | 70.13 | 66.45 |

The two views are clearly complementary (graph > hierarchy for cross-document HotpotQA, but both alone are well below the full model), and both closure and calibration add measurable lift.

### Retrieval Budget

Average F1 / BLEU-1 climb from 52.59 / 46.79 at Top-1 to 59.15 / 52.96 at Top-5 and peak at Top-10. Single-hop questions saturate earliest; multi-hop, temporal, and open-domain questions benefit from broader coverage. Top-5 (used in main experiments) trails Top-10 by only 0.65 F1 and 0.83 BLEU-1 with half the primary candidates.

## Key Takeaways

- Generated memory is optional. Structured evidence selection over original interaction traces with non-generative views can match or beat generated-memory pipelines on long-term and long-context QA.
- The bottleneck is LLM cost, not retrieval. Once LLM calls and tokens are removed from memory operations, latency drops by 57.6% versus the fastest LLM-using baseline (LightMem) and total memory-operation time falls to 334.77 s on the full benchmark.
- Graph + hierarchy are complementary. Graph handles cross-document relational evidence (Personalized PageRank over the entity–context graph); hierarchy preserves ordering, temporal locality, and session-level state. Routing between them by query profile (ρ = 0.6 globally) beats either view alone by 10+ F1 points.
- Provenance matters. Every retrieved unit is traceable to its original trace. This eliminates the omission/merging failure mode of generated memory and enables deterministic post-hoc calibration.
- Deterministic calibration is enough. Filter + Rank by subject / temporal / answer-type compatibility — and scalar answer replacement only by a unique type-compatible candidate — closes most of the gap to a fully generative pipeline.
- Reader is the only LLM. End-to-end, the system invokes exactly one LLM call (the final reader). Memory construction, organization, routing, retrieval, closure, evidence calibration, and answer calibration are all non-generative.

## Related Work Referenced

- **Memory-based baselines:** A-Mem (Zettelkasten-style), Mem0 / Mem0g, MemoryOS (OS-inspired tiered storage), LightMem (small-LM consolidation), SimpleMem (semantic compression + intent-aware retrieval), CompassMem (event-centric memory graphs), GAM (just-in-time task-specific contexts), Zep (temporal knowledge graph).
- **Memory-free baselines:** LONG-LLM (sliding window + per-block inference), RAG (chunked similarity retrieval).
- **Knowledge-graph retrieval lineage:** HippoRAG (Personalized PageRank over a KG, the closest relative of Zero-Mem's graph view).

## Related Concepts

- [[Concepts/zero-token-memory-operations]] — the operating regime Zero-Mem defines
- [[Concepts/dual-view-evidence-retrieval]] — the relational + temporal coordinate retrieval design
- [[Concepts/provenance-preserving-memory-substrate]] — the trace-as-source-of-record substrate
- [[Concepts/agent-memory-layer-patterns]] — broader landscape of agent memory systems
- [[Concepts/observational-memory-pattern]] — the non-generative memory philosophy
- [[Concepts/deterministic-first-architecture]] — the design bias toward non-LLM operations

## Related Entities

- [[Entities/bge-m3-embedding-model]] — the dense encoder used for indexing and scoring
- [[Entities/spacy-ner]] — the non-generative NER pipeline that builds the entity–context graph

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- arXiv: https://arxiv.org/html/2607.29377v1
