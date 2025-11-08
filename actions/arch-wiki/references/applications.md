# Arch-Wiki - Applications

**Pages:** 29

---

## List of applications/Internet

**URL:** https://wiki.archlinux.org/title/List_of_applications/Internet

**Contents:**
- Network connection
  - Network managers
  - VPN clients
  - Proxy servers
  - Anonymizing networks
  - Network tunnels
  - Deep packet inspection circumvention
  - Speedtest tools
- Web browsers
  - Console

See Network configuration#Network managers.

Tools to avoid censorship, bandwidth throttle without anonymization. See Wikipedia:Deep packet inspection, Wikipedia:Internet censorship circumvention for an introduction to the topic.

See also Wikipedia:Comparison of web browsers.

See also Wikipedia:Gecko (software).

See also Wikipedia:Blink (web engine).

See also Wikipedia:WebKit.

Most of these support ad-blocking via wyebadblock.

See also Wikipedia:Goanna (software).

See also Wikipedia:Gemini (protocol)#Software.

A web server serves HTML web pages and other files via HTTP to clients like web browsers. The major web servers can be interfaced with programs to serve dynamic content (web applications).

See also Category:Web server and Wikipedia:Comparison of web server software.

The Python standard library module http.server can also be used from the command-line.

Apache also supports WSGI with mod_wsgi.

See also Wikipedia:Comparison of download managers.

See also #LAN messengers.

See also Wikipedia:Comparison of FTP client software.

Some file managers like Dolphin, GNOME Files and Thunar also provide FTP functionality.

See also Wikipedia:List of FTP server software.

Some download managers are also able to connect to the BitTorrent network: Aria2, LFTP, FatRat, KGet, MLDonkey, uGet.

See also Wikipedia:Comparison of BitTorrent clients.

See also Wikipedia:Comparison of file-sharing applications.

See also Wikipedia:Pastebin.

Pastebin services are often used to quote text or images while collaborating and troubleshooting. Pastebin clients provide a convenient way to post from the command line.

Some services can be used with more general command line tool, such as cURL. For extensions, such as line numbers, one can use more command line tools. Such as cat -n.

See also Wikipedia:Comparison of email clients

See also Wikipedia:Mail retrieval agent.

See also Wikipedia:Comparison of instant messaging clients and Wikipedia:Comparison of VoIP software.

This section lists all client software with instant messaging support.

The number of networks supported by these clients is very large but they (like any multi-protocol clients) usually have very limited or no support for network-specific features.

See also Wikipedia:Comparison of Internet Relay Chat clients.

See also Wikipedia:XMPP.

See also Wikipedia:List of SIP software#Clients.

See also Matrix and Matrix Clients.

See also Tox and comparison clients

See also Avahi#Link-Local (Bonjour/Zeroconf) chat and Wikipedia:Comparison of LAN messengers.

See also Ring and Tox.

See also Wikipedia:Comparison of instant messaging protocols.

See also Wikipedia:List of SIP software#Servers.

See also Wikipedia:Collaborative software.

Web feeds aggregators. Some email clients are also able to act as news aggregator: Claws Mail RSSyl plugin, Evolution, SeaMonkey Mail & Newsgroups, Thunderbird.

See also Wikipedia:Comparison of feed aggregators.

Some media players are also able to act as podcast client: Amarok, Cantata, Clementine, Goggles Music Manager, Rhythmbox, VLC media player. git-annex can also function as podcatcher.

See also Wikipedia:List of podcatchers.

Some email clients are also able to act as Usenet newsreader: Claws Mail, Evolution, NeoMutt, SeaMonkey Mail & Newsgroups, Sylpheed, Thunderbird.

See also: Wikipedia:List of Usenet newsreaders, Wikipedia:Comparison of Usenet newsreaders.

See also Wikipedia:Blog software and Wikipedia:List of content management systems.

See also Wikipedia:Remote desktop software and Wikipedia:Comparison of remote desktop software.

See also Chrome Remote Desktop for a web browser based solution.

**Examples:**

Example 1 (unknown):
```unknown
eric6_browser
```

Example 2 (unknown):
```unknown
$ command | curl -F 'file=@-' 0x0.st
```

Example 3 (unknown):
```unknown
$ curl -F 'file=@-' 0x0.st < file
```

Example 4 (unknown):
```unknown
pastebinit -l
```

---

## List of applications/Documents

**URL:** https://wiki.archlinux.org/title/List_of_applications/Documents

**Contents:**
- Text editors
  - Console
    - Emacs-style text editors
    - Vi-style text editors
  - Graphical
- Office
  - Office suites
  - Word processors
    - WYSIWYG HTML editors
    - Desktop publishing

See also Wikipedia:Comparison of text editors.

Some of the lighter-weight Integrated development environments can also serve as text editors.

See also Wikipedia:Comparison of office suites.

See also Wikipedia:Comparison of word processors.

See also Wikipedia:Comparison of spreadsheet software.

For DBMS-specific tools, see:

See also Wikipedia:Comparison of database tools.

These kinds of software are in a substance somewhat between text processing core utilities like awk, spreadsheets and production-level database system. And they usually come with a non-SQL command-line interface.

See also #TeX formula editors and Wikipedia:Formula editor.

See also Wikipedia:Comparison of document markup languages.

See also Wikipedia:AsciiDoc.

See also the official website and Wikipedia:Markdown.

See also reStructuredText.

With TeX, LaTeX and friends, creation of any scientific document, article, journal, etc. is made commonplace.

See also Wikipedia:Comparison of TeX editors and Wikibooks:LaTeX/Installation#Editors.

See also Wikipedia:Comparison of XML editors.

See also #Markup languages and PDF, PS and DjVu.

See also Wikipedia:Comparison of reference management software.

See PDF, PS and DjVu.

Some PDF viewers like apvlv, Atril, MuPDF, Okular, Xreader, and Zathura also support the EPUB format.

Some PDF and E-book viewers like Atril, Bookworm, Calibre, Foliate, GNOME Document Viewer, Lector, MuPDF, Okular, Papers, Xreader and Zathura also support the Comicbook format.

See also Wikipedia:Microsoft Compiled HTML Help.

Some PDF and E-book viewers like Cool Reader, FBReader and Okular also support the CHM format.

See also Wikipedia:Comparison of optical character recognition software.

See also Wikipedia:Comparison of notetaking software.

See also Wikipedia:List of concept- and mind-mapping software.

See also #Markdown editors and Wikipedia:Full-screen writing program.

See also Wikipedia:Category:Dictionary software and Wikipedia:DICT#DICT clients.

See Language checking.

See also Wikipedia:Comparison of computer-assisted translation tools.

---

## Command-line shell

**URL:** https://wiki.archlinux.org/title/Command_shell

**Contents:**
- List of shells
  - POSIX compliant
  - Alternative shells
- Changing your default shell
- Uninstalling shell
- Login shell
- Configuration files
  - /etc/profile
  - Standardisation
- Input and output

Shells that are more or less POSIX compliant are listed under #POSIX compliant, while shells that have a different syntax are under #Alternative shells.

These shells can all be linked from /usr/bin/sh. When Bash, mkshAUR and zsh are invoked with the sh name, they automatically become more POSIX compliant.

After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

And to set one as default for your user do:

If you are using systemd-homed, run:

where /full/path/to/shell is the full path as given by chsh -l.

If you now log out and log in again, you will be greeted by the other shell.

Change the default shell before removing the package of the shell.

Alternatively, modify the user database.

Use it for every user with a shell other than bash set as their login shell (including root if needed). When completed, the package can be removed.

A login shell is an invocation mode, in which the shell reads files intended for one-time initialization, such as system-wide /etc/profile or the user's ~/.profile or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via SSH, changes the user with sudo or su using the --login parameter, or when the user manually invokes a login shell (e.g. by bash --login).

See #Configuration files and the links therein for an overview of the various initialization files. For more information about login shell, see also Difference between Login Shell and Non-Login Shell? and Why a "login" shell over a "non-login" shell? on Stack Exchange.

To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g. Bash#Configuration files or Zsh#Startup/Shutdown files.

See also Wikipedia:Unix shell#Configuration files for a comparison of various configuration files of various shells.

Upon login, all Bourne-compatible shells source /etc/profile, which in turn sources any readable *.sh files in /etc/profile.d/: these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

It is possible to make (some) shells configuration files follow the same naming convention, as well as supporting some common configuration between the shells.

See the article about this and the related repository. See also xsh.

See also GregsWiki and I/O Redirection.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/sh
```

Example 2 (unknown):
```unknown
$ chsh -s /full/path/to/shell
```

Example 3 (unknown):
```unknown
$ homectl update --shell=/full/path/to/shell user
```

Example 4 (unknown):
```unknown
/full/path/to/shell
```

---

## Command-line shell

**URL:** https://wiki.archlinux.org/title/Login_shell

**Contents:**
- List of shells
  - POSIX compliant
  - Alternative shells
- Changing your default shell
- Uninstalling shell
- Login shell
- Configuration files
  - /etc/profile
  - Standardisation
- Input and output

Shells that are more or less POSIX compliant are listed under #POSIX compliant, while shells that have a different syntax are under #Alternative shells.

These shells can all be linked from /usr/bin/sh. When Bash, mkshAUR and zsh are invoked with the sh name, they automatically become more POSIX compliant.

After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

And to set one as default for your user do:

If you are using systemd-homed, run:

where /full/path/to/shell is the full path as given by chsh -l.

If you now log out and log in again, you will be greeted by the other shell.

Change the default shell before removing the package of the shell.

Alternatively, modify the user database.

Use it for every user with a shell other than bash set as their login shell (including root if needed). When completed, the package can be removed.

A login shell is an invocation mode, in which the shell reads files intended for one-time initialization, such as system-wide /etc/profile or the user's ~/.profile or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via SSH, changes the user with sudo or su using the --login parameter, or when the user manually invokes a login shell (e.g. by bash --login).

See #Configuration files and the links therein for an overview of the various initialization files. For more information about login shell, see also Difference between Login Shell and Non-Login Shell? and Why a "login" shell over a "non-login" shell? on Stack Exchange.

To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g. Bash#Configuration files or Zsh#Startup/Shutdown files.

See also Wikipedia:Unix shell#Configuration files for a comparison of various configuration files of various shells.

Upon login, all Bourne-compatible shells source /etc/profile, which in turn sources any readable *.sh files in /etc/profile.d/: these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

It is possible to make (some) shells configuration files follow the same naming convention, as well as supporting some common configuration between the shells.

See the article about this and the related repository. See also xsh.

See also GregsWiki and I/O Redirection.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/sh
```

Example 2 (unknown):
```unknown
$ chsh -s /full/path/to/shell
```

Example 3 (unknown):
```unknown
$ homectl update --shell=/full/path/to/shell user
```

Example 4 (unknown):
```unknown
/full/path/to/shell
```

---

## List of applications/Utilities

**URL:** https://wiki.archlinux.org/title/Terminal_pager

**Contents:**
- Terminal
  - Command shells
  - Terminal emulators
    - VTE-based
    - KMS-based
    - framebuffer-based
  - Terminal pagers
  - Terminal multiplexers
  - Serial terminals
- Files

See the main article: Command-line shell.

See also Wikipedia:Comparison of command shells.

Terminal emulator shows a graphical user interface (GUI) window that contains a terminal. Most emulate xterm, which in turn emulates VT102, which emulates teletypewriter (TTY).

For a comprehensive list, see the List of terminal emulators.

VTE (Virtual Terminal Emulator) is a widget developed during early GNOME days for use in the GNOME Terminal. It has since given birth to many terminals with similar capabilities.

The following terminal emulators are based on the kernel mode setting that could be invoked without X.

In the GNU/Linux world, the framebuffer can refer to a virtual device in the Linux kernel (fbdev) or the virtual framebuffer system for X (xvfb). This section mainly lists the terminal emulators based on the in-kernel virtual device, i.e. fbdev.

See also Wikipedia:Terminal pager.

See also Wikipedia:Terminal multiplexer.

See Working with the serial console#Graphical front-ends.

See also Wikipedia:Comparison of file managers.

Note that some of these twin-panel file managers can also be set to have only one pane.

See Trash management#Trash creation.

This article or section is a candidate for merging with Synchronization and backup programs#Data synchronization.

