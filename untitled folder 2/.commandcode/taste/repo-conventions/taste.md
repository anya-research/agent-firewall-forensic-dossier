# Repository conventions (Cyrax321/CONTINUUM)

- Conventional Commits titles are enforced by CI (`feat:`, `fix:`, `docs(readme): ...`); follow the repo's `AGENTS.md` for commit body style. Confidence: 0.85
- Commits in this repo carry no AI co-author trailer, per the explicit rule in `AGENTS.md` — this overrides the default habit of adding one. Confidence: 0.9
- PR bodies follow `.github/PULL_REQUEST_TEMPLATE.md`: Description, Related issues, Types of changes, Breaking changes, How has this been tested?, Checklist, Additional context. Confidence: 0.9
- Use `Fixes #N` only when the issue is genuinely fully resolved; otherwise use `Addresses #N` / `Refs #N` per the template, to avoid closing an issue prematurely. Confidence: 0.85
- `main` branch protection requires an approving review from an account other than the last pusher, so a maintainer's own approval on their own push does not satisfy the gate. Confidence: 0.85
- `main` branch protection dismisses stale reviews, so an approval must be re-submitted after the final push. Confidence: 0.8
- The repo's translated READMEs (`README.es.md`, `.ja.md`, `.ko.md`, `.pt-BR.md`, `.zh-CN.md`) are kept in parity with `README.md` — same `##` section count, same link targets in the same order — and a docs guard test (`tests/test_docs_counts.py`) enforces the README's counts. Confidence: 0.85
- Fork PRs trigger a first-time-contributor workflow gate: `action_required` runs must be approved via the Actions API before CI executes. Confidence: 0.8
