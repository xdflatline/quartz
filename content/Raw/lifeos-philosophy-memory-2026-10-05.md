---
title: "LifeOS: Cortex / Memory (Philosophy)"
details: "Cortex — the memory system. Two files load into every prompt (about you, about itself); behind them sits a Knowledge Archive of typed-link notes that ripen from seedling to evergreen. The test for inclusion: would you look this up by name?"
tags:
  - raw
  - agent
  - memory
source: https://ourlifeos.ai/philosophy/memory/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Cortex / Memory

**Source:** [https://ourlifeos.ai/philosophy/memory/](https://ourlifeos.ai/philosophy/memory/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Cortex

The memory system: everything LifeOS knows, compounding across sessions.


Fig. 12·A small hot layer fed by a graph of maturing notes

Cortex is LifeOS’s memory system, named for where the brain keeps long-term memory: experience is consolidated while you work and rest, then stored for good. Most tools forget you the moment you close them. [LifeOS keeps what you build together](https://danielmiessler.com/blog/personal-ai-infrastructure) — the work, the failures, the people you meet, the ideas you land — and every new session starts from that instead of from zero. On top of the raw record sits a typed graph of what you know, so the system can look things up the way you would.

## Why it exists

A system can only [close the gap between where you are and where you want to be](https://ourlifeos.ai/philosophy/current-to-ideal-state) if it knows where you actually are. That picture is what memory holds: what you’re working on, what broke last week, who you talked to, what you decided. Without it the system guesses, and it guesses the same wrong things every session, because nothing sticks.

There’s a cheap kind of memory that stores a few preferences and calls it done. This is the full record instead. If you built knowledge together, it lives here: work tracking, lessons from wins and failures, research, contact notes, runtime state. The whole point is that the next conversation is smarter than this one.

## How it works

Two files load into every prompt: one for what the system knows about you, one for what it knows about itself. This is the hot layer, kept small and current, so the facts that matter most are always in front of the model with no lookup at all.

Behind them sits the Knowledge Archive, a set of notes sorted into four kinds of thing: people, companies, ideas, and research. Every note carries typed links to related notes, so the archive is a graph you can walk rather than a pile of files. Notes join with plain wikilinks and ripen over time, from a rough seedling to a settled evergreen. The test for what belongs is one question: would you look this up by name?

A note in the archivetyped links make it a graph, not a pile

Person · evergreen**Jane Rivera** — VP Eng at Northwind. Met at the API summit.

- works at→ Northwind company
- championed→ the webhook redesign idea
- cited in→ "queues beat polling" research

**Notes ripen:** a rough _seedling_ becomes a settled _evergreen_ as you add to it. The test for what belongs — would you look this up by name?

```
bun run ~/.claude/LIFEOS/TOOLS/KnowledgeGraph.ts traverse <slug> --hops 2
```

Getting a note back is a fast keyword search across the whole corpus, no database, just those same markdown files ranked and pulled in when they’re relevant.

```
bun run ~/.claude/LIFEOS/TOOLS/MemoryRetriever.ts "query terms"
```

Memory also curates itself. A background reviewer reads recent conversation and writes back the full desired state of a memory file, so forgetting is simply leaving a stale fact out. Four safety tiers set what the system may write on its own and what it has to ask you about first.

## Where it fits

In LifeOS terms, memory is how the system reads your current state, and [the whole climb](https://ourlifeos.ai/philosophy/hill-climbing) toward your ideal state is measured against it. A sharper memory means a truer gap and a better next step.

Knowledge also compounds in one direction. A live work session drops its lessons into [the learning layer](https://ourlifeos.ai/philosophy/learning); the durable facts graduate up into the archive. Each level is more general and longer-lived than the one below, so over time the system holds not just more, but better.

## What it feels like

You mention someone you talked about a month ago and the context is already there. You open a project and the system remembers the two things that went wrong last time. You stop re-explaining your setup and your goals, because none of it was thrown away. It feels like working with someone who was paying attention the whole time, not a tool you have to brief from scratch every morning.

[Full documentationCortex — the LifeOS Memory System →](https://docs.ourlifeos.ai/Memory__MemorySystem)
