---
title: "Procedural Graphs: Self-Evolving Execution Structures for LLM Agents"
details: "Introduces the Procedural Graph (PG), an attributed directed graph of (procedure, relation, procedure) triplets with condition/guidance/pitfalls edges, plus an online generative guidance mechanism (localize the active node, retrieve its h-hop neighborhood, verbalize via an LLM into situational advice) and an offline self-evolution loop (diagnostic rollout → LLM refiner proposes edits → validation gating with rejection memory). Across six benchmarks and four LLM families, PG ranks first in 21 of 24 settings and the self-evolution loop can build effective graphs from scratch or repair flawed expert priors."
tags: [research, agent, llm, graph-engineering, self-improving-agents]
source: https://arxiv.org/html/2609.09153v1
authors: ["Yuxing Lu", "Yicheng Chen", "Shanchan Wu", "Sercan Ö. Arık"]
venue: "arXiv:2609.09153v1 [cs.AI], 8 Sep 2026"
created: 2026-09-10
updated: 2026-09-10
type: article
---

# Procedural Graphs: Self-Evolving Execution Structures for LLM Agents

**Authors:** Yuxing Lu, Yicheng Chen, Shanchan Wu, Sercan Ö. Arık (Google; Georgia Institute of Technology; Peking University)
**Published:** 8 Sep 2026 — arXiv:2609.09153v1 [cs.AI]
**Link:** https://arxiv.org/html/2609.09153v1

---

## Overview

The paper argues that LLM agents lose procedural coherence because their procedural knowledge (what to do, in what order, under which conditions) is implicit in unconstrained generation over a growing trajectory log. To make it explicit and editable, the authors introduce the **Procedural Graph (PG)** — a (procedure, relation, procedure) graph whose edges carry **condition / guidance / pitfalls** attributes — and pair it with two mechanisms:

- **Online: Generative PG Guidance** — at each step, locate the active node from the last action, retrieve its *h-hop neighborhood* (default *h*=2) plus a recent trajectory window, and let a guidance LLM verbalize the surrounding edges into situational advice that is appended to the solver's prompt.
- **Offline: Self-Evolution Loop** — after each training batch, an LLM refiner contrasts successful and failed trajectories and proposes edits to the graph; the candidate is accepted only if it preserves or improves held-out validation performance, and rejected candidates are retained as a **rejection memory** to discourage repetition.

Across HotpotQA, MultiChallenge, GDPval, ALFWorld, τ-bench, BFCL v3, and EnterpriseArena (CFO simulator), the Procedural Graph ranks first or tied first in 21 of 24 model–benchmark cells, with the largest gains on long-horizon EnterpriseArena (e.g., survival 6.0% → 34.0% on Gemini 3.1 Pro). Self-evolution from a minimal skeleton matches or surpasses hand-designed expert graphs, and the loop recovers from a flawed expert prior that initially hurts performance (MultiChallenge: 58.93% → 92.86%).

## Core Contributions

