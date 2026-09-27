---
title: "Branch Summary on Tree Navigation"
details: "Pipeline that captures abandoned branch context as a BranchSummaryEntry when navigating the session tree (/tree), distinct from token-overflow compaction. Computes budget as contextWindow - reserveTokens, walks newest-to-oldest adding messages until the budget is reached, and attaches the summary at the navigation target using branchWithSummary(). Driven by branchSummary.enabled."
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

# Branch Summary on Tree Navigation

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated (gated by `branchSummary.enabled = false` default)

## Overview

Branch summarization is tied to **tree navigation**, not token overflow. When the user navigates the session tree (e.g., via `/tree`), the entries from the abandoned leaf to the common ancestor are summarized and attached at the navigation target as a `BranchSummaryEntry`. The abandoned branch itself is preserved unchanged — only the navigation target carries the new summary, so future resumes see the summary at that branch point but the abandoned history is still recoverable.

## Core Content

### Trigger (during `navigateTree(...)`)

1. Compute abandoned entries from old leaf to common ancestor using `collectEntriesForBranchSummary(...)`.
2. If caller requested summary (`options.summarize`), generate summary before switching leaf.
3. If summary exists, attach it at the navigation target using `branchWithSummary(...)`.

Operationally this is commonly driven by `/tree` flow when `branchSummary.enabled` is enabled.

### Branch-switch shape

```
Tree before navigation:

         ┌─ B ─ C ─ D (old leaf, being abandoned)
    A ───┤
         └─ E ─ F (target)

Common ancestor: A
Entries to summarize: B, C, D

After navigation with summary:

         ┌─ B ─ C ─ D (abandoned branch, unchanged)
    A ───┤
         └─ E ─ F ─ [summary of B,C,D] (new leaf)
```

### Preparation and token budget

`generateBranchSummary(...)` computes:

```
tokenBudget = model.contextWindow - branchSummary.reserveTokens
```

`prepareBranchEntries(...)` then:

1. **First pass:** collect cumulative file ops from all summarized entries, including prior pi-generated `branch_summary` details.
2. **Second pass:** walk newest → oldest, adding messages until the token budget is reached.
3. Prefer preserving recent context.
4. May still include large summary entries near the budget edge for continuity.

Compaction entries are included as messages (`compactionSummary`) during branch summarization input — so a previously summarized branch doesn't lose its summary when re-summarized.

### Summary generation and persistence

Branch summarization:

1. Converts and serializes selected messages.
2. Wraps in `<conversation>`.
3. Uses custom instructions if supplied, otherwise `branch-summary.md`.
4. Calls summarization model with `SUMMARIZATION_SYSTEM_PROMPT`.
5. Prepends `branch-summary-preamble.md`.
6. Appends file-operation tags.

Result is stored as `BranchSummaryEntry` with optional details (`readFiles`, `modifiedFiles`).

### Render step

When context is rebuilt, `branch_summary` entries are converted to `branchSummary` user-context messages and rendered through `packages/agent/src/compaction/prompts/branch-summary-context.md`.

### Cancellation

Branch summarization can be cancelled via abort signal (e.g., Escape), returning a canceled/aborted navigation result. The abandoned branch is left unchanged; no `BranchSummaryEntry` is committed.

### Hook surface

`session_before_tree` runs on tree navigation before default branch summary generation and can:
- cancel navigation
- provide custom `{ summary: { summary, details } }` used when user requested summarization

`session_tree` is the post-navigation event exposing new/old leaf and optional summary entry.

## Key Insights

1. **Distinct from compaction.** Branch summarization is triggered by navigation, not token overflow. The token budget here is `contextWindow - branchSummary.reserveTokens`, independent of the threshold maintenance budget. They are not interchangeable.
2. **Walk newest-to-oldest.** The second pass walks from newest to oldest, adding messages until the budget is reached — preserving recent context. Large summary entries near the budget edge may still be included for continuity.
3. **Abandoned branch is preserved.** Only the navigation target carries the new summary. The abandoned branch entries are unchanged in the journal. This is what makes `/tree` navigation reversible by resuming the abandoned leaf.
4. **Default is off.** `branchSummary.enabled = false` — this is opt-in. Users who don't navigate trees frequently don't pay the storage or summarization cost.
5. **File-ops are cumulative.** The first pass collects cumulative file ops from all summarized entries, so a branch that read many files and modified fewer of them gets a single coherent file-operations section in the summary.

## Related Concepts

- [[Concepts/session-entry-compaction-model]] — the `BranchSummaryEntry` schema
- [[Concepts/compaction-trigger-taxonomy]] — when threshold maintenance runs (different)
- [[Concepts/notes-backed-context-windows]] — alternative that avoids summarization entirely

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#branch-summarization-pipeline