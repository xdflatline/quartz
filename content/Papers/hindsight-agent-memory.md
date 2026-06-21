---
title: Hindsight - Building Agent Memory
detail: A novel memory architecture for AI agents that moves beyond stateless RAG.
tags: [research]
created: 2026-06-21
updated: 2026-06-21
type: article
---

# Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects

**Hindsight** is a novel memory architecture for AI agents that moves beyond stateless RAG (Retrieval-Augmented Generation) by treating memory as a structured, first-class substrate for reasoning. It enables agents to maintain long-term consistency, distinguish between facts and beliefs, and adapt their reasoning style over time.

---

## 1. Core Architecture: The Four-Network Model
Hindsight organizes memory into four distinct logical networks, each serving a specific epistemic role:

*   **World Network ($\mathcal{W}$):** Objective facts about the external environment (e.g., "Alice works at Google").
*   **Experience Network ($\mathcal{B}$):** First-person biographical information, actions, and recommendations.
*   **Opinion Network ($\mathcal{O}$):** Subjective judgments with confidence scores ($c \in [0,1]$) and timestamps.
*   **Observation Network ($\mathcal{S}$):** Preference-neutral, synthesized summaries of entities derived from $\mathcal{W}$ and $\mathcal{B}$.

---

## 2. The Three Core Operations
The system governs information flow through three specialized operations:

### Retain
Converts raw conversational transcripts into structured narrative facts.
*   **Process:** Uses LLM-based extraction to identify narrative facts, normalize temporal ranges, resolve entities, and construct graph links (temporal, semantic, entity, causal).
*   **Chunking:** Prefers "narrative extraction" (comprehensive, multi-turn summaries) over fragmented sentence-level storage to preserve context.

### Recall
An agent-optimized retrieval pipeline that balances coverage and token budgets.
*   **Four-Way Parallel Retrieval:** Executes semantic (vector), keyword (BM25), graph (spreading activation), and temporal (date-range filtering) searches simultaneously.
*   **Fusion:** Uses **Reciprocal Rank Fusion (RRF)** to merge results, followed by a **neural cross-encoder reranker** for precision.
*   **Interface:** Allows callers to specify a token budget ($k$), ensuring the retrieved context fits the downstream LLM's window.

### Reflect
Generates preference-conditioned responses and updates beliefs.
*   **Behavioral Profiles:** Uses disposition parameters (**Skepticism, Literalism, Empathy**) and a **Bias-strength ($\beta$)** parameter to shape the agent's reasoning style.
*   **Opinion Reinforcement:** When new facts are retained, the system assesses their relationship to existing opinions (reinforce, weaken, contradict, neutral) and updates confidence scores accordingly.

---

## 3. Key Technical Insights & Snippets

### Memory Unit Structure
Each memory unit is stored as a self-contained tuple:
```text
f = (u, b, t, v, τs, τe, τm, ℓ, c, x)
```
*(u: ID, b: bank, t: text, v: vector, τ: temporal metadata, ℓ: type, c: confidence, x: metadata)*

### Entity Resolution Formula
The system maps mentions to canonical entities using a weighted similarity score:
$$\rho(m) = \operatorname*{arg\,max}_{e \in E} \left[\alpha \cdot \text{sim}_{\text{str}}(m,e) + \beta \cdot \text{sim}_{\text{co}}(m,e) + \gamma \cdot \text{sim}_{\text{temp}}(m,e)\right]$$

### Opinion Reinforcement Logic
Opinions are not static; they evolve based on new evidence:
```text
c' = min(c + α, 1.0)  # if reinforce
c' = max(c - α, 0.0)  # if weaken
c' = max(c - 2α, 0.0) # if contradict
```

---

## 4. Empirical Performance

| Benchmark | Baseline (OSS-20B) | Hindsight (OSS-20B) | Hindsight (Gemini-3) |
| :--- | :--- | :--- | :--- |
| **LongMemEval** | 39.0% | 83.6% | 91.4% |
| **LoCoMo** | 75.78% (Prior) | 83.18% | 89.61% |

*   **Key Finding:** The memory architecture itself is the primary driver of performance. Even with a smaller 20B model, Hindsight outperforms full-context GPT-4o on LongMemEval.
*   **Temporal/Multi-session Gains:** Hindsight improved multi-session reasoning accuracy from 21.1% to 79.7% (OSS-20B) compared to the full-context baseline.

---

## 5. Actionable Resources
*   **Codebase:** [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
*   **Interactive Viewer:** [hindsight-benchmarks.vercel.app](https://hindsight-benchmarks.vercel.app/)
*   **Design Philosophy:** The authors emphasize **epistemic clarity** (separating facts from beliefs) and **preference consistency** (stable reasoning styles across sessions) as the primary requirements for next-generation AI agents.
