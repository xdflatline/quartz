---
title: "MRCR (Multi-Round Co-Reference Resolution)"
details: "MRCR (OpenAI, 2025; HuggingFace dataset) — long-context benchmark for multi-round co-reference resolution: retrieving the i-th instance of a specific user ask among similar user asks in a multi-turn conversation. Tests disambiguation among topically similar distractors within chat history. Closely related to LongMemEval's multi-session category but focused specifically on the i-th-retrieval mechanism."
tags:
  - entities
  - llm
  - benchmark
  - evaluation
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://huggingface.co/datasets/openai/mrcr
---

# MRCR (Multi-Round Co-Reference Resolution)

**Source:** OpenAI (2025). HuggingFace dataset: <https://huggingface.co/datasets/openai/mrcr>

## Overview

**MRCR** is a long-context benchmark for **multi-round co-reference resolution**: given a long multi-turn conversation and a query of the form "the i-th instance of the user's ask about X", retrieve the correct span.

The task explicitly creates **distractors**: many similar user asks on similar topics scattered throughout the conversation, with only the i-th one matching the query. The model must:

1. Identify which "ask" the query refers to.
2. Locate the i-th instance, not the 1st or 2nd.
3. Co-reference correctly across turns.

## Why it tests what NIAH does not

NIAH tests lexical retrieval of a single, distinct needle. MRCR tests **disambiguation among topically similar spans** — multiple instances of the same kind of ask, with only position distinguishing them.

This is a strong test of long-context disambiguation, and it surfaces the same kinds of failures Chroma documents in [[Concepts/distractor-resistance]].

## Relation to LongMemEval

MRCR overlaps with LongMemEval's **multi-session** category — both test retrieval across conversation history. The difference:

- **MRCR** is structured: each test instance has the i-th-retrieval pattern, making it cleanly scored.
- **LongMemEval** is broader: knowledge updates, temporal reasoning, and multi-session are all in scope.

## Related Pages

- Entity: [[Entities/michelangelo]] — the parent framework that originated this task
- Concept: [[Concepts/distractor-resistance]] — Chroma's controlled distractor study
- Concept: [[Concepts/longmemeval-benchmark]] — the broader conversational counterpart