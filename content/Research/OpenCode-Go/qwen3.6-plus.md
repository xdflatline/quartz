---
title: Qwen3.6 Plus
details: Alibaba's previous-generation Qwen model with 1M context, multimodal input, and tiered pricing.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# Qwen3.6 Plus

**Developer:** Alibaba (Qwen team)
**Model ID:** `opencode-go/qwen3.6-plus`

## Architecture

| Feature | Specification |
|---------|---------------|
| Architecture | Proprietary |
| Context Window | 1M tokens |
| Modalities | Text + image input (multimodal) |

## Key Features

- **Multimodal input** -- supports text and image inputs
- **1M context window** with tiered pricing
- **Previous generation** -- superseded by Qwen3.7 Plus but still available
- **Proprietary model** -- not open-weight

## Tiered Pricing

| Context Range | Input | Output | Cache Read | Cache Write |
|---------------|-------|--------|------------|-------------|
| <= 256K | $0.50 | $3.00 | $0.05 | $0.625 |
| > 256K | $2.00 | $6.00 | $0.20 | $2.50 |

## Pricing (OpenCode Go, <= 256K)

| Metric | Value |
|--------|-------|
| Input | $0.50 / 1M tokens |
| Output | $3.00 / 1M tokens |
| Cache Read | $0.05 / 1M tokens |
| Cache Write | $0.625 / 1M tokens |
| Est. requests per 5h | 3,300 |
| Est. requests per month | 16,300 |

## Differences from Qwen3.7 Plus

- Higher output pricing ($3.00 vs $1.60 per 1M at <= 256K)
- Previous generation architecture
- Likely lower benchmark performance
- Same context window and multimodal support

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible)

## Best For

- Workflows already built on Qwen3.6 that do not need upgrading
- Tasks where Qwen3.7 Plus is unavailable or rate-limited
- Mid-range multimodal coding tasks
