---
title: "Procedural Graphs for LLM Agents — Research Index"
details: "Synthesis index for the Procedural Graph framework introduced by Lu et al. (2026). Covers the (procedure, relation, procedure) graph representation, the online generative guidance mechanism, the offline self-evolution loop, and the empirical findings on seven benchmarks across four LLM families."
tags: [research, agent, llm, graph-engineering, self-improving-agents]
created: 2026-09-10
updated: 2026-09-10
type: research
sources:
  - .Raw/arxiv-procedural-graphs-2026-09-08.md
  - .Papers/procedural-graphs-2026-09-08.md
---

# Procedural Graphs for LLM Agents — Research Index

**Updated:** 2026-09-10
**Primary source:** Lu, Chen, Wu, Arık (2026), *Procedural Graphs: Self-Evolving Execution Structures for LLM Agents*, arXiv:2609.09153v1

---

## Overview

The Procedural Graph (PG) framework externalizes an agent's *procedural knowledge* — what to do, in what order, under which conditions — into a small directed attributed graph that sits outside model weights. The framework has three components: a **representation** (the graph data structure), an **online consumer** (generative guidance at each step), and an **offline writer** (the self-evolution loop). The paper demonstrates the design across seven benchmarks and four LLM families, with the largest gains on long-horizon tasks where constraint adherence matters (τ-bench, BFCL v3, EnterpriseArena CFO simulator).

## Concepts

### The Representation

- [[Concepts/procedural-graph-representation]] — (procedure, relation, procedure) triplets with condition/guidance/pitfalls edge attributes; the *what-to-do* counterpart to a knowledge graph

### Online Consumption

- [[Concepts/generative-pg-guidance]] — locate the active node, extract its h-hop neighborhood (or full graph on failure), generate step-level guidance via LLM verbalization; soft integration preserves reasoning freedom
- [[Concepts/localized-subgraph-vs-full-graph-guidance]] — empirical finding that localized generative guidance dominates both full-graph generative and full-graph raw injection on every measured benchmark

### Offline Evolution

- [[Concepts/pg-self-evolution-loop]] — diagnostic rollout → refiner mutation → validation gating → rejection memory; can build graphs from scratch or repair flawed priors
- [[Concepts/rejection-memory-as-negative-constraint]] — rejected candidates feed back as negative evidence; prevents repeated unsuccessful edits

## Tools & Projects

### The Paper Itself

- [[Entities/procedural-graph-paper]] — full research-artifact entry with authors, benchmarks, baselines, and related-work neighbors
- [[Papers/procedural-graphs-2026-09-08]] — paper-style summary with contributions, methodology, results, and key takeaways

### Adjacent Tools (mentioned in the paper)

The paper does not release code alongside the arXiv submission (as of v1). The closest related open artifacts in the field:

- **AutoGuide** (Fu et al. 2024) — the closest prior baseline. State-conditioned guidelines. PG extends with connected graph + structural refinement.
- **AFlow** (Zhang et al. 2025) — automated workflow search via MCTS over code graphs.
- **FlowBench** (Xiao et al. 2024) — workflow knowledge in text/code/flowchart; flowcharts are the empirical winner.
- **ToolNet** (Liu et al. 2024a) — directed tool-transition graph mined from LLM trajectories.
- **EnterpriseArena** (Han et al. 2026) — the long-horizon CFO simulator used as one of PG's evaluation benchmarks.

## Raw Sources

- [[Raw/arxiv-procedural-graphs-2026-09-08]] — full paper text with all six figures preserved as local asset references

## Key Results Table

| Benchmark | Best PG Wins Over Strongest Baseline | Note |
|-----------|---------------------------------------|------|
| HotpotQA | -0.90 to +1.30 pts (Ans F1) | Mixed; PG not strictly best |
| MultiChallenge | +0.61 pts (Sonnet 4.6 ties AWM) | Consistent 1st or tied |
| GDPval | +7.41 pts (Gemini 3.1 Pro) | Best across all 4 LLMs |
| ALFWorld | +1.49 pts (Gemini 3.1 Pro reaches 100.00%) | Best across all 4 LLMs |
| τ-bench | +6.96 pts (Gemini 3.1 Pro) | Best across all 4 LLMs |
| BFCL v3 | +9.00 pts (Gemini 3.5 Flash) | Best across all 4 LLMs |
| EnterpriseArena (CFO) | Survival 6.0% → 34.0% (Gemini 3.1 Pro) | Longest absolute margin |

