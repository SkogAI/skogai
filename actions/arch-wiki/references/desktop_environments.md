# Arch-Wiki - Desktop Environments

**Pages:** 71

---

## Window manager

**URL:** https://wiki.archlinux.org/title/Window_managers

**Contents:**
- Overview
  - Types
- List of window managers
  - Stacking window managers
  - Tiling window managers
  - Dynamic window managers
- See also

It can be part of a desktop environment or be used standalone.

Window managers are X clients that control the appearance and behaviour of the frames ("windows") where the various graphical applications are drawn. They determine the border, title bar, size, and ability to resize windows, and often provide other functionality such as reserved areas for sticking dockapps like Window Maker, or the ability to tab windows like Fluxbox. Some window managers are even bundled with simple utilities like menus to start programs or to configure the window manager itself.

The Extended Window Manager Hints specification is used to allow window managers to interact in standard ways with the server and the other clients.

Some window managers are developed as part of a more comprehensive desktop environment, usually allowing the other provided applications to better interact with each other, giving a more consistent experience to the user, complete with features like desktop icons, fonts, toolbars, wallpapers, or desktop widgets.

Other window managers are instead designed to be used standalone, giving the user complete freedom over the choice of the other applications to be used. This allows the user to create a more lightweight and customized environment, tailored to their own specific needs. "Extras" like desktop icons, toolbars, wallpapers, or desktop widgets, if needed, will have to be added with additional dedicated applications.

Some standalone window managers can be also used to replace the default window manager of a desktop environment, just like some desktop environment–oriented window managers can be used standalone too.

Prior to installing a window manager, a functional X server installation is required. See Xorg for detailed information.

See Comparison of tiling window managers and Wikipedia:Comparison of X window managers for comparison of window managers.

---

## MATE

**URL:** https://wiki.archlinux.org/title/MATE

**Contents:**
- Installation
  - MATE applications
  - Additional MATE packages
- Starting MATE
- Configuration
  - Accessibility
  - Notifications
- Tips and tricks
  - Disabling compositing
  - Disabling new window centering

MATE can be installed with one of the following:

The base desktop consists of marco, mate-panel and mate-session-manager.

MATE is largely composed of GNOME 2 applications and utilities, forked and renamed to avoid conflicting with their GNOME 3 counterparts. Below is a list of common GNOME applications which have been renamed in MATE.

Other applications and core components prefixed with GNOME (such as GNOME Terminal, GNOME Panel, GNOME Menus, etc.) have had the prefix changed to MATE so they become MATE Panel, MATE Menus etc.

There are a number of other unofficial MATE applications that are contributed to and maintained by the MATE community and therefore not included in the mate or mate-extra groups.

Additional packages need to be installed to take advantage of some of Caja's advanced features - see File manager functionality.

Choose MATE from the menu in a display manager of choice.

Alternatively, to start MATE with startx, append exec mate-session to your ~/.xinitrc file.

MATE can be configured with its Control Center application (mate-control-center) provided by the mate-control-center package. To manage some hardware, you may need to install additional tools.

MATE is well suited for use by individuals with sight or mobility impairment. Install orca, espeakAUR (Screen reader for individuals who are blind or visually impaired) and onboard (On-screen keyboard useful for mobility impaired users)

Before starting MATE for the first time, enter the following command as the user who needs accessibility features:

Once you start MATE, you can configure the accessibility applications via System > Preferences > Assistive Technologies, although if you need Orca, you will need to run it from the Alt-F2 run window in order to start getting speech.

To disable the notification on battery discharge, run:

See Backlight#Kernel command-line options.

Compositing is enabled by default. To disable it, navigate to Look and Feel > Windows > General in the System Preferences and tick the box alongside Enable software compositing window manager. Alternatively, you can run the following from the terminal:

By default, new windows are placed in the center. To disable centering new windows, navigate to run Windows > Placement in the System Preferences and tick the box alongside Center new windows. Alternatively, you can run the following from the terminal:

Window snapping is enabled by default. To disable it, navigate to run Windows > Placement in the System Preferences and tick the box alongside Enable window tiling. Alternatively, you can run the following from the terminal:

Hiding the decorations of maximized windows is possible with the use of mate-tweakAUR tool; after installation navigate to Look and Feel > MATE Tweak > Windows in the System Preferences and enable Undecorate maximized windows in the Window Behaviour section.

By default, MATE shows multiple icons on the desktop: the content of your desktop directory, computer, home and network directories, the trash and mounted drives. You can show or hide them individually or all at once using gsettings.

Doing so may cause some graphics artifacts on secondary monitors.

Hide user directory icon:

Hide mounted volumes:

Replace false with true for the icons to reappear.

The marco window manager can be replaced with another window manager via either of the following methods:

Execute the following to specify a different window manager for MATE:

You can autostart a window manager of your choice using mate-session-properties. This means that the autostarted window manager will replace the default window manager at login. Navigate to Startup Applications in the System Preferences. In the dialog click Add. The command should take the syntax wm-name --replace.

To prevent Caja from managing the desktop, execute the following:

You can change the button order using the graphical dconf-editor or the gsettings command line tool:

and put menu, close, minimize and maximize in your desired order, separated by commas. The colon is used to specify on which side of the titlebar the window buttons will appear and must be used for the changes to apply.

By default, MATE automatically opens a new file manager window when a drive is mounted. To disable this:

And to disable automounting:

To ensure that each new folder opens in a new window (known as spatial view), open Caja's preferences dialog, click on the behaviour tab and tick the 'Open each folder in its own window' option. Alternatively, execute the following command which achieves the same effect:

You can alter the DPI (dots per inch) of the fonts in MATE by right-clicking on the desktop and choosing Change desktop background > Fonts > Details > Resolution.

By default, the applications menu icon is set to start-here. To use a different icon, copy your icon to a folder such as /usr/local/share/pixmaps and execute the following:

where icon is the name of your icon. Do not include the file extension in the icon name. Finally, restart MATE Panel.

To adjust the amount of time it takes for the panel to disappear or reappear when autohide is enabled, execute the following:

where panel is either top or bottom and time is a value in miliseconds, e.g. 300.

To set the speed at which panel animations occur, execute the following:

where panel is either top or bottom and value is either "'fast'", "'medium'" or "'slow'".

The caja-open-terminal extension uses GSettings to determine which terminal to use - mate-terminal is the default. To change the terminal that will be used, run the following command

where my-terminal is the name of the terminal executable to be launched, for example: xterm.

Some software may have issues rendering graphics when working on an environment using the NVIDIA proprietary drivers and a compositing window manager.

To easily toggle the compositing feature, save the following script somewhere within the Home directory:

and then create a custom keyboard shortcut that executes the file, e.g. Ctrl+Alt+C, to sh ~/.scripts/compositing.sh.

Mate's window manager, marco, supports tear-free software compositing via DRI3/Xpresent. [1]

If your graphics driver does not support DRI3 (e.g. the Nvidia Proprietary driver), marco does not support vertical synchronization via OpenGL, which may cause video tearing with enabled compositing. [2] In this case, consider a different composite manager with OpenGL support such as picom.

See Cursor themes#Desktop environments.

If you wish to use the default MATE (1.8) Stripes background as the LightDM background as well so as to make for seamless transition from LightDM to MATE, you will find that it is runtime-constructed from a grayscale PNG upon which MATE layers a vertical blue-to-green gradient, something which LightDM does not currently support. If insistent, you can work around this by temporarily setting /org/mate/desktop/background/show-desktop-icons to false, either through the dconf-editor tool available from the System Tools menu or by running

from the Alt-F2 Run Application dialog, then running killall mate-panel from said dialog and hitting Print Screen before the panel reappears. You are then presented with a Save As dialog for exactly that fully rendered, screen-sized PNG that you need for LightDM. Run

to have your desktop icons reappear, if desired.

Due to a race condition, the panel shadow does not appear after logging in to the MATE desktop, even with compositing enabled. [3]

Copy /usr/share/applications/marco.desktop and add a delay:

If this has no effect, increase the delay duration.

When logging out or shutting down, you may find that you are presented with an A program is still running: at-spi-registryd.desktop popup. As a workaround, you can prevent at-spi-registryd from starting - see GTK#Suppress warning about accessibility bus - though this may have an effect on some accessibility features.

Since the migration to GTK 3 this feature is not working.[4]

Themes that come with mate-themes need optional dependencies gtk-enginesAUR and gtk-engine-murrineAUR for GTK 2 themes to function properly.

An extra decoration can appear on CSD applications (Firefox, Visual Studio Code...) when they are unmaximized.[5]

Uninstalling the package mate-netbook solves the issue.

When multiple keyboard layouts are enabled, a layout selection icon is displayed in the system tray. Because of a bug ([6]), depending on the currently used theme, it sometimes happens to be displayed with white font on bright background (or in some other barely legible configuration, such as with green font).

This issue can be worked around by manually setting the font color (e.g., '0 0 0' for black):

**Examples:**

Example 1 (unknown):
```unknown
exec mate-session
```

Example 2 (unknown):
```unknown
$ gsettings set org.mate.interface accessibility true
```

Example 3 (unknown):
```unknown
$ gsettings set org.mate.power-manager notify-discharging false
```

Example 4 (unknown):
```unknown
$ gsettings set org.mate.Marco.general compositing-manager false
```

---

## river

**URL:** https://wiki.archlinux.org/title/River

**Contents:**
- Installation
- Starting
  - Manually
  - From TTY
  - Display manager
- Configuration
  - Keyboard layout
  - Touchpad examples
  - Window rules
- Usage

river is a wlroots-based Wayland dynamic tiling compositor, inspired by, but not based on dwm, xmonad and bspwm. Configuration is by an external executable file.

Its declared design goals are:

River is installed with the river package.

A single executable file is used as a configuration file. No initialisation file is set up for the user by default, so no keybindings or default applications are available until an init file is created. Note that this includes the exit keybinding, so set up in tty or another desktop environment before running river.

An example config init file is available in /usr/share/river/example/. Copy this as ~/.config/river/init and ensure it is executable.

Enter river (exits to tty with user still logged in) or exec river (more securely exits to tty with user logged out)

River can be autostarted in a similar manner to startx, by setting up the environment variable checks in .bash_profile or the equivalent file for other shells. See Xinit#Autostart X at login, replacing $DISPLAY with $WAYLAND_DISPLAY, and running exec river.

River does not officially support display managers but many will work with no or minimal effort. A session entry is installed by default in /usr/share/wayland-sessions/.

The configuration file can be a shell script or executable program, comprising a list of riverctl individual commands which define key bindings, input settings and window rules. It is executed once at start-up but can be re-run like any other shell script (consider the effects of duplicating any autostarted spawned actions). Each setting can also be run individually by simply running the relevant riverctl line in a terminal. This allows temporary override of the init settings, dynamic updates and testing new settings.

For example, to map the shortcut Super+PrtSc to take a screenshot with the application grim and display a temporary desktop notification:

The spawn command can launch any application or script but expects a single word argument. Quote any longer expressions.

Multiple layouts can be entered as a comma-separated list, e.g. gb,fr.

Variables and other shell constructs can be used: mod='Mod4', set term foot, etc, as per your shell.

Certain touchpad behaviour and focus preferences are available.

Exact keyboard, mouse and touchpad models for use in these settings can be identified using:

It is sometimes desirable to set certain windows to be non-tiling by default. Floating windows can be defined by class or title:

Use riverctl spawn without a keybinding to launch any executable at startup, for example:

River does not define any scratchpads by default, but these can be set up on any tag beyond the default 0-9. First, define the tag number, then the key mapping to move an application to the scratchpad tag and toggle its appearance, and, finally, prevent new windows being assigned to the scratchpad.

River supports modes for key mapping, which allows for reuse of mappings, and combinations of fewer keys. There are two default modes of 'normal' and 'locked' (defining allowed key mappings when the screen is locked). Custom modes can be added. Eg. if floating windows are rarely used, the key mapping to manipulate those windows can be defined in a 'float' mode. Entry and exit key mappings for the mode are set as the first and last mappings, with other mapping between these.

Note that floating window modifiers also work on tiled windows, making them floating and giving potentially unpredictable layouts.

In common with many other Wayland minimalist tiling clients, other tools are not included. Example external bars, screenshot tools, launchers, etc. are listed in the River wiki, including several with River-specific functionality.

If Screencasting is not working with river, check if the needed environment variables are properly set for systemd:

You should find something like:

If any of these variables are not set, you may add this to your .config/river/init:

If you need further troubleshooting, try to:

Contrary to what you may find in older posts in the internet, it is not necessary to install pipewire-media-session, since wireplumber is working just fine now.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/river/example/
```

Example 2 (unknown):
```unknown
~/.config/river/init
```

Example 3 (unknown):
```unknown
.bash_profile
```

Example 4 (unknown):
```unknown
$WAYLAND_DISPLAY
```

---

## KDE

**URL:** https://wiki.archlinux.org/title/KWin

**Contents:**
- Installation
  - Plasma
  - Plasma Mobile
  - KDE applications
  - Unstable releases
- Starting Plasma
  - Using a display manager
  - From the console
- Configuration
  - Personalization

KDE is a software project currently comprising a desktop environment known as Plasma, a collection of libraries and frameworks (KDE Frameworks) and several applications (KDE Applications) as well.

KDE upstream has a well maintained UserBase wiki. Detailed information about most KDE applications can be found there.

Install the plasma-meta meta-package or the plasma group. For differences between plasma-meta and plasma reference Package group. Alternatively, for a more minimal Plasma installation, install the plasma-desktop package. Upstream KDE has package and setup recommendations to get a fully-featured Plasma session.

If you are an NVIDIA user with the proprietary nvidia driver and wish to use the Wayland session, enable the DRM kernel mode setting.

Install plasma-mobileAUR.

To install the full set of KDE Applications, install the kde-applications-meta meta-package or the kde-applications group. If you only want KDE applications for a certain category, like gaming or education, install the relevant dependency of kde-applications-meta. Note that installing applications alone will not install any version of Plasma.

See Official repositories#kde-unstable for beta releases.

Starting from Plasma 6.4, the Wayland session has matured enough to become the default and preferred one: the X11 session is only available separately with the plasma-x11-session package[1]. The Xorg session is still supported, but will be removed in Plasma 7. See Wayland Known Significant Issues and X11 Known Significant Issues for more information.

Plasma can be started either using a display manager, or from the console.

Most settings for KDE applications are stored in ~/.config/. However, configuring KDE is primarily done through the System Settings application. It can be started from a terminal by executing systemsettings.

There are different types of KDE themes, varying by scope of what they modify:

For easy system-wide installation and updating, some themes are available in both the official repositories and the AUR.

Global themes can also be installed through System Settings > Colors & Themes > Global Theme > Get New....

The recommended theme for a pleasant appearance in GTK applications is breeze-gtk, a GTK theme designed to mimic the appearance of Plasma's Breeze theme. Install kde-gtk-config (part of the plasma group), relogin and select Breeze as the GTK theme in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style....

This article or section is out of date.

In some themes, tooltips in GTK applications have white text on white backgrounds making it difficult to read. To change the colors in GTK2 applications, find the section for tooltips in the .gtkrc-2.0 file and change it. For GTK3 application two files need to be changed, gtk.css and settings.ini.

Some GTK2 programs like vuescan-binAUR still look hardly usable due to invisible checkboxes with the Breeze or Adwaita skin in a Plasma session. To workaround this, install and select e.g. the Numix-Frost-Light skin of the numix-frost-themesAUR under System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style... > GTK theme. Numix-Frost-Light looks similar to Breeze.

Plasma and SDDM will both use images found at /var/lib/AccountsService/icons/ as users' avatars. To configure with a graphical interface, you can use System Settings > Users. The file corresponding to your username can be removed to restore the default avatar.

Plasmoids are widgets for Plasma desktop shell designed to enhance the functionality of desktop, they can be found on the AUR.

Plasmoid scripts can also be installed by right-clicking onto a panel or the desktop and choosing Enter Edit Mode > Add Widgets... > Get New Widgets... > Download New Plasma Widgets. This will present a front-end for https://store.kde.org/ that allows you to install, uninstall, or update third-party Plasmoid scripts with just one click.

Install plasma-pa or kmix (start Kmix from the Application Launcher). plasma-pa is now installed by default with plasma, no further configuration needed.

As the Plasma panel is on top of other windows, its shadow is drawn over them. [5] To disable this behaviour without impacting other shadows, install xorg-xprop and run:

then select the panel with the plus-sized cursor. [6] For automation, install xorg-xwininfo and create the following script:

Make the script executable.

The factual accuracy of this article or section is disputed.

The script can be run on login with Add Login Script in Autostart:

See HiDPI#KDE Plasma.

The plasma-phone-settings repository contains several recommended settings which can be applied globally (/etc/xdg) and/or per user (~/.config).

/etc/xdg/kscreenlockerrc (or ~/.config/kscreenlockerrc) locks the screen immediately after login. [7] This is useful in combination with SDDM#Autologin.

To use a virtual keyboard in the Wayland session, install maliit-keyboard and enable it in System Settings > Keyboard > Virtual Keyboard.

If your device has a hardware keyboard, but you want to use the virtual keyboard, add the KWIN_IM_SHOW_ALWAYS=1 environment variable to your Wayland session.

To use a virtual keyboard in the X11 session, choose an appropriate one from List of applications/Utilities#On-screen keyboards and run it manually.

Window decorations can be found in the AUR.

They can be changed in System Settings > Colors & Themes > Window Decorations, there you can also directly download and install more themes with one click.

Icon themes can be installed and changed on System Settings > Colors & Themes > Icons.

The Plasma Netbook shell has been dropped from Plasma 5, see the following KDE forum post. However, you can achieve something similar by editing the file ~/.config/kwinrc adding BorderlessMaximizedWindows=true in the [Windows] section.

To allow thumbnail generation for media or document files on the desktop and in Dolphin, install kdegraphics-thumbnailers and ffmpegthumbs.

Then enable the thumbnail categories for the desktop via right click on the desktop background > Configure Desktop and Wallpaper... > Icons > Configure Preview Plugins....

In Dolphin, navigate to Configure > Configure Dolphin... > Interface > Previews.

Plasma provides a Redshift-like feature (working on both Xorg and Wayland) called Night Light. It makes the colors on the screen warmer to reduce eye strain at the time of your choosing. It can be enabled in System Settings > Colors & Themes > Night Light.

You can also configure printers in System Settings > Printers. To use this method, you must first install the following packages print-manager, cups, system-config-printer. See CUPS#Configuration.

The Dolphin share functionality requires the package kdenetwork-filesharing and usershares, which the stock smb.conf does not have enabled. Instructions to add them are in Samba#Enable Usershares, after which sharing in Dolphin should work out of the box after restarting Samba.

Accessing Windows shares from Dolphin works out of the box. Use the path smb://servername/share to browse the files.

Unlike GTK file browsers which utilize GVfs also for the launched program, opening files from Samba shares in Dolphin via KIO makes Plasma copy the whole file to the local system first with most programs (VLC is an exception). To workaround this, you can use a GTK based file browser like thunar with gvfs and gvfs-smb (and gnome-keyring for saving login credentials) to access SMB shares in a more able way.

Another possibility is to mount a Samba share via cifs-utils to make it look to Plasma like if the SMB share was just a normal local folder and thus can be accessed normally. See Samba#Manual mounting and Samba#Automatic mounting.

A GUI solution is available with samba-mounter-gitAUR, which offers basically the same functionality via an easy to use option located at System Settings > Network Drivers. However, it might break with new KDE Plasma versions.

KDE Desktop Activities are special workspaces where you can select specific settings for each activity that apply only when you are using said activity.

Install powerdevil for an integrated Plasma power managing service. This service offers additional power saving features, monitor brightness control (if supported) and battery reporting including peripheral devices.

The factual accuracy of this article or section is disputed.

Plasma can autostart applications and run scripts on startup and shutdown. To autostart an application, navigate to System Settings > Autostart and add the program or shell script of your choice. For applications, a .desktop file will be created, for login scripts, a .desktop file launching the script will be created.

See official documentation.

Phonon is being widely used within KDE, for both audio (e.g., the System notifications or KDE audio applications) and video (e.g., the Dolphin video thumbnails). It can use the following backends:

KDE recommends only the VLC backend, as the GStreamer backend is unmaintained.

Plasma stores personalized desktop settings as configuration files in the XDG_CONFIG_HOME folder. Use the detail of configuration files to select and choose a method of backup and restore.

Plasma uses a systemd user instance to launch and manage all the Plasma services. This is the default startup method since Plasma 5.25, but can be disabled to use boot scripts instead with the following command (however this may stop working in a future release):

More details about the implementation can be read in Edmundson's blog: Plasma and the systemd startup.

KDE applications use sonnet for spell checking. See its optional dependencies for the supported spell checkers.

Configure it in System Settings > Spell Check.

See https://community.kde.org/Plasma/Wayland/Nvidia.

The KDE project provides a suite of applications that integrate with the Plasma desktop. See the kde-applications group for a full listing of the available applications. Also see Category:KDE for related KDE application pages.

Aside from the programs provided in KDE Applications, there are many other applications available that can complement the Plasma desktop. Some of these are discussed below.

Navigate to the submenu System Settings > Keyboard > Advanced (tab) > Key sequence to kill the X server and ensure that the checkbox is ticked.

KCM stands for KConfig Module. KCMs can help you configure your system by providing interfaces in System Settings, or through the command line with kcmshell6.

More KCMs can be found at linux-apps.com.

KDE implements desktop search with a software called Baloo, a file indexing and searching solution.

The following web browsers can integrate with Plasma:

KDE offers its own stack for personal information management (PIM). This includes emails, contacts, calendar, etc. To install all the PIM packages, you could use the kde-pim package group or the kde-pim-meta meta package.

Akonadi is a system meant to act as a local cache for PIM data, regardless of its origin, which can be then used by other applications. This includes the user's emails, contacts, calendars, events, journals, alarms, notes, and so on. Akonadi does not store any data by itself: the storage format depends on the nature of the data (for example, contacts may be stored in vCard format).

Install akonadi. For additional addons, install kdepim-addons.

By default Akonadi will use /usr/bin/mysqld (MariaDB by default, see MySQL for alternative providers) to run a managed MySQL instance with the database stored in ~/.local/share/akonadi/db_data/.

Akonadi supports using the system-wide MySQL for its database.[10]

This article or section needs expansion.

Akonadi supports either using the existing system-wide PostgreSQL instance, i.e. postgresql.service, or running a PostgreSQL instance with user privileges and the database in ~/.local/share/akonadi/db_data/.

Install postgresql and postgresql-old-upgrade.

Edit the Akonadi configuration file so that it has the following contents:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

This requires an already configured and running PostgreSQL.

Create a PostgreSQL user account for your user:

Create a database for Akonadi:

Edit the Akonadi configuration file to match the configuration below:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

To use SQLite, edit the Akonadi configuration file to match the configuration below:

Users who want to disable Akonadi would need to not start any KDE applications that rely on it. See this section in the KDE userbase for more information.

KDE Connect provides several features to connect your Android or iOS phone with your Linux desktop:

You will need to install KDE Connect both on your computer and on your phone. For PC, install kdeconnect package. For Android, install KDE Connect from Google Play or from F-Droid. If you want to browse your phone's filesystem, you need to install sshfs as well and configure filesystem exposes in your Android app. For iOS, install KDE Connect from the App Store. Not all features from the Android version are available on the iOS version.

To use remote input functionality on a Plasma Wayland session, the xdg-desktop-portal package is required.

It is possible to use KDE Connect even if you do not use the Plasma desktop. For GNOME users, better integration can be achieved by installing gnome-shell-extension-gsconnectAUR instead of kdeconnect. To start the KDE Connect daemon manually, execute /usr/bin/kdeconnectd.

If you use a firewall, you need to open UDP and TCP ports 1714 through 1764.

Sometimes, KDE Connect will not detect a phone. You can restart the services by running killall kdeconnectd and then opening kdeconnect in system settings or running kdeconnect-cli --refresh followed by kdeconnect-cli -l. You can also use Pair new device > Add devices by IP on KDE Connect for Android.

It is possible to use a window manager other than KWin with Plasma. This allows you to combine the functionality of the KDE desktop with the utility of a tiling window manager, which may be more fleshed out than KWin tiling scripts.

The component chooser settings in Plasma no longer allows changing the window manager, but you are still able to swap KWin via other methods.

Since KDE 5.25, Plasma's systemd based startup is enabled by default.

To replace KWin in this startup, you must first mask the plasma-kwin_x11.service for the current user to prevent it from starting.

Then, create a new systemd user unit to start your preferred WM [11]:

To use it, do (as user units) a daemon-reload, make sure you have masked plasma-kwin_x11.service then enable the newly created plasma-custom-wm.service.

Plasma's script-based boot is used by disabling #systemd startup. If you have done so, you can change the window manager by setting the KDEWM environment variable before Plasma is invoked.

This article or section is a candidate for merging with Environment variables#Globally.

If you have root access, you can also add an XSession that will be available to all users as an option on the login screen.

First, create a script with execution permissions as follows:

Replace /usr/bin/i3 to the path to your preferred WM. Ensure the path is correctly set. If KDE is unable to start the window manager, the session will fail and the user will be returned to the login screen.

Then, to add an XSession, add a file in /usr/share/xsessions/ with the following content:

The openbox package provides a session for using KDE with Openbox. To make use of this session, disable #systemd startup and select KDE/Openbox from the display manager menu.

For those starting the session manually, add the following line to your xinit configuration:

A list of KWin extensions that can be used to make KDE behave more like a tiling window manager.

To enable display resolution management and multiple monitors in Plasma, install kscreen. This provides additional options to System Settings > Display & Monitor.

On X11, ICC profiles are handled by colord. To configure them in Plasma, install colord-kde. This provides additional options in System Settings > Color Management. ICC profiles can be imported using Import Profile.

For Wayland sessions, color management is handled by the compositor, i.e. KWin for Plasma. In this case, no additional package is required. The color profile can be configured per monitor in System Settings > Display & Monitor > Color Profile.

HDR support is experimental and only works in a Wayland session. System Settings > Display & Monitor > High Dynamic Range > Enable HDR.

For more information on displaying HDR content see HDR monitor support. Development details about HDR in Plasma can be found on Xaver Hugl's blog post.

When enabling HDR mode in KDE Plasma, SDR content can appear extremely dark, sometimes making the screen nearly unreadable. To address this, KDE provides two key sliders in display settings: Maximum SDR Brightness, which adjusts the brightness mapping for SDR content in HDR mode, and Brightness which controls the overall display backlight or luminance

To disable this feature, you currently have to edit the kwinrc config file and set the Meta key under ModifierOnlyShortcuts to an empty string:

Alternatively, you can also run the following command:

With the Plasma Browser integration installed, KDE will show bookmarks in the application launcher.

To disable this feature, go to System Settings > Search > Plasma Search and uncheck Bookmarks.

IBus is an input method framework and can be integrated into KDE. See IBus#Integration for details.

Using IBus may be required when using KDE on Wayland to offer accented characters and dead keys support [12].

See NetworkManager#Sharing internet connection over Wi-Fi.

If you have System Settings > Session > Desktop Session > Session Restore > On login, launch apps that were open: On last logout (default) selected, ksmserver (KDE's session manager) will automatically save/load all open applications to/from ~/.config/ksmserverrc on logout/login.

If you have set up local mail delivery with a mail server that uses the Maildir format, you may want to receive this mail in KMail. To do so, you can re-use KMail's default receiving account "Local Folders" that stores mail in ~/.local/share/local-mail/.

Symlink the ~/Maildir directory (where Maildir format mail is commonly delivered) to the Local Folders' inbox:

Alternatively, add a new receiving account with the type Maildir and set ~/Maildir as its directory.

Edit config/main.xml files in the /usr/share/plasma. For example, to configure the Application Launcher for all users, edit /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml. To prevent the files from being overwritten with package updates, add the files to Pacman's NoUpgrade

This article or section is a candidate for merging with Power management.

Properly disable the hibernate feature and hide it from the menu with a Polkit policy rule.

Alternatively, add the following lines to a file in /etc/systemd/sleep.conf.d/:

Kwin has the ability to specify rules for specific windows/applications. For example, you can force enable the window titlebar even if the application developer decided that there should not be one. You can set such rules as specific starting position, size, minimize state, keeping above/below others and so on.

To create a rule you can press Alt+F3 when the window of interest is in focus. Then, in More Actions > Configure special application/window settings, you can set the desired property. A list of created rules is available from System Settings > Window Management > Window Rules.

By default KDE mount manager (kio-fuse) will mount network shares to ${XDG_RUNTIME_DIR}/kio-fuse-6-char-random-string.

Create directory, e.g. mnt_kio in your home directory:

Override default kio-fuse.service using a drop-in file:

Now if you mount your network shares via dbus or by openning some file from remote share in Dolphin:

They will be mounted to ~/mnt_kio.

To have the menu bar integrated with the title bar, install material-kwin-decoration-gitAUR from the AUR, then in System Settings > Window Decorations, select 'Material' and add the Application Menu button to the title bar (preferably as second from the left). Works only on X11 session.

Xdg-desktop-portal-kde has support for remote input from a remote desktop session, a virtual KVM switch, kde-connect, emulated devices like a controller using steam-input, etc. This authorization is lost after the application or the desktop-portal is restarted, which causes the "Remote control requested" window pop up every time and makes unattended access impossible.

As of plasma version 6.3, a permission system was implemented, which allows to pre-authorize applications. Currently, the permission api is only available through the flatpak cli, although applications do not need to run as a flatpak to be able to get pre-authorized.

As per the upstream docs and flatpak-permission-set man pages, you need to figure out if the application you want to authorize sets an application ID or not. If started through a runner like KRunner, it gets set by plasma and is usually the filename of the .desktop-file under /usr/share/applications.

For example, to pre-authorize a virtual KVM switch like lan-mouse, you would do:

If you start it as a daemon in a systemd user-unit, you should use the name of that unit instead:

If you application does not set an ID, you can leave that field empty:

Wayland is used by default for KDE 6 applications, and the KDE applications fail to work under GNOME Wayland (and potentially other DEs/WMs) in this scenario. This can be fixed by setting the QT_QPA_PLATFORM=xcb environment variable.

This is a workaround for KDE bugs and not a problem with Wayland itself.

After the last upgrade to KDE 6 you may notice issues with all of the KDE icons not displaying. Newly created accounts showed them just fine.

The issue for this is that the theme got lost while upgrading and had to be reassigned manually. For this go to System Settings > Colors & Themes > Icons and select the theme you would like to use for the icons again.

This article or section is out of date.

Latest update might cause incompatible HiDPI scaling that made some interfaces becomes too big for your screen, some icons are missing or can not be displayed, and missing panels or widgets.

Try to remove qt5ct and kvantum related package, then apply default global Plasma theme. If the problem persists, try clearing all your KDE configuration and reinstalling plasma to overwrite the configuration. Be sure to check HiDPI scaling in KDE system settings as well.

Try to force font DPI to 96 in System Settings > Text & Fonts > Fonts.

If that does not work, try setting the DPI directly in your Xorg configuration as documented in Xorg#Setting DPI manually.

Many problems in KDE are related to its configuration.

Plasma problems are usually caused by unstable Plasma widgets (colloquially called plasmoids) or Plasma themes. First, find which was the last widget or theme you had installed and disable or uninstall it.

So, if your desktop suddenly exhibits "locking up", this is likely caused by a faulty installed widget. If you cannot remember which widget you installed before the problem began (sometimes it can be an irregular problem), try to track it down by removing each widget until the problem ceases. Then you can uninstall the widget, and file a bug report on the KDE bug tracker only if it is an official widget. If it is not, it is recommended to find the entry on the KDE Store and inform the developer of that widget about the problem (detailing steps to reproduce, etc.).

If you cannot find the problem, but you do not want all the settings to be lost, navigate to ~/.config/ and run the following command:

This command will rename all Plasma related configuration files to *.bak (e.g. plasmarc.bak) of your user and when you will relogin into Plasma, you will have the default settings back. To undo that action, remove the .bak file extension. If you already have *.bak files, rename, move, or delete them first. It is highly recommended that you create regular backups anyway. See Synchronization and backup programs for a list of possible solutions.

The problem may be caused by old cache. Sometimes, after an upgrade, the old cache might introduce strange, hard to debug behaviour such as unkillable shells, hangs when changing various settings, Ark being unable to extract archives or Amarok not recognizing any of your music. This solution can also resolve problems with KDE and Qt applications looking bad after an update.

Rebuild the cache using the following commands:

Optionally, empty the ~/.cache/ folder contents, however, this will also clear the cache of other applications:

Sometimes, empty the ~/.cache/ folder does not work, for example, if you encountered the following error:

It might be something related to outdated configuration files. In the above case, moving ~/.config/menus/ folder away may fix the issue. In other cases, try moving each file out of ~/.config/menus/ folder could be a good way to check what triggers the error.

Plasma desktop may use different settings than you set at KDE System Settings panel, or in locale.conf (per Locale#Variables). First thing to do is log out and log in after removing ~/.config/plasma-localerc, if this does not fix the issue, try to edit the file manually. For example, to set LANG variable to es_ES.UTF-8 and the LC_MESSAGES variable to en_US.UTF-8:

Make sure that QT_QPA_PLATFORMTHEME environment variable is unset, the command printenv QT_QPA_PLATFORMTHEME should show empty output. Otherwise if you had an environment set (most likely qt5ct or qt6ct) the variable will force qt5ct/qt6ct settings upon Qt applications, the command export QT_QPA_PLATFORMTHEME= should unset the environment.

An easier (and more reliable) solution can be to uninstall completely qt5ct and qt6ct.

Hiding certain items in the System Tray settings (e.g. Audio Volume, Media Player or Notifications) also disables related features. Hiding the Audio Volume disables volume control keys, Media Player disables multimedia keys (rewind, stop, pause) and hiding Notifications disables showing notifications.

The Login Screen KCM reads your cursor settings from ~/.config/kcminputrc, without this file no settings are synced. The easiest way to generate this file is to change your cursor theme in System Settings > Colors & Themes > Cursors, then change it back to your preferred cursor theme.

A crash or hardware change can modify the screen numbers, even on a single monitor setup. The panels/widgets can be missing after such an event, this can be fixed in the ~/.config/plasma-org.kde.plasma.desktop-appletsrc file by changing the lastScreen values.

Make sure you have the proper driver for your GPU installed. See Xorg#Driver installation for more information. If you have an older card, it might help to #Disable desktop effects manually or automatically for defined applications or #Disable compositing.

Hybrid graphics is a power management strategy commonly used in laptops that keeps the dedicated graphics processor (dGPU) inactive when not needed, defaulting to the integrated graphics processor (iGPU) for basic desktop rendering to conserve battery life.

While this approach saves power, it can result in suboptimal desktop performance, including low frame rates in animations and potential graphical artifacts, even on systems with capable dGPUs.

Forcing KDE Plasma to utilize the discrete GPU can significantly improve desktop responsiveness and visual quality.

For systems using open-source graphics drivers (Intel + AMDGPU, Intel + Nouveau), you can globally set the DRI_PRIME environment variable to specify the dGPU:

The index value (0 or 1) depends on your system configuration. Verify which index corresponds to your dGPU by running:

For direct control over KWin's GPU selection, create a startup script that sets the DRM device priority:

To identify your DRM cards and their corresponding GPUs:

List the dGPU first in the KWIN_DRM_DEVICES variable to prioritize it for rendering.

This command prints out a summary of the current state of KWin including used options, used compositing backend and relevant OpenGL driver capabilities. See more on Martin's blog.

Plasma has desktop effects enabled by default and e.g. not every game will disable them automatically. You can disable desktop effects in System Settings > Window Management > Desktop Effects and you can toggle desktop effects with Alt+Shift+F12.

Additionally, you can create custom KWin rules to automatically disable/enable compositing when a certain application/window starts under System Settings > Window Management > Window Rules.

If you use a transparent background without enabling the compositor, you will get the message:

In System Settings > Display & Monitor > Compositor, check Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Allow applications to block compositing. This may harm performance.

Setting the environment variable QSG_USE_SIMPLE_ANIMATION_DRIVER for KWIN reduces jerking in some Quick Scene Graphics based effects. For this purpose, it is sufficient to create a drop-in for the service running KWIN:

(in the case of Wayland session, use plasma-kwin_wayland.service.d as directory name)

Then restart the session.

Another try is to set QSG_NO_VSYNC instead of QSG_USE_SIMPLE_ANIMATION_DRIVER.

Create the directory ~/.local/share/icons/default/ (alternatively, ~/.icons/default), then, inside it, create a file named index.theme, then add to it the following contents:

If applicable, replace breeze_cursors with the cursor theme you use (cursor themes can be found in /usr/share/icons/, e.g. Breeze_Light).

On Wayland, it is necessary for xdg-desktop-portal-gtk to be installed for GTK/GNOME applications to correctly apply cursor themes.

Firefox and Thunderbird running under Wayland will refer to GSettings to determine which cursor to display.

To sync KDE settings to GTK applications, install kde-gtk-config.

If you do not want to install an extra package, you can set the cursor theme manually:

Try installing the appropriate 2D acceleration driver for your system and window manager.

Your local configuration settings for kscreen can override those set in xorg.conf. Look for kscreen configuration files in ~/.local/share/kscreen/ and check if mode is being set to a resolution that is not supported by your monitor.

In order to add icons to tray, applications often make use of the library appindicator. If your icons are blurry, check which version of libappindicator you have installed. If you only have libappindicator-gtk2AUR installed, you can install libappindicator as an attempt to get clear icons.

When running Plasma in a VMware, VirtualBox or QEMU virtual machine, kscreen may not allow changing the guest's screen resolution to a resolution higher than 800×600.

The workaround is to set the PreferredMode option in xorg.conf.d(5). Alternatively try using a different graphics adapter in the VM, e.g. VBoxSVGA instead of VMSVGA for VirtualBox and Virtio instead of QXL for QEMU. See KDE Bug 407058 for details.

Check whether your user directories (Documents, Downloads, etc.) are read-only.

In System Settings > Display & Monitor > Compositor, change Keep window thumbnails from Only from Shown windows to Never. If you are using Intel graphics, ensure that xf86-video-intel is not installed.

See XDG Desktop Portal#Poor font rendering in GTK applications on KDE Plasma.

You may observe that windows of some applications do not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk.

See Nouveau#Random lockups with kernel error messages.

If there is no sound after suspending and KMix does not show audio devices which should be there, restarting plasmashell and pulseaudio may help:

Some applications may also need to be restarted in order for sound to play from them again.

This can be solved by installing the GStreamer libav plugin (package gst-libav). If you still encounter problems, you can try changing the Phonon backend used by installing another such as phonon-qt6-vlc.

Then, make sure the backend is preferred via phononsettings.

Check if you have plasma-pa installed.

If journalctl -p4 -t pulseaudio contains entries saying Failed to create sink input: sink is suspended, try commenting the following line in /etc/pulse/default.pa:

If the issue persists, plasma-meta or plasma may have installed pulseaudio alongside wireplumber. To fix the issue, replace pulseaudio with pipewire-pulse. If pulseaudio is preferred, replace wireplumber with pipewire-media-session. See PipeWire#PulseAudio clients and this forum thread for more details.

If your system is able to suspend or hibernate using systemd but do not have these options shown in KDE, make sure powerdevil is installed.

Make sure you installed powerdevil and power-profiles-daemon. Run powerprofilesctl and check the driver. If it is intel_pstate or amd_pstate, you are done, otherwise see CPU frequency scaling#Scaling drivers for more information on enabling them.

See [13] for details.

If you want a backup, copy the following configuration directories:

For some IMAP accounts KMail will show the inbox as a top-level container (so it will not be possible to read messages there) with all other folders of this account inside.[14]. To solve this problem simply disable the server-side subscriptions in the KMail account settings.

While setting up EWS account in KMail, you may keep getting errors about failed authorization even for valid and fully working credentials. This is likely caused by broken communication between KWallet and KMail. To workaround the issue set a passsword via qdbus:

See Qt#Disable/Change Qt journal logging behaviour.

See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

It is not recommended to turn off the KWallet password saving system in the user settings as it is required to save encrypted credentials like Wi-Fi passphrases for each user. Persistently occuring KWallet dialogs can be the consequence of turning it off.

In case you find the dialogs to unlock the wallet annoying when applications want to access it, you can let the display managers SDDM and LightDM unlock the wallet at login automatically, see KDE Wallet#Unlock KDE Wallet automatically on login. The first wallet needs to be generated by KWallet (and not user-generated) in order to be usable for system program credentials.

In case you want the wallet credentials not to be opened in memory for every application, you can restrict applications from accessing it with kwalletmanager in the KWallet settings.

If you do not care for credential encryption at all, you can simply leave the password forms blank when KWallet asks for the password while creating a wallet. In this case, applications can access passwords without having to unlock the wallet first.

This can be solved by installing packagekit-qt6.

Discover sometimes will not remove its PackageKit alpm lock. To release it, remove /var/lib/PackageKit/alpm/db.lck. Use "Refresh" in Discover and updates should appear (if there are any updates pending).

As described in KDE Bug 347772 NVIDIA OpenGL drivers and QML may not play well together with Qt 5. This may lead kscreenlocker_greet to high CPU usage after unlocking the session. To work around this issue, set the QSG_RENDERER_LOOP environment variable to basic.

Then kill previous instances of the greeter with killall kscreenlocker_greet.

If your home directory is on a ZFS pool, create a ~/.config/akonadi/mysql-local.conf file with the following contents:

See MariaDB#OS error 22 when running on ZFS.

This is caused by the problematic way of GTK3 handling mouse scroll events. A workaround for this is to set environment variable GDK_CORE_DEVICE_EVENTS=1. However, this workaround also breaks touchpad smooth scrolling and touchscreen scrolling.

When using TeamViewer, it may behave slowly if you use smooth animations (such as windows minimizing). See #Disable compositing as a workaround.

Kmail may become unresponsive, show a black messageviewer or similar, often after having been minimized and restored. A workaround may be to set environment variable QT_QPA_PLATFORM="xcb;wayland". See KDE Bug 397825.

If you previously locked your widgets, you will probably find yourself unable to unlock them again. You just have to run this command to do so:

The new Customize Layout does not require to lock them back up but if want to do that:

Check file associations regarding HTML, PHP, etc... and change it to a browser. KIO's cache files are located in $HOME/.cache/kioexec. See also xdg-utils#URL scheme handlers.

In the System Settings application, KDE offers a setting to automatically lock the screen after waking up from sleep. Upon resuming, some users report that the screen is briefly showed before locking. To prevent this behavior and have KDE lock the screen before suspending, create a hook in systemd(1) by creating the following file as the root user:

The use of sleep is necessary in order for the loginctl lock-session command to complete before the device is suspended. Using a lower timeout may not allow for this to complete.

After creating the file, make it executable.

Finally, make sure that the KDE setting is enabled by going to System Settings > Screen Locking and checking the Lock screen automatically: After waking from sleep checkbox.

Some X11 software like freerdp can grab keyboard input since KDE 5.27. Others like VMware cannot grab correctly. [15]

It is inappropriate to force grab in Xserver or in compositors. [16] You can solve it in an elegant way as follows:

This can be caused because system settings cannot access/modify the .config folder in your home directory.

To fix this, you need to change the owner of the folder:

user refers to the name of the user that you are logged into in KDE Plasma. If the name of your home directory is not the same as the user you are logged in as, you can change it accordingly.

If this does not work, you might need to change the permissions of the folder:

There are issues with the Widget "Global Menu" not working with some applications even after installing appmenu-gtk-module and libdbusmenu-glib. The fix is to install the plasma5-integration and to restart your Session.

The factual accuracy of this article or section is disputed.

It is necessary to add a Polkit rule allowing mounting of internal drives without elevated privileges:

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/plasma-dbus-run-session-if-needed /usr/bin/startplasma-wayland
```

Example 2 (unknown):
```unknown
export DESKTOP_SESSION=plasma
```

Example 3 (unknown):
```unknown
exec startplasma-x11
```

Example 4 (unknown):
```unknown
startx /usr/bin/startplasma-x11
```

---

## xinit

**URL:** https://wiki.archlinux.org/title/Startx

**Contents:**
- Installation
- Configuration
  - xinitrc
  - xserverrc
    - Passing virtual terminal number
- Usage
- Tips and tricks
  - Override xinitrc
  - Autostart X at login
  - Switching between desktop environments/window managers

xinit is typically used to start window managers or desktop environments. While you can also use xinit to run GUI applications without a window manager, many graphical applications expect an EWMH compliant window manager. Display managers start Xorg for you and generally source xprofile.

Install the xorg-xinit package.

xinit and startx take an optional client program argument, see #Override xinitrc. If you do not provide one they will look for ~/.xinitrc to run as a shell script to start up client programs.

~/.xinitrc is handy to run programs depending on X and set environment variables on X server startup. If it is present in a user's home directory, startx and xinit execute it. Otherwise startx will run the default /etc/X11/xinit/xinitrc.

This default xinitrc will start a basic environment with Twm, xorg-xclock and Xterm (assuming that the necessary packages are installed). Therefore, to start a different window manager or desktop environment, first create a copy of the default xinitrc in your home directory:

Then edit the file and replace the default programs with desired commands. Remember that lines following a command using exec would be ignored. For example, to start xscreensaver in the background and then start openbox, use the following:

Long-running programs started before the window manager, such as a screensaver and wallpaper application, must either fork themselves or be run in the background by appending an & sign. Otherwise, the script would halt and wait for each program to exit before executing the window manager or desktop environment. Note that some programs should instead not be forked, to avoid race bugs, as is the case of xrdb. Prepending exec will replace the script process with the window manager process, so that X does not exit even if this process forks to the background.

The xserverrc file is a shell script responsible for starting up the X server. Both startx and xinit execute ~/.xserverrc if it exists, startx will use /etc/X11/xinit/xserverrc otherwise.

See Xserver(1) for a list of all command line options.

In order to maintain an authenticated session with logind and to prevent bypassing the screen locker by switching terminals, Xorg has to be started on the same virtual terminal where the login occurred [1]. For this purpose, Xorg needs to be passed the number of the current virtual terminal.

If you are invoking startx, nothing more needs to be done – it contains logic to compute and pass the virtual terminal number to Xorg.

In other cases, e.g. if you are running xinit, it is recommended to specify vt$XDG_VTNR in the ~/.xserverrc file:

To run Xorg as a regular user, issue:

Or if #xserverrc is configured:

Your window manager (or desktop environment) of choice should now start correctly.

To quit X, run your window manager's exit function (assuming it has one). If it lacks such functionality, run:

If you have a working ~/.xinitrc but just want to try other window manager or desktop environment, you can run it by issuing startx followed by the path to the window manager, for example:

If the binary takes arguments, they need to be quoted to be recognized as part of the first parameter of startx:

Note that the full path is required. You can also specify custom options for the #xserverrc script by appending them after the double dash -- sign:

Make sure that startx is properly configured.

Place the following in your login shell initialization file (e.g. ~/.bash_profile for Bash or ~/.zprofile for Zsh):

You can replace the -eq comparison with one like -le 3 (for vt1 to vt3) if you want to use graphical logins on more than one virtual terminal.

Alternative conditions to detect the virtual terminal include "$(tty)" = "/dev/tty1", which does not allow comparison with -le, and "$(fgconsole 2>/dev/null || echo -1)" -eq 1, which does not work in serial consoles.

The exec command ensures that the user is logged out when the X server exits, crashes or is killed by an attacker. If you want to take the risk and remain logged in when the X session ends, remove exec.

See also fish#Start X at login.

If you are frequently switching between different desktop environments or window managers, it is convenient to either use a display manager or expand ~/.xinitrc to make the switching possible.

The following example shows how to start a particular desktop environment or window manager with an argument:

To pass the argument session:

It is possible to start only specific applications without a window manager, although most likely this is only useful with a single application shown in full-screen mode. For example:

Alternatively the binary can be called directly from the command prompt as described in #Override xinitrc.

With this method you need to set each application's window geometry through its own configuration files (if possible at all).

See also Display manager#Starting applications without a window manager.

See Xorg#Session log redirection for details.

This article or section is a candidate for moving to Xorg.

Useful for running graphical applications:

Install xorg-server-xvfb, then run xvfb-run command.

**Examples:**

Example 1 (unknown):
```unknown
/etc/X11/xinit/xinitrc
```

Example 2 (unknown):
```unknown
$ cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

Example 3 (unknown):
```unknown
xscreensaver
```

Example 4 (unknown):
```unknown
...
xscreensaver &
exec openbox-session
```

---

## LightDM

**URL:** https://wiki.archlinux.org/title/LightDM

**Contents:**
- Installation
  - Greeter
- Enabling LightDM
- Command line tool
  - User switching
- Testing
- Optional configuration and tweaks
  - X session wrapper
    - Environment variables
    - Keymap

LightDM is a cross-desktop display manager. Its key features are:

More details about LightDM's design can be found here.

Install the lightdm package.

You will probably want to install a greeter. A greeter is a GUI that prompts the user for credentials, lets the user select a session, and so on. It is possible to use LightDM without a greeter, but only if an automatic login is configured; otherwise you will need to install xorg-server and one of the greeter packages below.

Themes for lightdm-webkit2-greeter:

Themes for web-greeterAUR and nody-greeterAUR:

You can set the default greeter by changing the [Seat:*] section of the LightDM configuration file, like so:

One way to check which greeters are available is to list the files in the /usr/share/xgreeters directory; each .desktop file represents an available greeter. In this example, the lightdm-gtk-greeter and lightdm-webkit2-greeter greeters are available:

Make sure to enable lightdm.service so LightDM will be started at boot; see also Display manager#Loading the display manager.

LightDM offers a command line tool, dm-tool, which can be used to lock the current seat, switch sessions, etc, which is useful with 'minimalist' window managers and for testing. To see a list of available commands, execute:

LightDM's dm-tool command can be used to allow multiple users to be logged in on separate ttys. The following will send a signal requesting that the current session be locked and then will initiate a switch to LightDM's greeter, allowing a new user to log in to the system.

First, install xorg-server-xephyr.

Then, run LightDM as an X application:

LightDM can be configured by modifying its configuration file, /etc/lightdm/lightdm.conf.

Some greeters have their own configuration files. For example:

lightdm-gtk-greeter: /etc/lightdm/lightdm-gtk-greeter.conf (or you can use the lightdm-gtk-greeter-settings gui).

lightdm-webkit2-greeter: /etc/lightdm/lightdm-webkit2-greeter.conf

This article or section is a candidate for merging with Xprofile.

If you are migrating from xinit, you will notice that the display is not launched by your shell. This is because, as opposed to your shell starting the display (and the display inheriting the environment of your shell), LightDM starts your display and does not source your shell. LightDM launches the display by running a wrapper script and that finally exec's your graphic environment. By default, /etc/lightdm/Xsession is run.

The script checks and sources /etc/profile, ~/.profile, /etc/xprofile and ~/.xprofile, in that order. If you are using a shell that does not source any of these files, you can create an ~/.xprofile to do so. (In this example, the login shell is zsh)

If you have shell variables that are important for your display (such as Gtk or QT themes, GNUPG location, configuration overrides, etc.) this will let your graphic environment have access to your environment without having to be launched by your login shell.

The script runs Xkbmap with arguments provided in files /etc/X11/Xkbmap, ~/.Xkbmap. If those files are not found, it runs xmodmap with /etc/X11/Xmodmap, ~/.Xmodmap. If using xkbmap, the files are parsed using cat. The following example works

Otherwise, the session inherits the system default mapping of X11. This mapping can be defined in the xorg configuration files, either manually or with localectl set-x11-keymap. See Xorg/Keyboard configuration#Setting keyboard layout.

To enable users switch between pre-defined keyboard layouts on the log-in screen enable the drop-down menu and configure the layouts. Either use the lightdm-gtk-greeter-settings gui or edit the configuration file directly:

Use localectl to set multiple layouts, e.g. de and its “variant” neo with the latter as primary:

Note the trailing comma which implies a blank variant for the second de.

You can set the background to a hex color or an image. Some greeters offer more robust background options like background selection from the login screen, random backgrounds, etc.

You can use the lightdm-gtk-greeter-settings gui.

Users wishing to customize the wallpaper on the greeter screen need to edit /etc/lightdm/lightdm-gtk-greeter.conf and define the background variable under the [greeter] section. For example:

GTK3 themes can be specified with the theme-name variable in the [greeter] section. The icon and cursor theme can be set in the same way, as shown in the following example:

Using lightdm-gtk-greeter out of the box in a HiDPI or 4K monitor, will render very small text and dialog boxes, it is possible to force a DPI setting like this:

In this case "192" means twice the 96 DPI setting of the screen, which is equivalent to the 2X Scale setting in other graphic environments. The value can be obtained with xdpyinfo | grep dots in Xorg, for example.

The lightdm-webkit2-greeter allows you to choose a background image directly on the login screen. It also offers an option to display a random image each time it starts if you use the Material theme. By default, images are sourced from /usr/share/backgrounds. You can change the background images directory by editing lightdm-webkit2-greeter.conf. For example:

Use the lightdm-settingsAUR GUI

First, make sure the accountsservice package is installed, then set it up as follows, replacing username with the desired user's login name.

The filename here should point to the icon created in the first step, so adjust the filename extension if necessary.

The archlinux-artworkAUR package contains some nice examples that install to /usr/share/archlinux/icons and that can be copied to /usr/share/icons/hicolor/64x64/devices as follows:

After copying, the archlinux-artworkAUR package can be removed.

Edit the LightDM configuration file and ensure these lines are uncommented and correctly configured:

You must be part of the autologin group to be able to login automatically without entering your password:

LightDM logs in using the session specified in the ~/.dmrc of the user getting logged in automatically. To override this file, specify autologin-session in lightdm.conf:

The list of valid session names can be found by listing /usr/share/xsessions/*.desktop for X's sessions and /usr/share/wayland-sessions/*.desktop for Wayland's.

LightDM goes through PAM so you must configure the lightdm configuration of PAM:

You must then also be part of the nopasswdlogin group and the autologin group to be able to login interactively without entering your password:

To create a new user account that logs in automatically and additionally able to login again without a password the user can be created with supplementary membership of both groups, e.g.:

To enable guest sessions in LightDM (without changing your system configuration) you need at least two things:

There are two AUR packages that enable guest sessions in lightdm:

To prevent system users from showing-up in the login, install the optional dependency accountsservice, or add the user names to /etc/lightdm/users.conf under hidden-users. The first option has the advantage of not needing to update the list when more users are added or removed.

This article or section is a candidate for merging with Display Manager.

Move the contents of xinitrc to xprofile, removing the call to start the window manager or desktop environment.

See Display manager#Run ~/.xinitrc as a session.

Install the numlockx package and then edit /etc/lightdm/lightdm.conf:

Lightdm, like other DMs, stores the last-selected xsession in ~/.dmrc. See Display manager#Session configuration for more info.

Users need to edit /etc/lightdm/lightdm-gtk-greeter.conf and enter a value for the position variable. It accepts x and y values, either absolute (in pixels) or relative (in percent). Each value can also have an additional anchor location for the window, start, center and end separated from the value by a comma.

Lightdm can also be used to connect to via VNC. Make sure to install tigervnc on the server side and optionally as your VNC client on the client PC.

Setup an authentication password on the server as root:

Edit the LightDM configuration file as shown below. Note that listen-address configures the VNC to only listen to connections from localhost. This is used to only allow connections via SSH and port forwarding. On the SSH client, make sure that you use localhost:5900 for the tunnel destination; using 127.0.0.1:5900 or ::1:5900 is not reliable on dual stack network connections. If you want to allow insecure connections you can disable this setting.

Now open an SSH tunnel and connect to localhost as described in TigerVNC#On the client.

light-locker is a simple screen locker using LightDM to authenticate the user. Once installed and running, you can lock your session via:

This requires light-locker to be started at the beginning of your session. By default, this is enabled through XDG Autostart. See Autostarting for more options.

Sometimes LightDM does not set the monitor resolution correctly on a multiple-monitor setup. The following Xorg configuration works with two monitors: a large primary screen on the left side, and a secondary smaller screen to its right. The order can be reversed and tweaked.

This makes the display-setup-script tweaks from /etc/lightdm/lightdm.conf redundant.

Ensure autologin-user= in /etc/lightdm/lightdm.conf contain the correct values. Trailing whitespace will cause errors.

If autologin fails with a blank screen or if the login screen immediately returns, you may need to set logind-check-graphical=true.

You can also install lightdm-autologin-greeter-gitAUR for this special purpose.

To view effective configuration, run:

This will show current settings, with the configuration files these settings were read from.

If you encounter consistent screen flashing and ultimately no LightDM on boot, ensure that you have defined the greeter correctly in LightDM's configuration file. And if you have correctly defined the GTK greeter, make sure the xsessions-directory (default: /usr/share/xsessions) exists and contains at least one .desktop file.

The same error can happen on lightdm startup if the last used session is not available anymore (eg. you last used gnome and then removed the gnome-session package): the easiest workaround is to temporarily restore the removed package. Another solution might be:

This example sets the session "xfce" as default for the user 1000.

In case of your locale not being displayed correctly in Lightdm add your locale to /etc/environment:

Alternatively if you want LightDM and its greeters to be in a language other than your set system locale, you can use the Environment= option in a drop-in file.

If you are using lightdm-gtk-greeter as a greeter and it shows placeholder images as icons, make sure valid icon themes and themes are installed and configured. Check the following file:

You may find that after entering the correct username and password and attempting to log in, LightDM freezes and you are unable to continue to the desktop. To fix the issue, reinstall the gdk-pixbuf2 package. See this forum thread.

If you are using multiple monitors, LightDM may display in the wrong one (e.g. if your primary monitor is on the right). To force the LightDM login screen to display on a specific monitor, edit /etc/lightdm/lightdm.conf and change the display-setup-script parameter like this:

Replace HDMI-1 with your real monitor ID, which you can find from xrandr command output.

Alternatively, if you are using the GTK greeter, you can edit /etc/lightdm/lightdm-gtk-greeter.conf and add the active-monitor parameter like this:

Replace 0 with the desired display number.

It may happen that your system boots so fast that LightDM service is started before your graphics drivers are properly loaded. If this is your case, you will want to add the following to your lightdm.conf file:

This setting will tell LightDM to wait until graphics devices are ready before spawning greeters/autostarting sessions on them.

With newer versions of LightDM, this is now the default setting. As a consequence, on some hardware, your graphics drivers may not be properly detected and LightDM may never attempt to launch a greeter--even after the system has stabilized after boot. If this occurs, setting this to false will disable the check and force LightDM to launch a greeter regardless.

See Intel graphics#AccelMethod.

See PulseAudio#Running.

Some LightDM themes try to access the user avatar located in HOME. If your HOME is encrypted, LightDM cannot access it and hangs. To prevent this from happening, you can either:

There is a possibility that user and group lookups fail if you modified /etc/nsswitch.conf. That happens when nsswitch.conf group: includes ldap without setting nss_initgroups_ignoreusers ALLLOCAL in /etc/nslcd.conf

Some greeters (lightdm-webkit2-greeter for example) do not support two sessions with the same name [1]. To check for duplicate entries:

Rename the duplicate entry in /usr/share/xsessions. For example:

Set a hostname as described in Network configuration#Set the hostname. See also FS#47694.

If you get stuck in loop in which you type your correct username and password but the screen goes black and then you return to the login prompt after every attempt, running rm ~/.Xauthority (or the stuck user's problematic .Xauthority) may fix the issue.

Another reason for this may be that you tried to recreate your "lightdm.conf" from scratch and your version is missing this line:

In that case, lightdm tries to use "lightdm-session" as the session-wrapper which does not exist on Arch Linux.

If your lightdm.conf file contains the intended session-wrapper but the lightdm logs indicate that the default session wrapper is being used instead, ensure that your lightdm.conf file is available during startup. For example, you may have created a symlink to a file in your home directory, but your home directory is not being mounted before the LightDM service started. In such cases LightDM will fall back to the default session wrapper.

When starting a Wayland session, input devices may sometimes not work unless disconnecting and reconnecting the physical connection. See LightDM issue 63.

A workaround is to delay the startup of Wayland compositors by adding sleep 1 to /etc/lightdm/Xsession. See archlinux/packaging/packages/lightdm!4 for a proposed workaround for the Arch package.

**Examples:**

Example 1 (unknown):
```unknown
/etc/lightdm/lightdm.conf
```

Example 2 (unknown):
```unknown
[Seat:*]
...
greeter-session=lightdm-yourgreeter-greeter
...
```

Example 3 (unknown):
```unknown
io.elementary.greeter.conf
```

Example 4 (unknown):
```unknown
lightdm-pantheon-greeter.conf
```

---

## GNOME/Document viewer

**URL:** https://wiki.archlinux.org/title/GNOME/Document_viewer

**Contents:**
- Installation
- Troubleshooting
  - Zoom-in is limited
  - PDF text is not shown correctly
  - Inverse search with SyncTeX does not work
  - WebP comic book support
  - Annotations
- Tips and Tricks
  - Annotation handling
  - Use as default PDF viewer

Document viewer is specifically designed to support the following file formats: PDF, PostScript, DjVu, tiff, dvi, XPS, SyncTex support with gedit, comics books (cbr,cbz,cb7 and cbt). For a comprehensive list of formats supported, see Supported Document Formats.

Document viewer uses the poppler library as a backend.

Install the evince package.

Increasing Evince's page cache size allows you to zoom in further, which is handy for large documents. By default the setting is set to 50MiB. Increasing the page cache size obviously increases Evince's memory consumption when zoomed-in.

The following command increases the page cache size to one gigabyte:

Try setting override-restrictions parameter to false:

Check that python-dbus is installed. After that Ctrl+click should work.

Some comic books files (cbr, cbz etc.) use WebP images. Install webp-pixbuf-loader for WebP comic book support.

Certain annotations created with Adobe Acrobat Reader are not displayed correctly. For annotations of type "insert text at cursor position" and "notice to replace text" only the visual part is displayed, while the text content of the comment appears wrongly to be empty. There currently is no solution for this problem.

Evince v3.31.0 adds keyboard hotkeys s for adding note text annotations and Ctrl+h for adding a highlight text annotation.

The default author for note text animations is equal to the GECOS comment for the current user, to change this:

To set the default association for xdg-open,

Other resource openers can be configured similarly.

**Examples:**

Example 1 (unknown):
```unknown
$ gsettings set org.gnome.Evince page-cache-size 'uint32 1000'
```

Example 2 (unknown):
```unknown
override-restrictions
```

Example 3 (unknown):
```unknown
$ gsettings set org.gnome.Evince override-restrictions false
```

Example 4 (unknown):
```unknown
# usermod -c "Your full new Real Name" yourusername
```

---

## Cinnamon

**URL:** https://wiki.archlinux.org/title/Cinnamon

**Contents:**
- Installation
  - Cinnamon applications
  - Fallback mode
- Starting
  - Graphical log-in
  - Starting Cinnamon manually
  - Restarting Cinnamon
- Configuration
  - Cinnamon settings
  - Applets and extensions

Cinnamon is a desktop environment which combines a traditional desktop layout with modern graphical effects. The underlying technology was forked from the GNOME desktop. As of version 2.0, Cinnamon is a complete desktop environment and not merely a frontend for GNOME like GNOME Shell and Unity.

Cinnamon can be installed with the package cinnamon.

Cinnamon introduces X-Apps which are based on GNOME Core Applications but are changed to work across Cinnamon, MATE and XFCE; they have the traditional user interface (UI).

On the event when Cinnamon crashes, its Fallback mode activates. To control opened windows in this mode, you need to install metacity package and gnome-shell to have a taskbar.

Choose Cinnamon or Cinnamon (Software Rendering) from the menu in a display manager of choice. Cinnamon is the 3D accelerated version, which should normally be used. If you experience problems with your video driver (e.g. artifacts or crashing), try the Cinnamon (Software Rendering) session, which disables 3D acceleration.

If you prefer to start Cinnamon manually from the console, add the following line to Xinitrc:

If the Cinnamon (Software Rendering) session is required, use cinnamon-session-cinnamon2d instead of cinnamon-session.

The following needs to be executed as the user the Cinnamon instance is running under:

To restart Cinnamon from outside a dbus session, you can use something like this:

Cinnamon is quite easy to configure — most common settings can be configured graphically. Its usability can be expanded with applets and extensions, and also it supports theming.

cinnamon-settings launches a settings module specified on the command line. Without (correct) arguments, it launches System Settings. For example, to start the panel settings:

To list all available modules:

While an applet is an addition to the Cinnamon panel, an extension can fully change the Cinnamon experience. They can be installed from the AUR, (package search), or from inside Cinnamon (Get more online):

Alternatively, install manually from Cinnamon spices.

This is the default behaviour. To change the setting, open the cinnamon-settings panel and click on the "Power Management" option. Change the "When the power button is pressed" option to your desired behaviour.

Cinnamon does not support using a different window manager.

The official tutorial on creating a Cinnamon applet can be found here.

When you add a wallpaper from a custom path in Cinnamon Settings, Cinnamon copies it to ~/.cinnamon/backgrounds. Thus, with every change of your wallpaper, you would have to add your updated wallpaper again from the settings menu or copy / symlink it manually to ~/.cinnamon/backgrounds.

Additionally, the official mint wallpapers are available for every release. Checkout the AUR.

By default, Cinnamon starts with desktop icons enabled but with no desktop icons on screen. To show desktop icons for the home folder, the filesystem, the trash, mounted volumes and network servers, open Cinnamon settings and click on desktop. Enable the checkboxes of the icons you want to see on screen.

The Menu applet supports launching custom commands. Right click on the applet, click on Configure... and then Open the menu editor. Select a sub-menu (or create a new one) and select New Item. Set Name, Command and Comment. Check the launch in terminal checkbox if needed. Leave unchecked for graphical applications. Click OK and close the menu editor afterwards. The launcher is added to the menu.

A workspace pager can be added to the panel. Right click the panel and choose the option Add applets to the panel. Add the Workspace switch applet to the panel. To change its position, right click on the panel and change the Panel edit mode on/off switch to on. Click and drag the switcher to the desired position and turn the panel edit mode off when finished.

By default, there are 2 workspaces. To add more, hit Control+Alt+Up to show all workspaces. Then click on the plus sign button on the right of the screen to add more workspaces.

Alternatively, you can choose the number by command-line:

Replacing 4 with the number of workspaces you want.

The desktop icons rendering feature is enabled in Nemo by default. To disable this feature, change the setting with the following command:

Linux Mint styled themes, icons and backgrounds can be installed with the mint-themesAUR, mint-l-themeAUR, mint-x-iconsAUR, mint-y-iconsAUR, mint-artworkAUR and mint-backgroundsAUR packages. Whereby the latter is a collection of all backgrounds included in all Linux Mint Versions. Backgrounds of individual Linux Mint versions are also available over the AUR.

The themes and icons can be edited in Settings > Themes. The backgrounds in Settings > Backgrounds.

Setting the desktop theme via shell can be done like this:

Cinnamon does not come with sounds used for events like the startup of the desktop that are also used in Linux Mint by default. These sound effects can be installed with the mint-artworkAUR package. The sound events can be edited in Settings > Sound > Sound Effects.

To resize windows with Alt+Right click, use gsettings:

To export your keyboard shortcut keys:

To later import it on another device:

As explained in Taking a screenshot, installing gnome-screenshot will add this functionality. The default shortcut key is PrintScreen key. This binding can be changed in the applet Menu > Preferences > Keyboard under Shortcuts > System > Screenshots and Recording. The default save directory is $HOME/Pictures, but can be customized with eg.

The cinnamon-settings-daemon provides a number of plugins which can manage the display, keyboard and mouse. These plugins will override user set configuration (such as xrandr commands in the xinitrc file). To stop user set configuration from being overridden, it is necessary to prevent the settings daemon plugins from being started.

This can be done by copying the .desktop entry for the relevant settings daemon plugin (these will be located in /etc/xdg/autostart/) to $HOME/.config/autostart. Then append the line Hidden=true to each copied entry.

To preserve display, keyboard and mouse settings, consider disabling the following:

You can use the cinnamon-looking-glass tool (Melange - Cinnamon Debugger) to inspect various things about the Cinnamon environment:

The "logs" feature is especially useful if you are encountering crashes (often happening due to extensions no being compatible or buggy).

If cinnamon-settings does not start with the message that it cannot find a certain module, e.g. the Image module, it is likely that it uses outdated compiled files which refer to no longer existing file locations. In this case, remove all *.pyc files in /usr/lib/cinnamon-settings and its sub-folders. See the upstream bug report.

If Cinnamon is completely unresponsive, it can be restarted from the TTY (Alt+F2) with:

Because muffin is based upon mutter, video tearing fixes for GNOME should also work in Cinnamon. See GNOME/Troubleshooting#Tear-free video with Intel HD Graphics for more information.

Even if you do not use NetworkManager and remove the Network Manager applet from the default panel, Cinnamon will still load nm-applet and display it in the system tray. You cannot uninstall the package because it is required by cinnamon and cinnamon-control-center, but you can still easily disable it. To do so, copy the autostart file from /etc/xdg/autostart/nm-applet.desktop to ~/.config/autostart/nm-applet.desktop. Open it with your favorite text editor and add at the end X-GNOME-Autostart-enabled=false.

Alternatively, you can disable it by creating the following symlink:

The ability to blacklist particular icons from the system tray (such as the nm-applet icon) has been requested upstream.

This article or section is out of date.

Cinnamon overrides custom settings in xorg.conf like display orientation and layout.

Open System Settings > Startup Applications and set Cinnamon Settings Daemon - xrandr to OFF.

Cinnamon uses Polkit to allow a non-root user to elevate their permissions in order to launch applications that require root permissions (such as Timeshift or GParted). Polkit requires this user to be part of the wheel group. If your user is not part of the wheel group, you may not receive the prompt for the root password when launching an application that requires root permissions (and thus the application will not be launched).

**Examples:**

Example 1 (unknown):
```unknown
exec cinnamon-session
```

Example 2 (unknown):
```unknown
cinnamon-session-cinnamon2d
```

Example 3 (unknown):
```unknown
cinnamon-session
```

Example 4 (unknown):
```unknown
$ cinnamon-dbus-command RestartCinnamon 1
```

---

## GNOME/Tips and tricks

**URL:** https://wiki.archlinux.org/title/GNOME/Tips_and_tricks

**Contents:**
- Keyboard
  - Turn on NumLock on login
  - Hotkey alternatives
  - XkbOptions keyboard options
  - De-bind the Super key
  - Modify Nautilus hotkeys
- Disks
- Hiding applications from the menu
- Screencast recording
- Screenshot

See Activating numlock on bootup#GNOME

A lot of hotkeys can be changed via GNOME Settings. For example, to re-enable the show desktop keybinding:

Settings > Keyboard > Customize Shortcuts > Navigation > Hide all normal windows

However, certain hotkeys cannot be changed directly via Settings. In order to change these keys, use dconf-editor or gsettings. An example of particular note is the hotkey Alt+` (the key above Tab on US keyboard layouts). In GNOME Shell it is pre-configured to cycle through windows of an application, however it is also a hotkey often used in the Emacs editor. It can be changed by using one of the aforementioned tools to modify the switch-group key found in org.gnome.desktop.wm.keybindings.

Using the dconf-editor, navigate to the xkb-options key under the org.gnome.desktop.input-sources schema and add desired XkbOptions (e.g. caps:swapescape) to the list.

See /usr/share/X11/xkb/rules/xorg for all XkbOptions and /usr/share/X11/xkb/symbols/* for the respective descriptions.

By default, the Super key will open the GNOME Shell overview mode. You can unbind this key by running the command below:

Since 3.15 it is not possible to use the accel file anymore, but it is possible to rebind keys by utilizing nautilus-python. Install the package and add the following file:

GNOME provides a disk utility to manipulate storage drive settings. These are some of its features:

Use the Main Menu application (provided by the alacarte package) to hide any applications you do not wish to show in the menu.

GNOME features built-in screencast recording with the Ctrl+Shift+Alt+r key combination. A red circle is displayed in the right side of the top bar near the system status area, while the recording is in progress. After the recording is finished, a file named Screencast from %d%u-%c.webm is saved in the Videos directory.

In order to use the screencast feature, some gst-plugin packages need to be installed. For example, the screencast pipeline depends on the vp8enc and webmmux elements from gst-plugins-good. If you get an error about missing "pipewiresrc" module when trying to record, install gst-plugin-pipewire.

The maximum screencast length is 30 seconds by default. This can be changed as follows:

Set length_in_seconds to 0 for unlimited length (per the description of max-screencast-length).

gnome-screenshot by default saves the image in the directory of the last save, which you can query:

Instead of using the above directory, you can set an auto save directory. e.g. for automatically saving screenshots to the user's desktop directory:

Check the gnome-screenshot(1) man page for more options.

To eliminate the default 60 second delay when logging out:

Gnome shell animation speed may be configured via a "slow down factor". Greater than 1.0 will slow down animations, between 0.0 & 1.0 speeds them up.

To set temporarily open looking glass with Alt-F2 enter lg then run, e.g. to speed up animations:

Alternatively use gnome-shell-extension-impatience-gitAUR

Slow down factor may be set permanently without an extension with environment variable GNOME_SHELL_SLOWDOWN_FACTOR, e.g.

Animations may be disabled via the GUI by toggling Settings > Accessibility > Seeing > Reduce Animation.

GNOME introduced HiDPI support in version 3.10. If your display does not provide the correct screen size through EDID, this can lead to incorrectly scaled UI elements. As a workaround you can open dconf-editor and find the key scaling-factor in org.gnome.desktop.interface. Set it to 1 to get the standard scale.

You can use the Passwords and Keys program seahorse to create a PGP key as it is a front end for GnuPG and installs it as dependency. This may be useful in the future (for instance if to encrypt a file). Create a key as shown below (the process may take about 10 minutes):

File > New > PGP Key > Name > Email > Defaults > Passphrase.

The default size of a new terminal can be adjusted in your profile's preferences. Select Preferences from the menu and select your profile under Profiles to access the settings to change the initial terminal size.

New terminals open in the $HOME directory by default. You can configure the terminal to adopt the current working directory by adding source /etc/profile.d/vte.sh to your shell configuration file.

To pad the terminal (create a small, invisible border between the window edges and the terminal contents) create the file below:

To disable the blinking cursor in GNOME 3.8 and above use:

To disable the blinking cursor in Terminal only use:

Note that gnome-settings-daemon, from the package of the same name, must be running for this and other settings changes to take effect in GNOME applications - see GNOME#Configuration.

The Terminal will always display a confirmation window when trying to close the window while one is logged in as root. To avoid this, execute the following:

The Terminal has support to change its color palette to your liking. Simply, go to Preferences, select your profile and finally edit the color palette.

Install the gogh-gitAUR package, which provides a set of custom schemes made for the GNOME Terminal. After you choose a scheme (or more than one), run gogh and input the number(s) of the scheme(s) that you chose.

After installation, go to Preferences of the Terminal, go to the Colors tab and select the name of the color scheme you installed from the left side of the window. You will see a small arrow next to the name, click it and select Set as default.

From here, further configuration can be taken. You may easily change certain colors you do not like.

To remove a scheme, make another one your default if you had that scheme as your default. Then select its name and click Delete.

This article or section is out of date.

By default, GNOME 3 disables middle mouse button emulation regardless of Xorg settings (Emulate3Buttons). To enable middle mouse button emulation use:

Since GTK 3.10, the GSettings key 'menus-have-icons' has been deprecated. Icons in buttons and menus can still be enabled by setting the following overrides:

To use custom colours and gradients for your desktop background, you will first need to set either a transparent picture or else a non-existent picture as your desktop background. For instance, the command below will set a non-existent picture as the background.

At this point, the desktop background should be a flat colour - the default colour setting is for a deep blue.

For a different flat colour you need only change the primary colour setting:

where <my color> is a hex value (such as ffffff for white).

For a colour gradient, you will also need to change secondary colour setting org.gnome.desktop.background secondary-color and select a shading type. For instance, if you want a horizontal gradient, execute the following:

If you are using a transparent picture as your background, you can set the opacity by executing the following:

where value is a number between 1 and 100 (100 for maximum opacity).

GNOME can transition between different wallpapers at specific time intervals. This is done by creating an XML file specifying the pictures to be used and the time interval. For more information on creating such files, see the following article.

It is possible to create custom GNOME sessions which use the GNOME session manager but start different sets of components (Openbox with tint2 instead of GNOME Shell for example).

Two files are required for a custom GNOME session: a session file in /usr/share/gnome-session/sessions/ which defines the components to be started and a desktop entry in /usr/share/xsessions which is read by the display manager. An example session file is provided below:

And an example desktop file:

This shows how to use Chromium for certain types of URLs while maintaining Firefox as default browser for all other tasks.

Make sure pcre is installed, to use pcregrep.

Setup custom xdg-open:

Configure domains for redirect to Chromium:

Setup xdg-open web as desktop application:

Set xdg-open web as default Web application in GNOME settings: Go to GNOME Settings > Default Applications and set Web to xdg-open web.

Nautilus (Files) overlays the film holes/film strip effect on video thumbnails since Gnome 3.12. To remove or override this effect, the environment variable G_RESOURCE_OVERLAYS can be used to reference the path of a compiled resource (in this instance filmholes.png) and specify the path for the relevant overlay. This environment variable has only been available since GLib 2.50 and will have no effect on versions before this.

Extract filmholes.png from Nautilus:

Edit filmholes.png using your preferred editor and remove the film effect from the image, leaving the transparency and dimensions intact, then overwriting the extracted image.

Copy or move the extracted image where desired, such as /usr/share/icons/ and edit ~/.profile, adding the following export, changing /usr/share/icons/ as needed to the location you placed the file:

If ffmpegthumbnailer has been installed as a dependency for another file manager that may generate thumbnails, the Exec line in /usr/share/thumbnailers/ffmpegthumbnailer.thumbnailer should be modified removing the -f flag.

To ensure that no thumbnails remain that may already have the film effect embedded, remove the thumbnail cache:

Log out and back in to your session and you should no longer have the film holes/film strip effect on your thumbnails in Nautilus.

packagekit integration was previously available through a package named gnome-software-packagekit-plugin but has been voluntarily disabled and is considered unsupported.

Apps installed with pacman are shown in but can't be uninstalled from GNOME Software. To not show them set this option and restart GNOME Software:

You can allow over-amplification by running the command below:

Alternatively, install the extension volume mixer. Then use the mouse to scroll above the volume icon in the top panel to increase the volume above and beyond 100%.

Or, open GNOME Tweaks and toggle General > Over-Amplification.

By default, pressing the keyboard's volume keys adjusts the volume by 6%. If smaller steps are desired, holding Shift while pressing the volume keys adjusts the volume in 2% steps.

Also, as of GNOME 3.36, it is now possible to directly adjust the volume step via a dconf setting. For example, to set the volume step to 2% execute the following:

Install the extension sound percentage to display the current output volume level next to the sound icon in the top panel.

Install switcheroo-control or switcheroo-control-gitAUR and start/enable switcheroo-control.service.

If you like having a tasks list on the bottom but dislike the default black color of this extension, first copy its directory:

Then edit the CSS to your liking. For example, to make the window list transparent, edit stylesheet.css as follows:

To mimic the behavior of Windows when switching between windows, first disable the default which restricts the window switching to those in the current workspace:

then, bind Alt+Tab and Alt+Shift+Tab to switch between windows, and not applications:

additionally, one can rebind the switching between applications (this example uses Super instead of the default Alt):

Install libheif to add support for HEIC image file format install `libheif`. Image Viewer uses `gdk-pixbuf2` library which lists `libheif` as one of the optional dependencies.

By default, dconf stores its configuration in a binary database blob located at $XDG_CONFIG_HOME/dconf/user. A dconf profile configuration may override this default if your home directories are stored in NFS, you keep dotfiles in version control, or other reasons. See dconf(7) § PROFILES for details on creating and using profiles.

Before changing the system-wide default, dump each user's existing dconf database to a text-based keyfile named user.txt. It does not appear to be possible to use a different extension. Assuming the default for XDG_CONFIG_HOME, that may be done with this command:

Once done, create the default dconf profile as root.

Log out and back in again and verify that changing dconf settings alters the text-based user.txt but not the old binary user file before deleting the binary database.

This setting should incur some minimal extra resource usage. Dconf still uses a binary database in the temporary XDG_RUNTIME_DIR directory, but it must recreate it at desktop startup. It must also keep user.txt up to date, and monitor the text file for changes as well.

**Examples:**

Example 1 (unknown):
```unknown
org.gnome.desktop.wm.keybindings
```

Example 2 (unknown):
```unknown
xkb-options
```

Example 3 (unknown):
```unknown
org.gnome.desktop.input-sources
```

Example 4 (unknown):
```unknown
/usr/share/X11/xkb/rules/xorg
```

---

## Openbox

**URL:** https://wiki.archlinux.org/title/Openbox

**Contents:**
- Installation
- Starting
  - Standalone
  - Other desktop environments
- Configuration
  - rc.xml
  - menu.xml
  - Autostart
  - environment
  - Themes

Openbox is a lightweight, powerful, and highly configurable stacking window manager with extensive standards support. It may be built upon and run independently as the basis of a unique desktop environment, or within other integrated desktop environments such as KDE and Xfce, as an alternative to the window managers they provide. The LXDE desktop environment is itself built around Openbox.

Install the openbox package. Also install TTF fonts such as ttf-dejavu and ttf-liberation.

Run openbox or openbox-session with xinit. Note that only openbox-session provides autostart.

See Desktop environment#Custom window manager.

Four key files form the basis of the openbox configuration, each serving a unique role. They are: rc.xml, menu.xml, autostart, and environment. Although these files are discussed in more detail below, to start configuring Openbox, it will first be necessary to create a local Openbox profile (i.e for your specific user account) based on them. This can be done by copying them from the global /etc/xdg/openbox profile (applicable to any and all users) as a template:

~/.config/openbox/rc.xml is the main configuration file, responsible for determining the behaviour and settings of the overall session, including:

This file is also pre-configured, meaning that it will only be necessary to amend existing content in order to customise behaviour to suit personal preference.

~/.config/openbox/menu.xml defines the type and behaviour of the desktop menu, accessible by right-clicking the background. Although the default provided is a static menu (meaning that it will not automatically update when new applications are installed), it is possible to employ the use of dynamic menus that will automatically update as well.

The available options are discussed extensively below in the #Menus section.

openbox-session provides two autostart mechanisms: XDG Autostart (which only works if python-pyxdg is installed) and Openbox's own autostart mechanism.

Openbox's own autostart mechanism:

Issues regarding commands in ~/.config/openbox/autostart being executed out of order (or skipped altogether) are often resolved by the addition of small delays. For instance:

In a standalone Openbox session, a Polkit authentication agent like the one provided by polkit-gnome can be launched from Openbox autostart. For example:

~/.config/openbox/environment can be used to export and set relevant environmental variables such as to:

Install obconf-qt and/or lxappearance-obconf for a GUI to configure visual settings and theming.

A good selection of themes are available in the openbox-themesAUR package or the AUR. Some GTK themes come with an Openbox theme as well. Both Openbox-specific and Openbox-compatible themes will be installed to the /usr/share/themes directory and will also be immediately available for selection.

box-look.org is an excellent and well-established source of themes. deviantART.com is another excellent resource. Many more can be found online.

The process of creating new or modifying existing themes is covered extensively at the official openbox.org website. obthemeAUR is a user-friendly GUI for doing so.

Several GUI applications are available to quickly and easily configure your Openbox desktop.

Programs and applications relating to the configuration of Openbox's desktop menu are discussed in #Menus.

Openbox will not always automatically reflect any changes made to its configuration files within a session. As a consequence, it will be necessary to manually reload those files after they have been edited. To do so, enter the following command:

Where intending to add this command as a keybind to ~/.config/openbox/rc.xml, it will only be necessary to list the command as reconfigure. An example has been provided below, using the Super+F11 keybind:

All keybinds must be added to the ~/.config/openbox/rc.xml file, and below the <!-- Keybindings for running aplications --> heading. Although a brief overview has been provided here, a more in-depth explanation of keybindings can be found at openbox.org.

Keybinds can be added to the configuration file using the following syntax:

The action name for running an external command is Execute. Use the following syntax to define an external command to execute:

See the Openbox wiki for a list of all available actions.

While the use of standard alpha-numeric keys for keybindings is self-explanatory, special names are assigned to other types of keys, such as modifiers, multimedia and navigation.

Modifier keys play an important role in keybindings (e.g. holding down the Shift or Ctrl key in combination with another key to undertake an action). Using modifiers helps to prevent conflicting keybinds, whereby two or more actions are linked to the same key or combination of keys. The syntax to use a modifier with another key is:

The modifier codes are as follows:

Where available, it is possible to set the appropriate multimedia keys to perform their intended functions, such as to control the volume and/or the screen brightness. These will usually be integrated into the function keys, and are identified by their appropriate symbols. See Keyboard input for details.

The volume and brightness multimedia codes are as follows (note that commands will still have to be assigned to them to actually function):

For a full list of XF86 multimedia keys, see LQWiki:XF86 keyboard symbols.

What commands should be used for controlling the volume will depend on whether ALSA, PulseAudio, or OSS is used for sound.

These are the directional / arrow keys, usually used to move the cursor up, down, left, or right. The (self-explanatory) navigation codes are as follows:

It is possible to employ three types of menu in Openbox: static, pipes (dynamic), and generators (static or dynamic). They may also be used alone or in any combination.

As the name would suggest, this default type of menu does not change in any way, and may be manually edited and/or (re)generated automatically through the use on an appropriate software package.

Fast and efficient, while this type of menu can be used to select applications, it can also be useful to access specific functions and/or perform specific tasks (e.g. desktop configuration), leaving the access of applications to another process (e.g. the synapse or xfce4-appfinder applications).

The ~/.config/openbox/menu.xml file will be the sole source of static desktop menu content.

menumaker automatically generates xml menus for several window managers, including Openbox, Fluxbox, IceWM and Xfce. It will search for all installed executable programs and consequently create a menu file for them. It is also possible to configure MenuMaker to exclude certain application types (e.g. relating to GNOME or KDE), if desired.

Once installed and executed, it will automatically generate a new ~/.config/openbox/menu.xml file. To avoid overwriting an existing file, enter:

Otherwise, to overwrite an existing file, add the force argument (f):

Once a new ~/.config/openbox/menu.xml file has been generated it may then be manually edited, or configured using a GUI menu editor, such as obmenuAUR.

obmenuAUR is a "user-friendly" GUI application to edit ~/.config/openbox/menu.xml, without the need to code in xml.

archlinux-xdg-menu will automatically generate a menu based on xdg files contained within the /etc/xdg/ directory for numerous Window Managers, including Openbox. Review the Xdg-menu#OpenBox article for further information.

The ~/.config/openbox/menu.xml file can be edited in order to provide a sub-menu with the same options as provided by oblogout. The sample script below will provide all of these options, with the exception of the ability to lock the screen:

Once the entries have been composed, add the following line to present the sub-menu where desired within the main desktop menu (usually as the last entry):

This type of menu is in essence a script that provides dynamic, refreshed lists on-the-fly as and when run. These lists may be used for multiple purposes, including to list applications, to provide information, and to provide control functions. Pre-configured pipe menus can be installed, although not from the official repositories. More experienced users can also modify and/or create their own custom scripts. Again, ~/.config/openbox/menu.xml may and commonly will contain several pipe menus.

Openbox.org also provides a further list of pipe menus.

This type of menu is akin to those provided by the taskbars of desktop environments such as Xfce or LXDE. Automatically updating on-the-fly, this type of menu can be powerful and very convenient. It may also be possible to add custom categories and menu entries; read the documentation for your intended dynamic menu to determine if and how this can be done.

A menu generator will have to be executed from the ~/.config/openbox/menu.xml file.

obmenu-generatorAUR is highly recommended despite being an unofficial package. With the ability to be used as a static or dynamic menu, it is highly configurable, powerful, and versatile. Menu categories and individual entries may also be easily hidden, customised, and/or added with ease. The official homepage provides further information and screenshots.

Below is an example of how obmenu-generator would be dynamically executed without icons in ~/.config/openbox/menu.xml:

To automatically iconify entries, the -i option would be added:

openbox-menuAUR uses the LXDE menu-cache to create dynamic menus. The official homepage provides further information and screenshots.

To show icons next to menu entries, it will be necessary to ensure they are enabled in the <menu> section of the ~/.config/openbox/rc.xml file:

Where using a static menu, it will then be necessary to edit the ~/.config/openbox/menu.xml file to provide both the icon = command, along with the full path and icon name for each entry. An example of the syntax used to provide an icon for a category is:

If you are having problems with icons not showing in the menu then try converting them to .png

xdotool is a package that can issue commands to simulate key presses / keybinds, meaning that it is possible to use it to invoke keybind-related actions without having to actually press their assigned keys. As this includes the ability to invoke an assigned keybind for the Openbox desktop menu, it is therefore possible to use XDoTool to turn the Openbox desktop menu into a panel menu. Especially where the desktop menu is heavily customised and feature-rich, this may prove very useful to:

Once XDoTool has been installed - if not already present - it will be necessary to create a keybind to access the root menu in ~/.config/openbox/rc.xml, and again below the <!-- Keybindings for running aplications --> heading. For example, the following code will bring up the menu by pressing Ctrl+m:

Openbox must then be reconfigured. In this instance, XDoTool will be used to simulate the Ctrl+m keypress to access the desktop menu with the following command (note the use of + in place of -):

How this command may be used as a panel launcher / icon is largely dependent on the features of panel used. While some panels will allow the above command to be executed directly in the process of creating a new launcher, others may require the use of an executable script. As an example, a custom executable script called obpanelmenu.sh will be created in the ~/.config directory and the appropriate XDoTool command is added to the file (to simulate the Ctrl+m keypress in this example):

After the file has been saved and closed, it may then be made into an executable script.

Executing it will bring up the Openbox desktop menu. Consequently, where using a panel that supports drag-and-drop functionality to add new launchers, simply drag the executable script onto it before changing the icon to suit personal taste.

A xdg compliant menu is based on the freedesktop.org standard. The menu is defined in menu-files which reside in /etc/xdg/menus. New applications will occur automatically in the menu.

The archlinux-menusAUR package provides an Arch Linux specific XDG-compliant menu.

See Cursor themes and Icons for details.

Openbox does not natively support the use of desktop icons or wallpapers.

See PCManFM, SpaceFM and Idesk.

See List of applications/Other#Wallpaper setters.

Openbox does not provide native support for compositing, and thus requires an external compositor for this purpose.

Although compositing is not a necessary component, it may specifically avoid issues such as screen distortion with oblogout, and visual glitches with terminal window transparency. See Xorg#List of composite managers for common choices.

See the Oblogout article for an overview on how to use this useful, graphical logout script.

If you need to execute a complex command, use shell functionality.

When writing your own scripts, make sure to escape xml special characters, such as "&" ("&amp;"), "<" ("&lt;"), ">" ("&gt;") and other (see more on Predefined entities in XML).

This example will turn off display immediately and lock screen with slock. It was taken from this thread.

Sometimes one need to specify environment variable for application:

Another example will launch application preserving all stdout and stderr output to file:

Given the lack of a desktop environment with a plain Openbox install, it can be useful to install one or more application launchers as supplements to the Openbox menu system and the hotkeys. Lists of such launchers can be found at Category:Application launchers and List of applications/Other#Application launchers; popular examples are Gmrun and dmenu.

It is possible to switch desktop by moving the mouse cursor to the edges of the screen. First install xdotool and add the following two lines to your ~/.xinitrc:

See the Default applications article.

The program transset-dfAUR can enable window transparency on-the-fly.

For example, using the following code in the <mouse> section of the ~/.config/openbox/rc.xml file will enable control of application window transparency by hovering the mouse-pointer over the title bar and scrolling with the middle button:

The openbox package provides a obxprop binary that can parse relevant values for applications settings in rc.xml. Officially obxprop | grep "^_OB_APP" is recommended for this task. Start the process by running the command shown, then click a window to see its properties in the terminal.

xorg-xprop can be used to relay property values for selected applications. Where frequently using per-application settings, the following Bash Alias may be useful:

To use Xorg-XProp, run using the alias given xp, and click on the active program desired to define with per-application settings. The results displayed will only be the information that Openbox itself requires, namely the WM_WINDOW_ROLE and WM_CLASS (name and class) values:

See the article section switching between keyboard layouts for instructions.

Install obsetlayoutAUR. To set a 2x2 grid for example:

Run it without arguments to know what the arguments mean.

lead-gitAUR provides hot corners for openbox and other lightweight window managers. Start the application with a entry in the autostart-file:

Commands can be edited in the configuration file ~/.config/lead/lead.conf (replace eDP1 with the name of your screen output, which you can find out using xrandr):

For more information see [2].

Many desktop environments and window managers support window snapping (e.g. Windows 7 Aero snap), whereby they will automatically snap into place when moved to the edge of the screen. This effect can also be simulated in Openbox through the use of keybinds on focused windows.

As illustrated in the example below, percentages must be used to determine window sizes (see openbox.org for further information). In this instance, The super key is used in conjunction with the navigation keys:

However, it should be noted that once a window has been 'snapped' to an edge, it will remain vertically maximised unless subsequently maximised and then restored. The solution is to implement additional keybinds - in this instance using the down and up keys - to do so. This will also make pulling 'snapped' windows from screen edges faster as well:

This Ubuntu forum thread provides more information. Applications such as opensnapAUR are also available to automatically simulate window snapping behaviour without the use of keybinds. Another option is to use bunsen-utilities-gitAUR which provides bl-aerosnap --left and bl-aerosnap --right commands which will snap active window on left or right edge respectively if it is not snapped and restore it to original size and position otherwise. Just bind these commands to the key combination of your choosing.

The example below will give you quarter window tiling in each corner of the screen using the alt key in combination with the navigation keys

Users of display managers might experience a flickering during the transition between the display manager and the Openbox desktop. The flickering comes from Openbox setting the root window's color during startup. Therefore there is a brief moment when the display flashes in a grey color, between the display manager's background and the desktop's wallpaper.

Setting the root window's background color can be disabled by editing the Openbox startup script found in /usr/lib/openbox/openbox-autostart. Simply comment out (or delete) the block starting with # Set a background color.

To remove window decorations for all or particular applications, use the <decor> option in the <applications> section of rc.xml (user: ~/.config/openbox/ or system: /etc/xdg/openbox/). Example for Firefox, including variants like Firefox-Beta and Firefox-Nightly:

One could also disable decorations for all applications (using class "*"), then enable them (using yes) for individual ones. To apply the changes, restart your desktop session, and thus Openbox. Reference: Openbox FAQ

Mozilla based browsers may ignore application rules (e.g. <desktop>) unless class="Firefox" is used. See #Xprop values for applications.

If for any reason the newly extracted theme cannot be selected, open the theme directory to first ensure that it is compatible with Openbox - there should be an openbox-3 directory and a themerc file within it. An .obt (OpenBox Theme) file may also be present in some instances, which can then be manually loaded in obconf-qt.

A theme may also be not accessible due to wrong permissions. See File permissions and attributes for more.

By default Openbox switches from the last desktop back to the first desktop on mouse wheel scroll. Use <wrap>no</wrap> in the mousebind section to disable this behaviour.

Some application windows (such as Firefox windows) may load behind the currently active window, causing you to need to switch to the window you just created to focus it. To fix this behavior add this to your ~/.config/openbox/rc.xml file, inbetween the <openbox_config> and </openbox_config> tags:

**Examples:**

Example 1 (unknown):
```unknown
openbox-session
```

Example 2 (unknown):
```unknown
openbox-session
```

Example 3 (unknown):
```unknown
environment
```

Example 4 (unknown):
```unknown
/etc/xdg/openbox
```

---

## KDevelop

**URL:** https://wiki.archlinux.org/title/KDevelop

**Contents:**
- Installation
- Features
  - Plugins
- Building additional plugins
- Troubleshooting
  - KDevCMakeManager
  - Debugging with gdb

From KDevelop's website:

KDevelop 5 has parser backends for C, C++, Objective-C, OpenCL and JavaScript/QML, with plugins supporting PHP, Python 3 and Ruby. Basic syntax highlighting and code folding are available for dozens of other source-code and markup formats, but without semantic analysis.

KDevelop is part of the KDE project, and is based on KDE Frameworks and Qt. The C/C++ backend uses Clang, clang-tidy and heaptrack to provide accurate information even for very complex codebases."

Install the kdevelop package to get started.

KDevelop uses an embedded text editor component through the KParts framework. The default editor is KDE Advanced Text Editor (Kate), which can optionally be replaced with a Qt Designer-based editor. This list focuses on the features of KDevelop itself.

KDevelop 4 is a completely plugin-based architecture. When a developer makes a change, they only must compile the plugin.

Code completion is available for C and C++. Symbols are kept in a Berkeley DB file for quick lookups without re-parsing. KDevelop also offers a developer framework which helps to write new parsers for other programming languages.

An integrated debugger allows graphically doing all debugging with breakpoints and backtraces. It even works with dynamically loaded plugins unlike command line GDB.

Quick Open allows quick navigation between files.

Currently, around 50 to 100 plugins exist for this IDE. Major ones include persistent project-wide code bookmarks, Code abbreviations which allow expanding text quickly, a Source formatter which reformats code to a style guide before saving, Regular expressions search, and project-wide search/replace which helps in refactoring code.

Install plugins to provide autocompletion and other language-specific features:

The KDevelop Parser Generator (kdevelop-pg-qt package) is required to build additional plugins. Plugins will not compile if this package is not installed beforehand.

Make sure cmake is installed if you get this error: "Could not load project management plugin KDevCMakeManager".

The debugging option to use gdb will not appear unless okteta is installed. Install okteta and restart KDevelop to enable gdb support.

---

## XDM

**URL:** https://wiki.archlinux.org/title/XDM

**Contents:**
- Installation
- Configuration
  - Defining the session
  - Theming
    - Background wallpaper
    - Font
    - Login dialog positioning
    - Removing the logo
  - Multiple X sessions & Login in the window
  - Passwordless login

From xdm(8) § DESCRIPTION:

XDM provides a simple and straightforward graphical login prompt.

Install the xorg-xdm package. Then enable xdm.service.

If you would like to use an Arch Linux theme for XDM, you can optionally install the xdm-archlinux package. If installing the latter package, then do not enable xdm.service, but instead enable xdm-archlinux.service.

Unlike many more modern display managers such as GDM or LightDM, XDM does not source available sessions from .desktop files located in the /usr/share/xsessions directory. As such, XDM does not have a 'session menu.' Instead, XDM will execute the .xsession file in the home directory.

For example, to start Xfce upon login, the ~/.xsession file should look like this:

Ensure that the .xsession file in your home directory is executable.

For the exact meanings of the options discussed below, see xdm(8). The configuration file is located in /etc/X11/xdm/Xresources, notice that if you installed xdm-archlinux the configuration file will instead be located in /etc/X11/xdm/archlinux/Xresources.

Create a directory to put wallpapers in, e.g /usr/local/share/backgrounds and then place them inside it.

Edit /etc/X11/xdm/Xsetup_0. Change the xconsole command to /usr/bin/qiv -zr /usr/local/share/backgrounds/*

This configuration will move the login dialog to the bottom right of the screen.

Comment out the logo defines:

With the XDMCP enabled, you can easily connect to local or remote XDM instance and run multiple X sessions simultaneously on the same machine:

This command will launch the second session in window using Xephyr:

In order to enable passwordless login for XDM, add the line below to /etc/X11/xdm/Xresources:

**Examples:**

Example 1 (unknown):
```unknown
xdm.service
```

Example 2 (unknown):
```unknown
xdm.service
```

Example 3 (unknown):
```unknown
xdm-archlinux.service
```

Example 4 (unknown):
```unknown
/usr/share/xsessions
```

---

## KDE

**URL:** https://wiki.archlinux.org/title/KDE

**Contents:**
- Installation
  - Plasma
  - Plasma Mobile
  - KDE applications
  - Unstable releases
- Starting Plasma
  - Using a display manager
  - From the console
- Configuration
  - Personalization

KDE is a software project currently comprising a desktop environment known as Plasma, a collection of libraries and frameworks (KDE Frameworks) and several applications (KDE Applications) as well.

KDE upstream has a well maintained UserBase wiki. Detailed information about most KDE applications can be found there.

Install the plasma-meta meta-package or the plasma group. For differences between plasma-meta and plasma reference Package group. Alternatively, for a more minimal Plasma installation, install the plasma-desktop package. Upstream KDE has package and setup recommendations to get a fully-featured Plasma session.

If you are an NVIDIA user with the proprietary nvidia driver and wish to use the Wayland session, enable the DRM kernel mode setting.

Install plasma-mobileAUR.

To install the full set of KDE Applications, install the kde-applications-meta meta-package or the kde-applications group. If you only want KDE applications for a certain category, like gaming or education, install the relevant dependency of kde-applications-meta. Note that installing applications alone will not install any version of Plasma.

See Official repositories#kde-unstable for beta releases.

Starting from Plasma 6.4, the Wayland session has matured enough to become the default and preferred one: the X11 session is only available separately with the plasma-x11-session package[1]. The Xorg session is still supported, but will be removed in Plasma 7. See Wayland Known Significant Issues and X11 Known Significant Issues for more information.

Plasma can be started either using a display manager, or from the console.

Most settings for KDE applications are stored in ~/.config/. However, configuring KDE is primarily done through the System Settings application. It can be started from a terminal by executing systemsettings.

There are different types of KDE themes, varying by scope of what they modify:

For easy system-wide installation and updating, some themes are available in both the official repositories and the AUR.

Global themes can also be installed through System Settings > Colors & Themes > Global Theme > Get New....

The recommended theme for a pleasant appearance in GTK applications is breeze-gtk, a GTK theme designed to mimic the appearance of Plasma's Breeze theme. Install kde-gtk-config (part of the plasma group), relogin and select Breeze as the GTK theme in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style....

This article or section is out of date.

In some themes, tooltips in GTK applications have white text on white backgrounds making it difficult to read. To change the colors in GTK2 applications, find the section for tooltips in the .gtkrc-2.0 file and change it. For GTK3 application two files need to be changed, gtk.css and settings.ini.

Some GTK2 programs like vuescan-binAUR still look hardly usable due to invisible checkboxes with the Breeze or Adwaita skin in a Plasma session. To workaround this, install and select e.g. the Numix-Frost-Light skin of the numix-frost-themesAUR under System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style... > GTK theme. Numix-Frost-Light looks similar to Breeze.

Plasma and SDDM will both use images found at /var/lib/AccountsService/icons/ as users' avatars. To configure with a graphical interface, you can use System Settings > Users. The file corresponding to your username can be removed to restore the default avatar.

Plasmoids are widgets for Plasma desktop shell designed to enhance the functionality of desktop, they can be found on the AUR.

Plasmoid scripts can also be installed by right-clicking onto a panel or the desktop and choosing Enter Edit Mode > Add Widgets... > Get New Widgets... > Download New Plasma Widgets. This will present a front-end for https://store.kde.org/ that allows you to install, uninstall, or update third-party Plasmoid scripts with just one click.

Install plasma-pa or kmix (start Kmix from the Application Launcher). plasma-pa is now installed by default with plasma, no further configuration needed.

As the Plasma panel is on top of other windows, its shadow is drawn over them. [5] To disable this behaviour without impacting other shadows, install xorg-xprop and run:

then select the panel with the plus-sized cursor. [6] For automation, install xorg-xwininfo and create the following script:

Make the script executable.

The factual accuracy of this article or section is disputed.

The script can be run on login with Add Login Script in Autostart:

See HiDPI#KDE Plasma.

The plasma-phone-settings repository contains several recommended settings which can be applied globally (/etc/xdg) and/or per user (~/.config).

/etc/xdg/kscreenlockerrc (or ~/.config/kscreenlockerrc) locks the screen immediately after login. [7] This is useful in combination with SDDM#Autologin.

To use a virtual keyboard in the Wayland session, install maliit-keyboard and enable it in System Settings > Keyboard > Virtual Keyboard.

If your device has a hardware keyboard, but you want to use the virtual keyboard, add the KWIN_IM_SHOW_ALWAYS=1 environment variable to your Wayland session.

To use a virtual keyboard in the X11 session, choose an appropriate one from List of applications/Utilities#On-screen keyboards and run it manually.

Window decorations can be found in the AUR.

They can be changed in System Settings > Colors & Themes > Window Decorations, there you can also directly download and install more themes with one click.

Icon themes can be installed and changed on System Settings > Colors & Themes > Icons.

The Plasma Netbook shell has been dropped from Plasma 5, see the following KDE forum post. However, you can achieve something similar by editing the file ~/.config/kwinrc adding BorderlessMaximizedWindows=true in the [Windows] section.

To allow thumbnail generation for media or document files on the desktop and in Dolphin, install kdegraphics-thumbnailers and ffmpegthumbs.

Then enable the thumbnail categories for the desktop via right click on the desktop background > Configure Desktop and Wallpaper... > Icons > Configure Preview Plugins....

In Dolphin, navigate to Configure > Configure Dolphin... > Interface > Previews.

Plasma provides a Redshift-like feature (working on both Xorg and Wayland) called Night Light. It makes the colors on the screen warmer to reduce eye strain at the time of your choosing. It can be enabled in System Settings > Colors & Themes > Night Light.

You can also configure printers in System Settings > Printers. To use this method, you must first install the following packages print-manager, cups, system-config-printer. See CUPS#Configuration.

The Dolphin share functionality requires the package kdenetwork-filesharing and usershares, which the stock smb.conf does not have enabled. Instructions to add them are in Samba#Enable Usershares, after which sharing in Dolphin should work out of the box after restarting Samba.

Accessing Windows shares from Dolphin works out of the box. Use the path smb://servername/share to browse the files.

Unlike GTK file browsers which utilize GVfs also for the launched program, opening files from Samba shares in Dolphin via KIO makes Plasma copy the whole file to the local system first with most programs (VLC is an exception). To workaround this, you can use a GTK based file browser like thunar with gvfs and gvfs-smb (and gnome-keyring for saving login credentials) to access SMB shares in a more able way.

Another possibility is to mount a Samba share via cifs-utils to make it look to Plasma like if the SMB share was just a normal local folder and thus can be accessed normally. See Samba#Manual mounting and Samba#Automatic mounting.

A GUI solution is available with samba-mounter-gitAUR, which offers basically the same functionality via an easy to use option located at System Settings > Network Drivers. However, it might break with new KDE Plasma versions.

KDE Desktop Activities are special workspaces where you can select specific settings for each activity that apply only when you are using said activity.

Install powerdevil for an integrated Plasma power managing service. This service offers additional power saving features, monitor brightness control (if supported) and battery reporting including peripheral devices.

The factual accuracy of this article or section is disputed.

Plasma can autostart applications and run scripts on startup and shutdown. To autostart an application, navigate to System Settings > Autostart and add the program or shell script of your choice. For applications, a .desktop file will be created, for login scripts, a .desktop file launching the script will be created.

See official documentation.

Phonon is being widely used within KDE, for both audio (e.g., the System notifications or KDE audio applications) and video (e.g., the Dolphin video thumbnails). It can use the following backends:

KDE recommends only the VLC backend, as the GStreamer backend is unmaintained.

Plasma stores personalized desktop settings as configuration files in the XDG_CONFIG_HOME folder. Use the detail of configuration files to select and choose a method of backup and restore.

Plasma uses a systemd user instance to launch and manage all the Plasma services. This is the default startup method since Plasma 5.25, but can be disabled to use boot scripts instead with the following command (however this may stop working in a future release):

More details about the implementation can be read in Edmundson's blog: Plasma and the systemd startup.

KDE applications use sonnet for spell checking. See its optional dependencies for the supported spell checkers.

Configure it in System Settings > Spell Check.

See https://community.kde.org/Plasma/Wayland/Nvidia.

The KDE project provides a suite of applications that integrate with the Plasma desktop. See the kde-applications group for a full listing of the available applications. Also see Category:KDE for related KDE application pages.

Aside from the programs provided in KDE Applications, there are many other applications available that can complement the Plasma desktop. Some of these are discussed below.

Navigate to the submenu System Settings > Keyboard > Advanced (tab) > Key sequence to kill the X server and ensure that the checkbox is ticked.

KCM stands for KConfig Module. KCMs can help you configure your system by providing interfaces in System Settings, or through the command line with kcmshell6.

More KCMs can be found at linux-apps.com.

KDE implements desktop search with a software called Baloo, a file indexing and searching solution.

The following web browsers can integrate with Plasma:

KDE offers its own stack for personal information management (PIM). This includes emails, contacts, calendar, etc. To install all the PIM packages, you could use the kde-pim package group or the kde-pim-meta meta package.

Akonadi is a system meant to act as a local cache for PIM data, regardless of its origin, which can be then used by other applications. This includes the user's emails, contacts, calendars, events, journals, alarms, notes, and so on. Akonadi does not store any data by itself: the storage format depends on the nature of the data (for example, contacts may be stored in vCard format).

Install akonadi. For additional addons, install kdepim-addons.

By default Akonadi will use /usr/bin/mysqld (MariaDB by default, see MySQL for alternative providers) to run a managed MySQL instance with the database stored in ~/.local/share/akonadi/db_data/.

Akonadi supports using the system-wide MySQL for its database.[10]

This article or section needs expansion.

Akonadi supports either using the existing system-wide PostgreSQL instance, i.e. postgresql.service, or running a PostgreSQL instance with user privileges and the database in ~/.local/share/akonadi/db_data/.

Install postgresql and postgresql-old-upgrade.

Edit the Akonadi configuration file so that it has the following contents:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

This requires an already configured and running PostgreSQL.

Create a PostgreSQL user account for your user:

Create a database for Akonadi:

Edit the Akonadi configuration file to match the configuration below:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

To use SQLite, edit the Akonadi configuration file to match the configuration below:

Users who want to disable Akonadi would need to not start any KDE applications that rely on it. See this section in the KDE userbase for more information.

KDE Connect provides several features to connect your Android or iOS phone with your Linux desktop:

You will need to install KDE Connect both on your computer and on your phone. For PC, install kdeconnect package. For Android, install KDE Connect from Google Play or from F-Droid. If you want to browse your phone's filesystem, you need to install sshfs as well and configure filesystem exposes in your Android app. For iOS, install KDE Connect from the App Store. Not all features from the Android version are available on the iOS version.

To use remote input functionality on a Plasma Wayland session, the xdg-desktop-portal package is required.

It is possible to use KDE Connect even if you do not use the Plasma desktop. For GNOME users, better integration can be achieved by installing gnome-shell-extension-gsconnectAUR instead of kdeconnect. To start the KDE Connect daemon manually, execute /usr/bin/kdeconnectd.

If you use a firewall, you need to open UDP and TCP ports 1714 through 1764.

Sometimes, KDE Connect will not detect a phone. You can restart the services by running killall kdeconnectd and then opening kdeconnect in system settings or running kdeconnect-cli --refresh followed by kdeconnect-cli -l. You can also use Pair new device > Add devices by IP on KDE Connect for Android.

It is possible to use a window manager other than KWin with Plasma. This allows you to combine the functionality of the KDE desktop with the utility of a tiling window manager, which may be more fleshed out than KWin tiling scripts.

The component chooser settings in Plasma no longer allows changing the window manager, but you are still able to swap KWin via other methods.

Since KDE 5.25, Plasma's systemd based startup is enabled by default.

To replace KWin in this startup, you must first mask the plasma-kwin_x11.service for the current user to prevent it from starting.

Then, create a new systemd user unit to start your preferred WM [11]:

To use it, do (as user units) a daemon-reload, make sure you have masked plasma-kwin_x11.service then enable the newly created plasma-custom-wm.service.

Plasma's script-based boot is used by disabling #systemd startup. If you have done so, you can change the window manager by setting the KDEWM environment variable before Plasma is invoked.

This article or section is a candidate for merging with Environment variables#Globally.

If you have root access, you can also add an XSession that will be available to all users as an option on the login screen.

First, create a script with execution permissions as follows:

Replace /usr/bin/i3 to the path to your preferred WM. Ensure the path is correctly set. If KDE is unable to start the window manager, the session will fail and the user will be returned to the login screen.

Then, to add an XSession, add a file in /usr/share/xsessions/ with the following content:

The openbox package provides a session for using KDE with Openbox. To make use of this session, disable #systemd startup and select KDE/Openbox from the display manager menu.

For those starting the session manually, add the following line to your xinit configuration:

A list of KWin extensions that can be used to make KDE behave more like a tiling window manager.

To enable display resolution management and multiple monitors in Plasma, install kscreen. This provides additional options to System Settings > Display & Monitor.

On X11, ICC profiles are handled by colord. To configure them in Plasma, install colord-kde. This provides additional options in System Settings > Color Management. ICC profiles can be imported using Import Profile.

For Wayland sessions, color management is handled by the compositor, i.e. KWin for Plasma. In this case, no additional package is required. The color profile can be configured per monitor in System Settings > Display & Monitor > Color Profile.

HDR support is experimental and only works in a Wayland session. System Settings > Display & Monitor > High Dynamic Range > Enable HDR.

For more information on displaying HDR content see HDR monitor support. Development details about HDR in Plasma can be found on Xaver Hugl's blog post.

When enabling HDR mode in KDE Plasma, SDR content can appear extremely dark, sometimes making the screen nearly unreadable. To address this, KDE provides two key sliders in display settings: Maximum SDR Brightness, which adjusts the brightness mapping for SDR content in HDR mode, and Brightness which controls the overall display backlight or luminance

To disable this feature, you currently have to edit the kwinrc config file and set the Meta key under ModifierOnlyShortcuts to an empty string:

Alternatively, you can also run the following command:

With the Plasma Browser integration installed, KDE will show bookmarks in the application launcher.

To disable this feature, go to System Settings > Search > Plasma Search and uncheck Bookmarks.

IBus is an input method framework and can be integrated into KDE. See IBus#Integration for details.

Using IBus may be required when using KDE on Wayland to offer accented characters and dead keys support [12].

See NetworkManager#Sharing internet connection over Wi-Fi.

If you have System Settings > Session > Desktop Session > Session Restore > On login, launch apps that were open: On last logout (default) selected, ksmserver (KDE's session manager) will automatically save/load all open applications to/from ~/.config/ksmserverrc on logout/login.

If you have set up local mail delivery with a mail server that uses the Maildir format, you may want to receive this mail in KMail. To do so, you can re-use KMail's default receiving account "Local Folders" that stores mail in ~/.local/share/local-mail/.

Symlink the ~/Maildir directory (where Maildir format mail is commonly delivered) to the Local Folders' inbox:

Alternatively, add a new receiving account with the type Maildir and set ~/Maildir as its directory.

Edit config/main.xml files in the /usr/share/plasma. For example, to configure the Application Launcher for all users, edit /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml. To prevent the files from being overwritten with package updates, add the files to Pacman's NoUpgrade

This article or section is a candidate for merging with Power management.

Properly disable the hibernate feature and hide it from the menu with a Polkit policy rule.

Alternatively, add the following lines to a file in /etc/systemd/sleep.conf.d/:

Kwin has the ability to specify rules for specific windows/applications. For example, you can force enable the window titlebar even if the application developer decided that there should not be one. You can set such rules as specific starting position, size, minimize state, keeping above/below others and so on.

To create a rule you can press Alt+F3 when the window of interest is in focus. Then, in More Actions > Configure special application/window settings, you can set the desired property. A list of created rules is available from System Settings > Window Management > Window Rules.

By default KDE mount manager (kio-fuse) will mount network shares to ${XDG_RUNTIME_DIR}/kio-fuse-6-char-random-string.

Create directory, e.g. mnt_kio in your home directory:

Override default kio-fuse.service using a drop-in file:

Now if you mount your network shares via dbus or by openning some file from remote share in Dolphin:

They will be mounted to ~/mnt_kio.

To have the menu bar integrated with the title bar, install material-kwin-decoration-gitAUR from the AUR, then in System Settings > Window Decorations, select 'Material' and add the Application Menu button to the title bar (preferably as second from the left). Works only on X11 session.

Xdg-desktop-portal-kde has support for remote input from a remote desktop session, a virtual KVM switch, kde-connect, emulated devices like a controller using steam-input, etc. This authorization is lost after the application or the desktop-portal is restarted, which causes the "Remote control requested" window pop up every time and makes unattended access impossible.

As of plasma version 6.3, a permission system was implemented, which allows to pre-authorize applications. Currently, the permission api is only available through the flatpak cli, although applications do not need to run as a flatpak to be able to get pre-authorized.

As per the upstream docs and flatpak-permission-set man pages, you need to figure out if the application you want to authorize sets an application ID or not. If started through a runner like KRunner, it gets set by plasma and is usually the filename of the .desktop-file under /usr/share/applications.

For example, to pre-authorize a virtual KVM switch like lan-mouse, you would do:

If you start it as a daemon in a systemd user-unit, you should use the name of that unit instead:

If you application does not set an ID, you can leave that field empty:

Wayland is used by default for KDE 6 applications, and the KDE applications fail to work under GNOME Wayland (and potentially other DEs/WMs) in this scenario. This can be fixed by setting the QT_QPA_PLATFORM=xcb environment variable.

This is a workaround for KDE bugs and not a problem with Wayland itself.

After the last upgrade to KDE 6 you may notice issues with all of the KDE icons not displaying. Newly created accounts showed them just fine.

The issue for this is that the theme got lost while upgrading and had to be reassigned manually. For this go to System Settings > Colors & Themes > Icons and select the theme you would like to use for the icons again.

This article or section is out of date.

Latest update might cause incompatible HiDPI scaling that made some interfaces becomes too big for your screen, some icons are missing or can not be displayed, and missing panels or widgets.

Try to remove qt5ct and kvantum related package, then apply default global Plasma theme. If the problem persists, try clearing all your KDE configuration and reinstalling plasma to overwrite the configuration. Be sure to check HiDPI scaling in KDE system settings as well.

Try to force font DPI to 96 in System Settings > Text & Fonts > Fonts.

If that does not work, try setting the DPI directly in your Xorg configuration as documented in Xorg#Setting DPI manually.

Many problems in KDE are related to its configuration.

Plasma problems are usually caused by unstable Plasma widgets (colloquially called plasmoids) or Plasma themes. First, find which was the last widget or theme you had installed and disable or uninstall it.

So, if your desktop suddenly exhibits "locking up", this is likely caused by a faulty installed widget. If you cannot remember which widget you installed before the problem began (sometimes it can be an irregular problem), try to track it down by removing each widget until the problem ceases. Then you can uninstall the widget, and file a bug report on the KDE bug tracker only if it is an official widget. If it is not, it is recommended to find the entry on the KDE Store and inform the developer of that widget about the problem (detailing steps to reproduce, etc.).

If you cannot find the problem, but you do not want all the settings to be lost, navigate to ~/.config/ and run the following command:

This command will rename all Plasma related configuration files to *.bak (e.g. plasmarc.bak) of your user and when you will relogin into Plasma, you will have the default settings back. To undo that action, remove the .bak file extension. If you already have *.bak files, rename, move, or delete them first. It is highly recommended that you create regular backups anyway. See Synchronization and backup programs for a list of possible solutions.

The problem may be caused by old cache. Sometimes, after an upgrade, the old cache might introduce strange, hard to debug behaviour such as unkillable shells, hangs when changing various settings, Ark being unable to extract archives or Amarok not recognizing any of your music. This solution can also resolve problems with KDE and Qt applications looking bad after an update.

Rebuild the cache using the following commands:

Optionally, empty the ~/.cache/ folder contents, however, this will also clear the cache of other applications:

Sometimes, empty the ~/.cache/ folder does not work, for example, if you encountered the following error:

It might be something related to outdated configuration files. In the above case, moving ~/.config/menus/ folder away may fix the issue. In other cases, try moving each file out of ~/.config/menus/ folder could be a good way to check what triggers the error.

Plasma desktop may use different settings than you set at KDE System Settings panel, or in locale.conf (per Locale#Variables). First thing to do is log out and log in after removing ~/.config/plasma-localerc, if this does not fix the issue, try to edit the file manually. For example, to set LANG variable to es_ES.UTF-8 and the LC_MESSAGES variable to en_US.UTF-8:

Make sure that QT_QPA_PLATFORMTHEME environment variable is unset, the command printenv QT_QPA_PLATFORMTHEME should show empty output. Otherwise if you had an environment set (most likely qt5ct or qt6ct) the variable will force qt5ct/qt6ct settings upon Qt applications, the command export QT_QPA_PLATFORMTHEME= should unset the environment.

An easier (and more reliable) solution can be to uninstall completely qt5ct and qt6ct.

Hiding certain items in the System Tray settings (e.g. Audio Volume, Media Player or Notifications) also disables related features. Hiding the Audio Volume disables volume control keys, Media Player disables multimedia keys (rewind, stop, pause) and hiding Notifications disables showing notifications.

The Login Screen KCM reads your cursor settings from ~/.config/kcminputrc, without this file no settings are synced. The easiest way to generate this file is to change your cursor theme in System Settings > Colors & Themes > Cursors, then change it back to your preferred cursor theme.

A crash or hardware change can modify the screen numbers, even on a single monitor setup. The panels/widgets can be missing after such an event, this can be fixed in the ~/.config/plasma-org.kde.plasma.desktop-appletsrc file by changing the lastScreen values.

Make sure you have the proper driver for your GPU installed. See Xorg#Driver installation for more information. If you have an older card, it might help to #Disable desktop effects manually or automatically for defined applications or #Disable compositing.

Hybrid graphics is a power management strategy commonly used in laptops that keeps the dedicated graphics processor (dGPU) inactive when not needed, defaulting to the integrated graphics processor (iGPU) for basic desktop rendering to conserve battery life.

While this approach saves power, it can result in suboptimal desktop performance, including low frame rates in animations and potential graphical artifacts, even on systems with capable dGPUs.

Forcing KDE Plasma to utilize the discrete GPU can significantly improve desktop responsiveness and visual quality.

For systems using open-source graphics drivers (Intel + AMDGPU, Intel + Nouveau), you can globally set the DRI_PRIME environment variable to specify the dGPU:

The index value (0 or 1) depends on your system configuration. Verify which index corresponds to your dGPU by running:

For direct control over KWin's GPU selection, create a startup script that sets the DRM device priority:

To identify your DRM cards and their corresponding GPUs:

List the dGPU first in the KWIN_DRM_DEVICES variable to prioritize it for rendering.

This command prints out a summary of the current state of KWin including used options, used compositing backend and relevant OpenGL driver capabilities. See more on Martin's blog.

Plasma has desktop effects enabled by default and e.g. not every game will disable them automatically. You can disable desktop effects in System Settings > Window Management > Desktop Effects and you can toggle desktop effects with Alt+Shift+F12.

Additionally, you can create custom KWin rules to automatically disable/enable compositing when a certain application/window starts under System Settings > Window Management > Window Rules.

If you use a transparent background without enabling the compositor, you will get the message:

In System Settings > Display & Monitor > Compositor, check Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Allow applications to block compositing. This may harm performance.

Setting the environment variable QSG_USE_SIMPLE_ANIMATION_DRIVER for KWIN reduces jerking in some Quick Scene Graphics based effects. For this purpose, it is sufficient to create a drop-in for the service running KWIN:

(in the case of Wayland session, use plasma-kwin_wayland.service.d as directory name)

Then restart the session.

Another try is to set QSG_NO_VSYNC instead of QSG_USE_SIMPLE_ANIMATION_DRIVER.

Create the directory ~/.local/share/icons/default/ (alternatively, ~/.icons/default), then, inside it, create a file named index.theme, then add to it the following contents:

If applicable, replace breeze_cursors with the cursor theme you use (cursor themes can be found in /usr/share/icons/, e.g. Breeze_Light).

On Wayland, it is necessary for xdg-desktop-portal-gtk to be installed for GTK/GNOME applications to correctly apply cursor themes.

Firefox and Thunderbird running under Wayland will refer to GSettings to determine which cursor to display.

To sync KDE settings to GTK applications, install kde-gtk-config.

If you do not want to install an extra package, you can set the cursor theme manually:

Try installing the appropriate 2D acceleration driver for your system and window manager.

Your local configuration settings for kscreen can override those set in xorg.conf. Look for kscreen configuration files in ~/.local/share/kscreen/ and check if mode is being set to a resolution that is not supported by your monitor.

In order to add icons to tray, applications often make use of the library appindicator. If your icons are blurry, check which version of libappindicator you have installed. If you only have libappindicator-gtk2AUR installed, you can install libappindicator as an attempt to get clear icons.

When running Plasma in a VMware, VirtualBox or QEMU virtual machine, kscreen may not allow changing the guest's screen resolution to a resolution higher than 800×600.

The workaround is to set the PreferredMode option in xorg.conf.d(5). Alternatively try using a different graphics adapter in the VM, e.g. VBoxSVGA instead of VMSVGA for VirtualBox and Virtio instead of QXL for QEMU. See KDE Bug 407058 for details.

Check whether your user directories (Documents, Downloads, etc.) are read-only.

In System Settings > Display & Monitor > Compositor, change Keep window thumbnails from Only from Shown windows to Never. If you are using Intel graphics, ensure that xf86-video-intel is not installed.

See XDG Desktop Portal#Poor font rendering in GTK applications on KDE Plasma.

You may observe that windows of some applications do not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk.

See Nouveau#Random lockups with kernel error messages.

If there is no sound after suspending and KMix does not show audio devices which should be there, restarting plasmashell and pulseaudio may help:

Some applications may also need to be restarted in order for sound to play from them again.

This can be solved by installing the GStreamer libav plugin (package gst-libav). If you still encounter problems, you can try changing the Phonon backend used by installing another such as phonon-qt6-vlc.

Then, make sure the backend is preferred via phononsettings.

Check if you have plasma-pa installed.

If journalctl -p4 -t pulseaudio contains entries saying Failed to create sink input: sink is suspended, try commenting the following line in /etc/pulse/default.pa:

If the issue persists, plasma-meta or plasma may have installed pulseaudio alongside wireplumber. To fix the issue, replace pulseaudio with pipewire-pulse. If pulseaudio is preferred, replace wireplumber with pipewire-media-session. See PipeWire#PulseAudio clients and this forum thread for more details.

If your system is able to suspend or hibernate using systemd but do not have these options shown in KDE, make sure powerdevil is installed.

Make sure you installed powerdevil and power-profiles-daemon. Run powerprofilesctl and check the driver. If it is intel_pstate or amd_pstate, you are done, otherwise see CPU frequency scaling#Scaling drivers for more information on enabling them.

See [13] for details.

If you want a backup, copy the following configuration directories:

For some IMAP accounts KMail will show the inbox as a top-level container (so it will not be possible to read messages there) with all other folders of this account inside.[14]. To solve this problem simply disable the server-side subscriptions in the KMail account settings.

While setting up EWS account in KMail, you may keep getting errors about failed authorization even for valid and fully working credentials. This is likely caused by broken communication between KWallet and KMail. To workaround the issue set a passsword via qdbus:

See Qt#Disable/Change Qt journal logging behaviour.

See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

It is not recommended to turn off the KWallet password saving system in the user settings as it is required to save encrypted credentials like Wi-Fi passphrases for each user. Persistently occuring KWallet dialogs can be the consequence of turning it off.

In case you find the dialogs to unlock the wallet annoying when applications want to access it, you can let the display managers SDDM and LightDM unlock the wallet at login automatically, see KDE Wallet#Unlock KDE Wallet automatically on login. The first wallet needs to be generated by KWallet (and not user-generated) in order to be usable for system program credentials.

In case you want the wallet credentials not to be opened in memory for every application, you can restrict applications from accessing it with kwalletmanager in the KWallet settings.

If you do not care for credential encryption at all, you can simply leave the password forms blank when KWallet asks for the password while creating a wallet. In this case, applications can access passwords without having to unlock the wallet first.

This can be solved by installing packagekit-qt6.

Discover sometimes will not remove its PackageKit alpm lock. To release it, remove /var/lib/PackageKit/alpm/db.lck. Use "Refresh" in Discover and updates should appear (if there are any updates pending).

As described in KDE Bug 347772 NVIDIA OpenGL drivers and QML may not play well together with Qt 5. This may lead kscreenlocker_greet to high CPU usage after unlocking the session. To work around this issue, set the QSG_RENDERER_LOOP environment variable to basic.

Then kill previous instances of the greeter with killall kscreenlocker_greet.

If your home directory is on a ZFS pool, create a ~/.config/akonadi/mysql-local.conf file with the following contents:

See MariaDB#OS error 22 when running on ZFS.

This is caused by the problematic way of GTK3 handling mouse scroll events. A workaround for this is to set environment variable GDK_CORE_DEVICE_EVENTS=1. However, this workaround also breaks touchpad smooth scrolling and touchscreen scrolling.

When using TeamViewer, it may behave slowly if you use smooth animations (such as windows minimizing). See #Disable compositing as a workaround.

Kmail may become unresponsive, show a black messageviewer or similar, often after having been minimized and restored. A workaround may be to set environment variable QT_QPA_PLATFORM="xcb;wayland". See KDE Bug 397825.

If you previously locked your widgets, you will probably find yourself unable to unlock them again. You just have to run this command to do so:

The new Customize Layout does not require to lock them back up but if want to do that:

Check file associations regarding HTML, PHP, etc... and change it to a browser. KIO's cache files are located in $HOME/.cache/kioexec. See also xdg-utils#URL scheme handlers.

In the System Settings application, KDE offers a setting to automatically lock the screen after waking up from sleep. Upon resuming, some users report that the screen is briefly showed before locking. To prevent this behavior and have KDE lock the screen before suspending, create a hook in systemd(1) by creating the following file as the root user:

The use of sleep is necessary in order for the loginctl lock-session command to complete before the device is suspended. Using a lower timeout may not allow for this to complete.

After creating the file, make it executable.

Finally, make sure that the KDE setting is enabled by going to System Settings > Screen Locking and checking the Lock screen automatically: After waking from sleep checkbox.

Some X11 software like freerdp can grab keyboard input since KDE 5.27. Others like VMware cannot grab correctly. [15]

It is inappropriate to force grab in Xserver or in compositors. [16] You can solve it in an elegant way as follows:

This can be caused because system settings cannot access/modify the .config folder in your home directory.

To fix this, you need to change the owner of the folder:

user refers to the name of the user that you are logged into in KDE Plasma. If the name of your home directory is not the same as the user you are logged in as, you can change it accordingly.

If this does not work, you might need to change the permissions of the folder:

There are issues with the Widget "Global Menu" not working with some applications even after installing appmenu-gtk-module and libdbusmenu-glib. The fix is to install the plasma5-integration and to restart your Session.

The factual accuracy of this article or section is disputed.

It is necessary to add a Polkit rule allowing mounting of internal drives without elevated privileges:

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/plasma-dbus-run-session-if-needed /usr/bin/startplasma-wayland
```

Example 2 (unknown):
```unknown
export DESKTOP_SESSION=plasma
```

Example 3 (unknown):
```unknown
exec startplasma-x11
```

Example 4 (unknown):
```unknown
startx /usr/bin/startplasma-x11
```

---

## GNOME

**URL:** https://wiki.archlinux.org/title/GNOME

**Contents:**
- Installation
- Starting
  - Graphically
  - Manually
    - Session type
    - Start session
  - GNOME applications in Wayland
- Navigation
- Legacy names
- Configuration

GNOME (/(ɡ)noʊm/) is a desktop environment that aims to be simple and easy to use. It is designed by The GNOME Project and is composed entirely of free and open-source software. It uses Wayland, and the available sessions are

The following package groups are available:

The base desktop consists of GNOME Shell, a plugin for the Mutter window manager. It can be installed separately with gnome-shell.

Unstable releases can also be used, see Official repositories#gnome-unstable.

GNOME can be started either graphically with a display manager or manually from the console (some features may be missing). The display manager included in gnome is GDM.

If you installed the gnome group and want GNOME to start automatically on next boot, enable gdm.service. You can then select the desired session: GNOME or GNOME Classic (only displayed if gnome-shell-extensions is installed) from the display manager's session menu.

If you prefer to start GNOME right away, thereby avoiding a reboot, start the aforementioned gdm.service from a graphically unoccupied tty instead.

GNOME session inherits session type from systemd. Systemd session type is determined from XDG_SESSION_TYPE environment variable when the session is started, and can only be changed by the controller of that session afterwards. See the systemd issue on Github.

Therefore merely setting XDG_SESSION_TYPE after login does not work. Instead, create a systemd drop-in file to set environment for getty :

To show session type after reload:

After XDG_SESSION_TYPE and login session type is set correctly, manually starting a Wayland session is possible with:

Running gnome-shell --wayland directly is not recommended, because it lacks session management.

Note that manual invocation of Gnome does not require gdm (consequently also the accompanying gdm.service) at all and is thus also accessible for users with a (possibly very) minimal installation of Gnome composing of a selected few packages included in the more inclusive gnome group in accordance to personal preference.

To start on login to tty1, add to your .bash_profile:

The --no-reexec flag prevents gnome-session from starting a login shell which sources the profile again and loops.

Firefox and QT applications do not respect XDG_SESSION_TYPE, so add variables for them as well:

When the GNOME session is used, GNOME applications will be run using Wayland. For debugging cases, https://docs.gtk.org/gtk3/running.html and https://docs.gtk.org/gtk4/running.html list options and environment variables.

To learn how to use the GNOME shell effectively, read the GNOME Shell Cheat Sheet; it highlights GNOME shell features and keyboard shortcuts. Features include task switching, keyboard use, window control, the panel, overview mode, and more. A few of the shortcuts are:

See /Tips and tricks#Navigation for changes to the default configuration making the window-switching resemble that of Windows.

See Keyboard navigation for more shortcuts.

GNOME Settings (gnome-control-center) and GNOME applications use the dconf configuration system to store their settings.

You can directly access the dconf database using the gsettings(1) command line tool. This also allows you to configure settings not exposed by the user interfaces. Command line tool dconf(1) can directly modify the underlying database, bypassing validation. The configuration keys of gsettings and dconf are equivalent, but in a slightly different format: gsettings set mygroup.mysubgroup mysetting myvalue in gsettings would be dconf write /mygroup/mysubgroup/mysetting myvalue in dconf.

Up until GNOME 3.24, settings were applied by the GNOME settings daemon (located at /usr/lib/gnome-settings-daemon/gnome-settings-daemon), which could be run outside of a GNOME session.

GNOME 3.24, however, replaced the GNOME settings daemon with several separate settings plugins /usr/lib/gnome-settings-daemon/gsd-* which were later moved to /usr/lib/gsd-*. These plugins are now controlled via desktop files under /etc/xdg/autostart/ (matching org.gnome.SettingsDaemon.*.desktop). To run these plugins outside of a GNOME session, you will now need to copy/edit the appropriate desktop entries to ~/.config/autostart.

The configuration is usually performed user-specific; this section does not cover how to create configuration templates for multiple users.

The daemon colord reads the display's EDID and extracts the appropriate color profile. Most color profiles are accurate and no setup is required; however, for those that are not accurate, or for older displays, color profiles can be put in ~/.local/share/icc/ and directed to.

GNOME comes with a built-in blue light filter similar to Redshift. You can enable and customise the time you want to enable Night Light from the display settings menu. Furthermore, you can tweak the kelvin temperature with the following dconf setting, where 5000 is an example value:

If the system has a configured Network Time Protocol daemon, it will be effective for GNOME as well. The synchronization can be set to manual control from the menu, if required.

GNOME supports automatic time zone selection (can be enabled in Date & Time section of the system settings, given that location services are enabled (see Privacy section of the settings).

To show the date in the top bar, execute:

Additionally, to show week numbers in the calendar opened on the top bar, execute:

Upon installing GNOME for the first time, you may find that the wrong applications are handling certain protocols. For example, totem opens videos instead of a previously used VLC. Some of the associations can be set from system settings via Default Applications.

For other protocols and methods, see Default applications for configuration.

Most touchpad settings can be set from system settings via Mouse & Touchpad.

Depending on your device, other configuration settings may be available, but not exposed via the default GUI. For example, a different touchpad click-method

By default, you can use your mouse to move windows by holding down Super, clicking and holding the left mouse button and dragging the mouse around.

Additionally, you can enable using your mouse to resize windows by holding down Super, clicking and holding the right mouse button and dragging the mouse around:

If you don't like the Super key, you can also change the modifier to something else, like Alt or Ctrl:

NetworkManager is the native tool of the GNOME project to control network settings from the shell. If you have not already, install the networkmanager package and enable the NetworkManager.service systemd unit.

While any other network manager can be used alternatively, NetworkManager provides the full integration via the shell network settings and a status indicator applet network-manager-applet (not required for GNOME).

Some online accounts, such as ownCloud, require gvfs-goa and gvfs-dnssd to be installed for full functionality in GNOME applications such as GNOME Files and GNOME Documents [2].

See Online accounts for more information.

The GNOME shell has a search that can be quickly accessed by pressing the Super key and starting to type. The localsearch package is installed by default as a dependency of nautilus from the gnome group and provides an indexing application and metadata database. It can be configured with the Search menu item in Settings. It is started automatically by gnome-session when the user logs in.

localsearch does not automatically recurse into all directories under the user's home directory, so you may need to add custom paths via the Search > Search locations menu item. To exclude a directory from the indexing, create an empty .nomedia file.

A status is available with localsearch status and the indexed content can be searched (localsearch search --help), edited (localsearch tag --help), or reset from the commandline. See localsearch help and localsearch command --help, or the online help for reference.

The database uses tinysparql-sql(1) and can also be queried directly, if needed.

GNOME has accessibility settings available via Settings > Accessibility. The main settings may be toggled directly after enabling a top bar icon, but note further settings are available via the sub-menus for Seeing, Hearing, Typing, Pointing and clicking and Zoom. See https://help.gnome.org/users/gnome-help/stable/a11y.html.en for information on them.

Additionally, a default set of keyboard shortcuts can be set via Settings > Keyboard > View and Customize Keyboard Shortcuts > Accessibility. For example, pressing Alt, Super and 8 toggles zooming.

GNOME 43 comes with a new Device Security panel in Settings. This requires fwupd in order to function. See [3].

As noted above, many configuration options such as changing the GTK theme or the window manager theme are not exposed in GNOME Settings (gnome-control-center). Those users that want to configure these settings may wish to use the GNOME Tweaks (gnome-tweaks), a convenient graphical tool which exposes many of these settings.

GNOME settings (which are stored in the DConf database) can also be configured using the dconf-editor (a graphical DConf configuration tool) or the gsettings command line tool. The GNOME Tweaks does not do anything else in the background of the GUI; note though that you will not find all settings described in the following sections in it.

The catalogue of extensions is available at https://extensions.gnome.org, they can be installed either through official repositories (only a few), the AUR or through the browser.

The factual accuracy of this article or section is disputed.

Installed extensions can also be configured, enabled or disabled through a GUI with gnome-extensions-app, from the command line with gnome-extensions(1), or from the browser. In your browser, extensions can be installed then activated in the browser by setting the switch in right top right of the screen to ON and clicking Install on the popup window (if the extension in question is not installed). Installed extensions may be seen at https://extensions.gnome.org/local/, where available updates can be checked.

The gnome-shell-extensions package provides a set of very useful extensions maintained as part of the GNOME project.

extension-manager is a graphical tool which can also be used to install and remove extensions, as well as enable and disable them, both system-wide and for a user. Prior to using it, consider its list of known issues.

To enable usage of extensions (disabled by default):

To list currently enabled extensions:

The above command may list extensions that have been removed. To only list extensions that are enabled and installed, use gnome-extensions instead:

For more information about GNOME shell extensions, see https://extensions.gnome.org/about/.

GNOME uses Adwaita by default. To apply Adwaita-dark only to GTK 2 applications, use the following symlink:

To select new themes (move them to the appropriate directory and) use GNOME Tweaks or the GSettings commands below.

See GTK#Themes and Icons#Icon themes.

To set the order for the GNOME window manager (Mutter, Metacity):

The theme of GNOME Shell itself is configurable. To use a Shell theme, firstly ensure that you have the gnome-shell-extensions package installed. Then enable the User Themes extension, either through the GNOME Extensions application or through the GNOME Shell Extensions webpage. Shell themes can then be loaded and selected using GNOME Extensions.

There are a number of GNOME Shell themes available in the AUR, many themes do not have the same name format, so instead try searching for the appropriate theme in the AUR. Shell themes can also be downloaded from gnome-look.org.

To enable AppIndicators, which is useful for controlling/monitoring certain applications running in the background, Install gnome-shell-extension-appindicator or gnome-shell-extension-appindicator-gitAUR, restart the GNOME Shell, then enable the AppIndicator extension in the GNOME Extensions application or by running

The GNOME shell animation can be sped up, slowed down or disabled. See GNOME/Tips and tricks#Change animation speed.

Blur my Shell is an extension that adds blur effects to the overview screen as well as the shell itself and other apps. Install gnome-shell-extension-blur-my-shellAUR or gnome-shell-extension-blur-my-shell-gitAUR for development updates. This extension is highly customizable, and you may choose to blur certain applications.

The default Alt-Tab in GNOME is very simple and does not show overviews of the selected windows. You can change the Alt-Tab shortcut from "Switch Applications" to "Switch Windows" in Settings to show window overviews.

You can also use Coverflow Alt-Tab. It is an extension that expands the Alt-Tab behavior and adds features to make switching between applications easier while also giving it a better look. Install gnome-shell-extension-coverflow-alt-tab-gitAUR, then you may change the configuration of this extension to your liking.

Note: Super-` provides "Switch windows of an application` by default.

GNOME implements XDG Autostart.

The gnome-tweaks allows managing autostart-entries.

To move the dash out of the overview and turn it into a dock to easily launch and switch applications, install gnome-shell-extension-dash-to-dockAUR.

Starting from GNOME 40, the desktop will start directly into Overview Mode instead of an empty desktop (like in previous versions). To mimic legacy behaviour, one may install gnome-shell-extension-no-overviewAUR.

Alternatively, you can disable it using gsettings if using gnome-shell-extension-dash-to-dockAUR:

See the discussion at [4].

Unlike other desktop environments, GNOME does not have a built-in tool to manage the clipboard history. This can be done however with the help of an extension. Install gnome-shell-extension-clipboard-indicatorAUR.

To display the current weather information in the top panel based on a chosen location, install gnome-shell-extension-openweatherAUR. The weather information is updated in real-time and displays useful data such as conditions, wind speed, pressure, etc...

This article or section is being considered for removal.

By default, if you want to change your sound input or output device or change your microphone's volume, you need to open GNOME Control Center and configure these settings from there. To integrate a device selector and a microphone volume slider, install gnome-shell-extension-sound-output-device-chooserAUR or gnome-shell-extension-sound-output-device-chooser-gitAUR. Further configuration can be done after installation.

Fonts can be set for Window titles, Interface (applications), Documents and Monospace. See the Fonts tab in the Tweaks for the relevant options.

For hinting, RGBA will likely be desired as this fits most monitors types, and if fonts appear too blocked reduce hinting to Slight or None.

GNOME has integrated support for input methods through IBus. Only ibus and the wanted input method engine (e.g. ibus-libpinyin for Intelligent Pinyin) needed to be installed. After installation, the input method engine can be added as a keyboard layout under Keyboard > Input Sources in GNOME Settings (gnome-control-center).

If you are using an alternative keyboard layout like Neo2 which uses multiple layers/modifiers, you might need to go to Keyboard > Type Special Characters in GNOME Settings (gnome-control-center) and change the Alternate Characters Key away from Right Alt so that it can be used as a native modifier of the keyboard layout. Setting it to e.g. Left Alt prevents Alt+Tab, so be careful what you change it to. Without this change, your left Mod3 key might work, but the right one (AltGr) does not. (As of 2021-05-18)

When you are using a laptop, you might want to alter the following settings controlling behavior when idle, screen lock power button presses and lid close:

To keep the monitor active when the lid is closed:

GNOME 3.24 deprecated the following settings:

The settings panel of GNOME does not provide an option for the user to change the action triggered when the laptop lid is closed. To change the lid switch action system-wide, edit the systemd settings in /etc/systemd/logind.conf. To turn off suspend on lid close, set HandleLidSwitch=ignore, as described in Power management#ACPI events.

The settings panel does not provide an option for changing the critical battery level action. These settings have been removed from dconf as well. They are now managed by upower. Edit the upower settings in /etc/UPower/UPower.conf. Find these settings and adjust to your needs.

Install the power-profiles-daemon optional dependency (of gnome-control-center) for power profiles support. Explicitly starting/enabling the power-profiles-daemon service is unnecessary since gnome-shell and GNOME Settings both request its activation upon launching.

When the service is active, power profiles can be managed through the Power section of GNOME Settings and in the system menu.

The built-in screenshot tool comes without the Screencast option by default. Install the gst-plugin-pipewire optional dependency (of gnome-shell) to enable screen recording.

GNOME Shell does not support using a different window manager, however GNOME Flashback provides sessions for Metacity and Compiz. Furthermore, it is possible to define your own custom GNOME sessions which use alternative components.

Under Wayland, replacing GNOME Shell with a different compositor will cause certain sections of gnome-control-center (GNOME Settings) to populate incorrectly. gnome-control-center will work, but since mutter (GNOME Shell) will not be available to provide settings for populating these sections, they will not have an effect or may not populate accurately with your settings. Sections affected are bluetooth, display, and mouse/touchpad to name a few.

**Examples:**

Example 1 (unknown):
```unknown
gdm.service
```

Example 2 (unknown):
```unknown
gdm.service
```

Example 3 (unknown):
```unknown
XDG_SESSION_TYPE
```

Example 4 (unknown):
```unknown
XDG_SESSION_TYPE
```

---

## Wayland

**URL:** https://wiki.archlinux.org/title/Wayland

**Contents:**
- Requirements
- Compositors
  - Stacking
  - Tiling
  - Dynamic
  - Other
- Display managers
- Xwayland
  - NVIDIA driver
  - Kwin Wayland debug console

Wayland is a display server protocol. It is aimed to become the successor of the X Window System. You can find a comparison between Wayland and Xorg on Wikipedia.

Display servers using the Wayland protocol are called compositors because they also act as compositing window managers. Below you can find a list of Wayland compositors.

For compatibility with native X11 applications to run them seamlessly, Xwayland can be used, which provides an X Server in Wayland.

Most Wayland compositors only work on systems using Kernel mode setting. Wayland by itself does not provide a graphical environment; for this you also need a compositor (see the following section), or a desktop environment that includes a compositor (e.g. GNOME or Plasma).

For the GPU driver and Wayland compositor to be compatible they must support the same buffer API. There are two main APIs: GBM and EGLStreams.

Since NVIDIA introduced GBM support, many compositors (including Mutter and KWin) started using it by default for NVIDIA ≥ 495. GBM is generally considered better with wider support, and EGLStreams only had support because NVIDIA did not provide any alternative way to use their GPUs under Wayland with their proprietary drivers. Furthermore, KWin dropped support for EGLStreams after GBM was introduced into NVIDIA.

If you use a popular desktop environment/compositor and a GPU still supported by NVIDIA, you are most likely already using GBM backend. To check, run journalctl -b 0 --grep "renderer for". To force GBM as a backend, set the following environment variables:

See Window manager#Types for the difference between Stacking, Tiling and Dynamic.

Some of the above may support display managers. Check /usr/share/wayland-sessions/compositor.desktop to see how they are started.

Display managers listed below support launching Wayland compositors.

Provides a TUI menu, but can also be used with other display managers.

Xwayland(1) is an X server that runs under Wayland and provides compatibility for native X11 applications that are yet to provide Wayland support. To use it, install the xorg-xwayland package.

Xwayland is started via a compositor, so you should check the documentation for your chosen compositor for Xwayland compatibility and instructions on how to start Xwayland.

Enabling DRM KMS is required. There may be additional information in the official documentation regarding your display manager (e.g. GDM).

If you use kwin, execute the following to see which windows use Xwayland or native Wayland, surfaces, input events, clipboard contents, and more.

To determine whether an application is running via Xwayland, you can run extramausAUR. Move your mouse pointer over the window of an application. If the red mouse moves, the application is running via Xwayland.

Alternatively, you can use xorg-xeyes and see if the eyes are moving, when moving the mouse pointer over an application window.

Another option is to run xwininfo (from xorg-xwininfo) in a terminal window: when hovering over an Xwayland window the mouse pointer will turn into a + sign. If you click the window it will display some information and end, but it will not do anything with native Wayland windows.You can use Ctrl+C to end it.

You can also use xlsclients (from the xorg-xlsclients package). To list all applications running via Xwayland, run xlsclients -l.

The gtk3 and gtk4 packages have the Wayland backend enabled. GTK will default to the Wayland backend, but it is possible to override it to Xwayland by modifying an environment variable: GDK_BACKEND=x11.

For theming issues, see GTK#Wayland backend.

To enable Wayland support in Qt 5, install the qt5-wayland package. Qt 5 applications will then run under Wayland on a Wayland session.

While it should not be necessary, to explicitly run a Qt application with the Wayland plugin [5], use -platform wayland or QT_QPA_PLATFORM=wayland environment variable.

To force the usage of X11 on a Wayland session, use QT_QPA_PLATFORM=xcb.

This might be necessary for some proprietary applications that do not use the system's implementation of Qt. QT_QPA_PLATFORM="wayland;xcb" allows Qt to use the xcb (X11) plugin instead if Wayland is not available.[6]

The factual accuracy of this article or section is disputed.

On some compositors, for example sway, Qt applications running natively might have missing functionality. For example, KeepassXC will be unable to minimize to tray. This can be solved by installing qt5ct and setting QT_QPA_PLATFORMTHEME=qt5ct before running the application.

Due to the Incorrect sizing and bad text rendering with WebEngine using fractional scaling on Wayland Qt WebEngine bug, applications using Qt WebEngine, for example Calibre, may display jagged fonts. A workaround is launching the application with QT_SCALE_FACTOR_ROUNDING_POLICY=RoundPreferFloor. This prevents the application window being fractional scaled.

The Clutter toolkit has a Wayland backend that allows it to run as a Wayland client. The backend is enabled in the clutter package.

To run a Clutter application on Wayland, set CLUTTER_BACKEND=wayland.

In SDL3, Wayland is used by default to communicate with the desktop compositor.

To run an SDL2 application on Wayland, set SDL_VIDEODRIVER=wayland. SDL_VIDEODRIVER="wayland,x11" allows SDL2 to use the x11 video driver instead if Wayland is not available.[7]. You may also want to install libdecor to enable window decorations (for example, on GNOME).

Refer to the official documentation for more details.

The glfw package has support for Wayland, and uses the Wayland backend if the environment variable XDG_SESSION_TYPE is set to wayland and the application developer has not set a specific desired backend.

See the source code for more information.

If the glew-wayland-gitAUR package does not work with the needed GLEW-based applications, the option is to use glew with Xwayland. See FS#62713.

Enlightenment has complete Wayland support.

To run an EFL-based application on Wayland, set ELM_DISPLAY=wl.

Winit is a window handling library in Rust. It will default to the Wayland backend, but it is possible to override it to Xwayland by modifying environment variables:

Wayland support can be activated using command line flags, or an environment variable.

See Chromium#Native Wayland support to command-line flags needed to work on Wayland. Note that the command-line flag --ozone-platform-hint=auto does not work since Electron 38.

You can pass these flags manually, persist them in an Electron configuration file, or override the .desktop file at ~/.local/share/applications of an application by adding the flags to the end of the Exec= line.

The factual accuracy of this article or section is disputed.

Electron enable WebRTC screen capture over PipeWire by default. The capture is based on xdg-desktop-portal.

A case of missing top bars can be solved by using: --enable-features=WaylandWindowDecorations. This will typically be necessary under GNOME (supported since electron17).

Applications using Electron between versions 28 and 37 can use the environment variable ELECTRON_OZONE_PLATFORM_HINT set to auto or wayland.

This takes lower priority than the command line flags.

The open source implementation of the Java platform OpenJDK, does not yet have native support for Wayland. Until Wakefield, the project that aims to implement Wayland in OpenJDK, is available, Xwayland can be used.

See Debian:Wayland#Java Programs (supported since OpenJDK 16?):

Since XWayland doesn't have full feature parity with Wayland, WLToolkit can be used to fill the gaps while Wakefield isn't ready. It can be activated with -Dawt.toolkit.name=WLToolkit. Some programs such as the JetBrains IDEs support it.

See Input remap utilities.

See Screen capture#Screencasting and Screen capture#Screencast Wayland windows with X11 applications.

This article or section is a candidate for moving to Chromium.

You have to enable Use system title bar and borders via the chrome://settings/appearance menu.

This article or section is a candidate for merging with Clipboard.

Due to Wayland's design philosophy, clipboard data is stored in the memory of the source client. When the client closes, the clipboard data is lost. You can solve this using wl-clip-persist, which runs in the background to reads the clipboard data and stores it in its own memory, separate from the source client.

If you do not want to use a display manager or a shell, you can autostart your Wayland compositor with a systemd service. Adjust the ExecStart line with the compositor you want to use. Here is an example for KDE Plasma:

You can use another wlroots renderer such as vulkan by specifying the WLR_RENDERER environment variable for wlroots based compositor. The list of available ones is on the wlroots documentation.

See Backlight#Color correction.

Gnome-shell users may experience display issues when they switch to Wayland from X. One of the root cause might be the CLUTTER_PAINT=disable-clipped-redraws:disable-culling set by yourself for Xorg-based gnome-shell. Just try to remove it from /etc/environment or other rc files to see if everything goes back to normal.

In contrast to Xorg, Wayland does not allow exclusive input device grabbing, also known as active or explicit grab (e.g. keyboard, mouse), instead, it depends on the Wayland compositor to pass keyboard shortcuts and confine the pointer device to the application window.

This change in input grabbing breaks current applications' behavior, meaning:

Wayland solves this by adding protocol extensions for Wayland and Xwayland. Support for these extensions is needed to be added to the Wayland compositors. In the case of native Wayland clients, the used widget toolkits (e.g GTK, Qt) needs to support these extensions or the applications themselves if no widget toolkit is being used. In the case of Xorg applications, no changes in the applications or widget toolkits are needed as the Xwayland support is enough.

These extensions are already included in wayland-protocols, and supported by xorg-xwayland.

The related extensions are:

Supporting Wayland compositors:

Supporting widget toolkits:

See https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland.

Add __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json as environment variable before launching a Wayland compositor like sway.

Screen magnifying is not solved yet, a pull request was merged mid-2022 providing the protocol wp-surface-scale.

Until this issue is patched in future kernel releases, a workaround is to add amdgpu.dcdebugmask=0x400 to the cmdline.

See: https://community.frame.work/t/wayland-lag-stuttering-since-kernel-6-11-2/59422

**Examples:**

Example 1 (unknown):
```unknown
journalctl -b 0 --grep "renderer for"
```

Example 2 (unknown):
```unknown
GBM_BACKEND=nvidia-drm
__GLX_VENDOR_LIBRARY_NAME=nvidia
```

Example 3 (unknown):
```unknown
/usr/share/wayland-sessions/compositor.desktop
```

Example 4 (unknown):
```unknown
$ qdbus6 org.kde.KWin /KWin org.kde.KWin.showDebugConsole
```

---

## GNOME/Gedit

**URL:** https://wiki.archlinux.org/title/GNOME/Gedit

**Contents:**
- Installation
- Configuration
  - Do not end files with a new line
  - Save backup versions of edited files
  - Syntax highlighting
    - PKGBUILD
- See also

gedit is a general-purpose text editor for GNOME.

Install the gedit package.

For additional features, install the gedit-plugins package.

Gedit can use multiple spell checking dictionaries, see Language checking.

If you want to ensure that gedit does not end files with a newline, execute the following:

If desired, gedit can create a backup copy of an edited file - the contents of the backup file will be the same as the contents of the original file before the edit was made and then saved. The backup file's name will be the same as original file's name but suffixed with a ~ symbol. Hence, for the file called file1 the backup copy would have the name file1~. Backup files are hidden by default.

To enable this behaviour, access gedit's Preferences panel (for GNOME Shell users, this can be found in gedit's global menu). In the preferences panel, click on the Editor tab and tick the option Create a backup copy of files before saving.

Gedit comes out-of-box with several syntax highlight thanks to gtksourceview4, so this section show exceptions.

Install gtksourceview4-pkgbuildAUR to have syntax highlight in PKGBUILDs.

**Examples:**

Example 1 (unknown):
```unknown
$ gsettings set org.gnome.gedit.preferences.editor ensure-trailing-newline false
```

---

## Desktop notifications

**URL:** https://wiki.archlinux.org/title/Notification

**Contents:**
- Libnotify
- Notification servers
  - Built-in
  - Standalone
- Tips and tricks
  - Send notifications to another user
  - Replace previous notification
  - Include Buttons or listen for close/on-click of the notification
  - Multiple notification servers with D-Bus services
- Troubleshooting

Desktop notifications are small, passive popup dialogs that notify the user of particular events in an asynchronous manner.

libnotify is a desktop-independent implementation of the Desktop Notifications Specification, which provides notify-send(1) utility and support for GTK and Qt applications. It is already used by many open source applications like Evolution and Pidgin.

In order to receive notifications sent via libnotify, a notification server is required.

Cinnamon, Deepin, Enlightenment, GNOME, and GNOME Flashback use their own implementations to display notifications, and may not be able to be replaced since their notification servers are started automatically on login to receive notifications from applications via DBus.

On KDE Plasma if you enter the configuration for the System Tray you can disable the built-in notification server under System Services by changing the drop-down next to Notifications to Disabled. You can then add your preferred notification server in the System Settings menu under System / Autostart by adding a new Autostart application. You will need to log out and back in to take effect.

In other desktop environments, a notification server needs to be manually installed and launched using e.g. XDG Autostart.

Alternatively, by making the notification server a D-Bus service, the notification server can be launched automatically on the first call to it. Most notification servers already ship a dbus service under /usr/share/dbus-1/services. For some implementations, e.g. notification-daemon package, it's necessary to create one manually in the user D-Bus services directory ($XDG_DATA_HOME/dbus-1/services):

Whenever an application sends a notification by sending a signal to org.freedesktop.Notifications, D-Bus activates /usr/lib/notification-daemon-1.0/notification-daemon if it has not already been activated.

You can also choose one of the following implementations:

systemd-run(1) can be used to enter another user's session and send notifications to them, e.g. from a background script running as root:

Another possibility is to use systembus-notify. The following command will show a notification to all users who run systembus-notify in their user session:

Notifications can be replaced if their ID is known; if a new notification request specifies the same ID, it will always replace the old notification. Unfortunately notify-send does not report this ID, so alternative tools are required to do this on CLI. One capable CLI-tool is the notify-send.py python script, which provides notify-send syntax with additional ID-reporting and replacing capabilities.

However, with some notification servers (such as Notify-OSD), you can use the string:x-canonical-private-synchronous: hint with notify-send to achieve the same result.

For example, to get a notification displaying time:

With the notify-send.py script, actions can be used to display buttons or to listen for the default-action of the notification (usually, when the user clicks on it) and the close-action. When the action-icons hint is set to true and the notification daemon supports this, the buttons will display icons instead of text. The script prints the action identifier or "close" to the command line when the corresponding event has occured. To listen for the default action (on-click), one has to use the action-identifier "default".

Example with icons on buttons:

As described in the section Standalone, users can create a D-Bus service so that a notification server can be launched automatically. Some implementations already include the D-Bus service files. However, this causes a problem when multiple notification servers are installed and when some of them come with the service files. For example, installing both dunst and mako without explicitly specifying the desired server, D-Bus then chooses one for the users, and the decision is out of users' control. To avoid the situation, you can override the service used by creating an org.freedesktop.Notifications.service (see #Standalone) and pointing to the service you want to use, then restarting the session.

If applications hang when attempting to show notifications, it might be because of a notification service falsely advertising its availability through the D-Bus service.

For instance, suppose a user recently installed a KDE component that requires plasma-workspace, but the user is still running XFCE. In this case, the KDE notifier will be prioritized, but the user is not running it. The application will hang while waiting for the service, and only after a timeout will it fall back to xfce4-notifyd.

The most noticeable hanging might come from the volume indicator scroll adjustment.

If you are in this situation, you should have two notification handlers:

Of those two, one fails regularly after a 1-minute timeout, as seen in the journal:

Choosing the service you want to use as described in #Multiple notification servers with D-Bus services will fix the problem.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/dbus-1/services
```

Example 2 (unknown):
```unknown
$XDG_DATA_HOME/dbus-1/services
```

Example 3 (unknown):
```unknown
org.freedesktop.Notifications.service
```

Example 4 (unknown):
```unknown
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

---

## Baloo

**URL:** https://wiki.archlinux.org/title/Baloo

**Contents:**
- Installation
- Usage and configuration
- Command-line usage
- Indexing a removable or remote device
- Disabling the indexer
- Troubleshooting
  - Inotify folder watch limit error
  - Plasma Vault Files are indexed and available even when vault is closed

Baloo is a file indexing and searching framework for KDE Plasma.

Install the baloo package.

In order to search using Baloo on the Plasma desktop, start KRunner (default keyboard shortcut Alt+F2) and type in your query. Within Dolphin press Ctrl+f.

By default the Desktop Search KCM exposes only two options: A panel to blacklist folders and a way to disable it with one click. Alternatively you can edit your ~/.config/baloofilerc file (info).

Additionally the balooctl6 process can also be used to control Baloo, e.g. in order to stop/start Baloo use balooctl6 suspend or balooctl6 resume to resume.

Once you added additional folders to the blacklist or disabled Baloo entirely, a process named baloo_file_cleaner removes all unneeded index files automatically. These are stored under ~/.local/share/baloo/.

Support for range queries:

Groups and OR/AND operators:

For a list of all supported filter properties available, see (info).

Note that text search index breaks down all metadata (including filenames) into "words", and does all its searches over it from the beginning of the word only. What this means is that while baloosearch "tutorial" would match my_great_tutorial.txt, baloosearch "utorial" would not match it. To see what "words" baloo stored in the index for a particular file do:

By default every removable and remote device is blacklisted. It is possible to remove devices from the blacklist in the KCM panel.

To disable the Baloo file indexer:

The indexer will be disabled on next login.

Alternatively, disable Enable File Search in System settings under Search > File search.

To permanently delete the index database, run:

This will also resolve the following error message in file dialogs and other applications (KDE bug 437176):

If you get the following error:

Then you will need to increase the inotify folder watch limit:

To make changes permanent, create a sysctl configuration file:

This is a major security bug not yet fixed. Any file inside vault is by default indexed and available through file manager search, Krunner and Kickoff.

One workaround is to stop folder(s) from being indexed by Baloo. The relevant options are available in System Settings > Search > File Search > Folder specific configuration > Add folder configuration > Stop indexing a folder. After adding the desired folder, the existing Baloo data needs to be removed and freshly indexed again:

**Examples:**

Example 1 (unknown):
```unknown
~/.config/baloofilerc
```

Example 2 (unknown):
```unknown
balooctl6 suspend
```

Example 3 (unknown):
```unknown
balooctl6 resume
```

Example 4 (unknown):
```unknown
baloo_file_cleaner
```

---

## GNOME/Flashback

**URL:** https://wiki.archlinux.org/title/GNOME/Flashback

**Contents:**
- Installation
- Starting
  - Graphical log-in
  - Manually
- Configuration
  - Customizing GNOME Panel
  - Alternative window manager
- Tips and tricks
  - Panel speed settings
  - Replace applications menu icon

GNOME Flashback (previously called GNOME fallback mode) is a shell for GNOME 3. The desktop layout and the underlying technology is similar to GNOME 2. It does not use 3D acceleration at all, so it is generally faster and less CPU intensive than GNOME Shell with llvmpipe.

GNOME Flashback can be installed from the gnome-flashback package. It is recommended to install its optional dependencies also to get a more complete desktop environment.

You can also install the following packages which provide some additional applets for the GNOME Panel:

It is recommended to install the gnome group, which contains applications required for the standard GNOME experience.

Choose GNOME Flashback (Metacity) from the menu in a display manager of choice.

Those who wish to use Compiz with GNOME Flashback should select GNOME Flashback (Compiz) instead.

After editing .xinitrc, GNOME Flashback can be launched with startx. See xinitrc for details.

GNOME Flashback shares most of its settings with GNOME. See GNOME#Configuration for more details.

You can use an alternative window manager with GNOME Flashback by creating a custom GNOME session with the following components:

where window-manager is the window manager you wish to use. See GNOME/Tips and tricks#Custom GNOME sessions.

Also see this article on running awesome as the window manager in GNOME.

To adjust the amount of time it takes for the panel to disappear or reappear when autohide is enabled, execute the following:

where panel is either top-panel or bottom-panel and time is a value in miliseconds, e.g. 300.

To set the speed at which panel animations occur, execute the following:

where panel is either top-panel or bottom-panel and value is either "'fast'", "'medium'" or "'slow'".

Replace /usr/share/icons/icon-theme/16x16/places/start-here.png with your own icon (where icon-theme is the name of your icon theme).

After making the change, restart GNOME Panel: gnome-panel --replace.

**Examples:**

Example 1 (unknown):
```unknown
export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
exec gnome-session --session=gnome-flashback-metacity
```

Example 2 (unknown):
```unknown
export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
exec gnome-session --session=gnome-flashback-compiz
```

Example 3 (unknown):
```unknown
RequiredComponents=gnome-flashback-init;gnome-flashback;gnome-panel;window-manager;gnome-settings-daemon;nautilus-classic;
```

Example 4 (unknown):
```unknown
RequiredComponents=gnome-flashback-init;gnome-flashback;gnome-panel;window-manager;gnome-settings-daemon;nautilus-classic;
```

---

## GNOME/Web

**URL:** https://wiki.archlinux.org/title/Epiphany

**Contents:**
- Installation
- Configuration
  - Blocking advertisements
  - Tracking Prevention
  - Firefox Sync
  - Web applications
  - Custom stylesheet
  - Fonts
  - Video
  - Hardware accelerated compositing

Web is the default web browser for GNOME. Web provides a simple and minimalist interface for accessing the internet. Whilst it is developed primarily for GNOME, Web works acceptably in other desktop environments as well.

Web can be installed with the epiphany package. If you want to save login passwords, install gnome-keyring.

Enabled by default, one can disable it by unchecking Block Advertisements in Preferences. EasyList is the default blocking list. All lists are periodically refreshed.

To get list of currently enabled filters:

The filters can be modified using a JSON-formatted resource following examples at https://gitlab.com/eyeo/filterlists/contentblockerlists:

Web includes Intelligent Tracker Prevention, which can be enabled in Preferences.

Web allows the usage of Firefox Sync to sync bookmarks, history, passwords and open tabs. It can be configured in the Import and Export dropdown menu.

Web can create web applications out of websites and add them to desktop menu. To configure and remove them enter about:applications in the address bar.

Web supports custom stylesheet you can enable under Fonts and style in Preferences.

Use example below to set new tab page layout and colors according to Adwaita dark variant:

Web does not check GNOME font settings, but checks Font configuration.

See GStreamer for required plugin installation.

To enable hardware accelerated video decoding, see GStreamer#Hardware video acceleration and #Hardware accelerated compositing.

By default hardware accelerated compositing is only used when required (on-demand) to display 3D transforms.

To force enable hardware accelerated compositing:

Web doesn't respect socks_proxy, instead, you can set http_proxy to a socks:// URL :

More information: Proxy server#Environment variables

By default, Web should work with your system language if the Spell Checking option is enabled in Preferences and relevant dictionaries are installed on your system. Additional languages have to be added to the Languages list in Web's preferences from a list of available ones. That list only shows languages for which the Locale has been enabled on your system. The selection of languages in Preferences controls both spell checking and also the Accept-Language header.

**Examples:**

Example 1 (unknown):
```unknown
$ gsettings get org.gnome.Epiphany content-filters
```

Example 2 (unknown):
```unknown
$ gsettings set org.gnome.Epiphany content-filters "['https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist_min_content_blocker.json', 'https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist+easylistchina-minified.json']"
```

Example 3 (unknown):
```unknown
about:applications
```

Example 4 (unknown):
```unknown
~/.config/epiphany/user-stylesheet.css
```

---

## xinit

**URL:** https://wiki.archlinux.org/title/Start_X_at_login

**Contents:**
- Installation
- Configuration
  - xinitrc
  - xserverrc
    - Passing virtual terminal number
- Usage
- Tips and tricks
  - Override xinitrc
  - Autostart X at login
  - Switching between desktop environments/window managers

xinit is typically used to start window managers or desktop environments. While you can also use xinit to run GUI applications without a window manager, many graphical applications expect an EWMH compliant window manager. Display managers start Xorg for you and generally source xprofile.

Install the xorg-xinit package.

xinit and startx take an optional client program argument, see #Override xinitrc. If you do not provide one they will look for ~/.xinitrc to run as a shell script to start up client programs.

~/.xinitrc is handy to run programs depending on X and set environment variables on X server startup. If it is present in a user's home directory, startx and xinit execute it. Otherwise startx will run the default /etc/X11/xinit/xinitrc.

This default xinitrc will start a basic environment with Twm, xorg-xclock and Xterm (assuming that the necessary packages are installed). Therefore, to start a different window manager or desktop environment, first create a copy of the default xinitrc in your home directory:

Then edit the file and replace the default programs with desired commands. Remember that lines following a command using exec would be ignored. For example, to start xscreensaver in the background and then start openbox, use the following:

Long-running programs started before the window manager, such as a screensaver and wallpaper application, must either fork themselves or be run in the background by appending an & sign. Otherwise, the script would halt and wait for each program to exit before executing the window manager or desktop environment. Note that some programs should instead not be forked, to avoid race bugs, as is the case of xrdb. Prepending exec will replace the script process with the window manager process, so that X does not exit even if this process forks to the background.

The xserverrc file is a shell script responsible for starting up the X server. Both startx and xinit execute ~/.xserverrc if it exists, startx will use /etc/X11/xinit/xserverrc otherwise.

See Xserver(1) for a list of all command line options.

In order to maintain an authenticated session with logind and to prevent bypassing the screen locker by switching terminals, Xorg has to be started on the same virtual terminal where the login occurred [1]. For this purpose, Xorg needs to be passed the number of the current virtual terminal.

If you are invoking startx, nothing more needs to be done – it contains logic to compute and pass the virtual terminal number to Xorg.

In other cases, e.g. if you are running xinit, it is recommended to specify vt$XDG_VTNR in the ~/.xserverrc file:

To run Xorg as a regular user, issue:

Or if #xserverrc is configured:

Your window manager (or desktop environment) of choice should now start correctly.

To quit X, run your window manager's exit function (assuming it has one). If it lacks such functionality, run:

If you have a working ~/.xinitrc but just want to try other window manager or desktop environment, you can run it by issuing startx followed by the path to the window manager, for example:

If the binary takes arguments, they need to be quoted to be recognized as part of the first parameter of startx:

Note that the full path is required. You can also specify custom options for the #xserverrc script by appending them after the double dash -- sign:

Make sure that startx is properly configured.

Place the following in your login shell initialization file (e.g. ~/.bash_profile for Bash or ~/.zprofile for Zsh):

You can replace the -eq comparison with one like -le 3 (for vt1 to vt3) if you want to use graphical logins on more than one virtual terminal.

Alternative conditions to detect the virtual terminal include "$(tty)" = "/dev/tty1", which does not allow comparison with -le, and "$(fgconsole 2>/dev/null || echo -1)" -eq 1, which does not work in serial consoles.

The exec command ensures that the user is logged out when the X server exits, crashes or is killed by an attacker. If you want to take the risk and remain logged in when the X session ends, remove exec.

See also fish#Start X at login.

If you are frequently switching between different desktop environments or window managers, it is convenient to either use a display manager or expand ~/.xinitrc to make the switching possible.

The following example shows how to start a particular desktop environment or window manager with an argument:

To pass the argument session:

It is possible to start only specific applications without a window manager, although most likely this is only useful with a single application shown in full-screen mode. For example:

Alternatively the binary can be called directly from the command prompt as described in #Override xinitrc.

With this method you need to set each application's window geometry through its own configuration files (if possible at all).

See also Display manager#Starting applications without a window manager.

See Xorg#Session log redirection for details.

This article or section is a candidate for moving to Xorg.

Useful for running graphical applications:

Install xorg-server-xvfb, then run xvfb-run command.

**Examples:**

Example 1 (unknown):
```unknown
/etc/X11/xinit/xinitrc
```

Example 2 (unknown):
```unknown
$ cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

Example 3 (unknown):
```unknown
xscreensaver
```

Example 4 (unknown):
```unknown
...
xscreensaver &
exec openbox-session
```

---

## Window manager

**URL:** https://wiki.archlinux.org/title/Window_manager

**Contents:**
- Overview
  - Types
- List of window managers
  - Stacking window managers
  - Tiling window managers
  - Dynamic window managers
- See also

It can be part of a desktop environment or be used standalone.

Window managers are X clients that control the appearance and behaviour of the frames ("windows") where the various graphical applications are drawn. They determine the border, title bar, size, and ability to resize windows, and often provide other functionality such as reserved areas for sticking dockapps like Window Maker, or the ability to tab windows like Fluxbox. Some window managers are even bundled with simple utilities like menus to start programs or to configure the window manager itself.

The Extended Window Manager Hints specification is used to allow window managers to interact in standard ways with the server and the other clients.

Some window managers are developed as part of a more comprehensive desktop environment, usually allowing the other provided applications to better interact with each other, giving a more consistent experience to the user, complete with features like desktop icons, fonts, toolbars, wallpapers, or desktop widgets.

Other window managers are instead designed to be used standalone, giving the user complete freedom over the choice of the other applications to be used. This allows the user to create a more lightweight and customized environment, tailored to their own specific needs. "Extras" like desktop icons, toolbars, wallpapers, or desktop widgets, if needed, will have to be added with additional dedicated applications.

Some standalone window managers can be also used to replace the default window manager of a desktop environment, just like some desktop environment–oriented window managers can be used standalone too.

Prior to installing a window manager, a functional X server installation is required. See Xorg for detailed information.

See Comparison of tiling window managers and Wikipedia:Comparison of X window managers for comparison of window managers.

---

## Desktop environment

**URL:** https://wiki.archlinux.org/title/Desktop_environment

**Contents:**
- List of desktop environments
  - Officially supported
  - Unofficially supported
- Custom window manager
- Custom environments

A desktop environment (DE) is an implementation of the desktop metaphor made of a bundle of programs, which share a common graphical user interface (GUI).

A desktop environment bundles together a variety of components to provide common graphical user interface elements such as icons, toolbars, wallpapers, and desktop widgets. Additionally, most desktop environments include a set of integrated applications and utilities. Most importantly, desktop environments provide their own window manager, which can however usually be replaced with another compatible one.

The user is free to configure their GUI environment in any number of ways. Desktop environments simply provide a complete and convenient means of accomplishing this task. Note that users are free to mix-and-match applications from multiple desktop environments. For example, a Plasma user may install and run GNOME applications such as the Epiphany web browser, should they prefer it over KDE Konqueror web browser. One drawback of this approach is that many applications provided by desktop environment projects rely heavily upon the libraries underlying the respective desktop environment. As a result, installing applications from a range of desktop environments will require installation of a larger number of dependencies. Users seeking to conserve disk space often avoid such mixed environments, or choose alternatives which do depend on only few external libraries.

Furthermore, applications provided by desktop environments tend to integrate better with their native environments. Superficially, mixing environments with different widget toolkits will result in visual discrepancies (that is, interfaces will use different icons and widget styles). In terms of usability, mixed environments may not behave similarly (e.g. single-clicking versus double-clicking icons; drag-and-drop functionality) potentially causing confusion or unexpected behavior.

Some desktop environments support using a non-default window manager, such as i3.

Desktop environments represent the simplest means of installing a complete graphical environment. However, users are free to build and customize their graphical environment in any number of ways if none of the popular desktop environments meet their requirements. Generally, building a custom environment involves selection of a suitable window manager or compositor, a taskbar and a number of applications (a minimalist selection usually includes a terminal emulator, file manager, and text editor).

Other components usually provided by desktop environments are:

---

## File manager functionality

**URL:** https://wiki.archlinux.org/title/File_manager

**Contents:**
- Overview
- Additional features
  - Mounting
    - File manager daemon
    - Standalone
  - Networks
    - Windows access
    - Apple access
    - sftp access
    - WebDAV

This article outlines the additional software packages necessary to expand the features and functionality of file managers, particularly where using a window manager such as Openbox. The ability to access partitions and removable media without a password—if affected—has also been provided.

A file manager alone will not provide the features and functionality that users of full desktop environments such as Plasma or Xfce will be accustomed to. This is because additional software packages will be required to enable a given file manager to:

When a file manager has been installed as part of a full desktop environment, most of these packages will usually have been installed automatically. Consequently, where a file manager has been installed for a standalone window manager then - as is the case with the window manager itself - only a basic foundation will be provided. The user must then determine the nature and extent of the features and functionality to be added.

This article or section needs expansion.

When using a lightweight environment, the more added file manager features, the more memory usage is needed. See also udisks.

Folders used by GVFS:

Additional packages for installation usually follows the gvfs-* pattern, for example:

Most graphical file managers have the ability to automount devices plugged in while the program is running. You can leverage this for a system-wide solution by running the file manager in daemon mode (i.e. as a background process), if supported. For example, when using PCManFM in Openbox, the following command would be added to the ~/.config/openbox/autostart file:

It will also be necessary to configure the file manager itself in respect to volume management (e.g. what it will do and what applications will be launched when certain file types are detected upon mounting).

Another option is to install a separate mount application. The advantages of using this are:

If using gvfs-smb, to access Windows/Cifs/Samba file shares first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

AFP support is included in gvfs. To access AFP files first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

SFTP support is also included in gvfs. To access folders via sftp, open the file manager, and enter the following into the path name, changing user@server_name and folder_name as appropriate:

For WebDAV, install gvfs-dnssd.

The following packages enable thumbnailing in most file managers, such as PCManFM, SpaceFM, Thunar, and xfeAUR. They are not needed for KDE's Dolphin or Konqueror, which use a separate thumbnailing system.

tumbler is the core backend for thumbnailing in many file managers. This must be installed to enable thumbnailing for various file types. It is not required for GNOME Files.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

PCManFM supports image thumbnails out of the box. However, in order to view thumbnails of other file types, PCManFM uses the information provided in the files located at /usr/share/thumbnailers. The packages which provide a thumbnailer usually add the corresponding .thumbnail file at /usr/share/thumbnailers. For example, in order to get thumbnails for OpenDocument files, you may install libgsf from the official repositories. For video files' thumbnails, the package ffmpegthumbnailer is required. For PDF files, you may install evince from the official repositories, which provides evince-thumbnailer and the corresponding file at /usr/share/thumbnailers. However, if you prefer not to install evince, you can also replicate the functionality of evince-thumbnailer using imagemagick's convert command. This is accomplished by creating a new file with the .thumbnailer extension (e.g.: imagemagick-pdf.thumbnailer) at /usr/share/thumbnailers with the following content:

Following this example, you can specify custom thumbnailers by creating your own .thumbnail files. Keep in mind that %i refers to the input file (the file which will have its thumbnail made), %o to the output file (the thumbnail image) and %s to the size of the thumbnail. These parameters will be automatically substituted with the corresponding data and passed to the thumbnailer program by PCManFM.

To extract compressed files such as tarballs (.tar and .tar.gz) within a file manager, it will first be necessary to install a GUI archiver such as file-roller. See List of applications/Utilities#Archiving and compression tools for further information. An additional package such as unzip must also be installed to support the use of zipped .zip files. Once an archiver has been installed, files in the file manager may consequently be right-clicked to be archived or extracted.

Archive files are mounted under folder /run/user/$(id -u)/gvfs/ with automatically created mount point that contains full path to the file in its name where all / are replaced with %252F and : replaced with %253A hex codes.

Example of path to the mounted archive /full/path/to/file/name.zip

See the NTFS article.

Some file managers make use of desktop notifications to confirm various events and statuses like mounting, unmounting and ejection of removable media.

The factual accuracy of this article or section is disputed.

Make trash directories .Trash-<uid> for each users on the top level of filesystems:

For example (mount point: /media/sdc1, uid: 1000, gid: 1000):

File managers using udisks require a polkit authentication agent. See polkit#Authentication agents.

The need to enter a password to access other partitions or mounted removable media will likely be due to the default permission settings of udisks2. More specifically, permission may be set to the root account only, not the user account. See Udisks#Configuration for details.

You may find that an application that is not a file manager, Audacious or Visual Studio Code for example, is set as the default application for opening directories — an application that specifies that it can handle the inode/directory MIME type in its desktop entry can become the default. You can query the default application for opening directories with the following command:

To ensure that directories are opened in the file manager, run the following command:

where my_file_manager.desktop is the desktop entry for your file manager — org.gnome.Nautilus.desktop for example.

Some other applications instead use the org.freedesktop.FileManager1 D-Bus protocol (e.g. Firefox). The following shows a list of currently installed services supporting this protocol:

To change what file manager is opened, symlink the file to $XDG_DATA_HOME/dbus-1/services/ or $HOME/.local/share/dbus-1/services/ if XDG_DATA_HOME variable is empty. Additionally, before the changes become active, kill the program currently implementing the D-Bus service.

Due to this gvfs commit you need to create your mount point inside /media/your-user-name/.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/gvfs/mounts/
```

Example 2 (unknown):
```unknown
~/.gvfs/mounts
```

Example 3 (unknown):
```unknown
~/.config/openbox/autostart
```

Example 4 (unknown):
```unknown
pcmanfm -d &
```

---

## GNOME/Troubleshooting

**URL:** https://wiki.archlinux.org/title/GNOME/Troubleshooting

**Contents:**
- Shell freezes
- Incorrect application defaults
- Search does not list any local files
- GNOME Online Accounts settings page does not show properly
- GNOME Online Accounts blank pop-up window when logging in
- Cannot change settings in dconf-editor
- When an extension breaks the shell
- Extensions do not work after GNOME 3 update
- Keyboard shortcut do not work with only conky running
- Unable to apply stored configuration for monitors

In the event of a shell freeze (which might be caused by certain appearance tweaks, malfunctioning extensions or perhaps a lack of available memory), restarting the shell by pressing Alt+F2 and then entering r may not be possible.

In this case, try switching to another TTY (Ctrl+Alt+F2) and entering the following command: pkill -HUP gnome-shell. It may take a few seconds before the shell successfully restarts. On X11, restarting the shell in this fashion should not log the user out, but it is a good idea to try and ensure that all work is saved anyway; on Wayland (currently the default), restarting the shell kills the whole session, so everything will be lost.

If this fails, the Xorg server will need to be restarted either by pkill X for console logins or by restarting gdm.service for GDM logins. Bear in mind that restarting the Xorg server will log the user out, so try to ensure that all work is saved before attempting this.

When installing applications for the first time you may find that GNOME has the wrong application associated to a certain protocols - for instance, easytag becomes the folder handler instead of GNOME Files.

For GNOME Files see the following page: GNOME Files#Files is no longer the default file manager.

To query the current associated application and recommended apps for pdfs in this case run:

To change the default app for pdfs to Document Viewer, run the following command:

For other applications, default handler settings are detailed on the following page: Default applications.

Optionally, you can install gnome-defaults-listAUR. It will place your configuration file at /usr/share/applications/gnome-mimeapps.list.

There is another mime type association command. If the current associated app queried using xdg-mime query default <mime-type> is already correct, but still the wrong app is handling the type, try this:

In order for Gnome's localsearch tool to index your local files, they must be stored in an XDG compliant directory (such as 'Documents' or 'Music'). For more information, see XDG user directories.

You can also configure localsearch to recursively search inside specific directories. These can be specified via Settings > Search > Search locations.

In some cases, due to interactions with Alacarte (menu editor), GNOME Online accounts settings page would not show. If that happens, "Restore System Configuration" in Alacarte can restore missing functions to gnome-control-center. (See https://bugzilla.redhat.com/show_bug.cgi?id=1520431.)

Some services require authentication to log in (Google, Microsoft, etc.), so in some situations (such as Nvidia drivers) the popup will go blank instead of redirecting to the login page. To solve this problem, temporarily disable WebKit Composite.

When one cannot set settings in dconf, it is possible their dconf user settings are corrupt. In this case it is best to delete the user dconf files in ~/.config/dconf/user* and set the settings in dconf-editor after.

When enabling shell extensions causes GNOME breakage, you should first remove the user-theme and auto-move-windows extensions from their installation directory.

The installation directory could be one of ~/.local/share/gnome‑shell/extensions, /usr/share/gnome‑shell/extensions or /usr/local/share/gnome‑shell/extensions. Removing these two extension-containing folders may fix the breakage. Otherwise, isolate the problem extension with trial‑and‑error.

Removing or adding an extension-containing folder to the aforementioned directories removes or adds the corresponding extension to your system. Details on GNOME Shell extensions are available at the GNOME web site.

If you have trouble with uninstalling an extension via extensions.gnome.org/local, then probably they have been installed as system-wide extensions with the gnome-shell-extensions package. Removing the package again obviously affects all user accounts.

Before trying the workarounds below, check if an update is available for the extension by visiting extensions.gnome.org/local.

If there is no update for your current GNOME version yet, use the following command to disable version validation for extensions:

Alternatively, you could modify the extension itself, changing the supported shell version to satisfy the version validation. See the method below.

Locate the folder where your extensions are installed. It might be ~/.local/share/gnome-shell/extensions or /usr/share/gnome-shell/extensions.

Edit each occurrence of metadata.json which appears in each extension sub-folder.

"3.x" indicates the extension works with every shell version. If it breaks, you will know to change it back.

The GNOME shell keyboard shortcuts like Alt+F2, Alt+F1, and the media key shortcuts do not work if conky is the only program running. However, if another application like gedit is running, then the keyboard shortcuts work.

Solution: edit .conkyrc

If you encounter this message try to disable the xrandr gnome-settings-daemon plugin:

See Cursor themes#Desktop environments.

In GNOME 3.6 and above, the mouse button modifier (the key that allows you to drag a window from a location other than the titlebar) is the Super key instead of the Alt key which was used in the past. The change was made in response to the following bug report.

To change the mouse button modifier back to the Alt key, execute the following:

Problems with the loading of system icons, such the ones in the title bar of Files, might be solved by executing the following command:

Running the aforementioned command may also fix repeated occurrences of the "Oh no! Something has gone wrong!" error screen and/or very slow loading and login with GDM as described in the following forum thread.

Maximizing windows may cause artifacts as of GNOME 3.12.0 - see the following forum thread and bug report. A solution is detailed in the following section: #Tear-free video with Intel HD Graphics.

According to a bug report, DRI3 includes the buffer_age extension that allows GNOME Shell's Mutter compositor to sync windows to vblank in an efficient way. Since version 1:2.99.917+682+g4eaab17-1, DRI3 is enabled by default in xf86-video-intel [1].

Enabling the Xorg Intel TearFree option is a known workaround for tearing problems on Intel adapters. However, the way this option acts increases memory consumption and lowers performance, see the original bug report's final comment.

GNOME Shell's Mutter compositor has a tweak known to address tearing problems (see the original suggestion for this fix and its mention in the Freedesktop bug report). To enable this tweak, append the following line to /etc/environment: CLUTTER_PAINT=disable-clipped-redraws:disable-culling. Then restart the Xorg server.

GNOME Shell does by default unredirect fullscreen applications. This may result in tearing. You can disable this with the gnome shell extension gnome-shell-extension-disable-unredirectAUR.

This is possibly a bug in GNOME Shell which causes new windows to open behind others. To fix this issue, one can run the following command:

Some laptops have a touchpad lock button that disables the touchpad so that users can type without worrying about touching the touchpad. Currently, it appears that although GNOME can lock the touchpad by pressing this button, it cannot unlock it. If the touchpad gets locked you can run the following to unlock it:

A menu showing the keyboard input sources (for example 'en' for an English keyboard layout) should be visible next to the status area containing icons for network, volume and power sources. If the keyboard sources menu is not visible, this is probably because you have configured your Xorg keyboard layout in a way which GNOME does not recognise.

To ensure that the menu is visible, remove any Xorg keyboard configuration you might have created and set the keyboard locale using localectl.

Upon running the command and then logging out, you should find that the keyboard input sources menu is visible in GDM and in the GNOME Shell desktop. See Input sources in GNOME for more information.

When using a separate window manager with gnome-settings-daemon, the mouse cursor may vanish. Run:

If XScreenSaver is installed, ensure that it is not running at startup, see GNOME#Autostart.

If you are running PulseAudio in system-wide mode, the PulseAudio 7.0 upgrade breaks GDM and GNOME. See this forum post for more information.

The dash is the "toolbar" that appears, by default, on the left when you click Activities. Applications can be reordered in the dash by dragging and dropping. If this fails, and/or causes GNOME to crash, try changing your icon theme.

See Codecs and containers#No H264, mpg4 or Musepack (.mpc) in Totem Player.

GNOME defaults to this behaviour about suspension:

Currently gnome-tweaks is not able to modify the behaviour on the second case, when a monitor is connected to the computer. While it can inhibit suspension with no monitor attached.

Sometimes gnome-session crashes immediately after login. This might be more visible on wayland and it might seem as if every second login attempt fails. The problem can be temporarily worked around by removing the files in ~/.config/gnome-session/saved-session. A more lasting work-around is to disable the session manager's auto-save-session feature:

This bug is much likely the cause of it. You should revert 383ba566bd7c2a76d0856015a66e47caedef06b6 commit in mutter. Use ABS for this and add git revert -n 383ba566bd7c2a76d0856015a66e47caedef06b6 to the prepare() function in the PKGBUILD or simply install mutter-performanceAUR instead.

If video playback stutters (a bit), try GNOME on Xorg instead of Wayland.

GNOME Wayland does not support more than one GPU for output yet, falling back on GNOME X11.

If your displays are only connected to one of your video devices, add this to your system environment variables:

See also GDM#Wayland and the proprietary NVIDIA driver.

Under alternative window managers (i3 for example), gnome-control-center starts as an empty window. You need to set the variable XDG_CURRENT_DESKTOP to GNOME to start it (either in a script or exporting the variable in ~/.profile).

This is a problem with the brazilian portuguese ABNT 2 keyboard. If you have the brazilian portuguese enabled, GNOME might experience this problem. To fix this issue and keep using this keyboard layout, un-map the scroll lock button by commenting this line at /usr/share/X11/xkb/symbols/br:

And restart the session (log out and in).

Ctrl+Plus and Ctrl+Minus keyboard shortcuts for zoom in/out functions do not work out of the box on some GNOME applications, such as Files and GNOME Terminal.

In such cases, open up GNOME Tweaks (gnome-tweaks) and navigate to Keyboard & Mouse > Additional Layout Options button > Layout of numeric keypad. Change the Disabled value to Hexadecimal.

CUPS and system-config-printer should be installed

Install espeak-ng. Alternatively, festival can be used

packagekit integration is voluntarily disabled and considered unsupported; see also archlinux/packaging/packages/gnome-software#4.

In touchpads where the buttons are divided (e.g. buttonless touchpads), tapping with one finger on the right side - or any other place - of the touchpad can give you the behavior of the left button, when right button is expected.

As of GNOME 3.28, the default behavior of touchpads is a two-finger tap emulate the mouse's right button. This behavior can be changed in GNOME Tweaks (gnome-tweaks) by going in Keyboard & Mouse in the left-side menu and then Mouse Click Emulation option.

The following values are available for click method:

Alternatively, this behavior can be changed in the command-line interface using gsettings. For instance, to set areas click method:

See GNOME#Device Security Settings.

This article or section is a candidate for merging with Wayland#Qt.

The cursor settings might not be set for some Qt applications like Telegram[2][3]. This may result in cursors being of the wrong theme, size and not being able to resize the window.

Set the XCURSOR_THEME and XCURSOR_SIZE environment variables manually (e.g., XCURSOR_THEME=Adwaita, XCURSOR_PATH=/usr/share/icons or XCURSOR_SIZE=24).

You can also use inline getting of current system's cursor size:

If mentioned variables does not work on Wayland (for example in Telegram), try also adding QT_QPA_PLATFORM=xcb

If you experience problems with your GPU driver, you can force software rendering of the GNOME session with the following environment variables:

**Examples:**

Example 1 (unknown):
```unknown
Ctrl+Alt+F2
```

Example 2 (unknown):
```unknown
pkill -HUP gnome-shell
```

Example 3 (unknown):
```unknown
gdm.service
```

Example 4 (unknown):
```unknown
$ xdg-mime query default application/pdf
```

---

## GNOME

**URL:** https://wiki.archlinux.org/title/Dconf

**Contents:**
- Installation
- Starting
  - Graphically
  - Manually
    - Session type
    - Start session
  - GNOME applications in Wayland
- Navigation
- Legacy names
- Configuration

GNOME (/(ɡ)noʊm/) is a desktop environment that aims to be simple and easy to use. It is designed by The GNOME Project and is composed entirely of free and open-source software. It uses Wayland, and the available sessions are

The following package groups are available:

The base desktop consists of GNOME Shell, a plugin for the Mutter window manager. It can be installed separately with gnome-shell.

Unstable releases can also be used, see Official repositories#gnome-unstable.

GNOME can be started either graphically with a display manager or manually from the console (some features may be missing). The display manager included in gnome is GDM.

If you installed the gnome group and want GNOME to start automatically on next boot, enable gdm.service. You can then select the desired session: GNOME or GNOME Classic (only displayed if gnome-shell-extensions is installed) from the display manager's session menu.

If you prefer to start GNOME right away, thereby avoiding a reboot, start the aforementioned gdm.service from a graphically unoccupied tty instead.

GNOME session inherits session type from systemd. Systemd session type is determined from XDG_SESSION_TYPE environment variable when the session is started, and can only be changed by the controller of that session afterwards. See the systemd issue on Github.

Therefore merely setting XDG_SESSION_TYPE after login does not work. Instead, create a systemd drop-in file to set environment for getty :

To show session type after reload:

After XDG_SESSION_TYPE and login session type is set correctly, manually starting a Wayland session is possible with:

Running gnome-shell --wayland directly is not recommended, because it lacks session management.

Note that manual invocation of Gnome does not require gdm (consequently also the accompanying gdm.service) at all and is thus also accessible for users with a (possibly very) minimal installation of Gnome composing of a selected few packages included in the more inclusive gnome group in accordance to personal preference.

To start on login to tty1, add to your .bash_profile:

The --no-reexec flag prevents gnome-session from starting a login shell which sources the profile again and loops.

Firefox and QT applications do not respect XDG_SESSION_TYPE, so add variables for them as well:

When the GNOME session is used, GNOME applications will be run using Wayland. For debugging cases, https://docs.gtk.org/gtk3/running.html and https://docs.gtk.org/gtk4/running.html list options and environment variables.

To learn how to use the GNOME shell effectively, read the GNOME Shell Cheat Sheet; it highlights GNOME shell features and keyboard shortcuts. Features include task switching, keyboard use, window control, the panel, overview mode, and more. A few of the shortcuts are:

See /Tips and tricks#Navigation for changes to the default configuration making the window-switching resemble that of Windows.

See Keyboard navigation for more shortcuts.

GNOME Settings (gnome-control-center) and GNOME applications use the dconf configuration system to store their settings.

You can directly access the dconf database using the gsettings(1) command line tool. This also allows you to configure settings not exposed by the user interfaces. Command line tool dconf(1) can directly modify the underlying database, bypassing validation. The configuration keys of gsettings and dconf are equivalent, but in a slightly different format: gsettings set mygroup.mysubgroup mysetting myvalue in gsettings would be dconf write /mygroup/mysubgroup/mysetting myvalue in dconf.

Up until GNOME 3.24, settings were applied by the GNOME settings daemon (located at /usr/lib/gnome-settings-daemon/gnome-settings-daemon), which could be run outside of a GNOME session.

GNOME 3.24, however, replaced the GNOME settings daemon with several separate settings plugins /usr/lib/gnome-settings-daemon/gsd-* which were later moved to /usr/lib/gsd-*. These plugins are now controlled via desktop files under /etc/xdg/autostart/ (matching org.gnome.SettingsDaemon.*.desktop). To run these plugins outside of a GNOME session, you will now need to copy/edit the appropriate desktop entries to ~/.config/autostart.

The configuration is usually performed user-specific; this section does not cover how to create configuration templates for multiple users.

The daemon colord reads the display's EDID and extracts the appropriate color profile. Most color profiles are accurate and no setup is required; however, for those that are not accurate, or for older displays, color profiles can be put in ~/.local/share/icc/ and directed to.

GNOME comes with a built-in blue light filter similar to Redshift. You can enable and customise the time you want to enable Night Light from the display settings menu. Furthermore, you can tweak the kelvin temperature with the following dconf setting, where 5000 is an example value:

If the system has a configured Network Time Protocol daemon, it will be effective for GNOME as well. The synchronization can be set to manual control from the menu, if required.

GNOME supports automatic time zone selection (can be enabled in Date & Time section of the system settings, given that location services are enabled (see Privacy section of the settings).

To show the date in the top bar, execute:

Additionally, to show week numbers in the calendar opened on the top bar, execute:

Upon installing GNOME for the first time, you may find that the wrong applications are handling certain protocols. For example, totem opens videos instead of a previously used VLC. Some of the associations can be set from system settings via Default Applications.

For other protocols and methods, see Default applications for configuration.

Most touchpad settings can be set from system settings via Mouse & Touchpad.

Depending on your device, other configuration settings may be available, but not exposed via the default GUI. For example, a different touchpad click-method

By default, you can use your mouse to move windows by holding down Super, clicking and holding the left mouse button and dragging the mouse around.

Additionally, you can enable using your mouse to resize windows by holding down Super, clicking and holding the right mouse button and dragging the mouse around:

If you don't like the Super key, you can also change the modifier to something else, like Alt or Ctrl:

NetworkManager is the native tool of the GNOME project to control network settings from the shell. If you have not already, install the networkmanager package and enable the NetworkManager.service systemd unit.

While any other network manager can be used alternatively, NetworkManager provides the full integration via the shell network settings and a status indicator applet network-manager-applet (not required for GNOME).

Some online accounts, such as ownCloud, require gvfs-goa and gvfs-dnssd to be installed for full functionality in GNOME applications such as GNOME Files and GNOME Documents [2].

See Online accounts for more information.

The GNOME shell has a search that can be quickly accessed by pressing the Super key and starting to type. The localsearch package is installed by default as a dependency of nautilus from the gnome group and provides an indexing application and metadata database. It can be configured with the Search menu item in Settings. It is started automatically by gnome-session when the user logs in.

localsearch does not automatically recurse into all directories under the user's home directory, so you may need to add custom paths via the Search > Search locations menu item. To exclude a directory from the indexing, create an empty .nomedia file.

A status is available with localsearch status and the indexed content can be searched (localsearch search --help), edited (localsearch tag --help), or reset from the commandline. See localsearch help and localsearch command --help, or the online help for reference.

The database uses tinysparql-sql(1) and can also be queried directly, if needed.

GNOME has accessibility settings available via Settings > Accessibility. The main settings may be toggled directly after enabling a top bar icon, but note further settings are available via the sub-menus for Seeing, Hearing, Typing, Pointing and clicking and Zoom. See https://help.gnome.org/users/gnome-help/stable/a11y.html.en for information on them.

Additionally, a default set of keyboard shortcuts can be set via Settings > Keyboard > View and Customize Keyboard Shortcuts > Accessibility. For example, pressing Alt, Super and 8 toggles zooming.

GNOME 43 comes with a new Device Security panel in Settings. This requires fwupd in order to function. See [3].

As noted above, many configuration options such as changing the GTK theme or the window manager theme are not exposed in GNOME Settings (gnome-control-center). Those users that want to configure these settings may wish to use the GNOME Tweaks (gnome-tweaks), a convenient graphical tool which exposes many of these settings.

GNOME settings (which are stored in the DConf database) can also be configured using the dconf-editor (a graphical DConf configuration tool) or the gsettings command line tool. The GNOME Tweaks does not do anything else in the background of the GUI; note though that you will not find all settings described in the following sections in it.

The catalogue of extensions is available at https://extensions.gnome.org, they can be installed either through official repositories (only a few), the AUR or through the browser.

The factual accuracy of this article or section is disputed.

Installed extensions can also be configured, enabled or disabled through a GUI with gnome-extensions-app, from the command line with gnome-extensions(1), or from the browser. In your browser, extensions can be installed then activated in the browser by setting the switch in right top right of the screen to ON and clicking Install on the popup window (if the extension in question is not installed). Installed extensions may be seen at https://extensions.gnome.org/local/, where available updates can be checked.

The gnome-shell-extensions package provides a set of very useful extensions maintained as part of the GNOME project.

extension-manager is a graphical tool which can also be used to install and remove extensions, as well as enable and disable them, both system-wide and for a user. Prior to using it, consider its list of known issues.

To enable usage of extensions (disabled by default):

To list currently enabled extensions:

The above command may list extensions that have been removed. To only list extensions that are enabled and installed, use gnome-extensions instead:

For more information about GNOME shell extensions, see https://extensions.gnome.org/about/.

GNOME uses Adwaita by default. To apply Adwaita-dark only to GTK 2 applications, use the following symlink:

To select new themes (move them to the appropriate directory and) use GNOME Tweaks or the GSettings commands below.

See GTK#Themes and Icons#Icon themes.

To set the order for the GNOME window manager (Mutter, Metacity):

The theme of GNOME Shell itself is configurable. To use a Shell theme, firstly ensure that you have the gnome-shell-extensions package installed. Then enable the User Themes extension, either through the GNOME Extensions application or through the GNOME Shell Extensions webpage. Shell themes can then be loaded and selected using GNOME Extensions.

There are a number of GNOME Shell themes available in the AUR, many themes do not have the same name format, so instead try searching for the appropriate theme in the AUR. Shell themes can also be downloaded from gnome-look.org.

To enable AppIndicators, which is useful for controlling/monitoring certain applications running in the background, Install gnome-shell-extension-appindicator or gnome-shell-extension-appindicator-gitAUR, restart the GNOME Shell, then enable the AppIndicator extension in the GNOME Extensions application or by running

The GNOME shell animation can be sped up, slowed down or disabled. See GNOME/Tips and tricks#Change animation speed.

Blur my Shell is an extension that adds blur effects to the overview screen as well as the shell itself and other apps. Install gnome-shell-extension-blur-my-shellAUR or gnome-shell-extension-blur-my-shell-gitAUR for development updates. This extension is highly customizable, and you may choose to blur certain applications.

The default Alt-Tab in GNOME is very simple and does not show overviews of the selected windows. You can change the Alt-Tab shortcut from "Switch Applications" to "Switch Windows" in Settings to show window overviews.

You can also use Coverflow Alt-Tab. It is an extension that expands the Alt-Tab behavior and adds features to make switching between applications easier while also giving it a better look. Install gnome-shell-extension-coverflow-alt-tab-gitAUR, then you may change the configuration of this extension to your liking.

Note: Super-` provides "Switch windows of an application` by default.

GNOME implements XDG Autostart.

The gnome-tweaks allows managing autostart-entries.

To move the dash out of the overview and turn it into a dock to easily launch and switch applications, install gnome-shell-extension-dash-to-dockAUR.

Starting from GNOME 40, the desktop will start directly into Overview Mode instead of an empty desktop (like in previous versions). To mimic legacy behaviour, one may install gnome-shell-extension-no-overviewAUR.

Alternatively, you can disable it using gsettings if using gnome-shell-extension-dash-to-dockAUR:

See the discussion at [4].

Unlike other desktop environments, GNOME does not have a built-in tool to manage the clipboard history. This can be done however with the help of an extension. Install gnome-shell-extension-clipboard-indicatorAUR.

To display the current weather information in the top panel based on a chosen location, install gnome-shell-extension-openweatherAUR. The weather information is updated in real-time and displays useful data such as conditions, wind speed, pressure, etc...

This article or section is being considered for removal.

By default, if you want to change your sound input or output device or change your microphone's volume, you need to open GNOME Control Center and configure these settings from there. To integrate a device selector and a microphone volume slider, install gnome-shell-extension-sound-output-device-chooserAUR or gnome-shell-extension-sound-output-device-chooser-gitAUR. Further configuration can be done after installation.

Fonts can be set for Window titles, Interface (applications), Documents and Monospace. See the Fonts tab in the Tweaks for the relevant options.

For hinting, RGBA will likely be desired as this fits most monitors types, and if fonts appear too blocked reduce hinting to Slight or None.

GNOME has integrated support for input methods through IBus. Only ibus and the wanted input method engine (e.g. ibus-libpinyin for Intelligent Pinyin) needed to be installed. After installation, the input method engine can be added as a keyboard layout under Keyboard > Input Sources in GNOME Settings (gnome-control-center).

If you are using an alternative keyboard layout like Neo2 which uses multiple layers/modifiers, you might need to go to Keyboard > Type Special Characters in GNOME Settings (gnome-control-center) and change the Alternate Characters Key away from Right Alt so that it can be used as a native modifier of the keyboard layout. Setting it to e.g. Left Alt prevents Alt+Tab, so be careful what you change it to. Without this change, your left Mod3 key might work, but the right one (AltGr) does not. (As of 2021-05-18)

When you are using a laptop, you might want to alter the following settings controlling behavior when idle, screen lock power button presses and lid close:

To keep the monitor active when the lid is closed:

GNOME 3.24 deprecated the following settings:

The settings panel of GNOME does not provide an option for the user to change the action triggered when the laptop lid is closed. To change the lid switch action system-wide, edit the systemd settings in /etc/systemd/logind.conf. To turn off suspend on lid close, set HandleLidSwitch=ignore, as described in Power management#ACPI events.

The settings panel does not provide an option for changing the critical battery level action. These settings have been removed from dconf as well. They are now managed by upower. Edit the upower settings in /etc/UPower/UPower.conf. Find these settings and adjust to your needs.

Install the power-profiles-daemon optional dependency (of gnome-control-center) for power profiles support. Explicitly starting/enabling the power-profiles-daemon service is unnecessary since gnome-shell and GNOME Settings both request its activation upon launching.

When the service is active, power profiles can be managed through the Power section of GNOME Settings and in the system menu.

The built-in screenshot tool comes without the Screencast option by default. Install the gst-plugin-pipewire optional dependency (of gnome-shell) to enable screen recording.

GNOME Shell does not support using a different window manager, however GNOME Flashback provides sessions for Metacity and Compiz. Furthermore, it is possible to define your own custom GNOME sessions which use alternative components.

Under Wayland, replacing GNOME Shell with a different compositor will cause certain sections of gnome-control-center (GNOME Settings) to populate incorrectly. gnome-control-center will work, but since mutter (GNOME Shell) will not be available to provide settings for populating these sections, they will not have an effect or may not populate accurately with your settings. Sections affected are bluetooth, display, and mouse/touchpad to name a few.

**Examples:**

Example 1 (unknown):
```unknown
gdm.service
```

Example 2 (unknown):
```unknown
gdm.service
```

Example 3 (unknown):
```unknown
XDG_SESSION_TYPE
```

Example 4 (unknown):
```unknown
XDG_SESSION_TYPE
```

---

## Wayland

**URL:** https://wiki.archlinux.org/title/Xwayland

**Contents:**
- Requirements
- Compositors
  - Stacking
  - Tiling
  - Dynamic
  - Other
- Display managers
- Xwayland
  - NVIDIA driver
  - Kwin Wayland debug console

Wayland is a display server protocol. It is aimed to become the successor of the X Window System. You can find a comparison between Wayland and Xorg on Wikipedia.

Display servers using the Wayland protocol are called compositors because they also act as compositing window managers. Below you can find a list of Wayland compositors.

For compatibility with native X11 applications to run them seamlessly, Xwayland can be used, which provides an X Server in Wayland.

Most Wayland compositors only work on systems using Kernel mode setting. Wayland by itself does not provide a graphical environment; for this you also need a compositor (see the following section), or a desktop environment that includes a compositor (e.g. GNOME or Plasma).

For the GPU driver and Wayland compositor to be compatible they must support the same buffer API. There are two main APIs: GBM and EGLStreams.

Since NVIDIA introduced GBM support, many compositors (including Mutter and KWin) started using it by default for NVIDIA ≥ 495. GBM is generally considered better with wider support, and EGLStreams only had support because NVIDIA did not provide any alternative way to use their GPUs under Wayland with their proprietary drivers. Furthermore, KWin dropped support for EGLStreams after GBM was introduced into NVIDIA.

If you use a popular desktop environment/compositor and a GPU still supported by NVIDIA, you are most likely already using GBM backend. To check, run journalctl -b 0 --grep "renderer for". To force GBM as a backend, set the following environment variables:

See Window manager#Types for the difference between Stacking, Tiling and Dynamic.

Some of the above may support display managers. Check /usr/share/wayland-sessions/compositor.desktop to see how they are started.

Display managers listed below support launching Wayland compositors.

Provides a TUI menu, but can also be used with other display managers.

Xwayland(1) is an X server that runs under Wayland and provides compatibility for native X11 applications that are yet to provide Wayland support. To use it, install the xorg-xwayland package.

Xwayland is started via a compositor, so you should check the documentation for your chosen compositor for Xwayland compatibility and instructions on how to start Xwayland.

Enabling DRM KMS is required. There may be additional information in the official documentation regarding your display manager (e.g. GDM).

If you use kwin, execute the following to see which windows use Xwayland or native Wayland, surfaces, input events, clipboard contents, and more.

To determine whether an application is running via Xwayland, you can run extramausAUR. Move your mouse pointer over the window of an application. If the red mouse moves, the application is running via Xwayland.

Alternatively, you can use xorg-xeyes and see if the eyes are moving, when moving the mouse pointer over an application window.

Another option is to run xwininfo (from xorg-xwininfo) in a terminal window: when hovering over an Xwayland window the mouse pointer will turn into a + sign. If you click the window it will display some information and end, but it will not do anything with native Wayland windows.You can use Ctrl+C to end it.

You can also use xlsclients (from the xorg-xlsclients package). To list all applications running via Xwayland, run xlsclients -l.

The gtk3 and gtk4 packages have the Wayland backend enabled. GTK will default to the Wayland backend, but it is possible to override it to Xwayland by modifying an environment variable: GDK_BACKEND=x11.

For theming issues, see GTK#Wayland backend.

To enable Wayland support in Qt 5, install the qt5-wayland package. Qt 5 applications will then run under Wayland on a Wayland session.

While it should not be necessary, to explicitly run a Qt application with the Wayland plugin [5], use -platform wayland or QT_QPA_PLATFORM=wayland environment variable.

To force the usage of X11 on a Wayland session, use QT_QPA_PLATFORM=xcb.

This might be necessary for some proprietary applications that do not use the system's implementation of Qt. QT_QPA_PLATFORM="wayland;xcb" allows Qt to use the xcb (X11) plugin instead if Wayland is not available.[6]

The factual accuracy of this article or section is disputed.

On some compositors, for example sway, Qt applications running natively might have missing functionality. For example, KeepassXC will be unable to minimize to tray. This can be solved by installing qt5ct and setting QT_QPA_PLATFORMTHEME=qt5ct before running the application.

Due to the Incorrect sizing and bad text rendering with WebEngine using fractional scaling on Wayland Qt WebEngine bug, applications using Qt WebEngine, for example Calibre, may display jagged fonts. A workaround is launching the application with QT_SCALE_FACTOR_ROUNDING_POLICY=RoundPreferFloor. This prevents the application window being fractional scaled.

The Clutter toolkit has a Wayland backend that allows it to run as a Wayland client. The backend is enabled in the clutter package.

To run a Clutter application on Wayland, set CLUTTER_BACKEND=wayland.

In SDL3, Wayland is used by default to communicate with the desktop compositor.

To run an SDL2 application on Wayland, set SDL_VIDEODRIVER=wayland. SDL_VIDEODRIVER="wayland,x11" allows SDL2 to use the x11 video driver instead if Wayland is not available.[7]. You may also want to install libdecor to enable window decorations (for example, on GNOME).

Refer to the official documentation for more details.

The glfw package has support for Wayland, and uses the Wayland backend if the environment variable XDG_SESSION_TYPE is set to wayland and the application developer has not set a specific desired backend.

See the source code for more information.

If the glew-wayland-gitAUR package does not work with the needed GLEW-based applications, the option is to use glew with Xwayland. See FS#62713.

Enlightenment has complete Wayland support.

To run an EFL-based application on Wayland, set ELM_DISPLAY=wl.

Winit is a window handling library in Rust. It will default to the Wayland backend, but it is possible to override it to Xwayland by modifying environment variables:

Wayland support can be activated using command line flags, or an environment variable.

See Chromium#Native Wayland support to command-line flags needed to work on Wayland. Note that the command-line flag --ozone-platform-hint=auto does not work since Electron 38.

You can pass these flags manually, persist them in an Electron configuration file, or override the .desktop file at ~/.local/share/applications of an application by adding the flags to the end of the Exec= line.

The factual accuracy of this article or section is disputed.

Electron enable WebRTC screen capture over PipeWire by default. The capture is based on xdg-desktop-portal.

A case of missing top bars can be solved by using: --enable-features=WaylandWindowDecorations. This will typically be necessary under GNOME (supported since electron17).

Applications using Electron between versions 28 and 37 can use the environment variable ELECTRON_OZONE_PLATFORM_HINT set to auto or wayland.

This takes lower priority than the command line flags.

The open source implementation of the Java platform OpenJDK, does not yet have native support for Wayland. Until Wakefield, the project that aims to implement Wayland in OpenJDK, is available, Xwayland can be used.

See Debian:Wayland#Java Programs (supported since OpenJDK 16?):

Since XWayland doesn't have full feature parity with Wayland, WLToolkit can be used to fill the gaps while Wakefield isn't ready. It can be activated with -Dawt.toolkit.name=WLToolkit. Some programs such as the JetBrains IDEs support it.

See Input remap utilities.

See Screen capture#Screencasting and Screen capture#Screencast Wayland windows with X11 applications.

This article or section is a candidate for moving to Chromium.

You have to enable Use system title bar and borders via the chrome://settings/appearance menu.

This article or section is a candidate for merging with Clipboard.

Due to Wayland's design philosophy, clipboard data is stored in the memory of the source client. When the client closes, the clipboard data is lost. You can solve this using wl-clip-persist, which runs in the background to reads the clipboard data and stores it in its own memory, separate from the source client.

If you do not want to use a display manager or a shell, you can autostart your Wayland compositor with a systemd service. Adjust the ExecStart line with the compositor you want to use. Here is an example for KDE Plasma:

You can use another wlroots renderer such as vulkan by specifying the WLR_RENDERER environment variable for wlroots based compositor. The list of available ones is on the wlroots documentation.

See Backlight#Color correction.

Gnome-shell users may experience display issues when they switch to Wayland from X. One of the root cause might be the CLUTTER_PAINT=disable-clipped-redraws:disable-culling set by yourself for Xorg-based gnome-shell. Just try to remove it from /etc/environment or other rc files to see if everything goes back to normal.

In contrast to Xorg, Wayland does not allow exclusive input device grabbing, also known as active or explicit grab (e.g. keyboard, mouse), instead, it depends on the Wayland compositor to pass keyboard shortcuts and confine the pointer device to the application window.

This change in input grabbing breaks current applications' behavior, meaning:

Wayland solves this by adding protocol extensions for Wayland and Xwayland. Support for these extensions is needed to be added to the Wayland compositors. In the case of native Wayland clients, the used widget toolkits (e.g GTK, Qt) needs to support these extensions or the applications themselves if no widget toolkit is being used. In the case of Xorg applications, no changes in the applications or widget toolkits are needed as the Xwayland support is enough.

These extensions are already included in wayland-protocols, and supported by xorg-xwayland.

The related extensions are:

Supporting Wayland compositors:

Supporting widget toolkits:

See https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland.

Add __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json as environment variable before launching a Wayland compositor like sway.

Screen magnifying is not solved yet, a pull request was merged mid-2022 providing the protocol wp-surface-scale.

Until this issue is patched in future kernel releases, a workaround is to add amdgpu.dcdebugmask=0x400 to the cmdline.

See: https://community.frame.work/t/wayland-lag-stuttering-since-kernel-6-11-2/59422

**Examples:**

Example 1 (unknown):
```unknown
journalctl -b 0 --grep "renderer for"
```

Example 2 (unknown):
```unknown
GBM_BACKEND=nvidia-drm
__GLX_VENDOR_LIBRARY_NAME=nvidia
```

Example 3 (unknown):
```unknown
/usr/share/wayland-sessions/compositor.desktop
```

Example 4 (unknown):
```unknown
$ qdbus6 org.kde.KWin /KWin org.kde.KWin.showDebugConsole
```

---

## Desktop environment

**URL:** https://wiki.archlinux.org/title/Desktop_environments

**Contents:**
- List of desktop environments
  - Officially supported
  - Unofficially supported
- Custom window manager
- Custom environments

A desktop environment (DE) is an implementation of the desktop metaphor made of a bundle of programs, which share a common graphical user interface (GUI).

A desktop environment bundles together a variety of components to provide common graphical user interface elements such as icons, toolbars, wallpapers, and desktop widgets. Additionally, most desktop environments include a set of integrated applications and utilities. Most importantly, desktop environments provide their own window manager, which can however usually be replaced with another compatible one.

The user is free to configure their GUI environment in any number of ways. Desktop environments simply provide a complete and convenient means of accomplishing this task. Note that users are free to mix-and-match applications from multiple desktop environments. For example, a Plasma user may install and run GNOME applications such as the Epiphany web browser, should they prefer it over KDE Konqueror web browser. One drawback of this approach is that many applications provided by desktop environment projects rely heavily upon the libraries underlying the respective desktop environment. As a result, installing applications from a range of desktop environments will require installation of a larger number of dependencies. Users seeking to conserve disk space often avoid such mixed environments, or choose alternatives which do depend on only few external libraries.

Furthermore, applications provided by desktop environments tend to integrate better with their native environments. Superficially, mixing environments with different widget toolkits will result in visual discrepancies (that is, interfaces will use different icons and widget styles). In terms of usability, mixed environments may not behave similarly (e.g. single-clicking versus double-clicking icons; drag-and-drop functionality) potentially causing confusion or unexpected behavior.

Some desktop environments support using a non-default window manager, such as i3.

Desktop environments represent the simplest means of installing a complete graphical environment. However, users are free to build and customize their graphical environment in any number of ways if none of the popular desktop environments meet their requirements. Generally, building a custom environment involves selection of a suitable window manager or compositor, a taskbar and a number of applications (a minimalist selection usually includes a terminal emulator, file manager, and text editor).

Other components usually provided by desktop environments are:

---

## GNOME/Keyring

**URL:** https://wiki.archlinux.org/title/GNOME_Keyring

**Contents:**
- Security
  - Protection against malicious application
  - Keyring is not locked when session is locked
- Installation
- Manage using GUI
- Using the keyring
  - PAM step
- SSH keys
  - Setup gcr
  - Using

GNOME Keyring is "a collection of components in GNOME that store secrets, passwords, keys, certificates and make them available to applications."

It provides org.freedesktop.secrets, an API that allows client applications to store secrets securely using a service running in the user's login session.

There was a security issue (known as CVE-2018-19358) reported in the past regarding the behaviour of the GNOME/Keyring API. Any application can easily read any secret if the keyring is unlocked. And, if a user is logged in, then the login/default collection is unlocked. Available D-Bus protection mechanisms (involving the busconfig and policy XML elements) are not used by default and would be easy to bypass anyway.

The GNOME project disagrees with this vulnerability report because, according to their stated security model, untrusted applications must not be allowed to communicate with the secret service.

Applications sandboxed via Flatpak only have filtered access to the session bus.

When the session is locked, the keyring is not automatically locked.[1] This means that the passwords remain in memory which opens the system up to a DMA attack.

gnome-keyring is a member of the gnome group is thus usually present on systems running GNOME. The package can otherwise be installed on its own. libsecret should also be installed to grant other applications access to your keyrings. Although libgnome-keyring is deprecated (and superseded by libsecret), it may still be required by certain applications.

The gnome-keyring-daemon is automatically started via a systemd user service upon logging in. It can also be started upon request via a socket.

Extra utilities related to GNOME Keyring include:

You can manage the contents of GNOME Keyring using Seahorse; install the seahorse package.

Passwords for keyrings (e.g., the default keyring, "Login") can be changed and even removed. See Create a new keyring and Update the keyring password in GNOME Help for more information.

The PAM module pam_gnome_keyring.so initialises GNOME Keyring partially, unlocking the login keyring in the process. The gnome-keyring-daemon is automatically started with a systemd user service.

When using a display manager, the keyring works out of the box for most cases. GDM, LightDM, LXDM, and SDDM already have the necessary PAM configuration. For a display manager that does not automatically unlock the keyring edit the appropriate file instead of /etc/pam.d/login as mentioned below.

When using console-based login, edit /etc/pam.d/login:

Add auth optional pam_gnome_keyring.so at the end of the auth section and session optional pam_gnome_keyring.so auto_start at the end of the session section.

GNOME Keyring can act as a wrapper around ssh-agent. In that mode, it will display a GUI password entry dialog each time you need to unlock an SSH key. The dialog includes a checkbox to remember the password you type, which, if selected, will allow fully passwordless use of that key in the future as long as your login keyring is unlocked.

The SSH functionality is disabled by default in gnome-keyring-daemon builds since version 1:46. It has been moved into /usr/lib/gcr-ssh-agent, which is part of the gcr-4 package.

All you need to do is:

There are many ways to set environment variables, and the one you use will depend on your specific setup and preferences.

to list loaded SSH keys in the running agent. This can help ensure you started the appropriate service and set SSH_AUTH_SOCK correctly.

To permanently save a passphrase in the keyring, use ssh-askpass from the seahorse package:

To manually add an SSH key from another directory:

To disable all manually added keys:

If you wish to run an alternative SSH agent (e.g. ssh-agent directly or gpg-agent), it is a good idea to disable GNOME Keyring's ssh-agent wrapper. Doing so is not strictly necessary, since each agent listens on a different socket and SSH_AUTH_SOCK can be used to choose between them, but it can make debugging issues easier. Note that the GNOME implementation does not support many scripting features such BatchMode [4].

To disable gcr-ssh-agent, ensure gcr-ssh-agent.socket and gcr-ssh-agent.service are both disabled and stopped in systemd.

This command performs a D-Bus method call to lock the login keyring. Alternatively, if you want to use a GUI, Seahorse can be used lock the keyring.

This command starts gnome-keyring-daemon, shutting down previously running instances.

The GNOME keyring is useful in conjunction with Git when you are pushing over HTTPS. The libsecret package needs to be installed for this functionality to be available.

Configure Git to use the libsecret helper:

The next time you run git push, you will be asked to unlock your keyring if it is not already unlocked.

Several applications which use GnuPG require a pinentry-program to be set. Set the following to use GNOME 3 pinentry for GNOME Keyring to manage passphrase prompts.

Another option is to force loopback for GPG which should allow the passphrase to be entered in the application.

The display name for a keyring (i.e., the name that appears in Seahorse and from file) can be changed by changing the value of display-name in the unencrypted keyring file. Keyrings will usually be stored in ~/.local/share/keyrings/ with the .keyring file extension.

Append password optional pam_gnome_keyring.so to /etc/pam.d/passwd:

The factual accuracy of this article or section is disputed.

If you are using sway, i3, or any window manager that does not execute

your window manager needs to execute the following commands during window manager startup. The commands do not need to be executed in any specific order.

This command passes environment variables from the window manager to session dbus. Without this, GUI prompts cannot be triggered over DBus. For example, this is required for seahorse password prompt.

This is required because session dbus is started before graphical environment is started. Thus, session dbus does not know about the graphical environment you are in. Someone or something has to teach session dbus about the graphical environment by passing environment variables describing the graphical environment to session dbus.

During login, PAM starts gnome-keyring-daemon --login which is responsible for keeping gnome-keyring unlocked with login password. If gnome-keyring-daemon --login is not connected to session dbus within a few minutes, gnome-keyring-daemon --login dies. If gnome-keyring-daemon --start ... is started against session dbus in a window manager, gnome-keyring-daemon --login is connected to session dbus. If your login session does not start gnome-keyring-daemon --start ... before gnome-keyring-daemon --login quits, you can also use any program that uses gnome-keyring or secret service API before gnome-keyring-daemon --login dies.

The factual accuracy of this article or section is disputed.

GNOME Keyring exposes an XDG Portal backend (for use with applications sandboxed through flatpak for example). In order for it to work outside of GNOME, one must add their desktop environment to the /usr/share/xdg-desktop-portal/portals/gnome-keyring.portal configuration file by modifying the UseIn key. For instance, to add sway:

See XDG Desktop Portal#Backends for more information about XDG Desktop Portal backends.

If you are prompted for a password after logging in and you find that your passwords are not saved, then you may need to create/set a default keyring. To do this using Seahorse (a.k.a. Passwords and Keys), see Create a new keyring and Change the default keyring in GNOME Help.

You will need to change your login keyring password if you receive the following error message: "The password you use to login to your computer no longer matches that of your login keyring".

Alternatively, you can remove the login.keyring and user.keystore files from ~/.local/share/keyrings/. Be warned that this will permanently delete all saved keys. After removing the files, simply log out and log in again.

The following error may appear in the journal after logging in:

This message "can be safely ignored" if there are no other related issues [5].

If you try to add a new keyring with Seahorse you may receive this error due to the following reasons:

This is caused by gnome-keyring-daemon being started for the second time. Since a systemd service is delivered together with the daemon, you do not need to start it another way. So make sure to remove the start command from your .zshenv, .bash_profile, .xinitrc, config.fish or similar. Alternatively you can disable the gnome-keyring-daemon.service and gnome-keyring-daemon.socket user units.

There are a few symptoms of this:

To address this, do the following:

If this does not fix the issue, consider resetting the keyring.

Symptom : ssh-add -L returns "Error connecting to agent: Connection refused"

Ensure gcr-ssh-agent.socket user unit is enabled and started:

$ systemctl --user enable --now gcr-ssh-agent.socket

Ensure gnome-keyring-daemon socket and service user unit are enabled and started:

$ systemctl --user enable gnome-keyring-daemon.{service,socket} $ systemctl --user start gnome-keyring-daemon.{service,socket}

**Examples:**

Example 1 (unknown):
```unknown
/etc/pam.d/login
```

Example 2 (unknown):
```unknown
/etc/pam.d/login
```

Example 3 (unknown):
```unknown
auth optional pam_gnome_keyring.so
```

Example 4 (unknown):
```unknown
session optional pam_gnome_keyring.so auto_start
```

---

## Comparison of desktop environments

**URL:** https://wiki.archlinux.org/title/Comparison_of_desktop_environments

**Contents:**
- See also

See Desktop environment for the main article.

---

## GNOME/Keyring

**URL:** https://wiki.archlinux.org/title/GNOME/Keyring

**Contents:**
- Security
  - Protection against malicious application
  - Keyring is not locked when session is locked
- Installation
- Manage using GUI
- Using the keyring
  - PAM step
- SSH keys
  - Setup gcr
  - Using

GNOME Keyring is "a collection of components in GNOME that store secrets, passwords, keys, certificates and make them available to applications."

It provides org.freedesktop.secrets, an API that allows client applications to store secrets securely using a service running in the user's login session.

There was a security issue (known as CVE-2018-19358) reported in the past regarding the behaviour of the GNOME/Keyring API. Any application can easily read any secret if the keyring is unlocked. And, if a user is logged in, then the login/default collection is unlocked. Available D-Bus protection mechanisms (involving the busconfig and policy XML elements) are not used by default and would be easy to bypass anyway.

The GNOME project disagrees with this vulnerability report because, according to their stated security model, untrusted applications must not be allowed to communicate with the secret service.

Applications sandboxed via Flatpak only have filtered access to the session bus.

When the session is locked, the keyring is not automatically locked.[1] This means that the passwords remain in memory which opens the system up to a DMA attack.

gnome-keyring is a member of the gnome group is thus usually present on systems running GNOME. The package can otherwise be installed on its own. libsecret should also be installed to grant other applications access to your keyrings. Although libgnome-keyring is deprecated (and superseded by libsecret), it may still be required by certain applications.

The gnome-keyring-daemon is automatically started via a systemd user service upon logging in. It can also be started upon request via a socket.

Extra utilities related to GNOME Keyring include:

You can manage the contents of GNOME Keyring using Seahorse; install the seahorse package.

Passwords for keyrings (e.g., the default keyring, "Login") can be changed and even removed. See Create a new keyring and Update the keyring password in GNOME Help for more information.

The PAM module pam_gnome_keyring.so initialises GNOME Keyring partially, unlocking the login keyring in the process. The gnome-keyring-daemon is automatically started with a systemd user service.

When using a display manager, the keyring works out of the box for most cases. GDM, LightDM, LXDM, and SDDM already have the necessary PAM configuration. For a display manager that does not automatically unlock the keyring edit the appropriate file instead of /etc/pam.d/login as mentioned below.

When using console-based login, edit /etc/pam.d/login:

Add auth optional pam_gnome_keyring.so at the end of the auth section and session optional pam_gnome_keyring.so auto_start at the end of the session section.

GNOME Keyring can act as a wrapper around ssh-agent. In that mode, it will display a GUI password entry dialog each time you need to unlock an SSH key. The dialog includes a checkbox to remember the password you type, which, if selected, will allow fully passwordless use of that key in the future as long as your login keyring is unlocked.

The SSH functionality is disabled by default in gnome-keyring-daemon builds since version 1:46. It has been moved into /usr/lib/gcr-ssh-agent, which is part of the gcr-4 package.

All you need to do is:

There are many ways to set environment variables, and the one you use will depend on your specific setup and preferences.

to list loaded SSH keys in the running agent. This can help ensure you started the appropriate service and set SSH_AUTH_SOCK correctly.

To permanently save a passphrase in the keyring, use ssh-askpass from the seahorse package:

To manually add an SSH key from another directory:

To disable all manually added keys:

If you wish to run an alternative SSH agent (e.g. ssh-agent directly or gpg-agent), it is a good idea to disable GNOME Keyring's ssh-agent wrapper. Doing so is not strictly necessary, since each agent listens on a different socket and SSH_AUTH_SOCK can be used to choose between them, but it can make debugging issues easier. Note that the GNOME implementation does not support many scripting features such BatchMode [4].

To disable gcr-ssh-agent, ensure gcr-ssh-agent.socket and gcr-ssh-agent.service are both disabled and stopped in systemd.

This command performs a D-Bus method call to lock the login keyring. Alternatively, if you want to use a GUI, Seahorse can be used lock the keyring.

This command starts gnome-keyring-daemon, shutting down previously running instances.

The GNOME keyring is useful in conjunction with Git when you are pushing over HTTPS. The libsecret package needs to be installed for this functionality to be available.

Configure Git to use the libsecret helper:

The next time you run git push, you will be asked to unlock your keyring if it is not already unlocked.

Several applications which use GnuPG require a pinentry-program to be set. Set the following to use GNOME 3 pinentry for GNOME Keyring to manage passphrase prompts.

Another option is to force loopback for GPG which should allow the passphrase to be entered in the application.

The display name for a keyring (i.e., the name that appears in Seahorse and from file) can be changed by changing the value of display-name in the unencrypted keyring file. Keyrings will usually be stored in ~/.local/share/keyrings/ with the .keyring file extension.

Append password optional pam_gnome_keyring.so to /etc/pam.d/passwd:

The factual accuracy of this article or section is disputed.

If you are using sway, i3, or any window manager that does not execute

your window manager needs to execute the following commands during window manager startup. The commands do not need to be executed in any specific order.

This command passes environment variables from the window manager to session dbus. Without this, GUI prompts cannot be triggered over DBus. For example, this is required for seahorse password prompt.

This is required because session dbus is started before graphical environment is started. Thus, session dbus does not know about the graphical environment you are in. Someone or something has to teach session dbus about the graphical environment by passing environment variables describing the graphical environment to session dbus.

During login, PAM starts gnome-keyring-daemon --login which is responsible for keeping gnome-keyring unlocked with login password. If gnome-keyring-daemon --login is not connected to session dbus within a few minutes, gnome-keyring-daemon --login dies. If gnome-keyring-daemon --start ... is started against session dbus in a window manager, gnome-keyring-daemon --login is connected to session dbus. If your login session does not start gnome-keyring-daemon --start ... before gnome-keyring-daemon --login quits, you can also use any program that uses gnome-keyring or secret service API before gnome-keyring-daemon --login dies.

The factual accuracy of this article or section is disputed.

GNOME Keyring exposes an XDG Portal backend (for use with applications sandboxed through flatpak for example). In order for it to work outside of GNOME, one must add their desktop environment to the /usr/share/xdg-desktop-portal/portals/gnome-keyring.portal configuration file by modifying the UseIn key. For instance, to add sway:

See XDG Desktop Portal#Backends for more information about XDG Desktop Portal backends.

If you are prompted for a password after logging in and you find that your passwords are not saved, then you may need to create/set a default keyring. To do this using Seahorse (a.k.a. Passwords and Keys), see Create a new keyring and Change the default keyring in GNOME Help.

You will need to change your login keyring password if you receive the following error message: "The password you use to login to your computer no longer matches that of your login keyring".

Alternatively, you can remove the login.keyring and user.keystore files from ~/.local/share/keyrings/. Be warned that this will permanently delete all saved keys. After removing the files, simply log out and log in again.

The following error may appear in the journal after logging in:

This message "can be safely ignored" if there are no other related issues [5].

If you try to add a new keyring with Seahorse you may receive this error due to the following reasons:

This is caused by gnome-keyring-daemon being started for the second time. Since a systemd service is delivered together with the daemon, you do not need to start it another way. So make sure to remove the start command from your .zshenv, .bash_profile, .xinitrc, config.fish or similar. Alternatively you can disable the gnome-keyring-daemon.service and gnome-keyring-daemon.socket user units.

There are a few symptoms of this:

To address this, do the following:

If this does not fix the issue, consider resetting the keyring.

Symptom : ssh-add -L returns "Error connecting to agent: Connection refused"

Ensure gcr-ssh-agent.socket user unit is enabled and started:

$ systemctl --user enable --now gcr-ssh-agent.socket

Ensure gnome-keyring-daemon socket and service user unit are enabled and started:

$ systemctl --user enable gnome-keyring-daemon.{service,socket} $ systemctl --user start gnome-keyring-daemon.{service,socket}

**Examples:**

Example 1 (unknown):
```unknown
/etc/pam.d/login
```

Example 2 (unknown):
```unknown
/etc/pam.d/login
```

Example 3 (unknown):
```unknown
auth optional pam_gnome_keyring.so
```

Example 4 (unknown):
```unknown
session optional pam_gnome_keyring.so auto_start
```

---

## KDE Wallet

**URL:** https://wiki.archlinux.org/title/KDE_Wallet

**Contents:**
- Installation
- Configuration
  - Unlock KDE Wallet automatically on login
    - Configure PAM
    - Using SDDM autologin and LUKS encryption
- Tips and tricks
  - Using the KDE Wallet to store ssh key passphrases
  - Using the KDE Wallet to store Git credentials
  - Store GPG key passphrases
  - KDE Wallet for Chrome and Chromium

KDE Wallet Manager is a tool to manage passwords on the KDE Plasma system. Using the KWallet subsystem allows a user to keep its own secrets, but also allows a user to access passwords stored by every application that integrates with KWallet.

A wallet (in the KDE's terminology, sometimes called vault or keyring) is an encrypted volume protected by a user-defined password where user and/or software can store secrets (often, credentials when the user checked "Remember the account" in an application). Those vaults can be created and used manually by the user or created and used automatically in the background by some software that integrates with the wallet subsystem (e.g. mail applications or games). Vaults are often decrypted automatically at the user login using a PAM module (see below).

KDE Wallet is often shipped with the KDE Plasma desktop environment. The wallet subsystem can be manually installed with the kwallet package.

Optionally install the kwalletmanager package for the wallet management tool. This tool can be used to graphically create and manage a KDE Wallet.

To unlock KDE Wallet automatically on login, install kwallet-pam for the PAM compatible module. The chosen KWallet password must be the same as the current user password.

The following lines must be present under their corresponding sections:

Edit the PAM configuration corresponding to your situation:

When the system is encrypted using dm-crypt it is possible to automatically unlock KDE Wallet using the passphrase that decrypts the disk. When SDDM#Autologin is configured, the wallet can still be unlocked automatically. Edit /etc/pam.d/sddm-autologin to add pam_systemd_loadkey(8):

Then edit sddm.service, and add:

Install ksshaskpass package.

Set the SSH_ASKPASS environment variable to ksshaskpass and SSH_ASKPASS_REQUIRE to prefer (prefer to use the askpass program instead of the TTY). To set it automatically on each login, create the following environment.d(5) file:

Restart your session (i.e. relogin) so that the environment variables take effect.

The first time you try to use an SSH key, you will get asked for its passphrase. Make sure to check the Remember password checkbox. Next time, the passphrase will be read from KDE Wallet.

Git can delegate credential handling to a credential helper. By using ksshaskpass as a credential helper, the HTTP/HTTPS and SMTP passwords can be safely stored in the KDE Wallet.

Install the ksshaskpass package.

Configure Git by setting the GIT_ASKPASS environment variable:

See gitcredentials(7) for alternatives and more details.

Native KDE windows can be used to prompt for GPG key passphrases and save them in KDE Wallet.

Configure gpg-agent to use /usr/bin/pinentry-qt.

Enable the Secret Service interface. There are two ways to do this:

Close the wallet and reopen it to affect these changes. You can do this using kwalletmanager or by issuing commands to Qt D-Bus directly:

Chrome/Chromium/Opera has built in wallet integration. To enable it, run Chromium with the --password-store=kwallet5 or --password-store=kwallet6 or --password-store=detect argument. To make the change persistent, see Chromium#Making flags persistent. (Setting CHROMIUM_USER_FLAGS will not work.)

Instead of storing passwords in plain text files, you can manually add new entries in your wallet and retrieve them with kwallet-query.

For example, if you want to log into the Docker Hub registry with Podman, which supports getting the passwords from stdin with the --password-stdin flag, you can use the following command to login:

This way, your password is not stored in any text file and neither is it stored in the terminal history file.

In order to run kwallet-query outside of a graphical session (for instance as part of an unattended backup script), set the QT_QPA_PLATFORM=offscreen environment variable:

To unlock KWallet protected by the login password, it is necessary to start /usr/lib/pam_kwallet_init in the autostart portion of your window manager's configuration file in addition to configuring PAM.

In case you want to permanently disable kwallet:

Most applications use org.freedesktop.secrets.service D-Bus service. KWallet does not provide a service file for it out of the box.

You can achieve automatic activation by creating such service file:

**Examples:**

Example 1 (unknown):
```unknown
~/.local/share/kwalletd
```

Example 2 (unknown):
```unknown
~/.kde4/share/apps/kwallet
```

Example 3 (unknown):
```unknown
auth            optional        pam_kwallet5.so
session         optional        pam_kwallet5.so auto_start
```

Example 4 (unknown):
```unknown
/etc/pam.d/sddm
```

---

## KRunner

**URL:** https://wiki.archlinux.org/title/KRunner

**Contents:**
- Installation
- Usage
- Open KRunner with the Meta key
- Change position where KRunner is displayed
- Switch active windows
  - Full list of windows with search by titles
  - Search by titles without full windows list
- See also

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

KRunner is an application built into KDE Plasma to perform functions and run commands quickly, and features a "runner" system to customize functions available for use.

Install the krunner package.

To open KRunner in Plasma, you can either right-click the desktop and press "run command", or you can use the default keybindings, Alt+Space or Alt+F2. In some workspaces such as a blank desktop, starting to type will automatically bring up KRunner.

KRunner can now be bound to the Meta key directly in System Settings > Shortcuts > Krunner.

By default KRunner is displayed at top of screen. To make it appear centered, run

The change will become effective on next login.

The factual accuracy of this article or section is disputed.

In Krunner configuration, there is a plug-in configuration button where you can choose needed search source. See the user manual for detail.

If you want to specify krunner search only by active window titles, just enable window plugin and disable the others.

This approach will require xdotool.

Note the space after window.

It is possible to specify the search query directly, but repeated search queries will be selected. To avoid this, use a state file to add a space in front of window.

Now you are able to get list of opened windows by specified shortcut and search by this list as you type;

This approach is more limited but far less ugly.

**Examples:**

Example 1 (unknown):
```unknown
$ kwriteconfig6 --file krunnerrc --group General --key FreeFloating true
```

Example 2 (unknown):
```unknown
/usr/local/bin/krunner-search-by-windows.sh
```

Example 3 (unknown):
```unknown
/usr/local/bin/krunner-search-by-windows.sh
```

Example 4 (unknown):
```unknown
#!/bin/bash
qdbus org.kde.krunner /App querySingleRunner windows "" 
sleep 0.2
xdotool key "ctrl+A"
xdotool type 'window '
xdotool key "shift+BackSpace"
```

---

## Niri

**URL:** https://wiki.archlinux.org/title/Niri

**Contents:**
- Installation
- Starting
- Configuration
  - Keymap
  - Outputs
    - Dynamic layouts using kanshi
  - Bindings
    - WASD-like navigation
  - Autostart
  - XWayland

Niri is a scrollable tiling Wayland compositor. Unlike Sway or Hyprland, Niri arranges the windows in an infinite horizontal desktop, where you can scroll to the left or to the right (although more advanced layouts are possible). It is similar to GNOME's PaperWM and KDE's Karousel.

Niri can be installed with the niri package. Additionally, to have a better experience, you may want to install:

Niri comes with a desktop entry that can be sourced by display managers; selecting it will run niri-session which handles exporting environment variables to systemd.

Additionally you can start Niri from a getty by executing:

This can be paired with auto login to have a seamless boot experience.

Niri reads the configuration from ~/.config/niri/config.kdl. It is a KDL file, divided by sections. The default configuration, created on the first run, documents the default options with comments. However, options introduced with updates will not be documented in the user's configuration; you may check Niri's official documentation instead.

Niri automatically applies the configuration when it's saved. The live reload of invalid configuration won't crash Niri; instead, the last working state is preserved, and the user is notified of the configuration error. niri validate can be invoked to validate the configuration outside of a Niri session.

To configure the keymap, edit the input/keyboard/xkb section.

For example, if you want to have a "US Int Alt Gr" layout with CapsLock acting as Ctrl key:

First run niri msg outputs to get an overview of the outputs recognized by Niri. Then you can apply configs to each monitor. For example to set the HDMI monitor to 2560x1440 60Hz with a 1.2 scaling, and turning off the laptop monitor, set the following:

Alternatively, you can use kanshi to set up dynamic layouts, for example, if you want to turn off an internal laptop screen when docked to a monitor.

The binds section allows to set up the different key combinations that have effect on Niri. Many bindings are already set in the default configuration generated on first launch. These are all remappable.

Please note that Niri does not load any default bindings. If a binding is not specified in the configuration, it will not be active. "Defaults" are simply bindings that are present in the automatically generated configuration. Therefore, take care when removing the bindings. It is recommended to instead comment out unused bindings.

Bindings are defined using the modifiers keys appended with a + sign and the action between brackets. The special action 'spawn' will launch a program. For example, you will find the following bindings that spawn alacritty and fuzzel on Mod+T and Mod+D respectively. Mod is usually the Super key if running standalone, but it is Alt if it is running inside of another compositor.

Note that all space-separated arguments to processes started by spawn must be enclosed in quotes:

It is possible to configure Niri workspaces and bindings so that jumping through windows follows a navigation similar to WASD as in games.

Be aware that this config will probably need other bindings to be remapped as well. Also, some people may prefer to have the WASD navigation on the right-hand side, or have a more Vim-like navigation.

Niri allows some programs to be started alongside with Niri. For example, some of the programs mentioned beforehand like mako, waybar and swayidle/swaylock can be configured:

Note that these processes are tied to the Niri session, and they will be killed when Niri exits or is suspended. To make a process persist, you may set it to a background task by providing the "&" argument.

Niri does not provide XWayland support for running X11 applications. Instead, it recommends using an external tool: xwayland-satellite is listed in the optional dependencies. After installation, no configuration is required.

**Examples:**

Example 1 (unknown):
```unknown
niri-session
```

Example 2 (unknown):
```unknown
niri-session
```

Example 3 (unknown):
```unknown
~/.config/niri/config.kdl
```

Example 4 (unknown):
```unknown
niri validate
```

---

## Desktop notifications

**URL:** https://wiki.archlinux.org/title/Desktop_notifications

**Contents:**
- Libnotify
- Notification servers
  - Built-in
  - Standalone
- Tips and tricks
  - Send notifications to another user
  - Replace previous notification
  - Include Buttons or listen for close/on-click of the notification
  - Multiple notification servers with D-Bus services
- Troubleshooting

Desktop notifications are small, passive popup dialogs that notify the user of particular events in an asynchronous manner.

libnotify is a desktop-independent implementation of the Desktop Notifications Specification, which provides notify-send(1) utility and support for GTK and Qt applications. It is already used by many open source applications like Evolution and Pidgin.

In order to receive notifications sent via libnotify, a notification server is required.

Cinnamon, Deepin, Enlightenment, GNOME, and GNOME Flashback use their own implementations to display notifications, and may not be able to be replaced since their notification servers are started automatically on login to receive notifications from applications via DBus.

On KDE Plasma if you enter the configuration for the System Tray you can disable the built-in notification server under System Services by changing the drop-down next to Notifications to Disabled. You can then add your preferred notification server in the System Settings menu under System / Autostart by adding a new Autostart application. You will need to log out and back in to take effect.

In other desktop environments, a notification server needs to be manually installed and launched using e.g. XDG Autostart.

Alternatively, by making the notification server a D-Bus service, the notification server can be launched automatically on the first call to it. Most notification servers already ship a dbus service under /usr/share/dbus-1/services. For some implementations, e.g. notification-daemon package, it's necessary to create one manually in the user D-Bus services directory ($XDG_DATA_HOME/dbus-1/services):

Whenever an application sends a notification by sending a signal to org.freedesktop.Notifications, D-Bus activates /usr/lib/notification-daemon-1.0/notification-daemon if it has not already been activated.

You can also choose one of the following implementations:

systemd-run(1) can be used to enter another user's session and send notifications to them, e.g. from a background script running as root:

Another possibility is to use systembus-notify. The following command will show a notification to all users who run systembus-notify in their user session:

Notifications can be replaced if their ID is known; if a new notification request specifies the same ID, it will always replace the old notification. Unfortunately notify-send does not report this ID, so alternative tools are required to do this on CLI. One capable CLI-tool is the notify-send.py python script, which provides notify-send syntax with additional ID-reporting and replacing capabilities.

However, with some notification servers (such as Notify-OSD), you can use the string:x-canonical-private-synchronous: hint with notify-send to achieve the same result.

For example, to get a notification displaying time:

With the notify-send.py script, actions can be used to display buttons or to listen for the default-action of the notification (usually, when the user clicks on it) and the close-action. When the action-icons hint is set to true and the notification daemon supports this, the buttons will display icons instead of text. The script prints the action identifier or "close" to the command line when the corresponding event has occured. To listen for the default action (on-click), one has to use the action-identifier "default".

Example with icons on buttons:

As described in the section Standalone, users can create a D-Bus service so that a notification server can be launched automatically. Some implementations already include the D-Bus service files. However, this causes a problem when multiple notification servers are installed and when some of them come with the service files. For example, installing both dunst and mako without explicitly specifying the desired server, D-Bus then chooses one for the users, and the decision is out of users' control. To avoid the situation, you can override the service used by creating an org.freedesktop.Notifications.service (see #Standalone) and pointing to the service you want to use, then restarting the session.

If applications hang when attempting to show notifications, it might be because of a notification service falsely advertising its availability through the D-Bus service.

For instance, suppose a user recently installed a KDE component that requires plasma-workspace, but the user is still running XFCE. In this case, the KDE notifier will be prioritized, but the user is not running it. The application will hang while waiting for the service, and only after a timeout will it fall back to xfce4-notifyd.

The most noticeable hanging might come from the volume indicator scroll adjustment.

If you are in this situation, you should have two notification handlers:

Of those two, one fails regularly after a 1-minute timeout, as seen in the journal:

Choosing the service you want to use as described in #Multiple notification servers with D-Bus services will fix the problem.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/dbus-1/services
```

Example 2 (unknown):
```unknown
$XDG_DATA_HOME/dbus-1/services
```

Example 3 (unknown):
```unknown
org.freedesktop.Notifications.service
```

Example 4 (unknown):
```unknown
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

---

## File manager functionality

**URL:** https://wiki.archlinux.org/title/File_manager_functionality

**Contents:**
- Overview
- Additional features
  - Mounting
    - File manager daemon
    - Standalone
  - Networks
    - Windows access
    - Apple access
    - sftp access
    - WebDAV

This article outlines the additional software packages necessary to expand the features and functionality of file managers, particularly where using a window manager such as Openbox. The ability to access partitions and removable media without a password—if affected—has also been provided.

A file manager alone will not provide the features and functionality that users of full desktop environments such as Plasma or Xfce will be accustomed to. This is because additional software packages will be required to enable a given file manager to:

When a file manager has been installed as part of a full desktop environment, most of these packages will usually have been installed automatically. Consequently, where a file manager has been installed for a standalone window manager then - as is the case with the window manager itself - only a basic foundation will be provided. The user must then determine the nature and extent of the features and functionality to be added.

This article or section needs expansion.

When using a lightweight environment, the more added file manager features, the more memory usage is needed. See also udisks.

Folders used by GVFS:

Additional packages for installation usually follows the gvfs-* pattern, for example:

Most graphical file managers have the ability to automount devices plugged in while the program is running. You can leverage this for a system-wide solution by running the file manager in daemon mode (i.e. as a background process), if supported. For example, when using PCManFM in Openbox, the following command would be added to the ~/.config/openbox/autostart file:

It will also be necessary to configure the file manager itself in respect to volume management (e.g. what it will do and what applications will be launched when certain file types are detected upon mounting).

Another option is to install a separate mount application. The advantages of using this are:

If using gvfs-smb, to access Windows/Cifs/Samba file shares first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

AFP support is included in gvfs. To access AFP files first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

SFTP support is also included in gvfs. To access folders via sftp, open the file manager, and enter the following into the path name, changing user@server_name and folder_name as appropriate:

For WebDAV, install gvfs-dnssd.

The following packages enable thumbnailing in most file managers, such as PCManFM, SpaceFM, Thunar, and xfeAUR. They are not needed for KDE's Dolphin or Konqueror, which use a separate thumbnailing system.

tumbler is the core backend for thumbnailing in many file managers. This must be installed to enable thumbnailing for various file types. It is not required for GNOME Files.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

PCManFM supports image thumbnails out of the box. However, in order to view thumbnails of other file types, PCManFM uses the information provided in the files located at /usr/share/thumbnailers. The packages which provide a thumbnailer usually add the corresponding .thumbnail file at /usr/share/thumbnailers. For example, in order to get thumbnails for OpenDocument files, you may install libgsf from the official repositories. For video files' thumbnails, the package ffmpegthumbnailer is required. For PDF files, you may install evince from the official repositories, which provides evince-thumbnailer and the corresponding file at /usr/share/thumbnailers. However, if you prefer not to install evince, you can also replicate the functionality of evince-thumbnailer using imagemagick's convert command. This is accomplished by creating a new file with the .thumbnailer extension (e.g.: imagemagick-pdf.thumbnailer) at /usr/share/thumbnailers with the following content:

Following this example, you can specify custom thumbnailers by creating your own .thumbnail files. Keep in mind that %i refers to the input file (the file which will have its thumbnail made), %o to the output file (the thumbnail image) and %s to the size of the thumbnail. These parameters will be automatically substituted with the corresponding data and passed to the thumbnailer program by PCManFM.

To extract compressed files such as tarballs (.tar and .tar.gz) within a file manager, it will first be necessary to install a GUI archiver such as file-roller. See List of applications/Utilities#Archiving and compression tools for further information. An additional package such as unzip must also be installed to support the use of zipped .zip files. Once an archiver has been installed, files in the file manager may consequently be right-clicked to be archived or extracted.

Archive files are mounted under folder /run/user/$(id -u)/gvfs/ with automatically created mount point that contains full path to the file in its name where all / are replaced with %252F and : replaced with %253A hex codes.

Example of path to the mounted archive /full/path/to/file/name.zip

See the NTFS article.

Some file managers make use of desktop notifications to confirm various events and statuses like mounting, unmounting and ejection of removable media.

The factual accuracy of this article or section is disputed.

Make trash directories .Trash-<uid> for each users on the top level of filesystems:

For example (mount point: /media/sdc1, uid: 1000, gid: 1000):

File managers using udisks require a polkit authentication agent. See polkit#Authentication agents.

The need to enter a password to access other partitions or mounted removable media will likely be due to the default permission settings of udisks2. More specifically, permission may be set to the root account only, not the user account. See Udisks#Configuration for details.

You may find that an application that is not a file manager, Audacious or Visual Studio Code for example, is set as the default application for opening directories — an application that specifies that it can handle the inode/directory MIME type in its desktop entry can become the default. You can query the default application for opening directories with the following command:

To ensure that directories are opened in the file manager, run the following command:

where my_file_manager.desktop is the desktop entry for your file manager — org.gnome.Nautilus.desktop for example.

Some other applications instead use the org.freedesktop.FileManager1 D-Bus protocol (e.g. Firefox). The following shows a list of currently installed services supporting this protocol:

To change what file manager is opened, symlink the file to $XDG_DATA_HOME/dbus-1/services/ or $HOME/.local/share/dbus-1/services/ if XDG_DATA_HOME variable is empty. Additionally, before the changes become active, kill the program currently implementing the D-Bus service.

Due to this gvfs commit you need to create your mount point inside /media/your-user-name/.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/gvfs/mounts/
```

Example 2 (unknown):
```unknown
~/.gvfs/mounts
```

Example 3 (unknown):
```unknown
~/.config/openbox/autostart
```

Example 4 (unknown):
```unknown
pcmanfm -d &
```

---

## Desktop entries

**URL:** https://wiki.archlinux.org/title/Desktop_entries

**Contents:**
- Basics
- Usage
- Application entry
  - File example
  - Key definition
  - Validation
  - Installation
  - Update database of desktop entries
- Icons
  - Common image formats

The XDG Desktop Entry specification defines a standard for applications to integrate into application menus of desktop environments implementing the XDG Desktop Menu specification.

Each desktop entry must have a Type and a Name key and can optionally define its appearance in the application menu.

The three available types are:

The following sections will roughly explain how these are created and validated.

Use a desktop opener like dex:

Desktop entries for applications, or .desktop files, are generally a combination of meta information resources and a shortcut of an application. These files usually reside in /usr/share/applications/ or /usr/local/share/applications/ for applications installed system-wide, or ~/.local/share/applications/ for user-specific applications. User entries take precedence over system entries.

Following is an example of its structure with additional comments. The example is only meant to give a quick impression, and does not show how to utilize all possible entry keys. The complete list of keys can be found in the freedesktop specification.

All recognized entries can be found on the freedesktop site. For example, the Type key defines three types of desktop entries: Application (type 1), Link (type 2) and Directory (type 3).

This should be avoided, as it will only be confusing to users. The Name key should only contain the name, or maybe an abbreviation/acronym if available.

As some keys have become deprecated over time, you may want to validate your desktop entries using desktop-file-validate(1) which is part of the desktop-file-utils package. To validate, run:

This will give you very verbose and useful warnings and error messages.

Use desktop-file-install(1) to install desktop file into target directory. For example:

This is also useful for customizing existing desktop entries (e.g. from /usr/share/applications) via edit options.

Usually, desktop entry changes are automatically picked up by desktop environments.

If this is not the case, and you want to forcefully update the desktop entries defined in ~/.local/share/applications, run the following command:

See also the Icon Theme Specification.

Here is a short overview of image formats commonly used for icons.

This article or section is a candidate for merging with ImageMagick#Usage.

If you stumble across an icon which is in a format that is not supported by the freedesktop.org standard (like gif or ico), you can use the magick tool (which is part of the imagemagick package) to convert it to a supported/recommended format, e.g.:

If you convert from a container format like ico, you will get all images that were encapsulated in the ico file in the form <icon name>-<number>.png. If you want to know the size of the image, or the number of images in a container file like ico you can use the identify tool (also part of the imagemagick package):

As you can see, the example ico file, although its name might suggest a single image of size 48x48, contains no less than 6 different sizes, of which one is even greater than 48x48, namely 128x128.

Alternatively, you can use icotool (from icoutils) to extract png images from ico container:

For extracting images from .icns container, you can use icns2png (provided by libicns):

Although packages that already ship with a .desktop file most certainly contain an icon or a set of icons, there is sometimes the case when a developer has not created a .desktop file, but may ship icons, nonetheless. So a good start is to look for icons in the source package. You can i.e. first filter for the extension with find and then use grep to filter further for certain buzzwords like the package name, "icon", "logo", etc, if there are quite a lot of images in the source package.

If the developers of an application do not include icons in their source packages, the next step would be to search on their web sites. Some projects, like i.e. tvbrowserAUR have an artwork/logo page where additional icons may be found. If a project is multi-platform, there may be the case that even if the linux/unix package does not come with an icon, the Windows package might provide one. If the project uses a Version control system like CVS/SVN/etc. and you have some experience with it, you also might consider browsing it for icons. If everything fails, the project might simply have no icon/logo yet.

The freedesktop.org standard specifies in which order and directories programs should look for icons:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Arronax is a graphical program to create and modify desktop entries for applications and locations. Install the arronaxAUR package to use it.

alacarte is a graphical menu editor for GNOME using the freedesktop.org menu specification. It also supports overriding desktop entries.

jddesktopentryeditAUR is a graphical program using Qt to edit desktop entries.

menulibreAUR is a graphical menu editor using GTK that provides modern features in a clean, easy-to-use interface.

libre-menu-editorAUR is a graphical program for editing desktop entries that aims to be feature-rich yet beginner-friendly.

It uses GTK with libadwaita and follows GNOME's interface guidelines, but is designed to work on any freedesktop.org compliant desktop environment.

gendesk started as an Arch Linux-specific tool for generating .desktop files by fetching the needed information directly from PKGBUILD files. Now it is a general tool that takes command-line arguments.

Icons can be automatically downloaded from openiconlibrary, if available. (The source for icons is configurable).

lsdesktopfAUR can list available .desktop files or search their contents.

It can also perform MIME-type-related searches. See XDG MIME Applications#lsdesktopf.

The fbrokendesktopAUR Bash script detects broken Exec values pointing to non-existent paths. Without any arguments it uses preset directories in the DskPath array. It shows only broken .desktop with full path and filename that is missing.

For system-wide .desktop files (e.g. those installed from a package), first copy the relevant .desktop file (e.g. from /usr/share/applications/) to $XDG_DATA_HOME/applications/ (e.g. ~/.local/share/applications/). This prevents your changes from being overwritten when the package gets updated during system upgrades. The local user-specific .desktop files should automatically take precedence over the system-wide files. Now you can modify the local user-specific .desktop file as needed.

Now, the file in your application launcher will stay the same as the one that is autostarted.

To set environment variables, in the .desktop file, edit the Exec= line to first use the env(1) command to set your variables. For example, with the original line commented out:

Also remove DBusActivatable=true (or set it to false) if present as it will cause the Exec line to be ignored.[1]

To change or add the command line arguments, edit the Exec= line to append the desired options. As an example, with the original line commented out:

Also remove DBusActivatable=true (or set it to false) if present as it will cause the Exec line to be ignored.[2]

The visibility of the desktop entry can be controlled in multiple ways. See the Desktop Entry Specification for more information. Add one of the following lines to your .desktop file:

**Examples:**

Example 1 (unknown):
```unknown
$ dex /usr/share/applications/firefox.desktop
```

Example 2 (unknown):
```unknown
KDE_SESSION_VERSION
```

Example 3 (unknown):
```unknown
/usr/share/applications
```

Example 4 (unknown):
```unknown
/usr/share/applications/
```

---

## Budgie

**URL:** https://wiki.archlinux.org/title/Budgie

**Contents:**
- Installation
  - Configuring user directories
  - File manager
- Starting
- Usage
- Theming
  - Customizing themes
    - Forking Materia
      - Making UI changes
      - Building and installing

Budgie is a desktop environment, formerly a project within Solus, becoming independent under the newly formed Buddies of Budgie organization in January 2022. It uses GTK for widgets, and is written in C and Vala. As of Budgie 10, the only available session is on Xorg.

Install the budgie package group to install all first-party components of the desktop. The individual budgie-desktop package. Installed alongside as runtime dependencies are budgie-screensaver for screen locking support, and budgie-control-center for modification of system settings. The following packages are optional, but add additional functionality to the desktop:

Extra applets developed by the Ubuntu Budgie team are available in the budgie-extras package - be warned, however, that this package also modifies existing functionality and could cause issues.

Follow the XDG user directories instructions to create the "well known" user directories like Desktop, Downloads, etc. Logout and log back in for the Budgie menu to detect changes to the configuration.

Budgie does not come with a file manager, and one is not installed by default. GNOME/Files (previously Nautilus) works well, and others are available.

Choose Budgie Desktop session from a display manager of choice, or modify xinitrc to include Budgie Desktop:

You can see your notification backlog, set the system and application volume, view a calendar, and see any currently playing videos or music with the "Raven" sidebar. The "Notifications" section can be accessed quickly with Super+n or by clicking on the Notifications applet in the panel, and the "Applets" section can be accessed quickly with Super+a. Raven can also be opened by clicking on the "Raven Trigger" applet in the panel, and will be opened to the previously selected pane.

Budgie uses GTK for its UI elements, and is thus supported by many GTK themes. Budgie also ships a built-in theme that is only applied to its own elements, such as panels and Raven, which can be toggled in Budgie Desktop Settings. Icon themes and cursor themes can be set in Budgie Desktop Settings as well.

Customizing GTK themes requires to build them from source. Each theme will have documentation on how to do so. For example, the Materia theme code can be found in their repository.

Materia comes with hacking and installation instructions. If the theme is already installed from the materia-gtk-theme package, it is recommended to rename the forked version just in case an edit breaks the UI:

The theme is written with Sass. For example, to make all windows have a square border (instead of rounded), change the $corner-radius variable:

The Sass compiler and the Meson builder are required. Both can be installed from dart-sass and meson packages. The theme can be built and installed with:

Once installed, the theme can be activated from Budge Desktop Settings.

Configuration of Budgie Desktop is done through the built-in Budgie Desktop Settings application, and changes to system settings are made through budgie-control-center.

Window button layout can be changed using dconf, dconf-editor or gsettings.

Budgie does not support using a different window manager.

**Examples:**

Example 1 (unknown):
```unknown
export XDG_CURRENT_DESKTOP=Budgie
exec budgie-desktop
```

Example 2 (unknown):
```unknown
meson_options.txt
```

Example 3 (unknown):
```unknown
option(
  'theme_name',
  type: 'string',
  value: 'Materia-fork',
  description: 'Base theme name',
)
```

Example 4 (unknown):
```unknown
$corner-radius
```

---

## Qtile

**URL:** https://wiki.archlinux.org/title/Qtile

**Contents:**
- Installation
- Starting
  - Xorg
  - Wayland
- Configuration
  - Groups
  - Group Rules
  - Keys
    - Sound
    - Language

From the project's website:

Install the qtile package.

In order to run Qtile as a Wayland compositor you will need to install python-pywlroots.

To run Qtile as an X11 window manager, run qtile start with xinit.

Start Qtile as a Wayland compositor by running qtile start -b wayland.

For the status of the Wayland development progress of Qtile, see https://github.com/qtile/qtile/discussions/2409.

As described in Configuration Lookup (or in the alternate documentation), Qtile provides a default configuration file at ~/.config/qtile/config.py that will be used in absence of user-defined ones.

The default configuration includes the shortcut Super+Enter to open a new terminal (selected from a hardcoded list), and Super+Ctrl+q to quit Qtile.

The most recent default configuration file can be downloaded from the git repository at libqtile/resources/default_config.py.

Several more complete configuration file examples can be found in the qtile-examples repository.

The configuration is fully done in Python: for a very quick introduction to the language you can read this tutorial.

Before restarting Qtile you can test your configuration file for syntax errors using the command:

If the command gives no output, your script is correct.

Alternatively, the command:

will perform a syntax check followed by additional type checking.

In Qtile, the workspaces (or views) are called Groups. They can be defined as following:

The following example shows how you can automatically move applications to workspaces based on properties such as title and wm_class. You might want to use xprop if you are running on X to get these.

You can configure your shortcuts with the Key class. Here is an example of the shortcut Alt+Shift+q to quit the window manager.

You can find out which modX corresponds to which key with the command Xmodmap.

You can add shortcuts to easily control the sound volume and state by adding a user to the audio group and using the alsamixer command-line interface, which can be installed through the alsa-utils package.

You can add shortcuts to easily switch between keyboard layouts in different languages using setxkbmap for example :

Create one Screen class for every monitor you have. The bars of Qtile are configured in the Screen class as in the following example:

You can find a list of all the built-in widgets in the official documentation (or in the alternate documentation).

If you want to add a widget to your bar, just add it like in the example above (for the WindowName widget). For example, if we want to add a battery notification, we can use the Battery widget:

To use Polybar instead of the default bar, you need to delete contents of the screen class:

To restart Polybar with Qtile, add Polybar's launching script with spawn command to restart Key in #Keys class, for example:

You can autostart applications using hooks, specifically the startup hook. For a list of available hooks see the documentation (or the alternate documentation).

Here is an example where an application starts only once:

Qtile writes its log into ~/.local/share/qtile/qtile.log

Starting Qtile on a different virtual screen can help diagnosing issues:

Qtile provides a Xephyr development script that can be easily modified to instantiate a system-installed package by replacing:

**Examples:**

Example 1 (unknown):
```unknown
qtile start
```

Example 2 (unknown):
```unknown
qtile start -b wayland
```

Example 3 (unknown):
```unknown
~/.config/qtile/config.py
```

Example 4 (unknown):
```unknown
Super+Enter
```

---

## File manager functionality

**URL:** https://wiki.archlinux.org/title/GVFS

**Contents:**
- Overview
- Additional features
  - Mounting
    - File manager daemon
    - Standalone
  - Networks
    - Windows access
    - Apple access
    - sftp access
    - WebDAV

This article outlines the additional software packages necessary to expand the features and functionality of file managers, particularly where using a window manager such as Openbox. The ability to access partitions and removable media without a password—if affected—has also been provided.

A file manager alone will not provide the features and functionality that users of full desktop environments such as Plasma or Xfce will be accustomed to. This is because additional software packages will be required to enable a given file manager to:

When a file manager has been installed as part of a full desktop environment, most of these packages will usually have been installed automatically. Consequently, where a file manager has been installed for a standalone window manager then - as is the case with the window manager itself - only a basic foundation will be provided. The user must then determine the nature and extent of the features and functionality to be added.

This article or section needs expansion.

When using a lightweight environment, the more added file manager features, the more memory usage is needed. See also udisks.

Folders used by GVFS:

Additional packages for installation usually follows the gvfs-* pattern, for example:

Most graphical file managers have the ability to automount devices plugged in while the program is running. You can leverage this for a system-wide solution by running the file manager in daemon mode (i.e. as a background process), if supported. For example, when using PCManFM in Openbox, the following command would be added to the ~/.config/openbox/autostart file:

It will also be necessary to configure the file manager itself in respect to volume management (e.g. what it will do and what applications will be launched when certain file types are detected upon mounting).

Another option is to install a separate mount application. The advantages of using this are:

If using gvfs-smb, to access Windows/Cifs/Samba file shares first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

AFP support is included in gvfs. To access AFP files first open the file manager, and enter the following into the path name, changing server_name and share_name as appropriate:

SFTP support is also included in gvfs. To access folders via sftp, open the file manager, and enter the following into the path name, changing user@server_name and folder_name as appropriate:

For WebDAV, install gvfs-dnssd.

The following packages enable thumbnailing in most file managers, such as PCManFM, SpaceFM, Thunar, and xfeAUR. They are not needed for KDE's Dolphin or Konqueror, which use a separate thumbnailing system.

tumbler is the core backend for thumbnailing in many file managers. This must be installed to enable thumbnailing for various file types. It is not required for GNOME Files.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

PCManFM supports image thumbnails out of the box. However, in order to view thumbnails of other file types, PCManFM uses the information provided in the files located at /usr/share/thumbnailers. The packages which provide a thumbnailer usually add the corresponding .thumbnail file at /usr/share/thumbnailers. For example, in order to get thumbnails for OpenDocument files, you may install libgsf from the official repositories. For video files' thumbnails, the package ffmpegthumbnailer is required. For PDF files, you may install evince from the official repositories, which provides evince-thumbnailer and the corresponding file at /usr/share/thumbnailers. However, if you prefer not to install evince, you can also replicate the functionality of evince-thumbnailer using imagemagick's convert command. This is accomplished by creating a new file with the .thumbnailer extension (e.g.: imagemagick-pdf.thumbnailer) at /usr/share/thumbnailers with the following content:

Following this example, you can specify custom thumbnailers by creating your own .thumbnail files. Keep in mind that %i refers to the input file (the file which will have its thumbnail made), %o to the output file (the thumbnail image) and %s to the size of the thumbnail. These parameters will be automatically substituted with the corresponding data and passed to the thumbnailer program by PCManFM.

To extract compressed files such as tarballs (.tar and .tar.gz) within a file manager, it will first be necessary to install a GUI archiver such as file-roller. See List of applications/Utilities#Archiving and compression tools for further information. An additional package such as unzip must also be installed to support the use of zipped .zip files. Once an archiver has been installed, files in the file manager may consequently be right-clicked to be archived or extracted.

Archive files are mounted under folder /run/user/$(id -u)/gvfs/ with automatically created mount point that contains full path to the file in its name where all / are replaced with %252F and : replaced with %253A hex codes.

Example of path to the mounted archive /full/path/to/file/name.zip

See the NTFS article.

Some file managers make use of desktop notifications to confirm various events and statuses like mounting, unmounting and ejection of removable media.

The factual accuracy of this article or section is disputed.

Make trash directories .Trash-<uid> for each users on the top level of filesystems:

For example (mount point: /media/sdc1, uid: 1000, gid: 1000):

File managers using udisks require a polkit authentication agent. See polkit#Authentication agents.

The need to enter a password to access other partitions or mounted removable media will likely be due to the default permission settings of udisks2. More specifically, permission may be set to the root account only, not the user account. See Udisks#Configuration for details.

You may find that an application that is not a file manager, Audacious or Visual Studio Code for example, is set as the default application for opening directories — an application that specifies that it can handle the inode/directory MIME type in its desktop entry can become the default. You can query the default application for opening directories with the following command:

To ensure that directories are opened in the file manager, run the following command:

where my_file_manager.desktop is the desktop entry for your file manager — org.gnome.Nautilus.desktop for example.

Some other applications instead use the org.freedesktop.FileManager1 D-Bus protocol (e.g. Firefox). The following shows a list of currently installed services supporting this protocol:

To change what file manager is opened, symlink the file to $XDG_DATA_HOME/dbus-1/services/ or $HOME/.local/share/dbus-1/services/ if XDG_DATA_HOME variable is empty. Additionally, before the changes become active, kill the program currently implementing the D-Bus service.

Due to this gvfs commit you need to create your mount point inside /media/your-user-name/.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/gvfs/mounts/
```

Example 2 (unknown):
```unknown
~/.gvfs/mounts
```

Example 3 (unknown):
```unknown
~/.config/openbox/autostart
```

Example 4 (unknown):
```unknown
pcmanfm -d &
```

---

## KDE

**URL:** https://wiki.archlinux.org/title/KDE_Plasma

**Contents:**
- Installation
  - Plasma
  - Plasma Mobile
  - KDE applications
  - Unstable releases
- Starting Plasma
  - Using a display manager
  - From the console
- Configuration
  - Personalization

KDE is a software project currently comprising a desktop environment known as Plasma, a collection of libraries and frameworks (KDE Frameworks) and several applications (KDE Applications) as well.

KDE upstream has a well maintained UserBase wiki. Detailed information about most KDE applications can be found there.

Install the plasma-meta meta-package or the plasma group. For differences between plasma-meta and plasma reference Package group. Alternatively, for a more minimal Plasma installation, install the plasma-desktop package. Upstream KDE has package and setup recommendations to get a fully-featured Plasma session.

If you are an NVIDIA user with the proprietary nvidia driver and wish to use the Wayland session, enable the DRM kernel mode setting.

Install plasma-mobileAUR.

To install the full set of KDE Applications, install the kde-applications-meta meta-package or the kde-applications group. If you only want KDE applications for a certain category, like gaming or education, install the relevant dependency of kde-applications-meta. Note that installing applications alone will not install any version of Plasma.

See Official repositories#kde-unstable for beta releases.

Starting from Plasma 6.4, the Wayland session has matured enough to become the default and preferred one: the X11 session is only available separately with the plasma-x11-session package[1]. The Xorg session is still supported, but will be removed in Plasma 7. See Wayland Known Significant Issues and X11 Known Significant Issues for more information.

Plasma can be started either using a display manager, or from the console.

Most settings for KDE applications are stored in ~/.config/. However, configuring KDE is primarily done through the System Settings application. It can be started from a terminal by executing systemsettings.

There are different types of KDE themes, varying by scope of what they modify:

For easy system-wide installation and updating, some themes are available in both the official repositories and the AUR.

Global themes can also be installed through System Settings > Colors & Themes > Global Theme > Get New....

The recommended theme for a pleasant appearance in GTK applications is breeze-gtk, a GTK theme designed to mimic the appearance of Plasma's Breeze theme. Install kde-gtk-config (part of the plasma group), relogin and select Breeze as the GTK theme in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style....

This article or section is out of date.

In some themes, tooltips in GTK applications have white text on white backgrounds making it difficult to read. To change the colors in GTK2 applications, find the section for tooltips in the .gtkrc-2.0 file and change it. For GTK3 application two files need to be changed, gtk.css and settings.ini.

Some GTK2 programs like vuescan-binAUR still look hardly usable due to invisible checkboxes with the Breeze or Adwaita skin in a Plasma session. To workaround this, install and select e.g. the Numix-Frost-Light skin of the numix-frost-themesAUR under System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style... > GTK theme. Numix-Frost-Light looks similar to Breeze.

Plasma and SDDM will both use images found at /var/lib/AccountsService/icons/ as users' avatars. To configure with a graphical interface, you can use System Settings > Users. The file corresponding to your username can be removed to restore the default avatar.

Plasmoids are widgets for Plasma desktop shell designed to enhance the functionality of desktop, they can be found on the AUR.

Plasmoid scripts can also be installed by right-clicking onto a panel or the desktop and choosing Enter Edit Mode > Add Widgets... > Get New Widgets... > Download New Plasma Widgets. This will present a front-end for https://store.kde.org/ that allows you to install, uninstall, or update third-party Plasmoid scripts with just one click.

Install plasma-pa or kmix (start Kmix from the Application Launcher). plasma-pa is now installed by default with plasma, no further configuration needed.

As the Plasma panel is on top of other windows, its shadow is drawn over them. [5] To disable this behaviour without impacting other shadows, install xorg-xprop and run:

then select the panel with the plus-sized cursor. [6] For automation, install xorg-xwininfo and create the following script:

Make the script executable.

The factual accuracy of this article or section is disputed.

The script can be run on login with Add Login Script in Autostart:

See HiDPI#KDE Plasma.

The plasma-phone-settings repository contains several recommended settings which can be applied globally (/etc/xdg) and/or per user (~/.config).

/etc/xdg/kscreenlockerrc (or ~/.config/kscreenlockerrc) locks the screen immediately after login. [7] This is useful in combination with SDDM#Autologin.

To use a virtual keyboard in the Wayland session, install maliit-keyboard and enable it in System Settings > Keyboard > Virtual Keyboard.

If your device has a hardware keyboard, but you want to use the virtual keyboard, add the KWIN_IM_SHOW_ALWAYS=1 environment variable to your Wayland session.

To use a virtual keyboard in the X11 session, choose an appropriate one from List of applications/Utilities#On-screen keyboards and run it manually.

Window decorations can be found in the AUR.

They can be changed in System Settings > Colors & Themes > Window Decorations, there you can also directly download and install more themes with one click.

Icon themes can be installed and changed on System Settings > Colors & Themes > Icons.

The Plasma Netbook shell has been dropped from Plasma 5, see the following KDE forum post. However, you can achieve something similar by editing the file ~/.config/kwinrc adding BorderlessMaximizedWindows=true in the [Windows] section.

To allow thumbnail generation for media or document files on the desktop and in Dolphin, install kdegraphics-thumbnailers and ffmpegthumbs.

Then enable the thumbnail categories for the desktop via right click on the desktop background > Configure Desktop and Wallpaper... > Icons > Configure Preview Plugins....

In Dolphin, navigate to Configure > Configure Dolphin... > Interface > Previews.

Plasma provides a Redshift-like feature (working on both Xorg and Wayland) called Night Light. It makes the colors on the screen warmer to reduce eye strain at the time of your choosing. It can be enabled in System Settings > Colors & Themes > Night Light.

You can also configure printers in System Settings > Printers. To use this method, you must first install the following packages print-manager, cups, system-config-printer. See CUPS#Configuration.

The Dolphin share functionality requires the package kdenetwork-filesharing and usershares, which the stock smb.conf does not have enabled. Instructions to add them are in Samba#Enable Usershares, after which sharing in Dolphin should work out of the box after restarting Samba.

Accessing Windows shares from Dolphin works out of the box. Use the path smb://servername/share to browse the files.

Unlike GTK file browsers which utilize GVfs also for the launched program, opening files from Samba shares in Dolphin via KIO makes Plasma copy the whole file to the local system first with most programs (VLC is an exception). To workaround this, you can use a GTK based file browser like thunar with gvfs and gvfs-smb (and gnome-keyring for saving login credentials) to access SMB shares in a more able way.

Another possibility is to mount a Samba share via cifs-utils to make it look to Plasma like if the SMB share was just a normal local folder and thus can be accessed normally. See Samba#Manual mounting and Samba#Automatic mounting.

A GUI solution is available with samba-mounter-gitAUR, which offers basically the same functionality via an easy to use option located at System Settings > Network Drivers. However, it might break with new KDE Plasma versions.

KDE Desktop Activities are special workspaces where you can select specific settings for each activity that apply only when you are using said activity.

Install powerdevil for an integrated Plasma power managing service. This service offers additional power saving features, monitor brightness control (if supported) and battery reporting including peripheral devices.

The factual accuracy of this article or section is disputed.

Plasma can autostart applications and run scripts on startup and shutdown. To autostart an application, navigate to System Settings > Autostart and add the program or shell script of your choice. For applications, a .desktop file will be created, for login scripts, a .desktop file launching the script will be created.

See official documentation.

Phonon is being widely used within KDE, for both audio (e.g., the System notifications or KDE audio applications) and video (e.g., the Dolphin video thumbnails). It can use the following backends:

KDE recommends only the VLC backend, as the GStreamer backend is unmaintained.

Plasma stores personalized desktop settings as configuration files in the XDG_CONFIG_HOME folder. Use the detail of configuration files to select and choose a method of backup and restore.

Plasma uses a systemd user instance to launch and manage all the Plasma services. This is the default startup method since Plasma 5.25, but can be disabled to use boot scripts instead with the following command (however this may stop working in a future release):

More details about the implementation can be read in Edmundson's blog: Plasma and the systemd startup.

KDE applications use sonnet for spell checking. See its optional dependencies for the supported spell checkers.

Configure it in System Settings > Spell Check.

See https://community.kde.org/Plasma/Wayland/Nvidia.

The KDE project provides a suite of applications that integrate with the Plasma desktop. See the kde-applications group for a full listing of the available applications. Also see Category:KDE for related KDE application pages.

Aside from the programs provided in KDE Applications, there are many other applications available that can complement the Plasma desktop. Some of these are discussed below.

Navigate to the submenu System Settings > Keyboard > Advanced (tab) > Key sequence to kill the X server and ensure that the checkbox is ticked.

KCM stands for KConfig Module. KCMs can help you configure your system by providing interfaces in System Settings, or through the command line with kcmshell6.

More KCMs can be found at linux-apps.com.

KDE implements desktop search with a software called Baloo, a file indexing and searching solution.

The following web browsers can integrate with Plasma:

KDE offers its own stack for personal information management (PIM). This includes emails, contacts, calendar, etc. To install all the PIM packages, you could use the kde-pim package group or the kde-pim-meta meta package.

Akonadi is a system meant to act as a local cache for PIM data, regardless of its origin, which can be then used by other applications. This includes the user's emails, contacts, calendars, events, journals, alarms, notes, and so on. Akonadi does not store any data by itself: the storage format depends on the nature of the data (for example, contacts may be stored in vCard format).

Install akonadi. For additional addons, install kdepim-addons.

By default Akonadi will use /usr/bin/mysqld (MariaDB by default, see MySQL for alternative providers) to run a managed MySQL instance with the database stored in ~/.local/share/akonadi/db_data/.

Akonadi supports using the system-wide MySQL for its database.[10]

This article or section needs expansion.

Akonadi supports either using the existing system-wide PostgreSQL instance, i.e. postgresql.service, or running a PostgreSQL instance with user privileges and the database in ~/.local/share/akonadi/db_data/.

Install postgresql and postgresql-old-upgrade.

Edit the Akonadi configuration file so that it has the following contents:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

This requires an already configured and running PostgreSQL.

Create a PostgreSQL user account for your user:

Create a database for Akonadi:

Edit the Akonadi configuration file to match the configuration below:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

To use SQLite, edit the Akonadi configuration file to match the configuration below:

Users who want to disable Akonadi would need to not start any KDE applications that rely on it. See this section in the KDE userbase for more information.

KDE Connect provides several features to connect your Android or iOS phone with your Linux desktop:

You will need to install KDE Connect both on your computer and on your phone. For PC, install kdeconnect package. For Android, install KDE Connect from Google Play or from F-Droid. If you want to browse your phone's filesystem, you need to install sshfs as well and configure filesystem exposes in your Android app. For iOS, install KDE Connect from the App Store. Not all features from the Android version are available on the iOS version.

To use remote input functionality on a Plasma Wayland session, the xdg-desktop-portal package is required.

It is possible to use KDE Connect even if you do not use the Plasma desktop. For GNOME users, better integration can be achieved by installing gnome-shell-extension-gsconnectAUR instead of kdeconnect. To start the KDE Connect daemon manually, execute /usr/bin/kdeconnectd.

If you use a firewall, you need to open UDP and TCP ports 1714 through 1764.

Sometimes, KDE Connect will not detect a phone. You can restart the services by running killall kdeconnectd and then opening kdeconnect in system settings or running kdeconnect-cli --refresh followed by kdeconnect-cli -l. You can also use Pair new device > Add devices by IP on KDE Connect for Android.

It is possible to use a window manager other than KWin with Plasma. This allows you to combine the functionality of the KDE desktop with the utility of a tiling window manager, which may be more fleshed out than KWin tiling scripts.

The component chooser settings in Plasma no longer allows changing the window manager, but you are still able to swap KWin via other methods.

Since KDE 5.25, Plasma's systemd based startup is enabled by default.

To replace KWin in this startup, you must first mask the plasma-kwin_x11.service for the current user to prevent it from starting.

Then, create a new systemd user unit to start your preferred WM [11]:

To use it, do (as user units) a daemon-reload, make sure you have masked plasma-kwin_x11.service then enable the newly created plasma-custom-wm.service.

Plasma's script-based boot is used by disabling #systemd startup. If you have done so, you can change the window manager by setting the KDEWM environment variable before Plasma is invoked.

This article or section is a candidate for merging with Environment variables#Globally.

If you have root access, you can also add an XSession that will be available to all users as an option on the login screen.

First, create a script with execution permissions as follows:

Replace /usr/bin/i3 to the path to your preferred WM. Ensure the path is correctly set. If KDE is unable to start the window manager, the session will fail and the user will be returned to the login screen.

Then, to add an XSession, add a file in /usr/share/xsessions/ with the following content:

The openbox package provides a session for using KDE with Openbox. To make use of this session, disable #systemd startup and select KDE/Openbox from the display manager menu.

For those starting the session manually, add the following line to your xinit configuration:

A list of KWin extensions that can be used to make KDE behave more like a tiling window manager.

To enable display resolution management and multiple monitors in Plasma, install kscreen. This provides additional options to System Settings > Display & Monitor.

On X11, ICC profiles are handled by colord. To configure them in Plasma, install colord-kde. This provides additional options in System Settings > Color Management. ICC profiles can be imported using Import Profile.

For Wayland sessions, color management is handled by the compositor, i.e. KWin for Plasma. In this case, no additional package is required. The color profile can be configured per monitor in System Settings > Display & Monitor > Color Profile.

HDR support is experimental and only works in a Wayland session. System Settings > Display & Monitor > High Dynamic Range > Enable HDR.

For more information on displaying HDR content see HDR monitor support. Development details about HDR in Plasma can be found on Xaver Hugl's blog post.

When enabling HDR mode in KDE Plasma, SDR content can appear extremely dark, sometimes making the screen nearly unreadable. To address this, KDE provides two key sliders in display settings: Maximum SDR Brightness, which adjusts the brightness mapping for SDR content in HDR mode, and Brightness which controls the overall display backlight or luminance

To disable this feature, you currently have to edit the kwinrc config file and set the Meta key under ModifierOnlyShortcuts to an empty string:

Alternatively, you can also run the following command:

With the Plasma Browser integration installed, KDE will show bookmarks in the application launcher.

To disable this feature, go to System Settings > Search > Plasma Search and uncheck Bookmarks.

IBus is an input method framework and can be integrated into KDE. See IBus#Integration for details.

Using IBus may be required when using KDE on Wayland to offer accented characters and dead keys support [12].

See NetworkManager#Sharing internet connection over Wi-Fi.

If you have System Settings > Session > Desktop Session > Session Restore > On login, launch apps that were open: On last logout (default) selected, ksmserver (KDE's session manager) will automatically save/load all open applications to/from ~/.config/ksmserverrc on logout/login.

If you have set up local mail delivery with a mail server that uses the Maildir format, you may want to receive this mail in KMail. To do so, you can re-use KMail's default receiving account "Local Folders" that stores mail in ~/.local/share/local-mail/.

Symlink the ~/Maildir directory (where Maildir format mail is commonly delivered) to the Local Folders' inbox:

Alternatively, add a new receiving account with the type Maildir and set ~/Maildir as its directory.

Edit config/main.xml files in the /usr/share/plasma. For example, to configure the Application Launcher for all users, edit /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml. To prevent the files from being overwritten with package updates, add the files to Pacman's NoUpgrade

This article or section is a candidate for merging with Power management.

Properly disable the hibernate feature and hide it from the menu with a Polkit policy rule.

Alternatively, add the following lines to a file in /etc/systemd/sleep.conf.d/:

Kwin has the ability to specify rules for specific windows/applications. For example, you can force enable the window titlebar even if the application developer decided that there should not be one. You can set such rules as specific starting position, size, minimize state, keeping above/below others and so on.

To create a rule you can press Alt+F3 when the window of interest is in focus. Then, in More Actions > Configure special application/window settings, you can set the desired property. A list of created rules is available from System Settings > Window Management > Window Rules.

By default KDE mount manager (kio-fuse) will mount network shares to ${XDG_RUNTIME_DIR}/kio-fuse-6-char-random-string.

Create directory, e.g. mnt_kio in your home directory:

Override default kio-fuse.service using a drop-in file:

Now if you mount your network shares via dbus or by openning some file from remote share in Dolphin:

They will be mounted to ~/mnt_kio.

To have the menu bar integrated with the title bar, install material-kwin-decoration-gitAUR from the AUR, then in System Settings > Window Decorations, select 'Material' and add the Application Menu button to the title bar (preferably as second from the left). Works only on X11 session.

Xdg-desktop-portal-kde has support for remote input from a remote desktop session, a virtual KVM switch, kde-connect, emulated devices like a controller using steam-input, etc. This authorization is lost after the application or the desktop-portal is restarted, which causes the "Remote control requested" window pop up every time and makes unattended access impossible.

As of plasma version 6.3, a permission system was implemented, which allows to pre-authorize applications. Currently, the permission api is only available through the flatpak cli, although applications do not need to run as a flatpak to be able to get pre-authorized.

As per the upstream docs and flatpak-permission-set man pages, you need to figure out if the application you want to authorize sets an application ID or not. If started through a runner like KRunner, it gets set by plasma and is usually the filename of the .desktop-file under /usr/share/applications.

For example, to pre-authorize a virtual KVM switch like lan-mouse, you would do:

If you start it as a daemon in a systemd user-unit, you should use the name of that unit instead:

If you application does not set an ID, you can leave that field empty:

Wayland is used by default for KDE 6 applications, and the KDE applications fail to work under GNOME Wayland (and potentially other DEs/WMs) in this scenario. This can be fixed by setting the QT_QPA_PLATFORM=xcb environment variable.

This is a workaround for KDE bugs and not a problem with Wayland itself.

After the last upgrade to KDE 6 you may notice issues with all of the KDE icons not displaying. Newly created accounts showed them just fine.

The issue for this is that the theme got lost while upgrading and had to be reassigned manually. For this go to System Settings > Colors & Themes > Icons and select the theme you would like to use for the icons again.

This article or section is out of date.

Latest update might cause incompatible HiDPI scaling that made some interfaces becomes too big for your screen, some icons are missing or can not be displayed, and missing panels or widgets.

Try to remove qt5ct and kvantum related package, then apply default global Plasma theme. If the problem persists, try clearing all your KDE configuration and reinstalling plasma to overwrite the configuration. Be sure to check HiDPI scaling in KDE system settings as well.

Try to force font DPI to 96 in System Settings > Text & Fonts > Fonts.

If that does not work, try setting the DPI directly in your Xorg configuration as documented in Xorg#Setting DPI manually.

Many problems in KDE are related to its configuration.

Plasma problems are usually caused by unstable Plasma widgets (colloquially called plasmoids) or Plasma themes. First, find which was the last widget or theme you had installed and disable or uninstall it.

So, if your desktop suddenly exhibits "locking up", this is likely caused by a faulty installed widget. If you cannot remember which widget you installed before the problem began (sometimes it can be an irregular problem), try to track it down by removing each widget until the problem ceases. Then you can uninstall the widget, and file a bug report on the KDE bug tracker only if it is an official widget. If it is not, it is recommended to find the entry on the KDE Store and inform the developer of that widget about the problem (detailing steps to reproduce, etc.).

If you cannot find the problem, but you do not want all the settings to be lost, navigate to ~/.config/ and run the following command:

This command will rename all Plasma related configuration files to *.bak (e.g. plasmarc.bak) of your user and when you will relogin into Plasma, you will have the default settings back. To undo that action, remove the .bak file extension. If you already have *.bak files, rename, move, or delete them first. It is highly recommended that you create regular backups anyway. See Synchronization and backup programs for a list of possible solutions.

The problem may be caused by old cache. Sometimes, after an upgrade, the old cache might introduce strange, hard to debug behaviour such as unkillable shells, hangs when changing various settings, Ark being unable to extract archives or Amarok not recognizing any of your music. This solution can also resolve problems with KDE and Qt applications looking bad after an update.

Rebuild the cache using the following commands:

Optionally, empty the ~/.cache/ folder contents, however, this will also clear the cache of other applications:

Sometimes, empty the ~/.cache/ folder does not work, for example, if you encountered the following error:

It might be something related to outdated configuration files. In the above case, moving ~/.config/menus/ folder away may fix the issue. In other cases, try moving each file out of ~/.config/menus/ folder could be a good way to check what triggers the error.

Plasma desktop may use different settings than you set at KDE System Settings panel, or in locale.conf (per Locale#Variables). First thing to do is log out and log in after removing ~/.config/plasma-localerc, if this does not fix the issue, try to edit the file manually. For example, to set LANG variable to es_ES.UTF-8 and the LC_MESSAGES variable to en_US.UTF-8:

Make sure that QT_QPA_PLATFORMTHEME environment variable is unset, the command printenv QT_QPA_PLATFORMTHEME should show empty output. Otherwise if you had an environment set (most likely qt5ct or qt6ct) the variable will force qt5ct/qt6ct settings upon Qt applications, the command export QT_QPA_PLATFORMTHEME= should unset the environment.

An easier (and more reliable) solution can be to uninstall completely qt5ct and qt6ct.

Hiding certain items in the System Tray settings (e.g. Audio Volume, Media Player or Notifications) also disables related features. Hiding the Audio Volume disables volume control keys, Media Player disables multimedia keys (rewind, stop, pause) and hiding Notifications disables showing notifications.

The Login Screen KCM reads your cursor settings from ~/.config/kcminputrc, without this file no settings are synced. The easiest way to generate this file is to change your cursor theme in System Settings > Colors & Themes > Cursors, then change it back to your preferred cursor theme.

A crash or hardware change can modify the screen numbers, even on a single monitor setup. The panels/widgets can be missing after such an event, this can be fixed in the ~/.config/plasma-org.kde.plasma.desktop-appletsrc file by changing the lastScreen values.

Make sure you have the proper driver for your GPU installed. See Xorg#Driver installation for more information. If you have an older card, it might help to #Disable desktop effects manually or automatically for defined applications or #Disable compositing.

Hybrid graphics is a power management strategy commonly used in laptops that keeps the dedicated graphics processor (dGPU) inactive when not needed, defaulting to the integrated graphics processor (iGPU) for basic desktop rendering to conserve battery life.

While this approach saves power, it can result in suboptimal desktop performance, including low frame rates in animations and potential graphical artifacts, even on systems with capable dGPUs.

Forcing KDE Plasma to utilize the discrete GPU can significantly improve desktop responsiveness and visual quality.

For systems using open-source graphics drivers (Intel + AMDGPU, Intel + Nouveau), you can globally set the DRI_PRIME environment variable to specify the dGPU:

The index value (0 or 1) depends on your system configuration. Verify which index corresponds to your dGPU by running:

For direct control over KWin's GPU selection, create a startup script that sets the DRM device priority:

To identify your DRM cards and their corresponding GPUs:

List the dGPU first in the KWIN_DRM_DEVICES variable to prioritize it for rendering.

This command prints out a summary of the current state of KWin including used options, used compositing backend and relevant OpenGL driver capabilities. See more on Martin's blog.

Plasma has desktop effects enabled by default and e.g. not every game will disable them automatically. You can disable desktop effects in System Settings > Window Management > Desktop Effects and you can toggle desktop effects with Alt+Shift+F12.

Additionally, you can create custom KWin rules to automatically disable/enable compositing when a certain application/window starts under System Settings > Window Management > Window Rules.

If you use a transparent background without enabling the compositor, you will get the message:

In System Settings > Display & Monitor > Compositor, check Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Allow applications to block compositing. This may harm performance.

Setting the environment variable QSG_USE_SIMPLE_ANIMATION_DRIVER for KWIN reduces jerking in some Quick Scene Graphics based effects. For this purpose, it is sufficient to create a drop-in for the service running KWIN:

(in the case of Wayland session, use plasma-kwin_wayland.service.d as directory name)

Then restart the session.

Another try is to set QSG_NO_VSYNC instead of QSG_USE_SIMPLE_ANIMATION_DRIVER.

Create the directory ~/.local/share/icons/default/ (alternatively, ~/.icons/default), then, inside it, create a file named index.theme, then add to it the following contents:

If applicable, replace breeze_cursors with the cursor theme you use (cursor themes can be found in /usr/share/icons/, e.g. Breeze_Light).

On Wayland, it is necessary for xdg-desktop-portal-gtk to be installed for GTK/GNOME applications to correctly apply cursor themes.

Firefox and Thunderbird running under Wayland will refer to GSettings to determine which cursor to display.

To sync KDE settings to GTK applications, install kde-gtk-config.

If you do not want to install an extra package, you can set the cursor theme manually:

Try installing the appropriate 2D acceleration driver for your system and window manager.

Your local configuration settings for kscreen can override those set in xorg.conf. Look for kscreen configuration files in ~/.local/share/kscreen/ and check if mode is being set to a resolution that is not supported by your monitor.

In order to add icons to tray, applications often make use of the library appindicator. If your icons are blurry, check which version of libappindicator you have installed. If you only have libappindicator-gtk2AUR installed, you can install libappindicator as an attempt to get clear icons.

When running Plasma in a VMware, VirtualBox or QEMU virtual machine, kscreen may not allow changing the guest's screen resolution to a resolution higher than 800×600.

The workaround is to set the PreferredMode option in xorg.conf.d(5). Alternatively try using a different graphics adapter in the VM, e.g. VBoxSVGA instead of VMSVGA for VirtualBox and Virtio instead of QXL for QEMU. See KDE Bug 407058 for details.

Check whether your user directories (Documents, Downloads, etc.) are read-only.

In System Settings > Display & Monitor > Compositor, change Keep window thumbnails from Only from Shown windows to Never. If you are using Intel graphics, ensure that xf86-video-intel is not installed.

See XDG Desktop Portal#Poor font rendering in GTK applications on KDE Plasma.

You may observe that windows of some applications do not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk.

See Nouveau#Random lockups with kernel error messages.

If there is no sound after suspending and KMix does not show audio devices which should be there, restarting plasmashell and pulseaudio may help:

Some applications may also need to be restarted in order for sound to play from them again.

This can be solved by installing the GStreamer libav plugin (package gst-libav). If you still encounter problems, you can try changing the Phonon backend used by installing another such as phonon-qt6-vlc.

Then, make sure the backend is preferred via phononsettings.

Check if you have plasma-pa installed.

If journalctl -p4 -t pulseaudio contains entries saying Failed to create sink input: sink is suspended, try commenting the following line in /etc/pulse/default.pa:

If the issue persists, plasma-meta or plasma may have installed pulseaudio alongside wireplumber. To fix the issue, replace pulseaudio with pipewire-pulse. If pulseaudio is preferred, replace wireplumber with pipewire-media-session. See PipeWire#PulseAudio clients and this forum thread for more details.

If your system is able to suspend or hibernate using systemd but do not have these options shown in KDE, make sure powerdevil is installed.

Make sure you installed powerdevil and power-profiles-daemon. Run powerprofilesctl and check the driver. If it is intel_pstate or amd_pstate, you are done, otherwise see CPU frequency scaling#Scaling drivers for more information on enabling them.

See [13] for details.

If you want a backup, copy the following configuration directories:

For some IMAP accounts KMail will show the inbox as a top-level container (so it will not be possible to read messages there) with all other folders of this account inside.[14]. To solve this problem simply disable the server-side subscriptions in the KMail account settings.

While setting up EWS account in KMail, you may keep getting errors about failed authorization even for valid and fully working credentials. This is likely caused by broken communication between KWallet and KMail. To workaround the issue set a passsword via qdbus:

See Qt#Disable/Change Qt journal logging behaviour.

See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

It is not recommended to turn off the KWallet password saving system in the user settings as it is required to save encrypted credentials like Wi-Fi passphrases for each user. Persistently occuring KWallet dialogs can be the consequence of turning it off.

In case you find the dialogs to unlock the wallet annoying when applications want to access it, you can let the display managers SDDM and LightDM unlock the wallet at login automatically, see KDE Wallet#Unlock KDE Wallet automatically on login. The first wallet needs to be generated by KWallet (and not user-generated) in order to be usable for system program credentials.

In case you want the wallet credentials not to be opened in memory for every application, you can restrict applications from accessing it with kwalletmanager in the KWallet settings.

If you do not care for credential encryption at all, you can simply leave the password forms blank when KWallet asks for the password while creating a wallet. In this case, applications can access passwords without having to unlock the wallet first.

This can be solved by installing packagekit-qt6.

Discover sometimes will not remove its PackageKit alpm lock. To release it, remove /var/lib/PackageKit/alpm/db.lck. Use "Refresh" in Discover and updates should appear (if there are any updates pending).

As described in KDE Bug 347772 NVIDIA OpenGL drivers and QML may not play well together with Qt 5. This may lead kscreenlocker_greet to high CPU usage after unlocking the session. To work around this issue, set the QSG_RENDERER_LOOP environment variable to basic.

Then kill previous instances of the greeter with killall kscreenlocker_greet.

If your home directory is on a ZFS pool, create a ~/.config/akonadi/mysql-local.conf file with the following contents:

See MariaDB#OS error 22 when running on ZFS.

This is caused by the problematic way of GTK3 handling mouse scroll events. A workaround for this is to set environment variable GDK_CORE_DEVICE_EVENTS=1. However, this workaround also breaks touchpad smooth scrolling and touchscreen scrolling.

When using TeamViewer, it may behave slowly if you use smooth animations (such as windows minimizing). See #Disable compositing as a workaround.

Kmail may become unresponsive, show a black messageviewer or similar, often after having been minimized and restored. A workaround may be to set environment variable QT_QPA_PLATFORM="xcb;wayland". See KDE Bug 397825.

If you previously locked your widgets, you will probably find yourself unable to unlock them again. You just have to run this command to do so:

The new Customize Layout does not require to lock them back up but if want to do that:

Check file associations regarding HTML, PHP, etc... and change it to a browser. KIO's cache files are located in $HOME/.cache/kioexec. See also xdg-utils#URL scheme handlers.

In the System Settings application, KDE offers a setting to automatically lock the screen after waking up from sleep. Upon resuming, some users report that the screen is briefly showed before locking. To prevent this behavior and have KDE lock the screen before suspending, create a hook in systemd(1) by creating the following file as the root user:

The use of sleep is necessary in order for the loginctl lock-session command to complete before the device is suspended. Using a lower timeout may not allow for this to complete.

After creating the file, make it executable.

Finally, make sure that the KDE setting is enabled by going to System Settings > Screen Locking and checking the Lock screen automatically: After waking from sleep checkbox.

Some X11 software like freerdp can grab keyboard input since KDE 5.27. Others like VMware cannot grab correctly. [15]

It is inappropriate to force grab in Xserver or in compositors. [16] You can solve it in an elegant way as follows:

This can be caused because system settings cannot access/modify the .config folder in your home directory.

To fix this, you need to change the owner of the folder:

user refers to the name of the user that you are logged into in KDE Plasma. If the name of your home directory is not the same as the user you are logged in as, you can change it accordingly.

If this does not work, you might need to change the permissions of the folder:

There are issues with the Widget "Global Menu" not working with some applications even after installing appmenu-gtk-module and libdbusmenu-glib. The fix is to install the plasma5-integration and to restart your Session.

The factual accuracy of this article or section is disputed.

It is necessary to add a Polkit rule allowing mounting of internal drives without elevated privileges:

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/plasma-dbus-run-session-if-needed /usr/bin/startplasma-wayland
```

Example 2 (unknown):
```unknown
export DESKTOP_SESSION=plasma
```

Example 3 (unknown):
```unknown
exec startplasma-x11
```

Example 4 (unknown):
```unknown
startx /usr/bin/startplasma-x11
```

---

## LXQt

**URL:** https://wiki.archlinux.org/title/LXQt

**Contents:**
- Installation
- Starting the desktop
  - Using xinit
  - Graphical login
- Configuration
  - Screen Brightness
  - Panel widgets
  - Use a different window manager
  - Wayland Session
  - Autostart

LXQt is a desktop environment built on Qt which derives from Razor-qt and LXDE components which were ported to Qt. While development is mainly focused on LXQt, the GTK 2 version of LXDE will see continued development.

First, install and configure Xorg. Then, install the lxqt group and an icon theme (e.g. breeze-icons or oxygen-icons).

For additional functionality, you may wish to install the following:

Append the following line to Xinitrc:

Choose LXQt Desktop from the menu in a display manager of choice.

LXQt in general tries to provide GUI applications to change its settings. Configuration files are in ~/.config/lxqt. This directory is initialized automatically. The default configuration for new users is found in /usr/share/lxqt.

If you find that LXQt uses screen contrast control instead of screen brightness control for the screen brightness keyboard shortcuts, you can change the command to use xbacklight instead under the LXQt configuration center > shortcut keys

If you are using the Intel kernel modesetting driver xbacklight will not work, but you can use the following command instead

You may need to create two scripts for screen brightness up and down and point the keyboard shortcut to the path of the scripts for it to work.

Another way to change screen brightness is to use brightnessctl

If you cannot add the CPU and System Statistics widgets to the panel, make sure libstatgrab and libsysstat are installed.

LXQt presents a dialog to pick the preferred window manager at the first login. After that, you can specify a different window manager to use with LXQt via Session Settings, lxqt-config-session; or by editing ~/.config/lxqt/session.conf. Change the following line:

to a window manager of choice:

To enable the experimental Wayland session lxqt-wayland-session has to be installed. This will enable under Session Settings the settings for the compositor and the screensaver under Wayland.

Supported compositors are hyprland, labwc, niri, kwin, river, sway and wayfireAUR. For other compositors manual configuration is needed, as the compositor needs to start lxqt-session.

Supported screensavers are hyprlock, swaylock and waylock. If kwin_wayland is used the command in Session Settings needs to be set to loginctl lock-session to use its screen locker.

Choose LXQt (Wayland) from the menu in a display manager which supports Wayland. The LXQt Wayland Session can be started from console directly with startlxqtwayland.

To have applications start on login, click the main menu from the LXQt > Preferences > LXQt Settings > Session Settings. Alternatively, this can be launched with:

From this window, click on AutoStart on the left side. Here you can add a new application to either the global autostart (launched in all sessions implementing the XDG Autostart specification) or your local autostart (labelled LXQt Autostart). For each item you add, lxqt-config-session will create a Desktop entry (.desktop file) in the appropriate XDG Autostart directory.

The distinction between "Global Autostart" and "LXQt Autostart" does not depend on the directory in which the corresponding .desktop file is located, but rather on the OnlyShowIn setting. If it is OnlyShowIn=true, it is considered an "LXQt Autostart". Furthermore, if X-LXQt-Module=true, the item is not shown in lxqt-config-session.

Environment variables for LXQt session can be defined in Session Settings.

It is possible to edit menu entries by editing their .desktop files stored in /usr/share/applications/lxqt-*.desktop files. See Desktop entries.

You can add a compositor like picom to autostart applications with a command like the following

One can customize the options available under Leave simply by copying the respective package provide .desktop file to ~/.local/share/applications and modifying it to contain the NoDisplay=true directive. Reference: #876.

Complete list of files to consider masking include:

Example: remove hibernate option.

When moving icons on the desktop it is possible to place them a bit too close to each other making them connected. If unable to separate them Stop Desktop from Session Settings, remove ~/.config/pcmanfm-qt/lxqt/desktop-items-0.conf and Start Desktop again.

Running LXQt with xrdp for remote login has the benefit of being fast and convenient, while minimizing resource consumption on the server. Setting up xrdp is rather painless, and only requires a user to adjust the ~/.xinitrc. Since LXQt appears to rely on some D-Bus service functionality, that file should have the following line at the end [1]:

**Examples:**

Example 1 (unknown):
```unknown
exec startlxqt
```

Example 2 (unknown):
```unknown
~/.config/lxqt
```

Example 3 (unknown):
```unknown
/usr/share/lxqt
```

Example 4 (unknown):
```unknown
xbacklight -inc 10
xbacklight -dec 10
```

---

## Window manager

**URL:** https://wiki.archlinux.org/title/Tiling_window_manager

**Contents:**
- Overview
  - Types
- List of window managers
  - Stacking window managers
  - Tiling window managers
  - Dynamic window managers
- See also

It can be part of a desktop environment or be used standalone.

Window managers are X clients that control the appearance and behaviour of the frames ("windows") where the various graphical applications are drawn. They determine the border, title bar, size, and ability to resize windows, and often provide other functionality such as reserved areas for sticking dockapps like Window Maker, or the ability to tab windows like Fluxbox. Some window managers are even bundled with simple utilities like menus to start programs or to configure the window manager itself.

The Extended Window Manager Hints specification is used to allow window managers to interact in standard ways with the server and the other clients.

Some window managers are developed as part of a more comprehensive desktop environment, usually allowing the other provided applications to better interact with each other, giving a more consistent experience to the user, complete with features like desktop icons, fonts, toolbars, wallpapers, or desktop widgets.

Other window managers are instead designed to be used standalone, giving the user complete freedom over the choice of the other applications to be used. This allows the user to create a more lightweight and customized environment, tailored to their own specific needs. "Extras" like desktop icons, toolbars, wallpapers, or desktop widgets, if needed, will have to be added with additional dedicated applications.

Some standalone window managers can be also used to replace the default window manager of a desktop environment, just like some desktop environment–oriented window managers can be used standalone too.

Prior to installing a window manager, a functional X server installation is required. See Xorg for detailed information.

See Comparison of tiling window managers and Wikipedia:Comparison of X window managers for comparison of window managers.

---

## libinput

**URL:** https://wiki.archlinux.org/title/Libinput

**Contents:**
- Installation
- Configuration
  - Via xinput on Xorg
  - Via Xorg configuration file
  - Via a udev rule
  - Graphical tools
- Tips and tricks
  - Tapping button re-mapping
  - Manual button re-mapping
  - Change touchpad sensitivity

From the libinput wiki page:

The X.Org input driver supports most regular input devices. Particularly notable is the project's goal to provide advanced support for touch (multitouch and gesture) features of touchpads and touchscreens. See the libinput documentation for more information.

If you installed either Xorg or Wayland, then Libinput should already be installed as a dependency; there are no necessary extra packages.

For Wayland, there is no libinput configuration file. The configurable options depend on the progress of your desktop environment's support for them (see #Graphical tools) or by applying desktop-agnostic udev rules (see Calibrating Touchscreen#Do it automatically via a udev rule and #Via a udev rule). To configure options that your desktop environment does not yet support (e.g. touchpad scroll speed on GNOME), libinput-config-gitAUR may be used as a work-around. Available options for that tool are documented in the libinput-config README.

For Xorg, a default configuration file for the wrapper is installed to /usr/share/X11/xorg.conf.d/40-libinput.conf. No extra configuration is necessary for it to autodetect keyboards, touchpads, trackpointers and supported touchscreens.

It will output the devices on the system and their respective features supported by libinput.

After a restart of the graphical environment, the devices should be managed by libinput with default configuration, if no other drivers are configured to take precedence.

See libinput(4) for general options to set and information about allowable values. The xinput tool is used to view or change options available for a particular device at runtime. For example:

to view all devices and determine their names and numbers. In the following, device is either the name or number identifying the device to operate with.

to change a setting. option can be either the number or the name of the option. For example, to set both options of libinput Click Method Enabled (303), either of the following can be issued:

See Xorg#Using .conf files for permanent option settings. Logitech Marble Mouse#X11 and #Tapping button re-mapping illustrate examples.

Alternative drivers for Xorg#Input devices can generally be installed in parallel. If you intend to switch driver for a device to use libinput, ensure no legacy configuration files /etc/X11/xorg.conf.d/ for other drivers take precedence.

One way to check which devices are managed by libinput is the xorg logfile. For example, the following:

is a notebook without any configuration files in /etc/X11/xorg.conf.d/, i.e. devices are auto-detected.

Of course you can elect to use an alternative driver for one device and libinput for others. A number of factors may influence which driver to use. For example, in comparison to Touchpad Synaptics the libinput driver has fewer options to customize touchpad behaviour to one's own taste, but far more programmatic logic to process multitouch events (e.g. palm detection as well). Hence, it makes sense to try the alternative, if you are experiencing problems on your hardware with one driver or the other.

Custom configuration files should be placed in /etc/X11/xorg.conf.d/ and following a widely used naming schema 30-touchpad.conf is often chosen as filename.

A basic configuration should have the following structure:

You may define as many sections as you like in a single configuration file (usually one per input device). To configure the device of your choice specify a filter by using one of the available filters from xorg.conf(5) § INPUTCLASS_SECTION, e.g.

The input device can then be configured with any of the lines of libinput(4) § CONFIGURATION_DETAILS. Common options include:

Bear in mind that some of them may only apply to certain devices and you will need to restart X for changes to take effect.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The main udev and Calibrating Touchscreen articles have more details, but to summarize:

Take note of the Device: name and Kernel path for the relevant input device. For example this might be HID 02eb:114e at path /dev/input/event0.

Create a rule for that device. E.g. to rotate all touchscreen input by 270 degrees:

Then, reload the rules and test to see if your device has registered the rule:

You should see your LIBINPUT_CALIBRATION_MATRIX listed there for the device.

Finally, either restart your machine or restart your Wayland desktop.

There are different GUI tools:

Swapping two- and three-finger tap for a touchpad is a straight forward example. Instead of the default three-finger tap for pasting, you can configure two-finger tap pasting by setting the TappingButtonMap option in your Xorg configuration file. To set 1/2/3-finger taps to left/right/middle, set TappingButtonMap to lrm, for left/middle/right set it to lmr.

Remember to remove MatchIsTouchpad "on" if your device is not a touchpad and adjust the Identifier accordingly.

For some devices, it is desirable to change the button mapping. A common example is the use of a thumb button instead of the middle button (used in X11 for pasting) on mice where the middle button is part of the mouse wheel. You can query the current button mapping via:

where device is either the device name or the device ID, as returned by xinput list. You can freely permutate the button numbers and write them back. Example:

In this example, we mapped button 6 to be the middle button and disabled the original middle button by assigning it to button 0. For more information, please read about "ButtonMapping" section in libinput(4). This may also be used for Wayland, but be aware both the device number and its button-map will be different. Hence, settings are not directly interchangeable.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Some devices occur several times under the same device name, with a different amount of buttons exposed. The following is an example for reliably changing the button mapping for a Logitech Revolution MX mouse via xinitrc:

You could also use the Xorg configuration file to do that. The trackball used in this example has a physical scroll wheel, devices without one may need to refer the configuration for Logitech Marble Mouse. The physical buttons in Kensington Slimblade Trackball layout are:

So, for the left hand user, you may use the configuration below. Although the device has no scroll up and scroll down buttons, you cannot disable them in the configuration or some application will not response to the action of the wheel.

The method of finding the correct thresholds for when libinput registers a touch as DOWN and back UP again can be found [2] in the upstream documentation.

Custom touchpad pressure values can be set via temporary local device quirks. See [3].

The LIBINPUT_IGNORE_DEVICE environment variable can be used to prevent initialization of a specific device. [6] This is best set using a udev rule:

where device_delineation delineates a specific device using udev syntax. For example, for a whole USB device you would like libinput to ignore, you could use SUBSYSTEMS=="usb", ATTRS{idVendor}=="vendor_id", ATTRS{idProduct}=="product_id" using the IDs from lsusb.

Once the file is created, udev will automatically pick up on the change (see Udev#Loading new rules); you just need to reconnect the device for the change to take place.

To disable a device such as a touchpad, first get its name with xinput list and then disable it with xinput disable name.

To make it permanent, see Autostarting.

To toggle, write a script such as [7].

While the libinput driver already contains logic to process advanced multitouch events like swipe and pinch gestures, the Desktop environment or Window manager might not have implemented actions for all of them yet.

For EWMH (see also wm-spec) compliant window managers, the libinput-gestures utility can be used meanwhile. The program reads libinput gestures (through libinput debug-events) from the touchpad and maps them to gestures according to a configuration file. Hence, it offers some flexibility within the boundaries of libinput's built-in recognition.

To use it, install the libinput-gesturesAUR package.

libinput-gestures needs access to the touchpad device. Traditionally, you can set this by adding yourself to the input group, but the more modern and safer approach is to manage access dynamically using udev, logind and acls. For this to work, create a file:

The number at the beginning of the file is important: at index 70, the device property ENV{ID_INPUT_TOUCHPAD} might be unset, and the uaccess tag needs to be added before index 73 for systemd-logind(8).

You can use the default system-wide configured swipe and pinch gestures or define your own in a personal configuration file, see the README for details.

If using touchegg, uninstall the libinput-gesturesAUR package to prevent conflicts (see [8]).

Fusuma is a multitouch gesture recognizer, written in Ruby, which can be used as an alternative to libinput-gestures.

Install the fusuma Ruby gem:

Alternatively, there is also ruby-fusumaAUR.

Other than the fusuma Ruby gem you have to install the fusuma-plugin-sendkey Ruby gem or one between the xdotool (for X) and ydotool (generic: Wayland, X11, etc). Other alternatives are listed here.

Then in ~/.config/fusuma/config.yml you have to set something like:

Same thing for ydotool.

The swipe threshold is important for not swiping back too many pages.

Notice that the configure is for three fingers swipe. Two fingers swipe is not supported [9].

Gebaar is another gesture recognizer. Unlike Fusuma, it does not support pinching (support is planned in the future though) and thresholds, but in addition to swiping left, right, up and down with 3/4 fingers, it also supports diagonal swipes, which Fusuma does not.

There is a fork of gebaar at Gebaar which could be installed through gebaar-libinput-gitAUR which supports pinch gestures and adds additional features to original gebaar. Take in mind that this version is currently under active development and introduces configuration changes which makes it incompatable to original Gebaar

For deeper integration with GNOME, there is GnomeExtendedGestures (gnome-shell-extension-extended-gestures-gitAUR). Three finger horizontal and vertical gestures can be configured to perform gnome-shell actions (such as toggling the application overview or cycling between them).

There is a nice trick to optimize scrolling with a mouse or trackball by holding a mouse button (like right or middle button, or some other if the mouse has more buttons) and moving the mouse. Very useful in case your mouse does not have the mouse wheel (often the case with the trackballs). To do that one has to set ScrollMethod to button and specify the mouse button in the ScrollButton option for the action. Here is an example for configuration to achieve that:

For some mice, especially when using on a HiDPI desktop, the wheel scrolls too slow. A patch is submitted to libinput but it has not been accepted. There is a third-party xf86-input-libinput that incorporates this patch.

This patch introduces a new property libinput Scroll Distance Scale to mice, and you can set a scaling factor like

where the device_name is the name of your mouse device, listed in xinput --list. 2.5 2.5 are the scaling factors, for x- and y-axis, respectively.

Alternatively, install libinput-multiplierAUR and restart Xorg, then enlarge y-axis scroll distance to 6 times by

Here is an example to modify the scaling factor upon focusing change

By default, libinput disables the mousepad when typing. This is conflicting for some software such as Inkscape which has keybindings that require mouse movement while a key is pressed. One way to enable the touchpad while typing is by adding the following line to the InputClass section of /etc/X11/xorg.conf.d/30-touchpad.conf:

The same effect can alternatively be accomplished using xinput. The property may be named something like libinput Disable While Typing Enabled.

First, see whether executing libinput debug-events can support you in debugging the problem, see libinput-debug-events(1) for options.

Some inputs require kernel support. The tool evemu-describe from the evemu package can be used to check:

Compare its output (for example) with a supported trackpad. i.e. a couple of ABS_ axes, a couple of ABS_MT axes and no REL_X/Y axis. For a clickpad the INPUT_PROP_BUTTONPAD property should also be set, if it is supported.

Ensure the touchpad events are being sent to the GNOME desktop by running the following command:

Additionally, GNOME may override certain behaviors, like turning off Tapping and forcing Natural Scrolling. In this case the settings must be adapted using GNOMEs gsettings command line tool or a graphical frontend of your choice. For example if you wish to enable Tapping and disable Natural Scrolling for your user, adjust the touchpad key-values like the following:

The feature is currently not implemented, see KDE bug 456383. As a workaround for Chromium-based browsers, install the SmoothScroll extension.

On some Tablet PCs (notably Lenovo Yogas), holding a keyboard key while entering the tablet mode can cause the key be stuck until the tablet mode is disabled. It is sometimes possible to fix this behavior by modifying libinput quirks files. See Issue 914.

For example, find the name of the keyboard device:

Then, create an override file:

ModelTabletModeNoSuspend=0 disables behavior that causes the bug. Consult Device quirks for information about configuration format and Match directives that select the device to configure. It is often possible to create an override file based on an existing quirks entry for your particular device. Default quirks files can be found in /usr/share/libinput/.

**Examples:**

Example 1 (unknown):
```unknown
xf86-input-
```

Example 2 (unknown):
```unknown
/usr/share/X11/xorg.conf.d/40-libinput.conf
```

Example 3 (unknown):
```unknown
# libinput list-devices
```

Example 4 (unknown):
```unknown
$ xinput list
```

---

## HDR monitor support

**URL:** https://wiki.archlinux.org/title/HDR_monitor_support

**Contents:**
- Requirements
- Configuration
  - Vulkan HDR WSI
  - Compositors
    - KDE Plasma
    - Hyprland
      - Monitor v1
      - Monitor v2
    - GNOME
    - Gamescope with Steam session

HDR support has been merged into Wayland, and some compositors have implemented it. X.org has no plans to support HDR.

For NVIDIA and mesa prior to version 25, vk-hdr-layer-kwin6-gitAUR is required for the VK_EXT_swapchain_colorspace and VK_EXT_hdr_metadata vulkan extensions [2] [3]. Without them, HDR will not work using the Vulkan API.

Enable the Vulkan Wayland HDR WSI layer by setting ENABLE_HDR_WSI=1. It is not recommended to enable this globally, instead enable it on each game and application you wish to use with HDR.

Ensure hyprland >= 0.47.0 and set the xx_color_management_v4 variable to true.

Append , bitdepth, 10, cm, hdr to the monitor's config line in your Hyprland config file.

Add a new line to the monitor's config and add

Additional settings can be found on the Hyprland wiki.

More information can be found in the Hyprland experimental docs and the Hyprland monitor docs.

Ensure mutter is >= 48.0.

Enable HDR in GNOME's display settings. The HDR toggle is per-monitor and is located next to the resolution and refresh rate setting.

Valve's Steam compositor gamescope offers experimental HDR support. Following these steps will allow you to try out Valve's Steam client running through the HDR capable gamescope.

You can now start gamescope from your login manager or a terminal using one of the following steps:

Log out and select the Steam Big Picture in your login manager and log in.

The COSMIC developers have promised HDR support in the initial stable release.

Add render_bit_depth 10 and hdr off to the outputs's config in your sway config file.

Setup a binding to toggle hdr or toggle manually i.e.: swaymsg output DP-1 hdr toggle.

HDR through Wine or Steam Proton requires DXVK (2.1+) or VKD3D-Proton (2.8+), depending on DirectX version used by the game.

To use HDR without gamescope run a build of Wine which includes the Wayland driver.

Gamescope with proper HDR requires scRGB and xx-color-management-v4 protocol support or frog-color-management-v1 protocol support in your compositor.

Because of this gamescope will not work with the vk-hdr-layer-kwin6-gitAUR layer. Ensure ENABLE_HDR_WSI is not 1.

You have many options for using gamescope depending on your desired configuration:

HDR in RetroArch is supported from version 1.10.0 with Vulkan video driver. First, select video driver Vulkan. Then, enable HDR in RetroArch video settings via Settings tab > Video > HDR > Enable HDR.

To run native games that use SDL with HDR set SDL_VIDEODRIVER=wayland.

For example for Quake II RTX:

For best image quality MPV maintainers recommend using gpu-next [9].

Other ways of enabling Wayland HDR support include using the dmabuf-wayland and drm video outputs.

firefox introduces working experimental HDR in 138.0 under the hidden preference gfx.wayland.hdr. You can enable it at about:config.

Stable HDR is still in progress [10] [11].

chromium has work-in-progress HDR support [12]. Support has been merged as of version 141.0.7370.0.

Kodi wiki maintains the list of fair use HDR video samples. These can be used to test the HDR output using video players that support HDR such has #mpv.

Pipewire attempts to stream what it sees as BGRA, which WebRTC cannot interpret, due to its current lack of capacity to interpret it. As such, a "ParamId:EnumFormat: 0:0 Invalid argument" exception is thrown and the WebRTC socket crashes for that application [13].

**Examples:**

Example 1 (unknown):
```unknown
VK_EXT_swapchain_colorspace
```

Example 2 (unknown):
```unknown
VK_EXT_hdr_metadata
```

Example 3 (unknown):
```unknown
ENABLE_HDR_WSI=1
```

Example 4 (unknown):
```unknown
xx_color_management_v4
```

---

## Session lock

**URL:** https://wiki.archlinux.org/title/Session_lock

**Contents:**
- By environment
  - Virtual console
  - Xorg
  - Wayland
- Triggering the lock
  - Shell triggers
    - Zsh
  - Xorg triggers
    - xss-lock
      - systemd events

There are numerous utilities to lock the screen of a session. But it is important to note that the utility to use is highly dependent on the environment you are in, either the virtual console, or a specific display server (Xorg or Wayland).

See List of applications/Security#Screen lockers.

This article or section is a candidate for merging with List of applications/Security#Screen lockers.

You can use vlock or physlockAUR to lock a virtual console.

There are many ways to lock the session under Xorg, so this section is likely to be incomplete. Some methods however include:

Most desktop environments come with some way to lock the session.

You can lock the session with one of the following methods:

You can lock a session using different methods:

The last point (triggering a lock from an event) is the trickiest, because you can do it in one of two ways:

To execute a command after terminal inactivity, you can use the TMOUT environment variable.

You can combine it with a trap on the ALARM signal to execute the lock. Without a trap, it will just terminate the shell.

You might want to detect if you are in a graphical environment, otherwise your GUI terminals might start disappearing without you understanding why.

xss-lock is triggered by one of two things:

The advantage of this is that you can control a lock issued manually, by inactivity, and by a suspend command at the same place.

To execute an action on one of those events:

By default, xss-lock subscribes to suspend, hibernate, lock-session, and unlock-session with appropriate actions (run locker and wait for user to unlock or kill locker).

You can prevent xss-lock from being triggered by suspend and hibernate using --ignore-sleep.

You can trigger a manual lock using loginctl lock-session, or lock all current sessions with loginctl lock-sessions.

To configure DPMS signaling timeout:

DPMS signaling can also be configured in /etc/X11/xorg.conf.d/ in the Monitor section.

Using DPMS signaling, you can set a second timer, for example to notify the user or to dim the screen. For example (from xss-lock(1)):

An example dim-screen.sh script can be found in /usr/share/doc/xss-lock.

Install the xautolockAUR package.

swayidle listens for idle activity from the Wayland compositor, as well as systemd events, and executes commands accordingly. See Sway#Idle.

hypridle Hyprland's idle daemon. See upstream for configuration.

Using loginctl lock-session, or the lock action in logind.conf(5), you can notify the system through DBUS that you want to lock. This notification can then be processed, for example by xss-lock.

In logind.conf(5), you can configure the IdleAction to lock. This will trigger a DBUS notification, that will have to be processed (for example by xsslock) to lock the session.

Note that this is for a global system (so this is not ideal for a multi user environment).

Note also that "this requires that user sessions correctly report the idle status to the system".

You can use a Sleep hook.

To enable it for a certain user, enable sleep@Username.service.

You can use the lock action using the related ACPI event.

**Examples:**

Example 1 (unknown):
```unknown
xsecurelock
```

Example 2 (unknown):
```unknown
xscreensaver-command -lock
```

Example 3 (unknown):
```unknown
$ xss-lock locker-utility
```

Example 4 (unknown):
```unknown
lock-session
```

---

## Compositor

**URL:** https://wiki.archlinux.org/title/Compositor

Compositor may refer to:

---

## picom

**URL:** https://wiki.archlinux.org/title/Picom

**Contents:**
- Installation
- Configuration
  - Disable shadows for some windows
  - Opacity
- Usage
- Multihead
- Grayscale
- Troubleshooting
  - Conky
  - dwm and dmenu

picom is a standalone compositor for Xorg, suitable for use with window managers that do not provide compositing. picom is a fork of compton, which is a fork of xcompmgr-dana, which in turn is a fork of xcompmgr.

Install the picom package.

The default configuration is available in /etc/xdg/picom.conf. For modifications, it can be copied to ~/.config/picom/picom.conf or ~/.config/picom.conf.

To use another custom configuration file with picom, use the following command:

See picom(1) § CONFIGURATION FILES for details.

The shadow-exclude option can disable shadows for windows if required. For currently disabled windows, see [1].

To disable shadows for menus add the following to wintypes in picom.conf:

The other WINDOW_TYPE values that can be used are defined in the EWMH standard: unknown, desktop, dock, toolbar, menu, utility, splash, dialog, normal, dropdown_menu, popup_menu, tooltip, notification, combo, and dnd.

To set opacity (in effect transparency) for focused and unfocused windows (for example terminal emulators), add the following to your picom.conf:

See also #Tabbed windows (shadows and transparency).

picom may be manually enabled or disabled at any time during a session, or autostarted as a background process for sessions. There are also several optional arguments that may be used to tweak the compositing effects provided. These include:

Many more options are available, including setting timings, displays to be managed, the opacity of menus, window borders, and inactive application menus. See picom(1).

To manually enable default compositing effects during a session, use the following command:

To autostart picom as a background process for a session, the -b argument can be used (may cause a display freeze):

Here is an example where additional arguments that require values to be set have been used:

If a multihead configuration is used without xinerama - meaning that X server is started with more than one screen - then picom will start on only one screen by default. It can be started on all screens by using the DISPLAY environment variable. For example, to run on X screen 0 in the background:

The above should work on all monitors. If it does not then try an older method that manually specifies each display:

It is possible to convert windows to grayscale by use of shaders.

As per picom(1), start by editing the default shader from the picom's sources.

Then start picom by including the file path to the shader. The glx backend will also, probably, be necessary.

Recent versions of picom had some problem with DRI2 acceleration and exhibited severe flickering when DRI2 is in use (picom bug, mesa bug). This has been worked around and reported to be working, but may still affect some users. DRI3 is unaffected by this particular issue.

The use of compositing effects may on occasion cause issues such as visual glitches when not configured correctly for use with other applications and programs.

To disable shadows around Conky windows, have the following in ~/.conkyrc:

In the case this solution fail with blur effect, you can try this in ~/.conkyrc:

dwm's statusbar is not detected by any of picom's functions to automatically exclude window manager elements. Neither dwm statusbar nor dmenu have a static window id. If you want to exclude it from inactive window transparency (or other), you will have to either patch a window class into the source code of each, or exclude by less precise attributes. The following example is with dwm's status on top, which allows a resolution independent of location exclusion:

Otherwise, where using a configuration file:

The override redirect property seems to be false for most windows- having this in the exclusion rule prevents other windows drawn in the upper left corner from being excluded (for example, when dwm statusbar is hidden, x0 y0 will match whatever is in dwm's master stack).

See #Disable shadows for some windows.

To disable shadows for Firefox elements add the following to shadow-exclude in picom.conf:

See [2] for more information.

Where inactive window transparency has been enabled (the -i argument when running as a command), this may provide troublesome results when also using slock. One solution is to amend the transparency to 0.2. For example, where running picom arguments as a command:

Otherwise, where using a configuration file:

Alternatively, you may try to exclude slock by its window id, or by excluding all windows with no name.

Exclude all windows with no name from picom using the following options:

Find your slock's window id by running the command:

Quickly click anywhere on the screen (before slock exits), then type your password to unlock. You should see the window id in the output:

Take the window id and exclude it from picom with:

Otherwise, where using a configuration file:

As a more simple solution, you could exclude fullscreen programs on the configuration file, for example:

Applies to fully maximized windows (in sessions without any panels) with the default picom.conf caused and resolved by the following option:

See [3] for more information.

If you observe screen tearing of video playback only in fullscreen, see #Flicker.

If you experience heavy lag when using Xft fonts in applications such as xterm or urxvt try:

or the xrender backend.

See [4] for more information.

When windows with transparency are tabbed, the underlying tabbed windows are still visible because of transparency. Each tabbed window also draws its own shadow resulting in multiple shadows.

Removing the multiple shadows issue can be done by adding the following to the already existing shadow-exclude list:

Not drawing underlying tabbed windows can be enabled by adding the following to your picom.conf:

Note that URxvt is the Xorg class name of your terminal. Change this if you use a different terminal. You can query a window's class by running the command xprop WM_CLASS and clicking the window.

See [5] for more information.

Currently, picom is incompatible with xsetroot's -solid option, a workaround is to use hsetroot to set the background color:

See [7] for more information.

Try this setting in picom.conf:

Try running picom with:

to your picom.conf file.

See [8] for more information.

Another option to reduce lag with the glx backend is to disable "allow flipping" [9] in nvidia settings (OpenGL section). This can also be done from the command line:

To load settings after reboot (see Autostarting) run

See #Lag with NVIDIA proprietary drivers and FullCompositionPipeline.

When using a systemd service to trigger slock on a suspend or hibernate action, one may find the screen unlocked for a few seconds after resume. To prevent, disable window fading:

A shadowed overlay on screen sharing and shadows of Zoom Meetings pop-up windows might be avoided by adding the following to shadow-exclude.

Blurred screen sharing is disabled by adding Zoom Meetings to blur-background-exclude with

For Microsoft Teams, the red border around the shared content is implemented with a mostly transparent window. Having blur enabled makes it impossible to work with and should be disabled as follows:

Adding --fade-in-step=1 --fade-out-step=1 --fade-delta=0 flag can disable the fade in and fade out effect when switching to a new workspace. [10]

This issue can happen after setting opacity in picom.conf. Setting use-damage = false in picom.conf would fix this issue.

**Examples:**

Example 1 (unknown):
```unknown
/etc/xdg/picom.conf
```

Example 2 (unknown):
```unknown
~/.config/picom/picom.conf
```

Example 3 (unknown):
```unknown
~/.config/picom.conf
```

Example 4 (unknown):
```unknown
$ picom --config path/to/picom.conf
```

---

## Comparison of tiling window managers

**URL:** https://wiki.archlinux.org/title/Comparison_of_tiling_window_managers

**Contents:**
- Comparison table
  - Management style
  - Layouts
  - Key bindings
- See also

This article provides an unbiased comparison of the most popular tiling window managers (as opposed to floating window managers).

The following table lists the most popular tiling window managers alongside notable features, providing readers with a quick overview.

Dynamic management emphasizes automatic management of window layouts for speed and simplicity. Manual management emphasizes manual adjustment of layout and sizing with potentially more precise control, at the cost of more time spent moving and sizing windows.

A number of common layout types appear in several tiling WMs, although the terminology varies somewhat.

Tiling window managers are usually designed to be used entirely with the keyboard or with keyboard & mouse. This is for speed (reaching for and moving a mouse is slow) and ease of use. Sensible key bindings are crucial to making workflow fast and efficient. Some default sets are better than others, but generally the keys can be rebound as desired by the user.

**Examples:**

Example 1 (unknown):
```unknown
herbstclient
```

Example 2 (unknown):
```unknown
_NET_ACTIVE_WINDOW
```

---

## PCManFM

**URL:** https://wiki.archlinux.org/title/PCManFM

**Contents:**
- Installation
- Desktop management
  - Desktop preferences
  - Creating new icons
- Daemon mode
- Autostarting
- Additional features and functionality
- Tips and tricks
  - Get thumbnails for other file types
  - Set the terminal emulator

PCManFM is an extremely fast and lightweight file manager and the standard file manager of LXDE. It uses GTK for its UI and GVFS (within GNOME's GIO library) to provide virtual filesystem functionality such as trashing files and mounting remote filesystems.

PCManFM-Qt is a port to Qt which is the standard file manager of LXQt. Despite using Qt as the UI toolkit, PCManFM-Qt retains GVFS rather than using KDE's KIO [1]. At their cores, both file managers are desktop-environment-agnostic.

Install one of the following the packages:

Optionally also install gvfs for support for trash, mounting volumes with udisks and remote filesystems and gvfs-smb for SMB/CIFS support.

PCManFM can manage the desktop, including setting a background wallpaper and showing desktop icons. To launch the desktop manager, run:

The native desktop menu of the window manager will be replaced with that provided by PCManFM. The native menu can be restored from the PCManFM menu by selecting Desktop Preferences and then enabling the Show menus provided by window managers when desktop is clicked option in the Advanced tab.

If using the native desktop menu provided by a window manager, enter the following command to set or amend desktop preferences at any time:

Consider adding this command to a keybind and/or the native desktop menu for easy access.

Files can be dragged and dropped directly onto the desktop. To create shortcuts for applications, copy their .desktop files to the ~/Desktop directory. Do not drag and drop the files there as they will be moved completely. The command is:

For example to create a desktop shortcut for lxterminal:

For those who used the XDG user directories program to create their $HOME directories, no further configuration will be required.

To run PCManFM as a background daemon (i.e. to automatically mount removable media), use:

Only one instance of PCManFM may run as a daemon at atime.

Should automount fail, see udisks.

PCManFM may be autostarted as a daemon process or to manage the desktop.

Less experienced users should be aware that a file manager alone — especially when installed in a standalone window manager such as Openbox — will not provide the features and functionality users of full desktop environments such as Xfce and KDE will be accustomed to. Review the file manager functionality article for further information.

See File manager functionality#Use PCManFM to get thumbnails for other file types.

You can configure what terminal emulator PCManFM should use for Tools > Open Current Folder in Terminal under Edit > Preferences > Advanced.

It is possible to choose the integrated archiver under Edit > Preferences > Advanced. PCManFM and PCManFM-Qt both support file-roller, xarchiver, engrampa and ark [2] [3]. PCManFM-Qt additionally supports lxqt-archiver, which is the default choice for LXQt.

PCManFM supports Desktop file specification extension (DES-EMA) which allows you to add arbitrary items to the context menu of files and directories. To add your own items, create ~/.local/share/file-manager/actions/ (if it does not already exist) and add .desktop files inside:

You can bind one or more profiles to a single action by listing their id separated by semicolons. Profiles allow you to specify which commands to execute for which file types — thus the same action can run different commands depending on the type of file selected. Besides specific MIME types (e.g. text/plain for text files), you can use the following general types:

PCManFM adds the files in ~/Templates as Create New... context menu items on startup.

The factual accuracy of this article or section is disputed.

Like some other file managers (e.g. Nautilus), PCManFM will load previews of all images in a folder. To not abuse the HDD, keep the number of images in a folder to a hundred.

If you do not see any applications to choose from in the open with dialog, then you can try removing gnome-menus and instead install lxmenu-data. Furthermore, set the following environment variables:

You can try this method: Delete all files in the $HOME/.cache/menus directory, and run PCManFM again.

PCManFM requires the environment variable XDG_MENU_PREFIX to be set. The value of the variable should match the beginning of a file present in the /etc/xdg/menus/ directory. See #"Open With" dialog window empty.

See these threads for more information: [4], and especially this post from the Linux Mint forums: [5]

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The factual accuracy of this article or section is disputed.

This article or section needs expansion.

If you are using a window manager instead of a desktop environment and you have no icons for folders and files, specify a GTK icon theme.

If you have e.g. oxygen-icons installed, edit ~/.gtkrc-2.0 or /etc/gtk-2.0/gtkrc and add the following line:

Else, use an different one (gnome, hicolor, and locolor do not work). To list all installed icon themes:

If none of them is suitable, install one. To list all installable icon packages:

A method to fix this is with Xbindkeys.

Install xbindkeys, xvkbdAUR and edit ~/.xbindkeysrc to contain the following:

Actual button codes can be obtained with package xorg-xev.

to your ~/.xinitrc to execute xbindkeys on log-in.

Make sure you have ownership and write permissions on ~/.config/pcmanfm.

Setting the wallpaper either by using the --desktop-pref parameter or editing ~/.config/pcmanfm/default/pcmanfm.config solves the problem.

The factual accuracy of this article or section is disputed.

Make sure you have the right permissions on the libfm configuration file:

You can use View > Sort Files to change the order in which PCManFM lists the files, but PCManFM will not remember that the next time you start it. To make it remember, go to Edit > Preferences and close. That will write your current sort_type and sort_by values into ~/.config/pcmanfm/LXDE/pcmanfm.conf.

Make this polkit rule in /etc/polkit-1/rules.d/00-mount-internal.rules:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

And add yourself to the storage user group.

Check first if you forgot to install the optional dependency gvfs, otherwise see the article on Session permissions.

Install a keyring application like GNOME/Keyring, KDE Wallet or lxqt_walletAUR for network shares or an SSH agent if appropriate.

**Examples:**

Example 1 (unknown):
```unknown
$ pcmanfm --desktop
```

Example 2 (unknown):
```unknown
$ pcmanfm --desktop-pref
```

Example 3 (unknown):
```unknown
$ cp /usr/share/applications/name-of-application.desktop ~/Desktop
```

Example 4 (unknown):
```unknown
$ cp /usr/share/applications/lxterminal.desktop ~/Desktop
```

---

## Xfwm

**URL:** https://wiki.archlinux.org/title/Xfwm

**Contents:**
- Installation
- Starting
- Configuration
  - Composite manager
  - Window roll-up
  - Window tiling
  - Extra settings provided by the Xfce settings manager
  - Additional themes
- Tips and tricks
  - Hide the titlebar when window is maximized

xfwm is the window manager for the Xfce environment.

Install the xfwm4 package.

Run xfwm4 with xinit.

Most xfwm settings can be accessed through xfwm4-settings, for window behavior and shortcuts, xfwm4-tweaks-settings, for advanced settings and compositing, and xfwm4-workspace-settings, for the number of workspaces and their names.

To enable or disable the Xfwm compositor and adjust its settings, go to Window Manager Tweaks:

Alternatively, it can be enabled with --compositor or using xfconf. For example:

Double clicking the titlebar, or clicking roll window up in the window menu, causes the window contents to disappear leaving only the titlebar. To disable this functionality with xfconf, run:

Xfwm can "tile" a window automatically when it is moved to an edge of the screen. It does so by resizing it to fit the top half of the screen. To enable or disable this behaviour with xfconf, run:

Alternatively, (un)check Window Manager Tweaks > Accessibility > Automatically tile windows when moving toward the screen edge.

Install the xfce4-settings package.

Install the xfwm4-themes package.

The themes installed will be shown in the xfwm4-settings window.

Go to Accessibility and check Hide title of windows when maximized.

This is fixed by installing the xfce4-settings package.

Keep in mind Xfwm assigns shortcuts to adding and removing workspaces. By default these are Alt+Delete and Alt+Insert, respectively.

If the number of workspaces resets at login, change the amount after Xfwm is started. This is ensured by the sleep command. [1]

or, from xfce4-session:

See also: Logout alters workspaces

If you experience video tearing, you could try to change the --vblank mode option of xfwm (glx, xpresent or off), try it with this command[2]:

If you use Intel graphics and you have already enabled "TearFree" option in Xorg as described in Intel graphics#Tearing, then disable Synchronize drawing to the vertical blank option.

If this does not fix the tearing, consider disabling Xfwm's compositor and using an alternative composite manager.

Xfwm may incorrectly render shadows above some dock windows (e.g.Plank). This would result in a horizontal line across the screen. A workaround is to disable Show shadows under dock windows under Settings > Window Manager Tweaks > Compositor.

**Examples:**

Example 1 (unknown):
```unknown
xfwm4-settings
```

Example 2 (unknown):
```unknown
xfwm4-tweaks-settings
```

Example 3 (unknown):
```unknown
xfwm4-workspace-settings
```

Example 4 (unknown):
```unknown
$ xfwm4-tweaks-settings
```

---

## GNOME/Files

**URL:** https://wiki.archlinux.org/title/GNOME_Files

**Contents:**
- Installation
  - Extensions
    - Applications that ship their own Nautilus extensions
    - Extensions that rely on non-free software
- Configuration
  - Change default item view
  - Sort by type
  - Remove folders from the places sidebar
  - Always show text-entry location
- Tips and tricks

Files is the default file manager for GNOME. Files attempts to provide a streamlined method to manage both files and applications.

Install the nautilus package. This package is part of the gnome group. See also File manager functionality#Additional features.

Some programs can add extra functionality to Files. Here are a few examples:

The following applications install their own extensions by default, thus providing integration with Nautilus:

Some extensions for GNOME Files, although free, might rely on non-free software. The following list provides a few examples:

Files is simple to configure graphically, but not all options are available in the preferences menu. More options are available with dconf-editor under org.gnome.nautilus.

You can change the default view for the items by setting the default-folder-viewer variable, e.g. for the list view:

To sort files in all folders by type:

The displayed folders are specified in ~/.config/user-dirs.dirs and can be altered with any editor. An execution of xdg-user-dirs-update will change them again, thus it may be advisable to set the file permissions to read-only.

The standard Files toolbar shows a button bar interface for path navigation. To enter path locations using the keyboard, you must expose the location text-entry field. This is done by pressing Ctrl+l

To make the location text-entry field always present, use gsettings as shown below:

See File manager functionality#Thumbnail previews.

Sometimes video thumbnails are not shown. To solve it (as mentioned in No video thumbnails on nautilus), you must install ffmpegthumbnailer, gst-libav, gst-plugins-ugly, and remove the content of ~/.cache/thumbnails/fail/.

To get this option one has to create a ~/Templates/ folder in your home folder and place an empty file inside the folder through your favorite Terminal by touch ~/Templates/new or by using any other file manager. Then just restart Files.

On non-English installations, the templates directory might have another name. One can find the actual directory with xdg-user-dir TEMPLATES.

The templates directory can be configured in the ~/.config/user-dirs.dirs file:

Like most other file managers GNOME Files hides files with names starting with a dot by default.

GNOME Files additionally hides files when their names are listed in a .hidden file in the same directory (one filename per line). See nautilus-hideAUR for an extension that facilitates adding/removing entries from such .hidden files.

If you are using tilixAUR terminal you can easily add "Open in Tilix" option to the context menu of GNOME Files by installing its optional dependency nautilus-python.

To add a folder to your bookmarks, simply press Ctrl+d when you have the folder opened in Nautilus. Note that the list of bookmarks is shared with other GNOME-based graphical file managers (e.g. Nemo), so a folder added or removed from one will affect the bookmarks seen in the other.

Scripts placed in ~/.local/share/nautilus/scripts can be run from the right click context menu of a file.

The context menu can also be organized into subfolders, e.g. ~/.local/share/nautilus/scripts/images and ~/.local/share/nautilus/scripts/music.

Scripts have access to the following environment variables:

Some example scripts:

Keybinds to execute scripts can be assigned in the ~/.config/nautilus/scripts-accels file:

By installing gvfs and the various gvfs-* packages, you can add support for various network based filesystems (e.g. SMB, NFS, WebDAV, Nextcloud) and some mobile phones (Android MTP, Apple AFC).

For more information and other supported virtual filesystems, see File manager functionality.

This can be caused by the file association for directories being reset. Installing anjutaAUR or visual-studio-code-binAUR tend to do this.

To solve this, open Files, right-click on a folder, and choose Open With Other Application > Files > Select. This will set the association for directories back to Files.

If this does not solve the issue, see File manager functionality#Directories are not opened in the file manager.

In case you have kdeconnect installed in your system, the problem might be caused by its file sharing module. Deactivate file sharing, and it should stop happening.

You may be missing one or more of the following packages:

Install them and you should be good to go.

To activate the WSD support in GNOME/Files install gvfs-wsdd to make GNOME/Files discover newer Windows machines in the network view. There is no further tweaking necessary.

Install gvfs-dnssd and restart Nautilus.

'Run as a Program' context menu option is hardcoded for gnome-console and if you use different terminal and the default gnome terminal is not present, the context menu option won't do anything.

Since it's just executing /usr/bin/kgx (executable for gnome-console) directly, you can create script (or symlink if your terminal has the same arguments) named kgx and place it inside /usr/bin/ to use your terminal for 'Run as a Program' context menu option.

Example for using wezterm-gitAUR as a terminal for 'Run as a Program'

It is possible to open a directory in a terminal emulator with "Open with..." right click menu entry. But the XDG desktop entry of the terminal is expected to contain appropriate Exec and MimeType values.

Following example shows how to create additional desktop entry for Alacritty terminal emulator which will be recognized by "Open with...".

Run update-desktop-database ~/.local/share/applications/ to apply changes.

If a terminal app became default file manager, it can be fixed with command xdg-mime default org.gnome.Nautilus.desktop inode/directory.

Check flags and desktop entry file of your preferred terminal application to adopt the example.

**Examples:**

Example 1 (unknown):
```unknown
audio/x-mp3
```

Example 2 (unknown):
```unknown
audio/x-flac
```

Example 3 (unknown):
```unknown
audio/x-vorbis+ogg
```

Example 4 (unknown):
```unknown
audio/x-speex+ogg
```

---

## KDE

**URL:** https://wiki.archlinux.org/title/Plasma

**Contents:**
- Installation
  - Plasma
  - Plasma Mobile
  - KDE applications
  - Unstable releases
- Starting Plasma
  - Using a display manager
  - From the console
- Configuration
  - Personalization

KDE is a software project currently comprising a desktop environment known as Plasma, a collection of libraries and frameworks (KDE Frameworks) and several applications (KDE Applications) as well.

KDE upstream has a well maintained UserBase wiki. Detailed information about most KDE applications can be found there.

Install the plasma-meta meta-package or the plasma group. For differences between plasma-meta and plasma reference Package group. Alternatively, for a more minimal Plasma installation, install the plasma-desktop package. Upstream KDE has package and setup recommendations to get a fully-featured Plasma session.

If you are an NVIDIA user with the proprietary nvidia driver and wish to use the Wayland session, enable the DRM kernel mode setting.

Install plasma-mobileAUR.

To install the full set of KDE Applications, install the kde-applications-meta meta-package or the kde-applications group. If you only want KDE applications for a certain category, like gaming or education, install the relevant dependency of kde-applications-meta. Note that installing applications alone will not install any version of Plasma.

See Official repositories#kde-unstable for beta releases.

Starting from Plasma 6.4, the Wayland session has matured enough to become the default and preferred one: the X11 session is only available separately with the plasma-x11-session package[1]. The Xorg session is still supported, but will be removed in Plasma 7. See Wayland Known Significant Issues and X11 Known Significant Issues for more information.

Plasma can be started either using a display manager, or from the console.

Most settings for KDE applications are stored in ~/.config/. However, configuring KDE is primarily done through the System Settings application. It can be started from a terminal by executing systemsettings.

There are different types of KDE themes, varying by scope of what they modify:

For easy system-wide installation and updating, some themes are available in both the official repositories and the AUR.

Global themes can also be installed through System Settings > Colors & Themes > Global Theme > Get New....

The recommended theme for a pleasant appearance in GTK applications is breeze-gtk, a GTK theme designed to mimic the appearance of Plasma's Breeze theme. Install kde-gtk-config (part of the plasma group), relogin and select Breeze as the GTK theme in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style....

This article or section is out of date.

In some themes, tooltips in GTK applications have white text on white backgrounds making it difficult to read. To change the colors in GTK2 applications, find the section for tooltips in the .gtkrc-2.0 file and change it. For GTK3 application two files need to be changed, gtk.css and settings.ini.

Some GTK2 programs like vuescan-binAUR still look hardly usable due to invisible checkboxes with the Breeze or Adwaita skin in a Plasma session. To workaround this, install and select e.g. the Numix-Frost-Light skin of the numix-frost-themesAUR under System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style... > GTK theme. Numix-Frost-Light looks similar to Breeze.

Plasma and SDDM will both use images found at /var/lib/AccountsService/icons/ as users' avatars. To configure with a graphical interface, you can use System Settings > Users. The file corresponding to your username can be removed to restore the default avatar.

Plasmoids are widgets for Plasma desktop shell designed to enhance the functionality of desktop, they can be found on the AUR.

Plasmoid scripts can also be installed by right-clicking onto a panel or the desktop and choosing Enter Edit Mode > Add Widgets... > Get New Widgets... > Download New Plasma Widgets. This will present a front-end for https://store.kde.org/ that allows you to install, uninstall, or update third-party Plasmoid scripts with just one click.

Install plasma-pa or kmix (start Kmix from the Application Launcher). plasma-pa is now installed by default with plasma, no further configuration needed.

As the Plasma panel is on top of other windows, its shadow is drawn over them. [5] To disable this behaviour without impacting other shadows, install xorg-xprop and run:

then select the panel with the plus-sized cursor. [6] For automation, install xorg-xwininfo and create the following script:

Make the script executable.

The factual accuracy of this article or section is disputed.

The script can be run on login with Add Login Script in Autostart:

See HiDPI#KDE Plasma.

The plasma-phone-settings repository contains several recommended settings which can be applied globally (/etc/xdg) and/or per user (~/.config).

/etc/xdg/kscreenlockerrc (or ~/.config/kscreenlockerrc) locks the screen immediately after login. [7] This is useful in combination with SDDM#Autologin.

To use a virtual keyboard in the Wayland session, install maliit-keyboard and enable it in System Settings > Keyboard > Virtual Keyboard.

If your device has a hardware keyboard, but you want to use the virtual keyboard, add the KWIN_IM_SHOW_ALWAYS=1 environment variable to your Wayland session.

To use a virtual keyboard in the X11 session, choose an appropriate one from List of applications/Utilities#On-screen keyboards and run it manually.

Window decorations can be found in the AUR.

They can be changed in System Settings > Colors & Themes > Window Decorations, there you can also directly download and install more themes with one click.

Icon themes can be installed and changed on System Settings > Colors & Themes > Icons.

The Plasma Netbook shell has been dropped from Plasma 5, see the following KDE forum post. However, you can achieve something similar by editing the file ~/.config/kwinrc adding BorderlessMaximizedWindows=true in the [Windows] section.

To allow thumbnail generation for media or document files on the desktop and in Dolphin, install kdegraphics-thumbnailers and ffmpegthumbs.

Then enable the thumbnail categories for the desktop via right click on the desktop background > Configure Desktop and Wallpaper... > Icons > Configure Preview Plugins....

In Dolphin, navigate to Configure > Configure Dolphin... > Interface > Previews.

Plasma provides a Redshift-like feature (working on both Xorg and Wayland) called Night Light. It makes the colors on the screen warmer to reduce eye strain at the time of your choosing. It can be enabled in System Settings > Colors & Themes > Night Light.

You can also configure printers in System Settings > Printers. To use this method, you must first install the following packages print-manager, cups, system-config-printer. See CUPS#Configuration.

The Dolphin share functionality requires the package kdenetwork-filesharing and usershares, which the stock smb.conf does not have enabled. Instructions to add them are in Samba#Enable Usershares, after which sharing in Dolphin should work out of the box after restarting Samba.

Accessing Windows shares from Dolphin works out of the box. Use the path smb://servername/share to browse the files.

Unlike GTK file browsers which utilize GVfs also for the launched program, opening files from Samba shares in Dolphin via KIO makes Plasma copy the whole file to the local system first with most programs (VLC is an exception). To workaround this, you can use a GTK based file browser like thunar with gvfs and gvfs-smb (and gnome-keyring for saving login credentials) to access SMB shares in a more able way.

Another possibility is to mount a Samba share via cifs-utils to make it look to Plasma like if the SMB share was just a normal local folder and thus can be accessed normally. See Samba#Manual mounting and Samba#Automatic mounting.

A GUI solution is available with samba-mounter-gitAUR, which offers basically the same functionality via an easy to use option located at System Settings > Network Drivers. However, it might break with new KDE Plasma versions.

KDE Desktop Activities are special workspaces where you can select specific settings for each activity that apply only when you are using said activity.

Install powerdevil for an integrated Plasma power managing service. This service offers additional power saving features, monitor brightness control (if supported) and battery reporting including peripheral devices.

The factual accuracy of this article or section is disputed.

Plasma can autostart applications and run scripts on startup and shutdown. To autostart an application, navigate to System Settings > Autostart and add the program or shell script of your choice. For applications, a .desktop file will be created, for login scripts, a .desktop file launching the script will be created.

See official documentation.

Phonon is being widely used within KDE, for both audio (e.g., the System notifications or KDE audio applications) and video (e.g., the Dolphin video thumbnails). It can use the following backends:

KDE recommends only the VLC backend, as the GStreamer backend is unmaintained.

Plasma stores personalized desktop settings as configuration files in the XDG_CONFIG_HOME folder. Use the detail of configuration files to select and choose a method of backup and restore.

Plasma uses a systemd user instance to launch and manage all the Plasma services. This is the default startup method since Plasma 5.25, but can be disabled to use boot scripts instead with the following command (however this may stop working in a future release):

More details about the implementation can be read in Edmundson's blog: Plasma and the systemd startup.

KDE applications use sonnet for spell checking. See its optional dependencies for the supported spell checkers.

Configure it in System Settings > Spell Check.

See https://community.kde.org/Plasma/Wayland/Nvidia.

The KDE project provides a suite of applications that integrate with the Plasma desktop. See the kde-applications group for a full listing of the available applications. Also see Category:KDE for related KDE application pages.

Aside from the programs provided in KDE Applications, there are many other applications available that can complement the Plasma desktop. Some of these are discussed below.

Navigate to the submenu System Settings > Keyboard > Advanced (tab) > Key sequence to kill the X server and ensure that the checkbox is ticked.

KCM stands for KConfig Module. KCMs can help you configure your system by providing interfaces in System Settings, or through the command line with kcmshell6.

More KCMs can be found at linux-apps.com.

KDE implements desktop search with a software called Baloo, a file indexing and searching solution.

The following web browsers can integrate with Plasma:

KDE offers its own stack for personal information management (PIM). This includes emails, contacts, calendar, etc. To install all the PIM packages, you could use the kde-pim package group or the kde-pim-meta meta package.

Akonadi is a system meant to act as a local cache for PIM data, regardless of its origin, which can be then used by other applications. This includes the user's emails, contacts, calendars, events, journals, alarms, notes, and so on. Akonadi does not store any data by itself: the storage format depends on the nature of the data (for example, contacts may be stored in vCard format).

Install akonadi. For additional addons, install kdepim-addons.

By default Akonadi will use /usr/bin/mysqld (MariaDB by default, see MySQL for alternative providers) to run a managed MySQL instance with the database stored in ~/.local/share/akonadi/db_data/.

Akonadi supports using the system-wide MySQL for its database.[10]

This article or section needs expansion.

Akonadi supports either using the existing system-wide PostgreSQL instance, i.e. postgresql.service, or running a PostgreSQL instance with user privileges and the database in ~/.local/share/akonadi/db_data/.

Install postgresql and postgresql-old-upgrade.

Edit the Akonadi configuration file so that it has the following contents:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

This requires an already configured and running PostgreSQL.

Create a PostgreSQL user account for your user:

Create a database for Akonadi:

Edit the Akonadi configuration file to match the configuration below:

Start Akonadi with akonadictl start, and check its status: akonadictl status.

To use SQLite, edit the Akonadi configuration file to match the configuration below:

Users who want to disable Akonadi would need to not start any KDE applications that rely on it. See this section in the KDE userbase for more information.

KDE Connect provides several features to connect your Android or iOS phone with your Linux desktop:

You will need to install KDE Connect both on your computer and on your phone. For PC, install kdeconnect package. For Android, install KDE Connect from Google Play or from F-Droid. If you want to browse your phone's filesystem, you need to install sshfs as well and configure filesystem exposes in your Android app. For iOS, install KDE Connect from the App Store. Not all features from the Android version are available on the iOS version.

To use remote input functionality on a Plasma Wayland session, the xdg-desktop-portal package is required.

It is possible to use KDE Connect even if you do not use the Plasma desktop. For GNOME users, better integration can be achieved by installing gnome-shell-extension-gsconnectAUR instead of kdeconnect. To start the KDE Connect daemon manually, execute /usr/bin/kdeconnectd.

If you use a firewall, you need to open UDP and TCP ports 1714 through 1764.

Sometimes, KDE Connect will not detect a phone. You can restart the services by running killall kdeconnectd and then opening kdeconnect in system settings or running kdeconnect-cli --refresh followed by kdeconnect-cli -l. You can also use Pair new device > Add devices by IP on KDE Connect for Android.

It is possible to use a window manager other than KWin with Plasma. This allows you to combine the functionality of the KDE desktop with the utility of a tiling window manager, which may be more fleshed out than KWin tiling scripts.

The component chooser settings in Plasma no longer allows changing the window manager, but you are still able to swap KWin via other methods.

Since KDE 5.25, Plasma's systemd based startup is enabled by default.

To replace KWin in this startup, you must first mask the plasma-kwin_x11.service for the current user to prevent it from starting.

Then, create a new systemd user unit to start your preferred WM [11]:

To use it, do (as user units) a daemon-reload, make sure you have masked plasma-kwin_x11.service then enable the newly created plasma-custom-wm.service.

Plasma's script-based boot is used by disabling #systemd startup. If you have done so, you can change the window manager by setting the KDEWM environment variable before Plasma is invoked.

This article or section is a candidate for merging with Environment variables#Globally.

If you have root access, you can also add an XSession that will be available to all users as an option on the login screen.

First, create a script with execution permissions as follows:

Replace /usr/bin/i3 to the path to your preferred WM. Ensure the path is correctly set. If KDE is unable to start the window manager, the session will fail and the user will be returned to the login screen.

Then, to add an XSession, add a file in /usr/share/xsessions/ with the following content:

The openbox package provides a session for using KDE with Openbox. To make use of this session, disable #systemd startup and select KDE/Openbox from the display manager menu.

For those starting the session manually, add the following line to your xinit configuration:

A list of KWin extensions that can be used to make KDE behave more like a tiling window manager.

To enable display resolution management and multiple monitors in Plasma, install kscreen. This provides additional options to System Settings > Display & Monitor.

On X11, ICC profiles are handled by colord. To configure them in Plasma, install colord-kde. This provides additional options in System Settings > Color Management. ICC profiles can be imported using Import Profile.

For Wayland sessions, color management is handled by the compositor, i.e. KWin for Plasma. In this case, no additional package is required. The color profile can be configured per monitor in System Settings > Display & Monitor > Color Profile.

HDR support is experimental and only works in a Wayland session. System Settings > Display & Monitor > High Dynamic Range > Enable HDR.

For more information on displaying HDR content see HDR monitor support. Development details about HDR in Plasma can be found on Xaver Hugl's blog post.

When enabling HDR mode in KDE Plasma, SDR content can appear extremely dark, sometimes making the screen nearly unreadable. To address this, KDE provides two key sliders in display settings: Maximum SDR Brightness, which adjusts the brightness mapping for SDR content in HDR mode, and Brightness which controls the overall display backlight or luminance

To disable this feature, you currently have to edit the kwinrc config file and set the Meta key under ModifierOnlyShortcuts to an empty string:

Alternatively, you can also run the following command:

With the Plasma Browser integration installed, KDE will show bookmarks in the application launcher.

To disable this feature, go to System Settings > Search > Plasma Search and uncheck Bookmarks.

IBus is an input method framework and can be integrated into KDE. See IBus#Integration for details.

Using IBus may be required when using KDE on Wayland to offer accented characters and dead keys support [12].

See NetworkManager#Sharing internet connection over Wi-Fi.

If you have System Settings > Session > Desktop Session > Session Restore > On login, launch apps that were open: On last logout (default) selected, ksmserver (KDE's session manager) will automatically save/load all open applications to/from ~/.config/ksmserverrc on logout/login.

If you have set up local mail delivery with a mail server that uses the Maildir format, you may want to receive this mail in KMail. To do so, you can re-use KMail's default receiving account "Local Folders" that stores mail in ~/.local/share/local-mail/.

Symlink the ~/Maildir directory (where Maildir format mail is commonly delivered) to the Local Folders' inbox:

Alternatively, add a new receiving account with the type Maildir and set ~/Maildir as its directory.

Edit config/main.xml files in the /usr/share/plasma. For example, to configure the Application Launcher for all users, edit /usr/share/plasma/plasmoids/org.kde.plasma.kickoff/contents/config/main.xml. To prevent the files from being overwritten with package updates, add the files to Pacman's NoUpgrade

This article or section is a candidate for merging with Power management.

Properly disable the hibernate feature and hide it from the menu with a Polkit policy rule.

Alternatively, add the following lines to a file in /etc/systemd/sleep.conf.d/:

Kwin has the ability to specify rules for specific windows/applications. For example, you can force enable the window titlebar even if the application developer decided that there should not be one. You can set such rules as specific starting position, size, minimize state, keeping above/below others and so on.

To create a rule you can press Alt+F3 when the window of interest is in focus. Then, in More Actions > Configure special application/window settings, you can set the desired property. A list of created rules is available from System Settings > Window Management > Window Rules.

By default KDE mount manager (kio-fuse) will mount network shares to ${XDG_RUNTIME_DIR}/kio-fuse-6-char-random-string.

Create directory, e.g. mnt_kio in your home directory:

Override default kio-fuse.service using a drop-in file:

Now if you mount your network shares via dbus or by openning some file from remote share in Dolphin:

They will be mounted to ~/mnt_kio.

To have the menu bar integrated with the title bar, install material-kwin-decoration-gitAUR from the AUR, then in System Settings > Window Decorations, select 'Material' and add the Application Menu button to the title bar (preferably as second from the left). Works only on X11 session.

Xdg-desktop-portal-kde has support for remote input from a remote desktop session, a virtual KVM switch, kde-connect, emulated devices like a controller using steam-input, etc. This authorization is lost after the application or the desktop-portal is restarted, which causes the "Remote control requested" window pop up every time and makes unattended access impossible.

As of plasma version 6.3, a permission system was implemented, which allows to pre-authorize applications. Currently, the permission api is only available through the flatpak cli, although applications do not need to run as a flatpak to be able to get pre-authorized.

As per the upstream docs and flatpak-permission-set man pages, you need to figure out if the application you want to authorize sets an application ID or not. If started through a runner like KRunner, it gets set by plasma and is usually the filename of the .desktop-file under /usr/share/applications.

For example, to pre-authorize a virtual KVM switch like lan-mouse, you would do:

If you start it as a daemon in a systemd user-unit, you should use the name of that unit instead:

If you application does not set an ID, you can leave that field empty:

Wayland is used by default for KDE 6 applications, and the KDE applications fail to work under GNOME Wayland (and potentially other DEs/WMs) in this scenario. This can be fixed by setting the QT_QPA_PLATFORM=xcb environment variable.

This is a workaround for KDE bugs and not a problem with Wayland itself.

After the last upgrade to KDE 6 you may notice issues with all of the KDE icons not displaying. Newly created accounts showed them just fine.

The issue for this is that the theme got lost while upgrading and had to be reassigned manually. For this go to System Settings > Colors & Themes > Icons and select the theme you would like to use for the icons again.

This article or section is out of date.

Latest update might cause incompatible HiDPI scaling that made some interfaces becomes too big for your screen, some icons are missing or can not be displayed, and missing panels or widgets.

Try to remove qt5ct and kvantum related package, then apply default global Plasma theme. If the problem persists, try clearing all your KDE configuration and reinstalling plasma to overwrite the configuration. Be sure to check HiDPI scaling in KDE system settings as well.

Try to force font DPI to 96 in System Settings > Text & Fonts > Fonts.

If that does not work, try setting the DPI directly in your Xorg configuration as documented in Xorg#Setting DPI manually.

Many problems in KDE are related to its configuration.

Plasma problems are usually caused by unstable Plasma widgets (colloquially called plasmoids) or Plasma themes. First, find which was the last widget or theme you had installed and disable or uninstall it.

So, if your desktop suddenly exhibits "locking up", this is likely caused by a faulty installed widget. If you cannot remember which widget you installed before the problem began (sometimes it can be an irregular problem), try to track it down by removing each widget until the problem ceases. Then you can uninstall the widget, and file a bug report on the KDE bug tracker only if it is an official widget. If it is not, it is recommended to find the entry on the KDE Store and inform the developer of that widget about the problem (detailing steps to reproduce, etc.).

If you cannot find the problem, but you do not want all the settings to be lost, navigate to ~/.config/ and run the following command:

This command will rename all Plasma related configuration files to *.bak (e.g. plasmarc.bak) of your user and when you will relogin into Plasma, you will have the default settings back. To undo that action, remove the .bak file extension. If you already have *.bak files, rename, move, or delete them first. It is highly recommended that you create regular backups anyway. See Synchronization and backup programs for a list of possible solutions.

The problem may be caused by old cache. Sometimes, after an upgrade, the old cache might introduce strange, hard to debug behaviour such as unkillable shells, hangs when changing various settings, Ark being unable to extract archives or Amarok not recognizing any of your music. This solution can also resolve problems with KDE and Qt applications looking bad after an update.

Rebuild the cache using the following commands:

Optionally, empty the ~/.cache/ folder contents, however, this will also clear the cache of other applications:

Sometimes, empty the ~/.cache/ folder does not work, for example, if you encountered the following error:

It might be something related to outdated configuration files. In the above case, moving ~/.config/menus/ folder away may fix the issue. In other cases, try moving each file out of ~/.config/menus/ folder could be a good way to check what triggers the error.

Plasma desktop may use different settings than you set at KDE System Settings panel, or in locale.conf (per Locale#Variables). First thing to do is log out and log in after removing ~/.config/plasma-localerc, if this does not fix the issue, try to edit the file manually. For example, to set LANG variable to es_ES.UTF-8 and the LC_MESSAGES variable to en_US.UTF-8:

Make sure that QT_QPA_PLATFORMTHEME environment variable is unset, the command printenv QT_QPA_PLATFORMTHEME should show empty output. Otherwise if you had an environment set (most likely qt5ct or qt6ct) the variable will force qt5ct/qt6ct settings upon Qt applications, the command export QT_QPA_PLATFORMTHEME= should unset the environment.

An easier (and more reliable) solution can be to uninstall completely qt5ct and qt6ct.

Hiding certain items in the System Tray settings (e.g. Audio Volume, Media Player or Notifications) also disables related features. Hiding the Audio Volume disables volume control keys, Media Player disables multimedia keys (rewind, stop, pause) and hiding Notifications disables showing notifications.

The Login Screen KCM reads your cursor settings from ~/.config/kcminputrc, without this file no settings are synced. The easiest way to generate this file is to change your cursor theme in System Settings > Colors & Themes > Cursors, then change it back to your preferred cursor theme.

A crash or hardware change can modify the screen numbers, even on a single monitor setup. The panels/widgets can be missing after such an event, this can be fixed in the ~/.config/plasma-org.kde.plasma.desktop-appletsrc file by changing the lastScreen values.

Make sure you have the proper driver for your GPU installed. See Xorg#Driver installation for more information. If you have an older card, it might help to #Disable desktop effects manually or automatically for defined applications or #Disable compositing.

Hybrid graphics is a power management strategy commonly used in laptops that keeps the dedicated graphics processor (dGPU) inactive when not needed, defaulting to the integrated graphics processor (iGPU) for basic desktop rendering to conserve battery life.

While this approach saves power, it can result in suboptimal desktop performance, including low frame rates in animations and potential graphical artifacts, even on systems with capable dGPUs.

Forcing KDE Plasma to utilize the discrete GPU can significantly improve desktop responsiveness and visual quality.

For systems using open-source graphics drivers (Intel + AMDGPU, Intel + Nouveau), you can globally set the DRI_PRIME environment variable to specify the dGPU:

The index value (0 or 1) depends on your system configuration. Verify which index corresponds to your dGPU by running:

For direct control over KWin's GPU selection, create a startup script that sets the DRM device priority:

To identify your DRM cards and their corresponding GPUs:

List the dGPU first in the KWIN_DRM_DEVICES variable to prioritize it for rendering.

This command prints out a summary of the current state of KWin including used options, used compositing backend and relevant OpenGL driver capabilities. See more on Martin's blog.

Plasma has desktop effects enabled by default and e.g. not every game will disable them automatically. You can disable desktop effects in System Settings > Window Management > Desktop Effects and you can toggle desktop effects with Alt+Shift+F12.

Additionally, you can create custom KWin rules to automatically disable/enable compositing when a certain application/window starts under System Settings > Window Management > Window Rules.

If you use a transparent background without enabling the compositor, you will get the message:

In System Settings > Display & Monitor > Compositor, check Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Enable on startup and restart Plasma.

In System Settings > Display & Monitor > Compositor, uncheck Compositing: Allow applications to block compositing. This may harm performance.

Setting the environment variable QSG_USE_SIMPLE_ANIMATION_DRIVER for KWIN reduces jerking in some Quick Scene Graphics based effects. For this purpose, it is sufficient to create a drop-in for the service running KWIN:

(in the case of Wayland session, use plasma-kwin_wayland.service.d as directory name)

Then restart the session.

Another try is to set QSG_NO_VSYNC instead of QSG_USE_SIMPLE_ANIMATION_DRIVER.

Create the directory ~/.local/share/icons/default/ (alternatively, ~/.icons/default), then, inside it, create a file named index.theme, then add to it the following contents:

If applicable, replace breeze_cursors with the cursor theme you use (cursor themes can be found in /usr/share/icons/, e.g. Breeze_Light).

On Wayland, it is necessary for xdg-desktop-portal-gtk to be installed for GTK/GNOME applications to correctly apply cursor themes.

Firefox and Thunderbird running under Wayland will refer to GSettings to determine which cursor to display.

To sync KDE settings to GTK applications, install kde-gtk-config.

If you do not want to install an extra package, you can set the cursor theme manually:

Try installing the appropriate 2D acceleration driver for your system and window manager.

Your local configuration settings for kscreen can override those set in xorg.conf. Look for kscreen configuration files in ~/.local/share/kscreen/ and check if mode is being set to a resolution that is not supported by your monitor.

In order to add icons to tray, applications often make use of the library appindicator. If your icons are blurry, check which version of libappindicator you have installed. If you only have libappindicator-gtk2AUR installed, you can install libappindicator as an attempt to get clear icons.

When running Plasma in a VMware, VirtualBox or QEMU virtual machine, kscreen may not allow changing the guest's screen resolution to a resolution higher than 800×600.

The workaround is to set the PreferredMode option in xorg.conf.d(5). Alternatively try using a different graphics adapter in the VM, e.g. VBoxSVGA instead of VMSVGA for VirtualBox and Virtio instead of QXL for QEMU. See KDE Bug 407058 for details.

Check whether your user directories (Documents, Downloads, etc.) are read-only.

In System Settings > Display & Monitor > Compositor, change Keep window thumbnails from Only from Shown windows to Never. If you are using Intel graphics, ensure that xf86-video-intel is not installed.

See XDG Desktop Portal#Poor font rendering in GTK applications on KDE Plasma.

You may observe that windows of some applications do not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk.

See Nouveau#Random lockups with kernel error messages.

If there is no sound after suspending and KMix does not show audio devices which should be there, restarting plasmashell and pulseaudio may help:

Some applications may also need to be restarted in order for sound to play from them again.

This can be solved by installing the GStreamer libav plugin (package gst-libav). If you still encounter problems, you can try changing the Phonon backend used by installing another such as phonon-qt6-vlc.

Then, make sure the backend is preferred via phononsettings.

Check if you have plasma-pa installed.

If journalctl -p4 -t pulseaudio contains entries saying Failed to create sink input: sink is suspended, try commenting the following line in /etc/pulse/default.pa:

If the issue persists, plasma-meta or plasma may have installed pulseaudio alongside wireplumber. To fix the issue, replace pulseaudio with pipewire-pulse. If pulseaudio is preferred, replace wireplumber with pipewire-media-session. See PipeWire#PulseAudio clients and this forum thread for more details.

If your system is able to suspend or hibernate using systemd but do not have these options shown in KDE, make sure powerdevil is installed.

Make sure you installed powerdevil and power-profiles-daemon. Run powerprofilesctl and check the driver. If it is intel_pstate or amd_pstate, you are done, otherwise see CPU frequency scaling#Scaling drivers for more information on enabling them.

See [13] for details.

If you want a backup, copy the following configuration directories:

For some IMAP accounts KMail will show the inbox as a top-level container (so it will not be possible to read messages there) with all other folders of this account inside.[14]. To solve this problem simply disable the server-side subscriptions in the KMail account settings.

While setting up EWS account in KMail, you may keep getting errors about failed authorization even for valid and fully working credentials. This is likely caused by broken communication between KWallet and KMail. To workaround the issue set a passsword via qdbus:

See Qt#Disable/Change Qt journal logging behaviour.

See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

It is not recommended to turn off the KWallet password saving system in the user settings as it is required to save encrypted credentials like Wi-Fi passphrases for each user. Persistently occuring KWallet dialogs can be the consequence of turning it off.

In case you find the dialogs to unlock the wallet annoying when applications want to access it, you can let the display managers SDDM and LightDM unlock the wallet at login automatically, see KDE Wallet#Unlock KDE Wallet automatically on login. The first wallet needs to be generated by KWallet (and not user-generated) in order to be usable for system program credentials.

In case you want the wallet credentials not to be opened in memory for every application, you can restrict applications from accessing it with kwalletmanager in the KWallet settings.

If you do not care for credential encryption at all, you can simply leave the password forms blank when KWallet asks for the password while creating a wallet. In this case, applications can access passwords without having to unlock the wallet first.

This can be solved by installing packagekit-qt6.

Discover sometimes will not remove its PackageKit alpm lock. To release it, remove /var/lib/PackageKit/alpm/db.lck. Use "Refresh" in Discover and updates should appear (if there are any updates pending).

As described in KDE Bug 347772 NVIDIA OpenGL drivers and QML may not play well together with Qt 5. This may lead kscreenlocker_greet to high CPU usage after unlocking the session. To work around this issue, set the QSG_RENDERER_LOOP environment variable to basic.

Then kill previous instances of the greeter with killall kscreenlocker_greet.

If your home directory is on a ZFS pool, create a ~/.config/akonadi/mysql-local.conf file with the following contents:

See MariaDB#OS error 22 when running on ZFS.

This is caused by the problematic way of GTK3 handling mouse scroll events. A workaround for this is to set environment variable GDK_CORE_DEVICE_EVENTS=1. However, this workaround also breaks touchpad smooth scrolling and touchscreen scrolling.

When using TeamViewer, it may behave slowly if you use smooth animations (such as windows minimizing). See #Disable compositing as a workaround.

Kmail may become unresponsive, show a black messageviewer or similar, often after having been minimized and restored. A workaround may be to set environment variable QT_QPA_PLATFORM="xcb;wayland". See KDE Bug 397825.

If you previously locked your widgets, you will probably find yourself unable to unlock them again. You just have to run this command to do so:

The new Customize Layout does not require to lock them back up but if want to do that:

Check file associations regarding HTML, PHP, etc... and change it to a browser. KIO's cache files are located in $HOME/.cache/kioexec. See also xdg-utils#URL scheme handlers.

In the System Settings application, KDE offers a setting to automatically lock the screen after waking up from sleep. Upon resuming, some users report that the screen is briefly showed before locking. To prevent this behavior and have KDE lock the screen before suspending, create a hook in systemd(1) by creating the following file as the root user:

The use of sleep is necessary in order for the loginctl lock-session command to complete before the device is suspended. Using a lower timeout may not allow for this to complete.

After creating the file, make it executable.

Finally, make sure that the KDE setting is enabled by going to System Settings > Screen Locking and checking the Lock screen automatically: After waking from sleep checkbox.

Some X11 software like freerdp can grab keyboard input since KDE 5.27. Others like VMware cannot grab correctly. [15]

It is inappropriate to force grab in Xserver or in compositors. [16] You can solve it in an elegant way as follows:

This can be caused because system settings cannot access/modify the .config folder in your home directory.

To fix this, you need to change the owner of the folder:

user refers to the name of the user that you are logged into in KDE Plasma. If the name of your home directory is not the same as the user you are logged in as, you can change it accordingly.

If this does not work, you might need to change the permissions of the folder:

There are issues with the Widget "Global Menu" not working with some applications even after installing appmenu-gtk-module and libdbusmenu-glib. The fix is to install the plasma5-integration and to restart your Session.

The factual accuracy of this article or section is disputed.

It is necessary to add a Polkit rule allowing mounting of internal drives without elevated privileges:

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/plasma-dbus-run-session-if-needed /usr/bin/startplasma-wayland
```

Example 2 (unknown):
```unknown
export DESKTOP_SESSION=plasma
```

Example 3 (unknown):
```unknown
exec startplasma-x11
```

Example 4 (unknown):
```unknown
startx /usr/bin/startplasma-x11
```

---

## GNOME/Web

**URL:** https://wiki.archlinux.org/title/GNOME/Web

**Contents:**
- Installation
- Configuration
  - Blocking advertisements
  - Tracking Prevention
  - Firefox Sync
  - Web applications
  - Custom stylesheet
  - Fonts
  - Video
  - Hardware accelerated compositing

Web is the default web browser for GNOME. Web provides a simple and minimalist interface for accessing the internet. Whilst it is developed primarily for GNOME, Web works acceptably in other desktop environments as well.

Web can be installed with the epiphany package. If you want to save login passwords, install gnome-keyring.

Enabled by default, one can disable it by unchecking Block Advertisements in Preferences. EasyList is the default blocking list. All lists are periodically refreshed.

To get list of currently enabled filters:

The filters can be modified using a JSON-formatted resource following examples at https://gitlab.com/eyeo/filterlists/contentblockerlists:

Web includes Intelligent Tracker Prevention, which can be enabled in Preferences.

Web allows the usage of Firefox Sync to sync bookmarks, history, passwords and open tabs. It can be configured in the Import and Export dropdown menu.

Web can create web applications out of websites and add them to desktop menu. To configure and remove them enter about:applications in the address bar.

Web supports custom stylesheet you can enable under Fonts and style in Preferences.

Use example below to set new tab page layout and colors according to Adwaita dark variant:

Web does not check GNOME font settings, but checks Font configuration.

See GStreamer for required plugin installation.

To enable hardware accelerated video decoding, see GStreamer#Hardware video acceleration and #Hardware accelerated compositing.

By default hardware accelerated compositing is only used when required (on-demand) to display 3D transforms.

To force enable hardware accelerated compositing:

Web doesn't respect socks_proxy, instead, you can set http_proxy to a socks:// URL :

More information: Proxy server#Environment variables

By default, Web should work with your system language if the Spell Checking option is enabled in Preferences and relevant dictionaries are installed on your system. Additional languages have to be added to the Languages list in Web's preferences from a list of available ones. That list only shows languages for which the Locale has been enabled on your system. The selection of languages in Preferences controls both spell checking and also the Accept-Language header.

**Examples:**

Example 1 (unknown):
```unknown
$ gsettings get org.gnome.Epiphany content-filters
```

Example 2 (unknown):
```unknown
$ gsettings set org.gnome.Epiphany content-filters "['https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist_min_content_blocker.json', 'https://gitlab.com/eyeo/filterlists/contentblockerlists/-/raw/master/easylist+easylistchina-minified.json']"
```

Example 3 (unknown):
```unknown
about:applications
```

Example 4 (unknown):
```unknown
~/.config/epiphany/user-stylesheet.css
```

---

## xinit

**URL:** https://wiki.archlinux.org/title/Xinitrc

**Contents:**
- Installation
- Configuration
  - xinitrc
  - xserverrc
    - Passing virtual terminal number
- Usage
- Tips and tricks
  - Override xinitrc
  - Autostart X at login
  - Switching between desktop environments/window managers

xinit is typically used to start window managers or desktop environments. While you can also use xinit to run GUI applications without a window manager, many graphical applications expect an EWMH compliant window manager. Display managers start Xorg for you and generally source xprofile.

Install the xorg-xinit package.

xinit and startx take an optional client program argument, see #Override xinitrc. If you do not provide one they will look for ~/.xinitrc to run as a shell script to start up client programs.

~/.xinitrc is handy to run programs depending on X and set environment variables on X server startup. If it is present in a user's home directory, startx and xinit execute it. Otherwise startx will run the default /etc/X11/xinit/xinitrc.

This default xinitrc will start a basic environment with Twm, xorg-xclock and Xterm (assuming that the necessary packages are installed). Therefore, to start a different window manager or desktop environment, first create a copy of the default xinitrc in your home directory:

Then edit the file and replace the default programs with desired commands. Remember that lines following a command using exec would be ignored. For example, to start xscreensaver in the background and then start openbox, use the following:

Long-running programs started before the window manager, such as a screensaver and wallpaper application, must either fork themselves or be run in the background by appending an & sign. Otherwise, the script would halt and wait for each program to exit before executing the window manager or desktop environment. Note that some programs should instead not be forked, to avoid race bugs, as is the case of xrdb. Prepending exec will replace the script process with the window manager process, so that X does not exit even if this process forks to the background.

The xserverrc file is a shell script responsible for starting up the X server. Both startx and xinit execute ~/.xserverrc if it exists, startx will use /etc/X11/xinit/xserverrc otherwise.

See Xserver(1) for a list of all command line options.

In order to maintain an authenticated session with logind and to prevent bypassing the screen locker by switching terminals, Xorg has to be started on the same virtual terminal where the login occurred [1]. For this purpose, Xorg needs to be passed the number of the current virtual terminal.

If you are invoking startx, nothing more needs to be done – it contains logic to compute and pass the virtual terminal number to Xorg.

In other cases, e.g. if you are running xinit, it is recommended to specify vt$XDG_VTNR in the ~/.xserverrc file:

To run Xorg as a regular user, issue:

Or if #xserverrc is configured:

Your window manager (or desktop environment) of choice should now start correctly.

To quit X, run your window manager's exit function (assuming it has one). If it lacks such functionality, run:

If you have a working ~/.xinitrc but just want to try other window manager or desktop environment, you can run it by issuing startx followed by the path to the window manager, for example:

If the binary takes arguments, they need to be quoted to be recognized as part of the first parameter of startx:

Note that the full path is required. You can also specify custom options for the #xserverrc script by appending them after the double dash -- sign:

Make sure that startx is properly configured.

Place the following in your login shell initialization file (e.g. ~/.bash_profile for Bash or ~/.zprofile for Zsh):

You can replace the -eq comparison with one like -le 3 (for vt1 to vt3) if you want to use graphical logins on more than one virtual terminal.

Alternative conditions to detect the virtual terminal include "$(tty)" = "/dev/tty1", which does not allow comparison with -le, and "$(fgconsole 2>/dev/null || echo -1)" -eq 1, which does not work in serial consoles.

The exec command ensures that the user is logged out when the X server exits, crashes or is killed by an attacker. If you want to take the risk and remain logged in when the X session ends, remove exec.

See also fish#Start X at login.

If you are frequently switching between different desktop environments or window managers, it is convenient to either use a display manager or expand ~/.xinitrc to make the switching possible.

The following example shows how to start a particular desktop environment or window manager with an argument:

To pass the argument session:

It is possible to start only specific applications without a window manager, although most likely this is only useful with a single application shown in full-screen mode. For example:

Alternatively the binary can be called directly from the command prompt as described in #Override xinitrc.

With this method you need to set each application's window geometry through its own configuration files (if possible at all).

See also Display manager#Starting applications without a window manager.

See Xorg#Session log redirection for details.

This article or section is a candidate for moving to Xorg.

Useful for running graphical applications:

Install xorg-server-xvfb, then run xvfb-run command.

**Examples:**

Example 1 (unknown):
```unknown
/etc/X11/xinit/xinitrc
```

Example 2 (unknown):
```unknown
$ cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

Example 3 (unknown):
```unknown
xscreensaver
```

Example 4 (unknown):
```unknown
...
xscreensaver &
exec openbox-session
```

---

## KDE Wallet

**URL:** https://wiki.archlinux.org/title/KWallet

**Contents:**
- Installation
- Configuration
  - Unlock KDE Wallet automatically on login
    - Configure PAM
    - Using SDDM autologin and LUKS encryption
- Tips and tricks
  - Using the KDE Wallet to store ssh key passphrases
  - Using the KDE Wallet to store Git credentials
  - Store GPG key passphrases
  - KDE Wallet for Chrome and Chromium

KDE Wallet Manager is a tool to manage passwords on the KDE Plasma system. Using the KWallet subsystem allows a user to keep its own secrets, but also allows a user to access passwords stored by every application that integrates with KWallet.

A wallet (in the KDE's terminology, sometimes called vault or keyring) is an encrypted volume protected by a user-defined password where user and/or software can store secrets (often, credentials when the user checked "Remember the account" in an application). Those vaults can be created and used manually by the user or created and used automatically in the background by some software that integrates with the wallet subsystem (e.g. mail applications or games). Vaults are often decrypted automatically at the user login using a PAM module (see below).

KDE Wallet is often shipped with the KDE Plasma desktop environment. The wallet subsystem can be manually installed with the kwallet package.

Optionally install the kwalletmanager package for the wallet management tool. This tool can be used to graphically create and manage a KDE Wallet.

To unlock KDE Wallet automatically on login, install kwallet-pam for the PAM compatible module. The chosen KWallet password must be the same as the current user password.

The following lines must be present under their corresponding sections:

Edit the PAM configuration corresponding to your situation:

When the system is encrypted using dm-crypt it is possible to automatically unlock KDE Wallet using the passphrase that decrypts the disk. When SDDM#Autologin is configured, the wallet can still be unlocked automatically. Edit /etc/pam.d/sddm-autologin to add pam_systemd_loadkey(8):

Then edit sddm.service, and add:

Install ksshaskpass package.

Set the SSH_ASKPASS environment variable to ksshaskpass and SSH_ASKPASS_REQUIRE to prefer (prefer to use the askpass program instead of the TTY). To set it automatically on each login, create the following environment.d(5) file:

Restart your session (i.e. relogin) so that the environment variables take effect.

The first time you try to use an SSH key, you will get asked for its passphrase. Make sure to check the Remember password checkbox. Next time, the passphrase will be read from KDE Wallet.

Git can delegate credential handling to a credential helper. By using ksshaskpass as a credential helper, the HTTP/HTTPS and SMTP passwords can be safely stored in the KDE Wallet.

Install the ksshaskpass package.

Configure Git by setting the GIT_ASKPASS environment variable:

See gitcredentials(7) for alternatives and more details.

Native KDE windows can be used to prompt for GPG key passphrases and save them in KDE Wallet.

Configure gpg-agent to use /usr/bin/pinentry-qt.

Enable the Secret Service interface. There are two ways to do this:

Close the wallet and reopen it to affect these changes. You can do this using kwalletmanager or by issuing commands to Qt D-Bus directly:

Chrome/Chromium/Opera has built in wallet integration. To enable it, run Chromium with the --password-store=kwallet5 or --password-store=kwallet6 or --password-store=detect argument. To make the change persistent, see Chromium#Making flags persistent. (Setting CHROMIUM_USER_FLAGS will not work.)

Instead of storing passwords in plain text files, you can manually add new entries in your wallet and retrieve them with kwallet-query.

For example, if you want to log into the Docker Hub registry with Podman, which supports getting the passwords from stdin with the --password-stdin flag, you can use the following command to login:

This way, your password is not stored in any text file and neither is it stored in the terminal history file.

In order to run kwallet-query outside of a graphical session (for instance as part of an unattended backup script), set the QT_QPA_PLATFORM=offscreen environment variable:

To unlock KWallet protected by the login password, it is necessary to start /usr/lib/pam_kwallet_init in the autostart portion of your window manager's configuration file in addition to configuring PAM.

In case you want to permanently disable kwallet:

Most applications use org.freedesktop.secrets.service D-Bus service. KWallet does not provide a service file for it out of the box.

You can achieve automatic activation by creating such service file:

**Examples:**

Example 1 (unknown):
```unknown
~/.local/share/kwalletd
```

Example 2 (unknown):
```unknown
~/.kde4/share/apps/kwallet
```

Example 3 (unknown):
```unknown
auth            optional        pam_kwallet5.so
session         optional        pam_kwallet5.so auto_start
```

Example 4 (unknown):
```unknown
/etc/pam.d/sddm
```

---

## Mouse buttons

**URL:** https://wiki.archlinux.org/title/Mouse_buttons

**Contents:**
- Prerequisite testing mouse input in X
- Rebinding mouse and keyboard functions
  - Binding mouse buttons to keyboard functions
    - xte
  - Binding keyboard keys to mouse buttons
    - xvkbd and xbindkeys
    - evrouter
- User tools
- evdev Xorg.conf setup
  - Finding the mouse name

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The factual accuracy of this article or section is disputed.

This article describes how to configure a mouse with more than 3 buttons.

This page assumes you are using Xorg (X Window System) and not Wayland.

You will first want to check what X sees from your mouse. X events can be displayed by the xev utility. A window will pop up by running

Any xevents (like moving, resizing, or clicking in) that window will then be reported to the console you launched xev from. Since you are filtering for lines which contain "button" it will show mouse click and release events with their relevant button numbers. For most mice, this will be '1' for left button, '2' for middle, '3' for right. Other buttons will vary (e.g. for an Logitech MX Master 3 the scroll wheel is 4 & 5, thumb wheel is 6 & 7, the thumb-tip button is 9, and the inner-thumb button is 8).

This corresponds to a left mouse click and release followed by a thumb-tip click and release.

You can use xev to confirm your mouse button numbers and to confirm that X is being notified of mouse clicks.

This section covers details of using various tools to rearrange mouse and keyboard functions.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

xte from xautomation comes handy when we want to bind keyboard buttons to mouse.

Here is example ~/.xbindkeysrc which binds Shift_R to mouse button 3 ("right click"):

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Let us say we want to bind some mouse buttons to keyboard ones. The problem we will encounter is that we do not know how to emulate a key press. Here comes in handy xvkbdAUR. We can use it along with xbindkeys.

To restart xbindkeys type:

Here is example ~/.xbindkeysrc config:

If you want to check your mouse buttons number use xev. Do not forget to type capital letters in xvkbd -text usage and to escape opening bracket with \ or you get simply [Shift] written.

Here is an example for xbindkeys to enable x selection paste(third click pasting), you need both xsel and xvkbd installed, What it does it executes that command whenever button 13 of the mouse is pressed (in ~/.xbindkeysrc) :

This is an example for a keybinding for Meta+M:

This article or section needs expansion.

Some programs, especially games, use different methods of reading input, so another program is needed: evrouterAUR.

For the evrouter command to be able to read the input devices, it will have to be run in the input group (or as root). This can be achieved by adding yourself to that group:

Now we can use the --dump option to display what the button to be changed is called:

Now press the buttons that you wish to change:

The line that ends with "fill this in!" can be copied into the configuration file which by default is ~/.evrouterrc. For example, using the X11 key event emulator built into evrouter:

The 'event1' was changed to 'event*' in case udev gives it a different device number at boot. The 'none' was changed to 'any' so that the rule works even if any modifier keys are pressed when the button is pressed. To determine the key codes (in brackets) you can use

See evrouter(1) for a full explanation of the fields.

After setting up the configuration file, run it as a daemon:

This section outlines hardware-specific tools which are useful for configuring mouse settings, and in particular their buttons. For the generic remap tools, see Input remap utilities.

This section explains setting up mice with more than 3 buttons using evdev. There are other ways to achieve this, but some of the notes and tools described here may be useful for people with other needs. Some parts may help getting extra mouse buttons working using other drivers as well.

We will be using the evdev driver for Xorg. EVentDEVice is an advanced driver for USB input devices which offers much greater power over the standard Xorg mouse driver. It is also more "direct" than the mouse driver, allowing lower latency and less translation issues.

With the Xorg 11R7.0 or newer, only the following changes to /etc/X11/xorg.conf need to be made.

The first step is to find the name of the mouse / mice. To do this, execute the following command:

This should output something like this:

Or this if you have more than one mouse:

The mouse is the one that has the Handlers=mouse0, so the name of the device is Logitech USB Gaming Mouse.

Copy the name of the device, and open up /etc/X11/xorg.conf.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Now, we need an entry in xorg.conf that tells X how to use this mouse. It should look something like this:

Replace the Name option with the name you copied from above. You may also omit the CorePointer option if you use multiple mice or experience errors when attempting to load Xorg. The other options are all basic mouse configurations for evdev and should work with most mice.

Next, we need to tell X to use the mouse, so look in xorg.conf for ServerLayout.

Modify the ServerLayout section to use "Evdev Mouse" as the device. When you are done, it should look something like this:

The only thing you should change in the layout is the InputDevice line that refers to your mouse.

That should be all that is required.

This is for Logitech G5 Mouse users. I have not tested this for other mice, but if you do not add this, your mouse MAY not work. If you do not need to add this, then do not.

in the InputDevice section or else the mouse will not be picked up.

[#] = The number you got from:

With the above method, your mouse might not to work after reboot (event number changes). To fix this, you can use symlinks in /dev/input/by-id. For example:

To find the appropriate id, do:

This article or section is out of date.

With a Desktop type keyboard-mouse, this does not work because there is only one USB attachment and /dev/input/by-id contains only the keyboard. In this case, we can create a udev rule to get a consistent link. The following rules create the link /dev/input/usbmouse which points on the correct event entry:

You can call it z10_usb_mouse.rules and put it in /etc/udev/rules.d

The cryptic value to use for SYSFS(modalias) can be gotten in the following way:

enter the command cat /proc/bus/input/devices

You will find the keyboard and the mouse and see event4 is the mouse in this case:

So I enter the following command (adapt event # to your particular case):

grab the ATTRS which becomes with usb: to complete "SYSFS{modalias}== " entry

And finally, use usbmouse as the Device Option in xorg.conf:

It works. Horizontal scroll works out of the box - push the scroll wheel left or right. Thumb buttons also work as next/previous page.

It works. Note: buttons can be mapped to functions easily in Preferences > Advanced > Shortcuts > Mouse set-up. For example, to bind button 8 to back:

To get back and forward enabled, instead of scroll left/right, change the following settings in about:config:

To do this we need to map keystrokes to the desired mouse buttons and install xvkbdAUR and xbindkeys.

In most modern applications which use back/forward features, XF86Back is mapped to back and XF86Forward is mapped to forward by default. On most MX mice the thumb buttons resolve to 8 & 9. If your mouse is different, check button numbers using xev and replace the numbers used in the example (b:8 & b:9).

So if you have an MX mouse you would create the file ~/.xbindkeysrc, containing:

Now to test... Run the following command and if it works as expected remember to add xbindkeys to .xinitrc or somewhere where it will be executed each time X starts. Also, this should work with Epiphany and Konqueror without any additional configuration or use of IMWheel.

Since xvkbd is not available from the official repositories here is another example using xte from the xautomation package

It may prove to be more comfortable for some to change the ordering of button codes, as the case may be for left-handed people. Depending on the environment you use, the button codes can be configured in two different ways. If you use .xinitrc to load X, then add this to .xinitrc (change for the number of buttons you have):

Note that buttons 4 and 5 must go on the end or else your scroll wheel will not work.

If you use GDM/SDDM/XDM instead of .xinitrc, then create the file ~/.Xmodmap and add this to it (change for the number of buttons you have):

You may have to play with these numbers a bit to get your desired behavior. Some mice use buttons 6 and 7 for the scroll wheel, in which case those buttons would have to be the last numbers. Keep playing with it until it works!

For debugging purposes xinput can be used as it is able to change the button map on the fly in userspace. The following line corrects the button mapping (there have been reported cases with Logitech M505/B605 mice and possibly others) so the received events are mapped correctly:

It is known that in xorg-server 1.18.0-3 side buttons of G600 are not recognized as a separate keyboard device, but another mouse which causes strange (moving mouse cursor to an edge of screen when one of main mouse buttons are clicked) behavior. To force xorg to recognize them as a keyboard buttons, add following section to your /etc/X11/xorg.conf:

These mice are designed for Windows 8 and have non-conventional behavior: the mouse appears as a mouse and keyboard and some buttons do not emit the standard mouse button event but a combination of keyboard and mouse button presses instead. This prevents "comfortable" use of this mouse under Linux.

The appropriate driver allows the mouse to be used like an ordinary mouse:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

See also Xbindkeys for mouse button mapping.

If you want to bind the buttons + and - in G5/7 mouse, which normally changes DPI, you have to use g5hack [3] released by a lomoco author.

This will change your DPI to 2000, light the 1st LED and disables DPI on-the-fly changing, so you can use it with evrouter. If you would use it frequently I suggest you to copy it to the /usr/bin directory:

If you want to bind your + and - buttons you must copy the line at the bottom (one with the comment '"-" button does not function anymore' above) to the mode you will be using, like, for example, under the "case 3:" you can put it on the line with the comment 'turn on third led' above (deleting the old one before of course).

For the newest G5 mouse which is reported as "product 0xc049" original hack does not work. You have to simply change the #define MOUSE_G5 0xc041 to #define MOUSE_G5 0xc049 and recompile.

You can execute the g5hack tool at system start up using systemd unit. See Systemd#Writing unit files for detail.

If you want to support more than two or three mouse buttons, the capability will depend on your hypervisor software.

For your Arch-based guest VM, add the below lines to its .vmx configuration file:

**Examples:**

Example 1 (unknown):
```unknown
$ xev -event button | grep button
```

Example 2 (unknown):
```unknown
state 0x0, button 1, same_screen YES
state 0x100, button 1, same_screen YES
state 0x0, button 9, same_screen YES
state 0x0, button 9, same_screen YES
```

Example 3 (unknown):
```unknown
~/.xbindkeysrc
```

Example 4 (unknown):
```unknown
~/.xbindkeysrc
```

---

## Xsettingsd

**URL:** https://wiki.archlinux.org/title/Xsettingsd

**Contents:**
- Installation
- Configuration
- Usage
- Troubleshooting
  - Unable to open connection to X server

Xsettingsd is a lightweight xsettings daemon which provides settings to Xorg applications via the XSETTINGS specification.

Some desktop environments (such as Plasma by default, or a custom one) do not include this. In such environments running an xsettings daemon is necessary for some applications (most notably GTK–, Java– and Wine–based) to use the selected theme, cursor, font, and other settings.

Install xsettingsd or xsettingsd-gitAUR.

xsettingsd(1) contains just brief intro, see README for details.

An example configuration to X FreeType font rendering (you can use your preferred config file path):

Start the user unit xsettingsd.service.

This unit is static, so it cannot be enabled directly. You can autostart it (or xsettingsd binary) on Xorg, desktop environment or window manager startup.

The unit is configured as PartOf the graphical-session.target, so it stops (restarts) when graphical-session.target is stopped (restarted), see systemd.unit(5) § [UNIT] SECTION OPTIONS and systemd.special(7) § Special Passive User Units.

Check that DISPLAY and XAUTHORITY environment variables are set.

If you are starting the systemd unit, check that systemctl --user import-environment DISPLAY XAUTHORITY was executed (it can be done by /etc/X11/xinit/xinitrc.d/50-systemd-user.sh invoked from your ~/.xinitrc).

**Examples:**

Example 1 (unknown):
```unknown
~/.config/xsettingsd/xsettingsd.conf
```

Example 2 (unknown):
```unknown
Xft/Antialias   1
Xft/DPI         98304
Xft/Hinting     1
Xft/HintStyle   "hintfull"
Xft/lcdfilter   "lcddefault"
Xft/RGBA        "rgb"
```

Example 3 (unknown):
```unknown
Xft.dpi: 96
```

Example 4 (unknown):
```unknown
~/.Xresources
```

---

## Xfce

**URL:** https://wiki.archlinux.org/title/Xfce

**Contents:**
- Installation
- Starting
- Configuration
  - Menu
    - Whisker menu
      - Set keyboard shortcut to launch whisker menu
    - Edit entries
    - Set preferred applications
  - Desktop
    - Remove desktop icons

Xfce is a lightweight and modular desktop environment based on GTK. To provide a complete user experience, it includes a window manager, a file manager, desktop and panel.

Install the xfce4 group. You may also wish to install the xfce4-goodies group which includes extra plugins and a number of useful utilities such as the mousepad editor. Xfce uses the Xfwm window manager by default.

Choose Xfce Session from the menu in a display manager of choice, or add exec startxfce4 to Xinitrc.

Xfce stores configuration options in Xfconf. There are several ways to modify these options:

See Xdg-menu for more info on using the Free Desktop menu system.

xfce4-whiskermenu-plugin (also part of xfce4-goodies) is an alternative application launcher. It shows a list of favorites, browses through all installed applications through category buttons, and supports fuzzy searching. After package being installed, it can replace Applications Menu as first item in Panel 1 (in Settings > Panel > Items add Whisker Menu).

To set a keyboard shortcut to launch the whisker menu, go to Settings > Keyboard and then the Application Shortcuts tab. Click on the Add button, set the command to xfce4-popup-whiskermenu and assign the desired keyboard shortcut.

A number of graphical tools are available for this task:

Alternatively, create the file ~/.config/menus/xfce-applications.menu manually. See the example configuration below:

The <MergeFile> tag includes the default Xfce menu.

The <Exclude> tag excludes applications which we do not want to appear in the menu. Here we excluded some Xfce default shortcuts, but you can exclude firefox.desktop or any other application.

The <Layout> tag defines the layout of the menu. The applications can be organized in folders or however we wish. For more details see the Xfce wiki.

You can also make changes to the Xfce menu by editing the .desktop files themselves. To hide entries, see Desktop entries#Hide desktop entries. You can edit the application's category by modifying the Categories= line of the desktop entry, see Desktop entries#File example.

To change the default applications used for opening certain resources, use the Preferred Applications setting. This will change the behavior of exo-open, which is invoked by resource openers such as xdg-open.

Issue the following command:

To reinstate icons on the desktop, issue the same command with a value of 2.

Xfce does not have a shortcut to kill a window, for example when a program freezes.

With xorg-xkill, use xkill to interactively kill a window. For the currently active window, use xdotool:

To add the shortcut, use Settings > Keyboard or an application like xbindkeys.

To launch custom applications when Xfce starts up, click the Applications Menu > Settings > Settings Manager and then choose the Session and Startup option and click the tab Application Autostart. You will see a list of programs that get launched on startup. To add an entry, click the Add button and fill out the form, specifying the path to an executable you want to run.

Autostart application location paths are described in the XDG Autostart specification.

Alternatively, add the commands you wish to run (including setting environment variables) to xinitrc (or xprofile when a display manager is being used).

xflock4 is the reference Shell script which is used to lock an Xfce session.

It tries to lock the screen with these screen lockers in the specified order:

It exits with return code 1 if it fails to find any of these.

The List of applications/Security#Screen lockers contains a short description of these screen lockers together with other popular applications.

To have xflock4 run a custom session locker, set LockCommand in the session's xfconf channel to the command line to be used:

The panel lock button in the Action Buttons panel simply executes /usr/bin/xflock4. It should work as expected as long as xflock4 is functioning i.e. one of the native lockers is installed or a custom locker is configured to integrate with it as proposed above.

Whether or not the session is systematically locked on suspend can be configured through the xfconf properties or from the GUI.

To prevent locking on suspend using the CLI, turn lock-screen-suspend-hibernate to false:

Similarly, turn it to true to lock the session on suspend.

The setting can also be controlled from the GUI: open the Session and Startup application and turn the flag General > Lock screen before sleep on or off.

Whenever the suspend keyboard button is pressed, it can be handled by either Xfce's power manager or by systemd-logind. To give precedence to logind, the following xfconf setting must be set to true:

Per user, saved sessions can be disabled by unchecking Applications > Settings > Session and Startup > General > Automatically save session on logout or by executing the following command:

Alternatively, Xfce kiosk mode can be used to disable the saving of sessions systemwide. To disable sessions, create or edit the file /etc/xdg/xfce4/kiosk/kioskrc and add the following:

You may need to remove previously saved sessions. Navigate to Applications > Settings > Session and Startup > Saved Sessions and press the Clear Saved Sessions button, or simply delete the ~/.cache/sessions/ directory.

The files specifying the default window manager are found in the following locations:

The default window manager for the user can be set easily using xfconf-query:

If you want to start the window manager with command line options, see the commands below:

If you need more command line options, simply add more -t string and -s --wm-option arguments to the command.

If you want to change the default window manager systemwide, edit the file specified above manually, changing xfwm4 to the preferred window manager and adding more <value type="string" value="--wm-option"/> lines for extra command line options if needed.

You can also change the window manager by autostarting wm_name --replace using the autostart facility or by running wm_name --replace & in a terminal and making sure the session is saved on logout. Be aware though that this method does not truly change the default manager, it merely replaces it at login. Note that if you are using the autostart facility, you should disable saved sessions as this could lead to the new window manager being started twice after the default window manager.

XFCE themes are available at xfce-look.org. Xfwm themes are stored in /usr/share/themes/theme_name/xfwm4, and set in Settings > Window Manager. GTK themes are stored in /usr/share/themes/theme_name/gtk-2.0 and /usr/share/themes/theme_name/gtk-3.0 and are set in Settings > Appearance.

To achieve a uniform look for all applications, see Uniform look for Qt and GTK applications.

See also Cursor themes, Icons, and Font configuration.

Xfce currently uses Server-Side Decorations (SSD) (see Wikipedia:Window decoration) themed by Xfwm for most windows and Client-side decoration (CSD) themed by the respective programs for Xfce Settings, Print, Save, and other dialogs.

Xfwm SSD window styles can be themed to match the CSD windows by manually adjusting or creating themes in /usr/share/themes/theme_name/xfwm4 or by using a tool such as the Xfwm4 Theme Generator which "Creates xfwm4 themes from client side decorations."

With Xfce 4.18, client-side decorations are optional and disabled by default. [1]

Non-Xfce applications may still use client-side decorations. To disable them globally, see GTK#Client-side decorations.

XFCE4 supports freedesktop system sounds, but it is not configured out of the box.

To enable a sound theme:

sound-theme-freedesktop provides a compatible sound theme, but it lacks many required events. A better choice is sound-theme-smoothAUR (SoundThemeName should be Smooth).

xfce4-pulseaudio-plugin provides a panel applet which has support for keyboard volume control and volume notifications. As an alternative, you can install xfce4-volumed-pulse, which also provides keybinding and notification control, but without an icon sitting in the panel. This is handy, for example, when using pasystray at the same time for a finer control.

Alternatively, xfce4-mixer also provides a panel applet and keyboard shortcuts. The Arch package only supports ALSA, but you can rebuild it manually to add PulseAudio support.

After installing the panels, you have to add it to the taskbar or the keyboard shortcuts will not work.

For non desktop environment specific alternatives, see List of applications/Multimedia#Volume control.

If you are not using an applet or daemon that controls the volume keys, you can map volume control commands to your volume keys manually using Xfce's keyboard settings. For the sound system you are using, see the sections linked to below for the appropriate commands.

Keyboard shortcuts are defined in two places: Settings > Window Manager > Keyboard, and Settings > Keyboard > Shortcuts.

The polkit-gnome agent will be installed along with xfce4-session and autostarted automatically; no user intervention is required. For more information, see Polkit#Authentication agents.

A third party polkit authentication agent for Xfce is also available, see xfce-polkitAUR or xfce-polkit-gitAUR.

Some programs that are commonly used with Xfce will control monitor blanking and DPMS (monitor powersaving) settings. They are discussed below.

Xfce Power Manager controls DPMS settings only. They can be configured in the Power Manager GUI within the Display tab.

Note that when Display power management is turned off, DPMS is fully disabled, but this does not mean that Power Manager will simply stop controlling DPMS. However, it does not control screen blanking, which may remain enabled even after display power management is disabled. [2] To disable both blanking and DPMS, right click on the power manager system tray icon or left click on the panel applet and make sure that the option labelled Presentation mode is ticked.

If xscreensaver is installed and runs alongside Xfce Power Manager, it may not be clear which application is in control of blanking and DPMS as both are competing for control of the same settings. Therefore, in a situation where it is important that the monitor not be blanked (when watching a video for instance), it is advisable to disable blanking and DPMS through both applications. To know more about XScreenSaver options, see XScreenSaver#DPMS and blanking settings.

If neither of the above applications are running, then blanking and DPMS settings can be controlled using the xset command, see DPMS#Runtime settings.

If plugged external drives does not appear and installation partitions are shown as mounted devices, on the desktop and in Thunar, install gvfs. See Udisks#Hide selected partitions for more advanced configuration options.

Xfce has its own screenshot tool, xfce4-screenshooter. It is part of the xfce4-goodies group.

Default keyboard shortcuts: Print opens the main dialog window, Alt+Print takes a screenshot of the active window, Shift+Print allows you to select a region to be captured.

Alternatively, an independent screenshot program like scrot can be used.

Terminal color themes or palettes can be changed in the GUI, under the Colors tab in Preferences. These are the colors that are available to most console applications like Emacs, Vi and so on.

The settings are stored in Xfconf. Although you can edit them directly, it might be more convenient to download or create a color preset file. The default presets are stored in /usr/share/xfce4/terminal/colorschemes/, custom presets can be placed in ~/.local/share/xfce4/terminal/colorschemes/. You can select a preset in Preferences > Colors > Presets.

Check forum thread Terminal Colour Scheme Screenshots for hundreds of available choices and themes.

A commented example of a color preset file:

The env-modulesAUR package provides shell autocompletion for login shells. However, by default, sessions in xfce4-terminal are not considered as login. To enable autocompletion for Environment Modules, tick the Run command as login shell checkbox in Preferences > General.

Xfce has no native support for colour management. [5] See ICC profiles for alternatives.

Xfce has support for multiple monitors, which can be configured in the Applications > Settings > Display dialog. In the Advanced tab, one can save profiles for different monitors and have them applied automatically as soon as the connected monitors change. For more information, see the display article from the Xfce documentation.

Alternatively, one can use arandr to manage display configurations in the form of xrandr commands which can be assigned to Xfce keyboard shortcuts.

By default, Xfce will try to load gpg-agent and ssh-agent. Since gpg-agent is handled by systemd, you may want to disable it in the Xfce settings:

If you plan to use the ssh-agent.service user unit as described in SSH keys#Start ssh-agent with systemd user, disable ssh-agent in the Xfce settings as well:

To use GNOME Keyring, simply tick the checkbox Launch GNOME services on startup in the Advanced tab of Session and Startup in Xfce's settings. This will also disable gpg-agent and ssh-agent.

Source: https://docs.xfce.org/xfce/xfce4-session/advanced#ssh_and_gpg_agents

Go to Main Menu > Settings > Window Manager Tweaks > Accessibility tab. Uncheck Raise windows when any mouse button is pressed.

By default, the mouse button modifier in Xfce is set to Alt. This can be changed with xfconf-query. For instance, the following command will set the Super key as the mouse button modifier:

Strictly speaking, using multiple modifiers is not supported. However, as a workaround, multiple modifiers can be specified if the key names are separated with ><. For instance, to set Ctrl+Alt as the mouse button modifier, you can use the following command:

Limiting the minimum brightness can be useful for displays which turn off backlight on a brightness level of 0. In xfce4-power-manager 1.3.2 a new hidden option had been introduced to set a minimum brightness value with a xfconf4-property. Add brightness-slider-min-level as an int property in xfconf4. Adjust the int value to get a suitable minimum brightness level.

To add profile pictures for each user to be displayed in the whisker-menu, simply place a 96x96 PNG file in /home/user/.face.

Image editing programs like GIMP can be used to scale your favourite images down to 96x96 and convert it.

The xfconf option show-panel-label of type int controls the label of the power manager, it can be configured for different label formats: it can be set to 0 (no label), 1 (percentage), 2 (remaining time) or 3 (both).

It is also accessible through the power manager plugin GUI in Properties > Show label

The Super key is treated as a modifier key, like Ctrl and Alt, instead of producing a keypress. Assigning an action to it will keep you from using it for other shortcuts, because it will trigger that action in addition to whatever else you assign to it.

To get around this, and make it more useful for shortcuts, install the application xcape. This lets you configure modifier keys to act as other keys when pressed and released on their own.

Next, go to Settings > Keyboard > Application Shortcuts and assign an unused key combination, say Alt+F1, to the Application menu (or whatever action you want when you press the Super key by itself). Test that it works. Next, use xcape to assign Alt+F1 to the Super key:

Check that the Super key now performs the action you assigned to Alt+F1.

If all is well, make this an autostart action; go to Settings > Session and Startup > Application Autostart tab, press the Add button and enter the command there to make it run every time you start Xfce (if xcape was already installed, also check that there is not already a similar entry registered).

Now, you can freely use the Super key in shortcuts. For example: In Window Manager > Keyboard, you can use Super and Up or Down for Raise window or Lower window.

Xfce supports both labwc and wayfireAUR as its Wayland compositor. However, only labwc works out of the box; Wayfire requires additional tweaking to the session file to make it work. For this purpose this section focuses on getting Xfce working with labwc as it requires the least effort to get Xfce working in Wayland.

After installing labwc, you should be able to switch to the Xfce Session (Wayland) option in your display manager of choice and log in as usual. Note that Wayland support is marked as experimental for a good reason: things will not work like you expect it to and a lot of stuff is generally broken. For example, desktop icons placed by xfdesktop may appear and disappear as the desktop gain and lose focus.

The labwc configuration files for Xfce are located in ~/.config/xfce4/labwc/ instead of the default labwc directory ~/.config/labwc/. If you have a custom environment file with keymaps in it, you need a lock file ~/.config/xfce4/labwc/lock, otherwise the layout gets overwritten by startxfce4 with the system's default layout.

If you are running a separate Xsettings daemon, it may make some configuration not taking effect. Disable it by removing or commenting the corresponding line and restart Xorg.

To detect and use the sensors of an NVIDIA GPU, install libxnvctrl and then rebuild xfce4-sensors-plugin with ABS. Another option is xfce4-sensors-plugin-nvidiaAUR which replaces xfce4-sensors-plugin.

Add a separator someplace before the right end and set its "expand" property. [6]

If for any reason you need to revert back to the default settings, remove or rename ~/.config/xfce4/:

Relogin for changes to take effect. If you get Unable to load a failsafe session upon login, see the #Session failure section.

Restarting Xfce or rebooting your system may solve the problem, but a corrupt session could also be the cause. Delete the session folder:

Also make sure that the relevant folders in $HOME are owned by the user starting xfce4. See Chown.

Run the following to make it visible:

Trash requires the optional dependency gvfs to work. Install gvfs and reboot the system.

If you are trying to get Xfce working with WayfireAUR, additional editing must be done to the session files to make it work.

If not, make sure you have labwc installed.

**Examples:**

Example 1 (unknown):
```unknown
exec startxfce4
```

Example 2 (unknown):
```unknown
xfce4-session
```

Example 3 (unknown):
```unknown
/usr/bin/xfce4-*
```

Example 4 (unknown):
```unknown
/usr/bin/xfdesktop-settings
```

---

## GNOME/Files

**URL:** https://wiki.archlinux.org/title/GNOME/Files

**Contents:**
- Installation
  - Extensions
    - Applications that ship their own Nautilus extensions
    - Extensions that rely on non-free software
- Configuration
  - Change default item view
  - Sort by type
  - Remove folders from the places sidebar
  - Always show text-entry location
- Tips and tricks

Files is the default file manager for GNOME. Files attempts to provide a streamlined method to manage both files and applications.

Install the nautilus package. This package is part of the gnome group. See also File manager functionality#Additional features.

Some programs can add extra functionality to Files. Here are a few examples:

The following applications install their own extensions by default, thus providing integration with Nautilus:

Some extensions for GNOME Files, although free, might rely on non-free software. The following list provides a few examples:

Files is simple to configure graphically, but not all options are available in the preferences menu. More options are available with dconf-editor under org.gnome.nautilus.

You can change the default view for the items by setting the default-folder-viewer variable, e.g. for the list view:

To sort files in all folders by type:

The displayed folders are specified in ~/.config/user-dirs.dirs and can be altered with any editor. An execution of xdg-user-dirs-update will change them again, thus it may be advisable to set the file permissions to read-only.

The standard Files toolbar shows a button bar interface for path navigation. To enter path locations using the keyboard, you must expose the location text-entry field. This is done by pressing Ctrl+l

To make the location text-entry field always present, use gsettings as shown below:

See File manager functionality#Thumbnail previews.

Sometimes video thumbnails are not shown. To solve it (as mentioned in No video thumbnails on nautilus), you must install ffmpegthumbnailer, gst-libav, gst-plugins-ugly, and remove the content of ~/.cache/thumbnails/fail/.

To get this option one has to create a ~/Templates/ folder in your home folder and place an empty file inside the folder through your favorite Terminal by touch ~/Templates/new or by using any other file manager. Then just restart Files.

On non-English installations, the templates directory might have another name. One can find the actual directory with xdg-user-dir TEMPLATES.

The templates directory can be configured in the ~/.config/user-dirs.dirs file:

Like most other file managers GNOME Files hides files with names starting with a dot by default.

GNOME Files additionally hides files when their names are listed in a .hidden file in the same directory (one filename per line). See nautilus-hideAUR for an extension that facilitates adding/removing entries from such .hidden files.

If you are using tilixAUR terminal you can easily add "Open in Tilix" option to the context menu of GNOME Files by installing its optional dependency nautilus-python.

To add a folder to your bookmarks, simply press Ctrl+d when you have the folder opened in Nautilus. Note that the list of bookmarks is shared with other GNOME-based graphical file managers (e.g. Nemo), so a folder added or removed from one will affect the bookmarks seen in the other.

Scripts placed in ~/.local/share/nautilus/scripts can be run from the right click context menu of a file.

The context menu can also be organized into subfolders, e.g. ~/.local/share/nautilus/scripts/images and ~/.local/share/nautilus/scripts/music.

Scripts have access to the following environment variables:

Some example scripts:

Keybinds to execute scripts can be assigned in the ~/.config/nautilus/scripts-accels file:

By installing gvfs and the various gvfs-* packages, you can add support for various network based filesystems (e.g. SMB, NFS, WebDAV, Nextcloud) and some mobile phones (Android MTP, Apple AFC).

For more information and other supported virtual filesystems, see File manager functionality.

This can be caused by the file association for directories being reset. Installing anjutaAUR or visual-studio-code-binAUR tend to do this.

To solve this, open Files, right-click on a folder, and choose Open With Other Application > Files > Select. This will set the association for directories back to Files.

If this does not solve the issue, see File manager functionality#Directories are not opened in the file manager.

In case you have kdeconnect installed in your system, the problem might be caused by its file sharing module. Deactivate file sharing, and it should stop happening.

You may be missing one or more of the following packages:

Install them and you should be good to go.

To activate the WSD support in GNOME/Files install gvfs-wsdd to make GNOME/Files discover newer Windows machines in the network view. There is no further tweaking necessary.

Install gvfs-dnssd and restart Nautilus.

'Run as a Program' context menu option is hardcoded for gnome-console and if you use different terminal and the default gnome terminal is not present, the context menu option won't do anything.

Since it's just executing /usr/bin/kgx (executable for gnome-console) directly, you can create script (or symlink if your terminal has the same arguments) named kgx and place it inside /usr/bin/ to use your terminal for 'Run as a Program' context menu option.

Example for using wezterm-gitAUR as a terminal for 'Run as a Program'

It is possible to open a directory in a terminal emulator with "Open with..." right click menu entry. But the XDG desktop entry of the terminal is expected to contain appropriate Exec and MimeType values.

Following example shows how to create additional desktop entry for Alacritty terminal emulator which will be recognized by "Open with...".

Run update-desktop-database ~/.local/share/applications/ to apply changes.

If a terminal app became default file manager, it can be fixed with command xdg-mime default org.gnome.Nautilus.desktop inode/directory.

Check flags and desktop entry file of your preferred terminal application to adopt the example.

**Examples:**

Example 1 (unknown):
```unknown
audio/x-mp3
```

Example 2 (unknown):
```unknown
audio/x-flac
```

Example 3 (unknown):
```unknown
audio/x-vorbis+ogg
```

Example 4 (unknown):
```unknown
audio/x-speex+ogg
```

---

## Thunar

**URL:** https://wiki.archlinux.org/title/Thunar

**Contents:**
- Installation
  - Plugins and addons
- Configuration
  - Configuring keybindings
  - Change the default sorting behavior
- Thunar Volume Manager
  - Configuration
- Custom actions
  - Open Terminal Here
  - Search for files and folders

From the project home page:

Install the thunar package. Thunar is part of the xfce4 group and the default file manager of the Xfce desktop environment.

To configure the keybindings, edit the file ~/.config/Thunar/accels.scm. To configure Thunar's hidden variables, use xfconf-query -c thunar -l -v.

In Thunar it is possible to change the default sorting order. The /etc/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar.xml file has to be edited, most likely even created. This is what the contents should be like for sort by name, ascending:

If both gvfs and thunar-volman are installed, Thunar can be configured to run commands automatically when media are connected. For mobile devices, which generally follow MTP, an additional gvfs-mtp package is required.

It can also be configured to execute certain actions when cameras and audio players are connected. After installing the plugin:

Here is an example setting for making Amarok play an audio CD.

This section covers useful custom actions which can be accessed through Edit -> Configure custom actions and which are stored in ~/.config/Thunar/uca.xml. More examples are listed in the Thunar wiki. Furthermore, this blog post provides a comprehensive collection of custom actions.

Open Terminal Here is the sole action on installation. Tell exo which terminal to use:

To use this action, you need to have catfish installed. The plocate and zeitgeist dependencies are optional for users that want to use a prebuilt index database.

To use this action, you need to have clamav and clamtk installed.

Please note that when using many custom actions to symlink files and folder to a particular place, it might be useful to put them into the Send To folder of the context menu to avoid that the menu itself gets bloated. This is fairly easy to achieve and requires a .desktop file in ~/.local/share/Thunar/sendto for each action to perform. Say we want to put the above Dropbox symlink action into Send To, we create a dropbox_folder.desktop with the following content. The new applied action will be active after restarting Thunar.

Since Xfce 4.8 (Thunar 1.2) it is possible to browse remote locations (such as FTP servers or Samba shares) directly in Thunar. To enable this functionality, ensure that gvfs and sshfs (as well as gvfs-smb if you need SMB/CIFS support) are installed. A 'Network' entry is visible in Thunar's side bar and remote locations can be opened by using the following URI schemes in the location dialog (opened with Ctrl+l): smb://, ftp://, ssh://, sftp://, davs:// & followed by the server hostname or IP address.

There is no URI scheme for NFS shares, but Thunar can issue a mount command if you setup your fstab properly.

What is important here is the noauto which prevents the share from being mounted until you click on it, user which allows any user to mount (and unmount) the share, _netdev which makes network connectivity a pre-requisite, and finally, bg which puts the mounting operation in the background so if your server requires some spin-up time, you will not have to deal with time out messages and re-clicking until it works.

Thunar may be run in daemon mode. This has several advantages, including a faster startup for Thunar, Thunar running in the background and only opening a window when necessary (for instance, when a flash drive is inserted), and letting Thunar handle automatic mounting of removable media.

Make sure the command thunar --daemon is autostarted on login. See Xfce and Autostarting for more details.

Some people still have problems with Thunar taking a long time to start for the first time. This is due to gvfs checking the network, preventing Thunar from starting until gvfs finishes its operations. To change this behaviour, edit /usr/share/gvfs/mounts/network.mount and change AutoMount=true to AutoMount=false.

There is a hidden menu to hide Shortcuts in the Side Pane.

Right click in the Side Pane where there are no shortcuts, like on the DEVICES section label. Then you will get a pop-up menu where you can uncheck items you do not want displayed.

See GTK#Keyboard shortcuts,

By default, Thunar will not show in devices any partitions defined in /etc/fstab besides the root partition.

We can change that by adding the option x-gvfs-show to fstab for the partition we wish to show.

Tumblerd, the service that watches the file system and notifies the system when a thumbnail needs to be made, may get stuck in a loop, using 100% of the system's CPU; see the bug report. The following script is a temporary workaround to stop this from happening. Copy, and paste this into a .sh file, save it somewhere in your home directory, mark the file as executable and then set up the system to autostart it at system startup.

Make sure all Thunar instances start after gvfs. [1] For thunar --daemon, you can create a wrapper that waits until GVFS is active:

See File manager functionality#Troubleshooting.

It might be the case that you have many files under the folder that you have set to be the XDG_TEMPLATES_DIR. See XDG user directories.

The solution is to move files from whatever folder is the XDG_TEMPLATES_DIR to another one, or set the XDG_TEMPLATES_DIR to another folder.

**Examples:**

Example 1 (unknown):
```unknown
~/.config/Thunar/accels.scm
```

Example 2 (unknown):
```unknown
xfconf-query -c thunar -l -v
```

Example 3 (unknown):
```unknown
/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
```

Example 4 (unknown):
```unknown
/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
```

---

## Equinox Desktop Environment

**URL:** https://wiki.archlinux.org/title/Equinox_Desktop_Environment

**Contents:**
- Installation
- Starting the DE
- Applications
  - Some recommendations

The Equinox Desktop Environment (EDE) is a desktop environment designed to be simple, extremely light-weight and fast.

It primarily offers the most basic things: A window manager (PekWM is used by default), a simple GUI including a panel, a daemon watching removable media and a notification daemon. Other than that there is not much more than some configuration programs, a calculator, etc. Beginning with version 2.0, EDE follows the FreeDesktop.org guidelines.

Unlike any other desktop environment, EDE is based upon the FLTK toolkit. It is especially fit for systems with little RAM or for users who want to completely customize their system and need a GUI that is not already bloated with functions and applications.

EDE can be installed with the edeAUR package.

To bring up EDE you can either use a display manager or use startx. If you choose the later, just write the following to the .xinitrc of your user:

Since EDE is a bare-bone DE, you will have to add even the most common applications like a file manager or an editor yourself. You have the freedom of choice.

Due to the nature of the DE, it obviously makes sense to install light-weight software. There are however not that many FLTK applications available so you will likely have to relay on a second toolkit like GTK for example.

**Examples:**

Example 1 (unknown):
```unknown
exec startede
```

---

## xinit

**URL:** https://wiki.archlinux.org/title/Xinit

**Contents:**
- Installation
- Configuration
  - xinitrc
  - xserverrc
    - Passing virtual terminal number
- Usage
- Tips and tricks
  - Override xinitrc
  - Autostart X at login
  - Switching between desktop environments/window managers

xinit is typically used to start window managers or desktop environments. While you can also use xinit to run GUI applications without a window manager, many graphical applications expect an EWMH compliant window manager. Display managers start Xorg for you and generally source xprofile.

Install the xorg-xinit package.

xinit and startx take an optional client program argument, see #Override xinitrc. If you do not provide one they will look for ~/.xinitrc to run as a shell script to start up client programs.

~/.xinitrc is handy to run programs depending on X and set environment variables on X server startup. If it is present in a user's home directory, startx and xinit execute it. Otherwise startx will run the default /etc/X11/xinit/xinitrc.

This default xinitrc will start a basic environment with Twm, xorg-xclock and Xterm (assuming that the necessary packages are installed). Therefore, to start a different window manager or desktop environment, first create a copy of the default xinitrc in your home directory:

Then edit the file and replace the default programs with desired commands. Remember that lines following a command using exec would be ignored. For example, to start xscreensaver in the background and then start openbox, use the following:

Long-running programs started before the window manager, such as a screensaver and wallpaper application, must either fork themselves or be run in the background by appending an & sign. Otherwise, the script would halt and wait for each program to exit before executing the window manager or desktop environment. Note that some programs should instead not be forked, to avoid race bugs, as is the case of xrdb. Prepending exec will replace the script process with the window manager process, so that X does not exit even if this process forks to the background.

The xserverrc file is a shell script responsible for starting up the X server. Both startx and xinit execute ~/.xserverrc if it exists, startx will use /etc/X11/xinit/xserverrc otherwise.

See Xserver(1) for a list of all command line options.

In order to maintain an authenticated session with logind and to prevent bypassing the screen locker by switching terminals, Xorg has to be started on the same virtual terminal where the login occurred [1]. For this purpose, Xorg needs to be passed the number of the current virtual terminal.

If you are invoking startx, nothing more needs to be done – it contains logic to compute and pass the virtual terminal number to Xorg.

In other cases, e.g. if you are running xinit, it is recommended to specify vt$XDG_VTNR in the ~/.xserverrc file:

To run Xorg as a regular user, issue:

Or if #xserverrc is configured:

Your window manager (or desktop environment) of choice should now start correctly.

To quit X, run your window manager's exit function (assuming it has one). If it lacks such functionality, run:

If you have a working ~/.xinitrc but just want to try other window manager or desktop environment, you can run it by issuing startx followed by the path to the window manager, for example:

If the binary takes arguments, they need to be quoted to be recognized as part of the first parameter of startx:

Note that the full path is required. You can also specify custom options for the #xserverrc script by appending them after the double dash -- sign:

Make sure that startx is properly configured.

Place the following in your login shell initialization file (e.g. ~/.bash_profile for Bash or ~/.zprofile for Zsh):

You can replace the -eq comparison with one like -le 3 (for vt1 to vt3) if you want to use graphical logins on more than one virtual terminal.

Alternative conditions to detect the virtual terminal include "$(tty)" = "/dev/tty1", which does not allow comparison with -le, and "$(fgconsole 2>/dev/null || echo -1)" -eq 1, which does not work in serial consoles.

The exec command ensures that the user is logged out when the X server exits, crashes or is killed by an attacker. If you want to take the risk and remain logged in when the X session ends, remove exec.

See also fish#Start X at login.

If you are frequently switching between different desktop environments or window managers, it is convenient to either use a display manager or expand ~/.xinitrc to make the switching possible.

The following example shows how to start a particular desktop environment or window manager with an argument:

To pass the argument session:

It is possible to start only specific applications without a window manager, although most likely this is only useful with a single application shown in full-screen mode. For example:

Alternatively the binary can be called directly from the command prompt as described in #Override xinitrc.

With this method you need to set each application's window geometry through its own configuration files (if possible at all).

See also Display manager#Starting applications without a window manager.

See Xorg#Session log redirection for details.

This article or section is a candidate for moving to Xorg.

Useful for running graphical applications:

Install xorg-server-xvfb, then run xvfb-run command.

**Examples:**

Example 1 (unknown):
```unknown
/etc/X11/xinit/xinitrc
```

Example 2 (unknown):
```unknown
$ cp /etc/X11/xinit/xinitrc ~/.xinitrc
```

Example 3 (unknown):
```unknown
xscreensaver
```

Example 4 (unknown):
```unknown
...
xscreensaver &
exec openbox-session
```

---

## Desktop entries

**URL:** https://wiki.archlinux.org/title/Desktop_entry

**Contents:**
- Basics
- Usage
- Application entry
  - File example
  - Key definition
  - Validation
  - Installation
  - Update database of desktop entries
- Icons
  - Common image formats

The XDG Desktop Entry specification defines a standard for applications to integrate into application menus of desktop environments implementing the XDG Desktop Menu specification.

Each desktop entry must have a Type and a Name key and can optionally define its appearance in the application menu.

The three available types are:

The following sections will roughly explain how these are created and validated.

Use a desktop opener like dex:

Desktop entries for applications, or .desktop files, are generally a combination of meta information resources and a shortcut of an application. These files usually reside in /usr/share/applications/ or /usr/local/share/applications/ for applications installed system-wide, or ~/.local/share/applications/ for user-specific applications. User entries take precedence over system entries.

Following is an example of its structure with additional comments. The example is only meant to give a quick impression, and does not show how to utilize all possible entry keys. The complete list of keys can be found in the freedesktop specification.

All recognized entries can be found on the freedesktop site. For example, the Type key defines three types of desktop entries: Application (type 1), Link (type 2) and Directory (type 3).

This should be avoided, as it will only be confusing to users. The Name key should only contain the name, or maybe an abbreviation/acronym if available.

As some keys have become deprecated over time, you may want to validate your desktop entries using desktop-file-validate(1) which is part of the desktop-file-utils package. To validate, run:

This will give you very verbose and useful warnings and error messages.

Use desktop-file-install(1) to install desktop file into target directory. For example:

This is also useful for customizing existing desktop entries (e.g. from /usr/share/applications) via edit options.

Usually, desktop entry changes are automatically picked up by desktop environments.

If this is not the case, and you want to forcefully update the desktop entries defined in ~/.local/share/applications, run the following command:

See also the Icon Theme Specification.

Here is a short overview of image formats commonly used for icons.

This article or section is a candidate for merging with ImageMagick#Usage.

If you stumble across an icon which is in a format that is not supported by the freedesktop.org standard (like gif or ico), you can use the magick tool (which is part of the imagemagick package) to convert it to a supported/recommended format, e.g.:

If you convert from a container format like ico, you will get all images that were encapsulated in the ico file in the form <icon name>-<number>.png. If you want to know the size of the image, or the number of images in a container file like ico you can use the identify tool (also part of the imagemagick package):

As you can see, the example ico file, although its name might suggest a single image of size 48x48, contains no less than 6 different sizes, of which one is even greater than 48x48, namely 128x128.

Alternatively, you can use icotool (from icoutils) to extract png images from ico container:

For extracting images from .icns container, you can use icns2png (provided by libicns):

Although packages that already ship with a .desktop file most certainly contain an icon or a set of icons, there is sometimes the case when a developer has not created a .desktop file, but may ship icons, nonetheless. So a good start is to look for icons in the source package. You can i.e. first filter for the extension with find and then use grep to filter further for certain buzzwords like the package name, "icon", "logo", etc, if there are quite a lot of images in the source package.

If the developers of an application do not include icons in their source packages, the next step would be to search on their web sites. Some projects, like i.e. tvbrowserAUR have an artwork/logo page where additional icons may be found. If a project is multi-platform, there may be the case that even if the linux/unix package does not come with an icon, the Windows package might provide one. If the project uses a Version control system like CVS/SVN/etc. and you have some experience with it, you also might consider browsing it for icons. If everything fails, the project might simply have no icon/logo yet.

The freedesktop.org standard specifies in which order and directories programs should look for icons:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Arronax is a graphical program to create and modify desktop entries for applications and locations. Install the arronaxAUR package to use it.

alacarte is a graphical menu editor for GNOME using the freedesktop.org menu specification. It also supports overriding desktop entries.

jddesktopentryeditAUR is a graphical program using Qt to edit desktop entries.

menulibreAUR is a graphical menu editor using GTK that provides modern features in a clean, easy-to-use interface.

libre-menu-editorAUR is a graphical program for editing desktop entries that aims to be feature-rich yet beginner-friendly.

It uses GTK with libadwaita and follows GNOME's interface guidelines, but is designed to work on any freedesktop.org compliant desktop environment.

gendesk started as an Arch Linux-specific tool for generating .desktop files by fetching the needed information directly from PKGBUILD files. Now it is a general tool that takes command-line arguments.

Icons can be automatically downloaded from openiconlibrary, if available. (The source for icons is configurable).

lsdesktopfAUR can list available .desktop files or search their contents.

It can also perform MIME-type-related searches. See XDG MIME Applications#lsdesktopf.

The fbrokendesktopAUR Bash script detects broken Exec values pointing to non-existent paths. Without any arguments it uses preset directories in the DskPath array. It shows only broken .desktop with full path and filename that is missing.

For system-wide .desktop files (e.g. those installed from a package), first copy the relevant .desktop file (e.g. from /usr/share/applications/) to $XDG_DATA_HOME/applications/ (e.g. ~/.local/share/applications/). This prevents your changes from being overwritten when the package gets updated during system upgrades. The local user-specific .desktop files should automatically take precedence over the system-wide files. Now you can modify the local user-specific .desktop file as needed.

Now, the file in your application launcher will stay the same as the one that is autostarted.

To set environment variables, in the .desktop file, edit the Exec= line to first use the env(1) command to set your variables. For example, with the original line commented out:

Also remove DBusActivatable=true (or set it to false) if present as it will cause the Exec line to be ignored.[1]

To change or add the command line arguments, edit the Exec= line to append the desired options. As an example, with the original line commented out:

Also remove DBusActivatable=true (or set it to false) if present as it will cause the Exec line to be ignored.[2]

The visibility of the desktop entry can be controlled in multiple ways. See the Desktop Entry Specification for more information. Add one of the following lines to your .desktop file:

**Examples:**

Example 1 (unknown):
```unknown
$ dex /usr/share/applications/firefox.desktop
```

Example 2 (unknown):
```unknown
KDE_SESSION_VERSION
```

Example 3 (unknown):
```unknown
/usr/share/applications
```

Example 4 (unknown):
```unknown
/usr/share/applications/
```

---

## GNOME/Flashback

**URL:** https://wiki.archlinux.org/title/GNOME_Flashback

**Contents:**
- Installation
- Starting
  - Graphical log-in
  - Manually
- Configuration
  - Customizing GNOME Panel
  - Alternative window manager
- Tips and tricks
  - Panel speed settings
  - Replace applications menu icon

GNOME Flashback (previously called GNOME fallback mode) is a shell for GNOME 3. The desktop layout and the underlying technology is similar to GNOME 2. It does not use 3D acceleration at all, so it is generally faster and less CPU intensive than GNOME Shell with llvmpipe.

GNOME Flashback can be installed from the gnome-flashback package. It is recommended to install its optional dependencies also to get a more complete desktop environment.

You can also install the following packages which provide some additional applets for the GNOME Panel:

It is recommended to install the gnome group, which contains applications required for the standard GNOME experience.

Choose GNOME Flashback (Metacity) from the menu in a display manager of choice.

Those who wish to use Compiz with GNOME Flashback should select GNOME Flashback (Compiz) instead.

After editing .xinitrc, GNOME Flashback can be launched with startx. See xinitrc for details.

GNOME Flashback shares most of its settings with GNOME. See GNOME#Configuration for more details.

You can use an alternative window manager with GNOME Flashback by creating a custom GNOME session with the following components:

where window-manager is the window manager you wish to use. See GNOME/Tips and tricks#Custom GNOME sessions.

Also see this article on running awesome as the window manager in GNOME.

To adjust the amount of time it takes for the panel to disappear or reappear when autohide is enabled, execute the following:

where panel is either top-panel or bottom-panel and time is a value in miliseconds, e.g. 300.

To set the speed at which panel animations occur, execute the following:

where panel is either top-panel or bottom-panel and value is either "'fast'", "'medium'" or "'slow'".

Replace /usr/share/icons/icon-theme/16x16/places/start-here.png with your own icon (where icon-theme is the name of your icon theme).

After making the change, restart GNOME Panel: gnome-panel --replace.

**Examples:**

Example 1 (unknown):
```unknown
export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
exec gnome-session --session=gnome-flashback-metacity
```

Example 2 (unknown):
```unknown
export XDG_CURRENT_DESKTOP=GNOME-Flashback:GNOME
exec gnome-session --session=gnome-flashback-compiz
```

Example 3 (unknown):
```unknown
RequiredComponents=gnome-flashback-init;gnome-flashback;gnome-panel;window-manager;gnome-settings-daemon;nautilus-classic;
```

Example 4 (unknown):
```unknown
RequiredComponents=gnome-flashback-init;gnome-flashback;gnome-panel;window-manager;gnome-settings-daemon;nautilus-classic;
```

---

## Hyprland

**URL:** https://wiki.archlinux.org/title/Hyprland

**Contents:**
- Installation
- Configuration
  - Keyboard
    - Keymap
    - Typematic delay and rate
    - Keyboard backlight
    - Media keys
  - Touchpad gestures
  - Display settings
    - Screen sharing

Hyprland is an independent tiling Wayland compositor written in C++. Noteworthy features of Hyprland include dynamic tiling, tabbed windows, a clean and readable C++ code-base, and a custom renderer that provides window animations, rounded corners, and Dual-Kawase Blur on transparent windows. General usage and configuration is thoroughly documented at Hyprland wiki.

Install the hyprland package.

As of #6608, Hyprland uses aquamarine as its own rendering backend library. Before that, it bundled its own version of wlroots, which closely followed wlroots-gitAUR.

Configuration is done through a single configuration file, hyprland.conf, though it supports splitting the configuration into multiple files and including them in hyprland.conf. The default file is /usr/share/hypr/hyprland.conf and, after logging in for the first time, ~/.config/hypr/hyprland.conf.

hyprland.conf includes directives to configure your devices (keyboards, mice, trackpads, monitors), as well as settings for animations, decorations, layout, etc. You can set key bindings, window rules, and execute commands (either once or each time) the configuration is reloaded.

The configuration is automatically reloaded each time you update the file. You can also use hyprctl reload for the same effect. For some settings (particularly input settings), you may have to restart your Hyprland session.

Settings can also be changed on the fly with hyprctl but they will not be saved.

By default Hyprland will use US Qwerty, you can configure it as follows:

See upstream's Wiki for all available options.

While Xorg users will be used to having this setting defined at the server level, on Wayland each compositor handles it on its own:

Using keyboard brightness controls in Hyprland is possible. Install brightnessctl then add the related binds (replace keyboard_brightness_* with SUPER, FX or XF86KbdBrightness depending on how your hardware exposes the keyboard backlight):

It is also possible to have on-screen notifications that fire when changes are made.

Using keyboard media controls in Hyprland is possible by making use of XF86Audio keysyms and an external application like pavucontrol or pamixer and playerctl:

It is also possible to have on-screen notifications that fire when changes are made.

Being a Wayland compositor, Hyprland has full support for touchpad gestures though they are disabled by default. To enable them, make the following edit:

See the upstream Wiki for all available options.

Being a wlroots-compatible compositor, Hyprland can utilize xdg-desktop-portal-wlr to enable screen capture in a range of applications by way of xdg-desktop-portal.

Hyprland also maintains xdg-desktop-portal-hyprland, which supports screen sharing (including region sharing and window sharing), global shortcuts, and has a graphical picker utility. Usage of the portal is further documented in the Hyprland wiki.

It is worth noting that xdg-desktop-portal-hyprland does not include a file picker, for which users can additionally install xdg-desktop-portal-gtk.

Hyprland will try to detect your screen resolution automatically and then select either 1x, 1.5x, or 2x screen scaling. [1] However, in some cases it will fail and default to a fail-safe, usually if there are multiple screens present or if you have a hybrid laptop. If everything on your screen is huge then you need to configure your default monitor and resolution.

First find your default monitor using hyprctl:

Then add your monitor to the configuration:

0x0 is a position offset used for multi screen setups and the final 1 is the screen scaling factor.

See the upstream Hyprland Monitors Wiki for more details.

There is the nwg-displays package, a GUI application for monitor arrangement, that supports Hyprland. It is part of the nwg-shell (but works standalone), see nwg-displays github for more details.

Install brightnessctl then add the following binds:

It is also possible to have on-screen notifications that fire when changes are made.

Universal Wayland Session Manager wraps the compositor and accordingly configured applications and daemons through systemd unit files, allowing you to control them with systemctl.

Hyprland can be started via a Display manager with uwsm by selecting hyprland (uwsm-managed).

You can start Hyprland with uwsm both in a getty via the following script in your login shell:

You can start Hyprland from a getty with the following command:

While launching from a display manager is not officially supported, users have reported success launching from GDM, SDDM, and others. The upstream wiki maintains a compatibility list with display managers. The hyprland package contains two desktop entries, and all Hyprland AUR packages will generate one automatically.

Both methods provide identical results, plus or minus a few environment variables and services.

Users can automatically login by using a display manager or adapting the method described in Xinit#Autostart X at login.

hyprctl is a command line utility that comes installed with Hyprland to communicate with the display server. It allows you to dispatch commands to the server (equivalent to commands in the configuration file, but with a slightly different syntax), set keywords, send queries and request information. See the full documentation.

Hyprland also exposes 2 UNIX Sockets for controlling and getting information about Hyprland via code or command-line utilities. These sockets broadcast events on focus change (windows, workspaces, monitors), creation of windows/workspace, and so on.

Both hyprctl and the IPC sockets can be effectively used in scripts to control Hyprland for complex tasks.

When starting applications it is important to use the correct type of dispatcher, using exec incorrectly can result in applications being started multiple times taking up system resources and in the worst cases, causing a race condition that can crash your system.

It is possible to set environment variables directly in hyprland.conf through the env keyword, which has a different syntax than the env UNIX command used by shells.

The differences are explained on the upstream Wiki.

The Hyprland development team are building an ecosystem of applications tailored to be specifically used with Hyprland, these tools will include dispatchers allowing for them to be controlled with hyprctl rather than relying on scripts.

Currently the ecosystem consists of:

Hyprpaper is a wallpaper utility, it can be installed with the hyprpaper package.

Hyprpicker is a utility to grab a colour from your desktop, it can be installed with the hyprpicker package.

Hypridle is an idle management daemon, it can be installed with the hypridle package.

Hyprlock is a screen lock manager, it can be installed with the hyprlock package.

Hyprcursor is a new format for handling screen cursors that offers many improvements over the traditional way, it can be installed with the hyprcursor package,

Cursor themes can be installed from the AUR, for example:

Instructions for porting existing themes to Hyprcursor are available on the upstream GitHub repository.

Hyprland's own implementation of XDG Desktop Portal. Compatible with other wlroots-based compositors, but provides extra functionality when used on Hyprland. Available through the xdg-desktop-portal-hyprland package.

Hyprpolkitagent is a polkit authentication daemon. It can be installed with the hyprpolkitagent package.

Hyprsunset is a small utility to provide a blue light filter for your system. It can be installed with the hyprsunset package.

Hyprsysteminfo is a system information fetching program like neofetchAUR or fastfetch. It can be installed with the hyprsysteminfoAUR AUR package.

Hyprland requires a wayland-compatible external application if graphical file management is desired. Using thunar as an example, we simply need to assign it a keybind as follows:

Hyprland requires a wayland-compatible external application to launch applications. Using wofi as an example, we simply need to assign it a keybind as follows:

Hyprland requires a wayland-compatible external idle management daemon. The most common setup is hypridle and hyprlock. You can lock your screen manually using a bind as follows:

Create the following file:

Hyprland has a built in dispatcher to handle DPMS requests however using it as a direct keybind is not recommended, doing so will result in you not being able to turn the screen back on and will require you to reboot.

Edit the file from above and change it to read:

Hyprland requires a wayland-compatible external application to display a status bar. Using waybar as an example, we simply need to call it as follows:

waybar has a built in, fully customisable module that supports Hyprland workspace switching natively.

See the waybar Wiki [2] for details.

Polkit authentication requires the use of an external authentication agent. Hyprland recommends using hyprpolkitagent but any should work.

Hyprland requires a wayland-compatible external application to manage desktop wallpapers. Using hyprpaper as an example, we simply need to call it as follows:

Additionally since hyprpaper requires a configuration file to start; make the file as follows:

Replace monitor with the monitor you would like the wallpaper to be set on, you can grab a list via hyprctl monitors.

Create the following script and make sure its executable:

Next create a new directory to store wallpapers, something like ~/.config/hypr/wallpapers should work fine, and populate it with any images you want.

Finally call the script when the specified bind is pressed:

On screen notifications for actions like brightness and volume changes are possible by using external notification daemons. This is a very complex topic and covering it completely is beyond the scope of this page. Rather, this section will focus on mako so go ahead and install it.

See Desktop notifications for further instructions and Desktop notifications#Standalone for a list of alternatives.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Mako is a lightweight notification daemon, you can read mako(5) for details. Its configuration file is ~/.config/mako/config, icons used for OSD are stored at ~/.config/mako/icons/ and should be in PNG format.

For the rest of this section all the images used by the scripts are available from this GitHub folder.

First create the following script:

Then add a new bind, or edit any existing one:

First create the following script:

Then add the following (or edit any existing binds):

First create the following script:

Then add the following (or edit any existing binds):

To run this script, you need a command-line JSON processor gojqAUR.

First create the following script:

Then add the following (or edit any existing binds):

Hyprland requires a wayland-compatible external application for power control. Using nwg-bar as an example, we simply need to bind it as follows:

Wayland clipboard behaviour deletes data when closing the application we copied it from. Other desktop environments work around this by using dedicated clipboard managers and on Hyprland there are multiple compatible choices. See the upstream Wiki for more information.

This section will cover cliphist as it supports copying images as well as text, start by adding the following:

Then create a bind to call the history in your chosen application launcher:

Now pressing Super+v will open up a wofi window with a clipboard history list.

To enable/disable devices (e.g. touchpad), first use:

to get the name of your device.

Put these lines of code into your configuration file (replace <device_name> with the name of your device queried above) to turn the device on/off:

To dynamically switch the device on/off use hyprctl:

You can also create a keybinding, e.g.:

Note: Prior to Hyprland v0.34(?), the following legacy syntax was used:

device:<device_name>:enabled

This older format has been removed. Also, earlier configuration files did not use a block-based device { name = <device_name> ... } structure, but a device:<device_name> { ... } structure.

In case you do not want to poison settings for other GTK-based DEs, you can use a separate dconf profile. For example:

Declare new global dconf profile:

Now you can use gsettings and it should not affect other desktop environments.

It is a widespread issue among NVIDIA users on Hyprland [3], [4] because of lack of support for explicit sync in Hyprland [5]. Recommended temporary fix is using X11 (XWayland) with the problematic apps by passing them --ozone-platform-hint=x11, or setting env = ELECTRON_OZONE_PLATFORM_HINT,x11 in ~/.config/hypr/hyprland.conf to force all electron apps to run using XWayland.

Jetbrains apps (Pycharm, Intellij) can have strange focus problems such as:

To mitigate the issue add this to hyprlands configuration file:

**Examples:**

Example 1 (unknown):
```unknown
seatd.service
```

Example 2 (unknown):
```unknown
hyprland.conf
```

Example 3 (unknown):
```unknown
/usr/share/hypr/hyprland.conf
```

Example 4 (unknown):
```unknown
~/.config/hypr/hyprland.conf
```

---

## Xcompmgr

**URL:** https://wiki.archlinux.org/title/Xcompmgr

**Contents:**
- Installation
- Configuration
  - Window transparency
- Tips and tricks
  - Start/Stop Xcompmgr on demand
  - Toggle Xcompmgr
- Troubleshooting
  - Background turns light gray briefly after logging in (e.g. in Openbox)
  - BadPicture request in awesome
  - Screen not updating in awesome after resolution change

Xcompmgr is a simple compositor capable of rendering drop shadows and, with the use of the transset utility, primitive window transparency. Designed solely as a proof-of-concept, Xcompmgr is a lightweight alternative to Compiz and similar composite managers.

Because it does not replace any existing window manager, it is an ideal solution for users of lightweight window managers, seeking a more elegant desktop.

Before installing Xcompmgr, make sure you have installed and correctly configured Xorg. To make sure the Composite extension is enabled for the X Server, run:

If there is no output, add the Composite option to the Extensions section of xorg.conf:

Xcompmgr can be installed with the package xcompmgr. For transparency also install the transset-dfAUR. See Xterm#Automatic transparency for an example.

To load xcompmgr, simply run:

To have it load at session start, add the following to xprofile:

Instead of -c you can experiment with the other switches to modify the drop-shadows or even enable fading. Below is a common example:

For a full list of options, run:

Although its practical use is limited, due to its slow performance, the transset-df utility can be used to set the transparency of individual windows.

To set the transparency of a program window, make sure the desired program is already running, then execute:

where opacity is a number between 0 and 1, 0 being transparent and 1 being opaque.

Once execution, the mouse cursor will transform to a cross-hair. Click a window and its transparency will change to the value specified. For example, transset-df 0.25 will set the target window to 25% opacity (75% transparency).

This script allows easy (re)starting and stopping of the compositing manager.

For ease of use, you can bind this script to a hot-key using, for example, Xbindkeys. This allows for fast restart or temporary composition removal if needed without interrupting other work.

Assign the following script to any hot-key:

This is fixed by installing hsetroot and setting the background color by executing hsetroot -solid "#000000" (just type the code of the color you want instead of #000000) before xcompmgr. Alternatively, if xcompmgr is called prior to exec in ~/.xinitrc, you can change xcompmgr & to (sleep 1 && xcompmgr) & which will fork a subshell and allow xcompmgr to execute after your window manager has already started.

If you get the following error in awesome:

just install feh and restart awesome.

When using an external monitor, you may encounter problems when automatically changing display resolutions: a part of the screen becomes "stuck" and no longer updates itself. This problem occurs because of the initial resolution change (happening before Xcompmgr starts) as well as awesome setting the background via feh.

To fix it, you need to install hsetroot and put the following line in .xinitrc, just before xcompmgr:

(you can replace #000066 with your color of choice).

**Examples:**

Example 1 (unknown):
```unknown
$ xdpyinfo | grep Composite
```

Example 2 (unknown):
```unknown
/etc/X11/xorg.conf
```

Example 3 (unknown):
```unknown
Section "Extensions"
        Option  "Composite" "true"
EndSection
```

Example 4 (unknown):
```unknown
$ xcompmgr -c
```

---

## xdg-menu

**URL:** https://wiki.archlinux.org/title/Xdg-menu

**Contents:**
- Installation
- Menu hierarchy
- Configuration
  - Adding desktop entries from other directories
- Usage
  - xdg_menu
  - update-menus
- Examples
  - Awesome
    - With xdg_menu

xdg-menu is a tool that generates XDG Desktop Menus for the following window managers:

KDE, GNOME, Xfce and Enlightenment are already XDG compatible.

Install the archlinux-xdg-menu package.

xdg_menu relies on three sets of information to generate menus: a root menu or in other words an XML menu template generally passed on the command line, information cached when it was last run, and a series of configuration files.

Other configuration file directories can be found under /usr/share. In most cases you will not need to touch these. However if you want to change how your menu is layed out you can alter the menu template for minor changes. Major changes require tweaking the actual xdg_menu perl script. If you find that applications do not appear or that they are called strange things, then you will need to look at the .desktop file in /usr/share/applications. Check the desktop entry specification.

By default, the Xdg-menu will be populated with applications which install their desktop entries to /usr/share/applications. To add applications to the menu which install their desktop entry to a user folder such as ~/.local/share/applications, edit the /etc/xdg/menus/arch-applications.menu file and add an <AppDir> tag for the relevant directory, see below:

update-menus updates WM's menus from XDG data and can be configured to do it automaticaly.

This is a script wrapper around xdg_menu that relies on /etc/update-menus.conf

To use it, you need to install the archlinux-xdg-menu package (xdg_menu)

In /etc/update-menus.conf, you have to select from a list of window managers for which the menu should be generated. Comments with # are allowed.

All generated menus are placed in /var/cache/xdg-menu/. See wm-specific #Examples section of this page to get more information.

Then, edit your rc.lua as shown below.

Change your menu file to include the generated menu.

For example, add this line:

For example, add this line:

And manually add it into your menu.xml. For example, put xdg-menu.xml into menu.xml and add:

Using xdg_open as a pipe menu gives you the added benefit of having a menu that automatically updates when you install new applications.

Add the following somewhere inside your menu.xml between your root menu tags:

A very basic example:

For example, add following to root-menu:

And add it into twmrc manually. In the case of twm derivatives with m4 preprocessing such as vtwm or ctwm it can be included by adding:

Into your WindowMaker menu file.

You can also use the WPrefs "Application Menu Definitions", and add the xdg command as a parameter in a "Generated Submenu" object.

And add it into the root menu:

Change your menu file to include the generated menu.

For example, add this line:

For example, add this line:

**Examples:**

Example 1 (unknown):
```unknown
/etc/xdg/menus
```

Example 2 (unknown):
```unknown
~/.xdg_menu_cache
```

Example 3 (unknown):
```unknown
/usr/share/applications
```

Example 4 (unknown):
```unknown
/usr/share/applications
```

---

## COSMIC

**URL:** https://wiki.archlinux.org/title/COSMIC

**Contents:**
- Installation
  - Individual components coming as dependencies of cosmic-session
  - Independent components
  - Network shares in COSMIC Files
- Starting
  - Using Cosmic Greeter
- Configuration
- See also

COSMIC is a desktop environment developed in the Rust programming language, using the iced cross platform GUI library for Rust, and Smithay as building blocks for its compositor, cosmic-comp. Cosmic-comp is comparable to smithay's own anvil compositor demonstration, just like the Wayland project uses Weston as demo compositor. Its first release is called Epoch.

COSMIC can be installed via cosmic-session or the cosmic group.

COSMIC comprises a compositor, library, and applets, which may be installed as parts. cosmic-comp, cosmic-applets, cosmic-app-library, cosmic-bg, cosmic-icon-theme, cosmic-launcher, cosmic-notifications, on screen display to overlay messages with cosmic-osd, a dock and panel with cosmic-panel, cosmic-settings, and others.

An editor, cosmic-text-editor, a file manager cosmic-files, a terminal, cosmic-terminal, a multimedia player cosmic-player, and wallpapers, cosmic-wallpapers are provided.

To connect to network shares in COSMIC Files, the relevant GVFS package needs to be installed:

COSMIC doesn't provide a secrets store/keyring, so to remember passwords, install a secrets storage component such as gnome-keyring. See also GNOME/Keyring.

The easiest way to start COSMIC is through a display manager, where it will show up as an additional option after installation, alongside GNOME, KDE Plasma, etc.

To start COSMIC directly from the console, run:

COSMIC ships cosmic-greeter, a display manager based on greetd. To use it, enable cosmic-greeter.service.

The panel can be used to configure besides using the settings applet, examples of applets are provided.

**Examples:**

Example 1 (unknown):
```unknown
CARGO_TARGET_DIR
```

Example 2 (unknown):
```unknown
MOLD_JOBS=1 CARGO_TARGET_DIR=/tmp/mytarget
```

Example 3 (unknown):
```unknown
$ start-cosmic
```

Example 4 (unknown):
```unknown
cosmic-greeter.service
```

---

## Cagebreak

**URL:** https://wiki.archlinux.org/title/Cagebreak

**Contents:**
- Installation
  - Optional dependencies
- Configuration
- Usage
  - Getting started
  - Keyboard layout
  - Interaction through socket
- See also

Cagebreak is a manually tiling compositor for Wayland, based on cage and inspired by ratpoison, which is easily controlled through the keyboard and a UNIX domain socket.

Install cagebreakAUR or cagebreak-binAUR. Alternatively, download the release tarball or clone the repository.

The general configuration for cagebreak is located in $XDG_CONFIG_PATH/cagebreak/config. This defaults to ~/.config/cagebreak/config.

Read cagebreak-config(5) for detailed information. Note that you can also add configuration by using #Interaction through socket.

An example configuration file may be found on GitHub.

Start cagebreak like any other binary.

The following is an example of how to install and use cagebreak with the configuration file provided on GitHub.

Set the environment variable XKB_DEFAULT_LAYOUT to the desired keyboard layout. See cagebreak(1) § ENVIRONMENT for further information.

If cagebreak is invoked with the -e option, cagebreak opens a UNIX domain socket through which interaction with the compositor is possible at run-time. The path to this socket is stored in the CAGEBREAK_SOCKET environment variable. For example, openbsd-netcat may be invoked with:

to send cagebreak any configuration while it is running. The syntax is identical to the syntax of the configuration file.

Add the --bs (bad security) option, if you want to see the names of views over the socket (please consider the security implications on your local system).

**Examples:**

Example 1 (unknown):
```unknown
$XDG_CONFIG_PATH/cagebreak/config
```

Example 2 (unknown):
```unknown
~/.config/cagebreak/config
```

Example 3 (unknown):
```unknown
$XDG_CONFIG_PATH/cagebreak/config
```

Example 4 (unknown):
```unknown
XKB_DEFAULT_LAYOUT=us cagebreak
```

---

## Weston

**URL:** https://wiki.archlinux.org/title/Weston

**Contents:**
- Installation
- Usage
  - Demo applications
  - Shortcuts
- Configuration
  - Monitors
  - Xwayland
  - High DPI displays
  - Shell font
- Tips and tricks

Weston is a Wayland compositor designed for correctness, reliability, predictability, and performance.

Install the weston package.

To launch Weston natively (from a TTY) or to run Weston inside a running X session:

See weston(1) for details and configuration flags.

Then within Weston, you can run the demos. To launch a terminal emulator:

To move flowers around the screen:

Following is an example configuration file. See weston.ini(5) for more.

Weston's outputs differ slightly from those of xorg.conf Monitors:

card0 is the unused built-in video adapter. The add-on adapter card1 is cabled to one HDMI and one DVI monitor, so the output names are HDMI-A-1 and DVI-I-1.

See Wayland#Xwayland for details and an overview of available packages.

Set the following to activate the use of Xwayland:

For Retina or HiDPI displays, use:

Weston uses the default sans-serif font for window title bars, clocks, etc. See Font configuration#Set default or fallback fonts for instructions on how to change this font.

Weston has built-in screencast recording which can be started and stopped by pressing the Super+r key combination. Screencasts are saved to the file capture.wcap in the current working directory of Weston. The WCAP format is a lossless video format specific to Weston, which only records the difference in frames. To be able to play the recorded screencast, the WCAP file will need to be converted to a format which a media player can understand. First, convert the capture to the YUV pixel format:

The YUV file can then be transcoded to other formats using FFmpeg or x264 (see x264 -h for more).

To switch windows with Super+Space instead of Super+Tab change KEY_TAB to KEY_SPACE in desktop-shell/shell.c and recompile weston.

Touch display mapping can be achieved through the use of udev rules. Just like the WL_SEAT or ID_SEAT device environment variable binds the device to a specified seat, the WL_OUTPUT variable may be used to bind the device to the appropriate output. This variable should match a monitor name. See #Monitors for an explanation of the monitor naming convention.

**Examples:**

Example 1 (unknown):
```unknown
$ weston-terminal
```

Example 2 (unknown):
```unknown
$ weston-flower
```

Example 3 (unknown):
```unknown
$ weston-image image1.jpg image2.jpg...
```

Example 4 (unknown):
```unknown
Ctrl+Alt+Backspace
```

---
