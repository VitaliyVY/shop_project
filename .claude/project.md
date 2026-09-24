# AntiGravity Project

## Goal

AntiGravity is an educational in-memory shop management system. It models
products, users, orders, payments, and statistics without a database.

## Technology

- Language: Python 3
- Tests: pytest
- Main entry point: `main.py`
- Application code: `src/`
- Tests: `tests/`

## Working Rules

- Keep business logic changes focused and covered by tests.
- Keep data in memory; do not add a database without a separate requirement.
- Run `python -m py_compile` for changed Python files.
- Run the test suite with `python -m pytest -q` when pytest is available.
- Do not run destructive shell commands or pipe downloaded scripts to a shell.
- Preserve existing user changes and avoid unrelated refactoring.