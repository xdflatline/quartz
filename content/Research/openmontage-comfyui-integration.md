---
title: "Research Index: OpenMontage + ComfyUI Integration"

details: "Research index synthesizing how to install OpenMontage and integrate it with ComfyUI. Captured 2026-07-02. The user runs Hermes on hardware that lacks support for ComfyUI local execution (verdict: cloud) → default to Comfy Cloud. ComfyUI exposes a REST API (POST /prompt) and WebSocket (/ws?clientId=...) for programmatic workflow execution, which makes it a viable drop-in local free video backend for OpenMontage's VIDEO_GEN_LOCAL_MODEL slot. This index documents: (1) why integrate, (2) the ComfyUI API surface, (3) the bridge pattern (custom tool adapter at tools/video/comfyui_video.py), (4) the integration protocol (Python shim + agent_skills[] entry + pipeline manifest override), (5) end-to-end example: a Ghibli-style 60-second short with Wan 2.1 video, Piper TTS narration, Remotion composition, FFmpeg post — all local via ComfyUI server."
tags:
  - research
  - video
  - tooling
created: 2026-07-02
updated: 2026-07-02
type: research
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Research Index: OpenMontage + ComfyUI Integration

**Updated:** 2026-07-02  
**Sources:** OpenMontage README / AGENT_GUIDE / PROJECT_CONTEXT, ComfyUI docs (comfy.org), Hermes `creative/comfyui` skill

---

## 1. Why Integrate OpenMontage with ComfyUI

OpenMontage is an **agentic** video production system — the AI coding assistant is the orchestrator, pipelines are YAML manifests, and tools are thin Python `BaseTool` subclasses. Its free / local video path (`VIDEO_GEN_LOCAL_ENABLED=true`) supports four backends out of the box:

- `wan2.1-1.3b` / `wan2.1-14b` — Wan 2.1
- `hunyuan-1.5` — Tencent Hunyuan
- `cogvideo-5b` — CogVideoX-5B
- `ltx2-local` — LTX-Video

Each of these requires its **native Python inference script** to be installed and a working CUDA / ROCm GPU. ComfyUI is a viable **alternative backend** because:

1. It ships **native nodes** for Wan 2.1 and Hunyuan Video.
2. It exposes a **REST + WebSocket API** (`POST /prompt`, `WS /ws`) — perfect for a `BaseTool` shim.
3. It runs **locally (CUDA / Metal / ROCm)** or on **Comfy Cloud** (1 concurrent free-tier job, 1080p VRAM ceiling).
4. The user's hardware lacks local GPU support → **Comfy Cloud** is the default per the established Hermes protocol.
5. Workflows are **declarative JSON DAGs** — reusable across runs, parameter-injectable from Python.

The result: an OpenMontage + ComfyUI integration lets the agent **drive ComfyUI workflows as tools** in any of the 12 production pipelines, with the agent deciding the prompt, the negative prompt, the seed, the LoRA stack, and the sampling parameters at runtime.

---

## 2. ComfyUI API Surface (for OpenMontage)

| Endpoint | Method | Purpose |
|---|---|---|
| `/system_stats` | GET | Server health and device info |
| `/object_info` | GET | List available node types and their schemas |
| `/prompt` | POST | Queue a workflow with a `client_id` |
| `/history/<prompt_id>` | GET | Fetch results after completion |
| `/view` | GET | Download an output file by filename |
| `/queue` | GET | Inspect the queue |
| `/ws?clientId=<id>` | WS | Real-time progress / execution events |

Local default: `http://127.0.0.1:8188`. Comfy Cloud default: `https://platform.comfy.org` (requires `COMFY_API_KEY`; 1 concurrent free-tier job, 1080p VRAM ceiling).

### The Minimal Workflow Submission

