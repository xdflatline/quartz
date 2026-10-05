---
title: "Self-Activating Skill Library with Intent Triggers"
details: "An architectural pattern for capability libraries in AI agent systems: each capability is wrapped in plain-language intent (a 'USE WHEN' clause) rather than fixed phrases. The agent matches the user's request *by meaning*, not by exact words — 'clean up this draft' and 'make this sound less like AI' both reach the same Writing skill. When a skill wakes, a routing table inside it points to the exact workflow for the job (the skill is the domain; the workflow is the specific procedure). Worked examples ship alongside each skill: showing a skill a real request-to-result pattern raises how often the system picks the right tool from 72% to 90%. Skills can compose: one can call another. A leading underscore marks the line between public (shareable) and private (personal, never leave your machine)."
tags:
  - concept
  - architecture-pattern
  - agent
  - tooling
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-skill-system-2026-10-05]]"
---

# Self-Activating Skill Library with Intent Triggers

**Source:** [[Raw/lifeos-philosophy-skill-system-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A skill is a piece of know-how the system already has, wrapped so it fires the moment you describe the task. You never pick it from a menu or memorize a command. You say what you want, and the skill that fits wakes up and runs.

An assistant that makes you remember how to reach each of its abilities isn't much of an assistant. Every command you have to look up is friction, and friction is where good tools quietly die.

## The four pieces

1. **The trigger** — a "USE WHEN" clause written as *intent*, not fixed phrases. The system reads triggers at startup and matches the user's request by meaning, not exact words.
2. **The routing table** — points at the exact workflow for the job. **The skill is the domain; the workflow is the specific procedure.** A blog skill holds separate workflows for drafting, publishing, and building a header image, and the request decides which one runs.
3. **The worked examples** — real request-to-result patterns. Showing a skill a worked example raises how often the system picks the right tool from 72% to 90%.
4. **The leading underscore convention** — plain-named skills are public and safe to share; underscore-named skills (`_MyPrivate`) hold personal detail and never leave your machine.

Trigger to actionyou describe the task; the right skill wakes

You say: "make this draft sound less like AI"

Matched by meaning, not exact words: The Writing skill's "USE WHEN" trigger fires — "clean up this draft" would reach it too.

Routes to the exact workflow: Its detect-and-rewrite workflow runs — not the draft or publish one.

## Composition and customization

**Skills compose.** One can call another, so a social-post skill pulls in the writing audit and the diagram maker without you wiring them together.

**Skills bend to you without losing their shared shape.** A public skill stays generic in its own files, then checks a separate folder for your preferences before it runs. The skill code is shareable; your taste lives outside it. That split is what lets the library be common to everyone and specific to you at the same time.

## Why this scales

There are already more than a hundred skills in the LifeOS reference library, covering writing, research, deploys, security, home devices, music, and much more. The library grows because adding a skill is how the whole system grows.

The key indicator that the pattern is working: **over time the shape of what you can ask keeps widening**, because every skill added is one more sentence the system now understands and can act on. The tool stops feeling like software you operate and starts feeling like a colleague who already knows the drill.

## Connection to other patterns

- [[Concepts/intent-engineering-as-productization]] — skills are the action surface that runs once intent is conveyed
- [[Concepts/ideal-state-artifact-isa]] — a skill's criteria sit in an ISA; the ISA is what the skill checks against
- [[Concepts/deterministic-hook-guardrails]] — hooks are the lifecycle and skill layers; both share the fixed-moments discipline

## Key Insights

1. **Triggers are intent, not strings.** "USE WHEN" matched by meaning; that's what makes the library self-activating.
2. **Skill = domain, workflow = execution.** One domain, multiple workflows; the request decides.
3. **Worked examples matter.** A request-to-result example lifts accuracy from 72% to 90% — the same data goes further with examples than with extra rules.
4. **A leading underscore is the privacy line.** Public skills share, private skills don't.

## Related Concepts

- [[Entities/lifeos]] — primary productization (the Skill System component)
- [[Concepts/intent-engineering-as-productization]] — the layer above that picks the right skill

## References

- Raw: [[Raw/lifeos-philosophy-skill-system-2026-10-05]]