# Contributing

Thanks for helping maintain Codex Maintainer Kit.

## Local Setup

```bash
python3 -m pip install -e .
python3 -m pytest tests -q
```

## Pull Request Expectations

- Keep each pull request focused on one maintenance or behavior change.
- Add or update tests when CLI behavior changes.
- Update the README or examples when user-facing output changes.
- Include the verification command you ran in the pull request description.

## Human Review

AI-assisted contributions are welcome, but a human maintainer must review the diff and test output before merge.
