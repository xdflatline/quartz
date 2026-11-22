---
title: "Dettato"
details: "A 20M-parameter open-source audio-to-MIDI transcription model from kobimusic, released 2026-11-16. Reports a 60.8 composite F1 (onsets 70.8, frames 79.1, offsets 40.9, drums 52.5), ahead of the closed Mirelo A2M v1.1 Pro at 56.1 and the 1.3B open MuScriptor at 47.4, while trained entirely without copyrighted recordings. Outputs beat-aligned performance MIDI, is weak at splitting instruments, and is hosted with a 30-credit-per-day free tier."
tags:
  - entity
  - music
  - llm
  - tooling
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# Dettato

**Category:** Audio-to-MIDI transcription model (open source)
**Author:** [[Entities/kobimusic]]
**Released:** 2026-11-16
**Code:** https://github.com/kobimusic/dettato
**Site:** https://kobi.music/research/dettato

## Overview

Dettato transcribes audio into MIDI note events. It is a **20M-parameter** model — roughly 65x smaller than the next best open model, MuScriptor at 1.3B — built on a [[Concepts/pitch-lane-transcription-model|pitch-lane formulation]] rather than a global generative one.

It was trained with **no copyrighted recordings**: synthetic instrument audio, CC-licensed solo instruments mixed via URMP, and about twenty morphed soundfonts ([[Concepts/copyright-clean-training-data]]).

## Reported benchmark results

| Measure | Dettato | Mirelo A2M v1.1 Pro | MuScriptor 1.3B | YourMT3+ 46M |
|---|---|---|---|---|
| Composite | **60.8** | 56.1 | 47.4 | 45.7 |
| Onsets | **70.8** | 67.1 | 57.0 | 58.2 |
| Frames | **79.1** | 75.7 | 71.2 | 63.9 |
| Offsets | **40.9** | 40.1 | 31.4 | 30.5 |
| Drums | **52.5** | 41.4 | 30.1 | 30.0 |

Composite sets: PHENICX, RWC classical, RWC royalty-free. Per-set results range from 91.3 (Bach10) to 48.7 (RWC Genre). See [[Concepts/transcription-evaluation-metrics]] for how to read them.

Notably, Dettato's margin over the closed Mirelo model narrows on RWC Classical (64.4 vs 65.8) — the only reported set where it trails.

## Output and limitations

- **Output:** performance MIDI with a beat aligned — not sheet music ([[Concepts/performance-midi-vs-notation]]).
- **Instrument splitting:** explicitly flagged by the author as a weak point.
- **Scope:** better suited to DAW/MIDI workflows than to producing a playable score; the author recommends Songscription or Klangio for notation.
- **Benchmarks:** vendor-run; the author cautions that accuracy depends on the use case and should be tested directly.

## Availability

- **Open source** — outputs usable commercially.
- **Hosted** — kobi.music workspace; a free account gets **30 credits a day**.
- **Demos** — Sousa, Swan Lake, Rachmaninoff, Mendelssohn and Buga Blue comparisons, with a downloadable public-domain MIDI sample.

## Related

- [[Concepts/pitch-lane-transcription-model]] — the architecture thesis behind the size
- [[Concepts/copyright-clean-training-data]] — the training corpus
- [[Research/audio-to-midi-transcription-2026]] — the synthesis

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Code: https://github.com/kobimusic/dettato
