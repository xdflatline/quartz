---
title: MiniMax M2.5
details: MiniMax's previous-generation Anthropic-compatible model on the Go catalog. Predates M2.7; retained for backward compatibility and stable cache writes.
tags:
  - research
created: 2026-07-31
updated: 2026-07-31
type: note
---
# MiniMax M2.5

**Developer:** MiniMax
**Model ID:** `opencode-go/minimax-m2.5`

## Architecture

| Feature | Specification |
|---------|---------------|
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 205K tokens (same as M2.7) |
| Modalities | Text (M2.5 predates M3's native multimodal upgrade) |

## Key Features

- **Previous-generation MiniMax** -- predates M2.7 in the catalog
- **Anthropic-compatible endpoint** -- uses the `/messages` API, not chat completions
- **Cache write support** -- same $0.375 / 1M token cache-write rate as M2.7
- **Retention reason** -- backward compatibility and stable cache writes for long-running sessions that pre-date the M2.7 cutover
- **No benchmark data** -- MiniMax did not publish M2.5 specs; the doc only exposes pricing and endpoint

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.30 / 1M tokens |
| Output | $1.20 / 1M tokens |
| Cache Read | $0.06 / 1M tokens |
| Cache Write | $0.375 / 1M tokens |

Pricing is identical to M2.7 and M3 (input, output, cache read); the cache-write price is also identical to M2.7.

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible, `@ai-sdk/anthropic`)

## Best For

- Long-running sessions that established cache writes before the M2.7 cutover
- Backward compatibility for code paths pinned to M2.5
- Use cases where M2.5 and M2.7 are interchangeable (consider migrating to M3 for the multimodal upgrade)
