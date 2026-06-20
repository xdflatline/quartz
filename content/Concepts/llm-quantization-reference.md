---
title: LLM Quantization Reference
detail: Quantization reduces model weight precision to trade off memory usage against output quality. The article recommends **Q4_K_M as the default sweet ...
details: Quantization reduces model weight precision to trade off memory usage against output quality. The article recommends **Q4_K_M as the default sweet ...
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# LLM Quantization Reference

**Source:** DEV Community article (https://dev.to/pavelespitia/how-much-ram-do-you-really-need-to-run-llms-locally-2026-benchmarks-3kd2)
**Category:** Technical Reference
**Status:** 2026 benchmarks

---

## Overview

Quantization reduces model weight precision to trade off memory usage against output quality. The article recommends **Q4_K_M as the default sweet spot** for most users.

---

## Quantization Levels

| Quantization | Bits/Param | GB per 1B Params | Quality Assessment | Use Case |
|--------------|------------|------------------|-------------------|----------|
| **FP16** | 16 | ~2.0 GB | Full, reference | Baseline comparison only |
| **Q8_0** | 8 | ~1.1 GB | Nearly lossless | Quality-critical, VRAM available |
| **Q5_K_M** | ~5.5 | ~0.75 GB | Very good | Higher quality than Q4, moderate VRAM |
| **Q4_K_M** | ~4.5 | ~0.6 GB | **Good (Sweet spot)** | **Default recommendation** |
| **Q3_K_M** | ~3.5 | ~0.5 GB | Noticeable degradation | Memory-constrained only |
| **Q2_K** | ~2.5 | ~0.4 GB | Often too lossy | Avoid unless desperate |

---

## Key Formula

```
Model Size (GB) = Parameters (Billions) × Bytes per Parameter (GB) + Overhead
```

**Overhead** includes KV cache and runtime — scales with context length.

---

## Practical Sizing Examples (Q4_K_M)

| Model | Params | Q4 Size | Min RAM (CPU) | Min VRAM (GPU) |
|-------|--------|---------|---------------|----------------|
| qwen2.5-coder:1.5b | 1.5B | ~1.0 GB | 4 GB | 2 GB |
| mistral:7b / llama3.1:8b | 7–8B | ~4.1–4.7 GB | 8 GB | 6 GB |
| deepseek-coder-v2 (MoE) | 16B | ~8.9 GB | 16 GB | 10 GB |

---

## Ollama Pull Commands

```bash
# Sweet spot (recommended)
ollama pull qwen2.5-coder:7b-instruct-q4_K_M

# Higher quality if VRAM allows
ollama pull qwen2.5-coder:7b-instruct-q8_0
```

---

## Related Concepts

- [[RAM vs VRAM for LLM Inference]]
- [[Local LLM Hardware Requirements]]
- [[Model Benchmark Tokens per Second]]

---

## References

- Raw Article: [[devto-llm-local-ram-benchmarks-2026]]
- Source: https://dev.to/pavelespitia/how-much-ram-do-you-really-need-to-run-llms-locally-2026-benchmarks-3kd2