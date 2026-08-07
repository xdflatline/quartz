---
title: "Local LLMs on Laptop CPU in 2026: Model Comparison for Self-Hosting"

details: "Synthesis of small open-weight LLMs (1B-30B) that can be self-hosted and run on a laptop CPU in 2026, with benchmark data, quantization trade-offs, runtime stack (llama.cpp / Ollama / MLX), and per-tier hardware recommendations. Covers Phi-4 / Phi-4-mini, Gemma 4 (E2B / E4B / 12B / 26B-A4B), Qwen 3 / 3.5 / 3.6, Mistral Small 3.1 / 4, Llama 3.x / 4 Scout, SmolLM3, and DeepSeek-R1 distill variants. Output: a single comparison matrix, a per-RAM-class decision tree, and a quantified read on the CPU-only vs Metal/CUDA vs NPU accelerator trade-off."
tags:
  - research
  - llm
  - inference
  - local-llm
created: 2026-07-31
updated: 2026-07-31
type: research
sources:
  - "Hugging Face blog — Best Open Source LLM Models to Run Locally in 2026 (https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally)"
  - "SitePoint — The Definitive Guide to Local LLMs in 2026 (https://www.sitepoint.com/definitive-guide-local-llms-2026-privacy-tools-hardware/)"
  - "LocalAIMaster — Best Small Language Models 2026 (https://localaimaster.com/blog/small-language-models-guide-2026)"
  - "PromptQuorum — Best CPU-Only Local LLM 2026 (https://www.promptquorum.com/local-llms/best-cpu-only-llm)"
  - "Google Blog — Introducing Gemma 4 12B (https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)"
  - "Hugging Face — google/gemma-4-12B model card (https://huggingface.co/google/gemma-4-12B)"
  - "Unsloth — Gemma 4 how to run locally (https://unsloth.ai/docs/models/gemma-4)"
  - "Hugging Face blog — SmolLM3 (https://huggingface.co/blog/smollm3)"
  - "Daily.dev — Best Local LLM Models to Run in 2026 (https://daily.dev/blog/best-local-llm-models-run/)"
  - "Onyx — Self-Hosted LLM Leaderboard (https://onyx.app/self-hosted-llm-leaderboard)"
  - "Pinggy — Picking the Right Hardware to Run LLMs Locally in 2026 (https://pinggy.io/amp/blog/best_hardware_for_self_hosting_local_llms/)"
  - "dev.to — Running Local LLMs, CPU vs GPU speed test (https://dev.to/maximsaplin/running-local-llms-cpu-vs-gpu-a-quick-speed-test-2cjn)"
---
# Research Index: Local LLMs on Laptop CPU in 2026 — Model Comparison for Self-Hosting

**Updated:** 2026-07-31
**Scope:** Open-weight LLMs in the 1B-30B range (with selected MoE variants up to ~120B) that can be self-hosted and run with usable throughput on a laptop CPU, with or without a discrete GPU. Covers July 2026 model landscape.

---

## 1. Overview

The "local LLM" question in 2026 is no longer "can it run" but "how much does it cost you in latency and quality." The CPU-only path is genuinely viable for 3-8B dense models at Q4_K_M, and for 4-bit MoE families (Qwen 3.5, Mistral Small 4) up to 30B total parameters with 3-6B active, because the active set is what gets serialized through memory bandwidth. The key technical shift in 2026 is **uniform-quantization at Q4 with calibrated quality recovery** (QAT) and **MoE with very low active parameter counts**, both of which let "laptop-class" hardware serve 70B-class quality.

The three forces shaping the landscape:
1. **GGUF + llama.cpp** is the de-facto portable runtime (Apple Metal, CUDA, Vulkan, CPU). Ollama, LM Studio, and MLX all sit on top of llama.cpp or its derivatives.
2. **Quantization-aware training (QAT)** — Google Gemma 4 ships with official 2-bit and 4-bit QAT checkpoints that recover near-FP16 quality at 2x compression. This is the first time a frontier lab has shipped trained-to-be-quantized weights instead of post-training quant.
3. **MoE with very small active sets** — Qwen 3.5-235B (22B active) and Qwen 3.6-35B-A3B (3B active) make "thinking 70B-class on 16GB unified memory" a real workload.

