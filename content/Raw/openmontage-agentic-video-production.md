---
title: OpenMontage — Agentic Video Production System (Raw Source)

details: "Verbatim summary of the OpenMontage repository, captured 2026-07-02. Covers the 12 production pipelines, 52 tools across image / video / TTS / music / SFX / analysis, the three-layer knowledge stack (tools / skills / .agents/skills), the instruction-driven architecture (no Python orchestrator), the render-runtime decision (Remotion vs HyperFrames vs FFmpeg), local GPU support (Wan 2.1, Hunyuan, CogVideo, LTX-Video), and example production costs (sub-dollar videos using free stock + Piper TTS + fal.ai cloud)."
tags:
  - raw
  - agent
  - github-readme
created: 2026-07-02
updated: 2026-07-02
type: raw
source: https://github.com/calesthio/OpenMontage
---

# OpenMontage — Raw Source

**Repository:** https://github.com/calesthio/OpenMontage  
**License:** GNU AGPLv3  
**Stats (as of 2026-07-01):** 31.1k stars · 3.5k forks · 187 commits · 18 contributors  
**Tagline:** *The first open-source, agentic video production system. Turn your AI coding assistant into a full video production studio.*

---

## 1. Core Value Proposition

OpenMontage is an **agent-first** video production framework. There is no central Python orchestrator — the AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex) **is** the orchestrator. It reads pipeline manifests (YAML), reads stage director skills (Markdown), invokes tools (Python `BaseTool` subclasses), self-reviews against a meta-skill, and checkpoints progress to disk.

> **Important distinction:** OpenMontage can make image-based videos, but it can also make a **real video** for free/open-source workflows: the agent builds a corpus from free stock footage and open archives (Archive.org, NASA, Wikimedia Commons, Pexels, Pixabay), retrieves actual motion clips, edits them into a timeline, and renders a finished piece. This is not the usual "animate a handful of stills" trick.

**Scale:** 12 production pipelines · 52 tools · 500+ agent skills · 15 JSON schemas

---

## 2. Quick Start

### Prerequisites
- Python 3.10+
- FFmpeg (`brew install ffmpeg` / `sudo apt install ffmpeg`)
- Node.js 18+
- An AI coding assistant (Claude Code, Cursor, Copilot, Windsurf, Codex)

### Install

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

**No `make` fallback (macOS/Linux):**
```bash
python3 -m venv .venv && source .venv/bin/activate \
  && python -m pip install -r requirements.txt \
  && cd remotion-composer && npm install && cd .. \
  && python -m pip install piper-tts \
  && cp .env.example .env
```

**Windows PowerShell:**
```powershell
py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cd remotion-composer; npm install; cd ..
python -m pip install piper-tts
Copy-Item .env.example .env
```

> **Windows npm fix:** If `npm install` fails with `ERR_INVALID_ARG_TYPE`, use `npx --yes npm install` instead.

### First Prompt

```
"Make a 60-second animated explainer about how neural networks learn"
```

Or the real-footage path:

```
"Make a 75-second documentary montage about city life in the rain. Use real footage only, no narration, elegiac tone, with music."
```

---

## 3. The 12 Production Pipelines

| # | Pipeline | Output | Best For |
|---|----------|--------|----------|
| 1 | Animated Explainer | Research, narration, visuals, music | Education, tutorials |
| 2 | Animation | Motion graphics, kinetic typography | Social media, product demos |
| 3 | Avatar Spokesperson | Avatar presenter videos | Corporate comms, training |
| 4 | Cinematic | Trailer, teaser, mood-driven edit | Brand films, promos |
| 5 | Clip Factory | Batch of ranked short clips from long source | Content repurposing |
| 6 | Documentary Montage | Thematic montage from CLIP-indexed free stock | Video essays, real-footage edits |
| 7 | Hybrid | Source footage + AI support visuals | Enhancing existing footage |
| 8 | Localization & Dub | Subtitle, dub, translate | Multi-language distribution |
| 9 | Podcast Repurpose | Podcast highlights → video | Audiograms, marketing |
| 10 | Screen Demo | Polished software recordings | Tutorials, docs |
| 11 | Talking Head | Speaker videos | Presentations, interviews |
| 12 | Character Animation (beta) | SVG-rigged cartoon characters with pose libraries | Reusable character acting |

Every pipeline follows: `research → proposal → script → scene_plan → assets → edit → compose`.

---

## 4. The 52 Tools by Domain

### Video Generation (14 providers)
- **Cloud:** Kling, Runway Gen-4, Google Veo 3, Grok Imagine Video, Higgsfield, MiniMax Hailuo, HeyGen
- **Local GPU (free):** WAN 2.1 (1.3B / 14B), Hunyuan, CogVideo (2B / 5B), LTX-Video
- **Stock:** Pexels, Pixabay, Wikimedia Commons

