---
title: Hindsight - Building Agent Memory
detail: A comprehensive technical overview of the Hindsight memory architecture for AI agents.
tags: [research]
created: 2026-06-21
updated: 2026-06-21
type: article
---

# Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects

**Hindsight** is a novel memory architecture that treats agent memory as a structured, first-class substrate for reasoning, moving beyond simple RAG (Retrieval-Augmented Generation) pipelines. It enables agents to accumulate experience, maintain consistent behavioral profiles, and evolve beliefs over time.

---

## 1. Core Architecture: The Four-Network Model
Hindsight organizes memory into four distinct logical networks, each serving a specific epistemic role:

*   **World Network ($\mathcal{W}$):** Objective facts about the external environment (e.g., "Alice works at Google").
*   **Experience Network ($\mathcal{B}$):** First-person biographical information, actions, and recommendations.
*   **Opinion Network ($\mathcal{O}$):** Subjective judgments with confidence scores ($c \in [0,1]$) and timestamps.
*   **Observation Network ($\mathcal{S}$):** Preference-neutral, synthesized entity profiles derived from $\mathcal{W}$ and $\mathcal{B}$.

---

## 2. Three Core Operations
The system governs information flow through three specialized operations:

1.  **Retain:** Ingests raw transcripts, extracts narrative facts, resolves entities, and updates the memory graph. It includes an **opinion reinforcement mechanism** that adjusts confidence scores based on new evidence.
2.  **Recall:** A multi-strategy retrieval pipeline that combines semantic vector search, BM25 keyword search, graph traversal (spreading activation), and temporal filtering. It uses **Reciprocal Rank Fusion (RRF)** and a neural cross-encoder for precision.
3.  **Reflect:** Uses a **behavioral profile** ($\Theta$) to generate responses. It integrates disposition parameters—**Skepticism, Literalism, and Empathy**—to ensure the agent maintains a stable, consistent reasoning style.

---

## 3. Key Technical Insights

### Memory Unit Structure
Each memory unit is stored as a self-contained node:
```text
f = (u, b, t, v, τs, τe, τm, ℓ, c, x)
```
*   *u*: Unique ID | *b*: Bank ID | *t*: Narrative text | *v*: Embedding | *τ*: Temporal metadata | *ℓ*: Fact type | *c*: Confidence | *x*: Metadata.

### Entity Resolution & Linking
Hindsight uses a weighted similarity function to map mentions to canonical entities, creating a graph where edges represent **temporal, semantic, entity, or causal** relationships. This allows for multi-hop discovery of information that simple vector search would miss.

### Preference-Conditioned Reasoning
CARA (Coherent Adaptive Reasoning Agents) uses a behavioral profile to modulate prompts.
*   **Bias Strength ($\beta$):** Controls how strongly the behavioral profile shapes the output.
*   **Opinion Evolution:** Opinions are not static; they are trajectories. Contradictory evidence weakens confidence, while supporting evidence reinforces it.

---

## 4. Empirical Performance

| Benchmark | Baseline (OSS-20B) | Hindsight (OSS-20B) | Hindsight (Gemini-3) |
| :--- | :--- | :--- | :--- |
| **LongMemEval** | 39.0% | 83.6% | **91.4%** |
| **LoCoMo** | 75.78% (Prior) | 83.18% | **89.61%** |

*   **Key Finding:** The memory architecture itself is the primary driver of performance, not just model size. Hindsight with a 20B model outperformed full-context GPT-4o on LongMemEval.
*   **Temporal/Multi-session Gains:** Multi-session reasoning improved from 21.1% to 79.7% (OSS-20B), demonstrating the effectiveness of the graph-based, time-aware retrieval.

---

## 5. Actionable Resources
*   **Codebase:** [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
*   **Benchmark Viewer:** [hindsight-benchmarks.vercel.app/](https://hindsight-benchmarks.vercel.app/)
*   **Implementation Note:** The system uses Pydantic models for structured output, ensuring that extracted facts and opinions are reliably parsed for the memory bank.

> "Hindsight treats agent memory as a structured, first-class substrate for reasoning... separating evidence from synthesized summaries and beliefs."
