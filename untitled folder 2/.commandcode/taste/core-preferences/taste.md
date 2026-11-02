# Core preferences
- Requires an explicit go-ahead before merging a PR or taking any irreversible action (push to a fork, merge to `main`); complete the verification first, then ask and wait. Confidence: 0.85
- Expects PR verdicts to be grounded in the actual diff and reproducible local checks, not in the summary/verdict posted by review bots (bots disagreed with each other; the real diff settled it). Confidence: 0.8
- Prefers mechanical verification over eyeballing: a small scratch script that asserts file-to-file parity (section counts, link order, bullet targets) is preferred over manual inspection. Confidence: 0.7
- Pastes the entire GitHub PR page as raw text rather than a link; work from that pasted content directly instead of asking for a link. Confidence: 0.6
- Likes adjacent findings surfaced explicitly for a decision (competing PRs touching the same files, other contributors claiming the same issue, unrelated test failures) rather than the agent silently widening scope or silently dropping them. Confidence: 0.7
- Cares about the public GitHub contribution graph looking authentic: wants commit bursts spread across realistic days and identifiable as genuine work rather than one giant same-day commit dump. Confidence: 0.8
- When history cleanup is requested, prefers the agent first diagnose exactly what the graph counts and why (per-ref duplication, push ledger) before recommending a rewrite, and to keep the actual code/content intact while re-dating or squashing commits. Confidence: 0.75
