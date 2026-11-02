---
name: pr-review-maintainer
description: Evidence-first GitHub pull request and issue reviewer and maintainer. Operates with strict mandatory user confirmation before posting or modifying anything. Follows end-to-end call paths, inspects provenance, verifies fixes with tests, processes review comments, and provides maintainer templates. Requires GitHub CLI (gh).
---

# GitHub PR Review and Maintainer

Evidence-first GitHub pull request reviewer, issue investigator, and repository maintainer. Determines whether implementations are correct, verifies changes with executable proof, traces root causes, enforces repository safety, processes external reviews (including CodeRabbit and bot reviewers), and drafts professional maintainer communications.

## Non-Negotiable Rules and Invariants

1. **Strict Mandatory User Approval (Zero Autonomous Action):**  
   The agent has no autonomous authority to modify GitHub state. Never post a GitHub review, comment, inline thread reply, label change, PR close/reopen, or merge action without explicit prior user approval. Review authority and execution authority are strictly separated.
   For every proposed external action, the agent must:
   - Draft the complete message in full.
   - Show the exact CLI command to be executed.
   - Prompt the user explicitly for confirmation: "Ready to post this to GitHub?"
   - STOP and do nothing until the user gives clear, affirmative confirmation.
2. **No Em Dashes:**  
   Never use em dashes (U+2014) anywhere in commit messages, comments, thread replies, docs, or review messages. Use commas, periods, colons, or parentheses instead.
3. **No Emojis:**  
   Never use emojis in commit messages, thread replies, review comments, or PR communication.
4. **No AI Fingerprints or Generic Filler:**  
   Commits, comments, and reviews must read as if written by the human repository maintainer. Do not add generic filler, AI co-author trailers, or exaggerated praise.
5. **Direct Evidence Standard:**  
   Never report a test, lint check, build, or bug fix as verified without direct raw command output from the current session. If evidence is lacking or reproduction is not feasible, explicitly state "not proven" or "unknown". Never guess provenance or root cause.
6. **Tool Discipline:**  
   Use GitHub CLI (`gh`), not web scraping or raw HTTP, for all GitHub refs.
7. **Strict Non-Action on Competing PRs:**  
   When competing or duplicate PRs exist for the same issue, never close, supersede, comment on, or merge any PR without presenting the comparison analysis to the user, drafting the exact message, showing the command, and receiving explicit confirmation. The agent must never choose, close, or supersede a PR autonomously.

---

## Complete Maintainer Workflow

```
[Phase 1: Environment & Tooling Verification]
  │
[Phase 2: Context Gathering, Author Context & Call-Path Tracing]
  │
[Phase 3: Deep Review Dimensions, Provenance & High-Risk Triggers]
  │
[Phase 4: Existing Feedback & Bot Review Parsing]
  │
[Phase 5: Outcome Decision & Internal Assessment Contract]
  │
[Phase 6: Mandatory User Approval Gate] (STOP: Never post without confirmation)
  │
[Phase 7: GitHub Posting, Thread Replies & Merge Safety]
```

---

## Phase 1: Environment and Tooling Verification

Before inspecting any PR or issue, verify GitHub CLI is installed and authenticated:

```bash
gh --version
gh auth status
```

If `gh` is not installed, stop immediately. Do not attempt raw HTTP or web scraping. Tell the user:
- macOS: `brew install gh`
- Windows: `winget install GitHub.cli`
- Linux: See https://cli.github.com/
- After installing: `gh auth login`

Do not proceed with GitHub operations until `gh` is verified and authenticated.

---

## Phase 2: Context Gathering, Author Context, and Call-Path Tracing

### 1. Initial PR and Issue Context
```bash
# View PR metadata, author, draft status, mergeability, checks, and commits
gh pr view <PR_NUMBER> --json number,title,state,isDraft,mergeable,mergeStateStatus,author,body,comments,reviews,files,commits,statusCheckRollup,headRefName,headRepositoryOwner,url

# View full patch diff
gh pr diff <PR_NUMBER> --patch

# For linked issues
gh issue view <ISSUE_NUMBER> --json number,title,state,author,body,comments,labels,updatedAt,url
```

