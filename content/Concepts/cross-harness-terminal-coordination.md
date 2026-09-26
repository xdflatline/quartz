---
title: "Cross-Harness Terminal Coordination"
details: "Coordination pattern where agents in different harnesses communicate by typing into each other's tmux sessions via send-keys, wrapped by an ergonomic CLI (e.g., `rig send`, `rig capture`, `rig transcript`) — instant messaging over terminals instead of an API."
tags:
  - concept
  - agent
  - multi-agent
  - tooling
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Cross-Harness Terminal Coordination

**Category:** Coordination Pattern
**Status:** Production pattern (OpenRig)

---

## Overview

Agents already live in terminals. Terminal multiplexers like **tmux** let you assign a handle to each terminal — a named "seat" an agent sits in. tmux's `send-keys` lets one process type prompts directly into another process's terminal. Combine the two and you get **instant messaging between agents**, with no API, no message bus, no schema.

OpenRig wraps tmux in ergonomic commands:

- **`rig send`** — type a prompt into another agent's terminal.
- **`rig capture`** — read another agent's live screen.
- **`rig transcript`** — read another agent's saved history.

The author's framing: "Anything you can do in the agent's terminal, another agent can now do it."

## Why terminals-as-API works

1. **Harness-agnostic.** Claude Code, Codex, OpenCode, anything that takes a prompt from stdin. The wire format is whatever the terminal already accepts.
2. **Zero integration cost.** No new transport, no SDK per vendor, no schema negotiation.
3. **Ergonomics are the only thing missing.** tmux is fiddly; wrapping it in a CLI makes it usable. The wrapping IS the value-add.
4. **Limits messages to chat history.** This is the well-known weakness: messages pile up, get ignored, scroll off. That's why a separate durable queue primitive is needed for handoffs.

## The pipe-flow diagram

```
┌─ agent A (Claude Code) ─┐                        ┌─ agent B (Codex) ─┐
│  terminal / tmux pane   │   send-keys via rig    │  terminal pane    │
│  "claude-pane"          │ ◄──────────────────────►│  "codex-pane"     │
│                         │   rig send "do X"      │                   │
│  rig capture → A        │   rig capture ← B      │  rig transcript   │
└─────────────────────────┘                        └───────────────────┘
```

## Limits

This primitive is **ephemeral** — messages land in chat history, scroll off, and (with enough agents) pile up and get ignored. The author explicitly calls out that you still need a durable handoff primitive: a queue where every item has an owner and a status. See [[Concepts/owner-status-queue-handoff]].

## Related Concepts

- [[Concepts/owner-status-queue-handoff]] — durable complement for handoffs
- [[Concepts/rig-meta-harness-team-wrapper]] — the team this coordination runs inside
- [[Entities/tmux]] — the underlying tool being wrapped

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Coordination: tmux + a queue"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Coordination"
