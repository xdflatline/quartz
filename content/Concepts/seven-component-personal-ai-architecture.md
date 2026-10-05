---
title: "Seven-Component Personal AI Architecture"
details: "A taxonomy of any personal AI system into seven orthogonal components: Intelligence (model + scaffolding), Context (who you are + what you've done), Personality (personality traits + voice + relationship model), Tools (skills + integrations + patterns), Security (prompt-injection defense + permissions + hooks), Orchestration (sub-agents + hooks + workflow composition), Interface (CLI + voice + ambient). Introduced by Daniel Miessler in January 2026 as an update to his 2024 four-component model; observed as the convergent pattern across PAI / LifeOS, Claude Code, Hermes Agent, OpenCode, and MoltBot. Used as the diagnostic frame for 'what's missing in my harness?' rather than a fixed implementation."
tags:
  - concept
  - architecture-pattern
  - agent
  - harness
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/daniel-miessler-personal-ai-infrastructure-2026-10-05]]"
---

# Seven-Component Personal AI Architecture

**Source:** [[Raw/daniel-miessler-personal-ai-infrastructure-2026-10-05]] (Daniel Miessler, January 2026 — published as a revision of the August 2024 four-component model)
**Category:** Architecture Pattern
**Status:** Active research area; converging pattern across multiple independent harness implementations

## Overview

Any personal AI system decomposes into seven orthogonal components. The taxonomy is a way to diagnose "what's missing in my harness?" rather than a fixed implementation — each component has multiple valid instantiations, and a healthy system works on all seven at once.

Miessler introduced the model in January 2026 as an update to his 2024 four-component essay. The argument is that **PAI, Claude Code, OpenCode, and MoltBot are independently converging on the same architecture**, which suggests the seven-component frame is closer to a description of the solution than to one author's design preference.

## The seven components

| # | Component | What it answers | Operational subparts |
|---|-----------|-----------------|----------------------|
| 1 | **Intelligence** | How smart is the system? | Model + scaffolding (context management, skills, hooks, AI steering rules) + continuous-learning mechanisms |
| 2 | **Context** | What does the system know about you? | Identity + history + current work + what worked/failed |
| 3 | **Personality** | What does it *feel* like to use? | Quantified traits + voice identity + relationship model (peer/master-servant) |
| 4 | **Tools** | What can it actually do? | Skills + integrations (MCP, plugins) + reusable patterns (Fabric, prompt libraries) |
| 5 | **Security** | How is it defended? | Prompt-injection defense + filesystem permissions + hook-based defense layers + detection + response |
| 6 | **Orchestration** | How are agents and automation managed? | Hook system + sub-agents + named agents + workflow composition |
| 7 | **Interface** | How do humans actually use it? | CLI + voice + terminal/IDE + future AR/gesture |

## Why this list

The 2024 four-component model was: **Model, Post-training, Internal Tooling, Agent Functionality.** That frame fit the vendor/ecosystem era (it predicted who would win the model wars). The 2026 seven-component frame fits the personal AI era, where the *harness* rather than the *model* is where value compounds.

Two upgrades from four → seven:

- **Personality** is broken out of "Internal Tooling." It's not a feature; it's a layer that determines whether the system feels like a tool or like a peer. Personality is the layer that turns a chatbot into an assistant.
- **Interface** is broken out of "Internal Tooling" because the surface of the interface (CLI, voice, ambient) is increasingly where the value is delivered, not where it's hidden.

Three components were *not* in the original four:

- **Context** — was implicit in "Internal Tooling," but personal AI makes it load-bearing. Without context you have a tool; with context you have an assistant that knows you.
- **Security** — was implicit in "Agent Functionality," but as harnesses gain filesystem and network authority, prompt-injection defense becomes a first-class concern.
- **Orchestration** — was implicit in "Agent Functionality," but the difference between "an agent that does one thing" and "a system that coordinates agents" is structural and worth naming.

## What this looks like in PAI / LifeOS

| Component | PAI v2.4 implementation | LifeOS equivalent |
|-----------|-------------------------|-------------------|
| **Intelligence** | The Algorithm (v0.2.23), Skills, AI Steering Rules | [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] + the skill library |
| **Context** | Three-tier Memory: Session / Work / Learning + the constitutional files | [[Raw/lifeos-philosophy-memory-2026-10-05]] (Cortex) + [[Raw/lifeos-philosophy-telos-2026-10-05]] |
| **Personality** | Twelve quantified traits (enthusiasm, energy, precision, …), voice identity (ElevenLabs TTS), peer relationship | Quantized as personality in the DA identity layer; voice is [[Raw/lifeos-philosophy-voice-2026-10-05]] |
| **Tools** | 67 skills / 333 workflows at the time + MCP integrations + 200+ Fabric patterns | The current [[Raw/lifeos-github-repo-catalog-2026-10-05\|56-skill library]] (grew as the project matured) |
| **Security** | Multiple hook-based defense layers + filesystem permissions + injection/access/deletion hooks | [[Raw/lifeos-philosophy-security-2026-10-05]] + the deny-list + the data-as-information-not-instructions constitutional rule |
| **Orchestration** | 17 hooks across 7 lifecycle events + sub-agents + named agents | [[Raw/lifeos-philosophy-hook-system-2026-10-05]] + [[Concepts/deterministic-hook-guardrails]] |
| **Interface** | CLI + voice notifications (ElevenLabs TTS) + tab management | CLI + [[Raw/lifeos-philosophy-voice-2026-10-05]] + [[Raw/lifeos-philosophy-helm-2026-10-05]] (the configured kitty + herdr terminal) |

