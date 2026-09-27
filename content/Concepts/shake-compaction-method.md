---
title: "Shake Compaction Method"
details: "Inline, local, model-free reduction step used as a compaction.methodOrder entry. Replaces eligible tool results and large fenced/XML blocks with recoverable artifact:// references, using a protected recent-token window and a minimum-savings threshold. Auto-shake emits the same auto-compaction events as LLM summarization but never calls a summarizer."
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

# Shake Compaction Method

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

`shake` is a compaction method that performs an inline, local, **model-free** reduction of context. It replaces eligible tool results and large fenced/XML blocks with recoverable `artifact://` references (rather than placeholder text), using a protected recent-token window and a minimum-savings threshold. Including `shake` in `compaction.methodOrder` makes it a first-class contender alongside `remote`, `snapcompact`, `handoff`, and `soft`.

## Core Content

### Behavior

- Local reduction — no API key, no network, no summarization model.
- Replaces eligible tool results and large fenced/XML blocks with `artifact://` references (recoverable, not just blanked).
- Uses a protected recent-token window (so the most recent context is preserved verbatim).
- Requires a minimum-savings threshold; otherwise the pass is a no-op.

### Event emission

Automatic shake emits the same `session_compact`-family events as LLM summarization, but with `action: "shake"`. The status line and UI hooks cannot distinguish auto-shake from auto-soft-compaction by event family — they must inspect the `action` field.

### Method-order semantics

- **Threshold, incomplete-output, and overflow recovery** advance to the next configured method when shake cannot reclaim enough context to get below the recovery band. This prevents repeated no-op shake loops in automatic maintenance.
- **Idle shake** does not use that fallback — the idle timer rechecks usage before running again.
- **Manual `/shake`** is a separate, more aggressive command that can target all eligible history (no protected recent window, no minimum-savings threshold for the manual variant).

### Distinction from `pruneToolOutputs`

| Pass | Scope | Replaces with | Frequency |
|------|-------|---------------|-----------|
| `pruneToolOutputs` (pre-compaction) | Token-budget over tool results only | `[Output truncated - N tokens]` placeholder | Runs before every compaction check |
| `shake` (compaction method) | Tool results + large fenced/XML blocks | `artifact://` references | Runs only when reached in `compaction.methodOrder` |

## Key Insights

1. **Recovery vs blanking.** Shake replaces content with `artifact://` references, not placeholders. The references are still resolvable to the original content, so downstream `read`/`grep` of the journal can recover the elided material.
2. **Method-order fallback prevents loop pathology.** Without advancing past shake on insufficient savings, an automatic maintenance path that keeps hitting shake would burn cycles doing nothing. The fallback to the next method is what gives `compaction.methodOrder` its try-then-escalate shape.
3. **Idle shake has different fallback semantics.** Idle maintenance's primary value is reducing context before a user comes back; if shake doesn't reclaim enough, the idle timer just rechecks later — there is no rush to escalate to a more expensive method.
4. **Manual vs automatic are different commands.** `/shake` (manual) is more aggressive — no protected window, no threshold. Including shake in `compaction.methodOrder` does not change `/shake`'s behavior.

## Related Concepts

- [[Concepts/pre-compaction-tool-result-pruning]] — runs before shake, smaller-scope
- [[Concepts/snapcompact-bitmap-archival]] — alternative offline method that archives (shake just elides)
- [[Concepts/compaction-trigger-taxonomy]] — what calls shake in the first place

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#shake-method