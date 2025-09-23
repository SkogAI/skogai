# Suggested Commands

## Environment Setup
```bash
# Load environment variables via direnv
direnv allow

# Or manually export environment
eval "$(skogcli config export-env --namespace skogai,claude)"
```

## Git Operations
```bash
# Check status
git status

# Update submodules
git submodule update --init --recursive

# Switch branches
git checkout develop
git checkout master
```

## File Navigation
```bash
# List all files including hidden
ls -la

# Navigate to AI shared folder
cd .skogai/

# View Claude configuration
cat CLAUDE.md
```

## System Commands (Linux)
- `ls` - list directory contents
- `cd` - change directory
- `cat` - display file contents
- `pwd` - print working directory
- `mkdir` - create directory
- `touch` - create empty file
- `rm` - remove files (use with caution)

## Important Notes
- Do NOT use find or grep unless absolutely necessary
- Never retry failed commands - inform skogix instead
- This project has no build/test/lint commands as it's configuration-only