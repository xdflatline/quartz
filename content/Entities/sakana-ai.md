---
title: "Sakana AI"
details: "Tokyo-based AI research lab (founded 2023) focused on evolutionary approaches for foundation models, including model merging, evolutionary model search, and the TRINITY evolved LLM coordinator (ICLR 2026). The lab's name comes from the Japanese word for a small, evolved salmon species."
tags:
  - entities
  - research-lab
  - llm
sources:
  - Raw/trinity-coordinator-arxiv.md
  - Papers/trinity-evolved-llm-coordinator.md
  - Raw/conductor-rl-orchestrator-arxiv.md
  - Papers/conductor-rl-orchestrator.md
created: 2026-08-19
updated: 2026-08-19
type: entity
---

# Sakana AI

**Source:** [[Raw/trinity-coordinator-arxiv]], [[Papers/trinity-evolved-llm-coordinator]]
**Category:** Research Lab
**Founded:** 2023
**Location:** Tokyo, Japan

## Overview

Sakana AI is a Tokyo-based AI research lab founded in 2023. The lab's research focus is on **evolutionary approaches for foundation models**, including model-merging techniques, evolutionary model search, and the TRINITY evolved LLM coordinator (ICLR 2026). The lab's name comes from the Japanese word *sakana* (さかな) — a tribute to *sake salmon*, a small, evolved landlocked salmon species that adapted to its environment through evolution.

## Notable Work

- **Model Merging** — Sakana's earlier work introduced evolutionary merging of foundation models: combining weights of separately-trained models using evolutionary search rather than retraining. This sidesteps the architectural-mismatch and closed-API problems of weight-merging.
- **Evolutionary Model Search** — Sakana uses evolutionary algorithms to discover new model architectures and training recipes, rather than designing them by hand.
- **TRINITY (ICLR 2026)** — A lightweight coordinator trained with separable CMA-ES that orchestrates multiple heterogeneous LLMs in a multi-turn loop. The coordinator assigns the selected LLM a role (Thinker, Worker, or Verifier) at each turn. Achieves 86.2% on LiveCodeBench V6.
- **Conductor (arXiv:2512.04388, 2026)** — A 7B language model trained end-to-end with reinforcement learning (GRPO) to design coordination strategies over a pool of worker LLMs. The Conductor's output is three parallel Python lists (subtasks, model IDs, access lists) that define a custom communication topology per query. Achieves state-of-the-art on GPQA Diamond and LiveCodeBench at a fraction of the inference cost of prior multi-agent baselines. Extended with randomised agent-pool training and recursive self-as-worker inference.

## Affiliation in TRINITY

Five of the six TRINITY authors are affiliated with Sakana AI. The sixth (Peter Schwendeman) interned at Sakana AI while an undergraduate at the University of Michigan. Qi Sun has a joint affiliation with the Institute of Science Tokyo.

## Related

- [[Papers/trinity-evolved-llm-coordinator]] — prior Sakana coordinator (CMA-ES)
- [[Papers/conductor-rl-orchestrator]] — later Sakana coordinator (RL/GRPO)
- [[Concepts/evolved-llm-coordinator]] — the architecture TRINITY introduces
- [[Concepts/separable-cma-es-lm-coordination]] — the optimisation method TRINITY uses
- [[Concepts/rl-conductor-trained-orchestrator]] — the architecture Conductor introduces
- [[Concepts/recursive-test-time-scaling]] — Conductor's recursive extension
