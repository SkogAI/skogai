# skogai-marketplace

a local development marketplace for skogix claude plugins.

## structure

```
skogix/
├── .claude-plugin/
│   └── marketplace.json    # marketplace definition
├── plugins/
│   ├── hello-world/        # example plugin
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   ├── agents/
│   │   ├── skills/
│   │   ├── hooks/
│   │   └── README.md
│   └── [other-plugins]/    # add more plugins here
├── docs/                   # shared documentation
└── CLAUDE.md              # project instructions
```

## installation

from the parent directory of this folder:

```bash
# start claude code
claude

# add this directory as a marketplace
/plugin marketplace add ./skogix

# install a plugin
/plugin install hello-world@skogai-marketplace

# restart claude code to activate
```

## available plugins

- **hello-world**: comprehensive demonstration of all claude plugin component types (commands, agents, skills, hooks)

## adding a new plugin

1. create a new directory under `plugins/`:
   ```bash
   mkdir -p plugins/your-plugin/.claude-plugin
   ```

2. create `plugins/your-plugin/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "your-plugin",
     "description": "your plugin description",
     "version": "1.0.0",
     "author": {
       "name": "your-name",
       "email": "your-email"
     }
   }
   ```

3. add your plugin components:
   - `commands/` - slash commands (*.md)
   - `agents/` - specialized subagents (*.md)
   - `skills/` - model-invoked capabilities (*/SKILL.md)
   - `hooks/` - event-triggered automation (hooks.json)

4. register in `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "your-plugin",
     "source": "./plugins/your-plugin",
     "description": "your plugin description"
   }
   ```

5. reinstall marketplace and plugin:
   ```bash
   /plugin marketplace remove skogai-marketplace
   /plugin marketplace add ./skogix
   /plugin install your-plugin@skogai-marketplace
   ```

## development workflow

1. edit plugin files in `plugins/your-plugin/`
2. uninstall plugin: `/plugin uninstall your-plugin@skogai-marketplace`
3. reinstall plugin: `/plugin install your-plugin@skogai-marketplace`
4. restart claude code
5. test changes

## references

- [claude code plugins docs](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [plugin reference](https://docs.anthropic.com/en/docs/claude-code/plugins-reference)
- [skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [hooks guide](https://docs.anthropic.com/en/docs/claude-code/hooks)