## The diagnostic question

When a personal AI system feels *broken* or *generic*, the seven components give a checklist: which one is under-resourced?

- **Intelligence** — output is shallow or wrong → upgrade scaffolding, not model.
- **Context** — system re-explains things you already told it → memory tier is broken.
- **Personality** — output reads like a tool, not a peer → personality layer is generic.
- **Tools** — system can't do the work → skill library is small or unreachable.
- **Security** — system leaks credentials or executes hostile instructions → defense layers are misconfigured.
- **Orchestration** — system can't coordinate multi-step work → hooks and sub-agents are missing.
- **Interface** — system is hard to actually use → ambient surfaces (voice, statusline) are absent.

## Why the components are orthogonal

Each component answers a different question; you can't substitute one for another. A brilliant model with no scaffolding (Intelligence 10, all others 0) is impressive but useless. A personality-rich system with no memory (Personality 10, Context 0) is a charming amnesiac. The components are *both* independent in design and necessary in combination at run time.

This is what makes the frame a *taxonomy* and not a *priority list*. A team can't decide to "do intelligence well and skip personality for v1"; the system will feel like a tool regardless of how smart it is.

## Convergent evidence

The argument that this is the right decomposition comes from observing independent systems arriving at the same shape. PAI/LifeOS, Claude Code, Hermes Agent, OpenCode, and MoltBot all implement some version of all seven. The convergence is evidence that the categories aren't an artifact of one author's preferences.

Concretely:

- **Intelligence** — every modern harness separates "the model" from "the scaffolding around it."
- **Context** — every modern harness has a memory subsystem loaded into every prompt.
- **Personality** — Claude Code's `CLAUDE.md` identity, Hermes's Hindsight personality layer, LifeOS's DA identity all serve this role.
- **Tools** — every harness has a notion of "skills" or "tools" available to the agent.
- **Security** — every harness has at least a sandbox + a permission model.
- **Orchestration** — every harness has hooks or sub-agents.
- **Interface** — every harness has a CLI; most also have a voice or statusline layer.

## Connection to other patterns

- [[Entities/lifeos]] — primary productization of the seven components
- [[Concepts/ideal-state-artifact-isa]] — what the Intelligence component produces
- [[Concepts/four-tier-verification-stack]] — what the Security component can sit on top of
- [[Concepts/deterministic-hook-guardrails]] — the mechanism that ties Security and Orchestration together
- [[Concepts/structured-telos-file-for-durable-intent]] — the durable half of the Context component
- [[Concepts/append-only-amber-ledger-capture]] — the input side of Context

## Key Insights

1. **The seven components are convergent, not prescriptive.** Independent systems arrive at this shape because the categories are real, not because they copied each other.
2. **Intelligence without scaffolding is wasted. A mediocre model with good scaffolding always wins.** (Miessler's central claim, supported by Trail of Bits' AIxCC experience.)
3. **Personality is a first-class component.** A system without one feels like a tool no matter how smart it is.
4. **Context is what turns a tool into an assistant.** Memory isn't optional in personal AI.
5. **The components are orthogonal in design but necessary in combination.** You can't pick two of seven and call it done.

## Related Concepts

- [[Concepts/ideal-state-artifact-isa]] — the testable spec produced by Intelligence
- [[Concepts/generalized-hill-climbing-llm-tasks]] — the Intelligence runtime loop
- [[Concepts/deterministic-hook-guardrails]] — Security + Orchestration mechanism
- [[Entities/lifeos]] — primary productization

## References

- Raw: [[Raw/daniel-miessler-personal-ai-infrastructure-2026-10-05]]
- Origin essay (the four-component predecessor): [The 4 Components of Top AI Model Ecosystems](https://danielmiessler.com/blog/ai-model-ecosystem-4-components)
- Related: [A Personal AI Maturity Model (PAIMM)](https://danielmiessler.com/blog/personal-ai-maturity-model) (the *progression* frame, complementary to the *component* frame)
- Companion: [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] + [[Raw/lifeos-philosophy-telos-2026-10-05]] + [[Raw/lifeos-philosophy-memory-2026-10-05]]