---
title: "Project: Quartz Digital Garden"
detail: Building a digital garden with Quartz static site generator
details: Building a digital garden with Quartz static site generator
tags:
  - projects
created: 2026-06-15
updated: 2026-06-17
type: project
project: Quartz Digital Garden
status: active
started: 2024-01-15
---
# Project: Quartz Digital Garden

## Objective
Create a public knowledge base using Quartz that mirrors Obsidian vault structure, with:
- Wikilinks support (`[[Note Name]]`)
- Graph visualization
- Full-text search
- GitHub Pages deployment
- Obsidian-flavored markdown (callouts, tasks, etc.)

## Progress Log
- **2024-01-15**: Initial setup complete — repo created, dependencies installed, config wizard run
- **2024-01-15**: GitHub Pages workflow created (`.github/workflows/deploy-pages.yaml`)
- **2024-01-15**: Base URL updated to `xdflatline.github.io/quartz`
- **2024-01-15**: Demo content created (this note, daily notes, concepts)

## Architecture Decisions

### Why Quartz?
- Native Obsidian compatibility (wikilinks, frontmatter, callouts)
- Fast builds with Vite
- Plugin ecosystem for extensibility
- SPA routing for snappy navigation
- Graph view for knowledge visualization

### Configuration Choices
| Setting | Value | Rationale |
|---------|-------|-----------|
| Template | `default` | Clean, minimal starting point |
| Link Resolution | `shortest` | Obsidian-style shortest-path links |
| Base URL | `xdflatline.github.io/quartz` | GitHub Pages subpath deployment |
| SPA | `true` | Instant navigation between notes |

## Resources
- [Quartz Documentation](https://quartz.jzhao.xyz/)
- [Obsidian Flavored Markdown Plugin](https://github.com/quartz-community/obsidian-flavored-markdown)
- [[Static-Site-Generators|Static Site Generators Comparison]]
- [[Digital-Gardens|Digital Garden Philosophy]]

## Blockers
- [ ] GitHub Pages not yet enabled in repository settings (manual step required)
- [ ] Need to verify custom domain / CNAME configuration

---

[[Projects/|← Back to Projects]]

#tags/project #quartz #web #obsidian