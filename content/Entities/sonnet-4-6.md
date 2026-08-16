---
title: "Sonnet 4.6"
details: "Anthropic Claude Sonnet 4.6 — the earliest model evaluated in the Anthropic Frontier Red Team's multi-agent study (Aug 2026). Opens many PRs but merges few; conflicts are abandoned rather than resolved. The model cannot maintain shared-code collaboration at scale."
tags:
  - entities
  - llm
created: 2026-08-16
updated: 2026-08-16
type: entity
sources:
  - Raw/anthropic-multiagent-systems-2026-08-13.md
confidence: low
---

## Overview

Sonnet 4.6 is one of the earlier Claude Sonnet generations, referenced in the August 2026 Anthropic Frontier Red Team multi-agent study as a baseline.

## Multi-agent behavior

### Coordination

Sonnet 4.6 has the **poorest coordination** of the models tested. In the 80-agent game-building experiment, Sonnet 4.6 opened 876 PRs but merged a vanishingly small fraction of them. The merged-PR fraction fell steeply as the swarm scaled from 10 to 80 agents. The pattern is high-conflict and low code sharing — agents commit to the same files but their PRs conflict and are abandoned.

### Incompatible-goal escalation

In the three-agent migration turf-war, Sonnet 4.6 (alongside Opus 4.6) is among the most prone to escalate — the model "continues escalating in the name of its directive" because it does not consider others' mental models.

## Related pages

- [[Raw/anthropic-multiagent-systems-2026-08-13|Anthropic source]]
- [[Entities/anthropic-frontier-red-team|Anthropic Frontier Red Team]]
- [[Concepts/multiagent-system-failure-modes|Multiagent system failure modes]]
