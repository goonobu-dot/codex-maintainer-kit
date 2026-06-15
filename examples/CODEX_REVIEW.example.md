# Codex Change Review

Repository: `/path/to/example-repo`
Git state: `dirty`
Risk level: **high**

3 changed file(s) detected across: ci, security-sensitive, tests.

## Changed Files

| File | Category | Review note |
| --- | --- | --- |
| `.github/workflows/tests.yml` | ci | Confirm the workflow does not require unexpected secrets or broad permissions. |
| `src/auth/token_store.py` | security-sensitive | Inspect auth, token, permission, or secret-handling behavior carefully. |
| `tests/test_token_store.py` | tests | Confirm tests cover behavior and would fail for a real regression. |

## Maintainer Review Checklist

- [ ] Read the actual diff, not only this generated summary.
- [ ] Confirm the change is scoped to one maintenance goal.
- [ ] Run the verification command or explain why it cannot be run.
- [ ] Tests were changed: confirm they would fail for the bug or missing behavior.
- [ ] CI or security-sensitive files changed: confirm permissions, secrets, tokens, and external calls.
- [ ] Do not auto-merge AI-generated changes without human review.

## Verification Commands

- `python3 -m pytest -p no:cacheprovider tests -q`

## Suggested Codex Review Prompt

Review the changed files above as an OSS maintainer. Focus on correctness, scope control, tests, documentation accuracy, security-sensitive changes, and whether the diff is small enough for human review. Do not approve the change unless the verification commands are practical and the remaining risks are named.

## Human Review Rule

This report is a review aid, not an approval. A human maintainer must inspect the actual diff before merge.
