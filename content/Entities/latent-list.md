---
title: "Latent List"
details: "Latent List — a task introduced as part of the Michelangelo evaluation framework (Vodrahalli et al., 2024). The model performs a fixed number of Python list operations (append, pop, slice, etc.) across varying input lengths. Demonstrates that the *type* of irrelevant filler matters: locally-cancelling list operations degrade performance more than print-statement filler. Insights were clarified by Kiran Vodrahalli (Google DeepMind) in July 2026."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://arxiv.org/abs/2409.12640
---

# Latent List

**Paper context:** Vodrahalli et al. (2024). "Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries." arXiv:2409.12640.
**URL:** <https://arxiv.org/abs/2409.12640>
**Clarifications:** Kiran Vodrahalli (Google DeepMind), July 2026

## Overview

**Latent List** is the canonical task introduced by Michelangelo. The model is given a list of Python list values embedded in a long context, plus a sequence of list operations (e.g. `append(x); pop(); slice(0, 5)`), and must execute the operations and report the final list state.

## The variable-filler design

The list is small (fixed size), but the surrounding context is padded with various kinds of irrelevant content:

| Filler type | Description |
|---|---|
| **None** | Minimal context, just the list and operations |
| **Print statements** | Repeating `print("...")` lines |
| **Locally-cancelling ops** | Additional list operations that net to no change (e.g. `append(x); pop()`) |

The finding: **locally-cancelling operations degrade model performance more than print statements**, even at the same filler token count. This suggests filler that is syntactically similar to the operative content imposes a higher processing cost than filler that is syntactically distinct.

## Relation to Chroma's distractor-resistance findings

Chroma's [[Concepts/distractor-resistance]] is a controlled extension of this principle: topically related distractors (similar in *semantic* content) degrade retrieval more than unrelated distractors, and the degradation amplifies with input length. Both Latent List and Chroma's distractor study conclude that **irrelevant content is not a neutral container**.

## Why this matters for evaluation design

Latent List is the cleanest demonstration that **the choice of filler matters for benchmark results**. Two long-context benchmarks with the same number of tokens but different filler types can produce meaningfully different scores. Benchmark publishers should disclose filler choice and ideally report sensitivity to it.

## Related Pages

- Entity: [[Entities/michelangelo]] — the parent framework
- Concept: [[Concepts/distractor-resistance]] — Chroma's controlled extension