# CLAUDE.md

## this project

**IMPORTANT**: this directory (`/home/skogix/skogix`) is the SOURCE for the skogai-marketplace project.

- this is a marketplace that can contain multiple plugins
- plugins are located in `plugins/*/` subdirectories
- when working with plugin components (skills, commands, agents, hooks), you are editing SOURCE files in `plugins/plugin-name/`
- plugin files get installed to `~/.claude/plugins/marketplaces/skogai-marketplace/` when loaded
- paths like `plugins/hello-world/skills/hello-world/SKILL.md` are relative to THIS project root, NOT the installed location
- this is the development/source repository, not the runtime installation

## The user Skogix

this @docs/skogix/user.md tells you more about Skogix and @docs/skogix/definitions.md defines some terms he uses a lot which have specific meanings.
