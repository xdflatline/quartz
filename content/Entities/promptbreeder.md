---
title: "Promptbreeder"

details: "Promptbreeder is the early predecessor of the modern [[Concepts/evolutionary-search-for-harnesses]] family. Its distinctive move: the mutations (the instructions to an LLM to mutate a task prompt) are themselves evolved. This self-referential layer — the system that improves the prompts is itself being improved — anticipates STOP and the modern self-improving-harness line."
tags:
  - entities
  - harness
  - prompt-engineering
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2309.16797
---

# Promptbreeder

**Source:** Fernando et al., "Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution," arXiv:2309.16797, 2023.

## Overview

**Promptbreeder** is an early entry in the prompt-evolution lineage. It optimizes task-specific prompts through a **rich set of mutation operations**, and **the mutation prompts themselves are also improved through evolution** — hence "self-referential."

## How It Works

1. Initialize a population of task prompts and a population of mutation prompts
2. Apply mutations to task prompts to produce candidates
3. Evaluate candidates on downstream tasks
4. Evolve both populations — task prompts (by fitness) and mutation prompts (by their ability to produce good mutations)
5. Repeat

## Why It's Notable

The **self-referential layer** (mutations that evolve) anticipates STOP ([[Concepts/self-taught-optimizer-stop]]) and the modern self-improving-harness line. The idea that the system that improves the prompts is itself being improved is the conceptual seed that Meta-Harness, DGM, and AHE inherit.

## Related

- [[Entities/gepa]] — the reflective successor
- [[Concepts/evolutionary-search-for-harnesses]] — the family
- [[Concepts/self-taught-optimizer-stop]] — the self-improvement successor
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
