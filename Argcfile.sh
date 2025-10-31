#!/usr/bin/env bash
# @describe AI-safe task runner with validated operations
# @meta version 0.1.0
# @meta symbol +int[`_int`]
#
# This template demonstrates AI-safe patterns for system operations:
#
# VALIDATION LAYERS:
# 1. Static choices    - Fixed options: --env[dev|qa|prod]
# 2. Dynamic choices   - Runtime state: --port[`_available_ports`]
# 3. Environment vars  - Context gates: @env ADMIN_MODE![secret]
# 4. Context-aware     - Agent/pwd scoped validation
#
# DESIGN PRINCIPLES:
# - @option = constrained choices (modes/behaviors) → self-correction
# - @arg    = arbitrary user data (paths/names/patterns)
# - Every option: explicit default OR required (!)
# - Choices prevent typos and show valid alternatives
# - Dynamic validation against CURRENT system state
# - Environment variables act as capability gates
#
# WHY THIS MATTERS FOR AI AGENTS:
# - Self-correcting: Invalid input shows valid options
# - No defensive code: Validation at CLI boundary
# - Auditable: Clear what can/cannot be done
# - Safe by construction: Can't run invalid operations

# @cmd skogix
skogix() {
  echo "$argc_int"
  echo "$argc_testargument"
  # something like this i think?
  # for int in "${argc_int[@]}"; do
  #   echo "  - number $int"
  # done
}

# @cmd Build the project
# @alias b
# @flag --clean         Clean build artifacts before building
# @flag --verbose       Show detailed build output
# @option --target[=all|frontend|backend|docs]  What to build
build() {
  echo "Building: $argc_target"
  [[ "$argc_clean" == "1" ]] && echo "Cleaning first..."
  [[ "$argc_verbose" == "1" ]] && echo "Verbose mode enabled"

  # Your build logic here
}

# @cmd Run tests
# @alias t
# @option --suite[=all|unit|integration|e2e]  Which test suite to run
# @flag --watch         Re-run tests on file changes
# @arg filter           Test name pattern (empty = run all)
test() {
  echo "Running suite: $argc_suite"
  echo "Filter: ${argc_filter:-*}"
  [[ "$argc_watch" == "1" ]] && echo "Watch mode enabled"

  # Your test logic here
  # suite is a constrained mode, filter is arbitrary user data
}

# @cmd Deploy to specified environment
# WARNING: Pushes to live infrastructure. Always use --dry-run first.
# Workflow: 1) deploy --dry-run --env qa api  2) deploy --env qa api
# @alias d
# @option --env![dev|qa|prod]  Target environment (REQUIRED to prevent accidents)
# @flag --dry-run               Preview deployment without applying changes
# @option --region[=us-east-1|eu-west-1|ap-south-1]  Deployment region
# @arg target!                  Service to deploy (e.g., api, web, worker)
deploy() {
  echo "Deploying: $argc_target"
  echo "Environment: $argc_env"
  echo "Region: $argc_region"

  if [[ "$argc_dry_run" == "1" ]]; then
    echo "DRY RUN - no changes will be applied"
    # Show what would happen
  else
    echo "LIVE DEPLOYMENT - applying changes..."
    # Actual deployment
  fi

  # The AI knows:
  # - Must specify --env (required!)
  # - Choices prevent typos (develop->dev self-correction)
  # - Region defaults to us-east-1
  # - Must specify what to deploy (target required!)
}

# @cmd Database operations
db() { :; }

# @cmd Backup database
# @option --format[=sql|binary]  Backup format
# @arg output                    Output file path
db::backup() {
  local output="${argc_output:-backup.sql}"
  echo "Backing up to: $output"
  echo "Format: $argc_format"

  # format is a constrained mode, output is arbitrary file path
}

# @cmd Run database migrations
# @option --direction[=up|down]  Migration direction
# @arg version                   Target version (empty = latest)
db::migrate() {
  local target="${argc_version:-latest}"
  echo "Migrating $argc_direction to: $target"

  # direction is a constrained mode, version is arbitrary data
}

# @cmd Initialize new project
# @option --template[=basic|api|fullstack]  Project template
# @option --lang[=bash|python|typescript]   Primary language
# @arg name!                                Project name
init() {
  echo "Creating project: $argc_name"
  echo "Template: $argc_template"
  echo "Language: $argc_lang"

  # template and lang are constrained modes, name is arbitrary data
}

# @cmd Start development server
# @option --port[`_available_ports`]  Ports to bind to (dynamically validated)
# @option --skogix  Ports to bind to (must be a int)
serve() {
  echo "Starting server on ports: ${argc_port[@]}"
  echo "Number of ports: ${#argc_port[@]}"
  for port in "${argc_port[@]}"; do
    echo "  - Port $port"
  done

  # Ports are GUARANTEED to be available - no validation needed!
  # AI gets self-correcting feedback if requested port is taken
}

_available_ports() {
  # Return only ports that are actually free right now
  for port in {8000..8100}; do
    if ! lsof -i :$port &>/dev/null; then
      echo $port
    fi
  done
}

_int() {
  seq 1 100
}

# @cmd Context-aware session management example
# Demonstrates: dynamic choices based on agent + pwd
# @option --session[`_choice_sessions`]  Resume a previous session
session() {
  echo "Resuming session: $argc_session"
  echo "Agent: ${SKOGAI_AGENT_NAME:-claude}"
  echo "Project: $(pwd)"

  # Session is GUARANTEED to exist in current context
}