- **Procedural Graph representation** — a directed, attributed graph $\mathcal{G}=(\mathcal{V}, \mathcal{R}, \mathcal{E}, \Phi)$ where each edge $e=(u, r, v)$ states "$v$ is admissible after $u$ under relation $r$" and $\Phi(e)$ holds textual condition, guidance, and pitfalls fields. The mirror to a knowledge graph is explicit: knowledge graphs answer *what-is* questions with (entity, relation, entity); procedural graphs answer *what-to-do* questions with (procedure, relation, procedure).
- **Generative Procedural Graph Guidance** — *locate* the active node, *extract* its h-hop neighborhood (or the full graph when matching fails), and *generate* step-level advice by an LLM reading the static edge attributes. The graph is frozen during inference.
- **Offline self-evolution loop** — *diagnostic rollout* (record traces with scores), *feedback-driven mutation* (refiner emits structured `add_nodes` / `add_edges` / `delete_nodes` / `delete_edges`), *validation gating* (accept iff validation score does not decrease, ties allowed), and *rejection memory* (append rejected candidates and serve them as negative evidence to the next round's refiner).
- **Localization > full-graph** — empirically, the localized subgraph beats full-graph generative guidance on tokens AND on every measured benchmark. Token reduction ranges from 14.8% (MultiChallenge) to 70.9% (ALFWorld); quality gains range from +2.0 to +9.0 points over the best alternative.
- **Loop repairs flawed priors** — on MultiChallenge, a hand-crafted expert graph initially drops success from 87.50% → 58.93%; the iterative evolution loop recovers to 92.86%, a +33.93-point swing, by editing topology and attributes from execution feedback.
- **Five construction modes** benchmarked head-to-head: hand-crafted expert, expert + static update, expert + online evolution, scratch + static build, scratch + online evolution. Mode 5 (scratch + online evolution) achieves the best HotpotQA F1 (78.79%) and the second-best MultiChallenge success (91.07%) without any human prior.

## Methodology

### Formal Representation

$$\mathcal{G}=(\mathcal{V}, \mathcal{R}, \mathcal{E}, \Phi), \qquad \mathcal{E} \subseteq \mathcal{V} \times \mathcal{R} \times \mathcal{V}$$

- $\mathcal{V}$ = abstract nodes (tool actions, reasoning steps, task statuses)
- $\mathcal{R}$ = relation vocabulary (in the experiments: LEADS_TO, TRIGGERS, PROVIDES_INPUT_FOR, CONVERGES_TO)
- $\Phi(e) = \{$ *condition*, *guidance*, *pitfalls* $\}$ — three textual fields describing when a transition applies, how to proceed, and what to avoid

Example edge: (cash_flow_forecast, LEADS_TO, fund_raising_request) with attributes "*condition*: projected runway falls below the safety buffer; *guidance*: submit the request early to allow for the financing delivery delay; *pitfalls*: do not stack a second request while one is pending."

### Generative Guidance at Inference

$$\mathcal{T}_t = (a_1, o_1, \dots, a_{t-1}, o_{t-1})$$
$$u_t = \mathrm{Match}(a_{t-1}, \mathcal{V})$$
$$\mathcal{G}_t = \begin{cases} \mathcal{N}_h(u_t), & u_t \neq \emptyset \\ \mathcal{G}, & \text{otherwise} \end{cases}$$
$$g_t = \Psi(\mathcal{G}_t, q, \mathcal{T}_{t-w:t})$$
$$a_t \sim P_{\text{solver}}(\cdot \mid q, \mathcal{T}_t, g_t)$$

The connected neighborhood lets the guidance model read transitions in their topological context (including h steps ahead). On matching failure the full graph is used. The solver receives both the trajectory and the freshly generated guidance; reasoning freedom is preserved (the guidance is appended, not enforced).

### Self-Evolution Loop

For round $k = 1, \dots, K$ starting from retained graph $\mathcal{G}_{k-1}$ with cached validation score $S_{k-1}$:

1. **Diagnostic rollout** — run the solver on a training batch $\mathcal{B}_k \subset \mathcal{D}_\text{train}$ with the current graph; record traces and scores $\mathcal{E}_k = \{(q_i, \mathcal{T}_i^{(k)}, S_i^{(k)})\}$.
2. **Feedback-driven mutation** — the refiner inspects high vs. low-scoring traces and emits a structured edit set $\Delta \mathcal{G}_k$ (node additions, edge additions, deletions). Attribute changes are performed as delete-then-add on the edge.
3. **Validation gating** — the candidate $\mathcal{G}_k^\text{cand} = \mathcal{G}_{k-1} \oplus \Delta \mathcal{G}_k$ is rolled out on $\mathcal{D}_\text{val}$; accept iff $S_\text{val}(\mathcal{G}_k^\text{cand}) \ge S_{k-1}$ (ties allowed).
4. **Rejection memory** — rejected candidates and their traces are appended to $\mathcal{H}_\text{rejected}$. The refiner receives $\mathcal{H}_\text{rejected}$ as negative evidence when proposing $\Delta \mathcal{G}_{k+1}$, discouraging repetition of unsuccessful edits.

Structural validator (independent of the refiner prompt) rejects malformed edits, invalid node/relation types, missing endpoints, and — when cycles are disallowed — introduces cycle-closing edges before validation.

### Experimental Setup

- **Benchmarks (7):** HotpotQA (multi-hop QA), MultiChallenge (multi-turn instruction retention), GDPval (open-ended professional deliverables), ALFWorld (embodied household), τ-bench (policy-compliant tool use), BFCL v3 (multi-turn function calling), EnterpriseArena (long-horizon financial simulation under unannounced macroeconomic crises).
- **Models:** Claude Sonnet 4.6, Gemini 3.1 Pro, Gemini 3.5 Flash, Grok 4.1 Fast. The guidance model and refiner always share the same underlying LLM as the solver.
- **Baselines:** Vanilla ReAct (no memory), MemoryBank, RAP, ExpeL, AutoGuide, AWM, KnowAgent — every learning-based baseline consumes the same training trajectories as the self-evolution loop.
- **PG configuration:** online $h=2$ neighborhood, $w=3$ trajectory window.
- **Decoding:** greedy, temperature 0.

## Results

### Main Results (Table 1, headline)

PG ranks first or tied first in 21 of 24 model–benchmark settings. Compared with the strongest baseline in each setting, PG records 19 wins, 2 ties, 3 losses (one-sided exact binomial sign test excluding ties, $p=4.3 \times 10^{-4}$). Largest margins:

- BFCL v3, Gemini 3.5 Flash: 67.00% vs. 58.00% (+9.00 points)
- GDPval, Gemini 3.1 Pro: 78.78 vs. 71.37 (+7.41 points)
- τ-bench, Gemini 3.1 Pro: 80.00% vs. 73.04% (+6.96 points)

### Long-Horizon Decision Making (EnterpriseArena)

PG achieves the highest full-horizon survival across all four LLMs on the CFO simulator. Survival lifts: 44.0% → 58.0% (Claude Sonnet 4.6), 6.0% → 34.0% (Gemini 3.1 Pro), 26.0% → 40.0% (Grok 4.1 Fast). The behavior that tracks survival across all models is **anticipatory fundraising** — submitting capital requests months before cash runs out — because capital delivery takes 1–6 months. The unguided Gemini 3.5 Flash baseline issues 18.94 redundant tool calls per month; PG-guided Flash reduces this to 12.53 while raising the average enterprise score.

### Construction Modes (Table 2)

| Mode | Init | Update | HotpotQA Ans F1 | MultiChallenge Overall |
|------|------|--------|----------------|------------------------|
| Unguided | — | — | 71.21 | 87.50 |
| 1: Hand-crafted Expert | expert | none | 76.61 | 58.93 |
| 2: Expert + Static Update | expert | one-shot | 77.16 | 53.57 |
| 3: Expert + Online Evolution | expert | iterative | 76.34 | **92.86** |
| 4: Scratch + Static Build | scratch | one-shot | 69.49 | 89.29 |
| 5: Scratch + Online Evolution | scratch | iterative | **78.79** | 91.07 |

Mode 5 (no human prior) wins HotpotQA; Mode 3 wins MultiChallenge by recovering from an expert graph that initially hurt performance by 28.57 points.

### Self-Evolution Trace (EnterpriseArena, Gemini 3.5 Flash, 10 rounds)

- Round 1: discovers the sequential backbone (audit cash → forecast runway → financing decision); validation survival jumps 0.0% → 45.0%.
- Round 2: adds `recall_notes` to reuse saved notes; survival reaches 80.0% and tool usage falls from 17.23 to 3.08 calls/month.
- Rounds 3–6: no committed update; one candidate fails structural verification before rollout.
- Round 7: prunes the `pass_action` branch.
- Round 8: introduces an administrative bypass; validation survival reaches 90.0%.
- Round 10: rejected → loop terminates. Test survival of the returned graph: 85.0% vs. baseline 0.0% (Fisher's exact $p=2.6 \times 10^{-8}$).

### Localization Ablation (Table 3)

For the same graph, with Gemini 3.5 Flash:

| Configuration | MultiChallenge | GDPval | ALFWorld |
|---------------|----------------|--------|----------|
| No graph baseline | 80.27 | 54.80 | 72.58 |
| Full graph, raw injection | 86.60 | 57.17 | 70.34 |
| Full graph, generative | 87.35 | 56.75 | 54.48 |
| **Subgraph, generative (Ours)** | **89.31** | **63.99** | **81.53** |

Localization cuts guidance tokens by 70.9% (ALFWorld), 18.1% (GDPval), 14.8% (MultiChallenge) relative to full-graph generative, and shortens solver trajectories on GDPval and ALFWorld.

## Key Takeaways

- **Procedure graphs complement knowledge graphs.** Where a KG answers *what is*, a PG answers *what to do next*. Edges carry not just relation but *condition*, *guidance*, and *pitfalls* — the action-time affordances knowledge graphs do not need.
- **Localize, then verbalize.** Retrieving the connected neighborhood around the current procedure beats full-graph injection on both tokens and quality. The localization radius (h=2) and trajectory window (w=3) are small hyperparameters with large effects.
- **Edit the graph, don't just append text.** Self-evolution changes topology (add/delete nodes and edges) and attributes (re-issue an edge with new guidance). Accept-on-validation gating plus rejection memory provides the safety net.
- **The loop repairs flawed priors.** A bad expert graph can be brought back above baseline by iterative offline editing. This matters for adoption: organizations don't need a perfect starting graph.
- **Compact graphs suffice.** The largest PG used (BFCL v3) has 131 nodes and 265 triplets; most others have ≤ 17 nodes and ≤ 27 triplets. The procedure graph is a small object, not a knowledge-base-scale artifact.
- **Gain correlates with explicit constraints.** Largest margins appear on benchmarks where environmental constraints exist (single-pending financing, sequential action ordering, multi-turn state retention) — PG's value scales with how much the agent benefits from knowing the rules.

## References

- [[Raw/arxiv-procedural-graphs-2026-09-08]] — full paper with all six figures preserved
- [[Concepts/procedural-graph-representation]] — the (procedure, relation, procedure) graph data structure with edge attributes
- [[Concepts/generative-pg-guidance]] — online locate→extract→generate mechanism
- [[Concepts/pg-self-evolution-loop]] — the offline four-step feedback loop
- [[Concepts/rejection-memory-as-negative-constraint]] — safeguard against repeated failed edits
- [[Concepts/localized-subgraph-vs-full-graph-guidance]] — empirical localization finding
- [[Entities/procedural-graph-paper]] — this paper as a research artifact