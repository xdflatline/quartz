---
title: Hindsight - Building Agent Memory
detail: A comprehensive technical overview of the Hindsight memory architecture for AI agents.
tags: [research]
created: 2026-06-21
updated: 2026-06-21
type: article
---

# Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects

Hindsight is a novel memory architecture that treats agent memory as a structured, first-class substrate for reasoning, moving beyond simple RAG (Retrieval-Augmented Generation) pipelines. It enables agents to accumulate experience, maintain stable perspectives, and distinguish between objective facts and subjective beliefs.

---

## 1. Core Architecture: The Four-Network Model

Hindsight organizes memory into four distinct logical networks, each serving a specific epistemic role:

*   **World Network ($\mathcal{W}$):** Objective facts about the external environment (e.g., "Alice works at Google").
*   **Experience Network ($\mathcal{B}$):** First-person biographical information, actions, and recommendations.
*   **Opinion Network ($\mathcal{O}$):** Subjective judgments with confidence scores ($c \in [0,1]$) and timestamps.
*   **Observation Network ($\mathcal{S}$):** Preference-neutral, synthesized summaries of entities derived from $\mathcal{W}$ and $\mathcal{B}$.

---

## 2. Three Core Operations

The system governs information flow through three specialized operations:

1.  **Retain:** Converts raw conversational transcripts into structured narrative facts with temporal ranges, canonical entities, and graph links.
2.  **Recall:** A multi-strategy retrieval pipeline (semantic, keyword, graph, and temporal) that uses Reciprocal Rank Fusion (RRF) and neural cross-encoder reranking to surface relevant context within a specified token budget.
3.  **Reflect:** Uses a behavioral profile ($\Theta$) to generate preference-conditioned responses, form new opinions, and update existing ones via reinforcement.

---

## 3. Key Components

*   **TEMPR (Temporal Entity Memory Priming Retrieval):** Handles the *Retain* and *Recall* operations. It builds a temporal, entity-aware memory graph where edges represent temporal, semantic, entity, or causal relationships.
*   **CARA (Coherent Adaptive Reasoning Agents):** Handles the *Reflect* operation. It integrates disposition behavioral parameters (Skepticism, Literalism, Empathy) and a bias-strength parameter ($\beta$) to ensure the agent maintains a stable, consistent reasoning style.

---

## 4. Key Technical Details

### Memory Unit Structure
Each memory unit is stored as a self-contained node:
> $f=(u,b,t,v,\tau_s,\tau_e,\tau_m,\ell,c,x)$
*(Where $u$=ID, $b$=bank, $t$=text, $v$=vector, $\tau$=timestamps, $\ell$=type, $c$=confidence, $x$=metadata)*

### Entity Resolution Logic
The system maps mentions to canonical entities using a weighted similarity score:
> $\rho(m)=\operatorname*{arg\,max}_{e\in E}\left[\alpha\cdot\text{sim}_{\text{str}}(m,e)+\beta\cdot\text{sim}_{\text{co}}(m,e)+\gamma\cdot\text{sim}_{\text{temp}}(m,e)\right]$

### Opinion Reinforcement Rule
Opinions are not static; they evolve based on new evidence:
> $c^{\prime}=\begin{cases}\min(c+\alpha,1.0)&\\text{if Assess}(o,f)=\\text{reinforce}\\\\ \max(c-\alpha,0.0)&\\text{if Assess}(o,f)=\\text{weaken}\\\\ \max(c-2\\alpha,0.0)&\\text{if Assess}(o,f)=\\text{contradict}\\\\ c&\\text{if Assess}(o,f)=\\text{neutral}\\end{cases}$

---

## 5. Performance Highlights

Hindsight significantly outperforms full-context baselines and existing memory architectures on long-horizon benchmarks:

| Benchmark | Baseline (OSS-20B) | Hindsight (OSS-20B) | Hindsight (Gemini-3) |
| :--- | :--- | :--- | :--- |
| **LongMemEval** | 39.0% | 83.6% | **91.4%** |
| **LoCoMo** | 75.78% (Prior) | 83.18% | **89.61%** |

*   **Key Insight:** The memory architecture itself—specifically the structured graph and temporal awareness—is the primary driver of performance, rather than just the size of the underlying LLM.

---

## 6. Actionable Resources
*   **Codebase:** [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
*   **Benchmarks Viewer:** [hindsight-benchmarks.vercel.app](https://hindsight-benchmarks.vercel.app/)
*   **Design Principle:** The system emphasizes epistemic clarity (separating facts from beliefs) and preference consistency (stable reasoning styles across sessions).