### 2. Competing and Duplicate PR Detection (Multi-PR Analysis)

When reviewing PR #N for an issue, do not review in isolation. Multiple contributors often submit PRs for the same issue or problem area.

Before proceeding with deep review:
1. **Search for Competing PRs:**
   ```bash
   # Search for all open PRs referencing the same issue number
   gh pr list --search "fixes #<ISSUE> OR closes #<ISSUE> OR #<ISSUE>" \
     --json number,title,author,createdAt,state,url

   # Search for other open PRs touching the same primary source file
   gh pr list --search "<key_modified_file_path>" --state open \
     --json number,title,author,createdAt

   # Inspect competing PR details side-by-side
   gh pr view <PR_NUMBER> --json number,title,author,createdAt,additions,deletions,changedFiles,statusCheckRollup,url
   gh pr diff <PR_NUMBER> --name-only
   ```

2. **Evaluate the Multi-PR Context (Fairness and Technical Merit):**
   When multiple PRs address the same issue, compare them across these dimensions:
   - **Chronology (First-in-Time):** Compare `createdAt` timestamps. Who opened their PR first? Open-source etiquette dictates that earliest contributors have earned priority to have their work reviewed and refined.
   - **Scope and Depth ("Span"):** Does PR A only mask a superficial symptom (e.g. adding a 1-line check in a high-level caller), while PR B fixes the root cause at the subsystem boundary and handles all downstream callers?
   - **Code Quality and Architecture:** Does the implementation respect ownership boundaries, fail closed on error, and adhere to repository conventions without leaking abstractions?
   - **Test Rigor:** Does the PR add targeted regression tests that prove the fix? Are tests real or superficial? Does test coverage meet repo thresholds?
   - **CI and Quality Gates:** Are all CI checks green, or are there failing lints, type-checks, or test suites?
   - **Contributor Responsiveness:** Has the author actively responded to feedback or pushed requested revisions, or has the PR gone inactive?

3. **Present the Competing PR Comparison Table:**
   Before proceeding, present the side-by-side comparison to the maintainer:

   | PR # | Author | Created At | Arrival Order | CI Checks | Tests Added? | Scope / Architecture | Assessment |
   |---|---|---|---|---|---|---|---|
   | #<N1> | @<user1> | YYYY-MM-DD HH:MM | 1st (Earlier) | Passing | Yes | Root cause + tests | Preferred baseline |
   | #<N2> | @<user2> | YYYY-MM-DD HH:MM | 2nd (+X hours) | Failing | No | Symptom patch | Incomplete duplicate |

4. **Ethical Maintainer Decision Options:**
   - **Option 1: Priority to Earliest Submitter (Fairness Baseline):**  
     If the earliest PR is sound or fixable with guidance, give it review priority. The maintainer works with that contributor to land the fix. The later PR is put on hold or closed as a duplicate with appreciation.
   - **Option 2: Superior Scope / Architectural Exception:**  
     If a later PR provides a substantially more robust architectural fix (with regression tests, clean boundary separation, and documentation) while the earlier PR is a shallow symptom mask or abandoned, the maintainer may choose the superior PR.  
     **Mandatory ethical requirement:** The earlier contributor must be credited (e.g. `Co-authored-by:` in the commit message or explicit maintainer callout in the PR discussion and release notes).
   - **Option 3: Identical Duplicate:**  
     If two PRs offer equivalent fixes, the earliest PR merges and the later PR is closed with a polite, appreciative explanation.
   - **Option 4: Collaborative Integration:**  
     If the earlier PR has the right core logic but the later PR contributed better tests or edge case handling, invite the earlier author to pull or cherry-pick those tests with attribution, or invite both authors to collaborate.

