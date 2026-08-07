---
title: "Wiki Housekeeping Plan — 2026-08-07"
detail: "Plan for normalizing Quartz frontmatter (drop detail, keep details), extending tags, creating a tag index, and creating the Workflows/ folder with a wiki-content-ingestion workflow."
details: "Comprehensive housekeeping plan for the Quartz wiki. Six phases: (1) create Workflows/ folder + tag index + first workflow, (2) frontmatter normalization (drop detail, fix entitie typo, fix missing frontmatter), (3) tag extension across 263 single-tag files via three parallel sub-agents scoped per tier, (4) build & verify, (5) PR chore/housekeeping-2026-08-07 → publish, (6) update memory and patch the jin wiki-content-ingestion skill. Each task has a state field (open / in progress / done) that is updated before every commit. The plan lives at the repo root by operator direction (outside content/)."
tags:
  - housekeeping
  - wiki
  - plan
created: 2026-08-07
updated: 2026-08-07
type: plan
branch: chore/housekeeping-2026-08-07
base-branch: publish
---

# Wiki Housekeeping Plan — 2026-08-07

**Branch:** `chore/housekeeping-2026-08-07`
**Base:** `publish` (currently at 83ce3e4)
**Merge strategy:** open PR for operator review when done
**Commit cadence:** one commit per state transition (`open` → `in progress` → `done`), pushed after every commit
**This document's location:** repo root, **outside** `content/` (operator direction)

---

## Operator's Requirements (verbatim)

1. Drop `detail:`, keep `details:` only. **Rule (operator directive 2026-08-07):** keep the more-informative of the two, harmonize under `details:`.
2. Extend the tag list for under-tagged files. 1–2 additional **categorical** tags beyond the primary tier tag. Don't over-do it.
3. **No product-name tags** (no `qwen` on a Qwen3.5 article, no `claude-code` on a Claude Code article). Use **topical/category** tags (`llm`, `agent`, `tooling`, etc.) instead.
4. **Tag index** at `content/tags.md` (operator directive 2026-08-07; operator wrote `Content/tags.md` — directory is `content/` lowercase per repo convention; on a case-sensitive filesystem this matters; on Linux it resolves the same). The tag index lists all tags with descriptions. New tags must be checked against this page before being invented.
5. **Reference the tag index from `content/index.md`** (operator directive 2026-08-07).
6. Tag index must be **kept up to date** during housekeeping.
7. New `Workflows/` folder with `index.md` describing its purpose: store repeatable workflows for agents.
8. Inside `Workflows/`, document the **wiki content schema, ingestion process, and its rules** — basically the wiki-content-ingestion skill, but **more concise** and **stripped of the gallery instructions**.
9. Each workflow follows the **skill format**: subfolder named after the workflow, `references/` and `scripts/` subfolders where needed, sensible frontmatter (no `detail`, just `details`).
10. Workflow file is **named after the actual workflow**, NOT `SKILL.md`.

---

## Audit Snapshot

276 .md files across 9 folders. Concrete numbers (from a fresh audit on 2026-08-07):

| Tier | Files | Issues |
|------|-------|--------|
| Raw | 14 | 2 missing frontmatter entirely (`agentos-sdk-dev-docs-2026-07-19.md`, `arxiv-zero-mem-2026-08-05.md`) |
| Concepts | 103 | Largest tier; majority single-tag |
| Entities | 98 | **53 files have `type: entitie` typo**, 47 have `type: entity` |
| Research | 28 | 3 well-tagged exemplars (`kaese-import-nach-schweiz` = 9 tags, `erbschaftssteuer-und-hypothek-zuerich` = 6, `aufbewahrungskorb-30x30-alternativen` = 7) |
| Papers | 2 | |
| Ideas | 1 | |
| Projects | 2 | one is subdirectory `example-project/` |
| Resources | 1 | |

