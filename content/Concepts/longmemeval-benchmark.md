---
title: "LongMemEval Benchmark"
details: "Long-context conversational QA benchmark from Wu et al. (2025, arXiv:2410.10813) used by Chroma to evaluate 18 frontier models on focused (~300 token) vs. full (~113k token) inputs. Surfaces context rot by forcing models to do retrieval + reasoning simultaneously: on full inputs the model must locate the relevant turn in chat history before answering, while on focused inputs it only reasons. Strongest single predictor of rot is distractor presence; Claude family exhibits the largest gap due to conservative abstention under ambiguity."
tags:
  - concepts
  - llm
  - evaluation
  - context-engineering
  - benchmark
created: 2026-09-25
updated: 2026-09-25
type: concept
sources:
  - "Raw/chroma-context-rot-2026-07.md"
---

# LongMemEval Benchmark

**Source:** [[Raw/chroma-context-rot-2026-07]] | [Original arXiv:2410.10813](https://arxiv.org/abs/2410.10813)
**Category:** Evaluation Benchmark
**Related:** [[Concepts/context-rot]], [[Concepts/repeated-words-task]], [[Concepts/needle-in-a-haystack-benchmark]]

## Overview

**LongMemEval** is a long-context conversational question-answering benchmark for evaluating chat assistants on **long-term interactive memory**. It was introduced by Wu et al. (2025) and used by Chroma (2026) to surface context rot in a realistic setting.

The benchmark models the chat-assistant use case directly: the model is given a chat history and asked to answer a question about it. Real applications — customer support bots, coding assistants, personal AI — all share this structure.

## The two-condition design

Chroma's LongMemEval usage introduces a controlled two-condition comparison:

| Condition | Setup | What the model does |
|---|---|---|
| **Focused input** | Only the relevant parts of the chat history (~300 tokens average) | Pure reasoning |
| **Full input** | The full 113k-token LongMemEval input, including irrelevant context and distractors | Retrieval + reasoning |

The model's reasoning ability is held constant across conditions; the only variable is whether it has to locate the relevant context itself. This isolates the **cost of retrieval from a long context** as the experimental variable.

## Dataset construction

Chroma uses the `LongMemEval_s` subset, filtering for three question categories:

- **Knowledge update** — questions about changes in facts over time (e.g. "What's my current job?")
- **Temporal reasoning** — questions requiring comparison across time points (e.g. "How many days between X and Y?")
- **Multi-session** — questions spanning multiple conversation sessions

After manual cleaning (38 prompts removed for ambiguity or unanswerability), the dataset has **306 prompts averaging ~113k tokens**.

Focused prompts are derived from the originally labeled data plus manual adjustments, averaging ~300 tokens — roughly **370× smaller** than full inputs.

## Headline empirical findings

- **Every model performs significantly better on focused inputs.** This is the strongest single signal in the study: even at 113k tokens, the relevant information is *in the prompt* — the model just can't find it.
- **Claude models exhibit the largest gap.** Driven by abstention: Opus 4 and Sonnet 4 say "I cannot determine..." when the relevant content is buried in noise, even though it is technically present. Older Claude models (3.5, 3.7) are less conservative and perform relatively better on full inputs.
- **Thinking mode helps both conditions** but does not close the gap. Models that support thinking (Opus 4, o3, Gemini 2.5 Pro) see gains on focused and full, but the gap between them persists.
- **Question-type ordering depends on thinking mode**:
  - Non-thinking: knowledge update > multi-session > temporal reasoning
  - Thinking: knowledge update > temporal reasoning > multi-session

## The canonical failure example

> **Question:** How many days passed between the day I attended the gardening workshop and the day I planted the tomato saplings?
> **Correct Answer:** 6 days (7 including the last day).
> **Model Output (Claude Sonnet 4, non-thinking, on full prompt containing the dates):** "I cannot determine the number of days between the gardening workshop and planting the tomato saplings because the specific dates for these events are not provided in the chat history."

The dates **are** in the chat history. The model failed to retrieve them.

## Why it matters

LongMemEval is the most realistic surface for context rot in the Chroma study because:

- The relevant information is present in the prompt (unlike pure hallucination tests).
- The task is concrete and verifiable (count days, name a job, identify a temporal sequence).
- Failure modes are observable: either the model hallucinates (GPT pattern) or abstains (Claude pattern).

This makes LongMemEval a more compelling evaluation for production chat assistants than NIAH-style retrieval.

## Related Concepts

- [[Concepts/context-rot]] — the phenomenon it surfaces
- [[Concepts/repeated-words-task]] — a simpler synthetic counterpart
- [[Concepts/needle-in-a-haystack-benchmark]] — the simpler lexical predecessor
- [[Entities/longmemeval]] — the canonical entity page

## References

- Raw Article: [[Raw/chroma-context-rot-2026-07]]
- Original paper: Wu et al., "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory," arXiv:2410.10813