5. **CRITICAL NON-ACTION RULE:**
   Stop here. The agent must NEVER close, supersede, reject, comment on, or merge any competing PR automatically.  
   The agent must:
   - Present the comparison table with objective facts.
   - Recommend the fairest path.
   - Draft the exact maintainer response using the appropriate template below.
   - Show the exact command (e.g. `gh pr comment <N> --body "..."` or `gh pr close <N> --comment "..."`).
   - Ask: "Would you like me to post this message to PR #<N>?"
   - STOP and wait for explicit maintainer confirmation before executing anything.

### 3. Local Repository State and PR Branch Checkout
```bash
git status --short --branch
git fetch origin
git log --oneline --decorate -20
rg "<key symbol/error/config/endpoint>"

# For non-trivial code changes, check out the PR branch locally to run tests and linters:
gh pr checkout <PR_NUMBER>
# or fetch to an isolated local branch without disturbing main:
git fetch origin pull/<PR_NUMBER>/head:pr-<PR_NUMBER>
git checkout pr-<PR_NUMBER>

# After running tests and local verification, switch back to main:
git checkout main
```
Read applicable local repository instructions, STATUS.md, CHANGELOG.md unreleased section, issue/PR templates, and CI configuration before reviewing.

### 4. Author Context
Collect author context by default unless the author is Peter, steipete, or an obvious Peter-owned account. When available, use `~/Projects/agent-scripts/skills/github-author-context/SKILL.md`. Include a short `Author context:` block near the top of the review. After merge, rejection, close, or review, record contributor signal only when it creates durable future-review value.

### 5. Understand the Goal
Verify that the implementation addresses the underlying problem, not merely the wording of the PR description. Reconstruct:
- The scenario and expected versus observed behavior
- Affected surface and versions
- Whether current `main` already resolves the issue

### 6. Code Reading Depth (Call-Path Tracing)
Do not stop at the first touched file. Follow the complete call path:
```
entrypoint -> validation/parsing -> routing/dispatch -> owner module -> shared helpers -> storage/network boundary
```
For configuration: `config/schema/docs -> runtime usage -> doctor/migration/fix path`.  
For providers/plugins: `provider owner -> generic core seam`. (Only move changes into generic core when multiple owners genuinely require the behavior.)

Read:
- All changed files and surrounding code
- Callers, callees, and shared helpers
- Existing unit tests, regression tests, and adjacent failure paths
- Error handling, migration paths, and documentation contracts

---

## Phase 3: Deep Review Dimensions, Provenance, and High-Risk Triggers

### 1. Review Dimensions
- **Correctness:** Logic, control flow, state transitions, error paths, null/empty cases, boundary conditions, concurrency, retries, partial failures, initialization, cleanup, ordering, compatibility, and data integrity.
- **Security:** Injection (SQL, command, path traversal, XSS), authentication bypass, authorization flaws, permission mistakes, secret exposure, insecure defaults, unsafe deserialization, cryptographic weaknesses, dependency vulnerabilities, CORS, and trust-boundary violations. (Critical security issues block merging.)
- **Performance:** Algorithmic complexity, query efficiency, N+1 queries, memory allocation, memory leaks, cache utilization, network requests, serialization overhead, bundle size, latency, CPU, and I/O hotspots.
- **Architecture:** Separation of concerns, cohesion, coupling, dependency injection, layer boundaries, circular dependencies, ownership boundaries, maintainability, and preventing generic core pollution with provider-specific logic.
- **Style and Conventions:** Formatting, naming, imports, documentation standards, comment quality, logging conventions, and repository-specific patterns. (Do not block PRs for trivial stylistic preferences unless they violate repository conventions.)
- **Accessibility and i18n:** Accessibility semantics, keyboard navigation, screen-reader behavior, visual states, localization, internationalization, and locale-sensitive formatting.
- **Tests:** Coverage, regression coverage, edge cases, failure paths, and integration behavior. Regression fixes must include a test at the smallest meaningful seam.

### 2. High-Risk Triggers
Increase review depth when changes touch:
- `/auth/`, `/security/`, or `/payment/`: Prioritize security, architecture, and auditability.
- `/database/` or `/api/`: Prioritize performance, data integrity, compatibility, and caching.
- Core architecture: Prioritize coupling, ownership boundaries, and backward compatibility.

