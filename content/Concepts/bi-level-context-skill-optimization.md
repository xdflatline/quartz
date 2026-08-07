---
title: "Bi-level Context + Skill Optimization (MCE)"

details: "MCE formalizes a skill as a context function c_s=(ρ_s, F_s) with static components (prompts, knowledge bases, code libraries) and dynamic operators (search, selection, filtering, formatting). The inner loop finds the best context for a fixed skill on training data; the outer loop finds the optimal skill that gives the best validation performance. Skills undergo agentic crossover over a history H of (skill, context, train-utility, val-utility) tuples. The base-level context engineer executes the current skill and learns the context function from rollout feedback. Both levels run in agentic coding envs with a standard tool set {Read, Write, Edit, Bash, Glob, Grep, TodoWrite}."
tags:
  - concepts
  - context-engineering
  - harness
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Bi-level Context + Skill Optimization (MCE)

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Learning Mechanism
**Status:** Active research area (arXiv 2026)

---

## Overview

**Meta Context Engineering (MCE; Ye et al. 2026)** separates **mechanism** (how to manage context) from **artifact content** (what is in context), running **skill evolution at the meta-optimization level** and **context optimization at the base level**. ACE (see [[Concepts/context-as-evolving-playbook]]) gives you the base level; MCE adds a meta level that evolves the structure of how you engineer context.

## Core Content

### The Skill Formalism

A skill $s \in \mathcal{S}$ defines a context function $c_s = (\rho_s, F_s)$ and maps an input $x$ to context $c = F_s(x; \rho_s)$:

- $\rho_s = \{\rho_1, \dots, \rho_m\}$ are **static components** — prompts, knowledge bases, code libraries
- $F_s = \{F_1, \dots, F_k\}$ are **dynamic operators** — search, selection, filtering, formatting

The context function is instantiated as a **collection of files in a dedicated directory**, including both static (`skill.md`) and dynamic (context + data rollouts) components.

### The Bi-level Optimization

$$
\text{Inner: } c_s^* = \arg\max_{c_s} J_\text{train}(c_s; s) \quad
\text{Outer: } s^* = \arg\max_{s \in \mathcal{S}} J_\text{val}(c_s^*)
$$

- **Inner** — given a fixed skill $s$, find the best context $c_s^*$ on training data (this is roughly what ACE does)
- **Outer** — given a set of skills, find the skill $s^*$ that produces the best validation performance

### Skill History and Agentic Crossover

The skill database tracks the history $\mathcal{H}_{k-1} = \{(s_i, c_i, J_i^\text{train}, J_i^\text{val})\}_{i=1}^{k-1}$.

A **meta-level agent** performs **agentic crossover** over prior skills to create a new skill given a task $\tau$:

$$
s_k = \text{crossover}(\tau, \mathcal{H}_{k-1})
$$

Crossover is the LLM-driven analog of genetic crossover: read prior skills and their scores, mix the successful parts, drop the failing parts, output a new candidate skill.

Then a **base-level context engineer** executes the skill and learns the context function from rollout feedback $\mathcal{R}_k$:

$$
c_k = \text{engineer}(\tau, s_k; c_{k-1}^*, \mathcal{R}_k)
$$

![MCE framework](assets/lilianweng-harness-2026-07-04/mce.png)
*MCE framework. (Image source: Ye et al. 2026)*

### The Standard Tool Set

Both meta-level and base-level optimization run in agentic coding envs with:

$$
\mathcal{T} = \{\texttt{Read}, \texttt{Write}, \texttt{Edit}, \texttt{Bash}, \texttt{Glob}, \texttt{Grep}, \texttt{TodoWrite}\}
$$

This is intentionally a **subset of the full coding-agent tool taxonomy** (no MCP, no web search, no agent delegation). Skills evolve within a sandbox.

### MCE vs ACE

| Property | ACE | MCE |
|----------|-----|-----|
| Optimized object | The context bullets | The skill (mechanism) AND the context (content) |
| Optimization level | Base level | Bi-level (meta + base) |
| Skill structure | Handcrafted | Evolved via agentic crossover |
| Update rule | Handcrafted (curator) | Handcrafted tool, but the rule itself is searched |

MCE is a strict superset of ACE in capability, with a more complex search procedure as the cost.

## Key Insights

1. **Mechanism is a first-class optimization target.** MCE's central move is treating "how you structure context" as something to search over, not just the content.
2. **Skills are files.** The skill + context state is a directory in the file system — so all the file-as-memory properties carry over (audit, recover, replay).
3. **The inner/outer split composes.** The outer loop searches skills; the inner loop fits context to a skill. Each can use a different agent, model, or search algorithm.
4. **Crossover is the LLM's analog of mutation.** Where a genetic algorithm mutates bit strings, the LLM reads prior skills and "crosses" them by recombining good parts.

## Related Concepts

- [[Concepts/context-as-evolving-playbook]] — ACE, the base level
- [[Concepts/agentic-crossover-skill-evolution]] — the crossover mechanism in detail
- [[Concepts/meta-harness-outer-loop]] — one level deeper still: the harness code itself
- [[Concepts/evolutionary-search-for-harnesses]] — broader evolutionary search applied to harnesses
- [[Concepts/file-system-as-agent-memory]] — skills and contexts are file-backed

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Paper: Ye et al., "Meta Context Engineering via Agentic Skill Evolution," arXiv:2601.21557, 2026.
- Related Entity: [[Entities/mce-paper]]
