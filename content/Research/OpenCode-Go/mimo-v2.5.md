---
title: MiMo-V2.5
details: Xiaomi's budget-tier MoE model with 1M context, extremely low cost, and strong coding capabilities for its size.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# MiMo-V2.5

**Developer:** Xiaomi
**Model ID:** `opencode-go/mimo-v2.5`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 310B |
| Active Parameters | 15B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Hidden Size | 4096 |
| Num Layers | 48 (1 dense + 47 MoE) |
| Context Window | 1M tokens |

## Key Features

- **Ultra-low cost** -- cheapest output pricing in the Go catalog alongside DeepSeek V4 Flash
- **1M context window** -- same context as the Pro tier at a fraction of the cost
- **MoE efficiency** -- only 15B active params keeps inference fast and cheap
- **Smaller sibling of MiMo-V2.5-Pro** -- shares architectural DNA at reduced scale
- **Open-weight** -- available on Hugging Face

## Trade-offs vs MiMo-V2.5-Pro

- Fewer total parameters (310B vs 1.02T)
- Fewer active parameters (15B vs 42B)
- Lower benchmark scores on complex agentic tasks
- No hybrid attention or MTP optimizations
- Suitable for simpler coding tasks, not long-horizon agent work

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.14 / 1M tokens |
| Output | $0.28 / 1M tokens |
| Cache Read | $0.0028 / 1M tokens |
| Est. requests per 5h | 30,100 |
| Est. requests per month | 150,400 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- High-throughput coding tasks where cost is the primary constraint
- Simple code generation, completion, and refactoring
- Rapid prototyping and iteration
- Tasks that need 1M context but not frontier-level reasoning
