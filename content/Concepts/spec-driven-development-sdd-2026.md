---
title: "Spec-Driven Development (SDD) for Agentic Software Engineering"
details: "SDD is a discipline that reconstitutes team-scale software engineering contracts (accountability, verifiability, transferability) in specification-centric form, after vibe coding dissolves them. Introduced by Diaz et al. (arXiv:2609.00252, Aug 2026) as the conceptual and methodological foundation for operating Agentic Software Engineering (ASE) at team scale. The central claim: specifications are the authoritative referent for every human–agent interaction — briefing, reviewing, raising consultations, encoding standing norms — making recurrent collaboration definable, teachable, and measurable."
tags: [concept, software-engineering, agentic, harness]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
  - "Raw/sdd-agentic-software-engineering-arxiv-2026.md"
---

# Spec-Driven Development (SDD)

SDD is the enabling discipline proposed by [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]] for operating Agentic Software Engineering (ASE) at team scale.

## Definition

SDD treats the **specification** — not code, not chat history — as the authoritative contract substrate between humans and agents. Under SDD, every recurring human–agent interaction becomes an operation on a specification:

- a human briefs an agent by writing a specification;
- an agent requests consultation by citing a specification clause it cannot resolve;
- a human reviews agent output by auditing evidence against the specification;
- a team encodes its standing norms as normative specifications.

Without the substrate, none of these interactions has a referent; with it, they become definable, teachable, and measurable.

## Common misunderstandings the authors flag

- SDD is **not** a return to traditional waterfall requirements engineering. Specifications in SDD are executable, living artifacts that drive agents; they are not static documents reviewed once and shelved.
- SDD is **not** prompt engineering. A prompt is a per-session instruction; a specification is a durable, versioned, normative artifact shared across sessions and team members.
- SDD is **not** "more documentation". The specification's role is functional: it is the substrate the agent operates against, the medium of human review, and the carrier of team norms.

## Specification hierarchy

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 3]] shows the four-level hierarchy:

- **System specifications**: stable normative context of the project.
- **Feature specifications**: task-specific changes, derived from system specs.
- **Artifacts**: derived from specifications (code, tests, configurations).
- **Skills**: reusable procedural capabilities loaded on demand.

## Relationship to the harness

SDD is the *discipline*; the [[Concepts/agentic-harness-team-governance-sdd-2026|harness]] is the *operationalization*. The methodological harness (eight mechanisms across knowledge management, production support, and governance) is what lets a team adopt SDD in fragments without losing the discipline's benefits — though partial adoption captures a fraction of the value while paying most of the discipline cost.

## Related Concepts

- [[Concepts/specifications-as-contract-substrate-agentic-se]] — why specifications (not code or chat) are the authoritative referent.
- [[Concepts/agentic-harness-team-governance-sdd-2026]] — the operationalization of SDD at team scale.
- [[Concepts/harness-mechanism-context-engineering-sdd-2026]] — what an agent knows within a session.
- [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026]] — what the team knows across sessions, the loop-closing mechanism.
- [[Concepts/human-agent-interaction-patterns-sdd-2026]] — the five recurring interaction patterns the substrate supports.