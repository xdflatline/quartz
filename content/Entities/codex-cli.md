---
title: "Codex CLI"
details: "OpenAI's command-line coding agent. One half of the canonical OpenRig cross-harness pair (paired with Claude Code); characterized in the source as precise, literal, best-in-class for debugging and code review."
tags:
  - entity
  - coding-agent
  - agent
created: 2026-09-26
updated: 2026-09-26
type: entity
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Codex CLI

**Type:** Coding agent (CLI)
**Vendor:** OpenAI

---

## What it is

OpenAI's command-line coding agent. One of the two canonical agents in OpenRig's cross-harness fleet.

The OpenRig source characterizes Codex as the **left-brain** half of the team:

> "Codex is like the left, precise, literal, but can get narrowly focused. But, it's the absolute best for debugging and code review."

## Role in OpenRig

- **Specialization:** precise, literal, narrow-focus — pairs naturally with Claude Code's creative, big-picture strength.
- **Best use cases (per source):** debugging, code review.
- **Coverage of the full SDLC:** in the OpenRig author's framing, Codex is good enough end-to-end to run on ordinary OpenAI subscriptions, just like Claude Code is on ordinary Anthropic subscriptions.

## How OpenRig uses it

- Codex runs in a tmux pane (a named "seat").
- Other agents reach it via `rig send` ([[Concepts/cross-harness-terminal-coordination]]).
- Codex's terminal output is captured via `rig capture` and read for progress.
- Codex is paired with [[Entities/claude-code]] in a single rig — usually with Codex as reviewer/builder of literal details and Claude as planner/architect.

## Why the cross-harness pairing matters

The OpenRig author's core thesis: today's best harnesses specialize. A Claude/Codex team can do strictly more than either one running alone, because each one's weaknesses (Claude undisciplined, Codex narrowly focused) are covered by the other. This is the empirical justification for the entire cross-harness architecture.

## Related

- [[Entities/openrig]] — the reference coordination layer
- [[Entities/claude-code]] — the other half of the pair
- [[Concepts/rig-meta-harness-team-wrapper]] — what wraps Codex into a team
