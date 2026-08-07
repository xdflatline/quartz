---
title: Piper TTS

details: "Piper is a fast, local, offline neural text-to-speech engine developed by Rhasspy. OpenMontage uses it as the default TTS for the zero-API-key free path. Installation: `python -m pip install piper-tts`. Speaks WAV files from text + a voice ONNX model. Voices are downloadable from the Piper voices repository (50+ languages, multiple voice styles). No network calls, no rate limits, no per-character costs. Limitation: quality is below ElevenLabs / OpenAI TTS / Google TTS; not ideal for hero pieces where voice quality is critical, but perfect for drafts, internal videos, podcasts, and zero-cost pipelines."
tags:
  - entities
  - tooling
created: 2026-07-02
updated: 2026-07-02
type: entity
source: https://github.com/rhasspy/piper
sources:
  - Raw/openmontage-agentic-video-production.md
---

# Piper TTS

**Repository:** [rhasspy/piper](https://github.com/rhasspy/piper)  
**Category:** Local offline text-to-speech engine

## Overview

Piper is a fast, local, offline neural text-to-speech engine developed by the Rhasspy project. OpenMontage uses it as the default TTS for the **zero-API-key free path** — `make setup` installs it as part of the standard setup.

## Installation

```bash
python -m pip install piper-tts
```

Then download a voice ONNX model from the [Piper voices repo](https://github.com/rhasspy/piper/blob/master/VOICES.md) (50+ languages, multiple voice styles per language).

## Strengths

- **Free, offline, no API key** — no network calls, no rate limits, no per-character billing
- **Fast** — runs on CPU; GPU optional but not required
- **Open source** — Apache 2.0
- **Multi-language** — 50+ languages with multiple voice styles

## Limitations

- Voice quality is below ElevenLabs, OpenAI TTS, and Google TTS (the cloud providers)
- Not ideal for hero pieces where voice quality is critical
- Great for drafts, internal videos, podcasts, screen demos, and zero-cost pipelines

## Role in OpenMontage

- Default TTS when no cloud TTS key is set
- Used in the `screen-demo`, `podcast-repurpose`, `talking-head` pipelines when running free
- Pairs naturally with the documentary montage pipeline (real-footage + narration) and the animation pipeline (image-based video with voiceover)

## Related

- [[OpenMontage]] — primary user
- [[Wan 2.1]] — local free video generation companion
- [[Raw/openmontage-agentic-video-production|OpenMontage — Raw Source]]

## References

- Piper GitHub: https://github.com/rhasspy/piper
- Piper voices: https://github.com/rhasspy/piper/blob/master/VOICES.md
