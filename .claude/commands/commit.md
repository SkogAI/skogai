---
allowed-tools: Read, Bash(git:*)
description: Stage and commit changes with automatic status checking
argument-hint: [commit message]
model: claude-3-5-sonnet-20241022
---

# Git Commit Command

Handles the complete git staging and commit workflow.

## Current Status
!`git status --porcelain`

## Recent Commits
!`git log --oneline -5`

## Instructions

1. Check the current git status above
2. If there are unstaged changes, stage them with `git add`
3. Create a commit with the provided message: $ARGUMENTS
4. If no message provided, generate one based on the changes
5. Show the final status after commit

Use standard git workflow:
- `git add` for staging
- `git commit -m` for committing
- Follow the project's commit message conventions if visible from recent commits