# Tooling

- Prefer the `gh` CLI over raw web/API calls for PR operations: `gh pr view --json`, `gh pr list --json`, `gh pr diff`, `gh pr edit --body-file`, `gh pr checks`, `gh run view/list/watch`. Confidence: 0.85
- Use `gh api graphql` for review-thread inspection and resolution (the REST review API is not enough); fall back to the REST `pulls/<n>/reviews` endpoint when a token cannot create reviews via GraphQL. Confidence: 0.8
- Fetch PR branches locally as `git fetch origin pull/<n>/head:pr-<n>` and diff against `origin/main` with `git diff --stat origin/main...pr-<n>` before reviewing. Confidence: 0.85
- Push as a specific account with `git -c credential.helper= -c credential.helper='!gh auth git-credential' push https://<user>@github.com/...` after a `--dry-run` check. Confidence: 0.8
- Keep throwaway scripts, PR bodies, and review text in the session scratchpad directory and reference them via `$COMMANDCODE_SCRATCHPAD`, rather than writing into the repo working tree. Confidence: 0.85
- Use `git worktree add <scratchpad-path> origin/main` to get a pristine base for baseline test runs, and remove the worktree when done. Confidence: 0.8
- Use `git merge --no-commit --no-ff <other-branch>` to trial-merge a competing PR for conflicts, then `git merge --abort`. Confidence: 0.7
- Structured JSON output (`--json ... --jq`) is preferred over parsing human-readable CLI output. Confidence: 0.8
- For merge state, `gh pr view --json state,closed,closedAt,mergedAt,mergedBy,mergeCommit` is the reliable set (`merged` is not a valid field and errors out). Confidence: 0.65
- `gh api repos/<owner>/<repo>/issues/<n>/comments` lists issue and PR comments but can omit a comment that `gh pr comment` reported; cross-check with the GraphQL `pullRequest.comments` connection before concluding a comment exists. Confidence: 0.6
- To audit contribution-graph anomalies use `gh api graphql` with `contributionsCollection.commitContributionsByRepository` to attribute a day to repos, and `gh api repos/<owner>/<repo>/commits?sha=<ref>&since=...&until=...` reading the `Link: rel="last"` header to count server-side reachable commits in a date window. Confidence: 0.85
- A contribution spike often lives in a different clone than the one in the working directory — scan all sibling git repos in the workspace folder when hunting a spike day. Confidence: 0.8
- `git filter-repo` is not preinstalled here; install with `pip3 install git-filter-repo` before planning any history rewrite. Confidence: 0.75
- `git init` still creates `master` while GitHub's default branch is `main`; after `gh repo create`, run `git branch -M main` (or push `main:refs/heads/main`) or the first push fails. Confidence: 0.75
