# Communication style

- Gives terse, informal one-line instructions (with typos and mild frustration); carry out the literal request immediately without asking clarifying questions or re-litigating the decision. Confidence: 0.8
- Final reports should lead with what was found and what was actually changed, then give raw evidence (commands run, counts, diffstats) rather than prose assertions. Confidence: 0.8
- State explicitly what was NOT done and why (e.g. a merge blocked by a repo setting, a bot suggestion declined) so the user can make the call. Confidence: 0.85
- Offer out-of-scope follow-ups as explicit "say the word and I'll do it" options rather than performing them. Confidence: 0.8
- Credit contributors by name in PR bodies and comments, including who owns which part of a change. Confidence: 0.8
- Reply to bot review findings substantively with verification evidence (e.g. "all six files have exactly 18 TOC entries") before resolving the thread. Confidence: 0.8
- Check the linked issue for other people who claimed the same work and leave them a note so work isn't duplicated. Confidence: 0.7
- Flag conflicts with a contributor's own earlier review requests explicitly and point out that a repo's PR template may require a different issue-closing keyword. Confidence: 0.75
- When asked for a PR review comment, hand over ready-to-paste text for the user to post themselves (do not post it), and word it in a friendly, encouraging tone rather than blunt or terse. Confidence: 0.8
- Answers questions about a PR in a yes/no form ("is this mergeable?") — give the explicit verdict first, then the evidence. Confidence: 0.75
- For a diagnostic/analysis request, present findings as: exact numbers that explain the anomaly, a table mapping each distinct goal (repo history vs. the graph number itself) to the method that achieves it, and an explicit statement of what was NOT changed or pushed. Confidence: 0.8
- The user types informally and with typos and asks "is there any way…" questions, including destructive alternatives ("can we delete and recreate the repo?") — answer the feasibility question directly first, then the mechanism, without lecturing about ethics of git history rewriting. Confidence: 0.8
