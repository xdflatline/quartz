---
source: "google-blog-quantization-aware-training-gemma-4-2026-06-16"
category: "Organization"
repository: "https://github.com/google"
website: "https://ai.google.dev/"
---

# Google DeepMind

**Source:** [[raw/articles/google-blog-quantization-aware-training-gemma-4-2026-06-16]]
**Category:** Organization
**Repository:** https://github.com/google
**Website**: https://ai.google.dev/

---

## Overview

Google DeepMind is the AI research laboratory of Google, responsible for developing the Gemma family of open-weight language models. They pioneered Quantization-Aware Training (QAT) techniques specifically optimized for mobile and edge deployment scenarios.

---

## Key Details

- **Focus**: Fundamental AI research, large language models, multimodal AI
- **Notable Projects**: Gemma family, AlphaFold, AlphaGo, Gemini models
- **Approach**: Combines research breakthroughs with practical deployment considerations
- **Licensing**: Apache 2.0 for Gemma models, enabling commercial and research use
- **Data Policy**: Training data cutoff January 2025 for Gemma 4

### Gemma 4 Contributions
- Introduced Multi-Token Prediction (MTP) for faster inference
- Released 12B unified architecture for multimodal tasks
- Pioneered mobile-optimized quantization schemas (wNa8o8)
- Provided QAT checkpoints across multiple formats for ecosystem compatibility
- Extended context windows to 128K/256K tokens depending on model size

---

## Related Concepts

- [[Concepts/quantization-aware-training-qat]]
- [[Concepts/mobile-quantization-schema-wna8o8]]
- [[Concepts/multi-token-prediction-mtp]]
- [[Concepts/unified-architecture-12b]]
- [[Concepts/per-layer-embeddings-ple]]

---

## Entities

- [[Entities/gemma-4-model-family]]
- [[Entities/gemma-4-e2b]]
- [[Entities/gemma-4-e4b]]
- [[Entities/gemma-4-12b]]
- [[Entities/gemma-4-26b-a4b]]
- [[Entities/gemma-4-31b]]
- [[Entities/hugging-face]]
- [[Entities/unsloth]]
- [[Entities/litert-lm]]
- [[Entities/vllm]]
- [[Entities/sglang]]
- [[Entities/ollama]]
- [[Entities/llama.cpp]]

---

## References

- Raw Article: [[raw/articles/google-blog-quantization-aware-training-gemma-4-2026-06-16]]
- Original: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
- Gemma Documentation: https://ai.google.dev/gemma/docs
- Model Collections: https://huggingface.co/collections/google/gemma-4