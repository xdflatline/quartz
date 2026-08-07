---
title: "Model-Agnostic Prompts for AI Video Workflows"

details: "Research index synthesizing the methodology from @jiaoshuo1997 on dev.to (captured 2026-07-23, source: Raw/model-agnostic-prompts-ai-video-workflows.md). Seven-part framework: (1) IR with explicit duration/aspect/subject/environment/composition/camera/action/lighting/end_state fields, (2) invariants vs preferences split with P0/P1/P2 priority levels, (3) two-stage renderer (visual state then temporal change), (4) per-model adapter that translates rather than copies, (5) pre-render validator for duration/aspect/required fields/camera direction/end state/timing, (6) structural fidelity evaluation in place of pixel similarity, (7) auditable artifact bundle per generation. Applies to: ComfyUI video backends (Wan 2.1, Hunyuan, CogVideoX, LTX-Video), OpenMontage pipelines with VIDEO_GEN_LOCAL_MODEL slots, and any agentic video orchestration where model versions are expected to churn. Tension with OpenMontage's existing tool design: each BaseTool currently targets one backend with backend-specific prompt construction — an adapter layer above BaseTool would generalize across all four local backends and any cloud model."
tags:
  - research
created: 2026-07-23
updated: 2026-07-23
type: research
sources:
  - Raw/model-agnostic-prompts-ai-video-workflows.md
---

# Model-Agnostic Prompts for AI Video Workflows

**Updated:** 2026-07-23
**Source:** @jiaoshuo1997, "Designing Model-Agnostic Prompts for AI Video Workflows" (dev.to, 2026) — see `Raw/model-agnostic-prompts-ai-video-workflows.md`

---

## 1. Core Thesis

A prompt that works in one model may misbehave in another, and model-specific syntax becomes obsolete after each model update. The durable alternative is to **treat prompts as compiled output, not as the source of truth**: a stable intermediate representation (IR) describes each shot as structured fields, and a thin per-model adapter translates that IR into the vocabulary of whichever generator is currently selected. When the model changes, only the adapter changes; the analysis, validation, and revision layers above it stay intact.

This is a compile/architecture pattern borrowed from software engineering: the IR is the source, the prompt is the build artifact, and the adapter is the target-specific backend.

## 2. The Shot Intermediate Representation

Each shot is a JSON object with explicit, separately validatable fields. The reference schema from the source article:

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

**Why structured fields beat a prose prompt:**

- Missing information is visible at a glance.
- Each field can be validated independently against a model-specific schema.
- The same IR renders cleanly to multiple backends without re-authoring.
- Revisions target a single layer (e.g., the camera instruction) without rewriting the whole prompt.
- Hard constraints (duration, aspect ratio) stay explicit and cannot be silently dropped.

The eight fields are not arbitrary. `subject` and `action` carry the narrative; `environment`, `composition`, `lighting` carry the visual state; `camera` and `end_state` carry the temporal contract. Duration and aspect ratio are structural and must round-trip cleanly through every adapter.

## 3. Invariants vs Preferences

Not every field has equal weight. The methodology splits the IR into two tiers:

- **Invariants** must survive every model translation unchanged. They are the contract the output is graded against: subject identity, action order, camera direction, duration, final state.
- **Preferences** are desirable but negotiable. They are the first to be dropped or approximated when a target model lacks the control: film grain, color mood, depth of field, minor background props.

A three-level priority scheme is suggested:

| Priority | Fields | Compromise policy |
|----------|--------|-------------------|
| **P0** | action order, camera direction, end state | Never compromise. A wrong direction or a missing end state is a generation failure, not a stylistic deviation. |
| **P1** | framing, environment, lighting | Approximate if the model cannot express the control natively (e.g., "cool ambient" rendered as "low color temperature 4500K"). |
| **P2** | texture, secondary props, stylistic accents | First to drop on a model that struggles with prompt length. |

> "When generation fails, preserve invariants first. A visually beautiful result is still wrong if the subject moves in the opposite direction or never completes the required action."

This is the same idea as a graceful-degradation policy in software: keep the load-bearing parts working, let the cosmetic parts fail silently.

## 4. The Two-Stage Renderer

Every model adapter renders the IR in two distinct stages. The split is the most operationally useful pattern in the article because it isolates two classes of failure:

| Stage | Builds | Fields it consumes | Failure mode it explains |
|-------|--------|-------------------|--------------------------|
| **Stage 1** | The visual state — the first frame | subject, wardrobe, environment, framing, lens cues, lighting, spatial relationships | "The first frame looks wrong" |
| **Stage 2** | The temporal change — motion across the duration | action, camera, timing beats, final frame | "The action stalls" / "the camera drifts" / "the end state is not reached" |

The author requires that **Stage 1 alone must be sufficient to sketch the opening frame**. If a human cannot draw the first frame from the Stage 1 fields, the IR is under-specified. This is a powerful test: it converts an opaque visual output into a check you can run on the IR before spending GPU time.

## 5. Translate, Do Not Copy

The adapter's job is to map the IR into the target model's preferred style, not to concatenate fields. Adapter responsibilities:

