---
title: "Owner-Status Queue Handoff"
details: "Coordination primitive for reliable inter-agent work transfer: a simple queue where every item carries an owner and a status, paired with cross-harness terminal coordination to give durable handoffs that survive ephemeral chat-scroll loss."
tags:
  - concept
  - agent
  - multi-agent
  - orchestration
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Owner-Status Queue Handoff

**Category:** Coordination Primitive
**Status:** Production pattern (OpenRig)

---

## Overview

A **durable queue** where every item has exactly two fields — **owner** (which agent is responsible right now) and **status** (where it is in its lifecycle) — paired with [[Concepts/cross-harness-terminal-coordination]] to give reliable handoffs between agents. The author's framing: "Not a Jira-shaped thing. That's built for humans and it's a bit overkill for agents. All you need is a simple queue where every item has an owner and a status."

## The shape

```
┌────────── owner-status queue ──────────┐
│                                        │
│  item#17   owner=builder   status=todo     │
│  item#18   owner=reviewer  status=in-review│
│  item#19   owner=planner   status=blocked  │
│  item#20   owner=builder   status=done     │
│                                        │
└────────────────────────────────────────┘
                    ▲
                    │ rig send delivers the actual prompt
                    ▼
        cross-harness terminal coordination
```

## Why this is the right minimum

1. **Owner field** makes the queue an explicit dispatch table — no agent needs to ask "is this for me?" — they grep for their own handle.
2. **Status field** gives the workflow engine (or human reviewer) a one-glance view of pipeline progress.
3. **Durability** decouples the handoff from ephemeral chat history. As the author notes: "messages can actually pile up and they get ignored" if you rely on tmux chat alone.
4. **Jira-shaped tools are overkill** for agent teams: no comments, no sprints, no epics, no assignees-vs-reviewers split. The owner/status pair is enough.

## Where the queue sits in the system

- The **queue** is the durable substrate that survives ephemeral chat loss.
- The **rig send** command is the *act of delivery* — when an item moves from owner A's queue slot to owner B's, `rig send` types the prompt into B's terminal.
- **Workflows** (a separate primitive, see [[Concepts/yaml-workflow-deterministic-rails]]) define the sequence of owner transitions.

## When to use

- Handoffs between distinct agents where the receiving agent might be busy when the sender fires.
- Multi-step pipelines (planner → builder → tester → reviewer) where each step needs a clear "what's mine, what's next" view.
- Anything where chat-scroll loss would silently drop work.

## When NOT to use

- Sub-second synchronous calls between co-located sub-agents in a single harness. Use the harness's native sub-agent mechanism.
- Human-to-human work tracking. The author's point is precisely that this is the lightweight, agent-appropriate version — humans deserve richer tools.

## Related Concepts

- [[Concepts/cross-harness-terminal-coordination]] — the ephemeral transport the queue rides on
- [[Concepts/yaml-workflow-deterministic-rails]] — what sequences owner transitions
- [[Concepts/coordinator-worker-task-dag-orchestration]] — broader DAG/orchestration lineage

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Coordination: tmux + a queue"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Coordination"
