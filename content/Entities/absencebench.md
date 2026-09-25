---
title: "AbsenceBench"
details: "AbsenceBench (Fu et al., 2025; arXiv:2506.11440) — long-context benchmark that tests whether models can recognize the *absence* of a given snippet of text. Demonstrates that LLMs fail at tasks where the answer is 'no, this does not appear in the context' — a fundamentally different failure mode from retrieval of present content."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://arxiv.org/abs/2506.11440
---

# AbsenceBench

**Paper:** Fu, Shrivastava, Moore, West, Tan, Holtzman (2025). "AbsenceBench: Language Models Can't Tell What's Missing." arXiv:2506.11440.
**URL:** <https://arxiv.org/abs/2506.11440>

## Overview

**AbsenceBench** tests whether LLMs can recognize the **absence** of a given snippet of text in a long context — a fundamentally different capability from retrieving content that *is* present.

The task: given a long context and a candidate snippet, decide whether the snippet appears in the context. If yes, identify it; if no, say so.

## Why it surfaces context rot

Retrieval benchmarks (NIAH, NoLiMa, LongMemEval) implicitly assume the answer *is* in the context. AbsenceBench inverts the prior: the most common case becomes "no, the answer is not here," and the model must calibrate its confidence to that negative.

Chroma's Context Rot report ([[Raw/chroma-context-rot-2026-07]]) cites AbsenceBench as evidence that context rot is not limited to retrieval — it extends to the calibration of "is this present or not?" judgments, which compounds the long-context challenge.

## The "language models can't tell what's missing" framing

The paper's title frames the result bluntly: frontier LLMs systematically fail at absence detection as input length grows. This is consistent with Chroma's broader finding that the cost of retrieval from a long context is not just finding what is there, but also recognizing what is not.

## Related Pages

- Entity: [[Entities/needle-in-a-haystack-benchmark]] — the lexical-retrieval counterpart
- Concept: [[Concepts/context-rot]] — the broader phenomenon AbsenceBench contributes evidence for