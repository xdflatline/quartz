---
title: "Async Speculative Compaction"
details: "Pre-threshold background summarization that arms a compaction result so it can be committed instantly when the threshold is actually crossed, hiding summarization latency. Runs the first configured LLM-backed method (remote, handoff, or soft) off a branch snapshot in a side session; armed results are discarded on branch-prefix changes, native-replay incompatibility, or excessive post-snapshot growth."
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

# Async Speculative Compaction

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated (default-on)

## Overview

When `compaction.asyncEnabled = true` (default), maintenance watches for context entering the pre-threshold band `[threshold − lead, threshold)` and starts a background summarization for the first configured LLM-backed method (`remote`, `handoff`, or `soft`) off a **branch snapshot** in a **side session**. The result is held "armed" and committed instantly when the threshold is actually crossed — post-snapshot turns are appended after the summary unchanged. This hides summarization latency from the live turn.

## Core Content

### Pre-threshold band

- `lead = clamp(threshold × 0.125, 8192, 32000)` — between 8,192 and 32,000 tokens below the threshold, scaled with window size.
- When context enters `[threshold − lead, threshold)`, async maintenance starts a background summary.

### Snapshot isolation

The speculation runs **off a branch snapshot** — a fork of the active path at the moment the speculation started — and is **isolated from the live turn by a side session id**. The live turn continues to write to the main session; the speculation runs on its own side session with the snapshot.

### Commit semantics

- **Armed result** is committed instantly when the threshold is actually crossed.
- Post-snapshot turns are appended after the summary unchanged — the live turn's writes since the snapshot started are not duplicated into the summary.

### Discard conditions (armed result is dropped)

1. Branch prefix changes — new compaction, reset boundary, `/tree` navigation.
2. Provider-native replay payload is no longer readable by the active model.
3. Context grows past `keepRecentTokens` since compute — a fresh speculation replaces it.

### Skip conditions (speculation does not start)

- An extension registers `session_before_compact` — extension pre-compaction control has priority.

### Status-line signaling

The status line pulses the auto-compact icon while a speculation runs and holds it in accent when a result is armed. Operators can see the speculative work happening even though the live turn is unaffected.

## Key Insights

1. **Snapshot, not live.** Speculation runs on a branch snapshot in a side session, so the live turn's writes cannot race with the summary or pollute its input. This is what guarantees the post-snapshot turns can be safely appended after the summary unchanged.
2. **Discard-by-event, not discard-by-version.** The three discard conditions are all branch-identity events (new compaction, reset, `/tree`, native-replay mismatch, growth past `keepRecentTokens`), not version counters. Once the live path has changed materially, the speculation's assumptions no longer hold.
3. **Latency hiding, not latency reduction.** Async compaction does not make summarization faster — it makes it invisible to the user. The total work is the same; the user-perceived wait is zero when the threshold is crossed.
4. **Only LLM-backed methods.** Shake and snapcompact don't speculate — they are local and instant. Only the methods that pay a network round-trip (`remote`, `handoff`, `soft`) are worth speculating on.

## Related Concepts

- [[Concepts/compaction-trigger-taxonomy]] — what the speculation pre-stages for
- [[Concepts/session-entry-compaction-model]] — what gets committed when the threshold crosses
- [[Concepts/provider-native-compaction]] — primary speculative target
- [[Concepts/handoff-document-generation]] — also speculative-eligible

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#settings-and-defaults