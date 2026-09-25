---
title: "Research Index: Ollaya decision-model ecosystem"
details: "Synthesis of Ollaya's four open decision-model families (laya, decider, nli, gliclass) — their architectures, accuracy, calibration, runtime parity, and the routing / fine-tuning story tying them together."
tags:
  - research
  - llm
created: 2026-09-26
updated: 2026-09-26
type: research
sources:
  - .Raw/ollaya-search-index-2026-09-26.md
  - .Raw/ollaya-library-laya-2026-09-26.md
  - .Raw/ollaya-library-decider-2026-09-26.md
  - .Raw/ollaya-library-nli-2026-09-26.md
  - .Raw/ollaya-library-gliclass-2026-09-26.md
---

# Research Index: Ollaya decision-model ecosystem

**Updated:** 2026-09-26
**Source:** Ollaya library pages — https://ollaya.dev/library/

---

## Overview

Ollaya (`https://ollaya.dev`) ships **four open-model families** that share one job: read an input state plus typed questions and return calibrated answers (`choice`, `score`, `noul`) in a single forward pass — never generating text. The families differ in backbone (encoder vs decoder), cost scaling (per option, per question), and zero-shot vs fine-tuned behavior. This index synthesizes what they have in common, where they diverge, and what the patterns teach about decision-model design.

## Concepts

### Decision-model pattern

- [[Concepts/decision-models-as-classifiers]] — the core pattern: state + typed questions → calibrated answers, never text generation
- [[Concepts/encoder-vs-decoder-decision-architectures]] — encoder (laya, nli, gliclass) vs decoder (decider) split
- [[Concepts/language-routing-in-decision-models]] — `laya:latest` as a router tag dispatching to language-specific backbones

### Quality dimensions

- [[Concepts/typed-decisions-benchmark-ollaya]] — Ollaya's 400-state evaluation suite
- [[Concepts/calibration-for-decision-models]] — ECE, temperature fitting, `CALIBRATION` Modelfile directive

### Runtime

- [[Concepts/onnx-decision-runtime-parity]] — sha256-pinned weights + Rust-runtime bit-exact parity

## Tools & Projects

### Decision-model families

- [[Entities/laya-decision-model]] — Convai Innovations' encoder family (ModernBERT-large / mmBERT-base). Includes the only fine-tuned typed-decisions variant in the catalog.
- [[Entities/decider-decision-model]] — Mapika's decoder family on Qwen3.5. Highest zero-shot accuracy at the 2B scale.
- [[Entities/nli-zero-shot-classifier]] — Moritz Laurer's zero-shot NLI (DeBERTa-v3-large + ModernBERT-large). Highest zero-shot encoder accuracy.
- [[Entities/gliclass-zero-shot-classifier]] — Knowledgator's single-sequence label scorer. Best when option count is large and per-option cost matters.

### Platform and authors

- [[Entities/ollaya]] — the local-first runtime that ties the four families together
- [[Entities/convai-innovations]] — laya author org
- [[Entities/mapika]] — decider author org
- [[Entities/moritz-laurer]] — nli author
- [[Entities/knowledgator]] — gliclass author org

## Raw Sources

- [[Raw/ollaya-search-index-2026-09-26]] — Ollaya `/search` results, four-model catalog snapshot
- [[Raw/ollaya-library-laya-2026-09-26]] — full laya library page
- [[Raw/ollaya-library-decider-2026-09-26]] — full decider library page
- [[Raw/ollaya-library-nli-2026-09-26]] — full nli library page
- [[Raw/ollaya-library-gliclass-2026-09-26]] — full gliclass library page

