# Documentation & translations

- Translated documents must mirror the English source structurally: identical `##` section count and order, the new section in the same relative position, and the same set of link targets in the same order. Confidence: 0.9
- Link targets are never translated; only link text/prose is localized. Confidence: 0.85
- Each translated file keeps its own house punctuation conventions (full-width brackets/separators in ja and zh-CN, half-width in ko and pt-BR, full-width commas in zh) — do not paste English commas into a translated file. Confidence: 0.8
- Before adding translated prose, grep the target file for the terms being translated to confirm the established wording in that language (e.g. provenance, compaction, seal, release notes) instead of inventing a new term. Confidence: 0.85
- A translated TOC must mirror the English TOC exactly, including the sections the English TOC omits; adding a TOC anchor only in the translations breaks parity. Confidence: 0.8
- Out-of-scope fixes that would require touching the English source (e.g. adding a missing TOC anchor to README.md) belong in a separate change, not folded into a docs PR that claims a narrower scope. Confidence: 0.8
- Verify every referenced path in a doc map actually exists before merging. Confidence: 0.85
- Doc-only changes generally do not need a CHANGELOG entry when repo precedent shows doc-only PRs skipping it — but check precedent rather than assuming. Confidence: 0.6
