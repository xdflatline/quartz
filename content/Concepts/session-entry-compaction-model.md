---
title: "Session-Entry Compaction Model"
details: "Pattern where compaction and branch summaries are first-class session entries with their own types (CompactionEntry, BranchSummaryEntry), persisted alongside ordinary message entries and converted back into user-context messages by a dedicated buildSessionContext step. This decouples summary storage from summarizer output and lets the journal be the single source of truth."
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

# Session-Entry Compaction Model

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated (oh-my-pi reference implementation)

## Overview

A session-journal schema where `CompactionEntry` and `BranchSummaryEntry` are first-class record types, not plain assistant/user messages. The session store carries them in the same ordered stream as ordinary turns; a dedicated `buildSessionContext` pass converts them back into `compactionSummary` / `branchSummary` user-context messages, which `convertToLlm()` then renders through static templates before they reach the provider. This separates the **summary as data** from the **summary as LLM input**, letting one compaction entry carry both provider-native payloads (`preserveData.openaiRemoteCompaction`, `preserveData.anthropicCompaction`) and a textual fallback summary for non-replaying providers.

## Core Content

### Entry shapes

```ts
CompactionEntry {
  type: "compaction"
  summary: string                 // always set
  shortSummary?: string
  firstKeptEntryId: string        // compaction boundary
  tokensBefore: number
  details?, preserveData?, fromExtension?, providerReplayThroughEntryId?
}

BranchSummaryEntry {
  type: "branch_summary"
  fromId: string
  summary: string
  details?, fromExtension?
}
```

The boundary `firstKeptEntryId` refers to an **original entry** in the journal — preparation does not move, duplicate, or rewrite journal entries. This makes the journal a write-once log: compaction appends, never edits in place.

### Rebuild order in `buildSessionContext`

1. Latest compaction on the active path → one `compactionSummary` message.
2. Kept entries from `firstKeptEntryId` to the compaction point are re-included.
3. Later entries on the path are appended.
4. `branch_summary` entries → `branchSummary` messages.
5. `custom_message` entries → `custom` messages.

### Render step in `convertToLlm()`

- `compactionSummary` and `branchSummary` → user messages rendered through `prompts/compaction-summary-context.md` / `prompts/branch-summary-context.md` (static templates).
- `custom` messages → developer messages with raw content (no template).

### Native replay requirements

Native replay (`providerReplayThroughEntryId`) requires a matching provider and a Responses-family API on the active model. A separate native compaction endpoint does not give a Chat Completions or Anthropic encoder the ability to consume its output. Disabling future native compaction does **not** disable normal replay of an existing payload — but compaction preparation has a stricter reuse policy: local summarization must re-expand the original messages rather than treat an opaque placeholder as a readable summary.

### Cut-point rules (from `prepareCompaction()`)

Valid cut points:
- message entries with roles: `user`, `assistant`, `bashExecution`, `hookMessage`, `branchSummary`, `compactionSummary`
- `custom_message` entries
- `branch_summary` entries

Hard rule: **never cut at `toolResult`** (preserves tool-call/result pairing). Pure metadata (`model_change`, `thinking_level_change`, labels) is filtered before cut-point selection but remains in the journal.

### Region partition

Every effective original message belongs to exactly one of three regions:
- `messagesToSummarize` (history side)
- `turnPrefixMessages` (split-turn prefix)
- `recentMessages` (retained)

For local summaries this is a hard invariant; for provider-native or speculative native replay it is not (the native payload may already cover the retained tail, and preparation must not double-count it).

## Key Insights

1. **Single source of truth.** The journal carries both the original messages and the summarizer outputs. There is no separate "compaction history" store; rebuilds reconstruct LLM input deterministically from the active leaf.
2. **Dual-track payloads.** `preserveData` carries provider-native structures (`openaiRemoteCompaction` version `"v2"`, `anthropicCompaction`, `snapcompact` PNG frames), while the textual `summary` remains readable by any provider. This lets one entry survive provider switching without rewriting.
3. **Display vs LLM context are separate.** The display transcript (`buildTranscriptSessionContext`) renders every path entry chronologically with inline divider glyphs (`── 📷 compacted · ctrl+o ──`) — only the LLM context resets at the compaction boundary, so the user's scrollback is preserved across resume.
4. **Split-turn summarization.** When the cut point is not at a user-turn start, compaction produces two summaries (history + turn prefix) merged into one stored summary with a `**Turn Context (split turn):**` divider.

## Related Concepts

- [[Concepts/compaction-trigger-taxonomy]] — what kicks off a new compaction entry
- [[Concepts/branch-summary-tree-navigation]] — the sibling `BranchSummaryEntry` pipeline
- [[Concepts/pre-compaction-tool-result-pruning]] — happens before a new entry is appended
- [[Concepts/notes-backed-context-windows]] — the experimental alternative that keeps the journal unchanged across "compactions"
- [[Concepts/agentic-harness-architecture]] — neighboring pattern

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#session-entry-model