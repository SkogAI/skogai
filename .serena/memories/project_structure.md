# Project Structure

## Root Directory
```
/home/skogix/dev/skogai/
├── CLAUDE.md          # Main Claude AI configuration (refers to .skogai)
├── README.md          # Project readme (minimal)
├── .envrc             # direnv configuration for environment
├── .gitignore         # Git ignore file
├── .gitmodules        # Git submodules configuration
│
├── .skogai/           # [SUBMODULE from github.com/skogai/.skogai]
│   ├── README.md      # Submodule readme
│   ├── todo           # Skogix's todo list
│   ├── docs/          # Documentation
│   │   ├── user.md    # Skogix's introduction
│   │   └── claude/    # Claude-specific docs
│   │       └── examples/
│   │           └── current-state-answer.md
│   ├── .gitignore     # Submodule gitignore
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

## Key Files in .skogai
- **todo**: Skogix's task list for the project
- **docs/user.md**: Introduction from skogix about communication style and preferences
- **docs/claude/**: Documentation specific to Claude setup

## File References in CLAUDE.md
- @CLAUDE.md - The main Claude configuration file
- @.skogai/ - Shared folder for all AI agents
- @.skogai/docs/user.md - Skogix's introduction
- @.skogai/todo - Skogix's todo list