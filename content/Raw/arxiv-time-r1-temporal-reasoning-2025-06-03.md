---
title: "Time-R1: Towards Comprehensive Temporal Reasoning in LLMs"
details: "Liu, Han, Yu, Li, You (UIUC / Siebel School, arXiv:2505.13508v2, submitted 2025-05-16, v2 2025-06-03). Introduces Time-R1, a 3B-parameter LLM trained via a three-stage reinforcement-learning curriculum (comprehension → future event prediction → creative scenario generation, with the third stage done by inference only) on a dynamic, rule-based reward system using GRPO. The model matches or exceeds DeepSeek-R1-671B on future event prediction (Stage 2 avg score 0.7780 vs 0.7503) and on creative future scenario generation (Stage 3 AvgMaxSim 48.90% vs DeepSeek-V3 48.81%), while being 200x smaller. Releases Time-Bench (200K+ news-derived temporal reasoning examples) and the model checkpoints. CC BY 4.0."
tags:
  - paper
source: "https://arxiv.org/abs/2505.13508v2"
authors:
  - "Zijia Liu"
  - "Peixuan Han"
  - "Haofei Yu"
  - "Haoru Li"
  - "Jiaxuan You"
venue: "arXiv:2505.13508v2 [cs.CL], 2025-06-03"
created: 2026-09-14
updated: 2026-09-14
type: raw
---

# Time-R1: Towards Comprehensive Temporal Reasoning in LLMs

