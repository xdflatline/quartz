---
title: Nature
details: A collection of nature-themed images generated using ComfyUI.
created: 2026-06-20
updated: 2026-06-20
type: Gallery
tags:
  - genai
---

# Nature

## Flux2 Klein 00128

![Flux2 Klein 00128](assets/flux2-klein_00128_.png)

**Prompt:** A candid 35mm photograph of a lush alpine valley with pristine clear water in the foreground and towering pine trees. Natural daylight with soft lens softness at the periphery. Authentic film grain, subtle atmospheric haze.

---

## Alpine Valley

![Alpine Valley](assets/flux2_klein_4b_alpine_valley.png)

**Prompt:** A candid, street-level 35mm film photograph of a flooded city street. Abandoned rusted cars are half-submerged in water, with moss and vines creeping over the metal. Low contrast, flat daylight, authentic film grain, high detail, optical lens falloff.

---

## Dawn Mist Forest

![Dawn Mist Forest](assets/flux2_klein_4b_dawn_mist_forest.png)

**Prompt:** hyper-realistic raw dense ancient pine forest at twilight, dappled moonlight through mist, authentic film grain, high detail, optical lens falloff, raw tactile texture

---

## Golden Hour Desert

![Golden Hour Desert](assets/flux2_klein_4b_golden_hour_desert.png)

**Prompt:** hyper-realistic raw desolate jagged arctic glacier landscape, blue ice textures, sharp morning light, authentic film grain, high detail, raw tactile texture

---

## Large Format Glacier

![Large Format Glacier](assets/flux2_klein_4b_large_format_glacier.png)

**Prompt:** hyper-realistic raw sun-drenched coastal cliff overlooking a stormy ocean, salty mist, dramatic lighting, authentic film grain, high detail, raw tactile texture

---

## Macro Dew Web

![Macro Dew Web](assets/flux2_klein_4b_macro_dew_web.png)

**Prompt:** hyper-realistic raw street level view of a bustling futuristic Tokyo market, rain-slicked neon streets with people walking on sidewalks and cars driving on the street, cinematic cyberpunk, authentic film grain, high detail, optical lens falloff, raw tactile texture

---

## Medium Format Wetlands

![Medium Format Wetlands](assets/flux2_klein_4b_medium_format_wetlands.png)

**Prompt:** hyper-realistic raw street level view of a bustling futuristic Tokyo market, rain-slicked neon streets, cinematic cyberpunk, authentic film grain, high detail, optical lens falloff, raw tactile texture

---

## Night Starry Mountains

![Night Starry Mountains](assets/flux2_klein_4b_night_starry_mountains.png)

**Prompt:** hyper-realistic raw medieval European village square at dawn, stone architecture, market stalls opening, soft natural morning light, authentic film grain, high detail, raw tactile texture

---

## Stormy Coast

![Stormy Coast](assets/flux2_klein_4b_stormy_coast.png)

**Prompt:** hyper-realistic raw abandoned desert city, weathered brutalist concrete structures, shifting sands, harsh midday sun, authentic film grain, high detail, raw tactile texture

---

## Ultrawide Volcanic Vent

![Ultrawide Volcanic Vent](assets/flux2_klein_4b_ultrawide_volcanic_vent.png)

**Prompt:** hyper-realistic raw modern glass and steel skyscraper interior looking out over a sprawling coastal metropolis at dusk, warm interior lighting, authentic film grain, high detail, raw tactile texture

---

## Fall 00001

![Fall 00001](assets/flux_klein_fall_00001_.png)

**Prompt:** A candid 35mm photograph of an alpine watermill at autumn, gold and red forest canopy, moody overcast sky, fallen leaves around the mill. Authentic fine film grain, cool color temperature.

---

## Img2Img 00001

![Img2Img 00001](assets/flux_klein_img2img_00001_.png)

**Prompt:** A candid 35mm photograph of an alpine watermill in a serene landscape. Base reference image used for seasonal variations. Natural light, film grain.

---

## Spring 00001

![Spring 00001](assets/flux_klein_spring_00001_.png)

**Prompt:** A candid 35mm photograph of an alpine watermill at spring, fresh green meadow with blooming wildflowers in the foreground. Soft natural daylight, pristine clear stream, subtle atmospheric haze, film grain.

---

## Summer 00001

![Summer 00001](assets/flux_klein_summer_00001_.png)

**Prompt:** A candid 35mm photograph of an alpine watermill at summer, vibrant lush greenery, high mountain sun with dramatic shadows, clear blue sky. Authentic film grain, crisp details.

---

## Winter 00001

![Winter 00001](assets/flux_klein_winter_00001_.png)

**Prompt:** A candid 35mm photograph of an alpine watermill in winter, heavy snow cover on roofs and surrounding pines, soft diffused winter light. Authentic film grain, subtle blue-tinted shadows.

---

## Technical Configuration

- **Workflow File:** `api/Flux.2Klein4B_T2I.json`
- **Model (UNET):** `flux-2-klein-4b.safetensors`
- **Model (CLIP):** `qwen_3_4b.safetensors` (Flux 2 type)
- **Model (VAE):** `flux2-vae.safetensors`
- **Architecture:** Flux.2 Klein 4B distilled
- **Sampler:** `euler`
- **Scheduler:** `Flux2Scheduler`
- **Steps:** 4 (fixed)
- **Resolution:** 1920×1080 (4B variant) or 1024×1024 (9B variant)
- **CFG Scale:** 1
- **Prompt Injection:** Node `76` (PrimitiveStringMultiline)
- **Tokyo Method:** Applied via photographic prompts focusing on 35mm candid composition, lens softness, and authentic film grain constraints.
