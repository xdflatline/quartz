---
title: "Rig Meta-Harness Team Wrapper"
details: "Architecture pattern where a single named config file wraps a whole team of agents (each itself a model-in-a-harness) into one durable, runnable unit — a 'harness for harnesses' run like infrastructure, comparable to Docker for agent teams."
tags:
  - concept
  - agent
  - harness
  - multi-agent
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Rig Meta-Harness Team Wrapper

**Category:** Architecture Pattern
**Status:** Active production pattern (OpenRig, Apache-2.0)
**Related:** [[Concepts/meta-harness-outer-loop]] — different "meta-harness" sense (optimizing harness code via search); the rig pattern is about composing agent teams into one runnable thing, not about optimizing harness code.

---

## Overview

A **rig** wraps a whole team of agents into one durable, nameable, runnable artifact. Because an agent is not just a model but a *model-in-a-harness* (tools, memory, files that let it actually work), a rig is the harness layer above that — a harness for harnesses, or **meta-harness** in the OpenRig author's vocabulary.

The critical insight: a rig is just a config file. That makes teams of agents as composable and runnable as infrastructure — "almost like Docker, but for agents."

## The composition

```
┌─────────────────── RIG (meta-harness, config file) ───────────────────┐
│                                                                         │
│   ┌── agent (model + harness + tools + memory) ──┐                     │
│   ┼── agent (model + harness + tools + memory) ──┼── deterministic     │
│   ┼── agent (model + harness + tools + memory) ──┼── handoffs via      │
│   └── agent (model + harness + tools + memory) ──┘   workflow + queue   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                  ▲
                                  │ single name, single config
                                  │ run like infrastructure
```

## Why this layer exists

Today's harnesses (Claude Code, Codex, OpenCode, etc.) let you scale **internally** via sub-agents. That's powerful, but it locks you into one harness's design choices. Scaling **externally** — composing agents from different harnesses — is what the rig enables:

- **Cross-vendor teams.** Claude (creative, big-picture) + Codex (precise, literal) is the canonical example from the source; the metaphor of left/right brain hemispheres maps the asymmetry. Other vendors slot in.
- **Run like infra.** A rig is a config file, not a custom application. You can version it, copy it, deploy it.
- **One name, one observable.** When something fails, you point at the rig, not at fifteen sub-processes.

## What a rig is NOT

- Not a single agent loop. A rig contains multiple agents; each agent still has its own loop.
- Not the same as [[Concepts/meta-harness-outer-loop]] — that pattern optimizes harness code via evolutionary search (Lee et al. 2026). The rig pattern composes teams of agents; it does not rewrite harness code.
- Not a workflow. Workflows (a separate OpenRig primitive) live inside the rig and define how work flows between its agents.

## Source quotes

> "An agent isn't just a model. It's a model sitting inside a harness, all the tools, memory, files that let it actually do work. A rig is the harness that wraps a whole team of those agents into one durable, nameable thing. So a harness for harnesses. Some call this a meta harness. And because a rig is just a config file, you can run those teams like infrastructure. Almost like Docker, but for agents."

## Related Concepts

- [[Concepts/meta-harness-outer-loop]] — the other "meta-harness" sense (optimize harness code)
- [[Concepts/cross-harness-terminal-coordination]] — how agents inside one rig talk to each other
- [[Concepts/yaml-workflow-deterministic-rails]] — what runs inside a rig
- [[Entities/openrig]] — the reference implementation

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Rigs: a harness for harnesses"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "The rig"
