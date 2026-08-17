---
title: "Daniel Kravets"
details: "Founding engineer at Vendict and author of the LeadDev article 'Your SDLC is Your Context Engineering' (August 10, 2026), documenting a one-month SDLC redesign for agent usability at Vendict — covering monorepo structure, four execution lanes, test subagent isolation, builder-reviewer separation at task granularity, and the devcontainer-as-execution-boundary pattern."
tags:
  - entity
  - agent
  - context-engineering
created: 2026-08-17
updated: 2026-08-17
type: entity
---

# Daniel Kravets

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Person

---

## Overview

Daniel Kravets is the founding engineer at Vendict. His August 2026 LeadDev article "Your SDLC is Your Context Engineering" documents the one-month SDLC redesign he led at the TPRM startup, arguing that the SDLC itself — not AGENTS.md files — is the operational context an AI agent needs. The article has become a reference point for the "agent usability as first-class design goal" framing.

## Key Details

- **Role:** Founding engineer, Vendict
- **Notable writing:** "Your SDLC is Your Context Engineering" — LeadDev, August 10, 2026
- **Thesis:** In the agentic era, the SDLC is the context. Operational decisions (what "done" means, when to escalate, how to slice) are structurally embedded in the workflow — not in a markdown file.
- **Practical contribution:** Detailed account of how a real SDLC was redesigned around agent usability, including reproducible patterns (lanes, standards layer, plan-implementer skill, devcontainer boundary).

## Related Concepts

- [[Concepts/sdlc-as-context-engineering]] — the core thesis Kravets argues
- [[Concepts/four-execution-lanes]] — Lane A/B/C/D
- [[Concepts/standards-layer-with-path-citation]] — `docs/standards/` profile pattern
- [[Concepts/builder-reviewer-task-granularity]] — `plan-implementer` skill architecture
- [[Concepts/test-design-subagent-isolation]] — test designer isolation
- [[Concepts/devcontainer-as-execution-boundary]] — host-side execution boundary

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering