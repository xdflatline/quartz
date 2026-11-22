---
title: "Looped transformers and the local frontier: Inkling 2 Mini"
details: "Synthesis of Thinking Machines' Inkling 2 Mini release: how weight-shared middle layers buy serial reasoning without parameters, how native NVFP4 training and usage-based expert pruning fit a 26.4B-parameter MoE into ~20GB, where the model leads open-weights peers under 100B (DeepSWE v1.1 48.2%, Vals Index 46.5%) and where it does not, and what the accompanying monitorability experiments imply for oversight of architectures that think without writing it down."
tags:
  - research
  - llm
  - local-llm
  - benchmark
  - evaluation
created: 2026-11-22
updated: 2026-11-22
type: research
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Looped transformers and the local frontier: Inkling 2 Mini

**Source:** [[Raw/inkling-2-mini-thinking-machines-2026-11-20]] — Thinking Machines Lab, 2026-11-20
**Status:** Vendor release with vendor-run benchmarks and preliminary monitorability research. Not independently replicated.

## The claim under test

A small model can be made to reason better **without getting bigger** — by spending more compute per token inside the network rather than in generated text — and that same change can be shipped to a laptop.

Inkling 2 Mini is the demonstration: 26.4B total parameters, 3.4B active, ~20GB on disk, running offline on a 48GB MacBook Pro.

## Architecture: depth without parameters

- **24 layers in four blocks of six.** The middle two blocks execute **three times per token**; prelude and final block once. That yields **48 layer applications per token** from 24 stored layers.
- **Middle, not last.** A middle-12 loop needed **1.51–1.91×** the compute of a no-loop baseline to match its loss at step 2,000; a last-12 loop needed only **1.24–1.36×**. Looping the middle won on **27 of 28** evaluations.
- **Stability mechanisms.** Attention residuals let each layer learn its own mix of earlier block outputs, and each loop pass reads a "message" from the previous pass through a **learned gate that starts closed** — so training begins identical to a non-looping model and looping is opened gradually.
- **Cost trade.** The non-looping sibling was 7.5% cheaper to train but needed **140% more inference compute** to match the looped model on 512k-token agentic traces.

See [[Concepts/looped-transformer-architecture]].

## Efficiency: how 26.4B parameters fit in 20GB

Three choices compound:

1. **Expert pruning.** Started at 8-of-384 routing; mid-training kept the **128 most-used experts per layer** (a two-thirds cut), then **healed on 1T distilled tokens** from a larger internal model. See [[Concepts/expert-pruning-and-healing]].
2. **Native low precision.** Expert layers trained and served in **NVFP4** on every forward pass; the last four layers in **MXFP8**. Weights ship in the trained formats, so there is no post-training conversion loss. See [[Concepts/native-low-precision-training]].
3. **Sparse activation.** 3.4B active parameters (5.4B weight activations per token once looped reads are counted).

The resulting footprint runs on any Mac with ≥32GB RAM via Ollama, on DGX Spark, and offline on a MacBook Pro.

## Where it stands

The vendor's framing is precise: it leads **every open-weights model with less than 100B total parameters** on DeepSWE v1.1 and Vals Index v2.2, and is behind only Qwen3.8-27B on several other suites.

| Benchmark | Inkling 2 Mini |
|---|---|
| DeepSWE v1.1 | **48.2%** |
| SWE-bench Pro v2 Hard | **77.9%** |
| SWE-bench Verified (bash only) | **79.2%** |
| Terminal Bench v2.1 | 71.6% (Qwen3.8-27B 73.0%) |
| BrowseComp (compaction) | **79.0%** |
| DeepSearchQA (compaction) | **85.3%** |
| MCP Atlas | **82.7%** |
| AA Index v5.0 | 20.1 (tied Qwen3.8-27B) |
| Vals Index v2.2 | **46.5%** |
| HLE-Diamond | 15.2% (Qwen 15.3%) |
| AA-Omniscience | −8.6 (Qwen −6.4, Nemotron −2.9) |

The pattern is a **tool-using agentic model**: strong on coding, search and tool orchestration; average on closed-book knowledge; weak on multi-turn chat (MultiChallenge 50.0%) and many-constraint instructions (ComplexConstraints 33.4%).

## The oversight result

Looping increases the model's serial depth per token, so it can reason without writing the reasoning down. The accompanying variable-loop study measures what that costs oversight:

