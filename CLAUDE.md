# CLAUDE.md

## the user Skogix

the document @docs/skogix/user.md tells you more about `Skogix` and the the path `@docs/skogix` contains more user-related documentation.

## the project SkogAI

SkogAI is a comprehensive AI-assisted development framework that manages Claude AI integration across projects. It solves the problem of **context management at scale** - handling the tens of millions of tokens worth of decisions that compound over time.

**core purpose:** establish a methodology for how Claude interfaces with projects through standardized documentation, configuration, and environment management.

**architecture:** two main components:
- **skogai core** - the foundational framework (this repository)
- **.skogai folder system** - integrated into individual projects as a git submodule

**key components:**
- **sc-context** - intelligent context management tool with rule-based categories
- **skills ecosystem** - skill-creator and mcp-builder for extending capabilities
- **documentation-first architecture** - CLAUDE.md files as interface contracts

**philosophy:**
- "old school" over "vibe-coding" - deliberate, documented, reproducible
- 4000 token max principle - good architecture reduces cognitive load
- documentation as infrastructure - not an afterthought
- claude as orchestrator - reasoning and perspective over grinding code

see @docs/skogai/ for detailed architecture, philosophy, and component documentation.
