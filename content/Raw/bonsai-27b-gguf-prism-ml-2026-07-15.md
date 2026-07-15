---
title: "Bonsai-27B-gguf (prism-ml)"
detail: Raw article — Bonsai-27B-gguf model card from prism-ml on Hugging Face. 1-bit GGUF Q1_0_g128 quantization of Qwen3.6-27B, ~3.9 GB deployed, ~90% of FP16 intelligence.
details: Raw article — Bonsai-27B-gguf model card from prism-ml on Hugging Face. 1-bit GGUF Q1_0_g128 quantization of Qwen3.6-27B, ~3.9 GB deployed, ~90% of FP16 intelligence.
tags:
  - raw
created: 2026-07-15
updated: 2026-07-15
type: raw
source: "https://huggingface.co/prism-ml/Bonsai-27B-gguf"
license: Apache 2.0
confidence: medium
---
# Bonsai-27B-gguf (prism-ml)

**Source:** https://huggingface.co/prism-ml/Bonsai-27B-gguf
**License:** Apache 2.0

## Summary

Bonsai-27B-gguf is a 1-bit (true 1.125 bpw) GGUF Q1_0_g128 quantization of Qwen3.6-27B from prism-ml, shipped at ~3.9 GB and claiming ~90% of FP16 intelligence with ~14.2x size reduction. Targeted at llama.cpp (CUDA, Metal, CPU) with an optional DSpark speculative-decoding drafter.

## Core Specifications

- **Base:** Qwen3.6-27B (27B hybrid-attention causal LM, architecture unchanged)
- **Parameters:** ~27.3B binary language weights + ~0.46B vision tower (27 blocks)
- **Architecture:** Hybrid attention (~75% linear / ~25% full), SwiGLU MLP, RoPE, RMSNorm
- **Context length:** 262K tokens
- **KV cache:** Near-lossless 4-bit KV quantization; full-attention cache on 16/64 layers (~4.3 GB at 262K)
- **Weight format:** GGUF Q1_0_g128 — {-1, +1} weights with FP16 group-wise scaling (1.125 bits/weight)
- **Deployed size:** ~3.9 GB (~14.2x reduction vs ~54 GB FP16)
- **Low-bit coverage:** End-to-end binary (embeddings, attention projections, MLP projections, LM head — no FP escape hatches)
- **Vision tower:** HQQ 4-bit (optional 0.63 GB mmproj pack, Q8_0 container)
- **Backends:** llama.cpp (CUDA, Metal, CPU)
- **Acceleration:** DSpark speculative-decoding drafter layer included

## Weight Representation: Q1_0_g128

Each weight is a single sign bit (`0` → `-scale`, `1` → `+scale`); every group of 128 weights shares one FP16 scale factor. Effective 1.125 bits/weight.

## Companion Variants

- **Bonsai-27B-mlx-1bit** — Native Apple Silicon (iPhone ~11 tok/s on iPhone 17 Pro Max via MLX Swift)
- **Ternary-Bonsai-27B-gguf** — Quality-oriented (~7.2 GB, 95% of FP16)

## Shipped Components

| Component | Pack | Size | Residency |
| :--- | :--- | --: | :--- |
| Language model | 1-bit g128 (Q1_0) | ~3.9 GB | Resident |
| DSpark drafter | Q4_1 (default) | 1.79 GB | Optional — speculative decoding |
| DSpark drafter | bf16 (reference) | 7.29 GB | Optional |
| Vision tower | mmproj HQQ 4-bit (Q8_0) | 0.63 GB | Optional — multimodal only |
| Vision tower | mmproj BF16 (reference) | 0.93 GB | Optional |

## Peak Memory at Context (Language Model Only)

| Build | Weights | 4K ctx | 10K ctx | 100K ctx |
| :--- | --: | --: | --: | --: |
| **1-bit Bonsai (llama.cpp Q1_0)** | 3.79 | 5.2 | 5.6 | 11.6 |
| Qwen3.6-27B "4-bit" (Q4_K_XL) | 17.6 | 19.2 | 19.6 | 25.6 |
| 27B 16-bit (GGUF bf16) | 51.25 | 52.6 | 53.3 | 59.3 |

100K context at 11.6 GB without KV compression fits mainstream laptops. With 4-bit KV cache: 100K drops to ~6.8 GB; full 262K fits in ~9.4 GB peak.

## Performance & Throughput

Measured with `llama-bench` on this GGUF pack (custom low-bit kernels). `tg128` = token generation; `pp512` = prompt processing.

| Platform | Footprint | TG128 (tok/s) | PP512 (tok/s) |
| :--- | --: | --: | --: |
| Laptop (Apple M5 Max, Metal) | 3.9 GB | 66.4 | 874 |
| Laptop (Apple M5 Pro, Metal) | 3.9 GB | 44.2 | 421 |
| Laptop (Apple M4 Pro, Metal) | 3.9 GB | 26.0 | 133 |
| Single GPU (H100, CUDA) | 3.9 GB | 104.8 | 2,755 |

**Energy efficiency:** Decode energy on M5 Pro measures 0.275 mWh/token (with DSpark drafter enabled) — an order of magnitude more efficient than datacenter GPUs (0.63–1.32 mWh/token).

## Speculative Decoding: DSpark

- **Architecture:** Compact six-layer block-parallel transformer conditioned on hidden states from five evenly spaced target layers
- **Serving weight footprint:** ~0.5 GB (embeddings/head shared with target)
- **Default pack:** Q4_1 at 1.79 GB (faster than bf16 reference, identical output quality)
- **Speedup:** 1.37x end-to-end on M5 Pro at typical context lengths
- **Lossless:** Verification preserves the target distribution exactly