**Tag distribution:** 263 files (95%) have exactly 1 tag, 10 have 0 tags, 3 are well-tagged (the Swiss/lifestyle exemplars).

**`type:` variants in the wild:** `concept` (77), `entitie` (53, typo), `entity` (47), `note` (19), `raw` (14), `research` (28), `content` (2), `article` (2), `project` (1), `index` (1), `idea` (1), `Resource` (1), `Opaque` (1), `"concept"` quoted (2).

**Detail vs Details:** every file has both fields. In the vast majority the two are near-duplicates; the migration rule is "keep the more-informative, harmonize under `details:`".

**Stray tags in the wild:** ~30+ `tags:` lines polluted by content from other YAML fields (e.g. `runbook-search:`, `incident-postmortem:`, `arXiv: 2605.17991`, `agentOS automatically injects...`). Mostly in `Raw/` files. Will be filtered out as part of the rewrite.

---

## The Plan (with per-task state)

State values: `open` → `in progress` → `done`. State is updated **immediately before** each commit.

### Phase 0 — Pre-flight

- [x] **T0.1** Plan authored and operator-approved. **state: done** (commit on chore/housekeeping-2026-08-07, 2026-08-07).
- [x] **T0.2** Migration strategy confirmed: keep more-informative, harmonize under `details:`. **state: done** (operator directive 2026-08-07).
- [x] **T0.3** Spot-check 10 random files to confirm `detail:` and `details:` are near-duplicates (the migration is safe). If any file has substantively different content in the two fields, escalate to operator before bulk delete. **state: done** (2026-08-07).

