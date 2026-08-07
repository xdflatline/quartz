---
title: "Rahul Garg"
details: "Principal Engineer at Thoughtworks, based in Gurgaon, India. Author of 'The Orchestrator's Tax' (martinfowler.com, 16 July 2026), which coined the term 'cognitive locality' and proposed four standing rules for protecting the orchestrator's working memory in long-running multi-agent sessions. Background in DDD, Clean Architecture, and AI for engineering excellence."
tags:
  - entity
  - agent
created: 2026-08-07
updated: 2026-08-07
type: entity
sources:
  - "[[Raw/martinfowler-orchestrators-tax-2026-07-16]]"
---

# Rahul Garg

**Category:** Person
**Affiliation:** Thoughtworks (Principal Engineer, Gurgaon, India)
**Source:** [[Raw/martinfowler-orchestrators-tax-2026-07-16]]

---

## Overview

Rahul Garg is a Principal Engineer at [[Entities/thoughtworks]] based in Gurgaon, India, working at the intersection of maintainable software craft (DDD, Clean Architecture) and AI-assisted engineering. His July 2026 post on Martin Fowler's site, *The Orchestrator's Tax*, is the source of the term **cognitive locality** and the proposed practice of treating subagents as a tool for protecting the orchestrator's working memory rather than primarily as a parallelism lever.

## Key Details

### Authored work in the wiki

- [[Raw/martinfowler-orchestrators-tax-2026-07-16]] — "The Orchestrator's Tax" (16 July 2026). Coins cognitive locality; introduces four standing rules for orchestrator hygiene; argues context pollution (not token spend) is the dominant cost in long-running multi-agent sessions. Acknowledges Birgitta Böckeler's *Harness Engineering* and his own earlier *Context Anchoring* piece as related work. Martin Fowler is thanked for guidance and feedback on the post.

### Recurring themes

- **The orchestrator is unique in the system.** Across a long session it is the only part that accumulates design rationale, architectural constraints, and trade-off history. Subagents are meant to be disposable; their exploration, failed approaches, and noisy intermediate reasoning should never return to the main thread.
- **Tokens vs. context is the central distinction.** Token costs are one-time. Context pollution compounds — it taxes every later turn in the session.
- **A bigger context window does not fix pollution.** Pollution is an attention problem, not a space problem.
- **Standing-rule discipline is itself a cost.** Every line in `CLAUDE.md` is paid on every future session. State the missing fact; resist encoding decision procedures as process.

## Related Concepts

- [[Concepts/cognitive-locality]] — the term he coined
- [[Concepts/orchestrators-tax]] — the framing he named
- [[Concepts/working-memory-preservation-subagent-purpose]] — the reframe of subagent purpose that follows from the framing
- [[Entities/thoughtworks]] — his employer

## References

- Raw Article: [[Raw/martinfowler-orchestrators-tax-2026-07-16]]
- Original: https://martinfowler.com/articles/orchestrator-tax.html
- Author bio on the post: "Rahul is a Principal Engineer at Thoughtworks, based in Gurgaon, India. He is passionate about the craft of building maintainable software through DDD and Clean Architecture, and explores how AI can help teams achieve engineering excellence."