### Image Generation (10 providers)
- **Cloud:** FLUX, Google Imagen 4, Grok Imagine Image, **GPT Image 2** (replaced DALL-E 2026-05-12), Recraft
- **Local / Free:** Local Diffusion (Stable Diffusion), Pexels, Pixabay, Unsplash, ManimCE

### Text-to-Speech (4 providers)
- ElevenLabs (cloud, premium)
- Google TTS (cloud, 700+ voices, 50+ languages)
- OpenAI TTS (cloud, fast, affordable)
- **Piper TTS (local, completely free, offline)**

### Music, SFX, Post-Production
- **Music:** Suno AI (full songs), ElevenLabs Music
- **SFX:** ElevenLabs SFX
- **Core (always free):** FFmpeg, Video Stitch/Trimmer, Audio Mixer/Enhance, Color Grade, Subtitle Gen

### Analysis & Enhancement
- **Analysis:** Transcriber (WhisperX), Scene Detect, Frame Sampler, Video Understand (CLIP/BLIP-2)
- **Enhancement:** Upscale (Real-ESRGAN), Background Remove (rembg), Face Enhance/Restore (CodeFormer/GFPGAN)
- **Avatar:** Talking Head (SadTalker/MuseTalk), Lip Sync (Wav2Lip)

---

## 5. Composition & Rendering Engines

Runtime is chosen at **proposal stage** (`render_runtime`) and locked through `edit_decisions`. Silent runtime swaps are treated as governance violations.

| Engine | Stack | Best For |
|--------|-------|----------|
| **Remotion** | React / Node.js | Data-driven explainers, data viz, charts, tables, word-level captions, talking heads |
| **HyperFrames** | HTML / CSS / GSAP | Kinetic typography, hand-crafted motion, product promos, SVG character animation, fully bespoke |
| **FFmpeg** | CLI | Fast image-based videos with Ken Burns motion, crossfades, overlays — minimum viable output |

**Hard rule (Decision Communication Contract):** When both Remotion and HyperFrames are available, the agent **MUST** present both to the user with one-sentence "best for this brief" and one-sentence honest tradeoff, then **wait for explicit approval** before locking `render_runtime`. A `decision_log` entry with only one runtime considered when both were available is a CRITICAL reviewer finding.

---

## 6. Free / Open Path (No API Keys)

Out of the box, `make setup` gives you:

| Capability | Free Tool | Notes |
|---|---|---|
| **Narration** | Piper TTS | Free, offline |
| **Open footage** | Archive.org + NASA + Wikimedia Commons | Free archival/documentary footage |
| **Extra stock** | Pexels + Unsplash + Pixabay | Free stock footage/images (developer keys free) |
| **Composition (React)** | Remotion | Spring animations, TikTok-style word-level captions, TalkingHead |
| **Composition (HTML/GSAP)** | HyperFrames | Kinetic typography, product promos, rigged SVG character animation |
| **Post-production** | FFmpeg | Encoding, subtitle burn-in, audio mixing, color grading |
| **Subtitles** | Built-in | Auto-generated captions with word-level timing |

### Example Production Costs (Verified)

| Production | Description | Cost |
|---|---|---|
| **"SIGNAL FROM TOMORROW"** | Cinematic sci-fi trailer — Veo motion clips, Remotion composition | — |
| **"THE LAST BANANA"** | 60s Pixar-style short; 6 Kling v3 motion clips (fal.ai), Google Chirp3-HD narration, royalty-free piano, TikTok-style word-level captions, Remotion composition | **$1.33** |
| **"The Library at Alexandria"** | 70s history elegy; 5 hand-authored bespoke scenes, OpenAI "ash" narration, free Pixabay strings score | **$0.02** |
| **"VOID — Neural Interface"** | Product ad with 1 API key (OpenAI); 4 GPT-generated images, TTS narration, auto-sourced music, WhisperX word-level subtitles, Remotion data viz | **$0.69** |
| **"Afternoon in Candyland"** | Ghibli-style anime; 12 FLUX images with multi-image crossfade, camera motion (zoom, pan, Ken Burns), particle overlays, ambient music | **$0.15** |
| **"Mori no Seishin"** | Ghibli-style forest spirit journey; 12 FLUX images with parallax crossfade, drift/pan motion, firefly/petal particles, cinematic vignette | **$0.15** |

---

## 7. Optional API Keys

```bash
# Image + video gateway:
FAL_KEY=your-key               # FLUX images + Google Veo + Kling + Hailuo + Recraft

# Free stock media (developer-tier free):
PEXELS_API_KEY=your-key
PIXABAY_API_KEY=your-key
UNSPLASH_ACCESS_KEY=your-key

# Music:
SUNO_API_KEY=your-key          # Full songs, instrumentals, any genre

# Voice & images:
ELEVENLABS_API_KEY=your-key    # Premium TTS, AI music, SFX
OPENAI_API_KEY=your-key        # OpenAI TTS, GPT Image 2
XAI_API_KEY=your-key           # Grok image edits/generation + Grok video
GOOGLE_API_KEY=your-key        # Google Imagen, Google TTS (700+ voices)

# More video providers:
HEYGEN_API_KEY=your-key        # VEO, Sora, Runway, Kling via single gateway
RUNWAY_API_KEY=your-key        # Runway Gen-4 direct
```