**Spot-check finding (247 files with both fields):**
- 71 files: `detail:` and `details:` are byte-identical → drop `detail:` is safe
- 175 files: `details:` is longer than `detail:` → keep `details:` (operator's "more-informative" rule); drop `detail:`
- **1 anomaly: `Entities/kernelbench.md`** — `detail:` is 13 chars longer and contains the citation, task count, and metric definition that `details:` lacks. **Per-file exception:** copy `detail:` text into `details:` first, then drop `detail:`.

**Bulk migration procedure (T2.1):**
1. For each file, compute `len(detail)` and `len(details)`.
2. If `len(detail) <= len(details)`: drop the `detail:` line (the 246 safe files).
3. If `len(detail) > len(details)`: copy `detail:` content into `details:` first, then drop the `detail:` line (the 1 kernelbench exception).
4. After the bulk pass, `grep -c "^detail:" content/**/*.md` must return 0.
- [x] **T0.4** Build the proposed tag vocabulary (~30–40 tags) as a Yaml list — the seed of the Tag Index. **state: done** (2026-08-07; vocabulary now lives in `content/tags.md`).
- [x] **T0.5** Open the `chore/housekeeping-2026-08-07` branch from `publish`. **state: done** (commit 759a721, 2026-08-07).
- [x] **T0.6** First workflow scope: both `wiki-content-ingestion` AND `wiki-catalog-research` (operator directive 2026-08-07), each in its own subfolder under `Workflows/`. **state: done** (operator directive 2026-08-07).

### Phase 1 — Create `Workflows/`, Tag Index, first workflow

- [x] **T1.1** Create `content/Workflows/` folder. **state: done** (2026-08-07).
- [x] **T1.2** Create `content/Workflows/index.md` describing the purpose of the folder (store repeatable workflows for agents). **state: done** (2026-08-07).
- [x] **T1.3** Create the **Tag Index** at `content/tags.md` (operator directive 2026-08-07; lowercase `content/` per repo convention). Pre-populated with the operator's existing good tags (from the kaese/erbschaft/aufbewahrung exemplars) + a starter vocabulary for the LLM/agent tier files. Each tag: name, scope description, when to use, when NOT to use. **state: done** (2026-08-07).
- [x] **T1.4** Update `Base.base` `formula.section` to include `Workflows` so it shows up in base views. Also added Papers and Resources which were missing. **state: done** (2026-08-07).
- [x] **T1.5** Add the tag-index backlink to `content/index.md` so the home page points to `[[tags|Tag Index]]` (operator directive 2026-08-07). **state: done** (2026-08-07; also added [[Workflows/|Workflows]] to the section list).
- [x] **T1.6** Create the first workflow subfolder: `content/Workflows/wiki-content-ingestion/`. **state: done** (2026-08-07).
- [x] **T1.7** Create the workflow file `content/Workflows/wiki-content-ingestion/wiki-content-ingestion.md` (named after the workflow, NOT `SKILL.md`). Frontmatter uses only `details:` (no `detail:`). **state: done** (2026-08-07).
- [x] **T1.8** Create `content/Workflows/wiki-content-ingestion/references/` with 2–3 trimmed reference docs (frontmatter-rules, build-verification, mermaid-pitfalls). **state: done** (2026-08-07; only `mermaid-pitfalls.md` is relevant — other jin references are inline in the workflow or skill-side only).
- [x] **T1.9** Create `content/Workflows/wiki-content-ingestion/scripts/` with the `quote-frontmatter.py` and `audit-garden.py` tools. **state: done** (2026-08-07; both copied from jin, with a `notes.md` in each subfolder explaining the trim and the known audit-garden issue).
- [x] **T1.10** Run `npx quartz build` to verify Phase 1 (after the first workflow). **state: done** (2026-08-07; 284 input files, 0 errors, 1050 emitted; the wiki-content-ingestion workflow renders at `public/workflows/wiki-content-ingestion/index.html` — 51 KB).
- [x] **T1.11** Create the second workflow subfolder: `content/Workflows/wiki-catalog-research/`. **state: done** (2026-08-07).
- [x] **T1.12** Create the workflow file `content/Workflows/wiki-catalog-research/wiki-catalog-research.md` (named after the workflow, NOT `SKILL.md`). Frontmatter uses only `details:`. **state: done** (2026-08-07; source is `~/.hermes/skills/wiki-catalog-research/SKILL.md` — note this skill lives in Hermes skills, not jin skills).
- [x] **T1.13** Create `content/Workflows/wiki-catalog-research/references/` with trimmed reference docs (catalog-pattern-reference, build-verification — only those that apply here). **state: done** (2026-08-07; only the worked example is relevant — other pitfalls are inlined in the workflow).
- [x] **T1.14** Create `content/Workflows/wiki-catalog-research/scripts/` if the source skill has any (e.g. catalog-update helpers). If none, omit the folder. **state: done** (2026-08-07; the source skill has no scripts — the workflow is procedural only. Folder omitted. Note added to the workflow's references/notes.md to document this.)
- [x] **T1.15** Final `npx quartz build` to verify the full Phase 1 (both workflows). **state: done** (2026-08-07; 287 input files, 0 errors, 1063 emitted. All four new pages render: workflows/index (26 KB), workflows/wiki-content-ingestion/index (51 KB), workflows/wiki-catalog-research/index (58 KB), tags (96 KB)). **Phase 1 complete.**

### Phase 2 — Frontmatter normalization

- [x] **T2.1** Bulk migration: for every file, drop the `detail:` line; keep the more-informative text in `details:`. Use the per-file procedure documented at T0.3 (drop if `detail` is shorter; copy `detail` into `details` first if `detail` is longer — applies to `Entities/kernelbench.md` only). Defensive read first per skill's `patch` pitfall warning. **state: done** (2026-08-07; 254 files changed — 249 dropped detail, 1 kernelbench exception handled, 4 detail-only files had their content copied into details). Build clean: 287 input files, 0 errors, 1063 emitted.)
- [ ] **T2.2** Fix the `type: entitie` typo (53 files in `Entities/`). Single `sed -i 's/^type: entitie$/type: entity/'` pass. **state: open**.
- [ ] **T2.3** Un-quote `type: "concept"` (2 files) → `type: concept`. **state: open**.
- [ ] **T2.4** Add minimal frontmatter to the 2 files currently missing it (`Raw/agentos-sdk-dev-docs-2026-07-19.md`, `Raw/arxiv-zero-mem-2026-08-05.md`). Defensive read of first 20 lines first. **state: open**.
- [ ] **T2.5** Run `npx quartz build` to verify Phase 2. **state: open**.

### Phase 3 — Tag extension

- [ ] **T3.1** Build the proposed tag vocabulary and surface it to the operator. Wait for sign-off. **state: open**.
- [ ] **T3.2** Spawn 3 parallel sub-agents (one per tier: Raw, Concepts, Entities) to propose 1–2 topical tags for each single-tag file. Sub-agents return only `(file, new_tags)` pairs — no file rewrites. **state: open**.
- [ ] **T3.3** Aggregate sub-agent proposals; spot-check 20 files; if quality is poor, refine instructions and re-run. **state: open**.
- [ ] **T3.4** Apply tag additions via `patch` (singular edits, auditable). **state: open**.
- [ ] **T3.5** Update the Tag Index with any new tags introduced by the sub-agents. **state: open**.
- [ ] **T3.6** Run `npx quartz build` to verify Phase 3. **state: open**.

### Phase 4 — Build & final verify

- [ ] **T4.1** Final `npx quartz build`. Must complete 0 errors. **state: open**.
- [ ] **T4.2** `git status --short` — only files I intended to add or modify. **state: open**.
- [ ] **T4.3** Verify the Tag Index is reachable (`public/concepts/tag-index.html` exists, > 5 KB). **state: open**.
- [ ] **T4.4** Verify the Workflows folder is reachable (`public/workflows/` exists, `wiki-content-ingestion.md` is there). **state: open**.
- [ ] **T4.5** Verify the 4-tier protocol is still intact in cross-links (no broken `[[Concepts/...]]` references). **state: open**.

### Phase 5 — PR to publish

- [ ] **T5.1** Open a PR from `chore/housekeeping-2026-08-07` → `publish` for operator review. **state: open**.

### Phase 6 — Update memory + jin skill

- [ ] **T6.1** Patch the `wiki-content-ingestion` skill in jin to remove the gallery instructions and the `detail` field from the "Required Frontmatter Keys" list. **state: open**.
- [ ] **T6.2** Update Hermes memory: "Quartz frontmatter uses `details:` (singular) only. `type:` enum is `raw|concept|entity|research|note|...` (no `entitie` typo). Tag index lives at `Concepts/tag-index`. New tags must be checked there first." **state: open**.

---

## What I Will NOT Do (out of scope)

- Won't touch the actual body content of the wiki pages. Only frontmatter and tag-list changes.
- Won't migrate `type: note` files to `type: concept` — `note` is a legitimate type for ad-hoc notes (19 files).
- Won't touch the well-tagged 3 files (kaese, erbschaft, aufbewahrung) unless they have the `entitie` typo (they don't).
- Won't add tags to files that already have multiple tags (they're the exemplars).
- Won't rename folders (`Ideas`, `Projects`, etc.).
- Won't add new folders beyond `Workflows/`.
- Won't reorganize the existing well-tagged research notes.
- Won't migrate the `wiki-content-ingestion` skill in jin until Phase 6 (T6.1) — jin skill stays as-is during the work, gets patched at the end.