```python
import json
import urllib.request
import websocket  # pip install websocket-client

PROMPT = {
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "seed": 42,
            "steps": 20,
            "cfg": 7.0,
            "sampler_name": "euler",
            "scheduler": "normal",
            "denoise": 1.0,
            "model": ["10", 0],
            "positive": ["6", 0],
            "negative": ["7", 0],
            "latent_image": ["12", 0],
        },
    },
    # ... more nodes
}

req = urllib.request.Request(
    "http://127.0.0.1:8188/prompt",
    data=json.dumps({"prompt": PROMPT, "client_id": "openmontage-tool-001"}).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as resp:
    prompt_id = json.loads(resp.read())["prompt_id"]
```

Then subscribe to WebSocket for progress and fetch outputs via `/view?filename=...&type=output`.

---

## 3. Integration Architecture

```
┌──────────────────────────────────────────────────────────┐
│  OpenMontage Agent (Claude Code / Cursor / Copilot)      │
│  reads pipeline_defs/<pipeline>.yaml                     │
│  reads skills/pipelines/<pipeline>/<stage>-director.md   │
│  invokes tools via tools/tool_registry.py                │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────────┐
│  Custom Tool Adapter: tools/video/comfyui_video.py       │
│  - discovers ComfyUI server (local or cloud)             │
│  - loads Wan 2.1 / Hunyuan workflow JSON from disk       │
│  - injects prompt / negative / seed / sampler params     │
│  - POST /prompt with client_id                           │
│  - subscribes WS /ws?clientId=<id> for progress          │
│  - fetches output via /view?filename=...&type=output     │
│  - returns final asset path to the agent                 │
└─────────────────────┬────────────────────────────────────┘
                      │  REST + WebSocket
                      ▼
┌──────────────────────────────────────────────────────────┐
│  ComfyUI Server (local:127.0.0.1:8188 OR Comfy Cloud)    │
│  - Wan 2.1 native nodes                                  │
│  - Hunyuan Video native nodes                            │
│  - Stable Diffusion / FLUX image nodes                   │
│  - Real-ESRGAN upscaler                                  │
└──────────────────────────────────────────────────────────┘
```

---

## 4. Setup: Step-by-Step

### 4.1 Install OpenMontage

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup   # or the no-make fallback in the README
cp .env.example .env
```

### 4.2 Install ComfyUI (or use Comfy Cloud)

**Local (requires CUDA / Metal / ROCm GPU):**
```bash
# Recommended via comfy-cli
pipx install comfy-cli   # or: uv tool install comfy-cli
comfy install
comfy launch
curl http://127.0.0.1:8188/system_stats
```

**Cloud (no GPU required):**
1. Sign up at https://platform.comfy.org
2. Get an API key
3. Set `COMFY_API_KEY` in your environment

### 4.3 Install Wan 2.1 Workflow Pack

Either via the ComfyUI Manager UI (search "Wan 2.1") or via CLI:
```bash
comfy node install ComfyUI-WanVideoWrapper
comfy model download Wan2.1-T2V-1.3B  # or 14B for higher quality
```

The Hermes `creative/comfyui` skill has `scripts/check_deps.py` and `scripts/auto_fix_deps.py` for one-shot dependency resolution.

### 4.4 Create the Custom Tool Adapter

Create `tools/video/comfyui_video.py` in the OpenMontage repo:

```python
"""ComfyUI video generation tool for OpenMontage.

Slotted into tools/video/ alongside wan_video, hunyuan_video, etc.
Registered as a video_gen capability. Discovers ComfyUI server, injects
parameters into a saved workflow JSON, submits via REST, monitors via
WebSocket, fetches output via /view.
"""
from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
import websocket
from pathlib import Path
from tools.base_tool import ToolContract


COMFY_HOST = os.environ.get("COMFY_HOST", "http://127.0.0.1:8188")
COMFY_API_KEY = os.environ.get("COMFY_API_KEY")  # for Comfy Cloud
WORKFLOW_DIR = Path(__file__).parent / "workflows"