## Key Threads/Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [Ollaya /search](https://ollaya.dev/search) | Model catalog index | 2026-09-26 | 4 model families, capability filters |
| [Ollaya /library/laya](https://ollaya.dev/library/laya) | laya — encoder, fine-tuned + multilingual | 2026-09-26 | 4 tags, ONNX parity audit, calibration caveat |
| [Ollaya /library/decider](https://ollaya.dev/library/decider) | decider — decoder on Qwen3.5 | 2026-09-26 | 3 tags, option-letter logits, BF16→fp32 widening |
| [Ollaya /library/nli](https://ollaya.dev/library/nli) | nli — zero-shot NLI | 2026-09-26 | 3 tags, per-option sequence-pair cost, license caveat on DeBERTa |
| [Ollaya /library/gliclass](https://ollaya.dev/library/gliclass) | gliclass — single-sequence label scorer | 2026-09-26 | 1 backbone, noul-without-criteria weakness |

## Cross-Cutting Themes

### Architecture and cost

1. **Encoder is 10× faster, decoder is more accurate (without fine-tuning).** On identical 5-question requests at fp16 on RTX 4090, laya finishes in 8–16 ms; decider takes 155–190 ms. The decoder's advantage is zero-shot accuracy (0.591 vs the encoder families' 0.36–0.55 range) and broad pretraining knowledge.
2. **Fine-tuning an encoder closes the gap.** `laya:typed-decisions` (encoder, 421M, fine-tuned) reaches 0.766 on the typed-decisions benchmark — well above `decider:2b`'s 0.591. Fine-tuning is the high-leverage move; backbone size is secondary.
3. **Per-question cost is the right unit.** All four families cost roughly the same per question (single forward pass), but `nli` adds an N× cost for N options (sequence pairs) and `decider` adds an options × context cost. `gliclass` is the cheapest for many options, `laya` the cheapest for few.

### Quality dimensions

4. **Calibration is a separate axis from accuracy.** The catalog numbers emphasize accuracy; calibration is published separately as ECE. laya (English, after temperature fitting) reaches ECE 0.081 — roughly 3× better than Jev (0.246). For threshold-based workflows, calibration matters more than accuracy.
5. **The typed-decisions benchmark is rank-ordering, not ground truth.** Ollaya is explicit: "labels have low annotator agreement, so compare the numbers to each other rather than reading them as absolutes." Cross-family comparisons are valid; absolute scores are not.

### Reproducibility and distribution

6. **Bit-exact parity is achievable for ONNX-exported decision models.** Ollaya publishes a 2,383-question parity audit on laya (100% agreement with PyTorch fp32, max probability delta 1.1 × 10⁻⁴). The recipe — pinned weights, small ONNX graph, Rust runtime — is the same across all four families.
7. **Don't re-host weights.** Each model pulls its `model.safetensors` from the author's Hugging Face repo, pinned to a commit, verified by sha256. Ollaya ships only the 5–8 MB ONNX graph. License and provenance stay with the original author.

### Language coverage

8. **Multilingual support is concentrated in one family.** Only `laya:multilingual` (mmBERT-base) covers 100+ languages. `nli`, `gliclass`, and `decider` are English-first or English-only. The router tag `laya:latest` dispatches to the right backbone per request.

### Operational concerns

9. **`noul` questions without explicit `true` / `false` criteria are the most common footgun.** gliclass specifically warns about this — a yes/no question scored as a single label with a sigmoid can be confidently wrong. Use `nli` for `noul`, or always provide criteria for `noul`.
10. **Score criteria must be a list, not an object, for `decider`.** A small TypeSafe-API compatibility constraint, easy to hit. Other families accept both.

## Next Research Directions

- [ ] **Benchmark all four families on a held-out evaluation set** beyond Ollaya's 400-state typed-decisions suite — measure accuracy, ECE, and p50/p95 latency on identical hardware, end-to-end through Ollaya, with calibrated and uncalibrated configurations.
- [ ] **Test `CALIBRATION` directive end-to-end** — fit temperatures on a small labeled set (e.g. 200–500 examples), bake in via Modelfile, verify that ECE drops to ≤ 0.10 on the typed-decisions benchmark for nli and gliclass.
- [ ] **Compare encoder-decision-model fine-tuning vs decoder-decision-model fine-tuning** at matched parameter counts (e.g. fine-tune a ModernBERT-large vs fine-tune a Qwen3.5-0.8B on the same typed-decisions data) — Ollaya currently only publishes the encoder-fine-tuned result (`laya:typed-decisions`, 0.766); a decoder-fine-tuned baseline would clarify which architecture has more headroom.
- [ ] **Probe `noul`-without-criteria failure modes** across gliclass and the others — characterize the confidently-wrong rate as a function of label ambiguity, and produce a defensive wrapper that falls back to `nli` when criteria are missing.
- [ ] **Investigate the language router's dispatch accuracy** on mixed-language inputs (e.g. English technical terms inside a Turkish sentence) — `laya:latest` may misclassify these, with downstream consequences for accuracy.
- [ ] **Audit ONNX parity for `decider`** in the same style as the laya 2,383-question parity audit — the page asserts parity but does not publish the per-question count.
