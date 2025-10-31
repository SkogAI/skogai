# 🚀 The Agentic Startup - User Guide

Welcome to The Agentic Startup framework! This guide will help you understand how to work with this structured approach to building features and solving problems.

## Quick Start

The framework provides four main commands that follow a natural workflow:

```
/start:analyze → /start:specify → /start:implement → /start:refactor
```

---

## The Four Core Commands

### 1️⃣ `/start:analyze [area]`

**Purpose**: Discover and document what exists in your codebase or domain.

**When to use**:
- Exploring unfamiliar territory
- Understanding existing systems before making changes
- Need to gather context about business rules, technical patterns, or integrations
- Starting a new project area

**What it does**:
- Iteratively explores the specified area
- Documents business rules, technical patterns, and system interfaces
- Creates organized documentation for future reference
- Identifies integration points and dependencies

**Examples**:
```bash
/start:analyze business      # Discover business rules and domain logic
/start:analyze technical     # Explore technical architecture and patterns
/start:analyze security      # Review security implementations
/start:analyze authentication flow  # Deep dive into specific area
```

**Output**: Documentation files in your project that capture discovered knowledge

---

### 2️⃣ `/start:specify [requirement]`

**Purpose**: Transform ideas into comprehensive specifications.

**When to use**:
- You have a feature request or requirement
- Need to plan before implementing
- Want clear acceptance criteria and test strategies
- Building something new or making significant changes

**What it does**:
- Creates detailed specification documents
- Defines acceptance criteria
- Plans implementation approach
- Outlines test strategy
- Identifies dependencies and risks

**Examples**:
```bash
/start:specify user authentication system
/start:specify payment processing integration
/start:specify admin dashboard with analytics
/start:specify API rate limiting middleware
```

**Output**: A specification document (e.g., `S001-user-authentication.md`) with:
- Feature overview and objectives
- Acceptance criteria
- Implementation plan
- Test strategy
- Dependencies and risks

---

### 3️⃣ `/start:implement [spec-id]`

**Purpose**: Execute the implementation plan from a specification.

**When to use**:
- You have a spec ready to build
- Want coordinated, parallel execution by specialists
- Ready to write code based on your plan

**What it does**:
- Reads the specification document
- Coordinates multiple specialist agents in parallel
- Implements the planned solution
- Ensures quality and testing
- Delivers working code

**Examples**:
```bash
/start:implement S001                    # By spec number
/start:implement S001-user-authentication # By full spec name
/start:implement user-authentication     # By feature name
```

**Output**: Working code that implements the specification

---

### 4️⃣ `/start:refactor [description]`

**Purpose**: Improve code quality without changing behavior.

**When to use**:
- Code works but is messy or hard to maintain
- Need better organization or patterns
- Want to reduce technical debt
- Preparing for future feature additions

**What it does**:
- Analyzes existing code
- Applies better patterns and practices
- Improves readability and maintainability
- Preserves existing functionality
- Includes comprehensive testing

**Examples**:
```bash
/start:refactor authentication module for better testability
/start:refactor API handlers to use consistent error handling
/start:refactor database layer to reduce query duplication
```

**Output**: Refactored code with improved quality and maintainability

---

## Common Workflows

### Building a New Feature

```bash
1. /start:specify [your feature idea]
   → Review and approve the generated spec

2. /start:implement [spec-id]
   → Let the specialists build it

3. (Optional) /start:refactor [improvements needed]
   → Polish and optimize
```

### Understanding Existing Code

```bash
1. /start:analyze [area or feature name]
   → Explore and document what exists

2. (If making changes) /start:specify [what you want to change]
   → Plan your changes

3. /start:implement [spec-id]
   → Execute the changes
```

### Improving Code Quality

```bash
1. (Optional) /start:analyze technical
   → Identify technical debt areas

2. /start:refactor [specific improvement]
   → Clean up the code
```

---

## The Philosophy

### Speed + Quality
- We execute fast BUT never compromise on quality
- Parallel execution for maximum velocity
- Proper planning prevents rework

### Documentation
- Document what matters
- Capture reusable patterns
- Build institutional knowledge

### Specialist Coordination
- Leverage experts for their domain
- Run parallel when possible
- Synthesize results into unified solutions

---

## Tips for Success

### 1. Start with Analysis (when needed)
If you're working in unfamiliar territory, use `/start:analyze` first to understand the landscape before making changes.

### 2. Be Specific in Specifications
The better your initial description in `/start:specify`, the better the resulting spec and implementation will be.

### 3. Review Before Implementing
Always review the generated specification before running `/start:implement`. Make sure it matches your expectations.

### 4. Trust the Process
The framework coordinates multiple specialists in parallel. Let it work its magic - don't micro-manage.

### 5. Refactor Proactively
Don't wait for code to become unmaintainable. Use `/start:refactor` regularly to keep quality high.

---

## Framework Structure

Your project will develop this structure:

```
.start/
├── specs/              # Specifications (S001-feature.md)
├── docs/               # Documentation from analysis
│   ├── business/      # Business rules
│   ├── technical/     # Technical patterns
│   └── integration/   # Integration interfaces
└── README.md          # Framework overview
```

---

## Example Session

```bash
# User wants to add a new feature
You: "I need to add user authentication with JWT tokens"

# Step 1: Create specification
/start:specify user authentication with JWT tokens
→ Reviews generated S001-user-authentication.md
→ Approves or requests changes

# Step 2: Implement it
/start:implement S001
→ Multiple specialists work in parallel:
  - Security review
  - Database schema
  - API endpoints
  - Frontend components
  - Tests
→ Feature is delivered!

# Step 3 (later): Clean up if needed
/start:refactor authentication middleware for better error handling
```

---

## Getting Help

- **Framework Issues**: Check `.start/README.md` in your project
- **Claude Code Help**: Type `/help` for general Claude Code assistance
- **Ask Questions**: Just ask! The framework is designed to guide you through the process

---

## Remember

✅ **DO**:
- Use `/start:analyze` when exploring unfamiliar code
- Review specifications before implementing
- Let specialists work in parallel
- Document important patterns
- Refactor proactively

❌ **DON'T**:
- Skip planning for complex features
- Ignore the generated specifications
- Try to micro-manage the implementation
- Forget to test
- Let technical debt accumulate

---

**Ready to build something amazing? Let's go! 🚀**
