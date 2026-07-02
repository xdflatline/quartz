---
title: OpenMontage
detail: "Open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turns any AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) into a full video production studio."
details: "OpenMontage is the first open-source, agentic video production system. The AI coding assistant is the orchestrator — there is no central Python orchestrator. The agent reads pipeline manifests (YAML), reads stage director skills (Markdown), invokes tools (Python BaseTool subclasses), self-reviews against a meta-skill, and checkpoints progress to disk. Supports 12 production pipelines (Animated Explainer, Cinematic, Documentary Montage, Hybrid, Avatar, Character Animation, etc.), 52 tools (Wan 2.1, Hunyuan, CogVideo, Kling, Veo, FLUX, Piper TTS, WhisperX, Remotion, HyperFrames, FFmpeg), 15 JSON schemas, and 500+ agent skills. Free open-source path: Piper TTS + Archive.org / NASA / Wikimedia / Pexels / Pixabay + Remotion or HyperFrames + FFmpeg. Verified sub-dollar productions (e.g., 'Mori no Seishin' Ghibli-style anime = $0.15)."
tags:
  - entities
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://github.com/calesthio/OpenMontage
sources:
  - Raw/openmontage-agentic-video-production.md
---

# OpenMontage

**Repository:** [github.com/calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)  
**License:** GNU AGPLv3  
**Category:** Agent-first video production framework

## Overview

OpenMontage is the first open-source, agentic video production system. The AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) is the orchestrator — there is no central Python orchestrator. The agent reads pipeline manifests (YAML), reads stage director skills (Markdown), invokes tools (Python `BaseTool` subclasses), self-reviews against a meta-skill, and checkpoints progress to disk.

> "The intelligence is in the skills, not in improvised code." — AGENT_GUIDE.md

## Scale

- 12 production pipelines
- 52 tools (video, image, TTS, music, SFX, analysis, enhancement)
- 500+ agent skills
- 15 JSON schemas (artifact contracts)

## Key Capabilities

- **Free / open path:** Piper TTS + Archive.org / NASA / Wikimedia / Pexels / Pixabay + Remotion or HyperFrames + FFmpeg. Zero API keys required.
- **Local GPU video:** Wan 2.1 (1.3B / 14B), Hunyuan, CogVideo (2B / 5B), LTX-Video.
- **Cloud video:** Kling, Runway Gen-4, Google Veo 3, Grok Imagine Video, MiniMax Hailuo, HeyGen.
- **Image:** FLUX, Google Imagen 4, Grok Imagine Image, GPT Image 2 (replaced DALL-E 2026-05-12), Recraft, Local Diffusion.
- **Composition engines:** Remotion (React), HyperFrames (HTML/GSAP), FFmpeg (CLI).
- **Reference-to-video:** Paste a YouTube/Short/Reel/TikTok URL → grounded production plan with cost estimate and sample.

## The 12 Pipelines

Animated Explainer, Animation, Avatar Spokesperson, Cinematic, Clip Factory, Documentary Montage, Hybrid, Localization & Dub, Podcast Repurpose, Screen Demo, Talking Head, Character Animation (beta).

Each pipeline: `research → proposal → script → scene_plan → assets → edit → compose`.

## Verified Sub-Dollar Productions

| Production | Description | Cost |
|---|---|---|
| **"THE LAST BANANA"** | 60s Pixar-style short; 6 Kling v3 motion clips, Google Chirp3-HD narration | **$1.33** |
| **"The Library at Alexandria"** | 70s history elegy; 5 bespoke scenes, OpenAI TTS, Pixabay score | **$0.02** |
| **"VOID — Neural Interface"** | Product ad; 4 GPT images, TTS, auto-sourced music, Remotion data viz | **$0.69** |
| **"Afternoon in Candyland"** | Ghibli-style anime; 12 FLUX images, camera motion, particle overlays | **$0.15** |
| **"Mori no Seishin"** | Ghibli-style forest spirit; 12 FLUX images, parallax crossfade, vignette | **$0.15** |

## Related

- [[Remotion]] — React-based composition engine
- [[HyperFrames]] — HTML/GSAP composition engine
- [[Wan 2.1]] — local free video generation model
- [[Piper TTS]] — local free text-to-speech
- [[instruction-driven-video-production|Instruction-Driven Video Production]] — core architectural pattern
- [[agent-first-pipeline-architecture|Agent-First Pipeline Architecture]] — no Python orchestrator
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]

## References

- GitHub: https://github.com/calesthio/OpenMontage
- AGENT_GUIDE: https://github.com/calesthio/OpenMontage/blob/main/AGENT_GUIDE.md
- PROJECT_CONTEXT: https://github.com/calesthio/OpenMontage/blob/main/PROJECT_CONTEXT.md
- License: GNU AGPLv3
