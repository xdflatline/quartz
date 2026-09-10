---
title: "Localized Subgraph vs Full-Graph Guidance"
details: "Empirical finding from the Procedural Graph paper: for the same underlying graph, *localized generative guidance* (read the h-hop neighborhood around the active node and verbalize via an LLM) dominates both *full-graph generative guidance* and *full-graph raw injection* on every measured benchmark, with smaller token cost. Token reduction vs full-graph generative: 70.9% on ALFWorld, 18.1% on GDPval, 14.8% on MultiChallenge. Quality gains over the best alternative: +2.0 points on MultiChallenge, +6.8 on GDPval, +9.0 on ALFWorld."
tags: [concepts, agent, llm, prompt-engineering, graph-engineering]
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - .Raw/arxiv-procedural-graphs-2026-09-08.md
  - .Papers/procedural-graphs-2026-09-08.md
---

# Localized Subgraph vs Full-Graph Guidance

**Source:** [[Raw/arxiv-procedural-graphs-2026-09-08]] · [[Papers/procedural-graphs-2026-09-08]]
**Category:** Architecture Pattern / Empirical Finding
**Status:** Active research area (introduced Lu et al. 2026)

## Overview

The paper's Section 5.5 ablation answers two design questions behind [[Concepts/generative-pg-guidance|Generative PG Guidance]]:

1. **What portion of the graph should the agent see?** Full graph, or a localized subgraph around the current procedure?
2. **How should the graph be consumed?** Raw injection into the prompt, or generative verbalization by an LLM?

The result: **localized generative guidance wins on both quality and tokens** across every measured benchmark. The pattern is *subgraph → generative*, not *full-graph → raw* (which loses on embodied tasks) and not *full-graph → generative* (which loses on tokens and on ALFWorld).

## Core Content

### The Four Configurations

Same underlying graph, same solver prompt template, Gemini 3.5 Flash:

| Configuration | Graph Scope | Consumption |
|---------------|-------------|-------------|
| Baseline | none | — |
| Full graph, raw injection | $\mathcal{G}$ | injected verbatim into prompt |
| Full graph, generative | $\mathcal{G}$ | $\Psi(\mathcal{G}, q, \mathcal{T}_{t-w:t})$ |
| **Subgraph, generative (Ours)** | $\mathcal{N}_h(u_t)$ | $\Psi(\mathcal{N}_h(u_t), q, \mathcal{T}_{t-w:t})$ |

The two PG-with-generative variants use *textually identical* prompts; only the content bound to the graph context slot differs.

### Headline Numbers (Section 5.5, Table 3)

| Configuration | MultiChallenge Acc. | GDPval Rubric | ALFWorld Success | Avg. Tok (MC) | Avg. Tok (GDPval) | Avg. Tok (ALFWorld) |
|---------------|---------------------|---------------|------------------|---------------|-------------------|---------------------|
| Baseline (no graph) | 80.27 | 54.80 | 72.58 | 6,629 | 275,638 | 18,055 |
| Full graph, raw injection | 86.60 | 57.17 | 70.34 | 10,164 | 264,680 | 21,062 |
| Full graph, generative | 87.35 | 56.75 | **54.48** | 14,434 | 448,972 | 96,360 |
| **Subgraph, generative (Ours)** | **89.31** | **63.99** | **81.53** | 12,295 | 367,738 | 28,064 |

Subgraph-generative beats the no-graph baseline by +9.04 (MC), +9.19 (GDPval), and +8.95 (ALFWorld) points.

### What Each Comparison Shows

- **Subgraph > full-graph (generative) on tokens.** Localization cuts guidance tokens by 70.9% on ALFWorld, 18.1% on GDPval, 14.8% on MultiChallenge. The full graph is 3–5x larger than the localized neighborhood, and the guidance LLM must read all of it.
- **Subgraph > full-graph (generative) on quality.** Full-graph generative drops ALFWorld success to 54.48% (vs. baseline 72.58%) — too much irrelevant structure drowns the signal. Localization wins back to 81.53%.
- **Generative > raw injection on ALFWorld and GDPval.** Raw injection of the full graph loses on embodied tasks (ALFWorld drops 2.24 points vs. baseline). The generative LLM compresses and contextualizes the graph into action-relevant guidance.
- **Localization also shortens trajectories.** On GDPval and ALFWorld, average solver steps drop from 28.20 → 18.57 and 21.84 → 18.80 respectively, while total token consumption is 33.4% and 55.4% higher than the no-graph baseline.

