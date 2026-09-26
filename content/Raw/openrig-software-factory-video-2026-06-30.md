---
title: "I Run A Cross-Harness Fleet As A Software Factory"
details: "Video transcript. After 8,000 hours coding with AI agents, the OpenRig creator describes a self-driving software factory built on four primitives: rigs, coordination, workflows, and workspaces — composed from Claude Code and Codex agents running in tmux."
tags:
  - raw
  - agent
  - agentic-system
created: 2026-09-26
updated: 2026-09-26
type: raw
source: https://m.youtube.com/watch?v=KlzyePs3bSk
---

# I Run A Cross-Harness Fleet As A Software Factory

**Channel:** OPENRIG
**Uploaded:** 2026-06-30
**Length:** 10:49
**URL:** https://m.youtube.com/watch?v=KlzyePs3bSk

> "After 8,000 hours coding with AI agents, I rigged Claude Code and Codex into one team — not two tabs I copy-paste between, but a cross-harness fleet that builds software while I steer."

## Description

After 8,000 hours coding with AI agents, the author rigged Claude Code and Codex into one team — not two tabs to copy-paste between, but a cross-harness fleet that builds software while the human steers. This is OpenRig.

Coding agents normally run alone, each locked in its own harness. OpenRig is the open-source coordination layer that wires them into one fluid team, a "rig." Claude is the big-picture, creative half. Codex is the relentless, precise half. OpenRig is the connective layer between them — the corpus callosum that lets two different model-brains act as one mind.

It runs locally on the Claude + Codex subscriptions you already have, and it's open source (Apache-2.0).

Under the hood it's just four small primitives: **rigs** (a whole team wrapped into one config file you run like infrastructure), **coordination** (agents talking over tmux, plus a durable queue so work never slips), **workflows** (deterministic rails the daemon enforces), and **workspaces** (a markdown control plane that keeps their thinking organized).

**GitHub:** github.com/mvschwarz/openrig
**Install:** `npm i -g @openrig/cli`
**Site:** openrig.dev
**License:** Apache-2.0

## Chapters

- 00:00 The self-driving software factory
- 00:54 The backstory: 8,000 hours
- 01:09 Scaling across harnesses: Claude + Codex
- 02:50 Rigs: a harness for harnesses
- 03:23 Coordination: tmux + a queue
- 05:16 Workflows: deterministic rails
- 06:12 Workspaces: the markdown control plane
- 07:25 Composing the software factory
- 08:14 Autonomy and recursive self-improvement
- 09:26 What it's like to use (Linkpix)
- 10:29 Outro

## Transcript

> "You tell me, but I think a lot of us want the same thing. A team of agents building and shipping real software on their own. In other words, a software factory. Unfortunately, this term carries a lot of hype right now, so it's kind of hard to tell what's real and what's a bit clickbait. But, here's a real deal, honest-to-goodness self-driving software factory."
>
> "This is a fleet of regular Claude Code and Codex agents working together to do real software development end to end with very little steering from me. They run in the terminal, so a regular Claude subscription will always work. This is Open Rig. It's open source. It's just a daemon, a CLI, and a web UI running on your laptop."
>
> "What's interesting is the core building blocks for this kind of software factory are deceptively simple."

### The backstory: 8,000 hours

> "The reason I built this is that I've already spent a ridiculous amount of time coding with agents, at least 8,000 hours. So, the math on that is it's been about 2 and 1/2 years since ChatGPT launched, and it's been an all-out sprint since then."
>
> "Today, the current harnesses let you scale mostly internally with sub-agents and things like that. This is powerful, but scaling externally is maybe even more important because it lets you team Claude with Codex or any other agent."

### Scaling across harnesses: Claude + Codex

> "Now, different models and harnesses specialize. Claude and Codex already demonstrate this. This is weird, but they map pretty cleanly onto our model of the left and right brain hemisphere. Claude is like the right hemisphere. Big picture, creative, but can become undisciplined. It's best for design and planning. Codex is like the left, precise, literal, but can get narrowly focused. But, it's the absolute best for debugging and code review. They balance like the hemispheres and coordinated well, they amplify each other and this is well worth the overhead."
>
> "So that coordination layer, like the corpus callosum inside the brain, well, that's where I've been focusing the bulk of the last year. For a long time I was just building little scripts and CLI wrappers, little tricks to keep this team of agents in the smart zone where they do their best work. A lot of it was slop. Some of it wasn't though. And the useful stuff proved itself over and over and eventually these distilled into a core set of primitives. And once those primitives started working together, I realized I wasn't just improving the code these agents could write. I was building a substrate for a software factory."

### Rigs: a harness for harnesses

> "There's just four main primitives. The first one is the rig. The easiest way to understand a rig is to start with one agent. An agent isn't just a model. It's a model sitting inside a harness, all the tools, memory, files that let it actually do work. A rig is the harness that wraps a whole team of those agents into one durable, nameable thing. So a harness for harnesses. Some call this a meta harness. And because a rig is just a config file, you can run those teams like infrastructure. Almost like Docker, but for agents."

### Coordination: tmux + a queue