## 2. The Comparison Matrix

All numbers are Q4_K_M quantized, GGUF, on llama.cpp unless noted. VRAM/RAM = approximate file size + KV cache headroom. "CPU tok/s" is a representative range across M-series Apple Silicon, recent Intel (i7-12700 / 14700K), and AMD Ryzen 7 (5700X-7800X3D) systems — see §5 for the methodology note.

| Model | Params | Active | License | Context | GGUF (Q4) | RAM needed | Best at | Source |
|---|---|---|---|---|---|---|---|---|
| **Gemma 4 E2B** | 5.1B (2.3B eff.) | 2.3B | Gemma | 128K | ~2 GB | 4 GB | Tiny / SBC / phone | [HF][onyx] |
| **Phi-4-mini** | 3.8B | 3.8B | MIT | 128K | ~2.5 GB | 4-8 GB | **CPU-only laptop** | [PQ][daily] |
| **SmolLM3-3B** | 3B | 3B | Apache 2.0 | 128K | ~2 GB | 4 GB | Edge / fully open data | [HF] |
| **Llama 3.2 3B** | 3B | 3B | Llama | 128K | ~2 GB | 3.5 GB | Balanced CPU small | [PQ] |
| **Gemma 4 E4B** | 8B (4B eff.) | 4B | Gemma | 128K | ~3.5 GB | 6-8 GB | Multimodal edge | [HF][onyx] |
| **Qwen 3 4B** | 4B | 4B | Apache 2.0 | 128K | ~3 GB | 6 GB | Quality at 4B | [daily][aim] |
| **Gemma 3 4B** | 4B | 4B | Gemma | 128K | ~3 GB | 6-8 GB | Multilingual 4B | [daily] |
| **Mistral 7B (v0.3)** | 7B | 7B | Apache 2.0 | 32K | ~4.5 GB | 8 GB | General small | [daily] |
| **Qwen 3 8B** | 8B | 8B | Apache 2.0 | 128K | ~5 GB | 8-10 GB | General 8B sweet spot | [daily] |
| **Llama 3.3 8B** | 8B | 8B | Llama | 128K | ~5 GB | 8-10 GB | Ecosystem/integrations | [meta-intel] |
| **Gemma 4 12B Unified** | 12B | 12B | Apache 2.0 | 256K | ~8 GB | 12-16 GB | **Laptop multimodal** | [google] |
| **Phi-4** | 14B | 14B | MIT | 16K | ~9 GB | 12 GB | Reasoning & code | [localaimaster] |
| **Mistral Small 3.1** | 24B | 24B | Apache 2.0 | 131K | ~14 GB | 20 GB | Instruction following | [onyx] |
| **Qwen 3 14B / 3.5 14B** | 14B | 14B | Apache 2.0 | 128K | ~9 GB | 14-16 GB | Balanced 14B | [ai-muninn] |
| **Gemma 3 27B** | 27B | 27B | Gemma | 128K | ~17 GB | 24 GB | Multilingual heavy | [onyx] |
| **Qwen 3.6-27B** | 27B | 27B | Apache 2.0 | 256K | ~14 GB (Q4) | 20-24 GB | Newer 27B refresh | [onyx] |
| **Gemma 4 26B-A4B** | 26B (4B act) | 4B | Apache 2.0 | 256K | ~16-18 GB | 22-28 GB | 70B-class at laptop RAM | [unsloth] |
| **Qwen 3.6-35B-A3B** | 35B (3B act) | 3B | Apache 2.0 | 256K | ~18 GB | 24-32 GB | Coding, MoE speed | [tech-insider] |
| **Qwen 3.5 32B** | 32B | 32B | Apache 2.0 | 128K | ~20 GB | 28-32 GB | Best dense 32B | [aim] |
| **DS-R1-Distill-Qwen-14B** | 14B | 14B | MIT | 128K | ~8 GB | 12 GB | Reasoning at 14B | [onyx] |
| **DS-R1-Distill-Llama-70B** | 70B | 70B | MIT | 128K | ~36 GB | 48-64 GB | 70B reasoning, big-RAM only | [onyx] |
| **Mistral Small 4** | 119B (6B act) | 6B | Apache 2.0 | 256K | ~32 GB (Q4) | 48 GB | Frontier at unified memory | [onyx][tech-insider] |
| **Llama 4 Scout** | 109B (17B act) | 17B | Llama | 10M | ~58 GB | 80 GB+ | Long-context research | [onyx] |

