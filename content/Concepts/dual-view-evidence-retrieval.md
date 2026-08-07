---
title: "Dual-View Evidence Retrieval"

details: "Dual-view evidence retrieval is the retrieval design at the heart of Zero-Mem. Two complementary non-generative views are built over the same provenance-bearing trace units: a relational view (Personalized PageRank over an entity–context graph) and a hierarchical view (coarse-to-fine descent over episode / window / turn / local). A query profile φ(q) deterministically routes to {relational, local} and sets the primary view weight ρ (default 0.6). Retrieval is executed on both views; rankings are normalized per view and fused by S_fuse(d) = ρ · Ŝ_primary(d) + (1 − ρ) · Ŝ_secondary(d). Evidence closure then adds bounded, query-conditioned support: Ng supplies graph-ranked contexts with relational or bridging support, Nh restores neighboring turns or local spans. Ablation on HotpotQA 56K: full model 72.07 F1 vs. graph-only 62.50 and hierarchy-only 54.88, confirming complementarity. The two views cover each other's failure modes: the graph connects evidence distributed across documents; the hierarchy preserves local, temporal, and session-level state."
tags:
  - concepts
created: 2026-08-05
updated: 2026-08-05
type: concept
sources:
  - "Raw/arxiv-zero-mem-2026-08-05"
---

# Dual-View Evidence Retrieval