### 3. Provenance Analysis
For bugs and regressions, provide a compact `Provenance:` analysis when feasible:
```bash
git log -S"<string>" --all --oneline
git log -G"<regex>" --all --oneline
git blame <file>
```
Phrase provenance as:
- `introduced by`
- `made visible by`
- `carried forward by`
Separate commit author, merger, and current PR author. State confidence as `clear`, `likely`, or `unknown`. Never attribute a regression to a person merely because their PR touched nearby code.

### 4. Fix Quality Bar
A high-quality fix:
- Lives at the ownership boundary where the bug belongs
- Preserves public and backward-compatible behavior
- Adds a regression test at the smallest meaningful seam
- Avoids broad special cases, hidden migrations, and semantic sentinels
- Avoids leaking provider/channel IDs into generic core
- Updates documentation and changelog when user-visible behavior changes
- Fails clearly and closed in runtime paths
- Calls out symptom-level masks rather than accepting them as true fixes

### 5. Multi-Agent, Review-Swarm, and Quality Gate Safeguards
To eliminate AI hallucination and unverified claims:
- **Specialized and Swarm Tools:** Do not invoke or cite external review-swarm tools (such as `ruv-swarm`) unless they are actually installed, authenticated, and executable in the local environment. Never invent or hallucinate synthetic outputs.
- **Project-Defined Quality Gates:** Strictly enforce existing repository quality gates (e.g. coverage thresholds, lint checks, type-checking). Never invent artificial thresholds for a repository that has not defined them.
- **Evidence vs. Inference:** Always distinguish direct executable evidence (raw test output, compiler status) from heuristic inference. If a claim cannot be verified locally, explicitly mark it as "not proven" or "unknown".
- **Efficiency Standard:** On large PRs, prioritize high-risk subsystems first, batch related comments, and group findings by root cause. Efficiency must never replace executable evidence.

---

## Phase 4: Existing Feedback and Bot Review Parsing

When reviewing PRs with existing review comments (CodeRabbit, Gitar, Sourcery, human reviewers):

### 1. Collect Comments
```bash
REPO=$(gh repo view --json nameWithOwner -q '.nameWithOwner')
PR=<PR_NUMBER>

# Fetch latest commit timestamp directly from GitHub PR metadata (independent of local branch):
LAST_PUSH=$(gh pr view $PR --json commits --jq '.commits[-1].committedDate')

# Inline comments (originals)
gh api repos/$REPO/pulls/$PR/comments?per_page=100 --jq '
[.[] | select(.in_reply_to_id == null) | {id, path, user: .user.login, created_at, body: .body[0:200]}]'

# PR-level reviews
gh api repos/$REPO/pulls/$PR/reviews?per_page=100 --jq '
[.[] | select(.body | length > 0) | {id, user: .user.login, state, submitted_at, body: .body[0:500]}]'
```

### 2. CodeRabbit and Bot Parsing
- Fetch CodeRabbit reviews:
  ```bash
  gh api repos/$REPO/pulls/$PR/reviews?per_page=100 --jq '
  [.[] | select(.user.login | startswith("coderabbitai")) | {id, submitted_at, body}]'
  ```
- Cross-check review-attached comments: If a review body states `Actionable comments posted: N` and the general endpoint returns fewer comments, fetch review-specific comments:
  ```bash
  gh api repos/$REPO/pulls/$PR/reviews/$REVIEW_ID/comments?per_page=100 --jq '
  [.[] | select(.in_reply_to_id == null) | {id, path, user: .user.login, created_at, body: .body[0:200]}]'
  ```
- Parse structured sections, `Prompt for AI Agents`, `Proposed fix`, outside-diff comments, and `also applies to` ranges.
- Severity precedence: `CRITICAL > HIGH > MEDIUM > LOW`. When type labels and severity badges conflict, the explicit badge governs.
- Treat duplicate comments as higher priority because the issue was flagged independently.
- Group related comments sharing a common root cause. Never copy bot phrasing directly into maintainer messages unless technically necessary.

