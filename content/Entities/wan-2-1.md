---
title: Wan 2.1

details: "Wan 2.1 is an open-source video foundation model from Wan-Video/Wan2.1. Available in two sizes: 1.3B parameters (fits consumer GPUs ~8GB VRAM with quantization) and 14B parameters (requires 24GB+ VRAM). Supports text-to-video, image-to-video, and instruction-guided video generation. ComfyUI has built-in nodes for Wan 2.1 (see docs.comfy.org/tutorials/video/wan/wan-video). In OpenMontage, Wan 2.1 is one of four local GPU video backends (Wan 2.1, Hunyuan, CogVideo, LTX-Video) enabled via VIDEO_GEN_LOCAL_ENABLED=true and VIDEO_GEN_LOCAL_MODEL=wan2.1-1.3b (or 14b). It is the cheapest path to actual motion video without cloud API spend."
tags:
  - entities
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://github.com/Wan-Video/Wan2.1
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Wan 2.1

**Repository:** [Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1)  
**Category:** Open-source text-to-video / image-to-video model

## Overview

Wan 2.1 is an open-source video foundation model from the Wan-Video team. It supports text-to-video, image-to-video, and instruction-guided video generation. ComfyUI ships native nodes for Wan 2.1 (see [ComfyUI Wan2.1 Video Examples](https://docs.comfy.org/tutorials/video/wan/wan-video)).

## Variants

| Model | Parameters | VRAM (with quantization) | Notes |
|---|---|---|---|
| `wan2.1-1.3b` | 1.3B | ~8 GB | Consumer-GPU friendly |
| `wan2.1-14b` | 14B | 24 GB+ | Higher quality, needs beefy GPU |

## Role in OpenMontage

Wan 2.1 is one of four local GPU video backends available in OpenMontage when `VIDEO_GEN_LOCAL_ENABLED=true`:

- `wan2.1-1.3b` / `wan2.1-14b` — Wan 2.1
- `hunyuan-1.5` — Tencent Hunyuan
- `cogvideo-5b` — CogVideoX-5B
- `ltx2-local` — LTX-Video (Lightricks)

It is the cheapest path to **actual motion video** without cloud API spend — the documentary montage pipeline uses it to generate b-roll when free stock archives don't have the right clip.

## Hardware Reality

The user's hardware lacks support for ComfyUI local execution → always default to Comfy Cloud for generation. Wan 2.1 1.3B at fp8 is the minimum threshold for consumer GPUs; 14B is impractical without datacenter-class hardware.

## Related

- [[OpenMontage]] — primary orchestration framework
- [[ComfyUI]] — Wan 2.1 has native ComfyUI nodes
- [[Piper TTS]] — local free narration companion
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]

## References

- Wan 2.1 GitHub: https://github.com/Wan-Video/Wan2.1
- ComfyUI Wan 2.1 docs: https://docs.comfy.org/tutorials/video/wan/wan-video
