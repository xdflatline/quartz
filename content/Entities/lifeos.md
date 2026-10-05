---
title: "LifeOS"
details: "LifeOS is an open-source, MIT-licensed AI harness created by Daniel Miessler (also author of the Fabric prompt-pattern library). It frames the system around a single move — close the gap from your current state to your ideal state — and exposes 27 named 'philosophy' components that serve that move: The Algorithm, ISA System, Workflows, Glance, Bunker, Cortex (memory), Synapse, Atlas, Vigil, Ledger, Hook System, Pulse, Learning, Assay, Security, Helm, plus the Skill System, Intent Engineering, Euphoric Surprise, and Generalized Hill Climbing as cross-cutting framings. v7.40.4 is the current release (Aug 14, 2026); the repo has 19.3k stars, 2.5k forks, 35 contributors. The skill library under `LifeOS/install/skills/` carries ~40 named skills."
tags:
  - entity
  - agent
  - harness
created: 2026-10-05
updated: 2026-10-05
type: entity
source: "[[Raw/lifeos-philosophy-the-algorithm-2026-10-05]]"
---

# LifeOS

**Source:** Daniel Miessler's LifeOS project ([[Raw/lifeos-philosophy-the-algorithm-2026-10-05]], GitHub repo, ourlifeos.ai)
**Category:** Project / Platform
**Author:** Daniel Miessler (danielmiessler on GitHub)
**Repository:** https://github.com/danielmiessler/LifeOS
**Website:** https://ourlifeos.ai/
**License:** MIT
**Latest Release:** v7.40.4 — "The Receipts Release" (Aug 14, 2026)
**GitHub Stats:** 19.3k stars, 2.5k forks, 35 contributors, 717 commits, 28 releases

## Overview

LifeOS is a self-installing AI harness. It does not write its own model — it sits between you and any model (Claude Code, Cursor, Codex, OpenCode, etc.) and supplies the missing layer that makes those models useful on your actual goals: durable intent, structured memory, an executable spec for each task, deterministic guardrails, a skills library, and a dashboard to watch it all run. The whole thing is installed by pasting one prompt into your AI engine or running `curl -fsSL https://ourlifeos.ai/install.sh | bash`.

The premise is that direction, not execution, is the scarce resource. Models are already extraordinary at doing; what they almost never get is clear instruction on what to do. LifeOS carries that clarity into every task: the long version of your intent lives in a file called [[Raw/lifeos-philosophy-telos-2026-10-05|TELOS]]; the testable shape of done lives in an [[Raw/lifeos-philosophy-the-isa-2026-10-05|ISA]] document; the work itself is a hill-climbing loop called [[Raw/lifeos-philosophy-the-algorithm-2026-10-05|The Algorithm]]; every decision is checked against verifiable evidence via [[Raw/lifeos-philosophy-assay-2026-10-05|Assay]] and [[Raw/lifeos-philosophy-glance-2026-10-05|Glance]].

## Core Components (the 27 "Unique Features")

