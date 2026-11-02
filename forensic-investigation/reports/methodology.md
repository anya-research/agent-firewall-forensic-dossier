# Forensic Investigation Methodology

## 1. Overview and Scope
This investigation evaluates the code provenance and derivation relationship between:
- **Project A:** `https://github.com/Cyrax321/SNAGLINE` (Original Project)
- **Project B:** `https://github.com/Bipin583/agent-firewall` / PyPI package `agent-firewall1` (Suspected Derivative Project)

The core investigative question is:
**Was Project B independently developed, or was it derived from, copied from, reverse-engineered from, or substantially reconstructed using Project A as its source?**

## 2. Evidence Preservation Protocol
1. **Repository Preservation:**
   - Project A: Full Git clone preserved from `https://github.com/Cyrax321/SNAGLINE` at commit `e358e1a` (4,753 Git objects, 261 non-hidden files).
   - Project B: Public GitHub repository `https://github.com/Bipin583/agent-firewall` returned HTTP 404 (deleted or converted to private between 2026-10-16 and 2026-10-27; user `Bipin583` profile shows 0 public repositories updated 2026-10-27T16:00:32Z). Source distribution preserved directly from the official PyPI registry (`agent_firewall1-0.1.0.tar.gz` and `agent_firewall1-0.1.0-py3-none-any.whl`, published 2026-10-10 10:59:26 UTC).
   - Upstream historical records preserved, including `PROVENANCE-SNAGLINE-vs-AgentFirewall.md` (authored 2026-10-16) and `snagline_report.pdf` (authored 2026-10-10).
2. **Cryptographic Integrity:**
   - Every preserved package, sdist archive, wheel, and source file was hashed with SHA-256. Hashes are recorded in `forensic-investigation/evidence/metadata/packages_sha256.txt` and verified against PyPI API metadata digests.
3. **Immutability:**
   - All comparisons are conducted against read-only copies stored within `forensic-investigation/evidence/`.

## 3. Analytical Dimensions and Techniques

### A. Exact and Normalized Textual Comparison
- **SHA-256 File Matching:** Full cryptographic hash matching across all files in both codebases.
- **Normalized Line Matching:** Normalization of whitespace, inline and block comments, blank lines, and docstrings.
- **Sequence Matching:** Python `difflib.SequenceMatcher` applied to normalized line streams to detect contiguous and non-contiguous structural block similarities.

### B. Abstract Syntax Tree (AST) & Identifier Forensics
- Complete AST parsing of all Python files in both repositories using Python standard library `ast`.
- Extraction and intersection of:
  - Class definitions, class inheritance hierarchies, and method sets.
  - Function definitions, argument signatures, and parameter ordering.
  - Import statements and module dependencies.
  - String, numeric, and regex constant literals.
- Identifier-normalized analysis to detect superficial renaming masking underlying algorithmic structure.

### C. Lexical N-Gram and Token Analysis
- Tokenization using regex word-boundary splitters (`[a-zA-Z_][a-zA-Z0-9_]*`).
- Token Jaccard similarity indices computed across all pairwise file permutations.
- 4-gram and 6-gram cross-repository indexing to isolate distinctive multi-word phrases and domain expressions from common boilerplate.

### D. Architectural and Behavioral Invariant Analysis
- Evaluation of fundamental system execution models:
  - Failure posture: Fail-Open (telemetry/observability) vs. Fail-Closed (pre-execution policy gateway).
  - Data ingestion pipeline: Event stream polling/push vs. Synchronous request-response policy evaluation.
  - State management: Temporal sliding windows, cumulative statistics (Welford/CUSUM) vs. Stateless request evaluation with append-only hash chains.

### E. Chronological and Historical Lineage Analysis
- Reconstruction of complete development timelines:
  - Initial public commits and release dates.
  - Feature implementation timestamps in Project A git history.
  - Publication timestamps of Project B on GitHub and PyPI.
  - Comparative analysis of code states on 2026-10-10 (date of Project B publication) vs. post-October 10 commits in Project A.

## 4. Evidentiary Standards
Findings are classified according to a strict four-level evidentiary hierarchy:
- **Level 1 (Direct Evidence):** Identical non-boilerplate code blocks, matching distinctive implementation sequences, or direct historical git lineage.
- **Level 2 (Strong Circumstantial Evidence):** Unusually identical multi-component architectural configurations, identical complex heuristics, or corresponding code transformations.
- **Level 3 (Supporting Evidence):** General structural similarity, shared dependency manifests, or standard industry naming conventions.
- **Level 4 (Weak / Ambiguous Evidence):** Conceptual functional overlap, common library boilerplate, or universal language idioms.

