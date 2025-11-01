---
title: claude-questions
permalink: claude/questions
description: things i'm uncertain about and need to learn
---

# questions

this file tracks things i'm uncertain about or don't fully understand yet. as i learn answers, i'll move them to learnings.md.

## about sc-context

### ~~how is sc-context actually implemented?~~ ✓ ANSWERED

**answer:** python-based tool with markdown files (yaml frontmatter) for rules

- installed at `/home/skogix/.local/bin/sc-context`
- rules stored in `.sc-context/rules/` (built-in in `sc/` subdirectory)
- tracks state in `.sc-context/curr_ctx.yaml` and `.sc-context/sc-state.yaml`
- uses jinja2 templates for rendering context

**see:** docs/claude/learnings.md for detailed notes

### ~~how does sc-context rule storage work?~~ ✓ ANSWERED

**answer:** rules are markdown files with yaml frontmatter in `.sc-context/rules/`

**structure:**
```
.sc-context/
├── config.yaml          # template configuration
├── curr_ctx.yaml        # current selections per profile
├── sc-state.yaml        # state tracking
└── rules/
    ├── sc/              # built-in rules (prm-, flt-, ins-, sty-, exc-)
    └── [user rules]     # project-specific rules
```

**built-in rules discovered:**
- `prm-developer`, `prm-rule-create` - prompt rules
- `flt-base`, `flt-no-files`, `flt-no-full`, `flt-no-outline` - filter rules
- `exc-base` - excerpting rules (code outlining)
- `ins-developer`, `ins-rule-framework`, `ins-rule-intro` - instruction rules
- `sty-code`, `sty-javascript`, `sty-jupyter`, `sty-python` - style rules

### what's the token counting mechanism?

**question:** how does sc-context actually count tokens? is it exact or approximate?

**observation:** when i ran `sc-context -p`, it reported "302.7 KB" - this is bytes, not tokens

**why it still matters:**
- need to understand the relationship between KB and tokens
- approximately 4 bytes per token (rough estimate)
- 302KB ≈ 75k tokens (still under claude's context window!)
- helps enforce 4000 token principle

**follow-up:** does sc-context have a token counting feature?

## about skill-creator and mcp-builder

### are these implemented yet?

**question:** do skill-creator and mcp-builder actually exist as tools, or are they concepts to be built?

**context:**
- i've documented them based on architectural vision
- conversation history suggests they're being worked on
- don't know current implementation status

**what i need:**
- see actual implementations if they exist
- understand their current capabilities
- know what's planned vs what's done

### how do they integrate with claude code?

**question:** what's the integration mechanism between these tools and claude code's skill system?

**specifically:**
- how are skills registered?
- how does claude discover them?
- how are mcp servers connected?

## about .skogai integration

### what's the bootstrap mechanism exactly?

**question:** how does .skogai automatically include itself in parent CLAUDE.md?

**possibilities:**
- git hook?
- init script?
- manual step in workflow?

**why it matters:**
- need to document it accurately
- understand when/how it runs
- know what to expect

### how are updates propagated?

**question:** when skogai core is updated, how do .skogai submodules get those updates?

**is it:**
- manual `git submodule update`?
- automatic on pull?
- periodic sync script?

## about permissions and auto-approval

### how do auto-approvals work?

**question:** i see in user-guide.md that certain bash commands are auto-approved (git, gh, etc.). how is this configured?

**specifically:**
- where are auto-approval rules defined?
- how are they updated?
- what's the mechanism?

**reference:**
- docs/skogix/user-guide.md:136 mentions `bash(gh:*)` and `bash(git:*)` are auto-approved
- [@todo:claude:"ask skogix about how his tools actually work behind the scenes when it comes to permissions, agents and especially cache and cache-solutions"]

### what are "basic permissions"?

**question:** user-guide.md:37 mentions "basic permissions might update this" - what are basic permissions?

**context:**
- seems related to tool auto-approval
- might be a claude code feature
- might be skogai-specific

## about caching and performance

### how does caching work in the tools?

**question:** conversation search mentioned "cache and cache-solutions" - what caching is in place?

**areas of interest:**
- episodic memory caching?
- sc-context result caching?
- mcp server caching?

**why it matters:**
- understand performance characteristics
- know when to expect fresh vs cached data
- properly document behavior

### what are the performance characteristics?

**question:** how do tools perform at scale?

**specifically:**
- sc-context on large codebases?
- episodic memory with thousands of conversations?
- skill discovery with many skills?

## about skogai history and evolution

### what's the full history?

**question:** how did skogai evolve to its current state?

**what i know:**
- recent "big restart" mentioned in conversation history
- evolved from earlier iterations
- continuous refinement of patterns

**what i want to know:**
- what were earlier versions like?
- what lessons led to current design?
- what didn't work and was changed?

### what's the roadmap?

**question:** where is skogai headed?

**areas of interest:**
- planned features
- expected evolution
- stability vs experimentation

## about working with skogix

### what are the collaboration patterns?

**question:** what working patterns has skogix established?

**what i know:**
- values reasoning over implementation
- prefers "old school" approach
- focused on context efficiency

**what i want to learn:**
- preferred communication style
- how to best surface options
- when to ask vs proceed

### what are the pet peeves?

**question:** what patterns does skogix particularly dislike?

**why it matters:**
- avoid frustration
- work more effectively
- demonstrate understanding

## about current state

### what's the current project state?

**question:** where are we in the skogai development lifecycle?

**areas:**
- which components are stable?
- what's experimental?
- what's next to be worked on?

### what's most important right now?

**question:** what should i focus on or prioritize?

**context:**
- documentation seems to be priority (this work)
- but what else is critical?

## how to resolve these questions

### search conversation history

many answers probably exist in episodic memory:

```
dispatch search-conversations agent
query: "{specific question}"
```

### read actual implementations

```bash
# find tool implementations
find /home/skogix/skogix -name "*sc-context*"
find /home/skogix/skogix -name "*skill-creator*"

# read them
read {file-path}
```

### ask skogix directly

use AskUserQuestion tool when:
- can't find answer in memory/code
- need clarification on preferences
- want to confirm understanding

### explore codebase

use explore agent for:
- understanding tool implementations
- finding related code
- discovering patterns

## meta-note

**this file is a working document**

as i learn answers, i will:
1. move the learning to learnings.md
2. remove or update the question here
3. add new questions as they arise

this is itself a demonstration of skogai's explicit-over-implicit principle.

## see also

- @docs/claude/learnings.md - lessons learned (where answers end up)
- @docs/claude/memory-palace.md - how i organize knowledge
- @docs/skogix/user-guide.md - skogix's working conventions
