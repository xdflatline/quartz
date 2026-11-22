---
title: "Decision-gated agent memory: judgments as the cost centre"
details: "Synthesis of Hindsight's 2026-11 model release: the argument that most memory-system model work is small judgments rather than writing, the four gates where a decision model replaces an LLM (recall prune/dedup, reflect evidence and sufficiency, consolidation triage, page-change impact), the reported quality/cost/latency deltas, and the economics of when a judge pays for itself. Includes the source's boundary conditions — vendor-run evals, a self-graded judge, an equal-mix cost baseline."
tags:
  - research
  - memory
  - agent
  - llm
  - benchmark
created: 2026-11-22
updated: 2026-11-22
type: research
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Decision-gated agent memory: judgments as the cost centre

**Source:** [[Raw/hindsight-models-decision-gated-memory-2026-11-03]] — Hindsight / Vectorize, 2026-11-03
**Status:** Vendor-reported benchmark results on Hindsight 1.2.0; not independently replicated.

## The thesis

A memory system's model budget is dominated by judgments, not generation. Storing a fact, merging it into beliefs, deciding what to retrieve, deciding when to stop retrieving, deciding whether a page needs rewriting — each of those is a small classification or scoring problem. Running a generative LLM for each one costs seconds and a full context read to produce a token that must then be parsed back into a boolean.

Hindsight's answer is to route those questions to a non-generative 0.8B decision model and leave the LLM the writing: query synthesis, answer prose, observation text, page edits. The tagline is exact: **the LLM writes, the decision model judges.**

## The four gates

| Gate | Question | Where it acts | Effect |
|---|---|---|---|
| [[Concepts/recall-time-prune-and-dedup\|Recall prune/dedup]] | Does this memory help? Is it a repeat? | Before results enter the agent's prompt | Fewer tokens on every agent turn; prune is free (reuses ranking), dedup costs one request over similar embeddings |
| [[Concepts/evidence-gated-reflect-loop\|Reflect]] | Does this evidence bear on the request? Is it enough? | Inside the multi-round search loop | LLM turns 4.4 → 2.5; 45K → 7.5K input tokens per question on `gemini-3.8-flash` |
| [[Concepts/judgment-triage-before-consolidation\|Consolidation]] | Restatement, chatter, or a change? | Before the LLM rewrites observations | All seven LLMs improved; `glm-5.3-flash` 36 → 84 |
| [[Concepts/change-impact-gating-page-refresh\|Page refresh]] | Could this memory change the page? | Incremental knowledge-page updates | ≈8.5 → 4 LLM calls per case; quality up and cost down simultaneously |

The design invariant across all four: **the gate is optional and the previous behaviour remains the fallback.** With no decision model configured, each site runs exactly as before; if the judge fails, reflect falls back to LLM agent turns.

## Reported results

Whole-system ("all of Hindsight", equal mix of retain, consolidation, reflect and knowledge pages):

- Quality improved for **six of seven** LLMs: `glm-5.3-flash` 73.8 → 87.1, `gemma-4-26b-a4b` 76.6 → 81.1, `deepseek-v4.1-flash` 81.9 → 85.1; roughly level for `gemini-3.1-flash-lite` (87.1 → 86.6).
- **Five of seven** got cheaper: `gemini-3.8-flash` $147 → $61, `gemini-3.1-flash-lite` $42 → $22, `claude-haiku-5.5` $31 → $18, `gpt-6-luna` $16 → $9.88, `gemma-4-26b-a4b` $16 → $12.
- Model-call time dropped for **all seven**, 1.2x–1.9x.
- On the operations where the judge participates (consolidation, reflect, page refresh), `gemini-3.8-flash` cost 2.5x less, spent 1.9x less time in model calls, and scored 2.2 points higher.

Per operation, the results diverge in an instructive way:

- **Reflect** — largest saving, only systematic quality regression (four of seven models down ~3 points; `gemini-3.1-flash-lite` 94.1 → 85.3).
- **Consolidation** — quality up for all seven, cost flat, time down up to 2.3x.
- **Knowledge pages** — quality up and cost down for most models; `gpt-6-luna` 82.5 → 90.0 at less than half the cost.
- **Retain** — untouched by the judge, so it dilutes whole-system averages.

## Economics

The judge's tokens cost **$4–7 per thousand cases**. That is small against a frontier LLM and decisive against a budget one:

