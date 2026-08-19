---
title: "RL-Trained Orchestrator Pattern (Conductor)"
details: "Architectural pattern introduced by Sakana AI's Conductor (Nielsen et al., arXiv:2512.04388, 2026): a small language model (3B/7B) trained end-to-end with reinforcement learning (GRPO) on a verifiable reward to output *coordination strategies* over a pool of worker LLMs. The orchestrator's output is parsed into three simple lists — subtasks, worker IDs, and access lists — that define a custom communication topology per query. Strong collaborative strategies (planners, verifiers, debate, role specialisation) emerge from RL rather than being hand-designed."
tags: [concepts, llm, agent, orchestration, agentic-system, training]
sources:
  - Papers/conductor-rl-orchestrator.md
  - Raw/conductor-rl-orchestrator-arxiv.md
created: 2026-08-19
updated: 2026-08-19
type: concept
---

# RL-Trained Orchestrator Pattern (Conductor)

**Source:** [[Papers/conductor-rl-orchestrator]] · [[Raw/conductor-rl-orchestrator-arxiv]]
**Category:** Architecture Pattern
**Status:** Production-validated (state-of-the-art on LiveCodeBench and GPQA Diamond)

---

## Overview

The RL-Trained Orchestrator pattern trains a *small* language model with reinforcement learning to dynamically design agentic workflows over a pool of worker LLMs. The orchestrator is itself an LLM — given any query, it outputs a complete coordination strategy in natural language that specifies which worker to call, what subtask to give it, and what context (prior subtask solutions) to include. Strategies like verification, debate, planning, and prompt engineering emerge from end-to-end reward maximisation, without hand-designed scaffolds.

The defining feature: **the coordination strategy is learned, not scripted.** This separates the Conductor from prior multi-agent systems (AFlow, DSPy, AutoGen, CrewAI) which encode fixed or library-of-templates workflows that humans designed.

## Core Mechanics

### The output format

For each input $q_i$, the Conductor emits an *agentic workflow* parsed from its post-CoT response as three Python lists of equal length:

```python
model_id    = [...]   # worker LLM IDs per step
subtasks    = [...]   # natural-language instructions per step
access_list = [...]   # which prior steps' outputs each worker sees
```

The format is intentionally simple — three Python lists are trivially parseable, executable, and verifiable. Common emergent topologies include best-of-N, sequential chains, parallel trees with aggregation, and recursive self-revision (see [[Concepts/recursive-test-time-scaling]]).

### Training recipe

The reward $r_i$ has two terms:

1. **Format reward** — 0 unless the three lists parse correctly. Forces the Conductor to commit to a runnable workflow.
2. **Correctness reward** — 1 if the final workflow output matches the ground-truth solution, 0.5 otherwise.

Trained with GRPO (the DeepSeek-R1 style RL formulation). The Conductor is initialised from Qwen-2.5-7B-Instruct and trained on a mix of verifiable reasoning tasks (MATH-500, MMLU, RLPR, LiveCodeBench).

### Randomised agent-pool training (the key generalisation trick)

At each training step, the available worker pool is sampled from a distribution over closed-source + open-source models. Without this, the Conductor overfits to its training-time pool. With it, the Conductor learns to **adapt its worker selection to whatever pool the user has** — including pools of only open-source models like Qwen-32B + Llama-3-70B.

## Why It Works

1. **Coordination strategies are discrete and verifiable.** A workflow either parses or it doesn't; the final answer is either right or wrong. This makes the supervision signal clean.
2. **The Conductor has full control over the prompt to each worker.** This lets it do prompt engineering *as part of the strategy* — emergent strategies include "instruct the worker to show its reasoning", "have agent A critique agent B's output", "use a cheap model as a final format-checker".
3. **Smaller is fine for the orchestrator role.** 7B is enough to learn coordination — the heavy reasoning happens in the workers. The orchestrator just needs to know *which worker to call and what to tell it*.

## Key Properties

| Property | Conductor | Prior multi-agent systems (AFlow, DSPy, MoA) |
|----------|-----------|---------------------------------------------|
| Workflow design | Learned (RL) | Hand-designed or template library |
| Worker pool | Arbitrary (randomised training) | Usually fixed |
| Inference cost | Sub-linear in agents used | Linear in agents used |
| Coordination topology | Per-query, emergent | Fixed or hand-tuned |
| Test-time scaling | Recursive self-as-worker | Best-of-N, self-reflect, debate |

## Scaling Behaviour

- **3B Conductor** learns correct worker selection but produces suboptimal subtasks. Still outperforms individual workers on average.
- **7B Conductor** learns the full prompt-engineering and verification strategies. Surpasses GPT-5 on GPQA Diamond and every multi-agent baseline on LiveCodeBench.
- **Recursive 7B Conductor** adds a self-as-worker step that lets the orchestrator iterate on its own strategy. Further gains on the hardest tasks.

## When to Use This Pattern

- You have a fixed set of complementary worker models (some strong at math, some at code, some at format) and want to combine them better than any single model alone.
- The task is verifiable — you can score a final answer's correctness.
- The user wants to supply their own agent pool (e.g. only open-source models for cost / privacy reasons).
- You want the orchestrator to *discover* coordination strategies rather than commit to a fixed pipeline.

## When NOT to Use

- The task is open-ended generation (creative writing, dialogue) without a verifiable reward.
- You only have one worker model — there's nothing to orchestrate.
- Latency is critical — running 5+ agents sequentially is expensive even with a small orchestrator.

## Related Concepts

- [[Concepts/coordinator-worker-task-dag-orchestration]] — general coordinator/worker DAG pattern; the Conductor's output is a per-query DAG
- [[Concepts/multi-agent-orchestration-patterns]] — broader taxonomy of multi-agent designs
- [[Concepts/recursive-test-time-scaling]] — the Conductor's recursive extension; a new axis of test-time compute
- [[Concepts/coordination-topology-in-natural-language]] — the specific output format that makes this pattern verifiable
- [[Concepts/evolved-llm-coordinator]] — TRINITY (Sakana's prior 2026 work) uses CMA-ES instead of RL for the same coordination goal
- [[Concepts/separable-cma-es-lm-coordination]] — the optimisation method TRINITY uses

## References

- Paper: [[Papers/conductor-rl-orchestrator]]
- Raw extraction: [[Raw/conductor-rl-orchestrator-arxiv]]
- Original: https://arxiv.org/html/2512.04388v5
