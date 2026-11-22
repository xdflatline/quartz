---
title: "Evidence-gated reflect loop (trim, judge sufficiency, answer)"
details: "Multi-round memory reasoning loop in which a decision model, not an LLM agent, owns the evidence loop: it ranks and trims retrieved evidence against the request, then judges whether the evidence already answers it, so the LLM only writes the query or the final answer. In Hindsight's evals this halved LLM turns (4.4 to 2.5) and cut input tokens per question from 45K to 7.5K on gemini-3.8-flash, at a roughly 3-point quality cost on four of seven models."
tags:
  - concept
  - memory
  - rag
  - llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Evidence-gated reflect loop (trim, judge sufficiency, answer)

**Category:** Retrieval / Reasoning Pattern
**Status:** Production in Hindsight 1.2 (vendor-reported)

## Overview

`reflect` answers a question by searching memory in rounds. In the pre-decision-model design an LLM agent ran every round: it chose a search tool, wrote a query, read every result, and decided whether to search again. That puts a multi-second generation in the loop for two jobs that are judgments — *what is relevant* and *do we have enough*.

The gated loop splits those jobs out.

## The loop

1. **One LLM call** turns the request into a search query, or finds there is nothing to search and returns at once.
2. **Searches run in parallel** with that query.
3. **The decision model trims the evidence** — it ranks what came back against the request and cuts what does not bear on it, so the LLM reads less.
4. **The decision model judges sufficiency** — does the evidence already answer the request? If yes, the next LLM call writes the answer. If not, the LLM writes the next query and another round runs.
5. **Knowledge pages first** — when the bank has knowledge pages, the loop first asks whether the pages alone answer the request and skips raw search when they do.

If the decision model fails, reflect falls back to LLM agent turns.

## Reported results

On `gemini-3.8-flash`:

- LLM turns per question: 4.4 → 2.5.
- Input tokens read per question: 45K → 7.5K.
- Cost: $36 → $7.91 per thousand questions (4.6x less).
- Model-call time: 1.1x–2.1x less across the seven LLMs tested.
- Quality: 94.1 → 91.2.

Cost drops 2.9x on `gemini-3.1-flash-lite`, 2.2x on `claude-haiku-5.5`, 2x on `gpt-6-luna`. Quality rises for `glm-5.3-flash` (91.2 → 94.1), holds for `gpt-6-luna`, and dips about 3 points on four of the seven models.

## The trade-off this loop exposes

Reflect is **the biggest saving and the only place quality systematically drops**. `gemini-3.1-flash-lite` falls from 94.1 to 85.3 — a reminder that "is this evidence enough?" is exactly the judgment a weak model is worst at, and that the gate inherits the judge's blind spots.

Mitigations visible in the design:

- **Fallback to agent turns** when the judge errors, rather than failing the reflect.
- **The judge only trims and decides**; the final answer is still written by the LLM, so the quality ceiling is the writer's, not the judge's.
- **Knowledge-page short-circuit** removes whole search rounds when curated pages already hold the answer.

## Why a judge beats an agent here

- **The loop is bounded arithmetic.** Each round adds evidence; the question "does this set answer the request" is a classification over the evidence set, not a synthesis.
- **Parallelism.** The decision model trims while the LLM is not running, so round latency is dominated by search rather than generation.
- **Cost is in the reading, not the deciding.** Cutting 37.5K input tokens per question dominates the price of the judge's own tokens.

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]] — the general pattern
- [[Concepts/recall-time-prune-and-dedup]] — the recall-level gates that also feed this loop
- [[Concepts/change-impact-gating-page-refresh]] — the page-refresh gate that reuses reflect on rebuilds
- [[Concepts/observational-memory-pattern]] — consolidation-side counterpart
- [[Concepts/mental-model-vs-knowledge-page]] — what the knowledge-page short-circuit is choosing between

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Research: [[Research/decision-gated-agent-memory]]
