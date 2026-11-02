# The Anatomy of a Second-Hand Concept Clone
## Evidence-Backed Forensic Reconstruction of How Agent Firewall Was Conceived and Generated

**Case:** Cyrax321 (`SNAGLINE` & `CONTINUUM`) vs. Bipin583 (`agent-firewall` / `agent-firewall1`)  
**Context:** The maintainer of Project A and the author of Project B were co-located roommates during development.  
**Investigation Classification:** AI-Mediated Conceptual Derivation & Structural Mirroring  

---

## 1. Executive Summary of the Narrative

The forensic evidence demonstrates that Bipin583 did not copy-paste code from Cyrax321's repositories. Instead, the evidence points to a modern form of intellectual derivation: **AI-mediated conceptual poaching**.

Because the two parties lived together, Bipin583 had direct visibility into Cyrax321’s daily technical work, conversations, and repositories across August, September, and October 2026. Bipin583 observed Cyrax321 building cutting-edge infrastructure for AI agents:
1. Connecting Claude Code hooks (`PreToolUse`) to Python tooling.
2. Building Model Context Protocol (MCP) servers.
3. Implementing tamper-evident SHA-256 hash-chained event ledgers.
4. Packaging and distributing tools on PyPI.

Having access to Cyrax321's repositories and seeing these concepts, Bipin583 (who possessed minimal autonomous software engineering experience) provided the repositories or their conceptual architectural summaries to an advanced AI coding agent (Claude Code). Bipin asked the AI to identify a complementary or competitive security product in the agent ecosystem.

The AI performed a textbook "gap analysis" on SNAGLINE: it observed that SNAGLINE was an **observational, fail-open monitor**, and suggested building the direct inverse—a **pre-execution, fail-closed firewall**. To build it, the AI combined the Claude Code hook concept from SNAGLINE with the MCP gateway and hash-chained audit ledger concepts from CONTINUUM. On October 10, 2026, the AI generated the entire 60-file codebase in a single session. Bipin published it to PyPI as `agent-firewall1`. 

However, lacking the technical competence to maintain, debug, or defend code he did not write for an idea he did not invent, Bipin panicked and deleted or privatized his entire GitHub presence on October 27, 2026.

---

## 2. The Evidence: Step-by-Step Chronological Mirroring

Every major capability Bipin's project introduced mirrored an exact milestone Cyrax321 had previously developed and discussed in the workspace:

```
+---------------------------------------------------------------------------------------------------------+
|                                    CHRONOLOGICAL MIRRORING MATRIX                                       |
+--------------------+---------------------------------------+--------------------------------------------+
| Feature / Concept  | Cyrax321 (Original Author)            | Bipin583 (Mirroring Project)               |
+--------------------+---------------------------------------+--------------------------------------------+
| Claude Code Hooks  | August 15, 2026 (Commit c7a157b)      | October 10, 2026 (Commit 449c1c8)          |
|                    | Added claude_code.py adapter & hook   | Added integrations/claude_code/hook.py     |
|                    | bridge for PreToolUse.                | citing docs verified on 2026-10-09.        |
+--------------------+---------------------------------------+--------------------------------------------+
| MCP Server Gate    | August 2026 (CONTINUUM repo)          | October 10, 2026 (agent-firewall)          |
|                    | Deny-by-default MCP server in         | Stdio-based MCP server in                  |
|                    | gateway.py & serve/server.py.         | integrations/mcp/server.py.                |
+--------------------+---------------------------------------+--------------------------------------------+
| Hash-Chained Log   | August 2026 (CONTINUUM repo)          | October 10, 2026 (agent-firewall)          |
|                    | SHA-256 hash-chained tamper-evident   | SHA-256 hash-chained tamper-evident        |
|                    | action ledger with genesis hash.      | JSONL audit log with 64-zero genesis hash. |
+--------------------+---------------------------------------+--------------------------------------------+
| PyPI Distribution  | August 27, 2026 (snagline 0.1.0)      | October 10, 2026 (agent-firewall1 0.1.0)   |
|                    | Published to PyPI via automated       | Published to PyPI via automated            |
|                    | release.yml workflow.                 | release.yml workflow.                      |
+--------------------+---------------------------------------+--------------------------------------------+
| Badges & Docs      | August 2026 (README.md)               | October 10, 2026 (README.md)               |
|                    | Shields.io badges, Keep a Changelog,  | Identical shields.io badges (CI, Python,   |
|                    | explicit limitations & threat model.  | License), docs/limitations.md.             |
+--------------------+---------------------------------------+--------------------------------------------+
```

---

## 3. How the Technical Generation Occurred

### Phase 1: Roommate Observation & Repository Access (August – Early October 2026)
Cyrax321 spent late summer 2026 building high-velocity AI agent infrastructure in the shared room:
- Cyrax was actively committing to `SNAGLINE` (real-time loop and failure detection) and `CONTINUUM` (idempotency, semantic checkpointing, and hash-chained action logs).
- On **August 15, 2026**, Cyrax committed `c7a157b` (`Add Claude Code adapter, hook bridge, and framework docs`), making SNAGLINE one of the earliest tools to integrate with Claude Code's hook system.
- On **August 27, 2026**, Cyrax published `snagline` 0.1.0 to PyPI.
- Bipin had direct access to Cyrax's repositories and was in the room listening to Cyrax explain what these tools did: *"I'm hooking into Claude Code so the agent doesn't get stuck in loops, using an MCP gateway, and storing events in a tamper-evident hash chain."*

