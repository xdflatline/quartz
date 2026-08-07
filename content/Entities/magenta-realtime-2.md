---
title: Magenta RealTime 2

details: Google Magenta's open and local live music models enabling real-time music synthesis with low latency on standard hardware like MacBooks.
tags:
  - entities
  - llm
  - local-llm
created: 2026-06-05
updated: 2026-06-05
type: entity
---
# Magenta RealTime 2

**Magenta RealTime 2 (MRT2)** is an open-weights live music model and efficient real-time inference engine released by the Google Magenta team. Designed as a true live interactive instrument, it can be controlled with MIDI, audio, and text, performing low-latency on-device inference to respond instantly to inputs.

## Core Advancements

Unlike traditional generative music models that operate offline to turn a prompt into a complete track, MRT2 runs locally (specifically optimized for Apple Silicon via the [[mlx|MLX framework]] or JAX) and reacts live:

- **Ultra-low latency**: Achieves a frame size of 40ms and control latency around 200ms, roughly 15x lower latency than the first iteration of Magenta RealTime.
- **Multimodal Control**: Supports continuous expressive musical control via MIDI, audio, and text prompts.
- **Standalone and Plugin Ready**: Can be run as a standalone app, dropped into a DAW as a plugin, or integrated into other music software.
- **C++ Inference Engine**: Utilizes Apple's MLX to compile the model into an `.mlxfn` file, enabling streaming audio generation directly on MacBook GPUs.
- **Open-Weights**: Offers a 2.4B parameter version and a smaller 230M version capable of high-quality synthesis.

## Architecture

Both MRT1 and MRT2 are codec language models operating on sequences of audio tokens from the SpectroStream codec. MRT2 achieves its lower latency through **frame-level autoregression with frame-aligned conditioning**. 
- It uses a causal sliding window attention mechanism to enable continuous streaming generation while bounding memory.
- Learnable attention embeddings are incorporated to prevent context eviction artifacts (like ringing or feedback) over long generations.

## Releases
- The open-weights model (2.4B parameters).
- An open-source Python library for inference.
- A C++ inference engine using MLX.
- A suite of example applications and plugins.

## References
- [Original Announcement: Magenta RealTime 2](https://magenta.withgoogle.com/magenta-realtime-2)
- [[magenta-realtime-2-announcement|Raw Scrape]]
