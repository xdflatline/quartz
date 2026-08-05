---
title: "Research Index: Zero-Token Agent Memory"
detail: "Synthesis of Zero-Mem and related zero-token, provenance-preserving agent memory systems — regimes where the LLM is reserved for the final reader and every memory operation runs deterministically."
details: "This index collects concepts, tools, and patterns from the Zero-Mem paper (Xiao et al., 2026) and situates it among related memory architectures. The central research question: can an agent memory system eliminate LLM calls from every operation outside final question answering, while retaining structured access beyond flat similarity retrieval? The answer (yes, with provenance preservation) is the operating regime this index covers. The research thread connects Zero-Mem to HippoRAG (the closest graph-retrieval relative), the broader family of generated-memory systems (Mem0, A-Mem, LightMem, SimpleMem, CompassMem, MemoryOS, GAM, Zep), and the practitioner's perspective on deterministic-first architecture for memory systems."
tags:
  - research
created: 2026-08-05
updated: 2026-08-05
type: research
---

# Research Index: Zero-Token Agent Memory

**Updated:** 2026-08-05
**Source:** Zero-Mem (Xiao et al., 2026, [arXiv:2607.29377](https://arxiv.org/html/2607.29377v1)) + related literature

---

## Overview

This index collects concepts, tools, and patterns from the Zero-Mem paper and related work on **non-generative agent memory systems**. The central research question is whether structured memory access requires generation at all. Zero-Mem's answer: no — original interaction traces can be the source of record, two complementary non-generative views (a relational entity–context graph and a temporal hierarchy) can be derived over them, and the LLM can be reserved for the final reader. The empirical result: 0 LLM tokens for memory operations, 57.6% latency reduction versus the fastest LLM-using baseline, and the best F1 and BLEU-1 across eight compared systems on LoCoMo and HotpotQA.

The thread connects to the broader memory systems landscape, the HippoRAG line of graph-based retrieval, and the deterministic-first architectural philosophy.

## Concepts

### Zero-Token Architecture
- [[Concepts/zero-token-memory-operations]] — Operating regime where every step outside final QA uses zero LLM calls and zero LLM tokens
- [[Concepts/dual-view-evidence-retrieval]] — Coordinate a relational view and a temporal view with a query profile, fuse rankings, add bounded structural support
- [[Concepts/provenance-preserving-memory-substrate]] — Treat original traces as the source of record; every derived unit retains a back-pointer
- [[Concepts/deterministic-first-architecture]] — The broader design rule: deterministic code first, AI as a small upgrade

### Related Memory Patterns
- [[Concepts/agent-memory-layer-patterns]] — Broader practitioner perspective on agent memory layers
- [[Concepts/observational-memory-pattern]] — A different non-generative memory pattern (Observer + Reflector background agents) — uses generation, not zero-token
- [[Concepts/hindsight-memory-architecture]] — Four-network memory design (World / Experience / Opinion / Observation) with explicit Retain / Recall / Reflect
- [[Concepts/multi-agent-orchestration-patterns]] — Orchestration patterns, including memory coordination
- [[Concepts/graph-based-workflow-engine]] — Graph algorithms in agent context

## Tools & Projects

### Encoders and Access Signals
- [[Entities/bge-m3-embedding-model]] — Dense encoder used in Zero-Mem for query-entity alignment and context priors
- [[Entities/spacy-ner]] — Non-generative NER pipeline that builds the entity–context graph

### Related Memory Systems (from the paper's Related Work)
| System | Core mechanism | LLM in memory ops? | Note |
|--------|----------------|---------------------|------|
| **Zero-Mem** (2026) | Entity–context graph + temporal hierarchy, deterministic calibration | **No** | This paper |
| Mem0 / Mem0g (2025) | LLM tool calls for add / update / delete / no-op on memory records; Mem0g adds directed labeled graph | Yes | Incremental extract-and-update |
| A-Mem (2025) | Zettelkasten note generation by LLM with keyword / tag / context fields, dynamic linking | Yes | Note-taking inspired |
| MemoryOS (2025) | OS-inspired tiered storage (short / mid / long-term), paging, popularity-based updates | Yes | Storage-tier design |
| LightMem (2026) | Pre-compression + topic segmentation by small LM; decouples online retrieval from offline consolidation | Yes (small LM) | Efficiency-oriented |
| SimpleMem (2026) | Semantic structured compression + online semantic synthesis + intent-aware retrieval planning | Yes | Efficiency-oriented |
| CompassMem (2026) | Event-centric memory graphs with explicit relations | Yes | Event-graph design |
| GAM (2025) | Lightweight offline memory + online deep research, just-in-time task-specific context | Yes (online LLM) | JIT research pattern |
| Zep (2025) | Temporal knowledge graph with episodic / semantic-entity / community subgraphs, dual-time model | Yes (graph construction) | Temporal KG design |
| HippoRAG (2024) | Personalized PageRank over a knowledge graph for long-term LLM memory | No (encoding only) | Closest relative of Zero-Mem's graph view |

## Raw Sources

- [[Raw/arxiv-zero-mem-2026-08-05]] — Full text of the Zero-Mem paper
- [[Papers/zero-mem-zero-token-agent-memory]] — Paper page with architecture, results, and ablation tables

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [arXiv:2607.29377](https://arxiv.org/html/2607.29377v1) | Zero-Mem: zero-token memory operations | 2026-08 | Zero-token regime, dual-view retrieval, deterministic calibration, +5.4 F1 on LoCoMo, 57.6% latency reduction |

## Cross-Cutting Themes

### Memory Architecture
1. **Generated memory is optional** — Zero-Mem shows that structured evidence selection over original traces can match or beat generated-memory pipelines on long-term and long-context QA. The two views (graph + hierarchy) plus deterministic calibration are sufficient.
2. **Provenance beats generation for traceable answers** — Every retrieved unit in Zero-Mem can be checked against the original trace. Generated memory drops, merges, or invents details; provenance-preserving memory does not.
3. **Two views > one view** — Graph handles cross-document relational evidence; hierarchy preserves local, temporal, and session-level state. Ablation: full model 72.07 F1 vs. graph-only 62.50 and hierarchy-only 54.88 on HotpotQA 56K.
4. **Routing between views is deterministic** — A lightweight profile (subject, keywords, answer-type, temporal-cues, boundary) is enough to choose which view is primary. No LLM needed for routing.
5. **Deterministic calibration closes most of the gap** — Filter on hard constraints, rank by compatibility, replace scalar answers only with a unique type-compatible candidate. No LLM needed for calibration.

### Cost and Latency
6. **LLM cost is the bottleneck, not retrieval** — Once LLM calls and tokens are removed from memory operations, latency drops by 57.6% versus the fastest LLM-using baseline (LightMem).
7. **Zero-token ≠ zero computation** — Encoder inference, memory organization, retrieval, and deterministic calibration still cost CPU/GPU. But the cost is deterministic, reproducible, and horizontally scalable.
8. **Two budgets, two optimization paths** — The zero-token regime splits the system into a deterministic budget (memory ops) and an LLM budget (the reader). They can be optimized independently.

### Positioning in the Memory Landscape
9. **Closest relative: HippoRAG** — HippoRAG (2024) also uses Personalized PageRank over a knowledge graph with non-LLM encoding. Zero-Mem extends this with a second hierarchical view, deterministic calibration, and a zero-token regime.
10. **Generated-memory systems (Mem0, A-Mem, SimpleMem, LightMem, CompassMem, GAM) keep LLM in the loop** — They reduce generative overhead but do not eliminate it. Zero-Mem's empirical result is that elimination is now competitive.
11. **Efficiency-oriented systems (LightMem, SimpleMem) are the strongest competition** — They are the closest to zero-token operation; the paper's 57.6% latency reduction is measured against LightMem.

## Practical Implications

- **For new agent memory systems.** The zero-token regime is now a credible default for long-term conversational memory and long-context multi-hop retrieval. The components are off-the-shelf (BM25, BGE-M3, spaCy, Personalized PageRank) and the design is reproducible.
- **For systems already using generated memory.** The cost is mostly in the LLM calls you already make. Switching to a zero-token pipeline is a substantial refactor, but the latency and cost savings (57.6% latency, 0 LLM tokens for memory ops) are large enough to be worth measuring.
- **For hybrid designs.** A small LLM (e.g. a fine-tuned 1B–3B model) is still in the LLM budget under the regime's definition. Systems that use a small LM for intent classification or routing have *reduced* the LLM cost without leaving the regime, but have not eliminated it.

## Cross-References

- [[Research/ai-agent-memory-orchestration]] — Practitioner perspective on memory layers, typed knowledge, and friction logging (HN-driven, 2025)
- [[Papers/hindsight-agent-memory]] — Hindsight's four-network memory design with Retain / Recall / Reflect (paper page)

## Next Research Directions

- [ ] Benchmark the zero-token regime against a real production agent (not just LoCoMo / HotpotQA) to measure end-to-end user-facing latency and cost
- [ ] Evaluate whether the dual-view design improves with more than two views (e.g. add a community-detection view for entity clustering)
- [ ] Test the deterministic calibration's robustness when the reader's LLM is small (3B–7B) versus the paper's GPT-4o-mini and Qwen2.5-14B
- [ ] Compare Zero-Mem's zero-token regime against a small-LM hybrid (e.g. using a 1B model for routing and calibration) on the same hardware budget
- [ ] Investigate whether the entity–context graph can be replaced by a community-detection-derived subgraph for very long histories (>1M turns) without losing relational evidence
- [ ] Reproduce the 57.6% latency reduction on a different hardware setup (e.g. Apple Silicon unified memory) to confirm the result is not GPU-specific
