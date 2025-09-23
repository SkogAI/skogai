# Skogai HQ - Project Overview

## THIS IS HEADQUARTERS
We are in the main **skogai** repository - the orchestration hub for the entire ecosystem. There is only ONE of these.

## Architecture Duality

### skogai (HQ - where we are now)
- The orchestration hub, the conductor
- Receives todos from ALL projects via their .skogai submodules
- Converts one-liner todos into actionable work plans
- Delegates work to specialized projects
- Confirms implementations via PRs/diffs
- Maintains the big picture of all skogai projects

### .skogai (the dotfiles - embedded everywhere)
- Git submodule that exists in EVERY skogai project
- Like ~/.config for home directories
- Contains minimal config and a todo dump
- Provides a backchannel to HQ
- Workers just dump "shit we want done" and move on

## Core Responsibility
As HQ, this project:
- Takes raw todos from the field
- Asks clarifying questions
- Creates detailed work plans
- Orchestrates work across specialized projects
- Tracks overall ecosystem progress
- Maintains cross-project standards

## Information Flow
```
[Project A] → dumps todo → [.skogai/todo] ↗
[Project B] → dumps todo → [.skogai/todo] → [SKOGAI HQ]
[Project C] → dumps todo → [.skogai/todo] ↘
                                               ↓
                                    [Orchestration & Planning]
                                               ↓
                            [Delegate to specialized projects]
                                               ↓
                                        [Confirm via PRs]
```

## Current Integration
- ✅ Serena MCP for memory management at HQ
- ✅ .skogai submodule structure defined
- ⏳ Other specialized projects to be integrated