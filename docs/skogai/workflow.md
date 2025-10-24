---
title: skogai/workflow
description: Workflow patterns and best practices for managing tasks and projects within the SkogAI ecosystem.
---

# skogai workflow patterns

## todo → planning → execution workflow

### 1. capture phase (.skogai/todo)

quick one-liner todos dumped into _any .skogai/todo_ from any project without much context.
these are meant to be:

- fast to write
- minimal cognitive load
- cross-project
- git-tracked for history
- maintained and gathered in the main skogai project

example:

```
- [ ] setup <tool_name>
- [ ] docs/<project>/<concept>
```

### 2. planning phase

when orchestrating a todo item:

1. take all items from .skogai/todo
2. create/update `current_objectives.md` in your task manager
3. propose a generalized and generic proposal to skogix together with:
   - questions clarifying the intention behind the changes
   - related context needed
   - skogai projects involved

## memory vs documentation

### memory

- project-specific details
- dynamic, changes during work per project
- technical implementation details
- current state and progress
- "working memory" of the project

### .skogai documentation

- cross-project standards
- user preferences
- ecosystem vision
- stable patterns and workflows
- "long-term memory" of the ecosystem

## example: "setup serena" expansion [TODO:find better and universal examples]

**original todo**: `- [ ] setup serena`

**expanded in current_objectives.md**:

- what: integrate serena mcp for code analysis
- why: need persistent project memory
- how: activate project, create memories, establish patterns
- success: clear separation of concerns documented

this pattern keeps todos lightweight while ensuring proper planning when work begins.
