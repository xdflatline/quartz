---
title: "Performance MIDI vs notation (what a transcription model actually outputs)"
details: "Audio-to-MIDI models emit performance MIDI: note events with timing, pitch and velocity, aligned to a beat. That is not sheet music — engraving requires quantization, enharmonic spelling, voice separation, beaming, instrument assignment and layout. Treating the two deliverables as the same thing is the most common misreading of transcription benchmarks, and vendors recommend dedicated notation tools when a playable score is the goal."
tags:
  - concept
  - music
  - tooling
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# Performance MIDI vs notation (what a transcription model actually outputs)

**Category:** Output Semantics / Tooling Boundary
**Status:** Design boundary stated by Dettato's author (2026-11)

## Overview

An audio-to-MIDI model does not produce sheet music. It produces **performance MIDI**: a stream of note events with onset time, pitch, duration and velocity, optionally aligned to a detected beat. Everything a musician reads from a score — staff placement, key signature, enharmonic spelling, stem direction, beaming, dynamics marks, instrument labels, page layout — is outside that artifact.

Dettato's author is explicit: "this just spits out performance MIDI with a beat aligned. If you're looking for something that you can actually play (e.g sheet music), I'd recommend songscription or klangio."

## The gap

| Layer | Performance MIDI | Notation |
|---|---|---|
| Pitch | MIDI note number | Staff position + clef + key, respelled per harmonic context |
| Time | Seconds / ticks, expressive microtiming | Quantized durations, tuplets, ties, bar lines |
| Duration | Note-on to note-off | Note value + articulation marks |
| Polyphony | Flat event set | Voices, chords, stems, cross-staff beaming |
| Instrumentation | Program change at best | Named parts, transposing instruments, divisi |
| Presentation | None | Layout, systems, page turns |

The hard part of notation is not detecting notes; it is **deciding how to write them**. A perfectly detected C-sharp may need to be written as D-flat, and a rubato performance must be quantized into a rhythm that is readable rather than literal.

## Practical consequences

- **Choose the tool by deliverable.** DAW editing, MIDI cleanup, analysis and re-performance → performance MIDI. Publishing, teaching, arranging for live players → notation tool.
- **Do not grade a transcription model on readability.** Frame, onset and offset F1 say nothing about engraving quality.
- **Expect instrument-splitting weaknesses to surface here.** A model that merges instruments produces a performance MIDI file that a notation tool will then render as an implausible part.
- **Beat alignment is a partial bridge, not notation.** Aligning to a beat grid makes the MIDI easier to import into a DAW; it does not produce bar-accurate rhythm.

## Why vendors point elsewhere

Recommending adjacent notation products is a credibility signal, not a concession: it separates the model's claim (accurate note events) from the user's goal (a score), which prevents the benchmark from being read as a promise it cannot keep. See [[Concepts/transcription-evaluation-metrics]] for what the numbers do measure.

## Related Concepts

- [[Concepts/pitch-lane-transcription-model]] — the model that produces this artifact
- [[Concepts/transcription-evaluation-metrics]] — the metrics that describe note events, not scores
- [[Concepts/copyright-clean-training-data]] — the corpus behind the model

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Songscription: https://www.songscription.ai/
- Klangio: https://klang.io/
- Research: [[Research/audio-to-midi-transcription-2026]]
