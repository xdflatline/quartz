---
title: "LifeOS: Voice (Philosophy)"
details: "Spoken notifications: while the system works it speaks the phase, the result, and warnings — out loud, in a voice you pick. Pulse hosts the endpoint. Two passes clean the text (term map for pronunciation, context pass for homographs) before it goes to the speech service."
tags:
  - raw
  - agent
  - tooling
source: https://ourlifeos.ai/philosophy/voice/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Voice

**Source:** [https://ourlifeos.ai/philosophy/voice/](https://ourlifeos.ai/philosophy/voice/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Voice

Spoken notifications in a voice you choose.


Fig. 20·Text, corrected for pronunciation, sent out as speech

LifeOS talks to you. While it works it speaks the phase it’s in, tells you when a task lands, and warns you when something breaks, out loud, in a voice you pick. Start a long job, look away, and you still know exactly where it stands without watching the terminal.

## Why it exists

A terminal only tells you something if you’re staring at it. Start a real piece of work and you get two bad options: sit and watch a spinner, or walk away and lose the thread. Both cost you. One burns your attention on nothing; the other means you come back cold and have to rebuild what happened while you were gone.

Voice closes the gap between “the system is doing work” and “you know what it’s doing.” You hear “Investigating the API connection” when the work starts and “done, tests green” when it lands. Your eyes stay free for whatever you moved on to. The point is to keep you in flow instead of tethered to a screen.

## How it works

Every spoken line runs through one place. The endpoint lives inside [Pulse](https://ourlifeos.ai/philosophy/pulse), the Life Dashboard: one daemon, one port, one background job (`com.lifeos.pulse`). A [skill](https://ourlifeos.ai/philosophy/skill-system) or an Algorithm phase POSTs the text, Pulse hands it to the speech service, and it comes out in your chosen voice.

```
curl -s -X POST http://localhost:31337/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Running the WORKFLOWNAME workflow in the SKILLNAME skill to ACTION"}' \
  > /dev/null 2>&1 &
```

The words match what you asked for. A question gets “Checking…” or “Looking up…”; a command gets “Fixing…” or “Creating…”; a debug request gets “Investigating…” The announcement names the real work, not a canned “task started.”

The word matches the workno canned "task started"

- A question"Checking…" · "Looking up…"
- A command"Fixing…" · "Creating…"
- A debug"Investigating…"

Two passes clean the text before it’s spoken. A term map fixes words the speech engine would mangle: names, acronyms, anything it reads wrong. Then a context pass fixes homographs. “Live” said about a website (the site is live) sounds different from “live” the verb (where you live), so the system respells only the broadcast sense and leaves the verb correct.

Effort scales the chatter. A quick task speaks only at the start and the end. A deep, multi-phase run speaks every phase, Observe through Learn, so a long climb narrates itself. It’s all fire-and-forget: a voice call never blocks the work, and a missing speech service fails quietly instead of stopping anything.

## Where it fits

Voice is a supporting component, one of the subsystems the unique features lean on. [The Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) does the work and marks each phase; Voice is how those marks reach your ears. Pulse hosts the endpoint, so the thing you watch and the thing you hear come from the same daemon.

It’s also the front of a wider notification layer. Beyond the speaker, the same system can push to your phone with [ntfy](https://ntfy.sh/), post to a Discord channel, or fire a native desktop alert, routed by event. A normal finish just speaks. A long task or an error also pings your phone. A security alert goes to every channel. The defaults stay quiet on purpose, so the system earns each interruption instead of drowning you in them.

## What it feels like

You kick off a big job and go make coffee. From the kitchen you hear “Building the migration…” and, a minute later, “Done, fourteen criteria green, you’re good to ship.” You never looked at the screen, and you never wondered. The work told you itself, in a voice you know, at the two moments you cared about. That’s the feeling: present without being pinned, informed without watching.

voice · a long job, heard from the kitchen

Building the migration…Done — fourteen criteria green, you're good to ship.you never looked at the screen, and never wondered

[Full documentationThe Notification System →](https://docs.ourlifeos.ai/Notifications__NotificationSystem)
