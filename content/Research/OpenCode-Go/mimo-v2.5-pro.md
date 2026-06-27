---
title: MiMo-V2.5-Pro
details: Xiaomi's flagship 1T-parameter MoE model with hybrid attention, MTP, and frontier-class agentic coding performance.
tags:
  - research
created: 2026-06-27
updated: 2026-06-27
type: note
---

# MiMo-V2.5-Pro

**Developer:** Xiaomi
**Released:** April 27, 2026
**License:** Open-source (permissive)
**Model ID:** `opencode-go/mimo-v2.5-pro`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 1.02T |
| Active Parameters | 42B per token |
| Architecture | Mixture-of-Experts (MoE) |
| Hidden Size | 6144 |
| Num Layers | 70 (1 dense + 69 MoE) |
| Context Window | 1M tokens (256K for base) |
| Precision | FP8 (E4M3) Mixed |
| Pre-training | 27T tokens at 32K native, extended to 1M |
| Attention | Hybrid: Sliding Window (128-token) + Global at 6:1 ratio |
| Decoding | Multi-Token Prediction (MTP), ~3x output throughput |

## Key Features

- **Trillion-scale MoE** -- 1.02T total / 42B active
- **Hybrid attention** -- 7x KV-cache reduction at long context via 6:1 SWA:Global ratio
- **Multi-Token Prediction** -- triples output throughput, accelerates RL rollouts
- **3-stage post-training:** SFT, domain-specialized RL, multi-teacher on-policy distillation (MOPD)
- **Harness awareness** -- actively manages its own context and memory during long tasks
- **1000+ tool calls** demonstrated in sustained agentic workflows

## Benchmarks

| Benchmark | Score |
|-----------|-------|
| SWE-Bench Pro | 57.2 |
| SWE-bench Verified | 78.9 |
| Terminal-Bench 2.0 | 68.4 |
| GDPVal-AA (Elo) | 1581 |
| tau3-bench | 72.9 |

Competitive with GPT-5.4 and Claude Opus 4.6 on coding agent benchmarks.

## Demonstrated Capabilities

- Built a SysY compiler in Rust (672 tool calls, 4.3 hours, 233/233 tests passed)
- Produced a full-featured video editor (8,192 lines, 1,868 tool calls, 11.5 hours)
- Designed analog EDA circuits (FVF-LDO in TSMC 180nm CMOS)

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $1.74 / 1M tokens |
| Output | $3.48 / 1M tokens |
| Cache Read | $0.0145 / 1M tokens |
| Est. requests per 5h | 3,250 |
| Est. requests per month | 16,300 |

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions`

## Best For

- Complex long-horizon agentic coding (1000+ tool calls)
- Full application development from prompts
- Tasks requiring frontier-class reasoning at open-weight pricing
- Multi-hour autonomous coding sessions
