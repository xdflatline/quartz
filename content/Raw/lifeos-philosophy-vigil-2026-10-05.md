---
title: "LifeOS: Vigil (Philosophy)"
details: "The always-on watch: every part of the system that notices something writes to one event log in one format; a reader checks that log every five minutes and decides whether to interrupt you. See everything, interrupt rarely."
tags:
  - raw
  - agent
  - observability
source: https://ourlifeos.ai/philosophy/vigil/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Vigil

**Source:** [https://ourlifeos.ai/philosophy/vigil/](https://ourlifeos.ai/philosophy/vigil/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Vigil

One log of everything that happened, and a watcher that decides whether to tell you.


Fig. 15·Many sources, one log; only the urgent reaches you

Vigil is [the always-on watch](https://danielmiessler.com/blog/vigil-and-idea-to-video). Every part of LifeOS that notices something, a failing check, a job that stopped running, a new security finding, writes it to one event log in one format. A reader checks that log every five minutes and decides whether the thing is worth interrupting you for.

## Why it exists

A system with dozens of moving parts has dozens of ways to tell you something went wrong. One sends an email, one writes a file, one turns a dashboard tile red, and most say nothing at all. There is no single place to ask what is going on right now, so the problem you most needed to hear about can reach you from a customer or the news before it reaches you from your own tools.

The opposite failure is just as bad. An assistant that pings on every event gets muted within a week, and after that it cannot reach you when something is real. Vigil is built against both: see everything, interrupt rarely.

## How it works

Emitters are the parts of the system that watch something: standing questions that flip from pass to fail, [app health checks](https://ourlifeos.ai/philosophy/bunker), the security findings registry, background jobs, the complaint log, the news reader. Each one posts events in the same shape: where it came from, when, what kind of thing it is, how severe, a short title and summary, a pointer back into its own records, a privacy class, and a key that stops the same event from being stored twice.

An emitter never waits on Vigil. It writes to a local outbox first, with no network call, and a forwarder ships the unsent lines to the store afterwards. If the store is down, the event sits in the outbox until it is back and the emitter’s own job keeps running. [Restricted data](https://ourlifeos.ai/philosophy/security) never enters an event. The log holds the fact that something happened and a pointer to where the details live, and the store refuses anything that looks like a secret even if an emitter tries to send one.

The reader pulls everything since it last looked and routes each event by rules you set. Critical and high go to your phone as a text, medium waits for the next digest, and low and info appear only on [the dashboard](https://ourlifeos.ai/philosophy/pulse). A rolling 24-hour ceiling caps how many texts it sends, and only critical events get past it. Only sources you have marked as trusted can text you at all. An event the ceiling holds back is logged as held, never dropped.

One event, routedfrom the finding to your phone

EventA new high-severity vulnerability lands in the security findings registry.

→

RoutedHigh severity, a source allowed to text, and today's texts still under the ceiling.

→

SentA text with the title and a pointer, and the decision itself written back to the log.

**Why the last step matters:** the notification is an event like any other, so the log can count how often it interrupted you and why.

Every event takes one of three routes, and the rules that pick it live in one policy file you can read:

- text→ critical and high, from a trusted source. Past the day's ceiling only critical still gets through. interrupt
- digest→ medium events, held together for the next digest window. batch
- dashboard→ low and info, visible on the dashboard when you look, silent otherwise. silence

Routing is deterministic today. A [judged router](https://ourlifeos.ai/philosophy/glance) that weighs the same event against your current state can take over later, but only after it has been scored in shadow against the rules’ own decisions.

## Where it fits

Vigil is not [Synapse](https://ourlifeos.ai/philosophy/synapse). Synapse routes what you chose to capture: a link, a video, a spoken idea. Vigil watches what happened without anyone choosing it: a job died, a check failed, a finding landed. Synapse brings things to a home; Vigil brings things to you, or to silence.

It also leaves every emitter’s records where they are. The findings registry keeps its findings and the health checks keep their history; Vigil holds the event and a pointer, never the record. Because every tick writes a heartbeat and every notification is logged back as an event, Vigil watches itself too. A reader that stops running shows up as a missing heartbeat, not as a quiet week.

## What it feels like

Most of the time you hear nothing from it. You stop checking five dashboards in case one of them turned red, because anything that crossed a line you set would already have reached you. When your phone does buzz, the text says what happened and where to look. And when you want the whole picture, “what is going on right now” has one answer, read from one log, instead of a tour through every tool you run.
