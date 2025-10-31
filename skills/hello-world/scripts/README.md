# scripts in skills

this directory demonstrates how skills can include executable scripts as resources.

## what are script resources?

scripts are helper programs that skills can execute using the Bash tool. they're part of level 3 (resources) in progressive loading.

## when to use scripts

use scripts in skills when:
- you need to perform complex shell operations
- multiple commands need to run together
- the logic is easier to express in bash/python/etc than in instructions
- you want reusable utilities across skill invocations

## example: demo.sh

the demo.sh script shows skill structure and information. a skill would use it like:

```markdown
## demonstrating skill structure

when user asks to see the skill structure, run:

```bash
bash skills/hello-world/scripts/demo.sh
```

this executes the demo script which shows:
- skill file structure
- progressive loading levels
- file sizes
- tool access info
```

## script guidelines

### 1. include shebangs

```bash
#!/usr/bin/env bash
#!/usr/bin/env python3
#!/usr/bin/env node
```

### 2. make executable

```bash
chmod +x scripts/my-script.sh
```

### 3. handle errors

```bash
set -e  # exit on error
set -u  # exit on undefined variable
```

### 4. provide clear output

```bash
echo "=== section header ==="
echo "informative message"
echo ""  # blank line for readability
```

### 5. be portable

```bash
# check for required commands
if ! command -v jq &> /dev/null; then
  echo "error: jq is required"
  exit 1
fi
```

## script types

### information scripts

show status, structure, or metadata:
```bash
skills/my-skill/scripts/info.sh
```

### validation scripts

check code quality or correctness:
```bash
skills/my-skill/scripts/validate.sh
```

### transformation scripts

modify or generate files:
```bash
skills/my-skill/scripts/transform.sh input.txt output.txt
```

### analysis scripts

process and analyze data:
```bash
skills/my-skill/scripts/analyze.sh logfile.log
```

## progressive loading with scripts

scripts demonstrate level 3 loading:

1. **metadata**: skill description mentions "includes validation scripts"
2. **instructions**: SKILL.md says "run scripts/validate.sh to check code"
3. **script**: validate.sh loads and executes only when referenced

## memory efficiency

```
without script:
- include validation logic in SKILL.md: +500 tokens always loaded

with script:
- reference in SKILL.md: +50 tokens in instructions
- script content: +500 tokens only when executed
- savings: 450 tokens when validation not needed
```

## allowing bash tool

to use scripts, skill must allow the Bash tool:

```yaml
---
name: my-skill
description: skill that uses scripts
allowed-tools:
  - Bash
  - Read  # to read script output
---
```

## security considerations

1. **validate inputs**: never pass unsanitized user input to scripts
2. **restrict access**: only include necessary tools in allowed-tools
3. **review scripts**: treat scripts as code - review for vulnerabilities
4. **document purpose**: clearly explain what each script does

## example skill using scripts

```markdown
---
name: code-validator
description: validates code style and correctness using custom validation scripts
allowed-tools:
  - Bash
  - Read
  - Glob
---

# code validator skill

this skill runs validation checks on code.

## workflow

1. identify files to validate using Glob
2. run appropriate validation script:
   ```bash
   bash skills/code-validator/scripts/validate-js.sh file.js
   bash skills/code-validator/scripts/validate-py.sh file.py
   ```
3. parse output and report issues
4. suggest fixes

## available scripts

- validate-js.sh: validates javascript/typescript
- validate-py.sh: validates python
- validate-style.sh: checks code formatting
```

## advantages of scripts

1. **reusable**: same script across multiple skill invocations
2. **maintainable**: update script once, all uses benefit
3. **efficient**: complex logic in native shell/python
4. **testable**: can test scripts independently
5. **familiar**: developers understand shell scripts

## when not to use scripts

don't use scripts when:
- logic is simple enough for inline Bash tool use
- script would be single-use
- instructions can express the logic clearly
- script would need frequent modification

keep it simple: only add scripts when they add clear value.
