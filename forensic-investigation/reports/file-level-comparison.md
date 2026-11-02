# Detailed File-by-File Forensic Comparison

## 1. Overview of File Inventories

- **Project A (SNAGLINE):** 261 non-hidden source files, including 15 behavioral detectors, 10 integration adapters, 9 telemetry sinks, 106 test files, benchmarks, examples, and comprehensive Sphinx documentation.
- **Project B (Agent Firewall - PyPI `agent_firewall1-0.1.0`):** 41 source and packaging files, comprising 1 core engine, 5 detection modules, 3 policy modules, 3 audit modules, 2 risk scoring modules, 3 API modules, 3 integration modules, and packaging manifests.

## 2. Direct File Hash Comparison (SHA-256)

Out of 41 files in Project B evaluated against all 261 files in Project A:
- **Exact Hash Matches:** Exactly **1 file**.
  - Match: `src/agent_firewall/py.typed` == `src/snagline/py.typed`
  - SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  - **Evidentiary Weight:** Zero. This is an empty 0-byte file mandated by PEP 561 to indicate inline typing.
- **Identical non-empty files:** **0 files (0.0%)**.

## 3. Comparative Module Analysis (Top Corresponding Modules)

### A. Claude Code Hook Adapters
- **Project A:** `src/snagline/adapters/claude_code.py` (305 lines)
- **Project B:** `src/agent_firewall/integrations/claude_code/hook.py` (88 lines)
- **SequenceMatcher Ratio:** 0.0954 (9.54%)
- **Token Jaccard Similarity:** 0.1420 (14.20%)
- **Analysis:**
  - Both modules read JSON from standard input provided by Claude Code's `PreToolUse` hook.
  - The shared vocabulary consists entirely of terms mandated by Claude Code's external specification:
    - `"hookSpecificOutput"`
    - `"hookEventName"`
    - `"permissionDecision"`
    - `"permissionDecisionReason"`
    - `"hook_event_name"`
    - `"tool_name"`
  - Algorithmic divergence:
    - Project A uses an in-memory `HookTracker` to compute elapsed latency between `PreToolUse` and `PostToolUse` to construct a `StepEvent` for loop and CUSUM analysis. It never outputs a blocking verdict (`return None` or empty response).
    - Project B normalizes the tool name and argument map into `NormalizedRequest`, passes it to `SecurityEngine.evaluate()`, and returns a blocking verdict (`permissionDecision: deny | ask | allow`).

### B. Shell Command Security Modules
- **Project A:** `src/snagline/shell_security.py` (378 lines, added 2026-10-22)
- **Project B:** `src/agent_firewall/detection/command_rules.py` (148 lines, published 2026-10-10)
- **SequenceMatcher Ratio:** 0.0329 (3.29%)
- **Token Jaccard Similarity:** 0.1751 (17.51%)
- **Analysis:**
  - Rule structures:
    - Project A defines rules as functional predicates returning `ShellFinding` with rule IDs `_DESTRUCTIVE`, `_PIPE_TO_SHELL`, `_CHAINING`, `_UNSAFE_REDIRECT`, `_OBFUSCATION`.
    - Project B defines a declarative tuple of compiled regexes with rule IDs `cmd.rm_rf_root`, `cmd.rm_rf_generic`, `cmd.dangerous_command` (mkfs, dd, fork bomb), `cmd.pipe_curl_to_shell`, `cmd.opaque_payload`, `cmd.unparseable`.
  - Zero regex patterns match between the two files.

### C. Secret Detection Modules
- **Project A:** `src/snagline/secret_security.py` (282 lines, added 2026-10-25)
- **Project B:** `src/agent_firewall/detection/secrets.py` (112 lines, published 2026-10-10)
- **SequenceMatcher Ratio:** 0.0783 (7.83%)
- **Token Jaccard Similarity:** 0.1984 (19.84%)
- **Shared Patterns:** 0 of 11 matching regexes.
- **Analysis:**
  - While both detect standard API keys (AWS, GitHub, Slack, Anthropic, OpenAI), their regular expression syntax, capture groups, and boundary constraints are completely different:
    - Project A: AWS `r"\b(AKIA[0-9A-Z]{16})\b"` (only AKIA).
    - Project B: AWS `r"\b(AKIA|ASIA)[0-9A-Z]{16}\b"` (includes temporary session credentials ASIA).
    - Project A: OpenAI `r"\b(sk-(?!ant-)[a-zA-Z0-9_-]{20,})\b"` (uses negative lookahead).
    - Project B: OpenAI `r"\bsk-[A-Za-z0-9]{20,}\b"` (standard prefix match).
    - Project B includes detection of PII/emails, Bearer tokens, and generic password strings; Project A includes Google Cloud `AIza` keys, Stripe live keys, and URL basic authentication credentials.

