# Skogai Project Overview

## Purpose
Skogai is a meta-project for AI agent coordination and configuration. It serves as a centralized hub for AI agents (including Claude, Serena MCP, and potentially others) to share project-specific information and coordinate activities.

## Key Components
- **CLAUDE.md**: Main configuration file for Claude AI with project-specific instructions
- **.skogai/**: Shared folder for all AI agents containing:
  - Project documentation
  - User instructions (docs/user.md)
  - Todo lists
  - Claude-specific configurations
  
## Integration Points
The project is designed to integrate:
- Serena MCP server for code analysis
- Skogai-memory MCP for persistent memory
- Skogai-reasoning MCP for enhanced thinking capabilities

## Git Structure
- Uses git submodules (`.skogai` is a submodule from https://github.com/skogai/skogai.git)
- Main branch: master
- Development branch: develop

## Important Instructions
- Never retry commands that fail - inform skogix instead
- Avoid using find/grep unless absolutely necessary
- Follow CLAUDE.md instructions strictly