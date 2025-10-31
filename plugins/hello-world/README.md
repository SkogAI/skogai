# skogix-hello-world plugin

a comprehensive "hello world" plugin demonstrating all component types in a claude plugin.

## what this is

this plugin showcases every component type available in the claude plugin system:

- **commands**: user-invoked slash commands
- **agents**: specialized subagents with custom context
- **skills**: model-invoked capabilities with progressive loading
- **hooks**: event-triggered automation

## structure

```
skogix/
├── .claude-plugin/
│   ├── plugin.json         # plugin metadata
│   └── marketplace.json    # local marketplace config
├── commands/
│   └── hello.md           # /hello command
├── agents/
│   └── greeter.md         # greeter agent
├── skills/
│   └── hello-world/
│       └── SKILL.md       # hello-world skill
├── hooks/
│   └── hooks.json         # event hooks
└── README.md              # this file
```

## installation

from the parent directory of this folder:

```bash
# start claude code
claude

# add this directory as a marketplace
/plugin marketplace add ./skogix

# install the plugin
/plugin install skogix-hello-world@skogix-local

# restart claude code to activate
```

## usage

### command component

```bash
/hello
```

demonstrates slash commands - user-invoked instructions.

### agent component

the greeter agent is available via the Task tool. claude will use it when appropriate, or you can explicitly request it.

### skill component

ask about plugin skills or request a demonstration:

```
show me how the hello world skill works
```

the skill activates automatically when its description matches your request.

### hook component

the hook triggers on user prompt submission and shows a brief message.

## component comparison

| component | invocation | use case |
|-----------|-----------|----------|
| **command** | `/command-name` | user explicitly runs workflows |
| **agent** | Task tool or auto | specialized context for tasks |
| **skill** | automatic | domain knowledge, progressive loading |
| **hook** | event-driven | automation, validation, notifications |

## development workflow

to modify this plugin:

1. edit component files directly
2. uninstall: `/plugin uninstall skogix-hello-world@skogix-local`
3. reinstall: `/plugin install skogix-hello-world@skogix-local`
4. restart claude code
5. test changes

## component details

### commands (commands/*.md)

- markdown files with optional YAML frontmatter
- `description` field appears in `/help`
- content provides instructions to claude
- triggered by `/filename` (without .md)

### agents (agents/*.md)

- markdown files with optional YAML frontmatter
- provide specialized context and instructions
- invoked via Task tool with subagent_type
- useful for complex, multi-step specialized tasks

### skills (skills/*/SKILL.md)

- directory-based with required SKILL.md
- YAML frontmatter: `name` and `description` (required)
- progressive loading: metadata → instructions → resources
- automatically triggered when description matches task
- can include additional files (scripts, docs, templates)

### hooks (hooks/hooks.json)

- JSON file defining event → command mappings
- available events: user-prompt-submit, file-write, etc
- commands are shell commands with access to event variables
- output appears in conversation

## next steps

- explore each component by using it
- modify components to see how changes affect behavior
- create your own plugin based on this template
- combine components to build powerful workflows

## references

- [claude code plugins docs](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [plugin reference](https://docs.anthropic.com/en/docs/claude-code/plugins-reference)
- [skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [hooks guide](https://docs.anthropic.com/en/docs/claude-code/hooks)
