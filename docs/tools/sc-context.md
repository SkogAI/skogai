---
title: sc-context
permalink: tools/sc-context
description: intelligent context management tool with rule-based categories
---

# sc-context

sc-context is skogai's intelligent context management tool that solves the problem of **what to include in claude's context** through a rule-based system.

## the problem

**naive approach:**
```bash
# include everything
cat src/**/*.ts > context.txt  # ← token bloat!
```

**problems:**
- includes irrelevant code
- wastes tokens on unnecessary details
- slows down ai processing
- increases costs
- reduces focus

## the solution

**rule-based selection:**
```bash
# include only what matches rules
sc-context apply prm-authentication flt-api-files ins-rest-conventions
```

**benefits:**
- includes only relevant code
- focused context
- fast processing
- lower costs
- better results

## architecture

### five category system

sc-context uses five rule categories, each with a specific purpose:

#### 1. prm- (prompts)

**what to tell claude to do**

examples:
- `prm-implement-feature` - instructions for implementing a feature
- `prm-fix-bug` - workflow for debugging
- `prm-refactor` - guidelines for refactoring

**structure:**
```yaml
name: prm-implement-authentication
description: implement user authentication feature
content: |
  implement user authentication with the following requirements:
  - support email/password login
  - use jwt for session management
  - follow rest conventions from ins-rest-conventions
  - use patterns from exc-auth-example
```

#### 2. flt- (filters)

**what files to include/exclude**

examples:
- `flt-api-files` - include api-related files
- `flt-no-tests` - exclude test files
- `flt-auth-components` - authentication-related components

**structure:**
```yaml
name: flt-api-files
description: include api-related files
include:
  - "src/api/**/*.ts"
  - "src/routes/**/*.ts"
exclude:
  - "**/*.test.ts"
  - "**/*.spec.ts"
```

#### 3. ins- (instructions)

**how to approach tasks**

examples:
- `ins-rest-conventions` - rest api conventions
- `ins-error-handling` - how to handle errors
- `ins-testing-strategy` - testing approach

**structure:**
```yaml
name: ins-rest-conventions
description: rest api conventions for this project
content: |
  rest api conventions:
  - use http verbs correctly (GET/POST/PUT/DELETE)
  - return appropriate status codes (200, 201, 400, 404, 500)
  - use consistent url patterns (/api/v1/resource/:id)
  - include error details in response body
```

#### 4. sty- (styles)

**code style, formatting, preferences**

examples:
- `sty-naming-conventions` - how to name things
- `sty-file-structure` - how to organize files
- `sty-code-style` - formatting preferences

**structure:**
```yaml
name: sty-naming-conventions
description: naming conventions for this project
content: |
  naming conventions:
  - files: kebab-case (user-service.ts)
  - classes: PascalCase (UserService)
  - functions: camelCase (getUserById)
  - constants: SCREAMING_SNAKE_CASE (MAX_RETRIES)
  - private members: prefix with _ (_internalState)
```

#### 5. exc- (excerpts)

**specific code snippets or examples**

examples:
- `exc-auth-example` - reference authentication implementation
- `exc-api-pattern` - example api endpoint
- `exc-error-handler` - error handling example

**structure:**
```yaml
name: exc-auth-example
description: reference authentication implementation
files:
  - path: src/auth/auth-service.ts
    excerpt: |
      export class AuthService {
        async login(email: string, password: string): Promise<Token> {
          // implementation here
        }
      }
```

**key benefit:** include specific snippets instead of entire files, saving tokens

## usage patterns

### basic usage

```bash
# apply single rule
sc-context apply prm-implement-feature

# apply multiple rules
sc-context apply prm-implement-auth flt-api-files ins-rest-conventions

# apply with output
sc-context apply prm-implement-auth flt-api-files > context.txt
```

### composition patterns

**pattern 1: feature implementation**
```bash
sc-context apply \
  prm-implement-feature \     # what to do
  flt-relevant-files \        # which files
  ins-methodology \           # how to approach
  sty-conventions \           # style to follow
  exc-reference-impl          # example to follow
```

