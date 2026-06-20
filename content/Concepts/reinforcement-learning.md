---
title: Reinforcement Learning (RL) for LLMs
detail: Aligning models using GRPO, PPO, DPO.
details: Aligning models using GRPO, PPO, DPO.
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# Reinforcement Learning for LLMs

RL techniques are used to shape the behavior of an LLM beyond basic next-token prediction, heavily utilized in reasoning and tool-calling models.

## Techniques

- **PPO (Proximal Policy Optimization)**: Requires a separate reward model.
- **DPO (Direct Preference Optimization)**: Uses preference pairs (chosen vs rejected) to optimize directly without a separate reward model.
- **GRPO (Group Relative Policy Optimization)**: Efficient RL algorithm that estimates baselines from multiple sampled outputs rather than a dedicated value network. Excellent for reasoning and math where correctness is binary.

[Unsloth RL Guide](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide)
