---
title: "OpenRig Software-Factory Primitives"
details: "Cross-source synthesis of the YouTube video (2026-06-30) and companion blog post defining OpenRig's four primitives — rigs, coordination, workflows, workspaces — plus the steering-by-altitude model and the recursive-self-improvement multi-rig experiment. Argues that cross-harness composition beats single-agent internal scaling."
tags:
  - research
  - agent
  - agentic-system
  - orchestration
created: 2026-09-26
updated: 2026-09-26
type: research
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# OpenRig Software-Factory Primitives

**Sources:**
- [[Raw/openrig-software-factory-video-2026-06-30]] (video, 2026-06-30, 10:49)
- [[Raw/openrig-software-factory-building-blocks-2026]] (companion blog post)

**Reference implementation:** [[Entities/openrig]]

---

## Thesis

Modern coding-agent harnesses (Claude Code, Codex, OpenCode, etc.) are individually powerful but architecturally locked in. The OpenRig author — after ~8,000 hours coding with agents and ~2.5 years since ChatGPT launched — argues that the right way to scale past a single harness is **cross-harness composition**, not deeper internal sub-agent trees. The artifact of this composition is a "self-driving software factory" — a fleet of agent harnesses wired together so that the human's job collapses to roadmap-setting and exception handling.

The factory rests on **four primitives**, each intentionally simple:

1. **Rig** — a config-file wrapper around a team of agents ([[Concepts/rig-meta-harness-team-wrapper]])
2. **Coordination** — tmux-backed terminal messaging + a durable owner/status queue ([[Concepts/cross-harness-terminal-coordination]], [[Concepts/owner-status-queue-handoff]])
3. **Workflows** — daemon-enforced YAML rails ([[Concepts/yaml-workflow-deterministic-rails]])
4. **Workspaces** — a markdown control plane ([[Concepts/markdown-control-plane-workspace-engineering]]), with the **slice** ([[Concepts/slice-folder-spec-progress-proof]]) as its smallest unit

On top of these, two operational patterns turn the factory from "runs" to "runs itself":

- **Steering by altitude** ([[Concepts/steering-by-altitude-manage-by-exception]]) — the autonomy dial
- **Recursive self-improvement** ([[Concepts/recursive-self-improvement-multi-rig-loop]]) — the dial turned to maximum

---

## The primitives, at a glance

```
                    ┌────────────────────────────────┐
                    │            RIG                 │  team in a config file
                    │  (meta-harness, config-as-infra)│
                    └───────────────┬────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐         ┌─────────────────┐         ┌─────────────────┐
│ COORDINATION  │         │   WORKFLOWS     │         │   WORKSPACES    │
│ tmux + queue  │         │ YAML, daemon-   │         │ markdown        │
│ rig send      │         │ enforced;       │         │ control plane;  │
│ rig capture   │         │ agents write    │         │ rig scope       │
│ rig transcript│         │ their own       │         │ slice create    │
└───────────────┘         └─────────────────┘         └─────────────────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    ▼
                          ┌─────────────────┐
                          │   SLICE         │  spec / progress / proof
                          │   smallest unit │
                          └─────────────────┘
```

---

## Key cross-cutting arguments

### 1. Scaling externally beats scaling internally

Today's harnesses already let you scale internally via sub-agents. That's powerful, but it locks you into one vendor's design choices. The author's claim is that **scaling externally** — composing agents from different harnesses — is more important, because different models and harnesses specialize, and the specialization is worth the overhead.

The canonical pair is Claude Code (right-brain, creative, big-picture) + Codex CLI (left-brain, precise, literal, debugging-strong). Different harnesses for different roles.

### 2. The corpus callosum

The author uses a vivid metaphor: **OpenRig is the corpus callosum** that lets two different model-brains act as one mind. Without it, you have two agents you manually copy-paste between. With it, you have a team.

### 3. "Harness engineering is really workspace engineering"

A large fraction of what makes agent teams work in practice is *what's on disk* — plugins, skills, steering docs, progress files in predictable folder locations. Markdown files become the **control plane**. The folder convention is non-trivial: the wrong shape "can guarantee a mess, and it can kill your project"; the right shape "keeps agents thinking organized and transferable, so a fresh agent can be productive immediately."

### 4. The autonomy dial, not the autonomy switch

