---
title: "AlphaEvolve"
detail: "Novikov et al. 2025. A coding-agent evolutionary search system — stores a pool of candidate programs and prompts frozen LLMs to generate diffs for improvement. Marked with # EVOLVE-BLOCK-START/END; meta-prompt co-evolves with instructions."
details: "AlphaEvolve is the reference implementation of LLM-driven evolutionary search over programs. The candidate solutions are code; the mutation operator is an LLM that produces diffs; the fitness signal is a benchmark score. The # EVOLVE-BLOCK markers explicitly delimit the editable regions — a discipline that AHE adopts for harness evolution. Meta-prompt co-evolution is AlphaEvolve's distinctive feature: the instructions to the mutator improve along with the programs it mutates."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2506.13131
---

# AlphaEvolve

**Source:** Novikov et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery," arXiv:2506.13131, 2025.

## Overview

**AlphaEvolve** is a coding-agent evolutionary search system. It stores a pool of candidate programs and prompts **frozen** LLMs to generate diffs for improvement. As the system repeatedly evaluates child programs and keeps successful ones, it discovers better solutions in time.

![AlphaEvolve overview](assets/lilianweng-harness-2026-07-04/alphaevolve.png)
*How AlphaEvolve works. (Image source: Novikov et al. 2025)*

## Key Design Details

- The prompt includes parent programs, results, instructions, and sometimes meta information
- The coding agent has access to the full repo, but code regions for improvement are **explicitly marked** with `# EVOLVE-BLOCK-START` and `# EVOLVE-BLOCK-END`
- The **meta-prompt co-evolves** with instructions and context, similar to how solution programs are evolved

## Ablations

The value of the following design choices is demonstrated empirically:

- The evolution procedure itself
- Context in prompts
- Meta-prompts
- Full-file evolution (vs. diff-only)
- Stronger LLMs

![AlphaEvolve ablations](assets/lilianweng-harness-2026-07-04/alphaevolve-plot.png)
*Ablations show the value of several designs in AlphaEvolve. (Image source: Novikov et al. 2025)*

## When It Works Best

- Matrix multiplication
- GPU kernel optimization
- Algorithm contests
- Datacenter scheduling

These are domains where candidates are automatically evaluable and fitness is easy to quantify — exactly the conditions evolutionary search needs.

## Related

- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Entities/shinkaevolve]] — sample-efficient descendant
- [[Entities/darwin-godel-machine]] — sibling work that evolves the harness itself
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
