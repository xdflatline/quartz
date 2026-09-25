---
title: "Context Rot"
details: "Non-uniform degradation of LLM performance as input length grows, even on simple retrieval and copy tasks, demonstrated by Chroma across 18 frontier models in July 2026. Held complexity constant while scaling context length, isolating input size as the primary cause of degradation. Four factors govern the rate and shape of rot: needle-question similarity, distractor density and individual-distractor identity, needle-haystack semantic similarity, and haystack structural coherence (shuffled haystacks outperform coherent ones)."
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

# Context Rot

**Source:** [[Raw/chroma-context-rot-2026-07]]
**Category:** Empirical Phenomenon
**Related:** [[Concepts/needle-question-similarity]], [[Concepts/distractor-resistance]], [[Concepts/needle-haystack-similarity]], [[Concepts/haystack-structure-effect]]

## Overview

**Context rot** is the observed phenomenon that LLM performance is **not uniform across input length** — even on simple retrieval and copy tasks, accuracy drops and noise grows as the context window fills, often in non-monotonic, model-specific ways. The name was coined and the phenomenon systematically measured by Chroma Research in July 2026 ([Hong, Troynikov, Huber 2026](https://www.trychroma.com/research/context-rot)).

The term matters because the field's leading long-context evaluation — Needle in a Haystack (NIAH) — measures only direct lexical retrieval, where frontier models score near-perfect across their full context windows. NIAH's success is therefore **misleading**: it suggests long-context is "solved," when in fact performance rots as soon as the task demands semantic reasoning, distractor disambiguation, or simple copying.

## Why NIAH misses it

NIAH's needle-question pairs share strong lexical overlap with the needle (e.g. question "What is the secret number?" — needle "The secret number is 42"). Modern models can pattern-match that without needing deep context integration. Real-world tasks require **inference over weakly related spans**, **disambiguation among topically similar distractors**, **temporal/multi-session reasoning across chat history**, and **faithful reproduction of structured content**. On all of these, frontier models degrade non-uniformly with input length.

## The four governing factors

The Chroma study isolates four variables that change the shape of context rot:

| Factor | What it controls | Effect on rot |
|---|---|---|
| **Needle-question similarity** | Cosine similarity of needle and question embeddings | Lower similarity → faster degradation as input length grows |
| **Distractor density and identity** | Number and individual content of topically related but non-answering spans | Non-uniform impact: each distractor degrades differently; degradation amplifies with input length |
| **Needle-haystack similarity** | Whether the needle topically blends into the surrounding text | Non-uniform across topics; semantic blending can hurt or help depending on haystack |
| **Haystack structure** | Whether the surrounding text preserves logical flow or is randomly shuffled | Counterintuitively, **shuffled haystacks outperform coherent ones** across all 18 models |

## Why it matters for context engineering

The Chroma paper's conclusion: "Whether relevant information is present in a model's context is not all that matters; what matters more is how that information is presented."

This reframes the goal of [[Concepts/context-engineering]] from "fit as much as possible" to "fit the right information, in the right form, with the right amount of surrounding context." It justifies techniques like:

- **Retrieval-then-prompt** over dump-everything prompts — a tightly focused prompt removes the need for retrieval across noise.
- **Scratchpads** for large tool outputs ([[Concepts/scratchpad-context-window-management]]) — disk-backed offloading prevents tool responses from flooding the window.
- **Pre-computed, versioned context** ([[Concepts/context-as-materialized-view]]) — curate once, reuse many times, eliminate the retrieval cost from each query.
- **Structured bullet memory** ([[Concepts/context-as-evolving-playbook|ACE]]) — grow context monotonically, avoiding collapse from full-prompt rewrites.
- **Methodological context engineering** ([[Concepts/harness-mechanism-context-engineering-sdd-2026]]) — make curation an explicit team convention, not a per-agent guess.

## Key empirical findings

- **Across all 18 models**, performance degrades as input length increases. The pattern is universal, not vendor-specific.
- **Lower needle-question similarity** → faster rot. This is the strongest single predictor of when a model will fail on a long-context task.
- **Distractors are non-uniform**: a single distractor helps less than the baseline would predict, and adding four compounds non-linearly; individual distractors (e.g. distractor 3 vs. distractor 1 in the PG/arXiv study) produce markedly different failure rates.
- **Shuffled haystacks beat coherent ones.** Counterintuitive but consistent across all 18 models and all needle-haystack combinations. Suggests that structural coherence introduces a processing cost (or a distraction cost) that shuffled text does not.
- **Family-specific behaviors under ambiguity**:
  - **Claude** (Opus 4, Sonnet 4) — low hallucination rate; conservative abstention ("I cannot determine...").
  - **GPT** — highest hallucination rate; confident-but-incorrect answers under distractor load.
  - **Gemini / Qwen** — intermediate; specific quirks (Qwen3-8B has 4.21% non-attempts; Gemini 2.5 Pro shows "I'-a-le-le" type syllable collapse on long sequences).
- **Repeated-words task**: even trivial copying degrades. Sonnet 3.5 outperforms newer Claude models up to its 8192 token output limit. Opus 4 has the slowest degradation but is the only Claude to refuse (2.89%).
- **Position accuracy**: the unique word is more likely to be placed correctly when positioned near the **beginning** of the sequence, especially as length grows.

## Mechanisms (still unknown)

The Chroma paper is empirical, not mechanistic. It notes that the haystack-structure result in particular points toward attention-pattern dynamics as a fruitful direction for **mechanistic interpretability** research — but does not propose a definitive explanation. The relationship between input length and degradation is also non-monotonic in places (e.g. GPT-4 Turbo has a local performance peak at ~500 words), suggesting that more than one underlying mechanism is in play.

## Key Insights

1. **NIAH is not evidence of long-context capability.** Universal near-perfect NIAH scores co-exist with universal non-uniform degradation on even slightly harder tasks.
2. **Task complexity must be held constant.** Many prior benchmarks conflate input length with task difficulty (e.g. Graphwalks). Chroma explicitly controls for this — a methodological standard future work should adopt.
3. **Rot is universal but shaped by the four factors.** No model is exempt; no model degrades uniformly. The shape of degradation differs by model family.
4. **Conservative refusal can mask rot.** Claude's "I cannot determine" outputs count as failures on LongMemEval even though they are not hallucinations — rot shows up as both hallucination and abstention, depending on the model.
5. **Context engineering is empirical, not theoretical.** The paper's strongest actionable conclusion is that practitioners must engineer the *form* of the context, not just populate it.

## Related Concepts

- [[Concepts/needle-question-similarity]] — the strongest single predictor of rot
- [[Concepts/distractor-resistance]] — the second-strongest, with non-uniform per-distractor impact
- [[Concepts/needle-haystack-similarity]] — mixed-direction effect on rot
- [[Concepts/haystack-structure-effect]] — the counterintuitive "shuffling helps" finding
- [[Concepts/longmemeval-benchmark]] — the conversational QA benchmark that surfaces rot in practice
- [[Concepts/repeated-words-task]] — the synthetic copying task that surfaces rot as position errors
- [[Concepts/context-as-materialized-view]] — pattern that preempts rot by serving focused context per query
- [[Concepts/scratchpad-context-window-management]] — pattern that prevents rot by offloading large tool outputs
- [[Concepts/context-as-evolving-playbook|ACE]] — pattern that controls rot by growing context as bullets, not as full rewrites
- [[Concepts/harness-mechanism-context-engineering-sdd-2026]] — the SDD methodological counterpart: explicit curation as a team convention

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]
- Original: <https://www.trychroma.com/research/context-rot>
- Code: <https://github.com/chroma-core/context-rot>
- Research Index: [[Research/llm-context-rot-evaluation-2026]]