---
title: "oh-my-pi"
details: "Coding-agent harness (can1357/oh-my-pi) — a Claude-Code-style agent loop with first-class compaction, branch summarization on /tree, native provider compaction integration (OpenAI Responses compact, Anthropic server-side beta), speculative async compaction, and a snapcompact strategy that archives history as vision-encoded PNG frames."
tags:
  - entity
  - coding-agent
  - harness
created: 2026-09-27
updated: 2026-09-27
type: entity
repository: https://github.com/can1357/oh-my-pi
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# oh-my-pi

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Project (coding-agent harness)
**Repository:** https://github.com/can1357/oh-my-pi

## Overview

oh-my-pi (also written "omp") is a coding-agent harness developed by `can1357`. It implements an agent loop with first-class session-entry types for compaction (`CompactionEntry`) and branch summarization (`BranchSummaryEntry`), an extensible compaction pipeline with six trigger types, and a novel local `snapcompact` archival strategy that renders serialized history as dense PNG frames for vision-capable models. The repo is heavily forked/starred (3.6k forks / 33.5k stars at fetch), placing it in the same tier as Claude Code and Codex CLI as a reference implementation of long-session maintenance.

## Key Details

- **Packages** (from the compaction doc's implementation file list):
  - `packages/agent/src/compaction/...` — compaction, branch summarization, pruning, shake, openai, v2 streaming, utils
  - `packages/snapcompact/...` — bitmap-image archival strategy
  - `packages/coding-agent/src/session/...` — agent session, session manager, session maintenance, messages
  - `packages/coding-agent/src/extensibility/hooks/types.ts` — extension hook surface
  - `packages/coding-agent/src/session/context-settings.ts` — settings registry
- **Compaction method order** (default): `["remote", "snapcompact", "handoff", "shake", "soft"]`
- **Native provider integration:**
  - OpenAI Responses compact (V1 `/responses/compact`, V2 streaming with retained-message budget default 64000)
  - Anthropic server-side compaction (`compact-2026-01-12` beta; Opus 4.6+, Sonnet 4.6+, Fable/Mythos 5)
  - Custom OpenAI-compatible `/chat/completions` endpoint (works with llama.cpp, vLLM)
- **Async speculative compaction** is default-on (`compaction.asyncEnabled = true`), pre-computing summaries on a side session while the live turn is still under threshold.
- **Experimental mode** (`compaction.experimentalContextManagement`) replaces summary recompression with persistent notes (`context_notes`), local rollover (`new_context`), and `history://current/full` retrieval — an alternative to summarization that keeps the original journal as ground truth.
- **Tree navigation** integrates branch summarization: abandoned branches get a `BranchSummaryEntry` attached at the navigation target, computed with a separate reserve budget (`branchSummary.reserveTokens = 16384`).

## Compaction strategy comparison

| Method | Network? | Vision required? | Use case |
|--------|---------|------------------|----------|
| `remote` (V1/V2/Anthropic) | Yes | No | Default; provider-native replacement history |
| `snapcompact` | No | Yes (model.input includes "image") | Offline; deterministic; large tool outputs |
| `handoff` | Yes | No | Live-cache side-request; preserves prompt cache |
| `shake` | No | No | Local elision of large tool results / fenced blocks |
| `soft` | Yes | No | Last-resort LLM summarization |

## Snapcompact frame-shape table

The bitmap shape resolves from the active model id (per the snapcompact 200k-token evals):

| Model family | Glyph | Pitch | Frame width | Notes |
|--------------|-------|-------|-------------|-------|
| Claude (Anthropic-native) | X.org `8x13` | 11px (black ink) | 1568px / 1932px (Opus 4.7+) | Routed through Vertex/OpenRouter keeps Claude shape |
| Gemini | `8x13` | 22px | 2048px | Bills 1,120-token budget per image at any size |
| GPT / Codex | `8x13` | 22px | 1568px | Patch billing area-proportional |
| Kimi / GLM | `8x13` | 16px | 1568px | Kimi processor downscales past 1792px |

Auto selection (`resolveShapeForText`) is also font-aware and falls back to `silver16-bw` for CJK-dominant transcripts.

## Related Concepts

- [[Concepts/session-entry-compaction-model]] — first-class `CompactionEntry` and `BranchSummaryEntry` types
- [[Concepts/compaction-trigger-taxonomy]] — six trigger paths with distinct semantics
- [[Concepts/provider-native-compaction]] — OpenAI V1/V2 + Anthropic beta integration
- [[Concepts/snapcompact-bitmap-archival]] — the snapcompact strategy in detail
- [[Concepts/async-speculative-compaction]] — pre-threshold background summarization
- [[Concepts/branch-summary-tree-navigation]] — branch summarization on `/tree`
- [[Concepts/notes-backed-context-windows]] — the experimental alternative to summary compaction
- [[Concepts/pre-compaction-tool-result-pruning]] — `pruneToolOutputs` + useless-result elision
- [[Concepts/shake-compaction-method]] — mechanical content elision
- [[Concepts/handoff-document-generation]] — live-cache-preserving handoff document
- [[Entities/omp-snapcompact]] — the bitmap archival package
- [[Concepts/agentic-harness-architecture]] — neighboring concept (Claude-Code-style loop)

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md