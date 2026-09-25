---
title: "Language routing in decision models (laya:latest auto-router)"
details: "Pattern of selecting a language-specific backbone at request time: laya:latest inspects incoming text and routes English to laya:en, everything else to laya:multilingual, returning the routing decision in the response."
tags:
  - concept
  - llm
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/ollaya-library-laya-2026-09-26.md
---

# Language routing in decision models (laya:latest auto-router)

**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Ollaya's `laya:latest` is a **router tag**, not a model. When a request arrives, it inspects the input text and dispatches to the appropriate language-specific backbone — English to `laya:en` (ModernBERT-large), everything else to `laya:multilingual` (mmBERT-base, 100+ languages). Pulling `laya:latest` pulls both backbones. The response includes a `routing` block that records which backbone was chosen and why, so consumers can audit the dispatch.

## Core Content

### Router behavior

```
input: "I was charged twice for my subscription..."
       ↓
detect: English Latin text
       ↓
route: laya:en
       ↓
respond with routing metadata:
  { "router": "laya:latest", "model": "laya:en",
    "route": "english", "reason": "English Latin text" }
```

For Turkish or any non-English text, the router sends the request to `laya:multilingual` and the response carries `route: "non-english"` (or similar).

### Why split by language at the model level

- **ModernBERT-large (English)** is the higher-accuracy backbone for English text but is not multilingual.
- **mmBERT-base (multilingual)** is smaller (322M vs 421M) and trades some English accuracy for 100+ language coverage.
- Routing at the model level lets each backbone specialize; routing at the request level lets the system pick the right specialist per call.

### Cost and latency trade-off

On RTX 4090 fp16, a 5-question request takes 16.3 ms on `laya:en` and 9.1 ms on `laya:multilingual`. The router adds a tiny detection overhead (it must inspect the input text), but for any request of non-trivial size this overhead is in the noise.

### What's NOT routed

The router only picks the language-specific backbone. It does **not** decide between encoder (laya) and decoder (decider), or between laya and nli / gliclass. That is the consumer's choice via the `model` field in the request body.

## Key Insights

1. **Specialist backbones + cheap router beats one multilingual model** for the laya family — the English backbone can be ModernBERT-large and the multilingual backbone can be a smaller mmBERT-base, with each tuned for its language set.
2. **Routing decisions belong in the response**, not in the consumer's logs. The `routing` block in Ollaya's response is the audit trail.
3. **Pulling `laya:latest` pulls both targets** — a deliberate design choice that prevents silent dispatch to a missing backbone.

## Related Concepts

- [[Concepts/encoder-vs-decoder-decision-architectures]] — routing is orthogonal to the encoder/decoder split
- [[Concepts/decision-models-as-classifiers]] — what the router dispatches

## References

- Raw: [[Raw/ollaya-library-laya-2026-09-26]]
