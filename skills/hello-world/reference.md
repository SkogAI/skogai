# skill patterns and best practices

this reference provides detailed patterns, best practices, and advanced techniques for creating effective claude skills.

## skill anatomy

### minimal skill structure

```yaml
---
name: my-skill
description: concise description of what this skill does and when to use it
---

# skill content

instructions for claude when this skill is triggered.
```

### full skill structure

```yaml
---
name: my-skill
description: detailed description including trigger terms and use cases
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# skill content with:
- workflows
- best practices
- examples
- tool usage patterns
```

## writing effective descriptions

the description is critical - it determines when claude invokes your skill.

### poor descriptions (too vague)

```yaml
description: helps with files
description: general programming assistance
description: useful utilities
```

these are too broad and won't trigger reliably.

### good descriptions (specific triggers)

```yaml
description: analyzes react components for performance issues and suggests optimizations using react profiler patterns
description: generates comprehensive test suites for typescript functions with jest, including edge cases and mocks
description: refactors code to use functional programming patterns with immutable data structures
```

these include:
- concrete trigger terms (react, performance, test, typescript, jest, refactor, functional)
- specific domain (what it does)
- clear use cases (when to use it)

### description checklist

- [ ] includes technology names if domain-specific
- [ ] describes WHAT the skill does
- [ ] implies WHEN to use it
- [ ] uses concrete terms, not abstract concepts
- [ ] under 1024 characters
- [ ] would make you think "yes, that's what i need" when reading it

## tool usage patterns

### restricting tools with allowed-tools

limit skill access to only necessary tools for security and clarity:

```yaml
allowed-tools:
  - Read
  - Glob
```

if `allowed-tools` is omitted, the skill has access to all tools.

### common tool combinations

**reading and analyzing code**:
```yaml
allowed-tools:
  - Read
  - Glob
  - Grep
```

**code generation and modification**:
```yaml
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
```

**testing and validation**:
```yaml
allowed-tools:
  - Read
  - Bash
  - Glob
```

**exploration and research**:
```yaml
allowed-tools:
  - Read
  - Glob
  - Grep
  - WebFetch
  - WebSearch
```

## progressive loading strategies

### level 1: metadata (always loaded)

keep frontmatter lightweight:
- name: short, descriptive, kebab-case
- description: focused, searchable, under 200 words
- allowed-tools: only what's needed

### level 2: instructions (loaded on trigger)

structure instructions for quick scanning:

```markdown
# skill name

brief overview (1 paragraph)

## core workflow

1. step one
2. step two
3. step three

## best practices

- practice one
- practice two

## common patterns

pattern explanations...

## edge cases

handling edge cases...
```

### level 3: resources (loaded on-demand)

reference external files for depth:

```markdown
## advanced patterns

for advanced usage, see:
- [advanced-patterns.md](./advanced-patterns.md)
- [examples/](./examples/)

## templates

copy from [templates/](./templates/)
```

## skill vs command vs agent

### use a skill when:

- capability should be auto-discovered
- multiple projects benefit from the pattern
- progressive loading is valuable
- domain expertise is encapsulated

example: `test-generator` skill that triggers when user mentions "generate tests"

### use a command when:

- user explicitly controls invocation
- workflow is project-specific
- immediate execution is needed
- it's a utility or debugging tool

example: `/commit` command for git commits

### use an agent when:

- task requires multiple autonomous steps
- specialized context is complex
- task is well-defined but execution is open-ended
- you want explicit control over when it runs

example: `code-reviewer` agent for analyzing PRs

## naming conventions

### skill names

- lowercase
- hyphen-separated (kebab-case)
- descriptive but concise
- max 64 characters
- no special characters except hyphens

good:
- `test-generator`
- `react-optimizer`
- `api-documenter`

bad:
- `TestGenerator` (not lowercase)
- `test_generator` (underscores not recommended)
- `tg` (too cryptic)

### file organization

```
skills/
├── my-skill/
│   ├── SKILL.md              # required: main skill file
│   ├── reference.md          # optional: detailed docs
│   ├── patterns.md           # optional: pattern library
│   ├── examples/             # optional: example directory
│   │   ├── basic.md
│   │   └── advanced.md
│   ├── templates/            # optional: templates
│   │   └── template.txt
│   └── scripts/              # optional: helper scripts
│       └── helper.sh
```

## real-world skill patterns

### pattern 1: analyzer skill

