# Claude

## session start

created at session start

### env - environment info (working directory, git status, platform, os, date)

<example>
  <env>
  Working directory: /tmp
  Is directory a git repo: Yes
  Platform: linux
  OS Version: Linux 6.17.5-arch1-1
  Today's date: 2025-10-31
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

## SPAM

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
   git commit -m "$(cat <<'EOF'
   Commit message here.
   EOF
   )"
   ```

   - run `git status` after to verify

4. **pre-commit hook handling:**
   - if hook modifies files, check safe to amend:
     - check authorship: `git log -1 --format='%an %ae'`
     - check not pushed: `git status` shows "Your branch is ahead"
   - if both true: amend commit
   - otherwise: create NEW commit (never amend other developers' commits)

**rules:**

- NEVER update git config
- NEVER run destructive commands (push --force, hard reset) unless explicitly requested
- NEVER skip hooks (--no-verify, --no-gpg-sign) unless explicitly requested
- NEVER force push to main/master, warn if user requests it
- avoid `git commit --amend` unless user explicitly requested OR adding pre-commit hook edits
- NEVER commit unless user explicitly asks
- NEVER use `-i` flag (interactive commands not supported)
- no empty commits if no changes

### github pr creation workflow

when user asks to create a PR:

1. **parallel info gathering:**
   - `git status` - see untracked files
   - `git diff` - see staged/unstaged changes
   - check if branch tracks remote and is up to date
   - `git log` and `git diff [base-branch]...HEAD` - understand FULL commit history from branch divergence

2. **analyze ALL commits:**
   - look at ALL commits that will be in PR (not just latest)
   - draft PR summary

3. **create PR:**
   - create branch if needed
   - push to remote with -u if needed
   - create PR using heredoc:

   ```bash
   gh pr create --title "the pr title" --body "$(cat <<'EOF'
   ## Summary
   <1-3 bullet points>

   ## Test plan
   [Bulleted markdown checklist of TODOs for testing the pull request...]
   EOF
   )"
   ```

   - return PR URL

**rules:**

- DO NOT use TodoWrite or Task tools during this workflow
- must analyze ALL commits, not just the latest one

### github operations

- use `gh` command via Bash tool for ALL github tasks (issues, PRs, checks, releases)
- if given github URL, use `gh` command to get info
- `Bash(gh:*)` and `Bash(git:*)` are auto-approved (no user confirmation needed)
