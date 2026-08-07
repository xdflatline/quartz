---
title: "Superpowers (Claude Code skill)"

details: "Superpowers is a skill package for Claude Code that operationalises the [[Concepts/six-step-ai-build-process]]. A 'skill' in Claude Code is a set of working instructions given to the model once and that then applies to every project. At its core, Superpowers does exactly one thing: it forces the AI into an engineering process. Claude Code is not allowed to just start writing code. It must first ask questions (one after another), write the decisions into a specification document, turn that into a plan with small testable tasks, and only then build. At each transition the human is the checkpoint; without human approval the process does not advance. Patrick (The Node AI) used Superpowers to build his Second Brain and attributes the success of the build to the skill rather than to Claude Code's raw capability. The same pattern is transferable to any AI-assisted project: first decide, then put it in writing, then have it built in small steps with approval between each."
tags:
  - entities
created: 2026-07-25
updated: 2026-07-25
type: entitie
source: "[[Raw/thenodeai-second-brain-architecture-2026-07-25]]"
sources:
  - "Raw/thenodeai-second-brain-architecture-2026-07-25"
---

# Superpowers (Claude Code skill)

**Category:** Tool / Claude Code skill
**Platform:** Claude Code
**Linked in:** [[Entities/thenodeai]] video description

---

## Overview

A skill package for Claude Code that operationalises the [[Concepts/six-step-ai-build-process]]. A "skill" in Claude Code is a set of working instructions given to the model once and that then applies to every project. At its core, Superpowers does exactly one thing: it forces the AI into an engineering process. The skill is the source of the discipline, not the AI's raw capability.

## What the skill enforces

For every project where Superpowers is active, Claude Code must follow this discipline (Steps 2-5 of the [[Concepts/six-step-ai-build-process]]):

1. **Brainstorm** — Claude Code asks the human questions, one after another. It does not start writing code. At the end it proposes 2-3 approaches with pros and cons and the human decides.
2. **Specification** — everything that was decided goes in writing into a design document, section by section, with explicit human approval at each section. The specification is the contract.
3. **Plan** — from the specification, Claude Code breaks the work into small tasks, each with a test and a binary completion criterion.
4. **Build** — for each task, a fresh subagent is deployed. The human reviews the result before the next task starts. The human's role is to look at results, not read code.
5. **Test** — what is not tested is not done. Run a practical comparison in real conditions.

At each transition the human is the checkpoint. Without human approval, the process does not advance. This is the safeguard against the biggest risk in AI projects: building the wrong thing at full speed, convincingly and completely off-target for hours.

## Why it exists

The Node AI's framing: "The biggest risk in AI projects is not bad code. It is that the AI builds the wrong thing at full speed, convincingly and completely off-target for hours." Superpowers is the answer to that risk. The user does not need to be a project manager or have led a software team. The skill brings the discipline; the user brings the decisions.

## How it relates to a personal knowledge system

The same discipline applies whether the project is a Second Brain or a SaaS product. The pattern — first decide, then put it in writing, then have it built in small steps with approval between — is the transferable artefact. Superpowers is one concrete implementation of that pattern for Claude Code; the same pattern can be enforced with any AI assistant by following the [[Concepts/six-step-ai-build-process]].

## What it is not

- Not a coding tool. The skill does not write any code itself; it tells Claude Code *when* it is allowed to write code.
- Not a project-management framework for humans. The discipline is enforced by the skill on the AI; the human is the decider, not the executor.
- Not a model-specific advantage. The pattern is transferable to any tool that can ask and answer questions in turn.

## How to obtain it

The Node AI's description of the video links to the Superpowers skill. The community around the skill publishes install instructions and the underlying prompt. As of the video, the skill is free and open.

## Related Concepts

- [[Concepts/six-step-ai-build-process]] — the workflow Superpowers enforces
- [[Concepts/capabilities-first-system-design]] — produces the input Superpowers reasons about
- [[Concepts/three-reference-roles]] — used during the brainstorm step inside Superpowers

## References

- Raw Article: [[Raw/thenodeai-second-brain-architecture-2026-07-25]]
- Original: https://m.youtube.com/watch?v=mHSOsy_usAg
- Linked in: [[Entities/thenodeai]] video description
