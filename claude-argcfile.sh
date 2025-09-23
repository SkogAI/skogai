#!/usr/bin/env bash

set -e

# @describe SkogAI orchestration tools
# @version 0.1.0

# @cmd Generate an argc command template
# @arg name! Command name
# @arg description! Command description
# @option -t --type=simple Type of command to generate <simple|crud|api>
# @flag -j --json Output as JSON
argc_generate() {
    local template=""

    case "$argc_type" in
        crud)
            template="# @cmd $argc_description
# @arg id! Resource ID
# @arg data* Resource data fields
${argc_name}_create() { echo \"Creating resource with data: \$argc_data\"; }
${argc_name}_read() { echo \"Reading resource: \$argc_id\"; }
${argc_name}_update() { echo \"Updating resource: \$argc_id\"; }
${argc_name}_delete() { echo \"Deleting resource: \$argc_id\"; }"
            ;;
        api)
            template="# @cmd $argc_description
# @arg endpoint! API endpoint
# @option -m --method=GET HTTP method <GET|POST|PUT|DELETE>
# @option -d --data JSON data for request body
# @flag -v --verbose Show detailed output
${argc_name}() {
    echo \"API call to: \$argc_endpoint\"
    echo \"Method: \$argc_method\"
    [[ -n \"\$argc_data\" ]] && echo \"Data: \$argc_data\"
}"
            ;;
        *)
            template="# @cmd $argc_description
${argc_name}() {
    echo \"TODO: Implement ${argc_name}\"
}"
            ;;
    esac

    if [[ "$argc_json" ]]; then
        # Proper JSON encoding using jq
        echo "{\"name\": \"$argc_name\", \"template\": $(echo "$template" | jq -Rs .)}"
    else
        echo "$template"
    fi
}

# @cmd List available agent prompts
# @flag -d --detailed Show full prompt content
argc_agents() {
    local agents_dir=".claude/agents"
    if [[ ! -d "$agents_dir" ]]; then
        echo "No agents directory found"
        return 1
    fi

    if [[ "$argc_detailed" ]]; then
        for agent in "$agents_dir"/*.md; do
            echo "=== $(basename "$agent" .md) ==="
            head -n 5 "$agent"
            echo
        done
    else
        ls -1 "$agents_dir"/*.md 2>/dev/null | xargs -n1 basename -s .md
    fi
}

eval "$(argc --argc-eval "$0" "$@")"