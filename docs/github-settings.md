# GitHub settings for mo to enable

These cannot be set from files in the repo. Do them once after creating the repo.

> Make the repo **public** first: branch protection is free on public repos. On a private repo it needs GitHub Pro,
> which is free with the GitHub Student Developer Pack (education.github.com/pack).

## 1. Collaborators
Settings > Collaborators > Add people: add @OmarMahmoud1024 and @Ali-1a with **Write**
role (not Admin). They must accept the email invite.

## 2. Merge options
Settings > General > Pull Requests:
- [x] Allow squash merging, default message: **Pull request title and description**
- [ ] Allow merge commits (off)
- [ ] Allow rebase merging (off)
- [x] Always suggest updating pull request branches
- [x] Automatically delete head branches

## 3. Protect `main`
Settings > Branches > Add branch protection rule, pattern `main`:
- [x] Require a pull request before merging
  - Required approvals: **1**
  - [x] Dismiss stale pull request approvals when new commits are pushed
  - [x] Require review from Code Owners
- [x] Require status checks to pass before merging
  - [x] Require branches to be up to date before merging
  - Add checks (they appear after CI has run once on a PR):
    `Lint (ruff)`, `Tests (pytest)`, `PR title and size`
- [x] Require conversation resolution before merging
- [x] Require linear history
- [x] Do not allow force pushes (Allow force pushes unchecked)
- [x] Do not allow deletions (Allow deletions unchecked)
- [ ] Do not allow bypassing the above settings: **leave this off**

Why leave bypass available: you are the only code owner, and GitHub never counts an
author's own approval. Admin bypass lets you merge your own PRs once CI is green (tick
"Merge without waiting for requirements"). Teammates have Write, not Admin, so they
cannot bypass and always need your approval.

## 4. Actions
Settings > Actions > General:
- Actions permissions: Allow all actions
- Workflow permissions: **Read repository contents** (default)

## Known limits
- Agreement on `common/` changes is a team rule, not enforced by GitHub.
- The 400-line limit is a CI warning, not a block.
