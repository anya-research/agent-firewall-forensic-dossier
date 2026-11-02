# Forensic Provenance Archive & Code Theft Exposure Repository
> **Victim / Originator Systems:** **SNAGLINE** and **CONTINUUM**, engineered by **Anandhu's Team** (Anandhu P Shaji `@Cyrax321`, Adhinan, Abishek, Sooraj, and Parthip).  
> **Derivative / Infringing Systems:** **Agent Firewall** (`agent-firewall1 0.1.0`) and **SentinelAI** presentation, published by Bipin (`@Bipin583`).  
> **Physical Context:** Co-located roommates living together in the same room, sharing living space, desk area, computer screens, whiteboards, and local WiFi network.

---

## 📌 PRIMARY FORENSIC DOSSIER
For the complete, exhaustive 900+ line technical report, side-by-side code snippets, minute-by-minute timeline, and faculty cross-examination guide, please read:

👉 **[`MASTER_FORENSIC_EXPOSURE_DOSSIER.md`](MASTER_FORENSIC_EXPOSURE_DOSSIER.md)**

For AI IDEs and autonomous agents (Cursor, Claude Code, Windsurf, Copilot, Antigravity), see:  
👉 **[`AGENTS.md`](AGENTS.md)** / **[`CLAUDE.md`](CLAUDE.md)** / **[`.cursorrules`](.cursorrules)**

---

## 🔍 EXECUTIVE SUMMARY

In October 2026, Bipin583 published a PyPI package named `agent-firewall1 0.1.0` and a presentation named `SentinelAI: A Dual-Layer Authorization & Outcome Verification Framework`. 

When Bipin claimed "I have evidence I didn't copy", he relied on a naive text-diff tool returning 0% line copying. That defense is a trick: Bipin did not copy-paste code with a mouse. **He fed the architectural breakthroughs of his roommates into Claude Code across a 24-part prompt.** 

The AI generated fresh variable names and syntax, creating an illusion of 0% string overlap on plagiarism tools. However, the AI left behind **conclusive digital fingerprints** embedded directly in the production code:

1. **The Prompt Leaks (Proof of 100% AI Generation):**  
   Five separate source files contain verbatim references to an assignment checklist:
   - `schema.py:5` $\rightarrow$ `# (Part 7 precedence rule #1 / Part 24 review item). Unknown keys are rejected.`
   - `engine.py:3 & 195` $\rightarrow$ `Public contract (Part 6)` and `"""Convenience wrapper matching the Part 6 interface name."""`
   - `evaluator.py:6` $\rightarrow$ `Precedence (Part 7), applied in order and documented in docs/policy-engine.md:`
   - `authorization.py:5 & 20` $\rightarrow$ `Part 7 rule #2... and #3...` and `# Tools whose schemas we understand and can evaluate (Part 8 coverage).`
   - `prompt_injection.py:5` $\rightarrow$ `do (Part 12). This module only raises the *risk*...`
2. **The CONTINUUM Cryptographic Theft:**  
   Poached the proprietary 64-zero genesis anchor constant (`GENESIS_HASH = "0" * 64`), canonical JSON sorting (`separators=(',', ':')`), sequential hash-chain verification loop, and lazy-import MCP server factory (`build_server`) from CONTINUUM.
3. **The SNAGLINE Claude Code Hook Interception:**  
   Poached the exact same 9 tools (`Bash`, `Read`, `Write`, `Edit`, `MultiEdit`, `NotebookEdit`, `Glob`, `Grep`, `WebFetch`) and argument extraction keys, simply inverting SNAGLINE's fail-open monitor into a fail-closed firewall.
4. **The SentinelAI Invoice Benchmark Poaching (`INV-001` $\rightarrow$ `INV-1001`):**  
   Bipin's entire presentation demo revolves around a simulated invoice workflow mutating `INV-1001`. This was copied directly from CONTINUUM's custom `invoice:INV-001` idempotency benchmark (`src/continuum/benchmark/__init__.py:395-435` and `STATUS.md`).
5. **The Fatal Packaging Blunder (Proof of Zero Testing):**  
   In `config.py:19`, `REPO_ROOT = PACKAGE_DIR.parent.parent` assumes a repository layout. When installed via `pip install agent-firewall1`, it looks for `/usr/local/lib/policies/default.yaml` and crashes instantly with `FileNotFoundError`.
6. **The Post-Discovery Panic Wipe:**  
   When confronted with this evidence on October 27, 2026, Bipin wiped his entire GitHub account to `public_repos: 0`, causing the repository URL to return HTTP 404.

---

## 📂 REPOSITORY STRUCTURE

```
.
├── MASTER_FORENSIC_EXPOSURE_DOSSIER.md    # Definitive 900+ line unabridged forensic report
├── AGENTS.md                             # Universal AI agent navigation & query routing guide
├── CLAUDE.md                             # Claude Code configuration
├── .cursorrules                          # Cursor IDE agent instructions
├── agent_firewall1-0.1.0/                # Infringing PyPI package source code
│   └── src/agent_firewall/               # Leaked prompt citations & copied modules
├── untitled folder 2/                    # Victim System A2: CONTINUUM (Recovery, MCP, Ledger)
│   └── src/continuum/                    # Original GENESIS_HASH, hashing, and benchmark
├── untitled folder 3/                    # Victim System A1: SNAGLINE (Failure detection)
│   └── src/snagline/                     # Original Claude Code hook & tool mapping
├── sentinelai_presentation_extracted/    # Extracted slides from SentinelAI presentation
│   └── SENTINELAI_PRESENTATION_COMPLETE_EXTRACTION.md
├── SentinelAI_Final_Presentation (1).pptx # Original PowerPoint presentation
├── completedate1.txt                     # Primary forensic notes & code comparison log
├── newprojectdata.txt                    # Slide-by-slide correlation analysis notes
└── forensic-investigation/               # Forensic reports, SHA-256 hashes & AST metrics
```

---

## ⚖️ PROVENANCE & AUTHORSHIP
- **Lead Originator:** Anandhu P Shaji ([@Cyrax321](https://github.com/Cyrax321))
- **Engineering Team:** Adhinan, Abishek, Anandhu, Sooraj, and Parthip
- **Infringing Party:** Bipin ([@Bipin583](https://github.com/Bipin583))

