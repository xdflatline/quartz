---
title: "LifeOS: The Skill System (Philosophy)"
details: "A library of self-activating, composable units of expertise. Every skill carries a 'USE WHEN' intent trigger; the system matches by meaning not exact words; one trigger can route to multiple workflows. Adding a skill is how the whole system grows."
tags:
  - raw
  - agent
  - tooling
source: https://ourlifeos.ai/philosophy/skill-system/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# The Skill System

**Source:** [https://ourlifeos.ai/philosophy/skill-system/](https://ourlifeos.ai/philosophy/skill-system/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# The Skill System

A growing library of self-activating, composable units of expertise.


Fig. 11·The one skill that fits rises on its own

A skill is a piece of know-how the system already has, wrapped so it fires the moment you describe the task. You never pick it from a menu or memorize a command. You say what you want, and the skill that fits wakes up and runs.

## Why it exists

An assistant that makes you remember how to reach each of its abilities isn’t much of an assistant. Every command you have to look up is friction, and friction is where good tools quietly die.

Skills remove that step. You describe the work in your own words and the right capability activates itself. The thesis states the job plainly: skills expand so the assistant can take more actions to [close the gap between where you are and where you want to be](https://ourlifeos.ai/philosophy/current-to-ideal-state). Each new skill is a new kind of move the system can make on your behalf.

There are already more than a hundred, covering writing, research, deploys, security, home devices, music, and much more. The library grows because adding a skill is how the whole system grows.

## How it works

Every skill is real code wrapped in a plain-language trigger. The trigger is a “USE WHEN” clause written as intent, not fixed phrases, so “clean up this draft” and “make this sound less like AI” both reach the same one. The system reads these triggers at startup and matches your request by meaning, not by exact words.

When a skill wakes, a routing table inside it points to the exact workflow for the job. [The skill is the domain; the workflow is the specific procedure](https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents). A blog skill holds separate workflows for drafting, publishing, and building a header image, and your request decides which one runs.

Trigger to actionyou describe the task; the right skill wakes

You say"make this draft sound less like AI"

↓

Matched by meaning, not exact wordsThe Writing skill's "USE WHEN" trigger fires — "clean up this draft" would reach it too.

↓

Routes to the exact workflowIts detect-and-rewrite workflow runs — not the draft or publish one.

**Worked examples do the heavy lifting.** Showing a skill a real request-to-result pattern raises how often the system picks the right tool from 72% to 90%.

Skills compose. One can call another, so a social-post skill pulls in the writing audit and the diagram maker without you wiring them together. Each skill also ships with worked examples, because showing the system a real request-to-result pattern raises how often it picks the right tool from 72% to 90%.

A leading underscore marks the line between public and private. Plain-named skills are generic and safe to share; underscore-named skills hold personal detail and never leave your machine.

## Where it fits

Skills are the system’s action surface. [The Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) decides what a task needs; skills are how the work actually gets done. When the Algorithm reaches a step that calls for a capability, it invokes the skill that owns it, the same way you would by naming the task.

They also bend to you without losing their shared shape. A public skill stays generic in its own files, then checks a separate folder for your preferences before it runs. The skill code is shareable; your taste lives outside it. That split is what lets the library be common to everyone and specific to you at the same time.

## What it feels like

You ask for a thing in the plainest words you have, and the right expertise is just there. No hunting for the command, no reading a manual to find the flag. Over time the shape of what you can ask keeps widening, because every skill added is one more sentence the system now understands and can act on. The tool stops feeling like software you operate and starts feeling like a colleague who already knows the drill.

[Full documentationCustom Skill System →](https://docs.ourlifeos.ai/Skills__SkillSystem)
