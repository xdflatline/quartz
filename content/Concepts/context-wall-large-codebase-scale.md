---
title: "The Context Wall in Large Codebase Work"
details: "The gap between a model's nominal context window and the point at which output quality actually degrades. Nominal windows reach a million tokens, but effective intelligence falls off past roughly 30,000 tokens in a request because quadratic attention and provider-side sparse or sliding-window techniques break down across a full window — which is why long-running single coding agents degrade and why context must be fetched, not accumulated."
tags:
  - concept
  - llm
  - context-engineering
  - coding-agent
created: 2026-10-23
updated: 2026-10-23
type: concept
sources:
  - "Raw/sedaily-episode-1975-blitzy-2026.md"
---

# The Context Wall in Large Codebase Work

**Source:** [[Raw/sedaily-episode-1975-blitzy-2026]]
**Category:** Limitation / Context Engineering
**Status:** Empirically observed (figures from [[Entities/blitzy]] engineering practice, episode 1975)

---

## Overview

The context wall is the point where a model's *effective* reasoning capacity degrades, which arrives far earlier than its *nominal* context window suggests. Every design decision for coding agents on large codebases is downstream of this fact: context must be **fetched on demand** from a substrate, not accumulated into a growing session.

## The three numbers

| Quantity | Value | Notes |
|---|---|---|
| Nominal context window | 1,000,000 tokens | ~100,000 lines of code |
| Provider effective ceiling | < 300,000 tokens | Providers apply sparse attention, sliding-window attention, or similar across the remainder |
| Practical intelligence degradation | Past ~30,000 tokens in the request | ~30,000 lines of code; quality falls off here |
| Long-context pricing threshold | ~272,000 tokens (one provider cited) | Requests above this are priced as long-context |

## The mechanism

Attention is quadratic: every token must map to every other token by a dot product in the matrix. No amount of compute or trick makes that effective across an entire window, so providers truncate the usable span with sparse or sliding-window attention. The nominal number is a capacity claim; the effective number is a quality claim, and only the second one matters for agent design.

## Why this breaks long-running agents

The wall explains a pattern practitioners recognise without being able to name it: quality in single-agent CLI tools degrades the longer they run, and every provider's guidance is to do short-running jobs. The cause is cumulative: a long session's context fills with tool output, intermediate reasoning, and stale file contents — and once past the effective threshold, the model is reasoning inside its own weakened regime.

The observation that generalises: a human-scale session transcript that filled ~700K tokens had "blown up all of the context writing the project," so the next task required compaction — and compaction loses far more than the plan it nominally preserves. The plan is a two-pager; the work is tens or hundreds of thousands of lines. A transcript cannot carry both.

## Design implications

- **Don't accumulate context; index it.** Build a substrate that can be queried for the one relevant item (see [[Concepts/codebase-knowledge-graph-context-substrate]]).
- **Don't rely on compaction to save a long session.** Compaction loses the work, not just the trivia.
- **Resume from a substrate, not a transcript.** See [[Concepts/refine-pr-resume-from-substrate]].
- **The wall is also a routing signal.** A model operating past the effective threshold is a worse tiebreaker than a fresh one — the basis of [[Concepts/multi-model-cross-tiebreak-routing]].

## Related Concepts

- [[Concepts/codebase-knowledge-graph-context-substrate]]
- [[Concepts/context-rot]]
- [[Concepts/context-gap-classification]]
- [[Concepts/compaction-trigger-taxonomy]]
- [[Concepts/async-speculative-compaction]]
- [[Concepts/scratchpad-context-window-management]]
- [[Concepts/multi-model-cross-tiebreak-routing]]

## Related Entities

- [[Entities/blitzy]]
- [[Entities/sid-pardeshi]]
