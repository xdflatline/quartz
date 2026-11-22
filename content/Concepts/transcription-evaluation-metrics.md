---
title: "Transcription evaluation metrics (onset, frame, offset, composite)"
details: "How audio-to-MIDI systems are scored: F1 on note onsets, frame-level activity and note offsets, plus a drums-specific score, averaged into a composite. The composite is a mean over heterogeneous datasets, so identical scores can hide very different performance — Dettato scores 91.3 on Bach10 and 48.7 on RWC Genre — and frame F1 is systematically easier than offset F1."
tags:
  - concept
  - music
  - evaluation
  - benchmark
created: 2026-11-22
updated: 2026-11-22
type: concept
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# Transcription evaluation metrics (onset, frame, offset, composite)

**Category:** Evaluation
**Status:** De-facto AMT scoring scheme, as used in Dettato's release (2026-11)

## Overview

Automatic music transcription is scored with note-level F1 measures, each answering a different question:

- **Onset F1** — was a note detected at the right time and pitch?
- **Frame F1** — is the pitch active in the right frames? A tolerant, dense measure; partial credit for sustained notes.
- **Offset F1** — did the note end at the right time? The hardest of the three, because release timing is ambiguous and masked by reverb/decay.
- **Drums** — a separate percussive score, since drum transcription has no pitch dimension.
- **Composite** — the mean of the above.

## Reported scores

| System | Composite | Onsets | Frames | Offsets | Drums | Params |
|---|---|---|---|---|---|---|
| Dettato | 60.8 | 70.8 | 79.1 | 40.9 | 52.5 | 20M |
| Mirelo A2M v1.1 Pro | 56.1 | 67.1 | 75.7 | 40.1 | 41.4 | not published |
| MuScriptor | 47.4 | 57.0 | 71.2 | 31.4 | 30.1 | 1.3B |
| YourMT3+ | 45.7 | 58.2 | 63.9 | 30.5 | 30.0 | 46M |

Note the systematic ordering: frames score highest, offsets lowest. A composite of 60.8 is not "61% of notes correct" — it is a mean across measures with different difficulty.

## The dataset spread is the real result

| Set | Dettato | MuScriptor | YourMT3+ |
|---|---|---|---|
| Bach10 | 91.3 | 54.7 | 57.9 |
| Dagstuhl ChoirSet | 60.8 | 35.5 | 28.0 |
| PHENICX-Anechoic | 64.8 | 54.4 | 44.8 |
| RWC Popular | 54.0 | 44.3 | 36.1 |
| RWC Classical | 64.4 | 58.4 | 62.4 |
| RWC Genre | 48.7 | 42.6 | 35.6 |
| RWC Jazz | 55.7 | 52.0 | 47.1 |
| RWC Royalty-Free | 61.6 | 46.8 | 45.4 |
| Slakh2100 (synthetic) | 68.4 | 51.1 | not reported |

Reading rules:

1. **Compare within a dataset, not across.** Bach10 is small, clean, four-part counterpoint where note boundaries are unambiguous; RWC Genre is dense mixed popular music. The 42-point gap is the task, not the model.
2. **The composite is set-weighted.** The headline 60.8 is computed over PHENICX, RWC classical and RWC royalty-free — a classical-heavy mix. A pop- or jazz-heavy use case should look at those rows, where the margin narrows (RWC Classical: 64.4 vs 65.8, i.e. Dettato trails Mirelo).
3. **Offsets are where systems are still weak.** Even the best system here sits in the low 40s; downstream users who need clean note lengths should expect manual cleanup.
4. **Synthetic sets reward synthetic-trained models.** Slakh2100 is rendered from MIDI, so a model trained on rendered audio has an in-distribution advantage. Keep it out of the real-world argument.

## What the metrics do not measure

- **Instrument attribution.** A model can score well on frame F1 while merging two instruments into one part; Dettato's author flags instrument splitting as a known weakness.
- **Notation quality.** Engraving is a separate problem ([[Concepts/performance-midi-vs-notation]]).
- **Musical usability.** Whether a transcription is worth editing depends on the player, the arrangement and the genre.

## Related Concepts

- [[Concepts/pitch-lane-transcription-model]] — the formulation these scores evaluate
- [[Concepts/performance-midi-vs-notation]] — why high F1 is not a score
- [[Concepts/copyright-clean-training-data]] — the synthetic-data question behind the Slakh row
- [[Concepts/typed-decisions-benchmark-ollaya]] — another case where a composite hides per-domain variance

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Research: [[Research/audio-to-midi-transcription-2026]]
