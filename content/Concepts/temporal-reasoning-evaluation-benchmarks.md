---
title: "Temporal Reasoning Evaluation Benchmarks"
details: "Evaluation methodology from Liu et al. (Time-R1, arXiv:2505.13508v2, 2025-06-03) for temporal reasoning tasks. Uses a rule-based, verifiable composite reward (R(x,y) = R_acc + R_format − P_penalty, range [-0.8, 1.1]) with exponential-decay date accuracy (e^(-α·Δm)), task-specific inconsistency / diversity penalties, and length/repetition penalties. Stage 3 uses AvgMaxSim — mean max cosine similarity (over all-MiniLM-L6-v2 384-d embeddings) between generated future scenarios and held-out real news, per month. The pattern is a recipe for evaluating any forward-looking generative task against ground-truth events."
tags:
  - llm
  - benchmark
  - evaluation
created: 2026-09-14
updated: 2026-09-14
type: concept
sources:
  - "[[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]"
---

# Temporal Reasoning Evaluation Benchmarks

**Source:** Liu, Han, Yu, Li, You, *Time-R1* (UIUC, arXiv:2505.13508v2, 2025-06-03) ([[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]), Sections 3.3 and 3.2.3
**Category:** Architecture Pattern (evaluation methodology)
**Status:** Production-validated

---

## Overview

Time-R1 introduces two complementary evaluation methodologies for temporal reasoning: a **rule-based composite reward** for Stage 1/2 (timestamp inference, time-difference estimation, event ordering, masked time entity completion, future event prediction) and **AvgMaxSim** for Stage 3 (creative future scenario generation). Together they form a recipe for evaluating any forward-looking generative temporal task: rule-based verifiable rewards where ground-truth admits a continuous distance metric, plus embedding-based semantic similarity to real events where ground-truth cannot be expressed as a single correct answer.

## Core Content

### Composite reward for verifiable temporal tasks

For Stage 1 and Stage 2, the evaluation reward is closed-form and verifiable:

$$R(x, y) = R_{\text{acc}} + R_{\text{format}} - P_{\text{penalty}}, \quad \text{range } [-0.8, 1.1]$$

**Accuracy components (task-specific):**

- **Timestamp Inference:** exponential decay on month-distance — $R_{\text{date}}(t_p, t_{gt}, \alpha) = e^{(-\alpha \cdot \Delta m(t_p, t_{gt}))}$
- **Time-Difference Estimation:** weighted combo of date accuracies for each event + difference accuracy + inconsistency penalty for contradictions between explicit difference and inferred dates
- **Event Ordering:** weighted combo of date accuracies + order accuracy (fraction of correct ordered pairs) + inconsistency penalty + diversity penalty (penalizes trivial all-identical-date or strictly-sequential solutions)
- **Masked Time Entity Completion:** weighted combo of date accuracy + entity accuracy (circular month-distance for Month entity)
- **Future Event Prediction:** same as Timestamp Inference but with fixed strict $\alpha = 0.1$

**Universal bonuses:**

- Format adherence $R_{\text{ans\_fmt}}$ — $b_{\text{fmt}} = 0.05$
- Tag structure $R_{\text{tags}}$ — `<think>`/`</answer>` correct count, max 0.05

**Universal penalties:**

- Length penalty $P_{\text{length}}$ — penalizes responses exceeding 900 tokens (max 1024)
- Repetition penalty $P_{\text{repetition}} = \max(P_{\text{word\_repeat}}, P_{\text{phrase\_repeat}}, P_{\text{ngram\_diversity}})$ — penalizes >5 consecutive identical words, recurring phrases, insufficient n-gram diversity
- No-event penalty $P_{\text{no\_event}}$ — penalizes refusals like "no event" / "none" (range 0.1–0.3 depending on stage and severity)

### AvgMaxSim for creative generation

For Stage 3 (creative future scenario generation), there is no single correct answer — many plausible news events could be generated for a given future month. The metric is **embedding-based semantic similarity to held-out real events**:

1. **Generate** $N_g = T \times N_{\text{div}}$ scenarios for month $m$ (T themes × N_div high-diversity items per theme)
2. **Embed** each generated item $\mathbf{A}_g$ and each real news item $\mathbf{B}_r$ using `all-MiniLM-L6-v2` (384-d)
3. **Compute cosine similarity** $\text{sim}(\mathbf{A}_g, \mathbf{B}_r) = \cos(\phi) = \frac{\mathbf{A}_g \cdot \mathbf{B}_r}{\|\mathbf{A}_g\| \|\mathbf{B}_r\|}$
4. **Average Max Similarity** per month:

$$\text{AvgMaxSim}_m = \frac{1}{N_g} \sum_{i=1}^{N_g} \left( \max_{\mathbf{B}_r \in \mathcal{D}_{\text{real},m}} \text{sim}(\mathbf{A}_{g,i}, \mathbf{B}_r) \right)$$

The metric is the average over generated items of the **maximum** similarity to any real event in the target month. This rewards scenarios that are *plausibly close to some* real event, rather than averaging similarity to all events (which would dilute the signal).

### Why these two together

The composite reward answers "**how close to the right answer?**" for tasks with verifiable ground truth. AvgMaxSim answers "**how plausible is this generated scenario compared to what actually happened?**" for tasks with open-ended ground truth. They cover the two regimes an LLM temporal task can fall into:

| Task type | Ground truth | Metric |
|-----------|--------------|--------|
| Predict event date | Single date | Composite reward with exponential decay |
| Order events | Single permutation | Composite reward with order accuracy |
| Generate future scenario | Open-ended | AvgMaxSim against held-out real events |

### Generalization to other temporal / generative tasks

The pattern extends to:

- **Any task with continuous-distance ground truth** (e.g., duration estimation, age prediction): use exponential-decay rewards
- **Any task with logical-consistency constraints** (e.g., "do your intermediate answers match your final answer?"): use inconsistency penalties
- **Any task where trivial solutions should be discouraged** (e.g., always returning the same date): use diversity penalties
- **Any open-ended forward-looking generative task**: use AvgMaxSim-style max-similarity to held-out real events

### The role of diversity filtering

Before AvgMaxSim evaluation, generated items pass through a **diversity filter**: greedy selection over embeddings to keep $N_{\text{div}} = 5$ high-diversity items per theme per month. Without this filter, a model that generates 5 nearly-identical items for "Foreign Affairs" could trivially maximize max-similarity by including one near-duplicate of a real event. The diversity filter ensures the metric measures genuine topical coverage.

## Key Insights

1. **Exponential decay rewards are well-suited to temporal tasks** because temporal distance is continuous and a single-month error is qualitatively different from a twelve-month error.
2. **Inconsistency penalties catch a specific failure mode** — models that guess intermediate steps inconsistently with the final answer. Without these penalties, models can get credit for correct final answers via inconsistent reasoning.
3. **Diversity penalties prevent trivial solutions.** A model that always returns identical dates for "Event Ordering" achieves 33% order accuracy by chance; the diversity penalty forces the model to actually reason.
4. **AvgMaxSim (max, not mean) is the right aggregation** for plausibility evaluation: we want scenarios close to *some* real event, not scenarios that are mediocre matches to *all* real events.
5. **Rule-based verifiable rewards generalize to RLVR.** No learned reward model is needed; the reward is closed-form on (prediction, ground-truth). This is the same pattern used in current RLVR work.

## Related Concepts

- [[Concepts/three-stage-rl-curriculum-temporal-reasoning]] — the framework these metrics evaluate
- [[Concepts/dynamic-reward-curriculum-rl-finetuning]] — the dynamic-α version of these rewards
- [[Concepts/post-knowledge-cutoff-temporal-prediction]] — the evaluation window these metrics cover
- [[Concepts/reinforcement-learning-grpo]] — the underlying RL algorithm

## Related Entities

- [[Entities/time-r1]] — model evaluated with these metrics
- [[Entities/time-bench]] — dataset these metrics evaluate on

## References

- Raw Article: [[Raw/arxiv-time-r1-temporal-reasoning-2025-06-03]]
- Paper: https://arxiv.org/abs/2505.13508v2
- Code: https://github.com/ulab-uiuc/Time-R1
