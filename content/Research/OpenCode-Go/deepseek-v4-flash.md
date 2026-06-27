---
title: DeepSeek V4 Flash
details: DeepSeek's efficient 284B MoE model with 1M context, near-Pro reasoning at a fraction of the cost.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# DeepSeek V4 Flash

**Developer:** DeepSeek
**Released:** April 24, 2026
**License:** Open-weight
**Model ID:** `opencode-go/deepseek-v4-flash`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 284B |
| Active Parameters | 13B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 1M tokens |
| Attention | Token-wise compression + DeepSeek Sparse Attention (DSA) |
| Modes | Thinking / Non-Thinking (dual mode) |

## Key Features

- **Ultra-efficient** -- only 13B active params out of 284B total
- **Near-Pro reasoning** -- reasoning capabilities closely approach V4-Pro
- **On par with Pro on simple agent tasks** -- same quality for routine work
- **Fast response times** -- smaller parameter count means faster inference
- **1M context** -- same context window as the Pro model
- **Dual modes** -- Thinking and Non-Thinking modes supported
- **Open-weight** -- available on Hugging Face

## Trade-offs vs V4-Pro

- Fewer total parameters (284B vs 1.6T)
- Fewer active parameters (13B vs 49B)
- Reasoning "closely approaches" but does not match Pro on hard tasks
- May struggle with the most complex multi-step reasoning
- Excellent for straightforward agent tasks where Pro's extra capacity is unnecessary

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.14 / 1M tokens |
| Output | $0.28 / 1M tokens |
| Cache Read | $0.0028 / 1M tokens |
| Est. requests per 5h | 31,650 |
| Est. requests per month | 158,150 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- High-throughput coding agents where cost is critical
- Simple to moderate agent tasks that do not need Pro-level reasoning
- Rapid iteration and prototyping
- Budget-conscious production workloads with 1M context needs
- Replacement for the retired `deepseek-chat` and `deepseek-reasoner` models
