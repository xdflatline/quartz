---
title: OpenCode Go Models
details: Catalog of all models available through the OpenCode Go subscription provider, with architecture, pricing, and capability summaries.
tags:
  - research
created: 2026-06-27
updated: 2026-07-31
type: note
---

# OpenCode Go Models

OpenCode Go is a low-cost subscription ($5 first month, then $10/month) providing access to curated open coding models. Hosted across US, EU, and Singapore. Uses `OPENCODE_API_KEY` for authentication.

**Updated 2026-07-31:** Catalog expanded from 13 to 17 active models. New additions since the original 2026-06-27 index: [[grok-4.5]] (2026-07-08), [[gpt-5.6-luna]] (2026-07-09, 80% price cut 2026-07-30), [[hy3]] (2026-07-06), [[kimi-k3]] (2026-07-16). Plus [[minimax-m2.5]] added to the endpoint table for backward compatibility.

## Provider Overview

- **Chat completions endpoint:** `https://opencode.ai/zen/go/v1/chat/completions` (GLM, Kimi, DeepSeek, MiMo, Hy3, Grok 4.5)
- **Messages endpoint:** `https://opencode.ai/zen/go/v1/messages` (MiniMax, Qwen) -- Anthropic-compatible
- **Responses endpoint:** `https://opencode.ai/zen/go/v1/responses` (GPT 5.6 Luna) -- OpenAI-native, not chat completions
- **Config format:** `opencode-go/<model-id>`

## Usage Limits (Dollar-Based)

| Window | Limit |
|--------|-------|
| 5 hours | $12 |
| Weekly | $30 |
| Monthly | $60 |

## Model Catalog

| Model | Developer | Params (Total/Active) | Context | Input $/1M | Output $/1M |
|-------|-----------|----------------------|---------|------------|-------------|
| [[grok-4.5]] | xAI | ~1.5T (dense V9) | 500K | $2.00 | $6.00 |
| [[gpt-5.6-luna]] | OpenAI | Proprietary | Standard | $0.20-$0.40 | $1.20-$1.80 |
| [[kimi-k3]] | Moonshot AI | 2.8T / ~50B | 1M | $3.00 | $15.00 |
| [[hy3]] | Tencent | 295B / 21B | 256K | $0.14 | $0.58 |
| [[glm-5.2]] | Zhipu AI | 753B / 40B | 1M | $1.40 | $4.40 |
| [[glm-5.1]] | Zhipu AI | 744B / 40B | 203K | $1.40 | $4.40 |
| [[kimi-k2.7-code]] | Moonshot AI | 1T / 32B | 262K | $0.95 | $4.00 |
| [[kimi-k2.6]] | Moonshot AI | 1T / 32B | 262K | $0.95 | $4.00 |
| [[mimo-v2.5]] | Xiaomi | 310B / 15B | 1M | $0.14 | $0.28 |
| [[mimo-v2.5-pro]] | Xiaomi | 1.02T / 42B | 1M | $1.74 | $3.48 |
| [[minimax-m3]] | MiniMax | 456B / 45.9B | 1M | $0.30 | $1.20 |
| [[minimax-m2.7]] | MiniMax | N/A | 205K | $0.30 | $1.20 |
| [[minimax-m2.5]] | MiniMax | N/A | 205K | $0.30 | $1.20 |
| [[qwen3.7-max]] | Alibaba | Proprietary | 1M | $2.50 | $7.50 |
| [[qwen3.7-plus]] | Alibaba | Proprietary | 1M | $0.40 | $1.60 |
| [[qwen3.6-plus]] | Alibaba | Proprietary | 1M | $0.50 | $3.00 |
| [[deepseek-v4-pro]] | DeepSeek | 1.6T / 49B | 1M | $1.74 | $3.48 |
| [[deepseek-v4-flash]] | DeepSeek | 284B / 13B | 1M | $0.14 | $0.28 |

Catalog sorted by release date (newest first), then by developer. Same 5h/weekly/monthly dollar limits apply to all models: $12 / $30 / $60.

## Highlights and Recommended Use Cases

