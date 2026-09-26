---
title: "tmux"
details: "Terminal multiplexer used as the transport substrate for cross-harness agent coordination in OpenRig. Named panes serve as agent 'seats'; `send-keys` enables inter-agent messaging; OpenRig wraps the fiddly bits in `rig send` / `rig capture` / `rig transcript`."
tags:
  - entity
  - cli
  - tooling
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# tmux

**Type:** Terminal multiplexer
**Role in OpenRig:** Transport substrate for [[Concepts/cross-harness-terminal-coordination]]

---

## What it is

tmux is a long-running terminal multiplexer — a single terminal that hosts many named panes, each of which can be a long-lived shell session. It survives disconnects, lets you detach and reattach, and exposes a programmatic control interface (notably `send-keys`) that lets one process type into another process's terminal.

## Why OpenRig uses it

The OpenRig author's insight is structural: **agents already live in terminals.** tmux's pane handles become agent "seats." `send-keys` becomes a generic inter-agent prompt bus. The wire format is whatever the terminal already accepts — no new transport, no SDK per vendor.

> "The agents already live in terminals. Tmux lets you assign a handle to each terminal and this is like a named seat that that agent sits in. Then there's the send keys command. It lets one agent directly type prompts into the terminal of another agent. So you combine these and you get instant messaging between agents."

## The wrapped interface

tmux is "a bit fiddly" — hence OpenRig's CLI wrappers:

| Wrapped command | Underlying tmux operation | Purpose |
|-----------------|--------------------------|---------|
| `rig send` | `send-keys` | Type a prompt into another agent's pane |
| `rig capture` | `capture-pane` | Read another agent's live screen |
| `rig transcript` | file read on saved pane history | Read another agent's history |

## The limit this imposes

tmux-mediated messages are **ephemeral** — they land in chat history, scroll off, pile up, and get ignored as agent count grows. This is exactly why OpenRig pairs the tmux layer with a [[Concepts/owner-status-queue-handoff]] for durable work transfer.

## Related

- [[Concepts/cross-harness-terminal-coordination]] — the pattern tmux enables
- [[Entities/openrig]] — the wrapper
