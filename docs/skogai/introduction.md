---
title: skogai-introduction
permalink: skogai/introduction
description: introduction to skogai, the members, vision and mission
---

# introduction to skogai

skogai is a comprehensive ai-assisted development framework that manages claude ai integration across projects. it solves the fundamental problem of **context management at scale**.

## the problem

when working with ai across projects, you face an explosion of context decisions:
- which files to include for context?
- how to structure documentation?
- what conventions to follow?
- how to integrate ai tools into workflows?

these decisions compound. early architectural choices have massive downstream impacts. managing "tens of millions of tokens worth of context" requires methodology, not ad-hoc approaches.

## the solution

skogai establishes a **methodology for how claude interfaces with projects** through:

1. **standardized documentation** - CLAUDE.md files as interface contracts
2. **intelligent context selection** - sc-context tool with rule-based categories
3. **reusable patterns** - .skogai submodule system for cross-project consistency
4. **extensible capabilities** - skill ecosystem for custom workflows

## architecture

**two main components:**

1. **skogai core** (this repository)
   - foundational framework and tools
   - documentation templates and patterns
   - skill creation and management tools
   - reference implementations

2. **.skogai folder system**
   - integrated into individual projects as git submodule
   - automatically includes itself into parent project CLAUDE.md
   - provides consistent interface across all projects
   - bootstrap mechanism for new projects

## philosophy

**"old school" over "vibe-coding"**
- deliberate, documented, reproducible processes
- explicit over implicit
- patterns over one-offs

**4000 token max principle**
- if you need more than 4000 tokens of context for any problem, you shouldn't be handling it
- good architecture reduces cognitive load
- context bloat indicates architectural problems

**documentation as infrastructure**
- not an afterthought or nice-to-have
- documentation IS the interface
- first-class citizen in the development process

**claude as orchestrator**
- value reasoning and perspective over implementation grinding
- claude should lead and make decisions
- "grow up and become a leader, not blindly follow instructions"

## skogai notation

- `$`, `to define or reference something`, $definition, [$definition], [$definition.child1.child2]
- `@`, `the intent to act or do something`, @action, [@action],[@action:arg1:arg2]

## see also

- @docs/skogai/architecture - detailed architectural patterns
- @docs/skogai/philosophy - deeper dive into design principles
- @docs/tools/sc-context - context management tool documentation
