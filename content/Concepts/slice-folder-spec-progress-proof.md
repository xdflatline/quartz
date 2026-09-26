---
title: "Slice Folder Spec Progress Proof"
details: "Workspace primitive where one CLI command (`rig scope slice create`) materializes a folder for a slice of work containing a spec, a progress file, and a proof directory — making work units self-contained, trackable, and instantly legible to fresh agents and the human UI."
tags:
  - concept
  - agent
  - context-engineering
  - tooling
created: 2026-09-26
updated: 2026-09-26
type: concept
sources:
  - .Raw/openrig-software-factory-video-2026-06-30.md
  - .Raw/openrig-software-factory-building-blocks-2026.md
---

# Slice Folder Spec Progress Proof

**Category:** Workspace Primitive
**Status:** Production primitive (OpenRig)

---

## Overview

The smallest unit of work in OpenRig's workspace engineering is a **slice** — a folder created by a single CLI command, containing exactly the three artifacts a slice needs:

1. **Spec** — what this slice is supposed to do.
2. **Progress** — where it currently is.
3. **Proof** — evidence the work was done right.

> "In just one move, an agent creates a ticket that's trackable in the system, along with a folder setup to use as a workspace for that slice."

The CLI is `rig scope slice create`. The output is a self-contained folder that any fresh agent can pick up without context from the originating agent.

## The shape

```
slices/
└── slice-017-linkpix-feed-polling/
    ├── spec.md       # what we're building
    ├── progress.md   # current state, blockers, next steps
    └── proof/        # screenshots, test runs, logs
        ├── test-output.txt
        └── demo-screenshot.png
```

## Why this is a primitive, not a convention

- **Single command.** No ad-hoc `mkdir` + write-three-files workflow. The shape is enforced.
- **Three is enough.** Spec / progress / proof. Not five, not seven. The discipline of "exactly three" matters because every added field is a field a fresh agent has to learn to read.
- **Self-contained.** The folder is portable. You can hand it to a different agent in a different rig and they can pick it up.
- **Feeds the UI.** The markdown in `slices/` is what generates the human-facing project view (web UI originally; `rig tui` terminal UI per the September 2026 update). The folder IS the source of truth; the UI is a derived view.

## The three fields, justified

- **Spec.md** — answers "what am I supposed to do?" A fresh agent's first read.
- **Progress.md** — answers "where am I?" Crucial for handoffs; lets the next agent see what's blocked, what's decided, what's been tried.
- **Proof/** — answers "did it actually work?" Not "did the code compile" but "did the feature work in practice." The author explicitly says "look at the proof that the work was done right."

## Trade-offs the source flags

- **Sometimes brittle.** The author is direct: "It's super simple, and sometimes a bit brittle, but it works."
- **Markdown over structured data.** Could have been JSON or a database. Markdown wins on portability and on being readable by both agents and humans.

## Relationship to other primitives

- **Workspace ([[Concepts/markdown-control-plane-workspace-engineering]]):** the slice is the smallest unit of the markdown control plane.
- **Workflow ([[Concepts/yaml-workflow-deterministic-rails]]):** a workflow usually orchestrates many slices; each slice becomes a queue item.
- **Queue ([[Concepts/owner-status-queue-handoff]]):** when a slice is ready for the next agent, it goes on the queue with `slice-017` as the handle.

## Related Concepts

- [[Concepts/markdown-control-plane-workspace-engineering]] — parent pattern
- [[Concepts/yaml-workflow-deterministic-rails]] — orchestration that moves slices between agents
- [[Concepts/owner-status-queue-handoff]] — durable handoff substrate for slices

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Workspaces: the markdown control plane"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Workspaces"
