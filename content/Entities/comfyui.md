---
title: ComfyUI
detail: "Node-based visual AI engine for Stable Diffusion, FLUX, Wan 2.1, Hunyuan Video, and other image / video / audio models. Exposes a REST API (POST /prompt) and WebSocket (/ws) for programmatic workflow execution. Open-source and self-hostable, with a managed Comfy Cloud option."
details: "ComfyUI is a node-based visual AI engine (comfy.org) for Stable Diffusion, FLUX, Wan 2.1, Hunyuan Video, and other image / video / audio models. Workflows are defined as JSON DAGs of nodes (KSampler, CLIPTextEncode, VAEDecode, LoadCheckpoint, WanVideoSampler, etc.). ComfyUI exposes a REST API for programmatic execution: POST /prompt (queue a workflow with a client_id), GET /history/<prompt_id> (fetch results), GET /view?filename=...&type=output (download outputs), and a WebSocket /ws?clientId=<id> for real-time progress. Local execution requires a CUDA / Metal / ROCm GPU; cloud execution is available via Comfy Cloud (platform.comfy.org). The Hermes ComfyUI skill (creative/comfyui) provides a verified two-layer setup: comfy-cli for server lifecycle, REST/WS scripts for workflow execution with parameter injection. Native nodes exist for Wan 2.1 (text-to-video, image-to-video) and Hunyuan Video, making ComfyUI a viable local free video backend for OpenMontage via a custom tools/video/comfyui_video.py adapter."
tags:
  - entities
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://comfy.org/
sources:
  - Raw/openmontage-agentic-video-production.md
---

# ComfyUI

**Website:** [comfy.org](https://comfy.org/)  
**Category:** Node-based visual AI engine (image / video / audio)

## Overview

ComfyUI is a node-based visual AI engine for Stable Diffusion, FLUX, Wan 2.1, Hunyuan Video, and other image / video / audio models. Workflows are defined as JSON DAGs of nodes (KSampler, CLIPTextEncode, VAEDecode, LoadCheckpoint, WanVideoSampler, etc.) and executed locally or on Comfy Cloud.

## API Surface (for programmatic use)

| Endpoint | Method | Purpose |
|---|---|---|
| `/prompt` | POST | Queue a workflow with a `client_id` |
| `/history/<prompt_id>` | GET | Fetch results after completion |
| `/view` | GET | Download an output file by filename |
| `/queue` | GET | Inspect the queue |
| `/ws?clientId=<id>` | WS | Real-time progress / execution events |
| `/system_stats` | GET | Server health and resource info |
| `/object_info` | GET | List available node types |

Local default: `http://127.0.0.1:8188`. Comfy Cloud default: `https://platform.comfy.org` (requires API key; 1 concurrent free-tier job, 1080p VRAM ceiling).

## Strengths for OpenMontage Integration

- **Wan 2.1 native nodes** — `WanVideoSampler`, `WanVideoTextEncode`, etc. Already documented in [ComfyUI Wan2.1 Video Examples](https://docs.comfy.org/tutorials/video/wan/wan-video).
- **Hunyuan Video native nodes** — full text-to-video and image-to-video.
- **Workflow reuse** — save a graph once, swap parameters per call.
- **Self-hostable OR Comfy Cloud** — works for users without a GPU (the user's hardware lacks local support).
- **Two-layer tooling** — Hermes `creative/comfyui` skill uses comfy-cli for server lifecycle and direct REST/WS scripts (`run_workflow.py`, `run_batch.py`) for parameter-injected execution.

## Limitations

- Local execution requires CUDA / Metal / ROCm GPU; consumer GPUs (RTX 2080 Ti, etc.) hit VRAM ceilings at higher resolutions — use fp8 quantization or lower resolution
- Comfy Cloud free tier: 1 concurrent job, 1080p VRAM ceiling
- Free stock footage and TTS are not ComfyUI's job — it focuses on generation, not post-production

## Related

- [[OpenMontage]] — primary integration target
- [[Wan 2.1]] — ComfyUI has native Wan 2.1 nodes
- [[Piper TTS]] — pairs with ComfyUI for fully local pipelines
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]

## References

- ComfyUI website: https://comfy.org/
- ComfyUI Wan 2.1 docs: https://docs.comfy.org/tutorials/video/wan/wan-video
- ComfyUI server routes: https://docs.comfy.org/development/comfyui-server/comms_routes
- Hermes skill: `creative/comfyui` (two-layer comfy-cli + REST/WS)
