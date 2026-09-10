---
title: "Rejection Memory as Negative Constraint"
details: "Safeguard mechanism in the Procedural Graph self-evolution loop. When a candidate edit fails the validation gate, the rejected candidate (its edit set, proposed graph, training traces, and validation outcome) is appended to a rejection history $\\mathcal{H}_{\\text{rejected}}$. Subsequent rounds' refiners receive $\\mathcal{H}_{\\text{rejected}}$ as negative evidence so they avoid re-proposing unsuccessful edits. Without rejection memory, iterative self-correction can repeatedly propose equivalent unsuccessful edits; the memory breaks the cycle."
tags: [concepts, agent, llm, self-improving-agents, feedback-loop]
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - .Raw/arxiv-procedural-graphs-2026-09-08.md
  - .Papers/procedural-graphs-2026-09-08.md
---

# Rejection Memory as Negative Constraint

**Source:** [[Raw/arxiv-procedural-graphs-2026-09-08]] · [[Papers/procedural-graphs-2026-09-08]]
**Category:** Learning Mechanism
**Status:** Active research area (introduced Lu et al. 2026)

## Overview

**Rejection memory** is the safeguard in [[Concepts/pg-self-evolution-loop|PG Self-Evolution]] that prevents the loop from re-proposing edits it has already seen fail. It is the negative-evidence counterpart to the validation gate's accept/reject decision: an accepted candidate becomes the next round's starting graph; a rejected candidate becomes part of the context for the next round's refiner.

## Core Content

### The Problem

Iterative self-correction by an LLM refiner can repeatedly propose **equivalent unsuccessful edits**. Without memory of what has already been tried:

- The refiner sees the same failed trajectory partition and proposes a similar edit.
- The candidate fails validation again.
- The refiner sees the same trace partition (now with the failed edit's diagnostic) and proposes another variant.
- The loop thrashes.

This is a well-known pathology in self-reflective agent loops: the same error patterns get verbalized differently across attempts.

### The Mechanism

When the validation gate rejects a candidate, the system records four items in $\mathcal{H}_\text{rejected}$:

| Item | Purpose |
|------|---------|
| $\Delta \mathcal{G}_k$ | The proposed edit set |
| $\mathcal{G}_k^\text{cand}$ | The candidate graph it would have produced |
| $\mathcal{E}_k$ | The training traces the refiner reasoned over |
| $S_\text{val}(\mathcal{G}_k^\text{cand})$ or $d_k$ | The validation outcome or structural-failure diagnostics |

The next round's refiner receives $\mathcal{H}_\text{rejected}$ as additional context:

$$\Delta \mathcal{G}_{k+1} \sim P_\text{refiner}(\cdot \mid \mathcal{G}_k, \mathcal{C}_{k+1}, \mathcal{H}_\text{rejected})$$

Where $\mathcal{C}_k$ is the (tail-trimmed) concatenation of training trajectories.

### Token-Budget Discipline

The trajectory context supplied to the refiner is the concatenation of the current round's traces $\mathcal{E}_k$. When this exceeds $L_\text{max}$ tokens, the implementation drops tokens from the *beginning* while preserving the final $L_\text{max}$ tokens in their original order. The choice to tail-trim rather than head-trim is deliberate: the trajectory *ending* is the operative signal — the most recent failures are what the refiner should reason about.

The same token-budget discipline applies to $\mathcal{H}_\text{rejected}$: prior candidate graphs are serialized into a textual record (`SerializeRejections`) that the refiner can read.

### What "Negative Constraint" Buys You

Three effects, all visible in the paper's results:

1. **Breaks repeated-edit cycles.** The refiner's chance of proposing an edit it has already seen fail drops sharply when the failure context is in $\mathcal{H}_\text{rejected}$.
2. **Surfaces structural failures.** When a candidate fails the structural validator (malformed edit, invalid endpoint, cycle closure), the diagnostic $d_k$ is added to $\mathcal{H}_\text{rejected}$, so the refiner knows *why* it failed structurally — not just that it failed.
3. **Compresses the search space.** Without it, every round is a fresh draw from the refiner's distribution conditioned on the current trajectory; rejection history steers the distribution away from previously rejected regions. This is search-trace compression, not search-termination.

### Worked Example from Appendix F.2 (MultiChallenge)

Validation sample 059 asks for a joke about renewable energy under an earlier "use only passive voice" constraint. The environment exposes the target question "Did the model consistently use passive sentence construction?"

- **Generation 2 candidate** — edge attribute on `AnalyzeTargetQuestion → Finish`: *"Direct finish for simple evaluations without drafting."* Recorded actions: `ParseHistory → AnalyzeTargetQuestion → Finish`. The model emits *"No, the model did not consistently use passive sentence construction."* — i.e. it evaluates the dialogue instead of answering the user. Success indicator: 0.
- **Generation 3** — the direct edge to `Finish` is removed. Guidance on `ExtractConstraints → Finish` now states: *"Do NOT write a meta-evaluation or answer the target question directly."* Recorded actions: `ParseHistory → AnalyzeTargetQuestion → ExtractConstraints → Finish`. Final response: *"A joke about renewable energy is being shared. Why are wind turbines loved by everyone? Many fans are known to be made by them."* Success indicator: 1.

The edge deletion + attribute update is exactly the kind of edit rejection memory is designed to encourage: the refiner saw a meta-evaluation failure, proposed a path through `ExtractConstraints` instead of direct Finish, and the success was recorded.

### What Rejection Memory Is *Not*

- **It is not a permanent failure blacklist.** A rejection at round $k$ does not forbid the same edit at round $k + 10$. It only informs the refiner about prior failures, similar to how a human researcher would remember their last dead end.
- **It is not prioritized over recent trajectories.** The rejection history is appended context; the current round's trajectory partition $\mathcal{C}_{k+1}$ remains the primary signal.
- **It is not bounded by size.** The token budget $L_\text{max}$ is the only constraint; prior rejections accumulate across rounds until the serializer hits the limit and trims from the front.

## Key Insights

1. **Negative evidence is half of search.** Most self-improvement loops only learn from accepted edits. PG's design treats rejected edits as first-class signal — the same refiner that proposes an edit also reads prior rejections when proposing the next.
2. **Tail-trim, not head-trim.** Dropping tokens from the beginning of long trajectories preserves the most recent (and operationally relevant) signal. This is a small choice with large effects on what the refiner reasons about.
3. **Structural diagnostics are signal too.** When a candidate fails before validation rollout, $d_k$ is recorded. The next refiner learns *why* the structural validator rejected the edit, not just that validation said no.
4. **The mechanism is general.** Any iterative-edit loop with an LLM proposer and a validation gate can use the same pattern: append rejected candidates to a negative-evidence buffer, include it in the proposer's context on subsequent rounds.

## Related Concepts

- [[Concepts/pg-self-evolution-loop]] — the loop this mechanism safeguards
- [[Concepts/procedural-graph-representation]] — the object being edited
- [[Concepts/generative-pg-guidance]] — the inference-time consumer
- [[Concepts/friction-logging-for-agents]] — adjacent pattern: log agent friction events to learn from them
- [[Concepts/agent-self-improvement]] — broader family of self-improvement mechanisms
- [[Concepts/human-approval-as-graph-edge]] — analogous "gate" pattern, but for human-in-the-loop

## References

- Raw: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Paper: [[Papers/procedural-graphs-2026-09-08]]
- Original: https://arxiv.org/html/2606.09153v1 (§3.3 Step 4, Appendix B.6, Appendix F.2)