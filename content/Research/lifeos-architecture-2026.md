---
title: "Research Index: LifeOS — A Universal AI Harness with Testable Intent"
details: "Synthesis of Daniel Miessler's LifeOS (v7.40.4, August 2026, 19.3k stars, MIT-licensed). LifeOS frames the entire agent loop around one move — close the gap from your current state to your ideal state — and exposes 27 named components that serve that move: The Algorithm (route → articulate → climb → verify → learn), the ISA system (12-section Ideal State Artifact that doubles as spec + test harness + completion record), TELOS (structured file of durable intent), Glance (one-question probabilistic judgment via the Jev model), Assay (model-judge verification), Bunker (universal application harness), Cortex/Synapse/Atlas (memory + capture + asset graph), Vigil/Ledger/Hook (observability + bookkeeping + fixed-point guardrails), Pulse (single-daemon life dashboard), the Skill System (self-activating libraries with intent triggers), and a Security model that substitutes one clear rule for thousands of regex. The corpus is 27 philosophy pages from ourlifeos.ai/philosophy/ + 40+ skills in the GitHub repo. Synthesizes 8 reusable architectural concepts and positions LifeOS relative to Claude Code, Hermes Agent, OpenCode, AgentOS, and other harnesses."
tags:
  - research
  - agent
  - harness
  - architecture-pattern
created: 2026-10-05
updated: 2026-10-05
type: research
sources:
  - .Raw/lifeos-philosophy-the-algorithm-2026-10-05.md
  - .Raw/lifeos-philosophy-current-to-ideal-state-2026-10-05.md
  - .Raw/lifeos-philosophy-hill-climbing-2026-10-05.md
  - .Raw/lifeos-philosophy-telos-2026-10-05.md
  - .Raw/lifeos-philosophy-the-isa-2026-10-05.md
  - .Raw/lifeos-philosophy-skill-system-2026-10-05.md
  - .Raw/lifeos-philosophy-intent-engineering-2026-10-05.md
  - .Raw/lifeos-philosophy-euphoric-surprise-2026-10-05.md
  - .Raw/lifeos-philosophy-glance-2026-10-05.md
  - .Raw/lifeos-philosophy-assay-2026-10-05.md
  - .Raw/lifeos-philosophy-hook-system-2026-10-05.md
  - .Raw/lifeos-philosophy-security-2026-10-05.md
  - .Raw/lifeos-philosophy-bunker-2026-10-05.md
  - .Raw/lifeos-philosophy-memory-2026-10-05.md
  - .Raw/lifeos-philosophy-synapse-2026-10-05.md
  - .Raw/lifeos-philosophy-atlas-2026-10-05.md
  - .Raw/lifeos-philosophy-vigil-2026-10-05.md
  - .Raw/lifeos-philosophy-ledger-2026-10-05.md
  - .Raw/lifeos-philosophy-pulse-2026-10-05.md
  - .Raw/lifeos-philosophy-observability-2026-10-05.md
  - .Raw/lifeos-philosophy-learning-2026-10-05.md
  - .Raw/lifeos-philosophy-workflows-2026-10-05.md
  - .Raw/lifeos-philosophy-dictation-2026-10-05.md
  - .Raw/lifeos-philosophy-voice-2026-10-05.md
  - .Raw/lifeos-philosophy-helm-2026-10-05.md
  - .Raw/lifeos-philosophy-spinner-verbs-2026-10-05.md
  - .Raw/lifeos-philosophy-tooltips-2026-10-05.md
related:
  - "[[Entities/lifeos]]"
---

# Research Index: LifeOS — A Universal AI Harness with Testable Intent

**Source:** Daniel Miessler's LifeOS project (v7.40.4, August 14, 2026)
**Authors:** Daniel Miessler and 35 contributors (the repo credits Claude and other contributors)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**License:** MIT
**GitHub Stats:** 19.3k stars, 2.5k forks, 717 commits, 28 releases

## Overview

LifeOS is an open-source AI harness created by Daniel Miessler. It does not include its own model — it sits between you and any model (Claude Code, Cursor, Codex, OpenCode, etc.) and supplies the missing layer that makes those models useful on your actual goals: durable intent, structured memory, an executable spec for each task, deterministic guardrails, a skills library, and a dashboard to watch it all run. The whole thing is installed by pasting one prompt into your AI engine or running one curl command.

