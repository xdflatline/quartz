---
title: Qwen3.7 Max
details: Alibaba's flagship Qwen3.7 model, the most capable and most expensive in the Go catalog.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# Qwen3.7 Max

**Developer:** Alibaba (Qwen team)
**Model ID:** `opencode-go/qwen3.7-max`

## Architecture

| Feature | Specification |
|---------|---------------|
| Architecture | Proprietary (likely sparse MoE) |
| Context Window | 1M tokens |
| Modalities | Text, video, and imagery inputs |

## Key Features

- **Flagship of the Qwen3.7 series** -- highest capability tier
- **Versatile agent foundation** -- equally capable at coding, office automation, and sustained agentic work
- **Multimodal input** -- supports text, video, and image inputs
- **1M context** -- handles large codebases and long sessions
- **Proprietary model** -- not open-weight (unlike most other Go models)

## Positioning

Qwen3.7 Max is the premium tier in the Go catalog. It has the highest input/output pricing ($2.50/$7.50 per 1M tokens) and is positioned for tasks requiring maximum capability. The Qwen3.7 series blog describes it as "built to be a versatile agent foundation."

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $2.50 / 1M tokens |
| Output | $7.50 / 1M tokens |
| Cache Read | $0.50 / 1M tokens |
| Cache Write | $3.125 / 1M tokens |
| Est. requests per 5h | 950 |
| Est. requests per month | 4,770 |

## Endpoint

Messages: `https://opencode.ai/zen/go/v1/messages` (Anthropic-compatible)

## Best For

- Tasks requiring maximum model capability regardless of cost
- Complex multimodal reasoning (text + image + video)
- High-stakes coding where quality trumps throughput
- Office automation and document processing workflows
