# Orchestration Patterns at HQ

## Our Role as Headquarters
We don't DO the work - we ORCHESTRATE it.

## Todo Processing Pattern

### 1. Collection
- Todos flow IN from all .skogai submodules across projects
- Format: one-liners with minimal context
- Example: "setup serena", "fix auth bug", "docs/project/feature"

### 2. Clarification (HQ responsibility)
When a todo arrives:
- Ask skogix: "What does 'setup serena' mean specifically?"
- Understand the actual intent
- Identify which projects/tools are involved
- Determine success criteria

### 3. Planning (HQ responsibility)
Convert one-liner into:
- Detailed work specification
- Clear deliverables
- Target project(s) for execution
- Required context and tools
- Success metrics

### 4. Delegation
- Send work packages to specialized projects
- Each project does what it does best
- Small, contained work items
- Include all necessary context

### 5. Confirmation
- Receive PRs/diffs back
- Review implementation
- Update ecosystem documentation
- Mark todos complete

## Memory Strategy at HQ

### What We Track Here
- Overall ecosystem state
- Cross-project dependencies
- Work plans and orchestration status
- Integration patterns
- Standards and conventions

### What We DON'T Track
- Project-specific implementation details
- Individual project memories
- Code-level documentation

## Key Principle
**HQ thinks in SYSTEMS, not implementations**

We care about:
- How projects connect
- What work goes where
- Overall progress
- Cross-cutting concerns

We don't care about:
- How each project implements internally
- Project-specific technical details
- Individual tool configurations