**pattern 2: debugging**
```bash
sc-context apply \
  prm-fix-bug \              # debugging workflow
  flt-error-location \       # files where error occurs
  ins-debugging-process \    # how to debug
  exc-similar-fix            # similar past fix
```

**pattern 3: refactoring**
```bash
sc-context apply \
  prm-refactor \             # refactoring task
  flt-target-files \         # files to refactor
  ins-refactor-safety \      # how to refactor safely
  exc-refactor-example       # example refactoring
```

## rule management

### creating rules

```bash
# create new prompt rule
sc-context create prm-my-task "description" "content"

# create new filter rule
sc-context create flt-my-files --include "src/**/*.ts" --exclude "**/*.test.ts"

# create new instruction rule
sc-context create ins-my-conventions "description" "content"
```

### listing rules

```bash
# list all rules
sc-context list

# list rules by category
sc-context list prm-
sc-context list flt-
sc-context list ins-

# search rules
sc-context search "authentication"
```

### editing rules

```bash
# edit existing rule
sc-context edit prm-implement-auth

# delete rule
sc-context delete prm-old-task
```

## best practices

### 1. small, focused rules

**good:**
```yaml
name: flt-auth-api
include: ["src/api/auth/**/*.ts"]
```

**bad:**
```yaml
name: flt-everything
include: ["src/**/*"]  # ← defeats the purpose!
```

### 2. compose rules, don't duplicate

**good:**
```bash
# reuse existing rules
sc-context apply prm-implement-feature flt-api-files ins-rest
```

**bad:**
```bash
# create monolithic rule with everything
sc-context create prm-giant-task "..." "..."  # ← hard to reuse
```

### 3. use excerpts for examples

**good:**
```yaml
name: exc-auth-pattern
files:
  - path: src/auth/service.ts
    excerpt: "specific function only"  # ← saves tokens
```

**bad:**
```yaml
name: flt-include-auth-file
include: ["src/auth/service.ts"]  # ← entire file, wastes tokens
```

### 4. document rule purpose

**good:**
```yaml
name: prm-implement-auth
description: implement authentication following security best practices
content: |
  # clear instructions here
```

**bad:**
```yaml
name: prm-task-1
description: "stuff"  # ← unclear purpose
```

## integration with skogai

### with CLAUDE.md

```markdown
## context rules

available sc-context rules:
- @sc-context:prm-implement-feature - feature implementation workflow
- @sc-context:flt-api-files - api-related files
- @sc-context:ins-rest-conventions - rest api conventions

see @docs/tools/sc-context for detailed documentation
```

### with .skogai

.skogai folder can include project-specific sc-context rules that are shared across related projects.

### with skills

skills can reference sc-context rules:

```yaml
name: implement-feature-skill
steps:
  - apply context: sc-context apply prm-implement-feature flt-relevant-files
  - implement following ins-conventions
  - verify with exc-test-pattern
```

## advanced features

### rule templates

create reusable templates:

```bash
# create template
sc-context template create feature-impl \
  --requires "feature-name" \
  --applies "prm-implement-{feature-name} flt-{feature-name}-files"

# use template
sc-context template apply feature-impl --feature-name authentication
```

### rule validation

validate rules before applying:

```bash
# check if rules exist
sc-context validate prm-task flt-files ins-conventions

# dry run (show what would be included)
sc-context apply --dry-run prm-task flt-files
```

### rule statistics

understand token usage:

```bash
# show token counts
sc-context stats prm-task flt-files

# compare approaches
sc-context stats flt-include-all  # ← 50000 tokens
sc-context stats flt-focused exc-examples  # ← 3000 tokens
```

## enforcing the 4000 token principle

sc-context helps enforce skogai's 4000 token principle:

**if context exceeds 4000 tokens:**
1. problem is too broad → break into smaller pieces
2. filters are too loose → tighten file selection
3. using files instead of excerpts → use exc- rules
4. wrong level of abstraction → rethink decomposition

**measurement:**
```bash
# check token count
sc-context apply prm-task flt-files | wc -c  # rough approximation
sc-context stats prm-task flt-files          # exact count
```

## see also

- @docs/skogai/architecture - context management architecture
- @docs/skogai/philosophy - context efficiency principle
- [@todo:skogix:"add actual sc-context implementation reference when available"]