| Model | Highlights | Recommended Use Case |
|-------|-----------|---------------------|
| [[grok-4.5]] | 80 TPS at frontier tier, trained alongside Cursor, 64.7% SWE-Bench Pro (vendor-reported) | High-volume coding agents where token efficiency and 80 TPS throughput are decisive; not available in EU at launch |
| [[gpt-5.6-luna]] | GPT-5.6 fast tier, 80% price cut on 2026-07-30, 90% prompt-cache reuse in tests, 2x usage multiplier on Go | High-volume production coding agents where cost-per-call dominates; default GPT-5.6 family member on Go |
| [[kimi-k3]] | First 3T-class open-weights model, 1M context, native vision, Kimi Delta Attention, BrowseComp 90.4% at full context | Frontier-quality open-weight coding; long-horizon agentic work; reserve (110 req/5h budget is the lowest in catalog) |
| [[hy3]] | Apache 2.0, 256K context, 21B active MoE, hybrid fast/slow thinking, second-cheapest in catalog | High-volume coding with permissive license requirements; drop-in for Hunyuan 2.0 users |
| [[glm-5.2]] | 1M context, dual reasoning modes (High/Max), MIT-licensed, IndexShare sparse attention | Long-horizon agentic coding, repo-scale refactoring |
| [[glm-5.1]] | Same MoE family as 5.2, 203K context, identical pricing | General coding tasks where 1M context is not needed |
| [[kimi-k2.7-code]] | 30% fewer reasoning tokens than K2.6, best instruction following in the Kimi line | Production coding agents, high-volume task throughput |
| [[kimi-k2.6]] | Natively multimodal (text + vision), first open model to beat GPT-5.4 on SWE-Bench Pro | Multimodal coding, UI/UX generation from mockups |
| [[mimo-v2.5]] | 15B active params, 1M context, cheapest output in catalog | High-throughput simple coding, rapid prototyping on a budget |
| [[mimo-v2.5-pro]] | 1.02T params, hybrid attention, 1000+ tool calls demonstrated, rivals Claude Opus 4.6 | Complex multi-hour autonomous coding, full app generation |
| [[minimax-m3]] | Native multimodal (text + image + video), sparse attention (1/20 cost at 1M) | Multimodal agents with video/image input, long-context tasks |
| [[minimax-m2.7]] | 205K context, cache write support, 128K max output | Text-only agentic workflows, tasks benefiting from cache writes |
| [[minimax-m2.5]] | Previous-gen MiniMax, identical pricing to M2.7, cache write support | Backward compatibility for code paths pinned to M2.5 |
| [[qwen3.7-max]] | Most capable Qwen in catalog, text + video + image input, proprietary | Maximum-quality tasks regardless of cost, document processing |
| [[qwen3.7-plus]] | Tiered pricing (3x cheaper under 256K), multimodal, highest Qwen throughput | Cost-efficient multimodal coding, high-volume production |
| [[qwen3.6-plus]] | Previous-gen Qwen, multimodal, tiered pricing | Legacy workflows on Qwen3.6, fallback when 3.7 is rate-limited |
| [[deepseek-v4-pro]] | 1.6T params, open-source SOTA in agentic coding, thinking/non-thinking modes | Complex reasoning, math/STEM, frontier-quality agent work |
| [[deepseek-v4-flash]] | 13B active, near-Pro reasoning on simple tasks, 158K est. requests/month | Budget production agents, simple tasks at Pro-level quality |

## Tier Summary

- **Budget / High-throughput:** MiMo-V2.5, DeepSeek V4 Flash (sub-$0.30/1M output), Hy3 ($0.58), GPT 5.6 Luna ($1.20-1.80)
- **Mid-range:** MiniMax M3 / M2.7 / M2.5, Qwen3.7 Plus, Qwen3.6 Plus, DeepSeek V4 Pro, GLM-5.1, Grok 4.5
- **Flagship:** GLM-5.2, Kimi K2.7 Code, Kimi K3, MiMo-V2.5-Pro, Qwen3.7 Max

New additions reshape the **budget tier** (Hy3 and GPT 5.6 Luna add cheap options that were not available in the original 2026-06-27 catalog) and the **flagship tier** (Kimi K3 is the new highest-context open-weight model, ahead of GLM-5.2 on context-window parity and the new open-weight SOTA on sustained-coding benchmarks). Grok 4.5 is the first non-Asian closed-model on Go, and the first with a Cursor-specific training partnership.

## Endpoint Routing Reference

| Endpoint | Models |
|----------|--------|
| `/v1/chat/completions` (OpenAI-compatible) | GLM-5.2, GLM-5.1, Kimi K2.6, Kimi K2.7 Code, Kimi K3, DeepSeek V4 Pro, DeepSeek V4 Flash, MiMo V2.5, MiMo V2.5 Pro, Hy3, Grok 4.5 |
| `/v1/messages` (Anthropic-compatible) | MiniMax M2.5, MiniMax M2.7, MiniMax M3, Qwen3.6 Plus, Qwen3.7 Plus, Qwen3.7 Max |
| `/v1/responses` (OpenAI-native) | GPT 5.6 Luna |

Note: the responses endpoint is **not** an OpenAI-compatible drop-in. Code that uses the OpenAI chat completions SDK against GPT 5.6 Luna must be configured to use the OpenAI Responses API or the `@ai-sdk/openai` package.
