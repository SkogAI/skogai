# Arch-Wiki Skill - Identified Gaps

## Baseline Test Results

**Test:** Scenario 1 - Debugging a crashed application

**Outcome:**
- ✅ Skill was discoverable (agent found it)
- ⚠️ Efficiency issue: Required 2 Read operations even though Quick Reference had complete info
- ✅ Final result was complete and actionable
- ❌ Quick Reference didn't feel authoritative/complete enough to be the stopping point

## Gap Analysis

### 1. Discoverability (CSO) Issues

**Current description:**
```yaml
description: Use when working with Arch Linux, pacman, AUR, system administration, installation, configuration, or troubleshooting Arch-based systems
```

**Problems:**
- Too generic - just lists technology names
- No specific symptoms, error messages, or problem triggers
- Doesn't help Claude differentiate between types of Arch Linux tasks
- Missing keywords for common scenarios: "crashed", "can't install", "permission denied", "pacman error"

**Should include:**
- Specific symptoms (crashes, package conflicts, permission errors)
- Error message patterns ("error: failed to commit transaction", "conflicting files")
- Task triggers (debugging crashes, installing packages, configuring desktop, setting up services)

### 2. Structure Issues

**Problem areas:**
1. **Quick Reference comes before "When to Use"** (line 22 vs line 10)
   - Users see examples before knowing when to use the skill

2. **Key Concepts buried at line 175**
   - Should be near top for context before diving into commands

3. **"Working with This Skill" section at line 229**
   - Navigation guidance comes too late
   - Should be near the top after Overview

4. **Multiple fragmented sections at end:**
   - Troubleshooting Tips (line 295)
   - Notes (line 318)
   - Updating (line 325)
   - These should be integrated or removed

5. **Reference Files section (line 199)**
   - Just lists files without guidance on when to use each
   - Doesn't explain the relationship between Quick Reference and reference files

**Optimal structure should be:**
1. Overview - What is this skill?
2. When to Use - Triggering conditions
3. Quick Reference - Most common tasks
4. Key Concepts - Core terminology
5. Common Workflows - End-to-end examples
6. Reference Files - Deep dives with clear guidance
7. Troubleshooting - Common problems

### 3. Quick Reference Issues

**Current state:**
- Has good commands but feels incomplete
- Examples are isolated without context
- No indication whether this is sufficient or if you need reference files
- Missing many common tasks that should be in Quick Reference

**Needs:**
- More complete coverage of frequent tasks
- Authority signals: "For most tasks, this Quick Reference is sufficient"
- Better organization by task type (not by technology)
- Clear indication when to go to reference files

**Missing Quick Reference items:**
- Package search: `pacman -Ss keyword`
- Package info: `pacman -Si package`
- Check installed packages: `pacman -Q | grep keyword`
- Clean package cache: `pacman -Sc`
- Fix broken symlinks after upgrade
- Common pacman error resolutions

### 4. Example Issues

**Current:**
- Examples exist but are scattered
- No end-to-end workflows
- Missing error scenarios and resolutions
- Commands shown without expected output

**Needs:**
- Complete workflows: "Installing and configuring SSH" (not just install command)
- Error examples: "What to do when pacman says 'conflicting files'"
- Expected output shown for commands
- Before/after states
- Real-world scenarios: "My system won't boot after update"

**Specific missing workflows:**
1. Complete package installation with AUR
2. Debugging a service that won't start
3. Fixing a failed system upgrade
4. Setting up a complete desktop environment
5. Configuring GPU drivers (common pain point)

### 5. Keyword Coverage

**Missing keywords for search:**
- Error messages: "conflicting files", "failed to commit", "unable to lock database"
- Symptoms: "won't boot", "black screen", "no sound", "slow boot"
- Tasks: "can't connect", "permission denied", "package not found"
- Tools: "systemctl", "journalctl", "lsmod", "dmesg"

### 6. Authority and Confidence

**Current issues:**
- Doesn't establish why reference files are trustworthy (official Arch Wiki)
- Doesn't indicate currency of information
- Doesn't guide when Quick Reference is sufficient vs when to deep-dive

**Needs:**
- Clear statement: "Quick Reference covers 80% of tasks"
- Authority: "All content from official Arch Wiki (continuously updated)"
- Currency: When these docs were last updated
- Confidence levels: "For standard tasks, use Quick Reference. For complex/rare issues, see reference files."

## Priority Fixes for GREEN Phase

### High Priority (Must fix):
1. ✅ Rewrite description with specific symptoms and error patterns
2. ✅ Reorder sections: Overview → When to Use → Quick Reference → Key Concepts → ...
3. ✅ Expand Quick Reference with missing common tasks
4. ✅ Add authority signal to Quick Reference
5. ✅ Add common error keywords throughout

### Medium Priority (Should fix):
6. ✅ Add 2-3 complete workflow examples
7. ✅ Improve Reference Files section guidance
8. ✅ Consolidate fragmented end sections
9. ✅ Add expected command outputs

### Low Priority (Nice to have):
10. Add more error scenarios
11. Add troubleshooting decision tree
12. Add package search tips

## Success Criteria

After fixes:
- Description includes specific symptoms/errors
- Agent can use Quick Reference without reading reference files for common tasks
- Structure flows logically: Overview → When → How → Deep Dives
- Keywords present for common scenarios
- At least 2 complete end-to-end workflow examples
