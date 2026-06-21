---
title: Hindsight - Building Agent Memory
detail: A comprehensive technical overview of the Hindsight memory architecture for AI agents.
tags: [research]
created: 2026-06-21
updated: 2026-06-21
type: article
---

# Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects

This paper introduces **Hindsight**, a novel memory architecture that treats agent memory as a structured, first-class substrate for reasoning. Moving beyond stateless RAG (Retrieval-Augmented Generation), Hindsight enables agents to accumulate long-term experience, maintain stable behavioral perspectives, and distinguish between objective facts and subjective beliefs.

---

## 1. Abstract
State-of-the-art Large Language Models (LLMs) suffer from memory fragmentation and loss of consistency over long-term interactions. Existing RAG-based approaches treat memory as an unordered bag of chunks, failing to preserve the epistemic status of information (e.g., whether a piece of information is a proven fact or a subjective belief). Hindsight introduces a structured memory system consisting of four interconnected networks—World ($\mathcal{W}$), Experience ($\mathcal{B}$), Opinion ($\mathcal{O}$), and Observation ($\mathcal{S}$)—and three operations—Retain, Recall, and Reflect—to achieve state-of-the-art performance on long-horizon reasoning tasks.

---

## 2. Core Architecture: The Four-Network Model

Hindsight organizes memory into four distinct logical networks, each serving a specific epistemic role:

*   **World Network ($\mathcal{W}$):** Stores objective facts about the external environment (e.g., entity attributes, verified relationships).
*   **Experience Network ($\mathcal{B}$):** Captures first-person biographical information, agent-specific actions, and user-provided recommendations.
*   **Opinion Network ($\mathcal{O}$):** Tracks subjective judgments, preferences, and beliefs, maintained with explicit confidence scores ($c \in [0,1]$) and temporal metadata.
*   **Observation Network ($\mathcal{S}$):** A synthesis layer providing preference-neutral summaries of entities derived from the World and Experience networks to facilitate faster, high-level reasoning.

---

## 3. The Three Core Operations

The system governs information flow through three specialized operations:

1.  **Retain:** Converts raw conversational transcripts into structured narrative facts. This process normalizes temporal ranges, performs canonical entity resolution, and constructs a graph of temporal, semantic, entity, and causal relationships.
2.  **Recall:** A multi-strategy retrieval pipeline that executes semantic (vector), keyword (BM25), graph-based (spreading activation), and temporal (date-range filtering) searches in parallel. Results are merged via **Reciprocal Rank Fusion (RRF)** and refined by a neural cross-encoder reranker to optimize precision within the LLM's limited token budget.
3.  **Reflect:** Uses a **behavioral profile** ($\Theta$) to generate preference-conditioned responses. It integrates dispositional parameters—**Skepticism, Literalism, and Empathy**—and a bias-strength parameter ($\beta$) to ensure the agent maintains a consistent reasoning style regardless of the current context.

---

## 4. Key Components

### TEMPR (Temporal Entity Memory Priming Retrieval)
TEMPR manages the *Retain* and *Recall* operations. By building a temporal, entity-aware memory graph, it allows the agent to perform multi-hop reasoning and discover relationships that would be invisible to standard flat-vector embedding systems.

### CARA (Coherent Adaptive Reasoning Agents)
CARA manages the *Reflect* operation. By utilizing a persistent behavioral profile, CARA modulates its output to align with user expectations. Importantly, opinions in CARA are trajectories: they evolve over time as new information reinforces, weakens, or contradicts existing beliefs.

---

## 5. Technical Specifications

### Memory Unit Structure
Each memory unit is stored as a self-contained node:
> $f=(u,b,t,v,\tau_{s},\tau_{e},\tau_{m},\ell,c,x)$
*(Where $u$=ID, $b$=bank, $t$=text, $v$=vector, $\tau$=timestamps, $\ell$=type, $c$=confidence, $x$=metadata)*

### Entity Resolution Logic
Mentions are mapped to canonical entities using a weighted similarity score:
> $\rho(m)=\operatorname*{arg\,max}_{e\in E}\left[\alpha\cdot\text{sim}_{\text{str}}(m,e)+\beta\cdot\text{sim}_{\text{co}}(m,e)+\gamma\cdot\text{sim}_{\text{temp}}(m,e)\right]$

### Opinion Reinforcement Rule
Confidence scores update based on new evidence:
> $c^{\prime}=\begin{cases}\min(c+\alpha,1.0)&\\text{if Assess}(o,f)=\\text{reinforce}\\\\ \max(c-\alpha,0.0)&\\text{if Assess}(o,f)=\\text{weaken}\\\\ \max(c-2\\alpha,0.0)&\\text{if Assess}(o,f)=\\text{contradict}\\\\ c&\\text{if Assess}(o,f)=\\text{neutral}\\end{cases}$

---

## 6. Empirical Performance

Hindsight significantly outperforms full-context baselines and existing memory architectures on long-horizon benchmarks:

| Benchmark | Baseline (OSS-20B) | Hindsight (OSS-20B) | Hindsight (Gemini-3) |
| :--- | :--- | :--- | :--- |
| **LongMemEval** | 39.0% | 83.6% | **91.4%** |
| **LoCoMo** | 75.78% (Prior) | 83.18% | **89.61%** |

*   **Key Insight:** The memory architecture itself—specifically the structured graph and temporal awareness—is the primary driver of performance, rather than just the size of the underlying LLM. Hindsight with a 20B model outperforms full-context GPT-4o on long-horizon reasoning tasks.

---

## 7. Actionable Resources
*   **Codebase:** [github.com/vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
*   **Results Viewer:** [hindsight-benchmarks.vercel.app/](https://hindsight-benchmarks.vercel.app/)
*   **Design Principle:** The system emphasizes epistemic clarity—structurally separating objective evidence from subjective beliefs—which allows for better traceability and consistent agent behavior over long-term interactions.
