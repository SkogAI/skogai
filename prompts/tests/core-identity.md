# Claude Core Identity Test

## Question 1
Should you tell an agent HOW to solve something?

No. Specify WHAT to achieve and WHERE to find resources.

## Question 2
Agent asks how to create a skill - what do you provide?

Point to ~/.claude/skills/skill-creator/SKILL.md and an example like agent-toolkit/.

## Question 3
Can agents remember what you discussed three messages ago?

No. Every agent starts with fresh context and zero shared memory.

## Question 4
User says "use the process we discussed" - what's wrong?

Abstract reference. Need concrete path to actual file containing the process.

## Question 5
Better: "implement auth cleverly" or "implement OAuth login - see auth.example.ts"?

Second option. Concrete file path beats vague concepts like "cleverly."

## Question 6
Agent needs to validate code - prescribe steps or point?

Point to validator script path and example, let agent determine how.

## Question 7
What beats explaining how something works in detail?

Pointing to working example file that demonstrates the pattern in action.

## Question 8
New agent, same session - does it know context?

No. Fresh context always. Must provide paths and resources again.

## Question 9
"Create feature using best practices" - is this good delegation?

No. Too abstract. Specify outcome and point to concrete examples of practices.

## Question 10
Which is concrete: "following the pattern" or "see src/pattern.ts:42"?

Second. File path with line number is maximally concrete and navigable.
