# Git workflow

We use **GitHub Flow**: `main` is always working, every change is a short-lived branch
merged through a pull request.

## Day to day
```bash
# 1. Start from the latest main
git switch main
git pull

# 2. Create a branch for ONE task
git switch -c feat/ingest-jbb-loader

# 3. Work and commit as often as you like
git add ingest/
git commit -m "wip: load JBB csv"

# 4. Keep up to date with main
git fetch origin
git rebase origin/main          # fix conflicts, then: git rebase --continue

# 5. Check locally
ruff check . && ruff format . && pytest

# 6. Push and open a PR
git push -u origin feat/ingest-jbb-loader
#    then open the PR on GitHub, fill in the template, title it
#    "feat(ingest): add JBB-Behaviors loader"

# 7. After it is squash merged, clean up
git switch main && git pull
git branch -d feat/ingest-jbb-loader
```

## Lifecycle of a PR
1. Open the PR (as a draft if it is not ready).
2. CI runs: PR title check, ruff lint and format, pytest. A size warning appears over 400 lines.
3. mo is requested automatically. Tag the folder owner too.
4. Address comments with new commits on the same branch (no force push needed).
5. When CI is green and mo approved, mo squash merges. The branch is deleted automatically.

## Changing shared things
`common/`, the schema, Kafka topics and message formats, Parquet layouts, and
cross-folder interfaces:
1. Write the proposal in an issue or the group chat.
2. Get a yes from the other two.
3. Open a PR that changes only that (`feat(common): add source_dataset column to schema`).
4. mo approves and merges once all three agreed. Others rebase their branches afterwards.

## Branch lifetime
Aim for branches that live 1 to 3 days. If a task is bigger, split it into
several PRs that each leave `main` working.

## Timeline
- Nov 25 to 26: setup and theory, no implementation.
- From Nov 27: implementation.
- Target: everything finished by Dec 24 (official deadline is in January).