---

## Verification

After every commit:
```bash
cd ~/quartz && npx quartz build 2>&1 | tail -10
# Expect: 0 errors, file count delta matches expectations

cd ~/quartz && git status --short
# Expect: ONLY files I intended to add or modify

cd ~/quartz && git diff --stat HEAD~1
# Expect: scope matches the phase
```

After Phase 2:
```bash
cd ~/quartz && grep -c "^detail:" content/**/*.md
# Should be 0
```

After Phase 2:
```bash
cd ~/quartz && grep -c "type: entitie" content/**/*.md
# Should be 0
```

After Phase 3:
```bash
cd ~/quartz && for f in content/**/*.md; do
  count=$(awk '/^tags:/{flag=1;next}flag && /^[[:space:]]*- /{count++;next}flag && /^[[:alnum:]]/{flag=0}END{print count+0}' "$f")
  [ "$count" -le 1 ] && echo "still single-tag: $f"
done | wc -l
# Should be small (only the 3 well-tagged exemplars + a few Research/ notes that already had multiple)
```

---

## Proposed Tag Vocabulary (for T3.1)

Controlled vocabulary, 30–40 tags. The 3 well-tagged exemplars use lifestyle/geography/topic tags; the LLM tier needs the same treatment but currently has none.

| Domain | Tags |
|--------|------|
| **LLM / ML** | `llm`, `quantization`, `inference`, `local-llm`, `rag`, `embedding`, `fine-tuning`, `training`, `benchmark`, `evaluation` |
| **Agent** | `agent`, `agentic-system`, `mcp`, `tooling`, `orchestration`, `multi-agent`, `memory`, `context-engineering`, `prompt-engineering`, `harness` |
| **Code / Dev** | `coding-agent`, `runtime`, `cli`, `sdk`, `kernel`, `kubernetes`, `serverless`, `infrastructure` |
| **Knowledge / Wiki** | `wiki`, `protocol`, `schema`, `ingestion`, `knowledge-management` |
| **Format / Type** | `tutorial`, `reference`, `guide`, `comparison`, `index`, `survey`, `architecture-pattern` |
| **Source** | `blog-post`, `paper`, `documentation`, `github-readme`, `hn-discussion` |
| **Lifestyle** | `schweiz`, `niederlande`, `zürich`, `shopping`, `wohnen`, `kinderzimmer`, `aufbewahrung`, `deko`, `reise` |
| **Topic** | `recht`, `zoll`, `erbschaft`, `hypothek`, `mehrwertsteuer`, `lebensmittel`, `käse`, `einfuhr` |