See also Synchronization and backup programs, Wikipedia:Comparison of file synchronization software, and Wikipedia:Comparison of backup software.

For archiving and compression command-line tools, see Archiving and compression.

See also Wikipedia:Comparison of file comparison tools.

For managing pacnew/pacsave files, specialised tools exist. See Pacnew and Pacsave files#Managing .pac* files.

See diff(1) from diffutils and its alternatives.

Vim and Emacs provide merge functionality with vimdiff and ediff.

See rename(1) from util-linux.

This section lists utilities for file searching based on filename, file path or metadata. For full-text searching, see the next section.

See also Wikipedia:List of search engines#Desktop search engines.

See find(1) from findutils and its alternatives.

These programs index your files to allow for quick searching.

See grep(1) from grep and its alternatives, which provide non-indexed full-text search.

See also Wikipedia:Comparison of revision control software.

See also Wikipedia:List of build automation software.

See also Wikipedia:Comparison of integrated development environments.

For PHP specific list, see PHP#Development tools.

See also D-Bus#Debugging.

Lex and Yacc are part of POSIX.

And then there are also:

These programs provide ready-made user interfaces for alerting the user or prompting for information. These are best suited for writing shell scripts; for more complex use-cases, see #GUI builders.

See also Wikipedia:Comparison of hex editors.

See also Wikipedia:Hex dump.

See also Wikipedia:Literate programming.

See also Wikipedia:List of Unified Modeling Language tools.

See also Git server#Advanced web applications.

See also Wikipedia:List of tools for code review.

See also Wikipedia:List of game engines.

This article or section is a candidate for moving to List of applications/Other#Desktop environments.

See Keyboard shortcuts#Xorg.

See the main article: Input method.

See Partitioning#Partitioning tools.

See File systems#Types of file systems.

See also udisks#Mount helpers.

See S.M.A.R.T.#GUI applications.

See File recovery#List of utilities.

See also Securely wipe disk.

See also Wikipedia:List of tools to create Live USB systems.

See also Category:Monitoring.

See lm_sensors#Graphical front-ends.

See also Wikipedia:Font management software.

See man page#Reading local man pages.

See Time synchronization.

See also Xrandr#Graphical front-ends.

See Backlight#Backlight utilities.

See ICC profiles#Utilities and Backlight#Color correction.

See CUPS#GUI applications.

See Bluetooth#Front-ends.

See Power management#Userspace tools.

See systemd#GUI configuration tools.

See GRUB/Tips and tricks#GUI configuration tools.

See pacman tips#Utilities.

See Libvirt#Client and VirtualBox.

See Wine (Windows) and Darling (MacOS).

**Examples:**

Example 1 (unknown):
```unknown
coredumpctl
```

Example 2 (unknown):
```unknown
drkonqi-coredump-gui
```

Example 3 (unknown):
```unknown
qtlogging.ini
```

Example 4 (unknown):
```unknown
ug --hexdump
```

---

## PC speaker

**URL:** https://wiki.archlinux.org/title/Disable_PC_speaker_beep

**Contents:**
- Mechanism
- Disabling the PC speaker
  - Physically
  - Globally
  - Console
    - Virtual console
    - Readline-aware shell
    - Less pager
    - Arch Linux ISO
  - ALSA

PC speaker—beeper—is a built-in loudspeaker in most personal computers since the first IBM PC. This speaker is not capable of high quality playback and merely serves as a simple means of auditory feedback in the form of beeps. Some software—e.g. web browsers, editors and terminals—may produce beeps which may or may not be desired by the user. This article serves as a guide for configuring and/or disabling the speaker entirely.

For situations where no sound card or speakers are available and a simple audio notification is desired, see #beep.

The PC speaker is typically a physical unit connected on the front connections header of the motherboard. Some motherboard manufacturers do not ship their motherboards with a PC speaker at all, whereas others may have the PC speaker soldered directly onto the surface. Laptops typically have no physical PC speaker but have the beeper routed to the laptop internal speakers. In some cases, the beeper is heard on the regular output—i.e. speakers or headphones—of the soundcard, which tends to be unexpectedly loud.

Upon boot the UEFI/BIOS will traditionally generate a beep during power-on self-test (POST). Recent motherboard models omit the POST beep in favor of rapidly booting into the operating system. The UEFI user interface typically allows for toggling the POST beeps but it cannot configure the PC speaker to be turned off completely.

Once the system has booted into Linux and the pcspkr kernel module is loaded, the PC speaker can be used by the environment, be invoked manually by the user, and be configured to some extent.

Because the PC speaker is controlled directly by the CPU, along with the fact that they are built for beeping only, PC speaker cannot be used for playing back audio files. If this is really desired, unloading the pcspkr module and installing the snd-pcsp-dkmsAUR package provides a rudimentary audio output.

By removing the PC speaker the system will not be able to produce beeps. This can be achieved by physically removing the unit from the motherboard (if possible). Some manufacturers may provide a jumper header to switch it off.

The PC speaker can be disabled by unloading the pcspkr and snd_pcsp kernel modules:

Blacklisting the pcspkr and snd_pcsp modules will prevent udev from loading them at boot. Create the file:

Blacklisting it on the kernel command line is yet another way. Simply add module_blacklist=pcspkr,snd_pcsp to your boot loader kernel line.

In virtual console (TTY) you can set the bell duration to zero milliseconds with setterm(1):

For a shell which utilizes the Readline library (e.g. Bash), uncomment this line in /etc/inputrc (or add it to ~/.inputrc):

To disable PC speaker in less(1) pager, you can launch it with less --quiet to mute PC speaker for end of file events, or less --QUIET to mute it altogether. For man pages, launch man --pager="less --QUIET" or set the $MANPAGER or $PAGER environment variables.

Alternatively, you can add these lines to your shell configuration file:

If you want to disable the init tune on the Arch Linux ISO, you will need to repack the ISO. To do so, first install the libisoburn and mtools packages.

Extract the El Torito boot images and systemd-boot configuration (loader.conf) from the ISO:

Make loader.conf writable and remove the beep option from it:

Add the modified loader.conf to the El Torito UEFI boot image:

Finally, repack the ISO using the modified boot image and loader.conf:

For most sound cards the PC speaker is listed as an ALSA channel, named either PC Speaker, PC Beep, or Beep. To mute the speaker, either use alsamixer(1) or amixer(1), for example:

To unmute the channel, see Advanced Linux Sound Architecture#Unmuting the channels.

Cinnamon seems to play a "water drop" sound. To disable it, set in gsettings(1):

Append this line to ~/.gtkrc-2.0:

Add the same line to the [Settings] section of $XDG_CONFIG_HOME/gtk-3.0/settings.ini:

This is documented in the Gnome Developer Handbook.

Bell notification settings can be modified in System Settings > Accessibility Options > Bell.

Play a sound instead of a PC speaker beep using PulseAudio#X11 Bell Events.

You can add this command to a startup file such as /etc/xprofile to make it permanent. See xprofile and xset(1) for more information.

beep(1) is a PC speaker beeping program. beep is useful for situations where no sound card and/or speakers are available, and simple audio notification is desired.

Install the beep package.

You may also need to unmute the PC speaker in ALSA.

beep uses /dev/input/by-path/platform-pcspkr-event-spkr to control the PC speaker which belongs to the input group, but adding user to input is not recommended by an upstream. To access the device file one has to set the proper permissions.

The following rule will allow any user, who is logged into the currently active virtual console session, to use the PC speaker:

Previous solution does not allow to use beep for users logged in remotely—e.g. via OpenSSH,—or processes running as any user other than the one logged into the currently active virtual console session. Alternatively, a new user group may be created with the corresponding rule to set the right permissions on the device file. With this solution any user in the beep group will be able to control the PC speaker:

To force reloading rules and device file to apply new user permission without a reboot, execute:

The following example plays slightly higher and shorter sound than beep default—see beep(1) § Tone options,—and repeats it two times:

Repositories collecting shell scripts playing various music using beep:

See also beep(1) § Sound Volume.

The PC speaker might remain silent when the HD Audio sound card is in power-saving mode. Apparently—depending on hardware—the beeps are actually fed as an analog input into the card, and will be ignored if the card is asleep. You can debug this by playing music (to keep the card awake) in one virtual console and then beeping in another.

For more information, see Advanced Linux Sound Architecture/Troubleshooting#Power saving.

**Examples:**

Example 1 (unknown):
```unknown
# rmmod pcspkr
# rmmod snd_pcsp
```

Example 2 (unknown):
```unknown
/etc/modprobe.d/nobeep.conf
```

Example 3 (unknown):
```unknown
blacklist pcspkr
blacklist snd_pcsp
```

Example 4 (unknown):
```unknown
module_blacklist=pcspkr,snd_pcsp
```

---

## GNU

**URL:** https://wiki.archlinux.org/title/GNU_Project

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## List of applications/Science

**URL:** https://wiki.archlinux.org/title/List_of_applications/Science

**Contents:**
- Mathematics
  - Calculator
    - Console
    - Graphical
    - Texas Instruments
  - Computer algebra system
  - Visualization of networks/graphs
  - Scientific or technical computing
  - Statistics
  - Data analysis and plotting

See also Wikipedia:Comparison of software calculators.

See also Wikipedia:Comparison of computer algebra systems.

See also Wikipedia:Comparison of numerical analysis software.

See also Wikipedia:Comparison of statistical packages.

See also Wikipedia:List of information graphics software.

See also List of applications/Documents#Spreadsheets.

See also Wikipedia:Proof assistant.

See also Wikipedia:List of molecular graphics systems.

See also Wikipedia:List of astrometric solvers.

See also Wikipedia:Planetarium software and Wikipedia:List of observatory software.

See also Wikipedia:List of open source bioinformatics software.

See also Wikipedia:List of computer-aided design editors.

Slicers convert 3D models into a format supported by the 3D printer, usually this format is G-code.

Software for controlling 3D printers, usually over a cable or wireless.

See also Wikipedia:Comparison of EDA software.

Digital logic software are mainly simple educational tools that intended for only designing and simulating logic circuits.

Also see Wikipedia:Hardware description language.

See the main article: Amateur radio#Software.

See also Wikipedia:List of software-defined radios.

See also Wikipedia:Comparison_of_photogrammetry_software.

---

## GNU Screen

**URL:** https://wiki.archlinux.org/title/GNU_Screen

**Contents:**
- Installation
- Usage
  - Common Commands
  - Command Prompt Commands
  - Named sessions
  - Customizing Screen
- Tips and tricks
  - Autostart with systemd
  - Change the escape key
  - Start at window 1

GNU Screen is a full-screen window manager that multiplexes a physical terminal between several processes, typically interactive shells. Programs running in Screen continue to run when their window is currently not visible and even when the whole screen session is detached from the user's terminal.

See the official overview GNU Screen manual for the description of the features.

Install the screen package.

Commands are entered pressing the "escape key" Ctrl+a and then the key binding.

Some users find the default escape key Ctrl+a inconvenient. The escape key can be changed to another key as described in #Change the escape key.

To create a named session, run screen with the following command:

To (re)name an existing a session, run the following command while screen is running:

Ctrl+a :sessionname session_name

To print a list of pid.tty.host strings identifying your screen sessions:

To attach to a named screen session, run this command:

You can modify the default settings for Screen according to your preference either through a personal .screenrc file which contains commands to be executed at startup (e.g. ~/.screenrc) or on the fly in command mode (e.g. Ctrl+a :vbell off).

This service autostarts screen for the specified user (e.g. systemctl enable screen@florian). Running this as a system unit is important, because systemd --user instance is not guaranteed to be running and will be killed when the last session for given the user is closed.

It can be a good idea to change the default escape key, not only because "a" is usually typed with the left pinky, but also because Ctrl+a is mapped to the common command beginning-of-line in GNU Readline and Bash-like shells.

The escape key can be changed with the escape option in ~/.screenrc, or the -e option to screen.

For example, if you find that you rarely type Ctrl+j in your shell or editor, you could use escape ^Jj to set the escape key to Ctrl+j. The second "j" means that a literal Ctrl+j can be sent to the terminal via the sequence Ctrl+j j. For Dvorak keyboard users, Ctrl+t (escape ^Tt) might be more convenient.

