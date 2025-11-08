# Arch-Wiki - Development

**Pages:** 6

---

## Jenkins

**URL:** https://wiki.archlinux.org/title/Jenkins

**Contents:**
- Installation
- Configuration
  - Log in as the Jenkins user
  - Running Jenkins with access to the display
- See also

Jenkins is an open source continuous integration server written in Java. It is capable of running scheduled automated builds and test suites of managed software projects. The build or tests for example may be triggered on a per commit basis or in a calendar driven manner. Jenkins thereby relies on the code being managed via a version control system (see git) and an automated build process. Note that Jenkins is not limited to Java applications and is suitable to manage projects in all common languages. Its capabilities can be further expanded by plugins.

Install jenkins for the latest stable release or jenkins-ltsAUR for the long-term-support version. The package will create a Jenkins user for the daemon using systemd-sysusers. If running on a server with only console access, also install packages fontconfig and freetype2.

In order to enable jenkins, you need to have jre21-openjdk installed and the path to your version of the Java Runtime Environment must be in the first line of the jenkins config file at /etc/conf.d/jenkins, if this is not the case, the jenkins.service will fail to start.

Project configuration can be done using the built-in web interface. To access it start/enable jenkins.service.

You can now open http://localhost:8090 with your browser and start setting up Jenkins.

The configuration file of the daemon running Jenkins is located at /etc/conf.d/jenkins. It is sourced by the according .service file and takes effect immediately after a restart.

jenkins listens on 0.0.0.0 and is immediately available remotely. If this is unwanted, for example on a test server, consider adding --httpListenAddress=127.0.0.1 to the configuration file (e.g. in JENKINS_OPTS).

The default Admin username is Admin. When you log into the Web interface at http://localhost:8090; you will need to view the file at /var/lib/jenkins/secrets/initialAdminPassword or run journalctl -u jenkins.service and search for the default password that was created upon installation.

The home folder of the jenkins user is located at /var/lib/jenkins. The Jenkins user does not have a default shell, so if you need to log in this user (for example to manage SSH keys) see su#Nologin users.

If Jenkins needs to run graphical applications that fail without a display (for example, the Unity Editor), you must run it from a desktop session. If you are running GNOME, you can do the following to automatically run Jenkins with access to the display:

After a reboot, GDM should automatically log into a gnome session. Then gnome should launch a terminal running a jenkins instance. This instance should be able to build Unity games without issue!

**Examples:**

Example 1 (unknown):
```unknown
/etc/conf.d/jenkins
```

Example 2 (unknown):
```unknown
jenkins.service
```

Example 3 (unknown):
```unknown
/etc/conf.d/jenkins
```

Example 4 (unknown):
```unknown
JAVA=/usr/lib/jvm/java-21-openjdk/bin/java
```

---

## Compile kernel module

**URL:** https://wiki.archlinux.org/title/Compile_kernel_module

**Contents:**
- Build environment
  - Traditional compilation
  - Arch Build System
- Source configuration
- Module compilation
- out-of-tree module compilation
- Module installation
- possible errors
- See also

Sometimes you may wish to compile Linux's Kernel module without recompiling the whole kernel.

Firstly you will need to install build dependencies such as a compiler (base-devel) and linux-headers.

Next you will need to get the source code for the kernel version the module is intended to run on. You may try using newer kernel sources but most likely the compiled module will not load.

In case the intended kernel version is the installed kernel, find its version with

There are two main options to acquire the required source. Each option has slightly different usage methods and directory structure.

See Kernel/Traditional compilation#Download the kernel source. If you fetch latest source using Git you will need to checkout needed version using tag (eg. v4.1).

For a general overview on Arch Build System read ABS. See Kernel/Arch build system for acquiring the kernel source, as well as the directory structure, and other details.

When you have the source code, enter its directory. For the #Arch Build System case, that directory would be src/archlinux-linux/ down from where the PKGBUILD is.

The output from make help is beneficial here. Start by cleaning with

An appropriate .config file is now required. If none is nearby, perhaps from a saved .config, and the intended kernel version is the running kernel, you can use its configuration file:

