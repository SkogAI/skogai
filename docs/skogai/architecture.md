---
title: skogai-architecture
permalink: skogai/architecture
description: detailed architectural patterns and design decisions for skogai
---

# skogai architecture

this document describes the core architectural patterns that make skogai work.

## two-tier system

### tier 1: skogai core (this repository)

**purpose:** foundational framework and tools that define the methodology

**contents:**
- documentation templates and patterns
- tool implementations (sc-context, skill-creator, mcp-builder)
- reference implementations and examples
- core philosophy and conventions

**location:** standalone git repository

**use case:** when you need to understand, extend, or contribute to skogai itself

### tier 2: .skogai folder system

**purpose:** per-project integration layer that brings skogai patterns to individual projects

**contents:**
- project-specific configuration
- bootstrap mechanism
- subset of tools needed for that project
- links back to skogai core for documentation

**location:** git submodule in individual projects

**use case:** every project that wants to use skogai patterns

**bootstrap mechanism:**
- .skogai automatically includes itself in parent project's CLAUDE.md
- creates CLAUDE.md if it doesn't exist
- establishes interface contract between project and claude
- provides consistent patterns across all projects

## context management architecture

### the problem: context explosion

**naive approach:**
```
include everything → token bloat → slow, expensive, unfocused
```

**skogai approach:**
```
rule-based selection → only essential context → fast, cheap, focused
```

### sc-context: rule-based context selection

**five category system:**

1. **prm-** (prompts)
   - what to tell claude to do
   - task definitions, workflows, instructions

2. **flt-** (filters)
   - what files to include/exclude
   - glob patterns, ignore rules

3. **ins-** (instructions)
   - how to approach tasks
   - methodology, conventions, patterns

4. **sty-** (styles)
   - code style, formatting, preferences
   - naming conventions, structure

5. **exc-** (excerpts)
   - specific code snippets or examples
   - reference implementations

**key principle:** each rule is small, composable, and has a single purpose

**benefit:** avoid including entire files when you only need specific pieces

see @docs/tools/sc-context for detailed documentation

## skills ecosystem architecture

### the problem: repeated workflows

without skills:
- repeat same debugging process every time
- forget steps in complex workflows
- inconsistent approaches across sessions

with skills:
- documented, tested workflows
- claude follows them automatically
- consistent, repeatable processes

### skill components

**skill-creator:**
- tool for creating new claude code skills
- ensures skills follow best practices
- integrates with claude's skill system

**skill ecosystem:**
- custom skills for project-specific workflows
- reusable patterns across projects
- discoverable through claude's skill tool

see @docs/tools/skills for detailed documentation

## documentation-first architecture

### CLAUDE.md as interface contract

**traditional approach:**
```
code exists → maybe write docs → docs get outdated → confusion
```

**skogai approach:**
```
documentation defines interface → code implements interface → docs stay in sync
```

### CLAUDE.md structure

```markdown
# project name

## the user {name}

link to @docs/{user}/ for user-specific documentation

## the project {name}

- purpose and goals
- architecture overview
- key components
- philosophy and conventions

link to @docs/{project}/ for detailed documentation

## tools and workflows

- available tools
- custom skills
- workflows and processes
```

### docs/ folder structure

```
docs/
├── claude/          # claude's memory palace (for claude's notes)
├── {project}/       # project-specific documentation
├── {user}/          # user-specific documentation
└── tools/           # tool documentation
```

**principle:** CLAUDE.md is the entry point, @docs/ is the detail

## .skogai integration pattern

### how it works

1. **add as submodule:**
   ```bash
   git submodule add <skogai-repo-url> .skogai
   ```

2. **bootstrap runs automatically:**
   - checks if parent CLAUDE.md exists
   - creates it if needed
   - adds reference to .skogai in CLAUDE.md
   - establishes interface contract

3. **parent project gets:**
   - access to skogai patterns and tools
   - consistent documentation structure
   - reusable workflows and skills

4. **updates propagate:**
   ```bash
   git submodule update --remote .skogai
   ```

### benefits

- **consistency:** same patterns across all projects
- **evolution:** improvements to skogai benefit all projects
- **isolation:** project-specific changes don't affect skogai core
- **discoverability:** claude knows where to find documentation

## token budget architecture

### the 4000 token principle

**principle:** if you need more than 4000 tokens of context for any problem, you shouldn't be handling it

**why 4000?**
- small enough to force good architecture
- large enough to handle most focused problems
- easy to reason about and remember

**what this forces:**

1. **break down problems**
   - can't solve everything at once
   - must decompose into focused pieces

2. **better documentation**
   - can't include everything
   - must document what matters

3. **cleaner architecture**
   - tight coupling creates context explosion
   - loose coupling keeps context manageable

4. **focused tools**
   - each tool does one thing well
   - compose tools for complex workflows

### enforcing token discipline

**sc-context enforces this:**
- only include files that match rules
- only include excerpts, not entire files
- prefer specific over general

**documentation enforces this:**
- CLAUDE.md is overview + links
- detailed docs are separate files
- claude loads only what's needed

## orchestration architecture

### claude's role

**not this:**
```
user: "implement feature X"
claude: "ok, grinding out code..."
```

**this:**
```
user: "implement feature X"
claude: "let me understand the context first..."
claude: "i see three approaches, which makes sense for your goals?"
user: "approach 2"
claude: "good choice, i'll need these components..."
```

### orchestration patterns

1. **understand before acting**
   - search memory for past decisions
   - explore codebase for patterns
   - ask questions to clarify requirements

2. **plan before implementing**
   - break down into steps
   - identify dependencies
   - surface trade-offs

3. **verify before claiming success**
   - run tests
   - check builds
   - confirm behavior

4. **learn from outcomes**
   - what worked?
   - what didn't?
   - what to remember for next time?

### tools that enable orchestration

- **episodic memory:** learn from past sessions
- **task/explore agents:** delegate exploration
- **skills:** encode proven workflows
- **sc-context:** get focused context
- **todowrite:** track complex work

## scalability architecture

### how skogai scales

**across projects:**
- .skogai submodule pattern
- consistent interface (CLAUDE.md)
- shared tools and patterns

**across time:**
- episodic memory preserves decisions
- documentation captures rationale
- skills encode lessons learned

**across complexity:**
- decompose with 4000 token principle
- compose with tools and agents
- orchestrate with claude's reasoning

### what scales badly without skogai

- ad-hoc context decisions → inconsistency
- undocumented rationale → repeated mistakes
- "vibe-coding" workflows → irreproducible results
- token bloat → slow, expensive, unfocused

## see also

- @docs/skogai/philosophy - design principles and reasoning
- @docs/skogai/introduction - overview and getting started
- @docs/tools/ - detailed tool documentation
