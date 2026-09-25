---
title: "Distractor Resistance"
details: "A controlled NIAH variant introduced by Chroma (2026) measuring how topically related but non-answering spans (distractors) degrade retrieval accuracy as input length grows. Even a single distractor reduces performance vs. the no-distractor baseline; four distractors compound non-linearly. Individual distractors have non-uniform impact — some are far more damaging than others, with the worst-case distractor's identity depending on haystack-needle pairing. Family-specific failure modes emerge under distractor load: Claude abstains conservatively, GPT hallucinates confidently."
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

# Distractor Resistance

**Source:** [[Raw/chroma-context-rot-2026-07]]
**Category:** Evaluation Methodology
**Related:** [[Concepts/context-rot]], [[Concepts/needle-question-similarity]], [[Concepts/haystack-structure-effect]]

## Overview

**Distractor resistance** is the capacity of an LLM to ignore topically related but non-answering spans when retrieving or reasoning over a long context. Chroma's Context Rot study (July 2026) operationalizes it as a three-level controlled experiment: needle only (baseline), needle + 1 distractor, needle + 4 distractors, all randomly positioned in the haystack.

The distinction from **irrelevant context** matters:

- **Distractors** — topically related to the needle, but do not answer the question. Example: when the question is "What was the best writing advice from your college classmate?", a distractor might be "The best writing tip from my college professor was to write everyday." (Wrong person, wrong frequency.)
- **Irrelevant content** — unrelated to the needle and question. Standard NIAH haystacks are largely this.

Distractors require the model to integrate more information than lexical matching: it must compare the entity ("classmate" vs "professor"), compare the attribute ("best" qualifier), and decide the candidate fails. Irrelevant content is dismissed by topical mismatch alone.

## The three conditions

For a high-similarity needle, Chroma constructs four human-written distractors and tests:

| Condition | Setup |
|---|---|
| **Baseline** | Needle only, no distractors |
| **Single distractor** | Needle + 1 randomly positioned distractor |
| **Multiple distractors** | Needle + all 4 distractors, randomly positioned |

The needle is chosen to be one with **high needle-question similarity** (the second-highest of eight) so that the needle itself is "easy" — this isolates the impact of the distractors.

## Headline empirical findings

- **Even one distractor reduces performance** vs. baseline. The effect is non-zero from the very first addition.
- **Four distractors compound non-linearly.** The drop from baseline to 4 distractors is greater than 4× the drop from baseline to 1.
- **Individual distractors are non-uniform.** In the arXiv haystack + PG-essay needle pairing, distractor 3 caused greater performance decline than distractor 1, 2, or 4. The "worst" distractor's identity depends on the haystack-needle combination.
- **Degradation amplifies with input length.** At short context, all conditions (0/1/4 distractors) cluster. As context grows, the conditions fan out, with 4-distractor performance falling fastest.
- **Hallucination patterns are model-specific:**
  - Distractors 2 and 3 appear most frequently in hallucinated responses (across all models) for the arXiv-haystack + PG-needle combination.
  - Claude models have the **lowest hallucination rates** but **high abstention rates** — under ambiguity, Claude Opus 4 and Sonnet 4 say "I cannot determine..." rather than guess.
  - GPT models show the **highest hallucination rates** — confident incorrect answers when distractors are present.

## Why the failure mode matters

A hallucination and an abstention look the same on an accuracy metric (both are "wrong"), but they have very different deployment consequences:

- **Hallucination** — silently wrong, dangerous in high-stakes domains.
- **Conservative abstention** — the system signals uncertainty; downstream can route to retrieval, escalation, or a different tool.

Claude's behavior under distractor load is closer to a calibrated "I don't know" than the GPT behavior, even though both families degrade.

## Practical implications

- **Test with multiple distractors**, not just one. Single-distractor tests under-estimate the problem.
- **Test with hand-written distractors**, not template-generated ones. Hand-written distractors have the same surface coherence as real adversarial inputs.
- **Distinguish hallucination from abstention** in your eval pipeline. Reporting only accuracy hides the safer-by-abstention behavior.
- **Distractor count is not the only axis.** Different individual distractors with the same surface form cause different failure rates — eval needs to enumerate the meaningful variants, not just count them.

## Related Concepts

- [[Concepts/context-rot]] — the broader phenomenon
- [[Concepts/needle-question-similarity]] — the orthogonal axis: how related the needle is to the question
- [[Concepts/haystack-structure-effect]] — orthogonal axis: does the haystack's coherence matter

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]
- Related work: Shi et al., "Large Language Models Can Be Easily Distracted by Irrelevant Context," arXiv:2302.00093 (2023) — pre-Chroma evidence that distractors matter