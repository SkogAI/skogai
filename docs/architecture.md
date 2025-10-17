---
title: skogai/architecture
description: Architecture overview of SkogAI - HQ vs Dotfiles
---

[$TODO]

1. this document should be generalized to cover all skogai architecture and subitems for those can be created; skogai/architecture/foo
   [/$TODO]

# SkogAI Architecture - HQ vs Dotfiles

## The Two Components of SkogAI

### skogai (Main Repository - HQ)

**Location**: github.com/skogix/skogai (this repository)
**Quantity**: ONE - there is only one HQ
**Role**: The orchestration hub, the conductor

**Responsibilities**:

- Receive todos from all projects via .skogai submodules
- Convert one-liner todos into detailed work plans
- Plan and orchestrate work across specialized projects
- Maintain ecosystem-wide documentation and standards
- Track overall progress and dependencies
- Define integration patterns

**What lives here**:

- Orchestration logic and workflows
- Cross-project documentation
- Ecosystem vision and standards
- Master todo aggregation
- Integration patterns
- Work planning capabilities

### .skogai (Submodule - Dotfiles)

**Location**: Embedded in EVERY skogai project as git submodule
**Quantity**: MANY - one per project
**Role**: Minimal configuration and todo collection endpoints

**Responsibilities**:

- Provide a standardized todo dump location
- Supply basic project context to HQ
- Receive shared configurations from HQ
- Act as the communication backchannel

**What lives there**:

- `todo` file for task dumping
- Basic project documentation
- User preferences (synchronized from HQ)
- Minimal bootstrapping configuration

## Information Flow

```
[Project A] → dumps todo → [.skogai/todo] ↗
[Project B] → dumps todo → [.skogai/todo] → [SKOGAI HQ]
[Project C] → dumps todo → [.skogai/todo] ↘
                                              ↓
                                   [Orchestration & Planning]
                                              ↓
                           [Delegate to specialized projects]
                                              ↓
                                       [Confirm via PRs]
```

## Key Design Principles

### At HQ (This Repository)

- **Think in systems**, not implementations
- **Orchestrate work**, never implement directly
- **Ask clarifying questions** on one-liner todos
- **Create detailed work specifications** for delegation
- **Track ecosystem-wide progress** and dependencies

### In .skogai (Submodules)

- **Minimal footprint** in each project
- **Quick todo dumping** without context switching
- **Standardized structure** across all projects
- **Git-tracked** for version control

## The Key Insight

**At HQ**: "How do we convert 'setup serena' into an actionable plan for the right project?"

**In .skogai**: "I need to setup serena" _dumps in todo_ _moves on with work_

This separation allows developers to quickly capture tasks without breaking flow, while HQ handles the complexity of planning and coordination.