Next ensure the .config file is adjusted for the kernel version. If you are using kernel sources for the exact current version then it should not ask anything. But for another version than the current kernel you might be asked about some options. In any case, for the #Arch Build System option, you might want to examine the PKGBUILD::prepare() function.

If the module you want to compile have some compilation options such as debug build, or it was not compiled before, you can also, possibly must, adjust the kernel configuration. You can do this with one of the many configuration targets mentioned by make help.

In order to compile and load our module cleanly, we must find the value of the EXTRAVERSION component of the current kernel version number so we can match the version number exactly in our kernel source. EXTRAVERSION is a variable set in the kernel top-level Makefile, but the Makefile in a vanilla kernel source will have EXTRAVERSION empty; it is set only as part of the Arch kernel build process. If relevant, the value of the current kernel's EXTRAVERSION can be found by looking at the output of the uname -r command. In general, the kernel version is the concatenation of three components. Namely, the numeric version, the EXTRAVERSION, and the LOCALVERSION. The numeric version itself is a concatenation of three numbers. If built by a PKGBUILD file, the LOCALVERSION will be taken from the pkgrel variable, prefixed by a hyphen. And the EXTRAVERSION will be the suffix of the pkgver variable, where the period character to the right of the third numeric number of the numeric version is replaced by a hyphen. For example, with the linux package linux 5.5.8.arch1-1, the LOCALVERSION is -1. The EXTRAVERSION is -arch1. The output of uname -r will be 5.5.8-arch1-1 in that example.

Once the EXTRAVERSION value is known, we prepare the source for module compilation:

Alternatively, if you are happy to load modules with modprobe using the --force-vermagic option to ignore mismatches in the kernel version number, you can simply run:

Finally, compile wanted module by specifying its directory name. You can find the module location, thus also its directory name, with modinfo or find.

As a last resort, if nothing else has worked, you can

Which will build all the modules from the kernel configuration.

get the official source code of the current running linux kernel as described in Kernel/Arch build system:

then point to the checked out source when compiling the module:

Now after successful compilation you just need to gzip and copy it over for your current kernel.

If you are replacing some existing module you will need to overwrite it (and remember that reinstalling linux will replace it with default module)

Or alternatively, you can place the updated module in the updates folder (create it if it does not already exist).

However if you are adding a new module you can just copy it to extramodules (note, this is just example as btrfs will not get loaded from here)

You need to rebuild the module dependency tree with "depmod" to use installed modules.

If you are compiling a module for early boot (e.g. updated module) which is copied to Initramfs then you must remember to regenerate it with (otherwise your compiled module will not be loaded).

If EXTRAVERSION is not set correctly the following errors may occur

adding force-vermagic makes it ignore the version mismatch

**Examples:**

Example 1 (unknown):
```unknown
src/archlinux-linux/
```

Example 2 (unknown):
```unknown
$ make mrproper
```

Example 3 (unknown):
```unknown
.config.old
```

Example 4 (unknown):
```unknown
$ zcat /proc/config.gz > .config
```

---

## Debugging/Getting traces

**URL:** https://wiki.archlinux.org/title/Debugging/Getting_traces

**Contents:**
- Introduction
- Getting the trace
  - Starting a new instance of a program
  - Attaching to an existing process
  - Examining a previous crash
- Manually getting debug info
  - Installing debug packages
  - Rebuilding packages
    - Compilation options
      - glibc

This article aims to help debugging software by providing traces and debug information. This information can then be used for the bug report to the (upstream) software developers or package maintainers.

Usually, executable files are stripped of human readable context to make them smaller. Obtaining traces without debugging information available drastically reduces their usefulness. For example, a trace from a gdb session where debugging information is not available may look as follows:

?? shows where debugging info is missing, as well as the name of library or executable which called the function. Similarly, when (no debugging symbols found) appears, you should look for the stated file names.

