---
title: "Handoff Document Generation"
details: "Compaction method that generates a handoff document through the live-cache side-request pipeline and commits it as a CompactionEntry on the current session — preserving the live agent's prompt cache prefix by sending the active system prompt, tool array, and real LLM message history, then appending one agent-attributed user message containing the handoff prompt."
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

# Handoff Document Generation

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

`handoff` is a compaction method that produces a structured handoff document (rather than a freeform summary) by sending the live agent's active system prompt, tool array, and real LLM message history — then appending one agent-attributed user message containing the handoff prompt. It uses the same `completeSimple(...)` oneshot style as summarization but with `toolChoice: "none"` and joined text blocks returned directly. The result commits as a regular `CompactionEntry` on the current session (no new session is created), so session id, transcript, and provider cache key stay unchanged.

## Core Content

### Generation pipeline (`generateHandoff(...)`)

1. Send the **active system prompt** (verbatim).
2. Send the **tool array** (verbatim).
3. Send the **real LLM message history** (verbatim) — this is what preserves the prompt-cache prefix.
4. Append one **agent-attributed user message** containing the handoff prompt.
5. Force `toolChoice: "none"` (no tools called during handoff).
6. Return joined text blocks directly (no streaming, no compaction entry yet).

### Commit semantics

- The handoff document is stored as the entry's `summary` with `firstKeptEntryId` from `prepareCompaction`.
- Recent history is **kept** (not summarized) — the handoff document sits at the boundary, and the kept messages from `firstKeptEntryId` forward are re-included on rebuild.
- Session id, transcript, and provider cache key are **unchanged** — this is the cache-preservation guarantee.

### When it runs

- **Manual `/handoff`** — via `SessionMaintenance.handoff()`.
- **Auto-maintenance `handoff` method** — when reached in `compaction.methodOrder` after `remote` and `snapcompact` are exhausted, and when the trigger is not overflow (`reason: "overflow"` skips handoff because the request would reuse overflowing input).
- **Post-turn threshold maintenance** schedules handoff as a post-prompt task (not inline) — pre-prompt and mid-turn checks run all methods inline to avoid racing the next turn.

### Optional disk artifact

When `compaction.handoffSaveToDisk = true`, an **automatically triggered** handoff also writes `handoff-<ISO timestamp>.md` in the persisted session's artifact directory.

- Manual handoffs are not written by this setting.
- Non-persisted sessions have no artifact directory, so the setting is a no-op for them.

### Eligibility

- Reachable `handoff` preference may run on `reason: "incomplete"` (input context is still usable).
- **Skipped** for `reason: "overflow"` (input is the overflow source — would reuse the bad input).

## Key Insights

1. **Cache prefix preservation is the whole point.** By sending the live system prompt + tools + real history, the handoff request reads the same prompt cache the previous turn wrote. The resulting document is consistent with the live model's view of the world — no "summary drift" between live turn and handoff.
2. **Recent history is kept.** Unlike a summarization compaction, handoff does not erase recent messages — it just adds a structured document at the boundary. This is what makes handoff usable as a `reason: "incomplete"` recovery (the assistant's last failed turn is still in the context).
3. **`toolChoice: "none"` is required.** The handoff prompt is a one-shot text generation; tool calls during handoff would be wasted (their outputs cannot reach the live session). Forcing `none` keeps the request cheap.
4. **Optional disk artifact is automatic-only.** Manual `/handoff` does not write to disk — the disk artifact is for **automatically triggered** handoffs, so a long-running session that auto-handed-off can produce a human-readable record outside the session journal.

## Related Concepts

- [[Concepts/provider-native-compaction]] — alternative cache-preserving path
- [[Concepts/session-entry-compaction-model]] — what wraps handoff output
- [[Concepts/compaction-trigger-taxonomy]] — which triggers allow handoff
- [[Concepts/notes-backed-context-windows]] — alternative that avoids summarization entirely

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#handoff-generation