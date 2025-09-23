# Current Objectives at HQ

## Understanding Check: Architecture Clarified ✅
We now understand:
- This is HEADQUARTERS (the only one)
- We orchestrate, we don't implement
- Todos flow up, work flows down, confirmations flow back

## Active Orchestration Items

### From .skogai/todo (needs expansion):
- [ ] setup claudes config
- [ ] docs/claude/commands
- [ ] docs/claude/agents  
- [ ] docs/claude/output-style
- [ ] docs/claude/hooks
- [ ] rules (what should go in hooks, claude.md and .skogai?)
- [ ] plan
- [ ] definitions
- [ ] append and pop

### Current Focus: Establish HQ Operations
We're building the orchestration patterns that will:
1. Process incoming todos from all projects
2. Convert one-liners into work plans
3. Delegate to appropriate specialized projects
4. Track and confirm implementations

## Orchestration Principles
- **Ask first**: Never assume what a one-liner means
- **Plan thoroughly**: Create detailed work specs before delegation
- **Track systematically**: Know what's where at all times
- **Confirm everything**: PRs/diffs back to HQ

## Next Priority
Start processing the todo items above by:
1. Asking skogix what each means
2. Creating work plans
3. Identifying target projects
4. Beginning orchestration

## Success Metric
When any project can dump "implement X" in their .skogai/todo and it flows here, gets planned, delegated, and completed without the original project thinking about it.