To obtain a proper trace that is useful to the program developers, follow the next sections. Separate debug files are available for most official Arch packages and can be downloaded with Debuginfod (see #Getting the trace). When enhanced debugging information was not added to the executable in the first place, one has to rebuild the package with debugging symbols enabled.

Use the complete stack trace to inform developers of a bug you have discovered before. This will be highly appreciated by them and will help to improve your favorite program.

The actual backtrace (or stack trace) can be obtained via gdb, the GNU Debugger. It can be used in several ways, depending on whether it should start a new instance of a program, attach to an existing process, or examine a previous crash.

Start gdb with an executable program that can be found in $PATH (or a full path):

gdb automatically tries to download debug information and symbols for packages in the official repositories. When gdb asks whether Debuginfod should be enabled in the debugging session, answer y:

Then, within gdb, type run followed by any arguments you wish the program to start with:

Now do whatever is necessary to evoke the bug. gdb will automatically halt the application when it crashes and prompt for commands. In case of freezes or similar issues, press Ctrl+c and you will be returned to the command prompt, too.

Then enable logging to a file:

And finally have the backtrace written to the specified file in the current working directory:

If the program you want to debug is already running, you need to first find its process ID. Tools such as pidof(1) or pgrep(1) are available. For example:

When the output does not give a unique ID, you can try more filtering or look at the output of ps aux or pstree --show-pids.

Attaching as regular user does not work by default due to restricted ptrace scope. The restriction can be lowered temporarily with echo 0 > /proc/sys/kernel/yama/ptrace_scope or you can run gdb as a privileged user, e.g. using sudo.

Start gdb attaching it to the process:

gdb will ask if Debuginfod should be enabled in this debugging session, to which you should answer y.

Note that attaching to a process has stopped it and it needs to be explicitly continued. This replaces the run command from the workflow in the #Starting a new instance of a program section:

Now do whatever is necessary to evoke the bug in the attached process. Then proceed with enabling logging and obtaining the trace same as in #Starting a new instance of a program.

To debug an application that has already crashed, you will want to invoke gdb on its core dump. See Core dump#Analyzing a core dump for details.

If debugging information for the crashed program is not available and a proper backtrace was not obtained, you may need to rebuild the package and reproduce the crash again.

This article or section is out of date.

The first thing to do is to obtain the names of the packages which require rebuilding or the install of a debug package.

For example for the above extract from a trace, the package name for the associated package can be obtained with pacman:

The package is called glibc in version 2.5-8. Repeat this step for every package that needs debugging information.

This article or section needs expansion.

A few mirrors currently distribute debug packages in accessible repositories. These are sponsored mirrors controlled by Arch Linux and are given access to the debug repositories.

To install a package you can install it directly from the repository. For example:

This article or section is a candidate for merging with Official repositories.

Another option is to add the repositories to your pacman configuration.

Place a mirror with debug packages as the first one in the mirrorlist file:

If debug information is not exposed through debuginfod (for example, when the package originates from the AUR), then it can be rebuilt from source. See ABS for packages in the official repositories, or AUR#Acquire build files for packages in the AUR.

To set the required #Compilation options, you can modify the makepkg configuration if you will only use makepkg for debug purposes. In other cases, you should modify package's PKGBUILD file only for each package you would like to rebuild.

As of pacman 4.1, makepkg.conf(5) has debug compilation flags in DEBUG_CFLAGS and DEBUG_CXXFLAGS. To use them, enable the debug makepkg option, and disable strip.

These settings will force compilation with debug symbols and will disable their stripping from executables.

To apply this setting to a single package, modify the PKGBUILD:

Alternatively you can put the debug information in a separate package by enabling both debug and strip, debug symbols will then be stripped from the main package and placed, together with source files to aid in stepping through the debugger, in a separate pkgbase-debug package. This is advantageous if the package contains very large binaries (e.g. over a GB with debug symbols included) as it might cause freezing and other strange, unwanted behavior occurring.

Certain packages such as glibc are stripped regardless. Check the PKGBUILD for sections such as:

And remove them where appropriate.

This article or section is out of date.

Packages using Clang as the compiler will not build with the debug option due to the debug flag -fvar-tracking-assignments' not being handled (e.g. the previous js78 PKGBUILD).

Add the following at the top of the build() function to only remove the flag for the affected package:

Using Link-time optimization (LTO) will, both during compiling and in a debugger, use more memory[1][2]. Depending on the application, especially if it is a large one like Firefox or Qt, it might exceed the available memory. Build the application without LTO if this happens.

All packages in the official repositories are generally built with LTO.

Build the package from source using makepkg while in the PKGBUILD's directory. This could take some time:

Then install the built package:

**Examples:**

Example 1 (unknown):
```unknown
[...]
Backtrace was generated from '/usr/bin/epiphany'

(no debugging symbols found)
Using host libthread_db library "/lib/libthread_db.so.1".
(no debugging symbols found)
[Thread debugging using libthread_db enabled]
[New Thread -1241265952 (LWP 12630)]
(no debugging symbols found)
0xb7f25410 in __kernel_vsyscall ()
#0  0xb7f25410 in __kernel_vsyscall ()
#1  0xb741b45b in ?? () from /lib/libpthread.so.0
[...]
```

Example 2 (unknown):
```unknown
(no debugging symbols found)
```

Example 3 (unknown):
```unknown
$ gdb application
```

Example 4 (unknown):
```unknown
This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.archlinux.org>
Enable debuginfod for this session? (y or [n]) y
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Downloading separate debug info for /usr/bin/application
Reading symbols from /home/user/.cache/debuginfod_client/fbaee841e2ed2c11ecbbda26f39eeec1da23d6c3/debuginfo...
```

---

## .NET

**URL:** https://wiki.archlinux.org/title/.NET

**Contents:**
- Installation
  - Version differences
  - Install multiple versions manually
  - Uninstall manually installed version
  - Install multiple versions via AUR
  - Install PowerShell Core
- Telemetry
- Tab-completion
- Troubleshooting
  - It was not possible to find any compatible framework version

.NET (previously named .NET Core) is a FOSS software framework from Microsoft for C#, Visual Basic, and F#. It is designed to be cross-platform, modular and apt for modern applications, as opposed to its predecessor, the .NET Framework.

The .NET source is available at dotnet/dotnet on GitHub.

If you only want to run .NET managed applications, install the dotnet-runtime package.

To build apps with .NET, install dotnet-sdk as well.

Lastly, to build dynamic web sites, applications, and services using ASP.NET Core, install aspnet-runtime.

Microsoft recommends using Visual Studio Code , their Electron-based IDE, to build & debug .NET apps.

To use .NET 6.0, 7.0 or 8.0 instead suffix above package with "-6.0", "-7.0" or "-8.0" respectively, such as dotnet-runtime-8.0, dotnet-sdk-8.0 and aspnet-runtime-8.0

.NET SDKs are published under several version schemes. Only SDK versions 1xx can be built from source and will be available in the official repositories. Should you require any other version you will need one of the *-bin packages from AUR.

You can install multiple versions of the .NET SDK or runtime side by side by using the dotnet-install.sh script provided by the .NET Foundation. You can find the documentation of the script here.

For instance, this command would install the latest version found in the "STS"(Standard Term Support) channel in /usr/share/dotnet:

You may want to simulate the installation first by using the -Dryrun flag.

Once installed, you can verify the SDKs available:

You may want to remove outdated versions installed with dotnet-install.sh. The automated .NET Uninstall Tool does still not support Linux, so the deinstallation has to be done manually.

Deinstallation of the sdk:

Using dotnet-install.sh also dotnet host and shared packages are getting installed, which may have to get removed additionally depending on the release.

Complete deinstallation of the .NET Version (sdk, host, shared):

Some of the AUR dotnet packages are made to be installed alongside each other. Only one host package (dotnet-host-binAUR or dotnet-host) is needed containing the command-line tool and you can install any of the available SDKs and Runtimes (latest packages of all major versions) next to it. List of compatible packages:

You can install PowerShell Core as a "global" tool also [1] [2]

to update to the current version

The Microsoft build of the .NET SDK collects telemetry, by default. AUR .NET SDK packages (the *-bin variants) are based on Microsoft builds of .NET. .NET runtime components do not collect telemetry in any scenario.

Community builds (including those in Arch; starting with .NET 7) do not collect telemetry, per a change to the .NET SDK by Red Hat.

Telemetry can be disabled by setting environment variable DOTNET_CLI_TELEMETRY_OPTOUT=1.

All dotnet programs that use System.CommandLine.Parser to parse their arguments have auto-complete support. Enabling it just requires adding a few lines to your .bashrc / .zshrc file, as described in their documentation. Instructions for standalone binaries are here.

If you get the following error when you try to run a newly created project, you no longer need to set a DOTNET_ROOT variable as described in the solutions of various GitHub issues. Arch's dotnet package (as of 3.1) installs it to the Microsoft recommended location of /usr/share/dotnet.

This is caused because the runtime is shipped as a separate package in Arch. You just need to make sure you have the aspnet-runtime package installed as well.

Some of the dotnet SDK tools (for example libman, dotnet-watch etc.) may expect you to have the environment variable DOTNET_ROOT pre-configured. If it is not, an error like this one could be observed: [3]

The workaround is to manually export DOTNET_ROOT in your shell:

This happens after an update. The currently running shell / login session is storing environment variables for the dotnet SDK version different from one installed. Restarting the shell or logging in again should fix this.

This is believed to be caused by a conflict between the Mono and MSBuild SDK libs and the dotnet ones. To fix this export the path manually in your shell (replacing the version number as necessary) e.g:

Installed packages do not uninstall dotnet-host, so uninstall dotnet-host

**Examples:**

Example 1 (unknown):
```unknown
~/.dotnet/tools
```

Example 2 (unknown):
```unknown
/usr/share/dotnet
```

Example 3 (unknown):
```unknown
# ./dotnet-install.sh --install-dir /usr/share/dotnet -channel STS -version latest
```

Example 4 (unknown):
```unknown
$ dotnet --list-sdks
```

---

## Ada

**URL:** https://wiki.archlinux.org/title/Ada

**Contents:**
- Installation
  - Test your installation
- See also
  - Language
  - Tools
  - Library Docs

Ada is a general purpose, compiled programming language. It features strong static typing, packages, exceptions, generics, tasking, object-orientation and contracts.

Install the gcc-ada package. This will install the GNAT compiler, which is an Ada front-end for the GNU Compiler Collection (GCC).

Signed, pre-built packages are available from the unofficial Ada repository.

Check that GNAT is installed correctly by building a simple program, as follows:

You can compile it with gnatmake:

**Examples:**

Example 1 (unknown):
```unknown
with Ada.Text_IO;

procedure Hello is
begin
   Ada.Text_IO.Put_Line ("Hello, Arch!");
end Hello;
```

Example 2 (unknown):
```unknown
$ gnatmake hello
```

Example 3 (unknown):
```unknown
gcc -c hello.adb
gnatbind -x hello.ali
gnatlink hello.ali
```

Example 4 (unknown):
```unknown
Hello, Arch!
```

---

## Debugging

**URL:** https://wiki.archlinux.org/title/Step-by-step_debugging_guide

**Contents:**
- Check availability of a core dump
- Segmentation faults
  - Gdb
  - Valgrind
- Memory errors
  - AddressSanitizer
  - Valgrind
- Missing files or libraries
  - Strace
  - LD_DEBUG

This article or section needs expansion.

This page is mainly about how to gather more information in connection with bug reports. Even though the word "debug" is used, it is not intended as a guide for how to debug programs while developing.

A core dump is a file containing a process's address space (memory) when the process terminates unexpectedly. If the application is compiled in a debug-friendly way, the "core" file can be used to find out where things went wrong.

The location of core dumps may vary depending on the operating system configuration. See core dump to find whether generation of core dump files is enabled on your system and where do they go.

There are several techniques that can be used to figure out what went wrong. Put your detective hat on.

gdb is an ancient and well tested application for debugging applications. See Debugging/Getting traces#Getting the trace for more instructions how to use it to obtain a trace. While running from gdb, you might have to wait for the segfault. Afterwards, post the trace to a pastebin service and include the URL in your bug report.

If you have a "core" file, it can be used together with gdb to get a backtrace:

Assuming you have an unstripped binary without inlined functions, it is usually a good idea to also run that program through valgrind. valgrind is a tool that emulates a CPU and usually shows where things go wrong or provide info in addition to gdb.

it will provide a lot of helpful debug output if there is a crash. Consider -v and --leak-check=full to get even more info.

and run the output through kcachegrind to graphically explore the functions the program uses. If a program hangs, this makes it easier to pinpoint the location of the error.

In some cases, it may be necessary to find out if the application handles its memory correctly. This only affects applications written in memory-unsafe languages. For example, some crashes may be caused by memory errors such as a heap overflow.

Keep in mind that packages on Arch Linux are compiled with additional flags to harden the application, which may influence memory errors. See Arch package guidelines/Security.

In order for ASan to work, the application must be compiled with -f sanitize=address and debugging symbols.

The compiled application will be slower with ASan enabled, but it heavily depends on the software itself, the compiler used (including its version) and the used -O value, among other things. If the application is unbearably slow, it is worth trying out different combinations. An extreme example is that Cataclysm: Dark Days Ahead took 60 minutes to load a simple save with GCC 9 and ASan enabled. Without ASan, the save would take under a minute to load. GCC 14 cut the loading time in half with ASan, but it still remained at 30 minutes, which is unacceptably slow. Clang 18 with ASan did not have that issue and the slowdown was negligible. However, forcing GCC 14 to use -O3 with ASan massively sped up the loading, but it still took a minute to load and was not as fast as clang.

An additional complication was that only GCC 9 was able to trigger the specific bug, a heap overflow. A version compiled with GCC 14 was unable to reproduce the bug. As such, it is important to keep the compiler versions in mind, too.

To find memory errors, simply run the application as normal. ASan will automatically crash the application on things such as a heap overflow or even use-after-free. When this happens, a detailed and helpful trace can be found in the output. The behavior of ASan can be influenced at runtime via the ASAN_OPTIONS environment variable. Additionally, there are compilation flags to alter its behavior.

A common use for this environment variable is to tell ASan to not fatally crash the application when it finds something other than a memory leak:

Further information can be found at:

Valgrind can also be used to detect these behaviors and in contrast to ASan it does not need to be compiled in. Compared to ASan, it is massively slower and a bit more limited.

In order to find memory errors, invoke Valgrind with:

strace finds out in detail what an application is actually doing. If an application tries to open a file that is not there, it can be discovered by strace.

For finding which files a program named appname tries to open:

Setting LD_DEBUG=files gives another overview of what files an application is looking for. For an application named appname:

The output will end up in appname.log.

For more information, see ld-linux(8).

If you get no such file or directory when running an application, try the following command:

(replace /usr/bin/appname with the location of your executable)

Make sure the interpreter in question (like /lib/ld-linux-x86-64.so.2) actually exists. Install ld-lsb if need be.

Use file on the executable to get more information:

If it says ELF, it is a binary executable. If it says Python script, you know you are dealing with an application written in Python.

If it is a shell script, open up the shell script in a text editor and see (usually at the bottom of the file) if you can find the name of the real application (ELF file). You can then temporarily put "gdb" right in the shellscript, before the name of the executable, for debugging purposes. See the sections about gdb further up. Prefix the command with gdb --args if the executable in question needs arguments as well.

For pure shell scripts, you can also use bash -x script_name or bash -xv script_name.

For Python applications, the output will often say which file and line number the crash occurred at. If you are proficient with Python, you can try to fix this and include the fix in the bug report.

First check if the bug in question is a packaging bug. If the bug is introduced due to how Arch Linux packages this application, report it to https://gitlab.archlinux.org/groups/archlinux/packaging/-/issues. This also includes issues with libraries or dependencies (e.g if one of them is not built with a specific feature that is needed). Inspect the PKGBUILD of the package, which is possible with the Arch build system, to see how it gets packaged. See Bug reporting guidelines#Upstream or Arch? for more information.

If the bug is not related to Arch Linux and is reproducible anywhere else, only report it to upstream. Arch Linux can not magically fix upstream bugs. Reporting it to the Arch bugtracker would not help and might even be counterproductive because it tends to waste time of the bug wranglers.

**Examples:**

Example 1 (unknown):
```unknown
$ gdb appname core
bt full
```

Example 2 (unknown):
```unknown
$ valgrind appname
```

Example 3 (unknown):
```unknown
--leak-check=full
```

Example 4 (unknown):
```unknown
$ valgrind --tool=callgrind appname
```

---