The primitives together make autonomy a continuous **dial**, not a yes/no. The human can be at any altitude — high (roadmap, watch, course-correct) or low (live in a terminal) — on any task, and move between altitudes as signals demand. **Manage by exception** is the operational mode: you enter the loop only when judgment is required.

### 5. Recursive self-improvement is the dial turned past 10

The author ran a three-rig closed loop (build / PM / dogfood) on OpenRig itself for several weeks. The loop closed: dogfood feedback → PM rig → better specs → build rig → new version → dogfood rig. It got stuck on rate limits repeatedly but auto-resumed. The author's reflection: "It wasn't like I was building software anymore. It was more like I was growing it." Subsequently dialed back to self-driving mode pending better guardrails.

---

## What this research adds to the garden

The OpenRig material is one of the cleanest real-world demonstrations of:

- **Meta-harness composition** — composing agent teams above the harness layer (cf. [[Concepts/meta-harness-outer-loop]], which optimizes harness code via search).
- **Filesystem-as-state** — using markdown folders as both coordination substrate and human UI source-of-truth.
- **Manage-by-exception operations** — the operational pattern that lets a human stay at high altitude while a fleet runs.
- **Empirical recursive self-improvement** — not a paper claim, an actual multi-week run with public GitHub history as evidence.

It is **not** a contribution to:

- New model architectures.
- New evaluation methodology.
- New agent memory systems (the workspace files substitute for, but do not replace, episodic memory).

---

## Concept map

```
                                  ┌──────────────────────────────┐
                                  │  steering-by-altitude        │
                                  │  (autonomy dial)             │
                                  └──────────────┬───────────────┘
                                                 │
                                                 ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │                       rig-meta-harness-team-wrapper             │
   │                       (the team, run like infra)                 │
   └────────────┬──────────────────┬───────────────────┬─────────────┘
                │                  │                   │
                ▼                  ▼                   ▼
   ┌─────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │ cross-harness       │  │ yaml-workflow    │  │ markdown-control │
   │ terminal coord      │  │ deterministic    │  │ plane workspace  │
   │ + owner-status queue│  │ rails            │  │ engineering      │
   └─────────────────────┘  └──────────────────┘  └────────┬─────────┘
                                                            │
                                                            ▼
                                               ┌──────────────────────┐
                                               │ slice-folder         │
                                               │ spec/progress/proof  │
                                               └──────────────────────┘

                ──────────────────────────────────────────────────
                maximum dial setting:
                          recursive-self-improvement-multi-rig-loop
                          (build + PM + dogfood, closed loop)
```

---

## Concepts added

- [[Concepts/rig-meta-harness-team-wrapper]]
- [[Concepts/cross-harness-terminal-coordination]]
- [[Concepts/owner-status-queue-handoff]]
- [[Concepts/yaml-workflow-deterministic-rails]]
- [[Concepts/markdown-control-plane-workspace-engineering]]
- [[Concepts/slice-folder-spec-progress-proof]]
- [[Concepts/steering-by-altitude-manage-by-exception]]
- [[Concepts/recursive-self-improvement-multi-rig-loop]]

## Entities added

- [[Entities/openrig]]
- [[Entities/codex-cli]]
- [[Entities/tmux]]

## Related existing pages

- [[Concepts/agentic-harness-engineering-ahe]] — overlapping discipline; OpenRig is an implementation of AHE principles with concrete primitives.
- [[Concepts/meta-harness-outer-loop]] — a different "meta-harness" sense (evolutionary search over harness code); OpenRig's "meta-harness" is about composing teams, not optimizing code.
- [[Concepts/coordinator-worker-task-dag-orchestration]] — broader lineage of orchestration patterns.
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — autonomy calibration as a harness mechanism.
- [[Concepts/agent-self-improvement]] — broader research lineage of self-improving agents.
- [[Research/claude-multi-agent-and-prompt-engineering-2026]] — earlier multi-agent research synthesis.
- [[Entities/claude-code]] — the other half of the canonical cross-harness pair.

## Open questions

- How does the recursive-self-improvement loop behave under adversarial prompt conditions? The author reports weeks-long runs; no adversarial-red-team data is in the source.
- What's the failure-mode distribution across the four primitives? Some primitives (workspaces) are flagged as "sometimes brittle"; no quantitative analysis is in the source.
- How does OpenRig's coordination layer interact with model-side tool-use protocols (MCP, function calling, computer-use)? Out of scope in the source.
