---
title: user-guide
permalink: skogix/user-guide
description: definitions of common terms used by skogix or related in relation to SkogAI
---

# claude

## session start

created at session start

### env - environment info (working directory, git status, platform, os, date)

<example>
  <env>
  working directory: /tmp
  is directory a git repo: yes
  platform: linux
  os version: linux 6.17.5-arch1-1
  today's date: 2025-10-31
  </env>
</example>

### available_skills - the skills list from when this conversation started, containing

- user skills (algorithmic-art, artifacts-builder, etc.)
- managed skills (gh-tool at that time)
- plugin skills (example-skills:\*)

### budget:token_budget - token usage tracking

most probably until exit and getting back to main session?

### tool:auto_approval - which tools have auto approval enabled

basic permissions might update this?

## spam

<system-reminder> - dynamic blocks that appear in tool results or user messages with contextual info

## skills

## git and github workflows

these are built into claude code's instructions - prescriptive workflows i'm supposed to follow.

### git commit workflow

when user asks to create a commit:

1. **parallel info gathering:**
   - `git status` - see untracked files
   - `git diff` - see staged/unstaged changes
   - `git log` - understand commit message style

2. **analyze and draft:**
   - summarize nature of changes (feature/fix/refactor/etc)
   - don't commit secrets (.env, credentials.json)
   - draft 1-2 sentence commit message (focus on "why" not "what")

3. **commit:**
   - add relevant files to staging
   - create commit with heredoc format:

   ```bash
   git commit -m "$(cat <<'eof'
   commit message here.
   eof
   )"
   ```

   - run `git status` after to verify

4. **pre-commit hook handling:**
   - if hook modifies files, check safe to amend:
     - check authorship: `git log -1 --format='%an %ae'`
     - check not pushed: `git status` shows "your branch is ahead"
   - if both true: amend commit
   - otherwise: create new commit (never amend other developers' commits)

**rules:**

- never update git config
- never run destructive commands (push --force, hard reset) unless explicitly requested
- never skip hooks (--no-verify, --no-gpg-sign) unless explicitly requested
- never force push to main/master, warn if user requests it
- avoid `git commit --amend` unless user explicitly requested or adding pre-commit hook edits
- never commit unless user explicitly asks
- never use `-i` flag (interactive commands not supported)
- no empty commits if no changes

### github pr creation workflow

when user asks to create a pr:

1. **parallel info gathering:**
   - `git status` - see untracked files
   - `git diff` - see staged/unstaged changes
   - check if branch tracks remote and is up to date
   - `git log` and `git diff [base-branch]...head` - understand full commit history from branch divergence

2. **analyze all commits:**
   - look at all commits that will be in pr (not just latest)
   - draft pr summary

3. **create pr:**
   - create branch if needed
   - push to remote with -u if needed
   - create pr using heredoc:

   ```bash
   gh pr create --title "the pr title" --body "$(cat <<'eof'
   ## summary
   <1-3 bullet points>

   ## test plan
   [bulleted markdown checklist of todos for testing the pull request...]
   eof
   )"
   ```

   - return pr url

**rules:**

- do not use todowrite or task tools during this workflow
- must analyze all commits, not just the latest one

### github operations

- use `gh` command via bash tool for all github tasks (issues, prs, checks, releases)
- if given github url, use `gh` command to get info
- `bash(gh:*)` and `bash(git:*)` are auto-approved (no user confirmation needed)
