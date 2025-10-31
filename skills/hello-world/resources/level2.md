# level 2 resources

this file demonstrates level 2 loading - automatically loaded when referenced from SKILL.md.

## what this shows

- SKILL.md linked to this file (e.g., `see resources/level2.md`)
- you loaded it automatically as part of following the instructions
- this proves skills can include additional context that loads when referenced

## the difference from level 3

- **level 2**: linked/referenced from SKILL.md → loads naturally when following instructions
- **level 3**: requires explicit instruction to look up (e.g., "now read resources/level3.md")

## progressive loading recap

1. **level 1**: YAML frontmatter - always in context (tiny metadata)
2. **level 2**: SKILL.md + linked docs like this one - loads when skill triggers
3. **level 3**: on-demand resources - loads only when explicitly instructed

this keeps the initial load lightweight while making deeper resources available when needed.
