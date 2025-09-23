# HQ vs Dotfiles - The Duality

## The Two Faces of Skogai

### skogai (Main Repository - HQ)
**Location**: github.com/skogai/skogai (where we are now)
**Quantity**: ONE - there is only one HQ
**Role**: The brain, the orchestrator, the conductor

**Responsibilities**:
- Receive todos from the field
- Convert chaos into order
- Plan and orchestrate work
- Maintain the big picture
- Track ecosystem progress
- Define standards

**What lives here**:
- Orchestration logic
- Work planning capabilities
- Cross-project documentation
- Ecosystem vision
- Integration patterns
- The master todo aggregation

### .skogai (Submodule - Dotfiles)
**Location**: Embedded in EVERY skogai project
**Quantity**: MANY - one per project
**Role**: The nervous system endpoints

**Responsibilities**:
- Provide a todo dump location
- Supply project context to HQ
- Receive configurations from HQ
- Act as the backchannel

**What lives there**:
- todo file (for dumping tasks)
- Basic project docs
- User preferences (from HQ)
- Minimal configuration

## The Key Insight

**At HQ**: We think about "How do we convert 'setup serena' into an actionable plan?"

**In .skogai**: They think "I need to setup serena *dumps in todo* *moves on*"

## Information Flow

```
.skogai (in Project A): "fix auth" → 
.skogai (in Project B): "add tests" → SKOGAI HQ → Planning → Delegation
.skogai (in Project C): "update docs" →
```

HQ never does the work - it ensures the work gets done by the right specialist.