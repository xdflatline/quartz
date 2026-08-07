---
title: "GEPA"

details: "GEPA is a prompt-evolution method that reads trajectories of trial and error, reflects on what went wrong, and proposes prompt updates in natural language. It is one of the foundational methods in the broader [[Concepts/evolutionary-search-for-harnesses]] family, alongside Promptbreeder and AlphaEvolve."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2507.19457
---

# GEPA

**Source:** Agrawal et al., "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning," arXiv:2507.19457, 2025.

## Overview

**GEPA** (Reflective Prompt Evolution) combines **reflection-based prompting** with **evolutionary search**. It uses natural language reflection over trajectories of trial and error to propose prompt updates.

## How It Works

1. Run a prompt on a set of tasks
2. Collect trajectories — what the model did, where it succeeded, where it failed
3. Reflect on the trajectories in natural language: what went wrong, what could be improved
4. Propose a new prompt based on the reflection
5. Evaluate, keep if better, repeat

## Why "Reflective" Matters

The reflection step is what makes GEPA different from random mutation: instead of trying random edits, the model *reads* the trajectory, *understands* what went wrong, and *proposes* a targeted fix. The result is a more sample-efficient search than blind mutation.

## Relationship to Other Methods

- **Promptbreeder** ([[Entities/promptbreeder]]) — also evolves prompts, but uses LLM-driven mutations; the mutations themselves evolve
- **AlphaEvolve** ([[Entities/alphaevolve]]) — evolves programs, not prompts; uses frozen-LLM diffs
- **AFlow** ([[Entities/aflow]]) — evolves workflow graphs via MCTS

GEPA is the simplest "read trajectory, reflect, propose edit" instance in this family.

## Related

- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Entities/promptbreeder]] — the predecessor
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
