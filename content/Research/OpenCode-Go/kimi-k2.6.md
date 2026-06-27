---
title: Kimi K2.6
details: Moonshot AI's natively multimodal open-weight model with strong coding, agent performance, and UI/UX generation capabilities.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# Kimi K2.6

**Developer:** Moonshot AI
**Model ID:** `opencode-go/kimi-k2.6`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 1T |
| Active Parameters | 32B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Number of Experts | 384 total, 8 activated per token |
| Context Window | 262K tokens (256K) |
| Attention | Multi-head Latent Attention (MLA) |
| Modalities | Text + Vision (natively multimodal) |

## Key Features

- **Natively multimodal** -- processes text and image inputs
- **First open-weight model to beat GPT-5.4 on SWE-Bench Pro**
- **Long-horizon coding** -- designed for sustained multi-step coding tasks
- **Coding-driven UI/UX generation** -- can generate interfaces from descriptions
- **Multi-agent orchestration** -- supports complex agent coordination patterns
- **Open-weight** -- identical architecture to K2.5, gains from training recipe

## Benchmarks

- SWE-Bench Pro: beats GPT-5.4 (first open-weight model to do so)
- Strong performance across coding agent benchmarks
- Competitive with Claude Opus on agentic tasks

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.95 / 1M tokens |
| Output | $4.00 / 1M tokens |
| Cache Read | $0.16 / 1M tokens |
| Est. requests per 5h | 1,150 |
| Est. requests per month | 5,750 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- Multimodal coding agents (image + text input)
- UI/UX generation from descriptions or mockups
- General-purpose agentic coding with vision capabilities
- Multi-agent orchestration workflows
