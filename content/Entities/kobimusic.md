---
title: "kobimusic"
details: "Independent music-ML project by the developer of Dettato (audio-to-MIDI) and an earlier optical-music-recognition model. Builds music tools intended to assist rather than replace musicians, publishes techniques such as 'soundfont babies', and trains models without copyrighted recordings."
tags:
  - entity
  - music
  - tooling
  - training
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/dettato-audio-to-midi-2026-11-16"
---

# kobimusic

**Category:** Independent music-ML project
**Site:** https://kobi.music/
**Status:** Active (2026)

## Overview

kobimusic builds music machine-learning tools. Its stated goal is "to help musicians, not replace them", which in practice shapes two choices visible across its work:

1. **Copyright compliance as a design constraint** — training data is assembled from synthetic and openly licensed sources rather than scraped recordings ([[Concepts/copyright-clean-training-data]]).
2. **Small, task-specific models over large general components** — Dettato is 20M parameters and reports beating a 1.3B open baseline ([[Concepts/pitch-lane-transcription-model]]).

## Projects

- **Dettato** (2026-11) — audio-to-MIDI transcription model, open source, 20M parameters ([[Entities/dettato]]).
- **Optical music recognition model** — the author's earlier model, referenced as the source of the "local reframing" insight applied to AMT.
- **Soundfont babies** — a published technique for generating new instrument timbres by morphing soundfonts; used to widen Dettato's training corpus.
- **kobi.music workspace** — hosted transcription service, free tier 30 credits/day.

## Notable positions

- **Architecture beats data** for structured prediction: the first ten months of Dettato treated transcription as a data problem and were scrapped; the reframing to a pitch-lane model is what produced the result.
- **Constraints drive innovation**: the no-copyright-data rule is framed as an advantage, not a handicap.
- **Benchmark honesty**: the release names its own weak points (instrument splitting, performance-MIDI-only output) and directs users to other vendors for notation.

## Related

- [[Entities/dettato]] — the model
- [[Research/audio-to-midi-transcription-2026]] — the synthesis of the release

## References

- Raw: [[Raw/dettato-audio-to-midi-2026-11-16]]
- Site: https://kobi.music/
- Soundfont babies: https://kobi.music/research/making-soundfont-babies
