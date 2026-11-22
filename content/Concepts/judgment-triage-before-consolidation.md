---
title: "Judgment triage before consolidation (restatement, chatter, change)"
details: "Three-way triage that runs before an LLM rewrites consolidated observations: a fact that restates an observation is attached as evidence with no LLM call, chatter is dropped with no LLM call, and only facts that change a belief, add something new, or are uncertain reach the model that writes observation text. In Hindsight's evals every one of seven LLMs consolidated more accurately, with glm-5.3-flash jumping from 36 to 84."
tags:
  - concept
  - memory
  - llm
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Judgment triage before consolidation (restatement, chatter, change)

**Category:** Memory Consolidation Pattern
**Status:** Production in Hindsight 1.2 (vendor-reported)

## Overview

Consolidation turns new facts into **observations** — the bank's current beliefs. The naive design sends every new fact to the LLM together with the observations it might touch, and asks the LLM to reconcile. Most of those facts do not need a model: they restate something already believed, or they are chatter with no bearing on any belief.

The pattern interposes a [[Concepts/decision-model-as-memory-judge|decision model]] that settles the easy facts first, one question per fact, before any LLM call.

## The triage

| Judgment | Action | LLM cost |
|---|---|---|
| **Restatement** — the fact repeats an existing observation | Attach the fact as evidence to that observation | none |
| **Chatter** — no bearing on any belief | Skip it | none |
| **Change / new / unsure** — it alters what an observation says, adds something, or the judge is not confident | Send to the LLM, which writes every observation's text | one call |

The LLM therefore receives only the facts that require rewriting prose — which is what the LLM is for.

## Reported results

- **All seven LLMs improved.** Consolidation quality rose for every model tested, the only operation where that happened.
- **`glm-5.3-flash`: 36 → 84.** Alone, its calls all succeed but it rarely updates observations; most failures are a new fact that no observation cites. Narrowed to the few facts that genuinely need rewriting, it handles them.
- **`deepseek-v4.1-flash`: 68 → 86**; **`gemma-4-26b-a4b`: 66 → 82.**
- **Cost stays about level.** The LLM makes roughly 20% fewer calls; consolidation spends up to 2.3x less time in model calls. The gain here is quality and latency, not money.

## Why the quality gain is larger than the call saving

Cheap LLMs are not failing to generate — they are failing to *notice* that an observation needs updating when the prompt mixes fifty easy facts with three hard ones. Triage narrows the task: the model sees a small set of facts that are already known to be relevant, and its writing quality is enough.

This is a general lesson about putting judgment before generation: **the generative model's job should be a small, well-posed writing task, not a mixed classification-and-writing task.**

## Relationship to observation design

- Triage assumes observations exist and are addressable — the fact must be comparable to a candidate observation before it can be called a restatement.
- "Unsure" facts deliberately fall through to the LLM. A triage that forced a binary decision would silently discard ambiguous evidence.
- The same decision can be exposed as a standalone API: "is this new, or already known?" is a question an application outside the memory system may ask too.

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]] — the general pattern
- [[Concepts/observational-memory-pattern]] — what consolidation produces
- [[Concepts/hindsight-memory-architecture]] — observation consolidation in Hindsight
- [[Concepts/knowledge-page-as-projected-view]] — the downstream artifact that consumes observations
- [[Concepts/change-impact-gating-page-refresh]] — the same "does this matter?" gate applied to pages

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Research: [[Research/decision-gated-agent-memory]]