### D. Filesystem Path Modules
- **Project A:** `src/snagline/path_security.py` (386 lines, added 2026-10-25)
- **Project B:** `src/agent_firewall/detection/filesystem_rules.py` (104 lines, published 2026-10-10)
- **SequenceMatcher Ratio:** 0.0711 (7.11%)
- **Token Jaccard Similarity:** 0.1582 (15.82%)
- **Analysis:**
  - Project A provides full Windows drive and cross-platform lexical normalization (`_WINDOWS_DRIVE_RE`, `normalize_lexical_path`, case-insensitive traversal checks) and modular rule functions (`rule_path_traversal`, `rule_sensitive_locations`, `rule_allowed_roots`, `rule_denied_paths`).
  - Project B provides POSIX-focused path normalization (`_normalise`), simple `../` counting (`has_traversal`), a static sensitive file set, and a simple `is_outside_project` directory prefix check.

### E. Tamper-Evident Audit Logging
- **Project A:** `src/snagline/security_audit.py` (278 lines, added 2026-10-31)
- **Project B:** `src/agent_firewall/audit/writer.py` & `verifier.py` (174 lines, published 2026-10-10)
- **SequenceMatcher Ratio:** 0.1114 (11.14%)
- **Token Jaccard Similarity:** 0.2135 (21.35%)
- **Analysis:**
  - Both use standard SHA-256 hash chaining initialized with a 64-zero genesis hash (`"0" * 64`).
  - Serialization:
    - Project A encapsulates the record in an `@dataclass AuditRecord` with a `canonical_payload()` method serializing `index`, `timestamp`, `decision`, `tool_name`, `policy_id`, `rule_findings`, `request_meta`, and `previous_hash`.
    - Project B uses flat dictionary functions (`canonical_json`, `compute_event_hash`, `build_event`) hashing `event_id`, `timestamp`, `request_id`, `tool_name`, `decision`, `risk_score`, `risk_level`, `redacted_summary`, `matched_policies`, `matched_rules`, `explanation`, and `prev_hash`.
  - Concurrency:
    - Project A uses an in-process `threading.Lock()`.
    - Project B uses filesystem lock files via `fcntl`/file locks for inter-process synchronization.

### F. Multi-Factor Risk Scoring
- **Project A:** `src/snagline/security_scoring.py` (248 lines, added 2026-10-31)
- **Project B:** `src/agent_firewall/risk/scorer.py` (84 lines, published 2026-10-10)
- **SequenceMatcher Ratio:** 0.1008 (10.08%)
- **Token Jaccard Similarity:** 0.1736 (17.36%)
- **Analysis:**
  - Both map security findings to a 0–100 integer score.
  - Mechanics:
    - Project A uses a weighted formula with configurable baseline penalties and explicit category saturation curves.
    - Project B uses a linear additive base weight table (Critical=85, High=50, Medium=25, Low=10, Info=0) plus category diversity bonuses (multi-category escalation capped at 100).

## 4. Summary Matrix of File Disparity

| Analysis Category | Measurement | Note |
|---|---|---|
| Total Files Compared | 261 (A) vs. 41 (B) | Significant asymmetry in project scope |
| Identical Files (SHA-256) | 1 (2.44% of B) | `py.typed` only (0 bytes) |
| Files with >50% Lexical Similarity | 0 (0.0%) | No copied modules |
| Files with >25% Lexical Similarity | 0 (0.0%) | No superficial refactorings |
| Files with 10–25% Lexical Similarity | 4 (9.7% of B) | All explained by shared problem domain or external specs |
| Files with <10% Lexical Similarity | 36 (87.8% of B) | Completely independent source implementations |