19 wins / 2 ties / 3 losses vs. the strongest baseline in each setting (one-sided exact binomial sign test excluding ties, $p = 4.3 \times 10^{-4}$).

## Cross-Cutting Themes

### Procedural vs Factual Knowledge

1. **Knowledge graphs answer *what-is*; Procedural graphs answer *what-to-do*.** The paper's central framing distinction. Edges in a KG carry plain relation labels; edges in a PG carry *condition*, *guidance*, *pitfalls* — the three action-time affordances an actor needs to decide.
2. **Compact graphs suffice.** Most PGs in the paper have ≤ 17 nodes and ≤ 27 triplets. The procedure graph is a small object, not a knowledge-base-scale artifact. BFCL v3's 131 nodes are an outlier mirroring its function-catalog size.

### Soft Guidance over Hard Workflows

3. **Reasoning freedom matters for non-trivial tasks.** Workflows and state machines constrain execution but require manual design. Soft guidance (appended, not enforced) lets the solver override the advice when it has stronger local evidence. The paper's Mode 3 recovers from a flawed expert prior; a hard workflow engine cannot.
4. **Localization beats global context.** Localized subgraph beats full-graph on tokens AND quality. Full-graph generative guidance *loses* to baseline on ALFWorld — too much irrelevant structure dilutes attention.

### Iterative Self-Improvement

5. **Validate on held-out, never on training.** The acceptance gate consumes validation performance. Training-set overfitting does not enter the loop's decisions.
6. **Rejection memory is half of search.** Without negative evidence, the refiner repeats unsuccessful edits. With it, the search distribution steers away from prior failures.
7. **A bad prior is recoverable.** Mode 1→3 progression on MultiChallenge (58.93% → 92.86%) demonstrates that iterative offline editing can rescue a flawed initialization. This lowers the adoption bar.
8. **Tail-trim trajectories, not head-trim.** When trajectory context exceeds the token budget, drop from the *beginning* — the recent trajectory is the operative signal. A small choice with large effects on what the refiner reasons about.

### Long-Horizon Resilience

9. **Anticipatory behavior emerges from graph structure.** On EnterpriseArena, the behavior that tracks survival across all four LLMs is *anticipatory fundraising* — submitting capital requests months before cash runs out. This is not in any baseline agent's prompt; it emerges from the graph's edges.
10. **Compact procedures, large gains.** The CFO graph has 11 nodes and 13 triplets, yet it raises full-horizon survival by 28 points on Gemini 3.1 Pro. The graph is not a knowledge base — it is a constraint reminder.

## Next Research Directions

- [ ] Reproduce Mode 5 (Scratch + Online Evolution) on a single benchmark with a smaller open model to validate the loop outside the paper's four LLM families
- [ ] Implement the structural validator (Appendix B.6) standalone — a delete-then-add edit interface with cycle policy and reachability check is a generally useful primitive beyond PG
- [ ] Compare PG's edit interface (delete-then-add for attributes) against diff-based attribute updates — does preserving the edge identity matter when the LLM rewrites the guidance string?
- [ ] Apply the rejection-memory pattern to other self-improvement loops (ExpeL, AWM, EvolveR) — measure whether negative-evidence feedback accelerates convergence
- [ ] Test transfer of a learned PG across solver models — if a HotpotQA PG works for Gemini 3.5 Flash, does it work for Claude Sonnet 4.6 without retraining? (The paper claims "evaluating transfer across solvers" as future work.)
- [ ] Map the seven PG construction modes to the 14 principles of [[Concepts/graph-engineering-discipline|Graph Engineering]] to identify which principles the loop *automates* and which it leaves to human designers

## References

- Paper entry: [[Papers/procedural-graphs-2026-09-08]]
- Raw text: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Paper artifact entry: [[Entities/procedural-graph-paper]]
- Original: https://arxiv.org/html/2609.09153v1