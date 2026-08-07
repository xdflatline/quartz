---
title: "ShinkaEvolve"

details: "ShinkaEvolve is the sample-efficiency-focused descendant of AlphaEvolve. The three new components — parent sampling balance, code-novelty rejection, meta-scratchpad — together address the two failure modes of LLM-driven evolutionary search: clonal dominance (one parent producing all offspring) and mode collapse (population converging to a single shape)."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2509.19349
---

# ShinkaEvolve

**Source:** Lange, Imajuku, and Cetin, "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution," arXiv:2509.19349, 2025.

## Overview

The **sample-efficiency-focused** descendant of [[Entities/alphaevolve]]. Three new components address the two failure modes of LLM-driven evolutionary search: clonal dominance and mode collapse.

## The Three Components

1. **Parent sampling balance** — pick parents with a probability that trades off performance rank and offspring count. Prevents the best candidate from producing all offspring.
2. **Code-novelty rejection sampling** — discard candidates too similar to the existing population based on embedding-based cosine similarity. Prevents mode collapse.
3. **Meta-scratchpad** — record patterns from successful solutions to guide future mutation. Curated memory of what worked.

## Related

- [[Entities/alphaevolve]] — the parent
- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Concepts/diversity-collapse-rsi]] — the failure mode ShinkaEvolve's components address
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
