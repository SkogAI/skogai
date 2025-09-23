# Project Structure

## Root Directory
```
/home/skogix/dev/skogai/
├── CLAUDE.md          # Main Claude AI configuration
├── README.md          # Project readme (minimal)
├── .envrc             # direnv configuration for environment
├── .gitignore         # Git ignore file
├── .gitmodules        # Git submodules configuration
│
├── .skogai/           # [SUBMODULE] Shared AI agent folder
│   ├── README.md      # Submodule readme
│   ├── claude/        # Claude-specific shared data
│   └── .git           # Submodule git data
│
├── .serena/           # Serena MCP configuration
│   └── project.yml    # Serena project config (auto-generated)
│
├── .claude/           # Claude's private folder
│
├── .aider.tags.cache.v4/  # Aider tool cache
├── .aider.chat.history.md  # Aider chat history
│
└── .git/              # Git repository data
```

## Key Directories
- **.skogai/**: Central hub for AI agent coordination (git submodule)
- **.serena/**: Serena MCP server configuration
- **.claude/**: Claude's private workspace

## Important Files
- **CLAUDE.md**: Primary configuration and instructions for Claude
- **.envrc**: Environment setup via direnv/skogcli
- **.gitmodules**: Defines .skogai as submodule from GitHub