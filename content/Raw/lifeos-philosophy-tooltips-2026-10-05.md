---
title: "LifeOS: Custom Tooltips (Philosophy)"
details: "The dashboard explains itself on hover: every number, chart, and badge carries a tooltip, plus a freshness marker so you can tell what's stale before you read it. The pattern is reused across every panel — learn it once, holds everywhere."
tags:
  - raw
  - tooling
source: https://ourlifeos.ai/philosophy/tooltips/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Custom Tooltips

**Source:** [https://ourlifeos.ai/philosophy/tooltips/](https://ourlifeos.ai/philosophy/tooltips/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Custom Tooltips

The dashboard explains itself on hover instead of sending you to a manual.


Fig. 27·Point at any part and it explains itself

A dashboard that shows enough to be useful shows enough to confuse you. [Pulse](https://ourlifeos.ai/philosophy/pulse) handles that by explaining itself: every number, chart, and badge that isn’t obvious carries a tooltip, so you learn what a metric means the moment you hover over it. The surface teaches you instead of sending you to a manual.

## Why it exists

Density is the tradeoff every good dashboard makes. To be worth opening, Pulse has to pack a lot onto one surface — rings, charts, badges, counters. All of that is only useful if you know what each piece means, and a legend off to the side, or worse a separate doc, is where understanding goes to die.

So the explanation goes to the number. Hover a metric and its meaning appears right there, in context, while you’re looking at it. You never break your attention to go find out what you’re seeing. The dashboard stays dense and stays legible at the same time.

## How it works

A few kinds of tooltip cover the surface. Hover any point on a chart and you get its exact value and the label it sits under. Status badges and KPI tiles explain their own scoring and thresholds when you hover them, and the insight panels do the same. A per-panel freshness marker tells you how recently the data was refreshed.

That last one matters more than it sounds. Old data that looks current is worse than no data, because you’d act on it. The freshness indicator makes a stale panel visibly stale, with a marker showing when it last updated, so you can trust what’s fresh and discount what isn’t.

Under the surface, all of this runs on a few shared pieces in the Pulse dashboard. One ChartTooltip component is reused across every chart. One FreshnessIndicator draws the per-panel marker, reading from the freshness data the system already tracks. The heavier insight panels — phase bottlenecks, error heatmaps, [the knowledge graph](https://ourlifeos.ai/philosophy/memory), the business and finance views — each hang their own tooltips off those same shared parts. They all draw from one stylesheet too, so a tooltip in the finance view looks and behaves exactly like a tooltip on a chart. You learn the pattern once and it holds everywhere.

## Where it fits

Tooltips are a surface feature — part of how you see and feel LifeOS, next to Pulse itself and [the custom spinner](https://ourlifeos.ai/philosophy/spinner-verbs). They don’t change what the system does. They change whether you can read what it did.

That fits the larger point of [the dashboard](https://danielmiessler.com/blog/the-life-dashboard). Pulse exists so you can watch the system [move you from where you are toward where you want to be](https://ourlifeos.ai/philosophy/current-to-ideal-state). A number you can’t interpret is a number you can’t act on, so the tooltip is what turns the dashboard from a wall of readouts into something you understand at a glance.

## What it feels like

You open Pulse and a ring is sitting at some number you don’t recognize. You hover it, and a line tells you exactly what it’s measuring and how it’s scored. No tab-switch, no separate doc — the answer was attached to the thing the whole time.

Hover, and it explains itselfthe answer is attached to the number

What you see

Momentum  ·  0.62

A number with no context. Good? Bad? Measured how? You'd have to go find a doc.

What the tooltip says

share of active goals that moved this week · updated 4m ago

Meaning and freshness, right where you're looking. No tab-switch, no manual.

Then you notice a panel wearing a stale marker, and you know, before you read a single value, not to trust it yet. The dashboard shows you the data and, in the same glance, how much to believe it.

[Full documentationCustom Tooltips →](https://docs.ourlifeos.ai/Pulse__Tooltips)
