# Arch-Wiki - Troubleshooting

**Pages:** 3

---

## Ryzen

**URL:** https://wiki.archlinux.org/title/Ryzen

**Contents:**
- Enable microcode support
- Tweaking Ryzen
  - Voltage, power and temperature monitoring
  - Power management, undervolting and overclocking
- Compiling a kernel
- Troubleshooting
  - Random reboots
  - System halts
  - Screen-tearing (APU)
  - Soft lock freezing

Ryzen is a brand of microprocessors manufactured by Advanced Micro Devices (AMD). This article covers system configuration and troubleshooting information for different generations of the CPU.

This article or section needs expansion.

Install the amd-ucode package to enable microcode updates and enable it with the help of the Microcode page. These updates provide bug fixes that can be critical to the stability of your system. It is highly recommended to use it despite it being proprietary.

lm_sensors should be able to monitor temperatures out of the box. However, for more detailed information such as power consumption and voltage, zenpower3-dkmsAUR is needed. For GUI based monitoring tools, use zenmonitorAUR or zenmonitor3-gitAUR for Zen 3 CPUs.

See Gentoo:Ryzen#Kernel on enabling Ryzen support. The officially supported kernels have the required configuration by default.

See Gentoo:Ryzen#Random_reboots_with_mce_events if you are experiencing random reboots.

With Ryzen 5000 series, particularly the higher-end models of 5950X and 5900X there seem to be some slight instability issues under Linux, related possibly to the 5.11+ kernel, as shown by this kernel bug. After investigating and reading reports on the Internet, It seems that out of the box, Windows seems to run the CPUs at higher voltage and lower peak frequencies, compared to the stock linux kernel, which depending on your draw from the silicon lottery could cause a host of random application crashes or hardware errors that lead to reboots. You will recognise those by dmesg logs that look like:

The CPU ID and the Processor number may vary. To solve this problem you need to supply higher voltage to your CPU so that it is stable when running at peak frequencies. The easiest way to achieve this is to use the AMD curve optimiser which is accessible via your motherboard's UEFI. Access it and put a positive offset of 4 points, which will increase the voltage your CPU is getting at higher loads. It will limit overclocking potential due to higher heat dissipation requirements, but it will run stable. For more details check this forum post. When I did this for my 5950X, my processor stabilised and the frequency and voltage ranges were more similar to those observed under windows.

Within similar context of #Random reboots, systems might halt under heavy or specific low loads, even after applying the fixes. Reset button or forced shutdowns don't work, peripherals powers off, video output might stop, and unplugging is the only way out of this state.

Reducing frequencies to within non-overclocked standards and increasing voltages of CPU or RAM helps, but might not fix the issue. A potential fix is to update the UEFI (also misnamed "BIOS updates"), and then apply the PBO+4 curve for more stability on higher frequencies. Per silicon lottery, some CPUs might need +6 or higher offsets.

If you are using Xorg and are experiencing screen-tearing, see AMDGPU#Tear free rendering.

This bug is well known and is being discussed on bugzilla and launchpad. While the solution is not the same in all cases, this one helped some users. Add the output of this command echo rcu_nocbs=0-$(($(nproc)-1)) as a kernel parameter where the command nproc just prints your CPU's threads. For this option to be applied, you need a compiled kernel with option CONFIG_RCU_NOCB_CPU (like linux).

A different cause for the freezes is the power saving management indicated by c-states. The maximum power saving state c6 can cause problems. Adding the kernel parameter processor.max_cstate=5 helped in some cases but other users reported that the option is not applied and the c6 state is still entered. For them, disabling C6 states through a helper script relying on zenstates-gitAUR helped. Before using it, modprobe msr needs to be run in order to activate that kernel module.

Some laptops with Ryzen CPUs such as the HP Envy x360 15-bq100na may experience CPU soft locks which result in a frozen system. These can be avoided with the kernel parameter idle=nomwait added.

In some cases, kernel parameter pci=nomsi fixes the issue.

In some other cases, the issue is simply bad hardware, and warranty claiming the CPU for a new one may just solve your issues.

