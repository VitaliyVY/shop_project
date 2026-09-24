# Laboratory Work 3: AntiGravity Hooks

## Created Files

- `.claude/settings.json` - Claude Code hook configuration.
- `.claude/project.md` - AntiGravity project context for new sessions.
- `.claude/hooks/block-dangerous` - PreToolUse safety hook.
- `.claude/hooks/session-start` - SessionStart context hook.
- `.claude/hooks/check-python` - PostToolUse Python syntax hook.

## Working Hooks

- `PreToolUse` blocks `rm -rf`/`rm -fr`, `chmod 777`, and `curl ... | sh` or
  `curl ... | bash`. It exits with code 2 when a command is blocked.
- `SessionStart` prints `.claude/project.md`.
- `PostToolUse` checks edited or written `.py` files with
  `python -m py_compile`.
- No Ruff or other project linter was installed, so no new linter was added.

## Verification

From the project root, run:

```powershell
'{"tool_input":{"command":"rm -rf build"}}' | python .claude/hooks/block-dangerous
'{"tool_input":{"command":"echo safe"}}' | python .claude/hooks/block-dangerous
'{"tool_input":{"file_path":"src/products.py"}}' | python .claude/hooks/check-python
python .claude/hooks/session-start
```

The first command prints `Blocked dangerous command (rm -rf/rm -fr).` and
returns exit code 2. A syntax error is reported by `py_compile`, for example:
`SyntaxError: invalid syntax`.

## Commands Used

- `python -m py_compile`
- `python -m pytest -q` (not available in the system Python environment)
- JSON and hook smoke tests using PowerShell pipelines
- Git status and remote inspection

## GitHub MCP Status

The available GitHub MCP integration does not expose branch, commit, or Pull
Request write operations in this environment. Create these manually:

```powershell
git switch -c feature/antigravity-hooks
git add .claude LAB3_SUMMARY.md
git commit -m "feat: add hooks for AntiGravity"
git push -u origin feature/antigravity-hooks
```

Then open a Pull Request from `feature/antigravity-hooks` to `main` in GitHub.