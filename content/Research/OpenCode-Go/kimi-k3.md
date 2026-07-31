---
title: Kimi K3
details: Moonshot AI's 2.8T-parameter open-weights flagship released July 16, 2026, with 1M context, native vision, and Kimi Delta Attention.
tags:
  - research
created: 2026-07-31
updated: 2026-07-31
type: note
---
# Kimi K3

**Developer:** Moonshot AI
**Released:** July 16, 2026 (API); weights due by July 27, 2026
**Model ID:** `opencode-go/kimi-k3`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 2.8T (world's first 3T-class open-source model) |
| Active Parameters | ~50B equivalent (16 of 896 experts per token) |
| Architecture | Sparse MoE with Stable LatentMoE framework |
| Total Experts | 896 |
| Selected Experts | 16 per token |
| Context Window | 1,048,576 tokens (1M) |
| Attention | Kimi Delta Attention (KDA) + Attention Residuals (AttnRes) -- hybrid linear |
| Modalities | Text + Vision (native, not adapter-based) |
| Training Precision | MXFP4 weights, MXFP8 activations |
| Reasoning | Always-on thinking mode (maximum reasoning effort default) |

## Key Features

- **First 3T-class open-source model** -- largest open-weights model available as of July 2026
- **Native vision** -- image understanding built into the backbone, not bolted on
- **Kimi Delta Attention (KDA)** -- hybrid linear attention with Attention Residuals, designed to help information flow through longer sequences and deeper models
- **Extreme sparsity** -- 16/896 expert routing, ~2.5x the scaling efficiency of K2
- **BrowseComp 90.4%** at full 1M context (Moonshot's own eval) -- the headline long-context number
- **Best on SWE Marathon (42.0) and ProgramBench (77.8)** -- leads on sustained-coding benchmarks, consistent with 1M context enabling full-repo understanding
- **0.5 pts behind GPT-5.6 Sol on Terminal-Bench 2.1 (88.3 vs 91.9)** -- within striking distance of the best closed-source model on agentic coding
- **vLLM support arriving with weight release** -- Kimi Delta Attention implementation scheduled

## Deployment Notes (Self-Hosting)

- **Not yet self-hostable from public weights as of 2026-07-31** -- weights due July 27, 2026
- Moonshot recommends **64+ accelerator supernode configuration** for production deployment
- Distributed inference required -- 896 experts with 16 active means expert-parallel routing is the dominant comms pattern
- License not yet published at announcement; weights release expected to clarify

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $3.00 / 1M tokens |
| Output | $15.00 / 1M tokens |
| Cache Read | $0.30 / 1M tokens |
| Est. requests per 5h | 110 |
| Est. requests per month | 490 |

Kimi K3 has the **second-highest per-token output cost** in the Go catalog (only above what doesn't yet exist) and the **lowest request budget** after the very low-throughput models. The 5h budget of 110 requests makes K3 a "frontier-only" model on Go -- reserve for tasks where it materially beats the cheaper flagships (GLM-5.2, MiniMax M3, Qwen3.7 Max).

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions` (OpenAI-compatible)

## Best For

- Frontier-quality open-weight coding and knowledge work
- Long-horizon agentic tasks where 1M context is the binding requirement
- Multimodal coding with image + text input (e.g., UI generation from mockups, screenshot-to-code)
- Tasks that benefit from Moonshot's always-on maximum-reasoning mode (long internal chains before output)
- Use cases that will eventually self-host K3 once weights ship and inference software matures
