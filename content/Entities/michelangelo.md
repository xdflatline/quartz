---
title: "Michelangelo (Long-Context Evaluation)"
details: "Michelangelo (Vodrahalli et al., 2024; arXiv:2409.12640) — long-context evaluation framework that goes beyond NIAH via latent structure queries. Introduces Latent List, a task where the model performs a fixed number of Python list operations across varying input lengths. Reveals that the type of irrelevant filler matters: locally-cancelling list operations degrade performance more than adding print statements."
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

# Michelangelo (Long-Context Evaluation)

**Paper:** Vodrahalli, Ontanon, Tripuraneni, Xu, Jain, Shivanna, Hui, Dikkala, Kazemi, Fatemi, et al. (2024). "Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries." arXiv:2409.12640.
**URL:** <https://arxiv.org/abs/2409.12640>

## Overview

**Michelangelo** is a long-context evaluation framework that uses **latent structure queries** — tasks that require the model to operate on a structured representation embedded in the input, rather than retrieve a specific span.

The canonical example task introduced by Michelangelo is **Latent List** ([[Entities/latent-list]]): a Python list of values is embedded in the prompt, and the model must perform a fixed sequence of operations (e.g. append, pop, sort, slice) regardless of how much irrelevant context surrounds the list.

## The "type of filler matters" finding

Michelangelo's Latent List varies the **kind** of irrelevant content used to pad the input. Three conditions were tested:

1. **No filler** — minimal context
2. **Print-statement filler** — repeating `print("...")` lines
3. **Locally-cancelling list operations** — additional list ops that cancel each other out (e.g. `append(x); pop()`)

The key finding: locally-cancelling list operations degrade model performance **more significantly** than print statements, even though both add the same number of tokens. This suggests that the *content* of the filler matters — filler that is syntactically similar to the operative content imposes a higher processing cost than filler that is syntactically distinct.

## Relation to Chroma's findings

Chroma's [[Concepts/distractor-resistance]] is a controlled extension of this principle: instead of irrelevant filler, Chroma tested **topically related distractors** and found a similar non-uniform, content-dependent degradation pattern. The two studies converge on the same conclusion: irrelevant content is not a neutral container.

## Related Pages

- Entity: [[Entities/latent-list]] — the specific Michelangelo task
- Entity: [[Entities/mrcr]] — the related Multi-Round Co-Reference Resolution benchmark
- Concept: [[Concepts/distractor-resistance]] — Chroma's extension of this idea