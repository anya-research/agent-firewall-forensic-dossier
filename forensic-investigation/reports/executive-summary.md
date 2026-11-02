# Forensic Code Provenance Investigation: Executive Summary

## 1. Executive Summary

This independent forensic code provenance investigation examined the relationship between:
- **Project A:** `https://github.com/Cyrax321/SNAGLINE` (Original Project, maintained by Cyrax321)
- **Project B:** `https://github.com/Bipin583/agent-firewall` / PyPI package `agent-firewall1` (Suspected Derivative Project, maintained by Bipin583)

The central investigative question was:
**Was Project B independently developed, or was it derived from, copied from, reverse-engineered from, or substantially reconstructed using Project A as its source?**

### Final Determination:
**Project B was INDEPENDENTLY DEVELOPED. The allegation of derivation, copying, reverse-engineering, or code reuse is UNSUPPORTED by the forensic evidence.**

The overall weighted forensic similarity index between the two codebases is **4.68%**, a figure fully accounted for by universal Python boilerplate, PEP 561 compliance markers, standard packaging structures, and Claude Code's public hook protocol.

---

## 2. Key Findings

1. **Zero Direct Code Copying:**
   - Across all 4,460 lines of code in Project B, exactly 1 file matches Project A: `py.typed`, an empty 0-byte file mandated by PEP 561.
   - All 14 non-trivial lines matching between the codebases are standard boilerplate (`from __future__ import annotations`, `import json`) or exact JSON field keys defined by Claude Code's external hook documentation.
2. **Zero Identifier or Conceptual Overlap:**
   - All 22 distinctive SNAGLINE domain identifiers (`FailureRisk`, `StepEvent`, `action_signature`, `CUSUM`, `Welford`, `silent_abort`, `meltdown`, `stagnation`, etc.) return **zero occurrences** in Project B.
3. **Absence of Project A's Core Domain:**
   - Project A is a **behavioral failure detector** designed to observe agent execution loops, stagnation, error cascades, latency drift, and entropy collapse.
   - Project B contains **none** of these detectors or concepts. It is an intercepting **pre-execution security policy firewall** designed to block tool execution based on authorization, secret scanning, command rules, filesystem checks, and prompt-injection indicators.
4. **Architectural Inversion:**
   - Project A's primary invariant is **Fail-Open** (`fail_open=True` in 671 occurrences; errors are caught and suppressed so host execution is never interrupted).
   - Project B's primary invariant is **Fail-Closed** (`deny > approval > allow`; errors and unhandled exceptions degrade to `ask` or `block`).
5. **Chronological Impossibility:**
   - Project B published its complete security firewall suite to PyPI on **October 10, 2026**.
   - On October 10, 2026, Project A contained **no** security gating, secret scanning, command rules, path checks, prompt injection heuristics, policy engines, audit logs, or MCP gateway features.
   - Project A introduced those security features in commits between **October 16 and October 31, 2026**.
   - It is physically and chronologically impossible for Project B to have derived features from Project A that Project A did not yet possess.

---

## 3. Major Differences

| Dimension | Project A (SNAGLINE) | Project B (Agent Firewall) |
|---|---|---|
| **Primary Goal** | Detect agent failure modes & loops in real time | Prevent unauthorized / dangerous tool actions |
| **Execution Point** | Post-action or in-flight passive monitoring | Pre-execution gatekeeper (intercepting proxy) |
| **Failure Mode** | Fail-Open (never blocks host agent) | Fail-Closed (denies by default) |
| **Core Algorithms** | Welford variance, CUSUM, sliding window n-grams | Regex rule suites, additive risk scoring, hash chains |
| **Output** | Diagnostic telemetry / risk alerts | Enforced tool verdicts (`deny`, `ask`, `allow`) |
| **Audit Mechanism** | External dispatch sinks (Slack, PagerDuty, Webhook) | Cryptographic SHA-256 hash-chained JSONL ledger |

---

## 4. Limitations of the Investigation

1. **Project B GitHub Repository Accessibility:**
   - The GitHub repository `https://github.com/Bipin583/agent-firewall` returned HTTP 404 during investigation, having been deleted or made private between 2026-10-16 and 2026-10-27.
   - Forensic analysis relied upon the immutable source distribution and binary wheels published on PyPI on 2026-10-10, cross-referenced with GitHub API user metadata and prior Git commit logs preserved on 2026-10-16.
2. **Private Development Logs:**
   - Private, uncommitted scratchpads or private conversations cannot be observed by public forensic tools. However, the artifact evidence (the code, architecture, and immutable publication timestamps) provides conclusive proof of independent development.




