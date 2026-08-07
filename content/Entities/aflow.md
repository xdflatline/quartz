---
title: "AFlow"
detail: "Zhang et al. 2025. Automating Agentic Workflow Generation — represents an agentic workflow as a graph (nodes = LLM-invoking actions, edges = code-level logic) and optimizes it with Monte Carlo Tree Search (MCTS)."
details: "AFlow showed decent improvement over manually designed workflows and ADAS on QA, code, and math tasks. The graph representation makes workflows explicit and inspectable; the MCTS selection rule (soft mixture of score and uniform exploration) avoids local optima."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2410.10762
---

# AFlow

**Source:** Zhang et al., "AFlow: Automating Agentic Workflow Generation," ICLR 2025.

## Overview

Represents an agentic workflow as a **graph** (nodes are LLM-invoking actions, edges are code-level logic) and optimizes it with **MCTS**. Improvement over manual workflows and ADAS on QA, code, and math tasks.

## Procedure

1. Initialize the starting workflow $W_0$ in the tree with a template
2. Select a workflow node using a **soft mixture of score and uniform exploration**
3. Expand it by asking an LLM to produce a modified workflow conditioned on its evaluation performance
4. Execute and evaluate
5. Add to the tree if improved, within an $N$-round budget
6. Repeat until top-$k$ average plateaus or budget is hit

## Related

- [[Concepts/meta-agent-workflow-search]] — the concept
- [[Entities/adas-paper]] — the archive-based sibling
- [[Concepts/graph-based-workflow-engine]] — adjacent graph-representation framing
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
