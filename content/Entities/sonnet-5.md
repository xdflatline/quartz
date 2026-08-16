---
title: "Sonnet 5"
details: "Anthropic Claude Sonnet 5 — the most recent model evaluated in the Anthropic Frontier Red Team's multi-agent study (Aug 2026). The only model that maintained both high PR merge fraction AND high code sharing in the fantasy game-building experiment — coordinating effectively without siloing."
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

Sonnet 5 is the latest generation of Anthropic's Sonnet model line, as referenced in the August 2026 Anthropic Frontier Red Team study of multi-agent systems.

## Multi-agent behavior

Sonnet 5 is the **only model** in the study that achieved both:
- High PR merge fraction (most PRs opened were merged)
- High code sharing (median agent made small contributions to files it did not own)

Earlier Sonnet 4.6 and Opus 4.6 had poor merge rates (PRs conflicted and were abandoned). Opus 4.8 and Mythos Preview "solved" the merge problem by siloing — each agent owned its own files and avoided conflict, but did not collaborate. **Sonnet 5 is the first model in the study to coordinate without siloing.**

## Related pages

- [[Raw/anthropic-multiagent-systems-2026-08-13|Anthropic source]]
- [[Entities/anthropic-frontier-red-team|Anthropic Frontier Red Team]]
- [[Concepts/multiagent-system-failure-modes|Multiagent system failure modes]]
