---
name: arch-wiki
description: Use when debugging crashes on Arch Linux (gdb, backtraces), resolving pacman errors (conflicting files, failed to commit, locked database), installing AUR packages, configuring system services (systemd), setting up desktop environments (MATE, window managers), troubleshooting hardware (GPU, audio), or managing packages - provides official Arch Wiki commands and patterns
---

# Arch Linux Wiki Skill

## Overview

**Comprehensive guidance for Arch Linux system administration, package management, configuration, and troubleshooting, extracted from official Arch Wiki documentation.**

**Authority:** All content sourced from https://wiki.archlinux.org/, continuously updated by the Arch Linux community. Reference files preserve structure and examples from source docs.

**Coverage:** The Quick Reference below covers ~80% of common tasks. For complex/rare issues, see Reference Files section for deep dives.

## When to Use This Skill

**Trigger when encountering:**
- **Package Management**: Installing, updating, removing packages with pacman; working with AUR; resolving "conflicting files", "failed to commit transaction", "unable to lock database" errors
- **System Administration**: Configuring systemd services, managing users, setting up shells, kernel modules
- **Desktop Environment**: Installing/configuring MATE, window managers, display managers; fixing screen tearing, compositing issues
- **Debugging**: Application crashes, getting gdb backtraces, analyzing core dumps, obtaining traces for bug reports
- **Networking**: Setting up SSH, VPN, network managers, firewalls; troubleshooting connectivity
- **Hardware**: Configuring GPUs (AMD, NVIDIA, Intel), audio (PipeWire, ALSA), peripherals
- **Boot Issues**: Black screen, slow boot, failed services, rescue mode
- **Development**: Compiling kernel modules, setting up build environments, debugging with gdb

## Key Concepts

**Package Management:**
- **pacman**: Official Arch Linux package manager for installing, updating, removing packages
- **AUR (Arch User Repository)**: Community-driven repository for user-submitted packages (use with caution)
- **PKGBUILD**: Build script defining how to build and package software
- **makepkg**: Tool to build packages from PKGBUILD files

**System:**
- **systemd**: Init system and service manager (use `systemctl` to manage services)
- **journalctl**: View systemd logs
- **chsh**: Change default login shell

**Debugging:**
- **gdb (GNU Debugger)**: Debug programs, examine crashes, get backtraces
- **Debuginfod**: Automatically downloads debug symbols from https://debuginfod.archlinux.org
- **Core dump**: Memory snapshot of crashed program for post-mortem analysis
- **Backtrace**: Sequence of function calls leading to a crash

**Desktop:**
- **Window Manager**: Controls window appearance/behavior (Marco for MATE, River for Wayland)
- **Compositing**: Rendering technique for transparency, shadows, effects (can cause screen tearing)

## Quick Reference

**For most common tasks, this Quick Reference is sufficient. See Reference Files for complex scenarios.**

### Essential Package Management

**Basic operations:**
```bash
# Update package database and upgrade all packages
pacman -Syu

# Install a package
pacman -S package_name

# Remove a package (keep dependencies)
pacman -R package_name

# Remove a package and unused dependencies
pacman -Rs package_name

# Search for a package
pacman -Ss search_term

# Get detailed package information
pacman -Si package_name

# List all installed packages
pacman -Q

# Search installed packages
pacman -Q | grep search_term

# Check which package owns a file
pacman -Qo /path/to/file

# Clean package cache (remove old versions)
pacman -Sc

# List explicitly installed packages
pacman -Qe
```

**Install multiple related packages:**
```bash
# Pattern expansion
pacman -S plasma-{desktop,mediacenter,nm}
```

**Resolve common errors:**
```bash
# Error: "conflicting files" - use with caution, only if you understand the conflict
pacman -S package_name --overwrite '*'

# Error: "unable to lock database" - check if pacman is already running, or remove stale lock
rm /var/lib/pacman/db.lck

# Error: "failed to commit transaction (invalid or corrupted package)"
# Update mirrorlist and clear cache:
pacman -Scc
pacman -Syyu
```

### Debugging Crashed Applications

**Get a backtrace with gdb:**
```bash
# Install gdb if not present
pacman -S gdb

# Start gdb with crashed program
gdb /path/to/executable

# Inside gdb, run the program
(gdb) run arg1 arg2

# When crash occurs, enable logging and get backtrace
(gdb) set logging file backtrace.log
(gdb) set logging enabled on
(gdb) bt full

# Debuginfod will automatically download symbols - answer "y" when prompted
```

