---
title: Local LLM Hardware Requirements
detail: Hardware tier recommendations based on real-world benchmarks for running LLMs locally via Ollama.
details: Hardware tier recommendations based on real-world benchmarks for running LLMs locally via Ollama.
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# Local LLM Hardware Requirements

**Source:** DEV Community article (https://dev.to/pavelespitia/how-much-ram-do-you-really-need-to-run-llms-locally-2026-benchmarks-3kd2)
**Category:** Hardware Specification
**Status:** 2026 benchmarks, practical tiers

---

## Overview

Hardware tier recommendations based on real-world benchmarks for running LLMs locally via Ollama.

---

## Tier 1: 8GB Laptop (No Dedicated GPU)

| Constraint | Detail |
|------------|--------|
| **Max Model** | 1.5B params (qwen2.5-coder:1.5b) |
| **Quantization** | Q4_K_M |
| **Tokens/sec** | 15–30 (CPU only) |
| **Caveat** | 7B models possible but struggle with OS/browser overhead |
| **RAM Budget** | Model ≤ Total RAM - 4GB ≈ 4GB for model |

**Verdict:** Usable for coding assistants on small models only.

---

## Tier 2: 16GB Dev Box (No Dedicated GPU) — *Sweet Spot*

| Constraint | Detail |
|------------|--------|
| **Max Model** | 7B–8B params (mistral:7b, llama3.1:8b) |
| **Quantization** | Q4_K_M |
| **Tokens/sec** | 4–9 (CPU only) |
| **Multitasking** | Comfortably runs 7B + IDE + browser |
| **RAM Budget** | Model ≤ 12GB (16 - 4GB overhead) |

**Verdict:** Best value for developers without GPU budget.

---

## Tier 3: 24GB+ System with GPU

| GPU VRAM | Max Model (Q4) | Performance |
|----------|----------------|-------------|
| **8–12 GB** | 7B–8B class | **45–80 tok/s** (full offload) |
| **16–20 GB** | 13B–16B class (MoE) | **50–80 tok/s** |
| **24 GB** | 32B class | **Snappy for large models** |

**Key Insight:** Full VRAM offload = 10x speedup vs CPU.

---

## Model Benchmark Reference (Q4_K_M)

| Model | Params | Q4 Size | Min RAM | CPU tok/s | GPU tok/s (8–12GB VRAM) |
|-------|--------|---------|---------|-----------|------------------------|
| qwen2.5-coder:1.5b | 1.5B | 1.0 GB | 4 GB | 15–30 | 80–130 |
| mistral:7b | 7B | 4.1 GB | 8 GB | 5–9 | 45–70 |
| llama3.1:8b | 8B | 4.7 GB | 8 GB | 4–8 | 40–65 |
| deepseek-coder-v2 | 16B MoE | 8.9 GB | 16 GB | 8–14 | 50–80 |

---

## Token/sec Quality Thresholds

| tok/s | Experience |
|-------|------------|
| **< 5** | Painful — noticeable lag |
| **5–15** | Usable but slow |
| **15–30** | Comfortable |
| **> 30** | Snappy / instant feel |

---

## Sizing Rules

1. **RAM-only:** `Max Model Budget = Total RAM - 4GB`
2. **With GPU:** `Max Model ≤ VRAM` (for full offload)
3. **Always pull explicit quantization tags**:
   ```bash
   ollama pull <model>:<size>-instruct-q4_K_M
   ```

---

## Related Concepts

- [[LLM Quantization Reference]]
- [[RAM vs VRAM for LLM Inference]]
- [[Model Benchmark Tokens per Second]]

---

## References

- Raw Article: [[devto-llm-local-ram-benchmarks-2026]]
- Source: https://dev.to/pavelespitia/how-much-ram-do-you-really-need-to-run-llms-locally-2026-benchmarks-3kd2