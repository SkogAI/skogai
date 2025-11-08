# Arch Wiki Skill - Test Scenarios

## Purpose
Test if the arch-wiki skill is discoverable, navigable, and useful for common Arch Linux tasks.

## Scenario 1: Debugging a Crashed Application
**User request:** "My application just crashed on Arch Linux. I need to get a backtrace for a bug report."

**Expected behavior:**
- Agent should load arch-wiki skill
- Find the gdb/debugging section
- Provide concrete gdb commands: `gdb /path/to/program`, `run`, `bt full`
- Mention debug symbols and debuginfod

**Success criteria:**
- Finds debugging section quickly
- Provides actionable commands
- Explains what the commands do

## Scenario 2: Setting Up SSH Server
**User request:** "I need to set up an SSH server on my Arch Linux machine so I can remote in."

**Expected behavior:**
- Agent should load arch-wiki skill
- Navigate to networking.md → SSH section
- Provide: `pacman -S openssh`
- Mention: config file location, systemctl enable/start, firewall considerations

**Success criteria:**
- Complete setup instructions
- Mentions security considerations
- Provides systemctl commands

## Scenario 3: Installing from AUR
**User request:** "How do I install a package from the AUR on Arch?"

**Expected behavior:**
- Agent should load arch-wiki skill
- Find package_management.md
- Explain AUR concept (not official repo, community-maintained)
- Mention AUR helpers or manual process with makepkg

**Success criteria:**
- Explains what AUR is
- Provides installation method
- Warns about trust/security

## Scenario 4: Changing Default Shell
**User request:** "I want to change my default shell from bash to zsh on Arch."

**Expected behavior:**
- Agent should load arch-wiki skill
- Find shell configuration section
- Provide: `chsh -l` to list shells
- Provide: `chsh -s /usr/bin/zsh` to change

**Success criteria:**
- Finds info in Quick Reference or main content
- Provides both list and change commands
- Mentions need to install zsh first if not present

## Scenario 5: MATE Desktop Configuration
**User request:** "I'm using MATE on Arch and the compositor is causing screen tearing. How do I disable it?"

**Expected behavior:**
- Agent should load arch-wiki skill
- Find MATE section in Quick Reference or desktop_environments.md
- Provide: `gsettings set org.mate.Marco.general compositing-manager false`

**Success criteria:**
- Finds MATE-specific configuration
- Provides exact gsettings command
- Explains what compositing is

## Scenario 6: False Positive Test (Should NOT match)
**User request:** "My tests are flaky and using setTimeout. Is there a better approach?"

**Expected behavior:**
- Agent should NOT load arch-wiki skill
- Should load condition-based-waiting or testing skill instead

**Success criteria:**
- Arch-wiki is not loaded
- Correct testing-related skill is used

## Scenario 7: Package Update Issues
**User request:** "I ran pacman -Syu and got errors about conflicting files. How do I fix this?"

**Expected behavior:**
- Agent should load arch-wiki skill
- Find package management troubleshooting
- Suggest: checking output, using --overwrite if safe, checking mirrors

**Success criteria:**
- Finds troubleshooting section
- Provides multiple resolution approaches
- Warns about being careful with overwrite

## Testing Protocol

### Baseline Test (Current Skill)
1. Run each scenario with a fresh subagent
2. Document:
   - Did agent load arch-wiki skill? (discoverability)
   - How long to find the right section? (navigation)
   - Were instructions complete and actionable? (usefulness)
   - What information was missing or hard to find?

### After Edit Test
1. Run same scenarios with edited skill
2. Compare: improvements in discoverability, navigation, completeness
3. Identify any remaining gaps

### Success Metrics
- **Discoverability**: Agent loads skill for 6/7 scenarios (excluding false positive)
- **Navigation**: Agent finds correct section in < 2 read operations
- **Usefulness**: Provides complete, actionable commands for each scenario
- **Precision**: Does NOT load for false positive scenario
