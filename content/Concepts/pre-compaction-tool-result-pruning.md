---
title: "Pre-Compaction Tool-Result Pruning"
details: "Inline elision of large tool outputs that runs before any compaction method, with a 40k-token recent protected window, a 20k-token minimum savings requirement, a 50-token per-result floor to avoid cache churn, plus a separate useless-result elision path that uses a different placeholder and bypasses the protected window. Defaults keep prompt-cache continuity intact."
tags:
  - concept
  - context-engineering
  - architecture-pattern
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# Pre-Compaction Tool-Result Pruning

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Two cooperating elision passes — `pruneToolOutputs` (token-budget pruning) and `pruneSupersededToolResults` (stale/useless-result pruning) — that run before any compaction method and can reduce the measured token count enough to defer a trigger. They replace blanked tool results with deterministic placeholders and **never remove the result from history**, only blank it in place, so tool-call/result pairing and provider-native replay remain intact.

## Core Content

### Default `pruneToolOutputs` policy

| Knob | Default | Why |
|------|---------|-----|
| Protect newest tool-output tokens | `40_000` | Recent results are most likely to be re-referenced; cache-friendly |
| Minimum total estimated savings | `20_000` | Sub-threshold prunes churn cache for little benefit |
| Minimum per-result size (`MIN_PRUNE_TOKENS`) | `50` tokens | Placeholder is ~8 tokens; pruning smaller grows the context |
| Protected tools | `skill` results, `read` of `skill://` paths, plan reference file | User-installed skills and active plan must stay verbatim |

### Placeholder

Pruned tool results are replaced with:

```
[Output truncated - N tokens]
```

If pruning changes entries, session storage is rewritten and agent message state is refreshed **before** compaction decisions are made.

### Superseded / useless — separate rules

**Superseded reads** prune for correctness regardless of size (a `read` whose result is overwritten by an `edit` to the same file is stale, even if small).

**Useless results** — flagged via `AgentToolResult.useless` (set by `ToolResultBuilder.useless()` or directly on the returned object) — bypass the protected recent window like superseded reads and receive the more specific `[Uneventful result elided]` (`USELESS_NOTICE`) placeholder instead of the token-count one.

### Useless-flag consumers (three places)

1. **Per-turn stale-result pass** (`pruneSupersededToolResults`, gated by `compaction.dropUseless`, default on): blanked to `USELESS_NOTICE` with cache-aware timing — only when the suffix after the candidate is small (≤ ~8k tokens) **or** the session has idled past the provider prompt-cache lifetime. Results smaller than the notice itself are never blanked (no savings); protected tools are exempt.
2. **Threshold prune** (`pruneToolOutputs`): flagged results bypass the protect-recent window, same as superseded reads, and receive `USELESS_NOTICE`.
3. **Summary serialization** (`serializeConversation` in both agent and snapcompact): the entire tool call/result pair is dropped from summarizer/archive input — the source region is discarded after summarization anyway, so the exclusion costs no cache.

### Hard invariants

- The `useless` flag is **never** set together with `isError` — errors always win.
- The flag never reaches provider wire formats.
- Flagged pairs are never removed from history (only blanked in place), so tool-call/result pairing and provider-native history replay stay intact.

## Key Insights

1. **Pruning can defer a compaction trigger.** By blanking large historical results before threshold comparison, the measured token count drops below `resolveThresholdTokens(...)` and the trigger is avoided. This is the cheapest possible context reclaim — no LLM call, no summary commit.
2. **The 50-token floor prevents cache thrash.** A placeholder costs ~8 tokens; replacing a 30-token result with an 8-token placeholder is a net loss *and* invalidates the prompt-cache prefix downstream. The floor guarantees prunes are always net-positive.
3. **Three coordinated consumers.** The same `useless` flag is consumed at three different layers — per-turn stale pass, threshold prune, summary serialization — each with different rules. The flag is **data**, not behavior.
4. **Cache-aware timing.** The per-turn pass only runs when the suffix is small enough or the cache is already dead — pruning mid-cache invalidates downstream turns and pays the cache-miss penalty.

## Related Concepts

- [[Concepts/compaction-trigger-taxonomy]] — what these passes defer
- [[Concepts/shake-compaction-method]] — heavier inline elision of fenced/XML blocks (uses `artifact://` references)
- [[Concepts/snapcompact-bitmap-archival]] — separate archival path that serializes pruned-out history as PNG frames

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#pre-compaction-pruning