---
title: "NoLiMa"
details: "NoLiMa (Modarressi et al., 2025; arXiv:2502.05167) — long-context evaluation benchmark for non-lexical matching. Needle-question pairs require the model to make latent associations using world knowledge (e.g. Kiasma museum → Helsinki). 72.4% of NoLiMa's needle-question pairs require external knowledge. Surfaces context rot on tasks where direct lexical overlap is absent."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://arxiv.org/abs/2502.05167
---

# NoLiMa

**Paper:** Modarressi, Deilamsalehy, Dernoncourt, Bui, Rossi, Yoon, Schütze (2025). "NoLiMa: Long-Context Evaluation Beyond Literal Matching." arXiv:2502.05167.
**URL:** <https://arxiv.org/abs/2502.05167>

## Overview

**NoLiMa** ("No Literal Matching") is a long-context evaluation benchmark designed to test whether LLMs can handle needle-question pairs that require **inference over latent associations** rather than direct lexical overlap.

The canonical example:

> **Question:** Which character has been to Helsinki?
> **Needle:** Actually, Yuki lives next to the Kiasma museum.

Answering this requires:
1. World knowledge: Kiasma museum is in Helsinki.
2. Latent association: "next to Kiasma" → "in Helsinki."
3. Entity matching: the "character" the question refers to (Yuki).

## The 72.4% world-knowledge point

72.4% of NoLiMa's needle-question pairs require such external world knowledge. This makes the benchmark closer to a test of *combined* non-lexical matching + world-knowledge retrieval than a pure test of either capability.

The implication for evaluation: a model that fails on NoLiMa might be failing on either the non-lexical matching or the world-knowledge layer. Chroma's Context Rot study ([[Raw/chroma-context-rot-2026-07]]) addresses this by varying **needle-question similarity continuously** rather than binarily, which can disentangle the two factors.

## Relation to Chroma's findings

Chroma (2026) used NoLiMa as the motivating example for why NIAH's binary lexical/non-lexical classification is too coarse. They built on NoLiMa's approach — non-lexical needle-question pairs — but extended it with continuous similarity quantification via five-embedder cosine averages.

## Related Pages

- Concept: [[Concepts/needle-question-similarity]] — Chroma's continuous extension
- Entity: [[Entities/needle-in-a-haystack-benchmark]] — the lexical predecessor