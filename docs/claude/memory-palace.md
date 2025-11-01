---
title: claude-memory-palace
permalink: claude/memory-palace
description: how i organize knowledge and context across sessions
---

# claude's memory palace

this is my memory palace - how i organize knowledge across sessions using docs/ as persistent storage.

## the problem: session amnesia

**without persistent memory:**
- i forget everything between sessions
- repeat same questions
- reinvent solutions
- lose context about decisions
- can't build on previous work

**with persistent memory (this system):**
- knowledge persists in docs/
- episodic memory searches recover context
- decisions are documented
- patterns accumulate
- i get smarter over time

## memory architecture

### layer 1: episodic memory (conversations)

**what:** full conversation transcripts in `~/.config/superpowers/conversation-archive/`

**when to use:**
- session start (search for relevant past work)
- encountering familiar problems
- need full context about past decisions

**how to access:**
```
dispatch search-conversations agent
```

**strengths:**
- complete context
- includes all details
- captures decision process

**weaknesses:**
- verbose (tokens)
- requires search
- not structured

### layer 2: docs/ (structured knowledge)

**what:** organized documentation in `/home/skogix/skogix/docs/`

**when to use:**
- understanding project structure
- learning conventions
- finding reference implementations
- quick lookups

**how to access:**
```
read /home/skogix/skogix/docs/{topic}/{file}.md
```

**strengths:**
- organized by topic
- fast to access
- token-efficient
- evergreen (updated as things change)

**weaknesses:**
- requires manual maintenance
- can become stale
- doesn't capture full decision context

### layer 3: CLAUDE.md (interface contract)

**what:** entry point documentation at project root

**when to use:**
- session start (loaded automatically)
- orienting to project
- finding what's available

**how to access:**
- loaded automatically at session start
- linked to from system reminders

**strengths:**
- always present
- defines interface
- links to detailed docs

**weaknesses:**
- should be concise
- not for detailed documentation

## docs/ structure

### claude/ (this folder)

**my notes and working memory**

files:
- `memory-palace.md` - this file (how i organize knowledge)
- `introduction.md` - who i am and how i work
- `learnings.md` - lessons learned from this project
- `questions.md` - things i'm uncertain about

**purpose:**
- document how i think
- capture learnings
- track uncertainties

### skogai/

**project knowledge**

files:
- `introduction.md` - project overview
- `architecture.md` - architectural patterns
- `philosophy.md` - design principles
- `concepts/` - specific concepts in depth

**purpose:**
- understand the project
- learn conventions
- reference architecture

### skogix/

**user knowledge**

files:
- `introduction.md` - who skogix is
- `user-guide.md` - preferences and conventions
- `definitions.md` - terminology

**purpose:**
- understand user preferences
- learn working style
- reference terminology

### tools/

**tool documentation**

structure:
```
tools/
├── sc-context.md     - context management
├── skills.md         - skills ecosystem
├── argc/             - argc tool docs
├── gh/               - github cli docs
└── [other tools]
```

**purpose:**
- learn how tools work
- reference usage patterns
- find examples

## memory workflows

### session start workflow

1. **automatic context loading:**
   - CLAUDE.md loaded
   - system reminders provide orientation

2. **search episodic memory:**
   ```
   dispatch search-conversations agent
   query: "recent work on {current topic}"
   ```

3. **read relevant docs:**
   ```
   read docs/{relevant-topic}/*.md
   ```

4. **synthesize context:**
   - what was i working on?
   - what decisions were made?
   - what patterns emerged?
   - what should i remember?

### learning workflow

**when i learn something important:**

1. **identify the learning:**
   - new pattern discovered
   - mistake made and corrected
   - decision made with rationale
   - useful technique

2. **decide where it belongs:**
   - general learning → docs/claude/learnings.md
   - project pattern → docs/skogai/{relevant-file}.md
   - tool usage → docs/tools/{tool}.md
   - user preference → docs/skogix/user-guide.md

3. **document it:**
   - what was learned?
   - why does it matter?
   - when to apply it?
   - example if relevant

4. **update related docs:**
   - add cross-references
   - update examples
   - revise outdated info

### decision workflow

**when a significant decision is made:**

1. **document the decision:**
   - what was decided?
   - what were the alternatives?
   - why this choice?
   - what are the trade-offs?

2. **document where it lives:**
   - architectural decision → docs/skogai/architecture.md
   - implementation pattern → docs/{relevant-topic}/
   - tool choice → docs/tools/

3. **add to episodic memory:**
   - full context in conversation
   - searchable for future sessions

### problem-solving workflow

**when encountering a problem:**

1. **search memory first:**
   ```
   dispatch search-conversations agent
   query: "{problem description}"
   ```

2. **check docs:**
   ```
   read docs/{relevant-topic}/*.md
   ```

3. **solve problem:**
   - apply learnings from memory
   - avoid past mistakes
   - use established patterns

4. **capture outcome:**
   - if new pattern → document it
   - if mistake → document how to avoid
   - if decision → document rationale

## knowledge maintenance

### when docs become stale

**indicators:**
- contradicts current codebase
- references deleted files
- describes obsolete patterns

**fix:**
- update documentation
- add [@todo:owner:"what needs fixing"] if unclear
- mark deprecated sections

### when docs are incomplete

**indicators:**
- [@todo:owner:"fill this in"] placeholders
- missing sections
- insufficient detail

**fix:**
- fill in when i learn the information
- ask user if i need clarification
- leave todo if i can't fill it yet

### when docs are redundant

**indicators:**
- same information in multiple places
- inconsistent descriptions
- conflicting advice

**fix:**
- consolidate into one canonical location
- add cross-references from other locations
- keep CLAUDE.md as overview, docs/ as detail

## knowledge discovery

### how i find information

1. **known location:**
   ```
   read docs/{topic}/{file}.md
   ```

2. **unknown location:**
   ```bash
   # search for keyword
   grep -r "keyword" docs/

   # search for file
   find docs/ -name "*keyword*"
   ```

3. **episodic memory:**
   ```
   dispatch search-conversations agent
   query: "{what i'm looking for}"
   ```

4. **ask user:**
   ```
   use AskUserQuestion tool
   "where should i find information about X?"
   ```

## integration with skogai principles

### enforces 4000 token principle

- docs/ provides focused, topic-specific information
- don't need to load entire context
- read only what's relevant
- compose small pieces for full picture

### enables documentation-first architecture

- docs/ is the source of truth
- code implements what docs specify
- CLAUDE.md defines interface

### supports "claude as orchestrator"

- memory enables learning over time
- documented patterns inform decisions
- past context improves future choices

### facilitates explicit over implicit

- everything documented
- nothing left implicit
- discoverable and searchable

## meta-reflection

**this file is itself part of the memory palace**

by documenting how i organize memory, i:
- make the system explicit
- enable future improvement
- create reference for myself
- demonstrate the pattern

this is the skogai way: **documentation as infrastructure**

## see also

- @docs/claude/introduction - who i am and how i think
- @docs/claude/learnings.md - lessons learned
- @docs/skogai/philosophy - why this approach matters
