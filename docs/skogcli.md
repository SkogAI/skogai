# SkogCLI

**Core Philosophy**: Unified command-line interface for the SkogAI ecosystem with integrated memory, scripting, configuration, and agent management.

## Architecture

- **Configuration-driven**: Central `./config/config.json` manages environments, API keys, and agent settings
- **Script ecosystem**: `./scripts/` directory with metadata tracking and template system
- **Memory integration**: Direct interface to basic-memory MCP for knowledge management
- **Agent orchestration**: Multi-agent system with configurable models and prompts

## Main Commands

### `skogcli memory`
Knowledge management with basic-memory integration:
- `write/read/search/list` - Core knowledge operations
- `sync/status` - Database synchronization and project health
- `bm` - Direct passthrough to basic-memory commands

### `skogcli config`
Sophisticated environment and configuration management built on JSON key-value storage:

**Basic Operations**:
- `show/get/set/edit` - Configuration CRUD operations with dotted key notation
- `backup/restore` - Configuration versioning and safety
- `list --env-only` - View all environment variables across namespaces

**Environment Management**:
- `export-env --namespace <ns1,ns2>` - Export environment variables with namespace layering
- Hierarchical override system (later namespaces override earlier ones)
- Per-directory environment switching via `.envrc` + `direnv`

**Key Patterns**:
```bash
# Set any configuration value
skogcli config set claude.env.PAGER "bat"
skogcli config set supabase.env.DATABASE_URL "postgresql://..."

# Get specific namespace configuration
skogcli config get claude.env
skogcli config get cloudflare

# Export layered environments for development contexts  
skogcli config export-env --namespace skogai,claude,supabase
```

**Directory-based Workflows**:
Create `.envrc` files with context-specific namespace combinations:
- Supabase projects: `eval "$(skogcli config export-env --namespace skogai,claude,supabase)"`
- Cloudflare projects: `eval "$(skogcli config export-env --namespace skogai,agent,cloudflare)"`
- Agent-specific work: `eval "$(skogcli config export-env --namespace skogai,goose)"`

### `skogcli script`
Script lifecycle management with automatic metadata tracking:

**Basic Operations**:
- `list/run/info` - List available scripts, execute with args/stdin, view usage metadata
- `create/edit/remove` - Script lifecycle management with template support
- `copy/import/export` - Script sharing and duplication

**AI-Powered Features**:
- `generate <name> <description>` - AI script creation with model selection
- `code <name> --content "..."` - Direct content replacement without editor
- `transform <name> -p "pattern" -r "replacement"` - Regex-based script modification

**Advanced Operations**:
- `batch/search` - Multi-script operations and content search
- `templates` - Available script scaffolding patterns
- Automatic usage tracking in `script_metadata.json` (run_count, last_run, last_updated)

**Example Usage**:
```bash
# Basic script execution
cat file.txt | skogcli script run token
skogcli script run skogai-test arg1 arg2

# AI-powered script creation and modification
skogcli script generate backup "create backup of directory with timestamp"
skogcli script code backup --content "#!/bin/bash\necho 'new script'"
skogcli script transform token -p "char_count" -r "character_count"
```

### `skogcli agent`
Multi-agent orchestration:
- `send/list/create` - Agent communication and management
- `get/set` - Agent configuration
- Integration with various AI models and custom prompts

### `skogparse`
Unified execution language that extends JSON with live command execution:

**Core Syntax**:
- `[@script:arg1:arg2:...]` - Execute skogcli scripts with arguments
- `$ namespace.key` - Query skogcli configuration values
- `[@guid:command:args]` - Stateful command execution with unique identifiers
- `[@toggle:guid]` - Control command execution state (active/dormant)

**JSON Compatibility**:
- Full JSON support: `[52.0, "string", true, {"key": "value"}]`
- Mixed notation: `[[@script:args], $ config.key, "static value"]`
- Structured output: All results typed as `{"type": "string|number|bool|array", "value": ...}`

**Dynamic Features**:
- **Live references**: `[@file:"/path/to/file"]` always returns current content
- **Recursive parsing**: Config values can contain skogparse commands (`$.claude.random = "[@rand]"`)
- **Execution control**: Toggle commands on/off without losing references
- **Self-updating context**: Message history remains current through live execution

**Example Usage**:
```bash
# Mixed command execution
skogparse '[[@skogai-test:a:b:c], $ claude.env.PAGER]' | jq

# Dynamic configuration values
skogparse '$ claude.random'  # Executes embedded [@rand] command

# Live file references  
skogparse '[@file:"/home/skogix/skogai/README.md"]'

# Standard JSON with live data
skogparse '[52.0, [@rand], $ claude.hello, true]'
```

**Integration Vision**:
- Parse all SkogAI messages and documents with live command execution
- Create self-updating documentation and conversation history
- Enable executable configuration files and dynamic data structures

## Key Features

- **Environment isolation**: Per-agent environment variables and configurations
- **Script templates**: Standardized Python/shell script scaffolding
- **Metadata tracking**: Usage statistics and script versioning in `script_metadata.json`
- **MCP integration**: Seamless connection to 100+ MCP tools via nvim-mcp-hub
- **API key management**: Centralized credential handling across services

## Configuration Structure

Built on simple JSON key-value storage (`./config/config.json`) with powerful namespace system:

**Core Namespaces**:
- `skogai.env.*`: Base system paths and settings (`SKOGAI`, `UV_TOOL_DIR`, `EDITOR`)
- `key.env.*`: Global API keys and credentials (`ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`)
- `settings.*`: UI preferences, memory configuration, script templates

**Agent Namespaces**:
- `claude.env.*`: Claude-specific environment (`PAGER="bat"`, `LLM_OUTPUT="./tmp/llm-output"`)
- `goose.env.*`: Goose agent configuration (`GOOSE_HOME`, `GOOSE_CONTEXT_UPDATE`)
- `amy.env.*`, `dot.env.*`: Additional agent-specific environments

**Service Namespaces**:
- `supabase.env.*`: Database connections, service keys, project references
- `cloudflare.env.*`: API tokens, account IDs, zone configurations
- `github.env.*`: Personal access tokens and authentication

**Environment Layering Logic**:
```bash
# Base + Agent + Service = Complete Environment
skogcli config export-env --namespace skogai,claude,supabase
# Results in: Base paths → Agent preferences → Service credentials
# Later namespaces override earlier ones (supabase.env.PAGER overrides claude.env.PAGER)
```

## TODO
- [ ] Document agent creation workflow
- [ ] Script template customization guide
- [ ] MCP server integration examples