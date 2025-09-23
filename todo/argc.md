# argc

**Core Philosophy**: CLI framework powering SkogAI command structure and argument parsing.

## Framework Integration

### SkogCLI Commands
argc provides the underlying CLI framework for SkogCLI's main commands:
- `skogcli memory` - Knowledge management operations
- `skogcli config` - Configuration and environment management  
- `skogcli script` - Script lifecycle and AI-powered generation
- `skogcli agent` - Multi-agent orchestration
- `skogparse` - Unified execution language parser

### Command Structure
- Hierarchical command organization with subcommands
- Automatic help generation and argument parsing
- Integration with SkogAI's configuration system
- Support for complex argument patterns and validation

## Implementation Structure

argc is implemented through the `skogai.sh` script at `/home/skogix/skogai/scripts/skogai.sh`, which defines the command hierarchy and integration patterns.

### Core Functions

**Information Commands**:
```bash
# @cmd Display system information
info() {
  echo "My SkogAI Script v1.0.0"
}

# @cmd Greet someone  
# @arg name! Person to greet
# @flag --formal Use formal greeting
greet() {
  echo "Hey there, $name! What's up?"
}
```

**Service Management**:
```bash
# @cmd passthrough to another skogai wrapper for systemctl
# @env SKOGIXISBEST![yes]  # Requires exact environment variable value
service::systemctl() {
  skogcli script run skogai-service "$@"
}

# @cmd systemctl status
service::status() {
  systemctl --user status
}
```

**Integration Features**:
```bash
# @cmd Calculate age using skogparse integration
age() {
  local age_expr="[@subtract:\"$current_year\":\"$birth_year\"]"
  local result=$(echo "$age_expr" | $SKOGPARSE --execute | jq -r '.value')
  echo "Age: $result"
}
```

## skogparse Integration

### Command Execution Patterns
```bash
# Direct script execution
argc

# Via skogparse notation
skogparse '[@argc]'           # Execute argc help
skogparse '[@skogai:info]'    # → "My SkogAI Script v1.0.0"
skogparse '[@skogai:greet:Claude]'  # → "Hey there, Claude! What's up?"

# Service management with environment validation
SKOGIXISBEST=yes skogparse '[@skogai:service:systemctl]'
```

### Environment Variable Validation

argc enforces strict environment variable requirements using the `@env` annotation:
```bash
# @env SKOGIXISBEST![yes]  # Must equal exactly "yes"
```

This provides secure command execution by requiring specific environment contexts.

## Architecture

- **Command Registration**: Automatic discovery of SkogCLI command modules
- **Argument Processing**: Robust parsing with type validation and defaults
- **Help System**: Auto-generated documentation and usage examples
- **Error Handling**: Structured error reporting and command suggestions

## Development Integration

- Template system for creating new SkogCLI commands
- Integration with SkogAI's script generation workflow
- Configuration-driven command customization
- Extensible plugin architecture for custom command modules