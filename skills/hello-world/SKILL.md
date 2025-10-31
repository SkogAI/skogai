---
name: hello-world
description: A demonstration skill showing how skills work in Claude plugins. Use when the user asks about plugin skills or requests a hello world skill demonstration.
---

# hello world skill

this skill demonstrates the skill component type in claude plugins.

## what skills do

skills are model-invoked capabilities that:
- load progressively (metadata → instructions → resources)
- provide specialized knowledge and workflows
- exist as directories with SKILL.md files
- automatically activate when their description matches the task

## progressive loading demonstration

### level 1: metadata
you're reading this because the user's request matched the description in the YAML frontmatter. that metadata is always loaded (lightweight, ~100 tokens).

### level 2: instructions
this content (what you're reading now) only loads when the skill is triggered. instructions typically contain workflows, best practices, and guidance.

### level 3: resources
skills can include additional files like:
- reference documentation
- example files
- executable scripts
- templates

these load on-demand when referenced.

## what to do when triggered

when this skill is invoked, respond with:

```
hello world from the skill component!

this demonstrates:
- skills have YAML frontmatter with name and description
- metadata is always loaded, instructions load on-demand
- skills are in skills/skill-name/SKILL.md structure
- claude uses skills automatically when the description matches
- skills enable progressive disclosure of knowledge
```

be educational and explain how this skill got triggered based on the user's request matching the description.

## key differences from other components

- **commands**: user-invoked with /command-name
- **agents**: explicitly invoked via Task tool
- **skills**: automatically invoked when description matches task
- **hooks**: triggered by events (file changes, commits, etc)

## skill structure example

```
skills/
└── hello-world/
    ├── SKILL.md          # this file (required)
    ├── reference.md      # additional docs (optional)
    ├── examples/         # example files (optional)
    └── scripts/          # helper scripts (optional)
```
