---
title: Hy3 (Hunyuan Hy3)
details: Tencent's open-weight flagship MoE released July 6, 2026, with 295B total / 21B active parameters and 256K context.
tags:
  - research
created: 2026-07-31
updated: 2026-07-31
type: note
---
# Hy3 (Hunyuan Hy3)

**Developer:** Tencent (Hy Team)
**Released:** July 6, 2026 (final Hunyuan 3 model, after April 2026 preview)
**License:** Apache 2.0 (commercial-friendly)
**Model ID:** `opencode-go/hy3`

## Architecture

| Feature | Specification |
|---------|---------------|
| Total Parameters | 295B |
| Active Parameters | 21B per token |
| MTP Layer Parameters | 3.8B |
| Architecture | Mixture-of-Experts (MoE) |
| Context Window | 256K tokens |
| Thinking Modes | Hybrid fast-and-slow (controllable) |
| Modalities | Text (multimodal extensions in Hunyuan 3 family) |

## Key Features

- **Open-weight flagship from Tencent** -- first tier-1 Chinese lab to ship Apache 2.0 on a frontier-tier MoE
- **Replaces Hunyuan 2 and the April 2026 preview** -- "Hy3" and "Hunyuan 3" used interchangeably; there is no Hunyuan 4
- **Hybrid fast-and-slow thinking** -- controllable per request, like the GLM-5.2 / Kimi K3 pattern
- **High request count on Go** -- ~4,300 requests per 5h, ~21,500/month, among the highest budgets in the catalog
- **Apache 2.0** -- matches Mistral, Qwen, and GPT-oss in license friendliness; not the more restrictive Tencent License of the earlier Hunyuan 2.0
- **Caixin-reported** "free agent" feature at launch -- bundled tool-use capability in the Tencent ecosystem

## Pricing (OpenCode Go)

| Metric | Value |
|--------|-------|
| Input | $0.14 / 1M tokens |
| Output | $0.58 / 1M tokens |
| Cache Read | $0.035 / 1M tokens |
| Est. requests per 5h | 4,300 |
| Est. requests per month | 21,500 |

Pricing is the second-cheapest in the catalog (only DeepSeek V4 Flash and MiMo V2.5 are cheaper on output). Combined with the high request budget, this is a strong default for high-volume, lower-stakes coding work.

## Endpoint

Chat completions: `https://opencode.ai/zen/go/v1/chat/completions` (OpenAI-compatible)

## Best For

- High-volume coding work where cost-per-call is the deciding factor
- Workflows that benefit from a 256K context window with no tiered pricing
- Tasks where Apache 2.0 is a license requirement (commercial redistribution, on-prem fine-tuning, etc.)
- Hybrid fast/slow thinking use cases where controllable reasoning effort matters
- Drop-in for Hunyuan 2.0 (406B) users who want a smaller, cheaper, more permissively-licensed Tencent model
