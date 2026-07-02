---
title: Capability-First Tool Design
detail: "Tool design pattern where a single selector tool delegates to a set of explicit provider tools. The selector asks the agent what capability it needs; the providers are concrete implementations. OpenMontage uses this for TTS, video generation, and image generation."
details: "Capability-first tool design is the pattern where a single selector tool asks the agent what capability it needs, then delegates to a set of explicit provider tools that are concrete implementations. OpenMontage uses this pattern across TTS, video, and image generation. The selector tool surfaces a provider menu; the agent picks based on cost, latency, and quality constraints. The provider tools are thin Python wrappers that call the actual API. Examples: tts_selector + elevenlabs_tts / google_tts / openai_tts / piper_tts; video_selector + heygen_video / wan_video / hunyuan_video / ltx_video_local / ltx_video_modal / cogvideo_video. This keeps the agent-facing surface area small (one selector per capability) while letting providers be added, swapped, or removed without changing the agent's logic."
tags:
  - concepts
created: 2026-07-02
updated: 2026-07-02
type: concept
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Capability-First Tool Design (Selector + Provider)

**Pattern source:** [[OpenMontage]]

## Overview

Capability-first tool design pairs a single **selector tool** with a set of explicit **provider tools**. The selector asks the agent what capability it needs (e.g., "text-to-speech") and returns a provider menu. The provider tools are thin Python wrappers that actually call the API or local backend.

This keeps the agent-facing surface area small (one selector per capability) while letting providers be added, swapped, or removed without changing the agent's logic.

## Examples from OpenMontage

### Text-to-Speech

```
tts_selector
├── elevenlabs_tts    (cloud, premium)
├── google_tts        (cloud, 700+ voices)
├── openai_tts        (cloud, fast, affordable)
└── piper_tts         (local, free, offline)
```

### Video Generation

```
video_selector
├── heygen_video          (cloud gateway)
├── wan_video             (local GPU, free)
├── hunyuan_video         (local GPU, free)
├── ltx_video_local       (local GPU, free)
├── ltx_video_modal       (Modal cloud)
└── cogvideo_video        (local GPU, free)
```

### Image Generation

```
image_selector
├── flux_image            (cloud)
├── imagen_image          (cloud, Google)
├── gpt_image             (cloud, OpenAI)
├── local_diffusion_image (local, free)
└── recraft_image         (cloud)
```

## Why This Pattern

- **Single contract per capability** — agent learns `tts_selector` once, gets every future provider
- **Provider isolation** — adding `elevenlabs_tts` doesn't break `piper_tts` or the agent
- **Cost-aware selection** — the selector can rank by cost/latency/quality and surface a menu
- **Easy A/B testing** — swap `wan_video` for `hunyuan_video` in a YAML override
- **Capability envelope** — registry can answer "what TTS providers are available right now?" with one call

## Provider Discovery

```python
from tools.tool_registry import registry
import json
registry.discover()
print(json.dumps(registry.support_envelope(), indent=2))
# Returns: { "tts": ["elevenlabs", "google", "openai", "piper"], ... }

print(json.dumps(registry.provider_menu(), indent=2))
# Returns: full menu with cost, latency, quality scores per provider
```

## The Seven-Dimension Scoring

Every provider selection is scored across **7 dimensions** with an auditable decision log:
1. Cost
2. Latency
3. Quality
4. Capability match
5. Reliability
6. License
7. Local vs cloud

The decision log is committed to the project — reviewers can later audit why a particular provider was chosen.

## Related

- [[instruction-driven-video-production|Instruction-Driven Video Production]]
- [[agent-first-pipeline-architecture|Agent-First Pipeline Architecture]]
- [[render-runtime-selection|Render Runtime Selection]]
- [[OpenMontage]] — primary implementation
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]
