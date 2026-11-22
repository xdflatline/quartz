---
title: "introducing dettato"
details: "kobimusic release post (2026-11-16) for Dettato, a 20M-parameter audio-to-MIDI transcription model that reports a 60.8 composite F1 against 56.1 for Mirelo's closed A2M v1.1 Pro and 47.4 for the 1.3B open MuScriptor, trained with no copyrighted recordings using synthetic instruments, CC solo instruments mixed via URMP, and roughly twenty soundfonts. Includes per-dataset results, the author's caveats about instrument splitting and performance-MIDI output, and the argument that transcription's bottleneck is architecture rather than data."
tags:
  - raw
  - music
  - llm
  - benchmark
  - training
created: 2026-11-22
updated: 2026-11-22
type: raw
source: "https://kobi.music/research/dettato"
---

# introducing dettato

**Source:** [kobi.music](https://kobi.music/research/dettato)
**Date Retrieved:** 2026-11-22
**Published:** 2026-11-16
**Author:** kobimusic
**Type:** Vendor research post (model release with benchmark results)

---

![A low-poly pink bird, drawn ten times in a loop, listening](https://kobi.music/media/dettato/title.svg)

we're introducing Dettato, a SOTA audio to MIDI transcription model that significantly beats MuScriptor 1.3B - the next best open model - and scores a bit higher than mirelo's closed source model 'Mirelo A2M v1.1 Pro' on their published benchmarks. all at just 20m parameters - roughly 65x smaller than muscriptor. Additionally, in training the model, we trained on absolutely no copyrighted recordings. the model is [open source](https://github.com/kobimusic/dettato) and you can use its outputs for commercial purposes.

## Benchmarks

| system | composite | onsets | frames | offsets | drums | parameters |
| --- | --- | --- | --- | --- | --- | --- |
| dettato | 60.8 | 70.8 | 79.1 | 40.9 | 52.5 | 20M |
| Mirelo A2M v1.1 Pro | 56.1 | 67.1 | 75.7 | 40.1 | 41.4 | not published |
| MuScriptor | 47.4 | 57.0 | 71.2 | 31.4 | 30.1 | 1.3B |
| YourMT3+ | 45.7 | 58.2 | 63.9 | 30.5 | 30.0 | 46M |

the composite, and the measures it is the mean of, for each system

sets used: PHENICX, RWC classical, RWC royalty-free

F1 per set: the mean of onset, frame and offset

## Per-set results

| set | dettato | mirelo A2M v1.1 pro | muscriptor 1.3B | yourmt3+ |
| --- | --- | --- | --- | --- |
| Bach10 | 91.3 | not reported | 54.7 | 57.9 |
| Dagstuhl ChoirSet | 60.8 | not reported | 35.5 | 28.0 |
| PHENICX-Anechoic | 64.8 | 60.9 | 54.4 | 44.8 |
| RWC Popular | 54.0 | not reported | 44.3 | 36.1 |
| RWC Classical | 64.4 | 65.8 | 58.4 | 62.4 |
| RWC Genre | 48.7 | not reported | 42.6 | 35.6 |
| RWC Jazz | 55.7 | not reported | 52.0 | 47.1 |
| RWC Royalty-Free | 61.6 | 56.2 | 46.8 | 45.4 |
| Slakh2100 (synthetic) | 68.4 | not reported | 51.1 | not reported |

F1 per set: the mean of onset, frame and offset

## Caveats

disclaimer with the benchmarks: it's difficult to gauge the true accuracy of the model for your use-case without trying it yourself. one thing my model performs poor on for instance, is splitting instruments correctly. In addition, this just spits out performance MIDI with a beat aligned. If you're looking for something that you can actually play(e.g sheet music), i'd reccommend [songscription](https://www.songscription.ai/) or [klangio](https://klang.io/) - both are excellent tools by great companies that push the envelope of what's possible in this field forward.

## Demos

the stars and stripes forever, swan lake, rachmaninoff, mendelssohn, buga blue — sample renderings with sections labelled intro, first strain, second strain, trio, breaks, strain, piccolo solo, break, strain again, grandioso; a recording/MIDI A/B player at 3:30.

sousa, the stars and stripes forever: "the president's own" united states marine band, from the complete marches of john philip sousa, vol. 3. a us government recording, public domain. [download the MIDI](https://kobi.music/media/dettato/samples/stars-and-stripes-forever.mid)

audio to midi needs an account. A free one gets 30 credits a day.

[make a free account](https://kobi.music/workspace/account?return=%2Fresearch%2Fdettato#sign-up) [sign in](https://kobi.music/workspace/account?return=%2Fresearch%2Fdettato)

## Training data and provenance

the driving goal of kobimusic: to help musicians, not replace them. a part of that goal means following copyright law. we trained dettato on a mix of synthetic instrument recordings and CC solo instruments mixed in using the URMP dataset. the rest of the instruments morph together ~20 soundfonts, using the ['soundfont babies'](https://kobi.music/research/making-soundfont-babies) technique i published. no copyrighted recordings were used.

## Design notes

I began working on dettato about 10 months ago, but scrapped what I had in about April. The reason why was that I treated AMT as a data problem - but in reality, the bottleneck is architecture. There are a lot of parellels that you can draw for OMR (first model i made) and AMT. both traditionally were tackled early on using algorithms. later, in both fields they plugged in giant LLM components. These models would naturally become overfit to synthetic data, since globally the problems of AMT and OMR become different than if you treat it locally. But, for both you can reframe it as a local problem. For OMR, using a detector model. For AMT, a pitch-lane model.

overall, i hope both open and closed weight music retrieval companies can learn from this. The constraint of not using copyrighted recordings doesn't hold you back, but actually encourages innovation, and it's likely you'll end up with a better model in the end.