### Free Local Video Generation (GPU required)

```bash
make install-gpu
# Then add to .env:
VIDEO_GEN_LOCAL_ENABLED=true
VIDEO_GEN_LOCAL_MODEL=wan2.1-1.3b  # or wan2.1-14b, hunyuan-1.5, ltx2-local, cogvideo-5b
```

---

## 8. Three-Layer Knowledge Stack

```
Layer 1: tools/ + pipeline_defs/    "What exists" — executable tools + YAML manifests
Layer 2: skills/                     "How to use it" — conventions and quality bars
Layer 3: .agents/skills/             "How it works" — external tech knowledge packs
```

Each tool's `agent_skills[]` field bridges Layer 1 → Layer 3. The agent MUST read the Layer 3 skill before calling the tool — these contain provider-specific prompting guidance and parameter optimization.

---

## 9. Repository Layout

```
OpenMontage/
├── tools/              # 52 Python tools (video, audio, graphics, enhancement, analysis, avatar, subtitle)
├── pipeline_defs/      # YAML pipeline manifests
├── skills/             # Markdown skills (pipelines/, creative/, core/, meta/)
├── schemas/            # 15 JSON Schemas (contract validation)
├── styles/             # Visual style playbooks (YAML)
├── remotion-composer/  # React/Remotion composition engine
├── ink-theater/        # Web-based animation (mocap, procedural)
├── lib/                # Core infrastructure (config, checkpoints, pipeline loader, scoring)
└── tests/              # Contract tests, QA integration tests
```

---

## 10. Agent Contract (Rule Zero)

> *"Every video production request MUST go through the pipeline system. No exceptions."*

1. **Identify the pipeline** — match request to one in `pipeline_defs/`.
2. **Read the pipeline manifest** — `pipeline_defs/<name>.yaml` — know stages, tools, quality gates.
3. **Run preflight** — discover tools via registry. Present capability menu.
4. **Execute stage by stage** — for EACH stage, read `skills/pipelines/<pipeline>/<stage>-director.md` BEFORE doing any work.
5. **Read Layer 3 skills** — before using any tool with an `agent_skills` field, read the referenced skill in `.agents/skills/`.

**Do NOT:**
- Write ad-hoc Python scripts to call tools directly
- Skip the pipeline and go straight to API calls
- Generate assets without reading the stage director skill first
- Use a tool without checking its Layer 3 skill for prompting guidance
- Bypass preflight, checkpoints, or review

> *"The intelligence is in the skills, not in improvised code."*

### Decision Communication Contract

**Announce before execution** — before any paid or consequential generation call, state: exact tool name, provider, model/variant, reason chosen, whether sample or batch run.

**Ask before major changes** — provider swap, model family/variant change, video-led to still-led treatment, composition engine swap, dropping approved creative elements, sample → batch mode.

---

## 11. ComfyUI Integration (Local Free Video Path)

OpenMontage does **not** ship a native ComfyUI provider. However, the local free video path (`VIDEO_GEN_LOCAL_ENABLED=true`) is designed to run video models locally. The available local video backends are:

- `wan2.1-1.3b` / `wan2.1-14b` — Wan 2.1 from Wan-Video/Wan2.1
- `hunyuan-1.5` — Tencent Hunyuan
- `cogvideo-5b` — CogVideoX-5B
- `ltx2-local` — LTX-Video (Lightricks)

**Bridge pattern:** ComfyUI exposes a REST API at `POST /prompt` plus WebSocket `/ws` for progress. OpenMontage's local video tools call model backends through their native Python APIs (e.g., `wan_video.py` wraps the Wan 2.1 inference script). To integrate ComfyUI as a backend, the typical pattern is:

1. Run a ComfyUI server (local or Comfy Cloud).
2. Submit an API-formatted workflow JSON to `POST http://HOST:PORT/prompt` with a `client_id`.
3. Subscribe to `ws://HOST:PORT/ws?clientId=<id>` for progress events.
4. Fetch the resulting image/video via `GET /view?filename=...&type=output` (or `/history/<prompt_id>`).

A custom OpenMontage `comfyui_video.py` tool would slot into `tools/video/` and be wired into `tool_registry.py` as a `video_gen` capability. The agent would discover it via `python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"`.

---

## 12. Source Attribution

- **README:** https://github.com/calesthio/OpenMontage/blob/main/README.md
- **AGENT_GUIDE:** https://github.com/calesthio/OpenMontage/blob/main/AGENT_GUIDE.md
- **PROJECT_CONTEXT:** https://github.com/calesthio/OpenMontage/blob/main/PROJECT_CONTEXT.md
- **License:** GNU AGPLv3
