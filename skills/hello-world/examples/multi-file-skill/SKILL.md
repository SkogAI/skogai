---
name: security-scanner
description: scans code for common security vulnerabilities including SQL injection, XSS, command injection, and insecure dependencies
allowed-tools:
  - Glob
  - Grep
  - Read
---

# security scanner skill

this skill scans codebases for common security vulnerabilities.

## workflow

when triggered:

1. **identify target language**: ask user or detect from file extensions
2. **load patterns**: reference the appropriate pattern file from this directory
3. **scan codebase**: use Grep with patterns from pattern files
4. **analyze results**: read flagged files for context
5. **report findings**: categorize by severity (critical, high, medium, low)

## pattern files

this skill uses separate pattern files for each language/category:

- [sql-injection.md](./sql-injection.md): sql injection patterns
- [xss-patterns.md](./xss-patterns.md): cross-site scripting patterns
- [command-injection.md](./command-injection.md): command injection patterns

these files load on-demand when scanning for specific vulnerabilities.

## usage

```
# read pattern file
Read skills/security-scanner/sql-injection.md

# extract patterns
# use Grep with patterns
# report findings
```

## progressive loading in action

- **level 1**: skill metadata loads (lightweight)
- **level 2**: this file loads when skill triggers
- **level 3**: pattern files load only for relevant vulnerability types

this keeps memory usage low - if user only cares about SQL injection, XSS patterns never load.

## output format

```
security scan results for <directory>

critical findings:
- SQL injection risk in src/api/users.ts:45
  pattern: raw string concatenation in query
  suggestion: use parameterized queries

high findings:
- potential XSS in src/components/Comment.tsx:23
  pattern: dangerouslySetInnerHTML without sanitization
  suggestion: use DOMPurify or avoid dangerouslySetInnerHTML

medium findings:
- command injection risk in src/utils/exec.ts:12
  pattern: user input in exec() call
  suggestion: validate and sanitize input, use execFile()
```
