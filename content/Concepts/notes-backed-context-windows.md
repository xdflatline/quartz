---
title: "Notes-Backed Context Windows"
details: "Experimental alternative to summary compaction that replaces automatic summary recompression with local context-window boundaries: a model-managed context_notes notebook, a new_context rollover at safe tool-loop boundaries, and a history://current/full retrieval route that exposes the original journal. Opt-in via compaction.experimentalContextManagement; keeps the session journal as the single source of truth."
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

# Notes-Backed Context Windows

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Experimental (`compaction.experimentalContextManagement = false` default)

## Overview

An opt-in alternative to summary compaction that keeps the original session journal as ground truth and uses three local mechanisms — a model-managed `context_notes` notebook, a `new_context` rollover at safe tool-loop boundaries, and a `history://current/full` retrieval route — instead of asking a summarization model to compress history. Enabling it adds `context_notes` and `new_context` to the running session's tool roster (and removes them on disable).

## Core Content

### Enabling

```yaml
compaction:
  experimentalContextManagement: true
```

Or toggle **Notes-backed context windows (experimental)** in `/settings`, then restart the session to refresh its tool roster. The mode also applies to `/compact` without an explicit mode or focus text — explicit compaction modes and focused instructions retain their existing behavior.

### `context_notes` — model-managed notebook

- Reads the current notebook when `text` is omitted.
- Replaces it when `text` is supplied.
- Clears it with `text: ""`.
- **Notebook revisions are journal entries on the active branch.** Only the latest visible revision is injected into model context, including after resume or fork.
- A context reset clears the visible notebook.
- Each replacement is limited to **16,384 UTF-8 bytes**; oversized writes fail without replacing the notes.

### `new_context` — local rollover

- Requests rollover at the next safe tool-loop boundary.
- Rollover **retains complete recent tool-call/result units and the notebook** without calling a summarization model.
- Near the automatic threshold, the model receives a once-per-window reminder to save its working state.

### `history://current/full` — raw-history retrieval

- `read` and `grep` can recover original messages and tool outputs through this route.
- The text includes **stable entry IDs** and window boundaries.
- Shared selectors work: `history://current/full:1-200`, `history://current/full:raw:1-200`.
- Queries, fragments, trailing slashes, and additional path components are rejected.
- Bound to the **calling session's current branch** — never falls back to another registered agent or an on-disk session search.
- Existing `history://<id>` routes retain their concise transcript behavior.

### Eligibility

Experimental rollover requires the effective tool set to contain `context_notes`, `new_context`, `read`, and `grep`. Restricted sessions without all four retain legacy maintenance.

### Disable behavior

Disabling the setting:
- Restores legacy compaction.
- Disables the experimental tools and full-history route.
- Existing notes remain in the journal and provider context (not erased).

### Caveats (from the doc footnote)

- Earlier pruning or explicit destructive history operations **cannot be undone** by enabling the setting.
- Text history represents images as markers.
- Notebook quality and timely updates remain the model's responsibility — the mode does not automatically generate missing notes.

## Key Insights

1. **Journal is the single source of truth.** Unlike summary compaction (which replaces the original prefix with a summary), notes-backed windows keep the full journal and only inject the notebook into context. The model can always recover the original messages via `history://current/full`.
2. **Notebook is a journal entry itself.** Each `context_notes` write is a branch-bound journal entry. The visible revision is the latest; forks and resumes see consistent state because they share the journal.
3. **Rollover is local, not summarization.** `new_context` does not call a summarizer — it just retains complete recent tool-call/result units and the notebook. This is why the strategy is faster and cheaper than summary compaction, but pushes more responsibility onto the model to maintain the notebook.
4. **Once-per-window reminder.** Near the automatic threshold, the model gets a reminder to save its working state — a soft nudge that turns the notebook from a passive store into an active survival mechanism.
5. **Stable entry IDs make retrieval usable.** Without stable IDs, `history://current/full:1-200` would refer to shifting content. Stable IDs are what let the model address specific journal entries from inside a notes-backed window.

## Related Concepts

- [[Concepts/session-entry-compaction-model]] — the journal schema that notes-backed windows preserve
- [[Concepts/pre-compaction-tool-result-pruning]] — the legacy prune pass, still used as a pre-rollover reclaim
- [[Concepts/compaction-trigger-taxonomy]] — the trigger taxonomy applies to legacy maintenance, not notes-backed mode

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#experimental-notes-backed-context-windows