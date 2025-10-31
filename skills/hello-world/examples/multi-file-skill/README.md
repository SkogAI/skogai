# multi-file skill example

this example demonstrates a skill with multiple resource files showing progressive loading in action.

## structure

```
multi-file-skill/
├── SKILL.md              # main skill file
├── sql-injection.md      # sql injection patterns
├── xss-patterns.md       # xss patterns
├── command-injection.md  # command injection patterns
└── README.md            # this file
```

## progressive loading demonstration

### level 1: metadata (always loaded)

```yaml
name: security-scanner
description: scans code for common security vulnerabilities...
allowed-tools: [Glob, Grep, Read]
```

this is ~100 tokens, always in context.

### level 2: main skill (loaded on trigger)

when user says "scan for security issues", SKILL.md loads:
- general workflow
- how to use pattern files
- output format
- references to pattern files

this is ~500 tokens, loaded when skill triggers.

### level 3: pattern files (loaded on-demand)

when checking for SQL injection, sql-injection.md loads:
- grep patterns for SQL injection
- dangerous code examples
- safe alternatives
- severity info

this is ~300 tokens, loaded only when needed.

## memory efficiency

if user only cares about SQL injection:
- level 1: 100 tokens (metadata)
- level 2: 500 tokens (SKILL.md)
- level 3: 300 tokens (sql-injection.md)
- total: ~900 tokens

xss-patterns.md and command-injection.md never load, saving ~600 tokens.

## workflow example

```
user: "scan my code for sql injection"

1. skill triggers (level 1 metadata matched)
2. SKILL.md loads (level 2)
3. claude reads: "reference sql-injection.md for patterns"
4. sql-injection.md loads (level 3)
5. claude uses grep patterns from sql-injection.md
6. scan completes
```

## key takeaways

1. **organize by topic**: each vulnerability type is a separate file
2. **reference explicitly**: SKILL.md tells claude which file to load
3. **load on-demand**: only load what's needed for current task
4. **keep metadata light**: description doesn't describe every pattern
5. **scale gracefully**: can add more pattern files without affecting metadata size

## when to use this pattern

use multi-file skills when:
- content naturally divides into topics
- not all topics needed for every invocation
- individual files are substantial (200+ tokens)
- skill serves multiple related purposes

## when not to use this pattern

keep everything in SKILL.md when:
- total content is small (<1000 tokens)
- all content needed for every invocation
- divisions would be artificial
- skill has single, focused purpose
