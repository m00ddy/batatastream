# Rules for AI coding assistants in this repo

You are helping one member of a 3-person student team build a Spark pipeline that
classifies adversarial prompts (UPB Big Data course). Stack: Python 3.11, PySpark and
MLlib, Kafka, Parquet, docker-compose, Postgres, Streamlit or Grafana. Each person owns
one folder: `ingest/` (A, mo), `ml/` (B), `serving/` (C). `common/` is shared.

Ask your human which role they are before you change anything, if you don't know.

## Hard rules
1. **Never push to `main`, never merge, never force push** to a branch you did not create.
2. **Branch from the latest `main`, one task per branch.** Name it
   `<feat|fix|docs|chore>/<ingest|ml|serving|common|report|infra>-<short-what>`,
   e.g. `feat/ml-tfidf-features`. Run `git fetch origin && git switch -c <name> origin/main`.
3. **Edit only your human's own folder** (plus `tests/` inside it).
4. **Do not change `common/`, the data schema, Kafka topics or message formats, Parquet
   layouts, or functions other folders call** inside a normal PR. If such a change is
   needed, stop and tell your human: it needs agreement from all three first, then a
   separate PR that does only that change.
5. **Every PR has tests or a stated verification.** Add pytest tests in `<folder>/tests/`.
   Mark tests that start Spark with `@pytest.mark.spark` and use `master("local[1]")`.
   If something can't be tested automatically, write the exact manual steps in the PR.
6. **Never commit secrets or data.** No `.env`, tokens, keys, datasets, `.parquet`,
   `.csv`, `.jsonl`, or model files. Write or update a download script in `scripts/`.
   Read secrets from environment variables; add new names to `.env.example`.
7. **Ask your human before** adding a dependency, bumping any version (Python, Spark,
   Kafka, packages), adding a docker-compose service, or deleting files you did not write.
8. **Keep PRs small: about 400 changed lines max.** If a task is bigger, propose a split.

## Before you open a PR
- `git fetch origin && git rebase origin/main`
- `ruff check . && ruff format .` must pass
- `pytest` must pass
- PR title is a conventional commit: `feat(ingest): add JBB-Behaviors loader`
  (types: feat, fix, docs, chore, test, refactor, perf, ci)
- Fill in every section of the PR template: What, Why, How tested, Checklist
- mo (@m00ddy) is requested automatically and is the only approver

## Style
- Python 3.11, type hints on public functions, docstrings on modules and public functions.
- Line length 100, ruff handles formatting and import order.
- Prefer Spark DataFrame APIs over Python UDFs; avoid `collect()` on large data.
- Paths and settings come from config or env vars, never hardcoded to one laptop.
- Keep notebooks out of `main` unless they are cleaned and small.

## When unsure
Stop and ask your human. Do not guess at shared interfaces, do not invent dataset
fields, and do not "fix" other people's folders.
