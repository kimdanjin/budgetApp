---
name: csv-budget-cli
description: Use for Python CSV-based budget CLI app work, including TDD implementation, test design, refactoring, and quality checks for this repository.
---

# CSV Budget CLI

Use this skill when working on the repository's Python CLI budget app.

## Core workflow

1. Start with tests before implementation.
2. Keep functions typed and short.
3. Check complexity before merging changes.
4. Run the QA review flow before commit.

## Repository rules

- Treat the app as a CSV-backed CLI budget tool.
- Prefer small, focused functions.
- Keep cyclomatic complexity at 10 or below.
- Use `pytest` for test runs.
- Use `radon cc` to inspect complexity.

## Delivery checklist

- Tests added before code.
- Type hints on all functions.
- No function over 50 lines.
- QA review completed by `qa_engineer`.
- Commit after one feature is complete.
