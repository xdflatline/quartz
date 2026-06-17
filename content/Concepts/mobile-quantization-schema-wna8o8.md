---
source: "google-blog-quantization-aware-training-gemma-4-2026-06-16"
category: "Architecture Pattern"
status: "Production-validated"
---

# Mobile Quantization Schema (wNa8o8)

**Source:** [[raw/articles/google-blog-quantization-aware-training-gemma-4-2026-06-16]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

The mobile quantization schema (wNa8o8) is a custom hardware-efficient quantization format engineered specifically for mobile accelerators. It structures compressed data to fit the design of mobile NPUs and DSPs, enabling efficient inference without slow workarounds or software emulation.

---

## Core Content

### Technical Specifications

| Component | Detail | Purpose |
|----------|--------|---------|
| **Weights** | 4-bit symmetric channel-wise quantization | Core weight compression |
| **Activations** | 8-bit symmetric quantization | Activation precision |
| **Schema Name** | wNa8o8 (weights N-bit, activations 8-bit, output 8-bit) | Naming convention |
| **Target Hardware** | Mobile NPUs, DSPs, Qualcomm Hexagon, Apple Neural Engine | Deployment platforms |
| **Data Layout** | Channel-first, aligned to hardware register widths | Memory access efficiency |

### Key Innovations

1. **Channel-wise Quantization**: 
   - Weights quantized per output channel rather than per tensor
   - Aligns with mobile accelerator architectures that process data channel-wise
   - Eliminates need for slow dequantization/re-quantization workarounds

2. **Static Activations**:
   - Scaling factors pre-calculated during training
   - Reduces real-time computation overhead on mobile chips
   - Eliminates runtime statistics gathering

3. **Targeted 2-bit Decoding Layers**:
   - Token generation layers compressed to 2-bit weights
   - Core reasoning layers maintained at higher precision (4-bit)
   - Leverages noise robustness of language model heads

### Implementation Details

#### Weight Quantization Formula
```
Q_w = round(W * S_w)  # Symmetric per-channel
W_dequant = Q_w / S_w
```
Where S_w is the scaling factor calculated per output channel.

#### Activation Quantization
```
Q_a = clamp(round(A * S_a), -127, 127)  # Symmetric int8
A_dequant = Q_a / S_a
```
With static S_a determined during training.

#### Memory Layout Optimizations
- Weights stored in channel-major order for coalesced memory access
- Bias terms fused where possible
- Quantization parameters stored alongside weights for cache locality

### Performance Characteristics

| Metric | Improvement |
|--------|-------------|
| **Inference Latency** | 2-3x faster than software-emulated quantization |
| **Memory Bandwidth** | Reduced by 4x (vs BF16) for weights |
| **Power Consumption** | 40-60% lower than FP16 inference |
| **NPU Utilization** | >85% vs <50% for unoptimized formats |

---

## Key Insights

1. **Hardware-Aligned Design**: The schema isn't just about bit-width; it's about data layout matching hardware capabilities
2. **Static vs Dynamic**: Pre-computed scaling factors eliminate runtime overhead critical for mobile battery life
3. **Hybrid Precision**: Different layers get different treatment based on sensitivity to noise
4. **Ecosystem Impact**: Enables LLMs to run on mid-tier smartphones without specialized cooling

---

## Related Concepts

- [[Concepts/quantization-aware-training-qat]]
- [[Concepts/static-activations]]
- [[Concepts/channel-wise-quantization]]
- [[Concepts/targeted-2bit-quantization]]
- [[Concepts/kv-cache-optimization]]
- [[Concepts/litert-lm]]
- [[Concepts/transformers-js]]

---

## Entities

- [[Entities/google-deepmind]]
- [[Entities/gemma-4-model-family]]
- [[Entities/litert-lm]]
- [[Entities/transformers-js]]
- [[Entities/qualcomm-hexagon]]
- [[Entities/apple-neural-engine]]

---

## References

- Raw Article: [[raw/articles/google-blog-quantization-aware-training-gemma-4-2026-06-16]]
- Original: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
- LiteRT-LM Discussion: https://github.com/google-ai-edge/LiteRT-LM/issues/2497
- Mobile Model Card: https://huggingface.co/google/gemma-4-E2B-it-qat-mobile-transformers
- Pulse 2.0 Analysis: https://pulse2.com/google-gemma-4-qat-models-reduce-memory-requirements-for-mobile-and-laptop-ai/