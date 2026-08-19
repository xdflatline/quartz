---
title: "TRINITY: An Evolved LLM Coordinator"
details: "A lightweight SLM-based coordinator trained with separable CMA-ES that orchestrates multiple heterogeneous LLMs in a multi-turn loop, assigning each selected model one of three roles (Thinker, Worker, Verifier) at each turn. Achieves 86.2% on LiveCodeBench V6 and demonstrates strong zero-shot transfer to unseen tasks."
tags: [research, agent, llm]
source: https://arxiv.org/abs/2512.04695
authors: ["Jinglue Xu", "Qi Sun", "Peter Schwendeman", "Stefan Nielsen", "Edoardo Cetin", "Yujin Tang"]
venue: "ICLR 2026 (to appear)"
created: 2026-08-19
updated: 2026-08-19
type: article
---

# TRINITY: An Evolved LLM Coordinator

**Authors:** Jinglue Xu, Qi Sun, Peter Schwendeman, Stefan Nielsen, Edoardo Cetin, Yujin Tang (Sakana AI; Institute of Science Tokyo; University of Michigan)
**arXiv:** [2512.04695v3](https://arxiv.org/abs/2512.04695) (submitted 4 Dec 2025, revised 27 Apr 2026)
**Venue:** To appear at the 14th International Conference on Learning Representations (ICLR 2026)

## Overview

Combining diverse foundation models is promising, but weight-merging is limited by mismatched architectures and closed APIs. Trinity addresses this with a lightweight coordinator that orchestrates collaboration among large language models (LLMs). The coordinator, comprising a compact language model (~0.6B parameters) and a lightweight head (~10K parameters), is optimized with an evolutionary strategy for efficient and adaptive delegation. Trinity processes queries over multiple turns, where at each turn the coordinator assigns one of three roles (Thinker, Worker, or Verifier) to a selected LLM, effectively offloading complex skill acquisition from the coordinator itself.

Experiments show that Trinity consistently outperforms individual models and existing methods across coding, math, reasoning, and domain knowledge tasks, and generalizes robustly to out-of-distribution tasks. On standard benchmarks, Trinity achieves state-of-the-art results, including a score of 86.2% on LiveCodeBench.

Theoretical and empirical analyses identify two main factors behind this performance:
1. The coordinator's hidden-state representations provide rich contextualization of inputs.
2. Under high dimensionality and strict budget constraints, the separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES) offers advantages over reinforcement learning, imitation learning, and random search by exploiting potential block-ε-separability.

## Architecture

The coordinator is a 0.6B-parameter small language model (SLM) with a ~10K-parameter linear head attached in parallel to the LM head. It takes the hidden state at the penultimate output token position as input and produces two logits:

- One over the LLM pool (the agent to invoke next)
- One over the three roles (Thinker, Worker, Verifier)

The lightweight head also fine-tunes the singular value scales of parameter matrices in the SLM's layers, indicated by red diagonal lines in the paper's parameterization diagram.

