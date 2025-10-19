---
prompt: |
  agent-expert(Validate agents in prompts directory)

  Please validate all agent definition files in /home/skogix/skogix/prompts/ directory.

  For each .md file that appears to be an agent definition, check:

  1. Frontmatter validity:
    - Has valid YAML frontmatter (between --- markers)
    - Has required 'name' field
    - Has 'description' field (should include examples)
    - Has 'color' field (valid: red, orange, yellow, green, blue, purple, pink, inherit)
    - Has 'model' field if specified (valid: opus, sonnet, haiku, inherit)
    - Has 'tools' field if specified (check for typos in tool names)
  2. Filename/name matching:
    - Does filename match the 'name' field? (e.g., if name is "silent-failure-hunter", filename should be "silent-failure-hunter.md")
  3. Common issues:
    - Tool name typos (like "KillShellias" instead of "KillShell")
    - Invalid tool references
    - Missing or weak descriptions
    - Any other structural problems

  Return a concise report listing each agent file with its status (✓ or issues found).
  Search(pattern: "**/*.md", path: "/home/skogix/skogix/prompts")
agent: |
  Search(pattern: "**/*.md", path: "/home/skogix/skogix/prompts")

  Found 13 files
  /home/skogix/skogix/prompts/claude-style-core.md
  /home/skogix/skogix/prompts/claude-agent-agent.md
  /home/skogix/skogix/prompts/code-type-designer.md
  /home/skogix/skogix/prompts/code-simplifier.md
  /home/skogix/skogix/prompts/code-shower.md
  /home/skogix/skogix/prompts/code-reviewer.md
  /home/skogix/skogix/prompts/code-flow-mapper.md
  /home/skogix/skogix/prompts/code-architect.md
  /home/skogix/skogix/prompts/claude-agent-skill.md
  /home/skogix/skogix/prompts/claude-agent-command.md
  /home/skogix/skogix/prompts/tests/core-identity.md
  /home/skogix/skogix/prompts/claude-style-orchestration.md
  /home/skogix/skogix/prompts/code-explorer.md
  ⎿  Read(file_path: "/home/skogix/skogix/prompts/claude-style-core.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/claude-agent-agent.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-type-designer.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-simplifier.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-shower.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-reviewer.md")

  ⎿  Read 48 lines

  ⎿  Read 533 lines

  ⎿  Read 112 lines

  ⎿  Read 81 lines

  ⎿  Read 142 lines

  ⎿  Read 48 lines

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-flow-mapper.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-architect.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/claude-agent-skill.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/claude-agent-command.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/claude-style-orchestration.md")

  ⎿  Read(file_path: "/home/skogix/skogix/prompts/code-explorer.md")

  ⎿  Read 19 lines

  ⎿  Read 35 lines

  ⎿  Read 211 lines

  ⎿  Read 467 lines

  ⎿  Read 146 lines

  ⎿  Read 57 lines
tokens:
  {
    "status": "completed",
    "prompt": "Please validate all agent definition files in /home/skogix/skogix/prompts/ directory.\n\nFor each .md file that appears to be an agent definition, check:\n\n1. **Frontmatter validity**:\n   - Has valid YAML frontmatter (between --- markers)\n   - Has required 'name' field\n   - Has 'description' field (should include examples)\n   - Has 'color' field (valid: red, orange, yellow, green, blue, purple, pink, inherit)\n   - Has 'model' field if specified (valid: opus, sonnet, haiku, inherit)\n   - Has 'tools' field if specified (check for typos in tool names)\n\n2. **Filename/name matching**:\n   - Does filename match the 'name' field? (e.g., if name is \"silent-failure-hunter\", filename should be \"silent-failure-hunter.md\")\n\n3. **Common issues**:\n   - Tool name typos (like \"KillShellias\" instead of \"KillShell\")\n   - Invalid tool references\n   - Missing or weak descriptions\n   - Any other structural problems\n\nReturn a concise report listing each agent file with its status (✓ or issues found).",
    "content": ["<cut>"],
    "totalDurationMs": 35997,
    "totalTokens": 48220,
    "totalToolUseCount": 14,
    "usage":
      {
        "input_tokens": 7,
        "cache_creation_input_tokens": 25672,
        "cache_read_input_tokens": 21032,
        "cache_creation":
          {
            "ephemeral_5m_input_tokens": 25672,
            "ephemeral_1h_input_tokens": 0,
          },
        "output_tokens": 1509,
        "service_tier": "standard",
      },
  }
