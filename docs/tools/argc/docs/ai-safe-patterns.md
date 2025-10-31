# AI-Safe Patterns with Argc

This document explains how argc enables **self-correcting, validated, auditable AI operations**.

## The Problem

Traditional AI-system interactions are fragile:

```bash
User: "restart the api service"
AI: systemctl restart api
System: Unit api.service not found
AI: *guesses* systemctl restart api.service
System: Unit api.service not found
AI: *more guessing*
```

## The Solution

Argc provides **runtime validation** that gives AI agents self-correcting feedback:

```bash
User: "restart the api service"
AI: argc service --action restart api
System: error: invalid value `api`
        [possible values: app-web, app-api, app-worker]
AI: argc service --action restart app-api
System: Success ✓
```

## The Four Validation Layers

### 1. Static Choices (Compile-time)

Fixed set of valid options:

```bash
# @option --env[dev|qa|prod]  Target environment
deploy() {
  # env is GUARANTEED to be dev, qa, or prod
}
```

**AI benefit:** Can't typo "develop" → gets corrected to "dev"

### 2. Dynamic Choices (Runtime state)

Validated against **current system state**:

```bash
# @option --port[`_available_ports`]  Port to bind
serve() {
  # port is GUARANTEED to be available RIGHT NOW
}

_available_ports() {
  for port in {8000..8100}; do
    ! lsof -i :$port &>/dev/null && echo $port
  done
}
```

**AI benefit:** Can't bind to occupied ports → shows which ARE available

**Real-world examples:**
- `_available_ports()` - Only free ports
- `_installed_mcps()` - Only installed MCP servers
- `_git_branches()` - Only existing branches
- `_running_containers()` - Only active Docker containers
- `_session_ids()` - Only valid session files

### 3. Environment Variables (Capability gates)

Operations require specific environment context:

```bash
# @env ADMIN_PASSPHRASE![supersecret]  Admin access required
admin() {
  # Only runs if ADMIN_PASSPHRASE=supersecret
}
```

**AI benefit:** Can't run privileged operations without explicit authorization

**Validation options:**
```bash
@env VAR!                  # Required to be set
@env VAR[a|b]              # Must be one of these values
@env VAR![exact]           # Required AND must match exactly
@env VAR[=default]         # Optional with default
@env VAR[`_choice_fn`]     # Dynamic validation
```

### 4. Context-Aware Validation (Agent/PWD scoped)

Validation changes based on **where you are** and **which agent is running**:

```bash
_choice_sessions() {
  local agent_home="${SKOGAI_AGENT_HOME:-$HOME/.claude}"
  local project_dir=$(pwd | sed 's|/|-|g' | sed 's|^-||')

  ls "$agent_home/projects/$project_dir/" 2>/dev/null
}
```

**AI benefit:**
- Different sessions available in different projects
- Different agents see different contexts
- Same command, different behavior per location

## Pattern Library

### Available Ports Pattern

```bash
# @option --port![`_available_ports`]  Port to bind (required)
serve() {
  echo "Binding to: $argc_port"
  # Port is GUARANTEED available
}

_available_ports() {
  for port in {8000..8100}; do
    ! lsof -i :$port &>/dev/null && echo $port
  done
}
```

**Demo:**
```bash
$ argc serve --port 8080  # Port taken
error: invalid value `8080`
  [possible values: 8000, 8001, ..., 8079, 8081, ...]

$ argc serve --port 8000  # Port available
Binding to: 8000 ✓
```

### MCP Server Management Pattern

```bash
# @arg server![`_installed_mcps`]  Server to remove
mcp-remove() {
  claude mcp remove "$argc_server"
}

_installed_mcps() {
  claude mcp list 2>&1 | grep -E '^[a-zA-Z0-9_-]+:' | awk -F': ' '{print $1}'
}
```

**Demo:**
```bash
$ argc mcp-remove notexists
error: invalid value `notexists`
  [possible values: skogai-memory, foo]

$ argc mcp-remove foo
Removed MCP server "foo" ✓
```

### Systemctl Services Pattern

```bash
# @arg service![`_managed_services`]  Service name
service() {
  systemctl --user $argc_action "$argc_service.service"
}

_managed_services() {
  systemctl --user list-units "app-*.service" --state=running \
    | grep "^app-" | awk '{print $1}' | sed 's/.service$//'
}
```

**Security:** AI can only touch services matching `app-*`, not system services

### Session ID Pattern

```bash
# @option --session[`_choice_sessions`]  Resume session
session() {
  # Session is GUARANTEED to exist in current project
}

_choice_sessions() {
  local agent_home="${SKOGAI_AGENT_HOME:-$HOME/.claude}"
  local project_dir=$(pwd | sed 's|/|-|g' | sed 's|^-||')

  ls "$agent_home/projects/$project_dir/" 2>/dev/null
}
```

**Context-aware:** Different sessions in `/home/user/project-a` vs `/home/user/project-b`

### Git Branches Pattern