This issue is strongly linked to the C6 CPU idle state, which can cause instability on Linux, particularly when used with power supplies or motherboards that do not handle ultra-low current draw well.

To mitigate this, enter the UEFI setup:

If your motherboard does not offer this setting, or if issues persist, alternative workarounds include:

Disabling deep C-states may raise idle power consumption by approximately 5–10 W, but typically resolves issues with suspend, reboot, and shutdown on affected systems.

**Examples:**

Example 1 (unknown):
```unknown
kernel: mce: [Hardware Error]: Machine check events logged
kernel: mce: [Hardware Error]: CPU 22: Machine Check: 0 Bank 1: bc800800060c0859
kernel: mce: [Hardware Error]: TSC 0 ADDR 7ea8f5b00 MISC d012000000000000 IPID 100b000000000 
kernel: mce: [Hardware Error]: PROCESSOR 2:a20f10 TIME 1636645367 SOCKET 0 APIC d microcode a201016
```

Example 2 (unknown):
```unknown
echo rcu_nocbs=0-$(($(nproc)-1))
```

Example 3 (unknown):
```unknown
CONFIG_RCU_NOCB_CPU
```

Example 4 (unknown):
```unknown
processor.max_cstate=5
```

---

## General troubleshooting

**URL:** https://wiki.archlinux.org/title/General_troubleshooting

**Contents:**
- General procedures
  - Additional support
- Boot problems
  - Console messages
    - Flow control
    - Printing more kernel messages
    - Producing debug kernel messages
      - Dynamic debugging
      - Subsystem-specific debugging
    - netconsole

This article explains some methods for general troubleshooting. For application specific issues, please reference the particular wiki page for that program.

This article or section needs expansion.

It is crucial to always read any error messages that appear. Sometimes it may be hard, e.g. with graphical applications, to get a proper error message.

If you require any additional support, you may ask on the forums or on IRC.

When asking for support post the complete output/logs, not just what you think are the significant sections. Sources of information include:

One of the better ways to post this information is to use a pastebin.

A link will then be output that you can paste to the forum or IRC.

Additionally, you may wish to review how to properly report issues before asking.

This article or section needs expansion.

When diagnosing boot problems, it is very important to know in which stage the boot fails.

If the debugging tools provided by any stage are not enough to fix the broken component, try using a e.g. USB stick with the latest Arch Linux ISO on it.

After the boot process, the screen is cleared and the login prompt appears, leaving users unable to read init output and error messages. This default behavior may be modified using methods outlined in the sections below.

Note that regardless of the chosen option, kernel messages can be displayed for inspection after booting by using journalctl -k or dmesg. To display all logs from the current boot use journalctl -b.

This is basic management that applies to most terminal emulators, including virtual consoles (VC):

This pauses not only the output, but also programs which try to print to the terminal, as they will block on the write() calls for as long as the output is paused. If your init appears frozen, make sure the system console is not paused.

To see error messages which are already displayed, see Getty#Have boot messages stay on tty1.

Most kernel messages are hidden during boot. You can see more of these messages by adding different kernel parameters. The simplest ones are:

Other parameters you can add that might be useful in certain situations are:

#Printing more kernel messages indicates how to print of the kernel log buffer to the console, but that buffer itself won't contain any messages it didn't already (aside from the debug systemd output). This heading discusses methods for getting more detailed information out of the kernel log.

Messages printed with pr_debug or related functions such as dev_dbg(), drm_dbg(), and bt_dev_dbg() will not be produced unless you either:

This section will discuss how to use dynamic debug, which is useful if you have already looked at your kernel log with everything up to informational logs, and would like even more debugging information from a particular location.

Firstly, you must be running a kernel that was compiled with the CONFIG_DYNAMIC_DEBUG kernel configuration option set. This is already the case for linux, so no action is required if you are using that kernel.

Then, you need to know where you want to see debug messages from. A couple of options are:

Using that "source" of messages, you have to come up with a dynamic debug query that indicates which debug messages to enable, of the format:

Some examples of queries are:

Finally, to actually enact the query, you can either:

This is a greatly simplified overview of dynamic debug's capabilities; see the documentation for further details.

