---
title: Static Site Generators
detail: Comparison of static site generators for digital gardens
details: Comparison of static site generators for digital gardens
tags:
  - concepts
created: 2026-06-15
updated: 2026-06-17
type: concept
---
# Static Site Generators Comparison

## Top Contenders for Digital Gardens

| Generator | Language | Obsidian Support | Graph View | Learning Curve | Best For |
|-----------|----------|------------------|------------|----------------|----------|
| **Quartz** | TypeScript | Native | Built-in | Low | Obsidian users, digital gardens |
| **Astro** | TypeScript | Via plugins | Via plugins | Medium | Content-heavy sites, blogs |
| **Docusaurus** | TypeScript | Limited | Via plugins | Medium | Documentation sites |
| **VitePress** | TypeScript | Limited | Via plugins | Low | Documentation, simple sites |
| **Hugo** | Go | Limited | Via templates | Steep | Blogs, large sites |
| **Jekyll** | Ruby | Limited | Via plugins | Medium | GitHub Pages native |

## Why Quartz Won

1. **Native Obsidian Compatibility**
   - Wikilinks `[[Note Name]]` work out of the box
   - Frontmatter parsing matches Obsidian
   - Callouts `> [!note]` render correctly
   - Tasks `- [ ]` with checkboxes

2. **Digital Garden Features Built-in**
   - Graph visualization (force-directed)
   - Full-text search (FlexSearch)
   - Backlinks panel
   - Tag pages & folder pages
   - Canvas page support

3. **Developer Experience**
   - Hot reload on config + content changes
   - SPA navigation (instant page transitions)
   - Plugin system with 100+ community plugins
   - TypeScript config with schema validation

## Migration Path

If moving from another SSG:
- **From Jekyll/Hugo**: Convert templates to Quartz components
- **From Docusaurus**: Restructure content folder, update frontmatter
- **From Obsidian Publish**: Export vault, point Quartz at content folder

## Resources
- [SSG Comparison 2024](https://jamstack.org/generators/)
- [Quartz vs Others](https://quartz.jzhao.xyz/philosophy/)
- [[Concepts/Digital-Gardens|Digital Gardens]]
- [[Projects/Quartz-Garden|This Project]]

---

[[Concepts|← Back to Concepts]]

#tags/concepts #web #ssg #comparison