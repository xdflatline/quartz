---
title: "omp-snapcompact"
details: "@oh-my-pi/snapcompact package — local, deterministic compaction strategy that archives discarded conversation history as dense PNG frames using bundled public-domain pixel fonts, shape-selected per model family. No network call; vision-capable model required."
tags:
  - entity
  - tooling
created: 2026-09-27
updated: 2026-09-27
type: entity
repository: https://github.com/can1357/oh-my-pi/tree/main/packages/snapcompact
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# omp-snapcompact

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Tool (npm package, part of [[Entities/oh-my-pi]])
**Repository:** https://github.com/can1357/oh-my-pi/tree/main/packages/snapcompact

## Overview

`@oh-my-pi/snapcompact` is the bitmap-archival compaction strategy used by oh-my-pi. When the compaction pipeline reaches `snapcompact` in its `methodOrder`, it replaces the LLM summarization call with a fully local pass: serialize the discarded history, whitespace-collapse it, render it onto model-aware PNG frames using bundled public-domain pixel fonts, and store both the bounded source text and the rendered frames inside `CompactionEntry.preserveData.snapcompact`. No API key, network call, or summarization model is involved.

## Key Details

### Frame-shape resolution

The shape (font, pitch, frame width) is keyed off the **active model id** because vision-token billing varies by provider:

| Family | Glyph | Pitch | Frame width | Trigger condition |
|--------|-------|-------|-------------|-------------------|
| Anthropic-native Claude | X.org `8x13` | 11px black | 1568px (older); 1932px (Opus 4.7+, Fable, Mythos) | Hits Anthropic's 4,784 visual-token cap on high-res lines |
| Google Gemini | `8x13` | 22px | 2048px | Gemini 3.x bills a flat 1,120-token budget per image regardless of pixel size |
| OpenAI / Codex | `8x13` | 22px | 1568px | Patch billing is area-proportional; larger frames cannot improve chars/token |
| Kimi / GLM | `8x13` | 16px | 1568px | Kimi's processor downscales past 1792px |

A Claude routed through Vertex or OpenRouter keeps its Claude shape. Unmeasured models fall back to their wire API family. Billing formulas always follow the API carrying the request, computed for the resolved frame size.

### Auto shape selection (`resolveShapeForText`)

When `snapcompact.shape = "auto"` (default), the resolver is also font-aware: if the model-default font cannot safely render the transcript, or wide CJK glyphs dominate and `silver16-bw` can render them safely, auto switches to `silver16-bw`. Forced variants are never overridden.

### Archive structure

The snapcompact archive is persisted as bounded source text plus rendered frames under `CompactionEntry.preserveData.snapcompact`. On each context rebuild it is reconstructed into ordered compaction blocks:

```
[plain text at oldest edge] [imaged middle] [plain text at newest edge]
```

The entry's `summary` is just the short resume lead-in plus the usual file-operation list. Later compactions re-render from `Archive.text`, not by carrying old PNGs forward blindly. `maxFrames` defaults to `MAX_FRAMES_DEFAULT` (80) and acts only as an upper limit; when the imaged middle is large it foveates internally (HQ/LQ/HQ), while both chronological edges stay verbatim text.

### Serialization knobs (`SerializeOptions`)

- `toolResultMaxChars` — head+tail truncation, default 2,000 chars
- `truncateHeadRatio` — head-vs-tail share of truncation, default 0.6
- `toolArgMaxChars` — per tool-call argument value cap, default 500
- `toolCallMaxChars` — per tool call cap, default 2,000
- `dimToolResults` — render tool output in dim gray ink so conversation reads louder; configurable

### Settings

- `snapcompact.systemPrompt` — default `"none"`; `"agents-md"` and `"all"` opt into transient system-prompt imaging
- `snapcompact.toolResults` — default `false` (transient imaging of large historical tool results)
- `snapcompact.shape` — default `"auto"`; forces one of the research-eval variants: square grids (`8x8r` / `8x8u` / `6x6u` / `5x8` × sentence-hue/black ink) or the per-model eval winners (`6x12-dim`, `8x13-bw`, `8on16-bw`, `8on22-bw`, `11on16-bw`, `silver16-bw`)

### Eligibility constraint

Automatic maintenance skips snapcompact and advances to the next configured method if the current model is not vision-capable (`model.input` does not include `"image"`). Manual `/compact` honors the method order unless custom instructions are given (which imply a directed LLM summary).

### Rationale

The shape table comes from snapcompact 200k-token evals in `packages/snapcompact`, where bitmap frames preserved QA recall at lower billed-token cost than raw text for vision-capable models. It is also safe for overflow recovery because no network call is involved.

## Related Concepts

- [[Concepts/snapcompact-bitmap-archival]] — the snapcompact concept page
- [[Concepts/provider-native-compaction]] — the alternative provider-side archival that snapcompact is positioned against
- [[Entities/oh-my-pi]] — parent project

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#snapcompact-method