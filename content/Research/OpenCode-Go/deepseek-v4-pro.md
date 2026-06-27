---
title: DeepSeek V4 Pro
details: DeepSeek's flagship 1.6T-parameter MoE model with 1M context, open-source SOTA in agentic coding.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# DeepSeek V4 Pro

**Developer:** DeepSeek
**Released:** April 24, 2026
**License:** Open-weight
**Model ID:** `opencode-go/deepseek-v4-pro`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 1.6T |
| Active Parameters | 49B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 1M tokens |
| Attention | Token-wise compression + DeepSeek Sparse Attention (DSA) |
| Modes | Thinking / Non-Thinking (dual mode) |

## Key Features

- **1.6T total parameters** -- largest model in the Go catalog
- **Open-source SOTA in agentic coding** benchmarks
- **Rich world knowledge** -- leads all current open models, trails only Gemini 3.1 Pro
- **World-class reasoning** -- beats all open models in Math/STEM/Coding
- **1M context as default** -- standard across all official DeepSeek services
- **Dual modes** -- Thinking (reasoning) and Non-Thinking (fast) modes
- **Seamless agent integration** -- works with Claude Code, OpenClaw, OpenCode
- **API compatibility** -- supports both OpenAI ChatCompletions and Anthropic APIs

## Benchmarks

- Open-source SOTA in agentic coding benchmarks
- Leads all open models in world knowledge
- Rivals top closed-source models in reasoning (Math/STEM/Coding)

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $1.74 / 1M tokens |
| Output | $3.48 / 1M tokens |
| Cache Read | $0.0145 / 1M tokens |
| Est. requests per 5h | 3,450 |
| Est. requests per month | 17,150 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- Complex reasoning tasks requiring maximum open-model capability
- Agentic coding at frontier quality
- Math, STEM, and science problem-solving
- Tasks needing rich world knowledge alongside coding ability
- Long-horizon agent workflows with thinking mode enabled
