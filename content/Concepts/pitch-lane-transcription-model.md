---
title: "Pitch-lane transcription model (reframing AMT as a local problem)"
details: "Architectural reframing of automatic music transcription: instead of a large generative model that predicts a whole performance as a global sequence, model each pitch as its own lane and decide onset, sustain and offset locally. The same move — global generation replaced by local detection — is the one that works for optical music recognition; Dettato reports 20M parameters beating a 1.3B open model on the published composite."
tags:
  - concept
  - music
  - architecture-pattern
  - llm
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# Pitch-lane transcription model (reframing AMT as a local problem)

**Category:** Architecture Pattern
**Status:** Implemented in Dettato (2026-11); vendor-reported results

## Overview

Automatic music transcription (AMT) turns audio into note events. The default modern approach bolts a large sequence model onto the problem and lets it generate the transcription globally — which forces the model to learn the joint distribution of every instrument, every voice and every timing decision at once.

The pitch-lane reframing treats each pitch as an independent lane. For each lane the model answers local questions: does this pitch start here, is it still sounding, when does it stop? The global transcription is the union of local decisions, not a single generated sequence.

## The argument

Dettato's author reports reaching this position the hard way: after roughly ten months of work, the first attempt was scrapped in April 2026 because it treated AMT as a **data problem**. The conclusion: **the bottleneck is architecture**.

The stated mechanism is overfitting to synthetic training data. A global model has to learn the differences between the real problem and its synthetic approximation; a local model only has to learn what a note looks like in one lane. Reframing as local shrinks the distribution the model must match.

## The OMR parallel

The same pattern appears in optical music recognition (OMR) — turning scanned scores into machine-readable notation:

- Both fields were originally solved with algorithms.
- Both then adopted giant LLM components.
- In both, the global formulation overfits synthetic data.
- In both, a local formulation wins: **detector model** for OMR, **pitch-lane model** for AMT.

This is a reusable diagnostic: when a structured-prediction task plateaus despite more data, ask whether the output is being generated globally when it could be decided locally.

## Reported evidence

| System | Composite F1 | Parameters |
|---|---|---|
| Dettato | 60.8 | 20M |
| Mirelo A2M v1.1 Pro (closed) | 56.1 | not published |
| MuScriptor | 47.4 | 1.3B |
| YourMT3+ | 45.7 | 46M |

The parameter gap — roughly 65x smaller than MuScriptor — is the point: the gain is attributed to formulation, not capacity. See [[Concepts/transcription-evaluation-metrics]] for what the composite hides.

## Design implications

- **Output representation matters more than decoder size.** A piano-roll-like multi-label output avoids autoregressive token generation over long performances.
- **Local labels are cheap to supervise.** Onset/offset/frame targets can be derived from MIDI ground truth without a generative objective.
- **Instrument splitting does not fall out for free.** Dettato's author flags it as a weakness, which follows from the formulation: per-pitch lanes do not by themselves encode which instrument is playing.
- **Beat alignment is also a separate concern.** The model emits performance MIDI aligned to a beat; notation-level decisions are out of scope ([[Concepts/performance-midi-vs-notation]]).

## Related Concepts

- [[Concepts/copyright-clean-training-data]] — the other half of the author's argument
- [[Concepts/transcription-evaluation-metrics]] — how the claim is measured
- [[Concepts/performance-midi-vs-notation]] — what the output is and is not
- [[Concepts/decision-models-as-classifiers]] — the same instinct in a different domain: make the model answer local typed questions instead of generating

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Research: [[Research/audio-to-midi-transcription-2026]]
- Code: https://github.com/kobimusic/dettato
