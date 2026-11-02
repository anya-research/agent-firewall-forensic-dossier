# Forensic Development Timeline & Publication Chronology

## 1. Timeline Table

| Date / Timestamp (UTC / Local) | Project / Actor | Event / Artifact | Verifiable Source / Reference | Evidentiary Significance |
|---|---|---|---|---|
| **2024-10-23 12:09:13 UTC** | Project B (`Bipin583`) | GitHub account created | GitHub Users API (`id: 186044657`) | Establishes account antiquity prior to both projects. |
| **2026-08-14 05:32:00 UTC** | Project A (`SNAGLINE`) | First public commit | Git commit `73133dd` (`Cyrax321/SNAGLINE`) | Establishes SNAGLINE inception: `FailureRisk`, `StepEvent`, fail-open `Monitor`. |
| **2026-08-14 to 2026-08-15** | Project A (`SNAGLINE`) | Core behavioral failure detectors added | Git commits `aa55d45`, `1242520`, `c7a157b` | Loop detection, error cascades, Welford/CUSUM latency anomalies, Claude Code adapter. |
| **2026-08-27 08:34:45 UTC** | Project A (`SNAGLINE`) | PyPI release `snagline` 0.1.0 | PyPI JSON API (`snagline-0.1.0.tar.gz`) | Initial public release of SNAGLINE as an agent failure detector. |
| **2026-10-09 (documented)** | Project B (`agent-firewall`) | Claude Code hook protocol research | Code comment in `src/agent_firewall/integrations/claude_code/hook.py` | Documents earliest verifiable internal work date for Project B. |
| **2026-10-10 08:17:00 UTC** | Project B (`agent-firewall`) | GitHub repository created | GitHub API metadata | Creation of repository `Bipin583/agent-firewall`. |
| **2026-10-10 08:17 to 11:02 UTC** (13:47 to 16:32 +0530) | Project B (`agent-firewall`) | 12 Git commits published | Commit sequence `449c1c8` through `75c802d` | Complete repository published in single burst: initial commit was 60 files / 4,460 lines. |
| **2026-10-10 10:59:26 UTC** | Project B (`agent-firewall`) | PyPI release `agent-firewall1` 0.1.0 | PyPI JSON API (`agent_firewall1-0.1.0.tar.gz`) | Publication of pre-execution policy firewall, DLP, secrets, shell rules, audit log, MCP gate. |
| **2026-10-10 (Preprint)** | Project A (`SNAGLINE`) | SNAGLINE Two-Week Engineering Report | `snagline_report.pdf` (Head commit `3d50a80`) | Technical report on SNAGLINE behavioral failure detection; no security gating features. |
| **2026-10-16 00:00:00 UTC** | Project A Maintainer | Internal provenance review | `PROVENANCE-SNAGLINE-vs-AgentFirewall.md` | Maintainer examines Agent Firewall; finds 0/22 identifier overlap; notes AF has capabilities SNAGLINE lacks. |
| **2026-10-16 10:32:49 +0530** | Project A (`SNAGLINE`) | Commit `7903bb9` (`feat(authz)`) | Git log `7903bb9` (#622) | First pre-execution authorization gate introduced into SNAGLINE. |
| **2026-10-22 20:04:07 +0800** | Project A (`SNAGLINE`) | Commit `1163f6f` (`feat(authz)`) | Git log `1163f6f` (#649) | Shell command threat detection (`shell_security.py`) added to SNAGLINE. |
| **2026-10-25 13:52:07 +0530** | Project A (`SNAGLINE`) | Commit `17e28f0` (`feat(path_security)`) | Git log `17e28f0` (#639, #673) | Path security checks (`path_security.py`) added to SNAGLINE. |
| **2026-10-25 16:27:46 +0530** | Project A (`SNAGLINE`) | Commit `93c8e66` (`feat(secret_security)`) | Git log `93c8e66` (#640, #674) | Secret detection & redaction (`secret_security.py`) added to SNAGLINE. |
| **2026-10-25 18:46:35 +0530** | Project A (`SNAGLINE`) | Commit `9dbed7f` (`feat(dlp_security)`) | Git log `9dbed7f` (#641, #675) | DLP checks (`dlp_security.py`) added to SNAGLINE. |
| **2026-10-27 16:00:32 UTC** | Project B Maintainer | GitHub repository deleted or set private | GitHub API user profile `Bipin583` (`public_repos: 0`) | `Bipin583/agent-firewall` becomes inaccessible via GitHub API (HTTP 404). |
| **2026-10-31 22:26 to 22:45 +0530** | Project A (`SNAGLINE`) | Commit sequence `df58b87` through `e358e1a` | Git log (commits `df58b87`, `80ea728`, `1a00705`, `f4c14e0`, `4c90fa5`, `e358e1a`) | Hash-chained audit log, prompt injection heuristics, 0-100 scoring, policy engine, and MCP gateway added to SNAGLINE. |

## 2. Chronological Analysis and Forensic Deduction

### A. The Baseline State of Project A on October 10, 2026
When Project B (`agent-firewall`) was published to PyPI on **October 10, 2026 (10:59 UTC)**, Project A (`SNAGLINE`) was at commit `1111cae` / `3d50a80`.
At that exact date, SNAGLINE was solely a **real-time behavioral failure detector** with:
- Temporal loop and repetition detection.
- Error cascade tracking.
- Latency anomaly detection using Welford's algorithm and CUSUM.
- Novelty and stagnation collapse detection.
- Entropy collapse / meltdown detection.
- Token runaway and context window exhaustion guards.
- Passive telemetry adapters for Claude Code, LangChain, AutoGen, and CrewAI.
- Output sinks for Slack, PagerDuty, Webhooks, and Continuum.

**Critically, on October 10, 2026, SNAGLINE contained zero security gating, zero secret detection, zero shell command inspection, zero path inspection, zero prompt injection heuristics, zero policy evaluation engines, zero hash-chained audit logging, and zero MCP gateway server capabilities.**

### B. The Feature Set of Project B on October 10, 2026
The PyPI source distribution of `agent-firewall1` 0.1.0 published on October 10, 2026 contained:
- `authorization.py`: Fail-closed identity and tool permission gate.
- `detection/command_rules.py`: Regex and command analysis (rm -rf, mkfs, fork bombs, pipe-to-shell, ufw disable).
- `detection/filesystem_rules.py`: Traversal, sensitive locations (.env, .ssh, .aws), outside-project checks.
- `detection/secrets.py`: Regex pattern matching for AWS, GitHub, Slack, OpenAI, Anthropic tokens.
- `detection/dlp.py`: Outbound transfer payload inspection.
- `detection/prompt_injection.py`: Heuristic prompt injection indicators (jailbreak, DAN, ignore instructions).
- `risk/scorer.py` and `risk/factors.py`: Multi-factor 0–100 additive risk scorer.
- `policies/schema.py`, `loader.py`, `evaluator.py`: Declarative YAML policy engine with precedence `deny > approval > allow`.
- `audit/writer.py` and `verifier.py`: Append-only, SHA-256 hash-chained tamper-evident JSONL audit log.
- `integrations/claude_code/hook.py`: Active `PreToolUse` hook emitting `permissionDecision: deny | ask | allow`.
- `integrations/mcp/server.py`: MCP gateway exposing `evaluate_tool_request`.

### C. Forensic Conclusion on Timeline Directionality
Because Project B published its entire security suite on **October 10, 2026**, and Project A did not implement corresponding security features until **October 16 through October 31, 2026**, it is **chronologically and physically impossible** for Project B to have derived its security architecture, rule systems, risk engine, audit log, or MCP gateway from Project A.