The premise is that **direction, not execution, is the scarce resource.** Models are already extraordinary at doing; what they almost never get is clear instruction on what to do. LifeOS carries that clarity into every task: the long version of your intent lives in a structured file called TELOS; the testable shape of done lives in an ISA document; the work itself is a hill-climbing loop called The Algorithm; every decision is checked against verifiable evidence via Assay and Glance; the result is graded against the success metric of *euphoric surprise*.

## The three-line thesis

1. **Every task has the same shape:** name where you are, name where you want to be, close the gap with steps you can check. The shape scales from a typo fix to a company launch because the work is always the same.
2. **Direction is the bottleneck.** As models get better, execution gets cheaper and direction gets more valuable. Intent engineering, ISA documents, and TELOS files are the layer that addresses that bottleneck.
3. **Verification is a ladder.** Move work down the ladder (human → Glance → code) as you earn durable labels; deterministic checks first, model-judge fallback only where code can't reach; treat judge disagreement as calibration debt to be mined into deterministic rules.

## Concepts

### Architectural patterns

- [[Concepts/ideal-state-artifact-isa]] — 12-section testable spec that doubles as harness + completion record
- [[Concepts/generalized-hill-climbing-llm-tasks]] — step-by-step gap-closing loop as the underlying runtime
- [[Concepts/intent-engineering-as-productization]] — conveying the WHAT into every interaction
- [[Concepts/structured-telos-file-for-durable-intent]] — durable mission/goals/strategies file the agent reads on every prompt
- [[Concepts/self-activating-skill-libraries]] — intent-matched capability libraries with worked examples
- [[Concepts/four-tier-verification-stack]] — code / glance / assay / human as the verification ladder
- [[Concepts/deterministic-hook-guardrails]] — fixed-point rule scripts that survive model forgetfulness
- [[Concepts/append-only-amber-ledger-capture]] — preserve-before-judge input pipeline
- [[Concepts/live-asset-graph-blast-radius]] — graph-not-list for security and ops inventories

### Evaluation metric

- [[Concepts/euphoric-surprise-as-success-metric]] — hard-to-vary recognition as the score, after Deutsch

## Entities

- [[Entities/lifeos]] — the platform itself; 27 named components, ~40 skills in the repo

## Raw Sources (27 philosophy pages + GitHub repo)

| File | Topic | Date | Key Items |
|------|-------|------|-----------|
| [[Raw/lifeos-philosophy-current-to-ideal-state-2026-10-05]] | The foundational move | 2026-10-05 | gap closing, written definition of done |
| [[Raw/lifeos-philosophy-euphoric-surprise-2026-10-05]] | Success metric | 2026-10-05 | Deutsch, hard-to-vary, 9-of-10 |
| [[Raw/lifeos-philosophy-intent-engineering-2026-10-05]] | Direction productization | 2026-10-05 | WHAT layer, intent → context → prompt |
| [[Raw/lifeos-philosophy-hill-climbing-2026-10-05]] | The runtime loop | 2026-10-05 | phases, single-step checks |
| [[Raw/lifeos-philosophy-telos-2026-10-05]] | Durable intent file | 2026-10-05 | mission/goals/strategies/narratives/challenges |
| [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] | The unified thinking system | 2026-10-05 | route → articulate → climb → verify → learn |
| [[Raw/lifeos-philosophy-the-isa-2026-10-05]] | The testable spec document | 2026-10-05 | 12 sections, ISCs, anti-criteria |
| [[Raw/lifeos-philosophy-skill-system-2026-10-05]] | Self-activating libraries | 2026-10-05 | intent triggers, worked examples |
| [[Raw/lifeos-philosophy-workflows-2026-10-05]] | Known-steps as YAML graphs | 2026-10-05 | 5 executors, JSON Schema |
| [[Raw/lifeos-philosophy-glance-2026-10-05]] | Small-typed-question judgment | 2026-10-05 | Jev, 18 questions, ~0.3s |
| [[Raw/lifeos-philosophy-assay-2026-10-05]] | Eval system | 2026-10-05 | four tiers, paired comparisons |
| [[Raw/lifeos-philosophy-bunker-2026-10-05]] | Universal app harness | 2026-10-05 | 6 planes, type-driven |
| [[Raw/lifeos-philosophy-memory-2026-10-05]] | Cortex memory system | 2026-10-05 | hot layer + Knowledge Archive |
| [[Raw/lifeos-philosophy-synapse-2026-10-05]] | Input router | 2026-10-05 | amber ledger, grade against TELOS |
| [[Raw/lifeos-philosophy-atlas-2026-10-05]] | Live asset graph | 2026-10-05 | owns / blast / unregistered |
| [[Raw/lifeos-philosophy-vigil-2026-10-05]] | Always-on watch | 2026-10-05 | one log, routing rules |
| [[Raw/lifeos-philosophy-ledger-2026-10-05]] | Version bookkeeping | 2026-10-05 | patch/feature/major, integrity check |
| [[Raw/lifeos-philosophy-hook-system-2026-10-05]] | Fixed-point guardrails | 2026-10-05 | 5 lifecycle moments, inline vs background |
| [[Raw/lifeos-philosophy-pulse-2026-10-05]] | Life Dashboard | 2026-10-05 | one daemon, Observatory |
| [[Raw/lifeos-philosophy-observability-2026-10-05]] | Agents dashboard | 2026-10-05 | climb-state kanban |
| [[Raw/lifeos-philosophy-learning-2026-10-05]] | Reflection layer | 2026-10-05 | events → patterns → Frames |
| [[Raw/lifeos-philosophy-dictation-2026-10-05]] | Foot-pedal input | 2026-10-05 | Typeless, Stream Deck, Hammerspoon |
| [[Raw/lifeos-philosophy-voice-2026-10-05]] | Spoken notifications | 2026-10-05 | Pulse endpoint, two text-clean passes |
| [[Raw/lifeos-philosophy-security-2026-10-05]] | Three-layer model | 2026-10-05 | constitutional + deny list + hook |
| [[Raw/lifeos-philosophy-helm-2026-10-05]] | Terminal config | 2026-10-05 | kitty + herdr |
| [[Raw/lifeos-philosophy-spinner-verbs-2026-10-05]] | Personal statusline | 2026-10-05 | source JSON + sync tool |
| [[Raw/lifeos-philosophy-tooltips-2026-10-05]] | Self-explaining dashboard | 2026-10-05 | freshness markers |

