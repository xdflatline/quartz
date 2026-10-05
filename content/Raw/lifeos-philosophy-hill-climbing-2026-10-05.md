---
title: "LifeOS: General Hill Climbing (Philosophy)"
details: "Generalized hill climbing applied to any goal: from wherever you are, find the move that closes the most gap, take it, then look again. The same algorithm works on a bug, a book, or a career; one small checked step at a time."
tags:
  - raw
  - agent
source: https://ourlifeos.ai/philosophy/hill-climbing/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# General Hill Climbing

**Source:** [https://ourlifeos.ai/philosophy/hill-climbing/](https://ourlifeos.ai/philosophy/hill-climbing/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# General Hill Climbing

Every goal is a hill; the system keeps picking the next move that closes the gap.


Fig. 04·Probe, take the steepest step, repeat

Picture your goal as a hill and yourself partway up it. The next good move is the step that takes you higher. [Hill climbing](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing) is the system doing exactly that, over and over: from wherever you are, find the move that closes the most gap, take it, then look again.

## Why it exists

Big goals don’t get reached in one leap. You don’t cross from [your current state to your ideal state](https://ourlifeos.ai/philosophy/current-to-ideal-state) in a single move, and any plan that pretends otherwise breaks the moment it meets reality. What actually works is a repeatable step: look at where you are, look at where you want to be, take the move that shrinks the distance.

Hill climbing exists because that step is general. It doesn’t care whether the hill is a bug you’re chasing or a book you’re two chapters into. The same move works on both. So the system doesn’t need a different method for every kind of goal. It needs one method it can apply again and again, and this is it.

There’s a second reason. A single step is small enough to check. You can look at one move and say whether it took you higher or not. That makes the climb honest at every point, instead of only at the end when it’s too late to fix.

## How it works

On every interaction the system does one thing: pick the next move that reduces the gap between your current state and your ideal state. That’s the whole climb, run one step at a time.

One climb"get the newsletter out," one move at a time

- ✓Pick the week's one throughline from your notes — higher
- ✓Draft the three sections around it — higher
- ✓Cut it to the length people actually read — higher
- ○Next move: line up the links and ship — the step in front of you

**You never see the whole hill at once.** The system holds the shape of the goal and hands you the one step that's next — small enough to actually take.

The steps get better as you go. [Memory](https://ourlifeos.ai/philosophy/memory) compounds, so each session the system reads your current state more accurately than the last. [Skills](https://ourlifeos.ai/philosophy/skill-system) keep expanding, which gives it new ways to act on the gap. And some of the climb now runs on its own: [hooks](https://ourlifeos.ai/philosophy/hook-system) automate the routine moves so they happen even when you’re not watching. Each of those makes the next step land better than the one before.

[The Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) is this loop made systematic. Where a quick reply might take one obvious step and stop, the Algorithm runs the full climb in phases and checks after each one whether it’s genuinely higher up the hill or just busy. Simple asks get a short climb. Hard ones get the whole ascent.

## Where it fits

Hill climbing sits between the other two core ideas. Current State to Ideal State is the move the whole system makes. Hill climbing is how it takes each individual step of that move. [Euphoric Surprise](https://ourlifeos.ai/philosophy/euphoric-surprise) is how you know a step actually landed.

The Algorithm is where the climbing happens in practice, one phase at a time. [Pulse](https://ourlifeos.ai/philosophy/pulse) is where you watch it: the dashboard shows how far up the hill a piece of work has come and what the next step is. Memory and skills are what make each step stronger than the last.

## What it feels like

Think about the last time a huge goal felt frozen. It was too big to start, so you stared at it and did nothing. The size of the hill was the whole problem.

Hill climbing takes the hill off your shoulders. You never have to see the whole ascent at once, only the next move. The system holds the shape of the goal and hands you one step at a time, each one small enough to actually take. Progress stops feeling like a cliff and starts feeling like walking. You keep moving, and one day you look back and you’re most of the way up.

[Full documentationLifeOS — The Life Operating System Thesis →](https://docs.ourlifeos.ai/LifeOs__LifeOsThesis)