There are also a number of separate debug parameters for enabling debugging in specific subsystems e.g. bootmem_debug, sched_debug. Also, initcall_debug can be useful to investigate boot freezes. (Look for calls that did not return.) Check the kernel parameter documentation for specific information.

netconsole is a kernel module that sends all kernel log messages (i.e. dmesg) over the network to another computer, without involving user space (e.g. syslogd). Name "netconsole" is a misnomer because it is not really a "console", more like a remote logging service.

It can be used either built-in or as a module. Built-in netconsole initializes immediately after NIC cards and will bring up the specified interface as soon as possible. The module is mainly used for capturing kernel panic output from a headless machine, or in other situations where the user space is no more functional.

Getting an interactive shell at some stage in the boot process can help you pinpoint exactly where and why something is failing. There are several kernel parameters for doing so, but they all launch a normal shell which you can exit to let the kernel resume what it was doing:

Another option is systemd's debug-shell which adds a root shell on tty9 (accessible with Ctrl+Alt+F9). It can be enabled by either adding systemd.debug_shell to the kernel parameters, or by enabling debug-shell.service.

See Kernel modules#Obtaining information.

Unfortunately, freezes are usually hard to debug and some of them take a lot of time to reproduce. There are some types of freezes which are easier to debug than others:

If nothing else helps, try a clean shutdown. Pressing the power button once may unfreeze the system and show the classic "shutdown screen" which displays all the units that are getting stopped. Alternatively, using the magic SysRq keys may also help to achieve a clean shutdown. This is very important because the journal may contain hints why the machine froze. The journal may not be written to disk on an unclean shutdown. Hard freezes in which the whole machine is unresponsible are harder to debug since logs can not be written to disk in time.

Remote logging may help if the freeze does not permit writing anything to disk. A crude remote logging solution, which needs to be invoked from another device, can be used for basic debugging:

