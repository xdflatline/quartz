---
title: "The building blocks of a software factory are simple — OpenRig"
details: "Blog post companion to the YouTube video. Defines the four OpenRig primitives (rig, coordination, workflows, workspaces), the steering-by-altitude model, and a recursive-self-improvement experiment that ran a build/PM/dogfood rig loop for weeks."
tags:
  - raw
  - agent
  - agentic-system
created: 2026-09-26
updated: 2026-09-26
type: raw
source: https://openrig.dev/blog/software-factory-building-blocks
---

# The building blocks of a software factory are simple — OpenRig

**Author:** OpenRig
**Published:** 2026 (companion post to the 2026-06-30 video)
**URL:** https://openrig.dev/blog/software-factory-building-blocks
**Companion video:** https://www.youtube.com/watch?v=KlzyePs3bSk

> "Self-driving software factory is a phrase with a lot of hype on it, so here's what I mean by it. I run a fleet of regular Claude Code and Codex agents that do real software development, end to end, with very little steering from me. They run in the terminal, on ordinary subscriptions. The software that runs them is OpenRig. It's open source, and it's just a daemon, a CLI and a web UI on your laptop."
>
> "What's interesting is that the core building blocks are deceptively simple. There are four of them."

## The rig

Start with one agent. An agent isn't just a model. It's a model sitting inside a harness, all the tools and memory that let it actually do work.

A rig is the harness that wraps a whole team of those agents into one durable thing with a name. A harness for harnesses. Some people call that a meta-harness. And because a rig is just a config file, you can run those teams like infrastructure. It's almost like Docker, but for agents.

## Coordination

Once you have more than one agent, they have to talk to each other. Mine do it by typing into each other's terminals, with `rig send`, and they hand off work on a queue where every item has an owner and a status. (The author has [a separate post about this piece](https://openrig.dev/blog/cross-harness-agents), and about why putting Claude and Codex on one team is worth it.)

## Workflows

Sometimes you want deterministic rails for the work. A workflow is another config file, and the daemon enforces it.

Let's say a planner agent writes a spec. The workflow routes it through the queue to an agent that implements it, then to an agent that tests it. The queue carries the work through the pipeline, not you, so you don't have to keep all of it in your head. The agents write these workflows themselves.

> "I know you've seen pipelines like this before. What's different here is how simple it is."

Workflows usually come with a watchdog, which is basically a clock. It wakes agents on a schedule, and it can keep them working for weeks if you want. Think of Claude Code's `/loop`, except it works for Codex too.

## Workspaces

Agents use the filesystem to organize their thinking over longer stretches of time. A lot of what people call harness engineering is really workspace engineering. Plugins, skills, steering docs and progress files, all in predictable folder locations. It adds up to a control plane written in markdown.

It gets hectic fast. Your folder convention sounds trivial, but it matters a lot. The wrong shape can guarantee a mess that confuses your agents and kills the project. The right shape keeps their thinking organized and transferable, so a fresh agent can be productive immediately without anything from you.

So the author made that a primitive too. `rig scope slice create` sets up a slice of work as a folder, with a spec, a progress file and a place for proof. The markdown in those folders feeds a web UI where you can check progress and look at the proof that the work was done right. It's simple, it's sometimes brittle, and it works.

> **Update, September 2026:** the web UI has since been replaced by a terminal UI. Run `rig tui` to see your projects, missions and slices, with each slice's progress.

## Putting them together

> The rig is the team. The workspace is where they think. Coordination is how they talk. Workflows make the handoffs deterministic. Put those together and a self-driving software factory is pretty straightforward.

Your job collapses to mostly one thing, steering. You define a roadmap, hand it off and watch, and you step in when something needs your judgment.

This is where **altitude** comes in. You decide how much to trust the agents on a given task, and then you manage by exception. You stay up high while things are running fine, and you drop all the way down into a terminal the moment you need to. The level of autonomy becomes a dial you control.

## One more notch

It turns out that once you have these pieces in place, you can turn that dial one more notch. A few months ago the author ran an experiment to see whether OpenRig could do recursive self-improvement.

He already had a **build rig** going, the one that bootstrapped the first version. He added a **product management rig** to write better specs. Then he added a **dogfood rig** to stress test things around the clock. Then he routed the dogfood feedback back to product management, and the loop closed.

It ran that way continuously for a few weeks. It got stuck on rate limits more than a few times, but when those cleared it just picked up and kept going. At that point you aren't really building software anymore. You're growing it.

The author has since dialed it back to mostly self-driving. He wants better guardrails before running it that way on a public project. The GitHub history tells the story. It's shipping about as fast as it can without getting his Claude account banned.

## The point

> What I want to make normal isn't one impressive agent. It's a real software team you can run on your laptop and scale into the cloud.

OpenRig is open source. If you want to try it, go to openrig.dev, or ask Claude or Codex to install the CLI. The video shows it running on a real project.