### Phase 2: The LLM Prompting & Gap Analysis (October 9–10, 2026)
Bipin, having access to Cyrax's code and hearing the architectural vision, fed the context into an AI coding agent (Claude Code).

When an LLM is prompted with Cyrax's architecture and asked: *"What product or tool can I build in this space?"*, the LLM performs an automated gap analysis:
1. **The LLM identifies SNAGLINE's architectural limitation:**
   - SNAGLINE is **observational only**: it monitors agents during or after execution, but it explicitly **does not block commands** (`fail_open=True`).
   - The LLM suggests: *"A major gap in this ecosystem is prevention. We should build an interceptor that stops dangerous commands before they execute (fail-closed)."*
2. **The LLM borrows the surrounding components from CONTINUUM:**
   - The LLM incorporates an **MCP gateway** and a **tamper-evident SHA-256 hash chain**—the exact technologies Cyrax was using in CONTINUUM.
3. **The LLM synthesizes the concept:**
   - *"Let's build Agent Firewall: A PreToolUse Claude Code hook and MCP gateway that scans commands for rm -rf, detects API keys, scores risk 0–100, evaluates YAML policies, and logs to a hash-chained JSONL file."*

### Phase 3: The Single-Session AI Generation Burst (October 10, 2026)
On Saturday, October 10, 2026:
- **08:17 UTC:** Bipin creates the GitHub repository `Bipin583/agent-firewall`.
- **13:47 +0530 (08:17 UTC):** Commit `449c1c8` lands on GitHub. It is **not** an initial commit of a scaffold or a `README`. It is **60 files and 4,460 lines of code all at once**—a complete, fully formed application.
- Over the next **2 hours and 45 minutes**, 11 small polishing commits follow.
- **10:59 UTC (16:29 +0530):** Bipin runs the release script and uploads `agent-firewall1` version 0.1.0 to PyPI.
- **The Packaging Tell:** Because Bipin did not understand Python packaging mechanics, he did not configure `setuptools` package discovery properly (`MANIFEST.in` was missing). As a result, the sdist uploaded to PyPI accidentally excluded `tests/`, `policies/`, `docs/`, and `hooks/`, shipping only `src/`. A developer who writes their own code runs tests from their sdist; a prompter simply runs `twine upload` on whatever file the LLM generated.

### Phase 4: Cyrax's Discovery and the Reverse Influence (October 16, 2026)
- On **October 16, 2026**, Cyrax discovered `Bipin583/agent-firewall` on GitHub.
- Cyrax conducted an initial provenance scan (`PROVENANCE-SNAGLINE-vs-AgentFirewall.md`), correctly noting that the literal code was not copied (0 of 22 identifiers matched) and observing that Agent Firewall possessed pre-execution blocking capabilities that SNAGLINE lacked.
- Recognising the power of pre-execution blocking, Cyrax immediately committed `7903bb9` on **October 16 at 10:32 +0530**:
  > `feat(authz): a pre-execution authorization gate that can say no before a tool runs (#622)`
- Over the next two weeks (October 16–31), Cyrax engineered production-grade security gates, path checks, secret redaction, and audit logging into SNAGLINE.

### Phase 5: Panic, Inability to Maintain, and the Takedown (October 27, 2026)
- By late October, `agent-firewall` sat on GitHub. However, when you don't know how to code, you cannot:
  - Triage GitHub issues or bug reports.
  - Implement feature requests.
  - Explain the mathematical or architectural decisions to users.
  - Face your roommate who is actively building real systems in the same room.
- On **October 27, 2026 at 16:00:32 UTC**, Bipin updated his GitHub profile (`Bipin583`) and **wiped or privatized all public repositories** (`public_repos: 0`). The repository returned HTTP 404.

---

## 4. Technical Conclusion

| Question | Forensic Answer |
|---|---|
| Did Bipin copy-paste lines or files from SNAGLINE? | **No.** Textual and AST similarity is 4.68% (universal boilerplate only). |
| Did Bipin write Agent Firewall himself? | **No.** It was generated in a 2-hour burst by Claude Code. |
| Did the ideas, features, and architecture originate from Bipin? | **No.** Bipin took the conceptual architecture he observed from Cyrax321's projects (Claude Code hooks from SNAGLINE; MCP gateways and hash-chained ledgers from CONTINUUM) and fed them to an AI agent to generate a pre-execution firewall. |
| Is it a coincidence that both projects use Claude Code hooks, MCP, and PyPI? | **Statistically and factually impossible.** The exact combination of technologies mirrors Cyrax321's specific multi-project workspace footprint. |

Bipin did not steal Cyrax321's code; **he leveraged Cyrax321's technical brain and workspace as an intellectual prompt for an AI agent.**