- **No-CoT capability rises.** Time horizon on Think Fast: 16 s at one pass → 37 s at three; flat afterwards; ten passes did not degrade a model trained to five.
- **Serial reasoning keeps scaling.** N-Hop Lookup accuracy improved out to ten loops.
- **CoT gets shorter, not murkier.** 3,703 → 1,661 reasoning tokens at 5 passes, with sentence length and dictionary-word fraction unchanged; uncertainty markers fell 9.7 → 3.6. The model backtracks less.
- **Controllability is low for everyone tested.** ≤0.1% instruction-following on CoT-Control-QA for Inkling 2 Mini, versus 0.3–1.3% for peers — too low to distinguish pass counts.
- **Agentic monitorability shows no loop trend.** With a strong monitor, almost all side tasks are caught. With a weak monitor restricted to tool calls, Inkling 2 Mini (helpful-only) had a 3.9% stealth rate, versus 1.3% when the monitor also saw text and thinking; across 1–5 passes there was no monotonic trend.

The authors' conclusion — more unverbalized capability, no meaningful monitorability reduction **at this scale** — is carefully scoped, and they flag larger models as the thing to watch. See [[Concepts/latent-reasoning-and-cot-monitorability]].

## Local economics

- **Intelligence per watt:** 0.703 on DGX Spark (MXFP8, low effort) versus 0.430 for Qwen3.6-35B-A3B, 0.159 for Gemma-4-26B-A4B, 0.036 for Qwen3.5-27B (Hazy Research / Scaling Intelligence, arXiv 2511.07885).
- **Multi-agent on one device:** twenty simulated residents, one model, one offline MacBook.
- **The trade:** decode bandwidth pays for the loops, and knowledge stays parameter-bound — the model compensates with tools.

See [[Concepts/local-agent-model-economics]].

## What generalizes

1. **Serial depth is a separate axis from parameter count.** Reasoning quality can be bought with repeated computation at inference instead of with weights at rest.
2. **Where you loop matters.** Middle layers carried the reasoning gain; the last layers did not.
3. **Efficiency is a stack, not a trick.** Pruning sets the parameter count, native low-bit training sets the bytes per parameter, and the target device sets both.
4. **Architecture changes the oversight contract.** Any technique that internalizes computation weakens CoT monitoring; that should be measured, not assumed away.
5. **Small models win on deployment constraints, not on generality.** Footprint, joules and offline operation are the axes where a 26B-total model competes with a 100B+ one.

## Boundaries of this source

- **Vendor-run benchmarks.** All results are from Thinking Machines; evaluation harnesses vary by model and the vendor says so in the chart notes.
- **"Best under 100B total parameters" is a scoped claim.** It excludes larger models and is reported per-benchmark, with Qwen3.8-27B winning several rows.
- **Theoretical decode speed.** The tokens-per-second axis is a ceiling at 614 GB/s with BF16 weights and batch size one — not a measured throughput, and not at the shipped precision.
- **Monitorability work is preliminary.** It uses a research variable-loop model trained mainly at 3 passes with limited exposure elsewhere; its RL was at 3 passes. Results at other depths likely understate what dedicated training would achieve.
- **The LinuxArena result uses a helpful-only fine-tune**, because the released model refuses many side tasks.
- **The Intelligence-per-Watt comparison used different precisions per model** (MXFP8, NVFP4, INT4) and one hardware configuration.
- **No ablation isolates** pruning, healing, looping and native 4-bit training from one another.

## Open questions

- Does middle-layer looping scale past 24 layers, or does the gain saturate with model size?
- Does monitorability hold at 100B+ parameters with the same loop depth, or is the current result a small-model artifact?
- How much of the benchmark position comes from looping versus the RL recipe (2.2T tokens, 2,000 steps, on-policy distillation)?
- Can the ~20GB footprint be reproduced without GB300-class training kernels, or is native NVFP4 a hardware-generation artifact?
- What is the actual energy per query under sustained multi-agent load, as opposed to the benchmark's single-query measure?

## Related Research

- [[Research/local-llm-cpu-inference-2026]] — hardware and runtime landscape for local inference
- [[Research/ollaya-decision-model-ecosystem]] — the small-purpose-model alternative to general small LLMs
- [[Research/decision-gated-agent-memory]] — another 2026-11 release about small, task-shaped models

## Related Concepts

- [[Concepts/looped-transformer-architecture]]
- [[Concepts/latent-reasoning-and-cot-monitorability]]
- [[Concepts/native-low-precision-training]]
- [[Concepts/expert-pruning-and-healing]]
- [[Concepts/local-agent-model-economics]]
- [[Concepts/quantization-aware-training-qat]]
- [[Concepts/llm-quantization-reference]]
- [[Concepts/local-llm-hardware-requirements]]
- [[Concepts/chain-of-thought-prompting]]

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Model: [[Entities/inkling-2-mini]] · Vendor: [[Entities/thinking-machines-lab]] · Platform: [[Entities/tinker]]
- Model card: https://thinkingmachines.ai/model-card/inkling-2-mini/
- Weights: https://huggingface.co/thinkingmachines/Inkling-2-Mini
- Intelligence per Watt: https://arxiv.org/abs/2511.07885
