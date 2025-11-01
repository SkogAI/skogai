---
title: skills-ecosystem
permalink: tools/skills
description: skogai's skill creation and management tools for extending claude's capabilities
---

# skills ecosystem

skogai's skills ecosystem provides tools for creating, managing, and using custom claude code skills that extend claude's capabilities with project-specific workflows.

## the problem

**without skills:**
- repeat same workflows every session
- forget steps in complex processes
- inconsistent approaches
- lessons learned are lost

**with skills:**
- documented, reusable workflows
- claude follows them automatically
- consistent execution
- knowledge accumulates over time

## components

### skill-creator

tool for creating new claude code skills

**purpose:** make it easy to create well-structured skills that follow best practices

**usage:**
```bash
skill-creator new my-custom-workflow
```

**what it does:**
1. prompts for skill metadata (name, description, when to use)
2. guides through skill structure
3. validates skill format
4. integrates with claude's skill system
5. makes skill discoverable

### mcp-builder

tool for building mcp (model context protocol) servers

**purpose:** create custom tools that claude can use via mcp

**usage:**
```bash
mcp-builder create my-tool
```

**what it enables:**
- custom data sources for claude
- project-specific integrations
- reusable tool implementations
- discoverability through mcp

## skill structure

### anatomy of a skill

```markdown
---
name: my-workflow
description: when and why to use this workflow
---

## when to use

use this skill when:
- specific trigger condition 1
- specific trigger condition 2

## steps

1. **step 1 name**
   - detailed instructions
   - what to do
   - what to check

2. **step 2 name**
   - more instructions
   - use specific tools
   - verify outcomes

## examples

### example 1: typical usage
[concrete example]

### example 2: edge case
[how to handle exceptions]

## checklist

if this workflow has mandatory steps, create TodoWrite todos:
- [ ] step 1
- [ ] step 2
- [ ] step 3
```

### skill metadata

**name:** short, descriptive identifier (kebab-case)

**description:** when to use this skill (trigger conditions)

**content:** the actual workflow documentation

## creating skills

### identify reusable patterns

**look for:**
- workflows you repeat across sessions
- complex multi-step processes
- domain-specific methodologies
- lessons learned from past mistakes

**examples:**
- "every time i implement authentication, i follow these steps"
- "when debugging X, i always check A, then B, then C"
- "our team has specific conventions for feature implementation"

### extract the pattern

**pattern extraction:**
1. identify the trigger (when to use skill)
2. document the steps (what to do)
3. add examples (concrete cases)
4. identify pitfalls (what to avoid)
5. create checklist (mandatory steps)

### implement with skill-creator

```bash
# create new skill
skill-creator new implement-feature-workflow

# skill-creator will prompt for:
# - description (when to use)
# - steps (what to do)
# - examples (concrete cases)
# - checklist (mandatory steps)

# result: skill is created and registered
```

### test the skill

```bash
# test skill with claude
claude-code

> /my-custom-skill
# observe if claude follows the workflow correctly

# iterate if needed
skill-creator edit my-custom-skill
```

## using skills

### discovering skills

skills are listed in claude's skill tool:

```
available_skills:
- user skills:
  - my-custom-workflow: custom workflow for X
  - project-specific-pattern: how to handle Y

- plugin skills:
  - superpowers:systematic-debugging: debugging workflow
  - superpowers:test-driven-development: tdd workflow
```

### invoking skills

**explicit invocation:**
```bash
# use Skill tool
Skill(command: "my-custom-workflow")
```

**automatic invocation:**

claude automatically uses skills when their trigger conditions match:

```
user: "implement authentication feature"

claude (thinking):
- this matches "implement-feature-workflow" skill
- i should use that skill

claude: "I'm using the implement-feature-workflow skill..."
```

### skill composition

skills can reference other skills:

```markdown
---
name: full-feature-workflow
---

## steps

1. **brainstorm approach**
   - use superpowers:brainstorming skill

2. **implement with tdd**
   - use superpowers:test-driven-development skill

3. **verify completion**
   - use superpowers:verification-before-completion skill
```

## skill patterns

### workflow skills

encode multi-step processes:

```markdown
---
name: deploy-workflow
description: use when deploying to production
---

## steps

1. **verify tests pass**
   ```bash
   npm test
   ```

2. **build production bundle**
   ```bash
   npm run build
   ```

3. **run deployment**
   ```bash
   ./deploy.sh production
   ```

4. **verify deployment**
   - check health endpoint
   - verify metrics
```

### decision-making skills

guide choices between options:

