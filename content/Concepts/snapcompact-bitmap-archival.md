---
title: "Snapcompact Bitmap Archival"
details: "Local, deterministic compaction strategy that archives discarded history as dense PNG frames using bundled public-domain pixel fonts, shape-selected per model family and pixel size to fit each provider's vision-token billing model. Stores both the bounded source text and the rendered frames under CompactionEntry.preserveData.snapcompact; rebuilds the archive as plain-text edges + imaged middle on each context rebuild."
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

# Snapcompact Bitmap Archival

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Experimental-to-production (200k-token evals in `packages/snapcompact`)

## Overview

Snapcompact is oh-my-pi's offline archival compaction strategy. Instead of calling a summarization model, it serializes the discarded history, whitespace-collapses it, and renders it onto model-aware PNG frames using bundled public-domain pixel fonts. The frame shape (font, pitch, width) is keyed off the active model id because vision-token billing differs across providers — Anthropic caps visual tokens at 4,784 for high-res lines, Gemini bills a flat 1,120-token budget per image regardless of pixel size, OpenAI's patch billing is area-proportional. The archive lives under `CompactionEntry.preserveData.snapcompact` and is rebuilt as plain-text edges + imaged middle on each context rebuild.

## Core Content

### Pipeline

1. **Serialize** the discarded history with `serializeConversation()` (snapcompact variant).
2. **Whitespace-collapse** the serialized text.
3. **Render** onto model-aware PNG frames using bundled public-domain pixel fonts.
4. **Persist** as bounded source text (`Archive.text`) plus rendered frames under `preserveData.snapcompact`.
5. **Rebuild** on context rebuild as `[plain text at oldest edge] [imaged middle] [plain text at newest edge]`.

### Frame-shape table (per model family)

| Family | Glyph | Pitch | Frame width | Billing |
|--------|-------|-------|-------------|---------|
| Anthropic-native Claude | X.org `8x13` | 11px (black ink) | 1568px (older); 1932px (Opus 4.7+, Fable, Mythos) | 4,784 visual-token cap on high-res lines |
| Google Gemini | `8x13` | 22px | 2048px (`8on22-bw`) | Flat 1,120-token budget per image at any pixel size |
| GPT / Codex | `8x13` | 22px | 1568px | Area-proportional patch billing |
| Kimi / GLM | `8x13` | 16px | 1568px (`8on16-bw`) | Kimi processor downscales past 1792px |

A Claude routed through Vertex or OpenRouter keeps its Claude shape. Unmeasured models fall back to their wire API family (Anthropic-family/unknown → `11on16-bw`, Google → `8on22-bw`, OpenAI-compatible → `8on22-bw`). Billing always follows the API carrying the request.

### Auto shape selection (`resolveShapeForText`)

When `snapcompact.shape = "auto"` (default), the resolver is font-aware: if the model-default font cannot safely render the transcript, or wide CJK glyphs dominate and `silver16-bw` (the embedded Silver TrueType font on a 16px grid) can render them safely, auto switches to `silver16-bw`. Forced variants are never overridden.

### Forced research-eval variants

`snapcompact.shape` may also force one of:
- Square grids: `8x8r`, `8x8u`, `6x6u`, `5x8` (with sentence-hue/black ink)
- Per-model eval winners: `6x12-dim`, `8x13-bw`, `8on16-bw`, `8on22-bw`, `11on16-bw`, `silver16-bw`

### Serialization knobs (`SerializeOptions`)

| Knob | Default | Purpose |
|------|---------|---------|
| `toolResultMaxChars` | 2,000 | Head+tail truncation of each tool result |
| `truncateHeadRatio` | 0.6 | Head-vs-tail share of the truncation |
| `toolArgMaxChars` | 500 | Per tool-call argument value cap |
| `toolCallMaxChars` | 2,000 | Per tool call cap |
| `dimToolResults` | true | Render tool output in dim gray ink (conversation reads louder) |

### Foveated middle

`maxFrames` defaults to `MAX_FRAMES_DEFAULT` (80) and acts only as an upper limit. When the imaged middle is large, it foveates internally (HQ/LQ/HQ pattern) — both chronological edges stay verbatim text regardless. Later compactions re-render from `Archive.text`, not by carrying old PNGs forward blindly.

### Eligibility

Automatic maintenance skips snapcompact and advances to the next configured method if the current model is not vision-capable (`model.input` does not include `"image"`). Manual `/compact` honors the method order unless custom instructions are given (which imply a directed LLM summary).

### Why bitmap works

The shape table comes from snapcompact 200k-token evals: bitmap frames preserved QA recall at lower billed-token cost than raw text for vision-capable models. No model, API key, or network is involved — so snapcompact is also safe for overflow recovery.

## Key Insights

1. **The shape is a billing calculation, not a font choice.** Each family's frame width is set to fit its visual-token cap *and* its billing model. Wider frames don't help Gemini (flat budget) or GPT (area-proportional but already optimal).
2. **Source text is preserved alongside frames.** The archive stores `Archive.text` (bounded source) and rendered frames separately. Rebuild always goes through source text — old PNGs are never carried forward, they are re-rendered. This is what makes the archive migration-safe across compaction rounds.
3. **Two display layers per rebuild.** The same `preserveData.snapcompact` produces a different effective LLM input depending on whether the model can see images; the rendered frames collapse to nothing for non-vision models and the source text takes over (and the entry's `summary` is just the short resume lead-in plus file-ops list).
4. **CJK-aware auto selection.** The `silver16-bw` font is what makes the strategy work for Chinese / Japanese / Korean transcripts — the default `8x13` glyph can't render those widths.

## Related Concepts

- [[Concepts/pre-compaction-tool-result-pruning]] — runs before snapcompact, smaller-scope
- [[Concepts/provider-native-compaction]] — alternative remote archival
- [[Concepts/session-entry-compaction-model]] — what wraps snapcompact output
- [[Entities/omp-snapcompact]] — the implementation

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#snapcompact-method