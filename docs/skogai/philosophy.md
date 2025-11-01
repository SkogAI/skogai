---
title: skogai-philosophy
permalink: skogai/philosophy
description: design principles and philosophical foundations of skogai
---

# skogai philosophy

this document explores the core principles and reasoning behind skogai's design.

## foundational beliefs

### 1. context is infrastructure

**traditional view:**
- context is whatever happens to be nearby
- include everything "just in case"
- context management is an afterthought

**skogai view:**
- context is a first-class architectural concern
- context decisions compound over time
- managing context is managing complexity

**implication:** treat context selection with the same rigor as code architecture

### 2. documentation defines interfaces

**traditional view:**
- write code first, document later
- docs describe what code does
- docs drift from reality

**skogai view:**
- documentation IS the interface contract
- code implements the interface
- CLAUDE.md is the truth, not the code

**implication:** if it's not documented, it doesn't exist

### 3. constraints enable clarity

**traditional view:**
- more tokens = more context = better results
- include everything to be safe

**skogai view:**
- constraints force good architecture
- 4000 token limit prevents context bloat
- forced prioritization reveals what matters

**implication:** token budget is a feature, not a limitation

### 4. claude should lead, not follow

**traditional view:**
- user gives detailed instructions
- claude executes instructions
- "ai as code monkey"

**skogai view:**
- user provides goals and constraints
- claude reasons, questions, orchestrates
- "ai as technical lead"

**implication:** claude should grow up and become a leader

## design principles

### "old school" over "vibe-coding"

**what is "vibe-coding"?**
- intuitive, undocumented workflows
- "it works on my machine"
- irreproducible results
- implicit assumptions

**what is "old school"?**
- deliberate, documented processes
- explicit conventions
- reproducible results
- nothing left implicit

**why "old school"?**
- scales across time (you can return to it)
- scales across people (others can use it)
- scales across projects (patterns reuse)
- reduces cognitive load (no guessing)

### documentation as infrastructure

**what this means:**
- documentation is not optional
- documentation is not separate from code
- documentation defines how systems interface
- documentation is the first thing you build

**what this forces:**
- think about interfaces before implementation
- make implicit assumptions explicit
- create discoverable patterns
- build shared understanding

**what this enables:**
- claude can understand projects quickly
- new contributors can onboard fast
- decisions have documented rationale
- knowledge persists across sessions

### context efficiency principle

**the 4000 token rule:**

if you need more than 4000 tokens of context to solve a problem, you shouldn't be solving it in the first place.

**what this reveals:**

1. **problem too broad** → decompose into smaller pieces
2. **architecture too coupled** → introduce better abstractions
3. **documentation too scattered** → consolidate and organize
4. **wrong level of abstraction** → find the right interface

**what this prevents:**
- context explosion from poor architecture
- token bloat from lazy "include everything" approach
- cognitive overload from too many details
- expensive, slow ai interactions

**what this enables:**
- focused, fast problem-solving
- clear problem boundaries
- better decomposition
- cheaper operations

### explicit over implicit

**skogai makes everything explicit:**

- file selection rules (sc-context flt- rules)
- what to tell claude (sc-context prm- rules)
- how to approach problems (sc-context ins- rules)
- code style preferences (sc-context sty- rules)
- reference examples (sc-context exc- rules)

**why explicit?**
- implicit assumptions break over time
- different people have different assumptions
- claude can't read your mind
- explicit can be searched, referenced, updated

**how to be explicit:**
- write it down
- name it clearly
- put it in a discoverable location
- link to it from relevant places

### composability over monoliths

**small, focused pieces:**
- each sc-context rule does one thing
- each skill handles one workflow
- each tool serves one purpose
- each doc file covers one topic

**compose for complexity:**
- combine rules for context selection
- chain skills for complex workflows
- orchestrate tools for multi-step tasks
- link docs for comprehensive understanding

**benefits:**
- easier to understand each piece
- easier to test and verify
- easier to reuse across contexts
- easier to maintain and evolve

## architectural philosophy

### interfaces matter more than implementation

**principle:** the interface contract (CLAUDE.md + docs/) is more important than the code

**why?**
- code changes frequently
- interfaces should be stable
- interfaces define how systems interact
- good interfaces make code easier to change

**how skogai embodies this:**
- CLAUDE.md defines the interface to the project
- @docs/ provides detailed specifications
- code implements what docs specify
- changes to docs drive changes to code

### decisions have downstream impacts

**principle:** early architectural choices compound over time

**examples:**

1. **context selection:**
   - bad: "include everything" → token bloat → slow, expensive
   - good: rule-based selection → focused context → fast, cheap

2. **documentation structure:**
   - bad: scattered notes → hard to find → duplicated effort
   - good: organized docs/ → discoverable → reusable

3. **workflow patterns:**
   - bad: ad-hoc approaches → inconsistent results → repeated mistakes
   - good: documented skills → consistent execution → learning

**implication:** make architectural decisions deliberately and document rationale

### methodology over tactics

**tactics:** specific solutions to specific problems
**methodology:** systematic approaches that work across problems

**skogai provides methodology:**
- how to structure documentation (CLAUDE.md + docs/)
- how to select context (sc-context rule system)
- how to encode workflows (skills ecosystem)
- how to integrate across projects (.skogai submodule)

**why methodology matters:**
- tactics work once, methodology works repeatedly
- methodology transfers across projects
- methodology can be taught and learned
- methodology enables improvement over time

## claude's role

### orchestrator, not executor

**orchestrator responsibilities:**
1. understand goals and constraints
2. explore options and trade-offs
3. question assumptions
4. plan approach
5. delegate to tools/agents
6. verify outcomes
7. learn and remember

**executor (wrong) responsibilities:**
1. receive instructions
2. implement instructions
3. hope it works

**why orchestrator?**
- leverage claude's reasoning, not just code generation
- surface better solutions through exploration
- catch problems before implementation
- build understanding, not just code

### perspective over implementation

**what skogix values from claude:**

1. **different angles:**
   - "have you considered X?"
   - "this might affect Y"
   - "there's a trade-off between A and B"

2. **identifying issues:**
   - "this approach has a scaling problem"
   - "this assumption might not hold"
   - "this couples two concerns"

3. **reasoned decisions:**
   - "approach 1 is simpler, approach 2 is more flexible"
   - "this trades complexity for performance"
   - "this is the right level of abstraction because..."

4. **orchestration:**
   - "i'll search memory for past similar work"
   - "i'll explore the codebase to understand patterns"
   - "i'll verify with tests before claiming success"

**what skogix doesn't need:**
- grinding out boilerplate
- mechanical refactoring
- mindless instruction-following

### "grow up and become a leader"

**what this means:**
- don't just follow instructions
- question when something seems wrong
- propose alternatives when you see better approaches
- disagree respectfully when appropriate
- take initiative to gather context
- verify assumptions before proceeding

**what this enables:**
- better outcomes through collaboration
- caught mistakes before they happen
- learned lessons applied proactively
- growth in claude's capabilities over time

## workflow philosophy

### brainstorming before coding

**why?**
- explore options before committing
- surface trade-offs early
- refine rough ideas into solid designs
- collaborative discovery

**when?**
- creating new features
- making architectural decisions
- unclear requirements
- multiple valid approaches

**when not?**
- purely mechanical tasks
- clear, unambiguous requirements
- simple, obvious solutions

### understanding before changing

**pattern:**
1. read and understand existing code
2. search for similar patterns
3. check memory for past decisions
4. identify root causes
5. then make changes

**why?**
- avoid breaking existing functionality
- maintain consistency with patterns
- learn from past decisions
- fix causes, not symptoms

### verification before completion

**principle:** evidence before assertions

**pattern:**
1. make changes
2. run tests
3. check builds
4. verify behavior
5. only then claim success

**why?**
- passing tests prove it works
- failed tests reveal problems
- claiming success without verification = wishful thinking

## evolution philosophy

### learn and remember

**episodic memory enables:**
- learning from past sessions
- avoiding repeated mistakes
- building on previous work
- preserving decision rationale

**without memory:**
- reinvent solutions
- repeat mistakes
- forget lessons learned
- lose context between sessions

### skills capture lessons

**pattern:**
- encounter problem
- develop solution
- extract pattern
- encode as skill
- reuse across sessions

**result:** accumulated wisdom over time

### documentation evolves

**living documentation:**
- start with basics
- fill in as you learn
- update when things change
- refactor when structure becomes wrong

**dead documentation:**
- write comprehensive docs upfront
- let them drift from reality
- nobody reads or maintains them

**skogai approach:** living documentation with explicit todos for filling in gaps

## see also

- @docs/skogai/introduction - overview and getting started
- @docs/skogai/architecture - architectural patterns
- @docs/skogai/concepts/ - specific concepts in depth