- Order fields by what the model attends to most strongly.
- Convert durations into the values the model actually supports (some accept only integer seconds, some accept ranges, some require explicit `num_frames`).
- Translate camera vocabulary ("truck left", "dolly in", "pan right") into the model's accepted phrasing or control tokens.
- Omit controls the model does not understand rather than passing them through and hoping for the best.
- Add only constraints the target model can actually enforce.

The IR itself must remain unchanged across adapters. If model quirks leak back into the IR, the next model migration will need to clean up the corpus before it can re-render — defeating the point of having a stable representation.

## 6. Pre-Render Validation

A lightweight validator runs before any GPU is touched. The minimum check set:

- `duration` is in the supported set for the target model.
- `aspect_ratio` is valid and supported.
- `subject` and `action` are non-empty.
- `camera` has an explicit direction or a lock behavior (e.g., "static").
- `action` has an observable `end_state`.
- The sum of timing beats does not exceed the total duration.

For **reference-video workflows** (e.g., reproducing a shot from existing footage), the article adds a stricter rule: every field must trace back to the source. The adapter must not invent wardrobe, dialogue, or camera movement just to make the description sound richer. The reference is the ground truth; the IR is a rephrasing of it, not an elaboration.

## 7. Structural Fidelity, Not Pixel Similarity

> "Pixel similarity is a poor measure for generative video."

The article replaces SSIM/PSNR-style metrics with a six-question structural checklist:

1. Was the shot type preserved?
2. Did the action occur in the correct order?
3. Did the camera move in the intended direction?
4. Was the final state reached?
5. Did subject identity and wardrobe remain consistent?
6. Was the pacing close to the reference?

Each question maps to a specific IR field and therefore a specific revision target:

| Failed check | Fix in IR |
|--------------|-----------|
| Wrong camera direction | Rewrite the `camera` field. |
| Incomplete action | Simplify the `action` field, or increase `duration`. |
| Identity drift | Strengthen the visual-state fields (`subject`, `wardrobe`, `environment`). |
| Wrong shot type | Rewrite `composition` and `lens` cues. |
| End state not reached | Add explicit timing beats to `action`; extend `duration` if needed. |

This converts "the output looks bad" — an unactionable complaint — into "change this field" — a targeted edit. It also produces a corpus of failed checks that can drive adapter improvements over time.

## 8. Auditable Artifact Bundle

Every generation produces and stores six artifacts together. Without this bundle, the workflow is not reproducible and successful prompts cannot be reused:

1. The IR (source of truth for the generation).
2. The rendered prompt (what was actually sent to the model).
3. The target model identifier and version.
4. The generation settings (seed, sampler, steps, CFG, LoRA stack).
5. The output media file.
6. Revision notes explaining any deviation from the IR or any post-hoc prompt edits.

The full pipeline as one expression:

```
source segment  ->  IR (shot)  ->  model adapter  ->  rendered prompt
              ->  generation result  ->  structural evaluation  ->  revision
```

Storing the entire chain makes it possible to answer "why did this shot work last week but not today?" — usually because the model version changed, and the bundle makes that change visible.

## 9. Application Notes

- **ComfyUI video backends** (Wan 2.1, Hunyuan, CogVideoX, LTX-Video): each has a different native prompt vocabulary and a different set of supported controls. The adapter pattern is the natural fit; the IR is the shared schema. A practical starter is to put per-backend prompt builders behind a single `render(ir, backend)` function and call it from any ComfyUI workflow generator.
- **OpenMontage pipelines**: the current `BaseTool` design targets one backend per tool (e.g., `WanVideoTool`, `HunyuanVideoTool`). An adapter layer above the tools would let a single pipeline manifest target any backend by changing the adapter, not the manifest. This is the cleanest path to making the four `VIDEO_GEN_LOCAL_MODEL` slots interchangeable.
- **Reference-video workflows** (reproducing a shot from existing footage): the strict-source rule in §6 is the most important guardrail. Without it, adapters will hallucinate plausible-but-wrong details and the evaluation will pass for the wrong reason.
- **Cloud vs local**: the IR is identical in both cases. The adapter is what differs. This is a feature, not a limitation — the same shot description can be rendered to a local Wan 2.1 instance and to a cloud model in the same pipeline.

## 10. Failure Modes the Methodology Exists to Prevent

| Failure | Root cause | What the IR/validator/evaluation prevents |
|---------|------------|-------------------------------------------|
| Model update silently breaks existing prompts | Prompts were written in model-specific syntax | IR is model-agnostic; only the adapter changes |
| Output looks beautiful but the action is reversed | Adapter honored preferences but not invariants | P0 invariants flagged by validator; structural check #2 catches it |
| Subject changes wardrobe between frames | Visual state not pinned in the prompt | Stage 1 fields (`subject`, `wardrobe`) are explicit; check #5 catches drift |
| Same prompt produces different results on rerun | No record of seed, sampler, or model version | Audit bundle stores generation settings |
| Team cannot reuse last week's successful prompt | Prompt was hand-edited away from the IR | IR + rendered-prompt pair stored together; revision notes document the diff |