**Per-tier tag strategy:**
- **Raw** (currently 1 tag = `raw`): add 1 source-format tag (`blog-post` / `paper` / `documentation` / `github-readme` / `hn-discussion`) + 1 topical tag from the LLM/Agent/Tooling domain.
- **Concepts** (currently 1 tag = `concepts`): add 1 topical tag (LLM, agent, code, etc.) + optionally 1 format tag (`architecture-pattern`, `guide`, `reference`).
- **Entities** (currently 1 tag = `entities`): add 1 topical tag (`llm`, `tooling`, `paper`, `framework`). **No product names** — Qwen3.5 articles get `llm`, not `qwen`.
- **Research** (currently 1 tag = `research`): add 2 topical tags (geography, topic, domain). Mirror the kaese/erbschaft style.

---

## Operator Sign-Off Needed

Before I start any of the work in Phase 1 onward, I need confirmation on:

1. **Plan location** ✓ (decided: repo root, outside `content/`)
2. **Branch model** ✓ (decided: `chore/housekeeping-2026-08-07` from `publish`, PR at the end)
3. **Commit granularity** ✓ (decided: per state transition, push after every commit)
4. **Tag vocabulary** — approved by operator 2026-08-07. Proceed with the 30–40-tag proposal at the bottom of the plan.
5. **Tag Index location** — `content/tags.md` (operator directive 2026-08-07; not `Concepts/` as originally proposed).
6. **Canonical `type:` enum** — `raw | concept | entity | research | paper | project | idea | note | index | resource | content` (drop `entitie` typo, drop `article`, drop `"concept"` quoted). Keep `Opaque` and `Resource` as-is? Anything to add?
7. **Workflows/ first migration** — `wiki-content-ingestion` AND `wiki-catalog-research`, each in its own subfolder (operator directive 2026-08-07; supersedes the single-workflow scope).
