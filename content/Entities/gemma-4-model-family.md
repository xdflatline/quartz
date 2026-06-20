---
title: Gemma 4 Model Family
detail: Gemma 4 is a family of open-weight generative AI models developed by Google DeepMind, designed for reasoning, summarization, and question answering...
details: Gemma 4 is a family of open-weight generative AI models developed by Google DeepMind, designed for reasoning, summarization, and question answering...
tags:
  - entities
created: 2026-06-16
updated: 2026-06-16
type: entitie
source: "Google Blog (Gemma 4 QAT)"
category: Model Family
repository: "https://huggingface.co/google"
website: "https://ai.google.dev/gemma"
license: Apache 2.0
---
# Gemma 4 Model Family

**Source:** Google Blog (Quantization-Aware Training)
**Category:** Model Family
**Repository**: https://huggingface.co/google
**Website**: https://ai.google.dev/gemma
**License**: Apache 2.0

---

## Overview

Gemma 4 is a family of open-weight generative AI models developed by Google DeepMind, designed for reasoning, summarization, and question answering. The family introduces native multimodal support and significantly expanded context windows, with specialized checkpoints optimized via Quantization-Aware Training (QAT) for efficient deployment across hardware tiers.

---

## Key Details

### Model Variants & Specifications

| Model | Type | Parameters | Context Window | Key Characteristics |
|-------|------|------------|----------------|---------------------|
| **Gemma 4 E2B** | Dense | ~2.6B effective | 128K tokens | Ultra-mobile optimized, Per-Layer Embeddings (PLE) |
| **Gemma 4 E4B** | Dense | ~4.4B effective | 128K tokens | Mobile/edge optimized, Per-Layer Embeddings (PLE) |
| **Gemma 4 12B** | Dense | 12B unified | 256K tokens | Encoder-free, direct modality projection |
| **Gemma 4 26B A4B** | MoE | 25.2B total, 3.8B active | 256K tokens | Mixture-of-Experts, high-throughput reasoning |
| **Gemma 4 31B** | Dense | 31B | 256K tokens | High-performance reasoning/coding |

### Quantization-Aware Training (QAT) Checkpoints

Each model is available with QAT optimization in multiple formats:

1. **Unquantized QAT (Q4_0)**: BF16 weights for research/custom compilation
2. **GGUF (Q4_0)**: Optimized for llama.cpp, Ollama, LM Studio
3. **Compressed Tensors (w4a16)**: For vLLM/SGLang server inference
4. **Mobile-optimized (wNa8o8)**: For edge/mobile deployment (LiteRT-LM, Transformers.js)

### Memory Footprints (QAT 4-bit)

| Model | Type | QAT 4-bit Memory | Typical Deployment |
|-------|------|------------------|-------------------|
| E2B | Dense | ~3GB (~1GB text-only) | Phones, Raspberry Pi 5 |
| E4B | Dense | ~5GB | 8GB laptops, 6GB+ GPUs |
| 12B | Dense | ~7GB | 8-12GB GPUs, 16GB Macs |
| 26B-A4B | MoE | ~15GB | 16GB Macs, 16GB GPUs |
| 31B | Dense | ~18GB | 24GB GPUs, 32GB Macs |

### Key Capabilities
- **Extended Context**: 128K (small), 256K (medium/large) tokens
- **Native Multimodality**: Text, image (variable resolution), video, audio
- **Reasoning & Agents**: Configurable "thinking mode", built-in function calling
- **System Prompts**: Native `system` role support for structured control
- **Speculative Decoding**: Dedicated draft model for faster inference
- **Multi-Token Prediction (MTP)**: Available for accelerated inference

### Supported Ecosystem Tools
- **Local**: llama.cpp, Ollama, LM Studio
- **On-Device/Web**: LiteRT-LM, Transformers.js
- **Server**: SGLang, vLLM
- **Apple Silicon**: MLX
- **Fine-tuning**: Hugging Face Transformers, Unsloth
- **Mobile**: Android NNAPI, iOS Core ML

---

## Related Concepts

- [[Concepts/quantization-aware-training-qat]]
- [[Concepts/mobile-quantization-schema-wna8o8]]
- [[Concepts/per-layer-embeddings-ple]]
- [[Concepts/unified-architecture-12b]]
- [[Concepts/mixture-of-experts-moe]]
- [[Concepts/multi-token-prediction-mtp]]
- [[Concepts/speculative-decoding]]
- [[Concepts/thinking-mode]]
- [[Concepts/static-activations]]
- [[Concepts/channel-wise-quantization]]
- [[Concepts/targeted-2bit-quantization]]
- [[Concepts/kv-cache-optimization]]

---

## Entities

- [[google-deepmind]]
- [[gemma-4-e2b]]
- [[gemma-4-e4b]]
- [[gemma-4-12b]]
- [[gemma-4-26b-a4b]]
- [[gemma-4-31b]]
- [[hugging-face]]
- [[unsloth]]
- [[litert-lm]]
- [[transformers-js]]
- [[vllm]]
- [[sglang]]
- [[ollama]]
- [[llama.cpp]]
- [[mlx]]
- [[kaggle]]

---

## References

- Raw Article: Google Blog (Quantization-Aware Training)
- Original: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
- Model Overview: https://ai.google.dev/gemma/docs/core
- Model Card: https://ai.google.dev/gemma/docs/core/model_card_4
- Hugging Face Collections: https://huggingface.co/collections/google/gemma-4
- Kaggle Models: https://www.kaggle.com/models?query=gemma-4&publisher=google