![Coordinator parameterization — a lightweight head operates in parallel to the base model's LM head and takes the hidden state corresponding to the penultimate output token as its sole input.](/assets/trinity-coordinator/fig02-parameterization.svg)

*Figure 2: Parametrization of the TRINITY coordinator.*

## Coordination Loop

At each turn, the full conversation transcript is passed to the coordinator. The head selects an LLM and assigns it one of three roles:

- **Thinker (T):** Devises high-level strategies and decompositions.
- **Worker (W):** Performs concrete problem-solving steps.
- **Verifier (V):** Evaluates the current solution's soundness and completeness.

A message processing module injects a role-specific prompt before the request is sent to the chosen LLM. The loop terminates when the verifier accepts the response, or when a fixed-turn budget is exhausted.

![Overview of the cyclical coordination architecture. In each turn, the full conversation transcript is passed to a compact coordinator model. A lightweight head selects an LLM and assigns it one of three roles: Thinker (T), Worker (W), or Verifier (V). A message processing module injects a role-specific prompt before the request is sent to the chosen LLM.](/assets/trinity-coordinator/fig01-overview.svg)

*Figure 1: TRINITY coordination architecture (left) and a worked example on a depreciation problem (right).*

## Why an Evolutionary Strategy?

Training is constrained by cost — each step requires running the coordinated agents for inference. The authors observe weak coupling among parameters: each has only a tiny influence on the scalar reward, making traditional methods like REINFORCE's per-parameter gradients low-SNR and therefore ineffective. In this regime (high dimensionality, weak parameter correlations, high per-step cost), a derivative-free Covariance Matrix Adaptation Evolution Strategy (CMA-ES) with diagonal covariance — separable CMA-ES (sep-CMA-ES) — is effective. The paper provides theoretical and empirical evidence that, in the extremely budget-tight scenario (1.5k–40k evaluations for a 10k-dimensional problem), sep-CMA-ES significantly outperforms RL and the random search baseline, suggesting strong block-ε-separability in the optimization objective.

## Results

| Benchmark | Trinity | Best Single Model | Notes |
|---|---|---|---|
| LiveCodeBench V6 | **86.2%** | 83.8% (GPT-5) | State-of-the-art |
| Math500 | ~0.79 | ~0.78 | Near per-question-best |
| MMLU | ~0.91 | ~0.85 | Near per-question-best |
| RLPR | ~0.36 | ~0.35 | |

On four held-out benchmarks (AIME, BigCodeBench, MT-Bench, GPQA-D), Trinity achieves the highest average score (54.21) and outperforms every individual baseline on each task.

![Trinity outperforms single- and multi-model baselines across four benchmarks. The approach (boldface on the x-axis) achieves the highest performance across four tasks, surpassing the baseline methods. In Math500, MMLU and LiveCodeBench, performance is close to the per-question-best upper bound.](/assets/trinity-coordinator/fig03-benchmarks.svg)

*Figure 3: Trinity outperforms single- and multi-model baselines across four benchmarks.*

![LiveCodeBench Results. Top: Trinity achieves state-of-the-art. Bottom: Trinity benefits from increasing maximum turns budgets.](/assets/trinity-coordinator/fig04-livecodebench.svg)

*Figure 4: LiveCodeBench state-of-the-art (top) and sensitivity to max collaboration turns (bottom).*

## Take-Aways

- **Hidden-state representations of a small LM are sufficient for coordination.** A 0.6B-parameter SLM with a ~10K-parameter head can orchestrate a pool of much larger model pools across domains.
- **sep-CMA-ES dominates RL/IL/RS in this regime.** High dimensionality, weak parameter coupling, and tight budgets favour black-box optimization with diagonal covariance.
- **Evolved coordination policy beats a uniform mixture.** Trinity's head learns a task-aware agent-selection distribution that favour high-performing LLMs and a meaningful role distribution, which is what produces the gains.

## Selection-Distribution Evolution

The choice of optimizer visibly shapes the learned agent-selection distribution during training. sep-CMA-ES adapts to a meaningful distribution that favours high-performing LLMs, while REINFORCE maintains an almost uniform selection pattern (indicating ineffective policy improvement). Random search often collapses to unipolar choices, over-selecting a single agent or role and limiting diversity.

![LLM selection distribution evolves as the coordinator learning progresses. Left: Distribution evolution from sep-CMA-ES. Right: Distribution evolution from REINFORCE. The sep-CMA-ES trajectory concentrates on a small, high-performing subset of the agent pool. The REINFORCE trajectory remains nearly uniform.](/assets/trinity-coordinator/fig06-es-vs-rl-distribution.svg)

*Figure 6: sep-CMA-ES (left) vs REINFORCE (right) — selection-distribution evolution.*

## Hidden-State Separability

The authors present a series of separability analyses of the penultimate-token hidden states, using PCA, LDA, UMAP, t-SNE, and linear/RBF SVMs. Linear and RBF SVMs both reach 100% accuracy on a task-type classification task; PCA, LDA, UMAP, and t-SNE all show clear clustering by task type and by agent selection. Separability index correlates positively with the head's linear classification accuracy on synthetic datasets, providing a controlled link between representation quality and downstream coordination accuracy.

![Task type separability in extracted hidden states. Both are based on penultimate-token hidden states processed by the SLM on the input sequence, and the labels are from the task metadata.](/assets/trinity-coordinator/fig05-task-separability.png)

*Figure 5: Task type separability in extracted hidden states.*

## Reduced Selection Distribution (Trained Coordinator)

The trained coordinator develops a clear task-aware selection strategy. The assignment of the seven agents (A0–A6) varies systematically across the four task types.

![Agent distribution over tasks. A0: GPT-5, A1: Claude-Sonnet-4-20250514, A2: Gemini-2.5-pro, A3: DeepSeek-R1-Distill-Qwen-32B, A4: Gemma-3-27b-It, A5: Qwen3-32B (reasoning), A6: Qwen/Qwen3-32B (direct). Trinity demonstrates strong task-aware agent selection strategy.](/assets/trinity-coordinator/fig15-agent-heatmap.png)

*Figure 15: Agent distribution over tasks learned by the trained coordinator.*

## Related

- [[Raw/trinity-coordinator-arxiv]] — full paper extraction with all 15 figures
- [[Concepts/evolved-llm-coordinator]] — the conceptual pattern
- [[Concepts/separable-cma-es-lm-coordination]] — the optimizer choice
- [[Concepts/role-based-llm-delegation]] — the Thinker/Worker/Verifier split
- [[Concepts/llm-routing-pool]] — related: routing routers
- [[Entities/sakana-ai]] — corresponding research lab
