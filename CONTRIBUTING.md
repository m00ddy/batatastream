# Contributing

Short version: branch from `main`, one task per branch, PR into `main`, mo reviews,
squash merge. Full walkthrough in [docs/workflow.md](docs/workflow.md).

## Rules
1. **Never push to `main`.** It is protected; everything goes through a PR.
2. **One task per branch**, created from the latest `main`.
3. **Branch names**: `<type>/<area>-<what>`
   - types: `feat`, `fix`, `docs`, `chore` (also `test`, `refactor`)
   - areas: `ingest`, `ml`, `serving`, `common`, `report`, `infra`
   - examples: `feat/ingest-jbb-loader`, `fix/ml-label-leak`, `docs/report-abstract`
4. **Edit only your own folder** (`ingest/` A, `ml/` B, `serving/` C).
5. **Shared things need a separate PR and agreement**: anything in `common/`, the data
   schema, Kafka topic names or message formats, Parquet layouts, or function signatures
   other folders call. Open an issue or message the group first, then a PR that does only
   that change. mo approves it once all three have agreed.
6. **Every PR has tests or a written verification** in the "How tested" section.
7. **No secrets or data in git**: no `.env`, tokens, datasets, Parquet files, or model
   weights. Add a download script under `scripts/` instead.
8. **Ask before big dependency changes**: new heavy packages, Spark/Python/Kafka version
   bumps, or new services in docker-compose.
9. **Keep PRs small**: about 400 changed lines max. Split bigger work.

## PR titles and commits
PRs are squash merged, so the **PR title becomes the commit on `main`**. Use
[conventional commits](https://www.conventionalcommits.org/):
```
feat(ingest): add WildJailbreak loader
fix(ml): drop duplicate rows before train/test split
docs(report): draft implementation section
chore(infra): pin pyspark 3.5.3
```
CI rejects titles that do not match. Commits inside your branch can be anything.

## Review
- mo (@m00ddy) is the code owner and must approve every PR.
- Also tag the owner of the folder you touched.
- mo is the only approver. mo merges his own PRs himself once CI is green.
- Reviewers answer within a day. Small PRs get reviewed faster.

## Before opening a PR
```bash
git fetch origin && git rebase origin/main
ruff check . && ruff format .
pytest
```