```bash
# @option --branch[`_git_branches`]  Target branch
git-deploy() {
  git checkout "$argc_branch"
}

_git_branches() {
  git branch 2>/dev/null | sed 's/^[* ]*//'
}
```

**Safety:** Can only checkout branches that actually exist in current repo

## Guidelines for AI-Safe Commands

### 1. Options vs Args

```bash
# @option = Constrained modes/behaviors
--env[dev|qa|prod]         # Deployment environment (mode)
--format[json|yaml|toml]   # Output format (mode)
--action[start|stop]       # Operation type (mode)

# @arg = Arbitrary user data
file                       # File path (user data)
name                       # Project name (user data)
pattern                    # Search pattern (user data)
```

### 2. Validation Strategy

```bash
# Static - Fixed values
--env[dev|qa|prod]

# Dynamic - Runtime state
--port[`_available_ports`]

# Required - Cannot omit
--env!

# Default - Fallback value
--env[=dev]

# Combined
--env![dev|qa|prod]        # Required + choices
--port[=8080|`_ports`]     # Default or dynamic
```

### 3. When to Use Each Layer

**Static choices** when:
- Options are known at design time
- Values don't change (formats, modes, actions)
- Example: `--format[json|yaml]`

**Dynamic choices** when:
- Validation requires system state
- Values change at runtime
- Example: `--port[`_available_ports`]`

**Environment variables** when:
- Access control needed
- Context requirements
- Example: `@env ADMIN_MODE!`

**Context-aware** when:
- Behavior changes per location/agent
- Multi-project/multi-agent scenarios
- Example: Session IDs, project-specific configs

## Comparison: Raw vs Argc-Wrapped

### Raw Command (Unsafe)

```bash
#!/bin/bash
# No validation, hope for the best
cd ~/claude
claude --print "$*"
```

**Problems:**
- No structure (black box to AI)
- No validation (errors discovered late)
- No introspection (can't discover capabilities)
- No self-correction (AI guesses on failure)

### Argc-Wrapped (Safe)

```bash
#!/bin/bash
# @describe Claude CLI with validated operations
# @option --output-format[text|json|stream-json]  Output format
# @arg prompt!  Your prompt

claude() {
  claude --print --output-format "$argc_output_format" "$argc_prompt"
}

eval "$(argc --argc-eval "$0" "$@")"
```

**Benefits:**
- **Structured:** Clear commands/options/args
- **Validated:** Invalid input rejected at parse time
- **Introspectable:** `argc help` shows capabilities
- **Self-correcting:** Wrong values show correct options

## Integration with Skogparse

Argc commands become **composable actions** in skogparse:

```bash
# Introspection
[@argc:help]              # Discover commands

# Execution
[@argc:serve --port 8080] # Validated execution

# Composition
port = [@argc-completions:choice-fn Argcfile.sh _available_ports | head -1]
[@argc:serve --port $port]
```

**Complete stack:**
1. **Argc** - Validation at CLI boundary
2. **Skogparse** - Composition and orchestration
3. **Actions** - Registered safe operations
4. **AI** - Uses validated, composable primitives

## Real-World Applications

### Constrain systemctl to specific services

```bash
# Only manage services matching pattern
_foo_services() {
  systemctl list-units "foo-*.service" --type=service \
    | grep "^foo-" | awk '{print $1}' | sed 's/.service$//'
}

# @arg service![`_foo_services`]
service-restart() {
  sudo systemctl restart "$argc_service.service"
}
```

### Safe Docker container management

```bash
# Only containers with label ai-managed=true
_ai_containers() {
  docker ps --filter "label=ai-managed=true" --format "{{.Names}}"
}

# @arg container![`_ai_containers`]
container-restart() {
  docker restart "$argc_container"
}
```

### Git operations scoped to feature branches

```bash
_feature_branches() {
  git branch --list "feature/*" "bugfix/*" | sed 's/^[* ]*//'
}

# @arg branch![`_feature_branches`]
git-deploy() {
  git checkout "$argc_branch" && git push
}
```

## Why This Matters

Traditional approach:
```
AI → Execute → Fail → Parse Error → Retry (slow, fragile)
```

Argc approach:
```
AI → Validate → Get Valid Options → Execute (fast, reliable)
```

**Benefits:**
1. **Self-correcting** - Invalid input shows valid alternatives
2. **Fast feedback** - Validation at parse time, not mid-execution
3. **No defensive code** - Trust validated inputs
4. **Auditable** - Clear capability boundaries
5. **Composable** - Chain validated operations safely
6. **Context-aware** - Validation scoped to agent/project/environment

## Conclusion

This isn't just "better CLI help" - it's a **type system for AI-system interactions**.

Every system command becomes:
- Self-documenting (introspectable capabilities)
- Self-correcting (shows valid alternatives)
- Safe by construction (validated at boundary)
- Context-aware (scoped to agent/project/env)

The result: **AI agents that can't accidentally break things because the system structurally prevents invalid operations.**
