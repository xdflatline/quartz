---
title: "Vendict"
details: "AI-native third-party risk management (TPRM) startup. Source of the LeadDev article 'Your SDLC is Your Context Engineering' (Daniel Kravets, Aug 2026), which documents a one-month SDLC redesign built around agent usability — including monorepo, four execution lanes, standards layer, builder-reviewer separation at task granularity, and devcontainer-as-execution-boundary."
tags:
  - entity
  - agent
  - context-engineering
created: 2026-08-17
updated: 2026-08-17
type: entity
---

# Vendict

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Company
**Website:** https://www.vendict.com

---

## Overview

Vendict is an AI-native third-party risk management (TPRM) startup that automates enterprise security and compliance workflows. It is the source organization for the engineering-process write-up by founding engineer Daniel Kravets, documenting a one-month SDLC redesign built explicitly around agent usability — the SDLC is treated as the agent's context layer rather than relying on AGENTS.md-style file-level instructions alone.

## Key Details

- **Sector:** TPRM (third-party risk management)
- **Product:** AI-native platform automating enterprise security and compliance workflows
- **Team:** Small engineering team (per the article, "my team is small, and the redesign took us roughly a month")
- **Stack:** Go (Lambda functions), Python ECS services, TypeScript/Vue frontend — a polyglot monorepo
- **Tooling:** Cursor, Claude Code, Codex, CodeRabbit as agent + review tools
- **Notable for:** Treating SDLC redesign as the agent-usability intervention (not just adding AGENTS.md)

## Related Concepts

- [[Concepts/sdlc-as-context-engineering]] — the thesis article Vendict operationalized
- [[Concepts/four-execution-lanes]] — Lane A/B/C/D as defined by Vendict's process
- [[Concepts/standards-layer-with-path-citation]] — Vendict's `docs/standards/` profile pattern
- [[Concepts/builder-reviewer-task-granularity]] — Vendict's `plan-implementer` skill architecture
- [[Concepts/test-design-subagent-isolation]] — Vendict's separate test designer subagent
- [[Concepts/devcontainer-as-execution-boundary]] — Vendict's host-side threat model

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering