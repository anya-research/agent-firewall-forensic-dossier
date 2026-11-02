# Verification & testing

- When a test fails on a branch, check whether it also fails on a clean checkout of the base branch before treating it as a regression; use a `git worktree` of `origin/main` to reproduce. Confidence: 0.9
- Distinguish environmental failures (port already bound by a stale server, untracked local scratch files) from real failures, and state them explicitly with evidence in the PR description. Confidence: 0.85
- Run the exact CI lint set locally (`npx markdownlint-cli2` over the same file globs the workflow uses) rather than a narrower selection. Confidence: 0.85
- Run the repo's own guard tests that cover the touched files (e.g. docs-count/parity tests) in addition to the full suite. Confidence: 0.8
- Write a small throwaway verification script for structural invariants (section counts, link order, bullet targets, trailing newline) instead of checking them by hand. Confidence: 0.8
- If a branch is far behind `main`, merge `main` in before judging test results; stale-base drift commonly causes false failures. Confidence: 0.8
- Do not kill or modify processes you did not start (e.g. a pre-existing server holding a port) — leave them and report the environmental cause. Confidence: 0.85
- Trial-merge a competing PR to check for conflicts, then abort the trial merge cleanly. Confidence: 0.7
- After writing to GitHub (posting/deleting a comment, pushing, resolving a thread), confirm the effect with an independent read; a 404 on `GET`/`DELETE` of a comment id means it never existed — `gh pr comment` can print a URL for a comment that never persisted. Confidence: 0.7
- Re-fetch the PR's live state (open/closed/merged, head SHA, mergeable flags) at the start of a review request instead of trusting earlier notes in the session; the user's request may be based on a stale view, and if the PR is already merged, verify what actually landed on `main` instead of producing a review. Confidence: 0.75
- When auditing commit history for artificial patterns, gather per-author/per-day histograms and compare author-date vs committer-date skew before drawing a conclusion; a single aggregate count is not evidence. Confidence: 0.8
- Establish the counting/attribution rule with a control case (a day whose count is expected to be genuine) instead of inferring it from one anomalous day. Confidence: 0.75
- When a plan hinges on a claim found on the web (e.g. "deleting a repo purges its contributions"), verify it empirically with a disposable probe repo — created with a clearly-labeled temporary description so it is safe to delete — instead of trusting a forum post. Confidence: 0.8
