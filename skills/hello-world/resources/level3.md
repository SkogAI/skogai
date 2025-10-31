# level 3 resources

this file demonstrates level 3 (on-demand) loading.

## what this shows

- SKILL.md mentioned this file exists but didn't auto-link it
- i had to be explicitly instructed to read it ("now read resources/level3.md")
- this proves skills can include deep documentation that loads only when specifically requested

## the key difference

- **level 2**: `resources/level2.md` - linked from SKILL.md, loads naturally when reading instructions
- **level 3**: `resources/level3.md` - requires explicit instruction to look up

## progressive loading complete

1. **level 1**: YAML frontmatter (name, description, allowed-tools) - always loaded
2. **level 2**: SKILL.md + linked resources like level2.md - loads when skill triggers
3. **level 3**: this file - loads only when explicitly instructed

## why this matters

keeps skills efficient. you only load what you need:
- metadata is always available (tiny)
- instructions + linked docs load when skill is invoked (moderate)
- deep resources load only when required (on-demand)

that's it - progressive loading demonstration complete.
