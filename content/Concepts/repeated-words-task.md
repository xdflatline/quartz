---
title: "Repeated Words Task"
details: "Synthetic copy-task benchmark from Chroma (2026): the model is asked to reproduce a sequence of N identical words with one unique word inserted at index i. Input and output length both scale with N (input = output tokens × 2). 1090 variants per word combination across N ∈ {25, 50, ..., 10000}. Surfaces context rot on the simplest possible operation: a string-copy. Sonnet 3.5 outperforms newer Claude models up to its 8192 output limit; Opus 4 has the slowest degradation but refuses 2.89% of attempts; position accuracy is highest when the unique word appears near the start."
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

# Repeated Words Task

**Source:** [[Raw/chroma-context-rot-2026-07]]
**Category:** Evaluation Benchmark
**Related:** [[Concepts/context-rot]], [[Concepts/longmemeval-benchmark]]

## Overview

The **repeated words task** is Chroma's synthetic benchmark designed to surface context rot on the simplest possible operation: a string-copy. The model is given a prompt like:

> Simply replicate the following text, output the exact same text: apple apple apple apple **apples** apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple apple

…and is expected to reproduce the input exactly, including the unique word at the correct index.

The task is intentionally trivial — it is the LLM analog of "repeat this string" in a `cat` shell command — yet it surfaces systematic, model-specific failures as input length grows.

## Why a synthetic task

Chroma wanted to isolate **input length as the only variable** in evaluating context rot. Real tasks confound input length with task difficulty (longer context typically means harder reasoning). Repeated-words sidesteps that:

- Input length scales (N words)
- Output length scales (≈N words)
- Task complexity is **constant**: copy N tokens verbatim

If performance degrades here, the only explanation is input/output length, not task difficulty.

## The 1090 variants

For each word combination, Chroma generates **1090 variants** across:

- **Word counts**: 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000 (12 levels)
- **Unique-word indices**:
  - Every possible position when N ≤ 100 (e.g. all 100 positions for N=100)
  - Otherwise: `num_words // 100` increments (e.g. 50 positions for N=5000)

Seven word combinations cover different lexical/semantic distances:

| Common word | Unique word | Distance |
|---|---|---|
| "apple" | "apples" | morphological (singular/plural) |
| "apples" | "apple" | reverse direction |
| "golden" | "Golden" | case |
| "orange" | "run" | semantic (totally unrelated) |
| "orange" | "San Francisco" | semantic (location) |
| "San Francisco" | "sf" | abbreviation |
| "Golden Gate Bridge" | "Golden Gate Park" | sub-token replace |

## Scoring

- **Normalized Levenshtein distance** — primary quality metric
- **Position accuracy** — whether the unique word appears at the correct index
- **Word count difference** — input word count minus output word count (positive = under-generation, negative = over-generation)

A pre-attempt penalty applies to outputs that begin with observation phrases (e.g. "I notice there's a discrepancy...") — these count as attempts but are slightly downweighted.

## Headline empirical findings

- **All models degrade as length grows.** Universal.
- **Position accuracy is highest near the start** of the sequence, especially as length grows. Models forget the index they were told to reproduce.
- **Sonnet 3.5 outperforms newer Claude models** up to its 8192 output limit — the newer models are *worse* at this trivial task than the older one within that range.
- **Opus 4 has the slowest degradation rate** but is the only Claude model to refuse the task (2.89% of attempts). Common refusal triggers: (a) perceived copyright risk, (b) detected "inconsistency" in the sequence (i.e. the unique word itself).
- **GPT-4 Turbo has a local performance peak at ~500 words.** Below that, it over-generates; at 500 words it matches input length well; beyond that it under-generates.
- **GPT-4.1 mini generates nonsense duplicates** ("Golden Golden", "Gate Gate") for "Golden Gate Bridge"/"Golden Gate Park" at long contexts.
- **GPT-4.1 nano lowercases "San"** in "San Francisco" → "san Francisco" at long contexts.
- **Gemini 2.5 Pro produces "syllable collapse"** — "I'-a-le-le-le-le-le-le-'a-le-le-le-le-le..." at 2500 words.
- **Qwen3-8B has 4.21% non-attempts** and produces extended hallucinated prose starting around 5000 words ("Okay, I'm going to take a break...").

## Why it matters

The repeated-words task is the strongest evidence that context rot is not just a retrieval problem. Retrieval failures can be explained as "the model couldn't find the needle." But failing to copy a 5000-word sequence verbatim — when the entire sequence is the input — cannot be explained as a retrieval failure. It is an **output-side** failure: the model cannot faithfully reproduce what it just read.

This complements the LongMemEval finding (input-side failures) and the distractor finding (disambiguation failures) to show that context rot is multi-faceted.

## Related Concepts

- [[Concepts/context-rot]] — the phenomenon it surfaces
- [[Concepts/longmemeval-benchmark]] — a more realistic conversational counterpart
- [[Concepts/needle-in-a-haystack-benchmark]] — the lexical predecessor

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]