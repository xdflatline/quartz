---
title: "Agentic Self-Pruning of Context During Retrieval"
details: "Pattern for multi-turn retrieval agents in which the agent itself decides which retrieved chunks to keep or discard via a dedicated prune_chunks tool, under a hard token budget enforced by the harness. Differs from summarization (lossy, irreversible compression) and from external memory paging (MemGPT, RLM — moves data outside the prompt) by performing selective, document-level retention inside the prompt. The agent has continuous visibility into its own token usage, a soft threshold that injects prune suggestions, and a hard cutoff past which only prune_chunks is accepted. Chroma Context-1 (Bashir et al., March 2026) demonstrates this: prune accuracy rose from 0.824 (base gpt-oss-20b) to 0.941, and trajectory recall rewards were made tractable because the harness preserves the full unpruned trajectory for credit assignment."
tags:
  - concept
  - context-engineering
  - agent
  - rag
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/chroma-context-1-2026-03.md
related:
  - "[[Concepts/context-rot]]"
  - "[[Concepts/scratchpad-context-window-management]]"
  - "[[Concepts/hybrid-retrieval-complementary-halves]]"
---

# Agentic Self-Pruning of Context During Retrieval

**Source:** [[Raw/chroma-context-1-2026-03]]
**Category:** Context Engineering Pattern
**Related:** [[Concepts/context-rot]], [[Concepts/scratchpad-context-window-management]], [[Concepts/hybrid-retrieval-complementary-halves]]

## Overview

In multi-turn retrieval, the agent's context window fills rapidly with retrieved documents — many tangential, redundant, or superseded by later evidence. Past a certain size, [context rot]([[Concepts/context-rot]]) degrades retrieval quality and inflates cost. Three families of remedies exist, and they differ in *where* the decision to discard lives and *what* is discarded:

1. **External memory paging** — MemGPT-style agents read and write from slower external storage, treating the prompt as a fast cache. Trades prompt real-estate for I/O round-trips.
2. **Lossy compression** — ReSum and similar systems periodically summarize accumulated context. Discards fine-grained evidence.
3. **Agentic self-pruning** — the agent itself, via a `prune_chunks(chunk_ids)` tool, decides which retrieved chunks to discard. The decision lives in the agent's policy; the harness simply enforces.

This page is about (3), as practiced by [[Entities/chroma]] Context-1 (Bashir et al., March 2026) and distilled in the source paper's "Agent Harness" section.

## Mechanism

The harness binds the context to a fixed token budget `T_budget`. Each tool call can return up to `S_budget` tokens of chunk content, yielding roughly `T_budget / S_budget` searches before the budget is exhausted.

Three layered mechanisms make the agent aware of and able to manage its budget:

- **Continuous visibility** — after every turn the harness appends the current token usage to the observation (`[Token usage: 14,203/32,768]`). The model always knows its headroom.
- **Soft threshold** — past `T_budget / 2`, the harness injects a suggestion that the model start pruning or concluding. Search and read results are truncated to fit the remaining budget, with a reserve kept for the model's next response. (Training-only; not shown at inference.)
- **Hard cutoff** — past a configurable threshold between `T_budget / 2` and `T_budget`, all tool calls except `prune_chunks` are rejected. The error message directs the model to prune or conclude.

When the model calls `prune_chunks`, the harness removes the specified chunks from the model's *view* but preserves the full unpruned trajectory for reward computation. This split — the model sees a pruned context; the reward sees everything — is what makes trajectory-recall credit assignment possible.

## Why Selective Retention over Compression

Summarization (e.g. ReSum) avoids external memory but discards fine-grained evidence that may prove relevant in later retrieval turns. Self-pruning preserves evidence at document granularity: the agent keeps or discards whole chunks rather than blending them into a summary. For multi-hop retrieval where the *exact* span later matters, lossy summaries are an irreversible loss; selective retention is not.

The training data also reflects this choice: [Context-1 is trained on document-level retention, not summaries]([[Research/chroma-context-1]]). The "Future Directions" section of the source paper flags hybrid approaches (selective retention of high-value passages plus targeted summarization) as a future direction, not a substitute.

## Prune Accuracy as a Trainable Skill

Self-pruning is only useful if the agent can identify irrelevant chunks reliably. Context-1 reports:

| Model | Prune accuracy |
| --- | --- |
| gpt-oss-20b (base) | 0.824 |
| Context-1 (trained) | 0.941 |

This is a learnt behavior: the SFT warmup exposes the model to well-formed pruning decisions from Kimi K2.5 rollouts, and the RL reward includes a repeated-pruning penalty (`p_prune = 0.1` per excess call beyond 3 consecutive, capped at 0.5) that discourages one-at-a-time batched-pruning anti-patterns.

## Reward Implications

Because the harness preserves the unpruned trajectory, the reward can credit the agent for documents it *encountered* during search even if they were later pruned. This is the [trajectory-recall reward term]([[Concepts/trajectory-recall-reward]]), and it is what prevents a degenerate strategy of "issue one broad search and prune everything else" — under pure output-F1 that strategy can score well, but under `r = 0.7·F_β + 0.3·r_traj + r_fa − penalties` it loses the trajectory-recall signal.

## Failure Modes

The source paper flags several:

- **Early termination under hard cutoff** — when frontier models were given a 200k budget and no prune tool, they outperformed their token-constrained counterparts. One reason: under budget pressure the agent terminates earlier, missing documents it would otherwise have encountered.
- **Lossy summarization** — abandoned in favor of selective retention; hybrid is the open direction.
- **One-by-one pruning** — explicitly penalized during training.

## Related Work

- [MemGPT](https://arxiv.org/abs/2310.08560) — external memory paging; a different point in the design space.
- [ReSum](https://arxiv.org/pdf/2509.13313) — periodic summarization; explicitly distinguished from self-pruning in the Context-1 paper.
- [SWE-Pruner](https://arxiv.org/abs/2601.16746) — trained 0.6B neural skimmer for source-code line selection; similar idea, task-specific.
- [Anthropic Opus-4.5 context awareness](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf) — clear stale tool-call results based on recency; harness-side pruning rather than agent-decided.
- [Recursive Language Models](https://arxiv.org/abs/2512.24601) — treats the prompt as a variable in an external REPL the model inspects programmatically.
