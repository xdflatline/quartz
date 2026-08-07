---
title: Quantization-Aware Training (QAT)

details: Quantization-Aware Training (QAT) is a technique where quantization errors are simulated during the training process, allowing the model to learn w...
tags:
  - concepts
  - quantization
  - training
created: 2026-06-17
updated: 2026-06-17
type: concept
source: "Google Blog (Gemma 4 QAT)"
category: Training Technique
status: Production-validated
---
# Quantization-Aware Training (QAT)

**Source:** Google Blog
**Category:** Training Technique | Learning Mechanism
**Status:** Production-validated

---

## Overview

Quantization-Aware Training (QAT) is a technique where quantization errors are simulated during the training process, allowing the model to learn weight configurations that are robust to low-precision arithmetic. Unlike Post-Training Quantization (PTQ) which compresses a model after training, QAT integrates the quantization simulation directly into the forward and backward passes, enabling the model to compensate for precision loss and maintain near-full-precision accuracy even at aggressive compression levels (2-bit and 4-bit).

---

## Core Content

### The Problem with PTQ

Post-Training Quantization applies rounding/clipping to weights after training completes. The model never encounters these quantization errors during training, so its weights are not optimized for the discretized weight space. This causes:
- **Accuracy Cliff**: Sharp degradation below 4-bit precision
- **Unpredictable Quality Loss**: Different layers degrade at different rates
- **No Recovery Path**: Errors are baked in; no way to fine-tune back without retraining

### How QAT Works

QAT uses the **Straight-Through Estimator (STE)** to overcome the non-differentiability of quantization operations:

```python
import torch

class STEFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        # Forward pass: quantize weights (e.g., to 4-bit grid)
        return torch.round(input)  # Simulated quantization
    
    @staticmethod
    def backward(ctx, grad_output):
        # Backward pass: pass gradients through unchanged
        # Treats rounding as identity function
        return grad_output

# In model layer:
quantized_weight = STEFunction.apply(full_precision_weight)
output = quantized_weight @ input
```

**Key Insight**: The forward pass uses quantized weights (simulating inference-time precision), while the backward pass treats the quantization as a transparent pass-through, allowing gradients to flow to full-precision latent weights.

### Gemma 4 QAT Specifics

| Aspect | Detail |
|--------|--------|
| **Precision Targets** | 4-bit (Q4_0), 2-bit (targeted layers) |
| **Training Integration** | Full training run with quantization simulation |
| **Quality Metric** | Near-BF16 performance at 4-bit; significant MMLU gains over PTQ |
| **Memory Reduction** | ~72% VRAM reduction vs BF16 |
| **Adapter Availability** | Unquantized checkpoints for custom compilation |

### QAT vs PTQ Comparison

| Feature | PTQ | QAT |
|---------|-----|-----|
| **Timing** | After training | During training |
| **Accuracy at 4-bit** | Moderate degradation | Near-full precision |
| **Accuracy at 2-bit** | Severe collapse | Usable (targeted layers) |
| **Compute Cost** | Low (minutes) | High (full training) |
| **Complexity** | Simple conversion | STE, custom schedulers |
| **Flexibility** | Any pre-trained model | Requires training from scratch or continued pre-training |

### Gemma 4 QAT Results

- **E2B Model**: ~3 GB total memory (mobile: ~1 GB text-only)
- **26B-A4B MoE**: Top-1 accuracy 85.6% with Unsloth dynamic GGUF (vs 70.2% naive Q4_0)
- **Sampling Params**: Temperature 1.0, Top-P 0.95, Top-K 64 (preserves original distribution)

---

## Key Insights

1. **QAT is not free** — requires full training infrastructure, but pays off at deployment scale
2. **STE is the enabling trick** — makes non-differentiable rounding differentiable for backprop
3. **Mixed precision by layer** — critical for aggressive compression; reasoning layers stay higher precision
4. **Format matters** — naive Q4_0 conversion of QAT checkpoints causes scale mismatch; use Unsloth dynamic GGUFs
5. **Ecosystem convergence** — QAT checkpoints shipped in multiple formats (GGUF, compressed tensors, mobile wNa8o8) for broad compatibility

---

## Related Concepts

- [[mobile-quantization-schema-wna8o8]]
- [[static-activations]]
- [[channel-wise-quantization]]
- [[targeted-2bit-quantization]]
- [[kv-cache-optimization]]
- [[multi-token-prediction-mtp]]
- [[per-layer-embeddings-ple]]
- [[post-training-quantization-ptq]]

---

## Entities

- [[google-deepmind]]
- [[gemma-4-model-family]]
- [[hugging-face]]
- [[unsloth]]

---

## References

- Raw Article: Google Blog (Quantization-Aware Training)
- Original: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
- Technical Deep Dive: https://explore.n1n.ai/blog/google-gemma-4-qat-quantization-aware-training-2026-06-13
- Self-Hosting Guide: https://lushbinary.com/blog/gemma-4-qat-self-hosting-guide-ollama-llama-cpp-vllm/
- Google AI Docs: https://ai.google.dev/gemma/docs/core