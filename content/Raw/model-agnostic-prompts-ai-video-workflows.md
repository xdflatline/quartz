---
title: "Raw: Designing Model-Agnostic Prompts for AI Video Workflows"

details: "Raw capture of the dev.to article by @jiaoshuo1997. The author argues that a prompt which works in one model may misbehave in another, and that model-specific syntax becomes obsolete after each model update. The durable alternative is a stable intermediate representation (IR) that is then translated per-model at render time. Captured 2026-07-23 from https://dev.to/jiaoshuo1997/designing-model-agnostic-prompts-for-ai-video-workflows-52hm. Original publication language: English. This Raw file is the unedited source; the synthesized knowhow lives at Research/model-agnostic-prompts-ai-video-workflows.md."
tags:
  - raw
created: 2026-07-23
updated: 2026-07-23
type: raw
source:
  title: "Designing Model-Agnostic Prompts for AI Video Workflows"
  author: "@jiaoshuo1997"
  url: "https://dev.to/jiaoshuo1997/designing-model-agnostic-prompts-for-ai-video-workflows-52hm"
  publisher: "DEV Community"
  captured: 2026-07-23
---

# Designing Model-Agnostic Prompts for AI Video Workflows

> A prompt that works well in one model may behave differently in another, and model-specific syntax can become obsolete after an update. A more durable approach is to represent the creative intent first, then translate that representation into the vocabulary of a chosen generator.

**Central Principle.** Treat prompts as **compiled output**, not as the source of truth. A stable intermediate representation makes an AI video workflow easier to test, debug, and migrate when models change.

## 1. Start with an Intermediate Representation

Instead of sending long natural-language paragraphs directly to a model, store each shot as structured fields:

```json
{
  "duration": 5,
  "aspect_ratio": "9:16",
  "subject": "a cyclist wearing a yellow rain jacket",
  "environment": "wet city street at dusk",
  "composition": "medium tracking shot, subject in right third",
  "camera": "truck left at cycling speed, stable horizon",
  "action": "cyclist passes two parked cars and looks over shoulder",
  "lighting": "cool ambient light with warm shop reflections",
  "end_state": "cyclist exits frame left"
}
```

**Practical Advantages:**

- Missing information is visible
- Fields can be validated independently
- One shot can be rendered for multiple models
- Revisions can target a single layer
- Duration and aspect-ratio constraints stay explicit

## 2. Separate Invariants from Preferences

Not every detail has equal importance. Divide the representation into two groups:

- **Invariants.** Requirements that survive every model translation (subject, action order, camera direction, duration, final state).
- **Preferences.** Desirable but negotiable details (film grain, color mood, shallow depth of field, minor background props).

**Priority Levels:**

```
P0: action order, camera direction, end state
P1: framing, environment, lighting
P2: texture, secondary props, stylistic accents
```

> When generation fails, preserve invariants first. A visually beautiful result is still wrong if the subject moves in the opposite direction or never completes the required action.

## 3. Use a Two-Stage Renderer

A model adapter transforms the intermediate representation in two distinct stages:

| Stage | Purpose | Contents |
|-------|---------|----------|
| **Stage 1** | Build the visual state | Opening frame: subject, wardrobe, environment, framing, lens cues, lighting, spatial relationships. Should be possible to sketch the first frame from this section alone. |
| **Stage 2** | Build the temporal change | Motion: what the subject does, how the camera moves, when events occur, what the final frame contains. |

**Debugging benefit.** If the first frame is wrong, revise Stage 1. If the action stalls or the camera drifts, revise Stage 2.

## 4. Translate, Do Not Copy

Each model adapter should map the same fields into the model's preferred style. Adapter responsibilities include:

- Ordering fields by importance
- Converting durations into supported values
- Translating camera vocabulary
- Omitting unsupported controls
- Adding only constraints the target model understands

The **source representation remains unchanged**, preventing model quirks from leaking into the analysis layer.

## 5. Validate Before Generation

A lightweight validator catches expensive errors:

```
- duration is supported by the target model
- aspect ratio is valid
- subject and action are present
- camera instruction has direction or lock behavior
- action has an observable end state
- timing beats do not exceed total duration
```

**For reference-video workflows.** Compare every field against the source. Do not invent wardrobe, dialogue, or camera movement just to make the description sound richer.

## 6. Measure Structural Fidelity

> Pixel similarity is a poor measure for generative video.

Evaluate **structure** instead:

- Was the shot type preserved?
- Did the action occur in the correct order?
- Did the camera move in the intended direction?
- Was the final state reached?
- Did subject identity and wardrobe remain consistent?
- Was the pacing close to the reference?

These checks create useful revision signals:

- Wrong camera direction → change the camera layer
- Incomplete action → simplify the action or allocate more time
- Identity drifts → strengthen visual-state constraints

## 7. Keep the Workflow Auditable

Store these artifacts together to produce an audit trail and make successful prompts reusable:

- Intermediate representation
- Rendered prompt
- Target model
- Generation settings
- Revision notes

**Full Pipeline:**

```
source segment -> structured shot -> model adapter -> rendered prompt
-> generation result -> evaluation -> revision
```