class ComfyUIVideo(ToolContract):
    name = "comfyui_video"
    description = "Generate a video via a ComfyUI workflow (Wan 2.1, Hunyuan Video, etc.)"
    cost_per_call = 0.0  # local or Comfy Cloud free tier
    latency_estimate_s = 60.0
    agent_skills = [
        "comfyui-rest-api",
        "wan-2-1-workflow",
        "video-prompting",
    ]

    def __init__(self, workflow_name: str = "wan2.1-t2v-1.3b"):
        self.workflow_name = workflow_name
        self.workflow = json.loads(
            (WORKFLOW_DIR / f"{workflow_name}.json").read_text()
        )

    def _inject(self, prompt: str, negative: str, seed: int, steps: int) -> dict:
        """Inject runtime parameters into the workflow graph."""
        wf = json.loads(json.dumps(self.workflow))  # deep copy
        for node in wf.values():
            ct = node.get("class_type", "")
            inputs = node.setdefault("inputs", {})
            if ct == "CLIPTextEncode" and inputs.get("text") in (None, "PLACEHOLDER_POSITIVE"):
                inputs["text"] = prompt
            elif ct == "CLIPTextEncode" and inputs.get("text") == "PLACEHOLDER_NEGATIVE":
                inputs["text"] = negative
            elif ct == "KSampler":
                inputs["seed"] = seed
                inputs["steps"] = steps
        return wf

    def run(self, *, prompt: str, negative: str = "", seed: int = 42,
            steps: int = 20, **_) -> dict:
        client_id = f"openmontage-{os.getpid()}-{int(time.time())}"
        workflow = self._inject(prompt, negative, seed, steps)

        # 1. POST /prompt
        req = urllib.request.Request(
            f"{COMFY_HOST}/prompt",
            data=json.dumps({"prompt": workflow, "client_id": client_id}).encode(),
            headers={"Content-Type": "application/json",
                     **({"Authorization": f"Bearer {COMFY_API_KEY}"} if COMFY_API_KEY else {})},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            prompt_id = json.loads(resp.read())["prompt_id"]

        # 2. WS /ws?clientId=<id> for progress
        ws = websocket.create_connection(
            f"{COMFY_HOST.replace('http', 'ws')}/ws?clientId={urllib.parse.quote(client_id)}"
        )
        output_filename = None
        try:
            while True:
                msg = json.loads(ws.recv())
                if msg["type"] == "executing" and msg["data"]["node"] is None and \
                   msg["data"]["prompt_id"] == prompt_id:
                    break
                if msg["type"] == "executed" and "output" in msg["data"]:
                    out = msg["data"]["output"]
                    if "videos" in out:
                        output_filename = out["videos"][0]["filename"]
        finally:
            ws.close()

        if not output_filename:
            raise RuntimeError("ComfyUI run completed but no video output found")

        # 3. GET /view?filename=...&type=output
        output_path = Path(f"./outputs/{output_filename}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(
            f"{COMFY_HOST}/view?filename={urllib.parse.quote(output_filename)}&type=output"
        ) as resp:
            output_path.write_bytes(resp.read())

        return {
            "path": str(output_path),
            "prompt_id": prompt_id,
            "seed": seed,
            "model": self.workflow_name,
        }
```

### 4.5 Save a Workflow JSON

Export a Wan 2.1 text-to-video workflow from the ComfyUI UI (right-click → "Save (API Format)"), then save it as `tools/video/workflows/wan2.1-t2v-1.3b.json`. Replace the `text` field of the positive CLIPTextEncode node with `"PLACEHOLDER_POSITIVE"` and the negative with `"PLACEHOLDER_NEGATIVE"`. The adapter will inject at runtime.

### 4.6 Register the Tool

Edit `tools/tool_registry.py` (or whatever the OpenMontage registry uses) to import and register the new tool:

```python
from tools.video.comfyui_video import ComfyUIVideo
registry.register(ComfyUIVideo())
```

### 4.7 Create a Layer 3 Skill

Add `.agents/skills/comfyui-video/SKILL.md` with prompting guidance specific to Wan 2.1 in ComfyUI (negative prompt curation, CFG/steps sweet spots for video, common failure modes like temporal flicker, etc.). This is mandatory — Rule Zero requires the agent to read Layer 3 skills before calling tools.

### 4.8 Optional: Override a Pipeline Manifest

To use ComfyUI as the default video provider in the documentary montage pipeline, edit `pipeline_defs/documentary-montage.yaml`:

```yaml
stages:
  assets:
    video:
      provider: comfyui_video
      model: wan2.1-t2v-1.3b
      negative_prompt: "static, slideshow, watermark, text, low quality"
```

---

## 5. End-to-End Example: 60s Ghibli-style Short (Fully Local)

**Prompt to the agent:**
```
"Make a 60-second Ghibli-style short about a fox wandering a misty forest at dawn.
Soft palette, watercolor, gentle camera drift. No narration. Ambient music only."
```

**Agent's pipeline execution (in order):**
1. **Pipeline selection** — `animation` (image-based, motion via Ken Burns) OR `cinematic` (real motion via ComfyUI video). Agent picks `cinematic` to use ComfyUI.
2. **Research** — web search for Ghibli visual references, ambient forest music sources.
3. **Script** — 60-second beat sheet: dawn, fox wakes, fox wanders, fox meets deer, fox returns to den.
4. **Scene plan** — 5 scenes × 12 seconds each, all video.
5. **Assets (video)** — `comfyui_video.run(prompt="...", seed=..., steps=...)` × 5 scenes via ComfyUI + Wan 2.1 1.3B.
6. **Audio** — `audio_mixer.assemble(music="ambient-forest.mp3", gain=-12dB)`.
7. **Edit** — `video_stitch.stitch(clips=[...], transitions=["crossfade"]*4)`.
8. **Compose** — `video_compose.compose(runtime="remotion", overlays=[captions])` — captions disabled, just title card.
9. **Self-review** — `ffprobe` checks duration ≈ 60s, `frame_sample` checks visual consistency, `audio_analysis` checks levels.
10. **Cost** — $0.00 (everything local).

**Result:** 60-second MP4, ~80MB, fully local, fully agent-driven, fully reproducible.

---

## 6. Verification Checklist

- [ ] OpenMontage `make setup` completes without error
- [ ] `comfy --version` works (local) OR `COMFY_API_KEY` is set (cloud)
- [ ] `curl http://127.0.0.1:8188/system_stats` returns JSON (local) OR `curl https://api.comfy.org/health` returns 200 (cloud)
- [ ] `python -c "from tools.tool_registry import registry; registry.discover(); print(registry.support_envelope())"` lists `comfyui_video` under `video_gen`
- [ ] `python -c "from tools.video.comfyui_video import ComfyUIVideo; t = ComfyUIVideo(); print(t.run(prompt='a fox in a forest', seed=1, steps=10))"` produces a video file
- [ ] Pipeline manifest override is valid YAML and parses without error
- [ ] Layer 3 skill at `.agents/skills/comfyui-video/SKILL.md` exists
- [ ] Test run with a 5-second Wan 2.1 video completes; output lands in `./outputs/`

---

## 7. Pitfalls

### Wan 2.1 14B is impractical without datacenter-class hardware
Stick to 1.3B for consumer GPUs, or default to Comfy Cloud for 14B. The user's hardware lacks local support → **always Comfy Cloud**.

### ComfyUI workflow JSON must be in API format
The editor-format JSON won't work for `POST /prompt` — you need the "Save (API Format)" export. Hermes `creative/comfyui` skill has a `template-integrity.md` reference that walks through this conversion.

### Cloud free tier has 1 concurrent job
If you queue two workflows in parallel, the second one stalls. The Hermes `creative/comfyui` skill's `run_batch.py` script has a `--max-concurrent 1` flag for cloud.

### The Layer 3 skill is mandatory
Rule Zero: "Use a tool without checking its Layer 3 skill for prompting guidance" is a CRITICAL reviewer finding. Don't skip the `.agents/skills/comfyui-video/SKILL.md`.

### Silent runtime swaps are governance violations
If you change `video_compose.runtime` from `remotion` to `ffmpeg` mid-pipeline, reviewers will catch it. Update the decision log explicitly.

### Parameter injection must be deterministic
Don't let the agent regenerate the workflow JSON at runtime — load the saved template, deep-copy, inject. This keeps runs reproducible.

---

## 8. Concepts

- [[instruction-driven-video-production|Instruction-Driven Video Production]] — OpenMontage's core pattern
- [[agent-first-pipeline-architecture|Agent-First Pipeline Architecture]] — no Python orchestrator
- [[capability-first-tool-design|Capability-First Tool Design]] — selector + provider pattern
- [[render-runtime-selection|Render Runtime Selection]] — Remotion vs HyperFrames vs FFmpeg
- [[style-playbook|Style Playbooks]] — YAML design tokens
- [[ai-agents|AI Agents]] — broader agent ecosystem context

## 9. Tools & Projects

- [[OpenMontage]] — agentic video production system
- [[ComfyUI]] — node-based visual AI engine (REST + WS API)
- [[Remotion]] — React composition engine
- [[HyperFrames]] — HTML/GSAP composition engine
- [[Wan 2.1]] — local free video model with native ComfyUI nodes
- [[Piper TTS]] — local free text-to-speech

## 10. Raw Sources

- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]] (README + AGENT_GUIDE + PROJECT_CONTEXT)

