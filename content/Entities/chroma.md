---
title: "Chroma"
details: "AI company that builds the open-source Chroma vector database and produced the Context Rot research report (Hong, Troynikov, Huber; July 2026). Chroma's product focus is on retrieval for AI applications — embeddings, vector search, and the surrounding infrastructure."
tags:
  - entities
  - llm
  - rag
  - company
created: 2026-09-25
updated: 2026-09-25
type: entity
source: https://www.trychroma.com/research/context-rot
---

# Chroma

**Website:** <https://www.trychroma.com>
**GitHub:** <https://github.com/chroma-core/chroma>
**Research:** <https://www.trychroma.com/research/> (Context Rot; Context-1)

## Overview

Chroma is the company behind the open-source **ChromaDB** vector database and the **Chroma Research** publication series. The research publications to date:

- **Context Rot** (Hong, Troynikov, Huber; July 2026) — systematic evaluation of how frontier LLM performance degrades with input length across 18 models. ([report](https://www.trychroma.com/research/context-rot))
- **Context-1: Training a Self-Editing Search Agent** (Bashir, Hong, Jiang, Shi; March 2026) — 20B parameter agentic search model trained with SFT + CISPO RL that matches frontier LLMs on retrieval benchmarks at a fraction of the cost. Weights released under Apache 2.0. ([report](https://www.trychroma.com/research/context-1), [weights](https://huggingface.co/chromadb/context-1))

Both reports are open-source: code for Context Rot at [chroma-core/context-rot](https://github.com/chroma-core/context-rot) and the Context-1 data-gen pipeline at [chroma-core/context-1-data-gen](https://github.com/chroma-core/context-1-data-gen), encouraging replication.

## Why it matters for the wiki

Chroma's positioning is interesting: a **vector database company publishing foundational LLM evaluation and training research**. The motivation is presumably aligned with their business — if retrieval matters more as context grows (because retrieval is what helps avoid context rot in production), and if retrieval can be offloaded to a small purpose-trained model (Context-1), then Chroma's tools become more valuable. The research is rigorous and the methodology sets a standard for both long-context evaluation (Context Rot) and small-model agentic training (Context-1).

## Related Pages

- Research: [[Research/llm-context-rot-evaluation-2026]]
- Research: [[Research/chroma-context-1]]
- Raw source: [[Raw/chroma-context-rot-2026-07]]
- Raw source: [[Raw/chroma-context-1-2026-03]]