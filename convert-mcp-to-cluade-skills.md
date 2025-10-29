# mcp-to-skill: Convert MCP Servers to Claude Skills

I built a tool that converts any MCP server into a Claude Skill, reducing context usage by 90%.

## The Problem I Hit

Using Claude with multiple MCP servers, I kept running into issues:

- Had ~15 MCP servers configured
- Tool definitions ate 30-40k tokens _before_ any actual work
- Claude felt slower, responses got cut off
- Adding more tools made it worse

## What I Learned

Found out playwright-skill does something clever. Instead of loading all tool definitions upfront (standard MCP approach), it uses "progressive disclosure":

- **At startup**: Just loads name + description (~100 tokens)
- **When needed**: Loads full instructions (~5k tokens)
- **When executing**: Code runs outside context (0 tokens)

Huge difference from MCP's "load everything always" approach.

## What I Built

A converter that applies this pattern to _any_ MCP server:

```bash
python mcp_to_skill.py \
  --mcp-config github-mcp.json \
  --output-dir ./skills/github
```

It generates a complete Skill structure:

- `SKILL.md` - Instructions for Claude
- `executor.py` - Handles MCP communication dynamically
- Config files

## How It Works

**Traditional MCP**:

```
Startup: Load all 20 tools → 30k tokens
Claude works with 30k less context available
```

**Generated Skill**:

```
Startup: Load 20 skill names → 2k tokens
User asks for something → Load relevant skill → 5k tokens
Executor calls MCP tool → 0 tokens (runs externally)
```

## Real Numbers

Example with GitHub MCP server (8 tools):

| Approach | Tokens at Startup | Tokens When Used |
| -------- | ----------------- | ---------------- |
| MCP      | 8,000 always      | 8,000 always     |
| Skill    | 100 idle          | 5,000 active     |
| Savings  | 98.75%            | 37.5%            |

With 20+ tools, savings are even bigger.

## How The Generated Skill Works

1. **Claude sees**: "github skill - access to GitHub API" (~100 tokens)
2. **User asks**: "create an issue on my repo"
3. **Claude loads**: Full SKILL.md with tool list (~5k tokens)
4. **Claude generates**: JSON tool call

```json
{
  "tool": "create_issue",
  "arguments": { "title": "...", "body": "..." }
}
```

5. **Executor runs**: Connects to MCP server, invokes tool, returns result
6. **Context used**: 5k for skill + 0 for execution

Compare to MCP: 8k always loaded whether used or not.

## Code Example

The converter introspects your MCP server and generates everything automatically:

```python
# Input: Your MCP config
{
  "name": "github",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {"GITHUB_TOKEN": "..."}
}

# Output: Complete Skill
skills/github/
├── SKILL.md          # What Claude reads
├── executor.py       # Calls MCP dynamically
├── mcp-config.json   # Server settings
└── package.json      # Dependencies
```

The generated executor handles all MCP communication. Claude just needs to generate the tool call JSON.

## Installation

```bash
# Get the converter
git clone https://github.com/GBSOSS/-mcp-to-skill-converter
cd mcp-to-skill-converter

# Convert an MCP server
python mcp_to_skill.py \
  --mcp-config your-mcp-config.json \
  --output-dir ./skills/your-skill

# Install and use
cd skills/your-skill
pip install mcp
cp -r . ~/.claude/skills/your-skill
```

Now Claude can use those tools with minimal context overhead.

## What It Works With

Any standard MCP server:

- ✅ @modelcontextprotocol/server-github
- ✅ @modelcontextprotocol/server-slack
- ✅ @modelcontextprotocol/server-filesystem
- ✅ @modelcontextprotocol/server-postgres
- ✅ Custom MCP servers

Basically anything implementing the MCP protocol.

## When To Use This

**Use mcp-to-skill when:**

- You have many tools (10+)
- Context window space is tight
- Most tools won't be used in each conversation
- Tools are relatively independent

**Stick with MCP when:**

- You have few tools (1-5)
- Tools need complex OAuth flows
- You need persistent database connections
- Cross-platform standardization is critical

**Use both:**

- MCP for core tools always needed
- Skills for extended toolset
- Get best of both worlds

## Limitations

Still early stage:

- Requires `mcp` Python package
- MCP server must be accessible
- Some complex auth flows might need adjustment
- Haven't tested with every MCP server

## Why This Matters

As we add more capabilities to Claude, context becomes the bottleneck. MCP solved the N×M integration problem, but at the cost of context efficiency.

Skills + this converter give you both:

- Standardized MCP servers (don't rebuild tools)
- Progressive disclosure (only load what you need)
- Unlimited tool capacity (context doesn't grow with tool count)

## Inspiration

Credit to @lackeyjb for playwright-skill which showed this pattern works. This tool just makes it work for any MCP server.

## Code

GitHub: https://github.com/GBSOSS/-mcp-to-skill-converter

Feedback welcome. This is a proof of concept showing the pattern, not a finished product.

---

**Tech Stack**: Python, asyncio, MCP SDK
**Status**: Functional but early
**License**: MIT