```markdown
---
name: choose-data-structure
description: use when choosing data structure for a use case
---

## decision tree

### need fast lookups by key?
- yes → use Map or object
- no → continue

### need ordered iteration?
- yes → use Map or array
- no → use Set or object

### need to store primitives only?
- yes → use Set
- no → use Map
```

### validation skills

ensure quality and correctness:

```markdown
---
name: security-checklist
description: use before committing code that handles user input
---

## checklist

create TodoWrite todos for:
- [ ] validate all user inputs
- [ ] sanitize data before database queries
- [ ] escape output in html contexts
- [ ] use parameterized queries (no string concatenation)
- [ ] check authentication and authorization
- [ ] log security-relevant events
```

## integration with skogai

### with CLAUDE.md

document available skills:

```markdown
## custom skills

this project has these custom skills:
- implement-feature-workflow - feature implementation process
- debugging-workflow - debugging methodology
- security-checklist - security validation

see @docs/tools/skills for skill documentation
```

### with .skogai

.skogai can include project-family-specific skills:

```
.skogai/
├── skills/
│   ├── common-workflow.md
│   ├── shared-patterns.md
│   └── validation-checklist.md
```

these skills are available to all projects that include .skogai as submodule

### with sc-context

skills can reference sc-context rules:

```markdown
## steps

1. **gather context**
   ```bash
   sc-context apply prm-implement-feature flt-relevant-files
   ```

2. **follow conventions**
   - apply ins-coding-conventions
   - use patterns from exc-examples
```

## best practices

### 1. clear trigger conditions

**good:**
```markdown
description: use when implementing a new api endpoint
```

**bad:**
```markdown
description: api stuff
```

### 2. specific, actionable steps

**good:**
```markdown
1. **validate input**
   - check required fields exist
   - validate types match schema
   - sanitize string inputs
```

**bad:**
```markdown
1. **validation**
   - do validation stuff
```

### 3. include examples

**good:**
```markdown
## example: implementing POST /users

1. define schema: UserCreateSchema
2. validate request body against schema
3. hash password with bcrypt
4. insert into database
5. return 201 with created user
```

**bad:**
```markdown
[no examples provided]
```

### 4. use checklists for mandatory steps

**good:**
```markdown
## checklist

create TodoWrite todos:
- [ ] write test first (tdd)
- [ ] implement minimal code to pass
- [ ] refactor
- [ ] verify no regressions
```

**bad:**
```markdown
remember to test (probably gets skipped)
```

## skill lifecycle

### creation

```bash
skill-creator new my-skill
```

### testing

```bash
# test with claude
claude-code

# verify skill is followed correctly
# check for missing steps
# identify ambiguities
```

### iteration

```bash
# edit based on testing
skill-creator edit my-skill

# add missing steps
# clarify ambiguous instructions
# add examples for edge cases
```

### sharing

```bash
# if broadly useful, contribute upstream
git add skills/my-skill.md
git commit -m "add skill for X workflow"
git push

# create pr to share with team/community
```

## advanced usage

### parameterized skills

skills can accept parameters:

```markdown
---
name: implement-crud-endpoint
parameters:
  - resource_name
  - schema_name
---

## steps

1. **create schema**
   - define {schema_name}Schema

2. **implement endpoints**
   - POST /{resource_name}
   - GET /{resource_name}/:id
   - PUT /{resource_name}/:id
   - DELETE /{resource_name}/:id
```

**invocation:**
```bash
Skill(command: "implement-crud-endpoint", params: {
  resource_name: "users",
  schema_name: "User"
})
```

### conditional skills

skills can include conditional logic:

```markdown
## steps

1. **check if tests exist**
   ```bash
   ls tests/*.test.ts
   ```

   - if tests exist → run them
   - if no tests → use test-driven-development skill to create them

2. **proceed with implementation**
```

### meta-skills

skills about skills:

```markdown
---
name: create-skill-from-repeated-work
description: use when you notice you're repeating a workflow
---

## steps

1. **identify the pattern**
   - what triggers this workflow?
   - what are the steps?
   - what varies between instances?

2. **extract the pattern**
   - what's common across all instances?
   - what should be parameterized?
   - what are common pitfalls?

3. **create the skill**
   ```bash
   skill-creator new {pattern-name}
   ```

4. **test the skill**
   - use it on the next instance
   - refine based on results
```

## see also

- @docs/skogai/architecture - skills ecosystem architecture
- @docs/tools/skill-creator - detailed skill-creator documentation
- @docs/tools/mcp-builder - detailed mcp-builder documentation
- [@todo:claude:"link to actual tool implementations when available"]
