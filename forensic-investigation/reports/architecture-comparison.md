# Forensic Architecture & Design Comparison

## 1. High-Level Architectural Comparison

Project A (SNAGLINE) and Project B (Agent Firewall) exhibit fundamentally divergent system architectures designed for two distinct operational problem domains:

```
+---------------------------------------------------------------------------------------------------+
|                                     PROJECT A (SNAGLINE)                                          |
|                                                                                                   |
|   Operational Domain: Post-Action / In-Flight Behavioral Failure & Loop Observability             |
|   Core Architectural Invariant: FAIL-OPEN (Under no circumstances does SNAGLINE block execution) |
|                                                                                                   |
|   [Agent Host] ---> (PreToolUse/PostToolUse) ---> [Hook Tracker / Normalizer]                     |
|                                                              |                                    |
|                                                              v                                    |
|                                                    [StepEvent Stream]                             |
|                                                              |                                    |
|                                                              v                                    |
|               +-------------------------------------------------------------+                     |
|               |                 Non-Blocking Monitor Engine                 |                     |
|               |  (Sliding Window, Welford Variance, CUSUM, Entropy, States) |                     |
|               +-------------------------------------------------------------+                     |
|                                       |                |                                          |
|                                       v                v                                          |
|                              [FailureRisk Score]   [Telemetry]                                    |
|                               (0.0 - 1.0 Informational)                                           |
|                                       |                                                           |
|                                       v                                                           |
|                  [Passive Sinks: Slack, PagerDuty, Webhook, Log]                                  |
+---------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------------+
|                                   PROJECT B (AGENT FIREWALL)                                      |
|                                                                                                   |
|   Operational Domain: Pre-Execution Authorization, Policy Enforcement & Attack Prevention         |
|   Core Architectural Invariant: FAIL-CLOSED (Precedence: deny > approval > allow)                 |
|                                                                                                   |
|   [Agent Host] ---> [PreToolUse Request] ---> [Authorization Gate (Identity & Tool)]              |
|                                                              |                                    |
|                                                              v                                    |
|                                                   [NormalizedRequest]                             |
|                                                              |                                    |
|                                                              v                                    |
|               +-------------------------------------------------------------+                     |
|               |                 Deterministic Detector Suite                |                     |
|               |   (Shell Rules, Path Rules, Secret Scanners, DLP, PI Hits)  |                     |
|               +-------------------------------------------------------------+                     |
|                                       |                                                           |
|                                       v                                                           |
|                           [Additive Risk Scorer] (0-100)                                          |
|                                       |                                                           |
|                                       v                                                           |
|                           [YAML Policy Evaluator]                                                 |
|                                       |                                                           |
|                                       v                                                           |
|                       [SecurityDecision: allow / ask / block]                                     |
|                                       |                                                           |
|                     +-----------------+-----------------+                                         |
|                     |                                   |                                         |
|                     v                                   v                                         |
|          [Host Enforcement]                 [Tamper-Evident SHA-256 Audit Log]                    |
|       (Blocks execution if deny)            (Hash-chained append-only JSONL)                      |
+---------------------------------------------------------------------------------------------------+
```

## 2. Core Abstractions & Data Model Comparison

