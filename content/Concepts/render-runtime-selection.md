---
title: Render Runtime Selection (Remotion vs HyperFrames vs FFmpeg)
detail: "Decision process for choosing between Remotion (React), HyperFrames (HTML/GSAP), and FFmpeg (CLI) for the final video composition. OpenMontage enforces a hard rule: when both Remotion and HyperFrames are available, the agent must present both and wait for explicit user approval."
details: "OpenMontage supports three render runtimes: Remotion (React/Node.js), HyperFrames (HTML/CSS/GSAP), and FFmpeg (CLI). Runtime is chosen at proposal stage (render_runtime) and locked through edit_decisions. Silent runtime swaps are treated as governance violations. The Decision Communication Contract hard rule: when both Remotion and HyperFrames are available, the agent must present both to the user with one-sentence best-for-this-brief, one-sentence honest tradeoff, and the agent's recommendation — then wait for explicit user approval. A decision_log entry with only one runtime considered when both were available is a CRITICAL reviewer finding. If only one runtime is available, the agent proceeds with it but says so explicitly and records the unavailable option as rejected_because: 'runtime not available on this machine'."
tags:
  - concepts
created: 2026-07-02
updated: 2026-07-02
type: concept
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Render Runtime Selection (Remotion vs HyperFrames vs FFmpeg)

**Pattern source:** [[OpenMontage]]

## The Three Runtimes

| Runtime | Stack | Best For |
|---|---|---|
| [[Remotion]] | React / Node.js | Data-driven explainers, data viz, charts, tables, word-level TikTok-style captions, talking heads, templated composition |
| [[HyperFrames]] | HTML / CSS / GSAP | Kinetic typography, hand-crafted motion, product promos, SVG-rigged character animation, atelier-mode (bespoke, one-of-a-kind) |
| FFmpeg | CLI | Fast image-based videos with Ken Burns motion, crossfades, overlays — minimum viable output |

## The State Machine

```
proposal  →  render_runtime chosen  →  edit_decisions locked  →  compose
```

Runtime is chosen at the **proposal stage** and recorded in `edit_decisions`. Silent runtime swaps are **governance violations** — reviewers flag them.

## The Hard Rule (Decision Communication Contract)

When both **Remotion** and **HyperFrames** are available (check `video_compose.get_info()["render_engines"]`), the agent **MUST present both options** to the user before locking `render_runtime`.

The presentation must include, for each runtime:
1. One-sentence plain-language description of what it is best at **for this specific brief**
2. One-sentence honest tradeoff (why it might not be the right pick)
3. Agent's recommendation and reason, tied to the brief's `delivery_promise` and visual approach

Then **wait for explicit user approval**. Record the full shortlist (both runtimes + any FFmpeg option) as `options_considered` in `decision_log` under `render_runtime_selection`.

> "A decision log entry with only one runtime considered when both were available is a CRITICAL reviewer finding." — AGENT_GUIDE.md

## Composition Authoring Mode

Separate decision from runtime. Log as `decision_log` (`category: "composition_mode"`).

| Mode | Description | When to Use |
|---|---|---|
| **Templated** | Assemble stock `cut.type` scene-types into compositions. Fast, cheap, reliable. Why most videos look alike. | Batch output, localization variants, quick drafts, low-stakes internal clips |
| **Atelier** | Hand-author composition from scratch: bespoke scenes, one-off theme, motion written for this piece. No reusable creative components. | **Default for hero pieces, brand films, festival shorts** |

## When Only One Runtime Is Available

If only one runtime is available, proceed with it but **say so explicitly** and record the unavailable option as `rejected_because: "runtime not available on this machine"`.

## Failure Mode Warning

The most common reviewer finding on OpenMontage productions is **silent runtime swap** — an agent that picked Remotion at proposal time, hit a snag during compose, and quietly fell back to FFmpeg without telling the user. This breaks the `delivery_promise` (the user was promised a Remotion data-viz explainer) and the fix is strict decision-log discipline.

## Related

- [[Remotion]] — React composition engine
- [[HyperFrames]] — HTML/GSAP composition engine
- [[instruction-driven-video-production|Instruction-Driven Video Production]]
- [[capability-first-tool-design|Capability-First Tool Design]]
- [[OpenMontage]] — primary implementation
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
