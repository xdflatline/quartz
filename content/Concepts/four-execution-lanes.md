---
title: "Four Execution Lanes (A/B/C/D)"
details: "Workflow pattern where every change is routed through one of four named lanes based on risk and design surface: Lane A (standard), Lane B (with spec-and-plan step), Lane C (control-plane, auth, data — CODEOWNERS + two approvals), Lane D (experiments, isolated). Lane assignment appears in Makefile targets, the AI-review config, AGENTS.md files, and human checklists — so all consumers see the same gating rules."
tags:
  - concept
  - agent
  - tooling
created: 2026-08-17
updated: 2026-08-17
type: concept
---

# Four Execution Lanes (A/B/C/D)

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

A "lane" is a designated path a change moves through, with the gates attached. Lane assignment is shared vocabulary across the agent, the AI reviewer (CodeRabbit), the CI system, and human reviewers. The same lane label appears in Makefile targets, the review config, AGENTS.md files, and human checklists. This makes the SDLC legible to all consumers from the same set of labels.

## Core Content

### The Four Lanes

| Lane | Purpose | Added Requirements |
|------|---------|--------------------|
| **Lane A** | Standard path for most work | Standard review |
| **Lane B** | Meaningful design surface | Adds spec-and-plan step before implementation |
| **Lane C** | Control-plane paths, CI config, auth, data access | Two approvals + CODEOWNERS enforcement |
| **Lane D** | Experiments | Isolated, clearly scoped changes |

### How the Lanes Show Up

- **Makefile targets** — lane-aware variants of `make test`, `make build`, etc.
- **CodeRabbit config** — path routing per lane; if a PR is marked Lane A but touches a Lane B or Lane C surface, it is escalated instead of being treated as a standard change
- **AGENTS.md files** — lane-aware deny-lists and required profiles per lane
- **Human review checklists** — same labels, same escalation rules

### Lane-Aware Escalation

The pattern is enforced *across* consumers, not just within one. If the PR metadata says Lane A but the diff touches Lane B or Lane C paths, the AI reviewer escalates rather than green-lighting — even if the substantive change is fine. This catches misclassification before the human reviewer has to.

### Known Side Effect

> "The system can make agents stricter than necessary. Even when a change is approved, a Lane A agent reviewing the change can warn 'this file wasn't supposed to change' if the plan did not include it. That is still better than the opposite problem."

The side effect is acceptable because the failure mode of false-positive strictness is recoverable (human override), while the failure mode of false-permissive review (sensitive file silently modified) is not.

## Key Insights

1. **Shared vocabulary is the point.** Lane labels are not just project management — they are a shared ontology the SDLC exposes to agents, CI, reviewers, and humans.
2. **Cross-consumer enforcement catches misclassification.** The same lane name appearing in Makefile + CodeRabbit + AGENTS.md + checklist means a Lane A PR touching a Lane C file is flagged everywhere, not just by one consumer.
3. **Lane C's two-approval + CODEOWNERS rule encodes the principle that some surfaces need humans in the loop regardless of agent confidence.**

## Related Concepts

- [[Concepts/sdlc-as-context-engineering]] — the lanes are an instance of the broader principle
- [[Concepts/standards-layer-with-path-citation]] — path-based citations are how lane-aware rules propagate
- [[Concepts/hitl-approval-gates-for-tool-calls]] — Lane C's two-approval rule is a HITL gate at the SDLC level

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering