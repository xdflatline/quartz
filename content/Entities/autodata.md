---
title: "Autodata"
detail: "Kulikov et al. 2026. An agentic data-scientist workflow that generates synthetic training/evaluation data at the 'just right' difficulty level — strong solver succeeds, weak solver fails — using challenger/solver/verifier roles."
details: "Autodata manages four roles: a main agent (the orchestrator), a challenger (proposes problems), a weak solver, a strong solver, and a verifier/judge. The challenger's prompt is updated iteratively based on feedback from the solvers and verifier. Limitation: synthesized tasks fine-tune weak solvers but not strong solvers; if the loop cannot iteratively improve the strong model, it is closer to indirect distillation over a generated prompt distribution than true RSI."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2606.25996
---

# Autodata

**Source:** Kulikov et al., "Autodata: An agentic data scientist to create high quality synthetic data," arXiv:2606.25996, 2026.

## Overview

An agentic data-scientist workflow for **generating synthetic training and evaluation data at the "just right" difficulty level** — the level where a strong solver succeeds but a weak solver fails. The system manages four roles in a closed loop.

## The Four Roles

- **Main agent** — orchestrator
- **Challenger** — proposes problems
- **Weak solver** — model being trained
- **Strong solver** — fixed reference model
- **Verifier / judge** — checks solver outputs and difficulty calibration

![Autodata workflow](assets/lilianweng-harness-2026-07-04/autodata.png)
*Autodata agentic workflow. (Image source: Kulikov et al. 2026)*

## The Loop

1. The challenger proposes a candidate problem
2. Both solvers attempt the problem
3. The verifier judges the attempts and the difficulty calibration
4. The challenger's prompt is updated based on feedback — produce more problems at the "just right" level

## Weng's Limitation

> Synthesized tasks are used to fine-tune weak solvers but not strong solvers. If the loop cannot iteratively improve the strong model, it is more like **indirect distillation** over a generated prompt distribution, with less RSI flavor.

The Autodata loop improves the *training data*, not the *strong solver itself*. This is one step removed from true recursive self-improvement.

## Related

- [[Entities/ai-scientist]] — sibling work at the manuscript level
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
- [[Concepts/agent-self-improvement]] — the broader paradigm
