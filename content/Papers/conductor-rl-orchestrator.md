---
title: "Conductor (RL-Trained LLM Orchestrator)"
details: "Sakana AI's Conductor (Nielsen et al., arXiv:2512.04388, 2026) is a small (3B/7B) language model trained end-to-end with reinforcement learning (GRPO) to dynamically design agentic workflows over a pool of worker LLMs. Given any user query, the Conductor outputs a complete coordination strategy — Python lists of natural-language subtasks, assigned worker IDs, and per-step access lists — that define a custom communication topology. The 7B Conductor attains state-of-the-art results on LiveCodeBench and GPQA Diamond while using a fraction of the inference cost of multi-agent baselines. Extended with randomized agent-pool training and a recursive self-as-worker loop that unlocks a new axis of test-time scaling."
tags: [research, paper, llm, agent, orchestration, agentic-system]
source: https://arxiv.org/html/2512.04388v5
authors: ["Stefan Nielsen", "Edoardo Cetin", "Peter Schwendeman", "Qi Sun", "Jinglue Xu", "Yujin Tang"]
venue: "arXiv:2512.04388v5, 2026"
created: 2026-08-19
updated: 2026-08-19
type: article
---

# Conductor: Learning to Orchestrate Agents in Natural Language

**Authors:** Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang (Sakana AI)
**Published:** arXiv:2512.04388v5, 2026
**Link:** https://arxiv.org/html/2512.04388v5

---

## Overview

The Conductor is a new kind of reasoning model trained with RL to dynamically divide challenging problems, delegate targeted subtasks, and design communication topologies for a set of worker LLM agents. The Conductor itself is a language model — its output is a sequence of workflow steps, each defined by a natural-language instruction, the assigned worker agent, and an access list specifying which prior subtask solutions that worker can see. This lets the Conductor construct entirely flexible agentic workflows customised to each input problem, with strategies such as prompt engineering, refinement, and even meta-prompt optimisation emerging naturally from end-to-end reward maximisation.

The 7B Conductor attains state-of-the-art results on LiveCodeBench and GPQA Diamond while using a fraction of the inference cost of prior multi-agent baselines. With random agent-pool training and recursive self-as-worker inference, the framework also generalises to arbitrary user-supplied worker pools and unlocks a new axis of test-time scaling.

![](/assets/conductor-2512-04388/fig01-leaderboard-sota.png)

*Figure 1: Our Conductor attains the state-of-the-art in GPQA and LiveCodeBench.*

## Core Contributions

1. **The RL Conductor formulation.** A small LLM trained end-to-end with GRPO to output *coordination strategies* in natural language: a sequence of `{subtask, agent_id, access_list}` triples that define a custom communication topology over a pool of worker LLMs.
2. **State-of-the-art results from a 7B orchestrator.** Beats both single-agent reflection baselines and prior multi-agent methods (e.g. AFlow, DSPy, Mixture-of-Agents) on LiveCodeBench, GPQA Diamond, MATH-500, MMLU, Medreason, and BigCodeBench — at a fraction of the inference cost.
3. **Randomised agent-pool training.** By randomising the available workers at each training step, the Conductor learns to generalise to arbitrary sets of open- and closed-source models. A user with only Qwen-32B and Llama-3-70B can still get state-of-the-art performance on their custom pool.
4. **Recursive self-as-worker topology.** When the Conductor is allowed to call itself as one of the workers, it iteratively revises its coordination strategy based on the previous round's outcome — a new form of online test-time scaling.
5. **Empirical evidence that coordination is learnable via RL.** Strong collaborative strategies (planners, verifiers, debate rounds, role specialisation) emerge from pure end-to-end reward maximisation, without hand-designed scaffolds.

## Methodology

### Task framing

For each input question $q_i$, the Conductor produces an *agentic workflow* — a sequence of steps whose final output is returned as the response $o_i$. Each step is parsed from the Conductor's post-chain-of-thought output into three Python lists of equal length:

- `subtasks[]` — natural-language instructions for each worker.
- `model_id[]` — the worker LLM assigned to that step.
- `access_list[]` — which prior subtask solutions are visible to this worker.

The format is exemplified in Figure 2 (caption-only in the Raw paper) and Figure 13 (full prompt). Common emergent topologies include best-of-N, sequential chains, parallel trees with aggregation, and recursive self-revision.

![](/assets/conductor-2512-04388/fig11-conductor-schematic.png)

*Figure 11: Conductor schematic visualisation. The Conductor combines the differing specialisations of the worker LLMs to answer complex user queries.*

### Training

The reward $r_i$ has two terms:

- **Format reward**: 0 unless the Python lists parse correctly.
- **Correctness reward**: 1 if the final workflow output matches the ground-truth solution $s_i$, 0.5 otherwise.

Trained with GRPO (the DeepSeek-R1 style RL recipe) over a mix of verifiable tasks (MATH-500, MMLU, RLPR, LiveCodeBench). The Conductor is initialised from Qwen-2.5-7B-Instruct and trained on a fixed pool of closed and open worker models.