**Attach gdb to running process:**
```bash
# Find process ID
pidof program_name

# Attach (may need sudo)
gdb -p PID

# Continue execution
(gdb) continue
```

**Analyze core dump:**
```bash
# If core dumps are enabled
gdb /path/to/application /path/to/core

# Get backtrace
(gdb) bt full
```

### System Service Management

```bash
# Start a service
systemctl start service_name

# Stop a service
systemctl stop service_name

# Enable service to start at boot
systemctl enable service_name

# Enable and start immediately
systemctl enable --now service_name

# Check service status
systemctl status service_name

# View service logs
journalctl -u service_name

# View logs from current boot
journalctl -b

# Follow logs in real-time
journalctl -f
```

### Shell Configuration

```bash
# List all installed shells
chsh -l

# Change your default shell
chsh -s /usr/bin/zsh

# For systemd-homed users
homectl update --shell=/usr/bin/zsh username
```

### Desktop Environment (MATE)

```bash
# Disable compositing (fixes screen tearing)
gsettings set org.mate.Marco.general compositing-manager false

# Enable accessibility features (before first MATE start)
gsettings set org.mate.interface accessibility true

# Disable low battery notifications
gsettings set org.mate.power-manager notify-discharging false
```

### SSH Server Setup

```bash
# Install OpenSSH
pacman -S openssh

# Enable and start SSH service
systemctl enable --now sshd

# Check if running
systemctl status sshd

# Configuration file
/etc/ssh/sshd_config

# Client configuration (per-user)
~/.ssh/config
```

### Kernel Module Compilation

```bash
# Install build essentials
pacman -S base-devel linux-headers

# Prepare kernel source
make mrproper
zcat /proc/config.gz > .config
make oldconfig
make prepare
make modules_prepare

# Compile specific module (example: btrfs)
make M=fs/btrfs
```

### Hardware Troubleshooting

```bash
# Check loaded kernel modules
lsmod

# Get module information
modinfo module_name

# View kernel messages (hardware detection)
dmesg

# View hardware logs from current boot
journalctl -b -k
```

## Common Workflows

### Complete SSH Server Setup

**Problem:** Need remote access to Arch Linux machine

**Solution:**
```bash
# Step 1: Install SSH server
pacman -S openssh

# Step 2: Start and enable service
systemctl enable --now sshd

# Step 3: Check firewall (if using)
# Allow SSH port 22
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Or with ufw:
ufw allow ssh

# Step 4: Test locally
ssh localhost

# Step 5: Connect from remote machine
ssh user@arch-machine-ip

# Step 6: (Optional) Configure key-based auth
# On client machine:
ssh-keygen -t ed25519
ssh-copy-id user@arch-machine-ip

# Step 7: (Security) Disable password auth in /etc/ssh/sshd_config
# PasswordAuthentication no
# Then: systemctl restart sshd
```

**Expected result:** Secure remote access to your Arch Linux machine

### Debugging a Crashed Application

**Problem:** Application crashed, need backtrace for bug report

**Solution:**
```bash
# Step 1: Install debugging tools
pacman -S gdb

# Step 2: Run application under gdb
gdb /usr/bin/application

# Step 3: Run the program (it will crash)
(gdb) run

# Expected output when crash occurs:
# Program received signal SIGSEGV, Segmentation fault.
# 0x00007ffff7a1234 in some_function ()

# Step 4: Configure logging
(gdb) set logging file ~/crash_backtrace.log
(gdb) set logging enabled on

# Output: Copying output to ~/crash_backtrace.log.

# Step 5: Get full backtrace
(gdb) bt full

# Expected output: Full stack trace with local variables
# Debuginfod will download symbols automatically

# Step 6: Exit gdb
(gdb) quit

# Step 7: Include ~/crash_backtrace.log in bug report
```

**Expected result:** Complete backtrace with symbols ready for bug report

### Resolving "Conflicting Files" Package Error

**Problem:** `pacman -S package` fails with "conflicting files" error

