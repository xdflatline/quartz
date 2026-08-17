---
title: "SDLC as Context Engineering"
details: "Architectural principle that the software development lifecycle itself — not file-level instructions like AGENTS.md — is the operational context an AI agent actually needs. Operational decisions (what 'done' means, which paths are off-limits, when to slice vs. ship, when to escalate) are embedded in how work gets specified, reviewed, tested, and shipped, so redesigning the SDLC for agent usability reshapes every stage of the lifecycle."
tags:
  - concept
  - agent
  - context-engineering
created: 2026-08-17
updated: 2026-08-17
type: concept
---

# SDLC as Context Engineering

**Source:** [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

The thesis from Daniel Kravets' LeadDev write-up: file-level context engineering (`AGENTS.md`) has won, but is **not enough**. An agent cannot infer from a markdown file what "done" means for a feature, which paths are off-limits, when to slice a change vs. ship whole, when to escalate, or which test belongs to which behavior. That operational context is structurally embedded in the SDLC — specification, review, test, ship — so the SDLC itself must be redesigned for agent usability, not just augmented with file instructions.

> "The same structure that lets 10 human engineers coordinate is what lets the 11th contributor – an AI agent – operate reliably."
> — Daniel Kravets, Vendict

## Core Content

### Why AGENTS.md Alone Fails

A clean `AGENTS.md` does not give the agent:
- What "done" means for a specific feature
- Which critical paths are strictly off-limits
- When to slice a large change vs. ship it whole
- When to escalate an edge case to a human vs. fix it in place
- Which kind of test belongs to which kind of behavior

These are not file-level facts. They are workflow-level commitments.

### Five Redesign Goals

Kravets names five goals evaluated against every downstream choice. Four mirror DORA's high-performer research; one is new for 2026.

| # | Goal | DORA Equivalent |
|---|------|-----------------|
| 1 | **Velocity** — substantially faster than a year ago, not by 50%; agents take meaningful share of work | (composite) |
| 2 | **Mainline safety** — `main` stays deployable at all times | Trunk-based dev, fast recovery |
| 3 | **Agent usability as first-class concern** — design for humans *and* agents from the start | — (new for 2026) |
| 4 | **Operational clarity** — anyone sees what is live, planned, experimental, which session changed what | Small batches |
| 5 | **Incremental adoption** — adoptable in days, hardened over weeks, forgiving in flight | Low change failure rate |

**The new goal reshapes the other four.** Agent usability is not bolted on; it changes what "trunk-based" means, what "small batches" means, what "fast recovery" means.

### Resulting System Shape

The Vendict redesign (one month, small team) produced:

- **Monorepo as shared context boundary** — agent and human see the same code; ownership/build/deploy live in separate systems
- **Three document lifecycles** — `docs/` (merged truth), `plans/` (execution artifacts, transient), `docs/adr/` (durable, never deleted, only superseded)
- **Four execution lanes** (A/B/C/D) gating review and approval
- **Standards layer in `docs/standards/`** — profiles authored once, cited by path from every consumer (agent, CI, reviewer, dev env)
- **Spec + plan as separate artifacts in one PR** — product/system review of spec, R&D review of plan
- **Builder-reviewer separation at task granularity** — four separate subagents per feature, not one PR-review handoff
- **Devcontainer as execution boundary** — limits credential and repository surface, leaves network open

### The Endgame

> "Reviewing documentation instead of code, and keeping documentation precise enough that both agents and humans can act on it without asking."

Documentation becomes the load-bearing artifact; the SDLC exists to keep it precise.

## Key Insights

1. **File-level context is necessary but not sufficient.** Workflow-level commitments (when to escalate, what to slice, how to classify failure) cannot live in a single markdown file because they are not declarative rules — they are patterns enforced by the system.
2. **Agent usability is a first-class design goal, not a retrofit.** Adding agent affordances to a human-only SDLC produces friction on both sides. Designing for both from the start changes the shape of every other goal.
3. **The SDLC must be tunable in flight.** Kravets explicitly avoided designing it perfectly upfront — "Designing the perfect SDLC in advance would have cost more than it saved." The system must be adoptable in days and forgiving when something needs adjustment.

## Related Concepts

- [[Concepts/agentic-harness-engineering-ahe]] — broader framework for treating agent tooling + repo conventions as a runtime
- [[Concepts/context-as-evolving-playbook]] — context is not a static file but an evolving artifact
- [[Concepts/four-execution-lanes]] — the A/B/C/D gating structure that makes the SDLC legible to agents
- [[Concepts/standards-layer-with-path-citation]] — `docs/standards/` profiles authored once, consumed many times
- [[Concepts/builder-reviewer-task-granularity]] — task-level separation, not PR-level

## References

- Raw Article: [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]]
- Original: https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering