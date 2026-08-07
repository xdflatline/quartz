---
title: "Meta-Agent Workflow Search (ADAS / AFlow)"
detail: "Treating workflow design as a search problem: ADAS (Hu et al. 2025) uses a meta-agent to program new agentic workflows from an archive; AFlow (Zhang et al. 2025) represents workflows as graphs and optimizes them with Monte Carlo Tree Search."
details: "Two complementary approaches to automated workflow design. ADAS: a meta-agent generates a high-level description then implements new agents in code, applies two self-refine steps for novelty, evaluates, and adds to an archive; initialization starts with simple agents (CoT, self-refine). AFlow: workflows are graphs where nodes are LLM-invoking actions and edges are code-level logic; optimization uses MCTS with soft mixture of score and uniform exploration, expanding nodes by asking the LLM to produce modified workflows conditioned on evaluation performance. AFlow showed decent improvement over manually designed workflows and ADAS on QA, code, and math."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Meta-Agent Workflow Search (ADAS / AFlow)

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Pattern
**Status:** Active research area (ICLR 2025)

---

## Overview

The workflow design space is enormous, and naturally we can think of workflow design as a **search problem** — so good solutions should be findable by algorithms rather than only by hand. Two complementary approaches define the state of the art: **ADAS** (Automated Design of Agentic Systems) and **AFlow** (automating workflow generation).

## Core Content

### ADAS — Automated Design of Agentic Systems (Hu et al. 2025)

Formulates agent design itself as an optimization problem: **"meta-agent search"** where a meta-agent proposes new designs of agentic workflows.

**Procedure:**

1. Initialize an archive of agentic workflows with simple agents (CoT, self-refine)
2. Ask a meta-agent to program new agents, all in code, inspired by existing solutions in the archive
3. The meta-agent first generates a high-level description of the new workflow, then implements it in code
4. The draft program goes through two self-refine steps (Madaan et al. 2023) by the meta-agent to check its novelty
5. Evaluate each new candidate; add successful ones back to the archive
6. Repeat steps 2-3 until the maximum iteration count is reached

![ADAS illustration](assets/lilianweng-harness-2026-07-04/adas.png)
*Illustration of ADAS. (Image source: Hu et al. 2025)*

**Key properties:**

- **Archive-based** — every successful candidate persists; later candidates can build on prior ones
- **Novelty-checked** — the self-refine steps prevent trivial duplicates
- **Code-level** — the artifact is runnable code, not a prompt

### AFlow (Zhang et al. 2025)

Represents an agentic workflow as a **graph**, where nodes are LLM-invoking actions and edges implement logical operations in code. Workflow optimization uses **MCTS (Monte Carlo Tree Search)**.

**Procedure:**

1. Initialize the starting workflow $W_0$ in the tree with a template
2. Select a workflow node using a **soft mixture of score and uniform exploration**
3. Expand it by asking an LLM to produce a modified workflow conditioned on its evaluation performance
4. Execute and evaluate the new workflow
5. Add it back to the tree if it shows improvement within a budget of $N$ rounds
6. Repeat steps 2-5 and stop when the top-$k$ average score plateaus or the budget is hit

![AFlow optimization](assets/lilianweng-harness-2026-07-04/aflow.png)
*AFlow optimization over a tree of workflow candidates. (Image source: Zhang et al. 2025)*

**Key properties:**

- **Graph representation** — explicit, inspectable, runnable
- **MCTS selection** — balances exploitation (best score) with exploration (uniform); avoids the local-optima trap of greedy search
- **Bounded budget** — $N$ rounds and a top-$k$ plateau check keep compute predictable

![AFlow experiments](assets/lilianweng-harness-2026-07-04/aflow-exp.png)
*AFlow experiments vs manual methods and ADAS. (Image source: Zhang et al. 2025)*

AFlow showed decent improvement of AFlow over manually designed workflows and ADAS on QA, code, and math tasks.

### ADAS vs AFlow

| Property | ADAS | AFlow |
|----------|------|-------|
| Search algorithm | Archive-based with self-refine novelty | MCTS |
| Workflow representation | Code (full agent) | Graph (nodes = LLM calls, edges = code) |
| Selection rule | "Add successful to archive" | Soft mixture of score and uniform |
| Budget | Iteration count | N rounds + top-k plateau |
| When to prefer | Open-ended exploration; heterogeneous agents | Refining an established template |

## Key Insights

1. **Workflow design is a search problem.** Once you treat it as one, the standard tool kit (MCTS, archive-based search) applies.
2. **The meta-agent is the operator.** The LLM proposes, edits, and refines; the surrounding code evaluates, archives, and budgets.
3. **A graph is more inspectable than a code blob.** AFlow's graph representation makes it easier to understand which nodes are responsible for which gains.
4. **The two methods compose with the self-improving family.** ADAS / AFlow are workflow-level search; Self-Harness, AHE, and Meta-Harness add observability and validation on top.

## Related Concepts

- [[Concepts/evolutionary-search-for-harnesses]] — the broader family (AlphaEvolve, ShinkaEvolve, DGM)
- [[Concepts/self-harness-propose-evaluate-accept]] — adds regression-test validation to the loop
- [[Concepts/agentic-harness-engineering-ahe]] — adds observability pillars
- [[Concepts/meta-harness-outer-loop]] — extends the search to harness code
- [[Concepts/graph-based-workflow-engine]] — the graph representation AFlow uses
- [[Concepts/capture-process-connect-create-workflow]] — adjacent workflow design framing

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Papers: Hu, Lu, and Clune, "Automated Design of Agentic Systems," ICLR 2025; Zhang et al., "AFlow: Automating Agentic Workflow Generation," ICLR 2025.
- Related Entities: [[Entities/adas-paper]], [[Entities/aflow]]