Key columns:
- **Active** for MoE models is the parameter count actually executed per token — this is what determines inference speed and memory bandwidth, not the total parameter count.
- **GGUF (Q4)** is the on-disk file size for the Q4_K_M quantization, which is the de-facto "good enough quality, half the size" default in 2026.
- **RAM needed** adds roughly 0.5-1.5 GB for KV cache at a default 4-8K context. Long contexts (32K+) push KV cache to multi-GB and dominate RAM usage at inference time.

## 3. The Five-Family Breakdown

### 3.1 Microsoft Phi-4 (and Phi-4-mini)

- **Phi-4 (14B, MIT)** — Best-in-class reasoning and code at the 14B tier. 84.8% MMLU, 82.6% HumanEval, **beat GPT-4o-mini on math reasoning** per the Microsoft technical report. Context is only 16K (smallest of the 14B tier), but quality is the leader. Fits a 12 GB laptop GPU comfortably; Q4_K_M lives in ~9 GB.
- **Phi-4-mini (3.8B, MIT)** — **The CPU-only default.** Needs only ~2.5 GB of RAM at Q4_K_M, runs at 30-50 tok/s on any modern laptop CPU per PromptQuorum, and at 9-12 tok/s on representative Ryzen/i7 systems. Instruction-following is materially better than Gemma 4 E2B at comparable size. **Recommended starting point if the target is "runs on a CPU laptop with no GPU at all."**

### 3.2 Google Gemma 4 (June 2026 release wave)

- **E2B / E4B** — Edge-first, multimodal (text + image + audio), Apache 2.0, fully open. E2B is the smallest viable general model. E4B is the new "multimodal on a phone" baseline.
- **12B Unified** — **The standout laptop model of 2026.** Encoder-free architecture (raw image patches and audio waveforms are projected straight into the LLM embedding space), Apache 2.0, 256K context, multimodal (text + image + audio), 77.2% MMLU Pro and 78.8% GPQA Diamond — within striking distance of the 26B MoE at less than half the RAM. Runs at 8-10 GB Q4 or 16 GB at 8-bit on a 16 GB-laptop.
- **26B-A4B** — MoE, only 4B active per token. 82.6% MMLU Pro at ~18 GB Q4. Reaches Gemma 3 27B-tier quality with a fraction of the active compute.
- **31B** — Flagship dense. 85.2% MMLU Pro. Needs 16-18 GB at Q4.
- The **Gemma 4 QAT** story (covered separately in the existing [[Research/gemma-4-qat|Gemma 4 QAT]] index) is what makes the smaller variants acceptable at 2-bit — the official QAT checkpoints recover quality that naive post-training quantization cannot.

### 3.3 Alibaba Qwen 3 / 3.5 / 3.6

