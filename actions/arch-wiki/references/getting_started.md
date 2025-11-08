# Arch-Wiki - Getting Started

**Pages:** 77

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Core

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## Disk quota

**URL:** https://wiki.archlinux.org/title/Disk_quota

**Contents:**
- Installation
- Configuration
  - Set up the filesystem
  - Create quota index
- Usage
  - Enable quota for user/group
  - Specify a grace period
  - Reports
  - Copy quota settings
    - To one or several users

This article covers the installation and setup of disk quota.

Install the quota-tools package.

Edit fstab to enable the quota mount option(s) on selected file systems, e.g.:

To additionally enable the group quota mount option:

If supported by the kernel and file system it is recommended to use journaled quota instead:

Append grpjquota=aquota.group to enable group quota.

Remount the partition to apply the change:

To create the quota index for /home:

Append the -g parameter to also create a group index.

To enable disk quotas for the desired file system:

To disable disk quotas for the file system:

Quotas are configured using edquota (as the root user) that will be opened in the default configured text editor:

Consider the following configuration for ftpuser1:

In this case if ftpuser1 uses over 976MB of space a warning will be issued. If the hard limit of 1GB has been reached the user will be unable to write any more data.

See #Specify a grace period to give users a specific amount of time to reduce storage usage when they hit their soft limit.

To give current users some time to reduce their file usage, a grace period can be configured. This specifies the allowed time a user/group can exceed their soft limit and while under their hard limit:

The grace period can be set in seconds, minutes, hours, days, weeks or months.

Shows all configured quotas:

Shows quotas on a specific partition:

Show quotas that apply to a user/user group:

To copy quota settings from user1 to user2:

To copy quota settings to several other users, append user3 user4 ...

To copy quota settings from group1 to group2:

The idea is to modify the quota settings for one user and copy the setting to all other users. Set the quota for user1 and apply the quota to users with a UID greater than 999:

The command warnquota can be used to warn the users about their quota. Configuration is available in /etc/warnquota.conf.

The command quotastats can be used to give more information about the current quota usage:

**Examples:**

Example 1 (unknown):
```unknown
/dev/sda3 /home ext4 defaults,usrquota 0 2
```

Example 2 (unknown):
```unknown
/dev/sda3 /home ext4 defaults,usrquota,grpquota 0 2
```

Example 3 (unknown):
```unknown
/dev/sda3 /home ext4 defaults,usrjquota=aquota.user,jqfmt=vfsv1 0 2
```

Example 4 (unknown):
```unknown
grpjquota=aquota.group
```

---

## 2bwm

**URL:** https://wiki.archlinux.org/title/2bwm

**Contents:**
- Installation
- Starting
- Using 2bwm
  - General commands
  - Window controls
  - Move, resize and teleport a window
  - Workspaces
  - Mouse controls
- Tips and tricks
  - Get the current workspace number using a script

Install the 2bwmAUR package. Although the installation process can be automatic, if directly building from the AUR, it is highly recommended to read and edit the config.h file in the source directory.

After the launch of 2bwm, a mouse cursor, a background, and a terminal will be the only thing on the screen (as specified in the .xinitrc). To open a terminal, using the default configuration, hit Super+Enter. Use the terminal as desired, for example to start a program with program_name &, however it is easier and more convenient to use a menu to launch programs, for instance dmenu or 9menuAUR.

Using the Super key combined with one of the key below on a specific focused window:

Using the Super key combined with one of the key below on a specific focused window:

By holding the Super Key, the mouse buttons act as follows:

Note that all functions activated from the keyboard work on the currently focused window regardless of the position of the mouse cursor. Of course, changing workspaces has nothing to do with the focused window.

You may change the keyboard mappings from config.h.

The following command yields the current workspace:

A simple trick to remember the meaning of the outer border colours would be by setting, for example, "fixed" to blue, "unkillable" to red, and "fixed + unkillable" to purple. The mix of blue and red create purple!

Setting borders[0] to a negative number will make the outer border turn into a square located in the top-left corner of the full-border. The colours set for the outer borders now stick to the square.

**Examples:**

Example 1 (unknown):
```unknown
Super+Enter
```

Example 2 (unknown):
```unknown
program_name &
```

Example 3 (unknown):
```unknown
Super+Ctrl+q
```

Example 4 (unknown):
```unknown
Super+Ctrl+r
```

---

## kernel-install

**URL:** https://wiki.archlinux.org/title/Kernel-install

**Contents:**
- Installation
- Configuration
  - Main configuration
  - Kernel command line
  - Plugins
  - Unified kernel images
- Usage
  - Manually
  - Automatically

kernel-install(8) is a flexible utility designed to streamline the installation and administration of Linux kernel images on a system. It features a plugin system, allowing for seamless integration with other utilities. These plugins define a range of actions and configurations required during the installation and management of Linux kernel images. Examples of such tasks include configuring boot loader entries, generating Unified kernel images (UKI), or facilitating kernel signing for Secure Boot compliance.

kernel-install is part of and packaged with systemd. The systemd-ukify optional dependency is also needed for unified kernel images unless a different UKI generator is specified (see #Main configuration).

The main configuration file is /etc/kernel/install.conf. Use it to configure the layout you want to use, i.e. bls for traditional split kernel and initramfs images, or uki for Unified kernel images:

Kernel parameters must be set in /etc/kernel/cmdline. They will either be embedded in the UKI, or added to the boot loader configuration, according to the layout used. If /etc/kernel/cmdline doesn't exist, kernel install will use the parameters in /usr/lib/kernel/cmdline or /proc/cmdline, not setting the kernel parameters in /etc/kernel/cmdline could result in kernel-install using the parameters of the current running kernel.

To list active plugins used by kernel-install when installing, upgrading, or removing a kernel image, you can use the inspect argument:

Available plugins are found under /usr/lib/kernel/install.d/:

Similarly named files in /etc/kernel/install.d/ will override the default ones.

For example, to disable the default sbctl plugin (which automatically signs new UKIs for Secure Boot):

You can also write your own kernel-install plugins, and place them in /etc/kernel/install.d/.

See Unified kernel image#kernel-install

To manually install a kernel from /usr/lib/modules, use the following add command:

To remove a kernel manually, use the remove command:

To trigger kernel-install and all active plugins automatically when a kernel package is installed or updated, you can install pacman-hook-kernel-installAUR.

To revert, simply delete the symlinks created above.

**Examples:**

Example 1 (unknown):
```unknown
kernel-install
```

Example 2 (unknown):
```unknown
/etc/kernel/install.conf
```

Example 3 (unknown):
```unknown
/etc/kernel/install.conf
```

Example 4 (unknown):
```unknown
initrd_generator=
```

---

## Laptop/Acer

**URL:** https://wiki.archlinux.org/title/Laptop/Acer

**Contents:**
- Model list
  - Aspire
  - AspireOne
  - Travelmate
  - Nitro
  - Predator
  - Swift
  - Enduro
- Troubleshooting
  - Flaky Secure Boot

Some models have a peculiar Secure Boot implementation which requires the following workaround to boot successfully the installation medium:

You may have to repeat these steps every firmware update.

Commonly, once a new Linux entry has been added to the EFI partition, trying to access Acer UEFI instead results in being permanently stuck on the loading screen.

This is because the Acer BIOS requires all .efi files to be marked as trusted, even if Secure Boot is disabled. Therefore, you must first remove them from the bootable entries to regain access to the BIOS, then manually mark these files as being safe.

The exact process will depend on your installation. For example:

At that point, both the Linux boot loader and the Acer BIOS should be accessible without issues.

This article or section is a candidate for moving to Acer Aspire 3 A315-56.

The firmware has a bug where you cannot see the internal SATA storage after first booting up. At boot, the boot loader can see the internal storage but the initial ramdisk is unable to see it due to this bug.

The only known solution to this is suspending and waking it up.

Add an early custom hook to put the laptop to sleep before the step to mount the filesystems:

This custom hook will reset the RTC alarm clock and set an alarm 2 seconds into the future for device wake-up, so you do not have to manually wake-up the laptop.

Add it the mkinitcpio HOOKS:

Finally regenerate the initramfs.

It is therefore highly recommended to issue an ATA SECURITY FREEZE LOCK command immediately after waking up, add add_binary hdparm to the build() function of the install hook and place the following commands at the end of the above run_hook() function of the runtime hook:

Linux does not support Optane with RAID NVMe mode which is default on some devices. The workaround is to swich NVMe mode to AHCI.

One can switch the mode on the Main tab of BIOS setup. This option is hidden by default and unavailable until Supervisor password set.

To set Supervisor password:

To change NVMe mode (might not be possible until Supervisor password set):

If your laptop uses predator sense app v4 or newer on windows, but mode key and fan speed monitoring are not working on linux, try acer_wmi.predator_v4=1 kernel module parameter to enable these features. And you can change mode key's behavior (toggling turbo mode or rotating each mode) using acer_wmi.cycle_gaming_thermal_profile.

**Examples:**

Example 1 (unknown):
```unknown
options snd-hda-intel model=laptop
```

Example 2 (unknown):
```unknown
/etc/modprobe.d/sound.conf
```

Example 3 (unknown):
```unknown
ln -sf /dev/sr0 /dev/archiso
```

Example 4 (unknown):
```unknown
rcutree.rcu_idle_gp_delay=1 acpi_osi=! acpi_osi="Windows 2009"
```

---

## Network configuration/Wireless

**URL:** https://wiki.archlinux.org/title/Network_configuration/Wireless

**Contents:**
- Device driver
  - Check the driver status
  - Installing driver/firmware
- Utilities
  - iw and wireless_tools comparison
- iw
  - Get the name of the interface
  - Get the status of the interface
  - Activate the interface
  - Discover access points

The main article on network configuration is Network configuration.

Configuring wireless is a two-part process; the first part is to identify and ensure the correct driver for your wireless device is installed (they are available on the installation media, but often have to be installed explicitly), and to configure the interface. The second is choosing a method of managing wireless connections. This article covers both parts, and provides additional links to wireless management tools.

The #iw section describes how to manually manage your wireless network interface / your wireless LANs using iw. The Network configuration#Network managers section describes several programs that can be used to automatically manage your wireless interface, some of which include a GUI and all of which include support for network profiles (useful when frequently switching wireless networks, like with laptops).

The default Arch Linux kernel is modular, meaning many of the drivers for machine hardware reside on the hard drive and are available as modules. At boot, udev takes an inventory of your hardware and loads appropriate modules (drivers) for your corresponding hardware, which will in turn allow creation of a network interface.

Some wireless chipsets also require firmware, in addition to a corresponding driver. Many firmware images are provided by the linux-firmware package; however, proprietary firmware images are not included and have to be installed separately. This is described in #Installing driver/firmware.

To check if the driver for your card has been loaded, check the output of the lspci -k or lsusb -v command, depending on if the card is connected by PCIe or USB. You should see that some kernel driver is in use, for example:

Also check the output of the ip link command to see if a wireless interface was created; usually the naming of the wireless network interfaces starts with the letters "wl", e.g. wlan0 or wlp2s0. Then bring the interface up with:

For example, assuming the interface is wlan0, this is ip link set wlan0 up.

Check kernel messages for firmware being loaded:

If there is no relevant output, check the messages for the full output for the module you identified earlier (iwlwifi in this example) to identify the relevant message or further issues:

If the kernel module is successfully loaded and the interface is up, you can skip the next section.

Check the following lists to discover if your card is supported:

Note that some vendors ship products that may contain different chip sets, even if the product identifier is the same. Only the USB ID (for USB devices) or PCI ID (for PCIe devices) is authoritative.

If your wireless card is listed above, follow the #Troubleshooting drivers and firmware subsection of this page, which contains information about installing drivers and firmware of some specific wireless cards. Then check the driver status again.

If your wireless card is not listed above, it is likely supported only under Windows (some Broadcom, 3com, etc). For these, you can try to use ndiswrapper.

Just like other network interfaces, the wireless ones are controlled with ip from the iproute2 package.

Managing a wireless connection can be accomplished using network manager which will use wpa_supplicant or iwd for wireless authentication, or using wpa_supplicant or iwd directly. For lower level configuring, or if you are using a legacy driver or a legacy authentication method, there are iw and the deprecated wireless_tools.

The table below gives an overview of comparable commands for iw and wireless_tools. See Replacing iwconfig with iw for more examples.

Examples in this section assume that your wireless device interface is interface and that you are connecting to your_essid Wi-Fi access point. Replace both accordingly.

To get the name of your wireless interface, do:

The name of the interface will be output after the word "Interface". For example, it is commonly wlan0.

To check link status, use the following command.

You can get statistic information, such as the amount of tx/rx bytes, signal strength etc., with the following command:

Some cards require that the kernel interface be activated before you can use iw or wireless_tools:

To verify that the interface is up, inspect the output of the following command:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

To see what access points are available:

The important points to check:

You might need to set the proper operating mode of the wireless card. More specifically, if you are going to connect an ad-hoc network, you need to set the operating mode to ibss:

Depending on the encryption, you need to associate your wireless device with the access point to use and pass the encryption key:

Regardless of the method used, you can check if you have associated successfully:

This article or section needs expansion.

There are mainly two options for Wi-Fi authentication on Linux: wpa_supplicant and iwd.

WPA2 Personal, a.k.a. WPA2-PSK, is a mode of Wi-Fi Protected Access.

You can authenticate to WPA2 Personal networks using wpa_supplicant or iwd, or connect using a network manager. If you only authenticated to the network, then to have a fully functional connection, you will still need to assign the IP address(es) and routes either manually or using a DHCP client.

WPA2 Enterprise is a mode of Wi-Fi Protected Access. It provides better security and key management than WPA2 Personal, and supports other enterprise-type functionality, such as VLANs and NAP. However, it requires an external authentication server, called RADIUS server, to handle the authentication of users. This is in contrast to Personal mode which does not require anything beyond the wireless router or access points (APs), and uses a single passphrase or password for all users.

The Enterprise mode enables users to log onto the Wi-Fi network with a username and password and/or a digital certificate. Since each user has a dynamic and unique encryption key, it also helps to prevent user-to-user snooping on the wireless network, and improves encryption strength.

This section describes the configuration of network clients to connect to a wireless access point with WPA2 Enterprise mode. See Software access point#RADIUS for information on setting up an access point itself.

For a comparison of protocols, see the following table.

WPA2-Enterprise wireless networks demanding MSCHAPv2 type-2 authentication with PEAP sometimes require pptpclient in addition to the stock ppp package. netctl seems to work out of the box without ppp-mppe, however. In either case, usage of MSCHAPv2 is discouraged as it is highly vulnerable, although using another method is usually not an option.

eduroam is an international roaming service for users in research, higher education and further education, based on WPA2 Enterprise.

WPA3 Personal, a.k.a. WPA3-SAE, is a mode of Wi-Fi Protected Access.

Both wpa_supplicant and iwd support WPA3 Personal.

WPA3 Enterprise is a mode of Wi-Fi Protected Access.

wpa_supplicant (since version 2:2.10-8) supports WPA3 Enterprise. See FS#65314.

The regulatory domain, or "regdomain", is used to reconfigure wireless drivers to make sure that wireless hardware usage complies with local laws set by the FCC, ETSI and other organizations. Regdomains use ISO 3166-1 alpha-2 country codes. For example, the regdomain of the United States would be "US", China would be "CN", etc.

Regdomains affect the availability of wireless channels. In the 2.4GHz band, the allowed channels are 1-11 for the US, 1-14 for Japan, and 1-13 for most of the rest of the world. In the 5GHz band, the rules for allowed channels are much more complex. In either case, consult this list of WLAN channels for more detailed information.

Regdomains also affect the limit on the effective isotropic radiated power (EIRP) from wireless devices. This is derived from transmit power/"tx power", and is measured in dBm/mBm (1dBm=100mBm) or mW (log scale). In the 2.4GHz band, the maximum is 30dBm in the US and Canada, 20dBm in most of Europe, and 20dBm-30dBm for the rest of the world. In the 5GHz band, maximums are usually lower. Consult the wireless-regdb for more detailed information (EIRP dBm values are in the second set of brackets for each line).

Misconfiguring the regdomain can be useful - for example, by allowing use of an unused channel when other channels are crowded, or by allowing an increase in tx power to widen transmitter range. However, this is not recommended as it could break local laws and cause interference with other radio devices.

The kernel loads the database directly when wireless-regdb is installed. For direct loading, the kernel should, for security's sake, be configured with CONFIG_CFG80211_USE_KERNEL_REGDB_KEYS set to yes to allow for cryptographic verification of the database. This is true of the stock Arch kernel, but if you are using an alternate kernel, or compiling your own, you should verify this. More information is available at this guide[dead link 2024-07-30—domain name not resolved].

To configure the regdomain, install wireless-regdb and reboot, then edit /etc/conf.d/wireless-regdom and uncomment the appropriate domain.

The current regdomain can be temporarily set to the United States with:

However, setting the regdomain may not alter your settings. Some devices have a regdomain set in firmware/EEPROM, which dictates the limits of the device, meaning that setting regdomain in software can only increase restrictions, not decrease them. For example, a CN device could be set in software to the US regdomain, but because CN has an EIRP maximum of 20dBm, the device will not be able to transmit at the US maximum of 30dBm.

For example, to see if the regdomain is being set in firmware for an Atheros device:

For other chipsets, it may help to search for "EEPROM", "regdomain", or simply the name of the device driver.

To see if your regdomain change has been successful, and to query the number of available channels and their allowed transmit power:

wpa_supplicant can also use a regdomain in the country= line of /etc/wpa_supplicant/wpa_supplicant.conf.

It is also possible to configure the cfg80211 kernel module to use a specific regdomain by adding, for example, options cfg80211 ieee80211_regdom=JP as module options. The module option is inherited from the old regulatory implementation and in modern kernels act as a userspace regulatory hint as if it came through nl80211 through utilities like iw and wpa_supplicant.

Many laptops have a hardware button (or switch) to turn off the wireless card; however, the card can also be blocked by the kernel. This can be handled by rfkill(8). To show the current status:

If the card is hard-blocked, use the hardware button (switch) to unblock it. If the card is not hard-blocked but soft-blocked, use the following command:

Hardware buttons to toggle wireless cards are handled by a vendor specific kernel module. Frequently, these are WMI modules. Particularly for very new hardware models, it happens that the model is not fully supported in the latest stable kernel yet. In this case, it often helps to search the kernel bug tracker for information and report the model to the maintainer of the respective vendor kernel module, if it has not happened already.

See Power saving#Network interfaces.

This section contains general troubleshooting tips, not strictly related to problems with drivers or firmware. For such topics, see next section #Troubleshooting drivers and firmware.

If you have problematic hardware and need internet access to, for example, download some software or get help in forums, you can make use of Android's built-in feature for internet sharing via USB cable. See Android tethering#USB tethering for more information.

A good first measure to troubleshoot is to analyze the system's logfiles first. In order not to manually parse through them all, it can help to open a second terminal/console window and watch the kernels messages with

while performing the action, e.g. the wireless association attempt.

When using a tool for network management, the same can be done for systemd with

Frequently, a wireless error is accompanied by a deauthentication with a particular reason code, for example:

Looking up the reason code might give a first hint. Maybe it also helps you to look at the control message flowchart, the journal messages will follow it.

The individual tools used in this article further provide options for more detailed debugging output, which can be used in a second step of the analysis, if required.

This article or section is out of date.

Before changing the channel to auto, make sure your wireless interface is down. After it has successfully changed it, you can bring the interface up again and continue from there.

If you are on a public wireless network that may have a captive portal, make sure to query an HTTP page (not an HTTPS page) from your web browser, as some captive portals only redirect HTTP. If this is not the issue, check if you can resolve domain names, it may be necessary to use the DNS server advertised via DHCP.

Wireless hardware disables RTS and fragmentation by default. These are two different methods of increasing throughput at the expense of bandwidth (i.e. reliability at the expense of speed). These are useful in environments with wireless noise or many adjacent access points, which may create interference leading to timeouts or failing connections.

Packet fragmentation improves throughput by splitting up packets with size exceeding the fragmentation threshold. The maximum value (2346) effectively disables fragmentation since no packet can exceed it. The minimum value (256) maximizes throughput, but may carry a significant bandwidth cost.

RTS improves throughput by performing a handshake with the access point before transmitting packets with size exceeding the RTS threshold. The maximum threshold (2347) effectively disables RTS since no packet can exceed it. The minimum threshold (0) enables RTS for all packets, which is probably excessive for most situations.

If your journal says wlan0: deauthenticating from MAC by local choice (reason=3) and you lose your Wi-Fi connection, it is likely that you have a bit too aggressive power-saving on your Wi-Fi card. Try disabling the wireless card's power saving features (specify off instead of on).

If your card does not support enabling/disabling power save mode, check the BIOS for power management options. Disabling PCI-Express power management in the BIOS of a Lenovo W520 resolved this issue.

If you are experiencing frequent disconnections and your journal shows messages such as

ieee80211 phy0: wlan0: No probe response from AP xx:xx:xx:xx:xx:xx after 500ms, disconnecting

try changing the channel bandwidth to 20MHz through your router's settings page.

On some laptop models with hardware rfkill switches (e.g., Thinkpad X200 series), due to wear or bad design, the switch (or its connection to the mainboard) might become loose over time resulting in seemingly random hardblocks/disconnects when you accidentally touch the switch or move the laptop. There is no software solution to this, unless your switch is electrical and the BIOS offers the option to disable the switch. If your switch is mechanical (and most are), there are lots of possible solutions, most of which aim to disable the switch: Soldering the contact point on the mainboard or Wi-Fi card, gluing or blocking the switch, using a screw nut to tighten the switch or removing it altogether.

Another cause for frequent disconnects or a complete failure to connect may also be a sub-standard router, incomplete settings of the router, interference by other wireless devices or low quality signal.

To troubleshoot, first try to connect to the router with no authentication and by getting closer to it. If it does not work, reboot the router and try with another device first.

If that works, enable WPA/WPA2 again but choose fixed and/or limited router settings. For example:

On some wireless network adapters (e.g. Qualcomm Atheros AR9485), random disconnects can happen with a DMA error:

A possible workaround is to disable the Intel IOMMU driver (DMA), adding intel_iommu=off to the kernel parameters [4].

If you are using a device with iwlwifi and iwlmvm for wireless connectivity, and your Wi-Fi card appears to disappear when on battery power (perhaps after a reboot or resuming from suspend), this can be fixed by configuring power saving settings in iwlmvm.

Create the file /etc/modprobe.d/iwlmvm.conf if it does not exist already, then add the following line to it:

A power_scheme of 1 sets iwlmvm to "Always Active." Available options are:

This fix was discovered at [5].

If your device undergoes long periods of inactivity (e.g. a file server), the disconnection may be due to power saving, which will block incoming traffic and prevent connections. Try disabling power saving for the interface:

You can create a udev rule to do this on boot, see Power management#Network interfaces.

If you notice occasional interruptions when connected to a mesh network (e.g., Wi-Fi 6) and notice a message such as:

You are experiencing roaming issues. Depending on your mean of connection and the issue at hand, one could:

If the computer's Wi-Fi channels do not match those of the user's country, some in-range Wi-Fi networks might be invisible because they use wireless channels that are not allowed by default. The solution is to configure the regulatory domain correctly; see #Respecting the regulatory domain.

This section covers methods and procedures for installing kernel modules and firmware for specific chipsets, that differ from generic method.

See Kernel modules for general information on operations with modules.

Some chipsets require additional firmware: linux-firmware-mediatek

Unified driver for Ralink chipsets (it replaces rt2500, rt61, rt73, etc). This driver has been in the Linux kernel since 2.6.24, you only need to load the right module for the chip: rt2400pci, rt2500pci, rt2500usb, rt61pci or rt73usb which will autoload the respective rt2x00 modules too.

A list of devices supported by the modules is available at the project's homepage.

For devices which use the rt3090 chipset, it should be possible to use the rt2800pci driver; however, it does not work with this chipset very well (e.g. sometimes it is not possible to use higher rate than 2Mb/s).

The rt3290 chipset is recognised by the kernel rt2800pci module. However, some users experience problems and reverting to a patched Ralink driver seems to be beneficial in these cases.

New chipset as of 2012. It may require proprietary drivers from Ralink. Different manufacturers use it; see the Belkin N750 DB wireless usb adapter forums thread.

New chipset as of 2014, released under their new commercial name MediaTek. It is an AC1200 or AC1300 chipset. Manufacturer provides drivers for Linux on their support page. As of kernel 5.5 it should be supported by the included mt76 driver.

DFS channels are currently not supported in 5 GHz AP mode.

There are some high latency problems with these MediaTek chipsets. To fix this, the only solution is to disable ASPM:

This configuration file will take effect on next reboot or after reloading the module with modprobe:

These are also sometimes branded as AMD RZ608 (mt7921) and RZ616 (mt7922).

This article or section is out of date.

See [7] for a list of Realtek chipsets and specifications.

The driver is now in the kernel, but many users have reported being unable to make a connection although scanning for networks does work.

8192cu-dkmsAUR includes many patches; try this if it does not work fine with the driver in kernel.

The rtl8723ae and rtl8723be modules are included in the mainline Linux kernel.

Some users may encounter errors with powersave on this card. This is shown with occasional disconnects that are not recognized by high level network managers (netctl, NetworkManager). This error can be confirmed by running dmesg -w as root or journalctl -f as root and looking for output related to powersave and the rtl8723ae/rtl8723be module. If you have this issue, use the fwlps=0 kernel module parameter which should prevent the Wi-Fi card from automatically sleeping and halting connection.

If you have poor signal, perhaps your device has only one physical antenna connected, and antenna autoselection is broken. You can force the choice of antenna with ant_sel=1 or ant_sel=2 kernel option. [8]

Realtek chipsets rtl8811au, rtl8812au, rtl8814au and rtl8821au designed for various USB adapters ranging from AC600 to AC1900. Several packages provide various kernel drivers, these require DKMS (the dkms package and the kernel headers installed):

rtl8821cu-dkms-gitAUR provides a kernel module for the Realtek 8811cu and 8821cu chipset.

This requires DKMS, so make sure you have your proper kernel headers installed.

If no wireless interface shows up even though the 8821cu module is loaded, you may need to manually specify the rtw_RFE_type kernel module parameter [9][10]. Try e.g. rtw_RFE_type=0x26, other values might also work.

rtl8821ce-dkms-gitAUR provides a kernel module for the Realtek 8821ce chipset found in the Asus X543UA.

This requires DKMS, so make sure you have your proper kernel headers installed.

rtl88x2bu-dkms-gitAUR provides a kernel module for the Realtek 8822bu chipset found in the Edimax EW7822ULC USB3, Asus AC53 Nano USB 802.11ac and TP-Link Archer T3U adapter.

This requires DKMS, so make sure you have your proper kernel headers installed.

This article or section needs expansion.

Issues with the rtl8xxxu mainline kernel module may be solved by compiling a third-party module for the specific chipset. The source code can be found in GitHub repositories.

Some drivers may be already prepared in the AUR, e.g. rtl8723bu-dkms-gitAUR, rtl8852au-dkms-gitAUR, rtl8852bu-dkms-gitAUR, rtl8852cu-dkms-gitAUR.

RWT88 kernel module is included in all officially supported Arch Linux kernels. The number of supported devices grew over time, currently it supports most RTW88 chip devices if configured and compiled to do so.

As of Linux 6.10.3, the driver supports: 882BE (possibly), 8703B, 8723CS, 8723D, 8723DE, 8723DS, 8723DU, 8723X, 8821C, 8821CE, 8821CS, 8821CU, 8822B, 8822BE, 8822BS, 8822BU, 8822C, 8822CE, 8822CS, 8822CU.

To get more up-to-date list, Ctrl+F CONFIG_RTW88_ linux's config or check out wireless-next upstream.

Make sure that wireless-regdom is configured. Otherwise, you will be able to see all Wi-Fi networks, but will not be able to connect. Out-of-tree driver rtl88x2bu-dkms-gitAUR can connect without such configuration, so it's important to set regulatory domain when switching from it.

Here is how those symptoms look in dmesg:

The RTW89 kernel module has been merged into the upstream kernel and provides support for newer Realtek wireless chipsets.

This driver supports: 8852AE, 8851BE, 8852BE, and 8852CE.

On some computers, you may experience unstable connections. It seems like a common issue on late models from HP and Lenovo. Try disabling ASPM-related features using the config below.

There are different drivers for devices with Atheros chipset:

There are some other drivers for some Atheros devices. See Linux Wireless documentation for details.

If you find web pages randomly loading very slow, or if the device is unable to lease an IP address, try to switch from hardware to software encryption by loading the ath5k module with nohwcrypt=1 option. See Kernel modules#Setting module options for details.

Some laptops may have problems with their wireless LED indicator flickering red and blue. To solve this problem, do:

For alternatives, see this bug report.

As of Linux 3.15.1, some users have been experiencing a decrease in bandwidth. In some cases, this can fixed by setting the nohwcrypt=1 kernel module parameter for the ath9k module.

Although Linux Wireless says that dynamic power saving is enabled for Atheros ath9k single-chips newer than AR9280, for some devices (e.g. AR9285), powertop might still report that power saving is disabled. In this case, enable it manually.

On some devices (e.g. AR9285), enabling the power saving might result in the following error:

The solution is to set the ps_enable=1 kernel module parameter for the ath9k module.

iwlegacy is the wireless driver for Intel's 3945 and 4965 wireless chips. The firmware is included in the linux-firmware package.

udev should load the driver automatically, otherwise load iwl3945 or iwl4965 manually. See Kernel modules for details.

If you have problems connecting to networks in general (e.g. random failures with your card on bootup or your link quality is very poor), try to disable 802.11n:

iwlwifi is the wireless driver for Intel's current wireless chips, such as 5100AGN, 5300AGN, and 5350AGN. See the full list of supported devices.

If you have problems connecting to networks in general or your link quality is very poor, try to disable 802.11n, and perhaps also enable software encryption:

If you have a problem with slow uplink speed you may try disabling power saving for your wireless adapter.

If you have an 802.11ax (Wi-Fi 6) access point and have problems detecting the beacons or an unreliable connection, review Intel Article 54799.

If you have difficulty connecting a bluetooth headset and maintaining good downlink speed, try disabling Bluetooth coexistence:

Make sure your firmware is fully updated before trying anything else.

You may have some issue where the driver outputs stack traces & errors, which can cause some stuttering.

Alternatively, you may simply experience miscellaneous issues (e.g. connection issues on 5GHz, random disconnections, no connection on resume).

To confirm it is the cause of the issues, downgrade the package linux-firmware.

If confirmed, move the buggy firmware files so that an older version is loaded (to be able to have an up to date linux-firmware since it is not only providing firmware updates for your Intel Wi-Fi card):

To avoid having to repeat these steps manually after each update, use the NoExtract and NoUpgrade arrays in pacman.conf with a wildcard to block their installation.

If the Wi-Fi adapter is not getting detected after finishing a session in Windows, this might be due to Windows' Fast Startup feature which is enabled by default. Try disabling Fast Startup. The iwlwifi kernel driver wiki has an entry for this.

The default settings on the module are to have the LED blink on activity. Some people find this extremely annoying. To have the LED on solid when Wi-Fi is active, you can use the systemd-tmpfiles:

Run systemd-tmpfiles --create phy0-led.conf for the change to take effect, or reboot.

To see all the possible trigger values for this LED:

The aic8800-dkmsAUR package should be used with these devices. These drivers are out of the mainline Linux kernel and require DKMS.

For this chip variant, aic8800d80-dkmsAUR package should be used instead of the one mentioned above.

See Broadcom wireless.

Treat this Tenda card as an rt2870sta device. See #rt2x00.

This should be a part of the kernel package and be installed already.

Some Orinoco chipsets are Hermes II. You can use the wlags49_h2_cs driver instead of orinoco_cs and gain WPA support. To use the driver, blacklist orinoco_cs first.

The driver p54 is included in kernel, but you have to download the appropriate firmware for your card from this site and install it into the /usr/lib/firmware directory.

zd1211rw is a driver for the ZyDAS ZD1211 802.11b/g USB WLAN chipset, and it is included in recent versions of the Linux kernel. See [12] for a list of supported devices. You only need to install the firmware for the device, provided by the zd1211-firmwareAUR package.

Host AP is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3 chipset. The driver is included in Linux kernel.

Ndiswrapper is a wrapper script that allows you to use some Windows drivers in Linux. You will need the .inf and .sys files from your Windows driver.

Follow these steps to configure ndiswrapper.

The ndiswrapper install is almost finished; you can load the module at boot.

Test that ndiswrapper will load now:

See Network configuration#Listing network interfaces for more assurance the wireless interface now exists.

If you have problems, some help is available at: ndiswrapper howto and ndiswrapper FAQ.

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -knnd ::0280
```

Example 2 (unknown):
```unknown
00:14.3 Network controller [0280]: Intel Corporation BE201 320MHz [8086:a840] (rev 10)
	Subsystem: Intel Corporation Device [8086:00e4]
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
```

Example 3 (unknown):
```unknown
dmesg | grep usbcore
```

Example 4 (unknown):
```unknown
usbcore: registered new interface driver rtl8187
```

---

## Fingerprint GUI

**URL:** https://wiki.archlinux.org/title/Fingerprint-gui

**Contents:**
- Installation
- Registering fingerprints
- Authentication
- Verification
- Exporting
- Password
- Known issues
  - Device is not recognized

Fingerprint GUI is a program that provides an interface and drivers for fingerprint readers. The package includes drivers from the open-source project fprint as well as proprietary drivers not included in fprint.

Install fingerprint-guiAUR.

The package includes an installation guide in HTML at /usr/share/doc/fingerprint-gui/Manual_en.html.

If you are using GNOME or KDE follow the instructions pacman gives and remove the following files:

If you are using a window manager, you may need an authentication agent. The package includes an authentication agent /lib/fingerprint-gui/fingerprint-polkit-agent. If your window manager is fully XDG compliant, this agent will autostart. An agent is only needed when enrolling fingers, not when identifying.

After installation, test if your hardware is recognized and correctly working by launching the configuration utility:

The -d is for debugging, and simply creates a verbose log of events. If you are comfortable without the debug info, you may safely omit the flag.

If your device is not recognized, you might need to reboot in order for udev to set the correct permissions for the device. You may need to add your user to the scanner group.

To start registering your fingerprints with the configuration utility, select the tab "Finger", select a finger and choose "next".

Once your fingerprints have been registered, you may notice that in the setup procedure that the "test" section does not yet work. This is because the necessary authentication has not been approved in the appropriate pam.d files.

As an example of how to set up fingerprint authetication for a given service, we will first start with sudo. Open /etc/pam.d/sudo in your text editor and insert the following bold text:

Keep in mind that your 'sudo' file may contain more entries.

Some users may not have (or want to have) sudo installed on their systems. In this case, it is still possible to use your fingerprint to authenticate su. This can be done just like the sudo example, of course instead adding an entry to /etc/pam.d/su. Again, add the following bold text.

One may also configure such things as GDM, SDDM, LightDM and the Gnome-Screensaver. Again, if more information or instruction is needed, please refer to the included manual. The Package Maintainer's Manual might provide further information that cannot be obtained by the included manual.

Now that the necessary authentication has been added to pam, you may wish the confirm the functionality of your setup. The easiest way to do this is to, again, launch the fingerprint-gui. Rather than go through the steps (as your fingerprints should already be established), click directly on the Settings tab. From here you may select the function you wish to test (ie. sudo, su, gdm, etc).

There is also an included utility to simply confirm that your registered fingerprints are recognized. This can be done by simply running:

and following the onscreen instructions.

If you wish to save your user's fingerprint data to a file, simply use the Export button in the Settings tab. A file Fingerprints.tar.gz" will be created in the desired directory. The saved file appears to be of little use, however, as an "Import" function has not yet been discovered (as of May 2018).

In some cases, using your fingerprint to log into the system may inhibit certain other functions of the desktop environment. For example, GNOME Keyring is dependent on your password, as it is used to encrypt the data in your keyring. To overcome this, Fingerprint GUI contains a feature that allows you to store your encrypted password on removable media (USB). You may then use the key to decrypt your keychain by authenticating your fingerprint while the removable media is plugged in.

The manual indicates that to use this function, mount your USB drive and ensure that you have write access to it. Under the "Password" tab of Fingerprint GUI, indicate the appropriate path to your device where it says "Save to directory" (ie. if using gvfs it should be under /run/media/your_uid/device). Enter your password and re-enter it and select "save". This will create a hidden directory on your removable media /.fingerprints and create a file username@hostname.xml. On the local machine, this will also create the file /var/lib/fingerprint-gui/username/config.xml.

If your device (for example 06cb:00bd, which can be found on recent Thinkpads) is not recognized while it is recognized by the CLI (fprint), it is because currently the Fingerprint GUI is based on an old version. See [1] for details.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/doc/fingerprint-gui/Manual_en.html
```

Example 2 (unknown):
```unknown
/etc/xdg/autostart/
```

Example 3 (unknown):
```unknown
polkit-gnome-authentication-agent-1.desktop
polkit-kde-authentication-agent-1.desktop
```

Example 4 (unknown):
```unknown
/lib/fingerprint-gui/fingerprint-polkit-agent
```

---

## Ventoy

**URL:** https://wiki.archlinux.org/title/Ventoy

**Contents:**
- Installation
- Usage
  - Use without installing
- Tips and tricks
  - What version is already installed?
  - Checking files integrity
- See also

Ventoy is a free and open source tool to create drives that allow you to select and boot any EFI, IMG, ISO, VHD(x), or WIM files stored on a rewritable partition on the drive.

Most types of operating systems are supported (Windows/WinPE/Linux/ChromeOS/Unix/VMware/Xen...), see the full list.

Install the ventoy-binAUR or ventoyAUR package.

There are three utilities for setting up the media:

The same utilities can be used for upgrading the Ventoy installation on the drive.

Ventoy creates two partitions on the drive. Their default names are Ventoy and VTOYEFI. The Ventoy partition is to store the bootable images (iso files), and any other data. VTOYEFI is for the Ventoy binaries.

To add images from which you can boot, mount the first partition and copy the images over.

If you just want to create a multi-boot drive, you can simply download the pre-built executable at the GitHub releases page. You need dosfstools to be installed because a vfat partition is created by using mkfs.vfat. After verifying the sha256sum and unpacking, you can display the included CLI's[1] help page by running the shell script without any arguments:

You can afterwards upgrade the drive for future versions by following a similar procedure. Downloading a NEWER-VERSION, verifying the sha256sum, unpacking, running

and following the on screen help message.

As an alternative to the shell script mentioned here, a GTK/qt[2], and a webUI[3], are also included.

With Ventoy2Disk.sh utility mentioned earlier, start, and do not approve, an upgrade process (-u). It will inform from which version it intends to upgrade, before asking for confirmation.

As described in upstream documentation, a built-in checksum utility allows verification of the integrity of the files on the disk.

**Examples:**

Example 1 (unknown):
```unknown
/opt/ventoy/Ventoy2Disk.sh
```

Example 2 (unknown):
```unknown
/opt/ventoy/VentoyGUI.x86_64
```

Example 3 (unknown):
```unknown
file:///opt/ventoy/WebUI/index.html
```

Example 4 (unknown):
```unknown
# ./ventoy-VERSION/Ventoy2Disk.sh
```

---

## Install Arch Linux from existing Linux

**URL:** https://wiki.archlinux.org/title/Install_Arch_Linux_from_existing_Linux

**Contents:**
- Backup and preparation
- From a host running Arch Linux
  - Create a new Arch installation
  - Create a copy of an existing Arch installation
- From a host running another Linux distribution
  - Using pacman from the host system
  - Creating a chroot
  - Using a chroot environment
    - Initializing pacman keyring
    - Downloading basic tools

This document describes the bootstrapping process required to install Arch Linux from a running Linux host system. After bootstrapping, the installation proceeds as described in the Installation guide.

Installing Arch Linux from a running Linux is useful for:

The goal of the bootstrapping procedure is to setup an environment from which the scripts from arch-install-scripts (such as pacstrap(8) and arch-chroot(8)) can be run.

If the host system runs Arch Linux, this can be achieved by simply installing arch-install-scripts. If the host system runs another Linux distribution, you will first need to set up an Arch Linux-based chroot.

Backup all your data including mails, webservers, etc. Have all information at your fingertips. Preserve all your server configurations, hostnames, etc.

Here is a list of data you will likely need:

In general, it is a good idea to have a local copy of your original /etc directory on your local hard drive.

Install the arch-install-scripts package.

Follow Installation guide#Mount the file systems to mount the filesystem that will be used for the root directory as well as all the other needed mount points. If you already use the /mnt directory for something else, just create another directory such as /mnt/install and use it as the mount point base for the rest of the installation.

At this stage, Arch Linux can either be installed from scratch or it can mirror the host installation. The two options are described thereafter.

Follow Installation guide#Installation.

In the procedure, the first step, Installation guide#Select the mirrors, can be skipped since the host should already have a correct mirrorlist.

It is possible to replicate an existing Arch Linux installation by copying the host filesystem to the new partition and make some adjustments to it to make it bootable and unique.

The first step is to copy the host files into the mounted new partition, for this, consider using the approach exhibited in rsync#Full system backup.

Then, follow the procedure described in Installation guide#Configure the system with some caveats and additional steps:

If the mirrored Arch installation may be used within a different configuration or with another hardware, consider the following additional operations:

There are multiple tools which automate a large part of the steps described in the following subsections. See their respective homepages for detailed instructions.

The manual way is presented in the following subsections. The idea is to either get pacman working directly on the host system, or to run an Arch system inside the host system, with the actual installation being executed from the Arch system. The nested system is contained inside a chroot.

Pacman can be compiled on most Linux distributions, and used directly on the host system to bootstrap Arch Linux. The arch-install-scripts should run without issues directly from the downloaded sources on any recent distribution.

Some distributions provide a package for pacman and/or arch-install-scripts in their official repositories which can be used for this purpose. As of July 2020, Void Linux is known to provide the pacman package, and Alpine Linux and Fedora are known to provide both pacman and arch-install-scripts.

Download the bootstrap tarball from a mirror into /tmp/.

Download the bootstrap tarball signature from the download page and place it in the same directory. Do not download it from a mirror.

Verify the signature with GnuPG.

Take note of the final --numeric-owner option, which is important for preserving correct UID and GID numbers of extracted files in case your existing Linux system uses different numbers than Arch Linux.

Select a repository server by editing /tmp/root.x86_64/etc/pacman.d/mirrorlist.

The bootstrap environment is really barebones (no nano or lvm2). Therefore, we need to set up pacman in order to download other necessary packages.

Before starting the installation, pacman keys need to be setup. Run the following commands:

See pacman/Package signing#Initializing the keyring for details.

Refresh the package lists and install what you need: base-devel, parted etc.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

You can now proceed to Installation guide#Mount the file systems and follow the rest of the Installation guide.

Some host systems or configurations may require certain extra steps. See the sections below for tips.

On some Debian-based host systems, pacstrap may produce the following error:

This is because in some versions of Debian, /dev/shm points to /run/shm while in the Arch-based chroot, /run/shm does not exist and the link is broken. To correct this error, create a directory /run/shm:

On Fedora based hosts and live USBs you may encounter problems when using genfstab to generate your fstab. Remove duplicate entries and the seclabel option where it appears, as this is SELinux-specific and will keep your system from booting normally.

Before rebooting, double check a few details in your installation to achieve a successful installation. To do so, first chroot into the newly-installed system, and then:

Find ~700 MiB of free space somewhere on the disk, e.g. by partitioning a swap partition. You can disable the swap partition and set up your system there.

Check cfdisk, /proc/swaps or /etc/fstab to find your swap partition. Assuming your hard drive is located on sdaX (X will be a number).

Disable the swap space:

Create a filesystem on it

Create a directory to mount it in

Finally, mount the new directory for installing the intermediate system.

Install essentials packages and any other package required to get a system with internet connection up and running in the temporary partition, being careful with the limit of ~700 MiB space. When specifying packages to be installed with pacstrap, consider adding the -c flag to avoid filling up valuable space by downloading packages to the host system.

Once the new Arch Linux system is installed, fix the boot loader configuration, then reboot into the newly created system, and rsync the entire system to the primary partition.

**Examples:**

Example 1 (unknown):
```unknown
/etc/resolv.conf
```

Example 2 (unknown):
```unknown
/etc/modules.conf
```

Example 3 (unknown):
```unknown
/mnt/install
```

Example 4 (unknown):
```unknown
/etc/pacman.conf
```

---

## General recommendations

**URL:** https://wiki.archlinux.org/title/General_recommendations

**Contents:**
- System administration
  - Users and groups
  - Security
  - Service management
  - System maintenance
- Package management
  - pacman
  - Repositories
  - Mirrors
  - Arch Build System

This document is an annotated index of popular articles and important information for improving and adding functionalities to the installed Arch system. Readers are assumed to have read and followed the Installation guide to obtain a basic Arch Linux installation. Having read and understood the concepts explained in #System administration and #Package management is required for following the other sections of this page and the other articles in the wiki.

This section deals with administrative tasks and system management. See Core utilities and Category:System administration for more.

A new installation leaves you with only the superuser account, better known as "root". Logging in as root for prolonged periods of time, possibly even exposing it via SSH on a server, is insecure. Instead, you should create and use unprivileged user account(s) for most tasks, only using the root account for system administration. See Users and groups#User management for details.

Users and groups are a mechanism for access control; administrators may fine-tune group membership and ownership to grant or deny users and services access to system resources. Read the Users and groups article for details and potential security risks.

Read Security for recommendations and best practices on hardening the system.

For a list of applications to allow running commands or starting an interactive shell as another user (e.g. root), see List of applications/Security#Privilege elevation.

Arch Linux uses systemd as the init process, which is a system and service manager for Linux. For maintaining your Arch Linux installation, it is a good idea to learn the basics about it.

Interaction with systemd is done through the systemctl command. See systemd#Basic systemctl usage for more information.

A logging system is also provided, with the command journalctl. See journal for more information.

Arch is a rolling release system and has rapid package turnover, so users have to take some time to do system maintenance.

This section contains helpful information related to package management. See FAQ#Package management and Category:Package management for more.

pacman is the Arch Linux package manager: it is highly encouraged to become familiar with it before reading any other articles.

For long term handling of cached packages, see pacman#Cleaning the package cache.

See pacman/Tips and tricks for suggestions on how to improve your interaction with pacman and package management in general.

See the Official repositories article for details about the purpose of each officially maintained repository.

If you plan on using 32-bit applications, you will want to enable the multilib repository.

The Unofficial user repositories article lists several other unsupported repositories.

You may consider installing the pkgstats service.

Visit the Mirrors article for steps on taking full advantage of using the fastest and most up to date mirrors of the official repositories. As explained in the article, a particularly good advice is to routinely check the Mirror Status page for a list of mirrors that have been recently synced. This can be automated with Reflector.

Ports is a system initially used by BSD distributions consisting of build scripts that reside in a directory tree on the local system. Simply put, each port contains a script within a directory intuitively named after the installable third-party application.

The Arch build system offers the same functionality by providing build scripts called PKGBUILDs, which are populated with information for a given piece of software: integrity hashes, project URL, version, license and build instructions. These PKGBUILDs are parsed by makepkg, the actual program that generates packages that are cleanly manageable by pacman.

Every package in the repositories along with those present in the AUR are subject to recompilation with makepkg.

While the Arch Build System allows the ability of building software available in the official repositories, the Arch User Repository (AUR) is the equivalent for user submitted packages. It is an unsupported repository of build scripts accessible through the web interface or through the Aurweb RPC interface.

This section contains information pertaining to the boot process. An overview of the Arch boot process can be found at Arch boot process. See Category:Boot process for more.

Hardware should be auto-detected by udev during the boot process by default. A potential improvement in boot time can be achieved by disabling module auto-loading and specifying required modules manually, as described in Kernel modules. Additionally, Xorg should be able to auto-detect required drivers using udev, but users have the option to configure the X server manually too.

Processors may have faulty behaviour, which the kernel can correct by updating the microcode on startup. See Microcode for details.

Once the login prompt appears, the messages from boot are cleared, leaving users unable to gather feedback from them. Disable clearing of boot messages to overcome this limitation.

Num Lock is a toggle key found in most keyboards. For activating Num Lock's number key-assignment during startup, see Activating numlock on bootup.

This section provides orientation for users wishing to run graphical applications on their system. See Category:Graphical user interfaces for additional resources.

This article or section is a candidate for merging with Arch boot process#Display manager.

Xorg is the public, open-source implementation of the X Window System (commonly X11, or X). It is required for running applications with graphical user interfaces (GUIs).

Wayland is a newer, alternative display server protocol with several compositors to choose from. Its advantages over Xorg are enhanced security features, more efficient handling of modern graphics tasks and active development while retaining compatibility through Xwayland.

The default modesetting display driver will work with most video cards, but performance may be improved and additional features harnessed by installing the appropriate driver for AMD or NVIDIA products.

Although the display server provides the basic framework for building a graphical environment, additional components may be considered necessary for a complete user experience. Desktop environments such as KDE, GNOME, COSMIC, Xfce, Cinnamon, LXDE, bundle together a wide range of well-integrated applications, such as a window manager or compositor, panel/taskbar, file manager, terminal emulator, text editor, icons, and other utilities. Users with less experience may wish to install a desktop environment for a more familiar environment. See Category:Desktop environments for additional resources.

A full-fledged desktop environment provides a complete and consistent graphical user interface, but tends to consume a good amount of system resources. Users seeking to maximize performance or otherwise simplify their environment may opt to install a window manager or compositor alone and hand-pick desired extras. Using Xorg, most desktop environments allow use of an alternative window manager as well. Dynamic, stacking, and tiling window managers differ in their handling of window placement.

Most desktop environments include a display manager for automatically starting the graphical environment and managing user logins. Users without a desktop environment can install one separately. Alternatively you may start X at login as a simple alternative to a display manager.

Well-known user directories like Downloads or Music are created by the xdg-user-dirs-update.service user service, that is provided by xdg-user-dirs and enabled by default upon install. If your desktop environment or window manager does not pull in the package, you can install it and run xdg-user-dirs-update manually as per XDG user directories#Creating default directories.

This section may be of use to laptop owners or users otherwise seeking power management controls. See Category:Power management for more.

See Power management for more general overview.

Users can configure how the system reacts to ACPI events such as pressing the power button or closing a laptop's lid. For the recommended method using systemd, see Power management#ACPI events. For the old method, see acpid.

Modern processors can decrease their frequency and voltage to reduce heat and power consumption. Less heat leads to more quiet system and prolongs the life of hardware. See CPU frequency scaling for details.

For articles related to portable computing along with model-specific installation guides, please see Category:Laptops. For a general overview of laptop-related articles and recommendations, see Laptop.

See the main article: Power management/Suspend and hibernate.

Category:Multimedia includes additional resources.

ALSA is a kernel sound system that should work out the box (it just needs to be unmuted). Sound servers such as PipeWire and PulseAudio can offer additional features and support more complex audio configuration.

See Professional audio for advanced audio requirements.

This section is confined to small networking procedures. See Network configuration for a full configuration guide and Category:Networking for related articles.

For better security while browsing the web, paying online, connecting to SSH services and similar tasks consider using DNSSEC-enabled DNS resolver that can validate signed DNS records, and an encrypted protocol such as DNS over TLS, DNS over HTTPS or DNSCrypt. See Domain name resolution for details.

A firewall can provide an extra layer of protection on top of the Linux networking stack. While the stock Arch kernel is capable of using Netfilter's iptables and nftables, neither are enabled by default. It is highly recommended to set up some form of firewall. See Category:Firewalls for available guides.

To share files among the machines in a network, follow the NFS or the SSHFS article.

Use Samba to join a Windows network. To configure the machine to use Active Directory for authentication, read Active Directory integration.

See also Category:Network sharing.

This section contains popular input device configuration tips. See Category:Input devices for more.

Non-English or otherwise non-standard keyboards may not function as expected by default. The necessary steps to configure the keymap are different for virtual console and Xorg, they are described in Keyboard configuration in console and Keyboard configuration in Xorg respectively.

Owners of advanced or unusual mice may find that not all mouse buttons are recognized by default, or may wish to assign different actions for extra buttons. Instructions can be found in Mouse buttons.

Many laptops use Synaptics or ALPS "touchpad" pointing devices. For these, and several other touchpad models, you can use either the Synaptics input driver or libinput; see Touchpad Synaptics and libinput for installation and configuration details.

See the TrackPoint article to configure your TrackPoint device.

This section aims to summarize tweaks, tools and available options useful to improve system and application performance.

Benchmarking is the act of measuring performance and comparing the results to another system's results or a widely accepted standard through a unified procedure.

The Improving performance article gathers information and is a basic rundown about gaining performance in Arch Linux.

The Solid state drive article covers many aspects of solid state drives, including configuring them to maximize their lifetimes, e.g. with TRIM.

This section relates to daemons.

Most distributions have a locate command available to be able to quickly search files. Arch Linux provides several alternatives, see locate for details.

Desktop search engines provide a similar service, while better integrated into desktop environments.

A default setup does not provide a way to synchronize mail. A list of mail delivery agents is available in the Mail server article.

CUPS is a standards-based, open source printing system developed by OpenPrinting for Linux. See Category:Printers for printer-specific articles.

This section contains frequently-sought "eye candy" tweaks for an aesthetically pleasing Arch experience. See Category:Eye candy for more.

You may wish to install a set of TrueType fonts, as only unscalable bitmap fonts are included in a basic Arch system. There are several general-purpose font families providing large Unicode coverage and even metric compatibility with fonts from other operating systems.

A plethora of information on the subject can be found in the Fonts and Font configuration articles.

If spending a significant amount of time working from the virtual console (i.e. outside an X server), users may wish to change the console font to improve readability; see Linux console#Fonts.

A big part of the applications with a graphical interface for Linux systems are based on the GTK or the Qt toolkits. See those articles and Uniform look for Qt and GTK applications for ideas to improve the appearance of your installed programs and adapt it to your liking.

This section applies to small modifications that improve console programs' practicality. See Category:Command-line shells for more.

It is recommended to properly set up extended tab completion right away, as instructed in the article of your chosen shell.

Aliasing a command, or a group thereof, is a way of saving time when using the console. This is especially helpful for repetitive tasks that do not need significant alteration to their parameters between executions. Common time-saving aliases can be found in Bash#Aliases, which are easily portable to zsh as well.

Bash is the shell installed by default in an Arch system. The live installation media, however, uses zsh with the grml-zsh-config addon package. See Command-line shell#List of shells for more alternatives.

A list of miscellaneous Bash settings, history search and Readline macros is available in Bash#Tips and tricks.

This section is covered in Color output in console.

Compressed files, or archives, are frequently encountered on a GNU/Linux system. Tar is one of the most commonly used archiving tools, and users should be familiar with its syntax (Arch Linux packages, for example, are simply zstd compressed tarballs). See Archiving and compression.

The console prompt (PS1) can be customized to a great extent. See Bash/Prompt customization or Zsh#Prompts if using Bash or Zsh, respectively.

Emacs is known for featuring options beyond the duties of regular text editing, one of these being a full shell replacement. Consult Emacs#Colored output issues for a fix regarding garbled characters that may result from enabling colored output.

Using a mouse with the console for copy-paste operations can be preferred over GNU Screen's traditional copy mode. Refer to General purpose mouse for comprehensive directions. Note that you can already do this in terminal emulators with the clipboard.

Using terminal multiplexers like tmux or GNU Screen, programs may be run under sessions composed of tabs and panes that can be detached at will, so when the user either kills the terminal emulator, terminates X, or logs off, the programs associated with the session will continue to run in the background as long as the terminal multiplexer server is active. Interacting with the programs requires reattaching to the session.

**Examples:**

Example 1 (unknown):
```unknown
xdg-user-dirs-update.service
```

Example 2 (unknown):
```unknown
xdg-user-dirs-update
```

---

## Arch IRC channels

**URL:** https://wiki.archlinux.org/title/IRC_channels

**Contents:**
- Main channels
  - Registration
  - Channel operators
  - Libera Chat group contacts
- Collaborative debugging
  - IRC usage
  - Output errors/messages to a file
- Other channels
  - International IRC channels

To use Internet Relay Chat (IRC), you need an IRC client. The installation live environment includes the Irssi client.

You are expected to familiarize yourself with our Code of conduct and General guidelines#IRC before joining any of the official channels. For a list of commonly used abbreviations, see Arch terminology.

This section is about #archlinux, the main Arch Linux support IRC channel, and #archlinux-offtopic, the main Arch Linux social channel, both available on the Libera Chat network. See https://archlinux.org/news/move-of-official-irc-channels-to-liberachat/

The central topic for #archlinux is support and general discussion about Arch Linux.

In order to reduce spam, #archlinux and #archlinux-offtopic have the channel mode set to +r and +q $~a. This means you have to be identified via NickServ to be able to join these channels and send messages, respectively. If you are not registered and identified, you will be forwarded to #archlinux-unregistered.

To register with NickServ, follow the Libera Chat FAQ, as well as NickServ HELP when connected to irc.libera.chat:

Arch operators are ops in both #archlinux and #archlinux-offtopic. See the list below, or run /msg phrik listops on Libera Chat.

If you for some reason need the help of an op, do not be shy to /query or /msg us. Here is the list of ops as of 2021-09-24:

Group contacts mediate matters between the Libera Chat network staff, Arch Linux staff and Arch Linux users. That includes the management of channels in the #archlinux-* namespace on the Libera Chat network and the assignment of archlinux/* hostmasks. Please note that only Arch Linux staff is eligible for hostmasks.

When requesting help from an IRC help channel (like #archlinux), it is inappropriate to paste logs into the channel and this may even get you kicked. Use a pastebin instead, you can use phriks factoid !paste to see which pastebins are acceptable. Acceptable pastebins usually work without enabling JavaScript. Some require enabling JavaScript for posting from a web browser, which is still acceptable because it does not affect the viewer. They should not display advertising or other disrupting content and should also not require a login. Excellent pastebins usually provide a way to paste output via piping.

An example list of acceptable pastebins:

When first entering the channel, there is no need to say hello. State the problem you are experiencing and make sure to be verbose and to provide logfiles. It also helps to search for any error messages you are getting first to not waste anybodys time. It is also worth it to search for issues on any of the bugtrackers of the relevant software. The more helpful and verbose you are, the quicker you are going to receive help.

If this is a problem or question which is very specific to a specific software, consider visiting the dedicated IRC channel for it if there is one. It is more likely to receive a good answer there.

Sometimes it is not possible to pipe the output to a pastebin directly and it should be written into a file before.

This is useful if pasting logs that contain sensitive data, e.g serial numbers in smartctl output, which have to be manually edited out.

The size of our community led to the creation of multiple IRC channels. To get a list of all channels on irc.libera.chat that contain archlinux in their name, use the command /query alis LIST *archlinux*. For further information on how to search channels, see https://libera.chat/guides/findingchannels.

International discussions are available at the following channels, also located at the irc.libera.chat IRC network, unless stated otherwise.

**Examples:**

Example 1 (unknown):
```unknown
NickServ HELP
```

Example 2 (unknown):
```unknown
/query NickServ HELP REGISTER
/query NickServ HELP IDENTIFY
```

Example 3 (unknown):
```unknown
/quote NickServ command
```

Example 4 (unknown):
```unknown
/msg NickServ command
```

---

## Google Authenticator

**URL:** https://wiki.archlinux.org/title/Google_Authenticator

**Contents:**
- Installation
- Configuration
  - SSH
    - Request OTP only when connecting from outside your local network
  - Desktop logins
- Usage
  - Generating a secret key file
    - Storage location
  - Code generation
    - Mobile phone generators

Google Authenticator provides a two-step authentication procedure using one-time passcodes (OTP), initially standardized by the Initiative for Open Authentication (OATH). The authentication mechanism integrates into the Linux PAM system. This guide shows the installation and configuration of this mechanism.

For the reverse operation (generating codes compatible with Google Authenticator under Linux) see #Code generation below.

Install the libpam-google-authenticator package, which provides the client program google-authenticator(1) and the PAM module pam_google_authenticator.so. The development version is available with google-authenticator-libpam-gitAUR.

This section covers configuring the system's PAM to require Google Authenticator OTP authentication for SSH and, optionally, desktop login.

Usually one demands two-pass authentication only for remote login. The corresponding PAM configuration file is /etc/pam.d/sshd. In case you want to use Google Authenticator globally you would need to change /etc/pam.d/system-auth, however, in this case proceed with extreme caution to not lock yourself out. In this guide we proceed with editing /etc/pam.d/sshd which is most safely (but not necessarily) done in a local session.

To enter both, your unix password and your OTP, add pam_google_authenticator.so above the system-remote-login lines to /etc/pam.d/sshd:

This will ask for the OTP before prompting for your Unix password. Changing the order of the two modules will reverse this order.

To allow login with either the OTP or your Unix password use:

Enable keyboard interactive authentication in /etc/ssh/sshd_config.d/99-archlinux.conf:

Finally, reload sshd.service.

Sometimes, we just want to enable the 2FA capability just when we connect from outside our local network. To achieve this, create a file (e.g. /etc/security/access-local.conf) and add the networks where you want to be able to bypass the 2FA from:

Then edit your /etc/pam.d/sshd and add the line:

The Google Authenticator PAM plugin can also be used for console logins and with GDM. Just add the following to /etc/pam.d/login or the /etc/pam.d/gdm-password file:

Every user who wants to use two-pass authentication needs to

The google-authenticator generates a TOTP secret key file as follows:

It is recommended to store the emergency scratch codes safely (print them out and keep them in a safe location) as they are your only way to log in (via SSH) when you lost your mobile phone (i.e. your OTP-generator). They are also stored in ~/.google_authenticator, so you can look them up any time as long as you are logged in.

If you want to change the secret key files' storage path, you can use the flag --secret:

Then, do not forget to change the location path for PAM, in /etc/pam.d/sshd:

user=root is used to force PAM to search the file using root user.

Also, take care with the permissions of the secret key file. Indeed, the file must be only-readable by the owner (chmod: 400). Here, the owner is root.

In the final setup step, each user has to associate the secret key file generated in their home directory with their choice of OTP-generators to serve the authentication codes. A user may set up generators on different devices for redundancy, for example in an OTP application on a mobile phone and a separate password manager, or decide to rely on the emergency scratch codes generated earlier as backup.

Install a generator application on your mobile phone (e.g.):

In the mobile application, create a new account and either scan the QR code from the URL you were told when generating the secret key file, or enter the secret key (in the example above 'ZVZG5UZU4D7MY4DH') manually.

Now you should see a new passcode token being generated every 30 seconds on your phone.

If you have Google Authenticator configured with other systems, then losing your device can prevent you from being able to log in to those systems. Having additional ways to generate the codes can be helpful.

A script that enables the display, generation, storage and management of Google Authenticator codes is provided by gashellAUR. An alternative option is auther-gitAUR.

GUI password manager keepassxc allows associating Google Authenticator codes to its entries, and then it can generate OTP codes and export its keys via QR code.

The easiest way to generate codes is with oathtool(1). It is available in the oath-toolkit package, and can be used as follows:

On most Android systems with sufficient user access, the Google Authenticator database can be copied off the device and accessed directly, as it is an sqlite3 database. However, at some point in July 2022, the secret column on the accounts table started using encryption. If your database backup does not use this encryption, this shell script will read a Google Authenticator database and generate live codes for each key found:

SSH to your host from another machine and/or from another terminal window:

**Examples:**

Example 1 (unknown):
```unknown
pam_google_authenticator.so
```

Example 2 (unknown):
```unknown
/etc/pam.d/sshd
```

Example 3 (unknown):
```unknown
/etc/pam.d/system-auth
```

Example 4 (unknown):
```unknown
/etc/pam.d/sshd
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Multilib

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## systemd-networkd

**URL:** https://wiki.archlinux.org/title/Systemd-networkd

**Contents:**
- Installation
  - Required services and setup
  - systemd-networkd-wait-online
- Configuration
  - systemd example network files
  - Multiple interfaces that are not connected all the time
  - Wait until network interfaces have a routable address
  - Wait until DNS servers are reachable
- Usage
  - networkctl

systemd-networkd is a system daemon that manages network configurations. It detects and configures network devices as they appear; it can also create virtual network devices. This service can be especially useful to set up complex network configurations for a container managed by systemd-nspawn or for virtual machines. It also works fine on simple connections.

systemd is part of the default Arch installation and contains all needed files to operate a wired network. Wireless adapters, covered later in this article, can be set up by services, such as wpa_supplicant or iwd.

To use systemd-networkd, start/enable systemd-networkd.service.

It is optional to also configure systemd-resolved, which is a network name resolution service to local applications, considering the following points:

Enabling systemd-networkd.service also enables systemd-networkd-wait-online.service, which is a oneshot system service that waits for the network to be configured. The latter has WantedBy=network-online.target, so it will be started only when network-online.target itself is enabled or pulled in by some other unit. See also systemd#Running services after the network is up.

By default, systemd-networkd-wait-online.service waits for all links managed by systemd-networkd to be fully configured or failed, and for at least one link to be online.

See systemd-networkd-wait-online(8) for details.

A quick way to enable a network interface is to use one of the provided .example files located in /usr/lib/systemd/network/. For instance, to enable Wi-Fi and Ethernet, you can create symbolic links to the example files:

You can use networkctl to add any additional custom configuration. See the #networkctl section.

For system with multiple network interfaces that are not expected to be connected all the time (e.g. if a dual-port Ethernet card, but only one cable plugged in), starting systemd-networkd-wait-online.service will fail after the default timeout of 2 minutes. This may cause an unwanted delay in the startup process. To change the behaviour to wait for any interface rather than all interfaces to become online, edit the service and add the --any parameter to the ExecStart line:

Alternatively, use systemd-networkd-wait-online@.service to wait for a specific interface. For example, to wait for enp1s0, disable systemd-networkd-wait-online.service and enable systemd-networkd-wait-online@enp1s0.service.

Per systemd-networkd-wait-online.service(8), "online means that the link's operational state is equal or higher than "degraded"." (see networkctl(1) for the definition of "degraded" and other operational statuses).

To prevent systemd-networkd-wait-online.service from exiting before network interfaces have a routable IP address (and thus having other services that require a working network connection starting too early), add RequiredForOnline=routable to the [Link] section in .network files:

systemd-networkd-wait-online.service(8) can be delayed until all configured interfaces can connect to their DNS servers. This improves the chances that DNS is operational when network-online.target is reached and units ordered after it begin to start.

To enable this feature, edit systemd-networkd-wait-online.service and add the --dns option to the ExecStart line:

This article or section is a candidate for merging with #Configuration.

This article or section needs expansion.

The global configuration file in /etc/systemd/networkd.conf may be used to override some defaults only. The main configuration is performed per network device. Configuration files are located in /usr/lib/systemd/network/, the volatile runtime network directory /run/systemd/network/ and the local administration network directory /etc/systemd/network/. Files in /etc/systemd/network/ have the highest priority.

There are three types of configuration files. They all use a format similar to systemd unit files.

They all follow the same rules:

After making changes to a configuration file, restart systemd-networkd.service.

You can use networkctl to query or modify the status of network links:

For example, to enable Multicast DNS for the Wi-Fi interface:

Replace wlan0 with your stable interface name or specify the full path instead. See networkctl(1).

Address= can be used more than once to configure multiple IPv4 or IPv6 addresses. See systemd.network(5) for more options.

In order to connect to a wireless network with systemd-networkd, a wireless adapter configured with another application such as wpa_supplicant or iwd is required.

If the wireless adapter has a static IP address, the configuration is the same (except for the interface name) as in a wired adapter.

To authenticate to the wireless network, use e.g. wpa_supplicant or iwd.

This setup will enable a DHCP IP for both a wired and wireless connection making use of the metric directive to allow the kernel to decide on-the-fly which one to use. This way, no connection downtime is observed when the wired connection is unplugged.

The kernel's route metric (same as configured with ip) decides which route to use for outgoing packets, in cases when several match. This will be the case when both wireless and wired devices on the system have active connections. To break the tie, the kernel uses the metric. If one of the connections is terminated, the other automatically wins without there being a gap with nothing configured (ongoing transfers may still not deal with this nicely but that is at a different OSI layer).

systemd-networkd does not set per-interface-type default route metrics, so it needs to be configured manually:

This is an example of a DHCP server configuration which works well with hostapd to create a wireless hotspot. IPMasquerade adds the firewall rules for NAT and implies IPv4Forwarding=yes to enable packet forwarding.

The factual accuracy of this article or section is disputed.

See systemd.network(5) § [DHCPSERVER] SECTION OPTIONS for all available options.

systemd-networkd can provide fully automatic configuration of networking for systemd-nspawn containers using private networking when it is used on the host system as well as inside the container. See systemd-nspawn#Networking for a comprehensive overview.

For the examples below,

First, create a virtual bridge interface with a .netdev unit file which tells systemd-networkd to create a device named br0 that functions as an Ethernet bridge.

Optionally add MACAddress=none to the NetDev section for the bridge to inherit MAC address from one of the bridged interfaces. This also requires a creation of 25-br0.link file.

Restart systemd-networkd.service to have systemd-networkd create the bridge.

To see the newly created bridge on the host and on the container, type:

Note that the interface br0 is listed but is still DOWN at this stage.

The next step is to add a network interface to the newly created bridge. The configuration file of the bridge must be loaded before those of the bridged interfaces, so its configuration file should be alphanumerically prior to those. In the example below, we add any interface that matches the name en* into the bridge br0.

The Ethernet interface must not have DHCP or an IP address associated, as the bridge requires an interface to bind to with no IP address.

Now that the bridge has been created and has been bound to an existing network interface, the IP configuration of the bridge interface must be specified. This is defined in a third .network file, the example below uses DHCP.

For the bridge to inhering MAC address from one of the bridged interfaces, set MACAddress=none and MACAddressPolicy=none.

Use the --network-bridge=br0 option when starting the container. See systemd-nspawn#Use a network bridge for details.

This article or section is out of date.

the above command output confirms we have a bridge with two interfaces binded to.

the above command outputs confirm we have activated br0 and host0 interfaces with an IP address and Gateway 192.168.1.254. The gateway address has been automatically grabbed by systemd-networkd.

Setting a static IP address for each device can be helpful in case of deployed web services (e.g. FTP, HTTP, SSH). Each device will keep the same MAC address across reboots if your system /usr/lib/systemd/network/99-default.link file has the MACAddressPolicy=persistent option (it has by default). This setup routes any service on the gateway to the desired device.

The following configuration needs to be done for this setup:

The configuration is very similar to the #Network bridge with DHCP section. First, a virtual bridge interface needs to be created and the main physical interface needs to be bound to it. This task can be accomplished with the following two files, with contents equal to those available in the DHCP section.

Next, you need to configure the IP and DNS of the newly created virtual bridge interface. For example:

To get configure a static IP address on the container, we need to override the system /usr/lib/systemd/network/80-container-host0.network file, which provides a DHCP configuration for the host0 network interface of the container. This can be done by placing the configuration into /etc/systemd/network/80-container-host0.network. For example:

Make sure that systemd-networkd.service is enabled in the container.

For the host to be able to reach containers connected via MACVLAN, the host itself also needs to connect via MACVLAN and not directly to the underlying Ethernet network interface.

On the host, attach the underlying Ethernet network interface to MACVLAN and make sure it does not get assigned IP addresses. For example, using mv-0 as the MACVLAN interface name and with enp1s0 as the host's Ethernet interface:

Create the MACVLAN bridge mv-0:

Configure the host's network connection on the MACVLAN bridge (mv-0). The following example uses DHCP, replace the options as necessary.

For the container, attach a MACVLAN to the underlying Ethernet network interface (enp1s0 in the examples above). For example, in /etc/systemd/nspawn/container_name.nspawn specify:

For containers started from the command line, pass them the --network-macvlan=enp1s0 option.

In the container, the MACVLAN interface will have the name mv-underlying_interface_name (e.g. mv-enp1s0). Configure the network connection as necessary (just like in the host) by matching the interface name. For example, using DHCP:

systemd-networkd does not have a proper interactive graphical management interface. Still, some tools are available to either display or modify the current state of the network, receive notifications or interact with the wireless configuration:

Often there is a situation where your home wireless network uses DHCP and office wireless network uses static IP. This mixed setup can be configured as follows:

See also Wireless bonding.

Bonding allows connection sharing through multiple interfaces, so if e.g. the wired interface is unplugged, the wireless is still connected and the network connectivity remains up seamlessly.

Create a bond interface. In this case the mode is active-backup, which means packets are routed through a secondary interface if the primary interface goes down.

Set the wired interface as the primary:

Set the wireless as the secondary:

Configure the bond interface just like a normal interface:

Now if the wired network is unplugged, the connection should remain through the wireless:

On a higher bandwidth link with moderate latency (typically a home Internet connection that is above 10 Mbit/s) the default settings for the TCP Slow Start algorithm are somewhat conservative. This issue exhibits as downloads starting slowly and taking a number of seconds to speed up before they reach the connection's full bandwidth. It is particularly noticeable with a pacman upgrade, where each package downloaded starts off slowly and often finishes before it has reached the connection's full speed.

These settings can be adjusted to make TCP connections start with larger window sizes than the defaults, avoiding the time it takes for them to automatically increase on each new TCP connection[1]. While this will usually decrease performance on slow connections (or if the values are increased too far) due to having to retransmit a larger number of lost packets, they can substantially increase performance on connections with sufficient bandwidth.

It is important to benchmark before and after changing these values to ensure it is improving network speed and not reducing it. If you are not seeing downloads begin slowly and gradually speed up, then there is no need to change these values as they are already optimal for your connection speed. When benchmarking, be sure to test against both a high speed and low speed remote server to ensure you are not speeding up access to fast machines at the expense of making access to slow servers even slower.

To adjust these values, edit the .network file for the connection:

The defaults of 10 work well for connections slower than 10 Mbit/s. For a 100 Mbit/s connection, a value of 30 works well. The manual page systemd.network(5) § [ROUTE] SECTION OPTIONS says a value of 100 is considered excessive.

If the sysctl setting net.ipv4.tcp_slow_start_after_idle is enabled then the connection will return to these initial settings after it has been idle for some time (and often a very small amount of time). If this setting is disabled then the connection will maintain a higher window if a larger one was negotiated during packet transfer. Regardless of the setting, each new TCP connection will begin with the Initial* settings set above.

The sysctl setting net.ipv4.tcp_congestion_control is not directly related to these values, as it controls how the congestion and receive windows are adjusted while a TCP link is active, and particularly when the path between the two hosts is congested and throughput must be reduced. The above Initial* values simply set the default window values selected for each new connection, before any congestion algorithm takes over and adjusts them as needed. Setting higher initial values simply shortcuts some negotiation while the congestion algorithm tries to find the optimum values (or, conversely, setting the wrong initial values adds additional negotiation time while the congestion algorithm works towards correcting them, slowing down each newly established TCP connection for a few seconds extra).

systemd-networkd does not set per-interface-type default route metrics, i.e. they need to be configured manually when using multiple network devices. For example, the following ip route shows multiple default routes:

Since the same default metric value 1024 is assigned, there is a race condition which of both is chosen as default route. Since the eno2 device came up first, it is preferred and thus, access available via eno1 may be ignored.

To prevent the race condition, assign different RouteMetric= values for the devices. See #Wired and wireless adapters on the same machine for a corresponding example.

If instead one device should not provide a default route, the UseGateway=false option in [DHCPv4] and [IPv6AcceptRA] sections can be used to omit creating the default route provided by the DHCP/RA server while keeping other classless static routes. This may be useful, for example, if the device provides a connection to a single other machine.

To make your computer appear as two completely separate devices to your router, you can create a virtual interface not just with a different IP but also with a different MAC address.

To achieve this, create a virtual interface (macvlan) on top of your physical interface with a unique MAC address:

Then add a network file as usual, using the same subnet and gateway, and avoiding the range of IP numbers used for DHCP if you configure a static IP. For example:

The macvlan interface route has metric 2. This ensures that traffic will prefer going through the main interface, since that (implicitly) has a default route with metric 1, unless specifically directed to use the macvlan interface.

Finally, add MACVLAN=eth210 to the [Network] section of the .network file of your main interface!

At this point, a fast way to make your router aware of the new MAC (and configure it to accept that MAC) you can for example run arping -I eth210 192.168.132.1 as root. After configuring your router for the "new device" you can test if the new interface has internet access with for example curl --interface 192.168.132.210 ifconfig.me that should then print your public IP number.

**Examples:**

Example 1 (unknown):
```unknown
systemd-networkd.service
```

Example 2 (unknown):
```unknown
systemctl --type=service
```

Example 3 (unknown):
```unknown
IPv6AcceptRA=
```

Example 4 (unknown):
```unknown
[IPv6AcceptRA]
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Testing

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## Cursor themes

**URL:** https://wiki.archlinux.org/title/Cursor_themes

**Contents:**
- Installation
  - Packages
  - Manually
- Configuration
  - GTK and Qt configuration files
    - GTK
    - Qt
  - Desktop environments
    - GNOME
    - MATE

The display server is accompanied by a cursor theme that helps with various aspects of GUI navigation and manipulation. The display server includes a cursor theme, however, other cursor themes can be installed and selected.

Installation can be done with a package, or downloaded and extracted to an appropriate directory.

Cursors themes are available in the:

If a cursor theme is not available in the official repositories or the AUR, it can be added manually. A number of websites exist where cursor themes can be downloaded. Once downloaded, they need to be put in the icons directory (as cursors have the ability to be bundled with icon themes).

Some websites that have cursor themes:

For user-specific installation, use the ~/.local/share/icons/ directory, or ~/.icons/ which is used for backwards compatibility. Extract them with this command that will work for most archives:

The cursor theme directory structure is theme-name/cursors, for example: ~/.local/share/icons/theme/cursors/; make sure the extracted files follow this structure.

Already installed cursor themes can be viewed with the command:

If the package includes an index.theme file, check if there is an "Inherits" line inside. If yes, check whether the inherited theme also exists on the system (rename if needed).

There are various ways to set the cursor theme. The cursor appearance may change from one window to another if programs are not configured to use the same cursor theme.

Installed cursors may generally be set per desktop environment and per GUI framework. The cursor theme named "default" is the fallback when a configuration is not set.

There is no Qt configuration for cursors. Qt programs may pick up a cursor theme from the desktop environment, X resources, or lastly the "default" cursor theme if none are configured. To make Qt programs find cursors in the ~/.local/share/icons/ path, it must be in the XCURSOR_PATH environment variable.

Desktop environments use the XSETTINGS protocol, typically implemented through a settings daemon like Xsettingsd.

To change the theme in GNOME, use gnome-tweaks or set the configuration directly with:

Change the cursor size with (depending on the theme, sizes are 24, 32, 48, 64):

In MATE one can use mate-control-center or gsettings(1). To change the theme:

xdg-desktop-portal-gtk must be installed for GTK applications to correctly apply cursor theming on Wayland.

To change the xcursor theme, use:

See Sway#Change cursor theme and size.

To locally name a cursor theme, add to the ~/.Xresources file:

To have the cursor theme properly loaded, it will need to be done so by the window manager; if it does not, it can be forced to load prior the window manager by putting the following command in .xinitrc or .xprofile (depending on ones personal setup):

Optionally, add this line to ~/.Xresources if your cursor theme supports multiple sizes:

If in doubt over supported cursor sizes, start X without this setting and let it choose the cursor size automatically. (Refer to your window manager documentation for details).

The cursor theme name "default" is used by an application if it cannot pick up on a configuration. Thus, a last resort to make the cursor choice consistent across fragmented configurations is to edit the default theme to become a synonym of the theme of choice.

The default cursor theme is in the usual theme locations:

The default theme can be aliased to any other cursor theme by symlinking/copying the directory containing the desired cursor to the default theme paths:

Alternatively, the theme can simply inherit another desired one:

LXAppearance creates an ~/.icons/default/index.theme file: if you edited that file manually, LXAppearance will overwrite it.

You can use an environment variable to set a theme for a single application to try it out temporarily, for example:

XCURSOR_SIZE is optional if your cursor theme supports multiple sizes.

The factual accuracy of this article or section is disputed.

If cursor themes are installed in ~/.local/share/icons/, in order to avoid possible issues, add that path to XCURSOR_PATH. For example:

Cursor theme can usually be set within a display manager, but keep in mind the cursor theme may not carry over to the user session.

See GDM#Changing the cursor theme.

Tor Browser has its own "virtual" home directory and does not read the file in the user's home directory. Therefore, you need to copy configuration and, if necessary, icon themes to the Tor Browser installation directory:

Create a GTK configuration file on the Tor Browser "virtual" home directory:

If your desired cursor theme is not installed system-wide, you'll have to copy it to the Tor Browser "virtual" home directory; for example:

You can also just simply copy your whole cursor themes folder:

Applications may keep using the default cursors when a theme lacks some cursors. This can be corrected by adding links to the missing cursors. For example:

If the above does not solve the problem, look in /usr/share/icons/whiteglass/cursors for additional cursors your theme may be missing, and create links for these as well.

Some programs set their own custom cursors ~/.Xresources which you may want to override. A common example of this is rdesktop, which connects to a Microsoft Windows computer and uses the cursors obtained from the remote machine, which can often be difficult to see due to protocol limitations yielding poor conversion quality.

This can be resolved by replacing these cursors with ones from the same (or another) cursor theme. In order to do this, the hash of the image must be obtained. This is done by setting the XCURSOR_DISCOVER environment variable prior to launching the application that sets these cursors:

The first time (and only the first time) the cursor is set, some details will be displayed, like this:

When Xcursor looks for missing cursors, the search path includes ~/.icons/default/cursors so this is where an image can be placed for Xcursor to find. First, create this directory if it does not already exist:

Then link the hash to the target image. Here we are using the left_ptr image from the Vanilla-DMZ cursor theme:

The change will be visible as soon as the application is restarted. No special method of launching the application is required.

The default X shaped Xcursor appears in window managers that do not set the default cursor to left_ptr or in window managers using XCB (like awesome) instead of Xlib.

To fix this, simply add the following to your ~/.xinitrc, xsession or window managers startup configuration if possible (for example bspwm's bspwmrc).

The list of cursor styles is in appendix B of the X protocol.

If you have conflicting cursors then it might be because a different cursor has been set in the ~/.Xdefaults file.

If you are trying to change cursor size via ~/.Xresources in your ~/.xinitrc and it does not work, make sure that xrandr runs before loading ~/.Xresources.

Make sure your ~/.xinitrc looks similar to the following:

When changing the cursor size or theme when using Plasma under Wayland, make sure to restart the session after applying the changes [1] [2].

This is a bug. See a workaround at KDE#Plasma cursor sometimes shown incorrectly.

**Examples:**

Example 1 (unknown):
```unknown
~/.local/share/icons/
```

Example 2 (unknown):
```unknown
$ tar xvf foobar-cursor-theme.tar.gz -C ~/.local/share/icons
```

Example 3 (unknown):
```unknown
theme-name/cursors
```

Example 4 (unknown):
```unknown
~/.local/share/icons/theme/cursors/
```

---

## Swap

**URL:** https://wiki.archlinux.org/title/Swap_file

**Contents:**
- Swap space
- Swap partition
  - Enabling at boot
  - Disabling swap
- Swap file
  - Swap file creation
  - Swap file removal
- Swap encryption
- Performance
  - Swappiness

This page provides an introduction to swap space and paging on GNU/Linux. It covers creation and activation of swap partitions and swap files.

From All about Linux swap space:

Support for swap is provided by the Linux kernel and user-space utilities from the util-linux package.

Swap space can take the form of a disk partition or a file. Users may create a swap space during installation or at any later time as desired. Swap space can be used for two purposes, to extend the virtual memory beyond the installed physical memory (RAM), and also for suspend-to-disk support.

Whether or not it is beneficial to extend the virtual memory with swap depends on the amount of installed physical memory. If the amount of physical memory is less than the amount of memory required to run all the desired programs, then it may be beneficial to enable swap. This avoids out of memory conditions, where the Linux kernel OOM killer mechanism will automatically attempt to free up memory by killing processes. To increase the amount of virtual memory to the required amount, add the necessary difference (or more) as swap space.

The biggest drawback of using swap when running out of memory is its lower performance, see section #Performance. Hence, enabling swap is a matter of personal preference: some prefer programs to be killed over enabling swap and others prefer enabling swap and slower system when the physical memory is exhausted.

To check swap status, use:

Or to show physical memory as well as swap usage:

A swap partition can be created with most GNU/Linux partitioning tools. Swap partitions are designated by the partition type GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F on GPT (8200 type for gdisk, swap type for fdisk) and type ID 82 on MBR.

To set up a partition as Linux swap area, the mkswap(8) command is used. For example:

To enable the device for paging:

See swapon(8) for the options syntax.

To enable the swap partition at boot time, either:

See fstab for the file syntax, and systemd#systemd.mount - mounting.

To deactivate specific swap space:

Alternatively use the -a switch to deactivate all swap space.

Since swap is managed by systemd, it will be activated again on the next system startup. To disable the automatic activation of detected swap space permanently, run systemctl --type swap to find the responsible .swap unit and mask it.

As an alternative to creating an entire partition, a swap file offers the ability to vary its size on-the-fly, and is more easily removed altogether. This may be especially desirable if disk space is at a premium (e.g. a modestly-sized SSD).

Use mkswap(8) to create a swap file the size of your choosing (see Partitioning#Swap for advice). For example, creating a 4 GiB swap file:

Activate the swap file:

Finally, edit the fstab configuration to add an entry for the swap file:

As an alternative to fstab, a swap unit can be created (see systemd.swap(5)):

Perform a daemon-reload and enable swapfile.swap.

For additional information, see fstab#Usage.

To remove a swap file, it must be turned off first and then can be removed:

Finally, remove the relevant entry from /etc/fstab.

See dm-crypt/Swap encryption.

Swap operations are usually significantly slower than directly accessing data in RAM. However, disabling swap entirely to improve performance can sometimes lead to a degradation. If there is not enough physical memory available to hold everything, swapping out nothing leaves less memory available for file system caches, causing more frequent and costly disk usage.

Swap values can be adjusted to help performance:

When memory usage reaches a certain threshold, the kernel starts looking at active memory and seeing what it can free up. File data can be written out to the file system (if changed), unloaded and re-loaded later; other data must be written to swap before it can be unloaded.

The swappiness sysctl parameter represents the kernel's preference for writing to swap instead of files. It can have a value between 0 and 200 (max 100 if Linux < 5.8); the default value is 60. A low value causes the kernel to prefer freeing up open files, a high value causes the kernel to try to use swap space, and a value of 100 means IO cost is assumed to be equal.

To check the current swappiness value:

Alternatively, the file /proc/sys/vm/swappiness can be read in order to obtain the raw integer value.

To temporarily set the swappiness value:

To set the swappiness value permanently, create a sysctl.d(5) configuration file. For example:

To have the boot loader set swappiness when loading the kernel, add a kernel parameter, e.g. sysctl.vm.swappiness=35.

Reasons for choosing a different swappiness can include:

Another sysctl parameter that affects swap performance is vm.vfs_cache_pressure, which controls the tendency of the kernel to reclaim the memory which is used for caching of VFS caches, versus pagecache and swap. Increasing this value increases the rate at which VFS caches are reclaimed. For more information on what it does, see the Linux kernel documentation.

The default value is 100, which states that filesystem cache is about as important as the other caches, so they should be reclaimed at about an equal weight. On desktops it has been argued that filesystem cache is more important than the other caches because filesystem browsing times affects operation latency (perceived responsiveness) more than the other caches, resulting a suggested value of 50. On the other hand, a higher value has been suggested when the VFS cache holds metadata on many small files that are not touched again. For more information on tuning this parameter, see OpenSUSE tuning guide (which recommends experimenting and checking the types of caches via slaptop).

If you have more than one swap file or swap partition you should consider assigning a priority value (0 to 32767) for each swap area. The system will use swap areas of higher priority before using swap areas of lower priority. For example, if you have a faster disk and a slower disk, assign a higher priority to the swap area located on the fastest device. Priorities can be assigned in fstab via the pri parameter:

Or via the --priority parameter of swapon:

If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them.

There is no necessity to use RAID for swap performance reasons. The kernel itself can stripe swapping on several devices, if you just give them the same priority in the /etc/fstab file. Refer to The Software-RAID HOWTO for details.

See Solid state drive#swap.

See Improving performance#Swap on zram or zswap.

If you only need swap as a hibernation image storage space, then you can use zswap and disable its writeback so that there are no disk writes from regular swap usage. See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation.

**Examples:**

Example 1 (unknown):
```unknown
$ swapon --show
```

Example 2 (unknown):
```unknown
0657FD6D-A4AB-43C4-84E5-0933C84B4F4F
```

Example 3 (unknown):
```unknown
# mkswap /dev/sdxy
```

Example 4 (unknown):
```unknown
# swapon /dev/sdxy
```

---

## Arch IRC channels

**URL:** https://wiki.archlinux.org/title/IRC

**Contents:**
- Main channels
  - Registration
  - Channel operators
  - Libera Chat group contacts
- Collaborative debugging
  - IRC usage
  - Output errors/messages to a file
- Other channels
  - International IRC channels

To use Internet Relay Chat (IRC), you need an IRC client. The installation live environment includes the Irssi client.

You are expected to familiarize yourself with our Code of conduct and General guidelines#IRC before joining any of the official channels. For a list of commonly used abbreviations, see Arch terminology.

This section is about #archlinux, the main Arch Linux support IRC channel, and #archlinux-offtopic, the main Arch Linux social channel, both available on the Libera Chat network. See https://archlinux.org/news/move-of-official-irc-channels-to-liberachat/

The central topic for #archlinux is support and general discussion about Arch Linux.

In order to reduce spam, #archlinux and #archlinux-offtopic have the channel mode set to +r and +q $~a. This means you have to be identified via NickServ to be able to join these channels and send messages, respectively. If you are not registered and identified, you will be forwarded to #archlinux-unregistered.

To register with NickServ, follow the Libera Chat FAQ, as well as NickServ HELP when connected to irc.libera.chat:

Arch operators are ops in both #archlinux and #archlinux-offtopic. See the list below, or run /msg phrik listops on Libera Chat.

If you for some reason need the help of an op, do not be shy to /query or /msg us. Here is the list of ops as of 2021-09-24:

Group contacts mediate matters between the Libera Chat network staff, Arch Linux staff and Arch Linux users. That includes the management of channels in the #archlinux-* namespace on the Libera Chat network and the assignment of archlinux/* hostmasks. Please note that only Arch Linux staff is eligible for hostmasks.

When requesting help from an IRC help channel (like #archlinux), it is inappropriate to paste logs into the channel and this may even get you kicked. Use a pastebin instead, you can use phriks factoid !paste to see which pastebins are acceptable. Acceptable pastebins usually work without enabling JavaScript. Some require enabling JavaScript for posting from a web browser, which is still acceptable because it does not affect the viewer. They should not display advertising or other disrupting content and should also not require a login. Excellent pastebins usually provide a way to paste output via piping.

An example list of acceptable pastebins:

When first entering the channel, there is no need to say hello. State the problem you are experiencing and make sure to be verbose and to provide logfiles. It also helps to search for any error messages you are getting first to not waste anybodys time. It is also worth it to search for issues on any of the bugtrackers of the relevant software. The more helpful and verbose you are, the quicker you are going to receive help.

If this is a problem or question which is very specific to a specific software, consider visiting the dedicated IRC channel for it if there is one. It is more likely to receive a good answer there.

Sometimes it is not possible to pipe the output to a pastebin directly and it should be written into a file before.

This is useful if pasting logs that contain sensitive data, e.g serial numbers in smartctl output, which have to be manually edited out.

The size of our community led to the creation of multiple IRC channels. To get a list of all channels on irc.libera.chat that contain archlinux in their name, use the command /query alis LIST *archlinux*. For further information on how to search channels, see https://libera.chat/guides/findingchannels.

International discussions are available at the following channels, also located at the irc.libera.chat IRC network, unless stated otherwise.

**Examples:**

Example 1 (unknown):
```unknown
NickServ HELP
```

Example 2 (unknown):
```unknown
/query NickServ HELP REGISTER
/query NickServ HELP IDENTIFY
```

Example 3 (unknown):
```unknown
/quote NickServ command
```

Example 4 (unknown):
```unknown
/msg NickServ command
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Staging

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## Network configuration/Wireless

**URL:** https://wiki.archlinux.org/title/Wireless_network_configuration

**Contents:**
- Device driver
  - Check the driver status
  - Installing driver/firmware
- Utilities
  - iw and wireless_tools comparison
- iw
  - Get the name of the interface
  - Get the status of the interface
  - Activate the interface
  - Discover access points

The main article on network configuration is Network configuration.

Configuring wireless is a two-part process; the first part is to identify and ensure the correct driver for your wireless device is installed (they are available on the installation media, but often have to be installed explicitly), and to configure the interface. The second is choosing a method of managing wireless connections. This article covers both parts, and provides additional links to wireless management tools.

The #iw section describes how to manually manage your wireless network interface / your wireless LANs using iw. The Network configuration#Network managers section describes several programs that can be used to automatically manage your wireless interface, some of which include a GUI and all of which include support for network profiles (useful when frequently switching wireless networks, like with laptops).

The default Arch Linux kernel is modular, meaning many of the drivers for machine hardware reside on the hard drive and are available as modules. At boot, udev takes an inventory of your hardware and loads appropriate modules (drivers) for your corresponding hardware, which will in turn allow creation of a network interface.

Some wireless chipsets also require firmware, in addition to a corresponding driver. Many firmware images are provided by the linux-firmware package; however, proprietary firmware images are not included and have to be installed separately. This is described in #Installing driver/firmware.

To check if the driver for your card has been loaded, check the output of the lspci -k or lsusb -v command, depending on if the card is connected by PCIe or USB. You should see that some kernel driver is in use, for example:

Also check the output of the ip link command to see if a wireless interface was created; usually the naming of the wireless network interfaces starts with the letters "wl", e.g. wlan0 or wlp2s0. Then bring the interface up with:

For example, assuming the interface is wlan0, this is ip link set wlan0 up.

Check kernel messages for firmware being loaded:

If there is no relevant output, check the messages for the full output for the module you identified earlier (iwlwifi in this example) to identify the relevant message or further issues:

If the kernel module is successfully loaded and the interface is up, you can skip the next section.

Check the following lists to discover if your card is supported:

Note that some vendors ship products that may contain different chip sets, even if the product identifier is the same. Only the USB ID (for USB devices) or PCI ID (for PCIe devices) is authoritative.

If your wireless card is listed above, follow the #Troubleshooting drivers and firmware subsection of this page, which contains information about installing drivers and firmware of some specific wireless cards. Then check the driver status again.

If your wireless card is not listed above, it is likely supported only under Windows (some Broadcom, 3com, etc). For these, you can try to use ndiswrapper.

Just like other network interfaces, the wireless ones are controlled with ip from the iproute2 package.

Managing a wireless connection can be accomplished using network manager which will use wpa_supplicant or iwd for wireless authentication, or using wpa_supplicant or iwd directly. For lower level configuring, or if you are using a legacy driver or a legacy authentication method, there are iw and the deprecated wireless_tools.

The table below gives an overview of comparable commands for iw and wireless_tools. See Replacing iwconfig with iw for more examples.

Examples in this section assume that your wireless device interface is interface and that you are connecting to your_essid Wi-Fi access point. Replace both accordingly.

To get the name of your wireless interface, do:

The name of the interface will be output after the word "Interface". For example, it is commonly wlan0.

To check link status, use the following command.

You can get statistic information, such as the amount of tx/rx bytes, signal strength etc., with the following command:

Some cards require that the kernel interface be activated before you can use iw or wireless_tools:

To verify that the interface is up, inspect the output of the following command:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

To see what access points are available:

The important points to check:

You might need to set the proper operating mode of the wireless card. More specifically, if you are going to connect an ad-hoc network, you need to set the operating mode to ibss:

Depending on the encryption, you need to associate your wireless device with the access point to use and pass the encryption key:

Regardless of the method used, you can check if you have associated successfully:

This article or section needs expansion.

There are mainly two options for Wi-Fi authentication on Linux: wpa_supplicant and iwd.

WPA2 Personal, a.k.a. WPA2-PSK, is a mode of Wi-Fi Protected Access.

You can authenticate to WPA2 Personal networks using wpa_supplicant or iwd, or connect using a network manager. If you only authenticated to the network, then to have a fully functional connection, you will still need to assign the IP address(es) and routes either manually or using a DHCP client.

WPA2 Enterprise is a mode of Wi-Fi Protected Access. It provides better security and key management than WPA2 Personal, and supports other enterprise-type functionality, such as VLANs and NAP. However, it requires an external authentication server, called RADIUS server, to handle the authentication of users. This is in contrast to Personal mode which does not require anything beyond the wireless router or access points (APs), and uses a single passphrase or password for all users.

The Enterprise mode enables users to log onto the Wi-Fi network with a username and password and/or a digital certificate. Since each user has a dynamic and unique encryption key, it also helps to prevent user-to-user snooping on the wireless network, and improves encryption strength.

This section describes the configuration of network clients to connect to a wireless access point with WPA2 Enterprise mode. See Software access point#RADIUS for information on setting up an access point itself.

For a comparison of protocols, see the following table.

WPA2-Enterprise wireless networks demanding MSCHAPv2 type-2 authentication with PEAP sometimes require pptpclient in addition to the stock ppp package. netctl seems to work out of the box without ppp-mppe, however. In either case, usage of MSCHAPv2 is discouraged as it is highly vulnerable, although using another method is usually not an option.

eduroam is an international roaming service for users in research, higher education and further education, based on WPA2 Enterprise.

WPA3 Personal, a.k.a. WPA3-SAE, is a mode of Wi-Fi Protected Access.

Both wpa_supplicant and iwd support WPA3 Personal.

WPA3 Enterprise is a mode of Wi-Fi Protected Access.

wpa_supplicant (since version 2:2.10-8) supports WPA3 Enterprise. See FS#65314.

The regulatory domain, or "regdomain", is used to reconfigure wireless drivers to make sure that wireless hardware usage complies with local laws set by the FCC, ETSI and other organizations. Regdomains use ISO 3166-1 alpha-2 country codes. For example, the regdomain of the United States would be "US", China would be "CN", etc.

Regdomains affect the availability of wireless channels. In the 2.4GHz band, the allowed channels are 1-11 for the US, 1-14 for Japan, and 1-13 for most of the rest of the world. In the 5GHz band, the rules for allowed channels are much more complex. In either case, consult this list of WLAN channels for more detailed information.

Regdomains also affect the limit on the effective isotropic radiated power (EIRP) from wireless devices. This is derived from transmit power/"tx power", and is measured in dBm/mBm (1dBm=100mBm) or mW (log scale). In the 2.4GHz band, the maximum is 30dBm in the US and Canada, 20dBm in most of Europe, and 20dBm-30dBm for the rest of the world. In the 5GHz band, maximums are usually lower. Consult the wireless-regdb for more detailed information (EIRP dBm values are in the second set of brackets for each line).

Misconfiguring the regdomain can be useful - for example, by allowing use of an unused channel when other channels are crowded, or by allowing an increase in tx power to widen transmitter range. However, this is not recommended as it could break local laws and cause interference with other radio devices.

The kernel loads the database directly when wireless-regdb is installed. For direct loading, the kernel should, for security's sake, be configured with CONFIG_CFG80211_USE_KERNEL_REGDB_KEYS set to yes to allow for cryptographic verification of the database. This is true of the stock Arch kernel, but if you are using an alternate kernel, or compiling your own, you should verify this. More information is available at this guide[dead link 2024-07-30—domain name not resolved].

To configure the regdomain, install wireless-regdb and reboot, then edit /etc/conf.d/wireless-regdom and uncomment the appropriate domain.

The current regdomain can be temporarily set to the United States with:

However, setting the regdomain may not alter your settings. Some devices have a regdomain set in firmware/EEPROM, which dictates the limits of the device, meaning that setting regdomain in software can only increase restrictions, not decrease them. For example, a CN device could be set in software to the US regdomain, but because CN has an EIRP maximum of 20dBm, the device will not be able to transmit at the US maximum of 30dBm.

For example, to see if the regdomain is being set in firmware for an Atheros device:

For other chipsets, it may help to search for "EEPROM", "regdomain", or simply the name of the device driver.

To see if your regdomain change has been successful, and to query the number of available channels and their allowed transmit power:

wpa_supplicant can also use a regdomain in the country= line of /etc/wpa_supplicant/wpa_supplicant.conf.

It is also possible to configure the cfg80211 kernel module to use a specific regdomain by adding, for example, options cfg80211 ieee80211_regdom=JP as module options. The module option is inherited from the old regulatory implementation and in modern kernels act as a userspace regulatory hint as if it came through nl80211 through utilities like iw and wpa_supplicant.

Many laptops have a hardware button (or switch) to turn off the wireless card; however, the card can also be blocked by the kernel. This can be handled by rfkill(8). To show the current status:

If the card is hard-blocked, use the hardware button (switch) to unblock it. If the card is not hard-blocked but soft-blocked, use the following command:

Hardware buttons to toggle wireless cards are handled by a vendor specific kernel module. Frequently, these are WMI modules. Particularly for very new hardware models, it happens that the model is not fully supported in the latest stable kernel yet. In this case, it often helps to search the kernel bug tracker for information and report the model to the maintainer of the respective vendor kernel module, if it has not happened already.

See Power saving#Network interfaces.

This section contains general troubleshooting tips, not strictly related to problems with drivers or firmware. For such topics, see next section #Troubleshooting drivers and firmware.

If you have problematic hardware and need internet access to, for example, download some software or get help in forums, you can make use of Android's built-in feature for internet sharing via USB cable. See Android tethering#USB tethering for more information.

A good first measure to troubleshoot is to analyze the system's logfiles first. In order not to manually parse through them all, it can help to open a second terminal/console window and watch the kernels messages with

while performing the action, e.g. the wireless association attempt.

When using a tool for network management, the same can be done for systemd with

Frequently, a wireless error is accompanied by a deauthentication with a particular reason code, for example:

Looking up the reason code might give a first hint. Maybe it also helps you to look at the control message flowchart, the journal messages will follow it.

The individual tools used in this article further provide options for more detailed debugging output, which can be used in a second step of the analysis, if required.

This article or section is out of date.

Before changing the channel to auto, make sure your wireless interface is down. After it has successfully changed it, you can bring the interface up again and continue from there.

If you are on a public wireless network that may have a captive portal, make sure to query an HTTP page (not an HTTPS page) from your web browser, as some captive portals only redirect HTTP. If this is not the issue, check if you can resolve domain names, it may be necessary to use the DNS server advertised via DHCP.

Wireless hardware disables RTS and fragmentation by default. These are two different methods of increasing throughput at the expense of bandwidth (i.e. reliability at the expense of speed). These are useful in environments with wireless noise or many adjacent access points, which may create interference leading to timeouts or failing connections.

Packet fragmentation improves throughput by splitting up packets with size exceeding the fragmentation threshold. The maximum value (2346) effectively disables fragmentation since no packet can exceed it. The minimum value (256) maximizes throughput, but may carry a significant bandwidth cost.

RTS improves throughput by performing a handshake with the access point before transmitting packets with size exceeding the RTS threshold. The maximum threshold (2347) effectively disables RTS since no packet can exceed it. The minimum threshold (0) enables RTS for all packets, which is probably excessive for most situations.

If your journal says wlan0: deauthenticating from MAC by local choice (reason=3) and you lose your Wi-Fi connection, it is likely that you have a bit too aggressive power-saving on your Wi-Fi card. Try disabling the wireless card's power saving features (specify off instead of on).

If your card does not support enabling/disabling power save mode, check the BIOS for power management options. Disabling PCI-Express power management in the BIOS of a Lenovo W520 resolved this issue.

If you are experiencing frequent disconnections and your journal shows messages such as

ieee80211 phy0: wlan0: No probe response from AP xx:xx:xx:xx:xx:xx after 500ms, disconnecting

try changing the channel bandwidth to 20MHz through your router's settings page.

On some laptop models with hardware rfkill switches (e.g., Thinkpad X200 series), due to wear or bad design, the switch (or its connection to the mainboard) might become loose over time resulting in seemingly random hardblocks/disconnects when you accidentally touch the switch or move the laptop. There is no software solution to this, unless your switch is electrical and the BIOS offers the option to disable the switch. If your switch is mechanical (and most are), there are lots of possible solutions, most of which aim to disable the switch: Soldering the contact point on the mainboard or Wi-Fi card, gluing or blocking the switch, using a screw nut to tighten the switch or removing it altogether.

Another cause for frequent disconnects or a complete failure to connect may also be a sub-standard router, incomplete settings of the router, interference by other wireless devices or low quality signal.

To troubleshoot, first try to connect to the router with no authentication and by getting closer to it. If it does not work, reboot the router and try with another device first.

If that works, enable WPA/WPA2 again but choose fixed and/or limited router settings. For example:

On some wireless network adapters (e.g. Qualcomm Atheros AR9485), random disconnects can happen with a DMA error:

A possible workaround is to disable the Intel IOMMU driver (DMA), adding intel_iommu=off to the kernel parameters [4].

If you are using a device with iwlwifi and iwlmvm for wireless connectivity, and your Wi-Fi card appears to disappear when on battery power (perhaps after a reboot or resuming from suspend), this can be fixed by configuring power saving settings in iwlmvm.

Create the file /etc/modprobe.d/iwlmvm.conf if it does not exist already, then add the following line to it:

A power_scheme of 1 sets iwlmvm to "Always Active." Available options are:

This fix was discovered at [5].

If your device undergoes long periods of inactivity (e.g. a file server), the disconnection may be due to power saving, which will block incoming traffic and prevent connections. Try disabling power saving for the interface:

You can create a udev rule to do this on boot, see Power management#Network interfaces.

If you notice occasional interruptions when connected to a mesh network (e.g., Wi-Fi 6) and notice a message such as:

You are experiencing roaming issues. Depending on your mean of connection and the issue at hand, one could:

If the computer's Wi-Fi channels do not match those of the user's country, some in-range Wi-Fi networks might be invisible because they use wireless channels that are not allowed by default. The solution is to configure the regulatory domain correctly; see #Respecting the regulatory domain.

This section covers methods and procedures for installing kernel modules and firmware for specific chipsets, that differ from generic method.

See Kernel modules for general information on operations with modules.

Some chipsets require additional firmware: linux-firmware-mediatek

Unified driver for Ralink chipsets (it replaces rt2500, rt61, rt73, etc). This driver has been in the Linux kernel since 2.6.24, you only need to load the right module for the chip: rt2400pci, rt2500pci, rt2500usb, rt61pci or rt73usb which will autoload the respective rt2x00 modules too.

A list of devices supported by the modules is available at the project's homepage.

For devices which use the rt3090 chipset, it should be possible to use the rt2800pci driver; however, it does not work with this chipset very well (e.g. sometimes it is not possible to use higher rate than 2Mb/s).

The rt3290 chipset is recognised by the kernel rt2800pci module. However, some users experience problems and reverting to a patched Ralink driver seems to be beneficial in these cases.

New chipset as of 2012. It may require proprietary drivers from Ralink. Different manufacturers use it; see the Belkin N750 DB wireless usb adapter forums thread.

New chipset as of 2014, released under their new commercial name MediaTek. It is an AC1200 or AC1300 chipset. Manufacturer provides drivers for Linux on their support page. As of kernel 5.5 it should be supported by the included mt76 driver.

DFS channels are currently not supported in 5 GHz AP mode.

There are some high latency problems with these MediaTek chipsets. To fix this, the only solution is to disable ASPM:

This configuration file will take effect on next reboot or after reloading the module with modprobe:

These are also sometimes branded as AMD RZ608 (mt7921) and RZ616 (mt7922).

This article or section is out of date.

See [7] for a list of Realtek chipsets and specifications.

The driver is now in the kernel, but many users have reported being unable to make a connection although scanning for networks does work.

8192cu-dkmsAUR includes many patches; try this if it does not work fine with the driver in kernel.

The rtl8723ae and rtl8723be modules are included in the mainline Linux kernel.

Some users may encounter errors with powersave on this card. This is shown with occasional disconnects that are not recognized by high level network managers (netctl, NetworkManager). This error can be confirmed by running dmesg -w as root or journalctl -f as root and looking for output related to powersave and the rtl8723ae/rtl8723be module. If you have this issue, use the fwlps=0 kernel module parameter which should prevent the Wi-Fi card from automatically sleeping and halting connection.

If you have poor signal, perhaps your device has only one physical antenna connected, and antenna autoselection is broken. You can force the choice of antenna with ant_sel=1 or ant_sel=2 kernel option. [8]

Realtek chipsets rtl8811au, rtl8812au, rtl8814au and rtl8821au designed for various USB adapters ranging from AC600 to AC1900. Several packages provide various kernel drivers, these require DKMS (the dkms package and the kernel headers installed):

rtl8821cu-dkms-gitAUR provides a kernel module for the Realtek 8811cu and 8821cu chipset.

This requires DKMS, so make sure you have your proper kernel headers installed.

If no wireless interface shows up even though the 8821cu module is loaded, you may need to manually specify the rtw_RFE_type kernel module parameter [9][10]. Try e.g. rtw_RFE_type=0x26, other values might also work.

rtl8821ce-dkms-gitAUR provides a kernel module for the Realtek 8821ce chipset found in the Asus X543UA.

This requires DKMS, so make sure you have your proper kernel headers installed.

rtl88x2bu-dkms-gitAUR provides a kernel module for the Realtek 8822bu chipset found in the Edimax EW7822ULC USB3, Asus AC53 Nano USB 802.11ac and TP-Link Archer T3U adapter.

This requires DKMS, so make sure you have your proper kernel headers installed.

This article or section needs expansion.

Issues with the rtl8xxxu mainline kernel module may be solved by compiling a third-party module for the specific chipset. The source code can be found in GitHub repositories.

Some drivers may be already prepared in the AUR, e.g. rtl8723bu-dkms-gitAUR, rtl8852au-dkms-gitAUR, rtl8852bu-dkms-gitAUR, rtl8852cu-dkms-gitAUR.

RWT88 kernel module is included in all officially supported Arch Linux kernels. The number of supported devices grew over time, currently it supports most RTW88 chip devices if configured and compiled to do so.

As of Linux 6.10.3, the driver supports: 882BE (possibly), 8703B, 8723CS, 8723D, 8723DE, 8723DS, 8723DU, 8723X, 8821C, 8821CE, 8821CS, 8821CU, 8822B, 8822BE, 8822BS, 8822BU, 8822C, 8822CE, 8822CS, 8822CU.

To get more up-to-date list, Ctrl+F CONFIG_RTW88_ linux's config or check out wireless-next upstream.

Make sure that wireless-regdom is configured. Otherwise, you will be able to see all Wi-Fi networks, but will not be able to connect. Out-of-tree driver rtl88x2bu-dkms-gitAUR can connect without such configuration, so it's important to set regulatory domain when switching from it.

Here is how those symptoms look in dmesg:

The RTW89 kernel module has been merged into the upstream kernel and provides support for newer Realtek wireless chipsets.

This driver supports: 8852AE, 8851BE, 8852BE, and 8852CE.

On some computers, you may experience unstable connections. It seems like a common issue on late models from HP and Lenovo. Try disabling ASPM-related features using the config below.

There are different drivers for devices with Atheros chipset:

There are some other drivers for some Atheros devices. See Linux Wireless documentation for details.

If you find web pages randomly loading very slow, or if the device is unable to lease an IP address, try to switch from hardware to software encryption by loading the ath5k module with nohwcrypt=1 option. See Kernel modules#Setting module options for details.

Some laptops may have problems with their wireless LED indicator flickering red and blue. To solve this problem, do:

For alternatives, see this bug report.

As of Linux 3.15.1, some users have been experiencing a decrease in bandwidth. In some cases, this can fixed by setting the nohwcrypt=1 kernel module parameter for the ath9k module.

Although Linux Wireless says that dynamic power saving is enabled for Atheros ath9k single-chips newer than AR9280, for some devices (e.g. AR9285), powertop might still report that power saving is disabled. In this case, enable it manually.

On some devices (e.g. AR9285), enabling the power saving might result in the following error:

The solution is to set the ps_enable=1 kernel module parameter for the ath9k module.

iwlegacy is the wireless driver for Intel's 3945 and 4965 wireless chips. The firmware is included in the linux-firmware package.

udev should load the driver automatically, otherwise load iwl3945 or iwl4965 manually. See Kernel modules for details.

If you have problems connecting to networks in general (e.g. random failures with your card on bootup or your link quality is very poor), try to disable 802.11n:

iwlwifi is the wireless driver for Intel's current wireless chips, such as 5100AGN, 5300AGN, and 5350AGN. See the full list of supported devices.

If you have problems connecting to networks in general or your link quality is very poor, try to disable 802.11n, and perhaps also enable software encryption:

If you have a problem with slow uplink speed you may try disabling power saving for your wireless adapter.

If you have an 802.11ax (Wi-Fi 6) access point and have problems detecting the beacons or an unreliable connection, review Intel Article 54799.

If you have difficulty connecting a bluetooth headset and maintaining good downlink speed, try disabling Bluetooth coexistence:

Make sure your firmware is fully updated before trying anything else.

You may have some issue where the driver outputs stack traces & errors, which can cause some stuttering.

Alternatively, you may simply experience miscellaneous issues (e.g. connection issues on 5GHz, random disconnections, no connection on resume).

To confirm it is the cause of the issues, downgrade the package linux-firmware.

If confirmed, move the buggy firmware files so that an older version is loaded (to be able to have an up to date linux-firmware since it is not only providing firmware updates for your Intel Wi-Fi card):

To avoid having to repeat these steps manually after each update, use the NoExtract and NoUpgrade arrays in pacman.conf with a wildcard to block their installation.

If the Wi-Fi adapter is not getting detected after finishing a session in Windows, this might be due to Windows' Fast Startup feature which is enabled by default. Try disabling Fast Startup. The iwlwifi kernel driver wiki has an entry for this.

The default settings on the module are to have the LED blink on activity. Some people find this extremely annoying. To have the LED on solid when Wi-Fi is active, you can use the systemd-tmpfiles:

Run systemd-tmpfiles --create phy0-led.conf for the change to take effect, or reboot.

To see all the possible trigger values for this LED:

The aic8800-dkmsAUR package should be used with these devices. These drivers are out of the mainline Linux kernel and require DKMS.

For this chip variant, aic8800d80-dkmsAUR package should be used instead of the one mentioned above.

See Broadcom wireless.

Treat this Tenda card as an rt2870sta device. See #rt2x00.

This should be a part of the kernel package and be installed already.

Some Orinoco chipsets are Hermes II. You can use the wlags49_h2_cs driver instead of orinoco_cs and gain WPA support. To use the driver, blacklist orinoco_cs first.

The driver p54 is included in kernel, but you have to download the appropriate firmware for your card from this site and install it into the /usr/lib/firmware directory.

zd1211rw is a driver for the ZyDAS ZD1211 802.11b/g USB WLAN chipset, and it is included in recent versions of the Linux kernel. See [12] for a list of supported devices. You only need to install the firmware for the device, provided by the zd1211-firmwareAUR package.

Host AP is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3 chipset. The driver is included in Linux kernel.

Ndiswrapper is a wrapper script that allows you to use some Windows drivers in Linux. You will need the .inf and .sys files from your Windows driver.

Follow these steps to configure ndiswrapper.

The ndiswrapper install is almost finished; you can load the module at boot.

Test that ndiswrapper will load now:

See Network configuration#Listing network interfaces for more assurance the wireless interface now exists.

If you have problems, some help is available at: ndiswrapper howto and ndiswrapper FAQ.

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -knnd ::0280
```

Example 2 (unknown):
```unknown
00:14.3 Network controller [0280]: Intel Corporation BE201 320MHz [8086:a840] (rev 10)
	Subsystem: Intel Corporation Device [8086:00e4]
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
```

Example 3 (unknown):
```unknown
dmesg | grep usbcore
```

Example 4 (unknown):
```unknown
usbcore: registered new interface driver rtl8187
```

---

## Preboot Execution Environment

**URL:** https://wiki.archlinux.org/title/PXE

**Contents:**
- Preparation
  - Overview
  - Boot from install medium
  - Boot from netboot
- Pixiecore
- Server setup
  - Network
  - DHCP + TFTP
    - BIOS boot from install medium
    - UEFI boot from netboot

From Wikipedia:Preboot Execution Environment:

In this guide, PXE is used to boot the installation medium with an appropriate option ROM that supports PXE on the target. This works well when you already have a server set up.

It is useful to give an overview of the PXE boot process in order to understand the #Server setup, the #Installation on the client side and the Arch Linux files needed.

The client starts by broadcasting packets asking for a DHCP server and containing specific PXE options. The DHCP server responds with networking information (the IP address assigned to the client) and also provides, by using specific bootstrap protocol (BOOTP) parameters of the DHCP, additional information like the TFTP server address, the path of the initial network bootstrap program (NBP) to download or the boot configuration file name.

The NBP is transferred from the PXE server to the client using TFTP, to be loaded into memory and executed. The kernel and the initramfs are also transferred this way.

Then the root file system is transferred using one of the following protocols: HTTP, NFS or NBD.

In order to gather the files that will be transferred from the server to the client for booting, get the latest official install image from the download page.

Next mount the image:

where release_date is the release date in the ISO filename like, e.g., 2022.10.01.

Arch Linux netboot images can be used to download the latest Arch Linux release on the fly upon system boot. Download the image compatible with your configuration.

An all-in-one solution is provided by pixiecore

You will need to setup a DHCP server, a TFTP server for transferring the NBP and one of the following services for transferring the root file system: HTTP server, NFS or NBD.

Bring up your wired network adapter, and assign it an address appropriately.

You can also use one of the network managers to configure the static IP.

You will need both a DHCP server and a TFTP server to configure networking on the install target and to facilitate the transfer of files between the server and the client. dnsmasq does both, and is extremely easy to set up.

Install the dnsmasq package.

dnsmasq needs to be configured. See instructions on how to setup a dnsmasq#TFTP server and a dnsmasq#PXE server.

Are provided below some common configuration instructions. tftp_root is the directory where the Arch ISO is mounted (e.g. /mnt/archiso) or where the network boot program is located.

To enable the DHCP server and give IPv4 addresses within a range, add to the configuration file a line similar to:

Or in case there is already a DHCP-server running on the network and you want to interoperate with it, see dnsmasq#Proxy DHCP.

Two examples covering different boot style and installation media are provided below.

Once configured according to your needs, start dnsmasq.service.

The path of the initial bootstrap program to be transferred is defined with the dhcp-boot option in the configuration file.

In order to send specific bootstrap protocol (BOOTP) parameters, like the configuration file path, the dhcp-option-force=flag,value line is used.

To send a file depending on the architecture, here the netboot image for UEFI-style boot, use:

If using netboot, the rest of the server setup section which focuses on the Arch ISO does not apply.

Thanks to archiso_pxe_http, archiso_pxe_nfs and archiso_pxe_nbd initcpio hooks in archiso, it is possible to boot using HTTP, NFS or NBD. Boot time is approximately the same in all three methods, but HTTP method allows you to watch a state of downloading airootfs.sfs in percents.

Among all alternatives, darkhttpd is by far the most trivial to setup (and the lightest-weight).

First, install the darkhttpd package.

Then start darkhttpd using our /mnt/archiso as the document root:

You will need to set up an NFS server with an export at the root of your mounted installation medium, which would be /mnt/archiso if you followed #Preparation. After setting up the server, add the following line to your /etc/exports file:

If the server was already running, re-export the file systems with exportfs -r -a -v.

The default settings in the installer expect to find the NFS at /run/archiso/bootmnt/, so you will need to edit the boot options. To do this, press Tab on the appropriate boot menu choice and edit the archiso_nfs_srv option accordingly:

Alternatively, you can use /run/archiso/bootmnt for the entire process.

After the kernel loads, the Arch bootstrap image will copy the root file system via NFS to the booting host. This can take a little while. Once this completes, you should have a running system.

Install the nbd package and configure it:

where release_date is the release date in the ISO filename like, e.g., 2022.10.01.

If you have an existing PXE server with a PXELINUX system setup (e.g. a combination of DHCP and TFTP), you can add the following menu items to your /tftpboot/pxelinux.cfg/default file in order to boot Arch via your preferred method.

Since PXELINUX supports HTTP, only the boot loader needs to be transferred over TFTP, everything else can use HTTP. E.g.:

For NFS and NBD, the kernel and initramfs must be downloaded from TFTP. E.g., for NFS:

The LINUX and INITRD paths are relative to TFTP root. For NBD, replace archiso_nfs_srv with archiso_nbd_srv in the above example. See usage examples in boot/syslinux/archiso_pxe.cfg file resided on Arch Linux ISO.

Whichever method you choose, you must pass ip= parameter to instruct the kernel to bring up the network interface before it attempts to mount the installation medium over the network. Passing BOOTIF= is required when there are several wired interfaces on the client side and/or you want resolv.conf to be already configured inside booted archiso. You can use sysappend mask 3 (which is 1+2) to pass these parameters automatically. For available boot parameters see README.bootparams.

For this portion you will need to figure out how to tell the client to attempt a PXE boot; in the corner of the screen along with the normal post messages, usually there will be some hint on which key to press to try PXE booting first. On an IBM x3650 F12 brings up a boot menu, the first option of which is Network; on a Dell PE 1950/2950 pressing F12 initiates PXE booting directly.

Looking at journald on the PXE server will provide some additional insight to what exactly is going on during the early stages of the PXE boot process:

After you load pxelinux.0 and archiso.cfg via TFTP, you will (hopefully) be presented with a syslinux boot menu with several options, where you can select Boot Arch Linux (x86_64) (HTTP).

Next the kernel and initramfs (appropriate for the architecture you selected) will be transferred, again via TFTP:

If all goes well, you should then see activity on darkhttpd coming from the PXE-target; at this point the kernel would be loaded on the PXE-target, and in init:

After the root file system is downloaded via HTTP, you will eventually end up at the normal live system root zsh prompt.

Unless you want all traffic to be routed through your PXE server (which will not work anyway unless you set it up properly), you will want to stop dnsmasq.service and get a new lease on the install target, as appropriate for your network layout.

You can also kill darkhttpd; the target has already downloaded the root file system, so it is no longer needed. While you are at it, you can also unmount the installation image:

At this point you can follow the Installation guide.

The copytoram initramfs option can be used to control whether the root file system should be copied to ram in its entirety in early-boot.

It highly recommended to leave this option alone, and should only be disabled if entirely necessary (systems with less than ~256MB physical memory). Append copytoram=n to your kernel line if you wish to do so.

If your network for PXE clients is private (for example, 192.168.1.0/24), and you want them to be able to access internet (for example, for packages installation), you should configure masquerade/source nat properly. Your PXE server must have a separate NIC connected to the internet. You can use such command to pass through the internet to clients:

To make this rule persistent after reboot, run the following command:

and enable iptables.service.

See Simple stateful firewall#Setting up a NAT gateway and Internet sharing#Enable NAT for more information.

FS#36749 causes default predictable network interface renaming to fail and then DHCP client to fail because of it. A workaround is to add the kernel boot parameter net.ifnames=0 to disable predictable interface names.

When using VirtualBox to test your configuration, the virtual machine may get stuck at:

While PXE booting with a real machine works fine. The problem may be because you have set several CPU cores to your client machine, and you set its type as Other and version as Other/Unknown (64 bit). So VirtualBox does not know which paravirtualization interface to use by default.

Adding loglevel=7 to the kernel parameters lets you see where it actually got stuck:

To resolve this, either use one CPU core, or go to Machine > Settings > System > Acceleration and set one of the following paravirtualization interface: Minimal, Hyper-V or KVM.

**Examples:**

Example 1 (unknown):
```unknown
# mount --mkdir -o loop,ro archlinux-release_date-x86_64.iso /mnt/archiso
```

Example 2 (unknown):
```unknown
release_date
```

Example 3 (unknown):
```unknown
pixiecore quick arch --dhcp-no-bind
```

Example 4 (unknown):
```unknown
# ip link set eth0 up
# ip addr add 192.168.0.1/24 dev eth0
```

---

## Preboot Execution Environment

**URL:** https://wiki.archlinux.org/title/Archiso_as_pxe_server

**Contents:**
- Preparation
  - Overview
  - Boot from install medium
  - Boot from netboot
- Pixiecore
- Server setup
  - Network
  - DHCP + TFTP
    - BIOS boot from install medium
    - UEFI boot from netboot

From Wikipedia:Preboot Execution Environment:

In this guide, PXE is used to boot the installation medium with an appropriate option ROM that supports PXE on the target. This works well when you already have a server set up.

It is useful to give an overview of the PXE boot process in order to understand the #Server setup, the #Installation on the client side and the Arch Linux files needed.

The client starts by broadcasting packets asking for a DHCP server and containing specific PXE options. The DHCP server responds with networking information (the IP address assigned to the client) and also provides, by using specific bootstrap protocol (BOOTP) parameters of the DHCP, additional information like the TFTP server address, the path of the initial network bootstrap program (NBP) to download or the boot configuration file name.

The NBP is transferred from the PXE server to the client using TFTP, to be loaded into memory and executed. The kernel and the initramfs are also transferred this way.

Then the root file system is transferred using one of the following protocols: HTTP, NFS or NBD.

In order to gather the files that will be transferred from the server to the client for booting, get the latest official install image from the download page.

Next mount the image:

where release_date is the release date in the ISO filename like, e.g., 2022.10.01.

Arch Linux netboot images can be used to download the latest Arch Linux release on the fly upon system boot. Download the image compatible with your configuration.

An all-in-one solution is provided by pixiecore

You will need to setup a DHCP server, a TFTP server for transferring the NBP and one of the following services for transferring the root file system: HTTP server, NFS or NBD.

Bring up your wired network adapter, and assign it an address appropriately.

You can also use one of the network managers to configure the static IP.

You will need both a DHCP server and a TFTP server to configure networking on the install target and to facilitate the transfer of files between the server and the client. dnsmasq does both, and is extremely easy to set up.

Install the dnsmasq package.

dnsmasq needs to be configured. See instructions on how to setup a dnsmasq#TFTP server and a dnsmasq#PXE server.

Are provided below some common configuration instructions. tftp_root is the directory where the Arch ISO is mounted (e.g. /mnt/archiso) or where the network boot program is located.

To enable the DHCP server and give IPv4 addresses within a range, add to the configuration file a line similar to:

Or in case there is already a DHCP-server running on the network and you want to interoperate with it, see dnsmasq#Proxy DHCP.

Two examples covering different boot style and installation media are provided below.

Once configured according to your needs, start dnsmasq.service.

The path of the initial bootstrap program to be transferred is defined with the dhcp-boot option in the configuration file.

In order to send specific bootstrap protocol (BOOTP) parameters, like the configuration file path, the dhcp-option-force=flag,value line is used.

To send a file depending on the architecture, here the netboot image for UEFI-style boot, use:

If using netboot, the rest of the server setup section which focuses on the Arch ISO does not apply.

Thanks to archiso_pxe_http, archiso_pxe_nfs and archiso_pxe_nbd initcpio hooks in archiso, it is possible to boot using HTTP, NFS or NBD. Boot time is approximately the same in all three methods, but HTTP method allows you to watch a state of downloading airootfs.sfs in percents.

Among all alternatives, darkhttpd is by far the most trivial to setup (and the lightest-weight).

First, install the darkhttpd package.

Then start darkhttpd using our /mnt/archiso as the document root:

You will need to set up an NFS server with an export at the root of your mounted installation medium, which would be /mnt/archiso if you followed #Preparation. After setting up the server, add the following line to your /etc/exports file:

If the server was already running, re-export the file systems with exportfs -r -a -v.

The default settings in the installer expect to find the NFS at /run/archiso/bootmnt/, so you will need to edit the boot options. To do this, press Tab on the appropriate boot menu choice and edit the archiso_nfs_srv option accordingly:

Alternatively, you can use /run/archiso/bootmnt for the entire process.

After the kernel loads, the Arch bootstrap image will copy the root file system via NFS to the booting host. This can take a little while. Once this completes, you should have a running system.

Install the nbd package and configure it:

where release_date is the release date in the ISO filename like, e.g., 2022.10.01.

If you have an existing PXE server with a PXELINUX system setup (e.g. a combination of DHCP and TFTP), you can add the following menu items to your /tftpboot/pxelinux.cfg/default file in order to boot Arch via your preferred method.

Since PXELINUX supports HTTP, only the boot loader needs to be transferred over TFTP, everything else can use HTTP. E.g.:

For NFS and NBD, the kernel and initramfs must be downloaded from TFTP. E.g., for NFS:

The LINUX and INITRD paths are relative to TFTP root. For NBD, replace archiso_nfs_srv with archiso_nbd_srv in the above example. See usage examples in boot/syslinux/archiso_pxe.cfg file resided on Arch Linux ISO.

Whichever method you choose, you must pass ip= parameter to instruct the kernel to bring up the network interface before it attempts to mount the installation medium over the network. Passing BOOTIF= is required when there are several wired interfaces on the client side and/or you want resolv.conf to be already configured inside booted archiso. You can use sysappend mask 3 (which is 1+2) to pass these parameters automatically. For available boot parameters see README.bootparams.

For this portion you will need to figure out how to tell the client to attempt a PXE boot; in the corner of the screen along with the normal post messages, usually there will be some hint on which key to press to try PXE booting first. On an IBM x3650 F12 brings up a boot menu, the first option of which is Network; on a Dell PE 1950/2950 pressing F12 initiates PXE booting directly.

Looking at journald on the PXE server will provide some additional insight to what exactly is going on during the early stages of the PXE boot process:

After you load pxelinux.0 and archiso.cfg via TFTP, you will (hopefully) be presented with a syslinux boot menu with several options, where you can select Boot Arch Linux (x86_64) (HTTP).

Next the kernel and initramfs (appropriate for the architecture you selected) will be transferred, again via TFTP:

If all goes well, you should then see activity on darkhttpd coming from the PXE-target; at this point the kernel would be loaded on the PXE-target, and in init:

After the root file system is downloaded via HTTP, you will eventually end up at the normal live system root zsh prompt.

Unless you want all traffic to be routed through your PXE server (which will not work anyway unless you set it up properly), you will want to stop dnsmasq.service and get a new lease on the install target, as appropriate for your network layout.

You can also kill darkhttpd; the target has already downloaded the root file system, so it is no longer needed. While you are at it, you can also unmount the installation image:

At this point you can follow the Installation guide.

The copytoram initramfs option can be used to control whether the root file system should be copied to ram in its entirety in early-boot.

It highly recommended to leave this option alone, and should only be disabled if entirely necessary (systems with less than ~256MB physical memory). Append copytoram=n to your kernel line if you wish to do so.

If your network for PXE clients is private (for example, 192.168.1.0/24), and you want them to be able to access internet (for example, for packages installation), you should configure masquerade/source nat properly. Your PXE server must have a separate NIC connected to the internet. You can use such command to pass through the internet to clients:

To make this rule persistent after reboot, run the following command:

and enable iptables.service.

See Simple stateful firewall#Setting up a NAT gateway and Internet sharing#Enable NAT for more information.

FS#36749 causes default predictable network interface renaming to fail and then DHCP client to fail because of it. A workaround is to add the kernel boot parameter net.ifnames=0 to disable predictable interface names.

When using VirtualBox to test your configuration, the virtual machine may get stuck at:

While PXE booting with a real machine works fine. The problem may be because you have set several CPU cores to your client machine, and you set its type as Other and version as Other/Unknown (64 bit). So VirtualBox does not know which paravirtualization interface to use by default.

Adding loglevel=7 to the kernel parameters lets you see where it actually got stuck:

To resolve this, either use one CPU core, or go to Machine > Settings > System > Acceleration and set one of the following paravirtualization interface: Minimal, Hyper-V or KVM.

**Examples:**

Example 1 (unknown):
```unknown
# mount --mkdir -o loop,ro archlinux-release_date-x86_64.iso /mnt/archiso
```

Example 2 (unknown):
```unknown
release_date
```

Example 3 (unknown):
```unknown
pixiecore quick arch --dhcp-no-bind
```

Example 4 (unknown):
```unknown
# ip link set eth0 up
# ip addr add 192.168.0.1/24 dev eth0
```

---

## Lenovo ThinkPad T480

**URL:** https://wiki.archlinux.org/title/Lenovo_ThinkPad_T480

**Contents:**
- TrackPoint and Touchpad
- Power management/Throttling issues
  - CPU stuck at minimum frequency
- Firmware
- Screen backlight
- Encryption and keyboard
- Fingerprint reader
- Function keys
  - Special buttons

This article or section does not follow the Laptop page guidelines.

This article covers the installation and configuration of Arch Linux on a Lenovo T480 laptop. Everything seems to work pretty much out the box.

For a general overview of laptop-related articles and recommendations, see Laptop.

TrackPoint and Touchpad work out of the box and do not seem to have the same issues as the X1 Carbon Gen 6.

However one could benefit from having greatly increased event reporting frequency by enabling psmouse kernel module option synaptics_intertouch=1.

This can be made permanent with:

For two-finger scrolling activity this gives a boost from 40 Hz to 135 Hz on average which is more than threefold increase. This boost greatly contributes to the Desktop environment scrolling performance and smoothness.

(evhz-gitAUR) may be of use to find out how frequently Touchpad reports events. For example after enabling said option:

Note that units adorned with the "glass Touchpad mod" [1] [2] will not benefit from the elevated Touchpad performance with the procedure above. Running evhz will also indicate a different Touchpad identifier:

Due to missing Intel Dynamic Platform and Thermal Framework (DPTF) support for Linux, a feature which should detect whether the laptop is used on a desk or on the lap so it can throttle the CPU in the latter case to reduce the temperature is not working and the CPU is always throttled. An Lenovo employee explained the situation and the solution Lenovo is building in a PDF posted in their forum (archive.org backup of the PDF). The firmware and EFI fixes have been released for a different model and Lenovo has recognized that the T480 is affected, so there is hope the T480 will get the fix too.

An interim fix is throttled (Github).

A signal called BD PROCHOT inside the laptop can force the CPU to the lowest power state (400 MHz in case of the T470s) regardless of the governor. This is meant to protect the system and can be triggered by many reasons -- the CPU temperature rising above 60 °C, using a third party battery... Luckily, it can be ignored by writing a value to a register [3]. This script is an alternative to the app ThrottleStop on Windows. Install msr-tools and execute this script after every boot (or make a systemd Oneshot service).

Lenovo provides firmware updates for this device through the Linux Vendor Firmware Service (LVFS).

Available updates and changelogs can be found on the LVFS website. These include security patches for the Intel Management Engine and the system firmware.

The updates can be installed using fwupd.

Without the intel driver (xf86-video-intel), neither xbacklight or xrandr brightness control are working.

However, the package acpilightAUR provides a drop-in replacement for xbacklight. Apart from installing the package (which conflicts with xorg-xbacklight), you have to add your user to the video group and add the following udev rule:

This allows you to control the backlight with xbacklight command provided by acpilight, as well as control the various LEDs on your T480.

Assuming encrypted installation, during boot process you are prompted to enter password to decrypt disk. In some cases you may not be able to enter password, because at this time keyboard driver is not loaded yet.

To fix this, add the atkbd module to the mkinitcpio MODULES array:

Regenerate the initramfs afterwards.

Install python-validityAUR and register fingerprints with:

Refer, for example, to the entry on fingerprint sensor of the similar Lenovo ThinkPad X270 for general procedures if list_devices failed is returned. You might also try referring to these steps, which are nominally for Fedora but which appear to work on Arch as well.

The factual accuracy of this article or section is disputed.

Some special buttons are not supported by X server due to keycode number limit. Certain keys are also handled by other devices other than the keyboard.

See Laptop/Lenovo#Special buttons.

**Examples:**

Example 1 (unknown):
```unknown
synaptics_intertouch=1
```

Example 2 (unknown):
```unknown
/etc/modprobe.d/psmouse.conf
```

Example 3 (unknown):
```unknown
options psmouse synaptics_intertouch=1
```

Example 4 (unknown):
```unknown
Press CTRL-C to exit.
...
^C
Average for Synaptics TM3276-022:   137Hz
```

---

## GRUB/Tips and tricks

**URL:** https://wiki.archlinux.org/title/GRUB/Tips_and_tricks

**Contents:**
- Alternative installation methods
  - Install to external USB stick
    - BIOS
    - EFI
  - Install to partition or partitionless disk
  - Generate core.img alone
- GUI configuration tools
- drop-in configuration
- Visual configuration
  - Setting the framebuffer resolution

Assume your USB stick's first partition is FAT32 and its partition is /dev/sdy1

Optionally backup configuration files of grub.cfg:

For removable installations you have to use --removable and specify both --boot-directory and --efi-directory. [1]

To set up grub to a partition boot sector, to a partitionless disk (also called superfloppy) or to a floppy disk, run (using for example /dev/sdaX as the /boot partition):

You need to use the --force option to allow usage of blocklists and should not use --grub-setup=/bin/true (which is similar to simply generating core.img).

grub-install will give out warnings like which should give you the idea of what might go wrong with this approach:

Without --force you may get the below error and grub-setup will not setup its boot code in the partition boot sector:

With --force you should get:

The reason why grub-setup does not by default allow this is because in case of partition or a partitionless disk is that GRUB relies on embedded blocklists in the partition bootsector to locate the /boot/grub/i386-pc/core.img file and the prefix directory /boot/grub. The sector locations of core.img may change whenever the file system in the partition is being altered (files copied, deleted etc.). For more info, see https://bugzilla.redhat.com/show_bug.cgi?id=728742 and https://bugzilla.redhat.com/show_bug.cgi?id=730915.

The workaround for this is to set the immutable flag on /boot/grub/i386-pc/core.img (using chattr command as mentioned above) so that the sector locations of the core.img file in the disk is not altered. The immutable flag on /boot/grub/i386-pc/core.img needs to be set only if GRUB is installed to a partition boot sector or a partitionless disk, not in case of installation to MBR or simple generation of core.img without embedding any bootsector (mentioned above).

Unfortunately, the grub.cfg file that is created will not contain the proper UUID in order to boot, even if it reports no errors. see https://bbs.archlinux.org/viewtopic.php?pid=1294604#p1294604. In order to fix this issue the following commands:

Now, install linux, then:

To populate the /boot/grub directory and generate a /boot/grub/i386-pc/core.img file without embedding any GRUB bootsector code in the MBR, post-MBR region, or the partition bootsector, add --grub-setup=/bin/true to grub-install:

You can then chainload GRUB's core.img from GRUB Legacy or syslinux as a Linux kernel or as a multiboot kernel (see also Syslinux#Chainloading).

Instead of editing /boot/grub/grub.cfg configuration file, it's possible to use your custom settings as drop-in file like /etc/default/grub.d/00-custom.cfg. Note that you have to create /etc/default/grub.d/ drop-in directory manually. Do not confuse this directory with /etc/grub.d/.

In GRUB it is possible, by default, to change the look of the menu. Make sure to initialize the GRUB graphical terminal, gfxterm, in /etc/default/grub:

GRUB can set the framebuffer for both GRUB itself (GFXMODE) and the kernel (GFXPAYLOAD). The old vga= way is deprecated. The preferred method is editing /etc/default/grub to set width (pixels) x height (pixels) x color depth:

Multiple resolutions can be specified, including the default auto, so it is recommended that you edit the line to resemble GRUB_GFXMODE=desired_resolution,fallback_such_as_1024x768,auto. For more information, refer to the GRUB gfxmode documentation. The gfxpayload property will make sure the kernel keeps the resolution.

If this method does not work for you, the deprecated vga= method will still work. Just add it next to the "GRUB_CMDLINE_LINUX_DEFAULT=" line in /etc/default/grub for example: "GRUB_CMDLINE_LINUX_DEFAULT="quiet splash vga=792" will give you a 1024x768 resolution.

GRUB comes with support for background images and bitmap fonts in pf2 format. The GNU Unifont font is included in the grub package under the filename unicode.pf2, or, as only ASCII characters under the name ascii.pf2. Run pacman -Ql grub | grep pf2 to get the file paths.

Image formats supported include JPEG, PNG and TGA, providing the correct modules are loaded. The maximum supported resolution depends on your hardware.

Make sure you have set up the proper framebuffer resolution.

Edit /etc/default/grub like this:

Re-generate grub.cfg to apply the changes. If adding the splash image was successful, the user will see "Found background image..." in the terminal as the command is executed. If this phrase is not seen, the image information was probably not incorporated into the grub.cfg file.

If the image is not displayed, check:

Here is an example for configuring Starfield theme which was included in GRUB package.

Edit /etc/default/grub:

Re-generate grub.cfg to apply the changes. If configuring the theme was successful, you will see Found theme: /usr/share/grub/themes/starfield/theme.txt in the terminal.

Your splash image will usually not be displayed when using a theme.

If the theme path may be inaccessible (e.g. due to encryption or an unavailable partition), copy it to /boot/grub/themes/ or install it using grub-install --themes=theme_names ....

You can set the menu colors in GRUB. The available colors for GRUB can be found in the GRUB Manual. Here is an example:

Edit /etc/default/grub:

One of the unique features of GRUB is hiding/skipping the menu and showing it by holding Esc when needed. You can also adjust whether you want to see the timeout counter.

Edit /etc/default/grub as you wish. Here are the lines you need to add to enable this feature, the timeout has been set to five seconds and to be shown to the user:

GRUB_TIMEOUT is how many seconds before displaying menu.

Users who use NVIDIA proprietary driver might wish to disable GRUB's framebuffer as it can cause problems with the binary driver.

To disable framebuffer, edit /etc/default/grub and uncomment the following line:

Another option if you want to keep the framebuffer in GRUB is to revert to text mode just before starting the kernel. To do that modify the variable in /etc/default/grub:

This article or section is being considered for removal.

grub-mkconfig utilizes gettext for translations. The language used is determined by the Locale#Variables.

You can temporarily override the Locale when running grub-mkconfig to generate config in a specific language, for example English (C locale):

GRUB supports booting from ISO images directly via loopback devices, see Multiboot USB drive#Using GRUB and loopback devices for examples.

If you want to secure GRUB so it is not possible for anyone to change boot parameters or use the command line, you can add a username and password to GRUB's configuration files. To do this, run the command grub-mkpasswd-pbkdf2, then enter a password and confirm it:

Then, adjust permissions on /etc/grub.d/40_custom such that only root can read it by running chmod o-r /etc/grub.d/40_custom. Then modify the file as following:

where password-hash is the string starting with grub.pbkdf2 generated by grub-mkpasswd_pbkdf2.

Regenerate your configuration file with grub-mkconfig. Accessing the GRUB command line, boot parameters and also booting an entry now require the specified username and password. The latter can be prevented by following #Password protection of GRUB edit and console options only.

This can be relaxed and further customized with configuring more users as described in the "Security" part of the GRUB manual.

Adding --unrestricted to a menu entry will allow any user to boot the OS while preventing the user from editing the entry and preventing access to the grub command console. Only a superuser or users specified with the --user switch will be able to edit the menu entry.

The factual accuracy of this article or section is disputed.

In order to make Linux entries --unrestricted, the CLASS variable in the beginning of /etc/grub.d/10_linux can be modified.

In order to achieve the fastest possible boot, instead of having GRUB wait for a timeout, it is possible for GRUB to hide the menu, unless the Shift key is held down during GRUB's start-up.

In order to achieve this, you should add the following line to /etc/default/grub:

Then create the file /etc/grub.d/31_hold_shift containing [3], make it executable, and regenerate the grub configuration:

If you like the idea of using UUIDs to avoid unreliable BIOS mappings or are struggling with GRUB's syntax, here is an example boot menu item that uses UUIDs and a small script to direct GRUB to the proper disk partitions for your system. All you need to do is replace the UUIDs in the sample with the correct UUIDs for your system. The example applies to a system with a boot and root partition. You will obviously need to modify the GRUB configuration if you have additional partitions:

If you have multiple kernels installed, say linux and linux-lts, by default grub-mkconfig groups them in a submenu. If you do not like this behaviour you can go back to one single menu by adding the following line to /etc/default/grub:

GRUB can remember the last entry you booted from and use this as the default entry to boot from next time. This is useful if you have multiple kernels (i.e., the current Arch one and the LTS kernel as a fallback option) or operating systems. To do this, edit /etc/default/grub and change the value of GRUB_DEFAULT:

This ensures that GRUB will default to the saved entry. To enable saving the selected entry, add the following line to /etc/default/grub:

This will only work if /boot is not a btrfs, because grub cannot write to btrfs. But it will generate a misleading error message: "sparse file not allowed. Press any key to continue.".

To change the default selected entry, edit /etc/default/grub and change the value of GRUB_DEFAULT:

Grub identifies entries in the generated menu (i.e. /boot/grub/grub.cfg) counted from zero. That means 0 for the first entry which is the default value, 1 for the second and so on. Main and submenu entries are separated by a > and are both identified by a number, title, or ID.

The example above boots the third entry from the main menu 'Advanced options for Arch Linux'.

Using IDs (see value after --id or $menuentry_id_option in grub.cfg if generating your grub.cfg):

Documentation of all three identifier methods: https://www.gnu.org/software/grub/manual/grub/html_node/default.html

The factual accuracy of this article or section is disputed.

The command grub-reboot is very helpful to boot another entry than the default only once. GRUB loads the entry passed in the first command line argument, when the system is rebooted the next time. Most importantly GRUB returns to loading the default entry for all future booting. Changing the configuration file or selecting an entry in the GRUB menu is not necessary.

You can play a tune through the PC-speaker while booting (right before the menu appears) by modifying the variable GRUB_INIT_TUNE:

You can add a menu entry to play each of these common GRUB_INIT_TUNE samples by creating the linked /etc/grub.d/91_tune_demo and then re-running grub-mkconfig.

For information on this, you can look at info grub -n play, while some collections exist.

If you require a special keymap or other complex steps that GRUB is not able to configure automatically in order to make /boot available to the GRUB environment, you can generate a core image yourself. On UEFI systems, the core image is the grubx64.efi file that is loaded by the firmware on boot. Building your own core image will allow you to embed any modules required for very early boot, as well as a configuration script to bootstrap GRUB.

Firstly, taking as an example a requirement for the dvorak keymap embedded in early-boot in order to enter a password for an encrypted /boot on a UEFI system:

Determine from the generated /boot/grub/grub.cfg file what modules are required in order to mount the crypted /boot. For instance, under your menuentry you should see lines similar to:

Take note of all of those modules: they will need to be included in the core image. Now, create a tarball containing your keymap. This will be bundled in the core image as a memdisk:

Now create a configuration file to be used in the GRUB core image. This is in the same format as your regular grub config, but need contain only a few lines to find and load the main configuration file on the /boot partition:

Finally, generate the core image, listing all of the modules determined to be required in the generated grub.cfg, along with any modules used in the early-grub.cfg script. The example above needs memdisk, tar, at_keyboard, keylayouts and configfile.

The generated EFI core image can now be used in the same way as the image that is generated automatically by grub-install: place it in your EFI system partition and enable it with efibootmgr, or configure as appropriate for your system firmware.

See also Debian cryptsetup docs.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Below is other relevant information regarding installing Arch via UEFI.

This article or section needs expansion.

Usually, GRUB keeps all files, including configuration files, in /boot, regardless of where the EFI system partition is mounted.

If you want to keep these files inside the EFI system partition itself, add --boot-directory=esp to the grub-install command:

This puts all GRUB files in esp/grub, instead of in /boot/grub. When using this method, make sure you have grub-mkconfig put the configuration file in the same place:

Configuration is otherwise the same.

See GRUB#Default/fallback boot path.

This section assumes you are creating a standalone GRUB for x86_64 systems (x86_64-efi). For 32-bit (IA32) EFI systems, replace x86_64-efi with i386-efi where appropriate.

It is possible to create a grubx64_standalone.efi application which has all the modules embedded in a tar archive within the UEFI application, thus removing the need to have a separate directory populated with all of the GRUB UEFI modules and other related files. This is done using the grub-mkstandalone command (included in grub) as follows:

Then copy the GRUB configuration file to esp/EFI/grub/grub.cfg and create a UEFI Boot Manager entry for esp/EFI/grub/grubx64_standalone.efi using efibootmgr.

The GRUB EFI file always expects its configuration file to be at ${prefix}/grub.cfg. However in the standalone GRUB EFI file, the ${prefix} is located inside a tar archive and embedded inside the standalone GRUB EFI file itself (inside the GRUB environment, it is denoted by "(memdisk)", without quotes). This tar archive contains all the files that would be stored normally at /boot/grub in case of a normal GRUB EFI install.

Due to this embedding of /boot/grub contents inside the standalone image itself, it does not rely on actual (external) /boot/grub for anything. Thus in case of standalone GRUB EFI file ${prefix}==(memdisk)/boot/grub and the standalone GRUB EFI file reads expects the configuration file to be at ${prefix}/grub.cfg==(memdisk)/boot/grub/grub.cfg.

Hence to make sure the standalone GRUB EFI file reads the external grub.cfg located in the same directory as the EFI file (inside the GRUB environment, it is denoted by ${cmdpath} ), we create a simple /tmp/grub.cfg which instructs GRUB to use ${cmdpath}/grub.cfg as its configuration (configfile ${cmdpath}/grub.cfg command in (memdisk)/boot/grub/grub.cfg). We then instruct grub-mkstandalone to copy this /tmp/grub.cfg file to ${prefix}/grub.cfg (which is actually (memdisk)/boot/grub/grub.cfg) using the option "boot/grub/grub.cfg=/tmp/grub.cfg".

This way, the standalone GRUB EFI file and actual grub.cfg can be stored in any directory inside the EFI system partition (as long as they are in the same directory), thus making them portable.

This article or section needs expansion.

If your arch installation should be bootable on both UEFI and BIOS systems, install GRUB using both methods. Partition the disk as GPT, create an EFI system partition and a BIOS boot partition as well, mount the ESP at /efi and run the GRUB install commands for both ways.

In a BIOS system the EFI variables are not present, thus the UEFI NVRAM boot entries cannot be set and the 2nd command will report an error. By using the --no-nvram and --removable option the system will have a good chance to be bootable in UEFI mode too:

For some BIOS implementations it may be necessary to set the PMBR’s boot flag, e.g. with parted

Upon boot GRUB may in some cases take a long time to verify the password. This can be due to a high cost parameters of the key derivation function, which you can check as follows:

The problem is that the cost parameters for a given keyslot are generated when the key is added to ensure a balance between being high enough to protect against brute force attacks and low enough to allow for fast key derivation by estimating the capabilities of your computer. However, when GRUB is started, it might not have the same computational resources at hand, thus being vastly slower.

If your password provides enough entropy to counter common attacks by itself, you can lower the parameters. For example to lower the iteration count of PBKDF2, use:

A minimum of 1000 iterations is recommended as per RFC 2898, but you should aim for higher values if you can (The cost for an attacker as well as the time for key derivation scale linearly).

Recommended parameters for Argon2 are discussed in RFC 9106.

**Examples:**

Example 1 (unknown):
```unknown
# mount --mkdir /dev/sdy1 /mnt/usb
# grub-install --target=i386-pc --debug --boot-directory=/mnt/usb/boot /dev/sdy
# grub-mkconfig -o /mnt/usb/boot/grub/grub.cfg
```

Example 2 (unknown):
```unknown
# mkdir -p /mnt/usb/etc/default
# cp /etc/default/grub /mnt/usb/etc/default
# cp -a /etc/grub.d /mnt/usb/etc
```

Example 3 (unknown):
```unknown
# sync; umount /mnt/usb
```

Example 4 (unknown):
```unknown
--removable
```

---

## Gambas

**URL:** https://wiki.archlinux.org/title/Gambas

**Contents:**
- Installation
- Tips and tricks
- See also

Gambas is an object-oriented dialect of the BASIC programming language as well as the integrated development environment that accompanies it.

Gambas consists of a runtime and IDE further broken up into several distinct components. Not all of them may be needed for what you wish to do with the IDE or for running a specific Gambas application. If you do not want to pick a subset tailored to your requirements, you can install the whole gambas3 group.

Gambas 3 can build installation packages for various distributions and has support for building Arch packages, perfect for use with the AUR.

Gambas supports both the GTK and Qt toolkits and can make use of both, allowing the application to fit seamlessly into most Desktop environments. This also applies to applications made inside the Gambas IDE, assuming the gb3-gui component is used.

---

## Installation guide

**URL:** https://wiki.archlinux.org/title/Installation_guide

**Contents:**
- Pre-installation
  - Acquire an installation image
  - Verify signature
  - Prepare an installation medium
  - Boot the live environment
  - Set the console keyboard layout and font
  - Verify the boot mode
  - Connect to the internet
  - Update the system clock
  - Partition the disks

This document is a guide for installing Arch Linux using the live system booted from an installation medium made from an official installation image. The installation medium provides accessibility features which are described on the page Install Arch Linux with accessibility options. For alternative means of installation, see Category:Installation process.

Before installing, it would be advised to view the FAQ. For conventions used in this document, see Help:Reading. In particular, code examples may contain placeholders (formatted in italics) that must be replaced manually.

This guide is kept concise and you are advised to follow the instructions in the presented order per section. For more detailed instructions, see the respective ArchWiki articles or the various programs' man pages, both linked from this guide. For interactive help, the IRC channel and the forums are also available.

Arch Linux should run on any x86_64-compatible machine with a minimum of 512 MiB RAM, though more memory is needed to boot the live system for installation.[1] A basic installation should take less than 2 GiB of disk space. As the installation process needs to retrieve packages from a remote repository, this guide assumes a working internet connection is available.

Visit the Download page and, depending on how you want to boot, acquire the ISO file or a netboot image, and the respective PGP signature.

It is recommended to verify the image signature before use, especially when downloading from an HTTP mirror, where downloads are generally prone to be intercepted to serve malicious images.

Download the ISO PGP signature from https://archlinux.org/download/#checksums to the ISO directory and follow the instructions there to verify it.

Alternatively, from an existing Arch Linux installation run:

The ISO can be supplied to the target machine via a USB flash drive, an optical disc or a network with PXE: follow the appropriate article to prepare yourself an installation medium from the ISO file.

For the netboot image, follow Netboot#Boot from a USB flash drive to prepare a USB flash drive for UEFI booting.

To switch to a different console—for example, to view this guide with Lynx alongside the installation—use the Alt+arrow keyboard shortcut. To edit configuration files, mcedit(1), nano and vim are available. See pkglist.x86_64.txt for a list of the packages included in the installation medium.

The default console keymap is US. Available layouts can be listed with:

To set the keyboard layout, pass its name to loadkeys(1). For example, to set a German keyboard layout:

Console fonts are located in /usr/share/kbd/consolefonts/ and can likewise be set with setfont(8) omitting the path and file extension. For example, to use one of the largest fonts suitable for HiDPI screens, run:

To verify the boot mode, check the UEFI bitness:

If the system did not boot in the mode you desired (UEFI vs BIOS), refer to your motherboard's manual.

To set up a network connection in the live environment, go through the following steps:

In the live environment systemd-timesyncd is enabled by default and time will be synced automatically once a connection to the internet is established.

Use timedatectl(1) to ensure the system clock is synchronized:

When recognized by the live system, disks are assigned to a block device such as /dev/sda, /dev/nvme0n1 or /dev/mmcblk0. To identify these devices, use lsblk or fdisk.

Results ending in rom, loop or airootfs may be ignored. mmcblk* devices ending in rpmb, boot0 and boot1 can be ignored.

The following partitions are required for a chosen device:

Use a partitioning tool like fdisk to modify partition tables. For example:

See also Partitioning#Example layouts.

Once the partitions have been created, each newly created partition must be formatted with an appropriate file system. See File systems#Create a file system for details.

For example, to create an Ext4 file system on /dev/root_partition, run:

If you created a partition for swap, initialize it with mkswap(8):

If you created an EFI system partition, format it to FAT32 using mkfs.fat(8).

Mount the root volume to /mnt. For example, if the root volume is /dev/root_partition:

Create any remaining mount points under /mnt (such as /mnt/boot for /boot) and mount the volumes in their corresponding hierarchical order.

For UEFI systems, mount the EFI system partition:

If you created a swap volume, enable it with swapon(8):

genfstab(8) will later detect mounted file systems and swap space.

Packages to be installed must be downloaded from mirror servers, which are defined in /etc/pacman.d/mirrorlist. The higher a mirror is placed in the list, the more priority it is given when downloading a package.

On the live system, all HTTPS mirrors are enabled (i.e. uncommented). The topmost worldwide mirror should be fast enough for most people, but you may still want to inspect the file to see if it is satisfactory. If it is not, edit the file accordingly, and move the geographically closest mirrors to the top of the list, although other criteria should be taken into account. Alternatively, you can use reflector to create a mirrorlist file based on various criteria.

This file will later be copied to the new system by pacstrap, so it is worth getting right.

No configuration (except for /etc/pacman.d/mirrorlist) gets carried over from the live environment to the installed system. The only mandatory package to install is base, which does not include all tools from the live installation, so installing more packages is frequently necessary.

In particular, review the following software and install everything that you need:

For comparison, packages available in the live system can be found in pkglist.x86_64.txt.

To install more packages or package groups, append the names to the pacstrap(8) command below (space separated) or use pacman to install them while chrooted into the new system.

For example, a basic installation with the Linux kernel and firmware for common hardware:

To get needed file systems (like the one used for the boot directory /boot) mounted on startup, generate an fstab file. Use -U or -L to define by UUID or labels, respectively:

Check the resulting /mnt/etc/fstab file, and edit it in case of errors.

To directly interact with the new system's environment, tools, and configurations for the next steps as if you were booted into it, change root into the new system:

For human convenience (e.g. showing the correct local time or handling Daylight Saving Time), set the time zone:

Run hwclock(8) to generate /etc/adjtime:

This command assumes the hardware clock is set to UTC. See System time#Time standard for details.

To prevent clock drift and ensure accurate time, set up time synchronization using a Network Time Protocol (NTP) client such as systemd-timesyncd.

To use the correct region and language specific formatting (like dates, currency, decimal separators), edit /etc/locale.gen and uncomment the UTF-8 locales you will be using. Generate the locales by running:

Create the locale.conf(5) file, and set the LANG variable accordingly:

If you set the console keyboard layout, make the changes persistent in vconsole.conf(5):

To assign a consistent, identifiable name to your system (particularly useful in a networked environment), create the hostname file:

Complete the network configuration for the newly installed environment. That may include installing suitable network management software, configuring it if necessary and enabling its systemd unit so that it starts at boot.

Creating a new initramfs is usually not required, because mkinitcpio was run on installation of the kernel package with pacstrap.

For LVM, system encryption or RAID, modify mkinitcpio.conf(5) and recreate the initramfs image:

Set a secure password for the root user to allow performing administrative actions:

Choose and install a Linux-capable boot loader.

Exit the chroot environment by typing exit or pressing Ctrl+d.

Optionally manually unmount all the partitions with umount -R /mnt: this allows noticing any "busy" partitions, and finding the cause with fuser(1).

Finally, restart the machine by typing reboot: any partitions still mounted will be automatically unmounted by systemd. Remember to remove the installation medium and then login into the new system with the root account.

See General recommendations for system management directions and post-installation tutorials (like creating unprivileged user accounts, setting up a graphical user interface, sound or a touchpad).

For a list of applications that may be of interest, see List of applications.

**Examples:**

Example 1 (unknown):
```unknown
$ pacman-key -v archlinux-version-x86_64.iso.sig
```

Example 2 (unknown):
```unknown
fbcon=font:TER16x32
```

Example 3 (unknown):
```unknown
# localectl list-keymaps
```

Example 4 (unknown):
```unknown
# loadkeys de-latin1
```

---

## Touchpad Synaptics

**URL:** https://wiki.archlinux.org/title/Synaptics

**Contents:**
- Installation
- Configuration
  - Frequently used options
  - Configuration on the fly
    - Console tools
    - Graphical tools
  - Xfce
  - Cinnamon
  - MATE
- Advanced configuration

This article details the installation and configuration process of the Synaptics input driver for Synaptics (and ALPS) touchpads found on most notebooks.

The Synaptics driver can be installed with the package xf86-input-synaptics.

The primary method of configuration for the touchpad is through an Xorg server configuration file. After installing xf86-input-synaptics, a default configuration file is located at /usr/share/X11/xorg.conf.d/70-synaptics.conf. Users can copy this file to /etc/X11/xorg.conf.d/ and edit it to configure the various driver options available. Refer to the synaptics(4) manual page for a complete list of available options. Machine-specific options can be discovered using #Synclient.

The following example file configures some common options, including vertical, horizontal and circular scrolling as well as tap-to-click:

Next to the traditional method of configuration, the Synaptics driver also supports on the fly configuration. This means that users can set certain options through a software application, these options are applied immediately without needing to restart Xorg. This is useful to test configuration options before you include them in the configuration file or a script. Note that on the fly configuration is not persistent and lasts only until the Xorg server exists.

To change these settings in Xfce:

To change these settings in Cinnamon:

It is possible to configure the way MATE handles the touchpad:

To prevent Mate settings daemon from overriding existing settings, do as follows:

Depending on your model, synaptic touchpads may have or lack capabilities. We can determine which capabilities your hardware supports by using xinput(1).

First, find the name of your touchpad:

You can now use xinput to find your touchpad's capabilities:

From left to right, this shows:

Use xinput list-props "SynPS/2 Synaptics TouchPad" to list all device properties. See synaptics(4) for full documentation of the Synaptics properties.

Synclient can configure every option available to the user as documented in synaptics(4). A full list of the current user settings can be brought up:

Every listed configuration option can be controlled through synclient, for example:

After you have successfully tried and tested your options through synclient, you can make these changes permanent by adding them to /etc/X11/xorg.conf.d/70-synaptics.conf.

The tool evtest can display pressure and placement on the touchpad in real-time, allowing further refinement of the default Synaptics settings. The evtest monitoring can be started with:

X denotes the touchpad's ID. It can be found by looking at the output of cat /proc/bus/input/devices.

evtest needs exclusive access to the device which means it cannot be run together with an X server instance. You can either kill the X server or run evtest from a different virtual terminal (e.g., by pressing Ctrl+Alt+F2).

The tool xorg-xev can display taps, clicks, pressure, placement and other measured parameters in real-time, allowing still further refinement of the default Synaptics settings. xev can be run in X and needs no specifics. using the -event parameter, it is possible to restrict the types of events that are reported.

Circular scrolling is a feature that Synaptics offers which closely resembles the behaviour of iPods. Instead of (or additional to) scrolling horizontally or vertically, you can scroll circularly. Some users find this faster and more precise. To enable circular scrolling, add the following options to the touchpad device section of /etc/X11/xorg.conf.d/70-synaptics.conf:

The option CircScrollTrigger may be one of the following values, determining which edge circular scrolling should start:

Specifying something different from zero may be useful if you want to use circular scrolling in conjunction with horizontal and/or vertical scrolling. If you do so, the type of scrolling is determined by the edge you start from.

To scroll fast, draw small circles in the center of your touchpad. To scroll slowly and more precise, draw large circles.

It is possible to enable natural scrolling through Synaptics. Simply use negative values for VertScrollDelta and HorizScrollDelta like so:

You might want to turn the touchpad on and off with a simple button click or shortcut. This can be done by binding the following xinput-based script:

Alternatively, synclient can be used to toggle the touchpad. However, it can only turn off touch events but not physical clickpad button usage:

First of all you should test if it works properly for your touchpad and if the settings are accurate. Enable palm detection with

Then test the typing. You can tweak the detection by setting the minimum width for the touch to be considered a palm, for example:

And you can tweak the minimum pressure required for the touch to be considered a palm, for example:

Once you have found the correct settings, you can add them to your config file:

syndaemon(1) monitors keyboard activity and disables the touchpad while typing. It has several options to control when the disabling occurs. View them with

For example, to disable tapping and scrolling for 0.5 seconds after each keypress (ignoring modifier keys like Ctrl), use

Once you have determined the options you like, you should use your login manager or xinitrc to have it run automatically when X starts. The -d option will make it start in the background as a daemon.

With the assistance of udev, it is possible to automatically disable the touchpad if an external mouse has been plugged in. To achieve this, use one of the following rules.

This is a basic rule generally for non-"desktop environment" sessions:

If the touchpad is always deactivated at startup, even when no mouse is plugged in, try adding the following criteria between the KERNEL and ACTION parameters above:

This article or section is out of date.

GDM stores the Xauthority files in /var/run/gdm in a randomly-named directory. You should find your actual path to the Xauthority file which can be done using ps ax. For some reason, multiple authority files may appear for a user, so a rule like this will be necessary:

Furthermore, you should validate that your udev script is running properly. You can check for the conditions by running udevadm monitor -p with root privileges.

syndaemon whether started by the user or the desktop environment can conflict with synclient and will need to be disabled. A rule like this will be needed:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

A touchpad-state-gitAUR package created around the udev rules in #With syndaemon running is available. It includes a udev rule and script:

GNOME users can install the GNOME shell extension Touchpad Indicator, change Switch Method to Synclient and enable Automatically switch Touchpad On/Off in its preferences.

If using Plasma, the plasma-desktop package can be used to manage the touchpad.

The factual accuracy of this article or section is disputed.

For an environment where multiple users are present, a slightly different approach is needed to detect the current users X environment. This script will help achieving this:

Update the TRACKPAD_NAME variable for your system configuration. Run find /sys/class/input/ -name mouse* -exec udevadm info -a {} \; | grep 'ATTRS{name}' to get a list of useful mice-names. Choose the one for your trackpad.

Then have udev run this script when USB mices are plugged in or out, with these udev rules:

Ever more laptops have a special kind of touchpad which has a single mouse button as part of the tracking plate, instead of external buttons. For example, the 2015 Dell XPS 13, HP series 4500 ProBooks, ThinkPad X220 and X1 ThinkPad series have this kind of a touchpad. By default, the whole button area is detected as a left button, so right and middle-click functions and click + drag will not work. It is possible to define two and three finger clicks as right and middle button clicks, and/or to define parts of the click pad surface as right and middle buttons. Note that although the driver registers multiple touches, it does not track individual fingers (as of version 1.7.1) which results in confusing behavior when using physical buttons of a clickpad for drag-and-drop and other gestures: you have to click with two or three fingers but then only move one of them while holding the button down with another. You can look into the xf86-input-mtrackAUR driver for better multitouch support.

Some desktop environments (KDE and GNOME at least) define sane and useful default configurations for clickpads, providing a right button at the bottom right of the pad, recognising two and three-finger clicks anywhere on the pad as right and middle clicks, and providing configuration options to define two and three-finger taps as right and middle clicks. If your desktop does not do this, or if you want more control, you can modify the touchpad section in /etc/X11/xorg.conf.d/70-synaptics.conf (or better, of your custom synaptics configuration file prefixed with a higher number). For example:

The format for the SoftButtonAreas option is (from synaptics(4)):

The above SoftButtonAreas option is commonly found in documentation or synaptics packages, and it defines the right half of the bottom 18% of the touchpad as a right button. There is no middle button defined. If you want to define a middle button remember one key piece of information from the manual; edge set to 0 extends to infinity in that direction.

In the following example the right button will occupy the rightmost 40% of the button area and the middle button 20% of it in the center. The leftmost 40% remains as a left button (as does the rest of the clickpad):

You can use synclient to check the soft button areas:

If your buttons are not working, soft button areas are not changing, ensure you do not have a synaptics configuration file distributed by a package which is overriding your custom settings (i.e. some AUR packages distribute configurations prefixed with very high numbers).

These settings cannot be modified on the fly with synclient, however, xinput works:

You cannot use percentages with this command, so look at /var/log/Xorg.0.log to figure out the touchpad x and y-axis ranges.

In some cases, for example Toshiba Satellite P50, everything work out of the box except often your click are seen as mouse movement and the cursor will jump away just before registering the click. This can be easily solved running

take the BottomEdge value and subtract a the wanted height of your button, then temporary apply with

when a good value has been found make it a fixed correction with

Occasionally touchpads will fail to work when the computer resumes from sleep or hibernation. This can often be corrected without rebooting by

If you are using a laptop computer and your touchpad does not work after switching the laptop's lid, you can just change your power management policy: when closing the lid, 'shutdown the screen' instead of 'suspend'(or 'hibernate'). This is useful for some laptops.

MATE will by default overwrite various options for your touchpad. This includes configurable features for which there is no graphical configuration within MATE's system control panel. This may cause it to appear that /etc/X11/xorg.conf.d/70-synaptics.conf is not applied. Follow #MATE to prevent this behavior.

Due to the way Synaptics is currently set-up, 2 instances of the Synaptics module are loaded. We can recognize this situation by opening the xorg log file (/var/log/Xorg.0.log) and noticing this:

Notice how 2 differently named instances of the module are being loaded. In some cases, this causes the touchpad to become nonfunctional.

We can prevent this double loading by adding MatchDevicePath "/dev/input/event*" to our /etc/X11/xorg.conf.d/70-synaptics.conf file:

Restart X and check xorg logs again, the error should be gone and the touchpad should be functional.

related bugreport: FS#20830

related forum topics:

This can be caused by a number of issues;

There also seems to be a problem with laptops which have both a touchscreen & a touchpad, such as the Dell XPS 12 or Dell XPS 13. To fix this, you can blacklist the i2c_hid driver, this does have the side-effect of disabling the touchscreen though.

This seems to be a known problem. Also see this thread.

Post kernel 3.15, having the module blacklisted may cause touchpad to stop working completely. Removing the blacklist should allow this to start working with limited functionality, see FS#40921.

In some cases, Synaptics touchpads only work partially. Features like two-finger scrolling or two-finger middle-click do not work even if properly enabled. This is probably related to the touchpad is not working problem mentioned above. Fix is the same, prevent double module loading.

If preventing the module from loading twice does not solve your issue, try commenting out the toggle MatchIsTouchpad (which is now included by default in the Synaptics configuration).

See https://unix.stackexchange.com/questions/28736/what-does-the-i8042-nomux-1-kernel-option-do-during-booting-of-ubuntu.

Some users have their cursor inexplicably jump around the screen. There currently no patch for this, but the developers are aware of the problem and are working on it.

Another possibility is that you are experiencing IRQ losses related to the i8042 controller (this device handles the keyboard and the touchpad of many laptops), so you have two possibilities here:

If that is the case, you can use this command to display information about your input devices:

Search for an input device which has the name "SynPS/2 Synaptics TouchPad". The "Handlers" section of the output specifies what device you need to specify.

In this case, the Handlers are mouse0 and event1, so /dev/input/mouse0 would be used.

This article or section needs expansion.

You can enable/disable some special events that Firefox handles upon tapping or scrolling certain parts of your touchpad by editing the settings of those actions. Type about:config in your Firefox address bar. To alter options, double-click on the line in question.

Horizontal scrolling will now by default scroll through pages and not through your history. To reenable Mac-style forward/backward with two-finger swiping, edit:

You may encounter accidental forwards/backwards while scrolling vertically. To change Firefox's sensitivity to horizontal swipes, edit:

The optimum value will depend on your touchpad and how you use it, try starting with 10. A negative value will reverse the swipe directions.

These problems seem to be occurring on several models of LG laptops. Symptoms include: when pressing Mouse Button 1, Synaptics interprets it as ScrollUP and a regular button 1 click; same goes for button 2.

The scrolling issue can be resolved by entering in xorg.conf:

Apparently, when trying to compile this against the latest version of Synaptics it fails. The solution to this is using the Git repository for Synaptics [5].

To build the package after downloading the tarball and unpacking it, execute:

First, make sure your section describing the external mouse contains this line (or that the line looks like this):

If the "Device" line is different, change it to the above and try to restart X. If this does not solve your problem, make your touchpad the CorePointer in the "Server Layout" section:

and make your external device "SendCoreEvents":

Finally, add this to your external device's section:

If all of the above does not work for you, please check relevant bug trackers for possible bugs, or go through the forums to see if anyone has found a better solution.

Many drivers include a firmware that is loaded into flash memory when the computer boots. This firmware is not necessarily cleared upon shutdown, and is not always compatible with Linux drivers. The only way to clear the flash memory is to shutdown completely rather than using reboot. It is generally considered best practice to never use reboot when switching between operating systems.

Certain touchpads (Elantech in particular) will fail to be recognized as a device of any sort after a standard shutdown. There are multiple possible solutions to this problem:

Newer Thinkpads do not have physical buttons for their Trackpoint anymore and instead use the upper area of the Clickpad for buttons (Left, Middle, Right). Apart from the ergonomic viewpoint this works quite well with current Xorg. Unfortunately, mouse wheel emulation using the middle button is not supported yet. Install xf86-input-evdev-trackpointAUR for a patched and properly configured version if you intend to use the Trackpoint.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/X11/xorg.conf.d/70-synaptics.conf
```

Example 2 (unknown):
```unknown
/etc/X11/xorg.conf.d/
```

Example 3 (unknown):
```unknown
/etc/X11/xorg.conf.d/70-synaptics.conf
```

Example 4 (unknown):
```unknown
Section "InputClass"
    Identifier "touchpad"
    Driver "synaptics"
    MatchIsTouchpad "on"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "VertEdgeScroll" "on"
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "CircularScrolling" "on"
        Option "CircScrollTrigger" "2"
        Option "EmulateTwoFingerMinZ" "40"
        Option "EmulateTwoFingerMinW" "8"
        Option "CoastingSpeed" "0"
        Option "FingerLow" "30"
        Option "FingerHigh" "50"
        Option "MaxTapTime" "125"
        ...
EndSection
```

---

## Install Arch Linux on a removable medium

**URL:** https://wiki.archlinux.org/title/Install_Arch_Linux_on_a_removable_medium

**Contents:**
- Installation
  - Installation tweaks
- Boot loader configuration
  - GRUB
  - Syslinux
  - rEFInd
- Tips and tricks
  - Using your portable install on multiple machines
    - Video drivers
    - Audio drivers

This page explains how to perform a regular Arch installation onto removable media (e.g. a USB flash drive). In contrast to having a LiveUSB as covered in USB flash installation medium, the result will be a persistent installation identical to normal installation to HDD.

There are various ways of installing Arch on removable media, depending on the operating system you have available:

Follow the instructions on GRUB#BIOS systems and GRUB#UEFI systems to install GRUB for both BIOS and UEFI booting:

See rEFInd#For manual boot stanzas for details on creating manual boot stanzas.

You must also use the --usedefault /dev/sdXY argument when installing rEFInd.

The factual accuracy of this article or section is disputed.

To support most common GPUs, install xf86-video-vesa, xf86-video-ati, xf86-video-amdgpu, xf86-video-fbdev.

To support most common sound cards, install sof-firmware and alsa-firmware. For more information about configuring audio device, see Advanced Linux Sound Architecture.

It is recommended to use UUID in both fstab and boot loader configuration. See Persistent block device naming for details.

Alternatively, you may create udev rule to create custom symlink for your disk. Then use this symlink in fstab and boot loader configuration. See udev#Setting static device names for details.

The factual accuracy of this article or section is disputed.

You may want to disable KMS for various reasons, such as getting a blank screen or a "no signal" error from the display, when using some Intel video cards, etc. To disable KMS, add nomodeset as a kernel parameter. See Kernel parameters for more info.

This article or section needs expansion.

The fallback image should be used for maximum compatibility.

When installing to a device that offers a limited number of writes before it wears out, such as a USB drive, SD card, or similar, reduce the number of writes to increase the device lifetime. This also reduces the performance impact of slow writes.

You might encounter UI freezes on high I/O load especially on slow drives. Improving performance#Changing I/O scheduler or switching to a kernel which uses a different default scheduler can drastically affect your UI responsiveness. For example BFQ can improve UI responsiveness which is default on linux-zen.

See Improving performance#The scheduling algorithms for more info.

**Examples:**

Example 1 (unknown):
```unknown
/etc/mkinitcpio.conf
```

Example 2 (unknown):
```unknown
# grub-install --target=i386-pc /dev/sdX --recheck
# grub-install --target=x86_64-efi --efi-directory=esp --removable --recheck
```

Example 3 (unknown):
```unknown
/boot/grub/device.map
```

Example 4 (unknown):
```unknown
LABEL Arch
        MENU LABEL Arch Linux
        LINUX ../vmlinuz-linux
        APPEND root=UUID=3a9f8929-627b-4667-9db4-388c4eaaf9fa rw
        INITRD ../initramfs-linux.img
```

---

## Swap

**URL:** https://wiki.archlinux.org/title/Swappiness

**Contents:**
- Swap space
- Swap partition
  - Enabling at boot
  - Disabling swap
- Swap file
  - Swap file creation
  - Swap file removal
- Swap encryption
- Performance
  - Swappiness

This page provides an introduction to swap space and paging on GNU/Linux. It covers creation and activation of swap partitions and swap files.

From All about Linux swap space:

Support for swap is provided by the Linux kernel and user-space utilities from the util-linux package.

Swap space can take the form of a disk partition or a file. Users may create a swap space during installation or at any later time as desired. Swap space can be used for two purposes, to extend the virtual memory beyond the installed physical memory (RAM), and also for suspend-to-disk support.

Whether or not it is beneficial to extend the virtual memory with swap depends on the amount of installed physical memory. If the amount of physical memory is less than the amount of memory required to run all the desired programs, then it may be beneficial to enable swap. This avoids out of memory conditions, where the Linux kernel OOM killer mechanism will automatically attempt to free up memory by killing processes. To increase the amount of virtual memory to the required amount, add the necessary difference (or more) as swap space.

The biggest drawback of using swap when running out of memory is its lower performance, see section #Performance. Hence, enabling swap is a matter of personal preference: some prefer programs to be killed over enabling swap and others prefer enabling swap and slower system when the physical memory is exhausted.

To check swap status, use:

Or to show physical memory as well as swap usage:

A swap partition can be created with most GNU/Linux partitioning tools. Swap partitions are designated by the partition type GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F on GPT (8200 type for gdisk, swap type for fdisk) and type ID 82 on MBR.

To set up a partition as Linux swap area, the mkswap(8) command is used. For example:

To enable the device for paging:

See swapon(8) for the options syntax.

To enable the swap partition at boot time, either:

See fstab for the file syntax, and systemd#systemd.mount - mounting.

To deactivate specific swap space:

Alternatively use the -a switch to deactivate all swap space.

Since swap is managed by systemd, it will be activated again on the next system startup. To disable the automatic activation of detected swap space permanently, run systemctl --type swap to find the responsible .swap unit and mask it.

As an alternative to creating an entire partition, a swap file offers the ability to vary its size on-the-fly, and is more easily removed altogether. This may be especially desirable if disk space is at a premium (e.g. a modestly-sized SSD).

Use mkswap(8) to create a swap file the size of your choosing (see Partitioning#Swap for advice). For example, creating a 4 GiB swap file:

Activate the swap file:

Finally, edit the fstab configuration to add an entry for the swap file:

As an alternative to fstab, a swap unit can be created (see systemd.swap(5)):

Perform a daemon-reload and enable swapfile.swap.

For additional information, see fstab#Usage.

To remove a swap file, it must be turned off first and then can be removed:

Finally, remove the relevant entry from /etc/fstab.

See dm-crypt/Swap encryption.

Swap operations are usually significantly slower than directly accessing data in RAM. However, disabling swap entirely to improve performance can sometimes lead to a degradation. If there is not enough physical memory available to hold everything, swapping out nothing leaves less memory available for file system caches, causing more frequent and costly disk usage.

Swap values can be adjusted to help performance:

When memory usage reaches a certain threshold, the kernel starts looking at active memory and seeing what it can free up. File data can be written out to the file system (if changed), unloaded and re-loaded later; other data must be written to swap before it can be unloaded.

The swappiness sysctl parameter represents the kernel's preference for writing to swap instead of files. It can have a value between 0 and 200 (max 100 if Linux < 5.8); the default value is 60. A low value causes the kernel to prefer freeing up open files, a high value causes the kernel to try to use swap space, and a value of 100 means IO cost is assumed to be equal.

To check the current swappiness value:

Alternatively, the file /proc/sys/vm/swappiness can be read in order to obtain the raw integer value.

To temporarily set the swappiness value:

To set the swappiness value permanently, create a sysctl.d(5) configuration file. For example:

To have the boot loader set swappiness when loading the kernel, add a kernel parameter, e.g. sysctl.vm.swappiness=35.

Reasons for choosing a different swappiness can include:

Another sysctl parameter that affects swap performance is vm.vfs_cache_pressure, which controls the tendency of the kernel to reclaim the memory which is used for caching of VFS caches, versus pagecache and swap. Increasing this value increases the rate at which VFS caches are reclaimed. For more information on what it does, see the Linux kernel documentation.

The default value is 100, which states that filesystem cache is about as important as the other caches, so they should be reclaimed at about an equal weight. On desktops it has been argued that filesystem cache is more important than the other caches because filesystem browsing times affects operation latency (perceived responsiveness) more than the other caches, resulting a suggested value of 50. On the other hand, a higher value has been suggested when the VFS cache holds metadata on many small files that are not touched again. For more information on tuning this parameter, see OpenSUSE tuning guide (which recommends experimenting and checking the types of caches via slaptop).

If you have more than one swap file or swap partition you should consider assigning a priority value (0 to 32767) for each swap area. The system will use swap areas of higher priority before using swap areas of lower priority. For example, if you have a faster disk and a slower disk, assign a higher priority to the swap area located on the fastest device. Priorities can be assigned in fstab via the pri parameter:

Or via the --priority parameter of swapon:

If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them.

There is no necessity to use RAID for swap performance reasons. The kernel itself can stripe swapping on several devices, if you just give them the same priority in the /etc/fstab file. Refer to The Software-RAID HOWTO for details.

See Solid state drive#swap.

See Improving performance#Swap on zram or zswap.

If you only need swap as a hibernation image storage space, then you can use zswap and disable its writeback so that there are no disk writes from regular swap usage. See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation.

**Examples:**

Example 1 (unknown):
```unknown
$ swapon --show
```

Example 2 (unknown):
```unknown
0657FD6D-A4AB-43C4-84E5-0933C84B4F4F
```

Example 3 (unknown):
```unknown
# mkswap /dev/sdxy
```

Example 4 (unknown):
```unknown
# swapon /dev/sdxy
```

---

## Offline installation

**URL:** https://wiki.archlinux.org/title/Offline_installation

**Contents:**
- Prepare local repository
- Mount and configure
- Pacstrap
- Offline installation of packages
  - Install from file
  - Offline cache
  - Local repository
    - Complete repository
- See also

This article provides instructions on installing Arch Linux on a system without an Internet connection. To do this, another system with a working Internet connection is required.

First, follow the Installation guide, skipping the steps requiring an internet connection (e.g. Installation guide#Connect to the internet), then continue with this guide instead of following Installation guide#Install essential packages.

Follow Pacman/Tips and tricks#Installing packages from a CD/DVD or USB stick for instructions on preparing a local repository with the necessary files on a separate host installation.

At the very least, for a functioning system, the following packages are recommended:

Create your custom offline repository:

The factual accuracy of this article or section is disputed.

This article or section needs expansion.

Once the repository is prepared, connect the external media to the new installation, and mount it on the newly created root filesystem:

Edit your archiso /etc/pacman.conf and add a new section:

Comment out [core] and [extra] so that pacman does not fail on the default repositories.

By default, pacman's keyring is initialized in the live session only once NTP is activated (https://bbs.archlinux.org/viewtopic.php?id=283075). In case NTP cannot be activated (e.g. you don't have internet access), you need to manually run

After this, you can continue to pacstrap your locally-available packages to the new installation:

In case the offline installation process was only temporary, but requires manual installation of some packages before being able to access a network, see pacman#Additional commands to learn how to install local packages.

Shell globbing can be used to install many packages at once:

You can put the required files into /var/lib/pacman/sync and /var/cache/pacman/pkg, so as to make pacman think it has everything it needs to do searches, updates, and installs. The following method is based on two forum threads: [1][2].

The following script will download the updated package databases. If needed, change MIRROR to any mirror from the mirror status list.

Make the script executable and run it. You will obtain multiple .db files.

The following steps will be transferring the .db files to the offline PC, making it so you are working with up-to-date package lists (as if you ran pacman -Sy), then generating a list of package required for the update:

You will also need to download the corresponding package signatures, so prepare the list of signatures to download:

Next, bring the two lists with you to a place where you have internet and download the listed packages in an empty directory:

Take all the *.pkg.tar.zst and *.pkg.tar.zst.sig files back home, put them in /var/cache/pacman/pkg and finally run:

In case the new system is expected to remain offline or airgapped, it should be configured to expect only local repositories.

After chrooting into your new installation, edit the new /etc/pacman.conf in the same way as previously (but without the /mnt prefix):

Comment out all other repositories and save. Continue configuring the new system as usual.

From now on any updates to the offline system can be made by bringing an up to date copy of the local repository, mounting it to /repo and running pacman commands as usual.

**Examples:**

Example 1 (unknown):
```unknown
airootfs.sfs
```

Example 2 (unknown):
```unknown
airootfs.sfs
```

Example 3 (unknown):
```unknown
# pacman -Syw --cachedir $PWD --dbpath /tmp/blankdb base linux linux-firmware
```

Example 4 (unknown):
```unknown
# repo-add ./custom.db.tar.zst ./*[^sig]
```

---

## Arch IRC channels

**URL:** https://wiki.archlinux.org/title/IRC_channel

**Contents:**
- Main channels
  - Registration
  - Channel operators
  - Libera Chat group contacts
- Collaborative debugging
  - IRC usage
  - Output errors/messages to a file
- Other channels
  - International IRC channels

To use Internet Relay Chat (IRC), you need an IRC client. The installation live environment includes the Irssi client.

You are expected to familiarize yourself with our Code of conduct and General guidelines#IRC before joining any of the official channels. For a list of commonly used abbreviations, see Arch terminology.

This section is about #archlinux, the main Arch Linux support IRC channel, and #archlinux-offtopic, the main Arch Linux social channel, both available on the Libera Chat network. See https://archlinux.org/news/move-of-official-irc-channels-to-liberachat/

The central topic for #archlinux is support and general discussion about Arch Linux.

In order to reduce spam, #archlinux and #archlinux-offtopic have the channel mode set to +r and +q $~a. This means you have to be identified via NickServ to be able to join these channels and send messages, respectively. If you are not registered and identified, you will be forwarded to #archlinux-unregistered.

To register with NickServ, follow the Libera Chat FAQ, as well as NickServ HELP when connected to irc.libera.chat:

Arch operators are ops in both #archlinux and #archlinux-offtopic. See the list below, or run /msg phrik listops on Libera Chat.

If you for some reason need the help of an op, do not be shy to /query or /msg us. Here is the list of ops as of 2021-09-24:

Group contacts mediate matters between the Libera Chat network staff, Arch Linux staff and Arch Linux users. That includes the management of channels in the #archlinux-* namespace on the Libera Chat network and the assignment of archlinux/* hostmasks. Please note that only Arch Linux staff is eligible for hostmasks.

When requesting help from an IRC help channel (like #archlinux), it is inappropriate to paste logs into the channel and this may even get you kicked. Use a pastebin instead, you can use phriks factoid !paste to see which pastebins are acceptable. Acceptable pastebins usually work without enabling JavaScript. Some require enabling JavaScript for posting from a web browser, which is still acceptable because it does not affect the viewer. They should not display advertising or other disrupting content and should also not require a login. Excellent pastebins usually provide a way to paste output via piping.

An example list of acceptable pastebins:

When first entering the channel, there is no need to say hello. State the problem you are experiencing and make sure to be verbose and to provide logfiles. It also helps to search for any error messages you are getting first to not waste anybodys time. It is also worth it to search for issues on any of the bugtrackers of the relevant software. The more helpful and verbose you are, the quicker you are going to receive help.

If this is a problem or question which is very specific to a specific software, consider visiting the dedicated IRC channel for it if there is one. It is more likely to receive a good answer there.

Sometimes it is not possible to pipe the output to a pastebin directly and it should be written into a file before.

This is useful if pasting logs that contain sensitive data, e.g serial numbers in smartctl output, which have to be manually edited out.

The size of our community led to the creation of multiple IRC channels. To get a list of all channels on irc.libera.chat that contain archlinux in their name, use the command /query alis LIST *archlinux*. For further information on how to search channels, see https://libera.chat/guides/findingchannels.

International discussions are available at the following channels, also located at the irc.libera.chat IRC network, unless stated otherwise.

**Examples:**

Example 1 (unknown):
```unknown
NickServ HELP
```

Example 2 (unknown):
```unknown
/query NickServ HELP REGISTER
/query NickServ HELP IDENTIFY
```

Example 3 (unknown):
```unknown
/quote NickServ command
```

Example 4 (unknown):
```unknown
/msg NickServ command
```

---

## VirtualBox/Install Arch Linux as a guest

**URL:** https://wiki.archlinux.org/title/VirtualBox/Install_Arch_Linux_as_a_guest

**Contents:**
- Installation
  - Installation in EFI mode (optional)
  - Install the Guest Additions
- Configuration
  - Load the VirtualBox kernel modules
  - Set optimal framebuffer resolution
  - Launch the VirtualBox guest services
  - Auto-resize Guest Display
  - Hardware acceleration
  - Enable shared folders

This article is about installing Arch Linux in VirtualBox.

Boot the Arch installation media through one of the virtual machine's virtual drives. Then, complete the installation of a basic Arch system as explained in the Installation guide.

Enabling EFI for Arch as guest is optional. If you want to install Arch Linux in EFI mode inside VirtualBox, you must change the firmware mode for the virtual machine. This must be done before installing Arch as guest, changing the option afterwards will result in an unbootable machine unless the setting is reverted.

To enable EFI for a virtual machine using the graphical interface, open the settings of the virtual machine, choose System item from the panel on the left and Motherboard tab from the right panel, and check the checkbox Enable EFI (special OSes only).

Alternatively the same can be accomplished from the command line using VBoxManage:

efi will set the firmware for the virtual machine to EFI with the bitness matching the virtual machine's CPU. To get a specific EFI bitness, set the firmware to efi64 for x86_64 EFI or efi32 for IA32 EFI.

After selecting the kernel from the Arch Linux installation media's menu, the media will hang for a minute or two and will continue to boot the kernel normally afterwards. Be patient.

VirtualBox Guest Additions provides drivers and applications that optimize the guest operating system including improved image resolution and better control of the mouse. Within the installed guest system, install:

The guest additions running on your guest, and the VirtualBox application running on your host must have matching versions, otherwise the guest additions (like shared clipboard) may stop working. If you upgrade your guest (e.g. pacman -Syu), make sure your VirtualBox application on this host is also the latest version. "Check for updates" in the VirtualBox GUI is sometimes not sufficient; check the VirtualBox.org website.

To load the modules automatically, enable vboxservice.service which loads the modules and synchronizes the guest's system time with the host.

To load the modules manually, type:

See VirtualBox#Set guest starting resolution.

After the rather big installation step dealing with VirtualBox kernel modules, now you need to start the guest services. The guest services are actually just a binary executable called VBoxClient which will interact with your X Window System. VBoxClient manages the following features:

All of these features can be enabled independently with their dedicated flags:

Notice that VBoxClient can only be called with one flag at a time, each call spawning a dedicated service process. As a shortcut, the VBoxClient-all bash script enables all of these features.

virtualbox-guest-utils installs /etc/xdg/autostart/vboxclient.desktop that launches VBoxClient-all on logon. If your desktop environment or window manager does not support XDG Autostart, you will need to set up autostarting yourself, see Autostarting#On desktop environment startup and Autostarting#On window manager startup for more details.

VirtualBox can also synchronize the time between the host and the guest, to do this, start/enable the vboxservice.service.

Now, you should have a working Arch Linux guest. Note that features like clipboard sharing are disabled by default in VirtualBox, and you will need to turn them on in the per-VM settings if you actually want to use them (e.g. Settings > General > Advanced > Shared Clipboard).

This option will automatically change the resolution of the Arch guest, whenever the window of the virtual machine is resized. This option is enabled by default, and in graphical interface is located at View > Auto-resize Guest Display. When using KDE Plasma, on GUI login screen (Session) select Plasma (X11) instead of the default session Plasma (Wayland), which does not work with auto-resize.

Hardware acceleration can be activated in the VirtualBox options. The GDM display manager 3.16+ is known to break hardware acceleration support. [1] So if you get issues with hardware acceleration, try out another display manager (lightdm seems to work fine). [2] [3]

If the hardware acceleration does not work as expected, try changing the Graphics Controller option found under the Screen tab in the Display options of the settings GUI. It seems that depending on the host GPU type, not all emulated controllers work equally well.

Shared folders are managed on the host, in the settings of the Virtual Machine accessible via the GUI of VirtualBox, in the Shared Folders tab. There, Folder Path, the name of the mount point identified by Folder name, and options like Read-only, Auto-mount and Make permanent can be specified. These parameters can be defined with the VBoxManage command line utility. See there for more details.

No matter which method you will use to mount your folder, all methods require some steps first.

To avoid this issue /sbin/mount.vboxsf: mounting failed with the error: No such device, make sure the vboxsf kernel module is properly loaded. It should be, since we enabled all guest kernel modules previously.

Two additional steps are needed in order for the mount point to be accessible from users other than root:

Use the following command to mount your folder in your Arch Linux guest:

where shared_folder_name is the Folder name assigned by the hypervisor when the share was created.

If the user is not in the vboxsf group, to give them access to our mountpoint we can specify the mount(8) options uid= and gid= with the corresponding values of the user. These values can obtained from the id command run against this user. For example:

In order for the automounting feature to work you must have checked the auto-mount checkbox in the GUI or used the optional --automount argument with the command VBoxManage sharedfolder.

The shared folder should now appear as /media/sf_shared_folder_name. If users cannot access the shared folders, check that /media has permissions 755 or is owned by the vboxsf group if using permissions 750. This is currently not the default if the /media directory is created by vboxservice.service.

You can use symlinks if you want to have a more convenient access and avoid to browse in that directory, e.g.:

You can mount your directory with fstab. However, to prevent startup problems with systemd, noauto,x-systemd.automount should be added to /etc/fstab. This way, the shared folders are mounted only when those mount points are accessed and not during startup. This can avoid some problems, especially if the guest additions are not loaded yet when systemd reads fstab and mounts the partitions.

As of 2012-08-02, mount.vboxsf does not support the nofail option:

See Working with the serial console#Connect using a terminal emulator program.

From the host, VirtualBox Manager, set the Display Scale-factor to 2.00 or 3.00.

Faulty or missing drivers may cause the guest to freeze after starting Xorg, see for example [4] and [5]. Try disabling 3D acceleration in Settings > Display, and check if all Xorg drivers are installed.

On some window managers (i3, awesome), VirtualBox has issues with fullscreen mode properly due to the overlay bar. To work around this issue, disable Show in Full-screen/Seamless option in Guest Settings > User Interface > Mini ToolBar. See the upstream bug report for more information.

If the guest's screen goes black above a certain size (e.g. above 2048 pixels wide), increasing the Settings > Display > Screen > Video Memory can help.

The AC97 audio driver within the Linux kernel occasionally guesses the wrong clock settings when running inside VirtualBox, leading to audio that is either too slow or too fast. To fix this, create a file in /etc/modprobe.d/ with the following line:

In some cases, audio can have laggy performance (for example lag behind video when streaming video online). A possible workaround can be to use the Intel HD Audio controller in VirtualBox and disable its power saving by adding the following line in a file in /etc/modprobe.d/ in the guest OS:

If you used pacstrap to also #Install the Guest Additions before performing a first boot into the new guest, you will need to umount -l /mnt/dev as root before using pacstrap again; a failure to do this will render it unusable.

To access the raw VMDK image on a Windows host, run the VirtualBox GUI as administrator.

virtualbox-guest-utils package as of version 5.2.16-2 does not contain the file VBoxEGL.so. This causes the Arch Linux guest to not have proper 3D acceleration. See FS#49752.

To deal with this problem, apply the patch set at FS#49752#comment152254. Some fix to the patch set is required to make it work for version 5.2.16-2.

See KDE#Cannot change screen resolution when running in a virtual machine.

If you used plasma-desktop minimal install instead of plasma (which includes Wayland support), then probably you will have black screen with cursor after starting Plasma-X11 session.

To fix this, resize the VirtualBox window several times, then set resolution manually in VirtualBox window itself by: View > Virtual Screen 1 > Resize to 1024x768 (or other resolution you like).

Then install kscreen.

Open in KDE launcher System Settings > Startup and Shutdown > Background Services, stop and unselect KScreen2 and save settings. Issue should go away forever.

**Examples:**

Example 1 (unknown):
```unknown
$ VBoxManage modifyvm "Virtual machine name" --firmware efi
```

Example 2 (unknown):
```unknown
rcvboxadd setup
```

Example 3 (unknown):
```unknown
pacman -Syu
```

Example 4 (unknown):
```unknown
vboxservice.service
```

---

## DSDT

**URL:** https://wiki.archlinux.org/title/DSDT

**Contents:**
- Before you start
  - Tell the kernel to report a version of Windows
  - Find a fixed DSDT
- Recompiling it yourself
- Using modified code
  - Using mkinitcpio's acpi_override hook
  - Using a CPIO archive
  - Compiling into the kernel
  - Using the AML with GRUB
  - Using the AML with dracut

DSDT (Differentiated System Description Table) is a part of the ACPI specification. It supplies information about supported power events in a given system. ACPI tables are provided in firmware from the manufacturer. A common Linux problem is missing ACPI functionality, such as: fans not running, screens not turning off when the lid is closed, etc. This can stem from DSDTs made with Windows specifically in mind, which can be patched after installation. The goal of this article is to analyze and rebuild a faulty DSDT, so that the kernel can override the default one.

Basically a DSDT table is the code run on ACPI (Power Management) events.

It is possible that the hardware manufacturer has released an updated firmware which fixes ACPI related problems. Installing an updated firmware is often preferred over this method because it would avoid duplication of effort.

This process does tamper with some fairly fundamental code on your installation. You will want to be absolutely sure of the changes you make. You might also wish to clone your disk beforehand.

Even before attempting to fix your DSDT yourself, you can attempt a couple of different shortcuts:

Use the variable acpi_os_name as a kernel parameter. For example:

To add a recognized OS interface, use the variable acpi_osi.

To use only one OS interface, add acpi_osi=!. This tells the firmware that there is only one supported operating system, so this is often the recommended solution.

To remove an interface, use an exclamation point in the beginning of the string.

Other strings to test:

Out of curiousity, you can follow the steps below to extract your DSDT and search the .dsl file. Just grep for "Windows" and see what pops up.

A DSDT file is originally written in ACPI Source language (an .asl/.dsl file). Using a compiler this can produce an 'ACPI Machine Language' file (.aml) or a hex table (.hex). To incorporate the file in your Arch install, you will need to get hold of a compiled .aml file — whether this means compiling it yourself or trusting some stranger on the Internet is at your discretion. If you do download a file from the world wide web, it will most likely be a compressed .asl file. So you will need to unzip it and compile it. The upside to this is that you will not have to research specific code fixes yourself.

Arch users with the same laptop as you are: a minority of a minority of a minority. Try browsing other distributions/Linux forums for talk about the same model. It is likely they have the same problems and either because there is a lot of them, or because they are tech savvy — someone there has produced a working DSDT and may even provide a precompiled version (again, use at your own risk). Search engines are your best tools. Try keeping it short: 'model name' + 'dsdt' will probably produce results.

Your best resources in this endeavor are going to be ACPI Spec homepage, and Linux ACPI Project[dead link 2023-09-16—HTTP 404] which supercedes the activity that occurred at acpi.sourceforge.net. In a nutshell, you can use Intel's ASL compiler to turn your systems DSDT table into source code, locate/fix the errors, and recompile.

You will need to install acpica to modify code.

What compiled the original code? Check if your system's DSDT was compiled using Intel or Microsoft compiler:

In case Microsoft's compiler had been used, abbreviation INTL would instead be MSFT. In the example, there were 5 errors on decompiling/recompiling the DSDT. Two of them were easy to fix after a bit of googling and delving into the ACPI specification. Three of them were due to different versions of compiler used and are, as later discovered, handled by the ACPICA at boot-time. The ACPICA component of the kernel can handle most of the trivial errors you get while compiling the DSDT. So do not fret yourself over compile errors if your system is working the way it should.

Extract the binary ACPI tables:

Disassemble the ACPI tables to a .dsl file:

Attempt to create a hex AML table (in C) from the .dsl file:

Examine any errors outputted from creating the hex AML table and fix them. For example:

Amend the file at line 6727 where the error occurred:

Increase the OEM version. Otherwise, the kernel will not apply the modified ACPI table. For example, before increasing the OEM version:

After increasing the OEM version:

Create the hex AML table again after fixing all errors and increasing the OEM version:

You might want to try the option -ic for C include file to insert into kernel source. If no errors and no warnings are raised, you should be good to go.

There are at least two ways to use a custom DSDT:

mkinitcpio provides an acpi_override hook which takes all .aml files found in /usr/initcpio/acpi_override/ and /etc/initcpio/acpi_override/ and places them in an early uncompressed CPIO archive inside /kernel/firmware/acpi/. This avoids the need to manually create a separate CPIO archive or to change the boot loader configuration since mkinitcpio packs the uncompressed CPIO archive together with the main initramfs image into one file.

First, create the /etc/initcpio/acpi_override directory and copy all needed .aml files to it. E.g.:

Add acpi_override to the HOOKS array in /etc/mkinitcpio.conf:

Finally, regenerate the initramfs and reboot.

This method has the advantage that you do not need to recompile your kernel, and updating the kernel will not make it necessary to repeat these steps.

This method requires the ACPI_TABLE_UPGRADE=y kernel configuration to be enabled (true for the linux package). See [1] for details.

First, create the following folder structure:

Copy the fixed ACPI tables into the just created kernel/firmware/acpi folder, for example:

Within the same folder where the newly created kernel/ folder resides, run:

This creates the CPIO archive containing the fixed ACPI tables. Copy the archive to the boot directory.

Lastly, configure the boot loader to load your CPIO archive, like the examples in Microcode#Microcode in a separate initramfs file.

Now all that is left to do is to reboot and to verify the result.

You will want to be familiar with compiling your own kernel. The most straightforward way is with the "traditional" approach. After compiling DSDT, iasl produce two files: dsdt.hex and dsdt.aml.

If you use GRUB you can use an even easier method. Copy the above created .aml file to your boot partition:

Then add the following line to your GRUB config:

You can e.g. add this to /etc/grub.d/40_custom, don't forget to generate your GRUB config afterwards.

If you use Dracut, you can simply copy the above created .aml file to a defined location. An according configuration file /etc/dracut.conf.d/acpi-fix.conf must be created:

Look for messages that confirm the override, for example:

**Examples:**

Example 1 (unknown):
```unknown
acpi_os_name
```

Example 2 (unknown):
```unknown
acpi_os_name="Microsoft Windows NT"
```

Example 3 (unknown):
```unknown
acpi_osi="Linux"
```

Example 4 (unknown):
```unknown
acpi_osi=! acpi_osi="Windows 2022"
```

---

## pacman

**URL:** https://wiki.archlinux.org/title/Installation_reason

**Contents:**
- Usage
  - Installing packages
    - Installing specific packages
      - Virtual packages
    - Installing package groups
  - Removing packages
  - Upgrading packages
  - Querying package databases
    - Pactree
    - Database structure

The pacman package manager is one of the major distinguishing features of Arch Linux. It combines a simple binary package format with an easy-to-use Arch build system. The goal of pacman is to make it possible to easily manage packages, whether they are from the official repositories or the user's own builds.

Pacman keeps the system up-to-date by synchronizing package lists with the master server. This server/client model also allows the user to download/install packages with a simple command, complete with all required dependencies.

Pacman is written in the C programming language and uses the bsdtar(1) tar format for packaging.

What follows is just a small sample of the operations that pacman can perform. To read more examples, refer to pacman(8).

A package is an archive containing:

Arch's package manager pacman can install, update, and remove those packages. Using packages instead of compiling and installing programs yourself has various benefits:

To install a single package or list of packages, including dependencies, issue the following command:

To install a list of packages with regex (see this forum thread):

Sometimes there are multiple versions of a package in different repositories (e.g. extra and extra-testing). To install the version from the extra repository in this example, the repository needs to be defined in front of the package name:

To install a number of packages sharing similar patterns in their names, one can use curly brace expansion. For example:

This can be expanded to however many levels needed:

A virtual package is a special package which does not exist by itself, but is provided by one or more other packages. Virtual packages allow other packages to not name a specific package as a dependency, in case there are several candidates. Virtual packages cannot be installed by their name, instead they become installed in your system when you have installed a package providing the virtual package. An example is the dbus-units package.

Some packages belong to a group of packages that can all be installed simultaneously. For example, issuing the command:

will prompt you to select the packages from the gnome group that you wish to install.

Sometimes a package group will contain a large amount of packages, and there may be only a few that you do or do not want to install. Instead of having to enter all the numbers except the ones you do not want, it is sometimes more convenient to select or exclude packages or ranges of packages with the following syntax:

which will select packages 1 through 10 and 15 for installation, or:

which will select all packages except 5 through 8 and 2 for installation.

To see what packages belong to the gnome group, run:

Also visit https://archlinux.org/groups/ to see what package groups are available.

To remove a single package, leaving all of its dependencies installed:

To remove a package and its dependencies which are not required by any other installed package:

The above may sometimes refuse to run when removing a group which contains otherwise needed packages. In this case try:

To remove a package, its dependencies and all the packages that depend on the target package:

To remove a package, which is required by another package, without removing the dependent package:

Pacman saves important configuration files when removing certain applications and names them with the extension: .pacsave. To prevent the creation of these backup files use the -n option:

Pacman can update all packages on the system with just one command. This could take quite a while depending on how up-to-date the system is. The following command synchronizes the repository databases and updates the system's packages, excluding "local" packages that are not in the configured repositories:

Pacman queries the local package database with the -Q flag, the sync database with the -S flag and the files database with the -F flag. See pacman -Q --help, pacman -S --help and pacman -F --help for the respective suboptions of each flag.

Pacman can search for packages in the database, searching both in packages' names and descriptions:

Sometimes, -s's builtin ERE (Extended Regular Expressions) can cause a lot of unwanted results, so it has to be limited to match the package name only; not the description nor any other field:

To search for already installed packages:

To search for package file names in remote packages:

To display extensive information about a given package (e.g. its dependencies):

For locally installed packages:

Passing two -i flags will also display the list of backup files and their modification states:

To retrieve a list of the files installed by a package:

To retrieve a list of the files installed by a remote package:

To verify the presence of the files installed by a package:

Passing the k flag twice will perform a more thorough check.

To query the database to know which package a file in the file system belongs to:

To query the database to know which remote package a file belongs to:

To list all packages no longer required as dependencies (orphans):

To list all packages explicitly installed and not required as dependencies:

See pacman/Tips and tricks for more examples.

For advanced functionality, install pkgfile, which uses a separate database with all files and their associated packages.

To view the dependency tree of a package:

To view the dependent tree of a package, pass the reverse flag -r to pactree.

The pacman databases are normally located at /var/lib/pacman/sync. For each repository specified in /etc/pacman.conf, there will be a corresponding database file located there. Database files are gzipped tar archives containing one directory for each package, for example for the which package:

The desc file contains meta data such as the package description, dependencies, file size and MD5 hash.

Pacman stores its downloaded packages in /var/cache/pacman/pkg/ and does not remove the old or uninstalled versions automatically. This has some advantages:

However, it is necessary to deliberately clean up the cache periodically to prevent the directory to grow indefinitely in size.

The paccache(8) script, provided within the pacman-contrib package, deletes all cached versions of installed and uninstalled packages, except for the most recent three, by default:

Enable and start paccache.timer to discard unused packages weekly. You can configure the arguments for the service in /etc/conf.d/pacman-contrib, e.g with PACCACHE_ARGS='-k1' or PACCACHE_ARGS='-uk0' for the two examples below.

You can also define how many recent versions you want to keep. To retain only one past version use:

Add the -u/--uninstalled switch to limit the action of paccache to uninstalled packages. For example to remove all cached versions of uninstalled packages, use the following:

See paccache -h for more options.

Pacman also has some built-in options to clean the cache and the leftover database files from repositories which are no longer listed in the configuration file /etc/pacman.conf. However pacman does not offer the possibility to keep a number of past versions and is therefore more aggressive than paccache default options.

To remove all the cached packages that are not currently installed, and the unused sync databases, execute:

To remove all files from the cache, use the clean switch twice, this is the most aggressive approach and will leave nothing in the cache directory:

pkgcachecleanAUR and pacleanerAUR are two further alternatives to clean the cache.

Download a package without installing it:

Install a 'local' package that is not from a remote repository (e.g. the package is from the AUR):

To keep a copy of the local package in pacman's cache, use:

Install a 'remote' package (not from a repository stated in pacman's configuration files):

Pacman always lists packages to be installed or removed, and asks for permission before taking any action.

To get a list in a processable format, and to prevent the actions of -S, -U and -R, you can use -p, short for --print.

--print-format can be added to format this list in various ways. --print-format %n will return a list without package versions.

The pacman database organizes installed packages into two groups, according to installation reason:

When installing a package, it is possible to force its installation reason to dependency with:

The command is normally used because explicitly-installed packages may offer optional packages, usually for non-essential features for which the user has discretion.

When reinstalling a package, though, the current installation reason is preserved by default.

The list of explicitly-installed packages can be shown with pacman -Qe, while the complementary list of dependencies can be shown with pacman -Qd.

To change the installation reason of an already installed package, execute:

Use --asexplicit to do the opposite operation.

When successful, the workflow of a transaction follows five high-level steps plus pre/post transaction hooks:

Pacman settings are located in /etc/pacman.conf: this is the place where the user configures the program to work in the desired manner. In-depth information about the configuration file can be found in pacman.conf(5).

General options are in the [options] section. Read pacman.conf(5) or look in the default pacman.conf for information on what can be done here.

To see old and new versions of available packages, uncomment the "VerbosePkgLists" line in /etc/pacman.conf. The output of pacman -Syu will be like this:

The number of packages being downloaded in parallel (at the same time) are configured in /etc/pacman.conf with the ParallelDownloads option under [options]. The /etc/pacman.conf shipped with the pacman package sets it to 5. If the option is unset, packages will be downloaded sequentially.

To have a specific package skipped when upgrading the system, add this line in the [options] section:

For multiple packages use a space-separated list, or use additional IgnorePkg lines. Also, glob patterns can be used. If you want to skip packages just once, you can also use the --ignore option on the command-line - this time with a comma-separated list.

It will still be possible to upgrade the ignored packages using pacman -S: in this case pacman will remind you that the packages have been included in an IgnorePkg statement.

As with packages, skipping a whole package group is also possible:

All files listed with a NoUpgrade directive will never be touched during a package install/upgrade, and the new files will be installed with a .pacnew extension.

Multiple files can be specified like this:

To always skip installation of specific files or directories list them under NoExtract. For example, to avoid installing bash completion scripts, use:

Later rules override previous ones, and you can negate a rule by prepending !.

If you have several configuration files (e.g. main configuration and configuration with testing repository enabled) and would have to share options between configurations you may use Include option declared in the configuration files, e.g.:

where /path/to/common/settings file contains the same options for both configurations.

Pacman can run pre- and post-transaction hooks from the /usr/share/libalpm/hooks/ directory; more directories can be specified with the HookDir option in pacman.conf, which defaults to /etc/pacman.d/hooks. Hook file names must be suffixed with .hook. Pacman hooks are not interactive.

Pacman hooks are used, for example, in combination with systemd-sysusers and systemd-tmpfiles to automatically create system users and files during the installation of packages. For example, tomcat8 specifies that it wants a system user called tomcat8 and certain directories owned by this user. The pacman hooks systemd-sysusers.hook and systemd-tmpfiles.hook invoke systemd-sysusers and systemd-tmpfiles when pacman determines that tomcat8 contains files specifying users and tmp files.

For more information on alpm hooks, see alpm-hooks(5).

Besides the special [options] section, each other [section] in pacman.conf defines a package repository to be used. A repository is a logical collection of packages, which are physically stored on one or more servers: for this reason each server is called a mirror for the repository.

Repositories are distinguished between official and unofficial. The order of repositories in the configuration file matters; repositories listed first will take precedence over those listed later in the file when packages in two repositories have identical names, regardless of version number. In order to use a repository after adding it, you will need to upgrade the whole system first.

Each repository section allows defining the list of its mirrors directly or in a dedicated external file through the Include directive; for example, the mirrors for the official repositories are included from /etc/pacman.d/mirrorlist. See the Mirrors article for mirror configuration.

Pacman stores downloaded package files in cache, in a directory denoted by CacheDir in [options] section of pacman.conf (defaults to /var/cache/pacman/pkg/ if not set).

Cache directory may grow over time, even if keeping just the freshest versions of installed packages.

If you want to move that directory to some more convenient place, do one of the following:

Pacman supports package signatures, which add an extra layer of security to the packages. The default configuration, SigLevel = Required DatabaseOptional, enables signature verification for all the packages on a global level. This can be overridden by per-repository SigLevel lines. For more details on package signing and signature verification, take a look at pacman-key.

If you see the following error: [1]

This is happening because pacman has detected a file conflict, and by design, will not overwrite files for you. This is by design, not a flaw.

The problem is usually trivial to solve (although to be sure, you should try to find out how these files got there in the first place). A safe way is to first check if another package owns the file (pacman -Qo /path/to/file). If the file is owned by another package, file a bug report. If the file is not owned by another package, rename the file which "exists in filesystem" and re-issue the update command. If all goes well, the file may then be removed.

If you had installed a program manually without using pacman, for example through make install, you have to remove/uninstall this program with all of its files. See also Pacman tips#Identify files not owned by any package.

Every installed package provides a /var/lib/pacman/local/package-version/files file that contains metadata about this package. If this file gets corrupted, is empty or goes missing, it results in file exists in filesystem errors when trying to update the package. Such an error usually concerns only one package. Instead of manually renaming and later removing all the files that belong to the package in question, you may explicitly run pacman -S --overwrite glob package to force pacman to overwrite files that match glob.

This article or section is out of date.

Look for .part files (partially downloaded packages) in /var/cache/pacman/pkg/ and remove them (often caused by usage of a custom XferCommand in pacman.conf).

That same error may also appear if archlinux-keyring is out-of-date, preventing pacman from verifying signatures. See Pacman/Package signing#Upgrade system regularly for the fix and how to avoid it in the future.

When pacman is about to alter the package database, for example installing a package, it creates a lock file at /var/lib/pacman/db.lck. This prevents another instance of pacman from trying to alter the package database at the same time.

If pacman is interrupted while changing the database, this stale lock file can remain. If you are certain that no instances of pacman are running then delete the lock file:

This error manifests as Not found in sync db, Target not found or Failed retrieving file.

Firstly, ensure the package actually exists. If certain the package exists, your package list may be out-of-date. Try running pacman -Syu to force a refresh of all package lists and upgrade. Also make sure the selected mirrors are up-to-date and repositories are correctly configured. You can also use Reflector to keep the mirrors up-to-date.

If pacman reports there is nothing to update, but the Failed retrieving file error continues to be printed, consider forcing a database download with pacman -Syyu. This is never needed under normal circumstances, so inspect more closely the status and consistency of the mirror.

It could also be that the repository containing the package is not enabled on your system, e.g. the package could be in the multilib repository, but multilib is not enabled in your pacman.conf.

See also FAQ#Why is there only a single version of each shared library in the official repositories?.

This article or section needs expansion.

Whether due to power loss, kernel panic or hardware failure an update may be interrupted. In most cases, there will not be much damage but the system will likely be unbootable.

Replicating the exact upgrade is needed to ensure the right scriptlets and hooks will run.

In the case that pacman crashes with a "database write" error while removing packages, and reinstalling or upgrading packages fails thereafter, do the following:

If /var/cache/pacman/pkg is a symlink, pacman will try to make a directory instead and thus remove this symlink during self-upgrade. This will cause the update to fail. As a result, /usr/bin/pacman and other contents of the pacman package will be missing.

Never symlink /var/cache/pacman/pkg because it is controlled by pacman. Use the CacheDir option or a bind mount instead; see #Package cache directory.

If you have already encountered this problem and broke your system, you can manually extract /usr contents from the package to restore pacman and then reinstall it properly; see FS#73306 and related forum thread for details.

pacman-staticAUR is a statically compiled version of pacman, so it will be able to run even when the libraries on the system are not working. This can also come in handy when a partial upgrade was performed and pacman can not run anymore.

The pinned comment and the PKGBUILD provides a way to directly download the binary, which can be used to reinstall pacman or to upgrade the entire system in case of partial upgrades.

In some situations, your system may be too broken (e.g., due to missing or incompatible libraries) to run `makepkg` or build the `pacman-static` package from the AUR successfully.

If building from the PKGBUILD fails or `makepkg` cannot be run, you can download a precompiled `pacman-static` binary from a trusted source. This static binary does not depend on system libraries and can be used to restore a working `pacman` on your system.

A reliable source for the binary is:

This will update your system and reinstall `pacman`, fixing broken dependencies related to missing shared libraries.

If even pacman-static does not work, it is possible to recover using an external pacman. One of the easiest methods to do so is by using the archiso and simply using --sysroot or --root to specify the mount point of the system to perform the operation on. See Chroot#Using chroot on how to mount the necessary filesystems required by --sysroot.

Even if pacman is terribly broken, you can fix it manually by downloading the latest packages and extracting them to the correct locations. The rough steps to perform are:

If you have a healthy Arch system on hand, you can see the full list of dependencies with:

But you may only need to update a few of them depending on your issue. An example of extracting a package is

Note the use of the w flag for interactive mode. Running non-interactively is very risky since you might end up overwriting an important file. Also take care to extract packages in the correct order (i.e. dependencies first). This forum post contains an example of this process where only a couple pacman dependencies are broken.

Most likely the initramfs became corrupted during a kernel update (improper use of pacman's --overwrite option can be a cause). There are two options; first, try the Fallback entry.

Once the system starts, run this command (for the stock linux kernel) either from the console or from a terminal to rebuild the initramfs image:

If that does not work, from a current Arch release (CD/DVD or USB stick), mount your root and boot partitions to /mnt and /mnt/boot, respectively. Then chroot using arch-chroot:

Reinstalling the kernel (the linux package) will automatically re-generate the initramfs image with mkinitcpio -p linux. There is no need to do this separately.

Afterwards, it is recommended that you run exit, umount /mnt/{boot,} and reboot.

As the error message says, your locale is not correctly configured. See Locale.

When locale files are intentionally removed by tools such as bleachbit or localepurgeAUR, pacman may issue warnings about missing locales during package updates.

To suppress these warnings, you can comment out the CheckSpace option in pacman.conf. Keep in mind that disabling CheckSpace turns off the space-checking functionality for all package installations, so use this workaround only when you have alternative means to monitor disk space.

Make sure that the relevant environment variables ($http_proxy, $ftp_proxy etc.) are set up. If you use pacman with sudo, you need to configure sudo to pass these environment variables to pacman. Also, ensure the configuration of dirmngr has honor-http-proxy in /etc/pacman.d/gnupg/dirmngr.conf to honor the proxy when refreshing the keys.

To reinstall all the native packages: pacman -Qnq | pacman -S - or pacman -S $(pacman -Qnq) (the -S option preserves the installation reason by default).

You will then need to reinstall all the foreign packages, which can be listed with pacman -Qmq.

It looks like previous pacman transaction removed or corrupted shared libraries needed for pacman itself.

To recover from this situation, you need to unpack required libraries to your filesystem manually. First find what package contains the missed library and then locate it in the pacman cache (/var/cache/pacman/pkg/). Unpack required shared library to the filesystem. This will allow to run pacman.

Now you need to reinstall the broken package. Note that you need to use --overwrite flag as you just unpacked system files and pacman does not know about it. Pacman will correctly replace our shared library file with one from package.

That's it. Update the rest of the system.

Some issues have been reported regarding network problems that prevent pacman from updating/synchronizing repositories. [2] [3] When installing Arch Linux natively, these issues have been resolved by replacing the default pacman file downloader with an alternative (see Improve pacman performance for more details). When installing Arch Linux as a guest OS in VirtualBox, this issue has also been addressed by using Host interface instead of NAT in the machine properties.

If you receive this error message with correct mirrors, try setting a different name server.

If you want to install a package on an sshfs mount using pacman -U and receive this error, move the package to a local directory and try to install again.

Upon executing, e.g., pacman -Syu inside a chroot environment an error is encountered:

This is frequently caused by the chroot directory not being a mountpoint when the chroot is entered. See the note at Install Arch Linux from existing Linux#Downloading basic tools for a solution, and arch-chroot(8) for an explanation and an example of using bind mounting to make the chroot directory a mountpoint.

If you are unable to update packages and receive this error, then try rm -r /var/lib/pacman/sync/ before attempting to update.

If removing sync files doesn't help, check that the sync files are gzip compressed data using file /var/lib/pacman/sync/* before attempting to update. A router or proxy might corrupt the downloads. Corruption could possibly be HTML type.

If sync files are of the correct type, there might be an issue with the mirror server. Look up the mirror server(s) in use with pacman-conf -r core and pacman-conf -r extra. Paste the first returned url in a browser and check that a file listing is returned. In case the mirror returns an error, comment it in /etc/pacman.d/mirrorlist. You may try updating or re-ranking mirrors.

If this error occurs and you're for instance unable to update your system or any package at all, it is possible that you have DISPLAY set to a blank value, which seems to break the GPG-Flow.

In this case, unset DISPLAY or setting it to a arbitrary value will most likely allow to update again, in case any other option above didn't do the trick yet. See this post for further details.

One may use the pacman -Qk $pkg to check if the installed files of the $pkg package match the files from its database version. For several packages, one may use the following loop to reinstall all packages which have missing file(s):

Suppose that your local database located in /var/lib/pacman is more up-to-date compared to installed packages in the / filesystem (e.g., because of a partial rollback), then this method is the appropriate one to re-synchronize the root filesystem with the local database.

**Examples:**

Example 1 (unknown):
```unknown
pacman -Ql pacman pacman-contrib | grep -E 'bin/.+'
```

Example 2 (unknown):
```unknown
pacman -Sy package_name
```

Example 3 (unknown):
```unknown
pacman -Syu package_name
```

Example 4 (unknown):
```unknown
# pacman -S package_name1 package_name2 ...
```

---

## cron

**URL:** https://wiki.archlinux.org/title/Cron

**Contents:**
- Installation
- Configuration
  - Activation and autostart
  - Handling errors of jobs
    - Example with sSMTP
    - Example with msmtp
    - Example with esmtp
    - Example with opensmtpd
    - Long cron job
- Crontab format

There are many cron implementations, but none of them are installed by default as the base system uses systemd/Timers instead. See the Gentoo wiki's cron guide, which offers comparisons.

After installation, the daemon will not be enabled by default. The installed package likely provides a service, which can be controlled by systemctl. For example, cronie uses cronie.service.

Check /etc/cron.daily/ and similar directories to see which jobs are present. Activating cron service will trigger all of them.

cron registers the output from stdout and stderr and attempts to send it as email to the user's spools via the sendmail command. Cronie disables mail output if /usr/bin/sendmail is not found. In order for mail to be written to a user's spool, there must be an smtp daemon running on the system, e.g. opensmtpd. Otherwise, you can install a package that provides the sendmail command, and configure it to send mail to a remote mail exchanger. You can also log the messages by using the -m option and writing a custom script.

sSMTP is a send-only sendmail emulator which delivers email from a local computer to an smtp server. While there are currently no active maintainers, it is still by far the simplest way to transfer mail to a configured mailhub. There are no daemons to run, and configuration can be as simple as editing 3 lines in a single configuration file (if your host is trusted to relay unauthenticated email through your mailhub). sSMTP does not receive mail, expand aliases, or manage a queue.

Install ssmtpAUR, which creates a symbolic link from /usr/bin/sendmail to /usr/bin/ssmtp. You must then edit /etc/ssmtp/ssmtp.conf. See sSMTP for details. Creating a symbolic link to /usr/bin/sendmail insures that programs like S-nail (or any package which provides /usr/bin/mail) will just work without modification.

Restart cronie.service to insure that it detects that you now have a /usr/bin/sendmail installed.

Install msmtp-mta, which creates a symbolic link from /usr/bin/sendmail to /usr/bin/msmtp. Restart cronie.service to make sure it detects the new sendmail command. You must then provide a way for msmtp to convert your username into an email address.

Then either add MAILTO line to your crontab, like so:

or create /etc/msmtprc and append this line:

and create /etc/aliases:

Then modify the configuration of cronie daemon by replacing the ExecStart command with:

Install esmtpAUR and procmailAUR.

After installation configure the routing:

Procmail needs root privileges to work in delivery mode but it is not an issue if you are running the cronjobs as root anyway.

To test that everything works correctly, create a file message.txt with "test message" in it.

From the same directory run:

You should now see the test message and the time and date it was sent.

The error output of all jobs will now be redirected to /var/spool/mail/user_name.

Due to the privileged issue, it is hard to create and send emails to root (e.g. su -c ""). You can ask esmtp to forward all root's email to an ordinary user with:

Run the following command to make sure it has the correct permission:

Edit /etc/smtpd/smtpd.conf. The following configuration allows for local delivery:

You can proceed to test it. First start smtpd.service. Then do:

user can check their mail in with any reader able to handle mbox format, or just have a look at the file /var/spool/mail/user. If everything goes as expected, you can enable opensmtpd for future boots.

This approach has the advantage of not sending local cron notifications to a remote server. On the downside, you need a new daemon running.

Suppose this program is invoked by cron :

What happens is this:

To solve this problem you can use the command chronic or sponge from moreutils. From their respective man page:

Chronic too buffers the command output before opening its standard output.

The basic format for a crontab is:

Spaces are used to separate fields. To fine-tune your schedule you may also use one of the following symbols:

For example, the line:

will execute the script i_love_cron.sh at five minute intervals from 9 AM to 4:55 PM on weekdays except during the months of June, July, and August.

In addition, crontab has some special keywords:

will execute the script i_love_cron.sh at startup.

See more at: https://www.adminschoice.com/crontab-quick-reference

More examples and advanced configuration techniques can be found below.

Crontabs should never be edited directly; instead, you should use the crontab program to work with your crontabs.

To view your crontabs:

To edit your crontabs:

To remove all of your crontabs:

If you have a saved crontab and would like to completely overwrite your old crontab:

To overwrite a crontab from the command line (Wikipedia:stdin):

To edit somebody else's crontab:

This same format (appending -u username to a command) works for listing and deleting crontabs as well.

runs the command /bin/echo Hello, world! on the first minute of every hour of every day of every month (i.e. at 12:01, 1:01, 2:01, etc.).

runs the same job every five minutes on weekdays during the month of January (i.e. at 12:00, 12:05, 12:10, etc.).

The line (as noted in crontab(5)):

will execute the script i_love_cron.sh at five minute intervals from 9 AM to 5 PM (excluding 5 PM itself) every weekday (Mon-Fri) of every month except during the summer (June, July, and August).

Periodical settings can also be entered as in this crontab template:

Here are some self-explanatory crontab syntax examples:

To use an alternate default editor, define the EDITOR environment variable in a shell initialization script as described in Environment variables.

As a regular user, su will need to be used instead of sudo for the environment variable to be pulled correctly:

To have an alias to this printf is required to carry the arbitrary string because su launches in a new shell:

Cron does not run under the X.org server therefore it cannot know the environmental variable necessary to be able to start an X.org server application so they will have to be defined. One can use a program like xuserrun-gitAUR to do it:

This article or section is out of date.

Or they can be defined manually (echo $DISPLAY will give the current DISPLAY value):

If running notify-send for desktop notifications in cron, notify-send is sending values to dbus. So it needs to tell dbus to connect to the right bus. The address can be found by examining DBUS_SESSION_BUS_ADDRESS environment variable and setting it to the same value. Therefore:

If done through say SSH, permission will need be given:

If you regularly turn off your computer but do not want to miss jobs, there are some solutions available (easiest to hardest):

cronie comes with anacron included. The project homepage says:

Cronie contains the standard UNIX daemon crond that runs specified programs at scheduled times and related tools. It is based on the original cron and has security and configuration enhancements like the ability to use pam and SELinux.

Vanilla dcronAUR supports asynchronous job processing. Just put it with @hourly, @daily, @weekly or @monthly with a jobname, like this:

cronwhipAUR is a script to automatically run missed cron jobs; it works with the former default cron implementation, dcron. See also the forum thread.

Anacron is a full replacement for dcron which processes jobs asynchronously.

It is provided by cronie. The configuration file is /etc/anacrontab. Information on the format can be found in the anacrontab(5). Running anacron -T will test /etc/anacrontab for validity.

Like anacron, fcron assumes the computer is not always running and, unlike anacron, it can schedule events at intervals shorter than a single day which may be useful for systems which suspend/hibernate regularly (such as a laptop). Like cronwhip, fcron can run jobs that should have been run during the computer's downtime.

When replacing cronie with fcron be aware the spool directory is /var/spool/fcron and the fcrontab command is used instead of crontab to edit the user crontabs. These crontabs are stored in a binary format with the text version next to them as foo.orig in the spool directory. Any scripts which manually edit user crontabs may need to be adjusted due to this difference in behavior.

A quick scriptlet which may aide in converting traditional user crontabs to fcron format:

See also the forum thread.

If you run potentially long-running jobs (e.g., a backup might all of a sudden run for a long time, because of many changes or a particular slow network connection), then flock (util-linux) can ensure that the cron job will not start a second time.

The relevant file hierarchy for cronie is the following:

Cronie provides both cron and anacron functionalities: cron runs jobs at regular time intervals (down to a granularity of one minute) as long as the system is available at the specified time, while anacron executes commands at intervals specified in days. Unlike cron, it does not assume that the system is running continuously. Whenever the system is up, anacron checks if there are any jobs that should have been run and handles them accordingly.

A cron job can be defined in a crontab-like file in the /etc/cron.d directory or added within the /etc/crontab file. Note the latter is not present by default but is used if it exists. As instructed by /etc/cron.d/0hourly, any executable file in /etc/cron.hourly will be run every hour (by default at minute 1 of the hour). Files in /etc/cron.minutely are executed every minute if instructed accordingly in /etc/cron.d/0minutely. The executables are typically shell scripts, symlinks to executable files can also be used. The /etc/cron.deny file includes the list of users not allowed to use crontab, without this file, only users listed in /etc/cron.allow can use it.

Anacron works similarly, by executing the files in the /etc/cron.daily, /etc/cron.weekly and /etc/cron.monthly directories, placed there depending on the desired job frequency. The cron job /etc/cron.hourly/0anacron makes sure that anacron is run once daily to perform its pending tasks.

The cron daemon parses a configuration file known as crontab. Each user on the system can maintain a separate crontab file to schedule commands individually. The root user's crontab is used to schedule system-wide tasks (though users may opt to use /etc/crontab or the /etc/cron.d directory, depending on which cron implementation they choose).

These lines exemplify one of the formats that crontab entries can have, namely whitespace-separated fields specifying:

The other standard format for crontab entries is:

The crontab files themselves are usually stored as /var/spool/cron/username. For example, root's crontab is found at /var/spool/cron/root

See the crontab man page for further information and configuration examples.

**Examples:**

Example 1 (unknown):
```unknown
cronie.service
```

Example 2 (unknown):
```unknown
/etc/cron.daily/
```

Example 3 (unknown):
```unknown
/usr/bin/sendmail
```

Example 4 (unknown):
```unknown
cronie.service
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Extra-testing

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## systemd-repart

**URL:** https://wiki.archlinux.org/title/Systemd-repart

**Contents:**
- Installation
- Usage
  - During Arch Linux Installation

systemd-repart(8) is a tool for manipulating GUID Partition Tables (GPTs).

systemd-repart is part of systemd. It is also present on the Arch Linux installation ISO.

systemd-repart can be used to create the necessary partitions during the Arch Linux installation process. Follow the steps below to set up your partitions.

First, create the required repart.d(5) configuration files. The following examples illustrate how to define partitions; adjust the parameters as needed for your specific setup.

Create the directory for the repart configuration files:

Then, create the configuration files for each partition:

After creating the configuration files, you can check the proposed changes by running:

If the output meets your expectations, you can apply the changes by executing:

This command will create the partitions as specified in your configuration files, and automatically encrypt and/or format them if required. Ensure that you have backed up any important data before proceeding, as this operation may overwrite existing data on the specified disk.

For more advanced configurations, refer to repart.d(5).

Then, mount the required partitions and proceed with the rest of the installation:

**Examples:**

Example 1 (unknown):
```unknown
# mkdir /etc/repart.d
```

Example 2 (unknown):
```unknown
/etc/repart.d/00-esp.conf
```

Example 3 (unknown):
```unknown
[Partition]
Type=esp
SizeMinBytes=1G
SizeMaxBytes=1G
Format=vfat
```

Example 4 (unknown):
```unknown
/etc/repart.d/10-root.conf
```

---

## Bubblewrap

**URL:** https://wiki.archlinux.org/title/Bubblewrap

**Contents:**
- Installation
- Configuration
- Configuration managers for bubblewrap
- Usage examples
  - No-op
  - Bash
  - Desktop entries
  - Filesystem isolation
- Troubleshooting
  - Using X11

Bubblewrap is a lightweight sandbox application used by Flatpak and other container tools. It has a small installation footprint and minimal resource requirements. While the package is named bubblewrap, the actual command-line interface is bwrap(1). Notable features include support for cgroup/IPC/mount/network/PID/user/UTS namespaces and seccomp filtering. Note that bubblewrap drops all capabilities within a sandbox and that child tasks cannot gain greater privileges than its parent. Notable feature exclusions include the lack of explicit support for blacklisting/whitelisting file paths.

Install the bubblewrap package.

Bubblewrap can be called directly from the command-line and/or within shell scripts as part of a complex wrapper. Unlike applications such as Firejail which automatically set /var and /etc to read-only within the sandbox, Bubblewrap makes no such operating assumptions. It is up to the user to determine which configuration options to pass in accordance to the application being sandboxed. Bubblewrap does not automatically create user namespaces when running with setuid privileges and can accommodate typical environment variables including $HOME and $USER.

It is highly recommended that you download strace to see what files the program you are trying to sandbox needs access to.

Instead of manually setting up the arguments a configuration manager can be used that configure bubblewrap automatically from a simpler configuration.

Please see /Examples for examples on how bubblewrap can be used. Alternatively, there are various projects that demonstrate how bubblewrap can be used for common applications:

A no-op bubblewrap invocation is as follows:

This will spawn a Bash process which should behave exactly as outside a sandbox in most cases. If a sandboxed program misbehaves, you may want to start from the above no-op invocation, and work your way towards a more secure configuration step-by-step.

Create a simple Bash sandbox:

Leverage Bubblewrap within desktop entries:

To further hide the contents of the file system (such as those in /var, /usr/bin and /usr/lib) and to sandbox even the installation of software, pacman can be made to install Arch packages into isolated filesystem trees.

In order to use pacman for installing software into the filesystem trees, you will need to install fakeroot and fakechroot.

Suppose you want to install the xterm package with pacman into an isolated filesystem tree. You should prepare your tree like this:

You may want to edit ~/sandboxes/${MYPACKAGE}/files/etc/pacman.conf and adjust the pacman configuration used:

Then install the base group along with the needed fakeroot into the isolated filesystem tree:

Since you will be repeatedly calling bubblewrap with the same options, make an alias:

You will need to set up the locales by editing ~/sandboxes/${MYPACKAGE}/files/etc/locale.gen and running:

Then set up pacman’s keyring:

Now you can install the desired xterm package.

If the pacman command fails here, try running the command for populating the keyring again.

Congratulations. You now have an isolated filesystem tree containing xterm. You can use bw-install again to upgrade your filesystem tree.

You can now run your software with bubblewrap. command should be xterm in this case.

Note that some files can be shared between packages. You can hardlink to all files of an existing parent filesystem tree to reuse them in a new tree:

Then proceed with the installation as usual by calling pacman from bw-install fakechroot fakeroot pacman ....

Bind mounting the host X11 socket to an alternative X11 socket may not work:

A workaround is to bind mount the host X11 socket to the same socket within the sandbox:

While bwrap provides some very nice isolation for sandboxed applications, there are ways for an application to escape as long as access to the X11 socket is available. X11 does not include isolation between applications, and this might allow for a malicious application to, for example, listen to inputs, inject keystrokes or record images of other applications.

One solution to this is to switch to a Wayland compositor with no access to the Xserver from the sandbox. Wayland implemented features to not allow applications to interact.

To keep using X11, you can use either xpra or xephyr. These tools allow to spawn secondary X11 instances only running your sandboxed application, that get displayed within a window in your current environment. This way the window cannot interact outside of it's own X11 instance. These methods work with bwrap as well.

This article or section needs expansion.

To test X11 isolation, run xinput test id (the keyboard id can be found with xinput list). When run without additional X11 isolation, this will show that any application with X11 access can capture keyboard input of any other application, which could allow for a malicious application to do keylogging.

This article or section is a candidate for merging with XDG Desktop Portal.

With workarounds, it is possible to sandbox programs with XDG Desktop Portals. The main advantage is with filesystem portals, as it makes it possible to not give a program access to the home directory, but still be able to access files. For security reasons, however, using portals requires tricking xdg-desktop-portal into thinking a sandboxed program is part of a Flatpak. This can be done by adding a .flatpak-info file to the sandbox's root filesystem.

In addition, one also needs to run xdg-dbus-proxy for more fine control over what portals can be accessed. This should be ran in a sandboxed environment, and as such also needs a .flatpak-info file. At the minimum, the proxy needs to have talk access to org.freedesktop.portal.Flatpak. Additional portals can be found in the Flatpak documentation.

A common use case is to allow restricting a program from having 100% access to the home directory, and instead only giving access to files and folders the user selects in a file chooser. To achieve this, xdg-dbus-proxy can be started with the following arguments:

When a wrapped IRC or email client attempts to open a URL, it will usually attempt to launch a browser process, which will run within the same sandbox as the wrapped application. With a well-wrapped application, this will likely not work. The approach used by Firejail is to give wrapped applications all the privileges of the browser as well, however this implies a good amount of permission creep.

A better solution to this problem is to communicate opened URLs to outside the sandbox. This can be done using snapd-xdg-open as follows:

The /usr/bin/chromium bind is only necessary for programs not using XDG conventions, such as Mozilla Thunderbird.

There is a security issue with TIOCSTI, (CVE-2017-5226) which allows sandbox escape. To prevent this, bubblewrap has introduced the new option '--new-session' which calls setsid(). However, this causes some behavioural issues that are hard to work with in some cases. For instance, it makes shell job control not work for the bwrap command.

It is recommended to use this if possible, but if not the developers recommend that the issue is neutralized in some other way, for instance using SECCOMP, which is what flatpak does: https://github.com/flatpak/flatpak/commit/902fb713990a8f968ea4350c7c2a27ff46f1a6c4

Certain applications such as Chromium already implement their own sandbox environment using suid helper files. This mechanism will be blocked when they are executed inside a bubblewrap container.

One solution is to have the application use the namespace created by bubblewrap. This can be achieved through zypakAUR which is also used by flatpak to run electron based apps inside an additional namespace. Example code that demonstrates how to use zypak with Chromium/Electron can be found at [1].

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

For certain programs using ALSA Sound System, add

**Examples:**

Example 1 (unknown):
```unknown
$ bwrap --dev-bind / / bash
```

Example 2 (unknown):
```unknown
$ ls /proc/self/ns
```

Example 3 (unknown):
```unknown
cgroup  ipc  mnt  net  pid  user uts
```

Example 4 (unknown):
```unknown
CONFIG_USER_NS=y
```

---

## Haskell

**URL:** https://wiki.archlinux.org/title/Haskell

**Contents:**
- Installation
- Native installation
  - Configuration
    - Invoking GHC directly
    - Configuring Cabal for dynamic linking
    - Configuring Stack for dynamic linking
- Package management
  - Cabal
    - Installing packages
    - Removing packages

There are several choices for Haskell installation. One is supported by Arch Linux, while others are officially supported by Haskell for any Linux distribution.

Since version 8.0.2-1, the Arch ghc package and all haskell-* packages in extra provide only dynamically linked libraries.

Using dynamic linking typically results in faster builds and smaller disk and RAM usage (by sharing pages between multiple running Haskell programs), and will free you from troubleshooting cross-GHC mixing errors. For this reason using pacman and the official repositories is preferred for managing end-user applications. But it has its own disadvantage: all tools you install from source will break on every update of ghc, ghc-libs or haskell-* packages since libraries compiled with GHC do not provide a stable ABI. When running such broken binary, you will see the usual message:

error while loading shared libraries: libHS...so: cannot open shared object file: No such file or directory

To fix this, just rebuild and reinstall the broken tool in order to relink it to newer libraries.

On the other hand, static linking is generally easier to maintain, does not force you to rebuild all tools from source after every update of their dependencies and is currently better supported by the GHC. For these reasons, static linking is the preferred and recommended option for local development. Otherwise, if you want dynamic linking, to link successfully one must configure GHC, Cabal and Stack for this, as the default is to use static linking.

If you wish to use ghc (from the official repositories) with static linking, it is possible, but is more complex to setup, see #Static linking.

To use Haskell, install the following packages:

In order to link successfully one must pass the -dynamic flag to GHC. You can try it with the following file:

Compile and run it with:

First, run the following command to download the latest list of packages from Hackage and create global configuration file ~/.cabal/config (or the file $CABAL_CONFIG points to):

To configure Cabal for dynamic linking, uncomment and edit the following options in ~/.cabal/config:

You can use stack setup command to initialize Stack and create global configuration file ~/.stack/config.yaml. By default Stack will automatically download its own version of GHC to an isolated location upon first invocation. To force Stack to use system GHC installation instead, run stack setup with --system-ghc and --resolver flags:

Note that you need to specify a resolver which is compatible with your system GHC. Otherwise Stack will happily ignore --system-ghc flag and download its own copy of GHC. You can determine the version of system GHC using ghc --version command:

Then visit Stackage website and pick a suitable Long Term Support (LTS) or nightly snapshot matching your system GHC version. Use the selected snapshot for --resolver flag on the command line, e.g. --resolver lts-16.15 or --resolver nightly-2020-09-01.

Stackage typically lags behind new GHC releases. It may happen that no Stackage snapshot for your system GHC has yet been released. In this case you might want to choose a snapshot for some earlier minor version of GHC or temporarily downgrade your Haskell installation and wait until support for newer GHC releases finally lands on Stackage.

To configure Stack for dynamic linking, add the following snippet to ~/.stack/config.yaml:

Most of Haskell libraries and executables are distributed in units of source packages available from Hackage and Stackage. Repositories used by Cabal and Stack respectively.

GHC, the standard compiler for Haskell, generates machine code that can be run natively on Linux. As is common in other compiled languages, a number of popular Haskell packages are available from official Arch repositories in pre-built form.

Some additional packages can be installed from AUR. This packages may need to build from source, building AUR packages or developing software require a compiler and build tools to be installed. Using the #Native installation method is discouraged for this use case, instead see #Alternate installations.

Therefore there are four main sources for Haskell packages: Hackage (Cabal), Stackage (Stack), official repositories and AUR.

The following table summarizes the advantages and disadvantages of different package management styles.

Cabal is "the original" build system for Haskell. Most of libraries and tools you can find on Hackage can be installed via Cabal.

To run user-wide executables installed by Cabal, ~/.cabal/bin must be added to the $PATH environment variable.

Run the following command to install a Hackage package and all of its dependencies in a single step:

You can also build and install a Haskell package from source. To do this, run cabal install without specifying any package in the directory with the sources.

Each Cabal package should specify a list of its dependencies and their version constraints in the .cabal file according to the Package Versioning Policy (PVP). During the package installation, Cabal tries to find a set of dependencies that satisfies all the constraints. This process is called dependency resolution.

There are reasons why Stack exists; Cabal is known to generate a lot of friction with beginners, although it has been getting better in the past years. Most of the time dependency resolution works well but sometimes it fails. In this case you will need to figure out the cause of the problem and give Cabal some hints about how to resolve offending dependencies. For example, sometimes it is necessary to add --allow-newer to allow Cabal to ignore package's PVP-dictated upper bounds on dependency versions, effectively installing package with newer dependencies than the package author has permitted. It gets hairier for less-well maintained packages; for another example, see this thread about installing Idris (another programming language, written in Haskell), where one had to use both --allow-newer and --constraint='haskeline < 0.8.0.0' command-line flags to get a successful compile.

There is no easy way to do it. Cabal does not have support for this functionality but there are external tools like cabal-store-gc.

To reinstall the entire user-wide Haskell package system, remove ~/.cabal and ~/.ghc and start from scratch. This is often necessary when GHC is upgraded.

For more precision, it is possible to use ghc-pkg unregister package or ghc-pkg hide package/ghc-pkg expose package directly on the user package database — this makes GHC "forget" about an installed package (or pretend it is not there). However neither of these removes any files.

Stack is another tool to manage Haskell packages. It has slightly different goals than Cabal, with a slightly different philosophy. It uses Cabal library under the hood and integrates with Hackage — but maintains its own repositories of packages (snapshots) on Stackage with the promise that snapshots are curated and include packages which work well together.

In its default configuration, Stack installs compiled executables to ~/.local/bin. Add this directory to the $PATH environment variable in your shell configuration file, for instance ~/.bashrc for bash or ~/.zshrc for zsh:

Run the following command to download, build and install a Stackage package:

You can also build and install a Haskell package from source by running the following command from the package directory:

Note that you should specify the same resolver as one used for stack setup command.

Stack does not support the "uninstall" operation.

If you want to reinstall the entire user-wide Haskell package system, remove ~/.stack directory and start from scratch. This is often necessary when GHC is upgraded.

haskell-language-server is a Language Server Protocol (LSP) implementation for Haskell. It provides IDE-like features such as code completion, "goto definition", documentation on hover, linting, formatting or refactoring for any editor integrating with the LSP.

If you are using dynamically linked Haskell packages from pacman, install haskell-language-server. Otherwise, if you prefer static linking, install haskell-language-server-staticAUR. This package contains statically linked binaries for each supported version of GHC. Alternatively, haskell-language-server can be installed via ghcup or by the Haskell extension for Visual Studio Code.

haskell-language-server will attempt to automatically determine the build configuration when you open your project. If automatic detection fails, you might want to configure it manually using a hie.yaml file in the project root directory.

ghcid is a GHCi-based tool for Haskell development that provides simple and robust way to display compiler errors and warnings on every source code change. It can be installed via ghcidAUR package.

hoogle allows you to search the Haskell libraries by either function name, or by approximate type signature. It can be installed via hoogle package.

An online version of hoogle is available at https://hoogle.haskell.org.

hlint suggests possible improvements to Haskell code such as using alternative functions, simplifying code and spotting redundancies. It is available through hlint package.

stan is a Haskell static analyzer, complementary to hlint. It is in the beta phase as of June 2021. Available in haskell-stanAUR.

weeder is an application to perform whole-program dead-code analysis.

Visual Studio Code has a Haskell extension powered by haskell-language-server. If you do not have haskell-language-server installed, the Haskell extension will automatically download and install statically linked Linux binaries for you.

IntelliJ IDEA support for Haskell is provided by the Haskell LSP plugin. It works with any edition of IntelliJ IDEA including intellij-idea-community-edition.

You will need to install Stack in order to create a new project or import an existing one into IntelliJ IDEA. As of June 2021 Cabal-only projects are not supported.

Basic syntax highlighting and indentation for Vim can be obtained via the haskell-vim plugin. For better IDE-like experience use one of LSP client plugins (e.g. coc.nvim, ALE, LanguageClient-neovim) together with haskell-language-server.

Basic Emacs support for Haskell is provided by the official haskell-mode. For more advanced features, also use lsp-haskell with haskell-language-server.

The methods described in this sections are best suited for Haskell development setups. It is possible to use them along packages from the official repositories, if this is the case, make sure you know which version of the Haskell package you are using, if the one installed by pacman or by one of the following methods.

This is the recommended method for installing Haskell in any Linux distribution. GHCup installs GHC, tools and libraries in your home directory and allows to have multiple versions in parallel and handle them with relative ease. It is similar in scope to rustup, pyenv and jenv.

Install ghcup-hs-binAUR package. Alternatively, you may follow official installation instructions or manually download ghcup binary and place it somewhere into your $PATH.

By default, ghcup will install executables into ~/.ghcup/bin. You need to add this directory to the $PATH environment variable in your shell configuration file, for instance ~/.bashrc for bash or ~/.zshrc for zsh. If you want to run executables installed by Cabal, add ~/.cabal/bin to $PATH as well:

GHCup provides a convenient TUI which supports most of its functionality:

Alternatively, you can use the following CLI commands:

List available versions of GHC and Cabal:

Install the recommended version of GHC:

You can also install a specific version of GHC, for example:

The commands above do not automatically make GHC available on the $PATH. You need to select which GHC version to use by default:

Install the recommended version of Cabal:

GHCup can install haskell-language-server too, use the following command:

For more information, refer to official ghcup and Cabal documentation.

In case you decide to use GHCup and Cabal along the native installation you need to specify Cabal which GHC to use specifying the path of the GHC version to use in $HOME/.config/cabal/config, search for the line with-compiler: and uncomment it:

Remember that the path of your GHC in case of using GHCup is going to be under $HOME/.ghcup/bin. Also GHCup, once you set the GHC version you wish, will link that version to $HOME/.ghcup/bin/ghc. If you set that path in the Cabal configuration, you can change which version of GHC Cabal uses using GHCup.

You can install Stack using the stack-binAUR package or using GHCup (see #ghcup). Alternatively, you may follow official installation instructions or manually download Stack binary and place it somewhere into your $PATH.

If you want to run executables installed by Stack, add ~/.local/bin directory to the $PATH, see Environment variables for more information on how to do this.

Stack will use an isolated version of GHC, so it does not require any additional configuration. Run stack setup to automatically install GHC from the latest Stackage LTS snapshot:

You can now use Stack to build and install statically linked Haskell packages without any special configuration or command line flags:

For more information, refer to official Stack documentation.

This article or section needs expansion.

A completely different way of installing Haskell is Nix package manager. Nix has a steeper learning curve but offers greater flexibility in managing both Haskell and non-Haskell packages in a reliable and reproducible fashion.

To use static linking, one must, at minimum, install the static boot libraries through the ghc-static package. This would allow you to build projects that depend exclusively on the boot libraries as well as on any other libraries that are not installed through the haskell-* packages from the official repositories.

Unfortunately, if your project depends on any of dynamically linked haskell-* packages that you have installed, Cabal does not take the absence of static libraries into account during dependency resolution. As a result, it will try to use the existing haskell-* package and then fail with linker errors when it discovers the static libraries are missing:

Unlike ghc-static, there are no "haskell-*-static" packages available for linkage. There are other ways to work around this issue though, as described in each of the sections below.

A direct approach is offered by the official ghc-static package, which exposes an alternative "static" global package database at /usr/lib/ghc-version/static-package.conf.d. The static database is limited to only the statically linkable boot packages, therefore if Cabal is reconfigured to use the static database instead of the default database, it would behave as though the dynamic-only haskell-* packages do not exist.

The precise path of the static database could be determined at build time using a command such as:

Here is how to enable the static database for use:

Install ghc-pristineAUR package, which wraps over an existing GHC installation to create a separate GHC distribution in /usr/share/ghc-pristine, with a package database that contains only boot libraries. This effectively creates a semi-isolated environment without dynamically linked haskell-* packages, but still makes use of the GHC compiler from the official repositories. Then, to build software with static linking, one simply needs to invoke the wrapped compiler /usr/share/ghc-pristine/bin/ghc. For Cabal, this amounts to the following configuration in ~/.cabal/config:

You can also specify the path to the compiler on a per-project basis by running the following command from the project directory:

Install stack-binAUR package. Similarly to cabal-static method, make sure that the only other Haskell packages you have installed from the official repositories are ghc, ghc-libs and ghc-static. Then setup Stack to use system GHC as explained in #Configuring Stack for dynamic linking:

To make these options permanent, paste the following snippet to ~/.stack/config.yaml:

This configuration will allow you to build statically linked packages as you would normally do, but using system GHC installation instead of GHC provided by Stack.

hpack-static-binAUR provides a statically linked (meaning no haskell-* dependencies) alternative to haskell-hpack. It is precompiled, so no make dependencies are needed.

**Examples:**

Example 1 (unknown):
```unknown
error while loading shared libraries: libHS...so: cannot open shared object file: No such file or directory
```

Example 2 (unknown):
```unknown
main = putStrLn "Hello, World"
```

Example 3 (unknown):
```unknown
$ ghc -dynamic Main.hs
$ ./Main
```

Example 4 (unknown):
```unknown
Hello, World
```

---

## Laptop/Lenovo

**URL:** https://wiki.archlinux.org/title/Laptop/Lenovo

**Contents:**
- IBM/Lenovo
  - ThinkPad battery control
  - UltraBay devices
  - T series
  - X series
- Lenovo
  - Battery conservation mode
  - Special buttons
  - BIOS/Firmware update
  - Advanced UEFI Options

Since kernel 4.17, newer Thinkpads can leverage the natacpi API (part of the thinkpad_acpi kernel module) via TLP. Older (pre-Ivy-Bridge / pre-2011) models may require tp_smapi instead. Refer to its documentation for supported devices and installation details.

See also - Which external kernel module do I need for my ThinkPad?

Ultrabay was IBM's, now Lenovo's name for the swappable bay. It is possible to hotswap a ultrabay by just releasing the UltraBay eject lever or pressing hotkeys such as Fn+F9. Consult ThinkWiki's page for detail.

Battery Conservation Mode is a feature that limits battery charging to 55-60% of its capacity to improve battery life, being most useful when the laptop tends to run on external power much of the time. This works on many Lenovo laptops like IdeaPad and Thinkbook series. To check if your laptop is supported, try to set the battery conservation mode in the Vantage app on Windows. If it works on Windows, it can be enabled or disabled on Linux in the following manner:

If you use GNOME you can install the Ideapad extension to get an easy toggle (do not forget to configure sudo for it as well).

If you instead use KDE, you can similarly install the PlasmaVantage applet to get a toggle (you can also enable Password-less operation).

Some special buttons are not supported by X server due to keycode number limit, and may also not be recognized on Wayland. Listed below are the two most common ones, but others can be encountered.

You can remap unsupported keys so that they can be detected and mapped in X by creating the following configuration:

Then follow the steps at Map scancodes to keycodes#Using udev.

Lenovo provides updates for firmware and BIOS updates for some of their devices via fwupd, supported devices can be found by searching on the fwupd website

To update other devices which Lenovo only provides Windows installers, you can manually download the firmware from Lenovo support website and install it by following the instructions in Flashing BIOS from Linux#Lenovo

Some IdeaPad and Legion models have some of the more advanced UEFI options locked. It may be useful to unlock them. There are a few known methods that may unlock the advanced options.

If you notice the pattern, it is just going down the column from F1 to the letter in the last keyboard row, from F1 to F6. (You may need to replace some keys accordingly if you got a QWERTZ layout or similar alternative layouts).

On some pre-2022 models, you can create an EFI variable, 6ACCE65D-DA35-4B39-B64B-5ED927A7DC7E-cE! and set it to 1 to enable the advanced options. The userspace efivar can be used to create this variable:

The currently unmaintained tool SmokelessRuntimeEFIPatcher can be used to patch/inject at runtime. There are several patches provided here: https://github.com/quanbingyi/SREP-Community-Patches

To use the amd_pstate driver, CPPC must be enabled, see CPU frequency scaling#Scaling drivers for details on how to enable CPPC.

See Chrome OS devices/Chromebook#Hardware comparisons.

Bluetooth needs investigation and should be working

Performance mode can be toggled between Quiet/Balanced/Performance through with Fn+Q shortcut. This and other keyboard shortcuts require the ideapad_laptop module.

IR Camera needs linux-enable-ir-emitter

Issues with Wifi 7 Intel BE200 card (commonly reported on other forums) when resuming from suspend. The device disappears and a reboot is needed to fix it. This can be resolved by disabling D3cold

This can be made persistent across reboots with a systemd service.

On some recent Lenovo ThinkPads (e.g. T16 Gen 2, AMD), custom UEFI boot entries created with efibootmgr(8) may disappear after reboot, with the firmware restoring only Windows Boot Manager and Lenovo entries (Diagnostics, PXE, Recovery, etc.).

Disabling the UEFI option Restart > OS Optimized Defaults prevents this behavior and allows custom boot entries such as systemd-boot to persist.

To resolve the touchpad not working after waking from suspend, create the following systemd unit:

And then enable/start touchpad-after-wake-fix.service.

Missing IVRS map in ACPI Table, add amd_iommu=pt ivrs_ioapic[32]=00:14.0 in kernel parameters.

In order to get X to work correctly, add iommu=soft in kernel parameters (Linux 4.20 only). On Linux 5.2, add iommu=pt to prevent render artifacts on X.

In order to get microsd (SDHCI) working, echo 'options sdhci debug_quirks2="0x8000"' > /etc/modprobe.d/sdhci.conf and change module load order MODULES=(sdhci sdhci_pci) in /etc/mkinitcpio.conf (line 7). Do not forget to run mkinitcpio -p linux afterwards.

If Wi-Fi does not work on RTL8822BE adapter models, create a file /etc/modprobe.d/wifi.conf and add the following lines:

Then, install rtw88-dkms-gitAUR and reboot.

To solve all these issues mentioned here easier just install the latest BIOS update from Lenovo support website. Missing IVRS map in ACPI Table, add amd_iommu=pt ivrs_ioapic[32]=00:14.0 in kernel parameters. In order to get X to work correctly, add iommu=soft in kernel parameters (Linux 4.20 only). In order to get microsd (SDHCI) working, echo 'options sdhci debug_quirks2="0x8000"' > /etc/modprobe.d/sdhci.conf and change module load order MODULES=(sdhci sdhci_pci) in /etc/mkinitcpio.conf (line 7). Do not forget to run mkinitcpio -p linux afterwards. Bluetooth does not work until a suspend/resume cycle occurs.

Update the BIOS, if missing IVRS map in ACPI Table.

BIOS update can help if Ethernet is not working.

MicroSD does not work out of the box, see #ThinkPad E585 to fix it.

Resume from hibernate will not work until intel_lpss_pci is added to MODULES() in /etc/mkinitcpio.conf. See Power management/Suspend and hibernate#Suspend/hibernate does not work, or does not work consistently for details.

After recovery from suspend, shortly thereafter, system reboots without user interaction. A workaround is available if you are willing to sacrifice suspend-to-ram for suspend-to-idle. The BIOS has two "Sleep State" options, called "Windows" (suspend-to-idle) and "Linux" (suspend-to-ram), which you can find in at Config -> Power -> Sleep State. If you change the setting to "Windows", this will change the state from suspend-to-ram to suspend-to-idle. You can see this if you run cat /sys/power/mem_sleep before and after the change.

The trackpoint and physical buttons will stop working after resuming from hibernate. Use modprobe -r psmouse followed by modprobe psmouse to get the functionailty back

Fingerprint reader is unsupported. Neither fprintd nor libfprintd-tod will work.

If the Fn keys do not work, to update the BIOS, download the "Bootable CD" of the BIOS Update, and use geteltoritoAUR to extract the .img from the .iso with geteltorito.pl -o bios.img downloaded.iso, then use etcher / mintstickAUR / dd to make a bootable USB. See [7] for details.

Panel Self-Refresh (PSR) can cause the screen to randomly freeze every few minutes. This can be fixed by disabling PSR.

See https://reddit.com/r/archlinux/comments/gu0a8a/ for more details.

On some models an issue has been observed, where they operate at a TDP much lower compared to Windows, even when using the performance CPU governor. The result is severe CPU throttling - see issue [10]. The solution is to install throttled and start/enable the throttled.service systemd service.

The subwoofer needs https://gist.github.com/BXZ/48cd8173807676a1402cf4bc7928c0c0 to get it working.

Touchpad fixed in recent kernels(or is it systemd, i have lost overview)(1-2 months ago or so i think and the date now is: 19.03.2023) so disregard the below if you have updated your system recently

Passing pci=nocrs as kernel parameter fixes the touchpad. Unfortunately this also disabled my Wi-Fi (it was seen by iwctl but never presented a station no matter what i did). I see others online also have this problem(various posts on stackexchange etc). I finally managed to fix it by also passing pci=realloc so the full line is:

for getting both Wi-Fi and touchpad working.

Note: I am using refind as boot manager(holy cow so much more straight-forward and less confusing than grub2) and i seem to recall being unable to boot with pci=realloc using grub2. This could just be me dreaming though so it probably bears testing first.

Everything else works, except the brightness keys -- which sometimes work, and sometimes do not. I have not figured out in which instance they work or not yet. I managed a fix which was to bind ctrl+f11 and ctrl+f12 in KDE to be able to set the brightness(up/down) all the time.

When you install an SSD in the place of the HDD and you want to have your HDD still inside the laptop, it is possible to install it in the place of the optical drive in a special "HDD caddy". The optical drive is of 9 mm height, but a 9,5 mm caddy (ultra slim) fits in the slot. A caddy with a SATA interface is needed. It is difficult to separate the front bezel from the original optical drive (and opening its case does not help, but brings a danger of making a mess in the opening mechanism; the only option is just to pull the bezel using a bit of force, but you risk breaking the latches).

While the HDD installed instead of the optical drive operates flawlessly in Windows, it was not going to work out of the box in Linux, at least in one case. The kernel tries to establish a connection with the disk, but fails to do it (SATA link down entry in /var/log/messages). The solution is to force a 1.5 Gbps transfer speed (instead of 6 Gbps) by adding a libata.force= kernel parameter. See [11] for details.

Sound: You may have to append options snd_hda_intel model=lenovo to /etc/modprobe.d/modprobe.conf for sound to work.

Tested with broadcom-wl-dkms 802.11 wireless driver

There is an issue with tpacpi-bat not reporting the right value for the stop threshold. This seems to be related to a buggy BIOS and can not be fixed application wise.

See https://github.com/teleshoes/tpacpi-bat/issues/44

The driver for the internal microphone for the IdeaPad laptops using the "Pink Sardine" platform is not loaded by default. First of all, identify the PCI audio device:

To ensure the kernel module snd_pci_ps is properly loaded, create:

Then reboot to confirm the microphone is now working.

It has been observed with consistency that Windows updates are what triggers the laptop's BIOS to enter an inconsistent state that makes it impossible to enter suspend.

An obvious tell is if the power button starts flashing

**Examples:**

Example 1 (unknown):
```unknown
thinkpad_acpi
```

Example 2 (unknown):
```unknown
acpi_sleep=nonvs
```

Example 3 (unknown):
```unknown
acpi_osi='!Windows 2012'
```

Example 4 (unknown):
```unknown
intremap=off
```

---

## USB flash installation medium

**URL:** https://wiki.archlinux.org/title/USB_flash_installation_medium

**Contents:**
- Using the ISO as is (BIOS and UEFI)
  - In GNU/Linux
    - Using basic command line utilities
    - Using KDE ISO Image Writer
    - Using GNOME Disk Utility
    - Using MultiWriter
    - Using Kindd
    - Using Popsicle
    - Using SUSE Studio ImageWriter
    - Using xorriso-dd-target

This page discusses various multi-platform methods on how to create an Arch Linux Installer USB drive (also referred to as "flash drive", "USB stick", "USB key", etc) for booting in BIOS and UEFI systems. The result will be a live USB system that can be used for installing Arch Linux, system maintenance or for recovery purposes, and that, because of using Overlayfs for /, will discard all changes once the computer shuts down.

If you would like to run a full install of Arch Linux from a USB drive (i.e. with persistent settings), see Install Arch Linux on a removable medium. If you would like to use your bootable Arch Linux USB stick as a rescue USB, see chroot.

Before following any of these steps, download the ISO from https://archlinux.org/download/ and verify its integrity.

This method is recommended due to its simplicity and universal availability, since these tools are part of coreutils (pulled in by the base meta package).

Find out the name of your USB drive with ls -l /dev/disk/by-id/usb-* and check with lsblk to make sure that it is not mounted.

Run one of the following commands, replacing /dev/disk/by-id/usb-My_flash_drive with your drive, e.g. /dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0. (Do not append a partition number, so do not use something like /dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0-part1 or /dev/sdb1):

See [1] and [2] for a comparison and perspective on the use of those tools and why dd may be the least adapted one.

KDE ISO Image Writer can be downloaded via isoimagewriter. It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

Linux distributions running GNOME can easily make a live USB through nautilus and gnome-disk-utility. Simply right-click on the .iso file, and select Open With Disk Image Writer. When GNOME Disk Utility opens, specify the flash drive from the Destination drop-down menu and click Start Restoring.

gnome-multi-writer is a simple GTK3 based graphical tool to write an ISO file to one or multiple USB devices at once.

Kindd is a Qt based graphical frontend for dd. It is available as kinddAUR.

Popsicle is a tool made for flashing ISO files to multiple USB devices in parallel by the PopOS development team. It is written in Rust and uses GTK. It is available as popsicleAUR.

SUSE Studio ImageWriter is a Qt based tool made by the openSUSE development team. It is available as imagewriterAUR.

xorriso-dd-target (from libisoburn) is a shell script which attempts to reduce the risk of overwriting the wrong storage device. Its safest mode is named -plug_test. For example, to use it as a regular user who can elevate to root using sudo:

See xorriso-dd-target(1) for details.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups. It is available as usbimagerAUR.

KDE ISO Image Writer can be downloaded as .exe file at isoimagewriter. It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

win32diskimager is another graphical tool for writing images to USB sticks or SD/CF cards from Windows. Select your ISO image and the target USB drive letter (you may have to format it first to assign it a drive letter), and click Write.

This method does not require any workaround and is as straightforward as dd under Linux. Just download the Arch Linux ISO, and with local administrator rights use the USBwriter utility to write to your USB flash memory.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

Rufus is a multi-purpose USB ISO writer. It provides a graphical user interface and does not care if the drive is properly formatted or not.

Simply select the Arch Linux ISO, the USB drive you want to create the bootable Arch Linux onto and click START.

Make sure your Cygwin installation contains the dd package.

Place your image file in your home directory:

Run cygwin as administrator (required for cygwin to access hardware). To write to your USB drive use the following command:

where archlinux-version-x86_64.iso is the path to the iso image file within the cygwin directory and \\.\x: is your USB flash drive where x is the windows designated letter, e.g. \\.\d:.

On Cygwin 6.0, find out the correct partition with:

and write the ISO image with the information from the output. Example:

A GPL licensed dd version for Windows is available at http://www.chrysocome.net/dd. The advantage of this over Cygwin is a smaller download. Use it as shown in instructions for Cygwin above.

To begin, download the latest version of dd for Windows. Once downloaded, extract the archive's contents into the Downloads directory or elsewhere.

Now, launch your Command Prompt as an administrator. Next, change directory (cd) into the Downloads directory.

If your Arch Linux ISO is elsewhere you may need to state the full path, for convenience you may wish to put the Arch Linux ISO into the same folder as the dd executable. The basic format of the command will look like this.

flashnul is an utility to verify the functionality and maintenance of Flash-Memory (USB-Flash, IDE-Flash, SecureDigital, MMC, MemoryStick, SmartMedia, XD, CompactFlash etc).

From a command prompt, invoke flashnul with -p, and determine which device index is your USB drive, e.g.:

When you have determined which device is the correct one, you can write the image to your drive, by invoking flashnul with the device index, -L, and the path to your image, e.g:

As long as you are really sure you want to write the data, type yes, then wait a bit for it to write. If you get an access denied error, close any Explorer windows you have open.

First, you need to identify the USB device. Open /Applications/Utilities/Terminal and list all storage devices with the command:

Your USB device will appear as something like /dev/disk2 (external, physical). Verify that this is the device you want to erase by checking its name and size and then use its identifier for the commands below instead of /dev/diskX.

A USB device is normally auto-mounted in macOS, and you have to unmount (not eject) it before block-writing to it with dd. In Terminal, do:

Now copy the ISO image file to the device:

This command will run silently. To view progress, send SIGINFO by pressing Ctrl+t. Note diskX here should not include the s1 suffix, or else the USB device will only be bootable in UEFI mode and not legacy. After completion, macOS may complain that The disk you inserted was not readable by this computer. Select Ignore. The USB device will be bootable.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

EtchDroid is a OS image flasher for Android. It works without root permissions since Android 5. Check the upstream GitHub if you have issue.

To create an Arch Linux installer, download the ISO image file on your Android device. Plug the USB drive to your device, using a USB-OTG adapter if needed. Open EtchDroid, select Flash raw image, select your Arch ISO, then select your USB drive. Grant the USB API permission and confirm.

Keep your phone on a table while it is writing the image: a lot of USB-OTG adapters are a bit wobbly and you might unplug it by mistake.

This method is more complicated than writing the image directly with dd, but it does keep the flash drive usable for data storage (that is, the ISO is installed in a specific partition within the already partitioned device without altering other partitions).

Syslinux files for BIOS systems are already copied to /mnt/boot/syslinux/. Unmount the FAT file system, install the syslinux and mtools packages and run the following commands to make the partition bootable:

For some old BIOS systems, only booting from USB-ZIP drives is supported. This method allows you to still boot from a USB hard drive.

From here continue with the manual formatting method. The partition will be /dev/disk/by-id/usb-My_flash_drive-part4 due to the way ZIP drives work.

For UEFI-only booting, it is enough to extract the ISO contents onto a FAT-formatted USB flash drive.

It does not require creating a EFI system partition on the drive as all UEFI will happily boot any FAT volume from USB flash drives. The most compatible setup would be using the MBR partition table with a single active (bootable) primary partition of type 0c "W95 FAT32 (LBA)".[3]

This method extracts files from the ISO image to a USB flash drive.

This method copies files from the ISO image to a USB flash drive.

Neither DiskImageMounter nor Disk Utility can mount isohybrid ISOs, but since macOS ships with libarchive, the ISO can simply be extracted onto the flash drive using bsdtar.

This article or section is a candidate for merging with Multiboot USB drive.

This allows booting multiple ISOs from a single USB device, including the archiso. Updating an existing USB drive to a more recent ISO is simpler than for most other methods. See Multiboot USB drive.

Ventoy is an open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files. With Ventoy, you do not need to format the disk over and over, you just need to copy the ISO/WIM/IMG/VHD(x)EFI files to the USB drive and boot them directly. You can copy many files at a time and Ventoy will give you a boot menu to select them. It is available as ventoy-binAUR.

This method uses Syslinux and a Ramdisk (MEMDISK) to load the entire Arch Linux ISO image into RAM. Since this will be running entirely from system memory, you will need to make sure the system you will be installing this on has an adequate amount. A minimum amount of RAM between 500 MB and 1 GB should suffice for a MEMDISK based, Arch Linux install.

For more information on Arch Linux system requirements as well as those for MEMDISK see the Installation guide and here. For reference, here is the preceding forum thread.

Begin by formatting the USB flash drive as FAT32. Then create the following folders on the newly formatted drive.

Next copy the ISO that you would like to boot to the Boot/ISOs folder. After that, extract from the following files from the latest release of syslinux from here and copy them into the following folders.

After copying the needed files, navigate to the USB flash drive, Boot/Settings and create a syslinux.cfg file.

For more information see the Syslinux article.

Finally, create a *.bat file where syslinux.exe is located and run it ("Run as administrator" if you are on Vista or Windows 7):

etcher contains analytics and first-party advertising. See [4], [5] and [6].

There are two ways to add an additional (third) partition to a drive prepared using #Using the ISO as is (BIOS and UEFI).

To edit the MBR partition table on the drive, run:

Use the n command to create a new partition (leave the default values for the first and last sectors if it should span all available free size). If you want to access it in other operating systems, change the MBR partition type ID using the t command (e.g. to 0c "W95 FAT32 (LBA)" or 07 "HPFS/NTFS/exFAT"). Write the changes to disk and exit via the w command.

After partitioning, create a file system on the new partition (/dev/disk/by-id/usb-My_flash_drive-part3).

If you get the device did not show up after 30 seconds error due to /dev/disk/by-label/ARCH_YYYYMM not mounting, try renaming your USB medium to ARCH_YYYYMM so Arch can find it. (e.g. For archlinux-2021.02.01-x86_64.iso, use ARCH_202102).

If you get losetup: /run/archiso/bootmnt/arch/x86_64/airootfs.sfs: failed to set up loop devices: No such file or directory, try using a USB 2.0 port. For example, some USB 3.0 ports through USB hubs do not work.

If you get other errors, try using another USB device. There are multiple scenarios in which it solved all issues.

**Examples:**

Example 1 (unknown):
```unknown
ls -l /dev/disk/by-id/usb-*
```

Example 2 (unknown):
```unknown
/dev/disk/by-id/usb-My_flash_drive
```

Example 3 (unknown):
```unknown
/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0
```

Example 4 (unknown):
```unknown
/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0-part1
```

---

## Help:Reading

**URL:** https://wiki.archlinux.org/title/Install

**Contents:**
- Organization
- Formatting
- Root, regular user or another user
- Append, add, create, edit
  - Make executable
- Source
- Installation of packages
  - Official packages
  - Arch User Repository
- Control of systemd units

Because the vast majority of the ArchWiki contains indications that may need clarification for users new to Arch Linux (or GNU/Linux in general), this rundown of basic procedures was written both to avoid confusion in the assimilation of the articles and to deter repetition in the content itself.

Most articles on the ArchWiki do not attempt to provide a holistic introduction to a single topic; they are instead written in adherence to the "Don't Repeat Yourself" principle, under the assumption that the user will seek out and read any supporting material that they do not yet understand. Where possible, such supporting material is indicated in the article via special formatting, see #Formatting.

Because of this organization, it may be necessary to examine several related sources in order to fully understand an ArchWiki article. In particular, users who are new to Arch (or GNU/Linux in general) should expect to end up reading a great number of articles even when solving simple problems. It is especially important to study the supporting material before seeking additional help from other users.

Some lines are written like so:

Others have a different prefix:

The numeral or hash sign (#) indicates that the command needs to be run as root, whereas the dollar sign ($) shows that the command should be run as a regular user.

When the commands need to run as a specific user, they will be prefixed by the username in square brackets, for example:

This means you should use a privilege elevation tool, e.g. with sudo:

A notable exception to watch out for:

In this example, the context surrounding the numeral sign communicates that this is not to be run as a command; it should be edited into a file instead. So in this case, the numeral sign denotes a comment. A comment can be explanatory text that will not be interpreted by the associated program. Bash scripts denotation for comments happens to coincide with the root PS1.

After further examination, "give away" signs include the uppercase character following the # sign. Usually, Unix commands are not written this way and most of the time they are short abbreviations instead of full-blown English words (e.g., Copy becomes cp).

Regardless, most articles make this easy to discern by notifying the reader:

Append to ~/path/to/file:

When prompted to append to, add to, create, or edit one or more files, it is implied that you should use one of the following methods.

To create or modify multiline files, it is suggested to use a text editor. For example, using the nano command to edit the file /etc/bash.bashrc is:

To create or overwrite a file from a string, it may be simpler to use output redirection. The following example creates or overwrites the contents of the file /etc/hostname with the text myhostname.

Output redirection can also be used to append a string to a file. The following example appends the text [custom-repo] to the file /etc/pacman.conf.

When prompted to create directories, use the mkdir command:

After creating a file, if it is meant to be run as a script (whether manually or called by another program), it needs to be set as executable, for example with:

See chmod. Some applications such as file managers may provide graphical interfaces to do the same.

Some applications, notably command-line shells, use scripts for their configuration: after modifying them, they must be sourced in order for the changes to be applied. In the case of bash, for example, this is done by running (you can also replace source with .):

When the wiki suggests modifying such a configuration script, it will not explicitly remind you to source the file, and only in some cases will it point to this section with a reminder link.

When an article invites you to install some packages in the conventional way, it will not indicate the detailed instructions to do so; instead, it will simply mention the names of the packages to be installed.

The subsections below give an overview of the generic installation procedures depending on the package type.

For packages from the official repositories, you will read something like:

This means that you have to run:

The pacman article contains detailed explanations to deal with package management in Arch Linux proficiently.

For packages from the Arch User Repository (AUR), you will read something like:

This means that in general you have to follow the foobarAUR link, download the PKGBUILD archive, extract it, verify the content and finally run, in the same folder:

The Arch User Repository article contains all the detailed explanations and best practices to deal with AUR packages.

When an article invites to start, enable, etc., some systemd unit (e.g. a service), it will not indicate the detailed instructions to do so, but instead you will read something like:

This means that you have to run:

A notable command that does not follow this exact pattern is systemctl daemon-reload which will be called without arguments.

The systemd#Using units section contains structured list of available actions (like start, enable, enable and start, etc.) with their corresponding systemctl commands.

It is important to remember that there are two different kinds of configurations on a GNU/Linux system. System-wide configuration affects all users. Since system-wide settings are generally located in the /etc directory, root privileges are required in order to alter them. For example, to apply a Bash setting that affects all users, /etc/bash.bashrc should be modified.

User-specific configuration affects only a single user. Dotfiles are used for user-specific configuration. For example, the file ~/.bashrc is the user-specific configuration file. The idea is that each user can define their own settings, such as aliases, functions and other interactive features like the prompt, without affecting other users' preferences.

Bash and other Bourne-compatible shells, such as Zsh, also source files depending on whether the shell is a login shell or an interactive shell. See Bash#Configuration files and Zsh#Startup/Shutdown files for details.

Some code blocks may contain so-called pseudo-variables, which, as the name says, are not actual variables used in the code. Instead they are generic placeholders and have to be manually replaced with system-specific configuration items before the code may be run or parsed. Common shells such as bash and zsh provide tab-completion to auto-complete parameters for common commands such as systemctl.

In the articles that comply with Help:Style/Formatting and punctuation, pseudo-variables are formatted in italics. For example:

In this case interface_name is used as a pseudo-variable placeholder in a systemd template unit. All systemd template units, identifiable by the @ sign, require a system-specific configuration item as argument. See systemd#Using units.

In this case the pseudo-variables are used to describe the parameters that must be substituted for them. Details on how to gather them are elaborated on in the section Securely wipe disk#Calculate blocks to wipe manually, which features the command.

This article or section needs expansion.

In case of file examples, pasting pseudo-variables in real configuration files might break the programs that use them.

In most cases, ellipses (...) are not part of the actual file content or code output, and instead represent omitted or optional text that is not relevant for the discussed subject.

For example HOOKS=(... encrypt ... filesystems ...) or:

Be aware though that, in a few instances, ellipses may be a meaningful part of the code syntax: attentive users should be able to recognize these cases by the context.

**Examples:**

Example 1 (unknown):
```unknown
# mkinitcpio -p linux
```

Example 2 (unknown):
```unknown
$ makepkg -s
```

Example 3 (unknown):
```unknown
sudo command
```

Example 4 (unknown):
```unknown
[postgres]$ initdb -D /var/lib/postgres/data
```

---

## Stubby

**URL:** https://wiki.archlinux.org/title/Stubby

**Contents:**
- Installation
- Configuration
  - Select resolver
  - Enable DNSSEC validation
  - Modify resolv.conf
  - Start systemd service
- Tips and tricks
  - Local DNS cache configuration
    - Change port
      - dnsmasq

Stubby is an application that acts as a local DNS Privacy stub resolver (using DNS-over-TLS). Stubby encrypts DNS queries sent from a client machine (desktop or laptop) to a DNS Privacy resolver, increasing end user privacy.

Install the stubby package.

To configure stubby, perform the following steps:

Upon installation, Stubby has some default resolvers. They can be found and edited in /etc/stubby/stubby.yml. You can use the defaults, uncomment one of prewritten resolvers or find another resolver from this list.

Example of a valid resolver configuration:

When you get warn log complaining wrong tls_pubkey_pinset, the tls_pubkey_pinset value may be wrong and the value of the tls_pubkey_pinset can be generated with:

Enable DNSSEC validation by uncommenting the following line in /etc/stubby/stubby.yml:

After selecting a resolver, modify the resolv.conf file and replace the current set of resolver addresses with address for localhost:

Other programs may overwrite this setting; see resolv.conf#Overwriting of /etc/resolv.conf for details.

Finally, start/enable the stubby.service.

Stubby does not have a built-in DNS cache, therefore every single query is transmitted and resolved, which can slow down connections. Setting up a DNS cache requires installing and configuring a separate DNS cacher.

In order to forward to a local DNS cache, Stubby should listen on a port different from the default 53, since the DNS cache itself needs to listen on 53 and query Stubby on a different port. Port number 54 is used as an example in this section.

Edit the value of listen_addresses as follows:

Configure dnsmasq as a local DNS cache. The basic configuration to work with Stubby is the following:

Restart dnsmasq.service to apply the changes.

For more DNS cachers, see DNSCrypt#Local DNS cache configuration. The configurations should be similar if not identical.

**Examples:**

Example 1 (unknown):
```unknown
/etc/stubby/stubby.yml
```

Example 2 (unknown):
```unknown
/etc/stubby/stubby.yml
```

Example 3 (unknown):
```unknown
upstream_recursive_servers:

## Cloudflare servers
 - address_data: 1.1.1.1
   tls_auth_name: "cloudflare-dns.com"
 - address_data: 1.0.0.1
   tls_auth_name: "cloudflare-dns.com"
 - address_data: 2606:4700:4700::1111
   tls_auth_name: "cloudflare-dns.com"
 - address_data: 2606:4700:4700::1001
   tls_auth_name: "cloudflare-dns.com"
```

Example 4 (unknown):
```unknown
tls_pubkey_pinset
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Extra

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## Booster

**URL:** https://wiki.archlinux.org/title/Booster

**Contents:**
- Install
- Usage
- Configuration
  - Early module loading
  - Encryption
    - systemd style binding
  - Removing modules
  - Stripping modules
  - Compression
- Boot loader configuration

Booster is a fast initramfs generator similar to mkinitcpio and dracut. Booster is inspired by the "distri" project and aims to create a small and fast init image.

Booster provides the /usr/bin/booster user-space tool, responsible for initramfs image generation. The generated images are located at /boot/ by default.

Install booster. The package installation hook will generate initramfs images, one per installed kernel (e.g. for linux, linux-lts). The images are located under /boot directory:

When configuration is done to Booster the initramfs images need to be regenerated for the changes to take affect, to do so, see the examples below.

Booster offers a convenience script that iterates over all installed kernels and generates an image for each of them:

Alternatively, you can generate images manually by calling booster directly with the build argument:

This will build an initramfs image in your current directory, do note that it may require escalated privileges depending on where it's being ran on the filesystem.

Booster's generator configuration file is located at /etc/booster.yaml. If there is no configuration file then the default configuration (host-specific images, no network) is used.

The configuration file helps to override the default behaviour. See booster(1) § CONFIG FILE for detailed information.

You can load some modules at initramfs stage forcibly.

For example, if you need Kernel mode setting#Early KMS start to avoid graphical session run before NVIDIA GPU is initialized, use the following configuration setting:

And then regenerate booster images.

Booster supports LUKS based full-disk encryption out-of-the-box like Clevis. The generator does not need any extra configuration. Yet, for the initramfs you need to append information about the LUKS partition where the root resides. This is done with either rd.luks.uuid=LUKSUUID or rd.luks.name=LUKSUUID=LUKSNAME kernel parameter that need to be specified in the boot loader configuration file. LUKSUUID specifies the UUID of the encrypted LUKS partition that needs to be unlocked by Booster. The booster(1) § UUID parameters manual recommends that the UUID does not contain any quotes. LUKSNAME specifies name of the unlocked partition (as in /dev/mapper/LUKSNAME). See booster(1) § BOOT TIME KERNEL PARAMETERS for related options.

No image rebuild is required. Once the boot loader configuration is done, reboot the computer. After that you will see a Enter passphrase for YOURROOT: prompt at boot time asking for a password for the encrypted root partition.

Booster also supports partitions bound with systemd such as systemd-fido2 and systemd-tpm2.

If you use `systemd-fido2` then please install libfido2 package and add fido2-assert to the image using following configuration:

Regenerate the booster images. Booster will detect this configuration during boot and use the present YubiKey to unlock the drive.

You can remove modules from initramfs via the - sign. An example to choose every modules manually and doing as same as Mkinitcpio/Minimal initramfs to improve boot performance is

You can reduce size of by initramfs by stripping modules.

Booster supports compression of initramfs, by default using the zstd algorithm. Currently supported algorithms are zstd, xz, gzip, lz4 or none.

Once the image is generated it is time to configure the boot loader.

Unlike mkinitcpio and dracut, Booster does not support including microcode updates into generated images; see Microcode#Microcode in a separate initramfs file for details on how to configure your boot loader to additionally load the appropriate microcode image.

If the configuration relies on automatic detection already, no additional configuration change is necessary. rEFInd supports initramfs files named booster*.

If you specify the initramfs path manually, either in refind.conf or in manual boot stanzas, make sure to use the correct files names. I.e. booster-linux.img instead of initramfs-linux.img.

To enable the new initramfs image with systemd-boot simply create a new boot loader entry like this one:

Where the root filesystem is referenced by UUID=08f83949-bcbb-47bb-bc17-089aaa59e17e. To find your root device UUID run blkid /dev/ROOTDEVICE.

If Booster has issues and does not work as expected, enable debug output that provides extra information about what is going on:

If you believe it is an issue with Booster itself, then please file a ticket on GitHub.

If you enabled strip and universal and see an error like /usr/lib/modules/glue_helper.ko: pipe2: too many open files, then you need to increase per-process limit for open files. See Limits.conf#nofile.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/booster
```

Example 2 (unknown):
```unknown
$ ls -lh /boot/booster*
```

Example 3 (unknown):
```unknown
-rwxr-xr-x 1 root root 4.0M Dec 16 16:20 /boot/booster-linux.img
```

Example 4 (unknown):
```unknown
# /usr/lib/booster/regenerate_images
```

---

## Install Arch Linux on WSL

**URL:** https://wiki.archlinux.org/title/WSL

**Contents:**
- Installation
  - Install WSL
  - Update WSL
  - Install Arch Linux in WSL
    - Automated installation
    - Manual installation
- Tips and tricks
  - Set default user
  - Open URLs in the WSL hosts browser
  - Run graphical applications with WSLg

Arch Linux provides an official WSL (Windows Subsystem for Linux) image as part of the archlinux-wsl project.

Images are built and released monthly and aim to provide the simplest but complete system to offer an outright Arch Linux experience with WSL.

Enable virtualization in the UEFI Setup, then install the Windows Subsystem for Linux from the Microsoft Store.

To update to the latest stable version of WSL and WSLg, run the following command in an elevated Windows command-line shell:

To update to the latest pre-release version, run instead:

From a Windows system with WSL 2 installed, use one of the following installation methods.

Run the following command in a Windows shell:

You can then run Arch Linux in WSL via the archlinux application from the Start menu, or by running wsl -d archlinux in a Windows shell.

Download the latest Arch Linux .wsl image and double-click on it to start the installation or run the following command in a Windows shell:

You can then run Arch Linux in WSL via the archlinux application from the Start menu, or by running wsl -d archlinux in a Windows shell.

To set a different default user than root, first ensure the user has been created, then append the following to the /etc/wsl.conf file:

Make sure to give your root user a password before you close your session. If you find yourself 'locked out', invoke

from a CMD window in the windows host.

The change will apply at the next session. To terminate your current session, run the following command in a Windows shell:

If you are using WSL 2.4.10 or later, you can set the default user for your distribution with:

This change will take effect the next time you launch the distribution.

In order to open links in your Windows host browser install the xdg-utils package. This is important for various commands like pkgctl repo web and widely used in the authentication flows of the various cloud provider CLI tools (i.e. az login).

WSLg (Windows Subsystem for Linux GUI) is a project that aims to enable running Linux applications with audio (PulseAudio) and graphical (X11 and Wayland) support within WSL.

WSLg is enabled by default. You can disable it by setting wsl2.guiApplications to false in the WSL configuration file.

To enable GPU video accelerated rendering in WSL, install the following packages:

You will need to install the vulkan-icd-loader (and lib32-vulkan-icd-loader if you also want to run 32-bit applications) as well.

If OpenGL falls back to the llvmpipe software renderer for Intel GPUs, you need to create a symlink for libedit:

See https://github.com/microsoft/wslg/issues/996 and Gentoo:Gentoo in WSL#OpenGL falling back to llvmpipe software renderer on Intel GPUs for more information.

WSL features interoperability between the Windows and WSL. This allows you to run Windows binaries from within WSL.

It is enabled by default. You can disable it by setting interop.enabled to false in the /etc/wsl.conf file. [1]

Various tools have been created to allow you to utilise Windows services and features from within WSL.

wsl2-ssh-agent is a tool that allows you to use the Windows SSH agent from within WSL.

This is especially useful if you utilise *-sk SSH keys requiring the use of physical security keys or even Windows Hello.

Install wsl2-ssh-agentAUR and add the following to your ~/.bashrc:

Restart your shell and the SSH_AUTH_SOCK environment variable should be configured correctly.

WSL-Hello-Sudo is a PAM plugin that allows you to authenticate your user via Windows Hello.

Install wsl-hello-sudo-binAUR and run /opt/wsl-hello-sudo/install.sh. The installer will copy a Windows executable to a directory of your choosing and store a certificate used to authenticate beside it.

Add auth sufficient pam_wsl_hello.so to any /etc/pam.d configuration files you wish to authenticate with Windows Hello for. For example, with sudo:

WSL 2 is a Hyper-V virtual machine. This allows for passthrough for physical devices from the host (Windows) to the guest (WSL 2).

WSL 2 supports attaching and mounting disks available to Windows.

To do so, first idenitfy the DeviceID for the given disk with the following PowerShell command:

Once you have found the disk you would like to pass, run the following on Windows (with Administrator privileges):

Once attached, you should be able to see the device with lsblk.

To unmount a disk, run:

For more information, see https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk.

usbipd-win is a project which allows for sharing locally connected USB devices to other machines, including WSL 2.

You first need to install the software on Windows. You can either run the installer (.msi) from the latest release or use use the Windows Package Manager:

Once installed, identify the USB devices available using and take note of the bus ID by running the following on Windows:

Prepare the USB device you have selected by running (this requires Administrator privileges):

Then, attach the USB device to WSL 2 using:

Once attached, you should be able to see the device with lsusb.

To detatch a USB device, run:

For more information, see https://learn.microsoft.com/en-us/windows/wsl/connect-usb.

By default, WSL will try to set your locale to match windows. If you want to override this, run:

Then set your locale the same way you would in any other installation.

One might face the following error when running a Docker container from WSL:

It is also possible that commands like docker run simply hang forever without producing any output.

This is because Docker expects the root (/) directory to be mounted with rshared propagation.

To make the change persistent, you can create a systemd service that runs this command early in the boot:

Then start/enable mount-root-rshared.service.

If you start your WSL Session using docker.service or after start/enable docker.socket and executing docker info or any other docker command, it might take a very long time for docker to initialize.

That's because docker.socket wants to start systemd-networkd-wait-online.service and that fails.

So disable systemd-networkd-wait-online.service fixes that.

**Examples:**

Example 1 (unknown):
```unknown
> wsl --update
```

Example 2 (unknown):
```unknown
> wsl --update --pre-release
```

Example 3 (unknown):
```unknown
> wsl --install archlinux
```

Example 4 (unknown):
```unknown
wsl -d archlinux
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Extra_repository

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## rsyslog

**URL:** https://wiki.archlinux.org/title/Rsyslog

**Contents:**
- Installation
  - Starting service
  - Configure hostname
- Configuration
  - imjournal
  - journald's syslog-forward feature
- Facility levels
- Severity levels
- Examples
  - journald with rsyslog for kernel messages

This article or section is out of date.

rsyslog is a syslog implementation that offers many benefits over syslog-ng. It can be configured to receive log entries from systemd's journal in order to process or filter them before quickly writing them to disk or sending them over network.

Install the rsyslogAUR package.

You can start/enable rsyslog.service after installation.

Rsyslog uses the glibc routine gethostname() or gethostbyname() to determine the hostname of the local machine. The gethostname() or gethostbyname() routine check the contents of /etc/hosts for the fully qualified domain name (FQDN) if you are not using BIND or NIS.

You can check what the local machine's currently configured FQDN is by running hostname --fqdn. The output of hostname --short will be used by rsyslog when writing log messages. If you want to have full hostnames in logs, you need to add $PreserveFQDN on to the beginning of the file (before using any directive that write to files). This is because, rsyslog reads its configuration file and applies it on-the-go and then reads the later lines.

The /etc/hosts file contains a number of lines that map FQDNs to IP addresses and that map aliases to FQDNs. See the example /etc/hosts file below:

localhost.localdomain is the first item following the IP address, so gethostbyname() function will return localhost.localdomain as the local machine's FQDN. Then /var/log/messages file will use localhost as hostname.

To use somehost as the hostname. Move somehost.localdomain to the first item:

rsyslog is configured in /etc/rsyslog.conf. See the official documentation for more information on the available configuration options.

By default, all syslog messages are handled by systemd's journal. In order to gather system logs in rsyslog, you either have to turn on #journald's syslog-forward feature or use the #imjournal module of rsyslog to gather the logs by importing it from the systemd journald.

If you want rsyslog to pull messages from systemd, load the imjournal module:

See the documentation on the imjournal input module for more information.

The rsyslogAUR does not create its working directory /var/spool/rsyslog defined by the $WorkDirectory variable in the configuration file. You might need to create it manually or change its destination.

Log output can be fine tuned in /etc/rsyslog.conf. The daemon uses Facility levels (see below) to determine what gets put where. For example:

States that all messages falling under the authpriv facility are logged to /var/log/secure.

Another example, which would be similar to the behaviour of syslog-ng for the old auth.log:

See Systemd/Journal#Journald in conjunction with syslog for more information.

As defined in RFC 5424, there are eight severity levels:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Since the syslog component of systemd, journald, does not flush its logs to disk during normal operation, these logs will be gone when the machine is shut down abnormally (power loss, kernel lock-ups, ...). In the case of kernel lock-ups, it can be important to have some kernel logs for debugging. Until journald gains a configuration option for flushing kernel logs, rsyslog can be used in conjunction with journald.

Summary of requirements:

Installation and configuration steps:

**Examples:**

Example 1 (unknown):
```unknown
rsyslog.service
```

Example 2 (unknown):
```unknown
gethostname()
```

Example 3 (unknown):
```unknown
gethostbyname()
```

Example 4 (unknown):
```unknown
gethostname()
```

---

## RemoteBox

**URL:** https://wiki.archlinux.org/title/RemoteBox

**Contents:**
- Installation
  - Client-side
  - Server-side
- Connecting RemoteBox to vboxwebsrv
- Troubleshooting
- See also

RemoteBox is an open-source remote client for managing VirtualBox, written in Perl and GTK. It enabled administering a VirtualBox installation on a server, including its guests and interact with them as if they were running locally. While VirtualBox is installed server-side, RemoteBox runs on a client machine. It provides a complete GTK graphical interface with a look and feel very similar to that of VirtualBox's native GUI. If you are familiar with other virtualization software, such as VMWare ESX, then think of RemoteBox as the "poor man's VI client".

RemoteBox is the client application, which can be obtained by installing the remoteboxAUR package. For remote desktop operations an RDP client is also needed. RemoteBox includes presets for freerdp, rdesktop and krdc. As of this writing, freerdp-gitAUR 2.0.0.beta1 has been tested and found working. Alternatively VNC can be used with included presets for TigerVNC, vinagre, krdc and realvnc-vnc-viewerAUR.

The VM host needs a working VirtualBox installation. For remote desktop operations a non-free Oracle VM VirtualBox Extension Pack is needed for RDP support or alternatively an open-source virtualbox-ext-vnc can be used for VNC support. Also consider installing guest additions ISO for guests to be able to install or update the tools.

VirtualBox installation includes the VirtualBox web service (vboxwebsrv) providing a HTTP(S) server offering API to clients such as RemoteBox. The service should not and also refuses to run as root. For improved security an additional user for running VMs and web service should be created. The user requires a password (to be used for remote login), a home directory (for VirtualBox settings and virtual machines configuration) and a shell (for RemoteBox to be able to login). The rest of this page assumes a vbox user with primary group vboxusers.

The provided service file /usr/lib/systemd/system/vboxweb.service serves as a template that can be custimized with a drop-in file as follows:

Logging can be enabled by editing the ExecStart line in the override file above to include the --logfile <log file location> directive. For increased verbosity you can also include the --verbose directive. Make sure the vbox user has permissions to write to the configured log file location.

The --host directive can be changed to localhost or the hostname to only bind the service locally, or be set to an IP of a single chosen interface. An alternative port from the default 18083 can be set with --port.

You also need to create a tmpfile rule for vboxwebsrv's PID file:

To test vboxweb.service immediately you need to first manually create the /run/vboxwebsrv directory:

Now the vboxweb.service can be started and/or enabled.

Open RemoteBox and click the Connect button. Specify the following:

To make it easier connecting during future sessions, after login go to File > Connection Profiles and create a new connection profile.

If you encounter a login problem connecting to the server, first check that the service is running. From the server console, check vboxweb.service unit status.

It should output that it is running. If not, check logging with journalctl and, if you configured --logfile, the vboxwebsrv's log file for any leads.

Even with increased verbosity the VirtualBox web service might not give you any useful leads. In that case you can try to run the server manually as vbox from the command line with su or sudo.

Omit the --background and --logfile directives. If the service starts, the problem could be permissions to the log file. Leave it running and check if you can connect with RemoteBox from the client. Also check the ~/.config/VirtualBox directory gets created and populated with configuration and/or log files.

If you still cannot connect, you can stop the service with Ctrl-c and start it with the --background directive. Next, using netstat or similar check whether vboxwebsrv is listening on port 18083. If you see a different port you can try connecting with RemoteBox on that port instead.

Another reason could be a firewall, either on your server, or even on your client.

If you are getting the following error message:

Check that your home directory is writable for the user vbox.

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/systemd/system/vboxweb.service
```

Example 2 (unknown):
```unknown
/etc/systemd/system/vboxweb.service.d/override.conf
```

Example 3 (unknown):
```unknown
[Service]
User=vbox
Group=vboxusers
PIDFile=/run/vboxwebsrv/vboxwebsrv.pid
ExecStart=
ExecStart=/usr/bin/vboxwebsrv --pidfile /run/vboxwebsrv/vboxwebsrv.pid --background --host 0.0.0.0
```

Example 4 (unknown):
```unknown
--logfile <log file location>
```

---

## Clover

**URL:** https://wiki.archlinux.org/title/Clover

**Contents:**
- Supported file systems
- Installation
  - UEFI Systems
  - BIOS Systems
- Configuration
  - chainload systemd-boot
- See also

Clover EFI is a boot loader developed to boot macOS (Hackintoshes), Windows and Linux in legacy or UEFI mode.

The main advantages of Clover are:

Clover inherits the support for the file systems from the firmware (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any UEFI drivers placed in the drivers subdirectory of its own installation directory on the ESP (i.e. esp/EFI/clover/drivers/)[1].

Clover also ships with multiple EFI file system drivers.

As Clover emulates a UEFI environment on BIOS systems, the steps for each type of system are similar.

Mount EFI system partition to /boot. This is the preferred method when directly booting an EFI boot stub kernel from UEFI.

Generate initial ramdisk environment with mkinitcpio

Download Clover Bootable ISO from here.

Extract the archive Clover-*-X64.iso.7z and find the Clover-*-X64.iso file, mount it to a directory like /mnt/iso. It should be noted all file/folder names will be displayed in lower case in Linux, which is different from Windows and Mac OS.

Copy the whole /mnt/iso/efi folder to your EFI system partition. The tree for /boot should look likes the following

Download the Clover Bootable ISO.

Extract the archive Clover-*-X64.iso.7z and find the Clover-*-X64.iso file, mount it to directory like /mnt/iso.

The Clover code must be merged now with current Master and Partition Boot Records. Example with block device /dev/sda and ESP on 1st partition /dev/sda1, change if necessary:

Mount the EFI system partition to /boot.

Copy the whole /mnt/iso/efi folder to your EFI system partition.

Copy the legacy boot loader to the EFI system partition:

Configuration is done through an XML file config.plist under path EFI/CLOVER from the EFI system partition.

For the meaning of each key, please reference their wiki for custom entries. The key Volume should be the PARTUUID of the EFI system partition and must be in uppercase. The minimal initramfs initramfs-linux.img in Argumentsand the Linux kernel executable vmlinuz-linux in Path are relative to the EFI system partition. Backslashes should be used in accordance with EFI standards. For other arguments in Arguments, please reference EFI boot stub and Kernel parameters#Parameter list.

In this example, the initramfs and kernel files are placed at the root of the EFI system partition, at the same level as the efi directory. The EFI system partition is mounted at /boot

If you need a boot loader for BIOS systems that follows The Boot Loader Specification, then systemd-boot can be pressed into service on BIOS systems. This is the configuration file needed make Clover chainload systemd-boot.

**Examples:**

Example 1 (unknown):
```unknown
esp/EFI/clover/drivers/
```

Example 2 (unknown):
```unknown
Clover-*-X64.iso.7z
```

Example 3 (unknown):
```unknown
Clover-*-X64.iso
```

Example 4 (unknown):
```unknown
/mnt/iso/efi
```

---

## Arch Linux

**URL:** https://wiki.archlinux.org/title/Arch_Linux

**Contents:**
- Principles
  - Simplicity
  - Modernity
  - Pragmatism
  - User centrality
  - Versatility
- History
  - The early years
  - The middle years
  - Birth of the ArchWiki

Arch Linux is an independently developed, x86-64 general-purpose GNU/Linux distribution that strives to provide the latest stable versions of most software by following a rolling release model.

The default installation is a minimal base system, configured by the user to only add what is purposely required.

Arch Linux defines simplicity as without unnecessary additions or modifications. It ships software as released by the original developers—upstream—with minimal distribution-specific downstream changes. Patches not accepted by upstream are avoided, and Arch's downstream patches consist almost entirely of backported bug fixes that are obsoleted by the project's next release.

In a similar fashion, Arch ships the configuration files provided by upstream with changes limited to distribution-specific issues like adjusting the system file paths. It does not add automation features such as enabling a service simply because the package was installed. Packages are only split when compelling advantages exist, such as to save disk space in particularly bad cases of waste.

Arch Linux official packages do not provide system-wide GUI configuration utilities (i.e. there is neither a GUI installation wizard nor a GUI system configuration tool, and Arch as a distribution does not promote GUI tools for system configuration), encouraging users to perform most system configuration from a command-line shell and a text editor.

Arch Linux strives to maintain the latest stable release versions of its software as long as systemic package breakage can be reasonably avoided. It is based on a rolling-release system, which allows a one-time installation with continuous upgrades.

Arch Linux incorporates the latest available kernels as well as features available to GNU/Linux users, including:

Arch Linux does not keep using ancient things if there are modern, future-proof, and better options.

Arch is a pragmatic distribution rather than an ideological one—the principles here are only useful guidelines. Ultimately, design decisions are made on a case-by-case basis through developer consensus. Evidence-based technical analysis and debate are what matter, not politics or popular opinion.

The large number of packages and build scripts in the various Arch Linux repositories offer free and open source software for those who prefer it, as well as proprietary software packages for those who embrace functionality over ideology.

Whereas many GNU/Linux distributions attempt to be more user-friendly, Arch Linux has always been, and shall always remain user-centric:

All users are encouraged to participate and contribute to the distribution. Reporting and helping fix bugs is highly valued and patches improving packages or the core projects are very appreciated: Arch's developers are volunteers and active contributors will often find themselves becoming part of that team. Archers can freely contribute packages to the Arch User Repository, improve the ArchWiki documentation, provide technical assistance to others or just exchange opinions in the forums, mailing lists, or IRC channels. Arch Linux is the operating system of choice for many people around the globe, and there exist several international communities that offer help and provide documentation in many different languages.

Arch Linux is a general-purpose distribution. Upon installation, only a command-line environment is provided; rather than tearing out unneeded and unwanted packages, the user is offered the ability to build a custom system by choosing among thousands of high-quality packages provided in the official repositories for the x86-64 architecture.

Arch is a rolling-release model backed by pacman, a lightweight, simple and fast package manager that allows for continuously upgrading the entire system with one command. Arch also provides the Arch build system, a ports-like system to make it easy to build and install packages from source, which can also be synchronized with one command. In addition, the Arch User Repository contains many thousands of community-contributed PKGBUILD scripts for compiling installable packages from source using the makepkg application. It is also possible for users to build and maintain their own custom repositories with ease.

The Arch community has grown and matured to become one of the most popular and influential Linux distributions, also testified by the attention and review received over the years.

Apart from select exceptions, Arch developers remain unpaid, part-time volunteers, and there are no prospects for monetizing Arch Linux, so it will remain free in all senses of the word. Those curious to peruse more detail about Arch's development history can browse the Arch entry in the Internet Archive Wayback Machine and the Arch Linux News Archives.

Judd Vinet—a Canadian programmer and occasional guitarist—began developing Arch Linux in early 2001. Its first formal release—Arch Linux 0.1—was on 2002-03-11. Inspired by the elegant simplicity of Slackware, BSD, PLD Linux and CRUX, and yet disappointed with their lack of package management at the time, Vinet built his own distribution on similar principles as those distributions. But, he also wrote a package management program called pacman, to automatically handle package dependency resolution, installation, removal, and upgrades.

The early Arch community grew steadily, as evidenced by this chart of forum posts, users, and bug reports. Moreover, it was from its early days known as an open, friendly, and helpful community.

On 2005-07-08 the ArchWiki was first set up on the MediaWiki engine.

In late 2007, Judd Vinet retired from active participation as an Arch developer, and smoothly transferred the reins over to American programmer Aaron Griffin, also known as Phrakture.

The Official Arch Linux Logo Contest—see the submissions—took place at the same time.

The 2012-07-15 release of the installation image deprecated the menu-driven Arch Installation Framework (AIF) in favor of the Arch Install Scripts (arch-install-scripts).

Between 2012 and 2013 the traditional UNIX System V init system was replaced by systemd. [1][2][3][4]

On 2017-01-25 it was announced that support for the i686 architecture would be phased out due to its decreasing popularity among the developers and the community. By the end of November 2017, all i686 packages were removed from the mirrors.

At the start of 2020, in a team effort the Arch Linux staff devised a new process for determining future leaders, documented in DeveloperWiki:Project Leader.

As Aaron Griffin had decided to step down from his role, a poll was held to elect a new person to replace him, and on 2020-02-24 its results were published, making the election of Levente Polyak official.

In May 2023, Arch Linux migrated its packaging infrastructure to a self-hosted GitLab instance. Besides internal changes and innovations, this also resulted in splitting the testing repository into core-testing and extra-testing, the staging repository into core-staging and extra-staging, and finally community has been merged into extra.

Several months later, in November 2023, the old Flyspray bug tracker bugs.archlinux.org was migrated to gitlab.archlinux.org and its collaboration features—issues and merge requests—were opened for public. For archiving reasons there remains a static copy of the old bug tracker, so that links—for example the randomly picked FS#56716—are still valid.

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Core-testing

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## Install Arch Linux with accessibility options

**URL:** https://wiki.archlinux.org/title/Install_Arch_Linux_with_accessibility_options

**Contents:**
- Pre-installation
  - Boot the live environment
  - Multiple sound cards
  - Change speech language
- Installation
  - Install essential packages
- Configure the system
  - Sound card
  - Enable the services
- Reboot

The official Arch Linux installation medium supports various Accessibility features:

This document describes how to install Arch Linux using these features.

When the installation medium starts booting, press Down followed by Enter to boot with speech enabled.

USB braille displays should be detected automatically via udev.

If your computer has several sound cards, you will hear the following message: Please select your sound card for speech output.

When you hear a beep on the output that you would like to use, press Enter to select the card.

To change the espeak-ng language/voice used by espeakup.service, edit the unit so that the language code is appended to default_voice= in the Environment= directive.

You can also change the espeak-ng voice variant by appending +variant to the language code. See espeakup(8) and espeak-ng(1) for more information.

For speech support in the installed system, you need espeakup and alsa-utils. If you use a braille display, install the brltty package.

Append the required packages to the pacstrap(8) call when installing:

If #Multiple sound cards were detected, copy the /etc/asound.conf file, which has been generated in the installation medium:

To have speech support after booting into the installed system you need to enable espeakup.service. See also #Change speech language.

After booting into the newly installed system it should start speaking automatically.

See Accessibility#Troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
espeakup.service
```

Example 2 (unknown):
```unknown
default_voice=
```

Example 3 (unknown):
```unknown
Environment=
```

Example 4 (unknown):
```unknown
# pacstrap -K /mnt base linux linux-firmware espeakup alsa-utils
```

---

## Working with the serial console

**URL:** https://wiki.archlinux.org/title/Serial_console

**Contents:**
- Configure console access on the target machine
  - Boot loader
    - GRUB
      - GRUB first stage serial console
    - GRUB Legacy
    - rEFInd
    - Syslinux
  - Kernel
  - getty
- Making Connections

An Arch Linux machine can be configured for connections via the serial console port, which enables administration of a machine even if it has no keyboard, mouse, monitor, or network attached to it.

Installation of Arch Linux is possible via the serial console as well.

A basic environment for this scenario is two machines connected using a serial cable (9-pin connector cable). The administering machine can be any Unix/Linux or Windows machine with a terminal emulator program (PuTTY or Minicom, for example).

The configuration instructions below will enable boot loader menu selection, boot messages, and terminal forwarding to the serial console.

When using GRUB with a generated grub.cfg, edit /etc/default/grub and enable serial input and output support:

Next add the GRUB_SERIAL_COMMAND variable and set the options for the serial connection. For COM1 (/dev/ttyS0) with baud rate of 115200 bit/s:

Read GRUB's manual on Using GRUB via a serial line and the serial command for detailed explanation of the available options.

When GRUB is installed to an encrypted /boot/ partition - GRUB first stage (core.img) will show Enter passphrase for hdX,gptY: password prompt only on platform console and will not show anything in serial console even if all serial console configuration steps were done properly.

This happens because the grub-install has special behavior for GRUB_ENABLE_CRYPTODISK=y and will create early config placed in /boot/grub/PLATFORM/load.cfg but grub-install ignores serial console configuration from /etc/default/grub for GRUB first stage.

The /boot/grub/PLATFORM/load.cfg file gets overwritten each time grub-install is launched.

To get the GRUB cryptodisk password prompt on the serial console a few extra configuration steps are required:

1. Run the following command to generate /boot/grub/PLATFORM/load.cfg and see the correct grub-mkimage parameters for your system:

You can reboot the system to check if it boots properly, but you should save the output of the commahd above - it will be hecessary at step 4.

2. Copy /boot/grub/PLATFORM/load.cfg to /boot/grub/PLATFORM/early-grub.cfg

3. Add the following lines at the beginning of /boot/grub/PLATFORM/early-grub.cfg (change those lines according to desired configuration as described above):

4. Edit grub-mkimage parameters from step 1 (the grub-install output):

Replace --config '/boot/grub/PLATFORM/load.cfg' to --config '/boot/grub/PLATFORM/early-grub.cfg' Remove paramters with empty arguments (like --dtb '' and --sbat '') and add serial and terminal modules to the end of the grub-mkimage parameters list.

5. Run grub-mkimage with these parameters.

6. On BIOS platforms like i386-pc (for EFI platforms just skip this step) run the following command to install new core.img to your system:

In order to revert those changes - just reinstall GRUB using grub-install command.

Edit the GRUB Legacy configuration file /boot/grub/menu.lst and add these lines to the general area of the configuration:

rEFInd supports serial console only in text mode. Edit refind.conf and uncomment textonly.

To enable serial console in Syslinux, edit syslinux.cfg and add SERIAL as the first directive in the configuration file.

For COM1 (/dev/ttyS0) with baud rate of 115200 bit/s:

The serial parameters are hardcoded to 8 bits, no parity and 1 stop bit.[1]. Read Syslinux Wiki:Config#SERIAL for the directive's options.

Kernel's output can be sent to serial console by setting the console= kernel parameter. The last specified console= will be set as /dev/console.

See https://docs.kernel.org/admin-guide/serial-console.html.

At boot, systemd-getty-generator(8) will start a getty instance for each console specified in the kernel command line.

If you have not configured console= in kernel command line start serial-getty@device.service. For /dev/ttyS0 (COM1) that would be serial-getty@ttyS0.service. Enable the service to start it at boot.

Unless specified otherwise in the kernel command line, getty will be expecting 38400 bit/s baud rate, 8 data bits, no parity and one stop bit-times.

Perform these steps on the machine used to connect the remote console.

uucp tool cu can be used to "Call Up" another system and act as a serial console:

dterm-gitAUR is a tiny serial communication program. If you invoke it without parameters, it will connect to /dev/ttyS0 at 9600 baud by default. The following example connect to /dev/ttyS0 at 115200 baud, with 8 data bits, no parity bit and 1 stop bit-times:

See its README for more examples.

minicom can be obtained from the official repositories. Start Minicom in setup mode:

Using the textual navigation menu, change the serial port settings to the following:

Press Enter to exit the menus (pressing Esc will not save changes). Remove the modem Init and Reset strings, as we are not connecting to a modem. To do this, under the Modem and Dialing menu, delete the Init and Reset strings. Optionally save the configuration by choosing save setup as dfl from the main menu. Restart minicom with the serial cable connected to the target machine. The special keys for navigating Minicom can be found in the help menu which is opened by pressing Ctrl+A Z (i.e., exit session is Ctrl+A X).

picocom is a tiny dumb-terminal emulation program that is very like minicom, but instead of mini, it is pico. The following example connect to ttyS0 at 9600 bps:

See its manual for detailed usage.

GNU Screen is able to connect to a serial port. It will connect at 9600 baud by default:

A different baud rate (e.g. 115200) may be specified on the command line.

To end the session, press Ctrl+a followed by K. Alternatively, press Ctrl+a, type :quit and confirm it by pressing Enter.

Serialclient[2] is a CLI client for serial connection written in ruby. Install ruby package, then install it with the following:

Then, you can use like this:

tinyserialAUR is a minicom replacement for accessing serial ports on Linux inspired by FreeBSD 'tip'.

tioAUR is a simple serial device tool which features a straightforward command-line and configuration file interface to easily connect to serial TTY devices for basic I/O operations. It has less focus on classic terminal/modem features and more focus on the needs of embedded developers and hackers. tio was originally created to replace screen for connecting to serial devices when used in combination with tmux.

socat is a command line based utility that establishes two bidirectional byte streams and transfers data between them.

microcom Copy bytes from stdin to TTY and from TTY to stdout, its part of busybox

On Windows machines, connect to the serial port using programs like PuTTY or Terminalbpp.

Even though [3] has only raw and terse instructions, it presents the full scene. It is important to note that here, the machine under test got unresponsive in a reproducible manner. And that it happened during normal operation. So it could be accessed normally before it needed debugging. However, in general, the serial console is also useful for debugging boot issues. Perhaps by configuring the boot loader by hand at machine startup time. Also note the mentioned netconsole within the P.S paragraph of the external link from this section.

Debugging a system by attaching a USB serial adapter requires starting serial-getty@ttyUSBN.service which may not be possible if the system cannot be interacted with in normal ways. A solution is to write an udev rule that starts the service when a USB serial adapter is plugged in.

To allow using the USB serial adapter the other way around too, the udev rule can be limited to trigger only on a specific USB port. To do that, plug in the adapter and find out its used USB port identifier. E.g. for /dev/ttyUSB0 run:

Create a udev rule with the following contents using the value obtained with the previous command:

Re-plug the USB serial adapter and the appropriate serial-getty@ttyUSBN.service will get started automatically. Verify it by checking the unit status with systemctl. The service will get automatically stopped when the USB device is unplugged.

If you are having trouble sending a Ctrl+c command through minicom you need to switch off hardware flow control in the device settings (minicom -s), which then enables the break.

Unlike ssh, serial connections do not have a mechanism to transfer something like SIGWINCH when a terminal is resized. This can cause weird problems with some full-screen programs (e.g. less) when you resize your terminal emulator's window.

Resizing the terminal via stty is a workaround:

However, this requires you to manually input the proper geometry. The following methods should be simpler.

1. There is a lesser-known utility called resize, shipped with xterm, that can solve this problem. Invoke it without parameters after you resize the terminal emulator's window:

2. If you do not want to install xterm, it is possible to do the same work via a shell function. Put the following function into your bash/zshrc and invoke it without parameters after resizing the terminal emulator's window:

The generic 8250 serial driver exposes 32 hardware serial ports, as set in the Arch kernel configuration. This means by default serial ports are created numbered from /dev/ttyS0 to /dev/ttyS31. On most systems many of these ports will be non-functional.

The number can be reduced by setting the kernel parameter 8250.nr_uarts. E.g.:

This value must be set as a kernel boot parameter not a module option, as the serial8250 driver is compiled into the kernel image.

**Examples:**

Example 1 (unknown):
```unknown
/etc/default/grub
```

Example 2 (unknown):
```unknown
/etc/default/grub
```

Example 3 (unknown):
```unknown
...
GRUB_TERMINAL_INPUT="console serial"
...
GRUB_TERMINAL_OUTPUT="gfxterm serial"
...
```

Example 4 (unknown):
```unknown
GRUB_SERIAL_COMMAND
```

---

## Mac

**URL:** https://wiki.archlinux.org/title/Mac

**Contents:**
- Overview
- Pre-installation
- Partitions
  - Arch Linux with macOS or other operating systems
- Installation
- Setup boot loader
  - Installing to the EFI system partition
    - systemd-boot
    - rEFInd
      - Installing from macOS

This page complements the Installation guide with instructions specific to Apple Macs. The Arch installation image supports Apple Macs with Intel processors, but neither PowerPC nor Apple Silicon processors.

Summed up, the procedure for installing Arch Linux on a Mac is:

Before proceeding with the installation of Arch Linux, follow these steps.

If only Arch Linux is desired, then format the entire disk according to Installation guide#Partition the disks. To set up dual boot, follow these steps. Once done, go to #Installation.

Macs typically have the following partition table. In Macs that use the Apple Fusion Drive, the partition scheme could be different.

To install Arch with macOS, keep these partitions, and follow these steps.

Here is an example setup with five discrete partitions:

These steps install Arch, assuming #Pre-installation and #Partitions are done.

Macs use UEFI for booting, so any UEFI boot loader will work. The built-in boot loader (shown when holding Alt during boot) will detect any EFI system partition that has a /EFI/BOOT/BOOTX64.EFI file, showing it as a "EFI Boot" entry. Most UEFI boot loaders support installing directly to this location, making a dual boot setup easy.

The boot loader also has an alternate partition discovery method described in #Installing a boot loader to a separate HFS+ partition which is the method used for booting macOS, but can also be used for Linux.

Follow the instructions at systemd-boot#Installing the UEFI boot manager. After installing, a copy of systemd-boot will be present at /EFI/BOOT/BOOTX64.EFI.

To install rEFInd to the /EFI/BOOT/BOOTX64.EFI location, run:

Where /dev/sdXY is the EFI system partition. After installing, see rEFInd#Configuration to finish setup.

These steps assume macOS is still installed on a partition, and the steps of the Installation guide were completed up to Installation guide#Boot loader. Boot into Safe Mode by holding down Command+R, then disable SIP.

Boot macOS, and run the rEFInd install script,

rEFInd installed itself into Apple's boot partition, and replaced Apple's boot menu with its own. Boot into Safe Mode by holding down Command+R, and enable SIP.

Reboot without holding down any keys. Arch should be recognized as vmlinuz-linux by default. If it is not, uncomment the lines scan_all_linux_kernels and also_scan_dirs in refind.conf. For configuration, see rEFInd#refind_linux.conf. Since rEFInd by default mounts root as ro, it is recommended to create refind-linux.conf.

To install GRUB to /EFI/BOOT/BOOTX64.EFI, follow the instructions at GRUB#Installation, adding the --removable option when running grub-install.

Despite using UEFI, the Mac native EFI boot loader does not use the EFI system partition for booting macOS. Instead, it uses the following conditions to find existing macOS installations inside all the partitions in internal and external drives and shows them as possible boot options if they are satisfied:

The advantage of this method to boot Arch over using a BOOTX64.EFI file in the EFI system partition is that it can coexist with macOS nicely, showing the partition as a bootable volume in the macOS Startup Disk settings. However, this method requires manual configuration. The following steps will illustrate how to perform this configuration using GRUB.

First, create a new HFS+ partition. This can be done through the macOS Disk Utility, or the mkfs.hfsplus tool in the hfsprogsAUR package. The size and mount point of the partition depend on how you plan to use it:

Mount the partition, then create the mach_kernel file:

Create the directory structure for the boot loader:

Now you can install any UEFI boot loader you want. For example, to do a manual install of rEFInd:

Finally, you can create an optional /mountpoint/System/Library/CoreServices/SystemVersion.plist file that will display some information about the volume in the macOS Startup Disk settings:

After following these instructions, the new volume will appear on the Mac boot loader when holding down Alt during boot, and it will also appear as a bootable volume in the macOS Startup Disk options.

It is possible to boot directly from GRUB in EFI mode without using rEFIt through what is known as "blessing" after placing GRUB on a separate partition. These instructions are known to work on a MacBook7,1. It is advisable to host GRUB on either a FAT32 or HFS+ partition, but ext2 or ext3 may also work.

After the GRUB install is in the desired location, the firmware needs to be instructed to boot from that location. This can be done from either an existing macOS install or an macOS install disk. The following command assumes that the GRUB install is in /efi/grub/ on an existing macOS partition:

Macs use ICC profiles which can easily be loaded in Arch. The current profile can be shown using ColorSync Utility or System Preferences > Displays > Color. These files correspond to particular models,

Install and configure lirc. See LIRC.

Make LIRC use /dev/usb/hiddev0 or /dev/hiddev0:

Use irrecord to create a configuration file matching your remote control signals:

Start lircd.service and use irw to check if it works.

Alternatively, use the following:

Install hfsprogsAUR and use fdisk to list the partitions:

The "Unknown" partition is our macOS partition, which is located in /dev/sda2. We can use this in our fstab:

It can then be mounted, and the content accessed.

This section addresses error message when mounting hfsplus partition:

Since Yosemite, HFS+ partitions are now wrapped a CoreStorage volume. Verify that you have an CoreStorage volume.

HFS+ uses two volume headers, one 1024 bytes into the device and one 1024 from the end of the device. With the HFS+ partition wrapped in the CoreStorage volume the end of the partition is not actually 1024 bytes from the end of the /dev/sdX2 partition. To fix this you need to specify sizelimit=X when mounting.

To determine sizelimit do the following:

What you see now is the output of the HFS partition itself without the CoreStorage volume. Take the size in sectors (622738176 in this example) and multiply by the number of bytes in your logical sector size (512 in this example).

622738176 * 512 = 318841946112

Finally, mount your disk with the sizelimit=X option.

HFS+ partitions are not fully supported by Linux and are mounted as read-only by default. In order to write to an HFS+ partition, the safe way is to disable journaling. This can be accomplished using the macOS Disk Utility. Refer to this Apple support page for more information or try to do it from the command line:

In this example we will use disk0s3 partition named as Macintosh HD. To know if journaling is activate or not you could execute:

As you can read the journaling is active. To turn off the journaling you could execute:

To verify it is done execute the info command again.

If you get noting as output, then journaling is disabled.

However, if you fail to disable journaling. You can change "auto,user,rw,exec" in /etc/fstab to "auto,user,force,rw,exec" and mount it.

If you want to access your macOS user directories from Linux, write down the UID and GID for the users. macOS begins with the first user's UID at 501 while Arch defaults to 1000.

The default UID and GID on Arch Linux for a user is 1000, adjust the following steps according to your setup.

In Leopard, the NetInfo Manager application is not present. A different set of steps is required for UID synchronization:

To synchronize your UID in Arch Linux, you are advised to perform this operation while creating a new user account. It is therefore recommended that you do this as soon as you install Arch Linux.

Now you must substitute Arch's home with macOS's home, by modify entries of /etc/fstab. In order to be able to access a macOS user's directory, only the uid and gid need to match (usernames can differ).

The startup chime volume is controlled by the EFI variable SystemAudioVolume-7c436110-ab2a-4bbb-a880-fe41995c9f82. So it can be muted with

Bear in mind that the file may have the immutable bit set by default, which will prevent even root from overwriting the file. See File permissions and attributes#File attributes. To remove it, issue the following:

After that, run the printf command and it should overwrite the file properly. Verify the file's contents and then set the immutable bit again with chattr +i once satisfied.

Alternatively, you can use a macOS install disk to mute the chime. Boot from it, select language, then click Utilities > Terminal, and enter

The Mac boot loader supports loading custom icons for each volume it detects. The custom icon must be in the .icns format, and be located at the root of the volume containing the boot loader, with the file name .VolumeIcon.icns.

The following example downloads an Arch logo SVG with wget, converts it to PNG with librsvg and then converts it to an .icns with libicns:

Obviously, you can replace the Arch logo with any other icon you like.

**Examples:**

Example 1 (unknown):
```unknown
partition  mountpoint  size          type  label
/dev/sda1  /efi        200MiB        vfat  EFI
/dev/sda2  -           ?             hfs+  macOS
/dev/sda3  -           ?             hfs+  Recovery
/dev/sda4  -           100MiB        hfs+  Boot Arch Linux from the Apple boot loader (optional)
/dev/sda5  /boot       100MiB        boot  boot
/dev/sda6  -           ?             swap  swap (optional)
/dev/sda7  /           15-20GiB      ext4  root
/dev/sda8  /home       remaining     ext4  home
```

Example 2 (unknown):
```unknown
arch noapic irqpoll acpi=force
```

Example 3 (unknown):
```unknown
/EFI/BOOT/BOOTX64.EFI
```

Example 4 (unknown):
```unknown
/EFI/BOOT/BOOTX64.EFI
```

---

## Stumpwm

**URL:** https://wiki.archlinux.org/title/Stumpwm

**Contents:**
- Installation
  - Install via Package Manager
  - Install via Roswell
- Documentation and support
- Configuration
  - Change cursor from default X shape
  - Change window focus on mouse click
  - Enable modeline
  - Set font for messages and modeline
- Tweaking

StumpWM is a manually tiling, keyboard driven X11 window manager written entirely in Common Lisp.

The spiritual successor to the cult classic Ratpoison, StumpWM adds all the flexibility and hackability of Common Lisp, allowing the user to make modifications to the source of the window manager even while it is running. It is also known as "the emacs of WMs."

From StumpWM's homepage:

Want to see it in action? A StumpWM user created a video.

A runnable StumpWM installation consists of 3 parts:

Install stumpwm or stumpwm-gitAUR.

If you are installing without an AUR helper, you should install these packages in the following order:

After installing put exec stumpwm in your ~/.xinitrc and run startx. To quit, with the default configuration press C-t ; then type quit and press enter.

Both packages will install an xsession entry in /usr/share/xsessions so if you use a display manager that checks that directory, you should be good to go.

For a list of commonly used key-bindings, press C-t ?.

It is highly recommended to use roswell to manage your Lisp REPL.

This method makes it easy to upgrade StumpWM together with other Lisp packages using ql:update-all-dists.

to start REPL in roswell run ros run in terminal, to install stumpwm run (ql:quickload :stumpwm) inside REPL

in order to launch it through login manager or ~/.xinitrc, an executable file must be created. create new project using roswell :

Then place stumpwm.ros file to wherever you like and make it the entry point of this awesome WM.

To add stumpwm to the Login Manager, create stumpwm.desktop in /usr/share/xsessions/:

or you can just start using ~/.xinitrc

There is a TeXInfo manual included in the AUR packages, the source, and online.

There is also a wiki, an IRC channel #stumpwm on Libera Chat, and a mailing list. For more information, see the project's website.

StumpWM stores its configuration in ~/.stumpwmrc or you can use ~/.config/stumpwm/config

By default StumpWM leaves the cursor as XOrg's standard X shape with the hotspot in the centre. You can have the more usual left-facing pointer by running

You can also put this in your configuration file

Clicking on another window will send the click event to that window, but it will not get focus meaning any keyboard input will go to whichever window has focus. The following line makes focus change to any window that is clicked on.

This sets up a basic modeline with the group name followed by window names on the left and the date and time on the right.

First set the window name format and overall modeline format

The date format is constructed using the same format specifiers as strftime(3) e.g.

Optionally change how often the modeline updates on its own, in seconds (it also updates whenever you do something with StumpWM like switch window).

Finally enable the modeline (this must come after you have set the options you wanted)

StumpWM uses the default XOrg font which is probably small and pixelated. You can set font by calling, for example,

where the string is generated by xorg-xfontsel.

Another way is to use the ttf-fonts module to set a custom font. Note that the performance in the result is not as great, and that it requires another lisp module clx-truetype, which is not in the quicklisp distribution any more. Get a copy of it from a backed up repository, put it under your ~/quicklisp/local-projects/, and run

See the wiki for a variety of useful tweaks for your .stumpwmrc.

Additionally, the stumpwm-contrib repository contains many useful utilities, and can be installed via stumpwm-contrib-gitAUR. For example, if you are an emacs user, you will find an emacs minor mode for editing StumpWM files (and interfacing with the program stumpish, but more on that below).

stumpish is the STUMP window manager Interactive SHell. It is a program that allows the user to interact with StumpWM while it is running, from the comfort of a terminal (or using the emacs mode). It is installed with StumpWM in /usr/bin/.

in the REPL, it can be solved by deleting ~/.Xauthority. See this issue on github

find / | grep sbcl.core

Then you may reinstall stumpwm

to your .stumpwmrc (source: [1])

**Examples:**

Example 1 (unknown):
```unknown
exec stumpwm
```

Example 2 (unknown):
```unknown
/usr/share/xsessions
```

Example 3 (unknown):
```unknown
ql:update-all-dists
```

Example 4 (unknown):
```unknown
(ql:quickload :stumpwm)
```

---

## Sound system

**URL:** https://wiki.archlinux.org/title/Sound_server

**Contents:**
- Drivers and low-level interfaces
- Sound servers

Any Linux sound system consists of several layers:

A default Arch Linux installation already includes the kernel sound system (ALSA), and lots of utilities for it can be installed from the official repositories. If you want additional features you can install one of several sound servers.

See also Wikipedia:Sound server.

---

## Sound system

**URL:** https://wiki.archlinux.org/title/Sound_system

**Contents:**
- Drivers and low-level interfaces
- Sound servers

Any Linux sound system consists of several layers:

A default Arch Linux installation already includes the kernel sound system (ALSA), and lots of utilities for it can be installed from the official repositories. If you want additional features you can install one of several sound servers.

See also Wikipedia:Sound server.

---

## Install Arch Linux via SSH

**URL:** https://wiki.archlinux.org/title/Install_Arch_Linux_via_SSH

**Contents:**
- On the remote (target) machine
- On the local machine
- Installation on a headless server
  - Prepare cloud-init configuration files
  - Using an additional FAT formatted drive
  - Using an additional ISO
  - Using a single USB flash drive
  - Using a single custom-built ISO
  - Boot from the installation medium

This article is intended to show users how to install Arch remotely via an SSH connection. Consider this approach when the host is located remotely or you wish to use the copy/paste ability of an SSH client to do the Arch install.

Follow the steps from Installation guide#Pre-installation up to and including connecting to the internet (setting the keyboard layout and font can be skipped).

At that point, set the required root password to allow an SSH connection, since the default Arch password for root is empty:

Confirm that PermitRootLogin yes is set in /etc/ssh/sshd_config. If it is not, set it and reload the OpenSSH daemon sshd.service to apply the changes.

On the local machine, connect to the target machine via SSH with the following command:

From here one is presented with the live environment's welcome message and is able to administer the target machine as if sitting at the physical keyboard. At this point, if the intent is to simply install Arch from the live media, resume at Installation guide#Update the system clock. If the intent is to edit an existing Linux install that got broken, follow the Install from existing Linux wiki article.

This article or section is a candidate for merging with Cloud-init#Archiso.

This section describes installation of Arch Linux on a headless server without a keyboard, mouse or display. It uses an additional drive with cloud-init NoCloud configuration to automatically configure OpenSSH authorized keys and optionally iwd connection(s).

There are three required cloud-init configuration files: meta-data, user-data and network-config.

The meta-data file can be empty:

user-data will contain the relevant configuration:

Replace ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX with your public SSH key. To add multiple keys, simply repeat the statement as shown above.

To automatically connect to a Wi-Fi network, use the write_files: statement to create iwd network configuration files in the correct directory. For example:

cloud-init creates network configuration that differs from one shipped in the ISO. I.e. mDNS responder and DHCPv6 client are not enabled. To avoid this, disable cloud-init's network configuration in network-config:

Once all three files are created they need to be placed on a drive with an ISO 9660 or FAT volume labeled CIDATA.

Use a FAT formatted drive. Copy meta-data, user-data and network-config to the drive and change the file system's LABEL to CIDATA.

You will need to attach this drive to the headless machine in addition to the one with the official ISO.

Create a cloud-init.iso file using xorriso from libisoburn:

Prepare the cloud-init data medium by burning cloud-init.iso to an optical disc or, if deployment options permit, use the ISO as is.

If the installation image is written to e.g. a USB flash drive, provided there is enough space on the drive, an additional partition to house cloud-init data can be created.

Install dosfstools, mtools and libisoburn.

First create a 2 MiB FAT image with its LABEL set to CIDATA:

Copy the meta-data and user-data files to the root of it:

Repack the official ISO to include the FAT image as a third partition:

Finally follow USB flash installation medium#Using the ISO as is (BIOS and UEFI) to prepare the USB flash drive installation medium using the repacked ISO (archlinux-version-x86_64-with-cidata.iso).

Alternatively, create a custom ISO using Archiso. This allows using only one drive regardless of type.

Use the releng profile as basis. Place the cloud-init configuration files in airootfs/var/lib/cloud/seed/nocloud/ and build the ISO.

Once finished, deploy the installation medium and the cloud-init data medium (if it is separate) to the headless machine using the appropriate method.

Power up the headless machine and boot into a live Arch environment from the installation medium. Wait for a minute or so to allow the headless machine time to boot up and connect to the network.

From your existing machine (with keyboard and display) SSH into the live Arch environment on the headless server and complete the installation as described in the Installation guide.

**Examples:**

Example 1 (unknown):
```unknown
PermitRootLogin yes
```

Example 2 (unknown):
```unknown
/etc/ssh/sshd_config
```

Example 3 (unknown):
```unknown
sshd.service
```

Example 4 (unknown):
```unknown
$ ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ip.address.of.target
```

---

## Touchpad Synaptics

**URL:** https://wiki.archlinux.org/title/Touchpad_Synaptics

**Contents:**
- Installation
- Configuration
  - Frequently used options
  - Configuration on the fly
    - Console tools
    - Graphical tools
  - Xfce
  - Cinnamon
  - MATE
- Advanced configuration

This article details the installation and configuration process of the Synaptics input driver for Synaptics (and ALPS) touchpads found on most notebooks.

The Synaptics driver can be installed with the package xf86-input-synaptics.

The primary method of configuration for the touchpad is through an Xorg server configuration file. After installing xf86-input-synaptics, a default configuration file is located at /usr/share/X11/xorg.conf.d/70-synaptics.conf. Users can copy this file to /etc/X11/xorg.conf.d/ and edit it to configure the various driver options available. Refer to the synaptics(4) manual page for a complete list of available options. Machine-specific options can be discovered using #Synclient.

The following example file configures some common options, including vertical, horizontal and circular scrolling as well as tap-to-click:

Next to the traditional method of configuration, the Synaptics driver also supports on the fly configuration. This means that users can set certain options through a software application, these options are applied immediately without needing to restart Xorg. This is useful to test configuration options before you include them in the configuration file or a script. Note that on the fly configuration is not persistent and lasts only until the Xorg server exists.

To change these settings in Xfce:

To change these settings in Cinnamon:

It is possible to configure the way MATE handles the touchpad:

To prevent Mate settings daemon from overriding existing settings, do as follows:

Depending on your model, synaptic touchpads may have or lack capabilities. We can determine which capabilities your hardware supports by using xinput(1).

First, find the name of your touchpad:

You can now use xinput to find your touchpad's capabilities:

From left to right, this shows:

Use xinput list-props "SynPS/2 Synaptics TouchPad" to list all device properties. See synaptics(4) for full documentation of the Synaptics properties.

Synclient can configure every option available to the user as documented in synaptics(4). A full list of the current user settings can be brought up:

Every listed configuration option can be controlled through synclient, for example:

After you have successfully tried and tested your options through synclient, you can make these changes permanent by adding them to /etc/X11/xorg.conf.d/70-synaptics.conf.

The tool evtest can display pressure and placement on the touchpad in real-time, allowing further refinement of the default Synaptics settings. The evtest monitoring can be started with:

X denotes the touchpad's ID. It can be found by looking at the output of cat /proc/bus/input/devices.

evtest needs exclusive access to the device which means it cannot be run together with an X server instance. You can either kill the X server or run evtest from a different virtual terminal (e.g., by pressing Ctrl+Alt+F2).

The tool xorg-xev can display taps, clicks, pressure, placement and other measured parameters in real-time, allowing still further refinement of the default Synaptics settings. xev can be run in X and needs no specifics. using the -event parameter, it is possible to restrict the types of events that are reported.

Circular scrolling is a feature that Synaptics offers which closely resembles the behaviour of iPods. Instead of (or additional to) scrolling horizontally or vertically, you can scroll circularly. Some users find this faster and more precise. To enable circular scrolling, add the following options to the touchpad device section of /etc/X11/xorg.conf.d/70-synaptics.conf:

The option CircScrollTrigger may be one of the following values, determining which edge circular scrolling should start:

Specifying something different from zero may be useful if you want to use circular scrolling in conjunction with horizontal and/or vertical scrolling. If you do so, the type of scrolling is determined by the edge you start from.

To scroll fast, draw small circles in the center of your touchpad. To scroll slowly and more precise, draw large circles.

It is possible to enable natural scrolling through Synaptics. Simply use negative values for VertScrollDelta and HorizScrollDelta like so:

You might want to turn the touchpad on and off with a simple button click or shortcut. This can be done by binding the following xinput-based script:

Alternatively, synclient can be used to toggle the touchpad. However, it can only turn off touch events but not physical clickpad button usage:

First of all you should test if it works properly for your touchpad and if the settings are accurate. Enable palm detection with

Then test the typing. You can tweak the detection by setting the minimum width for the touch to be considered a palm, for example:

And you can tweak the minimum pressure required for the touch to be considered a palm, for example:

Once you have found the correct settings, you can add them to your config file:

syndaemon(1) monitors keyboard activity and disables the touchpad while typing. It has several options to control when the disabling occurs. View them with

For example, to disable tapping and scrolling for 0.5 seconds after each keypress (ignoring modifier keys like Ctrl), use

Once you have determined the options you like, you should use your login manager or xinitrc to have it run automatically when X starts. The -d option will make it start in the background as a daemon.

With the assistance of udev, it is possible to automatically disable the touchpad if an external mouse has been plugged in. To achieve this, use one of the following rules.

This is a basic rule generally for non-"desktop environment" sessions:

If the touchpad is always deactivated at startup, even when no mouse is plugged in, try adding the following criteria between the KERNEL and ACTION parameters above:

This article or section is out of date.

GDM stores the Xauthority files in /var/run/gdm in a randomly-named directory. You should find your actual path to the Xauthority file which can be done using ps ax. For some reason, multiple authority files may appear for a user, so a rule like this will be necessary:

Furthermore, you should validate that your udev script is running properly. You can check for the conditions by running udevadm monitor -p with root privileges.

syndaemon whether started by the user or the desktop environment can conflict with synclient and will need to be disabled. A rule like this will be needed:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

A touchpad-state-gitAUR package created around the udev rules in #With syndaemon running is available. It includes a udev rule and script:

GNOME users can install the GNOME shell extension Touchpad Indicator, change Switch Method to Synclient and enable Automatically switch Touchpad On/Off in its preferences.

If using Plasma, the plasma-desktop package can be used to manage the touchpad.

The factual accuracy of this article or section is disputed.

For an environment where multiple users are present, a slightly different approach is needed to detect the current users X environment. This script will help achieving this:

Update the TRACKPAD_NAME variable for your system configuration. Run find /sys/class/input/ -name mouse* -exec udevadm info -a {} \; | grep 'ATTRS{name}' to get a list of useful mice-names. Choose the one for your trackpad.

Then have udev run this script when USB mices are plugged in or out, with these udev rules:

Ever more laptops have a special kind of touchpad which has a single mouse button as part of the tracking plate, instead of external buttons. For example, the 2015 Dell XPS 13, HP series 4500 ProBooks, ThinkPad X220 and X1 ThinkPad series have this kind of a touchpad. By default, the whole button area is detected as a left button, so right and middle-click functions and click + drag will not work. It is possible to define two and three finger clicks as right and middle button clicks, and/or to define parts of the click pad surface as right and middle buttons. Note that although the driver registers multiple touches, it does not track individual fingers (as of version 1.7.1) which results in confusing behavior when using physical buttons of a clickpad for drag-and-drop and other gestures: you have to click with two or three fingers but then only move one of them while holding the button down with another. You can look into the xf86-input-mtrackAUR driver for better multitouch support.

Some desktop environments (KDE and GNOME at least) define sane and useful default configurations for clickpads, providing a right button at the bottom right of the pad, recognising two and three-finger clicks anywhere on the pad as right and middle clicks, and providing configuration options to define two and three-finger taps as right and middle clicks. If your desktop does not do this, or if you want more control, you can modify the touchpad section in /etc/X11/xorg.conf.d/70-synaptics.conf (or better, of your custom synaptics configuration file prefixed with a higher number). For example:

The format for the SoftButtonAreas option is (from synaptics(4)):

The above SoftButtonAreas option is commonly found in documentation or synaptics packages, and it defines the right half of the bottom 18% of the touchpad as a right button. There is no middle button defined. If you want to define a middle button remember one key piece of information from the manual; edge set to 0 extends to infinity in that direction.

In the following example the right button will occupy the rightmost 40% of the button area and the middle button 20% of it in the center. The leftmost 40% remains as a left button (as does the rest of the clickpad):

You can use synclient to check the soft button areas:

If your buttons are not working, soft button areas are not changing, ensure you do not have a synaptics configuration file distributed by a package which is overriding your custom settings (i.e. some AUR packages distribute configurations prefixed with very high numbers).

These settings cannot be modified on the fly with synclient, however, xinput works:

You cannot use percentages with this command, so look at /var/log/Xorg.0.log to figure out the touchpad x and y-axis ranges.

In some cases, for example Toshiba Satellite P50, everything work out of the box except often your click are seen as mouse movement and the cursor will jump away just before registering the click. This can be easily solved running

take the BottomEdge value and subtract a the wanted height of your button, then temporary apply with

when a good value has been found make it a fixed correction with

Occasionally touchpads will fail to work when the computer resumes from sleep or hibernation. This can often be corrected without rebooting by

If you are using a laptop computer and your touchpad does not work after switching the laptop's lid, you can just change your power management policy: when closing the lid, 'shutdown the screen' instead of 'suspend'(or 'hibernate'). This is useful for some laptops.

MATE will by default overwrite various options for your touchpad. This includes configurable features for which there is no graphical configuration within MATE's system control panel. This may cause it to appear that /etc/X11/xorg.conf.d/70-synaptics.conf is not applied. Follow #MATE to prevent this behavior.

Due to the way Synaptics is currently set-up, 2 instances of the Synaptics module are loaded. We can recognize this situation by opening the xorg log file (/var/log/Xorg.0.log) and noticing this:

Notice how 2 differently named instances of the module are being loaded. In some cases, this causes the touchpad to become nonfunctional.

We can prevent this double loading by adding MatchDevicePath "/dev/input/event*" to our /etc/X11/xorg.conf.d/70-synaptics.conf file:

Restart X and check xorg logs again, the error should be gone and the touchpad should be functional.

related bugreport: FS#20830

related forum topics:

This can be caused by a number of issues;

There also seems to be a problem with laptops which have both a touchscreen & a touchpad, such as the Dell XPS 12 or Dell XPS 13. To fix this, you can blacklist the i2c_hid driver, this does have the side-effect of disabling the touchscreen though.

This seems to be a known problem. Also see this thread.

Post kernel 3.15, having the module blacklisted may cause touchpad to stop working completely. Removing the blacklist should allow this to start working with limited functionality, see FS#40921.

In some cases, Synaptics touchpads only work partially. Features like two-finger scrolling or two-finger middle-click do not work even if properly enabled. This is probably related to the touchpad is not working problem mentioned above. Fix is the same, prevent double module loading.

If preventing the module from loading twice does not solve your issue, try commenting out the toggle MatchIsTouchpad (which is now included by default in the Synaptics configuration).

See https://unix.stackexchange.com/questions/28736/what-does-the-i8042-nomux-1-kernel-option-do-during-booting-of-ubuntu.

Some users have their cursor inexplicably jump around the screen. There currently no patch for this, but the developers are aware of the problem and are working on it.

Another possibility is that you are experiencing IRQ losses related to the i8042 controller (this device handles the keyboard and the touchpad of many laptops), so you have two possibilities here:

If that is the case, you can use this command to display information about your input devices:

Search for an input device which has the name "SynPS/2 Synaptics TouchPad". The "Handlers" section of the output specifies what device you need to specify.

In this case, the Handlers are mouse0 and event1, so /dev/input/mouse0 would be used.

This article or section needs expansion.

You can enable/disable some special events that Firefox handles upon tapping or scrolling certain parts of your touchpad by editing the settings of those actions. Type about:config in your Firefox address bar. To alter options, double-click on the line in question.

Horizontal scrolling will now by default scroll through pages and not through your history. To reenable Mac-style forward/backward with two-finger swiping, edit:

You may encounter accidental forwards/backwards while scrolling vertically. To change Firefox's sensitivity to horizontal swipes, edit:

The optimum value will depend on your touchpad and how you use it, try starting with 10. A negative value will reverse the swipe directions.

These problems seem to be occurring on several models of LG laptops. Symptoms include: when pressing Mouse Button 1, Synaptics interprets it as ScrollUP and a regular button 1 click; same goes for button 2.

The scrolling issue can be resolved by entering in xorg.conf:

Apparently, when trying to compile this against the latest version of Synaptics it fails. The solution to this is using the Git repository for Synaptics [5].

To build the package after downloading the tarball and unpacking it, execute:

First, make sure your section describing the external mouse contains this line (or that the line looks like this):

If the "Device" line is different, change it to the above and try to restart X. If this does not solve your problem, make your touchpad the CorePointer in the "Server Layout" section:

and make your external device "SendCoreEvents":

Finally, add this to your external device's section:

If all of the above does not work for you, please check relevant bug trackers for possible bugs, or go through the forums to see if anyone has found a better solution.

Many drivers include a firmware that is loaded into flash memory when the computer boots. This firmware is not necessarily cleared upon shutdown, and is not always compatible with Linux drivers. The only way to clear the flash memory is to shutdown completely rather than using reboot. It is generally considered best practice to never use reboot when switching between operating systems.

Certain touchpads (Elantech in particular) will fail to be recognized as a device of any sort after a standard shutdown. There are multiple possible solutions to this problem:

Newer Thinkpads do not have physical buttons for their Trackpoint anymore and instead use the upper area of the Clickpad for buttons (Left, Middle, Right). Apart from the ergonomic viewpoint this works quite well with current Xorg. Unfortunately, mouse wheel emulation using the middle button is not supported yet. Install xf86-input-evdev-trackpointAUR for a patched and properly configured version if you intend to use the Trackpoint.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/X11/xorg.conf.d/70-synaptics.conf
```

Example 2 (unknown):
```unknown
/etc/X11/xorg.conf.d/
```

Example 3 (unknown):
```unknown
/etc/X11/xorg.conf.d/70-synaptics.conf
```

Example 4 (unknown):
```unknown
Section "InputClass"
    Identifier "touchpad"
    Driver "synaptics"
    MatchIsTouchpad "on"
        Option "TapButton1" "1"
        Option "TapButton2" "3"
        Option "TapButton3" "2"
        Option "VertEdgeScroll" "on"
        Option "VertTwoFingerScroll" "on"
        Option "HorizEdgeScroll" "on"
        Option "HorizTwoFingerScroll" "on"
        Option "CircularScrolling" "on"
        Option "CircScrollTrigger" "2"
        Option "EmulateTwoFingerMinZ" "40"
        Option "EmulateTwoFingerMinW" "8"
        Option "CoastingSpeed" "0"
        Option "FingerLow" "30"
        Option "FingerHigh" "50"
        Option "MaxTapTime" "125"
        ...
EndSection
```

---

## Swap

**URL:** https://wiki.archlinux.org/title/Swap_space

**Contents:**
- Swap space
- Swap partition
  - Enabling at boot
  - Disabling swap
- Swap file
  - Swap file creation
  - Swap file removal
- Swap encryption
- Performance
  - Swappiness

This page provides an introduction to swap space and paging on GNU/Linux. It covers creation and activation of swap partitions and swap files.

From All about Linux swap space:

Support for swap is provided by the Linux kernel and user-space utilities from the util-linux package.

Swap space can take the form of a disk partition or a file. Users may create a swap space during installation or at any later time as desired. Swap space can be used for two purposes, to extend the virtual memory beyond the installed physical memory (RAM), and also for suspend-to-disk support.

Whether or not it is beneficial to extend the virtual memory with swap depends on the amount of installed physical memory. If the amount of physical memory is less than the amount of memory required to run all the desired programs, then it may be beneficial to enable swap. This avoids out of memory conditions, where the Linux kernel OOM killer mechanism will automatically attempt to free up memory by killing processes. To increase the amount of virtual memory to the required amount, add the necessary difference (or more) as swap space.

The biggest drawback of using swap when running out of memory is its lower performance, see section #Performance. Hence, enabling swap is a matter of personal preference: some prefer programs to be killed over enabling swap and others prefer enabling swap and slower system when the physical memory is exhausted.

To check swap status, use:

Or to show physical memory as well as swap usage:

A swap partition can be created with most GNU/Linux partitioning tools. Swap partitions are designated by the partition type GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F on GPT (8200 type for gdisk, swap type for fdisk) and type ID 82 on MBR.

To set up a partition as Linux swap area, the mkswap(8) command is used. For example:

To enable the device for paging:

See swapon(8) for the options syntax.

To enable the swap partition at boot time, either:

See fstab for the file syntax, and systemd#systemd.mount - mounting.

To deactivate specific swap space:

Alternatively use the -a switch to deactivate all swap space.

Since swap is managed by systemd, it will be activated again on the next system startup. To disable the automatic activation of detected swap space permanently, run systemctl --type swap to find the responsible .swap unit and mask it.

As an alternative to creating an entire partition, a swap file offers the ability to vary its size on-the-fly, and is more easily removed altogether. This may be especially desirable if disk space is at a premium (e.g. a modestly-sized SSD).

Use mkswap(8) to create a swap file the size of your choosing (see Partitioning#Swap for advice). For example, creating a 4 GiB swap file:

Activate the swap file:

Finally, edit the fstab configuration to add an entry for the swap file:

As an alternative to fstab, a swap unit can be created (see systemd.swap(5)):

Perform a daemon-reload and enable swapfile.swap.

For additional information, see fstab#Usage.

To remove a swap file, it must be turned off first and then can be removed:

Finally, remove the relevant entry from /etc/fstab.

See dm-crypt/Swap encryption.

Swap operations are usually significantly slower than directly accessing data in RAM. However, disabling swap entirely to improve performance can sometimes lead to a degradation. If there is not enough physical memory available to hold everything, swapping out nothing leaves less memory available for file system caches, causing more frequent and costly disk usage.

Swap values can be adjusted to help performance:

When memory usage reaches a certain threshold, the kernel starts looking at active memory and seeing what it can free up. File data can be written out to the file system (if changed), unloaded and re-loaded later; other data must be written to swap before it can be unloaded.

The swappiness sysctl parameter represents the kernel's preference for writing to swap instead of files. It can have a value between 0 and 200 (max 100 if Linux < 5.8); the default value is 60. A low value causes the kernel to prefer freeing up open files, a high value causes the kernel to try to use swap space, and a value of 100 means IO cost is assumed to be equal.

To check the current swappiness value:

Alternatively, the file /proc/sys/vm/swappiness can be read in order to obtain the raw integer value.

To temporarily set the swappiness value:

To set the swappiness value permanently, create a sysctl.d(5) configuration file. For example:

To have the boot loader set swappiness when loading the kernel, add a kernel parameter, e.g. sysctl.vm.swappiness=35.

Reasons for choosing a different swappiness can include:

Another sysctl parameter that affects swap performance is vm.vfs_cache_pressure, which controls the tendency of the kernel to reclaim the memory which is used for caching of VFS caches, versus pagecache and swap. Increasing this value increases the rate at which VFS caches are reclaimed. For more information on what it does, see the Linux kernel documentation.

The default value is 100, which states that filesystem cache is about as important as the other caches, so they should be reclaimed at about an equal weight. On desktops it has been argued that filesystem cache is more important than the other caches because filesystem browsing times affects operation latency (perceived responsiveness) more than the other caches, resulting a suggested value of 50. On the other hand, a higher value has been suggested when the VFS cache holds metadata on many small files that are not touched again. For more information on tuning this parameter, see OpenSUSE tuning guide (which recommends experimenting and checking the types of caches via slaptop).

If you have more than one swap file or swap partition you should consider assigning a priority value (0 to 32767) for each swap area. The system will use swap areas of higher priority before using swap areas of lower priority. For example, if you have a faster disk and a slower disk, assign a higher priority to the swap area located on the fastest device. Priorities can be assigned in fstab via the pri parameter:

Or via the --priority parameter of swapon:

If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them.

There is no necessity to use RAID for swap performance reasons. The kernel itself can stripe swapping on several devices, if you just give them the same priority in the /etc/fstab file. Refer to The Software-RAID HOWTO for details.

See Solid state drive#swap.

See Improving performance#Swap on zram or zswap.

If you only need swap as a hibernation image storage space, then you can use zswap and disable its writeback so that there are no disk writes from regular swap usage. See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation.

**Examples:**

Example 1 (unknown):
```unknown
$ swapon --show
```

Example 2 (unknown):
```unknown
0657FD6D-A4AB-43C4-84E5-0933C84B4F4F
```

Example 3 (unknown):
```unknown
# mkswap /dev/sdxy
```

Example 4 (unknown):
```unknown
# swapon /dev/sdxy
```

---

## archinstall

**URL:** https://wiki.archlinux.org/title/Archinstall

**Contents:**
- Running the installer
  - Profiles
- See also

archinstall is a helper library which automates the installation of Arch Linux. It is packaged with different pre-configured installers, such as a "guided" installer.

This document does not discuss use of archinstall as a Python library; see the official documentation for that.

First, acquire and boot the live medium as described in Installation guide#Pre-installation.

It is possible to update archinstall before running if a new release was made after the monthly installation medium was created:

In this case, a partial upgrade is usually fine to run on the live ISO, although a complete update is preferable if system memory allows for adjusting the size of the root file system.

The archinstall package is part of the live medium and can be run directly:

The guided installer will perform or ask user input for multiple steps, described in the official documentation.

Additional packages can be installed by specifying them after the Write additional packages to install prompt.

Once the installation is complete, green text should appear saying that it is safe to reboot, which is also the command you use to reboot.

archinstall includes profiles, or sets of packages and pre-configured options which can be installed next to the base system.

**Examples:**

Example 1 (unknown):
```unknown
/var/log/archinstall/install.log
```

Example 2 (unknown):
```unknown
# pacman -Sy archinstall
```

Example 3 (unknown):
```unknown
# archinstall
```

---

## incron

**URL:** https://wiki.archlinux.org/title/Incron

**Contents:**
- Installation
- Activation and autostart
- Configuration
  - Using incrontab
  - Incrontab format
    - Mask types
    - Custom Mask Types

incron is an "inotify cron" system. It consists of a daemon and a table manipulator. You can use it a similar way as the regular cron. The difference is that the inotify cron handles filesystem events rather than time periods.

Install the incron package.

After installation, the daemon will not be enabled by default. You can enable incrond.service.

Incrontabs should never be edited directly; instead, users should use the incrontab program to work with their incrontabs.

To view their incrontabs, users should issue the command:

To edit their incrontabs, they should use:

To remove their incrontabs, they may use:

To reload incrond, use:

To edit another user's incrontab, isue the following command:

Each row in an incrontab file is a table that the dameon runs when an event happens to a certain directory or file.

The basic format for an incrontab is:

incrontab uses mask types to specify which file system event to monitor for. For more options see inotify(7)

To trigger a command if a file is accessed or read:

To trigger a command if metadata of a file change (e.g. timestamps, permissons):

To trigger a command if a file opened for writing is closed:

To trigger a command if a file or directory not opened for writing is closed:

To trigger a command if a file or directory is created in a watched directory:

To trigger a command if a file or directory is deleted from a watched directory:

To trigger a command if a watched file or directory is deleted (or moved to a different filesystem):

To trigger a command if a file was modified:

To trigger a command if a watched file or directory is moved within the filesystem:

To trigger a command if a file or directory is moved out of the watched directory:

To trigger a command if a file or directory is moved to the watched directory:

To trigger a command if a watched file or directory is opened:

Incrond provides additional custom event types to modify its monitoring behavior.

For instance, to pause monitoring an event until the current one is completely handled, add loopable=true to the event list, eg:

An event with the loopable event enabled will not fire again until the associated command exits.

See incrontab(5) for the complete list of custom mask types.

**Examples:**

Example 1 (unknown):
```unknown
incrond.service
```

Example 2 (unknown):
```unknown
$ incrontab -l
```

Example 3 (unknown):
```unknown
$ incrontab -e
```

Example 4 (unknown):
```unknown
$ incrontab -r
```

---

## NFS

**URL:** https://wiki.archlinux.org/title/NFS

**Contents:**
- Installation
- Server configuration
  - Custom export root
  - Starting the server
  - Restricting NFS to interfaces/IPs
  - Firewall configuration
- Client configuration
  - Manual mounting
  - Mount using /etc/fstab
  - Mount using /etc/fstab with systemd

The NFS FAQ lists file systems well tested and details limitations regarding FAT32.

Both client and server only require the installation of the nfs-utils package.

It is highly recommended to use a time synchronization daemon to keep client/server clocks in sync. Without accurate clocks on all nodes, NFS can introduce unwanted delays.

Global configuration options are set in /etc/nfs.conf. Users of simple configurations should not need to edit this file.

The NFS server needs a list of directories to share, in the form of exports (see exports(5) for details) which one must define in /etc/exports or /etc/exports.d/*.exports. By default, the directories are exported with their paths as-is; for example:

The above will make the directory /data/music mountable as MyServer:/data/music for both NFSv3 and NFSv4.

Shares may be relative to the so-called NFS root. A good security practice is to define a NFS root in a discrete directory tree which will keep users limited to that mount point. Bind mounts are used to link the share mount point to the actual directory elsewhere on the filesystem. An NFS root used to be mandatory for NFSv4 in the past; it is now optional (as of kernel 2.6.33 and nfs-utils 1.2.2, which implement a virtual root).

Consider this following example wherein:

To make the bind mount persistent across reboots, add it to fstab:

Add directories to be shared and limit them to a range of addresses via a CIDR or hostname(s) of client machines that will be allowed to mount them in /etc/exports, e.g.:

When using NFSv4, the option fsid=root or fsid=0 denotes the "root" export; if such an export is present, then all other directories must be below it. The rootdir option in the /etc/nfs.conf file has no effect on this. The default behavior, when there is no fsid=0 export, is to behave the same way as in NFSv3.

In the above example, because /srv/nfs is designated as the root, the export /srv/nfs/music is now mountable as MyServer:/music via NFSv4 – note that the root prefix is omitted.

It should be noted that modifying /etc/exports while the server is running will require a re-export for changes to take effect:

To view the current loaded exports state in more detail, use:

For more information about all available options see exports(5).

Users of protocol version 4 exports will probably want to mask at a minimum both rpcbind.service and rpcbind.socket to prevent superfluous services from running. See FS#76453. Additionally, consider masking nfs-server.service which is pulled in for some reason as well.

By default, starting nfs-server.service will listen for connections on all network interfaces, regardless of /etc/exports. This can be changed by defining which IPs and/or hostnames to listen on.

Restart nfs-server.service to apply the changes immediately.

To enable access of NFSv4-servers through a firewall, TCP port 2049 must be opened for incoming connections. (NFSv4 uses a static port number; it does not use any auxiliary services such as mountd or portmapper.)

To enable access of NFSv3 servers, you will additionally need to open TCP/UDP port 111 for the portmapper (rpcbind), as well as the MOUNT (rpc.mountd) port. By default, rpc.mountd selects a port dynamically, so if you're behind a firewall you will want to edit /etc/nfs.conf to set a static port instead. Use rpcinfo -p to examine the exact ports in use on the NFSv3 server:

Users intending to use NFS4 with Kerberos need to start and enable nfs-client.target.

For NFSv3 use this command to show the server's exported file systems:

For NFSv4 mount the root NFS directory and look around for available mounts:

Then mount omitting the server's NFS export root:

If mount fails try including the server's export root (required for Debian/RHEL/SLES, some distributions need -t nfs4 instead of -t nfs):

Using fstab is useful for a server which is always on, and the NFS shares are available whenever the client boots up. Edit /etc/fstab file, and add an appropriate line reflecting the setup. Again, the server's NFS export root is omitted.

Some additional mount options to consider:

Another method is using the x-systemd.automount option which mounts the filesystem upon access:

To make systemd aware of the changes to fstab, reload systemd and restart remote-fs.target [1].

The factual accuracy of this article or section is disputed.

Create a new .mount file inside /etc/systemd/system, e.g. mnt-home.mount. See systemd.mount(5) for details.

Where= path to mount the share

Options= share mounting options

To use mnt-home.mount, start the unit and enable it to run on system boot.

To automatically mount a share, one may use the following automount unit:

Disable/stop the mnt-home.mount unit, and enable/start mnt-home.automount to automount the share when the mount path is being accessed.

Using autofs is useful when multiple machines want to connect via NFS; they could both be clients as well as servers. The reason this method is preferable over the earlier one is that if the server is switched off, the client will not throw errors about being unable to find NFS shares. See autofs#NFS network mounts for details.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

This article or section needs expansion.

The NFSv4 protocol represents the local system's UID and GID values on the wire as strings of the form user@domain. The process of translating from UID to string and string to UID is referred to as ID mapping.

Display the system's effective NFSv4 domain name on stdout.

Edit to match up the Domain on the server and/or client:

These steps are only needed if the server and client have different user/group names. Changes are only done in the clients config file.

Only in the client configuration. Local user/group name to be used when a mapping cannot be completed:

This article or section is out of date.

When using NFS on a network with a significant number of clients one may increase the default NFS threads from 8 to 16 or even a higher, depending on the server/network requirements:

It may be necessary to tune the rsize and wsize mount options to meet the requirements of the network configuration.

In recent linux kernels (>2.6.18) the size of I/O operations allowed by the NFS server (default max block size) varies depending on RAM size, with a maximum of 1M (1048576 bytes), the max block size of the server will be used even if nfs clients requires bigger rsize and wsize. See https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/5.8_technical_notes/known_issues-kernel It is possible to change the default max block size allowed by the server by writing to the /proc/fs/nfsd/max_block_size before starting nfsd. For example, the following command restores the previous default iosize of 32k:

To make the change permanent, create a systemd-tmpfile:

To mount with the increased rsize and wsize mount options:

Furthermore, despite the violation of NFS protocol, setting async instead of sync or sync,no_wdelay may potentially achieve a significant performance gain especially on spinning disks. Configure exports with this option and then execute exportfs -arv to apply.

This trick is useful for NFS-shares on a wireless network and/or on a network that may be unreliable. If the NFS host becomes unreachable, the NFS share will be unmounted to hopefully prevent system hangs when using the hard mount option [4].

Make sure that the NFS mount points are correctly indicated in fstab:

Create the auto_share script that will be used by cron or systemd/Timers to use ICMP ping to check if the NFS host is reachable:

Make sure the script is executable.

Next check configure the script to run every X, in the examples below this is every minute.

Finally, enable and start auto_share.timer.

NetworkManager can also be configured to run a script on network status change.

The easiest method for mount shares on network status change is to symlink the auto_share script:

However, in that particular case unmounting will happen only after the network connection has already been disabled, which is unclean and may result in effects like freezing of KDE Plasma applets.

The following script safely unmounts the NFS shares before the relevant network connection is disabled by listening for the down, pre-down and vpn-pre-down events, make sure the script is executable:

Create a symlink inside /etc/NetworkManager/dispatcher.d/pre-down to catch the pre-down events:

NFS traffic can be encrypted using TLS as of Linux 6.5 using the xprtsec=tls mount option. To begin, install the ktls-utilsAUR package on the client and server, and follow the below configuration steps for each.

Create a private key and obtain a certificate containing your server's DNS name (see Transport Layer Security#Obtaining a certificate for more detail). These files do not need to be added to the system's trust store.

Edit /etc/tlshd.conf to use these files, using your own values for x509.certificate and x509.private_key:

Now start and enable tlshd.service.

This article or section needs expansion.

Add the server's TLS certificate generated in the previous step to the system's trust store (see Transport Layer Security#Add a certificate to a trust store for more detail).

Start and enable tlshd.service.

Now you should be able to mount the server using the server's DNS name:

Checking journalctl on the client should show that the TLS handshake was successful:

There is a dedicated article NFS/Troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
/etc/exports
```

Example 2 (unknown):
```unknown
/etc/nfs.conf
```

Example 3 (unknown):
```unknown
/etc/exports
```

Example 4 (unknown):
```unknown
/etc/exports.d/*.exports
```

---

## Official repositories

**URL:** https://wiki.archlinux.org/title/Official_repositories

**Contents:**
- Stable repositories
  - core
  - extra
  - multilib
    - Enabling multilib
    - Disabling multilib
- Testing repositories
  - core-testing
  - extra-testing
  - multilib-testing

A software repository is a storage location from which software packages are retrieved for installation.

Arch Linux official repositories contain essential and popular software, readily accessible via pacman. They are maintained by package maintainers.

Packages in the official repositories are constantly upgraded: when a package is upgraded, its old version is removed from the repository. There are no major Arch releases: each package is upgraded as new versions become available from upstream sources. Each repository is always coherent, i.e. the packages that it hosts always have reciprocally compatible versions.

This repository can be found in .../core/os/ on your favorite mirror.

core contains packages for:

as well as dependencies of the above (not necessarily makedepends) and the base meta package.

core has fairly strict quality requirements. Developers/users need to signoff on updates before package updates are accepted. For packages with low usage, a reasonable exposure is enough: informing people about update, requesting signoffs, keeping in core-testing up to a week depending on the severity of the change, lack of outstanding bug reports, along with the implicit signoff of the package maintainer.

This repository can be found in .../extra/os/ on your favorite mirror.

extra contains all packages that do not fit in core. This repository is jointly maintained by the Package Maintainers and Arch Developers. Examples: Xorg, window managers, web browsers, media players, tools for working with languages such as Python and Ruby, and a lot more.

This repository can be found in .../multilib/os/ on your favorite mirror.

multilib contains 32-bit software and libraries that can be used to run and build 32-bit applications on 64-bit installs (e.g. steam, etc).

With the multilib repository enabled, the 32-bit compatible libraries are located under /usr/lib32/.

To enable multilib repository, uncomment the [multilib] section in /etc/pacman.conf:

Then upgrade the system and install the desired multilib packages.

Execute the following command to remove all packages that were installed from multilib:

If you have conflicts with gcc-libs reinstall the gcc-libs package and the dependencies of the base-devel package (see Pacman/Tips and tricks#Dependencies of a package).

Comment out the [multilib] section in /etc/pacman.conf:

Then upgrade the system.

The intended purpose of the testing repositories is to provide a staging area for packages to be placed prior to acceptance into the main repositories. Package maintainers (and general users) can then access these testing packages to make sure that there are no problems integrating the new package. Once a package has been tested and no errors are found, the package can then be moved to the primary repositories.

Not all packages need to go through this testing process. New packages go into a testing repository if:

The testing repositories are also usually used for new releases of large collections of packages such as GNOME and KDE.

This repository can be found in .../core-testing/os/ on your favorite mirror.

core-testing contains packages that are candidates for the core repository.

core-testing is the only repository that can have name collisions with any of the other official repositories. If enabled, it has to be the first repository listed in your /etc/pacman.conf file.

This repository is similar to the core-testing repository, but for packages that are candidates for the extra repository.

This repository is similar to the core-testing repository, but for packages that are candidates for the multilib repository.

This repository contains testing packages for pre-releases (Alpha, Beta, RC) as well as stable versions of the GNOME desktop environment, prior to their transition to the main extra-testing repository.

To enable it, add the following lines to /etc/pacman.conf:

The gnome-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Please report packaging related bugs in Arch's GitLab, while anything else should be reported upstream to GNOME GitLab.

For additional assistance and information regarding this repository, please join the Matrix Group.

This repository contains the latest beta or Release Candidate of KDE Plasma and Applications.

To enable it, add the following lines to /etc/pacman.conf:

The kde-unstable entry should be at the top in the list of repositories (i.e., above the enabled core-testing entry; see warnings above).

Make sure you make bug reports if you find any problems.

If you enabled testing repositories, but later on decided to disable them, you should:

The second item is optional, but keep it in mind if you notice any problems.

This repository contains broken packages and is used solely by developers during rebuilds of many packages at once. In order to rebuild packages that depend on, for example, a new shared library, the shared library itself must first be built and uploaded to the staging repositories to be made available to other developers. As soon as all dependent packages are rebuilt, the group of packages is then moved to the testing or the main repositories, whichever is more appropriate.

See the announcement of the introduction of the staging repositories for more historical details.

Most of the repository splits are for historical reasons. Originally, when Arch Linux was used by very few users, there was only one repository known as official (now core). At the time, official basically contained Judd Vinet's preferred applications. It was designed to contain one of each "type" of program — one DE, one major browser, etc.

There were users back then that did not like Judd's selection, so since the Arch build system is so easy to use, they created packages of their own. These packages went into a repository called unofficial, and were maintained by developers other than Judd. Eventually, the two repositories were both considered equally supported by the developers, so the names official and unofficial no longer reflected their true purpose. They were subsequently renamed to current and extra sometime near the release version 0.5.

Shortly after the 2007.8.1 release, current was renamed core in order to prevent confusion over what exactly it contains. The repositories are now more or less equal in the eyes of the developers and the community, but core does have some differences. The main distinction is that packages used for Installation CDs and release snapshots are taken only from core. This repository still gives a complete Linux system, though it may not be the Linux system you want.

Some time around 0.5/0.6, there were a lot of packages that the developers did not want to maintain. Jason Chu set up the "Trusted User Repositories", which were unofficial repositories in which trusted users could place packages they had created. There was a staging repository where packages could be promoted into the official repositories by one of the Arch Linux developers, but other than this, the developers and trusted users were more or less distinct.

This worked for a while, but not when trusted users got bored with their repositories, and not when other users wanted to share their own packages. This led to the development of the AUR. The Trusted Users were conglomerated into a more closely knit group, and they now collectively maintained the community repository. The TUs were still a separate group from the Arch Linux developers, and there was not a lot of communication between them. However, popular packages were still promoted from community to extra on occasion. The AUR also allows all users to submit PKGBUILDs.

After a kernel in core broke many user systems, the "core signoff policy" was introduced. Since then, all package updates for core need to go through the core-testing repository first, and only after multiple signoffs from other developers or people on the Arch Testing Team are then allowed to move. Over time, it was noticed that various core packages had low usage, and user signoffs or even lack of bug reports became informally accepted as criteria to accept such packages.

In late 2009/the beginning of 2010, with the advent of some new filesystems and the desire to support them during installation, along with the realization that core was never clearly defined (just "important packages, handpicked by developers"), the repository received a more accurate description.

This article or section needs expansion.

Starting in 2021, and finalized in late 2023, the "Trusted Users" were renamed to "Package Maintainers".

In 2023 after years of prior work the distribution migrated their back-end services to git and in the same run also switched to a new repository layout. In the new layout extra would contain all packages that were previously in community and the testing repositories were split from testing to core-testing and extra-testing, community-testing was removed entirely. From that point on the Package Maintainers were also able to push new packages to extra.

**Examples:**

Example 1 (unknown):
```unknown
.../core/os/
```

Example 2 (unknown):
```unknown
.../extra/os/
```

Example 3 (unknown):
```unknown
.../multilib/os/
```

Example 4 (unknown):
```unknown
/usr/lib32/
```

---

## pacman

**URL:** https://wiki.archlinux.org/title/Uninstall

**Contents:**
- Usage
  - Installing packages
    - Installing specific packages
      - Virtual packages
    - Installing package groups
  - Removing packages
  - Upgrading packages
  - Querying package databases
    - Pactree
    - Database structure

The pacman package manager is one of the major distinguishing features of Arch Linux. It combines a simple binary package format with an easy-to-use Arch build system. The goal of pacman is to make it possible to easily manage packages, whether they are from the official repositories or the user's own builds.

Pacman keeps the system up-to-date by synchronizing package lists with the master server. This server/client model also allows the user to download/install packages with a simple command, complete with all required dependencies.

Pacman is written in the C programming language and uses the bsdtar(1) tar format for packaging.

What follows is just a small sample of the operations that pacman can perform. To read more examples, refer to pacman(8).

A package is an archive containing:

Arch's package manager pacman can install, update, and remove those packages. Using packages instead of compiling and installing programs yourself has various benefits:

To install a single package or list of packages, including dependencies, issue the following command:

To install a list of packages with regex (see this forum thread):

Sometimes there are multiple versions of a package in different repositories (e.g. extra and extra-testing). To install the version from the extra repository in this example, the repository needs to be defined in front of the package name:

To install a number of packages sharing similar patterns in their names, one can use curly brace expansion. For example:

This can be expanded to however many levels needed:

A virtual package is a special package which does not exist by itself, but is provided by one or more other packages. Virtual packages allow other packages to not name a specific package as a dependency, in case there are several candidates. Virtual packages cannot be installed by their name, instead they become installed in your system when you have installed a package providing the virtual package. An example is the dbus-units package.

Some packages belong to a group of packages that can all be installed simultaneously. For example, issuing the command:

will prompt you to select the packages from the gnome group that you wish to install.

Sometimes a package group will contain a large amount of packages, and there may be only a few that you do or do not want to install. Instead of having to enter all the numbers except the ones you do not want, it is sometimes more convenient to select or exclude packages or ranges of packages with the following syntax:

which will select packages 1 through 10 and 15 for installation, or:

which will select all packages except 5 through 8 and 2 for installation.

To see what packages belong to the gnome group, run:

Also visit https://archlinux.org/groups/ to see what package groups are available.

To remove a single package, leaving all of its dependencies installed:

To remove a package and its dependencies which are not required by any other installed package:

The above may sometimes refuse to run when removing a group which contains otherwise needed packages. In this case try:

To remove a package, its dependencies and all the packages that depend on the target package:

To remove a package, which is required by another package, without removing the dependent package:

Pacman saves important configuration files when removing certain applications and names them with the extension: .pacsave. To prevent the creation of these backup files use the -n option:

Pacman can update all packages on the system with just one command. This could take quite a while depending on how up-to-date the system is. The following command synchronizes the repository databases and updates the system's packages, excluding "local" packages that are not in the configured repositories:

Pacman queries the local package database with the -Q flag, the sync database with the -S flag and the files database with the -F flag. See pacman -Q --help, pacman -S --help and pacman -F --help for the respective suboptions of each flag.

Pacman can search for packages in the database, searching both in packages' names and descriptions:

Sometimes, -s's builtin ERE (Extended Regular Expressions) can cause a lot of unwanted results, so it has to be limited to match the package name only; not the description nor any other field:

To search for already installed packages:

To search for package file names in remote packages:

To display extensive information about a given package (e.g. its dependencies):

For locally installed packages:

Passing two -i flags will also display the list of backup files and their modification states:

To retrieve a list of the files installed by a package:

To retrieve a list of the files installed by a remote package:

To verify the presence of the files installed by a package:

Passing the k flag twice will perform a more thorough check.

To query the database to know which package a file in the file system belongs to:

To query the database to know which remote package a file belongs to:

To list all packages no longer required as dependencies (orphans):

To list all packages explicitly installed and not required as dependencies:

See pacman/Tips and tricks for more examples.

For advanced functionality, install pkgfile, which uses a separate database with all files and their associated packages.

To view the dependency tree of a package:

To view the dependent tree of a package, pass the reverse flag -r to pactree.

The pacman databases are normally located at /var/lib/pacman/sync. For each repository specified in /etc/pacman.conf, there will be a corresponding database file located there. Database files are gzipped tar archives containing one directory for each package, for example for the which package:

The desc file contains meta data such as the package description, dependencies, file size and MD5 hash.

Pacman stores its downloaded packages in /var/cache/pacman/pkg/ and does not remove the old or uninstalled versions automatically. This has some advantages:

However, it is necessary to deliberately clean up the cache periodically to prevent the directory to grow indefinitely in size.

The paccache(8) script, provided within the pacman-contrib package, deletes all cached versions of installed and uninstalled packages, except for the most recent three, by default:

Enable and start paccache.timer to discard unused packages weekly. You can configure the arguments for the service in /etc/conf.d/pacman-contrib, e.g with PACCACHE_ARGS='-k1' or PACCACHE_ARGS='-uk0' for the two examples below.

You can also define how many recent versions you want to keep. To retain only one past version use:

Add the -u/--uninstalled switch to limit the action of paccache to uninstalled packages. For example to remove all cached versions of uninstalled packages, use the following:

See paccache -h for more options.

Pacman also has some built-in options to clean the cache and the leftover database files from repositories which are no longer listed in the configuration file /etc/pacman.conf. However pacman does not offer the possibility to keep a number of past versions and is therefore more aggressive than paccache default options.

To remove all the cached packages that are not currently installed, and the unused sync databases, execute:

To remove all files from the cache, use the clean switch twice, this is the most aggressive approach and will leave nothing in the cache directory:

pkgcachecleanAUR and pacleanerAUR are two further alternatives to clean the cache.

Download a package without installing it:

Install a 'local' package that is not from a remote repository (e.g. the package is from the AUR):

To keep a copy of the local package in pacman's cache, use:

Install a 'remote' package (not from a repository stated in pacman's configuration files):

Pacman always lists packages to be installed or removed, and asks for permission before taking any action.

To get a list in a processable format, and to prevent the actions of -S, -U and -R, you can use -p, short for --print.

--print-format can be added to format this list in various ways. --print-format %n will return a list without package versions.

The pacman database organizes installed packages into two groups, according to installation reason:

When installing a package, it is possible to force its installation reason to dependency with:

The command is normally used because explicitly-installed packages may offer optional packages, usually for non-essential features for which the user has discretion.

When reinstalling a package, though, the current installation reason is preserved by default.

The list of explicitly-installed packages can be shown with pacman -Qe, while the complementary list of dependencies can be shown with pacman -Qd.

To change the installation reason of an already installed package, execute:

Use --asexplicit to do the opposite operation.

When successful, the workflow of a transaction follows five high-level steps plus pre/post transaction hooks:

Pacman settings are located in /etc/pacman.conf: this is the place where the user configures the program to work in the desired manner. In-depth information about the configuration file can be found in pacman.conf(5).

General options are in the [options] section. Read pacman.conf(5) or look in the default pacman.conf for information on what can be done here.

To see old and new versions of available packages, uncomment the "VerbosePkgLists" line in /etc/pacman.conf. The output of pacman -Syu will be like this:

The number of packages being downloaded in parallel (at the same time) are configured in /etc/pacman.conf with the ParallelDownloads option under [options]. The /etc/pacman.conf shipped with the pacman package sets it to 5. If the option is unset, packages will be downloaded sequentially.

To have a specific package skipped when upgrading the system, add this line in the [options] section:

For multiple packages use a space-separated list, or use additional IgnorePkg lines. Also, glob patterns can be used. If you want to skip packages just once, you can also use the --ignore option on the command-line - this time with a comma-separated list.

It will still be possible to upgrade the ignored packages using pacman -S: in this case pacman will remind you that the packages have been included in an IgnorePkg statement.

As with packages, skipping a whole package group is also possible:

All files listed with a NoUpgrade directive will never be touched during a package install/upgrade, and the new files will be installed with a .pacnew extension.

Multiple files can be specified like this:

To always skip installation of specific files or directories list them under NoExtract. For example, to avoid installing bash completion scripts, use:

Later rules override previous ones, and you can negate a rule by prepending !.

If you have several configuration files (e.g. main configuration and configuration with testing repository enabled) and would have to share options between configurations you may use Include option declared in the configuration files, e.g.:

where /path/to/common/settings file contains the same options for both configurations.

Pacman can run pre- and post-transaction hooks from the /usr/share/libalpm/hooks/ directory; more directories can be specified with the HookDir option in pacman.conf, which defaults to /etc/pacman.d/hooks. Hook file names must be suffixed with .hook. Pacman hooks are not interactive.

Pacman hooks are used, for example, in combination with systemd-sysusers and systemd-tmpfiles to automatically create system users and files during the installation of packages. For example, tomcat8 specifies that it wants a system user called tomcat8 and certain directories owned by this user. The pacman hooks systemd-sysusers.hook and systemd-tmpfiles.hook invoke systemd-sysusers and systemd-tmpfiles when pacman determines that tomcat8 contains files specifying users and tmp files.

For more information on alpm hooks, see alpm-hooks(5).

Besides the special [options] section, each other [section] in pacman.conf defines a package repository to be used. A repository is a logical collection of packages, which are physically stored on one or more servers: for this reason each server is called a mirror for the repository.

Repositories are distinguished between official and unofficial. The order of repositories in the configuration file matters; repositories listed first will take precedence over those listed later in the file when packages in two repositories have identical names, regardless of version number. In order to use a repository after adding it, you will need to upgrade the whole system first.

Each repository section allows defining the list of its mirrors directly or in a dedicated external file through the Include directive; for example, the mirrors for the official repositories are included from /etc/pacman.d/mirrorlist. See the Mirrors article for mirror configuration.

Pacman stores downloaded package files in cache, in a directory denoted by CacheDir in [options] section of pacman.conf (defaults to /var/cache/pacman/pkg/ if not set).

Cache directory may grow over time, even if keeping just the freshest versions of installed packages.

If you want to move that directory to some more convenient place, do one of the following:

Pacman supports package signatures, which add an extra layer of security to the packages. The default configuration, SigLevel = Required DatabaseOptional, enables signature verification for all the packages on a global level. This can be overridden by per-repository SigLevel lines. For more details on package signing and signature verification, take a look at pacman-key.

If you see the following error: [1]

This is happening because pacman has detected a file conflict, and by design, will not overwrite files for you. This is by design, not a flaw.

The problem is usually trivial to solve (although to be sure, you should try to find out how these files got there in the first place). A safe way is to first check if another package owns the file (pacman -Qo /path/to/file). If the file is owned by another package, file a bug report. If the file is not owned by another package, rename the file which "exists in filesystem" and re-issue the update command. If all goes well, the file may then be removed.

If you had installed a program manually without using pacman, for example through make install, you have to remove/uninstall this program with all of its files. See also Pacman tips#Identify files not owned by any package.

Every installed package provides a /var/lib/pacman/local/package-version/files file that contains metadata about this package. If this file gets corrupted, is empty or goes missing, it results in file exists in filesystem errors when trying to update the package. Such an error usually concerns only one package. Instead of manually renaming and later removing all the files that belong to the package in question, you may explicitly run pacman -S --overwrite glob package to force pacman to overwrite files that match glob.

This article or section is out of date.

Look for .part files (partially downloaded packages) in /var/cache/pacman/pkg/ and remove them (often caused by usage of a custom XferCommand in pacman.conf).

That same error may also appear if archlinux-keyring is out-of-date, preventing pacman from verifying signatures. See Pacman/Package signing#Upgrade system regularly for the fix and how to avoid it in the future.

When pacman is about to alter the package database, for example installing a package, it creates a lock file at /var/lib/pacman/db.lck. This prevents another instance of pacman from trying to alter the package database at the same time.

If pacman is interrupted while changing the database, this stale lock file can remain. If you are certain that no instances of pacman are running then delete the lock file:

This error manifests as Not found in sync db, Target not found or Failed retrieving file.

Firstly, ensure the package actually exists. If certain the package exists, your package list may be out-of-date. Try running pacman -Syu to force a refresh of all package lists and upgrade. Also make sure the selected mirrors are up-to-date and repositories are correctly configured. You can also use Reflector to keep the mirrors up-to-date.

If pacman reports there is nothing to update, but the Failed retrieving file error continues to be printed, consider forcing a database download with pacman -Syyu. This is never needed under normal circumstances, so inspect more closely the status and consistency of the mirror.

It could also be that the repository containing the package is not enabled on your system, e.g. the package could be in the multilib repository, but multilib is not enabled in your pacman.conf.

See also FAQ#Why is there only a single version of each shared library in the official repositories?.

This article or section needs expansion.

Whether due to power loss, kernel panic or hardware failure an update may be interrupted. In most cases, there will not be much damage but the system will likely be unbootable.

Replicating the exact upgrade is needed to ensure the right scriptlets and hooks will run.

In the case that pacman crashes with a "database write" error while removing packages, and reinstalling or upgrading packages fails thereafter, do the following:

If /var/cache/pacman/pkg is a symlink, pacman will try to make a directory instead and thus remove this symlink during self-upgrade. This will cause the update to fail. As a result, /usr/bin/pacman and other contents of the pacman package will be missing.

Never symlink /var/cache/pacman/pkg because it is controlled by pacman. Use the CacheDir option or a bind mount instead; see #Package cache directory.

If you have already encountered this problem and broke your system, you can manually extract /usr contents from the package to restore pacman and then reinstall it properly; see FS#73306 and related forum thread for details.

pacman-staticAUR is a statically compiled version of pacman, so it will be able to run even when the libraries on the system are not working. This can also come in handy when a partial upgrade was performed and pacman can not run anymore.

The pinned comment and the PKGBUILD provides a way to directly download the binary, which can be used to reinstall pacman or to upgrade the entire system in case of partial upgrades.

In some situations, your system may be too broken (e.g., due to missing or incompatible libraries) to run `makepkg` or build the `pacman-static` package from the AUR successfully.

If building from the PKGBUILD fails or `makepkg` cannot be run, you can download a precompiled `pacman-static` binary from a trusted source. This static binary does not depend on system libraries and can be used to restore a working `pacman` on your system.

A reliable source for the binary is:

This will update your system and reinstall `pacman`, fixing broken dependencies related to missing shared libraries.

If even pacman-static does not work, it is possible to recover using an external pacman. One of the easiest methods to do so is by using the archiso and simply using --sysroot or --root to specify the mount point of the system to perform the operation on. See Chroot#Using chroot on how to mount the necessary filesystems required by --sysroot.

Even if pacman is terribly broken, you can fix it manually by downloading the latest packages and extracting them to the correct locations. The rough steps to perform are:

If you have a healthy Arch system on hand, you can see the full list of dependencies with:

But you may only need to update a few of them depending on your issue. An example of extracting a package is

Note the use of the w flag for interactive mode. Running non-interactively is very risky since you might end up overwriting an important file. Also take care to extract packages in the correct order (i.e. dependencies first). This forum post contains an example of this process where only a couple pacman dependencies are broken.

Most likely the initramfs became corrupted during a kernel update (improper use of pacman's --overwrite option can be a cause). There are two options; first, try the Fallback entry.

Once the system starts, run this command (for the stock linux kernel) either from the console or from a terminal to rebuild the initramfs image:

If that does not work, from a current Arch release (CD/DVD or USB stick), mount your root and boot partitions to /mnt and /mnt/boot, respectively. Then chroot using arch-chroot:

Reinstalling the kernel (the linux package) will automatically re-generate the initramfs image with mkinitcpio -p linux. There is no need to do this separately.

Afterwards, it is recommended that you run exit, umount /mnt/{boot,} and reboot.

As the error message says, your locale is not correctly configured. See Locale.

When locale files are intentionally removed by tools such as bleachbit or localepurgeAUR, pacman may issue warnings about missing locales during package updates.

To suppress these warnings, you can comment out the CheckSpace option in pacman.conf. Keep in mind that disabling CheckSpace turns off the space-checking functionality for all package installations, so use this workaround only when you have alternative means to monitor disk space.

Make sure that the relevant environment variables ($http_proxy, $ftp_proxy etc.) are set up. If you use pacman with sudo, you need to configure sudo to pass these environment variables to pacman. Also, ensure the configuration of dirmngr has honor-http-proxy in /etc/pacman.d/gnupg/dirmngr.conf to honor the proxy when refreshing the keys.

To reinstall all the native packages: pacman -Qnq | pacman -S - or pacman -S $(pacman -Qnq) (the -S option preserves the installation reason by default).

You will then need to reinstall all the foreign packages, which can be listed with pacman -Qmq.

It looks like previous pacman transaction removed or corrupted shared libraries needed for pacman itself.

To recover from this situation, you need to unpack required libraries to your filesystem manually. First find what package contains the missed library and then locate it in the pacman cache (/var/cache/pacman/pkg/). Unpack required shared library to the filesystem. This will allow to run pacman.

Now you need to reinstall the broken package. Note that you need to use --overwrite flag as you just unpacked system files and pacman does not know about it. Pacman will correctly replace our shared library file with one from package.

That's it. Update the rest of the system.

Some issues have been reported regarding network problems that prevent pacman from updating/synchronizing repositories. [2] [3] When installing Arch Linux natively, these issues have been resolved by replacing the default pacman file downloader with an alternative (see Improve pacman performance for more details). When installing Arch Linux as a guest OS in VirtualBox, this issue has also been addressed by using Host interface instead of NAT in the machine properties.

If you receive this error message with correct mirrors, try setting a different name server.

If you want to install a package on an sshfs mount using pacman -U and receive this error, move the package to a local directory and try to install again.

Upon executing, e.g., pacman -Syu inside a chroot environment an error is encountered:

This is frequently caused by the chroot directory not being a mountpoint when the chroot is entered. See the note at Install Arch Linux from existing Linux#Downloading basic tools for a solution, and arch-chroot(8) for an explanation and an example of using bind mounting to make the chroot directory a mountpoint.

If you are unable to update packages and receive this error, then try rm -r /var/lib/pacman/sync/ before attempting to update.

If removing sync files doesn't help, check that the sync files are gzip compressed data using file /var/lib/pacman/sync/* before attempting to update. A router or proxy might corrupt the downloads. Corruption could possibly be HTML type.

If sync files are of the correct type, there might be an issue with the mirror server. Look up the mirror server(s) in use with pacman-conf -r core and pacman-conf -r extra. Paste the first returned url in a browser and check that a file listing is returned. In case the mirror returns an error, comment it in /etc/pacman.d/mirrorlist. You may try updating or re-ranking mirrors.

If this error occurs and you're for instance unable to update your system or any package at all, it is possible that you have DISPLAY set to a blank value, which seems to break the GPG-Flow.

In this case, unset DISPLAY or setting it to a arbitrary value will most likely allow to update again, in case any other option above didn't do the trick yet. See this post for further details.

One may use the pacman -Qk $pkg to check if the installed files of the $pkg package match the files from its database version. For several packages, one may use the following loop to reinstall all packages which have missing file(s):

Suppose that your local database located in /var/lib/pacman is more up-to-date compared to installed packages in the / filesystem (e.g., because of a partial rollback), then this method is the appropriate one to re-synchronize the root filesystem with the local database.

**Examples:**

Example 1 (unknown):
```unknown
pacman -Ql pacman pacman-contrib | grep -E 'bin/.+'
```

Example 2 (unknown):
```unknown
pacman -Sy package_name
```

Example 3 (unknown):
```unknown
pacman -Syu package_name
```

Example 4 (unknown):
```unknown
# pacman -S package_name1 package_name2 ...
```

---

## GRUB

**URL:** https://wiki.archlinux.org/title/BIOS_boot_partition

**Contents:**
- Supported file systems
- UEFI systems
  - Installation
  - Secure Boot support
    - CA Keys
    - Shim-lock
    - Using Secure Boot
- BIOS systems
  - GUID Partition Table (GPT) specific instructions
  - Master Boot Record (MBR) specific instructions

GRUB (GRand Unified Bootloader) is a boot loader. The current GRUB is also referred to as GRUB 2. The original GRUB, or GRUB Legacy, corresponds to versions 0.9x. This page exclusively describes GRUB 2.

GRUB bundles its own support for multiple file systems, notably FAT32, ext4, Btrfs or XFS. See #Unsupported file systems for some caveats.

First, install the packages grub and efibootmgr: GRUB is the boot loader while efibootmgr is used by the GRUB installation script to write boot entries to NVRAM.

Then follow the below steps to install GRUB to your disk:

After the above installation completed, the main GRUB directory is located at /boot/grub/. Read /Tips and tricks#Alternative install method for how to specify an alternative location. Note that grub-install also tries to create an entry in the firmware boot manager, named GRUB in the above example – this will, however, fail if your boot entries are full or the systems prevents the boot order from being manipulated (e.g. Thinkpad BIOSs have a setting called "Boot Order Lock" which needs to be disabled for efibootmgr to be able to add/remove entries); use efibootmgr to remove unnecessary entries.

See UEFI troubleshooting in case of problems. Additionally see /Tips and tricks#UEFI further reading.

GRUB fully supports secure boot utilising either CA keys or shim; the installation command, however, is different depending on which you intend to use.

To make use of CA Keys the command is:

When using Shim-lock, GRUB can only be successfully booted in Secure Boot mode if its EFI binary includes all of the modules necessary to read the filesystem containing the vmlinuz and initramfs images.

Since GRUB version 2.06.r261.g2f4430cc0, loading modules in Secure Boot Mode via insmod is no longer allowed, as this would violate the expectation to not sideload arbitrary code. If the GRUB modules are not embedded in the EFI binary, and GRUB tries to sideload/insmod them, GRUB will fail to boot with the message:

Ubuntu, according to its official build script, embeds the following GRUB modules in its signed GRUB EFI binary grubx64.efi:

You must construct your list of GRUB modules in the form of a shell variable that we denote as GRUB_MODULES. You can use the latest Ubuntu script as a starting point, and trim away modules that are not necessary on your system. Omitting modules will make the boot process relatively faster, and save some space on the ESP partition.

You also need a Secure Boot Advanced Targeting (SBAT) file/section included in the EFI binary, to improve the security; if GRUB is launched from the UEFI shim loader. This SBAT file/section contains metadata about the GRUB binary (version, maintainer, developer, upstream URL) and makes it easier for shim to block certain GRUB versions from being loaded if they have security vulnerabilities[1][2], as explained in the UEFI shim boot loader secure boot life-cycle improvements document from shim.

The first-stage UEFI boot loader shim will fail to launch grubx64.efi if the SBAT section from grubx64.efi is missing!

If GRUB is installed, a sample SBAT .csv file is provided under /usr/share/grub/sbat.csv.

Reinstall GRUB using the provided /usr/share/grub/sbat.csv file and all the needed GRUB_MODULES and sign it:

Reboot, select the key in MokManager, and Secure Boot should be working.

After installation see Secure Boot#Implementing Secure Boot for instructions on enabling it.

If you are using the CA Keys method then key management, enrollment, and file signing can be automated by using sbctl, see Secure Boot#Assisted process with sbctl for details.

On a BIOS/GPT configuration, a BIOS boot partition is required. GRUB embeds its core.img into this partition.

Create a mebibyte partition (+1M with fdisk or gdisk) on the disk with no file system and with partition type GUID 21686148-6449-6E6F-744E-656564454649.

This partition can be in any position order but has to be on the first 2 TiB of the disk. This partition needs to be created before GRUB installation. When the partition is ready, install the boot loader as per the instructions below.

The space before the first partition can also be used as the BIOS boot partition though it will be out of GPT alignment specification. Since the partition will not be regularly accessed performance issues can be disregarded, though some disk utilities will display a warning about it. In fdisk or gdisk create a new partition starting at sector 34 and spanning to 2047 and set the type. To have the viewable partitions begin at the base consider adding this partition last.

Usually the post-MBR gap (after the 512 byte MBR region and before the start of the first partition) in many MBR partitioned systems is 31 KiB when DOS compatibility cylinder alignment issues are satisfied in the partition table. However a post-MBR gap of about 1 to 2 MiB is recommended to provide sufficient room for embedding GRUB's core.img (FS#24103). It is advisable to use a partitioning tool that supports 1 MiB partition alignment to obtain this space as well as to satisfy other non-512-byte-sector issues (which are unrelated to embedding of core.img).

Install the grub package. (It will replace grub-legacyAUR if that is already installed.) Then do:

where i386-pc is deliberately used regardless of your actual architecture, and /dev/sdX is the disk (not a partition) where GRUB is to be installed. For example /dev/sda or /dev/nvme0n1, or /dev/mmcblk0. See Device file#Block device names for a description of the block device naming scheme.

Now you must generate the main configuration file.

If you use LVM for your /boot, you can install GRUB on multiple physical disks.

See grub-install(8) and GRUB Manual for more details on the grub-install command.

On an installed system, GRUB loads the /boot/grub/grub.cfg configuration file each boot. You can follow #Generated grub.cfg for using a tool, or #Custom grub.cfg for a manual creation.

This section only covers editing the /etc/default/grub configuration file. See /Tips and tricks for more information.

After the installation, the main configuration file /boot/grub/grub.cfg needs to be generated. The generation process can be influenced by a variety of options in /etc/default/grub and scripts in /etc/grub.d/. For the list of options in /etc/default/grub and a concise description of each refer to GNU's documentation.

If you have not done additional configuration, the automatic generation will determine the root filesystem of the system to boot for the configuration file. For that to succeed it is important that the system is either booted or chrooted into.

Use the grub-mkconfig tool to generate /boot/grub/grub.cfg:

By default the generation scripts automatically add menu entries for all installed Arch Linux kernels to the generated configuration.

To automatically add entries for other installed operating systems, see #Detecting other operating systems.

You can add additional custom menu entries by editing /etc/grub.d/40_custom and re-generating /boot/grub/grub.cfg. Or you can create /boot/grub/custom.cfg and add them there. Changes to /boot/grub/custom.cfg do not require re-running grub-mkconfig, since /etc/grub.d/41_custom adds the necessary source statement to the generated configuration file.

See #Boot menu entry examples for custom menu entry examples.

To have grub-mkconfig search for other installed systems and automatically add them to the menu, install the os-prober package and mount the partitions from which the other systems boot. Then re-run grub-mkconfig. If you get the following output: Warning: os-prober will not be executed to detect other bootable partitions then edit /etc/default/grub and add/uncomment:

For Windows installed in UEFI mode, make sure the EFI system partition containing the Windows Boot Manager (bootmgfw.efi) is mounted. Run os-prober as root to detect and generate an entry for it.

For Windows installed in BIOS mode, mount the Windows system partition (its file system label should be System Reserved or SYSTEM). Run os-prober as root to detect and generate an entry for it.

To pass custom additional arguments to the Linux image, you can set the GRUB_CMDLINE_LINUX + GRUB_CMDLINE_LINUX_DEFAULT variables in /etc/default/grub. The two are appended to each other and passed to kernel when generating regular boot entries. For the recovery boot entry, only GRUB_CMDLINE_LINUX is used in the generation.

It is not necessary to use both, but can be useful. For example, you could use GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=uuid-of-swap-partition quiet" where uuid-of-swap-partition is the UUID of your swap partition to enable resume after hibernation. This would generate a recovery boot entry without the resume and without quiet suppressing kernel messages during a boot from that menu entry. Though, the other (regular) menu entries would have them as options.

By default grub-mkconfig determines the UUID of the root filesystem for the configuration. To disable this, uncomment GRUB_DISABLE_LINUX_UUID=true.

For generating the GRUB recovery entry you have to ensure that GRUB_DISABLE_RECOVERY is not set to true in /etc/default/grub.

See Kernel parameters for more info.

By default, grub-mkconfig sorts the included kernels using sort -V and uses the first kernel in that list as the top-level entry. This means that, for example, since /boot/vmlinuz-linux-lts is sorted before /boot/vmlinuz-linux, if you have both linux-lts and linux installed, the LTS kernel will be the top-level menu entry, which may not be desirable. This can be overridden by specifying GRUB_TOP_LEVEL="path_to_kernel" in /etc/default/grub. For example, to make the regular kernel be the top-level menu entry, you can use GRUB_TOP_LEVEL="/boot/vmlinuz-linux".

This article or section is a candidate for merging with #Installation.

If you use LVM for your /boot or / root partition, make sure that the lvm module is preloaded:

This article or section is a candidate for merging with #Installation.

GRUB provides convenient handling of RAID volumes. You need to load GRUB modules mdraid09 or mdraid1x to allow you to address the volume natively:

For example, /dev/md0 becomes:

whereas a partitioned RAID volume (e.g. /dev/md0p1) becomes:

To install grub when using RAID1 as the /boot partition (or using /boot housed on a RAID1 root partition), on BIOS systems, simply run grub-install on both of the drives, such as:

Where the RAID 1 array housing /boot is housed on /dev/sda and /dev/sdb.

GRUB also has special support for booting with an encrypted /boot. This is done by unlocking a LUKS blockdevice in order to read its configuration and load any initramfs and kernel from it. This option tries to solve the issue of having an unencrypted boot partition.

To enable this feature encrypt the partition with /boot residing on it using LUKS as normal. Then add the following option to /etc/default/grub:

This option is used by grub-install to generate the grub core.img.

Make sure to install grub after modifying this option or encrypting the partition.

Without further changes you will be prompted twice for a passphrase: the first for GRUB to unlock the /boot mount point in early boot, the second to unlock the root filesystem itself as implemented by the initramfs. You can use a keyfile to avoid this.

Use grub-install as described in the #Installation section to create a bootable GRUB image with LUKS support. Note the following caveats:

If you enter an invalid passphrase during boot and end up at the GRUB rescue shell, try cryptomount -a to mount all (hopefully only one) encrypted partitions or use cryptomount -u $crypto_uuid to mount a specific one. Then proceed with insmod normal and normal as usual.

If you enter a correct passphrase, but an Invalid passphrase error is immediately returned, make sure that the right cryptographic modules are specified. Use cryptsetup luksDump /dev/nvme0n1p2 and check whether the hash function (SHA-256, SHA-512) matches the modules (gcry_sha256, gcry_sha512) installed and the PBKDF algorithm is pbkdf2. The hash and PBDKDF algorithms can be changed for existing keys by using cryptsetup luksConvertKey --hash sha256 --pbkdf pbkdf2 /dev/nvme0n1p2. Under normal circumstances it should take a few seconds before the passphrase is processed.

This article or section needs expansion.

This section describes the manual creation of GRUB boot entries in /boot/grub/grub.cfg instead of relying on grub-mkconfig.

A basic GRUB config file uses the following options:

For GRUB to set the LoaderDevicePartUUID UEFI variable required by systemd-gpt-auto-generator(8) for GPT partition automounting, load the bli module in grub.cfg:

For tips on managing multiple GRUB entries, for example when using both linux and linux-lts kernels, see /Tips and tricks#Multiple entries.

For Archiso and Archboot boot menu entries see Multiboot USB drive#Boot entries.

When launched in UEFI mode, GRUB can chainload other EFI binaries.

You can launch UEFI Shell by placing it in the root of the EFI system partition and adding this menu entry:

Download the gdisk EFI application and copy gdisk_x64.efi to esp/EFI/tools/.

If you have a unified kernel image generated from following Secure Boot or other means, you can add it to the boot menu. For example:

Assuming that the other distribution is on partition sda2:

Alternatively let GRUB search for the right partition by UUID or file system label:

If the other distribution has already a valid /boot folder with installed GRUB, grub.cfg, kernel and initramfs, GRUB can be instructed to load these other grub.cfg files on-the-fly during boot. For example, for hd0 and the fourth GPT partition:

When choosing this entry, GRUB loads the grub.cfg file from the other volume and displays that menu. Any environment variable changes made by the commands in file will not be preserved after configfile returns. Press Esc to return to the first GRUB menu.

This mode determines where the Windows boot loader resides and chain-loads it after GRUB when the menu entry is selected. The main task here is finding the EFI system partition and running the boot loader from it.

where $hints_string and $fs_uuid are obtained with the following two commands.

The $fs_uuid command determines the UUID of the EFI system partition:

Alternatively one can run lsblk --fs and read the UUID of the EFI system partition from there.

The $hints_string command will determine the location of the EFI system partition, in this case harddrive 0:

These two commands assume the ESP Windows uses is mounted at esp. There might be case differences in the path to Windows's EFI file, what with being Windows, and all.

Throughout this section, it is assumed your Windows partition is /dev/sda1. A different partition will change every instance of hd0,msdos1.

In both examples XXXX-XXXX is the filesystem UUID which can be found with command lsblk --fs.

For Windows Vista/7/8/8.1/10:

Do not use bootrec.exe /Fixmbr because it will wipe GRUB out. Or you can use Boot Repair function in the Troubleshooting menu - it will not wipe out GRUB but will fix most errors. Also you would better keep plugged in both the target hard drive and your bootable device ONLY. Windows usually fails to repair boot information if any other devices are connected.

It is possible to use file system labels, human-readable strings attached to file systems, by using the --label option to search. First of all, make sure your file system has a label.

Then, add an entry using labels. An example of this:

Since the MBR is too small to store all GRUB modules, only the menu and a few basic commands reside there. The majority of GRUB functionality remains in modules in /boot/grub/, which are inserted as needed. In error conditions (e.g. if the partition layout changes) GRUB may fail to boot. When this happens, a command shell may appear.

GRUB offers multiple shells/prompts. If there is a problem reading the menu but the boot loader is able to find the disk, you will likely be dropped to the "normal" shell:

If there is a more serious problem (e.g. GRUB cannot find required files), you may instead be dropped to the "rescue" shell:

The rescue shell is a restricted subset of the normal shell, offering much less functionality. If dumped to the rescue shell, first try inserting the "normal" module, then starting the "normal" shell:

GRUB supports pager for reading commands that provide long output (like the help command). This works only in normal shell mode and not in rescue mode. To enable pager, in GRUB command shell type:

The GRUB's command shell environment can be used to boot operating systems. A common scenario may be to boot Windows / Linux stored on a drive/partition via chainloading.

Chainloading means to load another boot-loader from the current one, ie, chain-loading.

The other boot loader may be embedded at the start of a partitioned disk (MBR), at the start of a partition or a partitionless disk (VBR), or as an EFI binary in the case of UEFI.

X=0,1,2... Y=1,2,3...

For example to chainload Windows stored in the first partition of the first hard disk,

Similarly GRUB installed to a partition can be chainloaded.

insmod fat is used for loading the FAT file system module for accessing the Windows boot loader on the UEFI system partition. (hd0,gpt4) or /dev/sda4 is the UEFI system partition in this example. The entry in the chainloader line specifies the path of the .efi file to be chain-loaded.

See the examples in #Using the rescue console

See #Using the command shell first. If unable to activate the standard shell, one possible solution is to boot using a live CD or some other rescue disk to correct configuration errors and reinstall GRUB. However, such a boot disk is not always available (nor necessary); the rescue console is surprisingly robust.

The available commands in GRUB rescue include insmod, ls, set, and unset. This example uses set and insmod. set modifies variables and insmod inserts new modules to add functionality.

Before starting, the user must know the location of their /boot partition (be it a separate partition, or a subdirectory under their root):

where X is the physical drive number and Y is the partition number.

To expand console capabilities, insert the linux module:

This introduces the linux and initrd commands, which should be familiar.

An example, booting Arch Linux:

With a separate boot partition (e.g. when using UEFI), again change the lines accordingly:

After successfully booting the Arch Linux installation, users can correct grub.cfg as needed and then reinstall GRUB.

To reinstall GRUB and fix the problem completely, changing /dev/sda if needed. See #Installation for details.

Before removing grub, make sure that some other boot loader is installed and configured to take over.

If BootOrder has grub as the first entry, install another boot loader to put it in front, such as systemd-boot above. grub can then be removed using its bootnum.

Also delete the esp/EFI/grub and /boot/grub directories.

To replace grub with any other BIOS boot loader, simply install them, which will overwrite the MBR boot code.

grub-install creates the /boot/grub directory that needs to be removed manually. Though some users will want to keep it, should they want to install grub again.

After migrating to UEFI/GPT one may want to remove the MBR boot code using dd.

In case that GRUB does not support the root file system, an alternative /boot partition with a supported file system must be created. In some cases, the development version of GRUB grub-gitAUR may have native support for the file system.

If GRUB is used with an unsupported file system it is not able to extract the UUID of your drive so it uses classic non-persistent /dev/sdXx names instead. In this case you might have to manually edit /boot/grub/grub.cfg and replace root=/dev/sdXx with root=UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. You can use the blkid command to get the UUID of your device, see Persistent block device naming.

While GRUB supports F2FS since version 2.0.4, it cannot correctly read its boot files from an F2FS partition that was created with the extra_attr flag enabled.

This error may occur when you try installing GRUB in a VMware container. Read more about it here. It happens when the first partition starts just after the MBR (block 63), without the usual space of 1 MiB (2048 blocks) before the first partition. Read #Master Boot Record (MBR) specific instructions

grub-install automatically tries to create a menu entry in the boot manager. If it does not, then see UEFI#efibootmgr for instructions to use efibootmgr to create a menu entry. However, the problem is likely to be that you have not booted your CD/USB in UEFI mode, as in Installation guide#Verify the boot mode.

As another example of creating a GRUB entry in the firmware boot manager, consider efibootmgr -c. This assumes that /dev/sda1 is the EFI System Partition, and is mounted at /boot/efi. Which are the default behavior of efibootmgr. It creates a new boot option, called "Linux", and puts it at the top of the boot order list. Options may be passed to modify the default behavior. The default OS Loader is \EFI\arch\grub.efi.

If GRUB loads but drops into the rescue shell with no errors, it can be due to one of these two reasons:

An example of a working UEFI:

If the screen only goes black for a second and the next boot option is tried afterwards, according to this post, moving GRUB to the partition root can help. The boot option has to be deleted and recreated afterwards. The entry for GRUB should look like this then:

Some UEFI firmwares require a bootable file at a known location before they will show UEFI NVRAM boot entries. If this is the case, grub-install will claim efibootmgr has added an entry to boot GRUB, however the entry will not show up in the VisualBIOS boot order selector. The solution is to install GRUB at the default/fallback boot path:

Alternatively you can move an already installed GRUB EFI executable to the default/fallback path:

If trying to boot Windows results in an "invalid signature" error, e.g. after reconfiguring partitions or adding additional hard drives, (re)move GRUB's device configuration and let it reconfigure:

grub-mkconfig should now mention all found boot options, including Windows. If it works, remove /boot/grub/device.map-old.

If booting gets stuck without any error message after GRUB loading the kernel and the initial ramdisk, try removing the add_efi_memmap kernel parameter.

Some have reported that other distributions may have trouble finding Arch Linux automatically with os-prober. If this problem arises, it has been reported that detection can be improved with the presence of /etc/lsb-release. This file and updating tool is available with the package lsb-release.

When installing GRUB on a LVM system in a chroot environment (e.g. during system installation), you may receive warnings like

This is because /run is not available inside the chroot. These warnings will not prevent the system from booting, provided that everything has been done correctly, so you may continue with the installation.

GRUB can take a long time to load when disk space is low. Check if you have sufficient free disk space on your /boot or / partition when you are having problems.

GRUB may output error: unknown filesystem and refuse to boot for a few reasons. If you are certain that all UUIDs are correct and all filesystems are valid and supported, it may be because your BIOS Boot Partition is located outside the first 2 TiB of the drive [4]. Use a partitioning tool of your choice to ensure this partition is located fully within the first 2 TiB, then reinstall and reconfigure GRUB.

This error might also be caused by an ext4 filesystem having unsupported features set:

GRUB seems to be unable to write to root Btrfs partitions [5]. If you use grub-reboot to boot into another entry it will therefore be unable to update its on-disk environment. Either run grub-reboot from the other entry (for example when switching between various distributions) or consider a different file system. You can reset a "sticky" entry by executing grub-editenv create and setting GRUB_DEFAULT=0 in your /etc/default/grub (do not forget grub-mkconfig -o /boot/grub/grub.cfg).

If a drive is formatted with Btrfs without creating a partition table (eg. /dev/sdx), then later has partition table written to, there are parts of the BTRFS format that persist. Most utilities and OS's do not see this, but GRUB will refuse to install, even with --force

You can zero the drive, but the easy solution that leaves your data alone is to erase the Btrfs superblock with wipefs -o 0x10040 /dev/sdx

A setting in Windows 8/10 called "Hiberboot", "Hybrid Boot" or "Fast Boot" can prevent the Windows partition from being mounted, so grub-mkconfig will not find a Windows install. Disabling Hiberboot in Windows will allow it to be added to the GRUB menu.

When using an encrypted /boot, and you fail to input a correct password, you will be dropped in grub-rescue prompt.

This grub-rescue prompt has limited capabilities. Use the following commands to complete the boot:

See this blog post for a better description.

Check /etc/default/grub if GRUB_TIMEOUT is set to 0, in which case set it to a positive number: it sets the number of seconds before the default GRUB entry is loaded. Also check if GRUB_TIMEOUT_STYLE is set to hidden and set it to menu, so that the menu will be shown by default. Then regenerate the main configuration file and reboot to check if it worked.

If it does not work, there may be incompatibility problems with the graphical terminal. Set GRUB_TERMINAL_OUTPUT to console in /etc/default/grub to disable the GRUB graphical terminal.

See Fixing Lenovo’s ERROR CODE 1962 by spoofing the EFI boot entries.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

You can do it manually or use a pacman hook, for example:

Change grub-install options such as the --efi-directory path to match your settings.

**Examples:**

Example 1 (unknown):
```unknown
grubx64.efi
```

Example 2 (unknown):
```unknown
grubx64.efi
```

Example 3 (unknown):
```unknown
grub-mkstandalone
```

Example 4 (unknown):
```unknown
grub-install
```

---

## Install Arch Linux on LVM

**URL:** https://wiki.archlinux.org/title/Install_Arch_Linux_on_LVM

**Contents:**
- Installation
  - Create partitions
  - Create physical volumes
  - Create and extend your volume group
    - Combined creation of physical volumes and volume groups
  - Create logical volumes
  - Format and mount logical volumes
- Configure the system
  - Adding mkinitcpio hooks
  - Kernel boot options

You should create your LVM Volumes between the partitioning and formatting steps of the installation procedure. Instead of directly formatting a partition to be your root file system, the file system will be created inside a logical volume (LV).

You will follow along with the installation guide until you come to Installation guide#Partition the disks. At this point you will diverge and doing all your partitioning with LVM in mind.

First, partition your disks as required before configuring LVM.

Create the partitions:

To list all your devices capable of being used as a physical volume:

Create a physical volume on them:

This command creates a header on each device so it can be used for LVM. As defined in LVM#LVM building blocks, DEVICE can be any block device, e.g. a disk /dev/sda, a partition /dev/sda2 or a loop back device. For example:

You can track created physical volumes with:

You can also get summary information on physical volumes with:

First you need to create a volume group on any one of the physical volumes:

See lvm(8) for a list of valid characters for volume group names.

Extending the volume group is just as easy:

For example, to add both sdb1 and sdc to your volume group:

You can track how your volume group grows with:

This is also what you would do if you wanted to add a disk to a RAID or mirror group with failed disks.

LVM allows you to combine the creation of a volume group and the physical volumes in one easy step. For example, to create the group VolGroup00 with the three devices mentioned above, you can run:

This command will first set up the three partitions as physical volumes (if necessary) and then create the volume group with the three volumes. The command will warn you if it detects an existing filesystem on any devices.

Now we need to create logical volumes on this volume group. You create a logical volume with the next command by specifying the new volume's name and size, and the volume group it will reside on:

This will create a logical volume that you can access later with /dev/VolGroup00/lvolhome. Just like volume groups, you can use any name you want for your logical volume when creating it besides a few exceptions listed in lvm(8) § VALID_NAMES.

You can also specify one or more physical volumes to restrict where LVM allocates the data. For example, you may wish to create a logical volume for the root filesystem on your small SSD, and your home volume on a slower mechanical drive. Simply add the physical volume devices to the command line, for example:

To use all the free space left in a volume group, use the next command:

You can track created logical volumes with:

Your logical volumes should now be located in /dev/YourVolumeGroupName/. If you cannot find them, use the next commands to bring up the module for creating device nodes and to make volume groups available:

Now you can format your logical volumes and mount them as normal partitions (see mount a file system for additional details):

Make sure the lvm2 package is installed.

In case your root filesystem is on LVM, you will need to enable the appropriate mkinitcpio hooks, otherwise your system might not boot. Enable:

udev is there by default. Edit the file and insert lvm2 between block and filesystems like so:

For systemd based initramfs:

Afterwards, you can continue in normal installation instructions with the recreate the initramfs image step.

If the root file system resides in a logical volume, the root= kernel parameter must be pointed to the mapped device, e.g /dev/vg-name/lv-name.

**Examples:**

Example 1 (unknown):
```unknown
/etc/mkinitcpio.conf
```

Example 2 (unknown):
```unknown
E6D6D379-F507-44C2-A23C-238F2A3DF928
```

Example 3 (unknown):
```unknown
# lvmdiskscan
```

Example 4 (unknown):
```unknown
# pvcreate DEVICE
```

---

## dm-crypt/Encrypting an entire system

**URL:** https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system

**Contents:**
- Overview
- LUKS on a partition
  - Preparing the disk
  - Preparing non-boot partitions
  - Preparing the boot partition
  - Mounting the devices
  - Configuring mkinitcpio
  - Configuring the boot loader
- LUKS on a partition with TPM2 and Secure Boot
  - Preparing the disk

The following are examples of common scenarios of full system encryption with dm-crypt. They explain all the adaptations that need to be done to the normal installation procedure. All the necessary tools are on the installation image.

If you want to encrypt an existing unencrypted file system, see dm-crypt/Device encryption#Encrypt an existing unencrypted file system.

Securing a root file system is where dm-crypt excels, feature and performance-wise. Unlike selectively encrypting non-root file systems, an encrypted root file system can conceal information such as which programs are installed, the usernames of all user accounts, and common data-leakage vectors such as locate and /var/log/. Furthermore, an encrypted root file system makes tampering with the system far more difficult, as everything except the boot loader and (usually) the kernel is encrypted.

All scenarios illustrated in the following share these advantages, other pros and cons differentiating them are summarized below:

shows a basic and straightforward set-up for a fully LUKS encrypted root.

Similar to the example above, with Secure Boot and TPM2 providing additional layers of security.

Same advantages as above, and

achieves partitioning flexibility by using LVM inside a single LUKS encrypted partition.

uses dm-crypt only after the LVM is setup.

uses dm-crypt only after RAID is setup.

uses dm-crypt plain mode, i.e. without a LUKS header and its options for multiple keys. This scenario also employs USB devices for /boot and key storage, which may be applied to the other scenarios.

shows how to encrypt the boot partition using the GRUB boot loader. This scenario also employs an EFI system partition, which may be applied to the other scenarios.

While all above scenarios provide much greater protection from outside threats than encrypted secondary file systems, they also share a common disadvantage: any user in possession of the encryption key is able to decrypt the entire drive, and therefore can access other users' data. If that is of concern, it is possible to use a combination of block device and stacked file system encryption and reap the advantages of both. See Data-at-rest encryption to plan ahead.

See dm-crypt/Drive preparation#Partitioning for a general overview of the partitioning strategies used in the scenarios.

Another area to consider is whether to set up an encrypted swap partition and what kind. See dm-crypt/Swap encryption for alternatives.

If you anticipate to protect the system's data not only against physical theft, but also have a requirement of precautions against logical tampering, see dm-crypt/Specialties#Securing the unencrypted boot partition for further possibilities after following one of the scenarios.

For solid state drives you might want to consider enabling TRIM support, but be warned, there are potential security implications. See dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD) for more information.

This example covers a full system encryption with dm-crypt + LUKS in a simple partition layout:

The first steps can be performed directly after booting the Arch Linux install image.

Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Then create the needed partitions, at least one for / (e.g. /dev/sda2) and /boot (/dev/sda1). See Partitioning.

This and the next section replace the instructions of Installation guide#Format the partitions.

The following commands create and mount the encrypted root partition. They correspond to the procedure described in detail in dm-crypt/Device encryption#Encrypting devices with LUKS mode. If you want to use particular non-default encryption options (e.g. cipher, key length, sector size), see the encryption options before executing the first command.

Create a file system on unlocked LUKS device. For example, to create an Ext4 file system, run:

Mount the root volume to /mnt:

Check the mapping works as intended:

If you created separate partitions (e.g. /home), these steps have to be adapted and repeated for all of them, except for /boot. See dm-crypt/Encrypting a non-root file system#Automated unlocking and mounting on how to handle additional partitions at boot.

Note that each block device requires its own passphrase. This may be inconvenient, because it results in a separate passphrase to be input during boot. An alternative is to use a keyfile stored in the root partition to unlock the separate partition via crypttab. See dm-crypt/Device encryption#Using LUKS to format partitions with a keyfile for instructions.

What you do have to setup is a non-encrypted /boot partition, which is needed for an encrypted root. For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

or for an ordinary boot partition on BIOS systems:

Afterwards create the directory for the mountpoint and mount the partition:

At the step Installation guide#Mount the file systems, you should mount the /dev/mapper/* devices (the contents of LUKS), not the actual partitions. Of course, the partition for /boot, which is not encrypted, should still be mounted directly. During installation, it should be mounted to /mnt/boot (assuming the device for the root file system is mounted to /mnt during installation).

Before following Installation guide#Initramfs you must do the following to your new system:

If using the default busybox-based initramfs, add the keyboard and encrypt hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the keymap and consolefont hooks, respectively.

If using a systemd-based initramfs, instead add the keyboard and sd-encrypt hooks. If you use a non-US console keymap or a non-default console font, additionally add the sd-vconsole hook.

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

If using the sd-encrypt hook, the following need to be set instead:

The device-UUID refers to the UUID of the LUKS superblock, in this example it is the UUID of /dev/sda2. See Persistent block device naming for details.

Also see dm-crypt/System configuration#Kernel parameters for more details.

This example is similar to #LUKS on a partition, but integrates the use of Secure Boot and a Trusted Platform Module (TPM), enhancing the overall security of the boot process.

In this configuration, only the EFI system partition remains unencrypted, housing a unified kernel image and systemd-boot—both signed for use with Secure Boot. If Secure Boot is disabled or its key databases are tampered with, the TPM will not release the key to unlock the encrypted partition. This approach is akin to BitLocker on Windows or FileVault on macOS. A recovery-key will also be created to make sure the data remains accessible in case of a problem with the TPM unlocking mechanism (unsigned boot loader or kernel update, firmware update, etc.). Optionally, a TPM pin can be set to be required during boot time to prevent fully automatic unlocking.

Make sure to thoroughly read the discussion and warnings in Trusted Platform Module#LUKS encryption.

In this example, partitions are created respecting systemd#GPT partition automounting, there is no need for an fstab or crypttab file.

Follow the Installation guide up to step Installation guide#Partition the disks.

Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Partition the drive with the GUID Partition Table (GPT).

Create an EFI system partition (e.g., /dev/sda1) with an appropriate size. This will be mounted at /boot.

In the remaining space, create a root partition (e.g., /dev/sda2) that will be encrypted and mounted at /. Set the partition type GUID for the root partition using type "Linux root (x86-64)" in fdisk or type code 8304 in gdisk.

Check the output of fdisk -l to make sure partition types are properly set.

The following commands create and mount the encrypted root partition. They correspond to the procedure described in detail in dm-crypt/Device encryption#Encrypting devices with LUKS mode.

If you want to use particular non-default encryption options (e.g. cipher, key length), or if you don't want to use TPM based decryption, see the encryption options before executing the first command.

Create the LUKS volume and mount it:

Create a file system on unlocked LUKS device. For example, to create an Ext4 file system, run:

Mount the root volume to /mnt:

Format the newly created EFI system partition as instructed in EFI system partition#Format the partition and mount it afterwards.

Continue the installation process until Installation guide#Initramfs. You can skip Installation guide#Fstab.

To build a working systemd based initramfs, modify the HOOKS= line in mkinitcpio.conf as follows:

Next, see Unified kernel image#mkinitcpio to configure mkinitcpio for Unified kernel images.

Do not regenerate the initramfs yet, as the /boot/EFI/Linux directory needs to be created by the boot loader installer first.

You can configure your system to directly boot the UEFI image without any boot loader, see Unified kernel image#Directly from UEFI.

If a boot loader is desired, continue installing systemd-boot with

The Unified kernel image generated by mkinitcpio will be automatically recognized and does not need an entry in /boot/loader/entries/.

See systemd-boot#Updating the UEFI boot manager and systemd-boot#Loader configuration for further configuration.

First, Regenerate the initramfs, and make sure the image generation is successful.

Make sure you did not forget to set a root password, reboot to finish the installation.

You can now sign the boot loader executables and the EFI binary, in order to enable Secure Boot. For a quick and easy way, see Unified Extensible Firmware Interface/Secure Boot#Assisted process with sbctl.

After signing the boot loader executables and enabling Secure Boot, you can now enroll the TPM in order to use it to unlock the LUKS volume. The following commands will remove the empty passphrase created during the LUKS format process, create a key bound to the TPM PCR 7 (Secure Boot state and enrolled certificates) and create a recovery key to be used in case of any problems. The TPM will automatically release the key as long as the boot chain is not tampered with. See systemd-cryptenroll#Trusted Platform Module and systemd-cryptenroll(1).

The straightforward method is to set up LVM on top of the encrypted partition instead of the other way round. Technically the LVM is setup inside one big encrypted block device. Hence, the LVM is not visible until the block device is unlocked and the underlying volume structure is scanned and mounted during boot.

The disk layout in this example is:

Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

Create a partition to be mounted at /boot with a size of 1 GiB or more.

Create a partition which will later contain the encrypted container.

Create the LUKS encrypted container at the designated partition. Enter the chosen password twice.

For more information about the available cryptsetup options see the LUKS encryption options prior to above command.

The decrypted container is now available at /dev/mapper/cryptlvm.

Create a physical volume on top of the opened LUKS container:

Create a volume group (in this example named MyVolGroup, but it can be whatever you want) and add the previously created physical volume to it:

Create all your logical volumes on the volume group:

Format your file systems on each logical volume. For example, using Ext4 for the root and home volumes:

Mount your file systems:

The boot loader loads the kernel, initramfs, and its own configuration files from the /boot directory. Any file system on a disk that can be read by the boot loader is eligible.

Create a file system on the partition intended for /boot. For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

or for an ordinary boot partition on BIOS systems:

Mount the partition to /mnt/boot:

At this point resume the common Installation guide#Installation steps. Return to this page to customize the Initramfs and Boot loader steps.

Make sure the lvm2 package is installed.

If using the default busybox-based initramfs, add the keyboard, encrypt and lvm2 hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the keymap and consolefont hooks, respectively.

If using a systemd-based initramfs, instead add the keyboard, sd-encrypt and lvm2 hooks. If you use a non-US console keymap or a non-default console font, additionally add the sd-vconsole hook.

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

Note: When using dracut, no additional setup is required, as the required modules are already included.

In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

If using the sd-encrypt hook, the following needs to be set instead:

The device-UUID refers to the UUID of the LUKS superblock, in this example it is the UUID of /dev/sda1. See Persistent block device naming for details.

If using dracut, these parameters are known to work:

you may need a more extensive list of parameters, try:

See dm-crypt/System configuration#Kernel parameters for details.

To use encryption on top of LVM, the LVM volumes are set up first and then used as the base for the encrypted partitions. This way, a mixture of encrypted and non-encrypted volumes/partitions is possible as well.

The following short example creates a LUKS on LVM setup and mixes in the use of a key-file for the /home partition and a temporary encrypted volume for swap. This is considered desirable from a security perspective, because no potentially sensitive temporary data survives the reboot, when the encryption is re-initialised. If you are experienced with LVM, you will be able to ignore/replace LVM and other specifics according to your plan.

If you want to span a logical volume over multiple disks that have already been set up, or expand the logical volume for /home (or any other volume), a procedure to do so is described in dm-crypt/Specialties#Expanding LVM on multiple disks. It is important to note that the LUKS encrypted container has to be resized as well.

This article or section needs expansion.

Randomise /dev/sda2 according to dm-crypt/Drive preparation#dm-crypt wipe on an empty device or partition.

Create a file system on unlocked LUKS device and mount it. For example, to create an Ext4 file system, run:

More information about the encryption options can be found in dm-crypt/Device encryption#Encryption options for LUKS mode. Note that /home will be encrypted in #Encrypting logical volume /home.

Create a file system on the partition intended for /boot. For an EFI system partition on UEFI systems, execute the following command to format the newly created partition:

or for an ordinary boot partition on BIOS systems:

Afterwards create the directory for the mountpoint and mount the partition:

Make sure the lvm2 package is installed.

If using the default busybox-based initramfs, add the keyboard, encrypt and lvm2 hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the keymap and consolefont hooks, respectively.

If using a systemd-based initramfs, instead add the keyboard, sd-encrypt and lvm2 hooks. if you use a non-US console keymap or a non-default console font, additionally add the sd-vconsole hook.

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

In order to unlock the encrypted root partition at boot, the following kernel parameters need to be set by the boot loader:

If using the sd-encrypt hook, the following need to be set instead:

The device-UUID refers to the UUID of the LUKS superblock, in this example it is the UUID of /dev/MyVolGroup/cryptroot. See Persistent block device naming for details.

See dm-crypt/System configuration#Kernel parameters for details.

Both crypttab and fstab entries are required to both unlock the device and mount the file systems, respectively. The following lines will re-encrypt the swap volume on each reboot:

Since this scenario uses LVM as the primary and dm-crypt as secondary mapper, each encrypted logical volume requires its own encryption. Yet, unlike the temporary file systems configured with volatile encryption above, the logical volume for /home should of course be persistent. The following assumes you have rebooted into the installed system, otherwise you have to adjust paths. To save on entering a second passphrase at boot, a keyfile is created:

The logical volume is encrypted with it:

Create a file system on unlocked LUKS device and mount it. For example, to create an Ext4 file system, run:

The encrypted mount is configured in both crypttab and fstab:

This example is based on a real-world setup for a workstation class laptop equipped with two SSDs of equal size, and an additional HDD for bulk storage. The end result is LUKS based full disk encryption (including /boot) for all drives, with the SSDs in a RAID0 array, and keyfiles used to unlock all encryption after GRUB is given a correct passphrase at boot.

This setup utilizes a very simplistic partitioning scheme, with all the available RAID storage being mounted at / (no separate /boot partition), and the decrypted HDD being mounted at /data.

Please note that regular backups are very important in this setup. If either of the SSDs fail, the data contained in the RAID array will be practically impossible to recover. You may wish to select a different RAID level if fault tolerance is important to you.

The encryption is not deniable in this setup.

For the sake of the instructions below, the following block devices are used:

Be sure to substitute them with the appropriate device designations for your setup, as they may be different.

Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

For BIOS systems with GPT, create a BIOS boot partition with size of 1 MiB for GRUB to store the second stage of BIOS boot loader. Do not mount the partition.

For UEFI systems create an EFI system partition with an appropriate size, it will later be mounted at /efi.

In the remaining space on the drive create a partition (/dev/sda3 in this example) for "Linux RAID". Choose partition type ID fd for MBR or partition type GUID A19D880F-05FC-4D3B-A006-743F0F84911E for GPT.

Once partitions have been created on /dev/sda, the following commands can be used to clone them to /dev/sdb.

The HDD is prepared with a single Linux partition covering the whole drive at /dev/sdc1.

Create the RAID array for the SSDs.

This example utilizes RAID0 for root, you may wish to substitute a different level based on your preferences or requirements.

As explained in dm-crypt/Drive preparation, the devices are wiped with random data utilizing /dev/zero and a crypt device with a random key. Alternatively, you could use dd with /dev/random or /dev/urandom, though it will be much slower.

And repeat above for the HDD (/dev/sdc1 in this example).

Set up encryption for /dev/md/root:

Create a file system on unlocked LUKS device. For example, to create an Ext4 file system, run:

Mount the root volume to /mnt:

And repeat for the HDD:

For UEFI systems, format the newly created EFI system partition and mount it:

Configure GRUB for the LUKS encrypted system by editing /etc/default/grub with the following:

If you have a USB keyboard on a newer system either enable legacy USB support in firmware or add the following to /etc/default/grub:

Otherwise you may not be able to use your keyboard at the LUKS prompt.

See dm-crypt/System configuration#Kernel parameters and GRUB#Encrypted /boot for details.

Complete the GRUB install to both SSDs (in reality, installing only to /dev/sda will work).

The next steps save you from entering your passphrase twice when you boot the system (once so GRUB can unlock the LUKS device, and second time once the initramfs assumes control of the system). This is done by creating a keyfile for the encryption and adding it to the initramfs image to allow the encrypt hook to unlock the root device. See dm-crypt/Device encryption#With a keyfile embedded in the initramfs for details.

Edit fstab to mount the root and data block devices and the ESP:

Save the RAID configuration:

Edit mkinitcpio.conf to include your keyfile and add the proper hooks:

See dm-crypt/System configuration#mkinitcpio for details.

Contrary to LUKS, dm-crypt plain mode does not require a header on the encrypted device: this scenario exploits this feature to set up a system on an unpartitioned, encrypted disk that will be indistinguishable from a disk filled with random data, which could allow deniable encryption. See also wikipedia:Disk encryption#Full disk encryption.

Note that if full disk encryption is not required, the methods using LUKS described in the sections above are better options for both system encryption and encrypted partitions. LUKS features like key management with multiple passphrases/key-files, master key backups or re-encrypting a device in-place are unavailable with plain mode.

Plain dm-crypt encryption can be more resilient to damage than LUKS, because it does not rely on an encryption master-key which can be a single-point of failure if damaged or forcefully destroyed. However, using plain mode also requires more manual configuration of encryption options to achieve the same cryptographic strength. See also Data-at-rest encryption#Cryptographic metadata. Using plain mode could also be considered if concerned with the problems explained in dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD).

The scenario uses two USB sticks:

It is vital that the mapped device is filled with random data. In particular this applies to the scenario use case we apply here.

See dm-crypt/Drive preparation and dm-crypt/Drive preparation#dm-crypt specific methods

See dm-crypt/Device encryption#Encryption options for plain mode for details.

Using the device /dev/sda, with the aes-xts cipher with a 512 bit key size and using a keyfile we have the following options for this scenario:

Unlike encrypting with LUKS, the above command must be executed in full whenever the mapping needs to be re-established, so it is important to remember the cipher, and key file details.

We can now check a mapping entry has been made for /dev/mapper/cryptlvm:

Next, we setup LVM logical volumes on the mapped device. See Install Arch Linux on LVM for further details:

We format and mount them and activate swap. See File systems#Create a file system for further details:

The /boot partition can be a typical FAT32 formatted partition on a USB stick, if required. But if manual partitioning is needed, then a small 1 GiB partition is all that is required. Create the partition using a partitioning tool of your choice.

Create a file system on the newly created partition intended for /boot:

Make sure the lvm2 package is installed.

If using the default busybox-based initramfs, add the keyboard, encrypt and lvm2 hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the keymap and consolefont hooks, respectively.

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

In order to boot the encrypted root partition, the following kernel parameters need to be set by the boot loader (note that 64 is the number of bytes in 512 bits):

The disk-ID-of-disk refers to the id of the referenced disk. See Persistent block device naming for details.

See dm-crypt/System configuration#Kernel parameters for details and other parameters that you may need.

You may wish to remove the USB sticks after booting. Since the /boot partition is not usually needed, the noauto option can be added to the relevant line in /etc/fstab:

However, when an update to anything used in the initramfs, or a kernel, or the boot loader is required; the /boot partition must be present and mounted. As the entry in fstab already exists, it can be mounted simply with:

This setup utilizes the same partition layout and configuration as the previous #LVM on LUKS section, with the difference that the GRUB boot loader is used since it is capable of booting from an LVM logical volume and a LUKS-encrypted /boot. See also GRUB#Encrypted /boot.

The disk layout in this example is:

Prior to creating any partitions, you should inform yourself about the importance and methods to securely erase the disk, described in dm-crypt/Drive preparation.

For UEFI systems create an EFI system partition with an appropriate size, it will later be mounted at /efi.

For BIOS/GPT setups create a BIOS boot partition with size of 1 MiB for GRUB to store the second stage of BIOS boot loader. Do not mount the partition. For BIOS/MBR setups this is not necessary.

Create a partition of type 8309, which will later contain the encrypted container for the LVM.

Create the LUKS encrypted container:

For more information about the available cryptsetup options see the LUKS encryption options prior to above command.

Your partition layout should look similar to this:

The decrypted container is now available at /dev/mapper/cryptlvm.

The LVM logical volumes of this example follow the exact layout as the #LVM on LUKS scenario. Therefore, please follow #Preparing the logical volumes above and adjust as required.

For UEFI systems, create a mountpoint for the EFI system partition at /efi for compatibility with grub-install and mount it:

At this point, you should have the following partitions and logical volumes inside of /mnt:

Now at this point resume the common Installation guide#Installation steps. Return to this page to customize the Initramfs and Boot loader steps.

Make sure the lvm2 package is installed.

If using the default busybox-based initramfs, add the keyboard, encrypt and lvm2 hooks to mkinitcpio.conf. If you use a non-US console keymap or a non-default console font, additionally add the keymap and consolefont hooks, respectively.

If using a systemd-based initramfs, instead add the keyboard, sd-encrypt and lvm2 hooks. if you use a non-US console keymap or a non-default console font, additionally add the sd-vconsole hook.

Regenerate the initramfs after saving the changes. See dm-crypt/System configuration#mkinitcpio for details and other hooks that you may need.

Configure GRUB to allow booting from /boot on a LUKS encrypted partition:

Set the kernel parameters, so that the initramfs can unlock the encrypted root partition. Using the encrypt hook:

If using the sd-encrypt hook, the following need to be set instead:

See dm-crypt/System configuration#Kernel parameters and GRUB#Encrypted /boot for details. The device-UUID refers to the UUID of the LUKS superblock, in this example it is the UUID of /dev/sda3 (the partition which holds the lvm containing the root file system). See Persistent block device naming.

install GRUB to the mounted ESP for UEFI booting:

install GRUB to the disk for BIOS booting:

Generate GRUB's configuration file:

If all commands finished without errors, GRUB should prompt for the passphrase to unlock the /dev/sda3 partition after the next reboot.

This article or section is a candidate for merging with Dm-crypt/Device encryption#With a keyfile embedded in the initramfs.

While GRUB asks for a passphrase to unlock the LUKS encrypted partition after above instructions, the partition unlock is not passed on to the initramfs. Hence, you have to enter the passphrase twice at boot: once for GRUB and once for the initramfs.

This section deals with extra configuration to let the system boot by only entering the passphrase once, in GRUB. This is accomplished by with a keyfile embedded in the initramfs.

First create a keyfile and add it as LUKS key:

Add the keyfile to the initramfs image:

Regenerate the initramfs.

Set the following kernel parameters to unlock the LUKS partition with the keyfile. Using the encrypt hook:

When using the sd-encrypt hook, /etc/cryptsetup-keys.d/name.key will be used by default, so no additional kernel parameters need to be set.

If for some reason the keyfile fails to unlock the boot partition, systemd will fallback to ask for a passphrase to unlock and, in case that is correct, continue booting.

To avoid having to memorise a complicated password, or using a simple one which may be guessed, a keyfile stored on an external USB drive can be used to unlock the LUKS volume. For this to be secure, this USB drive must be stored securely away from the computer when not in use.

First, generate a keyfile in the same way as in #Avoiding having to enter the passphrase twice. Do not use the same keyfile as if the USB drive is lost or compromised you will need to replace the keyfile embedded in initramfs.

Copy this keyfile to your USB drive and create a new GRUB configuration file:

Create a GRUB image and install it (not all of these modules will be needed depending on your file system):

This article or section is being considered for removal.

To use dm-crypt with ZFS, see ZFS#Encryption in ZFS using dm-crypt.

Additionally, ZFS features native encryption, which may also be utilized to encrypt the system root, excluding the boot loader and file system metadata. See:

After the installation, a boot loader can be verified with Secure Boot on UEFI-based systems.

**Examples:**

Example 1 (unknown):
```unknown
--pbkdf-memory
```

Example 2 (unknown):
```unknown
cryptsetup luksFormat --pbkdf pbkdf2
```

Example 3 (unknown):
```unknown
+-----------------------+------------------------+-----------------------+
| Boot partition        | LUKS encrypted root    | Optional free space   |
|                       | partition              | for additional        |
|                       |                        | partitions to be set  |
| /boot                 | /                      | up later              |
|                       |                        |                       |
|                       | /dev/mapper/root       |                       |
|                       |------------------------|                       |
| /dev/sda1             | /dev/sda2              |                       |
+-----------------------+------------------------+-----------------------+
```

Example 4 (unknown):
```unknown
# cryptsetup -v luksFormat /dev/sda2
# cryptsetup open /dev/sda2 root
```

---

## Network configuration/Wireless

**URL:** https://wiki.archlinux.org/title/Rfkill

**Contents:**
- Device driver
  - Check the driver status
  - Installing driver/firmware
- Utilities
  - iw and wireless_tools comparison
- iw
  - Get the name of the interface
  - Get the status of the interface
  - Activate the interface
  - Discover access points

The main article on network configuration is Network configuration.

Configuring wireless is a two-part process; the first part is to identify and ensure the correct driver for your wireless device is installed (they are available on the installation media, but often have to be installed explicitly), and to configure the interface. The second is choosing a method of managing wireless connections. This article covers both parts, and provides additional links to wireless management tools.

The #iw section describes how to manually manage your wireless network interface / your wireless LANs using iw. The Network configuration#Network managers section describes several programs that can be used to automatically manage your wireless interface, some of which include a GUI and all of which include support for network profiles (useful when frequently switching wireless networks, like with laptops).

The default Arch Linux kernel is modular, meaning many of the drivers for machine hardware reside on the hard drive and are available as modules. At boot, udev takes an inventory of your hardware and loads appropriate modules (drivers) for your corresponding hardware, which will in turn allow creation of a network interface.

Some wireless chipsets also require firmware, in addition to a corresponding driver. Many firmware images are provided by the linux-firmware package; however, proprietary firmware images are not included and have to be installed separately. This is described in #Installing driver/firmware.

To check if the driver for your card has been loaded, check the output of the lspci -k or lsusb -v command, depending on if the card is connected by PCIe or USB. You should see that some kernel driver is in use, for example:

Also check the output of the ip link command to see if a wireless interface was created; usually the naming of the wireless network interfaces starts with the letters "wl", e.g. wlan0 or wlp2s0. Then bring the interface up with:

For example, assuming the interface is wlan0, this is ip link set wlan0 up.

Check kernel messages for firmware being loaded:

If there is no relevant output, check the messages for the full output for the module you identified earlier (iwlwifi in this example) to identify the relevant message or further issues:

If the kernel module is successfully loaded and the interface is up, you can skip the next section.

Check the following lists to discover if your card is supported:

Note that some vendors ship products that may contain different chip sets, even if the product identifier is the same. Only the USB ID (for USB devices) or PCI ID (for PCIe devices) is authoritative.

If your wireless card is listed above, follow the #Troubleshooting drivers and firmware subsection of this page, which contains information about installing drivers and firmware of some specific wireless cards. Then check the driver status again.

If your wireless card is not listed above, it is likely supported only under Windows (some Broadcom, 3com, etc). For these, you can try to use ndiswrapper.

Just like other network interfaces, the wireless ones are controlled with ip from the iproute2 package.

Managing a wireless connection can be accomplished using network manager which will use wpa_supplicant or iwd for wireless authentication, or using wpa_supplicant or iwd directly. For lower level configuring, or if you are using a legacy driver or a legacy authentication method, there are iw and the deprecated wireless_tools.

The table below gives an overview of comparable commands for iw and wireless_tools. See Replacing iwconfig with iw for more examples.

Examples in this section assume that your wireless device interface is interface and that you are connecting to your_essid Wi-Fi access point. Replace both accordingly.

To get the name of your wireless interface, do:

The name of the interface will be output after the word "Interface". For example, it is commonly wlan0.

To check link status, use the following command.

You can get statistic information, such as the amount of tx/rx bytes, signal strength etc., with the following command:

Some cards require that the kernel interface be activated before you can use iw or wireless_tools:

To verify that the interface is up, inspect the output of the following command:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

To see what access points are available:

The important points to check:

You might need to set the proper operating mode of the wireless card. More specifically, if you are going to connect an ad-hoc network, you need to set the operating mode to ibss:

Depending on the encryption, you need to associate your wireless device with the access point to use and pass the encryption key:

Regardless of the method used, you can check if you have associated successfully:

This article or section needs expansion.

There are mainly two options for Wi-Fi authentication on Linux: wpa_supplicant and iwd.

WPA2 Personal, a.k.a. WPA2-PSK, is a mode of Wi-Fi Protected Access.

You can authenticate to WPA2 Personal networks using wpa_supplicant or iwd, or connect using a network manager. If you only authenticated to the network, then to have a fully functional connection, you will still need to assign the IP address(es) and routes either manually or using a DHCP client.

WPA2 Enterprise is a mode of Wi-Fi Protected Access. It provides better security and key management than WPA2 Personal, and supports other enterprise-type functionality, such as VLANs and NAP. However, it requires an external authentication server, called RADIUS server, to handle the authentication of users. This is in contrast to Personal mode which does not require anything beyond the wireless router or access points (APs), and uses a single passphrase or password for all users.

The Enterprise mode enables users to log onto the Wi-Fi network with a username and password and/or a digital certificate. Since each user has a dynamic and unique encryption key, it also helps to prevent user-to-user snooping on the wireless network, and improves encryption strength.

This section describes the configuration of network clients to connect to a wireless access point with WPA2 Enterprise mode. See Software access point#RADIUS for information on setting up an access point itself.

For a comparison of protocols, see the following table.

WPA2-Enterprise wireless networks demanding MSCHAPv2 type-2 authentication with PEAP sometimes require pptpclient in addition to the stock ppp package. netctl seems to work out of the box without ppp-mppe, however. In either case, usage of MSCHAPv2 is discouraged as it is highly vulnerable, although using another method is usually not an option.

eduroam is an international roaming service for users in research, higher education and further education, based on WPA2 Enterprise.

WPA3 Personal, a.k.a. WPA3-SAE, is a mode of Wi-Fi Protected Access.

Both wpa_supplicant and iwd support WPA3 Personal.

WPA3 Enterprise is a mode of Wi-Fi Protected Access.

wpa_supplicant (since version 2:2.10-8) supports WPA3 Enterprise. See FS#65314.

The regulatory domain, or "regdomain", is used to reconfigure wireless drivers to make sure that wireless hardware usage complies with local laws set by the FCC, ETSI and other organizations. Regdomains use ISO 3166-1 alpha-2 country codes. For example, the regdomain of the United States would be "US", China would be "CN", etc.

Regdomains affect the availability of wireless channels. In the 2.4GHz band, the allowed channels are 1-11 for the US, 1-14 for Japan, and 1-13 for most of the rest of the world. In the 5GHz band, the rules for allowed channels are much more complex. In either case, consult this list of WLAN channels for more detailed information.

Regdomains also affect the limit on the effective isotropic radiated power (EIRP) from wireless devices. This is derived from transmit power/"tx power", and is measured in dBm/mBm (1dBm=100mBm) or mW (log scale). In the 2.4GHz band, the maximum is 30dBm in the US and Canada, 20dBm in most of Europe, and 20dBm-30dBm for the rest of the world. In the 5GHz band, maximums are usually lower. Consult the wireless-regdb for more detailed information (EIRP dBm values are in the second set of brackets for each line).

Misconfiguring the regdomain can be useful - for example, by allowing use of an unused channel when other channels are crowded, or by allowing an increase in tx power to widen transmitter range. However, this is not recommended as it could break local laws and cause interference with other radio devices.

The kernel loads the database directly when wireless-regdb is installed. For direct loading, the kernel should, for security's sake, be configured with CONFIG_CFG80211_USE_KERNEL_REGDB_KEYS set to yes to allow for cryptographic verification of the database. This is true of the stock Arch kernel, but if you are using an alternate kernel, or compiling your own, you should verify this. More information is available at this guide[dead link 2024-07-30—domain name not resolved].

To configure the regdomain, install wireless-regdb and reboot, then edit /etc/conf.d/wireless-regdom and uncomment the appropriate domain.

The current regdomain can be temporarily set to the United States with:

However, setting the regdomain may not alter your settings. Some devices have a regdomain set in firmware/EEPROM, which dictates the limits of the device, meaning that setting regdomain in software can only increase restrictions, not decrease them. For example, a CN device could be set in software to the US regdomain, but because CN has an EIRP maximum of 20dBm, the device will not be able to transmit at the US maximum of 30dBm.

For example, to see if the regdomain is being set in firmware for an Atheros device:

For other chipsets, it may help to search for "EEPROM", "regdomain", or simply the name of the device driver.

To see if your regdomain change has been successful, and to query the number of available channels and their allowed transmit power:

wpa_supplicant can also use a regdomain in the country= line of /etc/wpa_supplicant/wpa_supplicant.conf.

It is also possible to configure the cfg80211 kernel module to use a specific regdomain by adding, for example, options cfg80211 ieee80211_regdom=JP as module options. The module option is inherited from the old regulatory implementation and in modern kernels act as a userspace regulatory hint as if it came through nl80211 through utilities like iw and wpa_supplicant.

Many laptops have a hardware button (or switch) to turn off the wireless card; however, the card can also be blocked by the kernel. This can be handled by rfkill(8). To show the current status:

If the card is hard-blocked, use the hardware button (switch) to unblock it. If the card is not hard-blocked but soft-blocked, use the following command:

Hardware buttons to toggle wireless cards are handled by a vendor specific kernel module. Frequently, these are WMI modules. Particularly for very new hardware models, it happens that the model is not fully supported in the latest stable kernel yet. In this case, it often helps to search the kernel bug tracker for information and report the model to the maintainer of the respective vendor kernel module, if it has not happened already.

See Power saving#Network interfaces.

This section contains general troubleshooting tips, not strictly related to problems with drivers or firmware. For such topics, see next section #Troubleshooting drivers and firmware.

If you have problematic hardware and need internet access to, for example, download some software or get help in forums, you can make use of Android's built-in feature for internet sharing via USB cable. See Android tethering#USB tethering for more information.

A good first measure to troubleshoot is to analyze the system's logfiles first. In order not to manually parse through them all, it can help to open a second terminal/console window and watch the kernels messages with

while performing the action, e.g. the wireless association attempt.

When using a tool for network management, the same can be done for systemd with

Frequently, a wireless error is accompanied by a deauthentication with a particular reason code, for example:

Looking up the reason code might give a first hint. Maybe it also helps you to look at the control message flowchart, the journal messages will follow it.

The individual tools used in this article further provide options for more detailed debugging output, which can be used in a second step of the analysis, if required.

This article or section is out of date.

Before changing the channel to auto, make sure your wireless interface is down. After it has successfully changed it, you can bring the interface up again and continue from there.

If you are on a public wireless network that may have a captive portal, make sure to query an HTTP page (not an HTTPS page) from your web browser, as some captive portals only redirect HTTP. If this is not the issue, check if you can resolve domain names, it may be necessary to use the DNS server advertised via DHCP.

Wireless hardware disables RTS and fragmentation by default. These are two different methods of increasing throughput at the expense of bandwidth (i.e. reliability at the expense of speed). These are useful in environments with wireless noise or many adjacent access points, which may create interference leading to timeouts or failing connections.

Packet fragmentation improves throughput by splitting up packets with size exceeding the fragmentation threshold. The maximum value (2346) effectively disables fragmentation since no packet can exceed it. The minimum value (256) maximizes throughput, but may carry a significant bandwidth cost.

RTS improves throughput by performing a handshake with the access point before transmitting packets with size exceeding the RTS threshold. The maximum threshold (2347) effectively disables RTS since no packet can exceed it. The minimum threshold (0) enables RTS for all packets, which is probably excessive for most situations.

If your journal says wlan0: deauthenticating from MAC by local choice (reason=3) and you lose your Wi-Fi connection, it is likely that you have a bit too aggressive power-saving on your Wi-Fi card. Try disabling the wireless card's power saving features (specify off instead of on).

If your card does not support enabling/disabling power save mode, check the BIOS for power management options. Disabling PCI-Express power management in the BIOS of a Lenovo W520 resolved this issue.

If you are experiencing frequent disconnections and your journal shows messages such as

ieee80211 phy0: wlan0: No probe response from AP xx:xx:xx:xx:xx:xx after 500ms, disconnecting

try changing the channel bandwidth to 20MHz through your router's settings page.

On some laptop models with hardware rfkill switches (e.g., Thinkpad X200 series), due to wear or bad design, the switch (or its connection to the mainboard) might become loose over time resulting in seemingly random hardblocks/disconnects when you accidentally touch the switch or move the laptop. There is no software solution to this, unless your switch is electrical and the BIOS offers the option to disable the switch. If your switch is mechanical (and most are), there are lots of possible solutions, most of which aim to disable the switch: Soldering the contact point on the mainboard or Wi-Fi card, gluing or blocking the switch, using a screw nut to tighten the switch or removing it altogether.

Another cause for frequent disconnects or a complete failure to connect may also be a sub-standard router, incomplete settings of the router, interference by other wireless devices or low quality signal.

To troubleshoot, first try to connect to the router with no authentication and by getting closer to it. If it does not work, reboot the router and try with another device first.

If that works, enable WPA/WPA2 again but choose fixed and/or limited router settings. For example:

On some wireless network adapters (e.g. Qualcomm Atheros AR9485), random disconnects can happen with a DMA error:

A possible workaround is to disable the Intel IOMMU driver (DMA), adding intel_iommu=off to the kernel parameters [4].

If you are using a device with iwlwifi and iwlmvm for wireless connectivity, and your Wi-Fi card appears to disappear when on battery power (perhaps after a reboot or resuming from suspend), this can be fixed by configuring power saving settings in iwlmvm.

Create the file /etc/modprobe.d/iwlmvm.conf if it does not exist already, then add the following line to it:

A power_scheme of 1 sets iwlmvm to "Always Active." Available options are:

This fix was discovered at [5].

If your device undergoes long periods of inactivity (e.g. a file server), the disconnection may be due to power saving, which will block incoming traffic and prevent connections. Try disabling power saving for the interface:

You can create a udev rule to do this on boot, see Power management#Network interfaces.

If you notice occasional interruptions when connected to a mesh network (e.g., Wi-Fi 6) and notice a message such as:

You are experiencing roaming issues. Depending on your mean of connection and the issue at hand, one could:

If the computer's Wi-Fi channels do not match those of the user's country, some in-range Wi-Fi networks might be invisible because they use wireless channels that are not allowed by default. The solution is to configure the regulatory domain correctly; see #Respecting the regulatory domain.

This section covers methods and procedures for installing kernel modules and firmware for specific chipsets, that differ from generic method.

See Kernel modules for general information on operations with modules.

Some chipsets require additional firmware: linux-firmware-mediatek

Unified driver for Ralink chipsets (it replaces rt2500, rt61, rt73, etc). This driver has been in the Linux kernel since 2.6.24, you only need to load the right module for the chip: rt2400pci, rt2500pci, rt2500usb, rt61pci or rt73usb which will autoload the respective rt2x00 modules too.

A list of devices supported by the modules is available at the project's homepage.

For devices which use the rt3090 chipset, it should be possible to use the rt2800pci driver; however, it does not work with this chipset very well (e.g. sometimes it is not possible to use higher rate than 2Mb/s).

The rt3290 chipset is recognised by the kernel rt2800pci module. However, some users experience problems and reverting to a patched Ralink driver seems to be beneficial in these cases.

New chipset as of 2012. It may require proprietary drivers from Ralink. Different manufacturers use it; see the Belkin N750 DB wireless usb adapter forums thread.

New chipset as of 2014, released under their new commercial name MediaTek. It is an AC1200 or AC1300 chipset. Manufacturer provides drivers for Linux on their support page. As of kernel 5.5 it should be supported by the included mt76 driver.

DFS channels are currently not supported in 5 GHz AP mode.

There are some high latency problems with these MediaTek chipsets. To fix this, the only solution is to disable ASPM:

This configuration file will take effect on next reboot or after reloading the module with modprobe:

These are also sometimes branded as AMD RZ608 (mt7921) and RZ616 (mt7922).

This article or section is out of date.

See [7] for a list of Realtek chipsets and specifications.

The driver is now in the kernel, but many users have reported being unable to make a connection although scanning for networks does work.

8192cu-dkmsAUR includes many patches; try this if it does not work fine with the driver in kernel.

The rtl8723ae and rtl8723be modules are included in the mainline Linux kernel.

Some users may encounter errors with powersave on this card. This is shown with occasional disconnects that are not recognized by high level network managers (netctl, NetworkManager). This error can be confirmed by running dmesg -w as root or journalctl -f as root and looking for output related to powersave and the rtl8723ae/rtl8723be module. If you have this issue, use the fwlps=0 kernel module parameter which should prevent the Wi-Fi card from automatically sleeping and halting connection.

If you have poor signal, perhaps your device has only one physical antenna connected, and antenna autoselection is broken. You can force the choice of antenna with ant_sel=1 or ant_sel=2 kernel option. [8]

Realtek chipsets rtl8811au, rtl8812au, rtl8814au and rtl8821au designed for various USB adapters ranging from AC600 to AC1900. Several packages provide various kernel drivers, these require DKMS (the dkms package and the kernel headers installed):

rtl8821cu-dkms-gitAUR provides a kernel module for the Realtek 8811cu and 8821cu chipset.

This requires DKMS, so make sure you have your proper kernel headers installed.

If no wireless interface shows up even though the 8821cu module is loaded, you may need to manually specify the rtw_RFE_type kernel module parameter [9][10]. Try e.g. rtw_RFE_type=0x26, other values might also work.

rtl8821ce-dkms-gitAUR provides a kernel module for the Realtek 8821ce chipset found in the Asus X543UA.

This requires DKMS, so make sure you have your proper kernel headers installed.

rtl88x2bu-dkms-gitAUR provides a kernel module for the Realtek 8822bu chipset found in the Edimax EW7822ULC USB3, Asus AC53 Nano USB 802.11ac and TP-Link Archer T3U adapter.

This requires DKMS, so make sure you have your proper kernel headers installed.

This article or section needs expansion.

Issues with the rtl8xxxu mainline kernel module may be solved by compiling a third-party module for the specific chipset. The source code can be found in GitHub repositories.

Some drivers may be already prepared in the AUR, e.g. rtl8723bu-dkms-gitAUR, rtl8852au-dkms-gitAUR, rtl8852bu-dkms-gitAUR, rtl8852cu-dkms-gitAUR.

RWT88 kernel module is included in all officially supported Arch Linux kernels. The number of supported devices grew over time, currently it supports most RTW88 chip devices if configured and compiled to do so.

As of Linux 6.10.3, the driver supports: 882BE (possibly), 8703B, 8723CS, 8723D, 8723DE, 8723DS, 8723DU, 8723X, 8821C, 8821CE, 8821CS, 8821CU, 8822B, 8822BE, 8822BS, 8822BU, 8822C, 8822CE, 8822CS, 8822CU.

To get more up-to-date list, Ctrl+F CONFIG_RTW88_ linux's config or check out wireless-next upstream.

Make sure that wireless-regdom is configured. Otherwise, you will be able to see all Wi-Fi networks, but will not be able to connect. Out-of-tree driver rtl88x2bu-dkms-gitAUR can connect without such configuration, so it's important to set regulatory domain when switching from it.

Here is how those symptoms look in dmesg:

The RTW89 kernel module has been merged into the upstream kernel and provides support for newer Realtek wireless chipsets.

This driver supports: 8852AE, 8851BE, 8852BE, and 8852CE.

On some computers, you may experience unstable connections. It seems like a common issue on late models from HP and Lenovo. Try disabling ASPM-related features using the config below.

There are different drivers for devices with Atheros chipset:

There are some other drivers for some Atheros devices. See Linux Wireless documentation for details.

If you find web pages randomly loading very slow, or if the device is unable to lease an IP address, try to switch from hardware to software encryption by loading the ath5k module with nohwcrypt=1 option. See Kernel modules#Setting module options for details.

Some laptops may have problems with their wireless LED indicator flickering red and blue. To solve this problem, do:

For alternatives, see this bug report.

As of Linux 3.15.1, some users have been experiencing a decrease in bandwidth. In some cases, this can fixed by setting the nohwcrypt=1 kernel module parameter for the ath9k module.

Although Linux Wireless says that dynamic power saving is enabled for Atheros ath9k single-chips newer than AR9280, for some devices (e.g. AR9285), powertop might still report that power saving is disabled. In this case, enable it manually.

On some devices (e.g. AR9285), enabling the power saving might result in the following error:

The solution is to set the ps_enable=1 kernel module parameter for the ath9k module.

iwlegacy is the wireless driver for Intel's 3945 and 4965 wireless chips. The firmware is included in the linux-firmware package.

udev should load the driver automatically, otherwise load iwl3945 or iwl4965 manually. See Kernel modules for details.

If you have problems connecting to networks in general (e.g. random failures with your card on bootup or your link quality is very poor), try to disable 802.11n:

iwlwifi is the wireless driver for Intel's current wireless chips, such as 5100AGN, 5300AGN, and 5350AGN. See the full list of supported devices.

If you have problems connecting to networks in general or your link quality is very poor, try to disable 802.11n, and perhaps also enable software encryption:

If you have a problem with slow uplink speed you may try disabling power saving for your wireless adapter.

If you have an 802.11ax (Wi-Fi 6) access point and have problems detecting the beacons or an unreliable connection, review Intel Article 54799.

If you have difficulty connecting a bluetooth headset and maintaining good downlink speed, try disabling Bluetooth coexistence:

Make sure your firmware is fully updated before trying anything else.

You may have some issue where the driver outputs stack traces & errors, which can cause some stuttering.

Alternatively, you may simply experience miscellaneous issues (e.g. connection issues on 5GHz, random disconnections, no connection on resume).

To confirm it is the cause of the issues, downgrade the package linux-firmware.

If confirmed, move the buggy firmware files so that an older version is loaded (to be able to have an up to date linux-firmware since it is not only providing firmware updates for your Intel Wi-Fi card):

To avoid having to repeat these steps manually after each update, use the NoExtract and NoUpgrade arrays in pacman.conf with a wildcard to block their installation.

If the Wi-Fi adapter is not getting detected after finishing a session in Windows, this might be due to Windows' Fast Startup feature which is enabled by default. Try disabling Fast Startup. The iwlwifi kernel driver wiki has an entry for this.

The default settings on the module are to have the LED blink on activity. Some people find this extremely annoying. To have the LED on solid when Wi-Fi is active, you can use the systemd-tmpfiles:

Run systemd-tmpfiles --create phy0-led.conf for the change to take effect, or reboot.

To see all the possible trigger values for this LED:

The aic8800-dkmsAUR package should be used with these devices. These drivers are out of the mainline Linux kernel and require DKMS.

For this chip variant, aic8800d80-dkmsAUR package should be used instead of the one mentioned above.

See Broadcom wireless.

Treat this Tenda card as an rt2870sta device. See #rt2x00.

This should be a part of the kernel package and be installed already.

Some Orinoco chipsets are Hermes II. You can use the wlags49_h2_cs driver instead of orinoco_cs and gain WPA support. To use the driver, blacklist orinoco_cs first.

The driver p54 is included in kernel, but you have to download the appropriate firmware for your card from this site and install it into the /usr/lib/firmware directory.

zd1211rw is a driver for the ZyDAS ZD1211 802.11b/g USB WLAN chipset, and it is included in recent versions of the Linux kernel. See [12] for a list of supported devices. You only need to install the firmware for the device, provided by the zd1211-firmwareAUR package.

Host AP is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3 chipset. The driver is included in Linux kernel.

Ndiswrapper is a wrapper script that allows you to use some Windows drivers in Linux. You will need the .inf and .sys files from your Windows driver.

Follow these steps to configure ndiswrapper.

The ndiswrapper install is almost finished; you can load the module at boot.

Test that ndiswrapper will load now:

See Network configuration#Listing network interfaces for more assurance the wireless interface now exists.

If you have problems, some help is available at: ndiswrapper howto and ndiswrapper FAQ.

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -knnd ::0280
```

Example 2 (unknown):
```unknown
00:14.3 Network controller [0280]: Intel Corporation BE201 320MHz [8086:a840] (rev 10)
	Subsystem: Intel Corporation Device [8086:00e4]
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
```

Example 3 (unknown):
```unknown
dmesg | grep usbcore
```

Example 4 (unknown):
```unknown
usbcore: registered new interface driver rtl8187
```

---

## GRUB

**URL:** https://wiki.archlinux.org/title/GRUB

**Contents:**
- Supported file systems
- UEFI systems
  - Installation
  - Secure Boot support
    - CA Keys
    - Shim-lock
    - Using Secure Boot
- BIOS systems
  - GUID Partition Table (GPT) specific instructions
  - Master Boot Record (MBR) specific instructions

GRUB (GRand Unified Bootloader) is a boot loader. The current GRUB is also referred to as GRUB 2. The original GRUB, or GRUB Legacy, corresponds to versions 0.9x. This page exclusively describes GRUB 2.

GRUB bundles its own support for multiple file systems, notably FAT32, ext4, Btrfs or XFS. See #Unsupported file systems for some caveats.

First, install the packages grub and efibootmgr: GRUB is the boot loader while efibootmgr is used by the GRUB installation script to write boot entries to NVRAM.

Then follow the below steps to install GRUB to your disk:

After the above installation completed, the main GRUB directory is located at /boot/grub/. Read /Tips and tricks#Alternative install method for how to specify an alternative location. Note that grub-install also tries to create an entry in the firmware boot manager, named GRUB in the above example – this will, however, fail if your boot entries are full or the systems prevents the boot order from being manipulated (e.g. Thinkpad BIOSs have a setting called "Boot Order Lock" which needs to be disabled for efibootmgr to be able to add/remove entries); use efibootmgr to remove unnecessary entries.

See UEFI troubleshooting in case of problems. Additionally see /Tips and tricks#UEFI further reading.

GRUB fully supports secure boot utilising either CA keys or shim; the installation command, however, is different depending on which you intend to use.

To make use of CA Keys the command is:

When using Shim-lock, GRUB can only be successfully booted in Secure Boot mode if its EFI binary includes all of the modules necessary to read the filesystem containing the vmlinuz and initramfs images.

Since GRUB version 2.06.r261.g2f4430cc0, loading modules in Secure Boot Mode via insmod is no longer allowed, as this would violate the expectation to not sideload arbitrary code. If the GRUB modules are not embedded in the EFI binary, and GRUB tries to sideload/insmod them, GRUB will fail to boot with the message:

Ubuntu, according to its official build script, embeds the following GRUB modules in its signed GRUB EFI binary grubx64.efi:

You must construct your list of GRUB modules in the form of a shell variable that we denote as GRUB_MODULES. You can use the latest Ubuntu script as a starting point, and trim away modules that are not necessary on your system. Omitting modules will make the boot process relatively faster, and save some space on the ESP partition.

You also need a Secure Boot Advanced Targeting (SBAT) file/section included in the EFI binary, to improve the security; if GRUB is launched from the UEFI shim loader. This SBAT file/section contains metadata about the GRUB binary (version, maintainer, developer, upstream URL) and makes it easier for shim to block certain GRUB versions from being loaded if they have security vulnerabilities[1][2], as explained in the UEFI shim boot loader secure boot life-cycle improvements document from shim.

The first-stage UEFI boot loader shim will fail to launch grubx64.efi if the SBAT section from grubx64.efi is missing!

If GRUB is installed, a sample SBAT .csv file is provided under /usr/share/grub/sbat.csv.

Reinstall GRUB using the provided /usr/share/grub/sbat.csv file and all the needed GRUB_MODULES and sign it:

Reboot, select the key in MokManager, and Secure Boot should be working.

After installation see Secure Boot#Implementing Secure Boot for instructions on enabling it.

If you are using the CA Keys method then key management, enrollment, and file signing can be automated by using sbctl, see Secure Boot#Assisted process with sbctl for details.

On a BIOS/GPT configuration, a BIOS boot partition is required. GRUB embeds its core.img into this partition.

Create a mebibyte partition (+1M with fdisk or gdisk) on the disk with no file system and with partition type GUID 21686148-6449-6E6F-744E-656564454649.

This partition can be in any position order but has to be on the first 2 TiB of the disk. This partition needs to be created before GRUB installation. When the partition is ready, install the boot loader as per the instructions below.

The space before the first partition can also be used as the BIOS boot partition though it will be out of GPT alignment specification. Since the partition will not be regularly accessed performance issues can be disregarded, though some disk utilities will display a warning about it. In fdisk or gdisk create a new partition starting at sector 34 and spanning to 2047 and set the type. To have the viewable partitions begin at the base consider adding this partition last.

Usually the post-MBR gap (after the 512 byte MBR region and before the start of the first partition) in many MBR partitioned systems is 31 KiB when DOS compatibility cylinder alignment issues are satisfied in the partition table. However a post-MBR gap of about 1 to 2 MiB is recommended to provide sufficient room for embedding GRUB's core.img (FS#24103). It is advisable to use a partitioning tool that supports 1 MiB partition alignment to obtain this space as well as to satisfy other non-512-byte-sector issues (which are unrelated to embedding of core.img).

Install the grub package. (It will replace grub-legacyAUR if that is already installed.) Then do:

where i386-pc is deliberately used regardless of your actual architecture, and /dev/sdX is the disk (not a partition) where GRUB is to be installed. For example /dev/sda or /dev/nvme0n1, or /dev/mmcblk0. See Device file#Block device names for a description of the block device naming scheme.

Now you must generate the main configuration file.

If you use LVM for your /boot, you can install GRUB on multiple physical disks.

See grub-install(8) and GRUB Manual for more details on the grub-install command.

On an installed system, GRUB loads the /boot/grub/grub.cfg configuration file each boot. You can follow #Generated grub.cfg for using a tool, or #Custom grub.cfg for a manual creation.

This section only covers editing the /etc/default/grub configuration file. See /Tips and tricks for more information.

After the installation, the main configuration file /boot/grub/grub.cfg needs to be generated. The generation process can be influenced by a variety of options in /etc/default/grub and scripts in /etc/grub.d/. For the list of options in /etc/default/grub and a concise description of each refer to GNU's documentation.

If you have not done additional configuration, the automatic generation will determine the root filesystem of the system to boot for the configuration file. For that to succeed it is important that the system is either booted or chrooted into.

Use the grub-mkconfig tool to generate /boot/grub/grub.cfg:

By default the generation scripts automatically add menu entries for all installed Arch Linux kernels to the generated configuration.

To automatically add entries for other installed operating systems, see #Detecting other operating systems.

You can add additional custom menu entries by editing /etc/grub.d/40_custom and re-generating /boot/grub/grub.cfg. Or you can create /boot/grub/custom.cfg and add them there. Changes to /boot/grub/custom.cfg do not require re-running grub-mkconfig, since /etc/grub.d/41_custom adds the necessary source statement to the generated configuration file.

See #Boot menu entry examples for custom menu entry examples.

To have grub-mkconfig search for other installed systems and automatically add them to the menu, install the os-prober package and mount the partitions from which the other systems boot. Then re-run grub-mkconfig. If you get the following output: Warning: os-prober will not be executed to detect other bootable partitions then edit /etc/default/grub and add/uncomment:

For Windows installed in UEFI mode, make sure the EFI system partition containing the Windows Boot Manager (bootmgfw.efi) is mounted. Run os-prober as root to detect and generate an entry for it.

For Windows installed in BIOS mode, mount the Windows system partition (its file system label should be System Reserved or SYSTEM). Run os-prober as root to detect and generate an entry for it.

To pass custom additional arguments to the Linux image, you can set the GRUB_CMDLINE_LINUX + GRUB_CMDLINE_LINUX_DEFAULT variables in /etc/default/grub. The two are appended to each other and passed to kernel when generating regular boot entries. For the recovery boot entry, only GRUB_CMDLINE_LINUX is used in the generation.

It is not necessary to use both, but can be useful. For example, you could use GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID=uuid-of-swap-partition quiet" where uuid-of-swap-partition is the UUID of your swap partition to enable resume after hibernation. This would generate a recovery boot entry without the resume and without quiet suppressing kernel messages during a boot from that menu entry. Though, the other (regular) menu entries would have them as options.

By default grub-mkconfig determines the UUID of the root filesystem for the configuration. To disable this, uncomment GRUB_DISABLE_LINUX_UUID=true.

For generating the GRUB recovery entry you have to ensure that GRUB_DISABLE_RECOVERY is not set to true in /etc/default/grub.

See Kernel parameters for more info.

By default, grub-mkconfig sorts the included kernels using sort -V and uses the first kernel in that list as the top-level entry. This means that, for example, since /boot/vmlinuz-linux-lts is sorted before /boot/vmlinuz-linux, if you have both linux-lts and linux installed, the LTS kernel will be the top-level menu entry, which may not be desirable. This can be overridden by specifying GRUB_TOP_LEVEL="path_to_kernel" in /etc/default/grub. For example, to make the regular kernel be the top-level menu entry, you can use GRUB_TOP_LEVEL="/boot/vmlinuz-linux".

This article or section is a candidate for merging with #Installation.

If you use LVM for your /boot or / root partition, make sure that the lvm module is preloaded:

This article or section is a candidate for merging with #Installation.

GRUB provides convenient handling of RAID volumes. You need to load GRUB modules mdraid09 or mdraid1x to allow you to address the volume natively:

For example, /dev/md0 becomes:

whereas a partitioned RAID volume (e.g. /dev/md0p1) becomes:

To install grub when using RAID1 as the /boot partition (or using /boot housed on a RAID1 root partition), on BIOS systems, simply run grub-install on both of the drives, such as:

Where the RAID 1 array housing /boot is housed on /dev/sda and /dev/sdb.

GRUB also has special support for booting with an encrypted /boot. This is done by unlocking a LUKS blockdevice in order to read its configuration and load any initramfs and kernel from it. This option tries to solve the issue of having an unencrypted boot partition.

To enable this feature encrypt the partition with /boot residing on it using LUKS as normal. Then add the following option to /etc/default/grub:

This option is used by grub-install to generate the grub core.img.

Make sure to install grub after modifying this option or encrypting the partition.

Without further changes you will be prompted twice for a passphrase: the first for GRUB to unlock the /boot mount point in early boot, the second to unlock the root filesystem itself as implemented by the initramfs. You can use a keyfile to avoid this.

Use grub-install as described in the #Installation section to create a bootable GRUB image with LUKS support. Note the following caveats:

If you enter an invalid passphrase during boot and end up at the GRUB rescue shell, try cryptomount -a to mount all (hopefully only one) encrypted partitions or use cryptomount -u $crypto_uuid to mount a specific one. Then proceed with insmod normal and normal as usual.

If you enter a correct passphrase, but an Invalid passphrase error is immediately returned, make sure that the right cryptographic modules are specified. Use cryptsetup luksDump /dev/nvme0n1p2 and check whether the hash function (SHA-256, SHA-512) matches the modules (gcry_sha256, gcry_sha512) installed and the PBKDF algorithm is pbkdf2. The hash and PBDKDF algorithms can be changed for existing keys by using cryptsetup luksConvertKey --hash sha256 --pbkdf pbkdf2 /dev/nvme0n1p2. Under normal circumstances it should take a few seconds before the passphrase is processed.

This article or section needs expansion.

This section describes the manual creation of GRUB boot entries in /boot/grub/grub.cfg instead of relying on grub-mkconfig.

A basic GRUB config file uses the following options:

For GRUB to set the LoaderDevicePartUUID UEFI variable required by systemd-gpt-auto-generator(8) for GPT partition automounting, load the bli module in grub.cfg:

For tips on managing multiple GRUB entries, for example when using both linux and linux-lts kernels, see /Tips and tricks#Multiple entries.

For Archiso and Archboot boot menu entries see Multiboot USB drive#Boot entries.

When launched in UEFI mode, GRUB can chainload other EFI binaries.

You can launch UEFI Shell by placing it in the root of the EFI system partition and adding this menu entry:

Download the gdisk EFI application and copy gdisk_x64.efi to esp/EFI/tools/.

If you have a unified kernel image generated from following Secure Boot or other means, you can add it to the boot menu. For example:

Assuming that the other distribution is on partition sda2:

Alternatively let GRUB search for the right partition by UUID or file system label:

If the other distribution has already a valid /boot folder with installed GRUB, grub.cfg, kernel and initramfs, GRUB can be instructed to load these other grub.cfg files on-the-fly during boot. For example, for hd0 and the fourth GPT partition:

When choosing this entry, GRUB loads the grub.cfg file from the other volume and displays that menu. Any environment variable changes made by the commands in file will not be preserved after configfile returns. Press Esc to return to the first GRUB menu.

This mode determines where the Windows boot loader resides and chain-loads it after GRUB when the menu entry is selected. The main task here is finding the EFI system partition and running the boot loader from it.

where $hints_string and $fs_uuid are obtained with the following two commands.

The $fs_uuid command determines the UUID of the EFI system partition:

Alternatively one can run lsblk --fs and read the UUID of the EFI system partition from there.

The $hints_string command will determine the location of the EFI system partition, in this case harddrive 0:

These two commands assume the ESP Windows uses is mounted at esp. There might be case differences in the path to Windows's EFI file, what with being Windows, and all.

Throughout this section, it is assumed your Windows partition is /dev/sda1. A different partition will change every instance of hd0,msdos1.

In both examples XXXX-XXXX is the filesystem UUID which can be found with command lsblk --fs.

For Windows Vista/7/8/8.1/10:

Do not use bootrec.exe /Fixmbr because it will wipe GRUB out. Or you can use Boot Repair function in the Troubleshooting menu - it will not wipe out GRUB but will fix most errors. Also you would better keep plugged in both the target hard drive and your bootable device ONLY. Windows usually fails to repair boot information if any other devices are connected.

It is possible to use file system labels, human-readable strings attached to file systems, by using the --label option to search. First of all, make sure your file system has a label.

Then, add an entry using labels. An example of this:

Since the MBR is too small to store all GRUB modules, only the menu and a few basic commands reside there. The majority of GRUB functionality remains in modules in /boot/grub/, which are inserted as needed. In error conditions (e.g. if the partition layout changes) GRUB may fail to boot. When this happens, a command shell may appear.

GRUB offers multiple shells/prompts. If there is a problem reading the menu but the boot loader is able to find the disk, you will likely be dropped to the "normal" shell:

If there is a more serious problem (e.g. GRUB cannot find required files), you may instead be dropped to the "rescue" shell:

The rescue shell is a restricted subset of the normal shell, offering much less functionality. If dumped to the rescue shell, first try inserting the "normal" module, then starting the "normal" shell:

GRUB supports pager for reading commands that provide long output (like the help command). This works only in normal shell mode and not in rescue mode. To enable pager, in GRUB command shell type:

The GRUB's command shell environment can be used to boot operating systems. A common scenario may be to boot Windows / Linux stored on a drive/partition via chainloading.

Chainloading means to load another boot-loader from the current one, ie, chain-loading.

The other boot loader may be embedded at the start of a partitioned disk (MBR), at the start of a partition or a partitionless disk (VBR), or as an EFI binary in the case of UEFI.

X=0,1,2... Y=1,2,3...

For example to chainload Windows stored in the first partition of the first hard disk,

Similarly GRUB installed to a partition can be chainloaded.

insmod fat is used for loading the FAT file system module for accessing the Windows boot loader on the UEFI system partition. (hd0,gpt4) or /dev/sda4 is the UEFI system partition in this example. The entry in the chainloader line specifies the path of the .efi file to be chain-loaded.

See the examples in #Using the rescue console

See #Using the command shell first. If unable to activate the standard shell, one possible solution is to boot using a live CD or some other rescue disk to correct configuration errors and reinstall GRUB. However, such a boot disk is not always available (nor necessary); the rescue console is surprisingly robust.

The available commands in GRUB rescue include insmod, ls, set, and unset. This example uses set and insmod. set modifies variables and insmod inserts new modules to add functionality.

Before starting, the user must know the location of their /boot partition (be it a separate partition, or a subdirectory under their root):

where X is the physical drive number and Y is the partition number.

To expand console capabilities, insert the linux module:

This introduces the linux and initrd commands, which should be familiar.

An example, booting Arch Linux:

With a separate boot partition (e.g. when using UEFI), again change the lines accordingly:

After successfully booting the Arch Linux installation, users can correct grub.cfg as needed and then reinstall GRUB.

To reinstall GRUB and fix the problem completely, changing /dev/sda if needed. See #Installation for details.

Before removing grub, make sure that some other boot loader is installed and configured to take over.

If BootOrder has grub as the first entry, install another boot loader to put it in front, such as systemd-boot above. grub can then be removed using its bootnum.

Also delete the esp/EFI/grub and /boot/grub directories.

To replace grub with any other BIOS boot loader, simply install them, which will overwrite the MBR boot code.

grub-install creates the /boot/grub directory that needs to be removed manually. Though some users will want to keep it, should they want to install grub again.

After migrating to UEFI/GPT one may want to remove the MBR boot code using dd.

In case that GRUB does not support the root file system, an alternative /boot partition with a supported file system must be created. In some cases, the development version of GRUB grub-gitAUR may have native support for the file system.

If GRUB is used with an unsupported file system it is not able to extract the UUID of your drive so it uses classic non-persistent /dev/sdXx names instead. In this case you might have to manually edit /boot/grub/grub.cfg and replace root=/dev/sdXx with root=UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. You can use the blkid command to get the UUID of your device, see Persistent block device naming.

While GRUB supports F2FS since version 2.0.4, it cannot correctly read its boot files from an F2FS partition that was created with the extra_attr flag enabled.

This error may occur when you try installing GRUB in a VMware container. Read more about it here. It happens when the first partition starts just after the MBR (block 63), without the usual space of 1 MiB (2048 blocks) before the first partition. Read #Master Boot Record (MBR) specific instructions

grub-install automatically tries to create a menu entry in the boot manager. If it does not, then see UEFI#efibootmgr for instructions to use efibootmgr to create a menu entry. However, the problem is likely to be that you have not booted your CD/USB in UEFI mode, as in Installation guide#Verify the boot mode.

As another example of creating a GRUB entry in the firmware boot manager, consider efibootmgr -c. This assumes that /dev/sda1 is the EFI System Partition, and is mounted at /boot/efi. Which are the default behavior of efibootmgr. It creates a new boot option, called "Linux", and puts it at the top of the boot order list. Options may be passed to modify the default behavior. The default OS Loader is \EFI\arch\grub.efi.

If GRUB loads but drops into the rescue shell with no errors, it can be due to one of these two reasons:

An example of a working UEFI:

If the screen only goes black for a second and the next boot option is tried afterwards, according to this post, moving GRUB to the partition root can help. The boot option has to be deleted and recreated afterwards. The entry for GRUB should look like this then:

Some UEFI firmwares require a bootable file at a known location before they will show UEFI NVRAM boot entries. If this is the case, grub-install will claim efibootmgr has added an entry to boot GRUB, however the entry will not show up in the VisualBIOS boot order selector. The solution is to install GRUB at the default/fallback boot path:

Alternatively you can move an already installed GRUB EFI executable to the default/fallback path:

If trying to boot Windows results in an "invalid signature" error, e.g. after reconfiguring partitions or adding additional hard drives, (re)move GRUB's device configuration and let it reconfigure:

grub-mkconfig should now mention all found boot options, including Windows. If it works, remove /boot/grub/device.map-old.

If booting gets stuck without any error message after GRUB loading the kernel and the initial ramdisk, try removing the add_efi_memmap kernel parameter.

Some have reported that other distributions may have trouble finding Arch Linux automatically with os-prober. If this problem arises, it has been reported that detection can be improved with the presence of /etc/lsb-release. This file and updating tool is available with the package lsb-release.

When installing GRUB on a LVM system in a chroot environment (e.g. during system installation), you may receive warnings like

This is because /run is not available inside the chroot. These warnings will not prevent the system from booting, provided that everything has been done correctly, so you may continue with the installation.

GRUB can take a long time to load when disk space is low. Check if you have sufficient free disk space on your /boot or / partition when you are having problems.

GRUB may output error: unknown filesystem and refuse to boot for a few reasons. If you are certain that all UUIDs are correct and all filesystems are valid and supported, it may be because your BIOS Boot Partition is located outside the first 2 TiB of the drive [4]. Use a partitioning tool of your choice to ensure this partition is located fully within the first 2 TiB, then reinstall and reconfigure GRUB.

This error might also be caused by an ext4 filesystem having unsupported features set:

GRUB seems to be unable to write to root Btrfs partitions [5]. If you use grub-reboot to boot into another entry it will therefore be unable to update its on-disk environment. Either run grub-reboot from the other entry (for example when switching between various distributions) or consider a different file system. You can reset a "sticky" entry by executing grub-editenv create and setting GRUB_DEFAULT=0 in your /etc/default/grub (do not forget grub-mkconfig -o /boot/grub/grub.cfg).

If a drive is formatted with Btrfs without creating a partition table (eg. /dev/sdx), then later has partition table written to, there are parts of the BTRFS format that persist. Most utilities and OS's do not see this, but GRUB will refuse to install, even with --force

You can zero the drive, but the easy solution that leaves your data alone is to erase the Btrfs superblock with wipefs -o 0x10040 /dev/sdx

A setting in Windows 8/10 called "Hiberboot", "Hybrid Boot" or "Fast Boot" can prevent the Windows partition from being mounted, so grub-mkconfig will not find a Windows install. Disabling Hiberboot in Windows will allow it to be added to the GRUB menu.

When using an encrypted /boot, and you fail to input a correct password, you will be dropped in grub-rescue prompt.

This grub-rescue prompt has limited capabilities. Use the following commands to complete the boot:

See this blog post for a better description.

Check /etc/default/grub if GRUB_TIMEOUT is set to 0, in which case set it to a positive number: it sets the number of seconds before the default GRUB entry is loaded. Also check if GRUB_TIMEOUT_STYLE is set to hidden and set it to menu, so that the menu will be shown by default. Then regenerate the main configuration file and reboot to check if it worked.

If it does not work, there may be incompatibility problems with the graphical terminal. Set GRUB_TERMINAL_OUTPUT to console in /etc/default/grub to disable the GRUB graphical terminal.

See Fixing Lenovo’s ERROR CODE 1962 by spoofing the EFI boot entries.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

You can do it manually or use a pacman hook, for example:

Change grub-install options such as the --efi-directory path to match your settings.

**Examples:**

Example 1 (unknown):
```unknown
grubx64.efi
```

Example 2 (unknown):
```unknown
grubx64.efi
```

Example 3 (unknown):
```unknown
grub-mkstandalone
```

Example 4 (unknown):
```unknown
grub-install
```

---

## rEFInd

**URL:** https://wiki.archlinux.org/title/REFInd

**Contents:**
- Supported file systems
- Installation
- Installing the rEFInd Boot Manager
  - Installation with refind-install script
    - Secure Boot
      - Using PreLoader
      - Using shim
        - Using hashes
        - Using Machine Owner Key
      - Using your own keys

rEFInd is a UEFI boot manager capable of launching kernels as EFI boot stubs. It is a fork of the no-longer-maintained rEFIt and fixes many issues with respect to non-Mac UEFI booting. It is designed to be platform-neutral and to simplify booting multiple operating systems.

rEFInd inherits the support for the file systems from the firmware (i.e. at least FAT12, FAT16 and FAT32). Additionally it loads any UEFI drivers placed in the drivers and drivers_x64 subdirectories of its own installation directory on the ESP. E.g. esp/EFI/refind/drivers_x64/.

rEFInd also ships with a small collection of read-only EFI file system drivers, notably ext4 and Btrfs.

Install the refind package.

rEFInd ships with UEFI drivers that implement read-only support for ReiserFS (deprecated), Ext2, Ext4, Btrfs, ISO-9660 and HFS+. Additionally rEFInd can access any file system that UEFI itself can, that includes FAT (as mandated by the UEFI specification), HFS+ on Macs and ISO-9660 on some systems.

To find additional drivers see The rEFInd Boot Manager: Using EFI Drivers: Finding Additional EFI Drivers.

To use the rEFInd, you must install it to the EFI system partition either using the refind-install script or by copying the files and setting up the boot entry manually.

The rEFInd package includes the refind-install script to simplify the process of setting rEFInd as your default EFI boot entry. The script has several options for handling differing setups and UEFI implementations. See refind-install(8) or read the comments in the install script for explanations of the various installation options.

For many systems it should be sufficient to simply run:

This will attempt to find and mount your ESP, copy rEFInd files to esp/EFI/refind/, and use efibootmgr to make rEFInd the default EFI boot application.

Alternatively you can install rEFInd to the default/fallback boot path esp/EFI/BOOT/bootx64.efi. This is helpful for bootable USB flash drives or on systems that have issues with the NVRAM changes made by efibootmgr:

Where /dev/sdXY is your EFI system partition (the block device, not its mountpoint).

After installing rEFInd's files to the ESP, verify that rEFInd has created refind_linux.conf containing kernel parameters in the same directory as your kernel. This configuration file will not be created if you used the --usedefault option, run mkrlconf as root to create it.

By default, rEFInd will scan all of your drives (that it has drivers for) and add a boot entry for each EFI boot loader it finds, which should include your kernel (since Arch enables EFI boot stubs by default). So you may have a bootable system at this point.

See Managing Secure Boot for Secure Boot support in rEFInd.

See Secure Boot#Set up PreLoader to acquire signed PreLoader.efi and HashTool.efi binaries.

Execute refind-install with the option --preloader /path/to/preloader

Next time you boot with Secure Boot enabled, HashTool will launch and you will need to enroll the hash of rEFInd (loader.efi), rEFInd's drivers (e.g. ext4_x64.efi) and kernel (e.g. vmlinuz-linux).

See refind-install(8) for more information.

Install shim-signedAUR. Read Secure Boot#shim, but skip all file copying.

To use only hashes with shim, execute refind-install with the option --shim /path/to/shim

Next time you boot with Secure Boot enabled, MokManager will launch and you will need to enroll the hash of rEFInd (grubx64.efi), rEFInd's drivers (e.g. ext4_x64.efi) and kernel (e.g. vmlinuz-linux).

To sign rEFInd with a Machine Owner Key (MOK), install sbsigntools.

Execute refind-install with the options --shim /path/to/shim and --localkeys:

refind-install will create the keys for you and sign itself and its drivers. You will need to sign the kernel with the same key, e.g.:

Once in MokManager add refind_local.cer to MoKList. refind_local.cer can be found inside a directory called keys in the rEFInd's installation directory, e.g. esp/EFI/refind/keys/refind_local.cer.

See refind-install(8) for more information.

Follow Secure Boot#Using your own keys to create keys.

Create directory /etc/refind.d/keys and place Signature Database (db) key and certificates in it. Name the files: refind_local.key (PEM format private key), refind_local.crt (PEM format certificate) and refind_local.cer (DER format certificate).

When running install script add option --localkeys, e.g.:

rEFInd EFI binaries will be signed with the supplied key and certificate.

If the refind-install script does not work for you, rEFInd can be set up manually.

First, copy the executable to the ESP:

If you want to install rEFInd to the default/fallback boot path replace esp/EFI/refind/ with esp/EFI/BOOT/ in the following instructions and copy rEFInd EFI executable to esp/EFI/BOOT/bootx64.efi:

Then use efibootmgr to create a boot entry in the UEFI NVRAM, where /dev/sdX and Y are the device and partition number of your EFI system partition. If you are installing rEFInd to the default/fallback boot path esp/EFI/BOOT/bootx64.efi, you can skip this step.

At this point, you should be able to reboot into rEFInd, but it may not be able to boot your kernel. If your kernel does not reside on your ESP, rEFInd may need to mount your partitions to find it. If the relevant file systems are not of the types supported by UEFI, additional driver files may be necessary. rEFInd automatically loads all drivers from the subdirectories drivers and drivers_arch (e.g. drivers_x64) in its install directory.

Now rEFInd should have a boot entry for your kernel, but it will not pass the correct kernel parameters. Set up #Passing kernel parameters. You should now be able to boot your kernel using rEFInd. If you are still unable to boot or if you want to tweak rEFInd's settings, many options can be changed with a configuration file:

The sample configuration file is well commented and self-explanatory.

Unless you have set textonly in the configuration file, you should copy rEFInd's icons to get rid of the ugly placeholders:

You can try out different fonts by copying them and changing the font setting in refind.conf:

Pacman updates the rEFInd files in /usr/share/refind/ and will not copy new files to the ESP for you. If refind-install worked for your original installation of rEFInd, you can rerun it to copy the updated files. The new configuration file will be copied as refind.conf-sample so that you can integrate changes into your existing configuration file using a diff tool. If your rEFInd required #Manual installation, you will need to figure out which files to copy yourself.

You can automate the update process using a pacman hook:

Where the Exec= may need to be changed to the correct update command for your setup. If you did #Manual installation, you could create your own update script to call with the hook.

The rEFInd configuration refind.conf is located in the same directory as the rEFInd EFI application (usually esp/EFI/refind or esp/EFI/BOOT). The default configuration file contains extensive comments explaining all its options, see Configuring the Boot Manager for more detailed explanations.

rEFInd detects bootable EFI binaries (Linux kernels, other operating system boot loaders, UEFI boot entries and etc.) at runtime. This means that in most simple situations, rEFInd works without any configuration. In particular, it is likely possible to boot Windows by default.

This does not mean there is no need to configure; for Linux, probably a user wants to set kernel parameters and initramfs. This can be done in another configuration file, refind_linux.conf. See below for details.

There are two methods for setting the kernel parameters that rEFInd will pass to the kernel.

rEFInd has two (or more) configuration files. refind.conf, which lies in the ESP, configures rEFInd itself. On the other hand refind_linux.conf lies in /boot, i.e. the directory that kernel images lie, and it configures how the kernels are booted.

For automatically detected kernels you can either specify the kernel parameters explicitly in /boot/refind_linux.conf or rely on rEFInd's ability to identify the root partition and kernel parameters. See Methods of Booting Linux: For Those With Foresight or Luck: The Easiest Method for more information.

For rEFInd to support the naming scheme of Arch Linux kernels and thus allow matching them with their respective initramfs images, you must uncomment and edit extra_kernel_version_strings option in refind.conf. E.g.:

If rEFInd automatically detects your kernel, you can place a refind_linux.conf file containing the kernel parameters in the same directory as your kernel. You can use /usr/share/refind/refind_linux.conf-sample as a starting point. The first uncommented line of refind_linux.conf will be the default parameters for the kernel. Subsequent lines will create entries in a submenu accessible using Insert, F2, Tab, or +.

Alternatively, try running mkrlconf as root. It will attempt to find your kernel in /boot and automatically generate refind_linux.conf. The script will only set up the most basic kernel parameters, so be sure to check the file it created for correctness.

If you do not specify an initrd= parameter, rEFInd will automatically add it by searching for common RAM disk filenames in the same directory as the kernel. If you need either multiple or non-default initrd= parameters, you must specify them manually in refind_linux.conf. For example:

If you merely install rEFInd onto the ESP and launch it without any further ado (say via UEFI shell or KeyTool, or directly from firmware) you still get a menu to boot from via autodetection, with no configuration required whatsoever.

This works because rEFInd has a fallback mechanism that can:

If your kernel is not autodetected, or if you simply want more control over the options for a menu entry, you can manually create boot entries using stanzas in refind.conf. Ensure that scanfor includes manual or these entries will not appear in rEFInd's menu. Kernel parameters are set with the options keyword. rEFInd will append the initrd= parameter using the file specified by the initrd keyword in the stanza.

Manual boot stanzas are explained in Creating Manual Boot Stanzas.

It is likely that you will need to change volume to match either a filesystem's LABEL, a PARTLABEL, or a PARTUUID of the partition where the kernel image resides. See Persistent block device naming#by-label for examples of assigning a volume label. If volume is not specified it defaults to volume from which rEFInd was launched (typically EFI system partition).

rEFInd is compatible with the EFI system partition created by a UEFI Windows installation, so there is no need to create or format another FAT32 partition when installing Arch alongside Windows. Simply mount the existing ESP and install rEFInd as usual. By default, rEFInd's autodetection feature should recognize any existing Windows or recovery boot loaders.

This article or section is a candidate for merging with Unified Extensible Firmware Interface.

rEFInd supports running various 3rd-party tools. Tools need to be installed separately. Edit showtools in refind.conf to choose which ones to show.

See Unified Extensible Firmware Interface#UEFI Shell.

Copy shellx64.efi to the root of the EFI system partition.

Install memtest86+-efi and copy it to esp/EFI/tools/.

rEFInd can detect Secure Boot key management tools if they are placed in rEFInd's directory on ESP, esp/ or esp/EFI/tools/.

Follow #Using PreLoader and HashTool.efi will be placed in rEFInd's directory.

Follow #Using shim and MokManager will be placed in rEFInd's directory.

Place KeyTool EFI binary in esp/ or esp/EFI/tools/ with the name KeyTool.efi or KeyTool-signed.efi.

See Secure Boot#Using KeyTool for instructions on signing KeyTool.efi.

Download the gdisk EFI application and copy gdisk_x64.efi to esp/EFI/tools/.

Install fwupd-efi and setup fwupd.

Copy the fwupdx64.efi binary and firmware file to esp/EFI/tools/:

rEFInd reportedly have poweroff and reboot menu entries built in. Since this list of tools is the most extensive of its kind in this wiki, users of UEFI shell, or other UEFI boot managers, such as systemd-boot, might be interested in powerofforreboot.efiAUR.

rEFInd supports extensive customization, allowing you to modify icons, backgrounds, and fonts on the boot screen.

To customize rEFInd, you need to edit the refind.conf configuration file, found in esp/EFI/refind. In the following example, all assets will be stored in esp/EFI/refind/assets.

To set a custom background image (banner), use the wallpaper directive in refind.conf:

To set a custom set of icons, use the icons_dir directive in refind.conf and point it to the folder containing your icons:

The refind package provides a set of icons for most distributions, including Arch Linux. These icons can be found in esp/EFI/refind/icons.

Installing external themes is straightforward. First, create a themes folder in your rEFInd directory:

Clone the theme (if it is hosted on GitHub, for example):

Or, copy the theme manually:

In refind.conf, include the theme's configuration file:

This article or section is a candidate for merging with Unified Extensible Firmware Interface#UEFI drivers.

To use rEFInd's drivers in UEFI shell load them using command load and refresh mapped drives with map -r.

Now you can access your file system from UEFI shell.

This article or section needs expansion.

If the resolution in refind.conf is set to an incorrect value, on all systems except Apple Macs rEFInd will display a list of supported resolutions. For Apple Macs it will silently use the default resolution.

To determine framebuffer resolutions supported by efifb, copy /usr/lib/gnuefi/apps/modelist.efi from gnu-efi to the root of ESP. Enter the UEFI shell and run modelist.efi.

Set one in refind.conf. Reboot and check if settings has been applied by running dmesg | grep efifb as root.

To allow kernel auto detection on a Btrfs subvolume uncomment and edit also_scan_dirs in refind.conf.

Next add subvol=subvolume to rootflags in refind_linux.conf and then prepend subvolume to the initramfs path.

If booting a btrfs subvolume as root, prepend the path to the subvolume to the loader and initramfs paths, and amend the options line with rootflags=subvol=root_subvolume. In the example below, root has been mounted as a btrfs subvolume called 'ROOT' (e.g. mount -o subvol=ROOT /dev/sdxY /mnt):

A failure to do so will otherwise result in the following error message: ERROR: Root device mounted successfully, but /sbin/init does not exist.

Since version 0.13.1, rEFInd supports setting the UEFI variable LoaderDevicePartUUID. Enabling this allows systemd-gpt-auto-generator(8) to automount the EFI system partition without needing to specify it in /etc/fstab. See systemd#GPT partition automounting.

For rEFInd to set LoaderDevicePartUUID, edit refind.conf and uncomment write_systemd_vars true:

You can verify if it is set by checking its value with cat /sys/firmware/efi/efivars/LoaderDevicePartUUID-4a67b082-0a4c-41cf-b6c7-440b29bb8c4f or by looking at the state of "Boot loader sets ESP information" in bootctl output.

rEFInd does not support booting ISO files since it lacks a loopback driver, but it can boot a ISO image that has been directly written to a partition. This requires the iso9660_x64.efi driver.

Use bless from within macOS to set rEFInd as the default boot entry:

If your drivers_x64 folder contains multiple file system drivers (see #Installing the rEFInd Boot Manager for clarification), this can lead to an improper functioning of rEFInd through a file system driver bug, whereby only a blank screen and with the rEFInd logo is shown (for custom themes, this would be the set background image). To fix this, simply remove all drivers except the one for the file system on which the kernel resides.

Another potential blank screen cause occurs when dual booting with Windows, where rEFInd is unsuccessful in auto-scanning the EFI system partitions on other disks. To remedy this, use blkid to identify Windows partitions, and add the PARTUUID of each Windows partition as a comma-separated entry to the variable dont_scan_volumes in refind.conf. For example:

If you see Tux instead of the Arch Logo, then you might be affected by this issue (your root partition is of type Linux x86-64 root (/) instead of Linux filesystem).

You can fix this using fdisk#Change partition type.

Additionally, if your root partition's label is simply "Linux" or if it contains the word "linux," Tux may be displayed. To specify the name of your distribution, consider renaming the partition label to reflect your distribution's name.

You can fix this using a file system label.

Another way to get the Arch Logo instead of Tux, is to copy the Arch Logo image file next to your kernel (e.g. vmlinuz-linux) and give the image file the same name as your kernel.

If you add a menuentry and set the volume token correctly but still received the "Error: Not Found while loading vmlinuz-linux" message, you may need to check if driver for the file system on which kernel resides is correctly installed. Remember unsupported filesystem will not be detected, even if they are in the configuration file.

**Examples:**

Example 1 (unknown):
```unknown
drivers_x64
```

Example 2 (unknown):
```unknown
esp/EFI/refind/drivers_x64/
```

Example 3 (unknown):
```unknown
# refind-install
```

Example 4 (unknown):
```unknown
esp/EFI/refind/
```

---

## Swap

**URL:** https://wiki.archlinux.org/title/Swap

**Contents:**
- Swap space
- Swap partition
  - Enabling at boot
  - Disabling swap
- Swap file
  - Swap file creation
  - Swap file removal
- Swap encryption
- Performance
  - Swappiness

This page provides an introduction to swap space and paging on GNU/Linux. It covers creation and activation of swap partitions and swap files.

From All about Linux swap space:

Support for swap is provided by the Linux kernel and user-space utilities from the util-linux package.

Swap space can take the form of a disk partition or a file. Users may create a swap space during installation or at any later time as desired. Swap space can be used for two purposes, to extend the virtual memory beyond the installed physical memory (RAM), and also for suspend-to-disk support.

Whether or not it is beneficial to extend the virtual memory with swap depends on the amount of installed physical memory. If the amount of physical memory is less than the amount of memory required to run all the desired programs, then it may be beneficial to enable swap. This avoids out of memory conditions, where the Linux kernel OOM killer mechanism will automatically attempt to free up memory by killing processes. To increase the amount of virtual memory to the required amount, add the necessary difference (or more) as swap space.

The biggest drawback of using swap when running out of memory is its lower performance, see section #Performance. Hence, enabling swap is a matter of personal preference: some prefer programs to be killed over enabling swap and others prefer enabling swap and slower system when the physical memory is exhausted.

To check swap status, use:

Or to show physical memory as well as swap usage:

A swap partition can be created with most GNU/Linux partitioning tools. Swap partitions are designated by the partition type GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F on GPT (8200 type for gdisk, swap type for fdisk) and type ID 82 on MBR.

To set up a partition as Linux swap area, the mkswap(8) command is used. For example:

To enable the device for paging:

See swapon(8) for the options syntax.

To enable the swap partition at boot time, either:

See fstab for the file syntax, and systemd#systemd.mount - mounting.

To deactivate specific swap space:

Alternatively use the -a switch to deactivate all swap space.

Since swap is managed by systemd, it will be activated again on the next system startup. To disable the automatic activation of detected swap space permanently, run systemctl --type swap to find the responsible .swap unit and mask it.

As an alternative to creating an entire partition, a swap file offers the ability to vary its size on-the-fly, and is more easily removed altogether. This may be especially desirable if disk space is at a premium (e.g. a modestly-sized SSD).

Use mkswap(8) to create a swap file the size of your choosing (see Partitioning#Swap for advice). For example, creating a 4 GiB swap file:

Activate the swap file:

Finally, edit the fstab configuration to add an entry for the swap file:

As an alternative to fstab, a swap unit can be created (see systemd.swap(5)):

Perform a daemon-reload and enable swapfile.swap.

For additional information, see fstab#Usage.

To remove a swap file, it must be turned off first and then can be removed:

Finally, remove the relevant entry from /etc/fstab.

See dm-crypt/Swap encryption.

Swap operations are usually significantly slower than directly accessing data in RAM. However, disabling swap entirely to improve performance can sometimes lead to a degradation. If there is not enough physical memory available to hold everything, swapping out nothing leaves less memory available for file system caches, causing more frequent and costly disk usage.

Swap values can be adjusted to help performance:

When memory usage reaches a certain threshold, the kernel starts looking at active memory and seeing what it can free up. File data can be written out to the file system (if changed), unloaded and re-loaded later; other data must be written to swap before it can be unloaded.

The swappiness sysctl parameter represents the kernel's preference for writing to swap instead of files. It can have a value between 0 and 200 (max 100 if Linux < 5.8); the default value is 60. A low value causes the kernel to prefer freeing up open files, a high value causes the kernel to try to use swap space, and a value of 100 means IO cost is assumed to be equal.

To check the current swappiness value:

Alternatively, the file /proc/sys/vm/swappiness can be read in order to obtain the raw integer value.

To temporarily set the swappiness value:

To set the swappiness value permanently, create a sysctl.d(5) configuration file. For example:

To have the boot loader set swappiness when loading the kernel, add a kernel parameter, e.g. sysctl.vm.swappiness=35.

Reasons for choosing a different swappiness can include:

Another sysctl parameter that affects swap performance is vm.vfs_cache_pressure, which controls the tendency of the kernel to reclaim the memory which is used for caching of VFS caches, versus pagecache and swap. Increasing this value increases the rate at which VFS caches are reclaimed. For more information on what it does, see the Linux kernel documentation.

The default value is 100, which states that filesystem cache is about as important as the other caches, so they should be reclaimed at about an equal weight. On desktops it has been argued that filesystem cache is more important than the other caches because filesystem browsing times affects operation latency (perceived responsiveness) more than the other caches, resulting a suggested value of 50. On the other hand, a higher value has been suggested when the VFS cache holds metadata on many small files that are not touched again. For more information on tuning this parameter, see OpenSUSE tuning guide (which recommends experimenting and checking the types of caches via slaptop).

If you have more than one swap file or swap partition you should consider assigning a priority value (0 to 32767) for each swap area. The system will use swap areas of higher priority before using swap areas of lower priority. For example, if you have a faster disk and a slower disk, assign a higher priority to the swap area located on the fastest device. Priorities can be assigned in fstab via the pri parameter:

Or via the --priority parameter of swapon:

If two or more areas have the same priority, and it is the highest priority available, pages are allocated on a round-robin basis between them.

There is no necessity to use RAID for swap performance reasons. The kernel itself can stripe swapping on several devices, if you just give them the same priority in the /etc/fstab file. Refer to The Software-RAID HOWTO for details.

See Solid state drive#swap.

See Improving performance#Swap on zram or zswap.

If you only need swap as a hibernation image storage space, then you can use zswap and disable its writeback so that there are no disk writes from regular swap usage. See Power management/Suspend and hibernate#Disable zswap writeback to use the swap space only for hibernation.

**Examples:**

Example 1 (unknown):
```unknown
$ swapon --show
```

Example 2 (unknown):
```unknown
0657FD6D-A4AB-43C4-84E5-0933C84B4F4F
```

Example 3 (unknown):
```unknown
# mkswap /dev/sdxy
```

Example 4 (unknown):
```unknown
# swapon /dev/sdxy
```

---

## PRoot

**URL:** https://wiki.archlinux.org/title/PRoot

**Contents:**
- Installation
- Usage
- Security

PRoot is program that implements functionality similar to GNU/Linux's chroot, mount --bind, and binfmt_misc in user-space, allowing an unprivileged user to execute programs with an alternative root directory, much like a chroot "jail". This is useful in cases where a chroot is not possible due to a lack of root privileges.

PRoot can be installed from the prootAUR package. pacstrap can be used to initialize the directory with an Arch environment before running proot.

After installation, PRoot does not require root privileges. As with chroot, PRoot must be given a directory to act as the new root directory for the program to be run. If a program is not specified, PRoot will launch /bin/sh by default. Virtual filesystems do not need to be manually mounted, as PRoot handles this automatically.

At this point a shell will start, with / corresponding to the ~/chroot/ directory on the host system.

Paths may be explicitly bound using the -b option:

This makes the host's /bin/bash available at the guest's /bin/sh

PRoot internally utilizes the qemu user-mode emulator to allow programs to be run inside the PRoot even when they are compiled for an architecture other than the host system's.

This article or section needs expansion.

Like chroot, PRoot provides only filesystem level isolation. Programs inside the PRoot "jail" share the same kernel, hardware, process space, and networking subsystem. chroot and PRoot are not designed to be substitutes for real virtualization applications, such as hypervisors and paravirtualizers.

**Examples:**

Example 1 (unknown):
```unknown
mount --bind
```

Example 2 (unknown):
```unknown
$ proot -r ~/mychroot/
```

Example 3 (unknown):
```unknown
$ proot -b /bin/bash:/bin/sh
```

---

## Install Arch Linux from existing Linux

**URL:** https://wiki.archlinux.org/title/Install_from_existing_Linux

**Contents:**
- Backup and preparation
- From a host running Arch Linux
  - Create a new Arch installation
  - Create a copy of an existing Arch installation
- From a host running another Linux distribution
  - Using pacman from the host system
  - Creating a chroot
  - Using a chroot environment
    - Initializing pacman keyring
    - Downloading basic tools

This document describes the bootstrapping process required to install Arch Linux from a running Linux host system. After bootstrapping, the installation proceeds as described in the Installation guide.

Installing Arch Linux from a running Linux is useful for:

The goal of the bootstrapping procedure is to setup an environment from which the scripts from arch-install-scripts (such as pacstrap(8) and arch-chroot(8)) can be run.

If the host system runs Arch Linux, this can be achieved by simply installing arch-install-scripts. If the host system runs another Linux distribution, you will first need to set up an Arch Linux-based chroot.

Backup all your data including mails, webservers, etc. Have all information at your fingertips. Preserve all your server configurations, hostnames, etc.

Here is a list of data you will likely need:

In general, it is a good idea to have a local copy of your original /etc directory on your local hard drive.

Install the arch-install-scripts package.

Follow Installation guide#Mount the file systems to mount the filesystem that will be used for the root directory as well as all the other needed mount points. If you already use the /mnt directory for something else, just create another directory such as /mnt/install and use it as the mount point base for the rest of the installation.

At this stage, Arch Linux can either be installed from scratch or it can mirror the host installation. The two options are described thereafter.

Follow Installation guide#Installation.

In the procedure, the first step, Installation guide#Select the mirrors, can be skipped since the host should already have a correct mirrorlist.

It is possible to replicate an existing Arch Linux installation by copying the host filesystem to the new partition and make some adjustments to it to make it bootable and unique.

The first step is to copy the host files into the mounted new partition, for this, consider using the approach exhibited in rsync#Full system backup.

Then, follow the procedure described in Installation guide#Configure the system with some caveats and additional steps:

If the mirrored Arch installation may be used within a different configuration or with another hardware, consider the following additional operations:

There are multiple tools which automate a large part of the steps described in the following subsections. See their respective homepages for detailed instructions.

The manual way is presented in the following subsections. The idea is to either get pacman working directly on the host system, or to run an Arch system inside the host system, with the actual installation being executed from the Arch system. The nested system is contained inside a chroot.

Pacman can be compiled on most Linux distributions, and used directly on the host system to bootstrap Arch Linux. The arch-install-scripts should run without issues directly from the downloaded sources on any recent distribution.

Some distributions provide a package for pacman and/or arch-install-scripts in their official repositories which can be used for this purpose. As of July 2020, Void Linux is known to provide the pacman package, and Alpine Linux and Fedora are known to provide both pacman and arch-install-scripts.

Download the bootstrap tarball from a mirror into /tmp/.

Download the bootstrap tarball signature from the download page and place it in the same directory. Do not download it from a mirror.

Verify the signature with GnuPG.

Take note of the final --numeric-owner option, which is important for preserving correct UID and GID numbers of extracted files in case your existing Linux system uses different numbers than Arch Linux.

Select a repository server by editing /tmp/root.x86_64/etc/pacman.d/mirrorlist.

The bootstrap environment is really barebones (no nano or lvm2). Therefore, we need to set up pacman in order to download other necessary packages.

Before starting the installation, pacman keys need to be setup. Run the following commands:

See pacman/Package signing#Initializing the keyring for details.

Refresh the package lists and install what you need: base-devel, parted etc.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

You can now proceed to Installation guide#Mount the file systems and follow the rest of the Installation guide.

Some host systems or configurations may require certain extra steps. See the sections below for tips.

On some Debian-based host systems, pacstrap may produce the following error:

This is because in some versions of Debian, /dev/shm points to /run/shm while in the Arch-based chroot, /run/shm does not exist and the link is broken. To correct this error, create a directory /run/shm:

On Fedora based hosts and live USBs you may encounter problems when using genfstab to generate your fstab. Remove duplicate entries and the seclabel option where it appears, as this is SELinux-specific and will keep your system from booting normally.

Before rebooting, double check a few details in your installation to achieve a successful installation. To do so, first chroot into the newly-installed system, and then:

Find ~700 MiB of free space somewhere on the disk, e.g. by partitioning a swap partition. You can disable the swap partition and set up your system there.

Check cfdisk, /proc/swaps or /etc/fstab to find your swap partition. Assuming your hard drive is located on sdaX (X will be a number).

Disable the swap space:

Create a filesystem on it

Create a directory to mount it in

Finally, mount the new directory for installing the intermediate system.

Install essentials packages and any other package required to get a system with internet connection up and running in the temporary partition, being careful with the limit of ~700 MiB space. When specifying packages to be installed with pacstrap, consider adding the -c flag to avoid filling up valuable space by downloading packages to the host system.

Once the new Arch Linux system is installed, fix the boot loader configuration, then reboot into the newly created system, and rsync the entire system to the primary partition.

**Examples:**

Example 1 (unknown):
```unknown
/etc/resolv.conf
```

Example 2 (unknown):
```unknown
/etc/modules.conf
```

Example 3 (unknown):
```unknown
/mnt/install
```

Example 4 (unknown):
```unknown
/etc/pacman.conf
```

---

## USB flash installation medium

**URL:** https://wiki.archlinux.org/title/USB_flash_installation_media

**Contents:**
- Using the ISO as is (BIOS and UEFI)
  - In GNU/Linux
    - Using basic command line utilities
    - Using KDE ISO Image Writer
    - Using GNOME Disk Utility
    - Using MultiWriter
    - Using Kindd
    - Using Popsicle
    - Using SUSE Studio ImageWriter
    - Using xorriso-dd-target

This page discusses various multi-platform methods on how to create an Arch Linux Installer USB drive (also referred to as "flash drive", "USB stick", "USB key", etc) for booting in BIOS and UEFI systems. The result will be a live USB system that can be used for installing Arch Linux, system maintenance or for recovery purposes, and that, because of using Overlayfs for /, will discard all changes once the computer shuts down.

If you would like to run a full install of Arch Linux from a USB drive (i.e. with persistent settings), see Install Arch Linux on a removable medium. If you would like to use your bootable Arch Linux USB stick as a rescue USB, see chroot.

Before following any of these steps, download the ISO from https://archlinux.org/download/ and verify its integrity.

This method is recommended due to its simplicity and universal availability, since these tools are part of coreutils (pulled in by the base meta package).

Find out the name of your USB drive with ls -l /dev/disk/by-id/usb-* and check with lsblk to make sure that it is not mounted.

Run one of the following commands, replacing /dev/disk/by-id/usb-My_flash_drive with your drive, e.g. /dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0. (Do not append a partition number, so do not use something like /dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0-part1 or /dev/sdb1):

See [1] and [2] for a comparison and perspective on the use of those tools and why dd may be the least adapted one.

KDE ISO Image Writer can be downloaded via isoimagewriter. It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

Linux distributions running GNOME can easily make a live USB through nautilus and gnome-disk-utility. Simply right-click on the .iso file, and select Open With Disk Image Writer. When GNOME Disk Utility opens, specify the flash drive from the Destination drop-down menu and click Start Restoring.

gnome-multi-writer is a simple GTK3 based graphical tool to write an ISO file to one or multiple USB devices at once.

Kindd is a Qt based graphical frontend for dd. It is available as kinddAUR.

Popsicle is a tool made for flashing ISO files to multiple USB devices in parallel by the PopOS development team. It is written in Rust and uses GTK. It is available as popsicleAUR.

SUSE Studio ImageWriter is a Qt based tool made by the openSUSE development team. It is available as imagewriterAUR.

xorriso-dd-target (from libisoburn) is a shell script which attempts to reduce the risk of overwriting the wrong storage device. Its safest mode is named -plug_test. For example, to use it as a regular user who can elevate to root using sudo:

See xorriso-dd-target(1) for details.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups. It is available as usbimagerAUR.

KDE ISO Image Writer can be downloaded as .exe file at isoimagewriter. It can auto-detect the USB-drive and you need to manually select a ISO file. It is recommended to use .sig file to signature but it can be skipped by clicking "create".

win32diskimager is another graphical tool for writing images to USB sticks or SD/CF cards from Windows. Select your ISO image and the target USB drive letter (you may have to format it first to assign it a drive letter), and click Write.

This method does not require any workaround and is as straightforward as dd under Linux. Just download the Arch Linux ISO, and with local administrator rights use the USBwriter utility to write to your USB flash memory.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

Rufus is a multi-purpose USB ISO writer. It provides a graphical user interface and does not care if the drive is properly formatted or not.

Simply select the Arch Linux ISO, the USB drive you want to create the bootable Arch Linux onto and click START.

Make sure your Cygwin installation contains the dd package.

Place your image file in your home directory:

Run cygwin as administrator (required for cygwin to access hardware). To write to your USB drive use the following command:

where archlinux-version-x86_64.iso is the path to the iso image file within the cygwin directory and \\.\x: is your USB flash drive where x is the windows designated letter, e.g. \\.\d:.

On Cygwin 6.0, find out the correct partition with:

and write the ISO image with the information from the output. Example:

A GPL licensed dd version for Windows is available at http://www.chrysocome.net/dd. The advantage of this over Cygwin is a smaller download. Use it as shown in instructions for Cygwin above.

To begin, download the latest version of dd for Windows. Once downloaded, extract the archive's contents into the Downloads directory or elsewhere.

Now, launch your Command Prompt as an administrator. Next, change directory (cd) into the Downloads directory.

If your Arch Linux ISO is elsewhere you may need to state the full path, for convenience you may wish to put the Arch Linux ISO into the same folder as the dd executable. The basic format of the command will look like this.

flashnul is an utility to verify the functionality and maintenance of Flash-Memory (USB-Flash, IDE-Flash, SecureDigital, MMC, MemoryStick, SmartMedia, XD, CompactFlash etc).

From a command prompt, invoke flashnul with -p, and determine which device index is your USB drive, e.g.:

When you have determined which device is the correct one, you can write the image to your drive, by invoking flashnul with the device index, -L, and the path to your image, e.g:

As long as you are really sure you want to write the data, type yes, then wait a bit for it to write. If you get an access denied error, close any Explorer windows you have open.

First, you need to identify the USB device. Open /Applications/Utilities/Terminal and list all storage devices with the command:

Your USB device will appear as something like /dev/disk2 (external, physical). Verify that this is the device you want to erase by checking its name and size and then use its identifier for the commands below instead of /dev/diskX.

A USB device is normally auto-mounted in macOS, and you have to unmount (not eject) it before block-writing to it with dd. In Terminal, do:

Now copy the ISO image file to the device:

This command will run silently. To view progress, send SIGINFO by pressing Ctrl+t. Note diskX here should not include the s1 suffix, or else the USB device will only be bootable in UEFI mode and not legacy. After completion, macOS may complain that The disk you inserted was not readable by this computer. Select Ignore. The USB device will be bootable.

USBImager is a multiplatform graphical application that writes and verifies compressed disk images to USB drives, and creates backups.

EtchDroid is a OS image flasher for Android. It works without root permissions since Android 5. Check the upstream GitHub if you have issue.

To create an Arch Linux installer, download the ISO image file on your Android device. Plug the USB drive to your device, using a USB-OTG adapter if needed. Open EtchDroid, select Flash raw image, select your Arch ISO, then select your USB drive. Grant the USB API permission and confirm.

Keep your phone on a table while it is writing the image: a lot of USB-OTG adapters are a bit wobbly and you might unplug it by mistake.

This method is more complicated than writing the image directly with dd, but it does keep the flash drive usable for data storage (that is, the ISO is installed in a specific partition within the already partitioned device without altering other partitions).

Syslinux files for BIOS systems are already copied to /mnt/boot/syslinux/. Unmount the FAT file system, install the syslinux and mtools packages and run the following commands to make the partition bootable:

For some old BIOS systems, only booting from USB-ZIP drives is supported. This method allows you to still boot from a USB hard drive.

From here continue with the manual formatting method. The partition will be /dev/disk/by-id/usb-My_flash_drive-part4 due to the way ZIP drives work.

For UEFI-only booting, it is enough to extract the ISO contents onto a FAT-formatted USB flash drive.

It does not require creating a EFI system partition on the drive as all UEFI will happily boot any FAT volume from USB flash drives. The most compatible setup would be using the MBR partition table with a single active (bootable) primary partition of type 0c "W95 FAT32 (LBA)".[3]

This method extracts files from the ISO image to a USB flash drive.

This method copies files from the ISO image to a USB flash drive.

Neither DiskImageMounter nor Disk Utility can mount isohybrid ISOs, but since macOS ships with libarchive, the ISO can simply be extracted onto the flash drive using bsdtar.

This article or section is a candidate for merging with Multiboot USB drive.

This allows booting multiple ISOs from a single USB device, including the archiso. Updating an existing USB drive to a more recent ISO is simpler than for most other methods. See Multiboot USB drive.

Ventoy is an open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files. With Ventoy, you do not need to format the disk over and over, you just need to copy the ISO/WIM/IMG/VHD(x)EFI files to the USB drive and boot them directly. You can copy many files at a time and Ventoy will give you a boot menu to select them. It is available as ventoy-binAUR.

This method uses Syslinux and a Ramdisk (MEMDISK) to load the entire Arch Linux ISO image into RAM. Since this will be running entirely from system memory, you will need to make sure the system you will be installing this on has an adequate amount. A minimum amount of RAM between 500 MB and 1 GB should suffice for a MEMDISK based, Arch Linux install.

For more information on Arch Linux system requirements as well as those for MEMDISK see the Installation guide and here. For reference, here is the preceding forum thread.

Begin by formatting the USB flash drive as FAT32. Then create the following folders on the newly formatted drive.

Next copy the ISO that you would like to boot to the Boot/ISOs folder. After that, extract from the following files from the latest release of syslinux from here and copy them into the following folders.

After copying the needed files, navigate to the USB flash drive, Boot/Settings and create a syslinux.cfg file.

For more information see the Syslinux article.

Finally, create a *.bat file where syslinux.exe is located and run it ("Run as administrator" if you are on Vista or Windows 7):

etcher contains analytics and first-party advertising. See [4], [5] and [6].

There are two ways to add an additional (third) partition to a drive prepared using #Using the ISO as is (BIOS and UEFI).

To edit the MBR partition table on the drive, run:

Use the n command to create a new partition (leave the default values for the first and last sectors if it should span all available free size). If you want to access it in other operating systems, change the MBR partition type ID using the t command (e.g. to 0c "W95 FAT32 (LBA)" or 07 "HPFS/NTFS/exFAT"). Write the changes to disk and exit via the w command.

After partitioning, create a file system on the new partition (/dev/disk/by-id/usb-My_flash_drive-part3).

If you get the device did not show up after 30 seconds error due to /dev/disk/by-label/ARCH_YYYYMM not mounting, try renaming your USB medium to ARCH_YYYYMM so Arch can find it. (e.g. For archlinux-2021.02.01-x86_64.iso, use ARCH_202102).

If you get losetup: /run/archiso/bootmnt/arch/x86_64/airootfs.sfs: failed to set up loop devices: No such file or directory, try using a USB 2.0 port. For example, some USB 3.0 ports through USB hubs do not work.

If you get other errors, try using another USB device. There are multiple scenarios in which it solved all issues.

**Examples:**

Example 1 (unknown):
```unknown
ls -l /dev/disk/by-id/usb-*
```

Example 2 (unknown):
```unknown
/dev/disk/by-id/usb-My_flash_drive
```

Example 3 (unknown):
```unknown
/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0
```

Example 4 (unknown):
```unknown
/dev/disk/by-id/usb-Kingston_DataTraveler_2.0_408D5C1654FDB471E98BED5C-0:0-part1
```

---

## Moving an existing install into (or out of) a virtual machine

**URL:** https://wiki.archlinux.org/title/Moving_an_existing_install_into_(or_out_of)_a_virtual_machine

**Contents:**
- Moving out of a virtual machine
  - Set up a shared folder
  - Transfer the system
  - Chroot and reinstall the boot loader
  - Adjust the fstab
  - Re-generate the initramfs image
- Moving into a virtual machine
  - Create the container
  - Transfer the system
  - Convert the container to a compatible format

This article describes how to transfer your current Arch Linux installation in or out of a virtual environment (i.e. QEMU, VirtualBox, VMware). A virtual machine uses different hardware, which needs to be addressed by re-generating the initramfs image and possibly adjusting the fstab – especially if it is an SSD.

Moving out of a virtual environment is relatively easy.

Setting up a shared folder between the guest virtual machine and the host depends on the hypervisor you use. Please thus refer to their specific wiki page or manual.

If you do not already have an ext4 partition, see File systems.

The factual accuracy of this article or section is disputed.

If you are on Windows, install Ext2Fsd to be able to mount ext volumes.

From the virtual machine, open a terminal and transfer the system:

This can also be done with clonezilla boot disk or dd from a random Linux live-cd. If you are using Virtualbox you need to connect the target drive through USB (or SATA to USB cable) otherwise use an external USB drive to save the disk image (with dd or clonezilla).

Boot a "live" GNU/Linux distribution, mount the root partition and chroot into it.

Reinstall your boot loader or boot manager: either Syslinux, GRUB or systemd-boot. Do not forget to update the configuration file: syslinux.cfg for Syslinux, grub.cfg for Grub, or the systemd-boot boot entries located in /boot/loader/entries/.

Since your entire root tree has been transferred to a single partition, edit the fstab file to reflect the right partition(s).

Check with the blkid command, since lsblk is not very useful inside a chroot.

Because the hardware has changed, while you are still in the chroot, regenerate the initramfs.

And that is about it.

You will most likely need to set up the network, since the virtual machine was probably piggybacking on the host OS's network settings. See Network configuration.

Moving into a virtual environment takes a little more effort.

This will create a 32 GiB raw image:

The factual accuracy of this article or section is disputed.

If you want to create one the exact size of your root partition, run fdisk -l and use the value from the Blocks column for the count= parameter. Note that you will transfer your entire root tree, so that includes the /boot and /home folders. If you have any separate partitions for those, you need to take them into account when creating the container.

Partition the /media/Backup/backup.img file by running your favourite partitioning tool. Create a partition table on it (e.g. msdos), choose the partition scheme and create the partitions.

Now load the necessary module and mount it as a loopback device, on /dev/loop5 (for example):

Then create a file system on the partitions, which will appear as /dev/loop5p1, /dev/loop5p2, etc.

Mount the loopback device and transfer the system:

Choose the appropriate command depending on the desired virtual machine.

To convert into a KVM container, use qemu-desktop with the following command line:

To convert into a VirtualBox container, use virtualbox with the following command line:

To convert into a VMware container, use virtualbox with the following command line:

Connect the container to the virtual machine, along with a Linux LiveCD (e.g. the latest Arch Linux ISO) in the virtual machine's virtual CD-ROM, then start the virtual machine and chroot into it:

Reinstall either Syslinux or GRUB. Do not forget to update its configuration file:

Since your entire root tree has been transferred to a single partition, edit the fstab file. You may use the UUID or label if you want, but those are more useful in multi-drive, multi-partition configurations (to avoid confusions). For now, /dev/sda1 for your entire system is just fine.

Having an nvidia, nouveau, radeon, intel, etc., entry in the Device section from one of the Xorg configuration files will prevent it from starting, since you will be using emulated hardware (including the video card). So it is recommended that you move/rename or delete the following:

Because the hardware has changed, while you are still in the chroot, re-generate the initramfs image and do a proper shutdown:

Finally, pull out the LiveCD (the ISO file), so that you do not boot back into it, and start the virtual machine.

Enjoy your new virtual environment.

Use losetup --partscan, for example:

This should create device nodes for each partition you have created inside the loop device.

It most likely means that you did not run poweroff like you were instructed to, and closed the virtual machine with the "close" button, which is the equivalent of a power outage. Now you need to regenerate your initramfs image. To do that, you can start the virtual machine using the Fallback entry. If you do not have a Fallback entry, press Tab (for Syslinux) or e (for GRUB) and rename it initramfs-linux-fallback.img. After it boots, open up a terminal and run:

This means that you forgot to add the drive's UUID, label or device name in /etc/fstab. The UUID is different every time you format it (or in this case, create one from scratch), and they likely do not match. Check with blkid.

**Examples:**

Example 1 (unknown):
```unknown
# rsync -aAXHSv /* /path/to/shared/folder --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found,/home/*/.gvfs}
```

Example 2 (unknown):
```unknown
syslinux.cfg
```

Example 3 (unknown):
```unknown
/boot/loader/entries/
```

Example 4 (unknown):
```unknown
# fallocate -l 32GiB -o 1024 /media/Backup/backup.img
```

---