## The Architecture, in One Picture

```
                    ┌─────────────────────────────┐
                    │      YOUR IDEAL STATE       │   ← TELOS (mission/goals/strategies)
                    └─────────────────────────────┘
                                    ▲
                                    │ gap (what every task is trying to close)
                                    │
                    ┌─────────────────────────────┐
                    │       CURRENT STATE         │   ← Cortex memory + Atlas asset graph
                    └─────────────────────────────┘
                                    ▲
                                    │ measured by
                                    │
                    ┌─────────────────────────────┐
                    │       THE ALGORITHM         │   ← route → articulate → climb → verify → learn
                    │  binds to an ISA document   │       (skill system + workflows underneath)
                    └─────────────────────────────┘
                                    │
                                    │ verified against
                                    ▼
                    ┌─────────────────────────────┐
                    │  FOUR-TIER VERIFICATION     │   ← code / glance (Jev) / assay (model judge) / human
                    │  protected by HOOK GUARDS   │   ← inline security; background ambient
                    │  classified via LEDGER       │       (patch/feature/major, integrity-checked)
                    │  logged via VIGIL           │       (one log, rule-routed by priority)
                    │  surfaced via PULSE         │       (one daemon, Observatory + menu-bar)
                    └─────────────────────────────┘
                                    │
                                    │ ambient automation
                                    ▼
                    ┌─────────────────────────────┐
                    │   BUNKER (universal app harness, optional)   │
                    └─────────────────────────────┘
                                    ▲
                                    │ fed by
                    ┌─────────────────────────────┐
                    │  SYNAPSE (amber ledger, input router)        │
                    └─────────────────────────────┘
```

## Cross-Cutting Themes

### 1. The intelligence-product pattern (everything runs on intent + reasoning)

- [[Raw/lifeos-philosophy-intent-engineering-2026-10-05]] holds the durable intent
- [[Raw/lifeos-philosophy-the-isa-2026-10-05]] holds the task intent
- [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] runs them, climbing on verified evidence
- [[Raw/lifeos-philosophy-euphoric-surprise-2026-10-05]] grades the result
- The test: a request gets handled in the context of your whole life, not just the words you typed

### 2. Verification that doesn't rely on the model remembering

- [[Raw/lifeos-philosophy-hook-system-2026-10-05]] runs guardrails at fixed points, regardless of attention
- [[Raw/lifeos-philosophy-assay-2026-10-05]] and [[Raw/lifeos-philosophy-glance-2026-10-05]] form the ladder
- [[Raw/lifeos-philosophy-vigil-2026-10-05]] catches drift; the rules that pick the route live in one policy file
- [[Raw/lifeos-philosophy-security-2026-10-05]] substitutes one clear rule for thousands of regex

