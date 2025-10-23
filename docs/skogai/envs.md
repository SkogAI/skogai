---
title: skogai/environment-variables
description: Comprehensive overview of SkogAI's environment variable management system using namespaces and JSON configuration.
---

# SkogAI Environment Variable Management

SkogAI uses a sophisticated namespace-based system for managing environment variables that bridges JSON configuration storage with shell environment variables.

## Core Architecture

### Storage: `config/config.json`

Environment variables are stored in JSON format, organized by namespace:

```json
{
  "skogai": {
    "env": {
      "EDITOR": "nvim",
      "PAGER": "cat",
      "SKOGAI_CONTEXT": "$SKOGAI/skogcontext"
    }
  },
  "claude": {
    "env": {
      "PAGER": "bat",
      "LLM_OUTPUT": "./tmp/llm-output",
      "SKOGAI_AGENT_NAME": "claude"
    }
  }
}
```

### Loading: `skogcli config export-env`

The bridge between JSON storage and shell environment is `skogcli config export-env`:

```bash
# Load environment variables from a specific namespace
eval "$(skogcli config export-env --namespace skogai)"

# This generates and evaluates export statements like:
# export EDITOR=nvim
# export PAGER=cat
# export SKOGAI_CONTEXT=/home/skogix/skogai/skogcontext
```

## Namespace Design

### Agent-Specific Contexts

Different agents and services get their own environment contexts:

- **`skogai`** - Core system variables, paths, and general settings
- **`claude`** - Claude Code specific settings (different pager, output paths)
- **`goose`** - Goose agent specific configuration
- **`github`** - GitHub tokens and API settings
- **`supabase`** - Database credentials and connection settings
- **`cloudflare`** - API keys and zone configurations

### Context Isolation

This design allows:

- **Isolated environments** per agent/service
- **Dynamic loading** of relevant variables only
- **Security separation** of credentials by context
- **Clean environment switching** between different operations

## Usage Patterns

### Shell Startup

Load core system variables in your shell startup files:

```bash
# ~/.bashrc or similar
export SKOGAI="/home/skogix/skogai"
eval "$(skogcli config export-env --namespace skogai)"
```

### Dynamic Context Switching

Load agent-specific environments as needed:

```bash
# When working with Claude Code
eval "$(skogcli config export-env --namespace claude)"
echo $PAGER  # Now "bat" instead of "cat"

# When doing GitHub operations
eval "$(skogcli config export-env --namespace github)"
# Now $GITHUB_TOKEN is available
```

### Multiple Context Loading

Load multiple namespaces for complex operations:

```bash
# Load both core and agent-specific variables
eval "$(skogcli config export-env --namespace skogai)"
eval "$(skogcli config export-env --namespace claude)"
```

## Variable Expansion

The system supports variable expansion within config.json:

```json
{
  "skogai": {
    "env": {
      "SKOGAI_CONTEXT": "$SKOGAI/skogcontext",
      "SKOGAI_CONTEXT_UPDATE": "$SKOGAI/skogcontext/update"
    }
  }
}
```

When exported, `$SKOGAI` is expanded to `/home/skogix/skogai`.

## Management Commands

### View Configuration

```bash
# View a specific namespace
skogcli config get claude.env

# View all namespaces
skogcli config get
```

### Export Variables

```bash
# Generate export statements (don't evaluate)
skogcli config export-env --namespace skogai

# Load into current shell
eval "$(skogcli config export-env --namespace skogai)"
```

### Current Environment

```bash
# Check what's currently loaded
env | grep SKOGAI
env | grep CLAUDE
```

## Security Considerations

- **Credential isolation** - API keys separated by service namespace
- **Selective loading** - Only load variables needed for current context
- **Version control** - Automatic backup system in `config/backups/`
- **Access control** - File permissions on config.json control access

## Integration with Tools

### Claude Code

Claude Code tools (like Bash) inherit whatever environment variables are loaded in the shell session. To ensure Claude gets its preferred settings:

```bash
eval "$(skogcli config export-env --namespace claude)"
```

### Argc Commands

The argc CLI system can bind to specific environments through the configuration system.

### Agent Workflows

Different AI agents automatically get their appropriate environment context loaded when invoked through the SkogAI system.

## Best Practices

1. **Load core `skogai` namespace** in shell startup
2. **Load agent-specific namespaces** when switching contexts
3. **Use meaningful namespace names** that match their purpose
4. **Group related variables** in the same namespace
5. **Backup configurations** before major changes
6. **Test variable expansion** after configuration changes

This system provides the flexibility of traditional environment variables with the organization and management benefits of structured configuration.
