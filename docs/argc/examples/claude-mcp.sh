#!/usr/bin/env bash
# @describe Wrapper for claude mcp commands with validation
# @meta version 0.1.0

# @cmd List installed MCP servers
list() {
    claude mcp list
}

# @cmd Add a new MCP server
# @arg name!         Server name
# @arg command!      Command to run
add() {
    claude mcp add "$argc_name" "$argc_command"
}

# @cmd Remove an MCP server (validated against installed servers)
# @arg server![`_claude_installed_mcps`]  Server name to remove
remove() {
    # Server is GUARANTEED to exist - no validation needed!
    claude mcp remove "$argc_server"
}

_claude_installed_mcps() {
    # Parse output of 'claude mcp list' to get server names
    # Format: "server-name: command - status"
    # Skip "Checking..." header and empty lines
    claude mcp list 2>&1 | grep -E '^[a-zA-Z0-9_-]+:' | awk -F': ' '{print $1}'
}

eval "$(argc --argc-eval "$0" "$@")"
