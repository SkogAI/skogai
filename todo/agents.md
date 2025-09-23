# Agent Architecture

## Core Principles

Agents in Claude Code are **stateless, isolated workers** that execute specific tasks without access to conversation history. This document explains how agents work, why tool restriction is critical, and how to design effective agents.

## Agent Isolation

### Key Characteristics

1. **No Context Inheritance**: Agents spawned via `@agent-name` start completely fresh
2. **No Chat History**: Cannot see previous conversation messages
3. **Stateless Execution**: Each invocation is independent
4. **Tool-Based Discovery**: Can only find information through allowed tools

Agents operate as isolated instances without access to the conversation history, requiring all necessary context to be explicitly provided in their invocation.

## Agent Invocation Methods

### 1. Direct Invocation via @agent-name

```
User: @agent-github-issue-creator create an issue
```

- Spawns fresh agent instance
- No conversation context
- Only has access to its defined tools
- Must gather all context from scratch

### 2. Command-Triggered Invocation

```
User: /issue need to fix login bug
Command: [translates to detailed prompt]
Agent: [receives complete context]
```

- Command has full conversation context
- Crafts detailed prompt for agent
- Agent receives self-contained task
- More efficient and predictable

### 3. Task Tool Invocation

```claude
Task tool with:
- description: "Create GitHub issue"
- prompt: [detailed instructions]
- subagent_type: "github-issue-creator"
```

- Programmatic agent invocation
- Precise prompt control
- No context leakage

## Tool Restriction: Critical for Efficiency

### The Impact of Unconstrained Agents

Agents with unrestricted tools tend to:
- Search broadly instead of focusing on the task
- Use more tokens and time than necessary
- Produce unpredictable results
- Deviate from intended behavior

### Constrained vs Unconstrained Performance

| Scenario | Tools | Efficiency | Result |
|----------|-------|------------|--------|
| Via Command (constrained) | 2-3 | High | Predictable execution |
| Direct with many tools | 5+ | Lower | Variable results |
| Direct without search tools | 3-5 | Medium | May need clarification |

### Best Practices for Tool Assignment

1. **Minimum Necessary**: 2-3 tools maximum
2. **Specific Permissions**: Use `Bash(gh:*)` not `Bash`
3. **No Search Tools**: Avoid Grep/Glob for sensitive operations
4. **Explicit Paths**: Use @ references for specific files

## Agent Definition Structure

```yaml
---
name: agent-name
description: When to use this agent (shown to Claude)
tools: Read, Bash(gh:*), WebFetch  # Minimal, specific tools
model: sonnet  # or opus, haiku
color: blue  # UI display color
---

# Agent Instructions

You are a specialized agent for [specific task].

## Your Responsibilities
1. [Specific task 1]
2. [Specific task 2]

## Constraints
- Only operate on provided paths
- Never search for sensitive information
- Return structured results
```

## Design Considerations

### Key Principles

1. **Specific Tool Permissions**: Use subcommands like `Bash(npm:test)`
2. **Focused Search**: Provide specific paths via @ references
3. **Clear Boundaries**: Define what the agent should and shouldn't do
4. **Predictable Behavior**: Constrain tools to ensure consistent results
5. **Graceful Handling**: When information is missing, request clarification

### Example: Focused vs Unfocused

**Unfocused Agent:**
```yaml
tools: Read, Write, Bash, Grep, Glob
# Too many options, unpredictable behavior
```

**Focused Agent:**
```yaml
tools: Read, Bash(npm:test), Edit
# Clear purpose, predictable execution
```

## Agent Design Patterns

### 1. Single-Purpose Executor
```yaml
name: test-runner
tools: Bash(npm:test), Read
# Only runs tests and reads results
```

### 2. Document Processor
```yaml
name: docs-updater
tools: Read, Edit, Glob(docs/**)
# Only operates on docs folder
```

### 3. Issue Manager
```yaml
name: github-issue-creator
tools: Bash(gh:issue), Read
# Only creates issues via gh CLI
```

## Testing Your Agent

### Isolation Test
1. Create information in conversation
2. Invoke agent without providing that context
3. Agent should request the missing information

### Tool Restriction Test
1. Give agent a task with minimal context
2. Observe if it stays focused on the task
3. Check efficiency metrics (tokens and time)

### Boundary Test
1. Provide vague instructions
2. Agent should ask for clarification
3. Should not make assumptions or search broadly

## Common Pitfalls

1. **Too Many Tools**: Agents wander and waste tokens
2. **Vague Instructions**: Agents make incorrect assumptions
3. **No Boundaries**: Agents search where they shouldn't
4. **Context Assumptions**: Expecting chat history access

## Summary

Agents are powerful but must be carefully constrained. The key insight: **agents are stateless workers, not conversation participants**. Design them to do one thing well with minimal tools, and use commands to provide the context they need.