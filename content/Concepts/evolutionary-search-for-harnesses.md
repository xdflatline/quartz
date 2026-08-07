---
title: "Evolutionary Search for Harnesses"
detail: "Family of methods that evolve a population of harness or solution candidates by mutating them and keeping high-fitness survivors. Includes Promptbreeder, GEPA, AlphaEvolve, ThetaEvolve, DemoEvolve, ShinkaEvolve, DGM, and Hyperagents."
details: "Evolutionary search evolves a population of solutions by mutating them and only keeping those with high fitness in the crowd. Useful when (1) the search space is extensive or weirdly shaped, and (2) it is hard to optimize directly with gradients but easy to evaluate solutions. Harness search is a good fit. Weng's survey covers: Promptbreeder (prompt-evolution, mutations also evolve), GEPA (reflection + evolutionary search over natural language), AlphaEvolve (pool of candidate programs + frozen-LLM diffs + # EVOLVE-BLOCK markers), ThetaEvolve (evo + RL + ICL), DemoEvolve (augment archive with human demos), ShinkaEvolve (parent sampling balancing rank/offspring + novelty rejection + meta-scratchpad), DGM (LLM edits its own harness codebase), and Hyperagents (meta-agent controls modification of task agents)."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Evolutionary Search for Harnesses

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Learning Mechanism
**Status:** Active research area (multiple methods 2023-2026)

---

## Overview

Evolutionary search evolves a population of solutions by mutating them and keeping high-fitness survivors. It is useful when (1) the search space is extensive or weirdly shaped, and (2) it is hard to optimize directly with gradients but easy to evaluate solutions. Harness search is a good fit on both counts. Weng's survey enumerates a rich family of methods that all share this shape.

## Core Content

### Why Evolutionary Search for Harnesses

- **Harnesses are code.** The mutation operator is "ask an LLM to edit the code," which is exactly what LLMs are good at.
- **Fitness is cheap** when the harness has a benchmark (e.g., Terminal-Bench-2) — evaluate, score, keep or discard.
- **The search space is non-smooth.** Tiny edits can flip the score; gradient-based methods don't apply.
- **Population-based** — keeps a Pareto frontier of candidates, not a single winner.

### Method Family

| Method | Year | Mutation | Fitness signal | Population |
|--------|------|----------|----------------|------------|
| **Promptbreeder** | 2023 | LLM mutates task prompt; mutation prompts also evolve | Downstream task score | Task prompts |
| **GEPA** | 2025 | Natural-language reflection over trial-and-error trajectories | Downstream task score | Prompt candidates |
| **AlphaEvolve** | 2025 | LLM emits a diff; `# EVOLVE-BLOCK` markers delimit editable regions | Benchmark score (matmul, kernels, scheduling) | Programs |
| **ThetaEvolve** | 2025 | Evo + RL + in-context learning | Test-time open problems | Programs |
| **DemoEvolve** | 2026 | Self-rollouts + human expert demonstrations | Harness-level diagnosis | Harness candidates |
| **ShinkaEvolve** | 2025 | Parent sampling (rank × offspring), code-novelty rejection, meta-scratchpad | Benchmark score | Programs |
| **DGM** | 2025 | LLM edits its own harness code via `bash` + `editor` | SWE-bench Verified, Polyglot | Harness agents |
| **Hyperagents** | 2026 | Meta-agent controls how to modify task agents | Downstream task score | Task agents |

### AlphaEvolve — The Reference Implementation

Novikov et al. 2025. A coding-agent evolutionary search system: stores a pool of candidate programs and prompts **frozen** LLMs to generate diffs for improvement.

![AlphaEvolve overview](assets/lilianweng-harness-2026-07-04/alphaevolve.png)
*How AlphaEvolve works. (Image source: Novikov et al. 2025)*

Key design details:

- The prompt includes parent programs, results, instructions, and sometimes meta information
- The coding agent has access to the full repo, but code regions for improvement are **explicitly marked** with `# EVOLVE-BLOCK-START` and `# EVOLVE-BLOCK-END`
- The **meta-prompt co-evolves** with instructions and context, similar to how solution programs are evolved

![AlphaEvolve ablations](assets/lilianweng-harness-2026-07-04/alphaevolve-plot.png)
*Ablations show the value of the evolution procedure, context in prompts, meta-prompts, full-file evolution, and stronger LLMs. (Image source: Novikov et al. 2025)*

### ShinkaEvolve — Sample-Efficient Extensions

Lange et al. 2025. Three new components for LLM sampling efficiency:

- **Parent sampling balance** — pick parents with a probability that trades off performance rank and offspring count (avoid clonal dominance of the best candidate)
- **Code-novelty rejection sampling** — discard candidates too similar to the existing population based on embedding-based cosine similarity (prevent mode collapse)
- **Meta-scratchpad** — record patterns from successful solutions to guide future mutation (curated memory of what worked)

### DGM and Hyperagents — Self-Editing the Harness

DGM (Zhang et al. 2025) is the most aggressive: an LLM-based coding agent is allowed to **modify its own harness code**. The parent reads its own benchmark evaluation log and proposes improvements to its own codebase, using only two tools: `bash` and `editor`. New agents are evaluated and only high-performing ones are kept.

In experiments with `Claude 3.5 Sonnet` as the base LLM and simple initial harness configs, DGM-discovered agents are comparable to or outperform handcrafted agents on **SWE-bench Verified (20% → 50%)** and **Polyglot (14.2% → 30.7%)**.

Hyperagents (Zhang et al. 2026) is the follow-up that introduces a **meta-agent to control how to modify existing task agents** — addressing the open question of which modification strategy to use.

### When Evolutionary Search Works

- Candidate solutions are **automatically evaluable** (matrix multiplication, GPU kernels, algorithm contests, datacenter scheduling)
- Fitness is **easy to quantify** and **fast to compute**
- The search space is large but structured (programs, prompts, harnesses)

### When It Struggles

- Evaluation is **slow, ambiguous, or heuristic-based** (e.g., "is this a good paper?")
- The reward signal is **hackable** (the agent exploits the benchmark)
- Compute cost grows quickly (each generation is a full LLM pass)

## Key Insights

1. **LLMs make a good mutation operator.** Reading, editing, and producing diffs is exactly what an LLM is good at. This is why "evolutionary search" suddenly became tractable for code.
2. **Diverse populations are critical.** Without explicit diversity pressure, the population collapses to a single mode. ShinkaEvolve's novelty rejection and DGM's inverse-children weighting are two responses.
3. **Self-editing the harness is the boldest move.** DGM and Meta-Harness treat the harness itself as the search target, not just the solution. The result is the closest current research comes to recursive self-improvement.
4. **The pattern is model-agnostic.** Any sufficiently strong LLM can serve as the mutation operator; the LLM doesn't need to be retrained.

## Related Concepts

- [[Concepts/darwin-godel-machine]] — DGM in detail
- [[Concepts/meta-harness-outer-loop]] — Meta-Harness, the harness-for-harnesses variant
- [[Concepts/meta-agent-workflow-search]] — ADAS / AFlow, the workflow-specific version
- [[Concepts/diversity-collapse-rsi]] — the failure mode the diversity tricks address
- [[Concepts/agentic-crossover-skill-evolution]] — the MCE equivalent for skills
- [[Concepts/agent-self-improvement]] — the broader paradigm these methods serve

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Related Entities: [[Entities/promptbreeder]], [[Entities/gepa]], [[Entities/alphaevolve]], [[Entities/thetaevolve]], [[Entities/demoevolve]], [[Entities/shinkaevolve]], [[Entities/darwin-godel-machine]], [[Entities/hyperagents]]
