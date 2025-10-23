---
description: Check if code changes have corresponding documentation updates
allowed-tools: Bash(git:*), Read, Grep
---

# Documentation Check Command

Check if recent code changes have corresponding documentation updates.

## Process

1. Get recently modified files from git:
   - Run `git diff --name-only HEAD~1..HEAD` to see changed files
   - Run `git diff HEAD~1..HEAD` to see what changed

2. Identify if documentation might be needed:
   - New features or API changes
   - Modified public interfaces
   - Changed configuration options
   - Updated CLI commands

3. Check for documentation:
   - Look for related .md files in docs/
   - Check README.md for updates
   - Look for inline code comments

4. Report findings:
   - List code changes that may need docs
   - List existing documentation found
   - Suggest specific documentation updates needed

## Output Format

```
📝 Documentation Check Results

Changed Files:
- file1.js (added new function)
- file2.py (modified API endpoint)

Documentation Status:
✅ docs/api.md - Updated
❌ README.md - Not updated (should document new feature)
⚠️  Missing: docs/new-feature.md

Recommendations:
1. Update README.md to mention new feature
2. Create docs/new-feature.md with usage examples
3. Add inline comments to complex logic in file1.js
```

## Usage

```bash
/check-docs
```

This will analyze the most recent commit for documentation coverage.