The project organizes itself as 27 named components on [ourlifeos.ai/philosophy/](https://ourlifeos.ai/philosophy/). They cluster into four roles** in the architecture:

**The central engine**

- **[The Algorithm]** ([[Raw/lifeos-philosophy-the-algorithm-2026-10-05]]) — the unified thinking loop: route → articulate criteria → climb → verify → learn
- **Generalized Hill Climbing** ([[Raw/lifeos-philosophy-hill-climbing-2026-10-05]]) — every goal becomes a hill; take the next move that closes the gap
- **Current → Ideal State** ([[Raw/lifeos-philosophy-current-to-ideal-state-2026-10-05]]) — the foundational move; both states named, gap closed one checked step at a time
- **Intent Engineering** ([[Raw/lifeos-philosophy-intent-engineering-2026-10-05]]) — the WHAT layer of prompting, productized so every short sentence carries your whole context
- **Euphoric Surprise** ([[Raw/lifeos-philosophy-euphoric-surprise-2026-10-05]]) — the success metric: a 9 or 10, the involuntary "OMG, this is brilliant"
- **TELOS** ([[Raw/lifeos-philosophy-telos-2026-10-05]]) — mission, goals, values, strategies, narratives, challenges, in one file every session reads
- **ISA System** ([[Raw/lifeos-philosophy-the-isa-2026-10-05]]) — Ideal State Artifact, the 12-section document that captures done before work starts and is the proof you got there
- **The Skill System** ([[Raw/lifeos-philosophy-skill-system-2026-10-05]]) — composable units of expertise with intent triggers ("USE WHEN"); self-activating

**The execution surface**

- **Workflows** ([[Raw/lifeos-philosophy-workflows-2026-10-05]]) — YAML graphs of known steps with declared executors (Code, Judgment, Model, Human, Workflow); same definition runs locally or in Cloudflare Workers
- **Glance** ([[Raw/lifeos-philosophy-glance-2026-10-05]]) — small typed questions answered with probabilities in ~0.3 s (backed by the Jev model); 18 questions route every prompt
- **Assay** ([[Raw/lifeos-philosophy-assay-2026-10-05]]) — model-judge tier of verification; calibrated against your ratings; paired deterministic + judge tests
- **Bunker** ([[Raw/lifeos-philosophy-bunker-2026-10-05]]) — universal application harness; one chassis that supplies Data/Control/Observability/Ecommerce/Identity/Security planes per app type
- **Learning** ([[Raw/lifeos-philosophy-learning-2026-10-05]]) — every Algorithm run ends with reflection; events → patterns → Frames (living models of domains)
- **Observability** ([[Raw/lifeos-philosophy-observability-2026-10-05]]) — agents dashboard inside Pulse: a kanban of climb states with live criteria counts

**The state stores**

- **Memory / Cortex** ([[Raw/lifeos-philosophy-memory-2026-10-05]]) — two files load into every prompt (about you, about itself) + a Knowledge Archive of typed-link notes that ripen from seedling to evergreen
- **Synapse** ([[Raw/lifeos-philosophy-synapse-2026-10-05]]) — input funnel with an append-only amber ledger; capture → preserve → read at full fidelity → grade against TELOS → route
- **Atlas** ([[Raw/lifeos-philosophy-atlas-2026-10-05]]) — a live graph of everything you own with built-in `owns`, `blast`, `unregistered` queries
- **Vigil** ([[Raw/lifeos-philosophy-vigil-2026-10-05]]) — one event log, one reader; see everything, interrupt rarely
- **Ledger** ([[Raw/lifeos-philosophy-ledger-2026-10-05]]) — every change classified (patch/feature/major) and recorded in an append-only registry; ships gated on a fresh integrity check

**The trust + surface layer**

- **The Hook System** ([[Raw/lifeos-philosophy-hook-system-2026-10-05]]) — small scripts wired to fixed moments in every session; security hooks run inline and can hard-stop unsafe actions
- **Security** ([[Raw/lifeos-philosophy-security-2026-10-05]]) — three layers: constitutional rule (outside content is information, never instruction), platform deny list, and a hook that tags web results "data, not instructions"
- **Pulse** ([[Raw/lifeos-philosophy-pulse-2026-10-05]]) — one always-on daemon, one process, crash-isolated modules (voice, Telegram, iMessage, observability); menu-bar green/yellow/red status; Observatory web dashboard
- **Helm** ([[Raw/lifeos-philosophy-helm-2026-10-05]]) — kitty + herdr configured as one terminal, installed with one command
- **Dictation** ([[Raw/lifeos-philosophy-dictation-2026-10-05]]) — Stream Deck foot pedal + Typeless + Hammerspoon plugin; tap for long thoughts, hold for quick ones
- **Voice** ([[Raw/lifeos-philosophy-voice-2026-10-05]]) — spoken notifications through a Pulse-hosted endpoint; effort scales the chatter; two text-cleaning passes before speech
- **Custom Spinner Verbs** ([[Raw/lifeos-philosophy-spinner-verbs-2026-10-05]]) — your own animated working-verb ("Forging", "Climbing") in your color and animation, plus rotating tips
- **Custom Tooltips** ([[Raw/lifeos-philosophy-tooltips-2026-10-05]]) — every dashboard metric explains itself on hover, with a freshness marker so stale panels are visibly stale

## Origins and context

LifeOS began as **PAI (Personal AI Infrastructure)**, Miessler's earlier project that focused on prompt patterns and AI workflows. The October 2026 release (v7.40.4) shipped the Hermes heartbeat, the KEV (Known Exploited Vulnerabilities) integration, and the ComplexityRatchet; the prior 7.28.3 release was when "Cortex" was named as the memory system and the Hermes sidecar was added. The rebrand from PAI to LifeOS was carried through the SECURITY.md rewrite, LICENSE, and full de-stale in July 2026. The companion project **Fabric** (a library of crowd-sourced prompt patterns) is integrated as one of the skills.

The skill library under `LifeOS/install/skills/` carries ~40 named skills, organized into the categories you'll see when installing: research (ArXiv, Science, RootCauseAnalysis, FirstPrinciples, SystemsThinking), writing (WriteStory, Aphorisms, ExtractWisdom, BeCreative, Ideate), security (Hardening, RedTeam, ThreatModel, WorldThreatModel, SecurityMarketData), operations (Daemon, Interceptor, Bunker, Upgrade, Migrate, Maintenance), media (Art, AudioEditor, Remotion, Tldraw, Webdesign), productivity (Council, Loop, Novelty, Optimize, Interview, IterativeDepth, Trim, SuggestSkills, PrivateInvestigator, CMUX, LocalIntelligence, Sales), integrations (Apify, BrightData), and foundations (LifeOS, Cortex, ISA, Telos, Prompting, Research, CreateCLI, CreateSkill, BiasCheck, BitterPillEngineering, HTML, DetectAI, Evals, Fabric, USMetrics, Vitals). The skill `Telos` and the philosophy page TELOS name the same idea; the skill `ISA` and the ISA System philosophy page likewise.

## Related Concepts

- [[Concepts/ideal-state-artifact-isa]] — the testable-spec document pattern (ISA System)
- [[Concepts/generalized-hill-climbing-llm-tasks]] — the climb-as-loop pattern (Hill Climbing)
- [[Concepts/intent-engineering-as-productization]] — the WHAT layer of prompting
- [[Concepts/euphoric-surprise-as-success-metric]] — Deutsch-derived eval target
- [[Concepts/four-tier-verification-stack]] — code / glance / assay / human
- [[Concepts/deterministic-hook-guardrails]] — fixed-point rule scripts that even a forgetful model can't skip
- [[Concepts/append-only-amber-ledger-capture]] — preserve before judge (Synapse)
- [[Concepts/live-asset-graph-blast-radius]] — graph, not list (Atlas)

## References

- Source: [[Raw/lifeos-philosophy-the-algorithm-2026-10-05]] and 26 sibling philosophy pages, all `lifeos-philosophy-*.md` in Raw
- GitHub: https://github.com/danielmiessler/LifeOS
- Website: https://ourlifeos.ai/
- Docs: https://docs.ourlifeos.ai/ (one page per philosophy component)
- Release notes: https://github.com/danielmiessler/LifeOS/releases