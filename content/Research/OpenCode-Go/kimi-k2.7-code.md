---
title: Kimi K2.7 Code
details: Moonshot AI's most capable coding model, optimized for instruction following in long contexts and higher task success rates.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# Kimi K2.7 Code

**Developer:** Moonshot AI
**Model ID:** `opencode-go/kimi-k2.7-code`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 1T |
| Active Parameters | 32B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Number of Experts | 384 total, 8 activated per token |
| Context Window | 262K tokens (256K) |
| Attention | Multi-head Latent Attention (MLA) |

## Key Features

- **Coding-specialized** -- fine-tuned specifically for coding tasks over the K2.6 base
- **30% reduction in reasoning token usage** compared to K2.6
- **Better instruction following** in long contexts
- **Higher coding task success rates** than K2.6
- **Open-weight** -- same 1T MoE family as K2.6

## Relationship to K2.6

K2.7 Code shares the same architecture as K2.6 (1T params, 32B active, 384 experts). The gains come from the training recipe -- specialized coding post-training that improves instruction adherence and reduces reasoning overhead.

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.95 / 1M tokens |
| Output | $4.00 / 1M tokens |
| Cache Read | $0.19 / 1M tokens |
| Est. requests per 5h | 1,350 |
| Est. requests per month | 9,250 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- Production coding agent workloads
- Tasks requiring precise instruction following in large contexts
- Multi-agent orchestration with coding focus
- Cost-efficient high-volume coding (best request throughput among Kimi models)
