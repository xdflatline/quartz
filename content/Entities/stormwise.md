---
title: "Stormwise"
details: "Severe-weather assistant built on Claude by Kadharmoideen Fadurudeen, structured as a two-stage pipeline: fetch official National Weather Service alerts, then let the model answer with them in context. Used as the evaluation vehicle for the source article's failure lessons — 117 cases from real alerts, measured false reassurance, token-budget behaviour on complex cases, and the unreliability of pattern-matching scoring. Write-up on arXiv 2611.05290."
tags:
  - entity
  - agent
  - evaluation
created: 2026-11-26
updated: 2026-11-26
type: entity
source: "https://kadhar.dev/blog/multi-agent-systems-from-scratch"
---

# Stormwise

**Source:** [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]]
**Category:** Project
**Repository:** not published in the source
**Website:** https://arxiv.org/abs/2611.05290 (evaluation write-up)

---

## Overview

Stormwise is a **severe-weather assistant built on Claude** by Kadharmoideen Fadurudeen. Its architecture is deliberately minimal: at its core it is a **pipeline of two stages** — retrieve the official alerts, then let the model answer the user's question with those alerts in hand. It is the article's counterweight to the dinner-recommender example: the same author runs one agent for a small task and a two-stage pipeline for a task where the evidence source is external and authoritative.

Its value to the garden is as an **evaluation vehicle**, not as a product. The article reports its failure lessons because they were measured, not asserted.

## Key Details

### Architecture

- **Stage 1:** fetch official National Weather Service alerts.
- **Stage 2:** the model answers the user's question with the alerts in context.
- No orchestration framework, no agent-to-agent negotiation — the two stages are wired explicitly.

### Evaluation

- **117 cases** built from real NWS alerts.
- 69 cases involve an active warning; false reassurance ("conditions are calm") was measured on that subset.
- Results: 38% false reassurance without alert access; 45% with an "admit you cannot see official alerts" instruction added; 0% with the real alerts and a plain prompt.
- 342 responses were hand-labelled after the pattern-matching scorer was found to have missed 53 of 57 real cases.
- Reported as arXiv **2611.05290**.

### Failure lessons attributed to it

1. **Test alerts consumed as live warnings** — the pipeline treated weather-service *test* alerts as real warnings, and the model believed them. The defect was in the stage before the model.
2. **A token budget sized for everyday questions failed on the complex cases** — in a storm, those are the cases that matter most.
3. **The automated checker was wrong** — a simple pattern-matching script for false reassurance missed 53 of 57 real cases and inverted the conclusion.

### Boundaries

The source does not publish the code, the prompt text, the model version, or the per-case labels. The percentages are therefore single-system, single-evaluator results. Treat the direction (grounding beats disclaimer prompting; handoff validation beats careful prompting) as the durable claim, and the exact rates as illustrative.

## Related Concepts

- [[Concepts/grounding-over-honesty-prompting|Grounding Over Honesty Prompting]] — the measured 38% / 45% / 0% result this system produced
- [[Concepts/handoff-contract-validation|Handoff Contract Validation]] — the control that would have stopped the test alerts at the boundary
- [[Concepts/agent-first-pipeline-architecture|Agent-First Pipeline Architecture]] — the two-stage shape Stormwise implements
- [[Concepts/multiagent-system-failure-modes|Multiagent System Failure Modes]] — the broader taxonomy its failures map onto

## References

- Raw Article: [[Raw/kadhar-multi-agent-systems-from-scratch-2026-11-26]]
- Original: https://kadhar.dev/blog/multi-agent-systems-from-scratch
- Evaluation: https://arxiv.org/abs/2611.05290
