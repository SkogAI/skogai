# simple skill example

this is a minimal skill demonstrating the essential structure.

## use case

a skill that helps users write better git commit messages following conventional commits format.

## skill file: skills/commit-helper/SKILL.md

```markdown
---
name: commit-helper
description: helps write conventional commit messages following the conventional commits specification with proper type, scope, and description
---

# commit helper skill

this skill helps you write better git commit messages.

## conventional commits format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

## common types

- **feat**: new feature
- **fix**: bug fix
- **docs**: documentation only
- **style**: formatting, missing semicolons, etc
- **refactor**: code change that neither fixes a bug nor adds a feature
- **perf**: performance improvement
- **test**: adding missing tests
- **chore**: changes to build process or auxiliary tools

## workflow

when user asks for help with commit messages:

1. ask what changes they made
2. suggest appropriate type
3. suggest scope if applicable
4. draft a concise description (50 chars or less)
5. add body if changes need explanation
6. add footer for breaking changes or issue references

## examples

```
feat(auth): add oauth2 login support
fix(api): handle null values in user endpoint
docs(readme): update installation instructions
refactor(utils): simplify date formatting logic
```

## tips

- use imperative mood ("add" not "added")
- don't capitalize first letter
- no period at the end
- keep description under 50 characters
- use body for "why" not "what"
```

## why this works

- **clear trigger terms**: "commit message", "conventional commits"
- **focused purpose**: only handles commit message formatting
- **includes examples**: shows concrete usage
- **actionable workflow**: clear steps for claude
- **no tools needed**: just knowledge and guidance

## triggering this skill

users might say:
- "help me write a commit message"
- "what's the conventional commits format?"
- "i need to commit these changes"
- "how should i format this commit?"
