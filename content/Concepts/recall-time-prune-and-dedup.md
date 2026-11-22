---
title: "Recall-time prune and dedup (shrinking the agent's prompt)"
details: "Two decision-model gates applied to memory recall before results reach the calling agent: prune drops memories that do not help the query by reusing the reranker's ranking scores, and dedup drops memories that repeat a better-ranked one, asking only about embedding-similar pairs and never across differing dates or kinds. Both are opt-in and target the agent's own LLM prompt, which is usually the largest cost centre."
tags:
  - concept
  - memory
  - rag
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/hindsight-models-decision-gated-memory-2026-11-03"
---

# Recall-time prune and dedup (shrinking the agent's prompt)

**Category:** Retrieval Optimization
**Status:** Shipped in Hindsight 1.2, off by default

## Overview

A memory recall ends up in the calling agent's prompt, and for most teams the agent's own LLM is the biggest recurring cost. Classic recall fills its token budget whether the returned memories help or not. This pattern adds two [[Concepts/decision-model-as-memory-judge|decision-model]] gates at the recall boundary so the agent receives only memories that answer the question.

## Prune

Drops memories that are no help to the query.

- **No extra request.** It reuses the ranking answers already produced by the reranker, so pruning adds no decision-model call.
- **Keeps the best memory.** The top-ranked result always survives, which prevents the pathological case of an empty or useless recall.
- **Effect.** A retrieve-20-then-prune-6 pattern shrinks the prompt without a second model pass.

## Dedup

Drops a memory that repeats a better-ranked one, so a fact retained from several documents reaches the agent once.

- **Costs one decision-model request**, but only over memories whose embeddings are alike.
- **Scoped by similarity first.** Cheap vector proximity selects candidate pairs; the judge only adjudicates those.
- **Never merges across time or type.** Memories dated differently, or of two different kinds, are never called repeats. This preserves the distinction between "the same fact, repeated" and "the fact changed over time" — critical for temporal memory.

## Configuration

Both are off by default and can be enabled per request:

```json
"rerank": { "prune": true, "dedup": true }
```

or per bank. Reflect and knowledge-page refreshes search through recall, so they inherit the gates automatically.

## Why it belongs at recall rather than at ingest

- **Query-relative relevance cannot be decided at write time.** Whether a memory helps depends on the question being asked now.
- **The saving compounds per turn.** Every agent turn that follows the recall pays for the tokens; dedup at ingest would still leave query-irrelevant memories in the prompt.
- **Recall is the shared choke point.** Reflect and page refresh both consume recall, so one gate improves three operations.

## Trade-offs

- **Recall quality becomes a model choice.** Pruning is a judgment, and a mis-pruned memory is invisible to the agent. The "best memory always stays" rule is the guardrail, not a guarantee that the rest is right.
- **Dedup needs an embedding model that separates near-duplicates well** — one reason the vendor ships a memory-tuned embedding model alongside the judge ([[Concepts/purpose-built-memory-model-stack]]).
- **The saving is downstream, so it is easy to miss.** The metric that moves is the agent's input-token bill, not the memory system's own latency.

## Related Concepts

- [[Concepts/decision-model-as-memory-judge]] — the division of labour this instantiates
- [[Concepts/evidence-gated-reflect-loop]] — the next gate downstream, which also trims evidence
- [[Concepts/hybrid-retrieval-complementary-halves]] — how the candidate set is produced before pruning
- [[Concepts/hindsight-memory-architecture]] — TEMPR retrieval substrate
- [[Concepts/trajectory-recall-reward]] — measuring whether recalled trajectories were worth their tokens

## References

- Raw: [[Raw/hindsight-models-decision-gated-memory-2026-11-03]]
- Vendor docs: https://hindsight.vectorize.io/developer/api/recall#rerank
