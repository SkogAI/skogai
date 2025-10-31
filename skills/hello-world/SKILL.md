---
name: hello-world
description: A demonstration skill showing how skills work in Claude plugins. Use when the user asks about plugin skills or requests a hello world skill demonstration.
allowed-tools:
  - Read
  - Bash
---

# hello world skill

hello world from the skill component!

## what just happened - progressive loading

skills load in 3 levels:

### level 1: metadata (always loaded)
the YAML frontmatter above - name, description, allowed-tools. lightweight, always in context.

### level 2: instructions (loaded when triggered)
this content you're reading now. loads when the skill is invoked.

for more details, see `resources/level2.md` which demonstrates level 2 resource loading.

### level 3: resources (loaded on-demand)
additional files that load only when explicitly instructed:
- documentation files (via Read)
- executable scripts (via Bash)

## demonstration

when triggered:

1. the level 2 resource (`resources/level2.md`) loads automatically as you read these instructions
2. demonstrate level 3 loading by explicitly asking to read `resources/level3.md`
3. run `scripts/demo.sh` to show script execution with timestamp proof

then explain:
- how you got invoked (description matched user's request)
- the 3 loading levels demonstrated
- difference from commands (/hello), agents (greeter), and hooks

## component comparison

- **command** `/hello` - user explicitly types it
- **agent** `greeter` - invoked via Task tool for complex work
- **skill** `hello-world` - auto-triggers when description matches
- **hook** - triggers on events (commits, file changes)

that's it. minimal demonstration of what skills are and how they work.
