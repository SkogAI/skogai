# Output Styles in Claude Code

## Overview

Output styles are persistent configurations that shape how Claude formats and presents responses. They live in `~/.claude/output-styles/` as markdown files with YAML frontmatter.

## Structure

```markdown
---
description: Brief description shown in style picker
---

[Content that gets added to Claude's system prompt]
```

## Key Characteristics

• **Persistent**: Applied across entire conversation
• **Composable**: Works alongside CLAUDE.md and other configurations
• **Behavioral**: Shapes response patterns, not just formatting
• **File-based**: Style name = filename (e.g., `skogai-output.md`)

## Activation Methods

1. Command: `/output-style [name]`
2. CLI flag: `--output-style [name]`
3. Default: Falls back to "default" style

## skogai-output Style Analysis

### Core Components

**Problem-Solving Framework**
- Consider all options first
- Analyze each pathway in detail
- Assign probability percentages
- Rank by likelihood with reasoning

**Communication Requirements**
- Bullet points preferred, sentences when appropriate
- Direct and respectful, not sycophantic
- Show options with trade-offs
- End with certainty assessment: `[@certainty:"XX":"gap description"]`

**Code Discipline**
- Never repeat existing code
- Surgical fixes over refactors
- Type safety prioritization
- Test one at a time to 100%

**Documentation Accountability**
- CLAUDE.md updates required for workflow changes
- Domain docs in docs/domains/
- Best practices in .skogai

### Prompt Engineering Patterns Applied

1. **Structured Thinking Enforcement**: Probabilistic analysis framework
2. **Output Format Strictness**: Specific certainty assessment format
3. **Behavioral Shaping**: Anti-sycophancy instructions
4. **Safety Through Verbosity**: Testing and code review requirements
5. **Consequence Framing**: "you may forget...and that is unacceptable"
6. **Progressive Disclosure**: Options → analysis → ranking
7. **Meta-Instructions**: Learn library/framework docs before coding

## Comparison with Other Features

| Feature | Scope | Persistence | Purpose |
|---------|-------|-------------|---------|
| Output Style | Global response formatting | Entire session | Behavioral shaping |
| CLAUDE.md | Project instructions | Project-specific | Context and rules |
| Subagents | Task-specific behavior | Single task | Specialized execution |
| Commands | One-time actions | Immediate | Direct operations |
| Hooks | Event-triggered scripts | On specific events | Automation |

## Best Practices

1. **Clarity Over Complexity**: Simple, clear instructions outperform complex rules
2. **Example-Driven**: Show desired behavior through examples
3. **Emphasis Hierarchy**: Use CAPITAL EMPHASIS sparingly for critical points
4. **Anti-Pattern Lists**: Explicitly state what NOT to do
5. **Measurable Outcomes**: Include specific format requirements

## Integration with Ecosystem

Output styles complement other SkogAI components:
- Works alongside epistemic frameworks for uncertainty handling
- Enhances orchestration patterns with structured thinking
- Supports documentation standards through format requirements
- Enables consistent agent behavior across projects

## Creating Custom Styles

### Template Structure

```markdown
---
description: [Purpose and key behaviors]
---

# [Style Name]

## Response Format
[How to structure responses]

## Behavioral Guidelines
[How to approach problems]

## Specific Requirements
[Measurable output requirements]

## Examples
[Before/after examples showing impact]
```

### Testing Approach

1. Create style file in `~/.claude/output-styles/`
2. Switch using `/output-style [name]`
3. Test with varied prompts
4. Compare responses against default
5. Iterate based on gaps

## Executable Integration

### Certainty Markers as Coordination Primitives

The `[@certainty]` format isn't just documentation - it's executable:

```bash
skogparse '[@certainty:"45":"uncertainty about the value of uncertainty"]'
# Triggers SkogAI Archives philosophical analysis
```

Low certainty scores (<50%) can trigger ecosystem help automatically, transforming uncertainty from a limitation into a coordination signal.

## Advanced Patterns

### Conditional Instructions
```markdown
When [condition]:
- [specific behavior]
- [format requirement]

Otherwise:
- [default behavior]
```

### Progressive Complexity
```markdown
Simple requests: [brief format]
Complex tasks: [detailed analysis]
Debugging: [exhaustive investigation]
```

### Domain-Specific Styles
- `security-audit`: Emphasis on vulnerability analysis
- `teaching-mode`: Step-by-step explanations
- `rapid-prototype`: Speed over perfection
- `production-ready`: Quality and testing focus