More exotic options include escape `` which sets the escape key to `, or escape ^^^ which sets it to Ctrl+^.

The escape key is also called the "command character" in Screen documentation.

By default, the first screen window is 0. If you would rather never have a window 0 and start instead with 1, add the following lines on your configuration:

It is possible to get stuck in a nested screen session. A common scenario: you start an SSH session from within a screen session. Within the SSH session, you start screen. By default, the outer screen session that was launched first responds to Ctrl+a commands. To send a command to the inner screen session, use Ctrl+a a, followed by your command. For example:

For Bash and Zsh, add the following snippet to your .bashrc or .zshrc before your aliases:

This article or section is out of date.

By default, Screen uses an 8-color terminal emulator. To enable more colors, you need to be using a terminal that supports them and set the correct term value. This will use terminfo to describe how the ANSI escape codes will be interpreted. An entry in the terminfo database structure must exist, ncurses provides many common descriptions stored under /usr/share/terminfo/.

First try the generic value:

If that does not work, try setting it based on your terminal. When using xterm-based terminal:

When using rxvt-unicode:

As a last resort, try setting termcapinfo instead:

The default statusbar may be a little lacking. You may find this one more helpful:

This one is pretty simple; just switch your current hardstatus line into a caption line with notification, and edit accordingly:

This will give you something like screen (0 bash) in the title of your terminal emulator. The caption supplies the date, current time, and colorizes your screen window collection.

The scroll buffer of GNU Screen can be accessed with Ctrl+a [. However, this is very inconvenient. To use the scroll bar of e.g. xterm or Konsole, add the following line [1]:

If you started a program outside Screen, but now you would like it to be inside, you can use reptyr to reparent the process from its current TTY to one inside screen.

Install the reptyr package.

Get the PID of the process (you can use ps ax for that). Now just enter the PID as argument to reptyr inside a screen window.

If you want a different bash prompt when in a screen session, add the following to your .bashrc[2]:

With this setting, Screen will not make an ugly screen flash instead of a bell sound.

To get rid of the vertical bars:

To hide the horizontal bar, set the back and foreground color to default (d) and display a blank (" "):

If this does not work, try caption string "%{00} " instead. For the default caption in black and white, use caption string "%{00}%3n %t".

When you open a text editor like nano in screen and then close it, the text may stay visible in your terminal. To fix this, put the following:

This article or section needs expansion.

Add following to ~/.screenrc:

**Examples:**

Example 1 (unknown):
```unknown
:source ~/.screenrc
```

Example 2 (unknown):
```unknown
/etc/screenrc
```

Example 3 (unknown):
```unknown
$ screen -S session_name
```

Example 4 (unknown):
```unknown
:sessionname session_name
```

---

## List of applications/Utilities

**URL:** https://wiki.archlinux.org/title/Terminal_emulator

**Contents:**
- Terminal
  - Command shells
  - Terminal emulators
    - VTE-based
    - KMS-based
    - framebuffer-based
  - Terminal pagers
  - Terminal multiplexers
  - Serial terminals
- Files

See the main article: Command-line shell.

See also Wikipedia:Comparison of command shells.

Terminal emulator shows a graphical user interface (GUI) window that contains a terminal. Most emulate xterm, which in turn emulates VT102, which emulates teletypewriter (TTY).

For a comprehensive list, see the List of terminal emulators.

VTE (Virtual Terminal Emulator) is a widget developed during early GNOME days for use in the GNOME Terminal. It has since given birth to many terminals with similar capabilities.

The following terminal emulators are based on the kernel mode setting that could be invoked without X.

In the GNU/Linux world, the framebuffer can refer to a virtual device in the Linux kernel (fbdev) or the virtual framebuffer system for X (xvfb). This section mainly lists the terminal emulators based on the in-kernel virtual device, i.e. fbdev.

See also Wikipedia:Terminal pager.

See also Wikipedia:Terminal multiplexer.

See Working with the serial console#Graphical front-ends.

See also Wikipedia:Comparison of file managers.

Note that some of these twin-panel file managers can also be set to have only one pane.

See Trash management#Trash creation.

This article or section is a candidate for merging with Synchronization and backup programs#Data synchronization.

See also Synchronization and backup programs, Wikipedia:Comparison of file synchronization software, and Wikipedia:Comparison of backup software.

For archiving and compression command-line tools, see Archiving and compression.

See also Wikipedia:Comparison of file comparison tools.

For managing pacnew/pacsave files, specialised tools exist. See Pacnew and Pacsave files#Managing .pac* files.

See diff(1) from diffutils and its alternatives.

Vim and Emacs provide merge functionality with vimdiff and ediff.

See rename(1) from util-linux.

This section lists utilities for file searching based on filename, file path or metadata. For full-text searching, see the next section.

See also Wikipedia:List of search engines#Desktop search engines.

See find(1) from findutils and its alternatives.

These programs index your files to allow for quick searching.

See grep(1) from grep and its alternatives, which provide non-indexed full-text search.

See also Wikipedia:Comparison of revision control software.

See also Wikipedia:List of build automation software.

See also Wikipedia:Comparison of integrated development environments.

For PHP specific list, see PHP#Development tools.

See also D-Bus#Debugging.

Lex and Yacc are part of POSIX.

And then there are also:

These programs provide ready-made user interfaces for alerting the user or prompting for information. These are best suited for writing shell scripts; for more complex use-cases, see #GUI builders.

See also Wikipedia:Comparison of hex editors.

See also Wikipedia:Hex dump.

See also Wikipedia:Literate programming.

See also Wikipedia:List of Unified Modeling Language tools.

See also Git server#Advanced web applications.

See also Wikipedia:List of tools for code review.

See also Wikipedia:List of game engines.

This article or section is a candidate for moving to List of applications/Other#Desktop environments.

See Keyboard shortcuts#Xorg.

See the main article: Input method.

See Partitioning#Partitioning tools.

See File systems#Types of file systems.

See also udisks#Mount helpers.

See S.M.A.R.T.#GUI applications.

See File recovery#List of utilities.

See also Securely wipe disk.

See also Wikipedia:List of tools to create Live USB systems.

See also Category:Monitoring.

See lm_sensors#Graphical front-ends.

See also Wikipedia:Font management software.

See man page#Reading local man pages.

See Time synchronization.

See also Xrandr#Graphical front-ends.

See Backlight#Backlight utilities.

See ICC profiles#Utilities and Backlight#Color correction.

See CUPS#GUI applications.

See Bluetooth#Front-ends.

See Power management#Userspace tools.

See systemd#GUI configuration tools.

See GRUB/Tips and tricks#GUI configuration tools.

See pacman tips#Utilities.

See Libvirt#Client and VirtualBox.

See Wine (Windows) and Darling (MacOS).

**Examples:**

Example 1 (unknown):
```unknown
coredumpctl
```

Example 2 (unknown):
```unknown
drkonqi-coredump-gui
```

Example 3 (unknown):
```unknown
qtlogging.ini
```

Example 4 (unknown):
```unknown
ug --hexdump
```

---

## List of applications/Documents

**URL:** https://wiki.archlinux.org/title/Text_editor

**Contents:**
- Text editors
  - Console
    - Emacs-style text editors
    - Vi-style text editors
  - Graphical
- Office
  - Office suites
  - Word processors
    - WYSIWYG HTML editors
    - Desktop publishing

See also Wikipedia:Comparison of text editors.

Some of the lighter-weight Integrated development environments can also serve as text editors.

See also Wikipedia:Comparison of office suites.

See also Wikipedia:Comparison of word processors.

See also Wikipedia:Comparison of spreadsheet software.

For DBMS-specific tools, see:

See also Wikipedia:Comparison of database tools.

These kinds of software are in a substance somewhat between text processing core utilities like awk, spreadsheets and production-level database system. And they usually come with a non-SQL command-line interface.

See also #TeX formula editors and Wikipedia:Formula editor.

See also Wikipedia:Comparison of document markup languages.

See also Wikipedia:AsciiDoc.

See also the official website and Wikipedia:Markdown.

See also reStructuredText.

With TeX, LaTeX and friends, creation of any scientific document, article, journal, etc. is made commonplace.

See also Wikipedia:Comparison of TeX editors and Wikibooks:LaTeX/Installation#Editors.

See also Wikipedia:Comparison of XML editors.

See also #Markup languages and PDF, PS and DjVu.

See also Wikipedia:Comparison of reference management software.

See PDF, PS and DjVu.

Some PDF viewers like apvlv, Atril, MuPDF, Okular, Xreader, and Zathura also support the EPUB format.

Some PDF and E-book viewers like Atril, Bookworm, Calibre, Foliate, GNOME Document Viewer, Lector, MuPDF, Okular, Papers, Xreader and Zathura also support the Comicbook format.

See also Wikipedia:Microsoft Compiled HTML Help.

Some PDF and E-book viewers like Cool Reader, FBReader and Okular also support the CHM format.

See also Wikipedia:Comparison of optical character recognition software.

See also Wikipedia:Comparison of notetaking software.

See also Wikipedia:List of concept- and mind-mapping software.

See also #Markdown editors and Wikipedia:Full-screen writing program.

See also Wikipedia:Category:Dictionary software and Wikipedia:DICT#DICT clients.

See Language checking.

See also Wikipedia:Comparison of computer-assisted translation tools.

---

## PC speaker

**URL:** https://wiki.archlinux.org/title/PC_speaker

**Contents:**
- Mechanism
- Disabling the PC speaker
  - Physically
  - Globally
  - Console
    - Virtual console
    - Readline-aware shell
    - Less pager
    - Arch Linux ISO
  - ALSA

PC speaker—beeper—is a built-in loudspeaker in most personal computers since the first IBM PC. This speaker is not capable of high quality playback and merely serves as a simple means of auditory feedback in the form of beeps. Some software—e.g. web browsers, editors and terminals—may produce beeps which may or may not be desired by the user. This article serves as a guide for configuring and/or disabling the speaker entirely.

For situations where no sound card or speakers are available and a simple audio notification is desired, see #beep.

The PC speaker is typically a physical unit connected on the front connections header of the motherboard. Some motherboard manufacturers do not ship their motherboards with a PC speaker at all, whereas others may have the PC speaker soldered directly onto the surface. Laptops typically have no physical PC speaker but have the beeper routed to the laptop internal speakers. In some cases, the beeper is heard on the regular output—i.e. speakers or headphones—of the soundcard, which tends to be unexpectedly loud.

Upon boot the UEFI/BIOS will traditionally generate a beep during power-on self-test (POST). Recent motherboard models omit the POST beep in favor of rapidly booting into the operating system. The UEFI user interface typically allows for toggling the POST beeps but it cannot configure the PC speaker to be turned off completely.

Once the system has booted into Linux and the pcspkr kernel module is loaded, the PC speaker can be used by the environment, be invoked manually by the user, and be configured to some extent.

Because the PC speaker is controlled directly by the CPU, along with the fact that they are built for beeping only, PC speaker cannot be used for playing back audio files. If this is really desired, unloading the pcspkr module and installing the snd-pcsp-dkmsAUR package provides a rudimentary audio output.

By removing the PC speaker the system will not be able to produce beeps. This can be achieved by physically removing the unit from the motherboard (if possible). Some manufacturers may provide a jumper header to switch it off.

The PC speaker can be disabled by unloading the pcspkr and snd_pcsp kernel modules:

Blacklisting the pcspkr and snd_pcsp modules will prevent udev from loading them at boot. Create the file:

Blacklisting it on the kernel command line is yet another way. Simply add module_blacklist=pcspkr,snd_pcsp to your boot loader kernel line.

In virtual console (TTY) you can set the bell duration to zero milliseconds with setterm(1):

For a shell which utilizes the Readline library (e.g. Bash), uncomment this line in /etc/inputrc (or add it to ~/.inputrc):

To disable PC speaker in less(1) pager, you can launch it with less --quiet to mute PC speaker for end of file events, or less --QUIET to mute it altogether. For man pages, launch man --pager="less --QUIET" or set the $MANPAGER or $PAGER environment variables.

Alternatively, you can add these lines to your shell configuration file:

If you want to disable the init tune on the Arch Linux ISO, you will need to repack the ISO. To do so, first install the libisoburn and mtools packages.

Extract the El Torito boot images and systemd-boot configuration (loader.conf) from the ISO:

Make loader.conf writable and remove the beep option from it:

Add the modified loader.conf to the El Torito UEFI boot image:

Finally, repack the ISO using the modified boot image and loader.conf:

For most sound cards the PC speaker is listed as an ALSA channel, named either PC Speaker, PC Beep, or Beep. To mute the speaker, either use alsamixer(1) or amixer(1), for example:

To unmute the channel, see Advanced Linux Sound Architecture#Unmuting the channels.

Cinnamon seems to play a "water drop" sound. To disable it, set in gsettings(1):

Append this line to ~/.gtkrc-2.0:

Add the same line to the [Settings] section of $XDG_CONFIG_HOME/gtk-3.0/settings.ini:

This is documented in the Gnome Developer Handbook.

Bell notification settings can be modified in System Settings > Accessibility Options > Bell.

Play a sound instead of a PC speaker beep using PulseAudio#X11 Bell Events.

You can add this command to a startup file such as /etc/xprofile to make it permanent. See xprofile and xset(1) for more information.

beep(1) is a PC speaker beeping program. beep is useful for situations where no sound card and/or speakers are available, and simple audio notification is desired.

Install the beep package.

You may also need to unmute the PC speaker in ALSA.

beep uses /dev/input/by-path/platform-pcspkr-event-spkr to control the PC speaker which belongs to the input group, but adding user to input is not recommended by an upstream. To access the device file one has to set the proper permissions.

The following rule will allow any user, who is logged into the currently active virtual console session, to use the PC speaker:

Previous solution does not allow to use beep for users logged in remotely—e.g. via OpenSSH,—or processes running as any user other than the one logged into the currently active virtual console session. Alternatively, a new user group may be created with the corresponding rule to set the right permissions on the device file. With this solution any user in the beep group will be able to control the PC speaker:

To force reloading rules and device file to apply new user permission without a reboot, execute:

The following example plays slightly higher and shorter sound than beep default—see beep(1) § Tone options,—and repeats it two times:

Repositories collecting shell scripts playing various music using beep:

See also beep(1) § Sound Volume.

The PC speaker might remain silent when the HD Audio sound card is in power-saving mode. Apparently—depending on hardware—the beeps are actually fed as an analog input into the card, and will be ignored if the card is asleep. You can debug this by playing music (to keep the card awake) in one virtual console and then beeping in another.

For more information, see Advanced Linux Sound Architecture/Troubleshooting#Power saving.

**Examples:**

Example 1 (unknown):
```unknown
# rmmod pcspkr
# rmmod snd_pcsp
```

Example 2 (unknown):
```unknown
/etc/modprobe.d/nobeep.conf
```

Example 3 (unknown):
```unknown
blacklist pcspkr
blacklist snd_pcsp
```

Example 4 (unknown):
```unknown
module_blacklist=pcspkr,snd_pcsp
```

---

## List of applications/Multimedia

**URL:** https://wiki.archlinux.org/title/List_of_applications/Multimedia

**Contents:**
- Codecs
- Image
  - Image viewers
    - Framebuffer
    - Console
    - Graphical
  - Image organizers
  - Image processing
    - Console
    - Graphical

See the main article: Codecs.

See also Wikipedia:Comparison of image viewers.

See also Wikipedia:Image organizer.

See also Wikipedia:Comparison of raster graphics editors.

Some image viewers and organizers like digiKam, Ephoto, GNOME Photos, gThumb, ida, nomacs, Pantheon Photos, Phototonic and Shotwell also provide some basic image manipulation functionality.

See also Wikipedia:Comparison of vector graphics editors.

Some of these programs may require using keyboard shortcuts in conjunction with the mouse, see Libinput#Enable the touchpad while typing for touchpad users.

See also Wikipedia:Comparison of font editors.

The drawing application Krita, the 3D editor Blender (Grease Pencil mode), and the python library Manim have 2D animation features too.

See also Wikipedia:Comparison of 3D computer graphics software.

See Screen capture#Screenshot software.

See gPhoto#Installation.

See ASCII art#Software.

See also the main article Sound system and Wikipedia:Sound server.

See also Wikipedia:Comparison of audio player software.

Many applications in the #Video players section also support audio playback.

See also Wikipedia:Comparison of digital audio editors.

See also Professional audio.

See also LilyPond#Front-ends and Wikipedia:Comparison of scorewriters.

See also Wikipedia:Comparison of audio synthesis environments.

This section contains drum machines, software samplers and software synthesizers.

See also PulseAudio#Front-ends and JACK Audio Connection Kit#Comparison of JACK control GUIs.

See Optical disc drive#Audio CD.

See also Wikipedia:Comparison of video player software.

See also Wikipedia:Comparison of video converters and Codecs and containers#Container format tools.

See also Wikipedia:Comparison of video editing software.

See also Wikipedia:Comparison of subtitle editors.

See Screen capture#Screencast software.

Miracast is a standard for wireless connections from sending devices to display receivers mainly using Wi-Fi Direct. Use iw dev to check your hardware support. Use iw reg get to make sure the regulatory domain is not set to "Global", as that might block some functionality.

See also FFmpeg#Recording webcam and Wikipedia:Comparison of webcam software.

See also Wikipedia:List of DVD authoring applications.

See Optical disc drive#DVD-Video.

See Optical disc drive#Burning CD/DVD/BD with a GUI.

**Examples:**

Example 1 (unknown):
```unknown
mate-color-select
```

Example 2 (unknown):
```unknown
-id3v2_version 4
```

Example 3 (unknown):
```unknown
calfjackhost
```

Example 4 (unknown):
```unknown
vlc -I ncurses
```

---

## Command-line shell

**URL:** https://wiki.archlinux.org/title/Shell

**Contents:**
- List of shells
  - POSIX compliant
  - Alternative shells
- Changing your default shell
- Uninstalling shell
- Login shell
- Configuration files
  - /etc/profile
  - Standardisation
- Input and output

Shells that are more or less POSIX compliant are listed under #POSIX compliant, while shells that have a different syntax are under #Alternative shells.

These shells can all be linked from /usr/bin/sh. When Bash, mkshAUR and zsh are invoked with the sh name, they automatically become more POSIX compliant.

After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

And to set one as default for your user do:

If you are using systemd-homed, run:

where /full/path/to/shell is the full path as given by chsh -l.

If you now log out and log in again, you will be greeted by the other shell.

Change the default shell before removing the package of the shell.

Alternatively, modify the user database.

Use it for every user with a shell other than bash set as their login shell (including root if needed). When completed, the package can be removed.

A login shell is an invocation mode, in which the shell reads files intended for one-time initialization, such as system-wide /etc/profile or the user's ~/.profile or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via SSH, changes the user with sudo or su using the --login parameter, or when the user manually invokes a login shell (e.g. by bash --login).

See #Configuration files and the links therein for an overview of the various initialization files. For more information about login shell, see also Difference between Login Shell and Non-Login Shell? and Why a "login" shell over a "non-login" shell? on Stack Exchange.

To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g. Bash#Configuration files or Zsh#Startup/Shutdown files.

See also Wikipedia:Unix shell#Configuration files for a comparison of various configuration files of various shells.

Upon login, all Bourne-compatible shells source /etc/profile, which in turn sources any readable *.sh files in /etc/profile.d/: these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

It is possible to make (some) shells configuration files follow the same naming convention, as well as supporting some common configuration between the shells.

See the article about this and the related repository. See also xsh.

See also GregsWiki and I/O Redirection.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/sh
```