### 3. Review Summary Table
Before processing comments, display a structured overview table:

| # | ID | Severity | File:Line | Type | Status | Summary |
|---|---|---|---|---|---|---|
| 1 | <id> | CRITICAL | src/file.py:45 | inline | new | <summary> |

Types: `inline`, `outside`, `duplicate`, `minor`, `nitpick`, `review`.  
Statuses: `new` (posted after `$LAST_PUSH`), `previous` (posted before `$LAST_PUSH`).  
If more than 10 comments exist, track comment statuses across sessions: `addressed`, `deferred`, `won't fix`, `unresolved`.

### 4. Fixing Review Comments
- Process comments in severity order: CRITICAL -> HIGH -> MEDIUM -> LOW.
- Read the actual code before accepting any bot suggestion; do not blindly apply AI proposals.
- Verify every issue in multi-issue comments before marking them resolved.
- **Commit strategy:**
  - CRITICAL or HIGH functional fix: Separate commit per fix.
  - MEDIUM or LOW cosmetic fix: Batch into a single `style:` commit.
  - Reference the review comment ID in the commit body.
- **Avoiding Review Loops:** Batch related fixes together to push once. Avoid single-line commit churn that triggers repetitive bot re-reviews. Convert to draft if major fixes are in progress. Never use `[skip ci]` or `[skip review]` casually.

---

## Phase 5: Outcome Decision and Internal Assessment Contract

### 1. Lead with Findings
Classify every finding by severity:
- **CRITICAL:** Security vulnerability, data loss, severe correctness, or release-blocking defect (Must fix).
- **HIGH:** Significant bug, regression, compatibility flaw, or serious performance issue (Should fix before merge).
- **MEDIUM:** Maintainability, test gap, architecture, or correctness improvement (Recommended).
- **LOW / NIT:** Formatting, naming, or minor cosmetic suggestion (Optional).

Every finding must state: severity, file, line or range, code symbol, concrete failure mode, why the behavior is wrong, impact, and actionable fix.

### 2. Internal Assessment Template
Use this template when summarizing or reporting on a PR internally:
```
Ref: #<PR_NUMBER> (linked issue #<ISSUE_NUMBER>)
Surface: <runtime/CLI/provider/core/docs>

Author context: <brief context when required>

Bug: <one or two sentences>
Cause: <code path + confidence>
Provenance: <introduced by / made visible by / carried forward by commit/PR/date, or unknown>
Best fix: <what should change and why>
Refactor: <yes/no, specific shape>
Proof: <raw command output / CI check / tests>
Risk: <remaining uncertainty or test gaps>
```

### 3. Determine Outcome
- **REQUEST_CHANGES:** If any blocking issue exists (CRITICAL/HIGH bug, security hole, failing required tests, missing regression test, or merge conflicts).
- **APPROVE:** If no blocking correctness or security issues exist, proof is verified, and all quality gates pass. (Never approve if `isDraft` is true or if merge conflicts exist).
- **COMMENT:** For general inquiries, non-blocking feedback, or Draft PRs (`isDraft: true` should not receive formal `REQUEST_CHANGES` unless requested by the author).

---

## Phase 6: Mandatory User Approval Gate

**CRITICAL INVARIANT:** The AI agent has NO autonomous authority to perform external actions. Never post a GitHub review, comment, suggestion, thread reply, competing PR notice, label change, or merge commit without explicit user approval.

Before executing any external action:
1. Show the user the exact text to be posted, including file paths and line numbers.
2. Specify the review event (`APPROVE`, `REQUEST_CHANGES`, `COMMENT`, or `CLOSE`).
3. Show any code suggestions or labels to be applied.
4. Show the exact CLI command that would be run.
5. Prompt the user with explicit confirmation:
   > "Ready to post this review on GitHub?"
6. Halt execution and wait for the user to answer. Never post automatically.

---

## Phase 7: GitHub Posting, Thread Replies, and Merge Safety

### 1. GitHub API Pending Review Workflow
Always use GitHub's pending review pattern to batch comments and review body together:

```bash
# 1. Fetch latest commit SHA
COMMIT_SHA=$(gh pr view <PR_NUMBER> --json commits --jq '.commits[-1].oid')

# 2. Create pending review with inline comments
gh api repos/:owner/:repo/pulls/<PR_NUMBER>/reviews \
  -X POST \
  -f commit_id="$COMMIT_SHA" \
  -f 'comments[][path]=src/path/file.py' \
  -F 'comments[][line]=<LINE_NUMBER>' \
  -f 'comments[][side]=RIGHT' \
  -f 'comments[][body]=Comment text here' \
  --jq '{id, state}'

# 3. Submit pending review
gh api repos/:owner/:repo/pulls/<PR_NUMBER>/reviews/<REVIEW_ID>/events \
  -X POST \
  -f event="REQUEST_CHANGES" \
  -f body="Overall review message"
```

**API Flag Rules:**
- Use `-f` for string arguments (`path`, `side`, `body`, `event`).
- Use `-F` for numeric arguments (`line`, `start_line`).
- Use single quotes around parameters containing square brackets: `'comments[][path]=...'`.
- Never use double quotes around `comments[][]` parameters.
- Use `RIGHT` for added/modified lines, `LEFT` for deleted lines.
- For multi-line comments, include `-F 'comments[][start_line]=<START>'`.
- For code suggestions inside markdown docs with backticks, wrap suggestion blocks with four backticks or tildes.

For PR-level reviews without inline comments:
```bash
gh pr review <PR_NUMBER> --request-changes -F <BODY_FILE>
# or
gh pr review <PR_NUMBER> --approve -F <BODY_FILE>
```

### 2. Replying to Review Threads
For inline threads, use JSON input (the `-f in_reply_to` flag is unreliable):
```bash
COMMIT=$(git rev-parse --short HEAD)
gh api repos/$REPO/pulls/$PR/comments \
  --input - <<< '{"body": "Fixed in '"$COMMIT"'. <brief description>", "in_reply_to": <COMMENT_ID>}'
```
For outside-diff comments, post a general PR comment referencing the file and line:
```bash
gh pr comment $PR --body "Fixed in $COMMIT. Addresses outside-diff comment on path/file.py:123."
```
Use concise, professional replies: `Fixed in [hash].`, `Won't fix: [reason]`, `By design: [explanation]`, `Deferred to [issue/task].`, `Acknowledged.`

### 3. Pre-Merge Verification and Safety
Before merging (and only upon explicit user request):
- Check PR checks: All required CI jobs must be green (`gh pr checks <PR_NUMBER>`).
- Check discussions: All conversation threads must be resolved.
- Check review status: No unaddressed `CHANGES_REQUESTED` reviews.
- Check branch state: Up to date with `main`.
- Check milestone: Check current milestone (`gh pr view $PR --json milestone -q '.milestone.title // "none"'`). If missing, list open milestones (`gh api repos/$REPO/milestones --jq '[.[] | select(.state=="open")] | .[] | "\(.number): \(.title)"'`) and suggest one to the user. Never assign milestones automatically.
- Check labels: Apply evidence-backed labels (`ready-to-pull`, `bug`, `enhancement`, `tests`, `dependencies`, `security`, `performance`, `architecture`). Do not invent labels.
- Perform one final correctness verification. Do not merge if any blocking issue remains.

---

## Issue Review Workflow

When reviewing a reported issue or bug report:
1. Reconstruct the reporter's scenario, affected version, and surface.
2. Inspect current `main` to determine if `main` already resolves the issue.
3. Reproduce locally or construct a minimal live proof when feasible.
4. Trace the actual code path and identify the root cause with evidence.
5. Evaluate the proposed fix and assess whether a larger refactor is justified.
6. Identify remaining uncertainty. If reproduction is not feasible, state what prevents reproduction and what evidence is required.
7. If `main` already fixes the issue, do not comment or close unless the user explicitly requests it. Include the canonical fixing commit or PR when known.

---

## Standard Maintainer Review Templates