**Solution:**
```bash
# Step 1: Read the error message carefully
# Example error:
# error: failed to commit transaction (conflicting files)
# package: /usr/bin/program exists in filesystem

# Step 2: Identify which package owns the conflicting file
pacman -Qo /usr/bin/program

# If output is "error: No package owns /usr/bin/program":
# File is orphaned, safe to overwrite

# Step 3: Use --overwrite flag (ONLY if you understand the conflict)
pacman -S package --overwrite /usr/bin/program

# Or overwrite all conflicting files (use with extreme caution):
pacman -S package --overwrite '*'

# Step 4: Verify installation
pacman -Q package
```

**Expected result:** Package installed without conflicts

### Installing AUR Package

**Problem:** Need software not in official repositories

**Solution:**
```bash
# Step 1: Ensure you have build tools
pacman -S --needed base-devel git

# Step 2: Clone AUR package (example: yay)
cd /tmp
git clone https://aur.archlinux.org/yay.git

# Step 3: Review PKGBUILD for security
cd yay
cat PKGBUILD
# READ THE PKGBUILD! Look for suspicious commands

# Step 4: Build and install
makepkg -si
# -s: Install dependencies
# -i: Install after building

# Expected output:
# ==> Making package: yay 12.1.2-1 (timestamp)
# ==> Checking runtime dependencies...
# ==> Installing package with pacman

# Step 5: Verify installation
which yay
yay --version
```

**Expected result:** AUR package safely built and installed

## Reference Files

**When to use reference files:** Quick Reference covers most tasks. Use reference files for:
- Complex configurations requiring multiple steps
- Uncommon hardware or software
- Deep troubleshooting requiring system internals
- Building custom packages or modules

**Available references in `references/` directory:**

- **package_management.md** - Deep dive into pacman, AUR helpers, repository management, package troubleshooting, mirrorlist configuration
- **system_administration.md** - System services, user management, monitoring, administrative tasks
- **troubleshooting.md** - Diagnostic tools, log analysis, common problems and solutions
- **development.md** - Jenkins setup, kernel module compilation, debugging with gdb, obtaining traces, debug symbols
- **desktop_environments.md** (71 pages) - Window managers (stacking, tiling, dynamic), DEs (MATE, GNOME, KDE), configuration
- **hardware.md** - GPU configuration, audio (PipeWire), printers, peripherals, kernel modules
- **networking.md** - Network configuration, SSH, VPN, firewalls, troubleshooting
- **applications.md** (29 pages) - Browsers, editors, office suites, media players (organized by category)
- **getting_started.md** - Installation guides, basic configuration, first-time setup
- **filesystem.md** - ext4, btrfs, xfs, partitioning, mounting, storage management
- **security.md** - Hardening, user permissions, encryption, security best practices
- **virtualization.md** - VirtualBox, QEMU/KVM, containers, VM management

**Navigation tip:** Each reference file includes table of contents, code examples with syntax highlighting, and original Wiki URLs.

## Troubleshooting Quick Index

**Package issues:**
- Conflicting files → See "Resolve common errors" in Quick Reference
- Failed to commit → Clear cache: `pacman -Scc`, update mirrors
- Locked database → Check for running pacman or remove `/var/lib/pacman/db.lck`
- Deep dive → **package_management.md**

**Service won't start:**
- Check status: `systemctl status service_name`
- View logs: `journalctl -u service_name -n 50`
- Deep dive → **system_administration.md**

**Boot failures:**
- Black screen → Check **troubleshooting.md** → Boot problems
- Use Arch install media for recovery
- Check bootloader configuration
- View boot logs: `journalctl -b -1` (previous boot)

**Hardware not working:**
- Check kernel modules: `lsmod | grep module_name`
- View hardware detection: `dmesg | grep -i device_name`
- Deep dive → **hardware.md** → Specific device type

**Application crashes:**
- Get backtrace → See "Debugging Crashed Applications" in Quick Reference
- Deep dive → **development.md** → Debugging section

## Related Skills

When working with Arch Linux, you may also need:
- **systematic-debugging** - For complex application debugging
- **Shell scripting** - Bash/Zsh automation
- **using-git-worktrees** - For kernel module development
- **test-driven-development** - When developing software on Arch

## Notes

- Content extracted from official Arch Wiki (https://wiki.archlinux.org/)
- Arch Wiki continuously updated by community - consider re-scraping periodically
- Quick Reference covers ~80% of common tasks
- Reference files available for deep dives into complex topics
- Code examples tested on Arch Linux (subject to upstream changes)
