---
title: "Decision-model cost leverage (and where it inverts)"
details: "The economics of adding a small judgment model to a memory pipeline: it pays when the LLM call it replaces is expensive, because the judge's own tokens are a small fraction of the bill, and it costs more when the LLM is already the cheapest option in the market. Reported break-even is a function of LLM price, not of the judge's quality — the same pattern that makes a frontier setup 2.4x cheaper can make a budget setup dearer."
tags:
  - concept
  - llm
  - evaluation
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Decision-model cost leverage (and where it inverts)

**Category:** Cost Model / Design Trade-off
**Status:** Vendor-reported economics, Hindsight 1.2 eval

## Overview

Adding a [[Concepts/decision-model-as-memory-judge|decision model]] to a memory pipeline changes two things at once: it removes LLM calls and input tokens, and it adds judge tokens. Whether the net is a saving depends almost entirely on the price of the LLM being replaced.

The judge's own bill in Hindsight's evals was **$4–7 per thousand cases** — about $3.93 of the $61 total on `gemini-3.8-flash`. That is a rounding error next to a frontier model and most of the bill next to a budget one.

## The reported numbers

| Setup | Quality | Cost per 1k cases |
|---|---|---|
| `gemini-3.8-flash` alone | 89.0 | $147 |
| `gemini-3.8-flash` + judge (all operations) | — | $61 (2.4x less) |
| `gemini-3.8-flash` + judge (judged operations only) | +2.2 points | 2.5x less |
| `gpt-6-luna` + judge | 87.0 | $9.88 |
| `glm-5.3-flash` + judge | 87.1 | $7.72 |
| `glm-5.3-flash` alone | 73.8 | $4.58 |
| `deepseek-v4.1-flash` alone | 81.9 | $10.57 |
| `deepseek-v4.1-flash` + judge | 85.1 | $12.21 |

Two distinct effects are visible:

1. **On expensive LLMs the judge is a discount.** Five of seven models got cheaper; `gemini-3.8-flash` went from $147 to $61 across all of Hindsight, and 2.5x cheaper on the operations where the judge participates.
2. **On the cheapest LLMs the judge is a quality purchase.** `glm-5.3-flash` costs 69% more ($4.58 → $7.72) and gains 13.3 quality points; `deepseek-v4.1-flash` costs 15% more and gains 3.2 points.

## The model-mix conclusion

A cheap LLM plus a judge landed within ~2 points of a frontier LLM alone:

- `glm-5.3-flash` + judge: 87.1 at $7.72 per thousand cases.
- `gemini-3.8-flash` alone: 89.0 at $147 — about 2 points more for **15–19x the cost**.

The largest single saving in the reported results is therefore not the judge itself but the *permission it grants* to switch to a cheaper LLM. Optimization order matters: add the judge, then re-select the LLM against the new cost curve. Tuning the LLM first and adding the judge afterwards leaves most of the saving on the table.

## Where the leverage disappears

- **Retain does not use the judge.** Its cost is unchanged, which waters down whole-system averages. Report memory operations separately or the effect is hidden.
- **The cheapest models may already be below the judge's marginal cost.** A pipeline built on a sub-dollar model should evaluate the judge as a quality feature, not a cost feature.
- **Time savings are more universal than money savings.** Time in model calls dropped for all seven LLMs (1.2x–1.9x), including models where cost rose.
- **Quality is not monotone.** Reflect dips for four of seven models; a cost win can be a quality loss on the operation with the biggest saving.

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]] — what is being added
- [[Concepts/purpose-built-memory-model-stack]] — the models priced here
- [[Concepts/evidence-gated-reflect-loop]] — the operation with the largest saving and the largest quality risk
- [[Concepts/change-impact-gating-page-refresh]] — the operation with simultaneous quality and cost gains
- [[Concepts/typed-decisions-benchmark-ollaya]] — alternative decision-model options and their cost shapes

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Benchmarks: https://benchmarks.hindsight.vectorize.io/leaderboards/all-operations
- Research: [[Research/decision-gated-agent-memory]]
