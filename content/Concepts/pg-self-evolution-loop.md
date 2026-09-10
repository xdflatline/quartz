---
title: "PG Self-Evolution Loop"
details: "Offline four-step feedback loop that revises a Procedural Graph from execution traces. Starting from a retained graph $\\mathcal{G}_{k-1}$ with cached validation score $S_{k-1}$, each round runs: (1) diagnostic rollout on a training batch and partition traces by score, (2) feedback-driven mutation by an LLM refiner that emits a structured edit set (add/delete nodes and edges, attribute updates via delete-then-add), (3) validation gating on a held-out set (accept iff validation score does not decrease, ties allowed), and (4) rejection memory that records rejected candidates and serves them as negative evidence to subsequent rounds. The loop can build effective graphs from a minimal skeleton or repair flawed expert priors."
tags: [concepts, agent, llm, self-improving-agents, feedback-loop]
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - .Raw/arxiv-procedural-graphs-2026-09-08.md
  - .Papers/procedural-graphs-2026-09-08.md
---

# PG Self-Evolution Loop

**Source:** [[Raw/arxiv-procedural-graphs-2026-09-08]] · [[Papers/procedural-graphs-2026-09-08]]
**Category:** Learning Mechanism
**Status:** Active research area (introduced Lu et al. 2026)

## Overview

The self-evolution loop is the offline counterpart to [[Concepts/generative-pg-guidance|Generative PG Guidance]]. Where guidance is a per-step read of the graph, the evolution loop is a periodic *write*: it observes how the solver performs with the current graph, proposes edits, validates the edit on a held-out set, and either commits or records the rejection. The loop runs between training batches, not within episodes — the graph is frozen during inference and validation rollouts.

## Core Content

### The Four Steps

For round $k = 1, \dots, K$, starting from retained graph $\mathcal{G}_{k-1}$ with cached score $S_{k-1}$:

**Step 1: Diagnostic Rollout**

Run the solver on a training batch $\mathcal{B}_k \subset \mathcal{D}_\text{train}$ using the current graph $\mathcal{G}_{k-1}$. Record traces and scores:

$$\mathcal{E}_k = \{ (q_i, \mathcal{T}_i^{(k)}, S_i^{(k)}) \}_{i=1}^{|\mathcal{B}_k|}$$

Traces are partitioned into high-scoring and low-scoring subsets (or successes vs. failures for binary outcomes) and supplied to the refiner as contrastive evidence.

**Step 2: Feedback-Driven Mutation**

An offline LLM refiner inspects the partitioned traces and identifies repeated error loops in failure trajectories plus multi-step reasoning shortcuts in successful runs. It emits a structured edit set $\Delta \mathcal{G}_k$:

- `add_nodes` — insert missing verification nodes
- `add_edges` — insert transitions (with condition / guidance / pitfalls attributes)
- `delete_nodes` — remove nodes that repeatedly steer trajectories into failure
- `delete_edges` — remove edges that prevent progress or lead to loops

Attribute revisions use the same interface: an edge is deleted and re-added with updated attribute values. This applies to any attribute in the schema, so the same refiner prompt handles structural and textual mutation uniformly.

The candidate graph is obtained by applying edits to a copy:

$$\mathcal{G}_k^\text{cand} = \mathcal{G}_{k-1} \oplus \Delta \mathcal{G}_k$$

The copy operation also performs any configured cycle repair.

**Step 3: Validation Gating**

A structurally valid candidate is evaluated on an independent validation set $\mathcal{D}_\text{val}$:

$$S_\text{val}(\mathcal{G}) = \frac{1}{|\mathcal{D}_\text{val}|} \sum_{(q,y) \in \mathcal{D}_\text{val}} S(f_{\text{solver}}(q \mid \mathcal{G}), y)$$

The initial graph is evaluated once to establish the reference score. For a structurally valid candidate, the retained graph is updated as:

$$\mathcal{G}_k = \begin{cases} \mathcal{G}_k^\text{cand}, & \text{if } S_\text{val}(\mathcal{G}_k^\text{cand}) \ge S_{k-1} \\ \mathcal{G}_{k-1}, & \text{otherwise} \end{cases}$$

Ties are accepted (the $\ge$ comparison). Structurally invalid candidates are discarded before validation rollout — the retained graph and its cached validation score are unchanged.

**Step 4: Rejection Memory as Negative Evidence**

Rejected candidates are appended to a rejection history $\mathcal{H}_\text{rejected}$, together with the proposed edits, the associated training traces $\mathcal{E}_k$, and the validation outcome. For the trajectory context supplied to the refiner, when the configured token budget $L_\text{max}$ is exceeded, tokens are dropped from the *beginning* while preserving the final $L_\text{max}$ tokens in their original order (a "tail" operation). The refiner for round $k+1$ receives $\mathcal{H}_\text{rejected}$ as negative evidence:

$$\Delta \mathcal{G}_{k+1} \sim P_\text{refiner}(\cdot \mid \mathcal{G}_k, \mathcal{C}_{k+1}, \mathcal{H}_\text{rejected})$$

This discourages the refiner from re-proposing edits it has already seen fail. The graph stays fixed during each training or validation episode; only between rounds does it change.

### Algorithm 1 (Offline Closed-Loop Self-Evolution)

The retained-checkpoint state is explicit: $\mathcal{G}_0$ is the initial graph; $\mathcal{D}_\text{train}$, $\mathcal{D}_\text{val}$ are fixed; $K$ is the round budget; $L_\text{max}$ is the trajectory token limit; $c$ is the cycle policy.

