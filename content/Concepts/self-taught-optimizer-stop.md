---
title: "Self-Taught Optimizer (STOP)"
detail: "Zelikman et al. 2023: an early example of recursive scaffolding improvement. A seed improver I_0 takes a solution s, utility u, and language model M, and returns an improved s'. STOP's goal is to improve the improver I itself, recursively: I_t = I_{t-1}(û, I_{t-1}; M)."
details: "STOP is one of the early examples of treating the optimizer itself as the optimization target. The meta-utility is the average utility of a given improver function I over a collection of downstream tasks D. The improved improver discovered strategies such as genetic algorithms, decomposing-and-improving-parts, multi-armed prompt bandits, simulated annealing, varying temperature, and beam/tree search — analogous to how a harness workflow can be represented as an object for optimization. The cautionary finding: STOP improved mean downstream performance with GPT-4 but DEGRADED with weaker models like GPT-3.5 and Mixtral. Recursive structure alone is not enough — the base model must be capable enough to improve the mechanism."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Self-Taught Optimizer (STOP)

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Learning Mechanism
**Status:** Historical (foundational; cautionary result)

---

## Overview

**Self-Taught Optimizer (STOP; Zelikman et al. 2023)** is one of the early examples of **recursive scaffolding improvement**. A seed improver $I_0$ takes an initial solution $s$, a utility function $u$, and a black-box language model $M$, and returns an improved solution $s' = I(u, s; M)$. The goal of STOP is not directly to improve $s$ — it is to improve **the improver $I$ itself**, recursively.

## Core Content

### The Recursive Update

The **meta-utility** is the average utility of a given improver function $I$ over a collection of downstream tasks $\mathcal{D}$:

$$
\hat{u}(I) \triangleq \frac{1}{|\mathcal{D}|} \mathbb{E}_{(u,s) \sim \mathcal{D}}[u(I(u, s; M))]
$$

Because improving the improver is itself an optimization problem, we recursively get a new version of $I_t$ based on $I_{t-1}$'s performance:

$$
I_t = I_{t-1}(\hat{u}, I_{t-1}; M)
$$

At each step, $I_{t-1}$ proposes an improved $I_t$ — the **proposer and the proposed are the same code path**, just at different meta-levels.

![STOP algorithm](assets/lilianweng-harness-2026-07-04/STOP-algo.png)
*STOP algorithm. (Image source: Zelikman et al. 2023)*

### Discovered Strategies

The improved improver $I_t$ discovered a remarkable range of strategies:

- **Genetic algorithms** — populations of solutions, mutation, selection
- **Decomposing-and-improving-parts** — split a problem into pieces, improve each, recombine
- **Multi-armed prompt bandits** — exploration vs exploitation over prompt variants
- **Simulated annealing** — accept worse solutions with decreasing probability
- **Temperature variation** — sweep the sampling temperature as a search parameter
- **Beam / tree search** — keep top-k candidates at each step

![STOP discovered strategies](assets/lilianweng-harness-2026-07-04/STOP-patterns.png)
*Examples of self-improvement strategies discovered by STOP. (Image source: Zelikman et al. 2023)*

The fact that the LLM could re-discover decades of optimization theory from a few iterations of self-improvement is a striking result.

### The Cautionary Finding

> STOP improved mean downstream performance across iterations with **GPT-4** but **degraded with weaker models** like GPT-3.5 and Mixtral.

Recursive structure alone is not enough. The base model must be **capable enough to improve the mechanism**. With a weak model, $I_{t-1}$ cannot propose a useful $I_t$, and the loop drifts.

The implication for harness design: **intelligence is still the core**; harness improvement is an *amplifier* of the underlying model, not a substitute for it.

### STOP in the Broader Picture

STOP is the conceptual ancestor of:

- **Meta-Harness** ([[Concepts/meta-harness-outer-loop]]) — the harness code is the improver
- **DGM** ([[Concepts/darwin-godel-machine]]) — the agent edits its own harness via `bash` + `editor`
- **Self-Harness** ([[Concepts/self-harness-propose-evaluate-accept]]) — bounded version of the same idea

What STOP introduced that all of these inherit: the **recursive update of the optimizer itself**, not just the solution.

## Key Insights

1. **The optimizer is a first-class optimization target.** This was STOP's contribution to the field; the rest of the field (DGM, Meta-Harness, Self-Harness) is variations on the theme.
2. **LLMs can rediscover classical search algorithms.** Genetic algorithms, simulated annealing, beam search — all were re-invented by the LLM in a few iterations. This is evidence that classical search is "in" the model's training distribution.
3. **Recursive structure is necessary but not sufficient.** The cautionary GPT-3.5 / Mixtral result is the canonical evidence: a weak model cannot self-improve, period.
4. **The base-model strength is the loop's ceiling.** Any self-improvement loop will plateau at whatever the base model can reliably improve. This is why the field has shifted toward harness-only improvement with a fixed model.

## Related Concepts

- [[Concepts/meta-harness-outer-loop]] — the modern "harness-for-harnesses" descendant
- [[Concepts/darwin-godel-machine]] — self-editing the harness
- [[Concepts/self-harness-propose-evaluate-accept]] — bounded version
- [[Concepts/agentic-harness-engineering-ahe]] — concurrent work with observability discipline
- [[Concepts/agent-self-improvement]] — the broader paradigm

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Paper: Zelikman et al., "Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation," COLM 2024.
