---
title: "Needle-Haystack Similarity"
details: "A controlled NIAH variant introduced by Chroma (2026): the same needle is placed in two thematically distinct haystacks (PG essays, arXiv papers), and the average cosine similarity of the needle to the top-5 haystack chunks is measured across five embedders. Needle-haystack similarity has a non-uniform effect on model performance — for PG haystacks, low-similarity arXiv needles outperform high-similarity PG needles, but for arXiv haystacks the effect is minimal. Suggests the haystack topic itself acts as a processing cost."
tags:
  - concepts
  - llm
  - evaluation
  - context-engineering
created: 2026-09-25
updated: 2026-09-25
type: concept
sources:
  - "Raw/chroma-context-rot-2026-07.md"
---

# Needle-Haystack Similarity

**Source:** [[Raw/chroma-context-rot-2026-07]]
**Category:** Evaluation Methodology
**Related:** [[Concepts/context-rot]], [[Concepts/needle-question-similarity]], [[Concepts/distractor-resistance]]

## Overview

**Needle-haystack similarity** is the degree to which a needle topically blends into the surrounding text of the haystack. Standard NIAH assumes the haystack is a neutral container — change its topic, and retrieval should still succeed. Chroma's Context Rot study (July 2026) tests this assumption by placing the same needles in two thematically distinct haystacks and measuring the effect on performance.

## How it's measured

1. **Two haystacks**: Paul Graham essays (as in the original NIAH) and arXiv papers (the `jamescalam/ai-arxiv2` dataset).
2. **Two needle sets**: PG-themed needles (about writing advice) and arXiv-themed needles (about re-ranking).
3. **Similarity score**: for each needle, embed the haystack, retrieve the top-5 most similar chunks, average their cosine similarities. Repeat across five embedding models for robustness.

The resulting similarity matrix (from the paper):

| | PG haystack | arXiv haystack |
|---|---|---|
| **PG needle** | mean 0.529, σ 0.101 | mean 0.394, σ 0.105 |
| **arXiv needle** | mean 0.368, σ 0.111 | mean 0.654, σ 0.086 |

The diagonal entries are the cases where needle and haystack match topically (high similarity); the off-diagonal entries are the cross-topic cases (low similarity).

## Headline empirical finding

The effect is **non-uniform and haystack-dependent**:

- **PG haystack**: arXiv needles (low similarity, mean 0.368) outperform PG needles (high similarity, mean 0.529). The needle that *blends in* is the harder one to retrieve.
- **arXiv haystack**: arXiv needles and PG needles perform nearly identically. The haystack topic dominates.

This means **needle-haystack similarity is not a single-direction variable**: in some haystacks, blending in hurts retrieval; in others, it has no effect.

## Why it matters

Standard NIAH evaluation treats haystack topic as irrelevant. Chroma's results say: the haystack topic itself is a processing cost, and a needle that topically matches its haystack can pay that cost by being harder to isolate. This complicates the comparison of model long-context performance across papers — if every paper uses a different haystack (PG essays, arXiv, Wikipedia, codebases), the "needle in haystack" score is not directly comparable.

## Limitations of the study

Chroma explicitly notes that testing across only two topics is **insufficient to generalize**. The non-uniformity could be a property of the specific PG/arXiv pair rather than a universal rule. More haystack topics would be needed to establish a general principle.

## Open research questions

- Does needle-haystack similarity matter more for some model families than others?
- Is there a haystack topic × needle topic interaction that produces this asymmetry?
- Does the effect scale with input length, or is it roughly constant?

## Related Concepts

- [[Concepts/context-rot]] — the broader phenomenon
- [[Concepts/needle-question-similarity]] — orthogonal axis: needle to question
- [[Concepts/haystack-structure-effect]] — orthogonal axis: structure within a single haystack topic

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]