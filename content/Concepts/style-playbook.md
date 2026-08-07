---
title: Style Playbooks (Design Tokens)

details: "Style playbooks are YAML-defined visual language playbooks for video production. They define typography, motion, audio, color, asset-generation constraints, and chart aesthetics. OpenMontage uses them to ensure visual consistency across a project and to bridge the gap between Remotion (React) and HyperFrames (HTML/GSAP) composition modes. The schema (schemas/styles/playbook.schema.json v2) defines design tokens: chart_palette, scale_system, weight_matrix, color_rules. The HyperFrames bridge (lib/hyperframes_style_bridge.py) converts a playbook into CSS custom properties plus a DESIGN.md, materializing a HyperFrames workspace ready to render. Playbooks are loaded via styles/playbook_loader.py — a Pydantic-validated loader that also serves as design intelligence."
tags:
  - concepts
  - architecture-pattern
created: 2026-07-02
updated: 2026-07-02
type: concept
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Style Playbooks (Design Tokens)

**Pattern source:** [[OpenMontage]]

## Overview

Style playbooks are YAML-defined visual language playbooks for video production. They define typography, motion, audio, color, asset-generation constraints, and chart aesthetics. They serve as the **single source of truth for visual style** across a project.

## Schema v2 Design Tokens

```yaml
# schema: schemas/styles/playbook.schema.json (v2)
playbook:
  name: "Ghibli Forest"
  chart_palette:
    primary:   "#5e8b3a"
    secondary: "#c9a85e"
    accent:    "#e87a3c"
  scale_system:
    base: 16
    ratio: 1.25     # major-third
  weight_matrix:
    thin:    300
    regular: 400
    bold:    700
  color_rules:
    text_on_dark: "#f4ecdc"
    text_on_light: "#2a2419"
  typography:
    display: "Cinzel"
    body:    "Lora"
  motion:
    ease:    "cubic-bezier(0.4, 0, 0.2, 1)"
    duration_short: 240
    duration_long:  1200
  audio:
    score_mood: "ambient, elegiac, sparse piano"
    sfx_profile: "soft, naturalistic"
  asset_generation:
    style_keywords: ["ghibli", "soft palette", "warm vignette"]
    negative_keywords: ["harsh shadows", "neon", "gritty"]
```

## The HyperFrames Bridge

`lib/hyperframes_style_bridge.py` converts a playbook into:
- **CSS custom properties** — `--color-primary`, `--scale-base`, etc. for the HyperFrames workspace
- **`DESIGN.md`** — a Markdown reference that the agent and human can read to understand the visual language

This materializes a HyperFrames workspace ready to render, with consistent typography, color, and motion.

## Loader and Validator

`styles/playbook_loader.py` is a Pydantic-validated loader that:
- Parses YAML against `playbook.schema.json`
- Validates design token references (e.g., `color_rules.text_on_dark` must point to a defined color)
- Surfaces the playbook to the rest of the system via a normalized object

It also acts as **design intelligence** — the loader can flag inconsistencies like "you defined `weight_matrix.bold: 700` but `typography.body` uses font weight 800".

## Why Playbooks Matter

- **Consistency** — every scene in a multi-clip production uses the same palette, motion, and typography
- **Cross-runtime portability** — a single playbook drives both Remotion and HyperFrames composition
- **Reviewability** — designers and producers can edit a YAML file, no code deploy needed
- **Version control** — playbooks diff cleanly in git, unlike binary assets

## Related

- [[HyperFrames]] — primary consumer
- [[Remotion]] — secondary consumer
- [[render-runtime-selection|Render Runtime Selection]]
- [[OpenMontage]] — primary implementation
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
