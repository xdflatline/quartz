---
title: "Trajectory-Recall Reward Term"
details: "RL reward-shaping pattern for multi-turn retrieval agents: add a process-level trajectory-recall term to the outcome reward, crediting the agent for encountering relevant documents during search even if they are later pruned from the final output set. Chroma Context-1 (Bashir et al., March 2026) uses `r = 0.7·F_β + 0.3·r_traj + r_fa − penalties`, with r_traj as 30% of the pre-penalty weight. Prevents a degenerate 'one broad search and stop' policy that would score well on output F1 alone but fails to explore the corpus."
tags:
  - concept
  - training
  - llm
  - agent
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/chroma-context-1-2026-03.md
related:
  - "[[Concepts/f-beta-reward-curriculum]]"
  - "[[Concepts/reinforcement-learning-grpo]]"
  - "[[Concepts/agentic-self-pruning-context]]"
---

# Trajectory-Recall Reward Term

**Source:** [[Raw/chroma-context-1-2026-03]]
**Category:** RL Reward Design
**Related:** [[Concepts/f-beta-reward-curriculum]], [[Concepts/reinforcement-learning-grpo]], [[Concepts/agentic-self-pruning-context]]

## Overview

In multi-turn retrieval, the agent's *trajectory* — the full sequence of tool calls and observations — contains far more information than its *final output* (the ranked document set it returns). A document that was retrieved, read, and then pruned is invisible to any output-level metric, but the agent's decision to retrieve it was correct.

A **trajectory-recall reward term** credits the agent for documents it encountered at any point during search, regardless of whether they appear in the final output. The full reward in Context-1 is:

> `r = clamp(0.7 · F_β + 0.3 · r_traj + r_fa − p_prune − p_turn, ε, r_pre)`

where `r_traj` is trajectory recall — the fraction of target documents the agent encountered during search. It is weighted at 30% of the pre-penalty reward.

## Why It Matters

Without `r_traj`, the agent can converge to a degenerate strategy:

> Issue one or two broad searches covering most of the corpus, return whatever came back, stop.

This can score well on output-level F1 if the broad searches happened to surface enough relevant documents. But it is not a *search* policy; it is a *dump-and-stop* policy. The model never learns to choose between documents, never learns to prune aggressively to make room for further search, never learns the core skill of multi-hop retrieval.

Adding `r_traj` couples the reward to exploration: even if documents are pruned later, the agent is rewarded for having found them. This is particularly important for [agentic self-pruning]([[Concepts/agentic-self-pruning-context]]) because pruning decisions are imperfect early in training — without the trajectory credit, the gradient would push the model away from pruning at all (since pruning reduces output recall) even when the search trajectory was correct.

## Implementation Detail: Preserving the Unpruned Trajectory

`r_traj` is only computable if the reward signal sees the *unpruned* trajectory. Context-1's harness preserves this:

> When the model calls `prune_chunks`, the harness removes the specified chunks from the model's view but preserves the full unpruned trajectory for reward computation.

This is the key design choice that makes the term possible. Without this split, pruning would hide evidence from the reward, and `r_traj` would be undefined.

## Weighting in Context-1

30% of pre-penalty weight is a substantial fraction — comparable to the F_β outcome component's contribution (70%). This signals that exploration is treated as roughly co-equal with selection. Without the trajectory term, the outcome component alone would over-emphasize final-output selection.

A smaller weight (say, 5–10%) would still help but not as strongly; the [paper]([[Raw/chroma-context-1-2026-03]]) does not ablate this directly, but the qualitative argument is that trajectory recall is the only signal that prevents the dump-and-stop collapse.

## Comparison to Outcome-Only Rewards

A pure outcome-only reward (just F_β, no `r_traj`) would also be workable but has the failure mode above. Other process reward formulations exist:

- **Per-step credit assignment** — credit each tool call for the documents it eventually led to. Higher variance, requires credit assignment across steps.
- **Dense intermediate rewards** — reward each successful retrieval as it happens. Same variance issue.
- **Trajectory recall (this page)** — coarse, low-variance, computed at episode end. Trades resolution for stability.

Context-1 uses trajectory recall because it composes well with within-group GRPO normalization (8 rollouts per query compete on their relative rewards) and CISPO clipping.

## When to Use

The pattern applies when:

- The agent performs multi-turn search or tool use.
- The output is a subset of the trajectory's evidence (documents, candidates, items).
- Selection is imperfect and worth learning.
- You want to prevent the degenerate "broad-then-stop" policy.

When *not* to use: when the trajectory and output are nearly identical (single-step retrieval, no pruning), or when process-level decisions are already well-shaped by supervised data.

## Related Work

- GRPO and CISPO — the policy optimization framework Context-1 uses; within-group normalization is what makes `r_traj`'s coarse signal sufficient.
- Outcome-supervised reward models (ORM) vs process-supervised reward models (PRM) — `r_traj` is closer to a coarse PRM that aggregates over the whole trajectory.
- MemGPT / ReSum — different mechanisms (external memory, summarization) for managing the same trajectory-vs-output tension.
