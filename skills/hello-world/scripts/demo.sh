#!/usr/bin/env bash

# demonstration script for hello-world skill
# shows how skills can include executable resources

set -e

echo "=== hello world skill - script demonstration ==="
echo ""

echo "1. skill information:"
echo "   - name: hello-world"
echo "   - location: skills/hello-world/"
echo "   - purpose: comprehensive skill demonstration"
echo ""

echo "2. skill structure:"
tree -L 2 skills/hello-world/ 2>/dev/null || {
  find skills/hello-world -type f -o -type d | sort | sed 's|skills/hello-world||' | sed 's|^|   |'
}
echo ""

echo "3. progressive loading levels:"
echo "   level 1: metadata (YAML frontmatter) - always loaded"
echo "   level 2: instructions (SKILL.md content) - loaded on trigger"
echo "   level 3: resources (reference.md, examples/, scripts/) - loaded on-demand"
echo ""

echo "4. file sizes:"
if command -v wc &> /dev/null; then
  echo "   SKILL.md:        $(wc -w < skills/hello-world/SKILL.md) words"
  echo "   reference.md:    $(wc -w < skills/hello-world/reference.md) words"
  echo "   examples:        $(find skills/hello-world/examples -type f -name "*.md" -exec wc -w {} + | tail -1 | awk '{print $1}') words"
fi
echo ""

echo "5. tool access:"
echo "   allowed-tools: Read, Bash, Glob"
echo "   you can verify this script ran using Bash tool!"
echo ""

echo "=== demonstration complete ==="
echo ""
echo "key insight: scripts are resources (level 3) that load and execute on-demand"
echo "this script loaded and ran because the skill's instructions referenced it"
