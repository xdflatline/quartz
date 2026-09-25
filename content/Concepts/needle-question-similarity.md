---
title: "Needle-Question Similarity"
details: "A controlled NIAH variant introduced by Chroma (Hong et al., 2026): instead of binary lexical/non-lexical classification, the cosine similarity between the needle and question embeddings is computed across five embedding models and treated as a continuous variable. Lower similarity → faster performance degradation as input length grows. Quantified on PG-essay (range 0.445-0.775) and arXiv (0.521-0.829) haystacks with <0.1 stddev across embedders."
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

# Needle-Question Similarity

**Source:** [[Raw/chroma-context-rot-2026-07]]
**Category:** Evaluation Methodology
**Related:** [[Concepts/context-rot]], [[Concepts/needle-in-a-haystack-benchmark]]

## Overview

**Needle-question similarity** is the cosine similarity between the embedding of the needle (the target fact) and the embedding of the question the model is asked. Chroma's Context Rot study (July 2026) uses this as a **continuous replacement** for the standard binary lexical / non-lexical distinction that earlier work like NoLiMa imposed.

The motivation: real-world queries rarely have exact lexical overlap with the passages that contain the answer. Agents searching a codebase for "how does the cache invalidation work" do not get a span that starts with the literal phrase "how does the cache invalidation work." They get spans that *mean* the same thing.

## Why a continuous similarity is more useful than binary lexical/non-lexical

Binary classification hides the spectrum. Chroma found:

- **PG-essay topic**: needle-question similarity ranges from **0.445 to 0.775** with `<0.1` stddev across embedders.
- **arXiv topic**: range **0.521 to 0.829** with `<0.1` stddev.

Treating the lower end as one category and the upper end as another obscures the fact that performance degrades **continuously** as similarity drops. Binary "non-lexical" (as NoLiMa defined it) lumps together similarity-0.45 and similarity-0.65 cases, which behave very differently under context scaling.

## The five-embedding-model average

For robustness, Chroma computes the cosine similarity across five different embedding models:

- `text-embedding-3-small`
- `text-embedding-3-large`
- `jina-embeddings-v3` (with `input_type='text-matching'`)
- `voyage-3-large`
- `all-MiniLM-L6-v2`

The mean across these is the reported similarity. The standard deviation across them is reported as an inter-embedder noise floor — and it stays under 0.1 for all needles.

## Headline empirical finding

**As needle-question similarity decreases, model performance degrades more quickly with increasing input length.**

At short input lengths, models perform well even on low-similarity pairs (in the high/medium-performance tier). As input length grows, the lower-similarity pairs degrade first and fastest. By the time input length reaches the model's upper bound, low-similarity pairs may be near-zero accuracy even when the same pair succeeded at 1k tokens.

Critically: the needle-question pair is held **fixed** across input lengths; only the surrounding haystack varies. So the degradation is not because the pair becomes intrinsically harder — it is because the model's ability to bridge the semantic gap **collapses** as context grows.

## Needle position has no notable effect

In the same study, Chroma tested 11 needle positions (from beginning to end of the haystack) and found **no notable variation in performance** for the NIAH-with-similarity task. This is an important negative result: it says the degradation is a property of the total input length, not of where the needle sits within the window.

## Practical implications for evaluation

- **Use multi-embedder average similarity**, not a single model, when constructing NIAH-style tests.
- **Report similarity as a continuous range**, not a binary lexical/non-lexical label.
- **Always test multiple input lengths** — a needle-question pair that succeeds at 1k and fails at 100k is a meaningful negative result, not noise.

## Related Concepts

- [[Concepts/context-rot]] — the phenomenon similarity predicts
- [[Concepts/needle-in-a-haystack-benchmark]] — the parent benchmark
- [[Concepts/distractor-resistance]] — a separate axis of degradation
- [[Concepts/needle-haystack-similarity]] — needle-haystack similarity, not needle-question

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]
- Related Entity: [[Entities/nolima]]