**Source:** [[Raw/arxiv-zero-mem-2026-08-05]] — Xiao et al., 2026 ([arXiv:2607.29377](https://arxiv.org/html/2607.29377v1))
**Category:** Architecture Pattern
**Status:** Active research area (validated by ablation: full > graph-only > hierarchy-only on HotpotQA 56K)

## Overview

A retrieval design that coordinates two non-generative views — a **relational view** over an entity–context graph and a **temporal view** over a turn / window / episode / local hierarchy — with a query-conditioned profile, fuses the rankings, and adds bounded structural support from each view. Both views resolve to the same provenance-bearing trace units, so the answer is always grounded in original interaction evidence.

The design addresses a long-standing failure mode in agent memory: flat similarity retrieval (whether lexical or dense) confuses semantically similar traces from different entities, sessions, or temporal states. A single view over the history cannot recover both *who* is connected to *what* and *when* a fact held. Two views, each covering the other's blind spot, do.

## The Two Views

### Relational View (Graph)

**Structure.** G = (Vd ∪ Ve, Ede ∪ Edd), where Vd are context nodes, Ve are entity nodes, Ede carries entity–context co-occurrence edges weighted by normalized occurrence frequency, and Edd carries adjacency edges between neighboring context units.

**Construction.** Run a non-generative NER (e.g. spaCy) over each context unit. For every detected entity e in context di, add an edge weighted by:

w(di, e) = c(e, di) / Σ(e' ∈ E(di)) c(e', di)

Adjacent context units are connected directly to preserve local continuity. The graph records observed co-occurrence and adjacency — no LLM-extracted triples, no inferred relations.

**Retrieval.** Align each query-extracted entity ê with the most similar observed graph entity e by cosine similarity over dense embeddings. Propagate activation through co-occurring entities and the sentences they share, combine with dense context priors into a reset vector rq, then run Personalized PageRank with damping γ:

πq = (1 − γ) rq + γ Pᵀ πq

PageRank values on context nodes form the graph ranking. Exact lexical/phrase matches refine the ranking for names, dates, values, titles, and quoted expressions.

### Hierarchical View (Temporal)

**Structure.** T(H) = Uturn ∪ Uwindow ∪ Uepisode ∪ Ulocal.

- **Turns** preserve atomic utterances.
- **Windows** retain short-range context (a few turns each).
- **Episodes** group adjacent windows into coherent event regions by semantic continuity and available temporal or session boundaries.
- **Local spans** preserve the immediate neighborhood of a candidate turn when surrounding context is needed.

All units inherit provenance from their underlying raw traces.

**Retrieval.** Coarse-to-fine: Uepisode → Uwindow → Uturn → Ulocal. Each unit is scored by semantic relevance to the query *plus* structural compatibility with the profile (subject consistency, temporal validity, boundary consistency, expected answer type, lexical/phrase support). The compatibility signals refine the semantic ranking; they are not independent evidence.

## Query-Conditioned Routing

Build a lightweight profile from the query and available metadata:

φ(q) = {subject, keywords, answer-type, temporal-cues, boundary}

- **Subject and keywords** provide content anchors.
- **Answer type and temporal cues** characterize the structural requirements of the requested evidence.
- **Boundary** specifies the admissible interaction scope when available.

Route(q) ∈ {relational, local} chooses which view is primary:

- **Relational** = graph priority (multi-hop / cross-document / entity-centric queries).
- **Local** = hierarchy priority (temporal / session-bounded / single-event queries).

Routing is deterministic: question form, temporal/aggregation requirements, and subject-anchor availability. Both views are always executed; routing controls their relative fusion weights. The globally shared primary-view weight ρ is the only tunable, set to 0.6 in Zero-Mem.

## Fusion

For each view v ∈ {g, h}, normalize scores to handle the absent / spread / degenerate cases:

Ŝv(d) = 0 if d absent from view v
Ŝv(d) = (Sv(d) − Sv_min) / (Sv_max − Sv_min) if Sv_max > Sv_min
Ŝv(d) = 1 if Sv_max = Sv_min

Then fuse:

S_fuse(d) = ρ · Ŝ_primary(d) + (1 − ρ) · Ŝ_secondary(d)

The graph view is primary for relational queries; the hierarchical view is primary for local queries. Let M(q) be the main evidence retained after fusion.

## Evidence Closure

Augment M(q) with bounded, query-conditioned support from each view:

C(q) = Dedup(M(q) ∪ Ng(M(q)) ∪ Nh(M(q)))

- **Ng** adds graph-ranked contexts with relational or bridging support — for multi-hop queries that need to follow connections across documents.
- **Nh** restores neighboring turns or local spans — for local queries that need conversational state around a candidate turn.

Either support set may be empty. Duplicates are merged by shared unit identifier or source provenance.

## Why Two Views Work (Ablation Evidence)

On HotpotQA with 56K-token contexts and GPT-4o-mini:

| Variant | F1 | BLEU-1 |
|---------|-----|--------|
| Full model (graph + hierarchy + closure + calibration) | 72.07 | 69.66 |
| Graph only | 62.50 | 59.90 |
| Hierarchy only | 54.88 | 51.40 |
| No evidence closure | 67.90 | 65.43 |
| No evidence calibration | 70.13 | 66.45 |

The graph view alone is stronger on HotpotQA because the benchmark rewards cross-document relational reasoning. Both views alone are well below the full model, confirming they are complementary. Closure adds ~4 F1 points by completing the evidence; calibration adds ~2 F1 points by refining it.

## Failure Modes Each View Covers

| Failure mode | View that covers it |
|--------------|---------------------|
| Evidence distributed across documents | Graph (Personalized PageRank) |
| Multi-hop reasoning | Graph (entity co-activation propagation) |
| Subject disambiguation across sessions | Graph (entity-context edges) |
| Local conversational state | Hierarchy (local span) |
| Temporal ordering | Hierarchy (turn / window / episode) |
| Session-level context | Hierarchy (window / episode) |
| Quoted expression / exact name | Graph refinement step (lexical match) |
| Session boundary scoping | Hierarchy + profile boundary check |

A single view either cannot reach across documents (hierarchy) or cannot preserve local order (graph). Dual-view retrieval makes both reachable in one pass.

## When to Use This Pattern

- **Long-term conversational memory** where the same entity reappears in distant sessions and disambiguation matters (e.g. LoCoMo).
- **Long-context multi-hop QA** where supporting evidence is distributed across many documents (e.g. HotpotQA 56K–448K).
- **State- and boundary-sensitive recall** where temporal validity and session scoping are part of the answer, not just the retrieval.

A dual-view design is overkill when:

- The history fits comfortably in the reader's context window — no memory system needed.
- The retrieval task is single-hop with no temporal dimension — flat similarity may be enough.
- The system is read-only and never needs to follow a chain of relations — graph propagation adds cost without benefit.

## Related Concepts

- [[Concepts/zero-token-memory-operations]] — the operating regime this design supports
- [[Concepts/provenance-preserving-memory-substrate]] — the trace structure that grounds both views
- [[Concepts/hindsight-memory-architecture]] — a different four-network agent memory design (World / Experience / Opinion / Observation)
- [[Concepts/graph-based-workflow-engine]] — graph algorithms in general agent context
- [[Concepts/agent-memory-layer-patterns]] — broader agent memory landscape

## References

- Raw Article: [[Raw/arxiv-zero-mem-2026-08-05]]
- Paper: [[Papers/zero-mem-zero-token-agent-memory]]
- arXiv: https://arxiv.org/html/2607.29377v1
