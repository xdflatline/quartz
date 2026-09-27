---
title: "F-Beta Reward Curriculum (Recall → Precision)"
details: "RL fine-tuning curriculum pattern in which the F_β weighting of the outcome reward is annealed across training epochs from a recall-heavy bias to a more precision-balanced one. Chroma Context-1 (Bashir et al., March 2026) anneals β from 4 (recall weighted 16x more than precision) at initialization to β = 2 (recall weighted 4x more than precision) by training end — a 4x reduction in recall-vs-precision asymmetry over 5 epochs. Pairs naturally with a difficulty curriculum that shifts query mix from low-hop to high-hop. Generalizes to any task where recall and precision are co-measured and the model must first explore broadly, then narrow. Distinct from [Dynamic Reward Curriculum for RL Fine-Tuning]([[Concepts/dynamic-reward-curriculum-rl-finetuning]]), which tightens a continuous-distance reward's decay coefficient rather than the recall-vs-precision axis."
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
  - "[[Concepts/dynamic-reward-curriculum-rl-finetuning]]"
  - "[[Concepts/trajectory-recall-reward]]"
  - "[[Concepts/reinforcement-learning-grpo]]"
---

# F-Beta Reward Curriculum (Recall → Precision)

**Source:** [[Raw/chroma-context-1-2026-03]]
**Category:** RL Training Methodology
**Related:** [[Concepts/dynamic-reward-curriculum-rl-finetuning]], [[Concepts/trajectory-recall-reward]], [[Concepts/reinforcement-learning-grpo]]

## Overview

F_β is a weighted harmonic mean of precision and recall, with `β > 1` weighting recall more than precision and `β < 1` weighting precision more. When β = 4, recall is weighted 16x more than precision. When β = 2, recall is weighted 4x more.

Chroma Context-1's reward is built around an F_β outcome term that is annealed across training:

> `r = clamp(0.7 · F_β + 0.3 · r_traj + r_fa − p_prune − p_turn, ε, r_pre)`

with β going from 4 to 2 over the course of training. This is a curriculum *within* the reward function itself, complementary to a difficulty curriculum that shifts the query distribution from low-hop to high-hop tasks.

## Why a Recall-First Curriculum

The intuition: early in training the model has not yet learned to search well. If the reward is too precision-heavy at this stage, the gradient will reinforce cautious, narrow searches that may miss documents the agent never even encountered. By weighting recall 16x, the agent is rewarded for finding relevant documents regardless of how much noise it accumulates — exploration is incentivized even when the final output is messy.

As training progresses and the agent becomes competent at searching and pruning, the precision bias can be safely increased. The model now has the search skill to find documents; what it lacks is the selection skill to keep only the relevant ones. β = 2 still weights recall 4x more than precision, so missing a critical document remains more costly than including noise, but the model is now expected to discriminate.

The asymmetry never disappears entirely. This reflects the architectural role: Context-1 is a retrieval subagent feeding a downstream answering model. The downstream model can filter noise but cannot recover information that was never retrieved. Missing a critical document is irreversible; including an irrelevant one is recoverable.

## Pairing With a Difficulty Curriculum

The F_β curriculum is paired with a difficulty curriculum on the query side:

- **Phase 1** — query distribution skewed toward lower-difficulty (fewer hops).
- **Phase 2** — query distribution skewed toward higher-difficulty multi-hop tasks.

This phasing allows a reasonable policy to be learned before exposing the model to problems where near-zero reward is likely without an already-competent search policy. Both curricula operate together: difficulty controls what the model sees; F_β controls how its performance on those tasks is rewarded.

## Generalization

The pattern applies anywhere:

- The agent's output is a set (documents, candidates, items to act on).
- Both recall and precision are well-defined over that set.
- The cost of missing a true positive is higher than the cost of a false positive.
- The model must first develop broad search/recall capability before it can usefully narrow to precision.

Other examples where the pattern could apply:

- **Candidate generation** for ranking models — first recall-heavy, then precision-balanced as the ranker improves.
- **Alert triage** — first surface everything that could match, then narrow to high-precision.
- **Citation generation** — first find any potentially relevant source, then filter for direct support.

## Comparison to Other Reward Curricula

| Pattern | What is annealed | Source |
| --- | --- | --- |
| **F_β reward curriculum (this page)** | Recall-vs-precision weighting in the outcome reward | [Context-1]([[Raw/chroma-context-1-2026-03]]) |
| **Dynamic Reward Curriculum for RL Fine-Tuning** | Decay coefficient of a continuous-distance rule-based reward | Time-R1 (Liu et al., 2025) |
| **Three-stage RL curriculum (temporal reasoning)** | Difficulty phases over reasoning depth | Time-R1 |

The F_β pattern is specifically about the *metric shape*, not the *task difficulty* (covered by the difficulty curriculum) and not the *reward distance function* (covered by Time-R1's pattern).

## When Not to Use

- When precision and recall are equally costly — use β = 1 (plain F1) and skip the curriculum.
- When the model is already precision-bound at training start — annealing from β = 4 will hurt early learning.
- When the output is not a set (e.g., free-form generation). F_β is a set-comparison metric; it doesn't apply.
