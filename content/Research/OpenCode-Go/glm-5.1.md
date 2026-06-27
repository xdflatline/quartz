---
title: GLM-5.1
details: Zhipu AI's predecessor to GLM-5.2, a 744B MoE model with strong coding and agentic capabilities.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# GLM-5.1

**Developer:** Zhipu AI (Z.ai)
**License:** MIT (open-weights)
**Model ID:** `opencode-go/glm-5.1`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | ~744B |
| Active Parameters | ~40B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 203K tokens |
| Pre-training Data | 23T+ tokens |

## Key Features

- **Coding-oriented** -- designed for software engineering and agentic workloads
- **Open weights** -- MIT licensed, available on Hugging Face
- **Scaled from GLM-4.5** -- 355B to 744B total params, 32B to 40B active
- **Function calling** support for tool-use agent loops
- **Predecessor to GLM-5.2** -- smaller context window (203K vs 1M), no IndexShare attention

## Differences from GLM-5.2

- Context window: 203K vs 1M tokens
- No IndexShare sparse attention scheme
- No dual reasoning modes (High/Max)
- Lower long-context benchmark performance

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $1.40 / 1M tokens |
| Output | $4.40 / 1M tokens |
| Cache Read | $0.26 / 1M tokens |
| Est. requests per 5h | 880 |
| Est. requests per month | 4,300 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- General coding tasks where 1M context is not required
- Cost-effective alternative to GLM-5.2 at identical pricing
- Shorter-context agentic workflows
