---
title: "Sourcegraph SCIP and LSIF"
details: "Binary index formats — SCIP (Structured Code Intelligence Protocol) and its predecessor LSIF — used by Sourcegraph and other repository intelligence platforms to persist out-of-core semantic code graphs that support cross-repository find-references, migration tracking, and symbol impact analysis."
tags:
  - entity
  - tool
  - format
created: 2026-09-19
updated: 2026-09-19
type: entity
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Sourcegraph SCIP and LSIF

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Tool / Format Standard
**Website:** https://sourcegraph.com

---

## Overview

SCIP (Structured Code Intelligence Protocol) is Sourcegraph's protobuf-based index format for encoding language-agnostic semantic code intelligence — symbol definitions, references, hover documentation, and cross-repository relationships. LSIF (Language Server Index Format) is its JSON-line predecessor. Together they underpin Sourcegraph's cross-repository code intelligence.

## Key Details

- **SCIP:** Protobuf-based, smaller, language-agnostic; designed to be the persistence layer for any code-intelligence tool, not just Sourcegraph.
- **LSIF:** JSON-line format; widely adopted prior to SCIP and still emitted by some indexers.
- **Indexers:** SCIP indexers exist for Go, TypeScript, Java, Python, Rust, C++, and more; LSIF indexers for most major languages via `lsif-clang`, `lsif-go`, `lsif-node`, etc.
- **Storage:** Indexes typically persist in RocksDB (embedded) or a graph backend; queries run over a network protocol against the index, not the source.

## Related Concepts

- [[Concepts/cross-repo-semantic-code-graphs]] — SCIP / LSIF are the canonical storage format for the cross-repo semantic graph pattern.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8