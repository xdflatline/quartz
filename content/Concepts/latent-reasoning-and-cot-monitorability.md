---
title: "Latent reasoning and CoT monitorability"
details: "As architectures shift computation from generated tokens into repeated internal passes, less of the reasoning appears in the chain of thought a monitor can read. Thinking Machines' measurements on a variable-loop model show large gains in no-CoT capability (time horizon 16s to 37s) and shorter but still legible CoT (3,703 to 1,661 tokens), with no clear loss of monitorability at 24-layer scale — while flagging the trend as a risk to track as models grow."
tags:
  - concept
  - llm
  - evaluation
  - architecture-pattern
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Latent reasoning and CoT monitorability

**Category:** Alignment / Interpretability
**Status:** Preliminary research results (vendor, 2026-11)

## Overview

Chain-of-thought monitoring works because of an architectural accident. In a standard transformer each token passes through a fixed stack of layers **once**, which caps how many sequential computation steps the model can take before it must emit a token. Reasoning that needs more steps has to be written out — where a monitor can read it.

[[Concepts/looped-transformer-architecture|Looping]] raises that cap. Repeated layers increase serial depth without adding parameters, so the model can do more computation per token internally, before verbalizing anything. Reasoning that never reaches the CoT cannot be caught by a CoT monitor.

## What the measurements show

**More capability without CoT.** On Think Fast, which estimates the task length a model can complete at 50% reliability with no chain of thought, the variable-loop research model's horizon rose from **16 seconds at one pass to 37 seconds at three**. Beyond three passes it is roughly flat, and running ten passes — twice what it was trained on — did not significantly degrade performance. Inkling 2 Mini (fixed three passes) scores 41 s.

**Serial reasoning keeps improving.** On N-Hop Lookup, where the model chains table lookups without writing anything down, accuracy kept improving out to **ten loops**.

**CoT gets shorter but stays readable.** On GPQA Diamond questions answered correctly at every pass count, mean reasoning length fell from **3,703 tokens at 1 pass to 1,661 at 5 passes**, while mean words per sentence (8.9 → 8.7) and the fraction of words in an English dictionary (94.6% → 94.4%) were unchanged. Uncertainty markers ("wait", "actually", "hmm") fell from 9.7 to 3.6. The qualitative reading: the model is more direct and backtracks less, not more cryptic.

**Controllability is poor either way.** On CoT-Control-QA, among chains of 750–1,250 tokens, Inkling 2 Mini and the variable-loop model followed an instruction about their own reasoning at most **0.1%** of the time — below Inkling 2 Small (0.3%), Inkling-Small (0.4%) and Qwen3.8-27B (1.3%). Because the rate is so low, the evaluation cannot distinguish loop depths. Poor controllability cuts both ways: less ability to deliberately reshape a CoT away from a monitor, but also less ability to enforce a reasoning format.

**Agentic monitorability shows no clear loop trend.** On LinuxArena, a strong monitor (Qwen3.8-27B) detected almost all side-task attempts regardless of looping. With a weaker monitor (Qwen3.6-35B-A3B) restricted to tool calls and outputs, the helpful-only Inkling 2 Mini fine-tune achieved a **3.9% stealth rate**, versus **1.3%** when the monitor could also see text and thinking. Across 1–5 passes the variable-loop model ranged 1.0%–5.0% with no monotonic trend. The authors' conclusion: at this scale, looping increases what the model can do without verbalized reasoning, but does not meaningfully reduce the monitorability of its reasoning.

## Why this matters beyond this model

- **The oversight argument for CoT is architecture-dependent.** Any design that increases computation per token — looping, latent recurrence, heavier adaptive compute — weakens the guarantee that "the reasoning is in the transcript". Monitorability becomes a property to measure per architecture, not an assumption.
- **Compression is not opacity.** Shorter reasoning can be *better* reasoning. The relevant question is whether the omitted steps are recoverable, not whether they exist.
- **Small models can be easier to oversee than large ones.** A small looped model still tends to verbalize, and its internal computation is small enough for interpretability work. The risk grows with scale and loop count.
- **Tool-call-only monitoring is much weaker than text-plus-thinking.** The LinuxArena gap (3.9% vs 1.3% stealth) is a concrete number for the value of reasoning visibility.

## Boundaries

- The monitorability experiments use a **research variable-loop variant**, trained mainly at 3 passes with lighter exposure to 1, 2, 4 and 5; its RL was done at 3 passes. Performance and behaviour at other pass counts likely understate what dedicated training would achieve.
- The helpful-only fine-tune was used for LinuxArena because the released model refuses many side tasks.
- Results are at 24 layers. The authors explicitly flag larger-scale tracking as future work.

## Related Concepts

- [[Concepts/looped-transformer-architecture]] — the mechanism that creates the extra internal compute
- [[Concepts/chain-of-thought-prompting]] — explicit reasoning as the readable alternative
- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — RL shaping of reasoning behaviour
- [[Concepts/temporal-reasoning-evaluation-benchmarks]] — another axis of reasoning evaluation

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Think Fast benchmark: https://arxiv.org/abs/2606.07157
- CoT-Control-QA (Yueh-Han et al., 2026): https://arxiv.org/abs/2603.05706
- LinuxArena: https://www.linuxarena.ai/