_choice_sessions() {
  # Context-aware: combines agent + pwd for scoped validation
  local agent_home="${SKOGAI_AGENT_HOME:-$HOME/.claude}"
  local project_dir=$(pwd | sed 's|/|-|g' | sed 's|^-||')

  ls "$agent_home/projects/$project_dir/" 2>/dev/null || echo "no-sessions"
}

# @cmd Environment-gated admin operations
# Demonstrates: environment variable validation with choices
# @env ADMIN_PASSPHRASE![supersecret]  Admin access required
admin() {
  echo "Running admin operation..."
  echo "Admin access verified via ADMIN_PASSPHRASE"

  # Only runs if ADMIN_PASSPHRASE=supersecret
  # Change to your actual passphrase or use dynamic validation
}

# @cmd Manage services (constrained pattern)
# Demonstrates: wrap system commands with safety boundaries
# @option --action![start|stop|restart|status]  Service action
# @arg service![`_managed_services`]            Service name (only managed services)
service() {
  echo "Action: $argc_action on service: $argc_service"

  # In real implementation:
  # systemctl --user $argc_action "$argc_service.service"
}

_managed_services() {
  # Only expose services matching your pattern (e.g., app-*)
  # systemctl --user list-units "app-*.service" --state=running | grep "^app-" | awk '{print $1}' | sed 's/.service$//'
  echo "app-web"
  echo "app-api"
  echo "app-worker"
}

# @cmd Git operations (context-validated)
# Demonstrates: validate against actual git state
# @option --branch[`_git_branches`]  Target branch
git-deploy() {
  echo "Deploying branch: ${argc_branch:-current}"

  # Branch is GUARANTEED to exist in current repo
}

_git_branches() {
  # Only show branches that actually exist
  git branch 2>/dev/null | sed 's/^[* ]*//' || echo "main"
}

# @cmd MCP server operations
# Demonstrates: manage external tools with validation
# @option --action![list|add|remove]     MCP operation
# @arg server[`_installed_mcps`]         Server name (for remove)
mcp() {
  case "$argc_action" in
  list)
    claude mcp list
    ;;
  remove)
    echo "Removing MCP server: $argc_server"
    # claude mcp remove "$argc_server"
    ;;
  *)
    echo "Use list or remove"
    ;;
  esac
}

_installed_mcps() {
  # Parse actual installed MCP servers
  claude mcp list 2>&1 | grep -E '^[a-zA-Z0-9_-]+:' | awk -F': ' '{print $1}' || echo "none"
}

### ################################################################################
### # PATTERN LIBRARY - Copy/adapt these for your use cases
### ################################################################################
### #
### # PATTERN: Available ports
### # _available_ports() {
### #   for port in {8000..8100}; do
### #     ! lsof -i :$port &>/dev/null && echo $port
### #   done
### # }
### #
### # PATTERN: Docker containers
### # _running_containers() {
### #   docker ps --format "{{.Names}}" 2>/dev/null
### # }
### #
### # PATTERN: Config files in directory
### # _config_files() {
### #   find ~/.config/myapp -name "*.conf" 2>/dev/null | xargs -n1 basename
### # }
### #
### # PATTERN: Environment with dynamic validation
### # @env PROJECT_NAME[`_valid_projects`]
### # _valid_projects() {
### #   ls ~/projects 2>/dev/null
### # }
### #
### # PATTERN: Multi-select with comma separation
### # @option --services*,[`_available_services`]
### #
### # PATTERN: Required with choices from function
### # @arg target![`_deployment_targets`]
### #
### ################################################################################
### # GUIDELINES FOR YOUR COMMANDS
### ################################################################################
### #
### # 1. OPTIONS vs ARGS
### #    - @option = Known modes/behaviors (build target, output format)
### #    - @arg    = User-provided data (file paths, names, patterns)
### #
### # 2. VALIDATION STRATEGY
### #    - Static [a|b|c]      → Fixed set of values
### #    - Dynamic [`fn`]      → Runtime system state
### #    - Required !          → Cannot be omitted
### #    - Default [=value]    → Fallback when not provided
### #
### # 3. ENVIRONMENT VARIABLES
### #    - @env VAR!           → Must be set
### #    - @env VAR[a|b]       → Must match choices
### #    - @env VAR[`fn`]      → Dynamic validation
### #    - Use for: access control, context requirements
### #
### # 4. SELF-DOCUMENTING
### #    - Add comments explaining WHY validation exists
### #    - Show example workflows in command descriptions
### #    - Document what's GUARANTEED after validation
### #
### # 5. COMPOSITION PATTERNS
### #    - Functions validate once, trust thereafter
### #    - Chain operations knowing inputs are safe
### #    - No defensive checks inside functions
### #
### ################################################################################

_argc_before() {
  if ! [[ "$argc_int" =~ ^[0-9]+$ ]]; then
    exit 1
  fi
  # extra validation:
  # if $argc_port is not a integer throw error
  if [[ -n "$argc_skogix" ]]; then
    for port in "${argc_skogix[@]}"; do
      if ! [[ "$port" =~ ^[0-9]+$ ]]; then
        echo "Error: --port must be an integer. Invalid value: $port"
        exit 1
      fi
    done
  fi
}

eval "$(argc --argc-eval "$0" "$@")"
