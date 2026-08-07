---
title: Stable Audio 3

details: Stable Audio 3 is a family of fast latent diffusion models for variable-length audio generation and editing, released May 2026. Available in small,...
tags:
  - entities
created: 2026-05-21
updated: 2026-05-21
type: entitie
sources:
  - .Raw/stable-audio-3-2026-05-21.md
confidence: high
---
# Stable Audio 3

## Overview

Stable Audio 3 is a family of fast latent diffusion models for variable-length audio generation and editing, released May 2026. Available in small, medium, and large variants.

## Technical Details

- **Architecture**: Latent diffusion operating on a novel semantic-acoustic autoencoder
- **Capabilities**: Text-to-audio generation, inpainting/editing, audio continuation
- **Performance**: Several minutes of audio generated in <2 seconds on H200 GPU, <few seconds on MacBook Pro M4
- **Variable-length**: Optimizes cost by only generating needed duration
- **Training data**: Licensed + Creative Commons (no scraped data)
- **Adversarial post-training**: Accelerates inference, improves fidelity and prompt adherence

## Release Status

- Weights released for **small** and **medium** models (consumer-usable)
- Large model available via API
- Training code and inference pipeline open source
- arXiv: 2605.17991 (cs.SD), submitted May 18, 2026

## Significance

Represents rapid maturation of generative audio:
- Competes with proprietary models in quality at consumer-accessible scales
- Variable-length generation addresses the fundamental cost problem in long-form audio
- Semantic-acoustic autoencoder design enables both fidelity AND editability

## Related Models
See also: [[lance-multimodal-model|Lance Multimodal Model]] — another recent open-weight generative model pushing boundaries at efficient scales.

[[stable-audio-3-2026-05-21|Source: stable-audio-3-2026-05-21]]