Example 2 (unknown):
```unknown
$ chsh -s /full/path/to/shell
```

Example 3 (unknown):
```unknown
$ homectl update --shell=/full/path/to/shell user
```

Example 4 (unknown):
```unknown
/full/path/to/shell
```

---

## Vim

**URL:** https://wiki.archlinux.org/title/Vim

**Contents:**
- Installation
- Usage
- Configuration
  - Clipboard
  - Syntax highlighting
  - Indentation
  - Visual wrapping
  - Using the mouse
  - Traverse line breaks with arrow keys
- Merging files

Vim a vi-style terminal text editor. It is an extended version of vi with additional features, including syntax highlighting, a comprehensive help system, native scripting (Vim script), a visual mode for text selection, comparison of files (vimdiff(1)), and tools with restricted capabilities such as rview(1) and rvim(1).

Install one of the following packages:

For a basic overview on how to use Vim, follow the Vim tutorial by running either vimtutor (for the terminal version) or gvimtutor (for the graphical version).

Vim includes a broad help system that can be accessed with the :h subject command. Subjects include commands, configuration options, key bindings, plugins etc. Use the :h command (without any subject) for information about the help system and jumping between subjects.

Vim's user-specific configuration file is located in the home directory: ~/.vimrc, and Vim files of current user are located inside ~/.vim/. The global configuration file is located at /etc/vimrc. Global Vim files such as defaults.vim and archlinux.vim are located inside /usr/share/vim/.

From version 9.1.0327 Vim adopts freedesktop XDG Base Directory Specification: that means, you can now place your configuration files under ~/.config/vim/ so Vim will stop littering your home directory.

For gVim, the user-specific configuration file is located at ~/.gvimrc and the global configuration file is located at /etc/gvimrc.

Vim commands such as :yank or :put normally operate with the unnamed register "". If the +clipboard feature is available and its value includes unnamed, then Vim yank, delete, change and put operations which would normally go to the unnamed register will use the clipboard register "* instead, which is the PRIMARY buffer in X.

