# Comprehensive Technical Forensic Investigation Report

## 1. Case Metadata & Overview

- **Investigation Authority:** Senior Software Forensics Specialist & Reverse-Engineering Analyst
- **Investigation Subject:** Provenance and software derivation analysis comparing:
  - **Project A:** `https://github.com/Cyrax321/SNAGLINE`
  - **Project B:** `https://github.com/Bipin583/agent-firewall` / PyPI `agent-firewall1`
- **Date of Investigation:** 2026-10-31
- **Preserved Evidence Artifacts:**
  - `snagline` Git repository (`Cyrax321/SNAGLINE`, commit `e358e1a`)
  - `agent_firewall1-0.1.0.tar.gz` (PyPI SHA-256: `6debd886e0f4074c272a9707685f2e2834a3e179c148993d3134c3882d5f8530`)
  - `agent_firewall1-0.1.0-py3-none-any.whl` (PyPI SHA-256: `6da98824206fa37c74fd850e37ba8fac8dfb5d4dac6ea0efe909a811dc577ffe`)
  - GitHub User Profile `Bipin583` metadata (0 public repos, updated 2026-10-27T16:00:32Z)
  - Historical project publication: `PROVENANCE-SNAGLINE-vs-AgentFirewall.md` (authored 2026-10-16)

---

## 2. Exhaustive Analysis by Investigation Dimension

### 2.1 Direct and Modified Source Code Analysis
- **Textual Equality:** No non-trivial Python source file in Project B matches any file in Project A. The sole identical file is `py.typed`, an empty zero-byte PEP 561 marker.
- **Line-by-Line Code Overlap:** Across all 4,460 lines of code in Project B, only 14 non-trivial lines (>= 28 characters) match lines in Project A. Every matching line represents:
  1. Universal Python standard boilerplate (`from __future__ import annotations`, `import json`, `from typing import Any`).
  2. Protocol fields mandated by Claude Code's external JSON API specification (`"hookSpecificOutput": {`, `"permissionDecision": perm`).
- **Identifier Matching:** An automated scan for 22 distinctive SNAGLINE domain identifiers (`FailureRisk`, `StepEvent`, `episode_id`, `action_signature`, `make_signature`, `fail_open`, `CUSUM`, `Welford`, `silent_abort`, `meltdown`, `stagnation`, `idle_gap`, `wall_clock_budget`, `compaction_tripwire`, `side_effect_duplicate`) returned **0 hits in Project B**.

### 2.2 Abstract Syntax Tree (AST) & Structural Similarity
- **Class Hierarchy:** AST analysis across 295 classes in Project A and 29 classes in Project B identified only **1 shared class name**: `Policy`.
  - In Project A (`authorize.py`), `Policy` is an authorization configuration class evaluating rule lists.
  - In Project B (`policies/schema.py`), `Policy` is a Pydantic model representing a declarative YAML policy rule with selectors and effects.
  - The internal fields, inheritance hierarchies, and method implementations share zero structural correspondence.
- **Function/Method Correspondence:** Of 2,553 functions in Project A and 87 functions in Project B, 16 share names. All 16 represent generic, domain-agnostic verbs: `__init__`, `main`, `run`, `check`, `score`, `as_dict`, `from_env`. None share identical call graphs, control flow, or argument signatures.

### 2.3 Algorithmic and Heuristic Distinctiveness
- **Behavioral Loop & Anomaly Detection:** Project A's signature algorithms—Welford's algorithm for online variance, CUSUM for cumulative drift, sliding-window n-gram signature normalization, and Echo State Networks (ESN)—are **entirely absent from Project B**.
- **Rule Engines:** Where functional objectives overlap (e.g., detecting secrets or shell attacks):
  - **Secret Detection:** 0 of 11 regular expression patterns match. Project B searches for AWS ASIA tokens, generic passwords, and emails; Project A searches for Google AIza keys, Stripe keys, and basic auth URLs.
  - **Prompt Injection:** 0 of 10 patterns match. The regexes differ in syntax, token classes, and boundary anchoring.
  - **Shell Threats:** Project B implements a monolithic compiled regex scanner (`_DANGEROUS` tuple); Project A implements modular predicate rule functions with configurable overrides.