![](/assets/conductor-2512-04388/fig03-training-emergence.svg)

*Figure 3: Emergence of powerful coordination strategies over training. Early in training, the Conductor issues sound subtasks but does not tap useful collaborative strategies such as verification. Near convergence, the Conductor has learned to utilise planners, issue targeted instructions, instruct workers to share reasoning, and leverage verification and refinement.*

### Extensions

- **Randomised pool finetuning.** At each training step, sample the available worker pool from a distribution (closed models + open models). This makes the Conductor robust to any user-supplied pool.
- **Recursive test-time scaling.** Append the Conductor itself to the worker pool. After the first round, the Conductor sees its own output and can either accept it or design a new coordination strategy that revises the answer. This is *dynamic* test-time scaling — the Conductor decides how many rounds to spend, not the user.

## Results

![](/assets/conductor-2512-04388/fig04-indist-eval.png)

*Figure 4: Conductor in-distribution evaluation against multi-agent methods and 5-turn reflection agent baselines. The Conductor surpasses all baselines by substantive margins.*

![](/assets/conductor-2512-04388/fig05-perf-vs-efficiency.png)

*Figure 5: Performance vs Efficiency. The Conductor far surpasses multi-agent baselines at a fraction of the cost.*

### Key benchmarks

| Benchmark | Conductor (7B) | Best prior | Improvement |
|-----------|----------------|------------|-------------|
| GPQA Diamond | 85.4% | ~70% (single GPT-5) | new SOTA |
| LiveCodeBench | 76.4% | ~71% (multi-agent) | new SOTA |
| MATH-500 | 97.8% | ~96% | competitive |
| MMLU | 92.4% | ~90% | competitive |

(See Raw file for the full Tables 1–11.)

### Recursive scaling

Test-time recursion (Table 2) gives further performance gains, especially on the most complex tasks. The Conductor decides when to stop — for simpler tasks one round is sufficient, for complex LiveCodeBench problems it typically iterates 2–3 times.

![](/assets/conductor-2512-04388/fig10-recursive-worker-dist.png)

*Figure 10: Recursive Conductor worker distribution on BigCodeBench. The Conductor redistributes its agent selection towards Claude and Gemini in recursive rounds, reflecting their superior performance on coding tasks.*

### Scaling behaviour

![](/assets/conductor-2512-04388/fig07-agent-distribution.png)

*Figure 7: Conductor Scale. The 3B Conductor still learns optimal agent selection. When scaling to 7B, the Conductor learns more refined coordination strategies.*

The 3B Conductor learns to pick the strongest workers but produces suboptimal subtasks. The 7B version produces richer prompt-engineered instructions and uses verification / debate strategies.

### Task adaptivity

![](/assets/conductor-2512-04388/fig08-task-adaptivity.png)

*Figure 8: Task adaptivity. On MMLU the Conductor learns that 2 agents working together is optimal. On LiveCodeBench the Conductor allocates more workers.*

## Recursive Topologies

![](/assets/conductor-2512-04388/fig12-recursive-schematic.png)

*Figure 12: Recursive Conductor visualisation. At test time, the Conductor is able to adapt its initial coordination strategies on-the-fly.*

When the Conductor is allowed to call itself as a worker, a new form of dynamic test-time scaling emerges. The Conductor sees the response from its previous coordination strategy and decides whether to iterate or pass through. Recursive rounds redistribute the worker pool (the Conductor learns to allocate Claude and Gemini to harder tasks), and overall accuracy improves further.

## Key Takeaways

1. **Coordination is a learnable skill.** Strong multi-agent strategies (planners, verifiers, debate, prompt engineering, role specialisation) emerge from RL on a verifiable reward — no hand-designed scaffolds needed.
2. **A small orchestrator can outperform large workers.** A 7B Conductor beats every individual worker it orchestrates, including GPT-5 and Gemini 2.5 Pro.
3. **The output format matters.** Parsing the Conductor's strategy as three simple Python lists (subtasks, model_ids, access_lists) makes the output verifiable, executable, and compatible with arbitrary worker pools.
4. **Randomised-pool training is the key generalisation technique.** Without it the Conductor overfits to its training-time workers. With it, the Conductor adapts to arbitrary user pools.
5. **Self-as-worker recursion is a new test-time scaling axis.** Unlike best-of-N (fixed rounds) or self-refine (single model), recursive Conductor lets the orchestrator itself decide how to spend additional compute — and learns to do so effectively.

## Limitations and Open Questions

- The Conductor's reward depends on verifiable tasks — extending to open-ended generation requires reward modelling.
- Worker pools must be relatively small (≤10 workers) for the Conductor's prompt to remain tractable.
- The recursive loop's stopping behaviour is emergent and not well-characterised theoretically.

## References

- Raw extraction: [[Raw/conductor-rl-orchestrator-arxiv]]
- Original: https://arxiv.org/html/2512.04388v5
- Related prior work from the same lab: [[Papers/trinity-evolved-llm-coordinator]] — TRINITY uses separable CMA-ES rather than RL, but the underlying coordination goal (a small orchestrator over heterogeneous workers) is the same.
