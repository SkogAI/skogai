# Code Style and Conventions

## General Principles
- This is primarily a configuration/documentation project, not a code project
- Minimal actual code (only dummy bash file for Serena activation)

## Documentation Style
- Use Markdown for all documentation
- Clear hierarchical structure with headers
- Include purpose and context for all configurations

## AI Instructions Format
- Instructions in CLAUDE.md should be clear and imperative
- Use @ prefix for file references (e.g., @CLAUDE.md, @.skogai/)
- Use [@todo:] format for pending integrations

## File Organization
- Project-specific AI configurations in root (CLAUDE.md)
- Shared AI agent information in .skogai/
- Tool configurations in respective dotfiles/folders (.serena/, .envrc)

## Git Conventions
- Main branch: master
- Development branch: develop
- Submodules for shared components