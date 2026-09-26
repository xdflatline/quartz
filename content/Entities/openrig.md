---
title: "OpenRig"
details: "Open-source (Apache-2.0) coordination layer for cross-harness coding-agent teams. Wraps Claude Code, Codex, and other CLI coding agents into a 'rig' (harness-for-harnesses) with tmux-based coordination, owner-status queues, YAML workflows, and a markdown workspace control plane. Distributed as a daemon, CLI, and (originally) web UI / (now) terminal UI via `rig tui`."
tags:
  - entity
  - agent
  - tooling
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# OpenRig

**Type:** Open-source tool (Apache-2.0)
**Author:** mvschwarz
**Repo:** github.com/mvschwarz/openrig
**Site:** openrig.dev
**Install:** `npm i -g @openrig/cli`

---

## What it is

OpenRig is the open-source coordination layer that turns a fleet of standalone coding-agent harnesses (Claude Code, Codex, etc.) into a self-driving software factory. It's a daemon + CLI + (web or terminal) UI running on your laptop.

The author's framing: "the corpus callosum that lets two different model-brains act as one mind" — Claude (creative, big-picture) + Codex (precise, literal) coordinated as a single team.

## The four primitives it implements

| Primitive | Implementation | Concept |
|-----------|----------------|---------|
| **Rig** | Config-file wrapper around a team of agents | [[Concepts/rig-meta-harness-team-wrapper]] |
| **Coordination** | tmux + send-keys, wrapped as `rig send` / `rig capture` / `rig transcript` | [[Concepts/cross-harness-terminal-coordination]] |
| **Queue** | Owner/status queue, paired with `rig send` for durable handoffs | [[Concepts/owner-status-queue-handoff]] |
| **Workflows** | YAML config files enforced by the daemon; agents write them | [[Concepts/yaml-workflow-deterministic-rails]] |
| **Workspaces** | Markdown control plane; `rig scope slice create` materializes slices | [[Concepts/markdown-control-plane-workspace-engineering]] / [[Concepts/slice-folder-spec-progress-proof]] |

Plus two operational layers on top:

- [[Concepts/steering-by-altitude-manage-by-exception]] — the autonomy dial
- [[Concepts/recursive-self-improvement-multi-rig-loop]] — the dial turned to maximum

## Why it matters

Most coding-agent tooling optimizes a single agent's loop. OpenRig's contribution is **cross-harness composition**: the recognition that today's best agents (Claude, Codex) are good at *different* things, and the value is in letting them specialize and coordinate rather than asking one of them to be good at everything. This is "scaling externally" vs. "scaling internally with sub-agents" — the author's core thesis.

## The recursive-self-improvement experiment

The author ran a three-rig closed loop (build / PM / dogfood) on OpenRig itself for several weeks. The GitHub history "tells the story" — the project kept shipping at the rate limited by the author's Claude account ban threshold. Subsequent public-project use has been dialed back to self-driving mode pending better guardrails.

## Companion reading

- [[Raw/openrig-software-factory-video-2026-06-30]] — the 10-minute video walkthrough
- [[Raw/openrig-software-factory-building-blocks-2026]] — the blog-post summary
- [openrig.dev/blog/cross-harness-agents](https://openrig.dev/blog/cross-harness-agents) — the coordination-specific deep dive (referenced by the source)
