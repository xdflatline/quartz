---
title: "Local agent-model economics (intelligence per joule, footprint per agent)"
details: "Why a ~20GB, 3.4B-active model changes what can be run locally: the binding constraints for persistent agents are memory footprint, energy per query and decode bandwidth, not raw parameter count. Includes the intelligence-per-watt result (0.703 on DGX Spark versus 0.430 for Qwen3.6-35B-A3B) and the multi-agent demonstration of twenty simulated residents on one offline MacBook."
tags:
  - concept
  - local-llm
  - inference
  - evaluation
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Local agent-model economics (intelligence per joule, footprint per agent)

**Category:** Deployment Economics
**Status:** Vendor-demonstrated, 2026-11

## Overview

For cloud inference the cost unit is tokens. For **local, always-on agents** the binding constraints are different:

- **Memory footprint** — how many models (and how much context) fit on the device.
- **Energy per query** — what it costs to keep agents running all day on a battery or a wall socket.
- **Decode bandwidth** — how fast tokens come out of a model whose weights are already resident.

A 26.4B-total, 3.4B-active Mixture-of-Experts with a **~20GB** total footprint and native 4-bit weights targets exactly those constraints. Inkling 2 Mini runs on any Mac with at least **32GB RAM** via Ollama, on an NVIDIA DGX Spark, and offline on a 48GB MacBook Pro.

## Intelligence per joule

Researchers at Stanford's Hazy Research and Scaling Intelligence labs measured **intelligence per watt** — energy needed per query to reach a given performance level — with early access to the model:

| Model (precision on DGX Spark) | Score |
|---|---|
| Inkling 2 Mini (MXFP8, low reasoning effort) | **0.703** |
| Qwen3.6-35B-A3B (NVFP4) | 0.430 |
| Gemma-4-26B-A4B (NVFP4) | 0.159 |
| Qwen3.5-27B (INT4) | 0.036 |

Source: *Intelligence per Watt: Measuring Intelligence Efficiency of Local AI*, Saad-Falcon and Narayan et al., 2025 (https://arxiv.org/abs/2511.07885).

The metric matters because local agents are **continuous** workloads, not per-request ones. A model that is 20% slower per token but draws a fraction of the power can be the better choice for twenty persistent agents and the worse choice for one batch job.

## Footprint per agent

The demonstration is blunt: **twenty simulated villagers in a pixel town, all driven by the same model, on one offline MacBook**. Each resident plans a day, gossips, hosts bake-offs and answers notes left on doors.

This is a multi-agent architecture where the scarce resource is not API budget but **RAM and joules**. Consequences for design:

- **One model serving many roles** is cheaper than many specialised models, even when a specialist would score better on its narrow task.
- **Context management matters more than model routing** — every cached context competes for the same memory.
- **Throughput, not latency, is the target** for background agents; interactive latency matters only for the human-facing turn.

## Decode speed versus quality

The vendor plots coding score against a **theoretical tokens-per-second ceiling** (614 GB/s, BF16 weights, batch size one, including repeated reads across loops). Two caveats:

- The ceiling is theoretical and computed at BF16 while the model ships at NVFP4/MXFP8, so it is a shape comparison, not a measured throughput.
- Looping reads the same weights several times per token, which raises bandwidth per token — the very property that buys reasoning depth costs decode speed.

## The capability ceiling

Local capability is bounded by knowledge, and knowledge is a function of total parameters:

- **Closed-book factuality is average for its size.** AA-Omniscience score −8.6 with a 63.4% non-hallucination rate, behind Qwen3.8-27B and Nemotron 3.5 Super VL.
- **The model compensates with search and tools.** It leads comparable open-weights models on BrowseComp (79.0%), DeepSearchQA (85.3%) and MCP Atlas (82.7%).
- **Multi-turn chat and many-constraint instructions are weak spots** — 50.0% on MultiChallenge and 33.4% on ComplexConstraints v1.1, behind Qwen3.8-27B on both.

The practical read: a local model of this class is a strong **tool-using agent** and a mediocre **general assistant**. Deploying it for background agent work exploits its strengths; deploying it as the only chat model does not.

## Related Concepts

- [[Concepts/local-llm-hardware-requirements]] — the size tiers this model sits above
- [[Concepts/native-low-precision-training]] — why the footprint is ~20GB rather than 50GB
- [[Concepts/expert-pruning-and-healing]] — why total parameters are 26.4B rather than 100B+
- [[Concepts/looped-transformer-architecture]] — the decode-bandwidth cost of extra passes
- [[Concepts/llm-quantization-reference]] — the precision vocabulary behind the table

## Related Research

- [[Research/local-llm-cpu-inference-2026]] — CPU/Metal/CUDA deployment landscape
- [[Research/looped-transformers-and-local-frontier]] — the full synthesis for this release

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Intelligence per Watt: https://arxiv.org/abs/2511.07885
- Model card: https://thinkingmachines.ai/model-card/inkling-2-mini/