- `gemini-3.8-flash` alone: 89.0 quality at $147/1k cases.
- `glm-5.3-flash` + judge: 87.1 at $7.72 — within ~2 points at 15–19x less cost.
- `deepseek-v4.1-flash` + judge: 85.1 at $12.21, up from $10.57 alone.
- `glm-5.3-flash` + judge: 87.1 at $7.72, up from $4.58 alone.

So the judge's biggest value is not its own inference saving but the **permission to downshift the LLM**. Optimization order matters: add the judge, then re-select the LLM against the new cost curve. Details in [[Concepts/decision-model-cost-leverage]].

## The model stack

Three open-weight models ship with the release — `hs-decide-1-flash` (0.8B, Apache 2.0), `hs-rerank-1` (114M, MIT), `hs-embed-1` (112M, MIT) — all multilingual across eight languages, with the retrieval pair viable on CPU via int8 ONNX. The decision model deliberately leads on memory judgments and trails on general decision benchmarks, the signature of task-shaped training. See [[Concepts/purpose-built-memory-model-stack]], [[Entities/hs-decide-1-flash]], [[Entities/hindsight-ai-model-family]], [[Entities/hindsight-inference]].

## What generalizes beyond Hindsight

1. **Enumerate the judgments before choosing a model.** If a step's output is a boolean, a ranking, or a score, a generative model is the wrong instrument.
2. **Gate at the boundary where cost is incurred.** Recall pruning targets the agent's prompt, not the memory system's own latency — that is where the money is.
3. **Judgment before generation beats judgment inside generation.** Triage makes consolidation a smaller, better-posed writing task; the quality gain on cheap models is larger than the call saving.
4. **Gate increments, not rebuilds.** Refreshing a page from deltas can skip the LLM entirely; regenerating it cannot.
5. **Measure operations separately.** Retain dilutes the effect; reflect hides a quality regression inside a cost win.

## Boundaries of this source

- **Vendor-run evals.** All numbers come from Hindsight's own system evals, run on Hindsight 1.2.0 against a fresh server through the public API. No independent replication is cited.
- **Self-graded rows.** The judge for all cases is `gemini-3.1-flash-lite`, which is also one of the seven LLMs tested, so its own rows are self-graded.
- **Equal-mix cost baseline.** "All of Hindsight" is an equal mix of retain, consolidation, reflect and knowledge pages. A real workload weights them differently, and the vendor says so.
- **Time is model-call time**, from traces, not end-to-end latency.
- **Benchmarks are hosted by the vendor**, and the comparison models for the decision/rerank/embed tables were selected by the vendor.
- **Model names and prices reflect the 2026-11 publication date** and may be superseded.

## Open questions

- Does the reflect quality dip on weaker models persist when the judge is a larger decision model, or is it a property of the 0.8B judge?
- How much of the consolidation gain is triage versus prompting — would an LLM prompted with a pre-filtered fact set show the same improvement without a decision model in the loop?
- Does prune/dedup change *answer* quality in a measurable way, or only token cost? The post reports tokens saved, not downstream task accuracy.
- Is change-impact gating safe for pages whose prior state is itself low-confidence?
- What does the break-even look like for a memory bank with a non-English-dominant corpus, given the eight-language claim?

## Related Research

- [[Research/ai-agent-memory-orchestration]] — the broader agent-memory landscape this sits in
- [[Research/ollaya-decision-model-ecosystem]] — alternative open decision-model families and benchmark methodology
- [[Research/zero-token-agent-memory]] — the other direction: removing model work from memory operations entirely

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]]
- [[Concepts/recall-time-prune-and-dedup]]
- [[Concepts/evidence-gated-reflect-loop]]
- [[Concepts/judgment-triage-before-consolidation]]
- [[Concepts/change-impact-gating-page-refresh]]
- [[Concepts/decision-model-cost-leverage]]
- [[Concepts/purpose-built-memory-model-stack]]
- [[Concepts/decision-models-as-classifiers]]
- [[Concepts/hindsight-memory-architecture]]
- [[Concepts/hindsight-knowledge-pages-feature]]

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Benchmarks: https://benchmarks.hindsight.vectorize.io/
- Weights: https://huggingface.co/hindsight-ai
- Product: [[Entities/hindsight-inference]]