To change the default register, you can :set clipboard=unnamedplus to use the "+ register instead. The "+ clipboard register corresponds to the CLIPBOARD buffer in X. It should be noted that the clipboard option can be set to a comma-delimited value. If you :set clipboard=unnamedplus,unnamed, then yank operations will also copy the yanked text to the "* register in addition to the "+ register (however, delete, change and put operations will still only operate on the "+ register).

For more information, see :help 'clipboard'. There are other values which can be set for the clipboard feature. You can use :help clipboard-unnamed to take you to the help topic for the first valid value which can be set for this feature, followed by help for all other valid values.

To enable syntax highlighting for many programming languages:

This article or section needs expansion.

The indent file for specific file types can be loaded with:

The wrap option is on by default, which instructs Vim to wrap lines longer than the width of the window, so that the rest of the line is displayed on the next line. The wrap option only affects how text is displayed, the text itself is not modified.

The wrapping normally occurs after the last character that fits the window, even when it is in the middle of a word. More intelligent wrapping can be controlled with the linebreak option. When it is enabled with set linebreak, the wrapping occurs after characters listed in the breakat string option, which by default contains a space and some punctuation marks (see :help breakat).

Wrapped lines are normally displayed at the beginning of the next line, regardless of any indentation. The breakindent option instructs Vim to take indentation into account when wrapping long lines, so that the wrapped lines keep the same indentation of the previously displayed line. The behaviour of breakindent can be fine-tuned with the breakindentopt option, for example to shift the wrapped line another four spaces to the right for Python files (see :help breakindentopt for details):

Vim has the ability to make use of the mouse, but it only works for certain terminals:

To enable this feature, add this line into ~/.vimrc:

The mouse=a option is set in defaults.vim.

By default, pressing Left at the beginning of a line, or pressing Right at the end of a line, will not let the cursor traverse to the previous, or following, line.

The default behavior can be changed by adding set whichwrap=b,s,<,>,[,] to your ~/.vimrc file.

Vim includes a diff editor (a program that shows differences between two or more files and aids to conveniently merge them). Use vimdiff to run the diff editor — just specify some couple of files to it: vimdiff file1 file2. Here is the list of vimdiff-specific commands.

To show the line number column, use :set number. By default absolute line numbers are shown, relative numbers can be enabled with :set relativenumber. Setting both enables hybrid line numbers—the current line is absolute, while the others are relative.

Jumping to a specific line is possible with :line number or line numbergg. Jumps are remembered in a jump list, see :h jump-motions for details.

Vim has the ability to do spell checking, enable by entering:

By default, only English language dictionaries are installed (in /usr/share/vim/vim82/spell/). More dictionaries can be found in the official repositories by searching for vim-spell. Additional dictionaries can be put in the folder ~/.vim/spell/ and enabled with the command: :setlocal spell spelllang=en_us (replacing the en_us with the name of the needed dictionary).

Normally, exiting vim discards all unessential information such as opened files, command line history, yanked text etc. Preserving this information can be configured in the following ways.

The viminfo file may also be used to store command line history, search string history, input-line history, registers' content, marks for files, location marks within files, last search/substitute pattern (to be used in search mode with n and & within the session), buffer list, and any global variables you may have defined. For the viminfo modality to be available, the version of vim you installed must have been compiled with the +viminfo feature.

Configure what is kept in your viminfo file, by adding (for example) the following to your ~/.vimrc file:

where each parameter is preceded by an identifier:

See the official viminfo documentation for particulars on how a pre-existing viminfo file is modified as it is updated with current session information, say from several buffers in the current session you are in the process of exiting.

Session files can be used to save the state of any number of particular sessions over time. One distinct session file may be used for each session or project of your interest. For that modality to be available, the version of vim you installed must have been compiled with the +mksession feature.

Within a session, :mksession[!] [my_session_name.vim] will write a vim-script to my_session_name.vim in the current directory, or Session.vim by default if you choose not to provide a file name. The optional ! will clobber a pre-existing session file with the same name and path.

A Vim session can be resumed either when starting Vim from terminal:

Or in an already opened session buffer by running the Vim command:

Exactly what is saved and additional details on session files options are extensively covered in the Vim documentation. Commented examples are found here.

See Restore cursor to file position in previous editing session on the Vim wiki.

Create an alias for vi to vim.

Alternatively, if you want to be able to type sudo vi and get vim, install vi-vim-symlinkAUR which will remove vi and replace it with a symlink to vim. You could also create this symlink yourself and place it somewhere higher in your path than /usr/bin to have it take precedence.

If there is a ^M at the end of each line then this means you are editing a text file which was created in MS-DOS or Windows. This is because in Linux only a single line feed character (LF) used for line break, but in Windows/MS DOS systems they are using a sequence of a carriage return (CR) and a line feed (LF) for the same. And this carriage returns are displayed as ^M.

To remove all carriage returns from a file do:

Note that there ^ is a control letter. To enter the control sequence ^M press Ctrl+v,Ctrl+m.

Alternatively install the package dos2unix and run dos2unix file to fix the file.

When using a window manager configured to ignore window size hints, gVim will fill the non-functional area with the GTK theme background color.

The solution is to adjust how much space gVim reserves at the bottom of the window. Put the following line in ~/.vimrc:

Scripts allow Vim to be used as a terminal pager, with the benefit of various vim features such as color schemes. To change the default pager, export the PAGER environment variable.

Vim comes with the /usr/share/vim/vim91/macros/less.sh script, for which you can create an alias. Note that this script does not support any command-line flags mentioned in less(1) § OPTIONS.

Alternatively, there is also the vimpager Vim script. Note that not all command-line flags are supported; the list of supported flags is available on GitHub.

A middle way between a pager and an editor are [g]vim -R (gvim -R is equivalent to gview). This will cause the editor to open files in a readonly mode. Every editor feature that does not involve modifying the files is available as usual. In fact, the readonly mode can be explicitly overridden, to enable modification as well.

In order to highlight the first string that will be matched in a search while typing the search, add the following line to your ~/.vimrc:

In order to highlight all strings that will be matched in a search while typing the search, and after the search has been executed, add the following line to your ~/.vimrc:

This article or section is out of date.

Since 7.3.1178 Vim will search for ~/.vim/vimrc if ~/.vimrc is not found.

[G]VIMINIT environment variable will also affect Neovim. If separate configs for Vim and Neovim are desired then the following will be a better choice:

Adding plugins to Vim can increase your productivity by extending Vim features. Plugins can alter Vim UI, add new commands, enable code completion support, integrate other programs and utilities with Vim, add support for additional languages and more.

Vim has the possibility to load third-party plugins natively. This functionality can be used by storing third-party packages in the ~/.vim/pack folder. The structure of this folder differs slightly from that of typical plugin managers which will usually have a single directory per plugin. What follows is a typical installation procedure and directory structure (using Tim Pope's vim-surround plugin as an example):

It is important to note that ~/.vim/pack/tpope is a package directory which is loosely defined as directory containing one or more plugins in the Vim documentation. Plugin repositories should not be downloaded to this directory though. The name of the package directory is also arbitrary. You can choose to keep all your plugins in a single package directory or, as in our example, use the author's GitHub name, tpope.

The package directory can contain the following subfolders:

Now change into the start folder and checkout the plugin repository:

This creates an additional subfolder, ~/.vim/pack/tpope/start/surround, where the plugin files are placed.

Next, update the help index if the plugin contains help files:

The plugin will now be loaded automatically when starting Vim. No changes to ~/.vimrc are required, barring plugin-specific options.

A plugin manager is a plugin that installs, manages and updates Vim plugins. This can be useful if you are also using Vim on platforms other than Arch Linux and want a consistent method of updating plugins.

The vim-plugins group provides various plugins. Use pacman -Sg vim-plugins command to list available packages which you can then install with pacman.

Cscope is a tool for browsing a project. By navigating to a word/symbol/function and calling cscope (usually with shortcut keys) it can find: functions calling the function, the function definition, and more.

Install the cscope package.

Copy the cscope default file where it will be automatically read by Vim:

Create a file which contains the list of files you wish cscope to index (cscope can handle many languages but this example finds .c, .cpp and .h files, specific for C/C++ project):

Create database files that cscope will read:

Default keyboard shortcuts:

Feel free to change the shortcuts.

Taglist provides an overview of the structure of source code files and allows you to efficiently browse through source code files in different programming languages.

Install the vim-taglistAUR package.

Useful options to be put in ~/.vimrc:

Vim's GTK 3 GUI may be slower than the GTK 2 version (see FS#51366). gvim-gtk2AUR can be installed as a workaround.

By default, gVim will try to search for an X11 display and resort to terminal if unable to find one. To use it under Wayland-only environments, add the GVIM_ENABLE_WAYLAND=1 environment variable.

Vim still lacks full bidirectional support, and this varies depending on the terminal.

Use :rightleft to force text alignment using. It can be assigned to a keybind using:

Vim has its own letter shaping functionality. Despite some rendering issues, this works on terminals with no letter shaping support like alacritty and st. The shaping depends on Arabic Presentation Forms-B (U+FE70–FEFF), so make sure your font includes support for these characters. As there is no known monospace font with full support for these characters, you need to have an additional fallback font (e.g: vazir-code-fontsAUR with fallback to ttf-dejavu). See St#Arabic shaping support for example terminal fonts setup.

However, if the terminal supports letter shaping like gnome-terminal and other libvte-based terminals, then Vim and the terminal letter shaping could conflict, resulting in mangled Arabic text. Currently, Vim doesn't detect if the terminal has letter-shaping capabilities or not. So the workaround is to manually tell Vim to leave letter-shaping up to the terminal by :set notbidi. Note that will cause reversed text when :set rightleft because of a limitation. See :set arabic for more info.

**Examples:**

Example 1 (unknown):
```unknown
vim-gvim-common
```

Example 2 (unknown):
```unknown
vim-gvim-gtk3
```

Example 3 (unknown):
```unknown
defaults.vim
```

Example 4 (unknown):
```unknown
archlinux.vim
```

---

## GNU

**URL:** https://wiki.archlinux.org/title/GDB

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## Bash/Prompt customization

**URL:** https://wiki.archlinux.org/title/Bash/Prompt_customization

**Contents:**
- Prompts
- Techniques
  - Bash escape sequences
  - Terminfo escape sequences
  - ANSI escape sequences
  - Embedding commands
  - PROMPT_COMMAND
  - Escapes between command input and output
  - Customizing root prompts
- Examples

Bash has several prompts which can be customized to increase productivity, aesthetic appeal, and nerd cred.

Bash has five prompt strings that can be customized:

All of the prompts are customized by setting the corresponding variable to the desired string (usually in ~/.bashrc), for example

While one can simply set their prompt to a plain string, there are a variety of techniques for making the prompt more dynamic and useful.

When printing the prompt string, Bash looks for certain backslash-escaped characters and will expand them into special strings. For example, \u is expanded into the current username and \A is expanded to the current time. So a PS1 of '\A \u $ ' would be printed like 17:35 username $ .

See the man page bash(1) § PROMPTING or the Bash reference manual for a complete list of escape sequences.

Aside from the escape characters recognized by Bash, most terminals recognize special escape sequences that affect the terminal itself rather than printing characters. For example they might change the color of subsequent printed characters, move the cursor to an arbitrary location, or clear the screen. These escape sequences can be somewhat illegible and can vary from terminal to terminal, so they are documented in the terminfo database. To see what capabilities your terminal supports, run

The capability names (the part before the =) can be looked up in terminfo(5) for a description of what they do. For example, setaf sets the foreground color of whatever text is printed after it. To get the escape code for a capability, you can use the tput command. For example

Prints the escape sequence to set the foreground color to green.

To practically incorporate these capabilities into your prompt, you can use Bash's command substitution and string interpolation. For example

Unfortunately, valid ANSI escape sequences may be missing from your terminal's terminfo database. This is especially common with escape sequences for newer features such as 256 color support. In that case you cannot use tput, you must input the escape sequence manually.

See Wikipedia:ANSI escape code for examples of escape sequences. Every escape sequence starts with a literal escape character, which you can input using the Bash escape sequence \e. So for example,\e[48;5;209m sets the background to a peachy color (if you have 256 color support) and \e[2;2H moves the cursor near the top-left corner of the screen.

In cases where Bash escape sequences are not supported (such as PS3) you can get a literal escape character using Bash's printf builtin:

If you want to add the output of some command to your prompt, you might be tempted to use command substitution. For example, to add the amount of free memory to your prompt you might try:

But this does not work; the amount of memory shown is the same every time! This is because the command is run once, when PS1 is first set, and never again. The trick is to simply prevent the substitution either by escaping the $ or by defining it in single quotes — either way it will be substituted when the prompt is actually displayed:

To prevent long commands from making your PS1 huge, you can define functions:

If the PROMPT_COMMAND variable or array is set, it will be evaluated right before PS1 is displayed. This can be used to achieve quite powerful effects. For example it can reassign PS1 based on some condition, or perform some operation on your Bash history every time you run a command.

You can affect your input text in Bash by not resetting the text properties at the end of your PS1. For example, inserting tput blink at the end of your PS1 will make your typed commands blink. However this effect will also continue through the command's output since the text properties are not reset when you hit Enter.

In order to insert escape sequences after you type a command but before the output is displayed, you can set PS0. Alternatively, you can trap Bash's DEBUG signal, which is sent right before each command is executed:

To ensure that you know when you are running as root, you can customize your root prompt to make it clearly stand out (perhaps blinking red?). This is done by customizing the Bash prompt as usual but in root's home directory, /root. Start off by copying the skeleton files /etc/skel/.bash_profile and /etc/skel/.bashrc to /root, then edit /root/.bashrc as desired.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To see the full range of colors your terminal supports, you can use a simple loop with tput (change setab to setaf for text foregrounds):

If that does not work (and you cannot fix it by setting the correct TERM value), you can test the different manual escape sequences:

To change the manual escapes from background to foreground, the standard color range is 30..37, the high intensity range is 90..97, and the 48 should be changed to 38 for 256 colors.

The following terminfo capabilities are useful for prompt customization and are supported by many terminals. #1 and #2 are placeholders for numeric arguments.

Using the same trick from embedding commands you can delay the interpolation of special Bash variables like $?. So the following prompt shows the exit code of the previous command:

This can be made more interesting using conditionals and functions:

It is possible to move the cursor around the screen inside of PS1 to make different parts of the prompt appear in different locations. However, to ensure that Bash positions the cursor and output in the right position, you must move the cursor back to the original position after you are done printing elsewhere. This can be done using the tput capabilities sc and rc to save and restore the cursor position. The general pattern for a prompt that moves the cursor is

where the entire block of repositioned prompt is wrapped in \[ \] to prevent Bash from counting it as part of the regular prompt.

The simplest way to print text on the right side of the screen is to use printf

This creates a right-justified variable-sized field %*s and sets its size to the current number of columns of the terminal $COLUMNS.

The cup capability moves the cursor to a specific position on the screen, for example tput cup 20 5 moves the cursor to line 20, column 5 (where 0 0 is the top left corner). cuu, cud, cuf, and cub (up, down, forward, back) move the cursor relative to its current position. For example tput cuf 10 moves the cursor 10 characters to the right. You can use the LINES and COLUMNS variables in the arguments to move the cursor relative to the bottom and right edges. For example, to move 10 lines and 5 columns away from the bottom right corner:

The terminal window title can be customized in much the same way as the prompt: by printing escape sequences in the shell. Thus it is common for users to include window title customizations in their prompt. Although this is technically a feature of xterm, many modern terminals support it. The escape sequence to use is ESC]2;new titleBEL where ESC and BEL are the escape and bell characters. Using #Bash escape sequences, changing the title in your prompt looks like

Of course your window title string can include output from embedding commands or variables such as $PWD, so that the title changes with each command.

**Examples:**

Example 1 (unknown):
```unknown
17:35 username $
```

Example 2 (unknown):
```unknown
$ tput setaf 2
```

Example 3 (unknown):
```unknown
xterm-256color
```

Example 4 (unknown):
```unknown
GREEN="\[$(tput setaf 2)\]"
RESET="\[$(tput sgr0)\]"

PS1="${GREEN}my prompt${RESET}> "
```

---

## List of applications/Other

**URL:** https://wiki.archlinux.org/title/List_of_applications/Other

**Contents:**
- Organization
  - CalDAV/CardDAV servers
  - Personal information managers
  - Time management
    - Console
    - Graphical
  - Timers
    - Countdown timers and stopwatch
    - Break timers
    - Pomodoro timers

These applications support time, task and contacts management.

See Wikipedia:Pomodoro Technique for an introduction.

See also Wikipedia:Comparison of accounting software.

See also Wikipedia:Comparison of project management software.

See also List of applications/Science#Navigation and routing.

See also List of games#Education.

See also Wikipedia:List of flashcard software.

See Accessibility for tips on operating the desktop and Category:Accessibility for all available articles. See also On-screen keyboards.

See also Wikipedia:Comparison of speech synthesizers and listening comparison of the different engines.

See also Wikipedia:Speech recognition software for Linux.

See the main article: Display manager#List of display managers.

See the main article: Desktop environment#List of desktop environments.

See also List of applications/Utilities#Terminal multiplexers, which offer some of the functions of window managers for the console.

See the main article: Window manager#List of window managers.

See the main article: Xorg#List of composite managers.

See the main article: Wayland#Compositors.

See also Wikipedia:Taskbar.

Desktop environments typically have their own system tray implementation. E.g. KDE ships with Plasma Panel and Xfce ships with xfce4-panel. For GNOME, see GNOME#AppIndicators/Top bar icons. For dwm, see systray patch.

Desktop-independent tray indicators. Useful for window managers without built-in tray widgets:

See also Wikipedia:Comparison of desktop application launchers.

See also Wikipedia:Wallpaper (computing).

See also Wikipedia:Pager (GUI).

See: Notification servers.

See Clipboard#Managers.

See also Wikipedia:Open-source artificial intelligence, Wikipedia:Lists of open-source artificial intelligence software, Wikipedia:Comparison of deep learning software

**Examples:**

Example 1 (unknown):
```unknown
display -backdrop -background '#3f3f3f' -flatten -window root image
```

---

## Category:Terminal multiplexers

**URL:** https://wiki.archlinux.org/title/Terminal_multiplexer

See Wikipedia:Terminal multiplexer.

See also List of applications/Utilities#Terminal multiplexers.

---

## GNU

**URL:** https://wiki.archlinux.org/title/GNU

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## Zsh

**URL:** https://wiki.archlinux.org/title/Zsh

**Contents:**
- Installation
  - Initial configuration
  - Making Zsh your default shell
- Startup/Shutdown files
- Configure Zsh
  - Simple .zshrc
  - Configuring $PATH
  - Command completion
    - Custom completion
  - Key bindings

Zsh is a powerful shell that operates as both an interactive shell and as a scripting language interpreter. While being compatible with the POSIX sh (not by default, only if issuing emulate sh), it offers advantages such as improved tab completion and globbing.

The Zsh FAQ offers more reasons to use Zsh.

Before starting, users may want to see what shell is currently being used:

Install the zsh package. For additional completion definitions, install the zsh-completions package as well.

Make sure that Zsh has been installed correctly by running the following in a terminal:

You should now see zsh-newuser-install, which will walk you through some basic configuration. If you want to skip this, press q. If you did not see it, you can invoke it manually with:

Change your shell to /usr/bin/zsh. See Command-line shell#Changing your default shell.

When starting, Zsh will read commands from the following files in this order by default, provided they exist.

See the graphic representation.

Although Zsh is usable out of the box, it is almost certainly not set up the way most users would like to use it. But due to the sheer amount of customization available in Zsh, configuring Zsh can be a daunting and time-consuming experience. For automatic configuration, see #Third-party extensions.

Included below is a sample configuration file. It provides a decent set of default options as well as giving examples of many ways that Zsh can be customized. In order to use this configuration save it as a file named .zshrc.

Here is a simple .zshrc:

See #Prompt themes for more details about the prompt theme system.

Zsh ties the PATH variable to a path array. This allows you to manipulate PATH by simply modifying the path array. See A User's Guide to the Z-Shell for details.

To add ~/.local/bin/ to the PATH:

Perhaps the most compelling feature of Zsh is its advanced autocompletion abilities. At the very least, enable autocompletion in .zshrc. To enable autocompletion, add the following to your ~/.zshrc:

The above configuration includes ssh/scp/sftp hostnames completion but in order for this feature to work, users must not enable ssh's hostname hashing (i.e. option HashKnownHosts in ssh client configuration).

For autocompletion with an arrow-key driven interface, add the following to:

To activate the menu, press Tab twice.

For enabling autocompletion of privileged environments in privileged commands (e.g. if you complete a command starting with sudo, completion scripts will also try to determine your completions with sudo), include:

You can write custom completions on your own. Should you do so, you can refer to the zshcompsys(1) man page.

Note that the official documentation can be hard to read. You can consider trying the simpler zsh-completion-howto tutorial for an easy start.

Zsh does not use readline, instead it uses its own and more powerful Zsh Line Editor (ZLE). It does not read /etc/inputrc or ~/.inputrc. Read A closer look at the zsh line editor and creating custom widgets for an introduction to ZLE configuration.

ZLE has an Emacs mode and a vi mode. If one of the VISUAL or EDITOR environment variables contain the string vi then vi mode will be used; otherwise, it will default to Emacs mode. Set the mode explicitly with bindkey -e or bindkey -v respectively for Emacs mode or vi mode. The delay of pressing Esc key in vi mode is 0.4s by default, and you can make it shorter (0.05s) with export KEYTIMEOUT=5.

Key bindings are assigned by mapping an escape sequence matching a keypress to a ZLE widget. The available widgets, with descriptions of their actions and their default keybindings, are listed in zshzle(1) § STANDARD WIDGETS and zshcontrib(1) § ZLE FUNCTIONS.

The recommended way to set key bindings in Zsh is by using string capabilities from terminfo(5). For example[1][2]:

You need to set up the key array and make sure that ZLE enters application mode to use the following instructions; see #Key bindings.

To enable history search add these lines to .zshrc file:

By doing this, only the past commands matching the current line up to the current cursor position will be shown when Up or Down keys are pressed.

xterm-compatible terminals can use extended key-definitions from user_caps(5). Those are combinations of Shift, Alt, Ctrl and Meta together with Up, Down, Left, Right, PageUp, PageDown, Home, End or Del. Refer to the zkbd source for a list of recommended names for the modifier keys and key combinations.

For example, for Ctrl+Left to move to the beginning of the previous word and Ctrl+Right to move to the beginning of the next word:

Zsh offers the options of using a prompt theme or, for users who are dissatisfied with the themes (or want to expand their usefulness), the possibility to build a custom prompt.

Prompt themes are a quick and easy way to set up a colored prompt in Zsh. See zshcontrib(1) § PROMPT THEMES for information about prompt themes and how to write your own theme.

To use a theme, make sure that prompt theme system is set to autoload in .zshrc. This can be done by adding these lines to:

Available prompt themes are listed by running the command:

For example, to use the walters theme, enter:

To preview all available themes, use this command:

It is possible to install themes manually, without external configuration manager tools. For a local installation, first create a folder and add it to the fpath array, eg:

Now create a symbolic link of your theme file in this folder:

If instead you wish to install a theme globally, do:

Now you should be able to activate it using:

If everything works, you can edit your .zshrc accordingly.

In addition to adding a prompt theme through its own file, it is possible to add themes from within another file (like your .zshrc), eg:

Additionally to a primary left-sided prompt PS1 (PROMPT, prompt) that is common to all shells, Zsh also supports a right-sided prompt RPS1 (RPROMPT). These two variables are the ones you will want to set to a custom value.

Other special purpose prompts, such as PS2 (PROMPT2), PS3 (PROMPT3), PS4 (PROMPT4), RPS1 (RPROMPT), RPS2 (RPROMPT2) and SPROMPT, are explained in zshparam(1) § PARAMETERS USED BY THE SHELL.

All prompts can be customized with prompt escapes. The available prompt escapes are listed in zshmisc(1) § EXPANSION OF PROMPT SEQUENCES.

Zsh sets colors differently than Bash; You do not need to use profuse ANSI escape sequences or terminal capabilities from terminfo(5). Zsh provides convenient prompt escapes to set the foreground color, background color and other visual effects; see zshmisc(1) § Visual effects for a list of them and their descriptions.

Colors can be specified using a decimal integer, the name of one of the eight most widely-supported colors or as a # followed by an RGB triplet in hexadecimal format. See the description of fg=colour in zshzle(1) § CHARACTER HIGHLIGHTING for more details.

Most terminals support the following colors by name:

Color numbers 0–255 for terminal emulators compatible with xterm 256 colors can be found in the xterm-256color chart.

With a correctly set TERM environment variable, the terminal's supported maximum number of colors can be found from the terminfo(5) database using echoti colors. In the case of 24-bit colors, also check the COLORTERM environment variable with print $COLORTERM. If it returns 24bit or truecolor then your terminal supports 16777216 (224) colors even if terminfo shows a smaller number.

An example of a simple colorless prompt:

How it will be displayed:

This is an example of a two-sided prompt with color:

And here is how it will be displayed:

To use colors from the 16-255 range and 24-bit true color, you can use the number from 0 to 255 assigned to the wanted color and its hexadecimal color code, respectively:

See dotfiles#User repositories for more.

See xinit#Autostart X at login.

Many programs change the terminal state, and often do not restore terminal settings on exiting abnormally (e.g. when crashing or encountering SIGINT).

This can typically be solved by executing reset(1):

The following sections describe ways to avoid the need to manually reset the terminal.

The ttyctl command can be used to "freeze/unfreeze" the terminal. To freeze the interactive shell on launch, use the following:

Alternate linedrawing character set can screw up the terminal in a way which ttyctl cannot prevent.

A simple solution is to output the escape sequences that reset the terminal from the precmd hook function, so that they are executed every time before the prompt is drawn. For example, using the escape sequence \e[0m\e(B\e)0\017\e[?5l\e7\e[0;0r\e8:

To test if it works, run:

Zsh can be configured to remember the DIRSTACKSIZE last visited folders. This can then be used to cd them very quickly. You need to add some lines to your configuration file:

to print the dirstack. Use cd -<NUM> to go back to a visited folder. Use autocompletion after the dash. This proves very handy if using the autocompletion menu.

cdr allows you to change the working directory to a previous working directory from a list maintained automatically. It stores all entries in files that are maintained across sessions and (by default) between terminal emulators in the current session.

See zshcontrib(1) § REMEMBERING RECENT DIRECTORIES for setup instructions.

zoxide is a smarter cd command that lets you navigate anywhere in just a few keystrokes. It remembers your frequently used directories and uses a scoring mechanism to guess where you want to go.

Unlike Bash, Zsh does not enable a built in help command, instead it provides run-help. By default run-help is an alias to man, it can be either executed manually by prepending it to a command or it can be invoked for the currently typed command with the keyboard shortcuts Alt+h or Esc h.

Since by default it is just an alias to man, it will only work on external commands. To improve its functionality, so that it works on shell builtins and other shell features, you need to use the run-help function. See zshcontrib(1) for more information on the run-help and its assistant functions.

First load the run-help function and then remove the existing run-help alias. For convenience help can be aliased to run-help. For example, add following to your zshrc:

Assistant functions have to be enabled separately:

For example, run-help git commit command will now open the man page git-commit(1) instead of git(1).

Typically, compinit will not automatically find new executables in the $PATH. For example, after you install a new package, the files in /usr/bin/ would not be immediately or automatically included in the completion. Thus, to have these new executables included, one would run:

This 'rehash' can be set to happen automatically.[3] Simply include the following in your zshrc:

As above, however pacman can be configured with hooks to automatically request a rehash, which does not incur the performance penalty of constant rehashing as above. To enable this, create the /etc/pacman.d/hooks directory, and a /var/cache/zsh directory, then create a hook file:

This keeps the modification date of the file /var/cache/zsh/pacman consistent with the last time a package was installed, upgraded or removed. Then, zsh must be coaxed into rehashing its own command cache when it goes out of date, by adding to your ~/.zshrc:

If the precmd hook is triggered before /var/cache/zsh/pacman is updated, completion may not work until a new prompt is initiated. Running an empty command, e.g. pressing enter, should be sufficient.

As above, however the hook file looks like this:

The function trap above can be replaced with a list trap trap 'rehash' USR1. See zshmisc(1) § Trap Functions for differences between types of traps.

This method will instantly rehash all zsh instances, removing the need to press enter to trigger precmd.

Bind a ncurses application to a keystroke, but it will not accept interaction. Use BUFFER variable to make it work. The following example lets users open ncmpcpp using Alt+\:

An alternate method, that will keep everything you entered in the line before calling application:

Key binds like those used in graphic file managers may come handy. The first comes back in directory history (Alt+Left), the second let the user go to the parent directory (Alt+Up). They also display the directory content.

If your terminal emulator supports it, you can set its title from Zsh. This allows dynamically changing the title to display relevant information about the shell state, for example showing the user name and current directory or the currently executing command.

The xterm title is set with the xterm control sequence operating system command \e]2;\a or \e]2;\e\\. For example:

will set the title to

A simple way to have a dynamic title is to set the title in the precmd and preexec hook functions. See zshmisc(1) § Hook Functions for a list of available hook functions and their descriptions.

By using print -P you can additionally take advantage of Zsh's prompt escapes.

Some terminal emulators and multiplexers support setting the title of the tab. The escape sequences depend on the terminal:

See a repository about shell environment detection for tests to detect the shell environment. This includes login/interactive shell, Xorg session, TTY and SSH session.

Use the zsh/net/tcp module:

You can now establish TCP connections:

More details are available in zshmodules(1) § THE_ZSH/NET/TCP_MODULE and zshtcpsys(1).

By default, Ctrl+d will not close your shell if the command line is filled, this fixes it:

pacman includes functionality to search for packages containing a file. The following command-not-found handler will use pacman directly to search for matching packages when an unknown command is executed.

For an alternative using pkgfile, see #pkgfile "command not found" handler.

By default, the clear screen keybinding will not clear the backbuffer (the part you need to scroll up for to see it) on most terminal emulators. A possible solution to this problem is the following.

Fish provides very powerful shell syntax highlighting and autosuggestions. To use both in Zsh, you can install zsh-syntax-highlighting, zsh-autosuggestions, and finally source one or both of the provided scripts from the end of your zshrc, ensuring that zsh-syntax-highlighting is sourced after zsh-autosuggestions [5]:

pkgfile includes a Zsh script file that provides a command_not_found_handler function that will automatically search the pkgfile database when entering an unrecognized command.

You need to source the script to enable it. For example:

For an alternative using pacman's native functionality, see #pacman -F "command not found" handler.

IOT instruction message just means that an application exited with signal 6 (SIGABRT, Signal Abort). The patch is already in upstream (i.e. you can use zsh-gitAUR) and it will be applied in 5.10. For more information, see [6], [7] and signal(7) § Standard signals.

**Examples:**

Example 1 (unknown):
```unknown
$ echo $SHELL
```

Example 2 (unknown):
```unknown
$ autoload -Uz zsh-newuser-install
$ zsh-newuser-install -f
```

Example 3 (unknown):
```unknown
/usr/bin/zsh
```

Example 4 (unknown):
```unknown
~/.bash_profile
```

---

## GNU

**URL:** https://wiki.archlinux.org/title/Info_manual

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## List of applications/Utilities

**URL:** https://wiki.archlinux.org/title/List_of_applications/Utilities

**Contents:**
- Terminal
  - Command shells
  - Terminal emulators
    - VTE-based
    - KMS-based
    - framebuffer-based
  - Terminal pagers
  - Terminal multiplexers
  - Serial terminals
- Files

See the main article: Command-line shell.

See also Wikipedia:Comparison of command shells.

Terminal emulator shows a graphical user interface (GUI) window that contains a terminal. Most emulate xterm, which in turn emulates VT102, which emulates teletypewriter (TTY).

For a comprehensive list, see the List of terminal emulators.

VTE (Virtual Terminal Emulator) is a widget developed during early GNOME days for use in the GNOME Terminal. It has since given birth to many terminals with similar capabilities.

The following terminal emulators are based on the kernel mode setting that could be invoked without X.

In the GNU/Linux world, the framebuffer can refer to a virtual device in the Linux kernel (fbdev) or the virtual framebuffer system for X (xvfb). This section mainly lists the terminal emulators based on the in-kernel virtual device, i.e. fbdev.

See also Wikipedia:Terminal pager.

See also Wikipedia:Terminal multiplexer.

See Working with the serial console#Graphical front-ends.

See also Wikipedia:Comparison of file managers.

Note that some of these twin-panel file managers can also be set to have only one pane.

See Trash management#Trash creation.

This article or section is a candidate for merging with Synchronization and backup programs#Data synchronization.

See also Synchronization and backup programs, Wikipedia:Comparison of file synchronization software, and Wikipedia:Comparison of backup software.

For archiving and compression command-line tools, see Archiving and compression.

See also Wikipedia:Comparison of file comparison tools.

For managing pacnew/pacsave files, specialised tools exist. See Pacnew and Pacsave files#Managing .pac* files.

See diff(1) from diffutils and its alternatives.

Vim and Emacs provide merge functionality with vimdiff and ediff.

See rename(1) from util-linux.

This section lists utilities for file searching based on filename, file path or metadata. For full-text searching, see the next section.

See also Wikipedia:List of search engines#Desktop search engines.

See find(1) from findutils and its alternatives.

These programs index your files to allow for quick searching.

See grep(1) from grep and its alternatives, which provide non-indexed full-text search.

See also Wikipedia:Comparison of revision control software.

See also Wikipedia:List of build automation software.

See also Wikipedia:Comparison of integrated development environments.

For PHP specific list, see PHP#Development tools.

See also D-Bus#Debugging.

Lex and Yacc are part of POSIX.

And then there are also:

These programs provide ready-made user interfaces for alerting the user or prompting for information. These are best suited for writing shell scripts; for more complex use-cases, see #GUI builders.

See also Wikipedia:Comparison of hex editors.

See also Wikipedia:Hex dump.

See also Wikipedia:Literate programming.

See also Wikipedia:List of Unified Modeling Language tools.

See also Git server#Advanced web applications.

See also Wikipedia:List of tools for code review.

See also Wikipedia:List of game engines.

This article or section is a candidate for moving to List of applications/Other#Desktop environments.

See Keyboard shortcuts#Xorg.

See the main article: Input method.

See Partitioning#Partitioning tools.

See File systems#Types of file systems.

See also udisks#Mount helpers.

See S.M.A.R.T.#GUI applications.

See File recovery#List of utilities.

See also Securely wipe disk.

See also Wikipedia:List of tools to create Live USB systems.

See also Category:Monitoring.

See lm_sensors#Graphical front-ends.

See also Wikipedia:Font management software.

See man page#Reading local man pages.

See Time synchronization.

See also Xrandr#Graphical front-ends.

See Backlight#Backlight utilities.

See ICC profiles#Utilities and Backlight#Color correction.

See CUPS#GUI applications.

See Bluetooth#Front-ends.

See Power management#Userspace tools.

See systemd#GUI configuration tools.

See GRUB/Tips and tricks#GUI configuration tools.

See pacman tips#Utilities.

See Libvirt#Client and VirtualBox.

See Wine (Windows) and Darling (MacOS).

**Examples:**

Example 1 (unknown):
```unknown
coredumpctl
```

Example 2 (unknown):
```unknown
drkonqi-coredump-gui
```

Example 3 (unknown):
```unknown
qtlogging.ini
```

Example 4 (unknown):
```unknown
ug --hexdump
```

---

## fzf

**URL:** https://wiki.archlinux.org/title/Fzf

**Contents:**
- Installation
- Configuration
  - Shells
    - Bash
    - Zsh
    - fish
  - Vim
- Arch specific fzf uses
  - Pacman
- Alternatives

fzf is a general-purpose command-line fuzzy finder.

Install the fzf package.

This article or section needs expansion.

Optional fzf keybindings and completion are available for various shells:

Source the desired files from your .bashrc:

From version 0.48 onwards, this can be accomplished with a single line:

The original syntax is still supported and useful for user-customized versions of the scripts.

Source the desired files from your .zshrc (after vi-mode, if using that, too):

From version 0.48 onwards, this can be accomplished with a single line:

For fish, keybindings are in:

fish will source this by default but the bindings have to be enabled manually:

fzf completion in fish can be enabled with custom functions: https://github.com/junegunn/fzf/wiki/Examples-(fish)

The basic Vim plugin is already included within the package and installed to Vim's global plugin directory. Thus, you do not need to add anything to your .vimrc to be able to use it. It only provides the FZF command, though. There is an additional Vim plugin made by the author of fzf that defines some convenience functions, see https://github.com/junegunn/fzf.vim.

Try this to fuzzy-search through all available packages, with package info shown in a preview window, and then install selected packages:

List all your installed packages, and then remove selected packages:

If you want to add package file list in preview – may be a bit slower updating preview window (make sure you run pacman -Fy with root privileges at least once before invocation to sync the pacman file database):

The paruzAUR package also provides a fzf terminal UI for paruAUR and pacman.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/fzf/key-bindings.bash
```

Example 2 (unknown):
```unknown
/usr/share/fzf/completion.bash
```

Example 3 (unknown):
```unknown
eval "$(fzf --bash)"
```

Example 4 (unknown):
```unknown
/usr/share/fzf/key-bindings.zsh
```

---

## Command-line shell

**URL:** https://wiki.archlinux.org/title/Command-line_shell

**Contents:**
- List of shells
  - POSIX compliant
  - Alternative shells
- Changing your default shell
- Uninstalling shell
- Login shell
- Configuration files
  - /etc/profile
  - Standardisation
- Input and output

Shells that are more or less POSIX compliant are listed under #POSIX compliant, while shells that have a different syntax are under #Alternative shells.

These shells can all be linked from /usr/bin/sh. When Bash, mkshAUR and zsh are invoked with the sh name, they automatically become more POSIX compliant.

After installing one of the above shells, you can execute that shell inside of your current shell, by just running its executable. If you want to be served that shell when you login however, you will need to change your default shell.

To list all installed shells, run:

And to set one as default for your user do:

If you are using systemd-homed, run:

where /full/path/to/shell is the full path as given by chsh -l.

If you now log out and log in again, you will be greeted by the other shell.

Change the default shell before removing the package of the shell.

Alternatively, modify the user database.

Use it for every user with a shell other than bash set as their login shell (including root if needed). When completed, the package can be removed.

A login shell is an invocation mode, in which the shell reads files intended for one-time initialization, such as system-wide /etc/profile or the user's ~/.profile or other shell-specific file(s). These files set up the initial environment, which is inherited by all other processes started from the shell (including other non-login shells or graphical programs). Hence, they are read-only once at the beginning of a session, which is, for example, when the user logs in to the console or via SSH, changes the user with sudo or su using the --login parameter, or when the user manually invokes a login shell (e.g. by bash --login).

See #Configuration files and the links therein for an overview of the various initialization files. For more information about login shell, see also Difference between Login Shell and Non-Login Shell? and Why a "login" shell over a "non-login" shell? on Stack Exchange.

To autostart programs in console or upon login, you can use shell startup files/directories. Read the documentation for your shell, or its ArchWiki article, e.g. Bash#Configuration files or Zsh#Startup/Shutdown files.

See also Wikipedia:Unix shell#Configuration files for a comparison of various configuration files of various shells.

Upon login, all Bourne-compatible shells source /etc/profile, which in turn sources any readable *.sh files in /etc/profile.d/: these scripts do not require an interpreter directive, nor do they need to be executable. They are used to set up an environment and define application-specific settings.

It is possible to make (some) shells configuration files follow the same naming convention, as well as supporting some common configuration between the shells.

See the article about this and the related repository. See also xsh.

See also GregsWiki and I/O Redirection.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/sh
```

Example 2 (unknown):
```unknown
$ chsh -s /full/path/to/shell
```

Example 3 (unknown):
```unknown
$ homectl update --shell=/full/path/to/shell user
```

Example 4 (unknown):
```unknown
/full/path/to/shell
```

---

## GNU

**URL:** https://wiki.archlinux.org/title/GNU_toolchain

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## GNU

**URL:** https://wiki.archlinux.org/title/Info

**Contents:**
- Texinfo
- Base system
- Toolchain
  - Build system
- Other software
- See also

Because the GNU kernel—Hurd—is not production-ready , GNU is usually used with the Linux kernel.

Arch Linux is such a GNU/Linux distribution, using GNU software such as the Bash shell, the GNU core utilities —coreutils, the GNU toolchain and numerous other utilities and libraries.

This page does not attempt to list all of the GNU packages, but only highlights some.

GNU software is documented using the Texinfo typesetting syntax. You can view Info documents using the info program, provided by the texinfo package. While most GNU software also provides man pages, the Info documents tend to be more comprehensive. To view an Info document, simply enter:

Most tools of the GNU toolchain are dependencies of the base-devel package, except glibc (required by base) and GDB.

Many other optional GNU tools are available in the official repositories:

**Examples:**

Example 1 (unknown):
```unknown
$ info page_name
```

---

## List of applications

**URL:** https://wiki.archlinux.org/title/List_of_applications

**Contents:**
- Generic software lists
- Software lists of other distributions
- Specialized software lists
- Software forges

This article is a general list of applications sorted by category, as a reference for those looking for packages. Many sections are split between console and graphical applications. Applications listed in "Console" sections can have graphical front-ends, official ones are currently omitted.

The content is split into the following subpages for individual categories (also accessible via the navigation bar at the top of the page and each subpage):

**Examples:**

Example 1 (unknown):
```unknown
pacman -Qql package | grep -Fe .service -e .socket
```

---

## xterm

**URL:** https://wiki.archlinux.org/title/Xterm

**Contents:**
- Installation
- Configuration
  - Resource file settings
    - TERM Environmental Variable
    - UTF-8
    - Make 'Alt' key behave as on other terminal emulators
    - Fix the backspace key
    - Key binding
  - Scrolling
    - Scrollbar

xterm is the standard terminal emulator for the X Window System. It is highly configurable and has many useful and some unusual features.

Install the xterm package.

There are several options you can set in your X resources files that may make this terminal emulator much nicer to use. See xterm(1) § RESOURCES for a complete list.

Allow xterm to report the TERM variable correctly. Do not set the TERM variable from your ~/.bashrc or ~/.bash_profile or similar file. The terminal itself should report the correct TERM to the system so that the proper terminfo file will be used. Two usable terminfo names are xterm and xterm-256color. To set the name, use the resource

You can check the result within xterm using either of these commands:

Ensure that your locale is set up for UTF-8. If you do not use UTF-8, you may need to force xterm to more strictly follow your locale by setting

This is often necessary because XTerm does not support all UTF-8 locales, including eo.UTF-8.

The default Alt key behavior in xterm is a modifier to send eight bit input characters e.g. to insert æ by pressing Alt+f. To make Alt instead send a ^[ (escape) key (as in gnome-terminal and konsole), set

On Arch Linux, xterm sends ^H key when backspace is pressed. This breaks the Ctrl+H key combination on Emacs. The workaround is to send ^? when backspace is pressed by setting the resources

xterm defines a whole suite of "actions" for manipulating the terminal e.g. copy-selection(), hard-reset(), scroll-back(), etc. These actions can be mapped to mouse/key combinations using the translations resource. For example, you can map Ctrl+M and Ctrl+R to maximize/restore the window:

#override indicates that these bindings should override any existing ones (you almost always want this for custom key bindings). Each binding must be separated by the escape sequence \n. If you want to insert a literal newline, it also needs to be escaped (hence \n\). See xterm(1) § KEY_BINDINGS for the full list of actions and many examples.

As new lines are written to the bottom of the xterm window, older lines disappear from the top. To scroll up and down through the off-screen lines one can use the mouse wheel, the key combinations Shift+PageUp and Shift+PageDown, or the scrollbar.

By default, 1024 lines are saved. You can change the number of saved lines with the saveLines resource:

Other X resources that affect scrolling are jumpScroll, multiScroll, and fastScroll (all under XTerm.vt100, see xterm(1) § VT100 Widget Resources). To scroll inside an alternate screen, set alternateScroll to true.

The scrollbar is not shown by default. It can be enabled and its appearance tweaked through resource settings (note the differing capitalization of "scrollbar"!)

See xterm(1) § Scrollbar Resources for other scrollbar resources.

The scrollbar operates differently from what you may be accustomed to using.

xterm is compiled with the toolbar, or menubar, disabled. The menus are still available as popups when you press Ctrl+MouseButton within the xterm window. The actions invoked by the menu items can often be accomplished using command line options or by setting resource values.

Some of the menu options are discussed below.

Opens with Ctrl+LeftMouse:

Opens with Ctrl+MiddleMouse:

Opens with Ctrl+RightMouse:

Opens from the Tek Window with Ctrl+MiddleMouse.

The first section's options allow you to change the Tek window font size. The second set of options are used to move the focus between the Tek emulation window and the main, or VT, window and to close or hide the Tek window.

First, highlighting text using the mouse in an xterm (or alternatively another application) will select the text to copy, then clicking the mouse middle-button will paste that highlighted text. The key combination Shift+Insert will paste highlighted text (but not in all applications).

See Clipboard#Selections for the terminology and general information.

This article or section needs expansion.

By default, xterm copies highlighted text into a buffer called the PRIMARY selection where the text is immediately replaced by a new PRIMARY selection as soon as another piece of text is highlighted. The PRIMARY selection can be pasted in xterm by pressing the middle-mouse button or Shift+Insert.

The CLIPBOARD selection is used for explicit copy/paste commands, e.g. via the shortcuts Ctrl+c, Ctrl+x, or Ctrl+v.

xterm allows users to switch between using PRIMARY or CLIPBOARD using Select to Clipboard on the #VT Options menu, or with the XTerm.vt100.selectToClipboard resource.

With the above setting you can select if you want to use PRIMARY or CLIPBOARD, but you can also hack it to add the selection to both. Just override the #Key binding for releasing the left mouse button:

You can add key bindings similar to other terminals' copy/paste behavior (such as gnome terminal):

The new user usually discovers that text may be selected using a "click-and-drag" with the left mouse button. Double-clicking will select a word, where a word is defined as consecutive alphabetic characters plus the underscore, or the Basic Regular Expression (BRE) [A-Za-z_]. Triple-clicking selects a line, with a "tab" character usually copied as multiple "space" characters.

Another way of selecting text, especially useful when copying more than one full screen, is:

You can clear any selected text by left-clicking once, anywhere within the xterm window.

When a character-based application runs inside xterm, it is allowed to receive mouse events. This may be a problem if the program can not communicate with the X11 clipboard. In order to pass these events to the underlying xterm, they must be accompanied by the Shift key. For example, in links (not xlinks -g), one can mouse-click on URLs and menu items, but not select or paste with a middle button. To do copy-paste, press the Shift key and then perform mouse clicks (the key needs to be pressed only during the click, so there is no need to hold it when dragging mouse to select, for instance, a text block).

xterm defaults to black text, the foreground color, on a white background. The foreground and background colors can be reversed by setting the resource

Alternatively, you can directly change the foreground and background colors (as well as the first sixteen terminal colors) using resources:

Some colors can be specified by assigned names. If emacs or vim has been installed, you can examine /usr/share/emacs/*/etc/rgb.txt or /usr/share/vim/*/rgb.txt to view the list of color names with their decimal RGB values. Colors may also be specified using hexadecimal RGB values with the format rgb:RR/GG/BB, or the older and not encouraged syntax #RRGGBB.

The color PapayaWhip is the same as rgb:ff/ef/d5, which is the same as #ffefd5.

Many suggestions for color schemes can be viewed in the forum thread, Terminal Colour Scheme Screenshots.

xterm's default font is the bitmap font named by the X Logical Font Description alias fixed, often resolving to

This font, also aliased to the name 6x13, has remakably wide coverage for unicode glyphs. The default "TrueType" font is the 14‑point font matched by the name mono. The FreeType font that will be used can be found with this command:

Fonts can be specified in your resources, depending on whether the font is TrueType or not:

To test, you can also set the font on the command line: -fa for faceName, -fn for font. If you set both kinds of fonts, you can alternate between the two by toggling TrueType Fonts from the #VT Fonts menu. You can also choose the default with the following resource

Italic fonts are shown as underlined characters when using XLFD names in xterm. TrueType fonts should use an oblique typeface.

If you do not specify a bold font at the command line, -fb, or through the XTerm.vt100.boldFont resource, xterm will attempt to find a bold font matching the normal font. If a matching font is not found, the bold font will be created by "overstriking" the normal font.

Many fonts do not contain glyphs for the double width Chinese, Japanese and Korean languages. Other terminal emulators such as urxvt may be better suited if you frequently work with these languages.

Using bitmapped XLFD fonts with CJK has many pitfalls in xterm. It is much easier to use TrueType fonts for CJK display, using the faceNameDoublesize resource. This example uses DejaVu Sans Mono as the normal font and WenQuanYi WenQuanYi Bitmap Song as the double width font:

Install a transset package, such as transset-dfAUR or xorg-transsetAUR, and a composite manager such as Xcompmgr. Then add the following line to your ~/.bashrc:

Now, each time you launch a shell in an xterm and a composite manager is running, the xterm window will be transparent. The test in front of transset-df keeps it from executing if XTERM_VERSION is not defined. Note that your terminal will not be transparent if you launch a program other than a shell this way. It is probably possible to work around this if you want the functionality.

Also see Per-application transparency.

To make the bell character notify the window manager of urgency, set:

When using small font sizes, bold or italic characters may be difficult to read. One solution is to turn off bolding and underlining or italics and use color instead. This example does just that:

See #Colors for formatting information.

Lines of text can sometimes be too close together, or they may appear to be too widely spaced. For one example, using DejaVu Sans Mono, the low underscore glyph may butt against CJK glyphs or the cursor block in the line below. Line spacing, called leading by typographers, can be adjusted with the following resource, for example to widen the spacing:

Valid values for range from 0.9 to 1.5, with 1.0 being the default.

If you have plotutils installed, you can use xterm's Tektronix 4014 emulation to view some of the plotutils package's test files. Open the Tek window from the #VT Options menu menu item Switch to Tek Mode or start a new xterm instance using this command:

Your PS1 prompt will not render correctly, if it appears at all. In the new window, enter the command,

A world map will appear in the Tek window. You can also view other *.tek files from that same directory. To close the Tek window, one can use the xterm menus.

It can be inconvenient to activate Secure Keyboard mode from the #Main Options menu. You can instead invoke the secure() action with a #Key binding:

Rebuild xterm using ABS and include the --enable-double-buffer flag:

See Xterm modifications for details.

Some applications, such as i3, call uxterm wrapper instead of xterm. This can be resolved by adding the same configurations for uxterm, such as:

If you prefer to not having duplicate entries in the configuration file, wildcard matching can be used:

If you have issues with changing the font size, install the xorg-mkfontscale package.

**Examples:**

Example 1 (unknown):
```unknown
~/.bash_profile
```

Example 2 (unknown):
```unknown
XTerm.termName: xterm-256color
```

Example 3 (unknown):
```unknown
$ echo $TERM
$ tset -q
```

Example 4 (unknown):
```unknown
XTerm.vt100.locale: true
```

---