**Authors:** Zijia Liu, Peixuan Han, Haofei Yu, Haoru Li, Jiaxuan You (Siebel School of Computing and Data Science, University of Illinois at Urbana-Champaign)
**arXiv:** [2505.13508v2](https://arxiv.org/abs/2505.13508v2) [cs.CL] · v1 2025-05-16 · v2 2025-06-03
**License:** CC BY 4.0
**Code/data/models:** [github.com/ulab-uiuc/Time-R1](https://github.com/ulab-uiuc/Time-R1) · [Hugging Face collection](https://huggingface.co/collections/ulab-ai/time-r1-682626aea47cb2b876285a16)

---

## Abstract

> Large Language Models (LLMs) demonstrate impressive capabilities but lack robust temporal intelligence, struggling to integrate reasoning about the past with predictions and plausible generations of the future. Meanwhile, existing methods typically target isolated temporal skills, such as question answering about past events or basic forecasting, and exhibit poor generalization, particularly when dealing with events beyond their knowledge cutoff or requiring creative foresight. To address these limitations, we introduce Time-R1, the first framework to endow a moderate-sized (3B-parameter) LLM with comprehensive temporal abilities: understanding, prediction, and creative generation. Our approach features a novel three-stage development path; the first two constitute a reinforcement learning (RL) curriculum driven by a meticulously designed dynamic rule-based reward system. This framework progressively builds (1) foundational temporal understanding and logical event-time mappings from historical data, (2) future event prediction skills for events beyond its knowledge cutoff, and finally (3) enables remarkable generalization to creative future scenario generation without any fine-tuning. Strikingly, experiments demonstrate that Time-R1 outperforms models over 200 times larger, including the state-of-the-art 671B DeepSeek-R1, on highly challenging future event prediction and creative scenario generation benchmarks. This work provides strong evidence that thoughtfully engineered, progressive RL fine-tuning allows smaller, efficient models to achieve superior temporal performance, offering a practical and scalable path towards truly time-aware AI. To foster further research, we also release Time-Bench, a large-scale multi-task temporal reasoning dataset derived from 10 years of news data, and our series of Time-R1 checkpoints.

## 1. Introduction

LLMs have achieved remarkable success across language understanding, generation, and complex reasoning tasks, but a persistent shortcoming in even the most advanced LLMs is their temporal reasoning ability. This encompasses several key capacities: accurately interpreting temporal relationships within their existing knowledge base (inferring event times, time differences, event order, completing temporal entities), predicting the timing of future events based on learned patterns, and creatively generating plausible future events anchored in time.

Studies show most LLMs struggle to update or contextualize knowledge under time constraints; even frontier models have been observed to perform worse than some smaller models in tasks requiring integration of new temporal information. The weakness stems from multiple factors:

- **Architectural limitations** — lack of explicit module representation of time
- **Static training corpora** — inevitably become outdated
- **Non-chronological training** — temporal information across different periods is processed concurrently rather than sequentially, hindering development of robust logical mappings between events and their times

While existing research aims to enhance temporal reasoning (Zhao et al. aligned LLM knowledge to target times; Kim et al. improved temporal consistency; Yuan et al. focused on future event prediction), these efforts typically target isolated skills. They fall short of endowing LLMs with **unified, comprehensive temporal intelligence** spanning past understanding, future prediction, and creative, time-anchored generation — especially for events beyond knowledge cutoffs.

### The Time-R1 framework

The paper equips a single 3B-parameter model with comprehensive temporal reasoning through multi-stage RL, building on Qwen2.5-3B-Instruct and showing it can surpass models over 200× larger (e.g., DeepSeek-R1 at 671B) on challenging temporal prediction and generation tasks.

**Three-stage framework:**

1. **Stage 1 — Comprehension:** RL fine-tune on pre-cutoff data across four fundamental temporal subtasks — *timestamp inference*, *time-difference estimation*, *event ordering*, *masked time entity completion* — to develop logical mappings between events and their times.
2. **Stage 2 — Prediction:** Train on post-cutoff data to predict events occurring after the model's knowledge cutoff, teaching it to extrapolate trends and anticipate future outcomes.
3. **Stage 3 — Generation:** Direct inference-only generation of logical future scenarios, leveraging the capabilities obtained from stages 1–2. **No additional fine-tuning.**

### Key contributions

1. **Unified temporal reasoning in one model:** first LLM with holistic temporal reasoning spanning logic, prediction, and generation.
2. **Small model, big performance:** a 3B model matches/exceeds hundreds-of-billions-parameter models on temporal prediction and generation.
3. **Fast adaptability and cost efficiency:** temporal knowledge can be refreshed cost-effectively; 3B can be quickly fine-tuned on new data, infeasible for hundreds-of-billions models (millions of dollars per fine-tune).
4. **Community resources:** Time-Bench dataset (>200K examples with explicit temporal annotations covering timestamp inference, time-gap estimation, event ordering, temporal entity completion); Time-R1 model checkpoints.

## 2. Related Work

**Temporal reasoning in LLMs.** LLMs struggle significantly with temporal reasoning — understanding time and event interrelations. Recent studies increasingly target deficiencies, often focusing on specific facets: improving temporal accuracy by aligning LLM knowledge with target time (Zhao et al.); better integrating temporal information into model representations; leveraging external knowledge sources or structured representations like temporal graphs. LLMs exhibit particularly poor generalization when reasoning about the future, especially for events beyond their knowledge cutoff or tasks requiring creative foresight. Robust methods for direct future event prediction or creative scenario generation remain scarce.

**Reinforcement learning in LLMs.** RL has attracted attention for scalability and generalization. Building on PPO, RLHF became standard for aligning LLMs. Recent advances simplify or improve this: Direct Preference Optimization (DPO) and Simple Preference Optimization (SimPO) replace the conventional RL loop with direct optimization of preference-based rewards. Group Regularized Policy Optimization (GRPO) introduces a group-based reward formulation in place of a single critic, achieving more stable training and better generalization. RLOO (REINFORCE-Leave-One-Out) refines LLM policies with reduced variance and cost. These have yielded SOTA on complex reasoning tasks including math, search/retrieval, and code generation. However, the application of RL to temporally-grounded reasoning remains underexplored.

## 3. Method

### 3.1 RL fine-tuning for temporal reasoning

Core process: LLM policy interacts with a rule-based environment. Given prompt $x$, the LLM (parameterized by $\theta$) generates output sequence $y$ autoregressively. All tasks use a structured generation template:

> *"You are a helpful assistant. You first think about the reasoning process in your mind and then provide the user with the answer."*

Outputs use `<think>…</think>` tags for reasoning and `<answer>…</answer>` tags for the final answer. The full sequence (thought + answer) is evaluated by the environment.

**Policy optimization using GRPO.** A key challenge in RL fine-tuning is the high variance of policy gradient estimates. GRPO addresses this by calculating the advantage of a generated response *relative to other responses sampled for the same prompt*, providing a more stable learning signal without requiring an auxiliary value function.

For prompt $x$, sample $K$ responses $\{y_k\}_{k=1}^K$ using reference policy $\pi_{\text{ref}}$ (typically the policy before the update step). After computing reward $R(x, y_k)$ for each, the group-normalized advantage is:

$$\hat{A}(x, y_k) = R(x, y_k) - b(x), \quad \text{where} \quad b(x) = \frac{1}{K} \sum_{j=1}^K R(x, y_j)$$

Probability ratio: $r_k(\theta) = \pi_\theta(y_k \mid x) / \pi_{\text{ref}}(y_k \mid x)$. Per-sample clipped objective (PPO-style):

$$L_k^{\text{CLIP}}(\theta) = \min\left(r_k(\theta) \hat{A}(x, y_k), \, \text{clip}(r_k(\theta), 1-\epsilon, 1+\epsilon) \hat{A}(x, y_k)\right)$$

Overall objective balances expected clipped advantage with KL-divergence penalty against the reference policy:

$$\max_\theta J_{\text{GRPO}}(\theta) = \mathbb{E}_{x \sim \mathcal{D}, \{y_k\} \sim \pi_{\text{ref}}}\left[\frac{1}{K} \sum_{k=1}^K L_k^{\text{CLIP}}(\theta)\right] - \beta \, \mathbb{E}_{x \sim \mathcal{D}} \mathbb{D}_{\text{KL}}\left[\pi_\theta(\cdot \mid x) \, \| \, \pi_{\text{ref}}(\cdot \mid x)\right]$$

with KL coefficient $\beta$, training set $\mathcal{D}$ (training-dataset union), and reference policy $\pi_{\text{ref}}$ (initialized from Qwen2.5-3B-Instruct for Stage 1, frozen stage-specific).

### 3.2 Three-stage temporal learning framework

**Stage 1 — Comprehension: Foundational temporal understanding via RL fine-tuning**

*Objective.* Establish robust foundation for temporal comprehension by interpreting fundamental temporal relationships between events and times via fine-tuning on historical news data from before the model's knowledge cutoff.

*Dataset.* Derived from a large corpus of New York Times (NYT) articles (>200,000) spanning January 2016 to December 2023. Each event $E$ represented by headline $h$ and abstract $a$, i.e., $E = (h, a)$.

*Four subtasks:*
1. **Timestamp Inference** — infer the specific date $t$ (e.g., `2023-12`) for a described event $E$.
2. **Time-Difference Estimation** — estimate the temporal gap $\Delta t$ (e.g., `14 months`) between two events $E_1$ and $E_2$.
3. **Event Ordering** — determine the correct chronological sequence $C$ (e.g., `Event order: 2-1-3`) of three events $E_1, E_2, E_3$ presented out of order.
4. **Masked Time Entity Completion** — fill in a masked temporal expression $M_e$ (e.g., `<Year>`, `<Month>`) within event description $E'$.

The model is forced to infer each event's date first, then give the task-specific answer. Both judged by a reward score (Section 3.3). This prevents the model from merely guessing the final answer implicitly. For Masked Time Entity Completion, success hinges on discerning detailed semantics from surrounding text, since the masked temporal entity often refers to a time distinct from the primary event date. Result: model checkpoint $\theta_1$ with robust foundational temporal understanding.

**Stage 2 — Prediction: Future event time prediction via RL fine-tuning**

*Objective.* Using Stage 1's foundational capabilities, train the model to predict timing of future events occurring after knowledge cutoff (2023): recall similar past events and dates, extrapolate temporal patterns, anticipate future events from post-cutoff information.

*Dataset.* Training set $\mathcal{D}_{\text{train}}^{(2)}$ constructed to prevent data leakage:
- 7,000 real news articles from January 2024 to July 2024 (aligning with DeepSeek-V3-0324-671B's July 2024 cutoff)
- Synthetic data for August 2024 – February 2025, generated using DeepSeek-V3 from May–July 2024 news, ~half the volume of real data

*Task.* Predict specific date $t$ (YYYY-MM) for a news event $E$ based on its headline and abstract. Initialized from $\theta_1$, continued GRPO fine-tuning on post-cutoff news. Result: checkpoint $\theta_2$ specialized in future event time prediction.

**Stage 3 — Generation: Creative future scenario generation and evaluation**

*Objective.* Pivot from training to application: leverage Stage 1 + 2 capabilities to directly generate plausible, diverse, temporally coherent future scenarios.

*Methodology — inference only* (no additional RL). Three sequential steps:

1. **Future news generation.** Generate hypothesized news events for specified future months $M$ (July 2024 onwards), conditioned on $T = 8$ common themes $\tau$ (Foreign Affairs, Business, Technology, Politics, etc.). Each prompt asks for 3 unique news items. Raw set $\mathcal{G}_{\text{raw}}$ includes each month $m$ and theme $\tau$.

2. **Diversity-based filtering.** Compute semantic embeddings $\mathbf{g} \in \mathbb{R}^{384}$ using `all-MiniLM-L6-v2`. Greedy selection per theme $\tau$ and month $m$ produces $\mathcal{G}_{\text{filt},m}$ containing $N_{\text{div}} = 5$ high-diversity news items per theme per month, totaling $N_g = T \times N_{\text{div}} = 40$ representative scenarios per month.

3. **Plausibility evaluation against real news.** Embed both filtered generated items $\mathbf{A}_g$ and real news items $\mathbf{B}_r$ from held-out test set $\mathcal{D}_{\text{test}}^{(2)}$ (real Aug 2024 – Feb 2025 events). Cosine similarity:
   $$\text{sim}(\mathbf{A}_g, \mathbf{B}_r) = \cos(\phi) = \frac{\mathbf{A}_g \cdot \mathbf{B}_r}{\|\mathbf{A}_g\| \|\mathbf{B}_r\|}$$
   Compute **Average Maximum Similarity (AvgMaxSim)** per month $m$:
   $$\text{AvgMaxSim}_m = \frac{1}{N_g} \sum_{i=1}^{N_g} \left( \max_{\mathbf{B}_r \in \mathcal{D}_{\text{real},m}} \text{sim}(\mathbf{A}_{g,i}, \mathbf{B}_r) \right)$$

This quantifies how closely generated plausible future events align semantically with events that actually transpired. Stage 3 success **without direct generation training** demonstrates that the S1+S2 curriculum builds transferable temporal reasoning.

### 3.3 Reward design

Total reward: $R(x, y) = R_{\text{acc}} + R_{\text{format}} - P_{\text{penalty}}$, range $[-0.8, 1.1]$.

**Universal bonuses and penalties:**
- *Format adherence bonus* $R_{\text{ans\_fmt}}$: $b_{\text{fmt}} = 0.05$ for valid format (e.g., `YYYY-MM`); prerequisite for accuracy scoring
- *Tag structure bonus* $R_{\text{tags}}$: $b_{\text{tag}} = 0.025$ each for correct `<think>`/`</answer>` tags; range $[0, 0.05]$
- *Length and repetition penalty* $P_{\text{len\_rep}} = \max(P_{\text{length}}, P_{\text{repetition}})$, range $[0, 0.5]$
  - $P_{\text{length}} = \min(1.0, (N - L_{\text{thresh}}) / (L_{\text{max}} - L_{\text{thresh}})) \times 0.3$ if $N > L_{\text{thresh}}$ (where $L_{\text{thresh}} = 900$ tokens, $L_{\text{max}} = 1024$)
  - $P_{\text{repetition}} = \max(P_{\text{word\_repeat}}, P_{\text{phrase\_repeat}}, P_{\text{ngram\_diversity}})$ — penalizes >5 consecutive identical words, recurring phrases, insufficient n-gram diversity

**Task-specific accuracy scores** ($R_{\text{acc}} \in [0, 1]$):

- *Timestamp Inference:* exponential decay on month-distance:
  $$R_{\text{acc}} = R_{\text{date}}(t_p, t_{gt}, \alpha) = e^{(-\alpha \cdot \Delta m(t_p, t_{gt}))}$$
  with dynamic $\alpha \in [0.07, 0.1]$ adjusted by sample difficulty and training step.

- *Time-Difference Estimation:* weighted combo $R_{\text{acc}} = (w_d R_{d_1} + w_d R_{d_2} + w_{\Delta t} R_{\Delta t}) \cdot P_{\text{incon}}$ with $w_d = 0.25, w_{\Delta t} = 0.5$. Includes **inconsistency penalty** $P_{\text{incon}}$ penalizing the difference between explicit $\Delta t_p$ and implied $\|t_{p_2} - t_{p_1}\|$.

- *Event Ordering:* $R_{\text{acc}} = (w_d \sum_{i=1}^3 R_{d_i} + w_{\text{ord}} R_{\text{order}}) \cdot P_{\text{incon}} \cdot P_{\text{div}}$ with $w_d = 0.2, w_{\text{ord}} = 0.4$. $R_{\text{order}} = N_{\text{correct\_pair}} / N_{\text{total\_pair}}$. **Diversity penalty** $P_{\text{div}}$ prevents trivial solutions (all identical dates, or sequential dates with trivial order).

- *Masked Time Entity Completion:* $R_{\text{acc}} = w_d R_{\text{date}} + w_e R_{\text{entity}}$ with $w_d = w_e = 0.5$. For Month entity, $\Delta m_c = \min(\|M_{e_p} - M_{e_{gt}}\|, 12 - \|M_{e_p} - M_{e_{gt}}\|)$ (circular difference).

- *Future Event Prediction:* same exponential decay but fixed $\alpha = 0.1$ (stricter; the model has foundational comprehension).

**Dynamic reward mechanism (Stage 1):** Three-phase curriculum on the decay coefficient $\alpha$ addresses the cold-start challenge and fosters robust performance on harder examples. Stratify training data by difficulty using initial Qwen2.5-3B-Instruct checkpoint on Timestamp Inference; samples with $|\Delta m| \leq 3$ are "easy," others "normal/hard."

- **Phase 1 — Foundational logic and format learning:** fine-tune on Timestamp Inference only, easy samples only, fixed strict $\alpha = \alpha_{\text{target}} = 0.1$. Goal: learn task logic and format.
- **Phase 2 — Exploration on full task suite:** expand to all four subtasks, full dataset. Normal/hard samples use lenient $\alpha = \alpha_{\text{start}} = 0.07$; easy samples keep $\alpha = 0.1$.
- **Phase 3 — Transition to strict evaluation:** continue on all tasks and difficulty levels; transition $\alpha$ for normal/hard samples linearly from $\alpha_{\text{start}} = 0.07$ to $\alpha_{\text{target}} = 0.1$ over $s_{\text{transition}} = 50$ steps, then fixed:
  $$\alpha_{\text{transition}}(s) = \alpha_{\text{start}} + (\alpha_{\text{target}} - \alpha_{\text{start}}) \cdot \min(1.0, s / s_{\text{transition}})$$

All test evaluations use fixed $\alpha = 0.1$ for comparability.

## 4. Experiments

### 4.1 Datasets
NYT-derived (Section 3.2).

### 4.2 Baselines
Two categories of six baselines:
- **Instruction-tuned LLMs:** Qwen2.5-3B-Instruct (base for Time-R1), Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct (medium scale), DeepSeek-V3-0324-671B (extra-large)
- **Specialized reasoning LLMs:** DeepSeek-Distill-Qwen-32B (reasoning emphasis), DeepSeek-R1-671B (SOTA across complex reasoning benchmarks)

### 4.3 Experimental setup
- Built on Qwen2.5-3B-Instruct using the **veRL** framework, GRPO algorithm
- KL coefficient $\beta = 0.001$, $K = 5$ rollout responses per prompt
- 4 NVIDIA A6000 GPUs
- Hyperparameter details in Appendix A

### 4.4 Main results

**Stage 1 — Foundational temporal reasoning (Table 1).** Time-R1 ($\theta_1$) shows +171.6% improvement over base Qwen2.5-3B-Instruct on overall average score. Outperforms DeepSeek-V3-0324-671B (much larger), highly competitive with DeepSeek-R1-671B. Best on Completion (0.7555), second-best on Event Ordering (0.6815). Ablation Time-R1-Fixed-Reward ($\theta_1'$) underperforms full Time-R1, validating the dynamic-reward curriculum.

| Model | Overall Avg.↑ | Ordering↑ | Completion↑ | Inference↑ | Difference↑ |
|---|---|---|---|---|---|
| Qwen2.5-3B-Instruct (base) | 0.2384 | 0.1583 | 0.2217 | 0.3372 | 0.2363 |
| Qwen2.5-7B-Instruct | 0.3092 | 0.2775 | 0.2953 | 0.3366 | 0.3275 |
| Llama-3.1-8B-Instruct | 0.2492 | 0.2239 | 0.2008 | 0.3339 | 0.2383 |
| DeepSeek-Distill-Qwen-32B | 0.4702 | 0.5026 | 0.3943 | 0.5264 | 0.4576 |
| DeepSeek-V3-0324-671B | 0.6471 | 0.6409 | 0.6777 | 0.6796 | 0.5901 |
| DeepSeek-R1-671B | 0.6916 | 0.6848 | 0.7493 | 0.7145 | 0.6172 |
| **Time-R1-Fixed-Reward** ($\theta_1'$, 3B) | 0.6259 | 0.6623 | 0.6977 | 0.5813 | 0.5621 |
| **Time-R1** ($\theta_1$, 3B) | **0.6476** | **0.6815** | **0.7555** | 0.5938 | 0.5599 |

**Stage 2 — Future event time prediction (Table 2).** Time-R1 ($\theta_2$, 3B) achieves highest score (0.7780), outperforming DeepSeek-R1-671B (0.7503) and DeepSeek-V3-671B (0.7036). Ablation Time-R1-S2-Direct ($\theta_2'$, 3B, Stage 2 only) at 0.7331 — Stage 1's foundational understanding contributes significantly.

| Model | Avg. Total Score↑ |
|---|---|
| Qwen2.5-3B-Instruct | 0.6036 |
| Qwen2.5-7B-Instruct | 0.6226 |
| Llama-3.1-8B-Instruct | 0.6015 |
| DeepSeek-Distill-Qwen-32B | 0.5997 |
| DeepSeek-V3-0324-671B | 0.7036 |
| DeepSeek-R1-671B | 0.7503 |
| Time-R1-S2-Direct ($\theta_2'$, 3B) | 0.7331 |
| **Time-R1** ($\theta_2$, 3B) | **0.7780** |

**Stage 3 — Creative scenario generation quality (Table 3).** Time-R1 ($\theta_2$, 3B) achieves highest AvgMaxSim (48.90%), surpassing DeepSeek-V3-0324-671B (48.81%) and DeepSeek-R1-671B (47.46%). Strong monthly scores: 50.81% in Jan 2025.

| Model | Avg. (%)↑ | 24-08 | 24-09 | 24-10 | 24-11 | 24-12 | 25-01 | 25-02 |
|---|---|---|---|---|---|---|---|---|
| Qwen2.5-3B-Instruct | 47.66 | 47.27 | 46.89 | 47.39 | 48.57 | 48.77 | 47.76 | 46.94 |
| DeepSeek-V3-0324-671B | 48.81 | 50.73 | 51.77 | 48.60 | 48.46 | 47.52 | 47.71 | 46.85 |
| DeepSeek-R1-671B | 47.46 | 47.55 | 49.64 | 47.29 | 45.29 | 47.85 | 47.30 | 47.31 |
| Time-R1-S2-Direct ($\theta_2'$, 3B) | 47.93 | 47.89 | 47.11 | 47.95 | 48.29 | 46.05 | 50.69 | 47.52 |
| **Time-R1** ($\theta_2$, 3B) | **48.90** | 47.75 | 48.29 | 49.81 | 48.77 | 49.03 | 50.81 | 47.83 |

### 4.5 Ablation studies

**4.5.1 Impact of dynamic reward mechanism.** Dynamic-reward model achieves consistently higher and more stable scores than fixed-reward ablation (Fig. 3a). On Masked Time Entity Completion (Fig. 3b), fixed-reward plateaus around 0.70 while curriculum-trained model continues to >0.75. Initial reward leniency + gradual strictness enables more effective exploration, prevents suboptimal policy convergence.

**4.5.2 Impact of staged curriculum learning.** Time-R1 ($\theta_2$, full S1+S2) vs Time-R1-S2-Direct ($\theta_2'$, S2 only):
- Stage 2: 0.7780 vs 0.7331 (+0.0449)
- Stage 3: 48.90% vs 47.93% (+0.97 pts)

Stage 1's foundational comprehension is crucial for superior predictive accuracy and generative plausibility. Stage 2 alone is effective but doesn't unlock the model's full potential.

## 5. Discussion

### 5.1 Reasoning process matters, not just response length

Dynamic-reward model produces consistently and significantly more concise outputs (~130 tokens) than fixed-reward model (~250 tokens) while achieving higher accuracy (Fig. 5). The curriculum fosters a more efficient, focused reasoning process — the model learns to achieve better outcomes without verbose outputs, implying a clearer, more direct approach to temporal tasks.

### 5.2 Challenges for standard LLMs in advanced temporal tasks

Standard LLMs, including SOTA reasoning-focused variants, perform commendably on foundational temporal tasks within knowledge cutoff (Stage 1), attributable to large scale and pre-training including math/logic data. But capabilities are substantially challenged on tasks requiring **extrapolation and nuanced future-oriented generalization**.

In Stage 2 and Stage 3, even DeepSeek-R1-671B is outperformed by Time-R1 ($\theta_2$, 3B): 0.7780 vs 0.7503 in prediction; 48.90% vs 48.81% in generation. This disparity suggests vast knowledge, large scale, or general reasoning prowess alone do not readily translate to proficiency in predicting future event timings or creatively generating plausible future scenarios. Standard training methodologies show a general weakness in future-oriented generation. **Specialized training regimes are necessary to cultivate comprehensive, practically useful temporal intelligence.**

## 6. Conclusion

Time-R1 is a 3B-parameter LLM achieving comprehensive temporal reasoning — understanding, prediction, and creative generation — through a three-stage RL curriculum with dynamic rewards. It outperforms models 200× its size on future event prediction and creative scenario generation, with robust generalization to the latter without task-specific fine-tuning. This addresses a critical research gap and demonstrates that progressive RL enables smaller, efficient models to achieve superior temporal performance, offering a practical, scalable path toward truly time-aware AI.

## References

- [1] Vaswani et al. "Attention is all you need." NeurIPS 2017.
- [2] Brown et al. (GPT-3). 2020.
- [13] Zhao et al. — knowledge alignment to target times
- [16] OpenAI o1
- [17] DeepSeek-R1 (671B)
- [18] PPO (Schulman et al.)
- [19] GRPO (Group Relative Policy Optimization)
- [24] DPO (Direct Preference Optimization)
- [25] SimPO
- [26] Ahmadian et al. — RLOO
- [36] NYT corpus
- [40] all-MiniLM-L6-v2 embedding model
- [42] Qwen2.5 (Qwen team)
- [43] Llama-3.1
- [44] DeepSeek-V3-0324
- [45] veRL framework

*(Full bibliography in arXiv source.)*
