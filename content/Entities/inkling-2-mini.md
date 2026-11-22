---
title: "Inkling 2 Mini"
details: "Thinking Machines Lab's 26.4B-total, 3.4B-active open-weights Mixture-of-Experts looped transformer (24 layers, middle twelve run three times, ~20GB footprint in native NVFP4/MXFP8). Leads open-weights models under 100B total parameters on DeepSWE v1.1 (48.2%) and Vals Index v2.2 (46.5%), runs offline on a 48GB MacBook Pro, and is available through Tinker, Ollama, SGLang, vLLM and GGUF builds."
tags:
  - entity
  - llm
  - local-llm
  - inference
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Inkling 2 Mini

**Category:** Open-weights language model
**Vendor:** [[Entities/thinking-machines-lab]]
**Released:** 2026-11-20
**Weights:** https://huggingface.co/thinkingmachines/Inkling-2-Mini

## Specifications

- **Architecture:** Mixture-of-Experts looped transformer, 24 layers in four blocks of six.
- **Looping:** blocks 2 and 3 run three times per token → 48 layer applications per token.
- **Parameters:** 26.4B total, 3.4B active, 5.4B weight activations per token (accounts for looped reads).
- **Routing:** sparsity 8-of-128 after pruning (started at 8-of-384).
- **Precision:** 20 layers NVFP4, final 4 layers MXFP8 — trained and deployed in the same formats.
- **Memory footprint:** ~20GB.
- **Context / deployment:** any Mac with ≥32GB RAM via Ollama; NVIDIA DGX Spark; GGUF via Unsloth and llama.cpp.
- **Modalities:** vision-capable (MMMU Pro 74.9%, ScreenSpot Pro 76.5% original / 87.7% with Python, OmniDocBench 92.8%).

## Reported benchmark highlights

| Area | Benchmark | Score |
|---|---|---|
| Coding | DeepSWE v1.1 | 48.2% |
| Coding | SWE-bench Pro v2 Hard | 77.9% |
| Coding | SWE-bench Verified (bash only) | 79.2% |
| Coding | SWE-bench Multilingual | 73.7% |
| Coding | Terminal Bench v2.1 | 71.6% |
| Coding | Vibe Code Bench v1.1 | 77.9% |
| Kernel | PMPP-Hard (AUC, 0–10h) | 455.82 |
| Tool use | BrowseComp (with compaction) | 79.0% |
| Tool use | DeepSearchQA (with compaction) | 85.3% |
| Tool use | MCP Atlas | 82.7% |
| Agentic work | JobBench | 49.6% |
| Agentic work | AutomationBench-AA v1.0.6 | 41.8% |
| Reasoning | HLE-Diamond | 15.2% |
| Reasoning | ARC-AGI v1 / v2 | 84.5% / 49.3% |
| Long context | LongBench v2 | 66.9% |
| Long context | MRCR v2 8-needle 256K–512K | 46.4% |
| Third-party | AA Index v5.0 | 20.1 |
| Third-party | Vals Index v2.2 | 46.5% |

The vendor states it leads **every open-weights model with less than 100B total parameters** on DeepSWE v1.1 and Vals Index v2.2, and is behind only Qwen3.8-27B on several others.

## Limitations (vendor-stated)

- **Multi-turn chat and many-constraint instructions:** MultiChallenge 50.0%, ComplexConstraints v1.1 33.4% — behind Qwen3.8-27B on both.
- **Reasoning-intensive benchmarks:** trails larger models on CritPt v2 and HLE-Diamond.
- **Knowledge:** AA-Omniscience −8.6 with a 63.4% non-hallucination rate; factuality is in line with same-size models, not better. Looping adds reasoning, not facts.
- **CoT controllability:** follows instructions about its own reasoning ≤0.1% of the time at matched CoT length — poor, like its sibling models.

## Training summary

1. Pretraining at sparsity 48 with 8-of-384 routing.
2. Midtraining: prune two-thirds of experts to the 128 most used per layer ([[Concepts/expert-pruning-and-healing]]).
3. Healing: 1T tokens distilled from a larger internal Inkling model.
4. SFT, then RL for 2.2T tokens over 2,000 steps, including on-policy distillation.
5. Native 4-bit training throughout ([[Concepts/native-low-precision-training]]).

## Availability

- **Tinker** — inference, fine-tuning, playground ([[Entities/tinker]]).
- **Local runtimes** — Ollama (Mac), Unsloth / llama.cpp (GGUF), SGLang, vLLM, NVIDIA Dynamo, TokenSpeed, Llama App.
- **RL fine-tuning** — SkyRL, Miles, NVIDIA AutoModel.
- **Research sibling** — `TML-d24-varloop-research` (1–5 variable loop passes) is released for monitorability and interpretability research.

## Related

- [[Concepts/looped-transformer-architecture]] — the architecture
- [[Concepts/latent-reasoning-and-cot-monitorability]] — the oversight analysis
- [[Concepts/local-agent-model-economics]] — why the footprint matters
- [[Research/looped-transformers-and-local-frontier]] — the synthesis

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Model card: https://thinkingmachines.ai/model-card/inkling-2-mini/
- Weights: https://huggingface.co/thinkingmachines/Inkling-2-Mini