### 3. State that compounds, rather than resets

- [[Raw/lifeos-philosophy-telos-2026-10-05]] carries durable intent across sessions
- [[Raw/lifeos-philosophy-memory-2026-10-05]] carries context (hot layer + typed-link graph)
- [[Raw/lifeos-philosophy-synapse-2026-10-05]] preserves every capture in an append-only ledger
- [[Raw/lifeos-philosophy-learning-2026-10-05]] rolls reflections up to patterns and Frames
- [[Raw/lifeos-philosophy-ledger-2026-10-05]] records every change with integrity gating

### 4. Small things done consistently

- The vocabulary of the system — *climb*, *ISA*, *criterion*, *probe*, *frame* — is small and consistent
- The mount-points for the system — hooks, scripts, schemas — are small and well-known
- The result is a system that runs on its own without becoming a tower of bespoke software

## Where it fits among other agent frameworks

| Dimension | LifeOS | Claude Code | Hermes Agent | AgentOS |
|-----------|--------|-------------|--------------|---------|
| Own model? | No | No (Anthropic models) | No (multi-provider) | No |
| Persistent intent file | Yes (TELOS) | Limited (memory) | Hindsight | No (stateless per session) |
| Testable spec layer | Yes (ISA) | Limited (todos) | No | No |
| Skill library size | 40+ bundled | None (relies on user) | Hermes-bundled + custom | No |
| Self-install into another agent | Yes (one prompt + curl) | No | No | No |
| Security model | Three layers | Permission system | Hindsight + policies | VM isolation |
| Open source / self-hosted | MIT | No | MIT | Apache-2.0 |

The thesis: LifeOS is the *platform* play in the harness space — it sits above individual agent CLIs (Claude Code, Codex, Cursor, OpenCode) and supplies the layer that makes any of them usable on your goals. Other harnesses (Hermes Agent) provide personal-assistant runtimes with strong memory and skills; AgentOS provides execution isolation; Claude Code provides the IDE-loop. LifeOS is closer to a *life operating system* — the meta-harness that consumes the others.

## What makes the system work, in one paragraph

You write down where you are and where you want to be, with criteria for done. The Algorithm turns your prompt into a routed agent run that climbs toward those criteria, checks each on real evidence, and folds what it learned back into the system. The work happens in skills, the guardrails run at hooks, the memory compounds in Cortex, the intent travels in TELOS, the tests live in your spec. The dashboard shows you the climb. The next run starts higher than this one did.

## Next Research Directions

- [ ] **Evaluate** the ISA pattern against existing spec formats (OpenAPI, AsyncAPI, JSON Schema docs) — which of LifeOS's 12 sections are reusable in non-AI projects?
- [ ] **Benchmark** Glance's 18-question routing against Hermes Agent's session-memory and against plain chain-of-thought prompting — measure latency, accuracy, and cost per decision.
- [ ] **Compare** LifeOS's three-layer security model against Claude Code's permission system and Hermes's Hindsight memory safety — which catches the most prompt injection for the least code?
- [ ] **Test** whether Euphoric Surprise as a metric can be operationalized without an essay prompt — e.g., when the work is a deploy, not a piece of writing.
- [ ] **Prototype** an ISA-shaped document for an existing project in this wiki (e.g., a Quartz ingestion) — does the 12-section discipline survive outside LifeOS?
- [ ] **Audit** the LifeOS skill library for skills worth their own wiki concept pages — Fabric, FirstPrinciples, SystemsThinking, RedTeam, Hardening, ThreatModel look cross-cutting enough to canonize.
- [ ] **Track** the rebrand from PAI to LifeOS — what's preserved across the boundary, what was renamed, what was dropped (e.g., the Fabric patterns, the PAI install script).

## References

- Source: [LifeOS repo](https://github.com/danielmiessler/LifeOS) (MIT, 19.3k stars)
- Philosophy: https://ourlifeos.ai/philosophy/ (27 pages, all linked from the Raw tier)
- Docs: https://docs.ourlifeos.ai/ (one page per philosophy component)
- Origin essay: [The Last Algorithm](https://danielmiessler.com/blog/the-last-algorithm) (Daniel Miessler)
- Related project: [Fabric](https://github.com/danielmiessler/Fabric) (crowd-sourced prompt patterns, integrated as a skill)