## 11. Cross-Cutting Themes

1. **Agent-First Wins** — instruction-driven beats framework-driven for production systems that need auditable, editable policy
2. **ComfyUI is a backend, not a replacement** — it slots into OpenMontage as one of many `video_gen` providers, not as a substitute for the orchestration layer
3. **Cloud-first for underpowered hardware** — Comfy Cloud's 1080p free tier is enough for most documentary-montage work; only drop to local when you have 24GB+ VRAM
4. **Workflows are the API contract** — a saved ComfyUI workflow JSON is the unit of reuse; the agent should never regenerate the graph at runtime
5. **Layer 3 skills carry the prompting knowledge** — Wan 2.1 in ComfyUI is forgiving but not magic; negative prompts, CFG, and steps matter

## 12. Next Research Directions

- [ ] Prototype `tools/video/comfyui_video.py` against local Wan 2.1 1.3B and benchmark latency
- [ ] Compare ComfyUI local (RTX 2080 Ti, fp8) vs Comfy Cloud free tier cost/perf
- [ ] Build a stable LoRA stack for Ghibli-style video in Wan 2.1
- [ ] Author a "decision log" review script that flags silent runtime swaps automatically
- [ ] Evaluate HeyGen gateway for the `cinematic` pipeline (it exposes VEO + Sora + Runway + Kling under one API key)
- [ ] Wire OpenMontage's `clip-factory` pipeline to use ComfyUI for batch clip generation
- [ ] Document an `ink-theater` + ComfyUI + HyperFrames workflow for character animation

## 13. References

- OpenMontage GitHub: https://github.com/calesthio/OpenMontage
- OpenMontage AGENT_GUIDE: https://github.com/calesthio/OpenMontage/blob/main/AGENT_GUIDE.md
- OpenMontage PROJECT_CONTEXT: https://github.com/calesthio/OpenMontage/blob/main/PROJECT_CONTEXT.md
- ComfyUI: https://comfy.org/
- ComfyUI Wan 2.1 docs: https://docs.comfy.org/tutorials/video/wan/wan-video
- ComfyUI server routes: https://docs.comfy.org/development/comfyui-server/comms_routes
- Hermes `creative/comfyui` skill — two-layer comfy-cli + REST/WS execution
- Hermes `wiki-content-ingestion` skill — Raw→Concept→Entity→Index protocol
