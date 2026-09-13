---
title: "Specifications as Contract Substrate for Agentic SE"
details: "A specification in SDD is the authoritative referent for every human–agent interaction: briefing, reviewing, raising consultations, encoding standing norms. The substrate replaces the chat history that vibe coding leaves behind, restoring accountability (you can cite a clause), verifiability (output can be audited against a clause), and transferability (a new team member or agent can read the contract). Without the substrate, none of these interactions has a referent; with it, they become definable, teachable, and measurable."
tags: [concept, software-engineering, agentic, harness, specification]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Specifications as Contract Substrate

The central architectural claim of [[Concepts/spec-driven-development-sdd-2026|SDD]]: specifications are the substrate over which all human–agent interaction is defined.

## Three problems the substrate solves

Diaz et al. organize the motivation around three problems:

- **The contract problem.** Without a durable artifact beyond the chat, who is accountable for what an agent produced? Specifications make accountability citable.
- **The coordination problem.** When multiple humans and multiple agents collaborate on the same system, who owns which decision? Specifications make coordination roles referenceable.
- **The trust problem.** How does a human know whether to accept an agent's output? Specifications make acceptance criteria auditable.

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 4]] shows specifications as the substrate through which contracts, coordination, and trust emerge. Without specifications, these must be reconstructed from code and conversational history; with SDD, they become a shared contract enabling auditable evidence and scalable trust.

## Operational implications

The substrate reframes every interaction as an operation on a specification:

- **Briefing**: the human writes a specification.
- **Consultation**: the agent cites a specification clause it cannot resolve.
- **Review**: the human audits the agent's evidence against the specification.
- **Encoding norms**: the team writes standing rules as normative specifications.

Each operation has a referent; each can be taught, audited, and measured. Vibe coding has none of these properties — its substrate is the chat transcript, which is per-session and per-developer.

## Related Concepts

- [[Concepts/spec-driven-development-sdd-2026]] — the discipline this substrate enables.
- [[Concepts/agentic-harness-team-governance-sdd-2026]] — the harness is what operationalizes the substrate at team scale.
- [[Concepts/harness-mechanism-normative-specifications-sdd-2026]] — the mechanism by which team norms are encoded into the substrate.
- [[Concepts/harness-mechanism-executable-specifications-sdd-2026]] — the mechanism that makes the substrate evaluable rather than merely readable.