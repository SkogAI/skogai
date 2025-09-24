---
allowed-tools: Read, Edit, Write, Bash(git:*), TodoWrite
description: Stage git changes, update documentation, and prepare for session handover
argument-hint: [summary of work completed]
---

# End Session Command

Prepares the repository for session handover by:

1. Staging current changes
2. Updating documentation where affected
3. Creating handover notes
4. Leaving changes unstaged for review

## Current Git Status

!`git status --porcelain`

## What Changed (Unstaged)

!`git diff`

## What Changed (Staged)

!`git diff --cached`

## Recent Commits

!`git log --oneline -5`

## Project Documentation

@CLAUDE.md
@docs/handover.md

## Instructions

1. **Review Changes**: Examine the git diff output above to understand what was modified
2. **Stage Changes**: Use `git add` to stage relevant changes (after reviewing the actual diffs)
3. **Update Documentation**:
   - Update CLAUDE.md if any new patterns/instructions emerged
   - Create/update docs/handover.md with session summary and next steps
4. **Prepare Handover**: Document:
   - What was accomplished: $ARGUMENTS
   - What remains to be done
   - Any blockers or considerations
   - Context for the next session
5. **Leave Unstaged**: After documentation updates, leave all changes unstaged for review
6. **Show Final Status**: Display git status to confirm all changes are ready for review

Follow the established commit conventions and documentation patterns from the repository.