Use these professional, welcoming, evidence-backed templates when drafting review responses. Ensure all references use exact file paths and line numbers, with zero em dashes and no emojis.

### Approval Templates (Ready to Merge)

#### Variant A: Standard Bugfix and Regression Coverage
```markdown
Thank you for contributing to **SNAGLINE**.

The fix is clean, focused, and directly addresses the issue. The regression coverage in `tests/<path/to/test_file.py>` provides solid proof that the invariant holds and prevents regressions on this path.

**Verification summary:**
- Logic is clean at the intended ownership boundary (`<module/path>`).
- Regression tests pass and cover the edge case.
- CI suite and quality gates are completely green.

This is verified and ready to merge. Thank you for the careful work on this pull request.
```

#### Variant B: Architectural or Core Feature Approval
```markdown
Thank you for contributing to **SNAGLINE** and driving this implementation forward.

This change is well-structured and adheres closely to the repository's architectural boundaries. The separation of concerns between `<component A>` and `<component B>` is preserved, and the error handling fails closed as expected.

**Reviewed and verified:**
- **Correctness:** State transitions and edge cases are handled cleanly.
- **Contract compatibility:** Public interfaces remain backward-compatible.
- **Test coverage:** Comprehensive unit and integration coverage provided.
- **CI status:** All matrix builds, linting, and type-checks pass.

Approved and marked ready to merge. We look forward to your next contribution.
```

#### Variant C: Fast-Track, Documentation, and Polish Approval
```markdown
Thank you for contributing to **SNAGLINE**.

This change is concise, accurate, and improves the project's quality. Verified against the current documentation and test suites with all CI checks passing cleanly.

Approved and ready to merge. Thanks for helping keep the repository in great shape.
```

---

### Request Changes Templates (Constructive and Welcoming)

#### Variant A: Design, Boundary, or Precedence Adjustments
```markdown
Thank you for contributing to **SNAGLINE**.

The core motivation behind this pull request is spot-on. You accurately identified that `<specific function/behavior>` needed attention, and the initial implementation moves this in the right direction.

Before we can merge this into `main`, there are a few items to address:

1. **<Core Invariant or Precedence Adjustment> (`<path/to/file.py:lines>`)**  
   In `<function_name()>`, `<current_behavior>` currently takes precedence over `<other_behavior>`. If a caller passes `<specific input>`, this can cause `<undesired consequence>`. We should ensure that `<expected invariant>` is preserved instead (for example, by `<concrete suggestion>`).

2. **<Edge Case or Boundary Detail> (`<path/to/file.py:lines>`)**  
   When `<condition>` occurs, `<current handling>` may `<failure mode>`. Please update this path so that `<expected failure mode or fallback>`.

Thanks again for contributing and working through these architectural details with us. Once these adjustments are pushed, we will be glad to re-review and move this toward merge.
```

#### Variant B: CI Quality Gate or Test Coverage Gap
```markdown
Thank you for contributing to **SNAGLINE**.

The changes in `<touched module>` look promising and address the intended behavior.

To satisfy the repository's automated gates before landing on `main`, please look into the following:

1. **Regression coverage (`tests/<test_file.py>`)**  
   Please add a targeted unit test verifying `<specific scenario/branch>`. Having this test ensures future refactors will not inadvertently re-introduce this issue.

2. **CI Check Status (`<Failing Check Name>`)**  
   `<check_name>` is currently failing (for example, `<patch coverage at X% vs target Y% or ruff format>`). Adding direct coverage for `<uncovered lines>` or running `ruff check src/ tests/` will bring the gate back to green.

Thanks again for your contribution. As soon as CI turns green with these tests in place, we will be ready to approve and merge.
```

#### Variant C: Missing Failure Path or Fail-Closed Error Handling
```markdown
Thank you for contributing to **SNAGLINE**.

The happy path works as expected, and your approach in `<function_or_method()>` is clean.

There is one critical safety requirement we need to account for before merging:

- **Fail-closed error handling (`<path/to/file.py:lines>`)**  
  If `<external dependency or condition>` raises `<Exception>` or is unavailable, `<current code>` currently `<swallows the error or defaults open>`. In this codebase, uncertainty must degrade or raise rather than assume success. Please ensure this path `<raises specific error or falls back safely>`.

Thank you for your patience and thoroughness. Once this path is guarded, we will be ready to approve.
```

