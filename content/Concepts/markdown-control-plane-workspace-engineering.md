---
title: "Markdown Control Plane Workspace Engineering"
details: "Architecture principle where agents organize their long-term thinking through a markdown control plane — predictable folder layouts holding plugins, skills, steering docs, and progress files — making harness engineering mostly workspace engineering."
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

# Markdown Control Plane Workspace Engineering

**Category:** Workspace / Context Pattern
**Status:** Production pattern (OpenRig)

---

## Overview

Agents use the filesystem to organize their thinking over long timeframes. When you give every artifact (plugins, skills, steering docs, progress files) a **predictable folder location**, the filesystem stops being ad-hoc scratch space and becomes a **control plane written in markdown**. The author's blunt claim: "A lot of what we call harness engineering is really workspace engineering."

## The shape

```
project-root/
├── steering-docs/          # standing rules, conventions
├── skills/                 # reusable agent capabilities
├── plugins/                # integrations
├── progress/               # what's done, what's blocked
├── slices/
│   ├── slice-001/          # one `rig scope` creates this
│   │   ├── spec.md
│   │   ├── progress.md
│   │   └── proof/          # evidence the work was done right
│   ├── slice-002/
│   └── slice-003/
└── missions.md             # roadmap
```

## Two strong claims the source makes

1. **"Your folder convention sounds trivial, but it matters a lot. The wrong shape can guarantee a mess, and it can kill your project. The right shape keeps agents thinking organized and transferable, so a fresh agent can be productive immediately without anything from you."**
2. **The markdown in these folders generates the human-facing UI.** (Originally a web UI; per the September 2026 update in the blog post, it's now a terminal UI via `rig tui`.) The markdown IS the source of truth; the UI is a derived view.

## Why this works as a control plane

- **Markdown is universal.** Any agent harness can read it. No vendor lock-in.
- **Filesystem = state.** No database to sync, no schema migrations, no "where's the latest spec?" detective work.
- **Fresh agents bootstrap instantly.** A new agent joining the project reads the predictable layout and finds everything.
- **Proof is co-located.** `proof/` next to `spec.md` means verification evidence lives with the work, not in a separate system.

## The `rig scope` slice primitive

The source's named primitive for instantiating this pattern: **`rig scope slice create`** creates a folder for one slice of work, with:

- A spec (what this slice is supposed to do)
- A progress file (where it currently is)
- A place for proof (evidence the work was done right)

See [[Concepts/slice-folder-spec-progress-proof]] for the dedicated concept page.

## The "engineering is really workspace engineering" reframing

If you accept that most of what makes an agent team succeed is *what's on disk* — plugins it can find, skills it can reuse, progress files it can read — then the bulk of "harness engineering" is really:

- Choosing the right folder shapes
- Standardizing the file formats inside each folder
- Making the convention **predictable** so any new agent can orient itself

This is structurally similar to [[Concepts/agentic-harness-engineering-ahe]] (Agentic Harness Engineering as a discipline) but specifically emphasizes the *workspace* slice of the harness.

## Related Concepts

- [[Concepts/slice-folder-spec-progress-proof]] — the `rig scope` primitive
- [[Concepts/agentic-harness-engineering-ahe]] — the broader discipline
- [[Concepts/context-as-materialized-view]] — context as files instead of in-prompt assembly
- [[Concepts/coordination-topology-in-natural-language]] — workspace-encoded coordination rules

## Source

- [[Raw/openrig-software-factory-video-2026-06-30]] § "Workspaces: the markdown control plane"
- [[Raw/openrig-software-factory-building-blocks-2026]] § "Workspaces"
