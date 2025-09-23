# skogai ecosystem vision

## core concept

a unified coordination layer for ai agents across all development projects, enabling persistent context, shared knowledge, and seamless collaboration between different ai tools and assistants.

## the problem

- many ai agents works on many projects - all needing different integrations, context and instructions
- each project requires manual setup and context building - many times identical in nature
- no standardized way to share project knowledge, tools and instructions between different projects
- repetitive explanations of user preferences and project conventions

## the solution

skogai provides a git-based, version-controlled system for:

- persistent project documentation that ai agents can reference
- user preferences that apply across all projects
- standardized project structures and conventions
- coordination between multiple ai tools (claude, serena, aider, etc.)

## ecosystem components

### skogai (the main git repository hub)

- where everything gets orchestrated from
- contains "static information" such as user preferences, global todos, documentation standards and show the "big picture" of everything skogai related
- version controlled for consistency

### .skogai (this submodule)

- shared across all projects via git submodule
- build upon and from the main skogai repository but specialized in "bootstrapping and setting up projects"
- version controlled as well as specialized in setting up a branch specialized for the project in question - while still being able to pull in updates from the main .skogai repo
- was made as the "dotfiles for skogai" just as "$HOME/.config/" is the dotfiles for a users home directory

### serena mcp

- project-specific dynamic memory
- symbolic code understanding
- handles the "working memory" of current tasks

### skogai-memory mcp (planned)

- long-term memory persistence
- cross-conversation context retention
- project history and decisions

### skogai-reasoning mcp (planned)

- enhanced thinking and planning capabilities
- complex task decomposition
- architectural decision support

## workflow philosophy

1. **capture**: quick one-liners in .skogai/todo
2. **plan**: expand items into detailed plans when starting work
3. **orchestrate**: delegate work items, tasks and the needed context and tools to the agents/projects where they belong
4. **confirm**: get back PR's, git diffs or in other ways "confirm the implementation" in the main skogai repo
5. save learnings back to memories/documentation

## success metrics

- consistent code style across all projects
- reduced cognitive load for human developers
- small, contained and specalized work items goes into specialized projects