- **Qwen 3 4B / 8B / 14B** — The "if unsure, pick Qwen" default family. Industry-leading coding, 100+ languages, Apache 2.0, long context (128K). The 14B variant is the recommended starting point on a 16 GB Mac per [[https://ai-muninn.com/en/blog/llm-101-how-to-choose-a-model|ai-muninn's brand guide]].
- **Qwen 3.5 32B / 235B-A22B** — 32B dense for the 32 GB tier; 235B with 22B active for unified-memory systems (M4 Max, Strix Halo). Qwen 3.5 32B runs at 25-30 tok/s on the right hardware — faster than most people read.
- **Qwen 3.6-27B / 3.6-35B-A3B** — The 2026 refresh. 3.6-35B-A3B is the "active-3B" MoE that ships 70B-class coding on modest hardware; only 3B active per token means CPU-side latency is dominated by 3B-class matrix multiplies.
- The Qwen family is the broadest 1B-to-trillion-parameter lineup in open weights, and the only one with credible coverage at every tier from 0.6B to 235B-MoE.

### 3.4 Mistral AI

- **Mistral 7B (v0.3)** — Apache 2.0, clean small-model choice for 8 GB laptops. ~6-7 GB at Q4.
- **Mistral Small 3.1 (24B)** — Apache 2.0, fast, strong instruction following, 131K context, ~14 GB Q4.
- **Mistral Small 4 (119B, 6B active)** — Frontier quality with 6B-active MoE — a "thinking 70B" on 48 GB unified memory. Apache 2.0, EU-data-residency friendly, 256K context, multimodal.
- Mistral's defining trait is **sliding window attention** (SWA) in the 22B-class models — memory does not scale linearly with sequence length, which is a real advantage for long-document work (legal, technical manuals).

### 3.5 Meta Llama 3.x and Llama 4

- **Llama 3.2 3B** — Smallest viable general model, ~2 GB Q4. Useful as a low-RAM baseline.
- **Llama 3.3 8B** — The "ecosystem default" — best tool/integration support, largest community, but slightly behind Phi-4 and Qwen 3 8B on raw benchmarks at the same size.
- **Llama 4 Scout (109B / 17B active)** — **10M token context** (the headline number), but 80 GB+ RAM requirement puts it out of reach for a laptop. Workstation-only.
- The Llama License is more restrictive than Apache 2.0 / MIT — the 700M-monthly-active-user clause in the Llama 4 license is a real adoption blocker for commercial products.

### 3.6 Honorable mentions

- **Hugging Face SmolLM3-3B** — Fully open (open data, open training code, open weights), Apache 2.0, 128K context, dual-mode reasoning. The "research / reproducibility" pick at 3B. Ships as a 2 GB int4 LiteRT-LM artifact for Android.
- **DeepSeek-R1 distill variants (14B / 32B / 70B)** — MIT, strong reasoning. R1-Distill-Qwen-14B is the best sub-12-GB reasoning model; R1-Distill-Llama-70B is the best sub-80-GB frontier reasoning model.
- **GPT-oss 20B / 120B** — OpenAI's open-weights release. Apache 2.0. 20B at 11 GB Q4 makes it competitive with Mistral Small 3.1 but with a more permissive license than Llama.

## 4. Decision Tree by Hardware Tier

### 4.1 Phone / edge / SBC / 4 GB RAM
- **Gemma 4 E2B** (`ollama pull gemma4:e2b`) — only ~2 GB RAM.
- **Phi-4-mini** at low precision — also viable, but Gemma 4 E2B is multimodal (text + image + audio) where Phi-4-mini is text-only.
- **SmolLM3-3B LiteRT-LM** — runs directly on Android via Google AI Edge Gallery.

### 4.2 8 GB laptop (CPU only or iGPU)
- **Best general: Qwen 3 8B or Llama 3.3 8B** at Q4 — ~5 GB, fits 8 GB with headroom.
- **Best small reasoner: Phi-4-mini** — best quality per GB, runs at 30-50 tok/s on CPU.
- **Best multilingual/edge multimodal: Gemma 4 E4B** — Apache 2.0, 4B active.
- **Note:** avoid anything 14B+ at this tier; it will swap or fail to load.

### 4.3 16 GB laptop (integrated GPU or entry dGPU)
- **Best overall: Gemma 4 12B Unified** at Q4_K_M — ~8-10 GB, fits 16 GB, multimodal, 256K context, Apache 2.0. The new default for this tier.
- **Best for code/reasoning: Phi-4 (14B)** at Q4 — ~9 GB, MIT.
- **Best for multilingual: Qwen 3 14B or Qwen 3.5 14B** at Q4.
- **Apple Silicon note:** MLX (Apple's framework) is 10-25% faster than llama.cpp/Ollama on the same M-series hardware. Prefer MLX on Mac.

### 4.4 32 GB laptop / Mac Studio M2-M4
- **Best general: Qwen 3 32B (3.5)** — 20 GB Q4, comfortable.
- **Best MoE: Qwen 3.6-35B-A3B** — 18 GB Q4, 3B active per token, very fast.
- **Best Apache 2.0 frontier: Gemma 4 26B-A4B** — 16-18 GB Q4.
- **Mistral Small 3.1 (24B)** at Q4 — ~14 GB, leaves headroom for long context.

### 4.5 48-64 GB unified memory (Mac Studio M2/M3/M4 Ultra, Strix Halo)
- **Mistral Small 4 (119B, 6B active)** — 32 GB Q4, frontier quality, Apache 2.0.
- **Qwen 3.5 235B-A22B** — 48 GB Q4, 22B active, near-frontier.
- **Llama 4 Scout** — 58 GB Q4, **10M context** for the long-document use case.
- On Strix Halo specifically, 12-15 tok/s on Llama 3.3 70B Q4 is achievable with a properly configured ROCm stack (community reports).

### 4.6 80 GB+ workstation
- Anything from DeepSeek-V3.2 (685B) down. Beyond "laptop CPU" scope but worth noting that the GGUF ecosystem now supports 1M+ token contexts with KV cache quantized to 4-bit, which makes these models tractable on a single 96 GB Mac Studio or dual-socket 192 GB Xeon.

## 5. The CPU vs Metal vs CUDA vs NPU Question

For pure-CPU inference, representative tok/s on **Phi-4-mini Q4_K_M (3.8B)** across hardware (community numbers, llama.cpp):

| Hardware | tok/s | Notes |
|---|---|---|
| Apple M1 (8 GB) | 18 | Near limit, swap pressure |
| Apple M1 (16 GB) | 22 | Comfortable |
| Apple M1 Pro | 38 | Good daily driver |
| Apple M1 Max | 42 | Overkill for 7B |
| Apple M2 (24 GB) | 28 | Noticeable bump over M1 |
| Apple M2 Max (32 GB) | 44 | Solid |
| Apple M3 Pro 12-core | 17.9 (CPU) / 21.1 (GPU) | GPU path only 18% faster |
| Apple M4 Max (64 GB) | 58 (Ollama) / 68 (MLX) | MLX wins |
| AMD Ryzen 7 7800X3D | 9.7 | DDR5 sweet spot |
| AMD Ryzen 9 7900 (DDR5-5400) | 13.45 | Fast RAM matters more than cores |
| Intel i7-12700 | 12 (Phi-4-mini) | AVX-512 enabled |
| Intel i7-14700K | 9.8 | Surprisingly mid-pack |
| AMD Ryzen 7 5700X | 9 | AVX2 only, no AVX-512 |
| Ryzen Z1 Extreme (25W, ROG Ally) | 5.3 | Power-constrained |

Key takeaways:
- **Memory bandwidth dominates.** DDR5-5400 vs DDR5-4800 on the same Ryzen 9 7900 lifts Phi-4-mini from 12.41 to 13.45 tok/s — a single-channel 8% gain in RAM speed = 8% gain in tokens/sec. This is the CPU-LLM bottleneck.
- **Apple Silicon wins CPU inference per watt** because unified memory is quad-channel LPDDR5X with very high bandwidth (~400 GB/s on M3 Max).
- **MLX > Ollama > llama.cpp > LM Studio on Mac** — MLX is ~10-25% faster than llama.cpp because it generates Metal kernels optimized for Apple's matrix unit rather than going through the general Metal backend.
- **GPU is 5-30x faster than CPU** for the same model — RTX 4090 does 7B Q4 at ~95 tok/s, an M4 Max CPU at 22 tok/s. The gap shrinks for very small models (1-3B) because the GPU has fixed launch overhead.
- **The NPU does not help LLM inference in 2026.** Ollama, llama.cpp, and MLX all use the GPU/Metal compute path, not the Neural Engine. The NPU is for image and audio models, not text.

## 6. Quantization: The Real Knob

Quality-vs-size trade-off for a typical 70B model, GGUF:

| Quant | Approx size | Quality impact | When to use |
|---|---|---|---|
| FP16 (no quant) | ~140 GB | Baseline | When you have the RAM |
| Q8_0 | ~70 GB | Negligible loss | Quality-critical offline work |
| Q6_K | ~54 GB | Minimal loss | |
| Q5_K_M | ~46 GB | Very slight loss | |
| **Q4_K_M** | **~40 GB** | **Best quality/size sweet spot** | **Default for self-hosting** |
| Q3_K_M | ~33 GB | Noticeable degradation | Only if you need to fit |
| Q2_K | ~25 GB | Significant degradation | Avoid unless desperate |

**Gemma 4 QAT shifts this curve.** The official QAT checkpoints at 2-bit (NVFP4 / Q2) recover most of the Q4-K_M quality because the model was trained to be quantized. This is the first time a frontier lab has shipped "Q2 that's actually good," and it's specifically what makes Gemma 4 26B-A4B at Q4 (16-18 GB) viable on a 24 GB laptop.

Practical rule: **Q4_K_M is the 2026 default for self-hosting.** Q8_0 only when you have the RAM and care about the last 1% of quality. Q2 only with QAT.

## 7. Runtime Stack

Three options cover almost every use case:

| Runtime | Best for | Pros | Cons |
|---|---|---|---|
| **Ollama** | Most users | Easiest install; model library; OpenAI-compatible API; one-line `ollama run` | Less granular control than llama.cpp |
| **llama.cpp** | Power users / cross-platform | Single-binary, Metal + CUDA + Vulkan + CPU; granular GPU-layer offload; reproducible build | CLI-only; manual model management |
| **MLX (Apple only)** | Mac users wanting max speed | 10-25% faster than llama.cpp on M-series; native Apple Silicon | Mac-only; smaller model library |
| **LM Studio** | GUI-first users | Desktop app, search, chat UI | Same backend as Ollama; less scriptable |
| **vLLM / SGLang** | Server-grade throughput | High concurrency, PagedAttention | GPU-first; not for CPU-only |

For pure CPU laptop inference, **Ollama + Qwen 3 8B (or Phi-4-mini) at Q4_K_M** is the lowest-friction starting point. The single command is `ollama run qwen3:8b`.

For Apple Silicon, **MLX + Gemma 4 12B** is the 2026 sweet spot — best quality-per-GB on 16 GB unified memory.

## 8. Key Cross-Cutting Themes

1. **Quality per GB is now the binding constraint, not absolute quality.** The frontier has plateaued (DeepSeek V3.2 / GLM-5.2 / Kimi K2.6 are all within 1-2% of each other on MMLU-Pro at the 700B+ tier). The differentiator is which model you can actually load and serve at 10+ tok/s on your hardware.
2. **MoE with low active-parameter counts (3-6B) is the structural enabler for laptop-class inference.** Qwen 3.6-35B-A3B (3B active), Gemma 4 26B-A4B (4B active), Mistral Small 4 (6B active) all deliver 70B-class quality at 18-32 GB Q4. This is the single most important trend in 2026 self-hosting.
3. **Quantization is solved at Q4, becoming solved at Q2 with QAT.** Naive Q4_K_M recovers most of FP16 quality for every model in the matrix above. QAT (Gemma 4) makes Q2-NVFP4 practical. Q3 and below are still risky without QAT.
4. **The "laptop" tier shifted from 7B to 14B-and-MoE.** A 16 GB laptop in 2026 runs Gemma 4 12B or Phi-4 comfortably — the same hardware that ran 7B in 2024. The MoE design is what makes this possible.
5. **License is now a first-class decision factor.** Apache 2.0 (Gemma 4, Qwen, Mistral, GPT-oss) and MIT (Phi-4, DeepSeek) dominate the laptop tier. The Llama License's 700M-MAU clause excludes many commercial uses; this is a real reason to prefer Qwen/Mistral/Phi over Llama at the same size.
6. **CPU-only is a real tier, not a fallback.** Phi-4-mini on a modern CPU delivers 12-30 tok/s — usable for chat, code completion, and short-form generation. The 3-4B tier on CPU is now the "always-on local assistant" tier.

## 9. Watch List / Open Questions

- **MLX-LM on M4 Ultra** has not yet been benchmarked at the Llama 4 Scout 10M context; expected late 2026.
- **AMD Strix Halo + ROCm + llama.cpp** is a major new path for affordable 70B-class laptop inference at $1500 — community benchmarks are still maturing, expect surprises.
- **Qwen 3.6 35B-A3B** active-parameter count is officially 3B but community reports suggest it behaves closer to 6-8B for tool use; needs a proper apples-to-apples test.
- **GPT-oss 20B** vs **Mistral Small 3.1 24B** at the same RAM tier — both Apache 2.0, both ~14 GB Q4, but benchmarks are sparse. Worth a focused test.

## 10. Concrete Recommendation (as of 2026-07-31)

If you have to pick one model today and your hardware is a typical 16 GB MacBook / Windows laptop:

- **CPU-only:** `ollama run phi4-mini` — 2.5 GB RAM, MIT, 128K context, best small reasoner.
- **With Metal/CUDA available:** `ollama run gemma4:12b` (or MLX variant) — 8-10 GB Q4, Apache 2.0, multimodal, 256K context. The best quality-per-GB on this hardware.
- **Want a coding model:** `ollama run qwen3:14b` — 9 GB Q4, Apache 2.0, 128K context, industry-leading coding at this size.

For a 32 GB Mac Studio: **Gemma 4 26B-A4B** (Apache 2.0, 18 GB Q4) or **Qwen 3 32B** (Apache 2.0, 20 GB Q4) — both at frontier-on-laptop quality.

## 11. Related Pages

- [[Entities/gemma-4-model-family|Gemma 4 Model Family]] — full entity page for the Gemini 4 series, including E2B/E4B/12B/26B-A4B/31B.
- [[Entities/qwen|Qwen]] — entity page for the Qwen model family (Qwen 2.5 / 3 / 3.5 / 3.6).
- [[Entities/mistral-ai|Mistral AI]] — entity page for the Mistral family.
- [[Research/gemma-4-qat|Gemma 4 QAT]] — separate research index on Quantization-Aware Training for Gemma 4 (Q2/Q4 quality recovery).
- [[Research/serverless-gpu-inference-providers|Serverless GPU Inference Providers]] — the cloud alternative for when local CPU/GPU is insufficient.

## 12. External Sources

Direct URLs (no Quartz Raw stubs created for this comparison — the research aggregates across 12+ primary sources rather than ingesting any single one in full):

- Hugging Face — Best Open Source LLM Models to Run Locally in 2026: https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally
- Google Blog — Introducing Gemma 4 12B: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/
- Google — gemma-4-12B model card: https://huggingface.co/google/gemma-4-12B
- Unsloth — Gemma 4 how to run locally: https://unsloth.ai/docs/models/gemma-4
- Hugging Face — SmolLM3 release: https://huggingface.co/blog/smollm3
- PromptQuorum — Best CPU-Only Local LLM 2026: https://www.promptquorum.com/local-llms/best-cpu-only-llm
- SitePoint — Definitive Guide to Local LLMs 2026: https://www.sitepoint.com/definitive-guide-local-llms-2026-privacy-tools-hardware/
- LocalAIMaster — Best Small Language Models 2026: https://localaimaster.com/blog/small-language-models-guide-2026
- LocalAIMaster — Apple Silicon buying guide: https://localaimaster.com/blog/apple-silicon-ai-buying-guide
- Onyx — Self-Hosted LLM Leaderboard 2026: https://onyx.app/self-hosted-llm-leaderboard
- Daily.dev — Best Local LLM Models to Run in 2026: https://daily.dev/blog/best-local-llm-models-run/
- Pinggy — Picking the Right Hardware to Run LLMs Locally in 2026: https://pinggy.io/amp/blog/best_hardware_for_self_hosting_local_llms/
- dev.to — Running Local LLMs, CPU vs GPU speed test: https://dev.to/maximsaplin/running-local-llms-cpu-vs-gpu-a-quick-speed-test-2cjn
- Meta-Intelligence — Phi-4 vs Gemma 3 vs Llama 3.3 enterprise edge AI: https://www.meta-intelligence.tech/en/insight-slm-enterprise
- Tech Insider — Llama 4 vs Qwen 3.5 vs Mistral 2026: https://tech-insider.org/llama-4-vs-qwen-vs-mistral-2026/
- ai-muninn — Gemma vs Llama vs Qwen vs Mistral brand guide: https://ai-muninn.com/en/blog/llm-101-how-to-choose-a-model
