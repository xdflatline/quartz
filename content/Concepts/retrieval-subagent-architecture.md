---
title: "Retrieval Subagent Architecture"
details: "Architectural pattern that separates search from generation by routing queries to a specialized retrieval subagent that returns a ranked set of supporting documents to a downstream answering model. Differs from the single-agent loop (one model does both) and from orchestration patterns (subagent-as-tool composition across many roles) by being a strict two-tier division of labor: a frontier reasoning model consumes the retrieved documents and never sees the corpus directly. Chroma Context-1 (Bashir et al., March 2026) operationalizes this as a 20B specialized search model that matches frontier LLMs at ~10x lower cost and latency. Anthropic's multi-agent research system is the multi-agent generalization: an orchestrator spawns parallel search subagents, with token usage explaining 80% of the variance in their internal evaluations."
tags:
  - concept
  - architecture-pattern
  - agent
  - rag
  - multi-agent
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/chroma-context-1-2026-03.md
related:
  - "[[Concepts/subagent-as-tool-composition]]"
  - "[[Concepts/verification-subagent-pattern]]"
  - "[[Concepts/parallel-subagent-process-manager]]"
---

# Retrieval Subagent Architecture

**Source:** [[Raw/chroma-context-1-2026-03]]
**Category:** Architectural Pattern
**Related:** [[Concepts/subagent-as-tool-composition]], [[Concepts/verification-subagent-pattern]], [[Concepts/parallel-subagent-process-manager]]

## Overview

A retrieval subagent architecture is one in which **search and generation are owned by different models**, with the retrieval model returning a ranked document set that a downstream reasoning model consumes. The reasoning model never sees the corpus directly; the retrieval model never produces a final answer.

The split is motivated by two facts the [Context-1 paper]([[Raw/chroma-context-1-2026-03]]) makes explicit:

1. **Search quality and reasoning quality are confounded in end-to-end evaluation.** If a downstream model fails to answer, you cannot tell whether retrieval was insufficient or the reasoning model failed to use what it was given. Isolating the retrieval contribution requires keeping the reasoning model out of the success signal.
2. **Frontier models are expensive as the search loop.** Anthropic's internal evaluation showed the multi-agent research system outperforms single-agent Opus 4 by 90% on research tasks, but token usage alone explained 80% of the variance. The practical barrier is the frontier model itself; offloading search to a smaller, purpose-trained model recovers most of the gain at a fraction of the cost.

## Two Tiers

**Tier 1 — Retrieval subagent.** Iteratively decomposes a query into subqueries, issues tool calls (search, grep, read, prune), and returns a ranked document set. The retrieval model is trained for *search quality*, not answer correctness; its reward signal is recall / precision / trajectory-recall over documents, not accuracy on the final question. Context-1 is the canonical example: 20B gpt-oss-20b base, SFT + CISPO RL, served at MXFP4 on a single B200.

**Tier 2 — Reasoning / answering model.** Receives the question and the ranked documents, produces the final answer. Typically a frontier model — Claude, GPT-5.x, Gemini, Kimi — selected for reasoning quality, not for tool use. The reasoning model has no corpus access and does not need a search tool; the search is done before it sees the query.

The two tiers are not symmetric. The retrieval subagent runs many times (potentially 4× in parallel for [[Research/chroma-context-1]]'s 4x configuration) and the reasoning model runs once on the fused document set.

## Why It Works at 20B

The intuition, articulated in the Context-1 paper, is that retrieval is a much narrower capability than general reasoning. A 20B model trained specifically on multi-hop document retrieval over millions of synthetic tasks can match a frontier model's *retrieval quality* without the general reasoning overhead. The result: a 4x parallel Context-1 rollout, fused with reciprocal rank fusion, is cheaper than a single call to a frontier model.

The paper also documents a generalization result: Context-1 was trained on web, legal, and finance tasks but improves on the held-out email domain and on public benchmarks (BrowseComp-Plus, SealQA, FRAMES, HLE) with different task formats — suggesting the underlying skills (query decomposition, iterative refinement, selective retention) transfer.

## Comparison to Adjacent Patterns

| Pattern | What the subagent does | Where decisions live |
| --- | --- | --- |
| **Single-agent RAG loop** | One model does both search and answer | One model |
| **Retrieval subagent (this page)** | Specialized search model returns documents to a separate answerer | Two roles |
| **Subagent-as-tool composition** | A subagent is callable like any other tool | Parent orchestrator |
| **Anthropic multi-agent research** | Orchestrator spawns parallel search subagents, fuses, answers | Orchestrator + N parallel searchers |

Context-1 is the "single specialized searcher" cell. The Anthropic multi-agent research system is the "orchestrator + N parallel searchers" cell. Both share the architectural choice of separating search from generation; they differ in whether the search tier is one model or many.

## Failure Modes

- **Frontier models with no budget constraint still win on the hardest benchmarks.** The 200k-context-no-prune variants of GPT-5.4 and Opus 4.6 outperform Context-1 (4x) on Seal0 (0.66–0.72 vs 0.52). Hard benchmarks with no natural corpus still favor the most capable single model.
- **Cost of replication at RL training time.** Training requires thousands of tool-call rollouts in parallel (peak 3,000+ q/s in Context-1's setup), which demands replicated search infrastructure. Chroma Cloud handled this; less mature stacks may not.
- **Reasoning model bottleneck.** The architecture does not solve the case where the answering model fails to use the retrieved evidence. The Context-1 paper isolates search quality by avoiding this confound, but a production deployment still has to pick a reasoning model that reads documents well.

## When to Use

- The bottleneck is **retrieval quality at low cost**, not reasoning quality.
- The corpus is large enough that stuffing it into one prompt is infeasible.
- Multi-hop reasoning over retrieved evidence is the dominant work pattern.
- The reasoning model is already a frontier LLM and you want to avoid paying its cost per search.

When *not* to use: when the question can be answered from a single retrieved chunk, or when the corpus is small enough to fit in context. A 20B specialized model is overkill for either.