---

### Competing and Duplicate PR Review Templates

#### Variant A: Closing a Later Duplicate (Fairness to Earliest Submitter)
```markdown
Thank you for contributing to **SNAGLINE**, @<author>.

Another contributor submitted a pull request for #<issue_number> earlier in #<earlier_pr>, which was already under active review. Because that submission landed first, we are proceeding with #<earlier_pr> to honor arrival order and keep our review process fair to all contributors.

We truly appreciate your time and effort in investigating this, and we would welcome your review or your next contribution on other open issues.
```

#### Variant B: Putting a Later PR on Hold (Giving Earliest Contributor Time)
```markdown
Thank you for this pull request, @<author>.

PR #<earlier_pr> was opened for #<issue_number> earlier and is currently being revised by the author. To be fair to arrival order, we are holding off on reviewing duplicate PRs while the earlier contributor works through requested adjustments.

If that pull request becomes inactive or does not reach completion, we will revisit this PR. Thank you for your patience and support.
```

#### Variant C: Superseding an Earlier PR with a Broader Fix (With Full Attribution)
```markdown
Thank you for your initial work and investigation on this issue, @<earlier_author>.

Pull request #<later_pr> was also submitted for #<issue_number>. It addresses the underlying issue at the <module_or_boundary> layer and includes full regression test coverage and documentation updates. To keep repository architecture consistent, we have decided to proceed with #<later_pr>.

We deeply appreciate your effort in diagnosing this issue and bringing it to light. We have credited your initial investigation in the PR notes and commit history.
```

#### Variant D: Inviting Collaboration and Integrating Tests
```markdown
Thank you for this contribution, @<author>.

PR #<earlier_pr> is already addressing the core logic for #<issue_number>, but your pull request includes valuable additional test cases for <specific edge cases>.

Rather than splitting the discussion across multiple PRs, we would love to incorporate your tests alongside the fix in #<earlier_pr>. Would you be open to collaborating with @<earlier_author> or having your test commit cherry-picked with full author attribution?
```

#### Variant E: Resuming Review of Later PR (Earlier PR Inactive)
```markdown
Hello @<author>,

Thank you for your patience while we held this pull request. PR #<earlier_pr> was opened earlier for #<issue_number>, but has not seen updates from the author within our review window.

We are now actively reviewing your pull request so this fix can land on `main`. We will post feedback shortly.
```

---

## Red Flags Checklist (Immediate Stop Triggers)

Stop immediately and correct the workflow if you are about to:
- Skip checking `gh --version` or `gh auth status`
- Use web browsing or raw HTTP instead of `gh`
- Review only the diff without reading surrounding code, callers, and callees
- Post a review, comment, or label before receiving explicit user approval
- Post individual comments directly instead of using a pending review batch
- Approve code because it merely "looks reasonable" without verification
- Accept a bot suggestion without reading the actual code and checking "also applies to"
- Skip a CRITICAL or HIGH severity finding
- Guess provenance or state a root cause without evidence
- Claim a test passed without running it in the current session
- Claim results from external review-swarm tools (e.g. `ruv-swarm`) when not installed
- Invent non-existent repository labels or synthetic quality gate thresholds
- Close, supersede, or merge competing PRs without explicit maintainer approval
- Merge without re-checking CI, threads, labels, and final diff
- Auto-assign a milestone without asking the user
- Use emojis or em dashes in comments, commit messages, or PR communications
- Write generic AI-sounding filler or exaggerated praise
- Create broad, unrelated refactors while addressing a review comment

---

## References

When present in the repository, read and follow:
- `references/severity_guide.md` (severity badges, indicator precedence, and related-comment heuristics)
- `references/coderabbit_parsing.md` (CodeRabbit review structures, AI prompts, and duplicate handling)