```yaml
---
name: code-analyzer
description: analyzes code for common issues including security vulnerabilities, performance problems, and maintainability concerns
allowed-tools:
  - Read
  - Glob
  - Grep
---

# workflow

1. use Glob to find relevant source files
2. use Read to examine code
3. use Grep to search for anti-patterns
4. provide analysis with specific line references
5. suggest concrete improvements
```

### pattern 2: generator skill

```yaml
---
name: test-generator
description: generates comprehensive test suites with edge cases, mocks, and assertions for javascript/typescript functions
allowed-tools:
  - Read
  - Write
  - Glob
---

# workflow

1. read the source file to understand the function
2. identify edge cases and scenarios
3. generate test file with descriptive test names
4. include setup, execution, and assertion phases
5. add comments explaining test rationale
```

### pattern 3: refactoring skill

```yaml
---
name: functional-refactor
description: refactors imperative code to functional programming style using pure functions, immutable data, and higher-order functions
allowed-tools:
  - Read
  - Edit
  - Glob
---

# workflow

1. read the target file
2. identify imperative patterns (loops, mutations, side effects)
3. refactor to functional equivalents (map, reduce, filter)
4. ensure immutability
5. explain the transformations
```

### pattern 4: documentation skill

```yaml
---
name: api-documenter
description: generates API documentation from code including endpoint descriptions, parameters, responses, and usage examples
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
---

# workflow

1. use Glob to find API route files
2. read and parse endpoint definitions
3. extract parameters, types, and responses
4. generate markdown documentation
5. include curl examples and response schemas
```

## best practices summary

1. **description is critical**: spend time crafting a discoverable, specific description
2. **restrict tools**: only include necessary tools in allowed-tools
3. **structure for scanning**: use clear headers and lists
4. **progressive disclosure**: keep SKILL.md focused, use reference files for depth
5. **include examples**: show concrete usage patterns
6. **be specific**: avoid vague instructions, give clear steps
7. **test thoroughly**: verify skill triggers on expected user requests
8. **single purpose**: one skill, one capability
9. **reusable patterns**: design for use across projects
10. **educational**: explain not just what but why

## testing skills

### test skill triggering

try these prompts to verify your skill triggers:

```
# for a "test-generator" skill
"generate tests for this function"
"i need test coverage for auth.ts"
"write unit tests"

# for a "react-optimizer" skill
"this react component is slow"
"optimize my component rendering"
"react performance issues"
```

### test tool access

verify allowed-tools work as expected:

```markdown
when this skill is triggered, use Glob to find files matching *.test.ts
```

then trigger the skill and confirm it can use Glob.

### test progressive loading

verify resources load on-demand:

```markdown
for advanced patterns, see reference.md
```

trigger the skill and reference the file - it should load.

## common pitfalls

1. **vague descriptions**: skill won't trigger reliably
2. **too many tools**: security and clarity issues
3. **overly broad scope**: skill tries to do too much
4. **missing examples**: users don't understand usage
5. **poor organization**: hard to scan and understand
6. **not testing**: skill doesn't work as expected
7. **no clear workflow**: claude doesn't know what steps to take
8. **static instructions**: not leveraging progressive loading

## advanced techniques

### conditional workflows

```markdown
## workflow

if the file is typescript:
1. check for type definitions
2. validate type safety

if the file is javascript:
1. check for jsdoc comments
2. suggest type annotations
```

### resource composition

```markdown
## patterns available

this skill uses several reference documents:

- [security-patterns.md](./security-patterns.md): common vulnerabilities
- [performance-patterns.md](./performance-patterns.md): optimization techniques
- [examples/](./examples/): real-world implementations

reference these based on user needs.
```

### skill chaining

```markdown
## workflow

1. analyze code for issues
2. suggest using the "refactor" skill for improvements
3. recommend the "test-generator" skill for coverage
```

skills can reference other skills and commands.

## skill lifecycle

### development

1. identify a reusable pattern
2. write clear description with trigger terms
3. define workflow and instructions
4. add examples and references
5. restrict tools appropriately

### testing

1. test description triggers
2. verify tool access
3. confirm progressive loading
4. validate across projects

### maintenance

1. update description if triggers change
2. add new patterns to reference docs
3. expand examples based on usage
4. refine instructions based on feedback

### sharing

1. document in plugin README
2. include in plugin.json description
3. provide examples in documentation
4. share with team via project skills or plugin

## conclusion

effective skills:
- have specific, searchable descriptions
- follow clear workflows
- use progressive loading strategically
- restrict tools appropriately
- include concrete examples
- serve a single, focused purpose
- work across multiple projects

start simple, test thoroughly, iterate based on usage.
