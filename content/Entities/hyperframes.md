---
title: HyperFrames

details: "HyperFrames is an HTML / CSS / GSAP-based composition engine. OpenMontage uses it as one of three render runtimes (Remotion, HyperFrames, FFmpeg). HyperFrames is best for kinetic typography, hand-crafted motion, product promos, and SVG-rigged character animation. It pairs with OpenMontage's 'Atelier' composition mode — hand-authoring composition from scratch: bespoke scenes, one-off theme, motion written for this piece, no reusable creative components. Default for hero pieces, brand films, festival shorts, and anything that needs to feel one-of-a-kind. Workspace is materialized via lib/hyperframes_style_bridge.py, which converts a style playbook into CSS custom properties + a DESIGN.md."
tags:
  - entities
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://github.com/calesthio/OpenMontage/blob/main/PROJECT_CONTEXT.md
sources:
  - Raw/openmontage-agentic-video-production.md
---

# HyperFrames

**Category:** Video composition engine (HTML / CSS / GSAP)  
**Used by:** [[OpenMontage]]

## Overview

HyperFrames is an HTML / CSS / GSAP-based composition engine. OpenMontage uses it as one of three render runtimes (alongside [[Remotion]] and FFmpeg). It pairs naturally with OpenMontage's **Atelier** composition mode — hand-authoring composition from scratch: bespoke scenes, one-off theme, motion written for this piece, no reusable creative components.

## Best For

- Kinetic typography
- Hand-crafted motion design
- Product promos
- SVG-rigged character animation (reusable character acting)
- Hero pieces, brand films, festival shorts
- Anything that needs to feel one-of-a-kind (vs. templated)

## Style Playbook Bridge

`lib/hyperframes_style_bridge.py` converts a YAML style playbook into CSS custom properties plus a `DESIGN.md` for the HyperFrames workspace. The playbook schema (`schemas/styles/playbook.schema.json` v2) defines design tokens: `chart_palette`, `scale_system`, `weight_matrix`, `color_rules`.

## Render Runtime Selection (Hard Rule)

When both Remotion and HyperFrames are available, OpenMontage's hard rule is to present both options to the user with:
1. One-sentence plain-language description of what it is best at for this specific brief
2. One-sentence honest tradeoff
3. Agent's recommendation and reason, tied to the brief's `delivery_promise` and visual approach

Then **wait for explicit user approval**. A `decision_log` entry with only one runtime considered when both were available is a **CRITICAL reviewer finding**.

## Related

- [[Remotion]] — React/Node.js alternative
- [[OpenMontage]] — primary user
- [[render-runtime-selection|Render Runtime Selection (Remotion vs HyperFrames vs FFmpeg)]]
- [[style-playbook|Style Playbooks (Design Tokens)]]
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
