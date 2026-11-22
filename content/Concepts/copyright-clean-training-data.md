---
title: "Copyright-clean training data (synthetic instruments and soundfonts)"
details: "Building a competitive audio model without any copyrighted recordings: synthesize instrument audio with exact MIDI ground truth, mix CC-licensed solo instruments through the URMP dataset, and morph roughly twenty soundfonts into additional timbres using the 'soundfont babies' technique. Dettato reports state-of-the-art transcription from this corpus, arguing the copyright constraint drives architecture innovation instead of blocking it."
tags:
  - concept
  - music
  - training
  - llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# Copyright-clean training data (synthetic instruments and soundfonts)

**Category:** Training Data / Provenance
**Status:** Used to train Dettato (2026-11); vendor-reported benchmark outcome

## Overview

Most audio models are trained on scraped recordings, which carry both licensing risk and imprecise labels. Dettato's training corpus was built from sources that can be used without permission, and the model still reports state-of-the-art transcription.

## The corpus

- **Synthetic instrument recordings** — audio rendered from known note events, so onset, pitch, duration and velocity labels are exact by construction.
- **CC-licensed solo instruments mixed through URMP** — the University of Rochester Multi-Modal Music Performance dataset, used to combine solo instrument tracks into ensemble mixtures.
- **~20 morphed soundfonts** — additional timbres generated with the author's ['soundfont babies'](https://kobi.music/research/making-soundfont-babies) technique, which interpolates between existing soundfont instruments.

No copyrighted recordings were used.

## Why synthetic data is a legitimate strategy here

- **Perfect labels.** MIDI-rendered audio comes with ground truth for free; no human annotation, no alignment error.
- **Controllable coverage.** The corpus can be steered toward rare instruments, dynamics and articulations that a scraped dataset might barely contain.
- **Mixture control.** Rendering separate stems and mixing them lets the model see ensemble combinations with per-stem labels — the URMP mixing step.
- **Legal clarity.** Outputs can be offered for commercial use, as Dettato's are.

## The usual objection, and the reported counter-evidence

The standard critique of synthetic training audio is the **synthetic-to-real gap**: models learn the renderer, not the instrument. Dettato's reported per-set scores are the author's answer — high F1 on real recordings, including:

- Bach10 (real ensemble recordings): 91.3
- PHENICX-Anechoic (real orchestral): 64.8
- RWC Classical (real): 64.4
- RWC Royalty-Free (real): 61.6

That is evidence, not proof: the scores are vendor-run, and the datasets are largely Western classical and small-ensemble material. See [[Concepts/transcription-evaluation-metrics]].

## The stronger claim

The author's argument is not merely that clean data is sufficient, but that the constraint **improves the result**:

> "The constraint of not using copyrighted recordings doesn't hold you back, but actually encourages innovation, and it's likely you'll end up with a better model in the end."

The mechanism is indirect: with no giant scraped corpus to throw at the problem, the team was pushed toward the architecture reframing in [[Concepts/pitch-lane-transcription-model]]. Data scarcity selected for a better inductive bias.

## Transferable pattern

1. **Start from what you can render or generate with exact labels**, then add real data only where the gap is demonstrated.
2. **Treat licensing as a design constraint, not a post-hoc filter** — it changes the architecture search, sometimes for the better.
3. **Mix synthetic stems, not synthetic mixtures**, so labels survive the mixing step.
4. **Report per-domain results**, because a synthetic-trained model's risk is concentrated in the domains the renderer covers least.

## Related Concepts

- [[Concepts/pitch-lane-transcription-model]] — the architecture the constraint pushed toward
- [[Concepts/transcription-evaluation-metrics]] — how to read the real-recording results
- [[Concepts/native-low-precision-training]] — another case where a training-time constraint shapes the final artifact
- [[Concepts/quantization-aware-training-qat]] — training-time constraints as quality levers

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Soundfont babies technique: https://kobi.music/research/making-soundfont-babies
- URMP dataset: https://www2.eecs.queensu.ca/ccm/?q=node/68
- Research: [[Research/audio-to-midi-transcription-2026]]
