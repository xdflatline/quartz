---
title: "Needle in a Haystack (NIAH) Benchmark"
details: "Long-context evaluation benchmark introduced by Greg Kamradt (2023). A random fact ('needle') is placed in a long context window ('haystack'), and the model is asked to retrieve it. Standard NIAH uses needle-question pairs with direct lexical overlap, which frontier models solve near-perfectly across their full context windows — leading to the misleading perception that long-context is solved. Chroma (2026) extended NIAH along four axes: needle-question similarity, distractor density, needle-haystack similarity, and haystack structure."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://github.com/gkamradt/LLMTest_NeedleInAHaystack
---

# Needle in a Haystack (NIAH) Benchmark

**Original Repo:** <https://github.com/gkamradt/LLMTest_NeedleInAHaystack>
**Introduced by:** Greg Kamradt, 2023
**Original task setup:** place a needle (random fact) inside a haystack (long document of unrelated text), ask the model to retrieve the needle.

## Overview

NIAH is the most widely used long-context evaluation benchmark. It is appealing because it is **scalable** — you can make the haystack as long as the model's context window — and it has a clear pass/fail criterion: did the model retrieve the needle.

The default haystack in Kamradt's original implementation is a series of **Paul Graham essays**, with a single random sentence (e.g. "The best thing to do in San Francisco is eat a sandwich at the park") inserted at varying positions. The model is then asked "What is the best thing to do in San Francisco?"

## The lexical-overlap limitation

Standard NIAH uses needle-question pairs with **direct lexical matches**. The question "What is the best thing to do in San Francisco?" overlaps almost word-for-word with the needle "The best thing to do in San Francisco is eat a sandwich at the park." This makes the task solvable by surface-level pattern matching — exactly the strength of attention heads in transformer LLMs.

As a result, **frontier models score near-perfect on NIAH across their full context windows** — 128k, 200k, even 1M tokens. This produced the widespread (incorrect) perception that long-context is solved.

## Chroma's extensions (2026)

Chroma's Context Rot report ([[Raw/chroma-context-rot-2026-07]]) extends NIAH along four axes:

| Axis | What it varies | Related concept |
|---|---|---|
| **Needle-question similarity** | Continuous cosine similarity of needle vs. question embeddings, replacing binary lexical/non-lexical | [[Concepts/needle-question-similarity]] |
| **Distractor density** | Number of topically related non-answering spans added to the haystack | [[Concepts/distractor-resistance]] |
| **Needle-haystack similarity** | Whether the needle topically blends into the haystack | [[Concepts/needle-haystack-similarity]] |
| **Haystack structure** | Coherent vs. shuffled sentence ordering within the haystack | [[Concepts/haystack-structure-effect]] |

## Variants and related benchmarks

- **NoLiMa** ([[Entities/nolima]]) — non-lexical needle-question pairs; latent associations required
- **AbsenceBench** ([[Entities/absencebench]]) — tests whether models can recognize the *absence* of a snippet
- **MRCR** ([[Entities/mrcr]]) — multi-round co-reference resolution, the i-th instance retrieval
- **Michelangelo** ([[Entities/michelangelo]]) — long-context evaluation via latent structure queries
- **Latent List** ([[Entities/latent-list]]) — fixed list operations across varying input lengths
- **Graphwalks** ([[Entities/graphwalks]]) — graph traversal with input length scaling the graph size
- **LongMemEval** ([[Entities/longmemeval]]) — conversational QA with retrieval + reasoning

## Why NIAH remains useful

Despite its limitations, NIAH is still a useful **smoke test** for whether a model can find a clearly-located span in a long context. Its problem is **not that it is wrong** — it is that it has been treated as sufficient when it is in fact necessary-but-not-sufficient. The pattern: NIAH + at least one of NoLiMa / MRCR / LongMemEval / repeated-words / distractor test is the minimum bar for "long-context capable."

## Related Pages

- Concept: [[Concepts/needle-question-similarity]]
- Concept: [[Concepts/distractor-resistance]]
- Concept: [[Concepts/needle-haystack-similarity]]
- Concept: [[Concepts/haystack-structure-effect]]
- Raw: [[Raw/chroma-context-rot-2026-07]]