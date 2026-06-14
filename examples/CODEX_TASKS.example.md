# Codex Maintenance Tasks

Repository: `/path/to/example-repo`
Project hints: python

## Task 1: Add LICENSE

Priority: `high`

Add a clear license so users know how the project can be reused.

### Codex Prompt

Add an MIT LICENSE file if the project owner approves MIT, then update README license references if needed.

### Completion Criteria

- [ ] A LICENSE file exists.
- [ ] README license references are accurate.
- [ ] No source files are changed unnecessarily.

### Human Review

Human review must confirm the intended license before merge.

## Task 2: Add AGENTS.md

Priority: `high`

Add repository instructions for Codex and other coding agents.

### Codex Prompt

Create AGENTS.md with the project purpose, development commands, testing command, and human review rule.

### Completion Criteria

- [ ] AGENTS.md exists.
- [ ] The test command is documented.
- [ ] The file says AI-generated changes require human review.

### Human Review

Human review should confirm the instructions match the real repository workflow.
