---
name: learning-argc
description: Use when creating argc commands, uncertain about argc syntax, or learning argc progressively - provides syntax quick reference, common mistakes with fixes, and progressive examples from simple to complex
---

# Learning Argc

## Overview

argc is a bash-based command runner that turns shell functions into CLI commands through comment annotations. This skill provides progressive examples and common pitfall fixes for learning argc systematically.

**Core principle:** Comment tags (`@cmd`, `@arg`, `@option`, `@flag`) turn bash functions into documented, validated CLI commands.

## When to Use

- Creating new Argcfile.sh scripts
- Uncertain about argc syntax (choices, defaults, modifiers)
- Need quick reference for common patterns
- Debugging argc validation issues

## Progressive Examples

### Level 1: Simple Command

```bash
#!/usr/bin/env bash

# @cmd Build the project
build() {
    echo "Building..."
}

eval "$(argc --argc-eval "$0" "$@")"
```

**Must include:** The `eval` line at the end (argc won't work without it)

### Level 2: Arguments and Flags

```bash
# @cmd Deploy service
# @arg environment             Optional positional arg
# @flag --dry-run              Boolean flag (no value)
deploy() {
    echo "Environment: $argc_environment"
    echo "Dry run: $argc_dry_run"  # "1" if set, empty if not
}
```

**Variable naming:** `argc_` + parameter name (hyphens become underscores)

### Level 3: Options with Defaults

```bash
# @option -o --output=dist <DIR>    Output directory (default: dist)
# @option --format[=json|yaml]      Format with choices and default
```

**Syntax:** `=value` for default, `[=choice1|choice2]` for choices with default

### Level 4: Required and Multi-Value

```bash
# @arg files+              One or more required files
# @arg patterns*           Zero or more patterns
# @option --tag*           Can be specified multiple times
# @env API_KEY!            Required environment variable
```

**Modifiers:**
- `!` = required
- `+` = one or more (required multi-value)
- `*` = zero or more (optional multi-value)

**Array access:** Use `${argc_files[@]}` for multi-value params

## Common Mistakes

### ❌ Choices in Description (No Validation)

```bash
# @option --region <REGION>  Region [us-east|us-west|eu-west]
```

This documents choices but doesn't validate them!

### ✅ Choices in Tag (Validates)

```bash
# @option --region[us-east|us-west|eu-west] <REGION>  Region to deploy
```

### ❌ Default in Description

```bash
# @option --port <PORT>  Port number (default: 8080)
```

### ✅ Default in Tag

```bash
# @option --port=8080 <PORT>  Port number
```

### ❌ Wrong Array Access

```bash
# @arg files+
deploy() {
    echo $argc_files  # Only prints first file!
}
```

### ✅ Correct Array Access

```bash
# @arg files+
deploy() {
    echo "${argc_files[@]}"  # Prints all files
}
```

## Quick Reference

| Pattern | Syntax | Example |
|---------|--------|---------|
| Required arg | `@arg name!` | `@arg file!` |
| Multi-value arg | `@arg name+` | `@arg sources+` |
| Optional multi | `@arg name*` | `@arg patterns*` |
| Flag | `@flag --name` | `@flag --verbose` |
| Option | `@option --name` | `@option --output <DIR>` |
| Short option | `@option -o --output` | `@option -o --output <DIR>` |
| Default value | `name=value` | `--port=8080` |
| Choices | `[choice1\|choice2]` | `[json\|yaml\|xml]` |
| Choice + default | `[=choice1\|choice2]` | `[=json\|yaml]` |
| Required env | `@env NAME!` | `@env API_KEY!` |
| Command alias | `@alias name` | `@alias t,tst` |
| Default cmd | `@meta default-subcommand` | On the command function |

## Variable Access

- **Single value:** `$argc_option_name`
- **Multi-value:** `${argc_option_name[@]}`
- **Flag:** `$argc_flag_name` (empty or "1")
- **Environment:** `$ENV_VAR_NAME` (use original name, not argc_ prefix)
- **Hyphens:** Converted to underscores (`--dry-run` → `$argc_dry_run`)

## Full Working Example

```bash
#!/usr/bin/env bash

# @describe A project build tool

# @env NODE_ENV[=dev|prod]  Environment

# @cmd Build the project
# @arg sources+ <FILE>           Source files to build
# @option -o --output=dist <DIR> Output directory
# @flag --watch                  Watch for changes
# @meta default-subcommand
build() {
    echo "Building ${#argc_sources[@]} files"
    for file in "${argc_sources[@]}"; do
        echo "  - $file"
    done
    echo "Output: $argc_output"
    [ -n "$argc_watch" ] && echo "Watch mode enabled"
}

# @cmd Run tests
# @alias t
# @arg patterns* <PATTERN>  Test patterns
# @flag --coverage          Generate coverage
test() {
    echo "Running tests in $NODE_ENV mode"
    echo "Patterns: ${argc_patterns[@]}"
    [ -n "$argc_coverage" ] && echo "Coverage enabled"
}

eval "$(argc --argc-eval "$0" "$@")"
```

## Documentation Location

Full argc docs: `/home/skogix/skogix/docs/tools/argc/docs/`
- `specification.md` - Complete syntax reference
- `command-runner.md` - Command patterns and organization
- `variables.md` - Variable access details

## Common Patterns

**Organize related commands:**
```bash
# @cmd
test() { :; }
# @cmd
test-unit() { :; }
# @cmd
test-integration() { :; }
```

**Command dependencies:**
```bash
# @cmd
deploy() {
    build    # Call another command
    echo "Deploying..."
}
```

**Require tools:**
```bash
# @meta require-tools git,jq,yq
```
