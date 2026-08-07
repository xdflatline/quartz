---
title: "ADAS paper (Automated Design of Agentic Systems)"
detail: "Hu, Lu, and Clune 2025. Formulates agent design as an optimization problem — a meta-agent proposes new agentic workflows, the draft goes through two self-refine steps for novelty, the result is evaluated and added to an archive of successful designs."
details: "The first paper to articulate 'meta-agent search' as a distinct subfield. The procedure — initialize an archive, ask the meta-agent to program new agents, self-refine for novelty, evaluate, add to archive — is now the canonical reference for workflow search."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2408.08435
---

# ADAS paper (Automated Design of Agentic Systems)

**Source:** Hu, Lu, and Clune, "Automated Design of Agentic Systems," ICLR 2025.

## Overview

The paper that introduced **"meta-agent search"** — a meta-agent proposes new agentic workflows, the draft goes through two self-refine steps for novelty, the result is evaluated and added to an archive of successful designs. The procedure is the canonical reference for [[Concepts/meta-agent-workflow-search]].

## Procedure

1. Initialize an archive of agentic workflows with simple agents (CoT, self-refine)
2. Ask a meta-agent to program new agents in code, inspired by existing archive solutions
3. The meta-agent first generates a high-level description, then implements it in code
4. The draft program goes through two self-refine steps (Madaan et al. 2023) for novelty
5. Evaluate the new candidate; add successful ones to the archive
6. Repeat until iteration budget is hit

## Related

- [[Concepts/meta-agent-workflow-search]] — the concept
- [[Entities/aflow]] — the MCTS-based successor
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
