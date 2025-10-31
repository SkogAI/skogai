---
name: hello-world
description: A comprehensive demonstration skill showing how skills work in Claude plugins, including tool usage, resource loading, and best practices. Use when the user asks about plugin skills, requests a hello world skill demonstration, or wants to learn skill capabilities.
allowed-tools:
  - Read
  - Bash
  - Glob
---

# hello world skill

this skill comprehensively demonstrates the skill component type in claude plugins.

## what skills do

skills are model-invoked capabilities that:
- load progressively (metadata → instructions → resources)
- provide specialized knowledge and workflows
- exist as directories with SKILL.md files
- automatically activate when their description matches the task
- can use tools to interact with the environment
- can include reference documentation and examples

## progressive loading demonstration

### level 1: metadata
you're reading this because the user's request matched the description in the YAML frontmatter. that metadata is always loaded (lightweight, ~100 tokens).

### level 2: instructions
this content (what you're reading now) only loads when the skill is triggered. instructions typically contain workflows, best practices, and guidance.

### level 3: resources
skills can include additional files that load on-demand when referenced:
- reference documentation → `reference.md`
- example files → `examples/`
- executable scripts → `scripts/`
- templates and configurations

## what to do when triggered

when this skill is invoked, demonstrate its capabilities by:

1. **greeting and context**: explain that this is the hello-world skill and how it was triggered
2. **tool demonstration**: use the allowed tools to show skill capabilities:
   - use Glob to find this skill's structure: `skills/hello-world/**/*`
   - use Read to show the existence of reference documentation
   - use Bash (if appropriate) to demonstrate script execution
3. **resource references**: mention the additional resources available:
   - reference.md for detailed patterns and best practices
   - examples/ directory for practical skill implementations
   - scripts/ directory for executable helpers

4. **educational summary**: explain key concepts:
   ```
   hello world from the skill component!

   this skill demonstrates:
   - YAML frontmatter with name, description, and allowed-tools
   - metadata is always loaded, instructions load on-demand
   - skills are in skills/skill-name/SKILL.md structure
   - claude uses skills automatically when description matches
   - skills can use tools to interact with the environment
   - skills enable progressive disclosure of knowledge
   - additional resources load when referenced
   ```

be educational and show concrete examples of what skills can do.

## tool usage in skills

this skill has `allowed-tools` specified in the frontmatter:
- **Read**: to read additional documentation and examples
- **Bash**: to execute helper scripts
- **Glob**: to explore skill structure and find resources

when invoked, actively use these tools to demonstrate capabilities.

## key differences from other components

- **commands** (`/hello`):
  - user explicitly invokes with /command-name
  - best for: user-initiated workflows, debugging, quick actions

- **agents** (greeter):
  - explicitly invoked via Task tool with subagent_type
  - best for: complex multi-step tasks, specialized context, autonomous work

- **skills** (this file):
  - automatically invoked when description matches task
  - best for: reusable patterns, domain expertise, progressive knowledge disclosure

- **hooks**:
  - triggered by events (file changes, commits, tool calls)
  - best for: automation, validation, workflow enforcement

## when to use skills

prefer skills over other components when:
1. **knowledge should be discovered**: the user doesn't need to know the exact command name
2. **context is reusable**: the same pattern applies across multiple projects
3. **progressive loading matters**: start lightweight, load details as needed
4. **tools are needed**: skills can use tools to demonstrate or implement capabilities
5. **domain expertise**: encapsulate specialized knowledge (e.g., "testing", "documentation", "optimization")

## skill structure

```
skills/hello-world/
├── SKILL.md          # this file (required) - metadata + instructions
├── reference.md      # detailed patterns and best practices
├── examples/         # practical skill examples
│   ├── simple-skill.md
│   ├── tool-using-skill.md
│   └── multi-file-skill/
└── scripts/          # executable helpers
    └── demo.sh
```

## resources available

after completing the demonstration, inform the user they can:
- read `skills/hello-world/reference.md` for detailed skill patterns
- explore `skills/hello-world/examples/` for practical implementations
- run scripts from `skills/hello-world/scripts/` to see executable resources

these files demonstrate level 3 (resource) loading in the progressive loading model.
