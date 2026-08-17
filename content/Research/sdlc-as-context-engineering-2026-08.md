---
title: "Research Index: SDLC as Context Engineering"
details: "Synthesis of the LeadDev write-up by Daniel Kravets (Vendict, Aug 2026) — the thesis that the SDLC itself, not AGENTS.md files, is the agent's operational context. Covers the Vendict redesign: monorepo, four execution lanes, three document lifecycles, standards layer with path citation, test subagent isolation, builder-reviewer separation at task granularity, devcontainer-as-execution-boundary, and the four-pronged rubric calibrated for AI-heavy review."
tags:
  - research
  - agent
  - context-engineering
created: 2026-08-17
updated: 2026-08-17
type: research
---

# Research Index: SDLC as Context Engineering

**Updated:** 2026-08-17
**Source:** LeadDev article by Daniel Kravets (Vendict), August 10, 2026

---

## Overview

Synthesis of the August 2026 LeadDev write-up "Your SDLC is Your Context Engineering" by Daniel Kravets (founding engineer, Vendict). The thesis: in the agentic era, the SDLC — not file-level instructions like AGENTS.md — is the operational context an AI agent actually runs on. Operational commitments (what "done" means, when to escalate, how to slice a change) cannot live in a single markdown file because they are not declarative rules — they are patterns enforced by the system. Therefore the SDLC itself must be redesigned for agent usability, with agent usability as a first-class design goal that reshapes every other goal.

Kravets documents the Vendict redesign: a one-month rebuild of a small team's development process around five goals (velocity, mainline safety, agent usability, operational clarity, incremental adoption), producing concrete artifacts — monorepo structure, three document lifecycles, four execution lanes, a `docs/standards/` profile layer, a `plan-implementer` skill spawning four subagents per feature, and a devcontainer-shaped execution boundary.

## Concepts

### Core Thesis
- [[Concepts/sdlc-as-context-engineering]] — the architectural principle that the SDLC itself is the agent's context

### Workflow Structure
- [[Concepts/four-execution-lanes]] — Lane A (most work) / B (with spec-and-plan) / C (control-plane, two approvals + CODEOWNERS) / D (experiments)
- [[Concepts/standards-layer-with-path-citation]] — `docs/standards/` profiles authored once, cited by path from every consumer

### Agent Architecture Within the SDLC
- [[Concepts/test-design-subagent-isolation]] — tests excluded from size caps + separate test designer subagent in isolated context
- [[Concepts/builder-reviewer-task-granularity]] — `plan-implementer` skill spawning four subagents (test designer, failure analyzer, verifier, linter) with circuit breakers
- [[Concepts/devcontainer-as-execution-boundary]] — host-side boundary: close credential surface, leave network open

## Tools & Projects

### Companies
- [[Entities/vendict]] — AI-native third-party risk management startup; source organization

### People
- [[Entities/daniel-kravets]] — founding engineer at Vendict; author of the article

### Tools
- [[Entities/coderabbit]] — AI-powered code reviewer; configured thinly because rules live in markdown, not YAML

## Raw Sources
- [[Raw/leaddev-sdlc-as-context-engineering-2026-08-10]] — full text of the LeadDev article (Aug 10, 2026)

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [LeadDev — Kravets](https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering) | SDLC as context | 2026-08-10 | Monorepo, four lanes, standards layer, test subagent isolation, builder-reviewer separation, devcontainer boundary |

## Cross-Cutting Themes

### Agent Usability as First-Class Goal
1. **Agent usability reshapes every other goal.** The five Vendict goals are not a list where agent usability is one item among five — it is the meta-goal that changes what the other four mean. "Trunk-based development" with agents looks different from trunk-based without; "small batches" with agents means something different.
3. **File-level context is necessary but insufficient.** A clean `AGENTS.md` does not tell an agent what "done" means for a specific feature, which paths are off-limits, when to slice vs. ship whole, when to escalate, or which test belongs to which behavior. These are workflow-level commitments.
5. **The SDLC must be tunable in flight.** Designing it perfectly upfront would have cost more than it saved. The system is adoptable in days, hardened over weeks, forgiving when something needs adjustment.

### Structural Isolation to Prevent Rationalization
1. **The implementation agent must not classify its own failures.** A separate failure analyzer makes the call; `UNCLEAR` is a first-class escalation state, not a fallback.
2. **The test designer must run in isolation from the implementation agent.** The same context cannot both drop an acceptance criterion and write a test verifying only the behavior shipped.
3. **Circuit breakers cap the loop.** Three test-fix cycles, two verification cycles, then escalate. Without hard caps, the agent burns cycles "almost working" indefinitely.

### One Source of Truth, Many Consumers
1. **Profiles authored once, cited by path.** Every consumer (agent, CI, reviewer, dev env, human) points at the same `docs/standards/` markdown. Vendor churn does not destroy accumulated rules — they live in the repo.
2. **Shared vocabulary across consumers.** Lane A/B/C/D appear in Makefile targets, CodeRabbit config, AGENTS.md files, and human review checklists. A Lane A PR touching Lane C paths is escalated everywhere, not just by one consumer.
3. **Verification has one interface.** `make ci`, `test`, `lint`, `fmt`, `build`, `run` work the same across languages, run by agent self-verify, CI, and human onboarding. Same surface, same outcome.

### Threat-Model Discipline
1. **One boundary, one threat.** The devcontainer is shaped for host-credential exfiltration, not for general sandboxing. Stricter boundaries (locked egress) were considered and rejected because they neutered research-shaped utility.
2. **Close the credential surface, leave the network surface open.** Network reach is necessary for research; the damage surface is exfiltration (creds, repo write).
3. **Production agent safety is a different problem.** Sandboxing, credential scoping, runtime governance for customer-facing agents — left out as the next article's topic. Out-of-scope discipline is itself part of the design.

## Next Research Directions

- [ ] Evaluate how the four-lane pattern (A/B/C/D) maps onto existing agent harnesses (Mastra, Mezmo Aura, Hermes) — which lanes each tool implicitly enforces today and where they fall short
- [ ] Benchmark whether test-designer isolation produces measurably better acceptance-criterion coverage than non-isolated test generation, using Vendict's 87%-on-small-diffs / 28%-on-large-diffs data as a baseline
- [ ] Compare `docs/standards/` path-citation patterns against vendor knowledge bases (CodeRabbit config, Cursor rules) — does rule-survival on tool swap match the article's claims in practice?
- [ ] Prototype a `UNCLEAR` failure-classification agent and measure how often human escalation is required vs. how often the classifier can resolve it
- [ ] Survey existing SDLC designs (GitHub Actions workflows, Buildkite pipelines, GitLab CI) for lane-aware escalation support — which natively support A/B/C/D gating and which require custom logic
- [ ] Document the relationship between SDLC-as-context-engineering and the broader agentic-harness-engineering framework (Lilian Weng, Jul 2026) — where they overlap and where each is unique