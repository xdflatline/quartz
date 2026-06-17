---
title: Gemma 4 with Quantization-Aware Training
detail: Google has released new **Quantization-Aware Training (QAT)** checkpoints for the Gemma 4 model family. By integrating quantization directly into t...
details: Google has released new **Quantization-Aware Training (QAT)** checkpoints for the Gemma 4 model family. By integrating quantization directly into t...
tags:
  - raw
created: 2026-06-16
updated: 2026-06-16
type: raw
---
# Gemma 4 with Quantization-Aware Training

**Source:** Google Blog (https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)
**Date Retrieved:** 2026-06-16
**Type:** Article

---

# Summary: Gemma 4 Quantization-Aware Training (QAT)

Google has released new **Quantization-Aware Training (QAT)** checkpoints for the Gemma 4 model family. By integrating quantization directly into the training process, these models achieve significantly higher quality than standard Post-Training Quantization (PTQ) while drastically reducing memory footprints for local and edge deployment.

---

## Key Technical Innovations

Google engineered a custom **mobile-quantization schema** to ensure high performance on edge hardware:

*   **Static Activations:** Pre-calculates scaling data during training to reduce real-time processing overhead on mobile chips.
*   **Channel-wise Quantization:** Data structures are optimized for native calculation on mobile accelerators, avoiding slow workarounds.
*   **Targeted 2-bit Quantization:** Compresses token-generation layers to 2-bit while maintaining higher precision in core reasoning layers.
*   **Memory Optimization:** Focuses compression on vocabulary lists and short-term memory (KV cache).
    *   *Insight:* The **Gemma 4 E2B text-only model** (excluding per-layer embeddings) can now run in **under 1GB of memory**.

---

## Deployment & Ecosystem Support

The QAT checkpoints are available immediately on [Hugging Face](https://huggingface.co/collections/google/gemma-4-qat-q4-0) and are compatible with a wide range of developer tools:

| Category | Supported Tools |
| :--- | :--- |
| **Desktop/Local** | `llama.cpp`, Ollama, LM Studio |
| **On-Device/Web** | LiteRT-LM, Transformers.js |
| **Server/Serving** | SGLang, vLLM |
| **Apple Silicon** | MLX |
| **Fine-tuning** | Hugging Face Transformers, Unsloth |

---

## Important Excerpts & Facts

### Why QAT?

> "By simulating quantization during training, QAT minimizes quality loss when the model is compressed... our QAT results yield even higher overall quality compared to standard PTQ baselines."

### Workflow Compatibility

*   **GGUF formats:** Ready for `llama.cpp`.
*   **Compressed tensors:** Provided for `vLLM`.
*   **Unquantized checkpoints:** Available for users who need to convert/quantize into custom formats supporting Q4_0.

### Strategic Context

This release follows a series of rapid updates to the Gemma 4 ecosystem:

1.  **Multi-Token Prediction (MTP):** Introduced to accelerate inference.
2.  **12B Model:** Released to bridge the gap between E4B and 26B MOE models.
3.  **Modularity:** Users can optimize memory further by deploying only the specific modalities (text, audio, or vision) required for their use case.

---

## Actionable Resources

*   **Weights:** [Q4_0 Collection](https://huggingface.co/collections/google/gemma-4-qat-q4-0) | [Mobile-Optimized Collection](https://huggingface.co/collections/google/gemma-4-qat-mobile)
*   **Documentation:** [Official QAT Deployment Guide](https://ai.google.dev/gemma/docs/core#qat)