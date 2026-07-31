---
title: Grok 4.5
details: xAI's flagship coding and agentic model released July 8, 2026, trained alongside Cursor after the Anysphere acquisition.
tags:
  - research
created: 2026-07-31
updated: 2026-07-31
type: note
---
# Grok 4.5

**Developer:** xAI (SpaceXAI)
**Released:** July 8, 2026
**Model ID:** `opencode-go/grok-4.5`

## Architecture

| Feature | Specification |
|---------|---------------|
| Architecture | Dense Transformer (V9 foundation) |
| Total Parameters | ~1.5T (vendor-reported, not independently audited) |
| Context Window | 500K tokens |
| Reasoning | Low / medium / high (default high) |
| APIs | Responses API, Chat Completions |
| Tools | Function calling, web search, X search, code execution |

## Key Features

- **Coding and agentic focus** -- xAI's first major release aimed at coding agents and long-running workflows rather than chat
- **Cursor training partnership** -- trained alongside Cursor after xAI's acquisition of Anysphere; default model in Grok Build
- **Aggressive pricing** -- $2 input / $6 output per 1M tokens, advertised as ~2x token-efficient vs comparable models
- **80 TPS throughput** -- xAI's main differentiator at the capability tier
- **Built on V9 foundation** -- Elon Musk has described V9 as a 1.5T-parameter base; treat the exact number as directional
- **Knowledge cutoff** -- February 1, 2026 (web/X search recommended for current events)
- **Prompt cache key required** -- without it, repeated context hits cold servers and bills at full input price

## Benchmarks

- SWE-Bench Pro: 64.7% resolve rate (xAI-reported) -- above Claude Opus 4.7 Max (64.3%), GLM-5.2 (62.1%), GPT-5.5 xhigh (58.6%); below Claude Opus 4.8 Max (69.2%) and Claude Fable Max (80.4%)
- 80 TPS at this capability tier is the operational differentiator vs slower frontier models

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $2.00 / 1M tokens |
| Output | $6.00 / 1M tokens |
| Cache Read | $0.30 / 1M tokens |
| Est. requests per 5h | 120 |
| Est. requests per month | 600 |

Note: Grok 4.5 has the **lowest estimated request budget in the catalog** -- ~17x fewer monthly requests than DeepSeek V4 Flash despite costing ~43x more per output token. Use sparingly, gated to high-value tasks.

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions` (OpenAI-compatible)

## Availability

- **Not available in the EU** at launch (delayed to mid-July 2026+)
- Available via xAI API, Grok Build CLI, Cursor (all plans, free for limited time), and gateways (OpenRouter, Vercel, Cloudflare, Snowflake, Databricks Mosaic)

## Best For

- High-volume background coding agents (CI fix bots, batch refactors, automated PR review)
- Cursor-integrated agentic workflows where the training-data alignment with Cursor session patterns helps
- Cost-sensitive frontier-tier work where 80 TPS throughput is the deciding factor
- Tasks where a 500K context window is enough (note: smaller than Grok 4.3's 1M window)
