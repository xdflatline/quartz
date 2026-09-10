---
title: "Procedural Graphs (Lu et al. 2026) — Paper"
details: "Research artifact entry for the arXiv paper 'Procedural Graphs: Self-Evolving Execution Structures for LLM Agents' by Yuxing Lu, Yicheng Chen, Shanchan Wu, and Sercan Ö. Arık (Google; Georgia Tech; Peking University), arXiv:2609.09153v1, posted 8 Sep 2026."
tags: [entities, research, agent, llm, paper]
source: https://arxiv.org/html/2609.09153v1
created: 2026-09-10
updated: 2026-09-10
type: entity
---

# Procedural Graphs (Lu et al. 2026) — Paper

**Type:** Research paper (arXiv preprint)
**arXiv:** 2609.09153v1 [cs.AI]
**Date:** 8 Sep 2026
**Authors:** Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık
**Affiliations:** Google; Georgia Institute of Technology; Peking University
**Link:** https://arxiv.org/html/2609.09153v1

## What It Is

A paper that introduces the **Procedural Graph (PG)** — a (procedure, relation, procedure) graph with textual condition / guidance / pitfalls attributes on each edge — and pairs it with an online generative guidance mechanism plus an offline self-evolution loop. Evaluated across seven benchmarks and four LLM families, the Procedural Graph ranks first or tied first in 21 of 24 model–benchmark settings; the self-evolution loop can build effective graphs from scratch or repair flawed expert priors.

## Key Contributions (one line each)

- **Procedural Graph representation** — directed attributed graph externalizing procedural knowledge, with three action-time edge fields
- **Generative PG Guidance** — locate the active node, extract its h-hop neighborhood, LLM-verbalize into situational advice
- **Self-Evolution Loop** — diagnostic rollout → refiner mutation → validation gating → rejection memory
- **Localization finding** — subgraph + generative beats full-graph + generative AND full-graph + raw injection on every measured benchmark

## Benchmarks Used

- **HotpotQA** — multi-hop QA with search tools (Yang et al. 2018)
- **MultiChallenge** — multi-turn instruction retention (Deshpande et al. 2025)
- **GDPval** — open-ended professional deliverables (Patwardhan et al. 2025)
- **ALFWorld** — embodied household tasks (Shridhar et al. 2021)
- **τ-bench** — policy-compliant customer-service tool use (Yao et al. 2024)
- **BFCL v3** — multi-turn function calling (Patil et al. 2025)
- **EnterpriseArena** — long-horizon financial simulation with unannounced crises (Han et al. 2026)

## Models Evaluated

- Claude Sonnet 4.6
- Gemini 3.1 Pro
- Gemini 3.5 Flash
- Grok 4.1 Fast

Guidance model and refiner share the underlying LLM as the solver in all experiments. Greedy decoding throughout.

## Baselines Compared

- Vanilla ReAct (no memory)
- MemoryBank — summarized experience with forgetting
- RAP — retrieval-augmented planning with in-context exemplars
- ExpeL — natural-language insight distillation
- AutoGuide — state-conditioned guidelines
- AWM — linear workflow induction
- KnowAgent — textual action-transition rules

## Related Entries in the Wiki

- [[Papers/procedural-graphs-2026-09-08]] — paper page (paper-style summary)
- [[Raw/arxiv-procedural-graphs-2026-09-08]] — full paper text with all 6 figures preserved
- [[Concepts/procedural-graph-representation]] — the (procedure, relation, procedure) data structure
- [[Concepts/generative-pg-guidance]] — online locate→extract→generate mechanism
- [[Concepts/pg-self-evolution-loop]] — offline four-step feedback loop
- [[Concepts/rejection-memory-as-negative-constraint]] — safeguard against repeated failed edits
- [[Concepts/localized-subgraph-vs-full-graph-guidance]] — empirical localization finding

## Citations (Besta, Han, Lu — selected from the paper's reference list)

The paper cites 24+ related methods in its Appendix A comparison. Notable neighbors:

- **AutoGuide (Fu et al. 2024)** — closest prior: state-conditioned guidelines. PG extends this with a *connected graph* of transitions plus structural refinement.
- **AFlow (Zhang et al. 2025)** — automated workflow search via MCTS over code-represented graphs.
- **FlowBench (Xiao et al. 2024)** — workflow knowledge in text/code/flowchart; flowcharts reduce planning hallucination most effectively.
- **ToolNet (Liu et al. 2024a)** — directed tool-transition graph mined from LLM trajectories.
- **ControlLLM (Liu et al. 2024b)** — tool dependency graph with Thoughts-on-Graph search.
- **MemP (Fang et al. 2025)** — procedural memory with build/retrieve/update lifecycle; no explicit graph.
- **EvolveR (Wu et al. 2025)** — offline self-distillation + online retrieval + policy reinforcement.
- **A-Mem (Xu et al. 2026), Zep/Graphiti (Rasmussen et al. 2025)** — knowledge-graph structure for *episodic* (not procedural) memory.

## References

- Paper entry: [[Papers/procedural-graphs-2026-09-08]]
- Raw text: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Original: https://arxiv.org/html/2609.09153v1