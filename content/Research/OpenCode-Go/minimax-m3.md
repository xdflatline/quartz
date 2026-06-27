---
title: MiniMax M3
details: MiniMax's native multimodal model with 1M context, sparse attention, and support for text, image, and video inputs.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# MiniMax M3

**Developer:** MiniMax
**Released:** May 31, 2026
**Model ID:** `opencode-go/minimax-m3`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 456B |
| Active Parameters | 45.9B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 1M tokens |
| Attention | MiniMax Sparse Attention (MSA) -- KV-block selection |
| Modalities | Text + Image + Video input, text output |

## Key Features

- **Native multimodal** -- processes text, images, and video natively (not bolted on)
- **MiniMax Sparse Attention (MSA)** -- replaces full attention with KV-block selection, ~1/20 the cost of previous gen at 1M tokens
- **Interactive user-simulator training** -- tuned for multi-turn, production-like collaboration
- **Long-horizon agentic work** -- oriented toward sustained multi-step tasks
- **Open weights** -- available on Hugging Face (`MiniMaxAI/Minimax-M3`)
- **Reasoning support** -- enables thinking tokens via API parameter

## Performance

- Substantially faster prefill and decode than M2.7
- Retains quality across most tasks despite aggressive attention sparsification
- Throughput: up to 54 tok/s (NovitaAI), latency p50: 0.67s (Together)

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.30 / 1M tokens |
| Output | $1.20 / 1M tokens |
| Cache Read | $0.06 / 1M tokens |
| Est. requests per 5h | 3,200 |
| Est. requests per month | 16,000 |

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible)

## Best For

- Multimodal coding agents (image/video + text input)
- Long-context tasks where cost efficiency matters
- Multi-turn collaborative coding sessions
- Tasks requiring native video understanding alongside code generation