| Conceptual Dimension | Project A (SNAGLINE) | Project B (Agent Firewall) | Evaluation & Lineage Assessment |
|---|---|---|---|
| **Primary Ingestion Entity** | `StepEvent` (`timestamp`, `episode_id`, `step_index`, `action_signature`, `latency_ms`, `error`) | `NormalizedRequest` (`request_id`, `agent_id`, `tool_name`, `action_type`, `resource`, `arguments`) | **Incompatible:** SNAGLINE models execution steps across time; Agent Firewall models isolated tool call payloads. |
| **Primary Output Entity** | `FailureRisk` (`score: float [0.0, 1.0]`, `detector: str`, `severity: Severity`, `evidence: dict`) | `SecurityDecision` (`decision: Decision`, `risk_score: int [0, 100]`, `matched_policies: list`, `explanation: str`) | **Incompatible:** SNAGLINE produces diagnostic advisory signals; Agent Firewall produces binding enforcement verdicts. |
| **Pipeline Posture** | Fail-Open (`fail_open=True` in 671 occurrences; errors swallowed to protect host) | Fail-Closed (`deny > approval > allow`; errors degrade to `ask` or `block`) | **Diametrically opposed:** Direct contradiction in core engineering philosophy. |
| **State Retention Model** | Stateful temporal windows (`WindowingBuffer`, exponential decaying counters, Welford accumulators) | Stateless per-request evaluation; append-only immutable hash-chained audit storage | **Incompatible:** SNAGLINE requires historical sequence context; Agent Firewall evaluates static rule invariants. |
| **Integration Pattern** | Sidecar observer; hook bridges that passively collect event metrics | Intercepting proxy; PreToolUse gate returning `permissionDecision: deny/ask/allow` | **Distinct:** Passive telemetry collector vs. Active gatekeeper. |
| **Storage Architecture** | Optional external sinks (Slack, PagerDuty, HTTP POST Webhook) | Local append-only JSONL with SHA-256 chain linking `prev_hash` to `event_hash` | **Distinct:** Telemetry dispatch vs. cryptographic tamper-evident ledger. |

## 3. Component Responsibility Matrix

| Subsystem | Project A (SNAGLINE - Baseline Oct 10) | Project B (Agent Firewall - Oct 10) | Structural Relationship |
|---|---|---|---|
| **Loop / Cycle Detection** | Implemented via signature normalization, sliding windows, and n-gram hash tables | **Absent** | Unique to Project A. |
| **Anomaly Detection** | Implemented via Welford mean/variance tracking and Cumulative Sum (CUSUM) | **Absent** | Unique to Project A. |
| **Stagnation / Entropy** | Implemented via novelty metrics and compression ratio tripwires | **Absent** | Unique to Project A. |
| **Secret Detection** | **Absent** on Oct 10 (added Oct 25) | Implemented via 11 deterministic regexes and token extractors | Unique to Project B on Oct 10. |
| **Shell Command Filtering** | **Absent** on Oct 10 (added Oct 22) | Implemented via regex rules (mkfs, rm -rf, fork bombs, pipe-to-shell) | Unique to Project B on Oct 10. |
| **Filesystem Path Rules** | **Absent** on Oct 10 (added Oct 25) | Implemented via traversal checks, sensitive targets, project bounds | Unique to Project B on Oct 10. |
| **Prompt Injection Heuristics**| **Absent** on Oct 10 (added Oct 31) | Implemented via heuristic classifier patterns | Unique to Project B on Oct 10. |
| **Policy Language** | Python `Config` class only | Declarative YAML schema with ANDed selectors and ORed lists | Unique to Project B on Oct 10. |
| **Audit Ledger** | **Absent** on Oct 10 (added Oct 31) | SHA-256 hash-chained JSONL ledger with verification CLI | Unique to Project B on Oct 10. |
| **MCP Integration** | **Absent** on Oct 10 (added Oct 31) | Stdio-based MCP server exposing `evaluate_tool_request` | Unique to Project B on Oct 10. |

## 4. Architectural Derivation Assessment
An architectural derivation requires evidence that the suspected derivative codebase preserves the component hierarchy, execution invariants, internal interfaces, or state management structures of the parent.

Here, **every architectural property is inverted or mutually exclusive**:
1. Project B lacks all 10 of Project A's behavioral failure detection components.
2. Project B's execution invariant (`fail-closed`) directly contradicts Project A's defining principle (`fail-open`).
3. Project B implements 7 major subsystems (Policy Engine, Hash Audit, Secrets, Command Rules, Path Rules, Prompt Injection, MCP Gateway) that were completely absent from Project A at the time Project B was released.

There is zero architectural derivation of Project B from Project A.

