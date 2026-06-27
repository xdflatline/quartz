---
title: GLM-5.2
details: Zhipu AI's flagship open-weight coding model with 1M context, MoE architecture, and dual reasoning modes.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# GLM-5.2

**Developer:** Zhipu AI (Z.ai)
**Released:** June 13, 2026
**License:** MIT (open-weights)
**Model ID:** `opencode-go/glm-5.2`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | ~753B |
| Active Parameters | ~40B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 1M tokens |
| Max Output | 131,072 tokens |
| Attention | IndexShare (sparse-attention, reuses indexer across sparse layers) |
| Decoding | Multi-token prediction (MTP) layers, ~20% acceptance rate boost |

## Key Features

- **Coding-first design** -- built for agentic coding, multi-step reasoning, and tool use rather than generic chat
- **Dual reasoning modes:** High (default, fast) and Max (complex bugs, architecture changes, higher latency)
- **Repo-scale context** -- 1M tokens handles entire monorepos without truncation
- **Function calling** -- first-class support for multi-turn tool-use loops
- **Long-horizon agents** -- maintains working memory across multi-day sessions

## Benchmarks

Z.ai did not publish a comprehensive benchmark suite at launch. Third-party reviews emphasize strong performance on repository-scale software engineering and long-running agent workflows. Competitive with frontier closed-source models on coding tasks.

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

- Long-horizon agentic coding workflows
- Repository-scale code understanding and refactoring
- Multi-step tool-use pipelines
- Complex debugging across large codebases
