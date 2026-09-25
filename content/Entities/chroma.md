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
**Research:** <https://www.trychroma.com/research/context-rot>

## Overview

Chroma is the company behind the open-source **ChromaDB** vector database and the **Chroma Research** publication series. The July 2026 Context Rot report is their flagship technical publication to date — a systematic evaluation of how frontier LLM performance degrades with input length across 18 models.

The Context Rot report is open-source (code at [chroma-core/context-rot](https://github.com/chroma-core/context-rot)) and the dataset of cleaned needles and distractors is published on Google Drive, encouraging replication.

## Why it matters for the wiki

Chroma's positioning is interesting: a **vector database company publishing foundational LLM evaluation research**. The motivation is presumably aligned with their business — if retrieval matters more as context grows (because retrieval is what helps avoid context rot in production), then Chroma's tools become more valuable. The research is rigorous and the methodology (controlled complexity, multi-model coverage, four governing factors) sets a standard for long-context evaluation that other researchers should follow.

## Related Pages

- Research: [[Research/llm-context-rot-evaluation-2026]]
- Raw source: [[Raw/chroma-context-rot-2026-07]]