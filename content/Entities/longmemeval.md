---
title: "LongMemEval"
details: "LongMemEval (Wu et al., 2025; arXiv:2410.10813) — long-context conversational QA benchmark that tests chat assistants on long-term interactive memory. Three question categories: knowledge update, temporal reasoning, multi-session. The cleaned subset LongMemEval_s has 306 prompts averaging ~113k tokens. Used by Chroma (2026) as a primary surface for context rot, with a focused-input (~300 tokens) vs. full-input (~113k tokens) comparison."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://arxiv.org/abs/2410.10813
---

# LongMemEval

**Paper:** Wu, Wang, Yu, Zhang, Chang, Yu (2025). "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory." arXiv:2410.10813.
**URL:** <https://arxiv.org/abs/2410.10813>

## Overview

**LongMemEval** is a long-context benchmark for evaluating chat assistants on **long-term interactive memory**: given a chat history and a question about it, the model must answer correctly. The benchmark models the production use case directly: persistent chat history + retrieval + reasoning.

## Three question categories

| Category | What it tests | Example |
|---|---|---|
| **Knowledge update** | Recall the *current* value of a fact that may have changed over the conversation | "What's my current job?" (after the user mentioned switching) |
| **Temporal reasoning** | Compute relationships across multiple time points | "How many days between the gardening workshop and planting the saplings?" |
| **Multi-session** | Information that spans multiple conversation sessions | References to facts mentioned in an earlier session |

## The LongMemEval_s subset

Chroma uses the `LongMemEval_s` subset, filtered to the three categories above. After manual cleaning (38 prompts removed for ambiguity or unanswerability), the dataset has **306 prompts averaging ~113k tokens**.

Focused counterparts (derived from the original labels plus manual adjustments) average **~300 tokens** — a 370× reduction. This is what enables Chroma's focused-vs-full comparison.

## The model's job

In a naive chat-assistant architecture, the entire chat history is concatenated into the prompt for each new turn. This requires the model to:

1. **Retrieve** the relevant parts of the chat history.
2. **Reason** over them to answer the question.

LongMemEval is testing both capabilities simultaneously. Chroma's two-condition design (focused vs. full) separates the cost of retrieval from the cost of reasoning: on focused inputs, the model only needs to reason; on full inputs, it must also retrieve.

## Headline finding from Chroma

Every frontier model tested performs significantly better on focused inputs than on full inputs. The relevant information **is present** in the full input — the model just cannot find it. This is the strongest single piece of evidence in the Context Rot study that long-context models degrade on the retrieval task itself.

## Related Pages

- Concept: [[Concepts/longmemeval-benchmark]] — the wiki concept page with detailed methodology
- Entity: [[Entities/chroma]] — the company that used it for context rot research