---
title: "Research Index: oh-my-pi Compaction Architecture"
details: "Cross-cutting synthesis of the oh-my-pi compaction architecture (can1357/oh-my-pi@main, docs/compaction.md, 2026-09-27): session-entry model, six trigger paths, pre-compaction pruning, shake/snapcompact/handoff/native-remote methods, branch summarization on tree navigation, async speculative compaction, and the experimental notes-backed-context-windows alternative."
tags:
  - research
  - context-engineering
  - agent
  - survey
created: 2026-09-27
updated: 2026-09-27
type: research
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# Research Index: oh-my-pi Compaction Architecture

**Updated:** 2026-09-27
**Source:** oh-my-pi `docs/compaction.md` (can1357/oh-my-pi@main, commit `6962d5c`, 2026-09-24) — fetched 2026-09-27

## Overview

oh-my-pi is a Claude-Code-style coding-agent harness whose compaction architecture is the most thoroughly documented in the open-source coding-agent space as of mid-2026. The doc at hand describes a single, layered system that combines first-class journal entries (`CompactionEntry` / `BranchSummaryEntry`), six distinct trigger paths, five compaction methods (`remote`, `snapcompact`, `handoff`, `shake`, `soft`), pre-compaction pruning, async speculative compaction, and an experimental notes-backed alternative — all wired together with extension hooks (`session_before_compact`, `session.compacting`, `session_compact`, `session_before_tree`, `session_tree`).

This index groups the extracted concepts by domain rather than by section, so a reader can scan the design space.

## Concepts

### Journal schema

- [[Concepts/session-entry-compaction-model]] — first-class `CompactionEntry` and `BranchSummaryEntry` types; the journal is the single source of truth; `preserveData` carries provider-native payloads alongside a textual fallback summary.

### Triggering

- [[Concepts/compaction-trigger-taxonomy]] — six trigger paths (manual, overflow, incomplete-output, threshold, mid-turn threshold, idle), each with distinct semantics for `willRetry`, handoff eligibility, and auto-continue.
- [[Concepts/async-speculative-compaction]] — pre-threshold background summarization that arms a result for instant commit.

### Pre-compaction passes

- [[Concepts/pre-compaction-tool-result-pruning]] — `pruneToolOutputs` (token-budget) and `pruneSupersededToolResults` (stale/useless), three coordinated consumers of the `useless` flag.

### Compaction methods

- [[Concepts/shake-compaction-method]] — inline, local, model-free reduction using `artifact://` references.
- [[Concepts/snapcompact-bitmap-archival]] — offline archival as model-aware PNG frames (per-family billing calculations).
- [[Concepts/provider-native-compaction]] — OpenAI Responses compact (V1/V2), Anthropic server-side `compact-2026-01-12` beta, custom `/chat/completions` endpoints.
- [[Concepts/handoff-document-generation]] — live-cache-preserving handoff document committed as a `CompactionEntry` on the same session.

### Navigation

- [[Concepts/branch-summary-tree-navigation]] — abandoned-branch summarization on `/tree`, distinct from token-overflow compaction.

### Alternatives

- [[Concepts/notes-backed-context-windows]] — experimental model-managed notebook + local rollover + `history://current/full` retrieval, replacing summary recompression.

## Tools & Projects

- [[Entities/oh-my-pi]] — the parent coding-agent harness
- [[Entities/omp-snapcompact]] — the bitmap-archival package

## Raw Sources

- [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]] — verbatim extraction of `docs/compaction.md` with GitHub UI chrome stripped

## Key Threads/Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [oh-my-pi docs/compaction.md @ `6962d5c`](https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md) | Compaction architecture | 2026-09-24 | Session-entry model, 6 triggers, 5 methods, pruning, speculation, branch summary |

## Cross-Cutting Themes

### Compaction as data, not just LLM output

1. **Dual-track payloads.** Every `CompactionEntry` carries a textual `summary` (always readable by any provider) and a structured `preserveData` (`openaiRemoteCompaction`, `anthropicCompaction`, `snapcompact`) for replay on a matching provider. One entry survives provider switching without rewriting.
2. **Display vs LLM context are separate streams.** The TUI renders every path entry chronologically with inline divider glyphs; only the LLM context resets at the compaction boundary. The user's scrollback survives across resume.
3. **The journal is the single source of truth.** All summaries — provider-native, handoff, snapcompact, soft — are journal entries, not separate stores. Rebuilds reconstruct LLM input deterministically from the active leaf.

### Trigger discipline

1. **Triggers are not interchangeable.** Overflow skips handoff (the request would reuse the overflowing input); incomplete-output allows handoff (input is still usable); threshold maintenance auto-continues; idle does not.
2. **`willRetry` is the spine.** It determines whether the agent schedules its own `agent.continue()` after a successful compaction. This is what gives manual compaction its "cut and resume" behavior.
3. **Measured tokens ≠ billed tokens.** `calculateContextTokens` subtracts provider-orchestration tokens that are billable but never replayed into the prefix — thresholds are not inflated by orchestration overhead.

### Cache as a first-class resource

1. **Live-cache preservation is the goal of native compaction.** Anthropic's lane sends the **live turn's own request** (same system prompt + tools + history) so it reads the cache the previous turn wrote.
2. **Handoff uses the same trick.** Sending the active system prompt + tools + history lets the handoff document be consistent with the live model's view.
3. **Async speculation snapshots the branch.** Speculation runs on a side session off a branch snapshot, so live writes cannot race the summary or pollute its input.

### Multi-strategy `methodOrder`

1. **Default `["remote", "snapcompact", "handoff", "shake", "soft"]`.** Each method has a different cost/benefit profile: `remote` is the most cache-friendly; `snapcompact` is offline; `handoff` is cache-friendly but structured; `shake` is local elision; `soft` is the last-resort local LLM summary.
2. **Method-order fallback prevents loop pathology.** Threshold / incomplete-output / overflow recovery advance past `shake` when it cannot reclaim enough — automatic maintenance does not loop on no-ops.
3. **Eligibility gates each method.** Snapcompact requires a vision-capable model; Anthropic native compaction requires an official endpoint URL; handoff skips on overflow; soft is always available.

## Next Research Directions

- [ ] **Evaluate Anthropic's `compact-2026-01-12` beta on Opus 4.6+ / Sonnet 4.6+ / Fable / Mythos 5.** Measure cache-hit rate and end-to-end cost vs local summarization with `compaction.methodOrder = ["remote", "soft"]` and `["soft"]` only — does the cache-preserving native lane beat the local LLM path enough to justify the API version dependency?
- [ ] **Compare snapcompact's billed-token cost vs raw text retention on vision-capable Claude/GPT/Codex models.** The doc claims QA recall at lower billed-token cost; reproduce this with `snapcompact.shape = "auto"` vs `"none"` on a representative coding task.
- [ ] **Investigate `notes-backed-context-windows` for long-running sessions.** The experimental mode avoids summarization entirely — does the model actually maintain the notebook well enough to make `history://current/full` retrieval unnecessary in practice?
- [ ] **Prototype async speculative compaction on a side session.** The discard conditions (branch-prefix changes, native-replay mismatch, growth past `keepRecentTokens`) suggest the discard rate may be high on long sessions — measure.
- [ ] **Audit `useless`-flag consumers for cross-tool consistency.** Three layers consume the same flag with different rules — does the per-turn stale-result pass ever conflict with threshold prune on the same tool result?