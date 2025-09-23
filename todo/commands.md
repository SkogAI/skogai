# Command Architecture

## Core Concept

Commands are **context-aware translators** that bridge the gap between user intent and agent execution. They have access to full conversation history and transform vague user requests into detailed, self-contained prompts for stateless agents.

## The Command → Agent Flow

```
User Input → Command (with context) → Detailed Prompt → Agent (no context) → Result
```

### Real Example: /issue Command

```
User: "/issue need to add issue command to claude code"
         ↓
Command: [Sees conversation, understands context]
         ↓
Prompt: "Create a GitHub issue with the following details:
        Title: Add /issue command to Claude Code
        Description: Need to implement a new slash command..."
         ↓
Agent: [Receives complete instructions, creates issue]
         ↓
Result: "Created issue #13"
```

## Command Efficiency Metrics

| Invocation Method | Context Access | Tool Usage | Efficiency | Result |
|-------------------|---------------|------------|------------|--------|
| `/command` route | Full | Minimal | High | Predictable |
| `@agent` direct | None | Variable | Lower | Depends on agent design |
| Task tool invocation | Filtered | Moderate | Medium | Depends on prompt quality |

**Key Insight**: Commands provide the most efficient and predictable path to agent execution.

## Command Definition Structure

```yaml
---
description: Brief description of what the command does
allowed-tools: [Task, Bash(gh:*)]  # Restrict to necessary tools
---

# Command Instructions

1. Parse user input from $ARGUMENTS
2. Transform into detailed agent prompt
3. Invoke appropriate agent via Task tool
4. Return formatted result
```

### Example: Well-Designed Command

```yaml
---
description: Create a GitHub issue
allowed-tools: [Task, Bash(gh:*)]
---

Create a GitHub issue based on the user's request in $ARGUMENTS.

Steps:
1. Take the input from $ARGUMENTS
2. Use the Task tool to invoke the github-issue-creator agent
3. The agent will create an appropriate GitHub issue
```

## Why Commands Matter

### 1. Context Bridge
Commands can see:
- Full conversation history
- Previous commands and results
- User's implied intent
- Project-specific context

Agents cannot see any of this.

### 2. Intelligent Translation

**User says**: "fix that bug we just discussed"

**Command knows**:
- Which bug (from conversation)
- What file (from context)
- Priority level (from discussion)

**Command sends to agent**:
```
Fix TypeError in /api/users.js line 47
Priority: High
Issue: Null reference when user object is undefined
```

### 3. Control Layer

Commands act as orchestrators:
- Validate and parse user input
- Define agent capabilities via tools
- Ensure predictable operations
- Add specific boundaries and context

## Command Design Patterns

### 1. Simple Translator
```yaml
name: test
allowed-tools: [Task]
---
Invoke test-runner agent with: "Run all tests in $ARGUMENTS"
```

### 2. Context Enricher
```yaml
name: fix
allowed-tools: [Task, Read]
---
1. Read current file context
2. Identify the issue mentioned
3. Create detailed fix instructions
4. Invoke fixer agent with complete context
```

### 3. Multi-Step Orchestrator
```yaml
name: deploy
allowed-tools: [Task, Bash(git:*)]
---
1. Check git status
2. If clean, invoke test-runner agent
3. If tests pass, invoke deploy agent
4. Report results
```

## Best Practices

### DO:
- ✅ Keep commands simple and focused
- ✅ Provide complete context to agents
- ✅ Use `allowed-tools` to restrict capabilities
- ✅ Parse and validate `$ARGUMENTS`
- ✅ Handle errors gracefully

### DON'T:
- ❌ Let commands do the actual work (use agents)
- ❌ Pass vague prompts to agents
- ❌ Give commands unrestricted tools
- ❌ Assume agents have context
- ❌ Create complex multi-purpose commands

## The Command-Agent Relationship

```
Commands are like Product Managers:
- Understand the big picture
- Know the context and history
- Write detailed specifications

Agents are like Junior Developers:
- Execute specific tasks
- Follow detailed instructions
- Don't need context to work
```

## Testing Your Commands

### 1. Context Test
Create information in conversation, then use command.
Command should translate context correctly to agent.

### 2. Vague Input Test
Give minimal input: `/fix bug`
Command should enrich with context or ask for clarification.

### 3. Validation Test
Provide unexpected input: `/deploy with-typos`
Command should handle gracefully and provide helpful feedback.

## Common Anti-Patterns

### 1. Command Doing Too Much
❌ **Bad**: Command reads files, processes data, creates output
✅ **Good**: Command prepares prompt, agent does the work

### 2. Vague Agent Instructions
❌ **Bad**: "Handle the user's request about: $ARGUMENTS"
✅ **Good**: "Create GitHub issue with title: X, description: Y, labels: Z"

### 3. Unrestricted Tools
❌ **Bad**: `allowed-tools: [*]`
✅ **Good**: `allowed-tools: [Task, Bash(npm:test)]`

### 4. No Error Handling
❌ **Bad**: Assume agent will succeed
✅ **Good**: Check agent response, provide fallback

## Real-World Example: /issue Command

### User Input
```
/issue app crashes on startup
```

### Command Processing
1. **Receives**: "app crashes on startup"
2. **Enriches**: Adds context about app type, recent changes
3. **Structures**: Creates proper bug report format
4. **Invokes**: Sends detailed prompt to agent

### Agent Receives
```
Create GitHub issue:
Title: [BUG] Application crashes on startup
Description: The application fails to start with...
Labels: bug, high-priority
Template: bug-report
```

### Result
Professional GitHub issue created in seconds.

## Summary

Commands are the intelligent layer that makes agents useful. They:
1. **See everything** (full context)
2. **Translate intelligently** (user intent → agent instructions)
3. **Enforce boundaries** (restricted tools, validated input)
4. **Improve efficiency** (faster execution, fewer tokens)

The golden rule: **Commands think, agents do**.