---

Agent Validation Report

✓ /home/skogix/skogix/prompts/claude-style-core.md

Status: Not an agent definition (style guide document)

- No frontmatter - this is a style/behavior guide, not an agent

✓ /home/skogix/skogix/prompts/claude-agent-agent.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: agent-expert, description, color: orange
- Filename should be agent-expert.md to match name field
- Issue: Filename mismatch - file is claude-agent-agent.md but name is agent-expert

✓ /home/skogix/skogix/prompts/code-type-designer.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: type-design-analyzer, description, color: pink, model: inherit
- Issue: Filename mismatch - file is code-type-designer.md but name is type-design-analyzer

✓ /home/skogix/skogix/prompts/code-simplifier.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: code-simplifier, description, color (implicit), model: opus
- Issue: Missing color field in frontmatter
- Filename matches name field ✓

✓ /home/skogix/skogix/prompts/code-shower.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: silent-failure-hunter, description, color: yellow, model: inherit
- Issue: Filename mismatch - file is code-shower.md but name is silent-failure-hunter

✓ /home/skogix/skogix/prompts/code-reviewer.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: code-reviewer, description, color: green, model: opus
- Filename matches name field ✓

✓ /home/skogix/skogix/prompts/code-flow-mapper.md

Status: Valid agent definition with issues

- Has valid YAML frontmatter
- Required fields present: name: code-flow-mapper, description, color: yellow
- Issue: Tool name typo - includes non-existent tools:
  - ExitPlanMode (invalid)
  - MultiEdit (invalid)
  - LS (invalid - should be part of Bash)
- Filename matches name field ✓

✓ /home/skogix/skogix/prompts/code-architect.md

Status: Valid agent definition with issues

- Has valid YAML frontmatter
- Required fields present: name: code-architect, description, color: green, model: sonnet
- Issue: Tool name issues:
  - LS (invalid - should be part of Bash)
- Filename matches name field ✓

✓ /home/skogix/skogix/prompts/claude-agent-skill.md

Status: Not an agent definition (skill documentation)

- Has YAML frontmatter with name: skill-creator and description
- This is a skill, not an agent (different format/purpose)
- Issue: Filename should be skill-creator.md to match name

✓ /home/skogix/skogix/prompts/claude-agent-command.md

Status: Valid agent definition

- Has valid YAML frontmatter
- Required fields present: name: command-expert, description, color: purple
- Issue: Filename mismatch - file is claude-agent-command.md but name is command-expert

✓ /home/skogix/skogix/prompts/tests/core-identity.md

Status: Not an agent definition (test document)

- No frontmatter - this is a test/quiz document

✓ /home/skogix/skogix/prompts/claude-style-orchestration.md

Status: Not an agent definition (style guide document)

- No frontmatter - this is a documentation/guide file

✓ /home/skogix/skogix/prompts/code-explorer.md

Status: Valid agent definition with issues

- Has valid YAML frontmatter
- Required fields present: name: code-explorer, description, color: yellow, model: sonnet
- Issue: Tool name issues:
  - LS (invalid - should be part of Bash)
- Filename matches name field ✓

---

Summary of Issues Found

Critical Issues:

1. Filename/name mismatches (5 files):

- claude-agent-agent.md → should be agent-expert.md
- code-type-designer.md → should be type-design-analyzer.md
- code-shower.md → should be silent-failure-hunter.md
- claude-agent-command.md → should be command-expert.md
- claude-agent-skill.md → should be skill-creator.md

2. Invalid tool references (3 files):

- code-flow-mapper.md: ExitPlanMode, MultiEdit, LS
- code-architect.md: LS
- code-explorer.md: LS

3. Missing required field:

- code-simplifier.md: Missing color field

Files that are not agents (4 files):

- claude-style-core.md - Style guide
- tests/core-identity.md - Test document
- claude-style-orchestration.md - Orchestration guide
  done (14 tool uses · 48.2k tokens · 36s)
