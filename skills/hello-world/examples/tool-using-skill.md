# tool-using skill example

this example demonstrates a skill that uses tools to interact with the codebase.

## use case

a skill that finds unused functions in a javascript/typescript codebase by analyzing imports and usages.

## skill file: skills/dead-code-finder/SKILL.md

```markdown
---
name: dead-code-finder
description: finds potentially unused functions and exports in javascript/typescript codebases by analyzing import statements and function calls
allowed-tools:
  - Glob
  - Grep
  - Read
---

# dead code finder skill

this skill identifies potentially unused code in javascript/typescript projects.

## workflow

when triggered, follow these steps:

### 1. find all source files

use Glob to find javascript/typescript files:
- `**/*.js`
- `**/*.ts`
- `**/*.tsx`
- `**/*.jsx`

exclude:
- `**/node_modules/**`
- `**/dist/**`
- `**/build/**`

### 2. identify exported functions

use Grep to find export statements:
- pattern: `export (function|const|class) (\w+)`
- output mode: content with line numbers

collect all exported function names.

### 3. search for imports

for each exported function, use Grep to search for imports:
- pattern: `import.*{functionName}.*from`
- pattern: `import.*functionName.*from` (default import)
- pattern: `require.*functionName`

### 4. search for direct usage

also search for the function name being called:
- pattern: `\bfunctionName\(`

### 5. report findings

for each function:
- if imported nowhere: "likely unused"
- if imported but never called: "imported but unused"
- if called: "in use"

## example output

```
potentially unused exports:

likely unused:
- calculateTax (src/utils/tax.ts:45)
- formatDate (src/utils/date.ts:12)

imported but potentially unused:
- validateEmail (src/utils/validation.ts:23)
  imported in: src/components/Form.tsx

in use:
- processPayment (src/payment/processor.ts:8)
  imported in: src/api/checkout.ts
  called in: src/api/checkout.ts:45
```

## limitations

explain to users:
- this is static analysis - may have false positives
- dynamic imports aren't detected
- usage in templates/jsx may be missed
- external packages importing your code won't be detected

## tips

- focus on clearly unused code (0 imports)
- suggest manual review for "imported but unused"
- recommend running tests to verify safety before removal
```

## why this works

- **uses tools effectively**: Glob for discovery, Grep for analysis, Read for detail
- **clear tool restrictions**: only the tools needed for the task
- **step-by-step workflow**: clear instructions for claude
- **manages expectations**: explains limitations
- **actionable output**: shows file paths and line numbers

## triggering this skill

users might say:
- "find unused code"
- "what functions aren't being used?"
- "help me identify dead code"
- "which exports can i remove?"

## tool usage notes

### Glob patterns
```
**/*.{js,ts,tsx,jsx}  # find all source files
!**/node_modules/**   # exclude dependencies
```

### Grep patterns
```
export function (\w+)           # named function export
export const (\w+) =            # const export
import.*{(\w+)}.*from           # named import
\b(\w+)\(                       # function call
```

### workflow optimization

1. use Glob once to get all files
2. use Grep with output_mode: files_with_matches first (fast)
3. use Grep with output_mode: content for details (slower)
4. use Read only when you need full file context

this progressive approach keeps the skill fast.