Many fatal freezes in which the whole system does not respond anymore and require a forced shutdown may be related to buggy firmware, drivers or hardware. Trying a different kernel (see Kernel#Debugging regressions) or even a different Linux distribution or operating system, updating the firmware and running hardware diagnostics may help finding the problem.

If a freeze does not permit gathering any kind of logs or other information required for debugging, try reproducing the freeze in a live environment. If a graphical environment is required to reproduce the freeze or if the freeze can be reproduced on the archiso, use the live environment of a different distribution, which is preferably not based on Arch Linux to eliminate the possibility that the freeze is related to the version or patches of the kernel. Should the freeze still happen in a live environment, chances are that it may be hardware-related. If it does not happen anymore, it is necessary to be aware of the differences of both systems. Different configurations, differences in versions and kernel parameters and other, similar changes may have fixed the freeze.

However, a blinking caps lock LED may indicate a kernel panic. Some setups may not show the TTY when a kernel panic occurred, which may be confusing and can be interpreted as another kind of freeze.

If an update causes an issue but downgrading the specific package fixes it, it is likely a regression. If this happened after a normal full system upgrade, check your pacman.log to determine which package(s) may have caused the issue. The most important part of debugging regressions is checking if the issue was already fixed, as this can save much time. To do so, first ensure the application is fully updated (e.g. ensure the application is the same version as in the official repositories). If it already is or if updating it does not fix the issue, try using the development version, usually a VCS version, which may already be packaged in the AUR. If this fixes the issue and the version with the fixes is not yet in the official repositories, wait until the new version arrives in them and then switch back to it.

If the issue still persists, debug the issue and/or bisect the application and report the bug on the upstream bug tracker so it can be fixed.

This will manifest commonly (but probably not only) as:

As partially covered in System maintenance#Restart or reboot after upgrades, the kernel is not updated when you update the package but only once you reboot afterwards. Meanwhile, the kernel modules, located in /usr/lib/modules/kernelversion/ are removed by pacman when installing the new kernel. As explained in FS#16702, this approach avoids leaving files on the system not handled by the package manager but leads to the aforementioned symptoms. To fix them, reboot systematically after updating the kernel. The long-term evolution, yet to be implemented, will be to use versioned kernel packages : the main blocker being how to handle the removal of the previous kernel versions once they are not needed anymore.

Another solution is available as kernel-modules-hook, where two pacman hooks use rsync to keep the kernel modules on the file system after the kernel update and linux-modules-cleanup.service that marks the old modules for removal four weeks after once enabled.

See Pacman#Troubleshooting for general topics, and pacman/Package signing#Troubleshooting for issues with PGP keys.

If a partial upgrade was performed, try updating your whole system. A reboot may be required.

If you usually boot into a GUI and that is failing, perhaps you can press Ctrl+Alt+F1 through Ctrl+Alt+F6 and get to a working tty to run pacman through.

If the system is broken enough that you are unable to run pacman, boot using a monthly Arch ISO from a USB flash drive, an optical disc or a network with PXE. (Do not follow any of the rest of the installation guide.)

Mount your root file system:

Mount any other partitions that you created separately, adding the prefix /mnt to all of them, i.e.:

Try using your system's pacman while chrooted:

If that fails, exit the chroot, and try:

This article or section needs expansion.

fuser is a command-line utility for identifying processes using resources such as files, file systems and TCP/UDP ports.

fuser is provided by the psmisc package, which should be already installed as a dependency of the base meta package. See fuser(1) for details.

First, make sure you have a valid local session within X:

This should contain Remote=no and Active=yes in the output. If it does not, make sure that X runs on the same tty where the login occurred. This is required in order to preserve the logind session.

Basic polkit actions do not require further set-up. Some polkit actions require further authentication, even with a local session. A polkit authentication agent needs to be running for this to work. See polkit#Authentication agents for more information on this.

If, while using a program, you get an error similar to:

Use pacman or pkgfile to search for the package that owns the missing library:

In this case, the libusb-compat package needs to be installed. Alternatively, the program requesting the library may need to be rebuilt following a soname bump.

The error could also mean that the package that you used to install your program does not list the library as a dependency in its PKGBUILD: if it is an official package, report a bug; if it is an AUR package, report it to the maintainer using its page in the AUR website.

**Examples:**

Example 1 (unknown):
```unknown
$HOME/.cache
```

Example 2 (unknown):
```unknown
$HOME/.local
```

Example 3 (unknown):
```unknown
systemd.log_level=debug
```

Example 4 (unknown):
```unknown
journalctl -k
```

---

## Frequently asked questions

**URL:** https://wiki.archlinux.org/title/FAQ

**Contents:**
- General
  - What is Arch Linux?
  - Why would I not want to use Arch?
  - Why would I want to use Arch?
  - What architectures does Arch support?
  - Does Arch follow the Linux Foundation's Filesystem Hierarchy Standard (FHS)?
  - I am a complete GNU/Linux beginner. Should I use Arch?
  - Is Arch designed to be used as a server? A desktop? A workstation?
  - I really like Arch, except the development team needs to implement feature X
  - When will the new release be made available?

See the Arch Linux article.

You may not want to use Arch, if:

Because Arch is the best.

Arch only supports the x86_64 (sometimes called amd64) architecture. Support for i686 was dropped in November 2017 [1].

There are derivative distributions for the i686 architecture [2] and ARM CPUs [3], each with their own community channels. They are not supported by Arch Linux.

If you wish for Arch to support other architectures, you can help out with existing porting efforts or start your own. See Getting involved#Help porting Arch Linux to other architectures.

Arch Linux follows the file system hierarchy for operating systems using the systemd service manager. See file-hierarchy(7) for an explanation of each directory along with their designations. In particular, /bin, /sbin, and /usr/sbin are symbolic links to /usr/bin, and /lib and /lib64 are symbolic links to /usr/lib.

If you are a beginner and want to use Arch, you must be willing to invest time into learning a new system, and accept that Arch is designed as a 'do-it-yourself' distribution; it is the user who assembles the system.

Before asking for help, do your own independent research by searching the Web, the forum and the superb documentation provided by the Arch Wiki. There is a reason these resources were made available to you in the first place. Many thousands of volunteered hours have been spent compiling this excellent information.

See also Arch terminology#RTFM and the Installation guide.

Arch is not designed for any particular type of use. Rather, it is designed for a particular type of user. Arch targets competent users who enjoy its 'do-it-yourself' nature, and who further exploit it to shape the system to fit their unique needs. Therefore, in the hands of its target user base, Arch can be used for virtually any purpose. Many use Arch on both their desktops and workstations. And of course, archlinux.org, aur.archlinux.org and almost all of Arch's infrastructure runs on Arch.

Get involved, contribute your code/solution to the community. If it is well-regarded by the community and development team, perhaps it will be merged. The Arch community thrives on contribution and sharing of code and tools.

Arch Linux releases are simply a live environment for installation or rescue, which include the base meta package and a few other packages. The releases are issued usually in the first half of every month.

It is the user who is ultimately responsible for the stability of their own rolling release system. The user decides when to upgrade, and merges necessary changes when required. If the user reaches out to the community, help is often provided in a timely manner. The difference between Arch and other distributions in this regard is that Arch is truly a 'do-it-yourself' distribution; complaints of breakage are misguided and unproductive, since upstream changes are not the responsibility of Arch devs.

See the System maintenance article for tips on how to make an Arch Linux system as stable as possible.

Arch gets plenty of press as it is. The goal of Arch Linux is not to be large; rather, organic, sustainable growth occurs naturally amongst the target user base.

Possibly so. Feel free to volunteer your time! Visit the forums, IRC channels, and mailing lists, and see what needs to be done. See also Getting involved for details.

A guided installer with a text-based user interface is available. See archinstall for details.

See General recommendations.

Since many are available to you, use the one that best fits your needs. Have a look at the Desktop environment and Window manager articles.

See Arch compared to other distributions.

See also System maintenance.

Is your network configured correctly? Have a look at the Network configuration article. For advanced setups, you may also want to look at traffic shaping.

One of the most commonly used kernels, linux, tends to be newer than the kernel of other, more stable, Linux distributions. Because of that, you may rarely experience a kernel regression or driver bug, especially if using Wi-Fi. Do note that the vast majority of those bugs are not Arch Linux-specific as Arch Linux only applies the most basic of patches. This needs to be taken upstream. See #I have found an error with package X. What should I do?.

Essentially, unused RAM is wasted RAM.

Many new users notice how the Linux kernel handles memory differently than they are used to. Since accessing data from RAM is much faster than from a storage drive, the kernel caches recently accessed data in memory. The cached data is only cleared when the system begins to run out of available memory and new data needs to be loaded.

We could distinguish the difference from free command:

It is important to note the difference between "free" and "available" memory. In the above example, a system with 377 GiB of total RAM appears to be using more than half of it, with only 146 GiB as free memory. However, 196 GiB of it is "buff/cache". There is still 337 GiB available for starting new applications, without swapping. See free(1) for details. The result of all this? Performance!

See this wonderful article if your curiosity has been piqued. There is also a website dedicated to clearing this confusion: https://www.linuxatemyram.com/.

The answer to this question depends on your system. There are some fine utilities that may help you find the answer.

Have you mistyped your password or cancelled a sudo command three times in fifteen minutes? If so, you have triggered a prevention mechanism against brute-force attacks: see Security#Lock out user after three failed login attempts for more details.

You may want to voluntarily "phone home" by contributing to the pkgstats project that collects anonymous data of package popularity to help Arch developers prioritize their efforts.

See the pacman, pacman/Tips and tricks and Official repositories pages for more answers.

First, you need to figure out if this error is something the Arch team can fix. Often it is not (e.g. Firefox crashes may be the fault of the Mozilla team); this is called an upstream error, see Bug reporting guidelines#Upstream or Arch?. If it is an Arch problem, there is a series of steps you can take:

This has been discussed on the Arch mailing list. Some proposed a .pac file extension, but there is no plan to change the package extension. As Tobias Kieslich, one of the Arch developers, put it, "A package is a [compressed] tarball! And it can be opened, investigated and manipulated by any tar-capable application. Moreover, the mime-type is automatically detected correctly by most applications."

Pacman is a front-end to libalpm(3)—the "Arch Linux Package Management" library—which allows alternative front-ends, like a GUI front-end, to be written.

If you think an idea has merit, you may choose to discuss it on pacman-dev. Also check https://gitlab.archlinux.org/pacman/pacman/-/issues for existing feature requests.

However, the best way to get a feature added to pacman or Arch Linux is to implement it yourself. The patch or code may or may not be officially accepted, but perhaps others will appreciate, test and contribute to your effort.

If you are using a desktop environment like KDE or GNOME, the program should automatically show up in your menu if it comes with a desktop entry. If you are trying to run the program from a terminal and do not know the binary name, use:

Several distributions, such as Debian, have different versions of shared libraries packaged as different packages: libfoo1, libfoo2, libfoo3 and so on. In this way it is possible to have applications compiled against different versions of libfoo installed on the same system.

In case of a distribution like Arch, only the latest packaged versions are officially supported. By dropping support for outdated software, package maintainers are able to spend more time ensuring that the newest versions work as expected. As soon as a new version of a shared library becomes available from upstream, it is added to the repositories and affected packages are rebuilt to use the new version.

This scenario should not happen at all. Assuming an application called foobaz is in one of the official repositories and builds successfully against a new version of a shared library called libbaz, it will be updated along with libbaz. If, however, it does not build successfully, foobaz package will have a versioned dependency (e.g. libbaz 1.5), and will be removed by pacman during libbaz upgrade, due to a conflict.

If foobaz is a package that you built yourself and installed from AUR, you should rebuild foobaz against the new version of libbaz. If the build fails, report the bug to the foobaz developers.

No, it is not possible. Major kernel updates (e.g. linux 3.5.0-1 to linux 3.6.0-1) are always accompanied by rebuilds of all supported kernel driver packages. On the other hand, if you have an unsupported driver package (e.g. from the AUR) installed on your system, then a kernel update might break things for you if you do not rebuild it for the new kernel. Users are responsible for updating any unsupported driver packages that they have installed.

Follow the System maintenance#Upgrading the system section.

pacman mirrors are not synced immediately. It may take over 24 hours before an update is available to you. The only options are be patient or use another mirror. MirrorStatus can help you identify an up-to-date mirror.

Package updates will be released when they are ready. The specific amount of time can be as short as a few hours after upstream releases a minor bugfix update to as long as several weeks after a large package group's major update. The amount of time from an upstream's new version to Arch releasing a new package depends on the specific packages and the availability of the package maintainers. Additionally, some packages spend some time in the testing repository, so this can prolong the time before a package is updated. Package maintainers attempt to work quickly to bring stable updates to the repositories. If you find a package in the official repositories that is out of date, go to that package's page at the package website and flag it.

If you are lucky, it might work, for a time. Regardless, it is not a proper solution, because:

Instead, e.g. use/write a compat (compatibility) package, which provides the required library version.

If your processor is x86_64 compatible, you will have the lm (long mode) flag in /proc/cpuinfo. For example,

Under Windows, using the freeware CPU-Z helps determine whether your CPU is 64-bit compatible. CPUs with AMD's instruction set "AMD64" or Intel's solution "EM64T" should be compatible with the x86_64 releases and binary packages.

It is faster under most circumstances and as an added bonus also inherently more secure due to the nature of Address space layout randomization (ASLR) in combination with Position-independent code (PIC) and the NX Bit which is not available in the stock i686 kernel due to disabled Physical Address Extension (PAE). If your computer has more than 4 GiB of RAM, only a 64-bit OS will be able to fully utilize it.

Programmers also increasingly tend to care less about 32-bit ("legacy") as "new" x86 CPUs typically support the 64-bit extensions.

There are many more reasons we could list here to tell you to avoid 32-bit, but between the kernel, userspace and individual programs it is simply not viable to list every last thing that 64-bit does much better these days.

**Examples:**

Example 1 (unknown):
```unknown
total        used        free      shared  buff/cache   available
Mem:           377Gi        40Gi       146Gi       1.1Gi       196Gi       337Gi
Swap:          377Gi       1.1Gi       376Gi
```

Example 2 (unknown):
```unknown
$ pacman -Qlq package_name | grep /usr/bin/
```

Example 3 (unknown):
```unknown
/proc/cpuinfo
```

Example 4 (unknown):
```unknown
$ grep -w lm /proc/cpuinfo
```

---
