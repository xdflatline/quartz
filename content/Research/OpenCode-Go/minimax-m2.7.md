---
title: MiniMax M2.7
details: MiniMax's previous-generation model with 205K context, agentic capabilities, and function calling support.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# MiniMax M2.7

**Developer:** MiniMax
**Model ID:** `opencode-go/minimax-m2.7`

## Architecture

| Feature | Specification |
|---------|---------------|
| Context Window | 205K tokens |
| Max Output | 128K tokens (including CoT) |
| Modalities | Text input, text output |

## Key Features

- **Agentic capabilities** -- function calling and tool use
- **Advanced reasoning** -- chain-of-thought support
- **Real-time streaming** support
- **Cost-effective** -- same pricing as M3 despite being previous generation
- **Cache write support** -- $0.375/1M for cache writes (unique among Go models)

## Differences from MiniMax M3

- Smaller context window (205K vs 1M)
- No native multimodal support (text only, no image/video)
- No MiniMax Sparse Attention (MSA) optimization
- Slower throughput than M3
- Supports cache writes (M3 does not list this)

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.30 / 1M tokens |
| Output | $1.20 / 1M tokens |
| Cache Read | $0.06 / 1M tokens |
| Cache Write | $0.375 / 1M tokens |
| Est. requests per 5h | 3,400 |
| Est. requests per month | 17,000 |

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible)

## Best For

- Text-only agentic coding tasks
- Workflows that benefit from cache write support
- Mid-range context needs (under 200K tokens)
- Cost-conscious users who do not need multimodal input
