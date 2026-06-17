---
title: Memori (Dual-Mode Memory Layer)
detail: "Open-source **memory layer for AI agents** with dual-mode architecture:"
details: "Open-source **memory layer for AI agents** with dual-mode architecture:"
tags:
  - entities
created: 2026-06-13
updated: 2026-06-13
type: entitie
---
# Memori (Dual-Mode Memory Layer)

**Source:** HN Show HN (https://news.ycombinator.com/item?id=44821941)
**Category:** Tool / Open Source Project
**Repository:** https://github.com/GibsonAI/memori

---

## Overview

Open-source **memory layer for AI agents** with dual-mode architecture:
- **Short-term "conscious" memory** — working memory analog
- **Long-term retrieval** — SQL full-text search (not vector stores)

---

## Architecture

- **Multi-agent design:** Memory agent, Conscious agent, Retrieval agent
- **Structured storage** with zero-config startup
- **Multi-backend:** SQLite, PostgreSQL, MySQL
- **Automatic promotion:** Important long-term memories promoted to short-term

---

## Key Features

| Feature | Description |
|---------|-------------|
| Dual-mode memory | Working memory + persistent long-term |
| SQL full-text search | Avoids vector store complexity |
| Multi-agent internal | Specialized agents for memory ops |
| Zero config | Works out of the box |
| Multi-backend | SQLite/Postgres/MySQL |

---

## Status

- Show HN: 10 months ago (as of 2025-06-13)
- Active development
- Community: Positive early feedback ("Much better experience")

---

## Related Concepts

- [[Agent Memory Layer Patterns]]
- [[Typed Knowledge Architecture]]

---

## References

- HN Thread: https://news.ycombinator.com/item?id=44821941
- GitHub: https://github.com/GibsonAI/memori