### The Mechanism

The localization finding has a clean intuition: **the agent is at one node right now, and the next-step distribution is dominated by that node's outgoing transitions, not by nodes five hops away.** Injecting or verbalizing the whole graph pays an attention cost for irrelevant structure. The $h = 2$ default exposes the immediate action plus one-after-next — empirically enough context for the guidance LLM to produce actionable advice without dilution.

The intuition also matches the failure modes in the paper's ALFWorld analysis: full-graph generative guidance on an embodied household task floods the prompt with kitchen-and-bedroom transitions when the agent is currently at "find the alarm clock", distracting it from the local reasoning. Localization avoids this.

### Where Raw Injection Wins

Raw injection of the full graph improves performance on **structured dialogue** (MultiChallenge rises from 80.27 to 86.60) but lowers success on **embodied execution** (ALFWorld drops from 72.58 to 70.34). This is a domain-dependent finding: when the next action is highly constrained by the dialogue state (MultiChallenge's instruction-retention tests), raw text in the prompt helps. When the next action requires compositional reasoning over many possible tool sequences (ALFWorld), the generative LLM does better at compressing to the relevant subset.

The paper does not claim raw injection is universally worse — it claims that across the three benchmarks measured, the localized-generative configuration is the best single choice.

### Cost-Quality Tradeoff

The localized configuration is not the cheapest (raw injection of the full graph is cheaper on MultiChallenge at 10,164 tokens vs. 12,295), but it is the cheapest *among configurations that match the no-graph baseline on every benchmark*. Raw injection of the full graph underperforms the baseline on ALFWorld; full-graph generative underperforms on ALFWorld and is more expensive everywhere. Localization is the cheapest Pareto-optimal point.

## Key Insights

1. **Locality is a token-budget multiplier.** The h-hop neighborhood is dramatically smaller than the full graph (often 5–10x), so the guidance LLM reads less, writes less, and the solver prompt is shorter. The savings compound across steps.
2. **Generative compression beats raw injection for embodied tasks.** When the agent has many possible tool calls to choose from, the guidance LLM's compression into situational advice beats dumping all edges into the prompt. The reverse holds for highly structured dialogue.
3. **Full-graph is an anti-pattern for embodied domains.** The full-graph generative row loses ALFWorld by 18 points vs. baseline. The mechanism is probably attention dilution — too many irrelevant transitions in context.
4. **Localization + generative is the cheapest Pareto-optimal choice.** Across three benchmarks with very different characteristics (dialogue retention, professional deliverables, embodied household), localized-generative beats every alternative on quality at a modest token premium over the cheapest configuration.
5. **The default h=2 is empirically validated.** The paper's main results all use $h = 2$ (one immediate + one-after-next). No ablation sweeps h; the choice is justified by the Table 3 win, not a parameter search.

## Related Concepts

- [[Concepts/generative-pg-guidance]] — the mechanism being ablated
- [[Concepts/procedural-graph-representation]] — the graph being consumed
- [[Concepts/hybrid-retrieval-complementary-halves]] — the broader hybrid retrieval pattern; PG guidance is one instance
- [[Concepts/context-gap-classification]] — irrelevant context dilutes signal; localization is a remedy
- [[Concepts/critical-path-latency]] — the guidance call adds latency; localization keeps the call small
- [[Concepts/context-as-evolving-playbook]] — localization picks the relevant slice of the playbook per step

## References

- Raw: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Paper: [[Papers/procedural-graphs-2026-09-08]]
- Original: https://arxiv.org/html/2609.09153v1 (§5.5, Table 3)