```
S_0 = Evaluate(G_0, D_val)
H_rejected = []
for k = 1, ..., K:
    G_k = G_{k-1}; S_k = S_{k-1}                # retain unless accepted
    B_k = sample(D_train)
    E_k = Rollout(G_{k-1}, B_k)                 # training traces + scores
    C_k = Tail_{L_max}(ConcatTrajectories(E_k))
    R_k = SerializeRejections(H_rejected)
    DeltaG_k = Refiner(G_{k-1}, C_k, scores, R_k)
    (G_k_cand, d_k) = PrepareCandidate(G_{k-1}, DeltaG_k, c)
    if d_k != empty:
        H_rejected.append(...)
        continue                                  # structural fail, no rollout
    S_k_cand = Evaluate(G_k_cand, D_val)
    if S_k_cand >= S_{k-1}:
        G_k = G_k_cand; S_k = S_k_cand           # accept, ties included
    else:
        H_rejected.append(...)
return G_K
```

### Structural Validator

`PrepareCandidate` applies edits to a copy of the retained graph (deletes before adds), runs structural checks, and reports diagnostics $d_k$ on failure:

- malformed edit shapes
- invalid node or relation types
- missing edge endpoints
- cycle-closing edges (when cycles are disallowed, these are removed before validation)
- reachability: every node must have a directed path to a terminal node (zero out-degree). Not specifically to the node named `End`.

Action-node names matching the available tool catalog is enforced *by the refiner prompt*, not by the structural validator — the validator does not independently check tool-catalog membership.

### Worked Trace: 10-Round Evolution on EnterpriseArena

Gemini 3.5 Flash CFO simulator, baseline validation survival 0.0% (34.8 month mean lifespan):

| Round | Outcome | Change | Val. Survival |
|-------|---------|--------|---------------|
| 1 | Accepted | Discovers the sequential backbone (audit cash → forecast runway → financing decision) | 0.0% → 45.0% |
| 2 | Accepted | Adds `recall_notes` to reuse Round 1's saved notes; tool usage 17.23 → 3.08 calls/month | 45.0% → 80.0% |
| 3–6 | No commit | One candidate fails structural verification before rollout | 80.0% (held) |
| 7 | Accepted | Prunes `pass_action` branch | 80.0% → ~85% |
| 8 | Accepted | Introduces administrative bypass | 85% → 90.0% |
| 9 | Accepted | Refinement | 90.0% (held) |
| 10 | Rejected | Edit fails validation | 90.0% (held) |

Returned graph: test survival 85.0% vs. baseline 0.0% (Fisher's exact $p = 2.6 \times 10^{-8}$).

### Construction Modes Compared

The paper benchmarks five initializations / update schedules head-to-head:

| Mode | Initialization | Update Schedule |
|------|----------------|------------------|
| 1 | Hand-crafted expert | none (zero-shot) |
| 2 | Hand-crafted expert | one-shot static |
| 3 | Hand-crafted expert | iterative online evolution |
| 4 | Scratch (`Start → End`) | one-shot static build |
| 5 | Scratch (`Start → End`) | iterative online evolution |

Mode 5 (no human prior, iterative) wins HotpotQA F1 (78.79%) and is second-best on MultiChallenge (91.07%). Mode 3 wins MultiChallenge (92.86%) by repairing an expert graph that initially drops success from 87.50% → 58.93%.

## Key Insights

1. **Validate on held-out, never on training.** The validation set $\mathcal{D}_\text{val}$ is disjoint from both training and test. The accept gate consumes validation performance, so training-set overfitting does not enter the loop's decisions.
2. **Ties are accepted.** The gate is $\ge$, not $>$. This avoids thrashing when scores are noisy at small validation-set sizes; the loop terminates by round budget, not by a strict-improvement requirement.
3. **Delete-then-add for attribute updates.** Refining an edge's guidance is implemented as a deletion followed by an addition. This keeps the edit interface uniform and the structural validator trivially checks endpoint validity.
4. **Rejection memory prevents loop pathologies.** Iterative self-correction can repeatedly propose equivalent unsuccessful edits without negative evidence. Appending rejected candidates to $\mathcal{H}_\text{rejected}$ and feeding them back as negative examples breaks the cycle.
5. **Tail-trim, not head-trim, on long traces.** When trajectory context exceeds $L_\text{max}$, drop tokens from the *beginning* — the recent trajectory is the operative signal for the refiner. This is a small but principled design choice.
6. **A bad prior is recoverable.** The Mode 1→3 progression on MultiChallenge (58.93% → 92.86%) demonstrates that the loop can edit its way out of a flawed initialization. This lowers the adoption bar: the initial graph doesn't need to be perfect.
7. **Cycle policy is configurable.** When cycles are allowed, the cycle-closing repair and acyclicity check are skipped. The default policy in the experiments is cycles-disallowed, but the framework accommodates both.

## Related Concepts

- [[Concepts/procedural-graph-representation]] — the data structure being edited
- [[Concepts/generative-pg-guidance]] — the inference-time consumer of the graph
- [[Concepts/rejection-memory-as-negative-constraint]] — the safeguard mechanism (Step 4)
- [[Concepts/evolutionary-search-for-harnesses]] — related family: harness-level evolution
- [[Concepts/darwin-godel-machine]] — broader self-improvement lineage
- [[Concepts/agent-self-improvement]] — general agent self-improvement concept
- [[Concepts/friction-logging-for-agents]] — alternative trajectory-based learning signal
- [[Concepts/dataset-creation]] — the trajectories here serve as the training corpus

## References

- Raw: [[Raw/arxiv-procedural-graphs-2026-09-08]]
- Paper: [[Papers/procedural-graphs-2026-09-08]]
- Original: https://arxiv.org/html/2609.09153v1 (§3.3, §5.3, §5.4, Appendix B.6, Appendix E)