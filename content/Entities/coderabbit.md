---
title: "CodeRabbit"
details: "AI-powered code review tool used at Vendict as the AI reviewer in their SDLC. Configured thinly because the rules live in version-controlled markdown profiles (`docs/standards/code-review-rubric.md`), not in YAML — the CodeRabbit config is mostly path routing per lane. Catches the residual failures isolation cannot — tests effectively mocked into passing, weak assertions, missing non-mocked smoke tests on major changes, and lane misclassification (Lane A PR touching Lane B/C surface is escalated)."
tags:
  - entity
  - agent
  - tooling
created: 2026-08-17
updated: 2026-08-17
type: entity
---

# CodeRabbit

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Tool

---

## Overview

CodeRabbit is an AI-powered code review tool used as one of the consumers of the standards layer in Vendict's SDLC. Its configuration is intentionally thin — the rules live in version-controlled markdown profiles, and the CodeRabbit config is mostly path routing: for files matching this pattern, review against `docs/standards/python-profile.md` and `docs/standards/code-review-rubric.md`. Lane-aware escalation is part of the same layer: a PR marked Lane A that touches a Lane B or Lane C surface is escalated rather than treated as standard change.

## Key Details

- **Role in Vendict's SDLC:** AI reviewer that reads the same standards as humans and as the agent
- **Configuration style:** Thin — rules live in markdown, not YAML
- **What it catches:**
  - Tests that are effectively mocked into passing
  - Missing non-mocked smoke tests on major changes
  - Weak assertions that prove nothing
  - Lane misclassification (Lane A PR touching Lane B/C surface)
- **Replaces:** Vendict does not depend on it specifically — the methodology works with any equivalent AI reviewer

## Related Concepts

- [[Concepts/standards-layer-with-path-citation]] — CodeRabbit is one consumer of the standards layer
- [[Concepts/test-design-subagent-isolation]] — CodeRabbit catches what the test subagent cannot
- [[Concepts/four-execution-lanes]] — lane-aware escalation is encoded in the CodeRabbit config
- [[Concepts/builder-reviewer-task-granularity]] — CodeRabbit reads the same canonical `code-review-rubric.md`

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering