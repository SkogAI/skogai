---
prompt: |
  agent-expert(Analyze prompts directory structure)

  Prompt:
   Please examine the contents of /home/skogix/skogix/prompts/ directory to understand what agent definitions and related files exist there. The user mentioned that some files may
   have been moved around and names might be "borked" (incorrect/broken).

   Your task:
   1. Explore the directory structure of prompts/
   2. Identify all agent-related files (especially in .claude/agents/ if it exists there)
   3. Read the agent definition files to understand their purpose and structure
   4. Note any naming inconsistencies, structural issues, or organizational problems
   5. Provide a clear summary of what agents exist, their purposes, and any issues you found

   Return a comprehensive report about the agents in that directory including their current state and any recommendations for fixes or improvements.
  Response:
  Perfect! Now I have a complete understanding. Let me create a comprehensive report:
---

# Agent Directory Analysis Report

Executive Summary

The /home/skogix/skogix/prompts/ directory contains a complex but mostly well-organized collection of agent definitions, style guides, and configuration files. There are several
structural issues including broken symlinks, duplicate files, naming inconsistencies, and a typo in one agent definition.

---

# Directory Structure Overview

/home/skogix/skogix/
├── .claude/ # Main Claude Code configuration (active)
│ ├── agents/
│ │ ├── claude-agent-agent.md # Agent Expert (meta-agent)
│ │ ├── claude-agent-command.md # Command Expert (meta-agent)
│ │ ├── claude-agent-skill.md # Skill Creator (meta-agent)
│ │ ├── code-architect.md # Architecture designer
│ │ ├── code-explorer.md # Code analysis specialist
│ │ ├── code-reviewer.md # Code review specialist
│ │ └── code-simplifier.md # Code simplification specialist
│ ├── output_styles/
│ │ ├── claude-style-core.md # Core identity/personality
│ │ └── claude-style-orchestration.md # Delegation patterns
│ ├── claude-style-settings.json # Settings configuration
│ ├── commands/ # Empty directory for slash commands
│ └── skills/ # Empty directory for skills
│
└── prompts/ # Development/backup directory
├── .claude/ # Duplicate structure with issues
│ ├── agents/
│ │ ├── agent-expert.md -> BROKEN SYMLINK
│ │ ├── command-expert.md -> BROKEN SYMLINK
│ │ ├── code-architect.md # Duplicate (identical)
│ │ ├── code-explorer.md # Duplicate (typo: "KillShellias")
│ │ ├── code-reviewer.md # Duplicate (identical)
│ │ ├── code-simplifier.md # Duplicate (identical)
│ │ ├── code-shower.md # Actually "silent-failure-hunter"
│ │ ├── code-type-designer.md # Actually "type-design-analyzer"
│ │ └── code-flow-mapper.md # Flow analysis specialist
│ ├── skills/
│ │ └── skill-creator.md -> BROKEN SYMLINK
│ └── settings.local.json # Project-specific settings
│
├── claude-agent-agent.md # Source file for Agent Expert
├── claude-agent-command.md # Source file for Command Expert
├── claude-agent-skill.md # Source file for Skill Creator
├── claude-style-core.md # Duplicate of output_styles version
├── claude-style-orchestration.md # Duplicate of output_styles version
├── claude-style-settings.json # Output style reference (invalid JSON)
├── code-architect.md # Duplicate (identical)
├── code-explorer.md # Duplicate (identical to root)
├── code-reviewer.md # Duplicate (identical)
├── code-simplifier.md # Duplicate (identical)
└── tests/
└── core-identity.md # Test file

---

# Agent Inventory

Active Agents (in /home/skogix/skogix/.claude/agents/)

1. claude-agent-agent.md (Agent Expert)

- Name: agent-expert
- Color: orange
- Purpose: Meta-agent for creating specialized Claude Code agents
- Description: Specializes in agent design, prompt engineering, domain modeling, and agent best practices
- Status: ✅ Working, properly structured

2. claude-agent-command.md (Command Expert)

- Name: command-expert
- Color: purple
- Purpose: Meta-agent for creating CLI commands
- Description: Specializes in command design, argument parsing, task automation, and CLI development
- Status: ✅ Working, properly structured

3. claude-agent-skill.md (Skill Creator)

- Name: skill-creator
- Color: Not specified
- Purpose: Meta-agent for creating skills
- Description: Guide for creating effective skills that extend Claude's capabilities
- Status: ✅ Working, properly structured

4. code-architect.md

- Name: code-architect
- Color: green
- Model: sonnet
- Tools: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput
- Purpose: Designs feature architectures by analyzing existing codebase patterns
- Status: ✅ Working

5. code-explorer.md

- Name: code-explorer
- Color: yellow
- Model: sonnet
- Tools: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput
- Purpose: Deeply analyzes existing codebase features by tracing execution paths
- Status: ✅ Working

6. code-reviewer.md

- Name: code-reviewer
- Color: green
- Model: opus
- Purpose: Reviews code for adherence to project guidelines and best practices
- Status: ✅ Working, includes confidence scoring system

7. code-simplifier.md

- Name: code-simplifier
- Color: Not specified
- Model: opus
- Purpose: Simplifies code for clarity and maintainability while preserving functionality
- Status: ✅ Working

Additional Agents (only in /home/skogix/skogix/prompts/.claude/agents/)

8. code-shower.md (NAMING ISSUE)

- Actual Name: silent-failure-hunter
- Color: yellow
- Model: inherit
- Purpose: Reviews code for silent failures and inadequate error handling
- Status: ⚠️ Filename mismatch - file is named code-shower.md but agent name is silent-failure-hunter
- Issue: This is a comprehensive error handling auditor with zero tolerance for silent failures

9. code-type-designer.md (NAMING ISSUE)

- Actual Name: type-design-analyzer
- Color: pink
- Model: inherit
- Purpose: Expert analysis of type design, invariants, and encapsulation
- Status: ⚠️ Filename mismatch - file is named code-type-designer.md but agent name is type-design-analyzer

10. code-flow-mapper.md

- Name: code-flow-mapper
- Color: yellow
- Tools: Task, Bash, Glob, Grep, LS, ExitPlanMode, Read, Edit, MultiEdit, Write, NotebookRead, NotebookEdit, WebFetch, TodoWrite, and many MCP tools
- Purpose: Traces execution paths and file interconnections
- Status: ⚠️ Highly specialized workflow - expects specific file structure and report formats

---

# Issues Identified

Critical Issues

1. Broken Symlinks ❌

Location: /home/skogix/skogix/prompts/.claude/agents/

agent-expert.md -> ../../prompts/claude-agent-agent.md # BROKEN
command-expert.md -> ../../prompts/claude-agent-command.md # BROKEN

Problem: Symlinks use incorrect relative paths. From /home/skogix/skogix/prompts/.claude/agents/, the path ../../prompts/ resolves to /home/skogix/skogix/../prompts/ which
doesn't exist.

Fix: Should be ../claude-agent-agent.md and ../claude-agent-command.md (without the ../../prompts/ prefix)

2. Typo in code-explorer.md ❌

Location: /home/skogix/skogix/prompts/.claude/agents/code-explorer.md

Line 4:
tools: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShellias, BashOutput

Issue: KillShellias should be KillShell (extra "ias" at the end)

3. Agent Filename Mismatches ⚠️

Two agents have filenames that don't match their internal names:

| Filename              | Internal Name         | Issue                        |
| --------------------- | --------------------- | ---------------------------- |
| code-shower.md        | silent-failure-hunter | Completely different concept |
| code-type-designer.md | type-design-analyzer  | Similar but inconsistent     |

Impact: Users looking for "code-shower" won't find what they expect. The filename suggests showing code, but the agent hunts for silent failures.

Organizational Issues

4. Duplicate Files 📂

Multiple files exist in both /home/skogix/skogix/.claude/ and /home/skogix/skogix/prompts/:

Identical Duplicates:

- code-architect.md
- code-reviewer.md
- code-simplifier.md
- claude-style-core.md
- claude-style-orchestration.md

Near-Identical (except for the typo):

- code-explorer.md

Meta-agents:

- claude-agent-agent.md (in root .claude/agents/)
- claude-agent-command.md (in root .claude/agents/)
- claude-agent-skill.md (in root .claude/agents/)

These exist in prompts/ root AND are referenced by broken symlinks in prompts/.claude/agents/

5. Inconsistent Structure 🔀

Two .claude directories:

- /home/skogix/skogix/.claude/ - Main, active configuration
- /home/skogix/skogix/prompts/.claude/ - Development/testing copy?

Purpose unclear: Why maintain two separate .claude structures?

6. Invalid JSON ⚠️

Location: /home/skogix/skogix/prompts/claude-style-settings.json

--{
"outputStyle": "claude-style-settings.json"
}

Issue: Invalid JSON (starts with --). This appears to be a reference/comment rather than actual configuration.

---

Agent Quality Assessment

Well-Structured Agents ✅

code-reviewer.md:

- Excellent confidence scoring system (0-100)
- Clear review scope and responsibilities
- Structured output format
- Good examples in description

code-explorer.md:

- Clear 4-phase analysis approach
- Specific output guidance with file:line references
- Well-defined tools list

code-architect.md:

- Comprehensive 3-phase process
- Detailed output guidance with specific sections
- Clear decision-making framework

silent-failure-hunter (code-shower.md):

- Extremely comprehensive error handling analysis
- Detailed review process with specific questions
- Strong principles and validation framework
- Excellent output format specification

type-design-analyzer (code-type-designer.md):

- Sophisticated 5-dimension rating framework
- Clear analysis structure
- Practical improvement suggestions
- Good balance between safety and usability

Meta-Agents ✅

agent-expert (claude-agent-agent.md):

- Comprehensive guide for creating agents
- Multiple agent patterns (technical, domain, industry, workflow)
- Detailed best practices and examples
- Clear naming conventions and color coding

command-expert (claude-agent-command.md):

- Clear command structure templates
- Good documentation standards
- Proper argument handling guidance

skill-creator (claude-agent-skill.md):

- Clear anatomy of skills
- SKILL.md structure well-defined
- Bundled resources explained

---

# Recommendations

# Immediate Fixes (High Priority)

1. Fix the typo in code-explorer.md:

## Change from

tools: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShellias, BashOutput

## To

tools: Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput 2. Fix or remove broken symlinks:

- Option A: Fix the symlink paths
- Option B: Copy the actual files instead of using symlinks
- Option C: Remove the broken symlinks entirely

3. Rename mismatched agent files:
   mv code-shower.md silent-failure-hunter.md
   mv code-type-designer.md type-design-analyzer.md

# Organizational Improvements (Medium Priority)

4. Consolidate duplicate files:

- Decide which location is canonical
- Remove duplicates from the other location
- Consider if prompts/ is a development directory or should be cleaned up

5. Clarify directory purpose:

- Document what /home/skogix/skogix/prompts/ is for
- If it's for development/testing, add a README
- If it's obsolete, clean it up

6. Move unique agents to main .claude directory:

## Move these from prompts/.claude/agents/ to .claude/agents/

- silent-failure-hunter.md (after renaming)
- type-design-analyzer.md (after renaming)
- code-flow-mapper.md

# Long-term Improvements (Low Priority)

7. Add missing frontmatter:

- code-simplifier.md - missing color
- skill-creator.md - missing color

8. Standardize agent descriptions:

- Some agents have 3-4 examples, others have fewer
- Ensure all have practical, realistic examples
- Use consistent formatting

9. Create agent registry/index:

- Document all available agents
- Include when to use each one
- Cross-reference related agents

10. Fix invalid JSON:

- Either fix /home/skogix/skogix/prompts/claude-style-settings.json
- Or remove it if it's just a reference note

---

# Agent Categorization

## Meta-Agents (Agent Management)

- agent-expert - Creates specialized agents
- command-expert - Creates CLI commands
- skill-creator - Creates skills

## Code Analysis Agents

- code-explorer - Traces and analyzes features
- code-flow-mapper - Maps execution paths

## Code Quality Agents

- code-reviewer - Reviews against standards
- code-simplifier - Simplifies and refactors
- silent-failure-hunter - Error handling auditor
- type-design-analyzer - Type design analysis

## Code Design Agents

- code-architect - Designs feature architectures

---

# Summary Statistics

- Total unique agents: 10
- Working agents in main .claude/: 7
- Additional agents in prompts/.claude/: 3
- Broken symlinks: 3
- Duplicate files: 5 files duplicated across directories
- Naming mismatches: 2
- Typos found: 1
- Missing frontmatter fields: 2 agents missing color

---

# Conclusion

The agent system is well-designed with high-quality, specialized agents covering different aspects of software development. However, there are organizational issues stemming from
what appears to be a migration or reorganization in progress:

1. The main .claude/ directory contains 7 working agents
2. The prompts/.claude/ directory appears to be a development/testing area with 3 additional agents and broken symlinks
3. Several files are duplicated between locations
4. Some agents have filename/name mismatches that could confuse users

Primary recommendation: Clean up the prompts/ directory structure, fix the typo in code-explorer.md, rename mismatched agents, and migrate the unique agents
(silent-failure-hunter, type-design-analyzer, code-flow-mapper) to the main .claude/agents/ directory.
Done (37 tool uses · 46.4k tokens · 4m 25s)
