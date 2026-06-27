---
title: Qwen3.7 Plus
details: Alibaba's mid-tier Qwen3.7 model offering strong capability at low cost, with multimodal input support.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# Qwen3.7 Plus

**Developer:** Alibaba (Qwen team)
**Model ID:** `opencode-go/qwen3.7-plus`

## Architecture

| Feature | Specification |
|---------|---------------|
| Architecture | Proprietary |
| Context Window | 1M tokens |
| Modalities | Text, video, and imagery inputs |

## Key Features

- **Multimodal input** -- supports text, video, and image inputs
- **1M context window** with tiered pricing (cheaper under 256K)
- **Strong price-performance** -- $0.40/$1.60 per 1M at sub-256K context
- **High throughput** -- 4,300 estimated requests per 5h (best among Qwen models)
- **Proprietary model** -- not open-weight

## Tiered Pricing

Pricing depends on context length used:

| Context Range | Input | Output | Cache Read | Cache Write |
|---------------|-------|--------|------------|-------------|
| <= 256K | $0.40 | $1.60 | $0.04 | $0.50 |
| > 256K | $1.20 | $4.80 | $0.12 | $1.50 |

## Pricing (OpenCode Go, <= 256K)

| Metric | Value |
|--------|-------|
| Input | $0.40 / 1M tokens |
| Output | $1.60 / 1M tokens |
| Cache Read | $0.04 / 1M tokens |
| Cache Write | $0.50 / 1M tokens |
| Est. requests per 5h | 4,300 |
| Est. requests per month | 21,600 |

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible)

## Best For

- Multimodal coding agents at low cost
- High-throughput workflows where context stays under 256K
- General-purpose agentic tasks with image/video input
- Cost-sensitive production workloads
