---
title: "MCE paper (Meta Context Engineering via Agentic Skill Evolution)"

details: "The MCE paper is the meta-level extension of the ACE line. The bi-level formalism, the skill history H, the agentic crossover operator, and the standard tool set {Read, Write, Edit, Bash, Glob, Grep, TodoWrite} are all defined here. Implementation-wise, a context function is a collection of files in a dedicated directory including both static (skill.md) and dynamic (context + data rollouts) components."
tags:
  - entities
  - harness
  - context-engineering
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2601.21557
---

# MCE paper (Meta Context Engineering via Agentic Skill Evolution)

**Source:** Ye et al., "Meta Context Engineering via Agentic Skill Evolution," arXiv:2601.21557, 2026.

## Overview

The bi-level optimization framework behind [[Concepts/bi-level-context-skill-optimization]]. Inner loop: best context for a fixed skill. Outer loop: best skill for a validation set. Skills are evolved via **agentic crossover** over the history of past skills, contexts, and utilities.

## Formalism

A skill $s \in \mathcal{S}$ defines a context function $c_s = (\rho_s, F_s)$ with static components $\rho_s$ (prompts, knowledge bases, code libraries) and dynamic operators $F_s$ (search, selection, filtering, formatting). A skill is instantiated as files in a dedicated directory, including both static (`skill.md`) and dynamic (context + data rollouts) components.

## The Standard Tool Set

Both meta-level and base-level optimization run in agentic coding envs with:

$$
\mathcal{T} = \{\texttt{Read}, \texttt{Write}, \texttt{Edit}, \texttt{Bash}, \texttt{Glob}, \texttt{Grep}, \texttt{TodoWrite}\}
$$

This is intentionally a subset of the full coding-agent tool taxonomy.

## Related

- [[Concepts/bi-level-context-skill-optimization]] — the concept
- [[Concepts/agentic-crossover-skill-evolution]] — the crossover mechanism
- [[Entities/ace-paper]] — the base level
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
