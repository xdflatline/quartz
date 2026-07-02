---
title: Remotion
detail: "React-based video composition engine used by OpenMontage. Renders data-driven explainers, data visualizations, charts, tables, word-level TikTok-style captions, and talking heads via Node.js."
details: "Remotion is a React / Node.js framework for programmatically creating videos. OpenMontage uses it as one of three render runtimes (Remotion, HyperFrames, FFmpeg). Remotion is best for data-driven explainers, data viz, charts, tables, word-level captions, and talking heads. Spring animations, component composition, and integration with React's ecosystem (TypeScript, hooks) make it ideal for templated composition — assembling stock cut.type scene-types into compositions quickly, cheaply, reliably."
tags:
  - entities
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://github.com/calesthio/OpenMontage/blob/main/README.md
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Remotion

**Repository:** [remotion-dev/remotion](https://github.com/remotion-dev/remotion)  
**Category:** Video composition engine (React / Node.js)

## Overview

Remotion is a React-based framework for programmatically creating videos. OpenMontage uses it as one of three render runtimes (alongside HyperFrames and FFmpeg). Runtime is chosen at **proposal stage** (`render_runtime`) and locked through `edit_decisions`. Silent runtime swaps are treated as governance violations.

## Best For

- Data-driven explainers
- Data visualizations, charts, tables
- Word-level TikTok-style captions
- Talking heads
- Templated composition (assembling stock `cut.type` scene-types)
- React/TypeScript-native workflows

## Why It Works for OpenMontage

- Spring animations, component composition
- React ecosystem integration (TypeScript, hooks, npm packages)
- 8 Remotion components in `remotion-composer/src/components/`: TextCard, StatCard, ProgressBar, CalloutBox, ComparisonCard, and charts
- Fast templated scene assembly → ideal for batch output, localization variants, quick drafts, low-stakes internal clips

## Render Runtime Selection

When both **Remotion** and **HyperFrames** are available, OpenMontage's hard rule is to present both options to the user with:
1. One-sentence plain-language description of what it is best at for this specific brief
2. One-sentence honest tradeoff
3. Agent's recommendation and reason, tied to the brief's `delivery_promise` and visual approach

Then **wait for explicit user approval**. Record full shortlist as `options_considered` in `decision_log` under `render_runtime_selection`.

## Related

- [[HyperFrames]] — HTML/GSAP composition engine
- [[OpenMontage]] — primary user
- [[render-runtime-selection|Render Runtime Selection (Remotion vs HyperFrames vs FFmpeg)]]
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]

## References

- Remotion GitHub: https://github.com/remotion-dev/remotion
- Remotion docs: https://www.remotion.dev/docs/
