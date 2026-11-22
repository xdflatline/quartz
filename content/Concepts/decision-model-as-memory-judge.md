---
title: "Decision model as memory judge (LLM writes, judge decides)"
details: "Division-of-labour pattern for agent memory: every small judgment in the memory lifecycle — is this new, which of these matter, is the evidence enough, could this change the page — is routed to a non-generative decision model that returns a typed answer, leaving the generative LLM only the work of writing text. Reported effect in Hindsight 1.2: about a third fewer LLM calls and 167 ms median latency for the judgment versus 1–7 s for the LLM call it replaces."
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

# Decision model as memory judge (LLM writes, judge decides)

**Category:** Architecture Pattern
**Status:** Production in Hindsight 1.2 (vendor-reported, 2026-11)

## Overview

A memory system spends most of its model budget on **judgments**, not writing. Between storing a fact and answering a question it asks: is this fact new or already known? Does it change what we believe? Which of these memories matter for this question? Is this evidence enough to answer? Could this new memory change that knowledge page?

The pattern routes each of those questions to a [[Concepts/decision-models-as-classifiers|decision model]] — a non-generative model that takes a state plus a typed question and returns a structured answer (a choice with a probability per option, a point on a scale, or a likelihood that a statement holds). The generative LLM is reserved for the parts that genuinely need prose: writing a search query, writing an answer, writing the observation or page text.

Hindsight's framing: **"The LLM writes, the decision model judges."**

## Why it is worth doing

- **Latency.** A decision-model request took 167 ms at the median (350 ms at p90) in Hindsight's own runs; the LLM call it replaces takes 1–7 s at the median depending on model.
- **Call count.** With judgments answered by the decision model, the LLM made about a third fewer calls on Hindsight's evals: 3.1 per case instead of 4.5.
- **Parsing.** An LLM answers a yes/no question with free text that must be parsed back into a boolean; a decision model returns the typed answer directly.
- **Prompt size.** Because the judge can trim evidence before the LLM reads it, the LLM reads fewer input tokens — often the dominant cost in memory operations.

## Where the judgments sit

| Stage | Judgment asked | Effect |
|---|---|---|
| Recall | Does this memory help the query? Is it a repeat of a better-ranked one? | Prune and dedup before the agent's prompt — see [[Concepts/recall-time-prune-and-dedup]] |
| Reflect | Does this evidence bear on the request? Is it enough to answer? | Fewer rounds and far fewer input tokens — see [[Concepts/evidence-gated-reflect-loop]] |
| Consolidation | Is this fact a restatement, chatter, or something that changes a belief? | Only the hard facts reach the LLM — see [[Concepts/judgment-triage-before-consolidation]] |
| Knowledge pages | Could this new memory change the page? | Updates can skip the LLM entirely — see [[Concepts/change-impact-gating-page-refresh]] |

## Design constraints

- **Typed question per call.** The judge must know the option set, the scale, or the proposition. Questions that need open-ended synthesis stay with the LLM.
- **Fallback path.** Hindsight falls back to LLM agent turns when the decision model fails; the judge is an accelerator, not a hard dependency.
- **Not free.** The judge's tokens cost money — roughly $4–7 per thousand cases in these evals — so the economics invert on the cheapest LLMs. See [[Concepts/decision-model-cost-leverage]].
- **Off by default.** Every judgment site retains its previous behaviour when no decision model is configured, so the optimization is opt-in per bank or per request.

## Related Concepts

- [[Concepts/decision-models-as-classifiers]] — the underlying pattern and question types (`choice`, `score`, `noul`)
- [[Concepts/calibration-for-decision-models]] — a judge is only as good as its calibration
- [[Concepts/recall-time-prune-and-dedup]] · [[Concepts/evidence-gated-reflect-loop]] · [[Concepts/judgment-triage-before-consolidation]] · [[Concepts/change-impact-gating-page-refresh]] — the four instances
- [[Concepts/decision-model-cost-leverage]] — when the pattern pays for itself
- [[Concepts/hindsight-memory-architecture]] — the memory substrate the judges gate

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Research: [[Research/decision-gated-agent-memory]]
- Vendor: [[Entities/vectorize]], [[Entities/hs-decide-1-flash]]
