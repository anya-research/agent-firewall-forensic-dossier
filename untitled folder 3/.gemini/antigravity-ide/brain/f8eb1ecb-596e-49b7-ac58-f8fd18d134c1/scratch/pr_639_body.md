## Summary
Add deterministic filesystem path security checks for tool requests that read, write, edit, or otherwise access files (issue #639).

The new `snagline.path_security` module normalizes paths lexically and identifies attempts to access restricted locations, path traversal sequences, and sensitive credential files before execution.

## Key Changes
* **Lexical Path Normalization**:
  * Normalize paths lexically (`normalize_lexical_path`) without hitting the physical filesystem.
  * Standardize directory separators, collapse `.` and `..` segments, preserve Windows drive letters, and resolve relative paths against a configurable `base_dir`.
* **Path Traversal Detection**:
  * Detect directory traversal attempts (`..` escaping roots or working directories).
  * Immediately flag embedded null byte injections (`\0`) as critical security violations.
* **Sensitive File and Location Detection**:
  * Detect attempts to access sensitive files including environment files (`.env`, `.env.*`), SSH keys and config (`~/.ssh`, `id_rsa`, `id_ed25519`, `authorized_keys`), cloud credentials (`~/.aws`, `~/.azure`, `credentials.json`, `service_account.json`), system files (`/etc/shadow`, `/etc/sudoers`, `/etc/master.passwd`), cryptographic keys (`*.pem`, `*.key`, `*.pfx`), shell history files, and git credentials.
* **Allowed Roots and Denied Paths/Patterns**:
  * Enforce configurable `allowed_roots`, `denied_paths`, and `denied_patterns` with boundary-aware path comparisons.
* **Authorize Pipeline Integration**:
  * Provide `as_authorize_rule` converting path security findings into `snagline.authorize.RuleVerdict` instances (`deny` or `ask`).
  * Extend declarative policy schema (`policy_from_dict`) with full support for `type="path_security"` configuration.
* **Independence and Limitations**:
  * Pure lexical checks: zero filesystem access, zero stat calls, zero file creation or modification.
  * Completely independent of the `Monitor` event ingestion pipeline.
  * Explicitly documents limitations regarding symlinks, TOCTOU races, and hard links in the module docstring.

## Verification
* 44/44 tests in `tests/test_path_security.py` passed with 100% line and branch coverage on `src/snagline/path_security.py`.
* 76/76 tests in `tests/test_authorize.py` passed with 92% coverage on `src/snagline/authorize.py`.
* 46/46 tests in `tests/test_shell_security.py` passed with 98% coverage.
* Full security suite (166 tests) passed in 1.10s.
* `ruff check`, `ruff format --check`, and `mypy` clean with 0 errors across all modified and created files.

Fixes #639
