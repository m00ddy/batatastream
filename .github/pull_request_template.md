<!-- PR title must be a conventional commit: feat(ingest): add JBB loader
     types: feat, fix, docs, chore, test, refactor, perf, ci
     areas: ingest, ml, serving, common, report, infra -->

## What
<!-- One or two sentences. What does this PR change? -->

## Why
<!-- The task, issue, or reason. Link the issue if there is one: Closes #12 -->

## How tested
<!-- Tests added or run, commands, screenshots, sample output.
     If there are no automated tests, say exactly how you verified it. -->

## Checklist
- [ ] Branch is from the latest `main` and does one task
- [ ] Only touches my own folder (or this is a separate, agreed PR for `common/`, schema, or interfaces)
- [ ] Tests added or a verification is described above
- [ ] `ruff check .`, `ruff format --check .` and `pytest` pass locally
- [ ] No secrets, `.env` files, datasets, or model weights committed
- [ ] No new heavy dependency or version bump without asking the team first
- [ ] Under ~400 changed lines (or I explain why above)
