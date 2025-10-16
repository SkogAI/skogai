# Claude Workflow Configuration

This directory contains all configuration files that control Claude Code's behavior, permissions, and workflows.

## Quick Start

### For Users

**Tell Claude to change something, and it will modify these files directly.**

Examples:
- "Add docker permissions"
- "Be more verbose in explanations"
- "Create a /deploy command"
- "Enable TTS notifications"
- "Block commands that delete files in /tmp"

### For Claude

**You have full permission to modify all files in this directory.** When the user asks you to change your workflow, behavior, or configuration:

1. **Read** the relevant file with `view`
2. **Edit** it with `str_replace` or `create`
3. **Test** if applicable (hooks can be tested with JSON input)
4. **Commit** the change with a descriptive message

See `CLAUDE.md` for comprehensive documentation.

## Directory Structure

```
claude/
├── README.md                          # This file - quick reference
├── CLAUDE.md                          # Hook-specific documentation
├── WORKFLOW_MODIFICATION_EXAMPLES.md  # 8 practical examples
├── settings.json                      # Core configuration (permissions, hooks, flags)
├── output-styles/                     # Behavioral guidelines
│   └── regular.md                     # Default behavior and principles
├── commands/                          # Custom slash commands
│   ├── add.md                         # /add command
│   ├── commit.md                      # /commit command
│   └── git-flow.md                    # /git-flow command
├── hooks/                             # Lifecycle event hooks
│   ├── CLAUDE.md                      # Hook documentation
│   ├── session_start.py               # Session initialization
│   ├── user_prompt_submit.py          # Prompt preprocessing
│   ├── pre_tool_use.py                # Tool validation (safety)
│   ├── post_tool_use.py               # Tool result processing
│   ├── notification.py                # User notifications (TTS)
│   ├── stop.py                        # Session cleanup
│   ├── subagent_stop.py               # Subagent completion
│   ├── pre_compact.py                 # Context compaction handling
│   └── utils/                         # Shared utilities
│       ├── llm/                       # LLM integrations
│       │   ├── oai.py                 # OpenAI
│       │   ├── anth.py                # Anthropic
│       │   └── ollama.py              # Local Ollama
│       └── tts/                       # Text-to-speech
│           ├── elevenlabs_tts.py      # ElevenLabs
│           ├── openai_tts.py          # OpenAI TTS
│           └── pyttsx3_tts.py         # Local TTS
├── status_lines/                      # Status line generators
│   ├── status_line_v2.py
│   ├── status_line_v3.py
│   └── status_line_v4.py
└── prompt-engineering.md              # Advanced prompting techniques

```

## Key Files

### settings.json
Core configuration controlling:
- **Permissions** - What tools and commands Claude can use
- **Hooks** - Lifecycle event handlers
- **Flags** - Feature toggles like `alwaysThinkingEnabled`

### output-styles/regular.md
Behavioral guidelines defining:
- Core operating principles
- Response patterns
- Prohibited behaviors
- Success metrics

### commands/*.md
Custom slash commands that users can invoke.
Each file defines a workflow with allowed tools and instructions.

### hooks/*.py
Python scripts that run at specific lifecycle points:
- Before/after tool use
- On session start/stop
- On user prompts
- On notifications

## Common Modifications

### Add a Tool Permission
```json
// In settings.json, add to "allow" array:
"Bash(docker:*)"
```

### Create a Custom Command
```bash
# Create claude/commands/mycommand.md
---
description: My custom command
allowed-tools: Bash(git:*), Write
---
# Instructions here
```

### Enable Hook Flags
```json
// In settings.json, modify hook command:
"command": "uv run /path/to/hook.py --flag"
```

### Modify Behavior
```markdown
// In output-styles/regular.md:
- **NEW_PRINCIPLE** - Description here
```

## Testing

### Test a Hook
```bash
echo '{"session_id": "test", "tool_name": "Bash"}' | \
  uv run claude/hooks/pre_tool_use.py
```

### Test Settings Validity
```bash
python -m json.tool claude/settings.json
```

### View Recent Logs
```bash
ls -lt ~/.claude/logs/
tail -f ~/.claude/logs/user_prompt_submit.json
```

## Documentation

- **`../CLAUDE.md`** - Repository-level guidance (comprehensive workflow documentation)
- **`CLAUDE.md`** - Hook architecture and development
- **`WORKFLOW_MODIFICATION_EXAMPLES.md`** - 8 practical examples
- **`prompt-engineering.md`** - Advanced prompting techniques

## Safety

Claude has safety guards in `hooks/pre_tool_use.py`:
- Blocks dangerous `rm` commands
- Blocks access to `.env` files (secrets)
- Can be extended with custom validation

## Emergency Revert

```bash
# Revert all changes in claude/
git checkout HEAD -- claude/

# Revert specific file
git checkout HEAD -- claude/settings.json
```

## See Also

- Main documentation: `../CLAUDE.md`
- Examples: `WORKFLOW_MODIFICATION_EXAMPLES.md`
- Hook details: `hooks/CLAUDE.md`
