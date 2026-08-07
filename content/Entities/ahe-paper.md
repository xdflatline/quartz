---
title: "AHE paper (Agentic Harness Engineering)"

details: "AHE identifies seven editable harness components: system prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, long-term memory. Two hard constraints: (1) the runs directory, tracer, verifier, and LLM config are read-only, disabling a set of reward hacking; (2) every edit has a manifesto entry with the failure evidence name, inferred root cause, targeted fix, and predicted impact. On Terminal-Bench-2, AHE beat human-designed harnesses (OpenCode, Terminus-2, Codex) except for the Hard tier."
tags:
  - entities
  - harness
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2604.25850
---

# AHE paper (Agentic Harness Engineering)

**Source:** Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses," arXiv:2604.25850, 2026.

## Overview

Observability-driven automatic evolution of coding-agent harnesses. The paper identifies the bottleneck of harness evolution as **observability** — when a rollout fails, you need to know which component is responsible; every edit should be grounded by evidence.

## The Three Observability Pillars

1. **Component observability** — every editable component has a file-system representation
2. **Experience observability** — per-task analysis reports aggregated into a benchmark overview
3. **Decision observability** — every edit is a falsifiable file-level claim with a manifesto entry

## The Seven Editable Components

System prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, long-term memory.

## The Two Hard Constraints

1. The runs directory, tracer, verifier, and LLM config are **read-only** — disables reward hacking
2. Every edit has a **manifesto entry** (failure evidence name, inferred root cause, targeted fix, predicted impact)

## Result

On Terminal-Bench-2, AHE beat human-designed harnesses (OpenCode, Terminus-2, Codex) except for the Hard tier and a few other self-evolve baselines (ACE, TF-GRPO). The same frozen harness transfers to SWE-bench-verified — evidence the evolved harness encodes engineering experience, not benchmark-specific optimization.

## Related

- [[Concepts/agentic-harness-engineering-ahe]] — the concept
- [[Concepts/evidence-driven-harness-edits]] — the manifesto-entry pattern
- [[Entities/terminus-2]] — a baseline AHE beats
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
