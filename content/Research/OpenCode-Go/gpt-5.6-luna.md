---
title: GPT 5.6 Luna
details: OpenAI's fast, cost-efficient GPT-5.6 tier, added to the Go catalog on July 9, 2026, with 80% price reduction on July 30, 2026.
tags:
  - research
created: 2026-07-31
updated: 2026-07-31
type: note
---
# GPT 5.6 Luna

**Developer:** OpenAI
**Released:** July 9, 2026 (Go catalog)
**Model ID:** `opencode-go/gpt-5.6-luna`

## Architecture

| Feature | Specification |
|---------|---------------|
| Family | GPT-5.6 series (Sol / Terra / Luna) |
| Tier | Fast, cost-efficient |
| Context Window | Standard GPT-5.6 window |
| APIs | Responses API (OpenAI-native) |

## Key Features

- **Fastest and most affordable tier** in the GPT-5.6 family
- **80% price reduction** applied on July 30, 2026 (per OpenAI announcement) -- now sub-budget tier on Go
- **Production agentic coding** -- OpenAI positions Luna as the recommended model for high-volume coding agent loops
- **High prompt-cache reuse** -- Luna deployments move prompt-cache reuse from 24% to 90% in OpenAI's own tests
- **40% faster and 40% cheaper** than OpenAI's previous default model for the same agentic tasks
- **2x usage multiplier** on Go (per the changelog) -- effectively doubles the request budget compared to other tiers

## Pricing (OpenCode Go)

Two-tier pricing by context length (per OpenAI announcement, post-July-30 update):

| Metric | ≤ 272K tokens | > 272K tokens |
|--------|---------------|---------------|
| Input | $0.20 / 1M | $0.40 / 1M |
| Output | $1.20 / 1M | $1.80 / 1M |
| Cache Read | $0.02 / 1M | $0.04 / 1M |
| Cache Write | $0.25 / 1M | $0.50 / 1M |
| Est. requests per 5h | 2,050 | -- |
| Est. requests per month | 10,250 | -- |

The 2x usage multiplier brings the effective request budget higher than the raw price would suggest. Among OpenAI's Go models this is the workhorse.

## Endpoint

Responses API: `https://opencode.ai/zen/go/v1/responses` (OpenAI-native, not chat completions)

## Best For

- High-volume agentic coding loops where cost-per-call dominates the budget
- Tasks that benefit from extreme prompt-cache reuse (long system prompts, large tool definitions)
- Fast iteration on agent workflows where the previous default model was the bottleneck
- Default GPT-5.6 family member for Go; use Sol or external Claude Fable for hard frontier tasks