### 2.4 Architectural Forensics: The Inversion Invariant
The most conclusive technical finding is that the two systems embody **diametrically opposed architectural invariants**:
- **Project A (SNAGLINE): Fail-Open.** SNAGLINE's mission is non-intrusive monitoring. It enforces `fail_open=True` (referenced 671 times in the repository). If an exception occurs in an adapter or detector, it is caught and suppressed to prevent crashing or halting the agent. SNAGLINE does not issue execution-blocking commands.
- **Project B (Agent Firewall): Fail-Closed.** Agent Firewall's mission is pre-execution policy enforcement. Its formal threat model (`docs/limitations.md`) declares: *"Fail-closed. Unknown tools, authorization failures, detector crashes, and policy-load errors never silently allow. They degrade to block or ask."* Its evaluation logic enforces `deny > approval > allow`.

A derivative codebase does not systematically invert its parent's fundamental execution invariant across all modules while simultaneously removing all monitoring detectors.

### 2.5 Historical Chronology and Timeline Directionality
The historical timeline establishes an insurmountable physical barrier to the derivation hypothesis:
1. **October 10, 2026 (10:59 UTC):** Project B was published on PyPI as `agent-firewall1` 0.1.0, containing its full pre-execution policy gate, shell rules, path rules, secret detection, DLP, prompt injection heuristics, additive risk scoring, hash-chained audit logging, and MCP gateway.
2. **October 10, 2026:** Project A (`SNAGLINE`) at commit `1111cae` / `3d50a80` contained **none** of those security or gating capabilities.
3. **October 16, 2026:** Project A's maintainer conducted an internal provenance review (`PROVENANCE-SNAGLINE-vs-AgentFirewall.md`), finding zero identifier matches and explicitly stating that Agent Firewall had capabilities that SNAGLINE did not possess.
4. **October 16 to October 31, 2026:** Project A began adding security gating capabilities to SNAGLINE:
   - `authorize.py` added on October 16 (#622).
   - `shell_security.py` added on October 22 (#649).
   - `path_security.py`, `secret_security.py`, `dlp_security.py` added on October 25 (#673, #674, #675).
   - `security_audit.py`, `prompt_injection.py`, `security_scoring.py`, `security_evaluation.py`, and `adapters/mcp_gateway.py` added on October 31.

Because Project B possessed these features on October 10 and Project A did not introduce them until October 16–31, **Project B could not have copied or derived them from Project A**.

### 2.6 AI-Assisted Development Analysis
Both repositories exhibit traits consistent with AI-assisted software engineering:
- Use of Claude Code configuration files (`.claude/settings.json`).
- Highly structured docstrings and commit messages.
- Cohesive multi-file implementations committed in single milestones.
However, the artifact evidence demonstrates that AI assistance was applied to **two separate problem statements from different premises**:
- In Project A, AI tools assisted in developing an agent failure and loop observability framework.
- In Project B, AI tools assisted in developing a pre-execution firewall and policy enforcement gate.
There is zero evidence that an AI agent was used to ingest Project A's source code, refactor it, and output Project B.

---

## 3. Evidence Classification Summary

| Evidence Item | Description | Evidentiary Level | Lineage Implication |
|---|---|---|---|
| EVD-001 | 0/22 distinctive SNAGLINE domain terms in Project B | Level 1 (Direct) | Disproves lexical or conceptual copying. |
| EVD-002 | Universal failure posture inversion (Fail-Open vs. Fail-Closed) | Level 1 (Direct) | Disproves architectural derivation. |
| EVD-003 | Absence of all 15 SNAGLINE behavioral failure detectors in Project B | Level 1 (Direct) | Disproves functional reuse. |
| EVD-004 | Chronological impossibility: AF security features (Oct 10) precede SNAGLINE security features (Oct 16-31) | Level 1 (Direct) | Disproves historical derivation. |
| EVD-005 | Zero matching regex patterns across secret, prompt injection, and command rules | Level 2 (Strong Circumstantial) | Demonstrates independent heuristic formulation. |
| EVD-006 | Disparate data models (`StepEvent`/`FailureRisk` vs. `NormalizedRequest`/`SecurityDecision`) | Level 2 (Strong Circumstantial) | Demonstrates independent abstraction design. |
| EVD-007 | 14 shared lines >= 28 chars, all universal boilerplate or Claude Code hook schema | Level 3 (Supporting) | Attributable to public standard specification. |
| EVD-008 | Shared `release.yml` structure following PyPA publisher action template | Level 3 (Supporting) | Attributable to upstream reference documentation. |

