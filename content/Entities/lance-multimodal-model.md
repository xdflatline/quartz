---
title: Lance Multimodal Model
detail: Lance is a 3B active-parameter native unified multimodal model from ByteDance supporting image/video understanding, generation, and editing within ...
details: Lance is a 3B active-parameter native unified multimodal model from ByteDance supporting image/video understanding, generation, and editing within ...
tags:
  - entities
created: 2026-05-21
updated: 2026-05-21
type: entitie
sources:
  - .raw/articles/lance-multimodal-image-video-generation-2026-05-21.md
confidence: medium
---
# Lance Multimodal Model

## Overview

Lance is a 3B active-parameter native unified multimodal model from ByteDance supporting image/video understanding, generation, and editing within a single framework. Trained from scratch (except ViT and VAE encoders) on 128 A100 GPUs.

## Capabilities

- **Text-to-Video**: Generate videos from text prompts with temporal consistency
- **Video Editing**: Multi-turn editing with temporal coherence across frames
- **Intelligent Video Understanding**: QA over video content, action counting, physics reasoning
- **Text-to-Image Generation**: Quality comparable to specialized image models
- **Image Editing**: Subject replacement, style transfer, object manipulation

## Key Claims

- Only **3B active parameters** achieves competitive benchmarks
- Staged multi-task training recipe
- Open weights for small and medium models
- Runs on consumer-grade hardware

## Significance

Pushes the frontier of unified multimodal modeling — a single model doing what previously required separate architectures for generation, editing, and understanding. The efficiency at 3B scale challenges the assumption that multimodal capability requires massive parameter counts.

## Competition
Related efforts: [[Concepts/stable-audio-3|Stable Audio 3]] shows similar trend toward efficient, open generative models at consumer-accessible scales.

[[Raw/articles/lance-multimodal-image-video-generation-2026-05-21|Source: lance-multimodal-image-video-generation-2026-05-21]]
