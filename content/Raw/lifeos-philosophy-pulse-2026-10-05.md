---
title: "LifeOS: Pulse (Philosophy)"
details: "The Life Dashboard — one always-on process (one daemon, one port, crash-isolated modules). The Observatory shows current-to-ideal progress plus the live health of every subsystem. Green/yellow/red menu-bar read at a glance."
tags:
  - raw
  - agent
  - observability
source: https://ourlifeos.ai/philosophy/pulse/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Pulse

**Source:** [https://ourlifeos.ai/philosophy/pulse/](https://ourlifeos.ai/philosophy/pulse/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Pulse

The Life Dashboard — the live surface where you watch the system run.


Fig. 18·One heartbeat, isolated modules, one parked by its breaker

LifeOS keeps running whether you’re watching or not — checks fire on their schedule, [memory](https://ourlifeos.ai/philosophy/memory) updates in the background. Pulse is where you watch it. One always-on surface: your progress from [current state to ideal state](https://ourlifeos.ai/philosophy/current-to-ideal-state), and the live health of everything doing the work.

## Why it exists

A system that works in the background is easy to lose track of. If you can’t see what it’s doing, you can’t tell whether it’s actually helping, and you can’t step in at the right moment. Trust needs a window.

Pulse is that window. It takes what LifeOS does out of the logs and puts it on a surface you can glance at. The point isn’t decoration. [A dashboard](https://danielmiessler.com/blog/the-life-dashboard) is what lets an operating system be an operating system _to you_, instead of a black box that occasionally speaks up. A LifeOS with no dashboard would still be a LifeOS. It just wouldn’t be one you could watch.

## How it works

Pulse is a single always-on process. On this machine it runs under one launchd job on one port, and it folded four services that used to run on their own into modules inside that one process: voice notifications, the Telegram bot, the iMessage bot, and [the observability server](https://ourlifeos.ai/philosophy/observability). Each module runs in its own crash-isolated loop, so if Telegram loses its connection the rest keep going.

At the center is a heartbeat loop. Every tick, Pulse checks each scheduled job against its cron schedule, runs the ones that are due, and routes their output to where you’ll catch it, whether that’s [spoken aloud](https://ourlifeos.ai/philosophy/voice) or pushed to your phone. Most jobs are small local checks that cost nothing: email, calendar, website health. When a check finds nothing worth saying, it emits a sentinel value and Pulse stays quiet instead of pinging you over noise. If a job fails three times running, a circuit breaker parks it until you’ve fixed the cause.

On top of the daemon sits the Observatory, a web dashboard served from the same process. That’s where the current-to-ideal picture lives: goal progress, what [the Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) is working on, your memory and freshness state, and the health of each subsystem. A native menu-bar app gives you the same read at a glance — green when it’s running, yellow when a tick goes stale, red when jobs are failing.

```
cd ~/.claude/LIFEOS/PULSE/MenuBar
bash install.sh    # Builds, deploys to ~/Applications, installs plist
```

The menu-bar readthe system's health, without opening anything

**Green** — ticks firing on schedule, jobs healthy. The system is alive.

**Yellow** — a tick went stale. Nothing broken yet, but something's lagging.

**Red** — jobs are failing. A circuit breaker parked something; it needs you.

## Where it fits

Pulse sits at the visible edge of the system. LifeOS is the operating system doing the work; Pulse is how you see it run. The two are separate on purpose. The OS would still be an OS with no dashboard, but you’d be flying blind, and Pulse is what keeps the whole thing in view.

It’s also where the other surface features show up. The [custom spinner verb](https://ourlifeos.ai/philosophy/spinner-verbs) and its rotating tips, plus the tooltips that explain each number, all render on or around this dashboard. If [euphoric surprise](https://ourlifeos.ai/philosophy/euphoric-surprise) is the feeling the system aims for and the Algorithm is the engine, Pulse is the pane of glass you press your face against to watch both happen.

## What it feels like

You start the day and Pulse has already run its checks. A voice tells you the two meetings coming up and the one email that actually needs you, and the rest stays quiet. Glance at the menu bar and it’s green, so you know the system is alive without opening anything.

pulse · morning run, spoken aloud

Two meetings today — standup at ten, the sponsor call at two.One email actually needs you: the contract from legal.everything else stayed quiet on purpose

Then you open the Observatory and see the shape of your week: how far each goal has moved, what the Algorithm ran while you slept, which parts of your memory are fresh and which have gone stale. It’s the difference between hoping a background system is working and watching it work.

[Full documentationPulse — the Life Dashboard →](https://docs.ourlifeos.ai/Pulse__PulseSystem)