> "Now, if you want to run more than one agent, you have to solve coordination first. So how do separate agents actually talk to each other? Well, this is simple. Just use tmux. The agents already live in terminals. Tmux lets you assign a handle to each terminal and this is like a named seat that that agent sits in. Then there's the send keys command. It lets one agent directly type prompts into the terminal of another agent. So you combine these and you get instant messaging between agents. Tmux can be a bit fiddled though, so Open Rig wraps it with the `rig send` command. So it's easier to use. So, there's no API and anything you can do in the agent's terminal, another agent can now do it. There's also the `rig capture` command, which can read another agent's live screen. And then `rig transcript` reads its saved history. So, that gives you the basic backbone. Agents now have these ergonomic tools that they can use to talk to each other."
>
> "Okay, but these messages, they're just ephemeral and they just end up in the chat history. And as you add more and more agents, messages can actually pile up and they get ignored. So, you'll still need a durable way to send work that won't fall through the cracks. Not a Jira-shaped thing. That's built for humans and it's a bit overkill for agents. All you need is a simple queue where every item has an owner and a status. So, you combine `rig send` with this `rig queue` and that's a reliable handoff between agents and it just works. So, we're just connecting all these tools together and now the system keeps work moving without me babysitting it."

### Workflows: deterministic rails

> "The third primitive is workflows. These are for when you need deterministic rails for the work agents do. A workflow is also a YAML config file. The daemon enforces it. For example, the planner agent writes a spec and then it gets routed via the queue to an agent that implements it, which then gets routed to an agent that tests it. So, the queue carries the work through the pipeline, not you. You don't have to track all this in your head anymore. And the agents write these workflows themselves."
>
> "Now, I realize this probably isn't the first time you've seen this, but what's unique is how simple it is. Workflows are often paired with a `rig watchdog` command. It's basically the clock, but it's useful because it can keep agents awake and working for weeks if you want. So, think of it like the loop command, except it works for both Claude and Codex."

### Workspaces: the markdown control plane

> "The fourth primitive is workspaces. So, the file system is super important. Agents use it to organize their thoughts, especially over long time frames, and a lot of what we call harness engineering is really workspace engineering. Plugins and skills, progress files, all in predictable folder locations. So, this has become a full-on control plane, except written in markdown. All this can get hectic real quick though, so your folder convention, it sounds trivial, but it's really important. The wrong shape can guarantee a mess, and it can kill your project. The right shape keeps agents thinking organized and transferable. So, a fresh agent can be productive immediately."
>
> "I took this seriously enough and made a simple primitive to make this easy and repeatable. The first win from thinking this way was the `rig scope` command. In just one move, an agent creates a ticket that's trackable in the system, along with a folder setup to use as a workspace for that slice. The markdown in these folders then generates this web UI you can use to check progress and look at the proof that the work was done right. It's super simple, and sometimes a bit brittle, but it works."

### Composing the software factory

> "Once you have those primitives now, you just compose them. The rig is the team, the workspace is where they think, coordination is how they talk, and workflows make the handoffs deterministic. You put those together, and a self-driving software factory is straightforward."
>
> "So, then your job collapses to mostly just one thing, steering. So you define a road map, you hand it off, and then you can watch. And then you step in when something needs your judgment. This is where the concept of altitude comes in. You decide how much to trust the agents on a given task, and then you manage by exception. Which means you stay up high while things are running just fine. And you drop all the way down into a terminal the moment you need to. So that level of autonomy becomes a dial that you control."

### Autonomy and recursive self-improvement

> "It turns out that if you have these primitives in place, you can turn that dial one more notch. A few months ago I ran this experiment on Open Rig to see if it could do recursive self-improvement. I already had a build rig going. The one that bootstrapped the first version. I then added a dedicated product management rig so that it could write better specs. After that I added a dog food rig so I could stress test things 24/7. So then I just took the feedback from the dog food rig, routed it to the product management rig, and well, the loop closed. It could run this way continuously. And it did so for a few weeks. Well, it actually got stuck a number of times on rate limits. But when those cleared it just resumed and kept going. It was weird. In RSA mode, it wasn't like I was building software anymore, obviously. It was more like I was growing it. I've since dialed it back to mostly just self-driving mode. I definitely need better guardrails in place before I do that in a public project. But the GitHub tells the story. It's currently shipping about as fast as it can without getting my Claude account banned."

### What it's like to use (Linkpix)

> "So what's it like to use? Well, most of the time you're just talking to one agent. The orchestrator. You tell it what you want. It'll `rig scope` that work into missions and slices, write the specs, hands the pieces to the right rigs, a build rig then builds, reviewers review, and then you get proof at the end. Step in only when something needs you. This link picks project is a good example. So, this was a half-built project I had. I thought might make a good low-stakes demo video so you could see it in action. It was like the flick of a finger and it built this road map and it started building. Now, I realize a single cloud code could have probably one-shotted this nowadays, but the point is that this project could continue building on its own like this for months. Maybe I'll make a follow-up video to show that."
>
> "So, that's the thing I want to make normal. Not just one impressive agent, but a real software team you can run locally on your laptop and then scale it straight into the cloud."

## Tags

`#AIcoding #ClaudeCode #Codex #AIagents #vibecoding #opensource #multiagent #softwarefactory #openrig`
