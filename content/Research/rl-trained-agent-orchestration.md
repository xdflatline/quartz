---
title: "RL-Trained Agent Orchestration"
details: "Cross-cutting synthesis of research on using reinforcement learning to train a small language model that orchestrates pools of worker LLMs. The Conductor (Sakana AI, arXiv:2512.04388, 2026) is the canonical recent example — a 7B GRPO-trained orchestrator that designs coordination strategies in natural language, attains SOTA on GPQA Diamond and LiveCodeBench, generalises to arbitrary worker pools, and supports recursive self-as-worker test-time scaling. Contrasts with prior evolutionary (TRINITY) and hand-designed multi-agent approaches."
tags: [research, llm, agent, orchestration, agentic-system]
sources:
  - Papers/conductor-rl-orchestrator.md
  - Papers/trinity-evolved-llm-coordinator.md
  - Raw/conductor-rl-orchestrator-arxiv.md
created: 2026-08-19
updated: 2026-08-19
type: research
---

# Research Index: RL-Trained Agent Orchestration

**Updated:** 2026-08-19

---

## Overview

This research line investigates whether the *coordination* of multiple LLMs can itself be learned as a skill, rather than hand-engineered. The Conductor paper (Sakana AI, arXiv:2512.04388, 2026) demonstrates that a 7B language model, trained end-to-end with GRPO on a verifiable reward, can learn to design coordination strategies over a pool of worker LLMs that outperform both individual workers and prior multi-agent baselines — at a fraction of the inference cost.

The pattern generalises: any small LLM trained on `(task, reward)` pairs can learn to issue targeted subtasks, design communication topologies, and prompt-engineer its workers, all in natural language output.

## Concepts

### Coordination Patterns
- [[Concepts/rl-conductor-trained-orchestrator]] — the canonical pattern: a small LLM trained with RL to output coordination strategies
- [[Concepts/recursive-test-time-scaling]] — recursive self-as-worker extension; a new test-time compute axis
- [[Concepts/coordination-topology-in-natural-language]] — the Python-list output format that makes RL training possible
- [[Concepts/coordinator-worker-task-dag-orchestration]] — broader DAG-style coordination taxonomy
- [[Concepts/multi-agent-orchestration-patterns]] — full taxonomy of multi-agent designs (hand-engineered, template-based, learned)
- [[Concepts/evolved-llm-coordinator]] — TRINITY's evolutionary alternative to RL
- [[Concepts/separable-cma-es-lm-coordination]] — the optimisation method TRINITY uses

### Test-Time Compute
- [[Concepts/recursive-test-time-scaling]] — recursive self-as-worker extension; a new test-time compute axis

## Tools & Projects

### Research Labs
- [[Entities/sakana-ai]] — Tokyo-based lab behind both TRINITY and the Conductor

### Worker LLMs Referenced in the Paper
- [[Entities/claude-code]] — Claude Sonnet 4 referenced as a worker
- [[Entities/qwen]] — Qwen-32B referenced as a worker (and Qwen-2.5-7B-Instruct as the Conductor's base model)
- [[Entities/gemini-3-5-flash]] — Gemini 2.5 Pro referenced as a worker

## Raw Sources

- [[Raw/conductor-rl-orchestrator-arxiv]] — full Conductor paper, 2026
- [[Raw/trinity-coordinator-arxiv]] — full TRINITY paper (predecessor from same lab)

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [Conductor (arXiv:2512.04388)](https://arxiv.org/html/2512.04388v5) | RL-trained orchestrator | 2026 | GRPO on coordination strategies, recursive test-time scaling, randomised pools |
| [TRINITY (ICLR 2026)](https://arxiv.org/abs/...) | Evolved coordinator | 2026 | CMA-ES on Thinker/Worker/Verifier roles |

## Cross-Cutting Themes

### Coordination is a learnable skill
Strong multi-agent strategies (planners, verifiers, debate, role specialisation, prompt engineering) emerge from RL on a verifiable reward. The Conductor did not have hand-designed scaffolds for verification or debate — these behaviours emerged from end-to-end reward maximisation. This is the headline finding: **the orchestrator itself is the artifact**, and learning it is a tractable problem.

### Output format matters more than model size
The Conductor's three-Python-list output (subtasks, model IDs, access lists) is what makes RL training possible — the format reward is hard, the correctness reward is clean. A more flexible format (free-form JSON) would have been much harder to train.

### Smaller is fine for the orchestrator role
A 7B orchestrator is enough to coordinate 5–10 worker LLMs each 10× larger. The orchestrator doesn't need to know how to solve the problem — it needs to know which worker to call and what to tell it. This separates "reasoning" (the worker's job) from "coordination" (the orchestrator's job).

### Adaptive test-time compute
Prior test-time scaling techniques (best-of-N, self-refine, majority vote) use *fixed* rounds. Recursive Conductor uses *learned* rounds — the orchestrator decides when to stop iterating. This is a new axis of inference-time scaling that is orthogonal to context length, model size, and chain-of-thought depth.

### Generalisation to arbitrary worker pools
The randomised-pool training trick is the key to making the orchestrator user-customisable. Without it, the Conductor overfits to its training-time workers; with it, the Conductor adapts to whatever pool the user has — including pools of only open-source models.

## Open Questions

1. **Beyond verifiable tasks.** The Conductor's reward is binary correctness — what happens for open-ended generation where the reward is subjective?
2. **Scaling beyond 10 workers.** The orchestrator's prompt is the bottleneck. Can retrieval-based worker selection scale to hundreds of workers?
3. **Theoretical characterisation of the stopping policy.** Recursive Conductor learns *when* to stop, but no theory explains the emergent behaviour.
4. **Composition with other test-time scaling.** Can recursive Conductor be combined with chain-of-thought, self-consistency, or process reward models?
5. **Cross-task transfer.** The Conductor is trained on math + code + science. Does it transfer to dialogue, retrieval, or other domains?

## Next Research Directions

- **Prototype a Conductor-style orchestrator** for a verifiable task (e.g. SQL generation) using a small open-source orchestrator (Qwen-2.5-7B-Instruct) and 2-3 worker models. Measure gains over single-agent self-refine. **Success criteria**: orchestrator beats best individual worker by ≥5 percentage points at ≤2× inference cost.
- **Compare GRPO vs CMA-ES** for training the same orchestrator architecture on the same task. The Conductor uses GRPO; TRINITY uses separable CMA-ES. Which learns faster? Which generalises better? **Success criteria**: head-to-head benchmark on one verifiable reasoning task.
- **Test randomised-pool training** as a transfer technique. Train an orchestrator on a fixed pool, then evaluate zero-shot on an unseen pool (e.g. swap GPT-5 for Qwen-32B mid-evaluation). **Success criteria**: orchestrator retains ≥80% of its in-distribution performance.
- **Investigate emergent prompt-engineering strategies** the Conductor discovers — what patterns does it learn within `subtasks[]`? Can those patterns be extracted and reused as standalone prompting techniques? **Success criteria**: catalogue of ≥10 distinct prompt-engineering patterns from the paper's example completions.
- **Combine recursive Conductor with best-of-N** — at each recursive round, run the inner coordination strategy N times and majority-vote. **Success criteria**: outperforms both techniques alone.

## Related Research

This research line intersects with broader multi-agent systems research and test-time compute scaling. See [[Concepts/multi-agent-orchestration-patterns]] for the broader taxonomy and [[Entities/sakana-ai]] for the lab that produced both the Conductor and its predecessor TRINITY.
