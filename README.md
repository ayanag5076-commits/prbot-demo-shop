# prbot-demo-shop

A tiny SQLite shop backend used as the live demo target for **prbot**, an autonomous PR review and
code-patching agent (LangGraph reviewer → ReAct patcher → Docker test runner with a self-correction loop).

- `main` holds the clean base: schema, seed data and tests.
- PR #1 adds user lookups and order reporting. It's the PR prbot reviews.

```bash
pip install pytest
pytest
```
