# SkogArgc - AI-Safe Argc Templates

**Build self-correcting, validated command-line interfaces for AI agents.**

## What is This?

A template and pattern library for creating **AI-safe system operations** using [argc](https://github.com/sigoden/argc) with runtime validation.

Instead of AI agents guessing commands and hoping they work, they get **self-correcting feedback** when inputs are invalid.

## Quick Example

**Traditional approach (fragile):**
```bash
$ systemctl restart api-service
Unit api-service.service not found
# AI guesses more variations...
```

**Argc approach (self-correcting):**
```bash
$ argc service --action restart api
error: invalid value `api`
  [possible values: app-web, app-api, app-worker]

$ argc service --action restart app-api
Success ✓
```

## The Four Validation Layers

### 1. Static Choices
```bash
# @option --env[dev|qa|prod]  Target environment
```
AI can't typo "develop" → argc corrects to "dev"

### 2. Dynamic Runtime Validation
```bash
# @option --port[`_available_ports`]  Port to bind
_available_ports() {
  for port in {8000..8100}; do
    ! lsof -i :$port &>/dev/null && echo $port
  done
}
```
AI can't bind to occupied ports → argc shows which ARE available

### 3. Environment Variable Gates
```bash
# @env ADMIN_MODE![supersecret]  Admin access required
```
AI can't run privileged ops without authorization

### 4. Context-Aware Scoping
```bash
_choice_sessions() {
  local agent_home="${SKOGAI_AGENT_HOME:-$HOME/.claude}"
  local project_dir=$(pwd | sed 's|/|-|g' | sed 's|^-||')
  ls "$agent_home/projects/$project_dir/"
}
```
Different sessions in different projects/agents

## Getting Started

### 1. Copy the Template

```bash
cp Argcfile.sh your-project.sh
chmod +x your-project.sh
```

### 2. Add Your Commands

```bash
# @cmd Deploy application
# @option --env![dev|qa|prod]  Target environment (required)
# @arg service!                Service to deploy
deploy() {
  echo "Deploying $argc_service to $argc_env"
  # Your deployment logic
}
```

### 3. Add Dynamic Validation

```bash
# @arg service![`_available_services`]
deploy() {
  # service is GUARANTEED to exist
}

_available_services() {
  ls ~/services/*/config.yml | xargs -n1 dirname | xargs -n1 basename
}
```

### 4. Test the Validation

```bash
$ argc deploy --env production nonexistent
error: invalid value `nonexistent`
  [possible values: api, web, worker]
```

## Pattern Library

The template includes ready-to-use patterns:

- **Available ports** - Only bind to free ports
- **MCP servers** - Only manage installed servers
- **Git branches** - Only deploy existing branches
- **Service management** - Only touch allowed services
- **Session IDs** - Context-aware session selection
- **Docker containers** - Only manage specific containers

See [docs/ai-safe-patterns.md](docs/ai-safe-patterns.md) for complete examples.

## Real-World Use Cases

### Constrain Systemctl Operations

```bash
_managed_services() {
  systemctl --user list-units "myapp-*.service" \
    | grep "^myapp-" | awk '{print $1}' | sed 's/.service$//'
}

# @arg service![`_managed_services`]
service-restart() {
  sudo systemctl restart "$argc_service.service"
}
```

**Result:** AI can only restart services matching `myapp-*`, not system services.

### Validate MCP Server Operations

```bash
_installed_mcps() {
  claude mcp list 2>&1 | grep -E '^[a-zA-Z0-9_-]+:' | awk -F': ' '{print $1}'
}

# @arg server![`_installed_mcps`]
mcp-remove() {
  claude mcp remove "$argc_server"
}
```

**Result:** Can't remove servers that don't exist.

### Safe Docker Management

```bash
_ai_containers() {
  docker ps --filter "label=ai-managed=true" --format "{{.Names}}"
}

# @arg container![`_ai_containers`]
container-restart() {
  docker restart "$argc_container"
}
```

**Result:** AI can only touch containers explicitly marked as manageable.

## Integration with Skogparse

Argc commands become composable actions:

```bash
# Discovery
[@list-actions]

# Introspection
[@argc:help]

# Execution
[@argc:serve --port 8080]

# Composition
port = [@argc-completions:choice-fn script.sh _available_ports | head -1]
[@argc:serve --port $port]
```

## Why This Matters

Traditional AI-system interaction:
```
AI → Execute → Fail → Parse Error → Retry (slow, fragile)
```

With argc validation:
```
AI → Validate → Get Valid Options → Execute (fast, reliable)
```

**Benefits:**
- ✅ Self-correcting - Shows valid alternatives
- ✅ Fast feedback - Validation at parse time
- ✅ No defensive code - Trust validated inputs
- ✅ Auditable - Clear capability boundaries
- ✅ Composable - Chain operations safely
- ✅ Context-aware - Scoped to agent/project/env

## Documentation

- [docs/ai-safe-patterns.md](docs/ai-safe-patterns.md) - Complete pattern guide
- [docs/specification.md](docs/specification.md) - Argc syntax reference
- [docs/variables.md](docs/variables.md) - Variable usage
- [examples/](examples/) - Working examples

## Examples

See working examples in [examples/](examples/):

- `claude-mcp.sh` - MCP server management with validation
- `Argcfile.sh` - Full template with all patterns

## Design Philosophy

**Every option should be:**
- Required (`!`) OR have explicit default (`[=value]`)
- Constrained to valid choices (`[a|b]`) when possible
- Dynamically validated (`` [`fn`] ``) against system state when needed

**Never:**
- Optional with no default (ambiguous empty state)
- Free-form text when choices exist (AI will typo)
- Trust user input without validation (defensive code smell)

## Contributing

This is a template repository. Fork it, adapt it, improve it!

Key areas for contribution:
- New validation patterns
- Integration examples (CI/CD, deployment, etc.)
- Documentation improvements
- Real-world case studies

## License

MIT

## Credits

Built on [argc](https://github.com/sigoden/argc) by sigoden.

Developed for AI-safe system operations in the Skogai ecosystem.
