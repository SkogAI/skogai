# Arch-Wiki - Filesystem

**Pages:** 34

---

## dracut

**URL:** https://wiki.archlinux.org/title/Dracut

**Contents:**
- Installation
- Usage
  - Additional options
- Advanced configuration
  - dracut modules
    - TPM2
  - Early kernel module loading
  - Kernel command line options
    - Miscellaneous notes
  - Unified kernel image

dracut creates an initial image used by the kernel for preloading the block device modules (such as IDE, SCSI or RAID) which are needed to access the root filesystem. Upon installing linux, you can choose between mkinitcpio, booster, and dracut. dracut is used by Fedora, RHEL and Gentoo, among others. Arch uses mkinitcpio by default.

You can read the full project documentation for dracut in the documentation.

Install the dracut package.

dracut is easy to use and typically does not require user configuration, even when using non-standard setups, like LVM on LUKS.

To generate an initramfs for the running kernel:

To generate a fallback initramfs run:

Note that starting from v108 of dracut, in usual configuration fallback initramfs should not be needed as the default initramfs has most of the kernel drivers already included.

/boot/initramfs-linux.img refers to the output image file. If you are using an other kernel, consider changing the file name. For example, for the linux-lts kernel, the output file should be named /boot/initramfs-linux-lts.img. However, you can name these files whatever you wish as long as your boot loader configuration uses the same file names.

The --force flag overwrites the image file if it is already present.

The --kver option specifies which kernel to use. The argument to this option must match the name of a directory present in /usr/lib/modules.

More flags can be found with dracut(8).

It is important to note that there are two distinct approaches how the various tasks during initial ramdisk phase are performed:

The concrete variant is determined by the absence or presence of the systemd dracut module. See #dracut modules for more details.

dracut can be configured by directly passing arguments on the command line (see dracut(8) § OPTIONS). If you wish to always execute dracut with a certain set of flags, you can save a specified configuration in a .conf file in /etc/dracut.conf.d/. For example:

You can see more configuration options with dracut.conf(5). Fuller descriptions of each option can be found with dracut(8). We will describe a few common options in what follows.

dracut uses a modular approach to build the initramfs (see dracut.modules(7)). All of dracut 's builtin modules are located in /lib/dracut/modules.d and can be listed with dracut --list-modules. Extra modules can be provided by external packages e.g. dracut-sshd-gitAUR. dracut 's built-in modules unfortunately lack documentation, although their names can be self-explanatory.

Some of the modules are active/inactive by default, and can be activated/deactivated with --add/--omit command line argument or with the add_dracutmodules+=""/omit_dracutmodules+="" persistent config entry lines.

For dracut module documentation, see the upstream dracut documentation.

Most dracut modules are dependent on other dracut modules. As an example the bluetooth dracut module depends on the dbus dracut module.

To make use of systemd 's unlocking of luks2 encrypted volumes using TPM2 through systemd-cryptenroll, install tpm2-tools package and enable the tpm2-tss dracut module.

Dracut enables early loading (at the initramfs stage, via modprobe) through its --force_drivers command or force_drivers+="" config entry line. For example:

Kernel command line options can be placed in a .conf file in /etc/dracut.conf.d/, and set via the kernel_cmdline= flag. Dracut will automatically source this file and create a 01-default.conf file and place it inside the initramfs directory /etc/cmdline.d/. For example, your kernel command line options file could look like:

It is not necessary to specify the root block device for dracut. From dracut.cmdline(7):

However, it may be useful to set some parameters early, and you can enable additional features like prompting for additional command line parameters. See dracut.cmdline(7) for all options. Here are some example configuration options:

dracut can produce unified kernel images with the --uefi command line option or with the uefi="yes" configuration option.

You can view information about a generated initramfs image, which you may wish to view in a pager:

This command will list the arguments passed to dracut when the image was created, the list of included dracut modules, and the list of all included files.

To reduce the amount of time spent compressing the final image, you may change the compression program used.

Simply add any one of the following lines (not multiple) to your dracut configuration:

gzip is the default compression program used. compress="cat" will make the initramfs with no compression.

You can also use a non-officially-supported compression program:

Some considerations to optimize the boot and initramfs creation performance are:

The dracut package include hooks for pacman to automatically generate new initramfs images upon each kernel upgrade.

You should stop mkinitcpio from creating and removing initramfs images as well, either by removing mkinitcpio or with the following commands:

Dracut will enable the bluetooth module automatically when a bluetooth keyboard is detected. However it is required that dracut is in hostonly mode for dracut to auto-discover bluetooth keyboard.

The limine-dracut-supportAUR package utilizes limine-entry-tool with dracut and pacman hooks to automate the installation and removal of kernels and boot entries in the Limine boot loader. See Limine#Boot entry automation for more information.

If resuming from hibernation does not work, you may need to configure dracut to include the resume module. You will need to add a configuration file:

If applicable to your system, you may also want to see instructions to resume from an encrypted swap partition including the dracut specific instructions.

If the kernel has issues auto discovering and mounting LVM / software RAID / LUKS blocks. You can retry generating an initramfs with the following kernel command line options:

If you have issues booting or very long shutdown processes while the system waits for brltty, add the following to the dracut configuration line:

Alternatively, uninstall brltty if it is not needed.

A failure to boot with a message similar to the above typically will only require the user to include the crypt module via add_dracutmodules.

**Examples:**

Example 1 (unknown):
```unknown
# dracut --add-confdir no-network /boot/initramfs-linux.img
```

Example 2 (unknown):
```unknown
# dracut -f --regenerate-all
```

Example 3 (unknown):
```unknown
# dracut -f --add-confdir rescue /boot/initramfs-linux-fallback.img
```

Example 4 (unknown):
```unknown
/boot/initramfs-linux.img
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/Repartition

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## udisks

**URL:** https://wiki.archlinux.org/title/Udisks

**Contents:**
- Installation
- Configuration
  - Permissions
  - Default mount options
- Usage
- Tips and tricks
  - Mount helpers
    - udevadm monitor
  - Mount to /media
  - Mount loop devices

udisks provides a daemon udisksd, that implements D-Bus interfaces used to query and manipulate storage devices, and a command-line tool udisksctl, used to query and use the daemon.

Install the udisks2 package.

udisksd(8) is started on-demand by D-Bus and should not be enabled explicitly. It can be controlled through the command-line with udisksctl(1).

Actions a user can perform using udisks are restricted with polkit. If the user session is not activated or present (for example, when controlling udisks from a systemd/User service), adjust polkit rules accordingly.

See https://github.com/coldfix/udiskie/wiki/Permissions for common udisks permissions for the storage group, and [1] for a more restrictive example. If you are using Dolphin, you may see [2].

It is possible to define default mount options in /etc/udisks2/mount_options.conf. Create the file if it does not already exist. The built-in defaults and some examples can be seen in /etc/udisks2/mount_options.conf.example.[3]

The options can target specific filesystem types. For example, mount btrfs filesystems with zstd compression enabled:

To manually mount a removable drive, for example /dev/sdc:

See udisksctl help for more.

The automatic mounting of devices is easily achieved with udisks wrappers. See also List of applications/Utilities#Mount tools.

You may use udevadm monitor to monitor block events and mount drives when a new block device is created. Stale mount points are automatically removed by udisksd, such that no special action is required on deletion.

By default, udisks2 mounts removable drives under the ACL controlled directory /run/media/$USER/. If you wish to mount to /media instead, use this rule:

Since /media, unlike /run, is not mounted by default as a tmpfs, you may also wish to create a tmpfiles.d snippet to clean stale mountpoints at every boot:

To easily mount ISO images, use the following command:

This will create a read only loop device and show the ISO image ready to mount. Remove the -r flag to be able to write to it. The name of the created loop device is output by the above loop-setup command.

You can unmount, and remount, the image as long as the specific loop device is in place. When done working with the specific loop device, use

to delete it. Substitute /dev/loop0 with the name of the specific loop device.

Loop devices are cheap. Therefore, many loop devices can be created in practice without worrying about a denial of service issue. See [4].

If you wish to prevent certain partitions or drives appearing on the desktop, you can create a udev rule, for example /etc/udev/rules.d/10-local.rules:

shows all partitions with the exception of sda1 and sda2 on your desktop.

Because block device names can change between reboots, it is also possible to use UUIDs to hide partitions or whole devices. Matching by UUID is only possible after /usr/lib/udev/rules.d/60-persistent-storage.rules has been processed, so make sure to choose a file name that will be ordered after it. For example:

The above line is also useful to hide multi device btrfs filesystems, as all the devices from a single btrfs filesystem will share the same UUID across the devices but will have different SUB_UUID for each individual device.

At start-up and when a drive is connected, udisksd will apply configuration stored in the file /etc/udisks2/IDENTIFIER.conf where IDENTIFIER is the value of the Drive:Id property for the drive. Currently ATA settings are supported. See udisks(8) for available options. These settings have essentially the same effect as those of hdparm, but they are persistent as long as the udisks daemon is autostarted.

For example, to set standby timeout to 240 (20 minutes) for a drive, add the following:

To obtain the DriveId for your drive, use udevadm info --query=all --name=sdx | grep ID_SERIAL | sed "s/_/-/g"

Alternatively, use a GUI utility to manage the configuration file, such as gnome-disk-utility.

If most of the devices mounted with Udisks are flash memories, like USB sticks and SD cards, configuring Udisks to not update files' access time may be beneficial. It causes additional and unexpected writes, despite the memory has apparently only been read. The default relatime mount option limits excessive writes for main storage. It does not prevent updates if the access time is older than 24 hours, which is often the case on removable media. To set noatime as the default for all Udisks mounts, add:

This option may be overridden later for specific mounts that do require atime: either in mount-specific /etc/udisks2/mount_options.conf section or through a udev rule setting ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="relatime".

Udisks2 hides certain devices from the user by default. If this is undesired or otherwise problematic, copy /usr/lib/udev/rules.d/80-udisks2.rules to /etc/udev/rules.d/80-udisks2.rules and remove the following section in the copy:

The udisks daemon polls S.M.A.R.T. data from drives regularly. Hard drives with a longer standby timeout than the polling interval may fail to enter standby. Drives that are already spun down are usually not affected. There seems no way to disable polling or change the interval as for udisks2 by now. See [5], [6].

However, Standby timeout applied by udisks2 seems to be unaffected. To set standby timeout via udisks, see #Apply ATA settings.

Other possible workarounds could be setting the timeout below the polling interval (10 minutes) or forcing a manual spindown using hdparm -y /dev/sdx.

The factual accuracy of this article or section is disputed.

If mounting a ntfs partition fails with the error:

and in the kernel log with journalctl/dmesg ran as root:

The problem is (as of udisks 2.10), the default is using the NTFS-3G driver, and there are 2 solutions for this:

1: Install NTFS-3G, and restart your machine.

2: Configure udisks2. By default, udisks2 is not configured on an Arch system, and no defaults are defined for non-native filesystems. The easiest way to do so, is to copy /etc/udisks2/mount.options.conf.example to /etc/udisks2/mount.options.conf and uncomment the following lines:

and restart the udisk2 daemon, or restart your machine.

udisks 2.8.2 introduced a breaking change by adding windows_names to NTFS mount options, preventing creation of Win32-incompatible filenames such as nul, screenshot 23-08-21 19:22.jpg. Among other things, this causes Steam Proton to stop initializing. To revert this behavior, use:

Bad filenames generally do not cause issues in Windows unless accessed. chkdsk will treat these names as errors and move the renamed files to found.nnn folders under filesystem root.

If an external HDD is not powered off properly at system shutdown, it may be desirable to fix the issue.

Enable udisks2.service.

A service to invoke our script might look like so:

Enable handle_external_hdds.service

Do a systemd daemon-reload to apply the new setting.

Reboot or restart graphical.target to check if works.

An example script to handle an arbitrary amount of partitions on a single disk looks like so:

uuid_list is a list of space delimited UUIDs corresponding to partitions of the device to check, e.g. "uuid_1" "uuid_2".

Even if nothing seems to be written to a USB stick, memory card, or other removable media, file access times may still be updated. This is a change that needs to be flushed to the device. If that is of concern, consider setting the noatime option for all Udisks mounts.

**Examples:**

Example 1 (unknown):
```unknown
/etc/udisks2/mount_options.conf
```

Example 2 (unknown):
```unknown
/etc/udisks2/mount_options.conf.example
```

Example 3 (unknown):
```unknown
/etc/udisks2/mount_options.conf
```

Example 4 (unknown):
```unknown
[defaults]
btrfs_defaults=compress=zstd
```

---

## Solid state drive

**URL:** https://wiki.archlinux.org/title/Solid_state_drive

**Contents:**
- Usage
  - TRIM
    - Periodic TRIM
    - Continuous TRIM
    - Trim an entire device
    - LVM
    - dm-crypt
    - swap
  - Maximizing performance
    - SSD memory cell clearing

This article covers special topics for operating solid state drives (SSDs) and other flash-memory based storage devices.

If you want to partition an SSD for a specific purpose, it may be useful to consider the List of file systems optimized for flash memory.

For general usage, simply choose your preferred file system and enable #TRIM.

Compared to hard drives, where deleting a file is only handled at the file system level[1], SSDs benefit from informing the disk controller when blocks of memory are free to be reused. Since the flash cells they are made of are worn out a little with each write operation, the disk controllers use algorithms to share the write operations on all the cells: this process is called wear leveling. Without the NVMe DEALLOCATE, SAS UNMAP or ATA_TRIM command (supported by most SSDs), the disk controller takes more time to do a write operation as soon as there is no empty memory blocks, as it has to shuffle data around to erase a cell before writing to it (see Wikipedia:Write amplification): a TechSpot benchmark shows the performance impact before and after filling an SSD with data.

As of Linux kernel version 3.8 onwards, support for TRIM was continually added for the different file systems. See the following table for an indicative overview:

To verify TRIM support, run:

And check the values of DISC-GRAN (discard granularity) and DISC-MAX (discard max bytes) columns. Non-zero values indicate TRIM support.

For SATA SSDs only, the hdparm package can detect TRIM support via hdparm -I /dev/sda | grep TRIM as the root user. hdparm does however not support NVMe SSDs.

The util-linux package provides fstrim.service and fstrim.timer systemd unit files. Enabling the timer will activate the service weekly. The service executes fstrim(8) on all mounted file systems on devices that support the discard operation.

The timer relies on the timestamp of /var/lib/systemd/timers/stamp-fstrim.timer (which it will create upon first invocation) to know whether a week has elapsed since it last ran. Therefore there is no need to worry about too frequent invocations, in an anacron-like fashion.

To query the units activity and status, see journalctl. To change the periodicity of the timer or the command run, edit the provided unit files.

Instead of issuing TRIM commands once in a while (by default once a week if using fstrim.timer), it is also possible to issue TRIM commands each time files are deleted instead. The latter is known as the continuous TRIM.

Using the discard option for a mount in /etc/fstab enables continuous TRIM in device operations. For example:

On the ext4 file system, the discard flag can also be set as a default mount option using tune2fs:

Using the default mount options instead of an entry in /etc/fstab is particularly useful for external drives, because such partition will be mounted with the default options also on other machines. This way, there is no need to edit /etc/fstab on every machine.

If you want to trim your entire SSD at once, e.g. for a new install or if you want to sell the drive, you can use the blkdiscard command.

TRIM requests that get passed from the file system to the logical volume are automatically passed to the physical volume(s). No additional configuration is necessary.

No LVM operations (lvremove, lvreduce and all others) issue TRIM requests to physical volume(s) by default. This is done to allow restoring previous volume group configuration with vgcfgrestore(8). The setting issue_discards in /etc/lvm/lvm.conf controls whether discards are sent to a logical volume's underlying physical volumes when the logical volume is no longer using the physical volumes' space.

Follow the instructions in dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD) to enable discard support for LUKS and plain dm-crypt devices.

To enable discard for swap space, either add the discard option to a swap device's entry in fstab or pass --discard when calling swapon.

Discard is not automatically enabled for swap partitions when using GPT partition automounting.

See swapon(8) for discussion on when swap is discarded: discard=once or discard=pages. If discard is specified without a specific mode, the default is to enable both.

Follow the tips in Improving performance#Storage devices to maximize the performance of your drives.

On occasion, users may wish to completely reset an SSD's cells to the same virgin state they were at the time the device was installed, thus restoring it to its factory default write performance. Write performance is known to degrade over time even on SSDs with native TRIM support: TRIM only safeguards against file deletes, not replacements such as an incremental save.

The reset can be accomplished by following the appropriate procedure denoted in Solid state drive/Memory cell clearing, either for SATA or NVMe SSDs.

Some motherboard firmware issue a ATA SECURITY FREEZE LOCK command to SATA devices on initialization, setting the drive to frozen mode which transitions it to SEC2 state (security disabled, not locked, frozen). Likewise some SSD (and HDD) are set to this state in the factory already. This can be seen in hdparm and smartctl output:

Operations like formatting the device or installing operating systems are not affected by the frozen mode.

The above hdparm output shows the device is not locked by an HDD-password on boot and the frozen state safeguards the device against malwares which may try to lock it by setting a password to it at runtime.

If you intend to set a password to a "frozen" device yourself, a motherboard BIOS with support for it is required. A lot of notebooks have support, because it is required for hardware encryption, but support may not be trivial for a desktop/server board. For the Intel DH67CL/BL motherboard, for example, the motherboard has to be set to "maintenance mode" by a physical jumper to access the settings.[10]

If you intend to erase the SSD, see Securely wipe disk#hdparm and /Memory cell clearing.

When waking up from S3 sleep, the SATA SSD will most likely have reverted to SEC1 state (security disabled, not locked, not frozen), leaving it vulnerable to ATA SECURITY ERASE UNIT commands like those described in /Memory cell clearing.

In order to prevent this issue, a script can be run after waking up from sleep:

If the system has multiple storage devices and/or portable USB-drives, another option is to adapt Hdparm#Persistent configuration using udev rule to issue a --security-freeze for all drives (incl. HDD).

As noted in #Frozen mode, setting a password for a storage device (SSD/HDD) in the BIOS may also initialize the hardware encryption of devices supporting it. If the device also conforms to the OPAL standard, this may also be achieved without a respective BIOS feature to set the passphrase. See Self-encrypting drives.

It is possible that the issue you are encountering is a firmware bug which is not Linux specific, so before trying to troubleshoot an issue affecting the SSD device, you should first check if updates are available for:

Even if it is a firmware bug it might be possible to avoid it, so if there are no updates to the firmware or you hesitant on updating firmware then the following might help.

Some SSDs and SATA chipsets do not work properly with Linux Native Command Queueing (NCQ). The tell-tale errors in the journal look like:

To disable NCQ on boot, add libata.force=noncq to the kernel command line in the boot loader configuration. To disable NCQ only for disk 0 on port 9 use: libata.force=9.00:noncq

Alternatively, you may disable NCQ for a specific drive without rebooting via sysfs:

If this (and also updating the firmware) does not resolve the problem or causes other issues, then file a bug report.

Some SSDs (e.g. Transcend MTS400 or Crucial M550 SSDs) are failing with certain SATA controllers when SATA Active Link Power Management (ALPM), is enabled.

ALPM is enabled by default since linux-4.16, or may be enabled at runtime by a power saving daemon (e.g. TLP, Laptop Mode Tools). See Power management#SATA Active Link Power Management for more on this.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Several USB-to-SATA bridge chips (like VL715, VL716 etc.) and also USB-to-PCIe bridge chips (like the JMicron JMS583 used in external NVMe enclosures like IB-1817M-C31) support TRIM-like commands that can be sent through the USB Attached SCSI driver (named "uas" under Linux).

But the kernel may not automatically detect this capability, and therefore might not use it. Assuming your block device in question is /dev/sdX, you can find out whether that is the case by using the command from sg3_utils:

If in its output you find a line stating Logical block provisioning: lbpme=0 then you know that the kernel assumes the device does not support "Logical Block Provisioning Management" because the (LBPME) bit is not set.

If this is the case, then you should next find out whether the "Vital Product Data" (VPD) page on "Logical Block Provisioning" of your device tells of supported mechanisms for unmapping data. You can do this using the command:

Look for lines in the output that look like this:

This example would tell you the device supports the "UNMAP" command.

Have a look at the output of

If the kernel did not detect the capability of your device to unmap data, then this will likely return "full". Apart from "full", the kernel SCSI storage driver currently knows the following values for provisioning_mode:

For the example above, you could now write "unmap" to "provisioning_mode" to ask the kernel to use that:

This should immediately enable you to use tools like blkdiscard on /dev/sdX or fstrim on file systems mounted on /dev/sdX.

If you want to enable a "provisioning_mode" automatically when an external device of a certain vendor/product is attached, this can be automated via the "udev" mechanism. First find the USB Vendor and Product IDs:

Then create or append to a udev rule file (example here using idVendor 152d and idProduct 0583):

(You can also use the lsusb command to look for the relevant idVendor/idProduct.)

If supported by the device vendor, it is recommended to update firmware using the fwupd utility.

To check your current firmware version:

Updating SSD firmware under Linux is not supported by ADATA. A Windows-only utility called SSD ToolBox is provided by ADATA through their support page and through their ADATA XPG support page to monitor, TRIM, benchmark and update ADATA SSD firmware.

Crucial provides an option for updating the firmware with an ISO image. These images can be found after selecting the product on their SSD support page and downloading the "Manual Boot File."

Owners of an M4 Crucial model, may check if a firmware upgrade is needed with smartctl.

Users seeing this warning are advised to backup all sensible data and consider upgrading immediately. Check this instructions to update Crucial MX100 firmware by using the ISO image and Grub.

Besides the bootable ISO, micron-storage-executive-cliAUR is a command-line tool for flashing firmwares and also offers additional SSD information.

Intel has a Linux live system based Firmware Update Tool for operating systems that are not compatible with its Windows Intel® Memory and Storage Tool (GUI) software.

There is also a newer Linux command-line utility that can reflash firmware called the Intel Memory and Storage (MAS) Tool available as intel-mas-cli-toolAUR. There is a PDF user guide available.

An example for checking the firmware status is:

-intelssd 0 can be omitted if there is only one Intel SSD in the system, or 1 passed for the second SSD, and so on.

If an update is available, it is performed by running intelmas load -intelssd 0. The PDF user guide suggests that this procedure needs to be performed twice in Linux, with a power cycle in between. The latest firmware for all devices is distributed as part of the MAS Tool itself, so does not need to be downloaded separately.

KFU tool is available for the Sandforce based drives, kingston_fw_updaterAUR.

The lesser known Mushkin brand solid state drives also use Sandforce controllers, and have a Linux utility (nearly identical to Kingston's) to update the firmware.

OCZ has a Command Line Online Update Tool (CLOUT) available for Linux. The existing packages are ocz-ssd-utilityAUR, ocztoolboxAUR and oczcloutAUR.

Although Samsung deems firmware update methods outside of their Magician software as "unsupported", they still can work. The Magician software can create a bootable USB drive containing the firmware update, however Samsung no longer provides the software for consumer SSDs. Samsung also provides pre-made bootable ISO images that can be used to update the firmware. Another option is to use Samsung's magician utility provided by samsung_magician-consumer-ssdAUR. Magician only supports Samsung-branded SSDs; those manufactured by Samsung for OEMs (e.g., Lenovo) are not supported.

Users preferring to run the firmware update from a live USB created under Linux (without using Samsung's Magician software under Microsoft Windows) can refer to [11] for more details. Note that this blog post details creating a bootable USB drive with Master Boot Record (MBR) that some newer motherboards, e.g. Intel NUC no longer support.

The SSD firmware can be updated natively (without making a bootable USB stick) as shown below. First visit the Samsung downloads page, go to the "Samsung SSD Firmware" section, and download the latest firmware for your SSD—it should be an ISO image.

Extract the initrd Linux image from the ISO image:

Extract root/fumagician/. This directory contains the firmware update files:

Finally, run root/fumagician/fumagician with root privileges and reboot your system (if the firmware was successfully updated).

If after reboot the firmware version does not change, run root/fumagician/fumagician 2> log and search for errors in the log file. For example, if the log shows 'unzip is not available', install unzip or extract it from the initrd.

Some of the SSD firmware ISO images contain a FreeDOS image instead of an initrd Linux image, so the steps needed to update the SSD firmware differ from above. The following table lists these SSDs (and relevant paths):

First, extract the FreeDOS image from the ISO image:

Mount the FreeDOS image to /mnt/:

Get the disk number of the SSD under Disk Number from the Magician SSD management utility:

Update the SSD firmware for the specified disk by providing the firmware package path:

Finally, verify whether the firmware was successfully updated by checking the version under Firmware from the output of magician --list (with root privileges). Reboot your system if so.

SanDisk makes ISO firmware images to allow SSD firmware update on operating systems that are unsupported by their SanDisk SSD Toolkit.

One must choose the firmware for the correct SSD model, and the correct capacity that it has (e.g. 60GB, or 256GB). After burning the ISO firmware image, simply restart the PC to boot with the newly created CD/DVD boot disk (may work from a USB stick).

The iso images just contain a linux kernel and an initrd. Extract them to /boot partition and boot them with GRUB or Syslinux to update the firmware.

**Examples:**

Example 1 (unknown):
```unknown
$ lsblk --discard
```

Example 2 (unknown):
```unknown
hdparm -I /dev/sda | grep TRIM
```

Example 3 (unknown):
```unknown
fstrim.service
```

Example 4 (unknown):
```unknown
fstrim.timer
```

---

## FAT

**URL:** https://wiki.archlinux.org/title/FAT

**Contents:**
- File system creation
- Kernel configuration
- Writing to FAT32 as normal user
- Detecting FAT type
- See also

From Wikipedia:File Allocation Table:

To create a FAT filesystem, install dosfstools.

mkfs.fat supports creating FAT12, FAT16 and FAT32, see Wikipedia:File Allocation Table#Types for an explanation on their differences. mkfs.fat will select the FAT type based on the partition size, to explicitly create a certain type of FAT filesystem use the -F option. See mkfs.fat(8) for more information.

Format a partition to FAT32:

Here is an example of the default mount configuration in the kernel:

A short description of the options:

If the partition type detected by mount is VFAT then it will run the /usr/bin/mount.vfat script.

To write on a FAT32 partition, you must make a few changes to the fstab file.

The user option means that any user (even non-root) can mount and unmount the partition /dev/sdxY (mount(8) § Non-superuser mounts). rw gives read-write access.

For example, if your FAT32 partition is on /dev/sda9, and you wish to mount it to /mnt/fat32, then you would use:

Now, any user can mount it with:

Note that FAT does not support Linux file permissions. Each file will also appear to be executable. You may want to use the showexec option to only mark Windows executables (com, exe, bat) as executable. See mount(8) § Mount options for fat for more options.

If you need to know which type of FAT file system a partition uses, use the file command:

Alternatively you can use minfo from the mtools package:

**Examples:**

Example 1 (unknown):
```unknown
# mkfs.fat -F 32 /dev/partition
```

Example 2 (unknown):
```unknown
$ zgrep -e FAT -e DOS /proc/config.gz | sort -r
```

Example 3 (unknown):
```unknown
# DOS/FAT/NT Filesystems
CONFIG_FAT_FS=m
CONFIG_MSDOS_PARTITION=y
CONFIG_FAT_FS=m
CONFIG_MSDOS_FS=m
CONFIG_VFAT_FS=m
CONFIG_FAT_DEFAULT_CODEPAGE=437
CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"
CONFIG_NCPFS_SMALLDOS=y
```

Example 4 (unknown):
```unknown
CONFIG_FAT_DEFAULT_CODEPAGE
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/Partitioning

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## Securely wipe disk

**URL:** https://wiki.archlinux.org/title/Shred

**Contents:**
- Common use cases
  - Wipe all data left on the device
  - Preparations for block device encryption
- Data remanence
  - Operating system, programs and filesystem
  - Hardware-specific issues
    - Flash memory
    - Marked Bad Sectors
    - Residual magnetism
- Select a target

Wiping a disk is done by writing new data over every single bit.

The most common usecase for completely and irrevocably wiping a device is when the device is going to be given away or sold. There may be (unencrypted) data left on the device and you want to protect against simple forensic investigation that is mere child's play with for example File recovery software.

If you want to quickly wipe everything from the disk, /dev/zero or simple patterns allow maximum performance while adequate randomness can be advantageous in some cases that should be covered up in #Data remanence.

Every overwritten bit means to provide a level of data erasure not allowing recovery with normal system functions (like standard ATA/SCSI commands) and hardware interfaces. Any file recovery software mentioned above then would need to be specialized on proprietary storage-hardware features.

In case of a HDD, data recreation will not be possible without at least undocumented drive commands or tinkering with the device's controller or firmware to make them read out for example reallocated sectors (bad blocks that S.M.A.R.T. retired from use).

There are different wiping issues with different physical storage technologies. Most notably, all Flash memory based devices and older magnetic storage (old HDDs, floppy disks, tape).

To prepare a drive for block device encryption inside the wiped area afterwards, it is recommended to use #Random data generated by a cryptographically strong random number generator (referred to as RNG in this article from now on).

See also Wikipedia:Random number generation.

See also Wikipedia:Data remanence. The representation of data may remain even after attempts have been made to remove or erase the data.

The operating system, executed programs or journaling file systems may copy your unencrypted data throughout the block device. When writing to plain disks, this should only be relevant in conjunction with one of the above.

If the data can be exactly located on the disk and was never copied anywhere else, wiping with pseudorandom data can be thoroughgoing and impressively quick.

A good example is cryptsetup using /dev/urandom for wiping the LUKS keyslots.

Write amplification and other characteristics make Flash memory, including SSDs, a stubborn target for reliable wiping. As there is a lot of transparent abstraction in between data as seen by a device's controller chip and the operating system, sight data is never overwritten in place and wiping particular blocks or files is not reliable.

Other "features" like transparent compression (all SandForce SSDs) can compress your zeros or repetitive patterns, so if wiping is fast beyond belief this might be the cause.

Disassembling Flash memory devices, unsoldering the chips and analyzing data content without the controller in between is feasible without difficulty using simple hardware. Data recovery companies do it for cheap money.

For more information see:

If a hard drive marks a sector as bad, it cordons it off, and the section becomes impossible to write to via software. Thus a full overwrite would not reach it. However because of block sizes, these sections would only amount to a few theoretically recoverable KiB.

A single, full overwrite with zeros or random data does not lead to any recoverable data on a modern high-density storage device. Note that repeating the operation should not be necessary nowadays. [1] Indications otherwise refer to single residual bits; reconstruction of byte patterns is generally not feasible.[2] See also [3], [4] and [5].

Use fdisk to locate all read/write devices the user has read access to.

Check the output for lines that start with devices such as /dev/sdX.

This is an example for a HDD formatted to boot a linux system:

Or another example with the Arch Linux image written to a 4GB USB thumb drive:

If you are worried about unintentional damage of important data on the primary computer, consider using an isolated environment such as a virtual environment (VirtualBox, VMWare, QEMU, etc...) with direct connected disk drives to it or a single computer only with a storage disk(s) that need to be wiped booted from a Live Media (USB, CD, PXE, etc...) or use a script to prevent wiping mounted partitions by typo.

To wipe sensitive data, one can use any data pattern matching the needs.

Overwriting with /dev/zero or simple patterns is considered secure in most situations. With today's HDDs, it is deemed appropriate and fast for disk wiping.

However, a drive that is abnormally fast in writing patterns or zeroing could be doing transparent compression. It is obviously presumable not all blocks get wiped this way. Some #Flash memory devices do "feature" that.

To setup block device encryption afterwards, one should wipe the area with random data (see next section) to avoid weakening the encryption.

/dev/urandom can be used as a fast and secure source of cryptographically secure pseudorandom data from the Linux kernel. For more details about sources of random and pseudorandom data, see Random number generation.

In the past when the kernel's random number generator was slow, a common alternative for pseudorandom data generation was to use an encrypted datastream, such as by encrypting /dev/zero with a random key. While this should in theory be secure, it no longer presents any advantages over the kernel's new, faster random number generator, and there is a risk that the temporary key may accidentally be saved someplace.

See also Wikipedia:Dd (Unix)#Block size, blocksize io-limits.

If you have an Advanced Format hard drive it is recommended that you specify a block size larger than the default 512 bytes. To speed up the overwriting process choose a block size matching your drive's physical geometry by appending the block size option to the dd command (i.e. bs=4096 for 4 KiB).

fdisk prints physical and logical sector size for every disk. Alternatively sysfs does expose information:

Block storage devices are divided in sectors, and the size of a single sector can be used to calculate the size of the entire device in bytes. To do so, multiply the number of sectors by the drive sector size.

As an example we use the parameters with the dd command to wipe a partition:

Here, to illustrate with a practical example, we will show the output of the fdisk command on the partition /dev/sdX:

To wipe partition /dev/sdX1, the example parameters with logical sectors would be used like follows.

with Start=2048, End=3839711231 and BytesInSector=512.

with LogicalSectors=3839709184.

Or, to wipe the whole disk by using physical sectors:

with AllDiskPhysicalSectors=488378646 and PhysicalSectorSizeBytes=4096.

You can choose from several utilities to overwrite a drive. If you only want to wipe a single file, Securely wipe disk/Tips and tricks#Wipe a single file has considerations in addition to the utilities mentioned below.

The redirected output can be used to create files, rewrite free space on the partition, and to wipe the whole device or a single partition on it. The examples here use /dev/zero to zero the device, but /dev/urandom may be substituted if a random wipe is desired.

The following examples show how to rewrite the partition or a block device by redirecting stdout from other utilities:

See also dd and Securely wipe disk/Tips and tricks#Wipe a single file.

Zero-fill the disk by writing a zero byte to every addressable location on the disk using the /dev/zero stream.

Or the /dev/urandom stream:

The process is finished when dd reports No space left on device and returns control back:

To speed up wiping a large drive, see also:

The file copy command cp(1) can also be used to rewrite the device, because it ignores the type of the destination:

Using pv will show a progress bar, the time spent and the estimated time till completion. Pass the selected data source to pv(1) and use the -o/--output option to specify the disk which will be written to. For example, to fill the disk /dev/sdX with /dev/zero:

A program specialized on wiping files. It is available as part of the wipe package. To make a quick wipe of a destination, you can use something like:

See also wipe(1). The tool was last updated in 2009. Its SourceForge page suggests that it is currently unmaintained.

shred (from the coreutils package) is a Unix command that can be used to securely delete individual files or full devices so that they can be recovered only with great difficulty with specialised hardware, if at all. By default shred uses three passes, writing pseudo-random data to the device during each pass. This can be reduced or increased.

The following command invokes shred with its default settings and displays the progress.

Shred can also be used on a single partition, e.g. to wipe the first partition use shred -v /dev/sdX1.

Alternatively, shred can be instructed to do only one pass, with entropy from e.g. /dev/urandom, and a final overwrite with zeros.

scrub iteratively writes patterns on files or disk devices to make retrieving the data more difficult.

The following command invokes scrub with the default settings, in mode 1, overwriting the target device using patterns compliant with NNSA Policy Letter NAP-14.x. This is the most effective method.

The following command invokes scrub with the default settings, in mode 2, overwriting the target file using patterns compliant with NNSA Policy Letter NAP-14.x, rounding the bytes written up to fill out the last file system block. Note that there are caveats for this mode, see the manual for further details.

The following command invokes scrub with the default settings, in mode 3, creating a directory and filling it with files until the file system is full. The files are then scrubbed using patterns compliant with NNSA Policy Letter NAP-14.x, rounding the bytes written up to fill out the last file system block. Note that there are caveats for this mode, see the manual for further details.

For further usage and information, see the manual.

The tool badblocks from e2fsprogs is able to perform destructive read-write test, effectively wiping the device. By default, it performs four passes and can take a long time.

hdparm supports ATA Secure Erase, which is functionally equivalent to zero-filling a disk. It is however handled by the hard drive firmware itself, and includes "hidden data areas". As such, it can be seen as a modern-day "low-level format" command. SSD drives reportedly achieve factory performance after issuing this command, but may not be sufficiently wiped (see #Flash memory).

Some drives support Enhanced Secure Erase, which uses distinct patterns defined by the manufacturer. If the output of hdparm -I for the device indicates a many-fold time advantage for the Enhanced erasure, the device probably has a hardware encryption feature and the wipe will be performed to the encryption keys only.

For detailed instructions on using ATA Secure Erase, see Solid state drive/Memory cell clearing and the Linux ATA wiki.

See Solid state drive/Memory cell clearing#Common method with blkdiscard

**Examples:**

Example 1 (unknown):
```unknown
/dev/urandom
```

Example 2 (unknown):
```unknown
Disk /dev/sda: 250.1 GB, 250059350016 bytes, 488397168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00ff784a

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048      206847      102400   83  Linux
/dev/sda2          206848   488397167   244095160   83  Linux
```

Example 3 (unknown):
```unknown
Disk /dev/sdb: 4075 MB, 4075290624 bytes, 7959552 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x526e236e

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           0      802815      401408   17  Hidden HPFS/NTFS
```

Example 4 (unknown):
```unknown
/dev/urandom
```

---

## Disk cloning

**URL:** https://wiki.archlinux.org/title/Ddrescue

**Contents:**
- Block-level cloning
  - Using dd
  - Using ddrescue
    - First round
    - Second round
    - Third round (optional)
    - Fourth round
    - Fifth round (optional)
- File system cloning
  - Using e2image

Disk cloning is the process of making an image of a partition or of an entire hard drive. This can be useful for copying the drive to other computers or for backup and recovery purposes.

See dd#Disk cloning and restore and Core utilities#dd alternatives.

If possible, data recovery from disks should be performed using their native interface: SATA or, for older drives, IDE. Results may vary while using USB adapters.

GNU ddrescue is a data recovery tool capable of ignoring read errors. ddrescue is not related to dd in any way except that both can be used for copying data from one device to another. The key difference is that ddrescue uses a sophisticated algorithm to copy data from failing drives causing them as little additional damage as possible. See the ddrescue manual for details.

To clone a faulty or dying drive, run ddrescue twice. For the first round, copy every block without read error and map the errors to rescue.map.

This command copies data from one device (/dev/sdX) to another device (/dev/sdY) while prioritizing speed (by skipping retry attempts).

For the second round, copy only the bad blocks and try 3 times to read from the source before giving up.

This command attempts to read problematic sectors more aggressively.

if you encounter issue like this:

check sector size of the device:

This will display the sector size in bytes. For example, most CD/DVD drives, the correct sector size is 2048 bytes. and specify sector size manually:

--reverse reads the drive in reverse, which can sometimes bypass issues that prevent forward reads.

For the fourth round, use scraping mode for fine-grained recovery:

--retry-passes=3 will scrape over the problematic sectors multiple times. It tries to rescue data from the most damaged sectors.

When to stop: If the drive continues to have read speeds near 0 B/s with no further improvement, the likelihood of recovering more data diminishes. In such cases, professional data recovery services might be the best option. Ultimately, if the process continues to stall without rescuing more data, the drive might be physically failing, and further attempts may yield minimal results..

In some circumstances the disk controller or a USB adapter may lock, while attempting to read a particular sector. The --input-position option may be used to instruct ddrescue to start reading after that position.

Now you can check the file system for corruption and mount the new drive.

Once the copy is complete, run a final pass in read-only mode to verify integrity of the rescued image:

or mounting the image, if it's CD/DVD/BD:

Or run a checksum if you have a reference file.

e2image is a tool included in e2fsprogs for debugging purposes. It can be used to copy ext2, ext3, and ext4 partitions efficiently by only copying the used blocks. Note that this only works for ext2, ext3, and ext4 filesystems, and the unused blocks are not copied so this may not be a useful tool if one is hoping to recover deleted files.

To clone a partition from physical disk /dev/sda, partition 1, to physical disk /dev/sdb, partition 1 with e2image, run

xfs_copy(8) from xfsprogs can be used to copy an XFS file system to one or more block devices in parallel.

For example, to clone the file system on /dev/sda1 to /dev/sdb1, run:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

These applications allow easy backup of entire file systems and recovery in case of failure, usually in the form of a Live CD or USB drive. They contain complete system images from one or more specific points in time and are frequently used to record known good configurations. See Wikipedia:Comparison of disk cloning software for their comparison.

See also Synchronization and backup programs for other applications that can take full system snapshots, among other functionality.

**Examples:**

Example 1 (unknown):
```unknown
# ddrescue --force --no-scrape /dev/sdX /dev/sdY rescue.map
```

Example 2 (unknown):
```unknown
--no-scrape
```

Example 3 (unknown):
```unknown
# ddrescue --force --idirect --retry-passes=3 --no-scrape /dev/sdX /dev/sdY rescue.map
```

Example 4 (unknown):
```unknown
--sector-size
```

---

## LVM

**URL:** https://wiki.archlinux.org/title/LVM

**Contents:**
- Background
  - LVM building blocks
  - Advantages
  - Disadvantages
- Installation
- Volume operations
  - Physical volumes
    - Creating
    - Growing
    - Shrinking

From Wikipedia:Logical Volume Manager (Linux):

Logical Volume Management utilizes the kernel's device-mapper feature to provide a system of partitions independent of underlying disk layout. With LVM you abstract your storage and have "virtual partitions", making extending/shrinking easier (subject to potential filesystem limitations).

Virtual partitions allow addition and removal without worry of whether you have enough contiguous space on a particular disk, getting caught up fdisking a disk in use (and wondering whether the kernel is using the old or new partition table), or, having to move other partitions out of the way.

Basic building blocks of LVM:

LVM gives you more flexibility than just using normal hard drive partitions:

Make sure the lvm2 package is installed.

If you have LVM volumes not activated via the initramfs, enable lvm2-monitor.service, which is provided by the lvm2 package.

To create a PV on /dev/sda1, run:

You can check the PV is created using the following command:

After extending or prior to reducing the size of a device that has a physical volume on it, you need to grow or shrink the PV using pvresize(8).

To expand the PV on /dev/sda1 after enlarging the partition, run:

This will automatically detect the new size of the device and extend the PV to its maximum.

To shrink a physical volume prior to reducing its underlying device, add the --setphysicalvolumesize size parameters to the command, e.g.:

The above command may leave you with this error:

Indeed pvresize will refuse to shrink a PV if it has allocated extents after where its new end would be. One needs to run pvmove beforehand to relocate these elsewhere in the volume group if there is sufficient free space.

Before freeing up physical extents at the end of the volume, one must run pvdisplay -v -m to see them. An alternative way to view segments in a tabular form is pvs --segments -v.

In the below example, there is one physical volume on /dev/sdd1, one volume group vg1 and one logical volume backup.

One can observe FREE space are split across the volume. To shrink the physical volume, we must first move all used segments to the beginning.

Here, the first free segment is from 0 to 153600 and leaves us with 153601 free extents. We can now move this segment number from the last physical extent to the first extent. The command will thus be:

Once all your free physical segments are on the last physical extents, run vgdisplay with root privileges and see your free PE.

Then you can now run again the command:

Last, you need to shrink the partition with your favorite partitioning tool.

To create a VG MyVolGroup with an associated PV /dev/sdb1, run:

You can check the VG MyVolGroup is created using the following command:

You can bind multiple PVs when creating a VG like this:

By default, this will reactivate the volume group when applicable. For example, if you had a drive failure in a mirror and you swapped the drive; and ran (1) pvcreate, (2) vgextend and (3) vgreduce --removemissing --force.

To start the rebuilding process of the degraded mirror array in this example, you would run:

You can monitor the rebuilding process (Cpy%Sync Column output) with:

This will deactivate the volume group and allow you to unmount the container it is stored in.

Use the vgrename(8) command to rename an existing volume group.

Either of the following commands renames the existing volume group MyVolGroup to my_volume_group

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the renamed volume group.

You first create a new physical volume on the block device you wish to use, then extend your volume group

This of course will increase the total number of physical extents on your volume group, which can be allocated by logical volumes as you see fit.

If you created a logical volume on the partition, remove it first.

All of the data on that partition needs to be moved to another partition. Fortunately, LVM makes this easy:

If you want to have the data on a specific physical volume, specify that as the second argument to pvmove:

Then the physical volume needs to be removed from the volume group:

Or remove all empty physical volumes:

For example: if you have a bad disk in a group that cannot be found because it has been removed or failed:

And lastly, if you want to use the partition for something else, and want to avoid LVM thinking that the partition is a physical volume:

To create a LV homevol in a VG MyVolGroup with 300 GiB of capacity, run:

or, to create a LV homevol in a VG MyVolGroup with the rest of capacity, run:

To create the LV while restricting it to specific PVs within the VG, append them to the command:

The new LV will appear as /dev/MyVolGroup/homevol. Now you can format the LV with an appropriate file system.

You can check the LV is created using the following command:

To rename an existing logical volume, use the lvrename(8) command.

Either of the following commands renames logical volume old_vol in volume group MyVolGroup to new_vol.

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the renamed logical volume.

Extend the logical volume mediavol in MyVolGroup by 10 GiB and resize its file system all at once:

Set the size of logical volume mediavol in MyVolGroup to 15 GiB and resize its file system all at once:

If you want to fill all the free space on a volume group, use the following command:

See lvresize(8) for more detailed options.

For file systems not supported by fsadm(8) will need to use the appropriate utility to resize the file system before shrinking the logical volume or after expanding it.

To extend logical volume mediavol within volume group MyVolGroup by 2 GiB without touching its file system:

Now expand the file system (ext4 in this example) to the maximum size of the underlying logical volume:

For Btrfs, btrfs-filesystem(8) expects the mountpoint instead of the device, the equivalent is:

To reduce the size of logical volume mediavol in MyVolGroup by 500 MiB, first calculate the resulting file system size and shrink the file system (Ext4 in this example) to the new size:

Unlike Ext4, Btrfs supports online shrinking (again, a mountpoint should be specified) e.g.:

When the file system is shrunk, reduce the size of logical volume:

To calculate the exact logical volume size for ext2, ext3, ext4 file systems, use a simple formula: LVM_EXTENTS = FS_BLOCKS × FS_BLOCKSIZE ÷ LVM_EXTENTSIZE.

Passing --resizefs will confirm that the correctness.

See lvresize(8) for more detailed options.

First, find out the name of the logical volume you want to remove. You can get a list of all logical volumes with:

Next, look up the mountpoint of the chosen logical volume:

Then unmount the filesystem on the logical volume:

Finally, remove the logical volume:

Confirm by typing in y.

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the removed logical volume.

You can verify the removal of the logical volume by typing lvs as root again (see first step of this section).

LVM supports CoW (Copy-on-Write) snapshots. A CoW snapshot initially points to the original data. When data blocks are overwritten, the original copy is left intact and the new blocks are written elsewhere on-disk. This has several desirable properties:

LVM snapshots are at the block level. They make a new block device, with no apparent relationship to the original except when dealing with the LVM tools. Therefore, deleting files in the original copy does not free space in the snapshots. If you need filesystem-level snapshots, you rather need btrfs, ZFS or bcachefs.

You create snapshot logical volumes just like normal ones.

With that volume, you may modify less than 100 MiB of data, before the snapshot volume fills up.

Reverting the modified lvol logical volume to the state when the snap01vol snapshot was taken can be done with

In case the origin logical volume is active, merging will occur on the next reboot (merging can be done even from a LiveCD).

Also multiple snapshots can be taken and each one can be merged with the origin logical volume at will.

A snapshot provides a frozen copy of a file system to make backups. For example, a backup taking two hours provides a more consistent image of the file system than directly backing up the partition.

The snapshot can be mounted and backed up with dd or tar. The size of the backup file done with dd will be the size of the files residing on the snapshot volume. To restore just create a snapshot, mount it, and write or extract the backup to it. And then merge it with the origin.

See Create root filesystem snapshots with LVM for automating the creation of clean root file system snapshots during system startup for backup and rollback.

This article or section needs expansion.

See dm-crypt/Encrypting an entire system#LUKS on LVM and dm-crypt/Encrypting an entire system#LVM on LUKS for the possible schemes of combining LUKS with LVM.

This article or section needs expansion.

Convert your fast disk (/dev/fastdisk) to PV and add to your existing VG (MyVolGroup):

Create a cache pool with automatic meta data on /dev/fastdisk and convert the existing LV MyVolGroup/rootvol to a cached volume, all in one step:

Cachemode has two possible options:

If a specific --cachemode is not indicated, the system will assume writethrough as default.

If you ever need to undo the one step creation operation above:

This commits any pending writes still in the cache back to the origin LV, then deletes the cache. Other options are available and described in lvmcache(7).

LVM may be used to create a software RAID. It is a good choice if the user does not have hardware RAID and was planning on using LVM anyway. From lvmraid(7):

LVM RAID supports RAID 0, RAID 1, RAID 4, RAID 5, RAID 6 and RAID 10. See Wikipedia:Standard RAID levels for details on each level.

Create physical volumes:

Create volume group on the physical volumes:

Create logical volumes using lvcreate --type raidlevel, see lvmraid(7) and lvcreate(8) for more options.

Please mind how the examples below each specify the physical volumes. This can make sense in some situations to have LVM use a specific subset of devices for your new logical volume. But generally speaking, this is not necessary.

will create a 70 GiB striped (raid0) logical volume named "myraid1vol" in VolGroup00. Stripes will be spread over /dev/nvme1n1p1 and /dev/nvme0n1p1. Stripesize is set to be 64K.

will create a 20 GiB mirrored logical volume named "myraid1vol" in VolGroup00 on /dev/sda2 and /dev/sdb2.

RAID5 requires at least three drives (number of --stripes plus one parity device). Data and parity blocks are stored on each device, typically in a rotating pattern.

will create a 40 GiB striped logical volume named "myraid5vol" in VolGroup00 on /dev/sda2, /dev/sdb2 and /dev/sdc2. On each disk, the RAID5 will occupy about 20 GiB.

RAID6 requires at least five drives (number of --stripes plus two parity devices). As with RAID5, data and parity blocks are stored on each device, typically in a rotating pattern.

will create a 60 GiB striped logical volume named "myraid6vol" in VolGroup00 on /dev/sda2, /dev/sdb2, /dev/sdc2 and /dev/sdd2. On each disk, the RAID6 will occupy about 20 GiB.

will create a 100 GiB RAID10 logical volume named "myraid1vol" in VolGroup00 on /dev/sdd1, /dev/sdc1, /dev/sdb1, and /dev/sda5.

You can convert easily a non-RAID (e.g. linear) volume to pretty much any other raid configuration provided that you have enough physical devices to meet the RAID requirements. Some of them will require you to go through intermediate steps which lvconvert will inform you about and prompt you to agree. raid10 below can be replaced with raid0, raid1, raid5 etc.

You can keep track of the progress of conversion with:

Here is the classic use case. Suppose you want to start your own VPS service, initially hosting about 100 VPSes on a single PC with a 930 GiB hard drive. Hardly any of the VPSes will actually use all of the storage they are allotted, so rather than allocate 9 GiB to each VPS, you could allow each VPS a maximum of 30 GiB and use thin provisioning to only allocate as much hard drive space to each VPS as they are actually using. Suppose the 930 GiB hard drive is /dev/sdb. Here is the setup.

Prepare the volume group, MyVolGroup.

Create the thin pool LV, MyThinPool. This LV provides the blocks for storage.

The thin pool is composed of two sub-volumes, the data LV and the metadata LV. This command creates both automatically. But the thin pool stops working if either fills completely, and LVM currently does not support the shrinking of either of these volumes. This is why the above command allows for 5% of extra space, in case you ever need to expand the data or metadata sub-volumes of the thin pool.

For each VPS, create a thin LV. This is the block device exposed to the user for their root partition.

The block device /dev/MyVolGroup/SomeClientsRoot may then be used by a VirtualBox instance as the root partition.

Thin snapshots are much more powerful than regular snapshots, because they are themselves thin LVs. See Red Hat's guide [4] for a complete list of advantages thin snapshots have.

Instead of installing Linux from scratch every time a VPS is created, it is more space-efficient to start with just one thin LV containing a basic installation of Linux:

Then create snapshots of it for each VPS:

This way, in the thin pool there is only one copy the data common to all VPSes, at least initially. As an added bonus, the creation of a new VPS is instantaneous.

Since these are thin snapshots, a write operation to GenericRoot only causes one COW operation in total, instead of one COW operation per snapshot. This allows you to update GenericRoot more efficiently than if each VPS were a regular snapshot.

There are applications of thin provisioning outside of VPS hosting. Here is how you may use it to grow the effective capacity of an already-mounted file system without having to unmount it. Suppose, again, that the server has a single 930 GiB hard drive. The setup is the same as for VPS hosting, only there is only one thin LV and the LV's size is far larger than the thin pool's size.

This extra virtual space can be filled in with actual storage at a later time by extending the thin pool.

Suppose some time later, a storage upgrade is needed, and a new hard drive, /dev/sdc, is plugged into the server. To upgrade the thin pool's capacity, add the new hard drive to the VG:

Now, extend the thin pool:

Since this thin LV's size is 16 TiB, you could add another 15.09 TiB of hard drive space before finally having to unmount and resize the file system.

Some customisation is available by editing /etc/lvm/lvm.conf. You may find it useful to customize the output of lvs and pvs which by default does not include the % sync (useful to see progress of conversion between e.g. linear and raid type) and type of logical volume:

The dm_mod module should be automatically loaded. In case it does not, explicitly load the module at boot.

If you are trying to mount existing logical volumes, but they do not show up in lvscan, you can use the following commands to activate them:

Cause: removing an external LVM drive without deactivating the volume group(s) first. Before you disconnect, make sure to:

Fix: assuming you already tried to activate the volume group with vgchange -ay vg, and are receiving the Input/output errors:

Unplug the external drive and wait a few minutes:

The factual accuracy of this article or section is disputed.

In order for LVM to work properly with removable media – like an external USB drive – the volume group of the external drive needs to be deactivated before suspend. If this is not done, you may get buffer I/O errors on the dm device (after resume). For this reason, it is not recommended to mix external and internal drives in the same volume group.

To automatically deactivate the volume groups with external USB drives, tag each volume group with the sleep_umount tag in this way:

Once the tag is set, use the following unit file for systemd to properly deactivate the volumes before suspend. On resume, they will be automatically activated by LVM.

Finally, enable the unit.

If trying to extend a logical volume errors with:

The reason is that the logical volume was created with an explicit contiguous allocation policy (options -C y or --alloc contiguous) and no further adjacent contiguous extents are available.[5]

To fix this, prior to extending the logical volume, change its allocation policy with lvchange --alloc inherit logical_volume. If you need to keep the contiguous allocation policy, an alternative approach is to move the volume to a disk area with sufficient free extents. See [6].

Make sure to remove snapshot volumes before generating grub.cfg.

With a large number of snapshots, thin_check runs for a long enough time so that waiting for the root device times out. To compensate, add the rootdelay=60 kernel boot parameter to your boot loader configuration. Or, make thin_check skip checking block mappings (see [7]) and regenerate the initramfs:

If you use RAID, snapshots or thin provisioning and experience a delay on shutdown, make sure lvm2-monitor.service is started. See FS#50420.

See Power management/Suspend and hibernate#Hibernation into a thinly-provisioned LVM volume.

**Examples:**

Example 1 (unknown):
```unknown
Physical disks

  Disk1 (/dev/sda):
    ┌──────────────────────────────────────┬─────────────────────────────────────┐
    │ Partition1  50 GiB (Physical volume) │ Partition2 80 GiB (Physical volume) │
    │ /dev/sda1                            │ /dev/sda2                           │
    └──────────────────────────────────────┴─────────────────────────────────────┘

  Disk2 (/dev/sdb):
    ┌──────────────────────────────────────┐
    │ Partition1 120 GiB (Physical volume) │
    │ /dev/sdb1                            │
    └──────────────────────────────────────┘
```

Example 2 (unknown):
```unknown
LVM logical volumes

  Volume Group1 (/dev/MyVolGroup/ = /dev/sda1 + /dev/sda2 + /dev/sdb1):
    ┌─────────────────────────┬─────────────────────────┬──────────────────────────┐
    │ Logical volume1 15 GiB  │ Logical volume2 35 GiB  │ Logical volume3 200 GiB  │
    │ /dev/MyVolGroup/rootvol │ /dev/MyVolGroup/homevol │ /dev/MyVolGroup/mediavol │
    └─────────────────────────┴─────────────────────────┴──────────────────────────┘
```

Example 3 (unknown):
```unknown
/dev/VolumeGroupName/LogicalVolumeName
```

Example 4 (unknown):
```unknown
/dev/mapper/VolumeGroupName-LogicalVolumeName
```

---

## LLVM

**URL:** https://wiki.archlinux.org/title/LLVM

**Contents:**
- Toolchain
- See also

This article or section needs expansion.

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/Partition

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## LVM on software RAID

**URL:** https://wiki.archlinux.org/title/LVM_on_software_RAID

**Contents:**
- Introduction
  - Swap space
  - Boot loader
- Installation
  - Load kernel modules
  - Prepare the hard drives
  - RAID installation
    - Synchronization
    - Scrubbing
      - General Notes on Scrubbing

This article will provide an example of how to install and configure Arch Linux with Logical Volume Manager (LVM) on top of a software RAID.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Although RAID and LVM may seem like analogous technologies they each present unique features. This article uses an example with three similar 1TB SATA hard drives. The article assumes that the drives are accessible as /dev/sda, /dev/sdb, and /dev/sdc.

Many tutorials treat the swap space differently, either by creating a separate RAID1 array or a LVM logical volume. Creating the swap space on a separate array is not intended to provide additional redundancy, but instead, to prevent a corrupt swap space from rendering the system inoperable, which is more likely to happen when the swap space is located on the same partition as the root directory.

This tutorial will use Syslinux instead of GRUB. GRUB when used in conjunction with GPT requires an additional BIOS boot partition.

GRUB supports the default style of metadata currently created by mdadm (i.e. 1.2) when combined with an initramfs, which has replaced in Arch Linux with mkinitcpio. Syslinux only supports version 1.0, and therefore requires the --metadata=1.0 option.

Some boot loaders (e.g. GRUB Legacy, LILO) will not support any 1.x metadata versions, and instead require the older version, 0.90. If you would like to use one of those boot loaders make sure to add the option --metadata=0.90 to the /boot array during RAID installation.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Obtain the latest installation media and boot the Arch Linux installer as outlined in the installation guide.

Load the appropriate RAID (e.g. raid0, raid1, raid5, raid6, raid10) and LVM (i.e. dm-mod) modules. The following example makes use of RAID1 and RAID5.

Partition each hard drive with a 1 GiB /boot partition, a 4 GiB /swap partition, and a / partition that takes up the remainder of the disk.

The boot partition must be RAID1; i.e it cannot be striped (RAID0) or RAID5, RAID6, etc.. This is because GRUB does not have RAID drivers. Any other level will prevent your system from booting. Additionally, if there is a problem with one boot partition, the boot loader can boot normally from the other two partitions in the /boot array.

After creating the physical partitions, you are ready to setup the /boot, /swap, and / arrays with mdadm. It is an advanced tool for RAID management that will be used to create a /etc/mdadm.conf within the installation environment.

Create the / array at /dev/md0:

Create the /swap array at /dev/md1:

Create the /boot array at /dev/md2:

After you create a RAID volume, it will synchronize the contents of the physical partitions within the array. You can monitor the progress by refreshing the output of /proc/mdstat ten times per second with:

Further information about the arrays is accessible with:

Once synchronization is complete the State line should read clean. Each device in the table at the bottom of the output should read spare or active sync in the State column. active sync means each device is actively in the array.

It is good practice to regularly run data scrubbing to check for and fix errors.

To initiate a data scrub:

As with many tasks/items relating to mdadm, the status of the scrub can be queried:

To stop a currently running data scrub safely:

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

The check operation scans the drives for bad sectors and mismatches. Bad sectors are automatically repaired. If it finds mismatches, i.e., good sectors that contain bad data (the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below). This "do nothing" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

It is a good idea to set up a cron job as root to schedule a periodic scrub. See raid-checkAUR which can assist with this.

Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy. These non-0 counts will only exist in transient data areas where they do not pose a problem. However, since we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem. This fact is a source of false positives for RAID1 and RAID10 arrays. It is however recommended to still scrub to catch and correct any bad sectors there might be in the devices.

This section will convert the two RAIDs into physical volumes (PVs). Then combine those PVs into a volume group (VG). The VG will then be divided into logical volumes (LVs) that will act like physical partitions (e.g. /, /var, /home). If you did not understand that make sure you read the LVM Introduction section.

Make the RAIDs accessible to LVM by converting them into physical volumes (PVs) using the following command. Repeat this action for each of the RAID arrays created above.

Confirm that LVM has added the PVs with:

Next step is to create a volume group (VG) on the PVs.

Create a volume group (VG) with the first PV:

Confirm that LVM has added the VG with:

In this example we will create separate /, /var, /swap, /home LVs. The LVs will be accessible as /dev/VolGroupArray/<lvname>.

Create a /home LV that takes up the remainder of space in the VG:

Confirm that LVM has created the LVs with:

Since the installer builds the initramfs using /etc/mdadm.conf in the target system, you should update that file with your RAID configuration. The original file can simply be deleted because it contains comments on how to fill it correctly, and that is something mdadm can do automatically for you. So let us delete the original and have mdadm create you a new one with the current setup:

Follow the directions outlined the in #Installation section until you reach the Prepare Hard Drive section. Skip the first two steps and navigate to the Manually Configure block devices, filesystems and mountpoints page. Remember to only configure the PVs (e.g. /dev/VolGroupArray/lvhome) and not the actual disks (e.g. /dev/sda1).

mkinitcpio can use a hook to assemble the arrays on boot. For more information see mkinitcpio Using RAID. Add the mdadm_udev and lvm2 hooks to the HOOKS array in /etc/mkinitcpio.conf after udev.

Once it is complete you can safely reboot your machine:

Once you have successfully booted your new system for the first time, you will want to install the boot loader onto the other two disks (or on the other disk if you have only 2 HDDs) so that, in the event of disk failure, the system can be booted from any of the remaining drives (e.g. by switching the boot order in the BIOS). The method depends on the boot loader system you are using:

Log in to your new system as root and do:

Syslinux will deal with installing the boot loader to the MBR on each of the members of the RAID array:

Now that you are done, it is worth taking a second to archive off the partition state of each of your drives. This guarantees that it will be trivially easy to replace/rebuild a disk in the event that one fails. See fdisk#Backup and restore partition table.

For further information on how to maintain your software RAID or LVM review the RAID and LVM articles.

**Examples:**

Example 1 (unknown):
```unknown
/dev/VolGroupArray
```

Example 2 (unknown):
```unknown
--metadata=1.0
```

Example 3 (unknown):
```unknown
--metadata=0.90
```

Example 4 (unknown):
```unknown
# modprobe raid1
# modprobe raid5
# modprobe dm-mod
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/MBR

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## FAT

**URL:** https://wiki.archlinux.org/title/VFAT

**Contents:**
- File system creation
- Kernel configuration
- Writing to FAT32 as normal user
- Detecting FAT type
- See also

From Wikipedia:File Allocation Table:

To create a FAT filesystem, install dosfstools.

mkfs.fat supports creating FAT12, FAT16 and FAT32, see Wikipedia:File Allocation Table#Types for an explanation on their differences. mkfs.fat will select the FAT type based on the partition size, to explicitly create a certain type of FAT filesystem use the -F option. See mkfs.fat(8) for more information.

Format a partition to FAT32:

Here is an example of the default mount configuration in the kernel:

A short description of the options:

If the partition type detected by mount is VFAT then it will run the /usr/bin/mount.vfat script.

To write on a FAT32 partition, you must make a few changes to the fstab file.

The user option means that any user (even non-root) can mount and unmount the partition /dev/sdxY (mount(8) § Non-superuser mounts). rw gives read-write access.

For example, if your FAT32 partition is on /dev/sda9, and you wish to mount it to /mnt/fat32, then you would use:

Now, any user can mount it with:

Note that FAT does not support Linux file permissions. Each file will also appear to be executable. You may want to use the showexec option to only mark Windows executables (com, exe, bat) as executable. See mount(8) § Mount options for fat for more options.

If you need to know which type of FAT file system a partition uses, use the file command:

Alternatively you can use minfo from the mtools package:

**Examples:**

Example 1 (unknown):
```unknown
# mkfs.fat -F 32 /dev/partition
```

Example 2 (unknown):
```unknown
$ zgrep -e FAT -e DOS /proc/config.gz | sort -r
```

Example 3 (unknown):
```unknown
# DOS/FAT/NT Filesystems
CONFIG_FAT_FS=m
CONFIG_MSDOS_PARTITION=y
CONFIG_FAT_FS=m
CONFIG_MSDOS_FS=m
CONFIG_VFAT_FS=m
CONFIG_FAT_DEFAULT_CODEPAGE=437
CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"
CONFIG_NCPFS_SMALLDOS=y
```

Example 4 (unknown):
```unknown
CONFIG_FAT_DEFAULT_CODEPAGE
```

---

## ZFS

**URL:** https://wiki.archlinux.org/title/ZFS

**Contents:**
- Installation
  - Kernel-specific packages
  - DKMS
  - Required Dependencies
  - Root on ZFS
- Experimenting with ZFS
- Configuration
  - Automatic start
    - Using zfs-mount.service
    - Using zfs-mount-generator

ZFS is an advanced filesystem, originally developed and released by Sun Microsystems in 2005.

Described as "The last word in filesystems", ZFS is stable, fast, secure, and future-proof. Features of ZFS include: pooled storage (integrated volume management – zpool), Copy-on-write, snapshots, data integrity verification and automatic repair (scrubbing), RAID-Z, a maximum 16 exabyte file size, and a maximum 256 quadrillion zettabyte storage with no limit on number of filesystems (datasets) or files[1].

ZFS is licensed under the Common Development and Distribution License (CDDL). Because the CDDL is incompatible with the GPL, it is not possible for ZFS to be included in the Linux Kernel. This requirement, however, does not prevent a native Linux kernel module from being developed and distributed by a third party, as is the case with OpenZFS (previously named ZFS on Linux).

As a result of ZFS not being included in the Linux kernel:

The kernel modules for ZFS can be installed in two ways—either installing a package that provides the modules for a specific kernel version or using a DKMS package that builds the modules for installed kernels. See the following sections.

ZFS userspace utilities are provided by the zfs-utilsAUR package which is a dependency of all zfs kernel module packages.

Install from the archzfs repository or alternatively the Arch User Repository:

Test the installation by issuing zpool status on the command line. If an "insmod" error is produced, try depmod -a.

Users can make use of Dynamic Kernel Module Support (DKMS) to rebuild the ZFS modules automatically.

Install from the archzfs repository or alternatively the Arch User Repository:

To compile the ZFS modules provided by the aforementioned dkms packages, it is also necessary to install the appropriate headers package(s) for your installed kernel(s) (e.g. linux-headers for linux, linux-lts-headers for linux-lts, etc.). When either the dkms packages or the kernel is updated, the kernel modules will be automatically recompiled thanks to the DKMS pacman hook.

The package zfs-utils now requires libunwind as a dependency. Although it is not listed by any of the packages as a required dependency, yet, attempting to create a zpool or zfs mountpoint will result in failure.

See Install Arch Linux on ZFS#Installation.

Users wishing to experiment with ZFS on virtual block devices (known in ZFS terms as VDEVs) which can be simple files like ~/zfs0.img ~/zfs1.img ~/zfs2.img etc. with no possibility of real data loss are encouraged to see the Experimenting with ZFS article. Common tasks like building a RAIDZ array, purposefully corrupting data and recovering it, snapshotting datasets, etc. are covered.

ZFS is considered a "zero administration" filesystem by its creators; therefore, configuring ZFS is very straight forward. Configuration is done primarily with two commands: zfs and zpool.

For ZFS to live by its "zero administration" namesake, you probably want the pools to be automatically imported at boot time.

zfs-import-cache.service imports the zfs pools by reading the file /etc/zfs/zpool.cache. For each imported pool you want automatically imported by zfs-import-cache.service, execute:

To actually mount the ZFS filesystems (without listing the ZFS filesystems in /etc/fstab), you have 2 choices:

In order to mount ZFS filesystems automatically on boot you need to enable zfs-mount.service.

You can also use the zfs-mount-generator to create systemd mount units for your ZFS filesystems at boot. systemd will automatically mount the filesystems based on the mount units without having to use the zfs-mount.service. To do that, you need to:

You need to add a file in /etc/zfs/zfs-list.cache for each ZFS pool in your system. Make sure the required units and targets are enabled.

It is not necessary to partition the drives before creating the ZFS filesystem. It is recommended to point ZFS at an entire disk (ie. /dev/sdx rather than /dev/sdx1), which will automatically create a GPT (GUID Partition Table) and add an 8 MB reserved partition at the end of the disk for legacy bootloaders. However, you can specify a partition or a file within an existing filesystem, if you wish to create multiple volumes with different redundancy properties.

OpenZFS recommends using device IDs when creating ZFS storage pools of less than 10 devices[4]. Use Persistent block device naming#by-id and by-path to identify the list of drives to be used for ZFS pool.

The disk IDs should look similar to the following:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Disk labels and UUID can also be used for ZFS mounts by using GPT partitions. ZFS drives have labels but Linux is unable to read them at boot. Unlike MBR partitions, GPT partitions directly support both UUID and labels independent of the format inside the partition. Partitioning rather than using the whole disk for ZFS offers two additional advantages. The OS does not generate bogus partition numbers from whatever unpredictable data ZFS has written to the partition sector, and if desired, you can easily over provision SSD drives, and slightly over provision spindle drives to ensure that different models with slightly different sector counts can zpool replace into your mirrors. This is a lot of organization and control over ZFS using readily available tools and techniques at almost zero cost.

Use gdisk to partition the all or part of the drive as a single partition. gdisk does not automatically name partitions so if partition labels are desired use gdisk command "c" to label the partitions. Some reasons you might prefer labels over UUID are: labels are easy to control, labels can be titled to make the purpose of each disk in your arrangement readily apparent, and labels are shorter and easier to type. These are all advantages when the server is down and the heat is on. GPT partition labels have plenty of space and can store most international characters wikipedia:GUID_Partition_Table#Partition_entries allowing large data pools to be labeled in an organized fashion.

Drives partitioned with GPT have labels and UUID that look like this.

To create a ZFS pool:

Create pool with single raidz vdev:

Create pool with two mirror vdevs:

At pool creation, ashift=12 should always be used, except with SSDs that have 8k sectors where ashift=13 is correct. A vdev of 512 byte disks using 4k sectors will not experience performance issues, but a 4k disk using 512 byte sectors will. Since ashift cannot be changed after pool creation, even a pool with only 512 byte disks should use 4k because those disks may need to be replaced with 4k disks or the pool may be expanded by adding a vdev composed of 4k disks. Because correct detection of 4k disks is not reliable, -o ashift=12 should always be specified during pool creation. See the OpenZFS FAQ for more details.

Create pool with ashift=12 and single raidz vdev:

By default, zpool create enables all features on a pool. If /boot resides on ZFS when using GRUB you must only enable features supported by GRUB otherwise GRUB will not be able to read the pool. ZFS includes compatibility files (see /usr/share/zfs/compatibility.d) to assist in creating pools at specific feature sets, of which grub2 is an option.

You can create a pool with only the compatible features enabled:

If the command is successful, there will be no output. Using the mount command will show that the pool is mounted. Using zpool status will show that the pool has been created:

At this point it would be good to reboot the machine to ensure that the ZFS pool is mounted at boot. It is best to deal with all errors before transferring data.

Eventually a pool may fail to auto mount and you need to import to bring your pool back. Take care to avoid the most obvious solution.

Adapt one of the following commands to import your pool so that pool imports retain the persistence they were created with:

Finally check the state of the pool:

ZFS makes it easy to destroy a mounted storage pool, removing all metadata about the ZFS device.

To destroy a dataset:

And now when checking the status:

If a storage pool is to be used on another system, it will first need to be exported. It is also necessary to export a pool if it has been imported from the archiso as the hostid is different in the archiso as it is in the booted system. The zpool command will refuse to import any storage pools that have not been exported. It is possible to force the import with the -f argument, but this is considered bad form.

Any attempts made to import an un-exported storage pool will result in an error stating the storage pool is in use by another system. This error can be produced at boot time abruptly abandoning the system in the busybox console and requiring an archiso to do an emergency repair by either exporting the pool, or adding the zfs_force=1 to the kernel boot parameters (which is not ideal). See #On boot the zfs pool does not mount stating: "pool may be in use from other system".

A device (a partition or a disk) can be added to an existing zpool:

To import a pool which consists of multiple devices:

A device (a partition or a disk) can be attached aside an existing device to be its mirror (similar to RAID 1):

You can attach the new device to an already existing mirror vdev (e.g. to upgrade from a 2-device to a 3-device mirror) or attach it to single device to create a new mirror vdev.

Renaming a zpool that is already created is accomplished in 2 steps:

The mount point for a given zpool can be moved at will with one command:

When using a newer zfs module, zpools may display an upgrade indication:

To upgrade the version of zpool bigdata:

To upgrade the version of all zpools:

Users can optionally create a dataset under the zpool as opposed to manually creating directories under the zpool. Datasets allow for an increased level of control (quotas for example) in addition to snapshots. To be able to create and mount a dataset, a directory of the same name must not pre-exist in the zpool. To create a dataset, use:

It is then possible to apply ZFS specific attributes to the dataset. For example, one could assign a quota limit to a specific directory within a dataset:

To see all the commands available in ZFS, see zfs(8) or zpool(8).

ZFS offers the following supported encryption options: aes-128-ccm, aes-192-ccm, aes-256-ccm, aes-128-gcm, aes-192-gcm and aes-256-gcm. When encryption is set to on, aes-256-gcm will be used. See zfs-change-key(8) for a description of the native encryption, including limitations.

The following keyformats are supported: passphrase, raw, hex.

One can also specify/increase the default iterations of PBKDF2 when using passphrase with -o pbkdf2iters <n>, although it may increase the decryption time.

To create a dataset including native encryption with a passphrase, use:

To use a key instead of using a passphrase:

The easy way to make a key in human-readable form (keyformat=hex):

To verify the key location:

To change the key location:

You can also manually load the keys by using one of the following commands:

To mount the created encrypted dataset:

It is possible to automatically unlock a pool dataset on boot time by using a systemd unit. For example create the following service to unlock any specific dataset:

Enable/start the service for each encrypted dataset, (e.g. zfs-load-key@pool0-dataset0.service). Note the use of -, which is an escaped / in systemd unit definitions. See systemd-escape(1) for more info.

An alternative is to load all possible keys:

Enable/start zfs-load-key.service.

If you are not encrypting the root volume, but only the home volume or a user-specific volume, another idea is to wait until login to decrypt it[dead link 2024-11-06—HTTP 404]. The advantages of this method are that the system boots uninterrupted, and that when the user logs in, the same password can be used both to authenticate and to decrypt the home volume, so that the password is only entered once.

There are two methods for unlocking the home dataset: #PAM module or #Custom script. Both methods assume your datasets are structured similar to:

Replace rpool/home, user, and child with the values from your setup.

OpenZFS includes a PAM module since 2.0.0. It supports child datasets since 2.3.1.

First, use the following:

This stops systemd from automatically mounting rpool/home. This property will be inherited by all child datasets.

Then create the following file:

mount_recursively may be ommited if there are no child datasets in any of the users' datasets.

Finally, add the following to the beginning of /etc/pam.d/system-auth and /etc/pam.d/su-l:

First set the mountpoint to legacy to avoid having it mounted by zfs mount -a:

Ensure that it is in /etc/fstab so that mount /home will work:

Alternatively, you can keep using ZFS mounts if you use both:

The first will stop ZFS automatically mounting it, and the second systemd, but you will still be able to manually (or through the following scripts) mount it. If you have child datasets, org.openzfs.systemd:ignore=on will be inherited, but you will need to set canmount=noauto on each as it is not inheritable, otherwise they will try to mount without a mountpoint.

On a single-user system, with only one /home volume having the same encryption password as the user's password, it can be decrypted at login as follows: first create /usr/local/bin/mount-zfs-homedir

do not forget to make it executable; then get PAM to run it by adding the following line to /etc/pam.d/system-auth:

Now it will transparently decrypt and mount the /home volume when you log in anywhere: on the console, via ssh, etc.

A caveat is that since your ~/.ssh directory is not mounted, if you log in via ssh, you must use password authentication the first time rather than relying on ~/.ssh/authorized_keys.

If you do not wish to enable (insecure) password authentication, you can instead move ~/.ssh/authorized_keys to a new location. Make /etc/ssh/user_config/ and inside it a folder for each user, owned by that user and with 700 permissions. Then move each user's authorized_keys into their respective folders, and edit the system sshd configuration:

Then restart sshd.service. You can also optionally make a link for each user from ~/.ssh/authorized_keys to the new location so users can still edit it as they are used to.

This will let you log in, but your home partition will not be mounted, and you will need to do so manually. There are multiple options to work around this:

It is possible to set up PAM to only prompt for a password via SSH when it is necessary to decrypt your home partition. You will need to enable both publickey and keyboard-interactive authentication methods:

This will mean it asks for the password after validating the key, but using PAM we can stop it asking for the password when not needed. We make a script that will fail when the key is not available to us:

And make it executable.

Now we want to configure PAM to call this, and skip asking for the password if the script succeeds because we already have the key available. Add this line above the existing auth line(s) you want to skip (all of them unless you have something else set up) for the SSH service:

With this, you will be prompted for a password only when the key is not loaded.

A simpler option is to just enable both methods, meaning your key still gets checked, but then you have to type the password too, which will decrypt your home partition.

This works (and will not let anyone authenticate with just a password), but has the downside of requiring your password every time.

You can also specify something like:

This allows clients to either use either just a public key, or one and a password. Which the client will do will be based on the PreferredAuthentications option. -o PreferredAuthentications=password,publickey will ask for the password, while -o PreferredAuthentications=publickey will not. This is more manual than automated fallback, but has less moving parts, and avoids asking you every time if you prefer publickey by default (you can use host-specific options on clients to simplify setting these options).

ZFS does not allow to use swapfiles, but users can use a ZFS volume (ZVOL) as swap. It is important to set the ZVOL block size to match the system page size, which can be obtained by the getconf PAGESIZE command (default on x86_64 is 4KiB). Another option useful for keeping the system running well in low-memory situations is not caching the ZVOL data.

Create a 8 GiB zfs volume:

Prepare it as swap partition:

To make it permanent, edit /etc/fstab. ZVOLs support discard, which can potentially help ZFS's block allocator and reduce fragmentation for all other datasets when/if swap is not full.

Add a line to /etc/fstab:

To use ACL on a dataset:

Setting xattr is recommended for performance reasons [5].

It may be preferable to enable ACL on the zpool as datasets will inherit the ACL parameters. Setting aclinherit=passthrough may be wanted as the default mode is restricted [6]; however, it is worth noting that aclinherit does not affect POSIX ACLs [7]:

ZFS, unlike most other file systems, has a variable record size, or what is commonly referred to as a block size. By default, the recordsize on ZFS is 128KiB, which means it will dynamically allocate blocks of any size from 512B to 128KiB depending on the size of file being written. This can often help fragmentation and file access, at the cost that ZFS would have to allocate new 128KiB blocks each time only a few bytes are written to.

The factual accuracy of this article or section is disputed.

Most RDBMSes work in 8KiB-sized blocks by default. Although the block size is tunable for MySQL/MariaDB, PostgreSQL, and Oracle database, all three of them use an 8KiB block size by default. For both performance concerns and keeping snapshot differences to a minimum (for backup purposes, this is helpful), it is usually desirable to tune ZFS instead to accommodate the databases, using a command such as:

These RDBMSes also tend to implement their own caching algorithm, often similar to ZFS's own ARC. In the interest of saving memory, it is best to simply disable ZFS's caching of the database's file data and let the database do its own job:

ZFS uses the ZIL for crash recovery, but databases are often syncing their data files to the file system on their own transaction commits anyway. The end result of this is that ZFS will be committing data twice to the data disks, and it can severely impact performance. You can tell ZFS to prefer to not use the ZIL, and in which case, data is only committed to the file system once. However, doing so on non-solid state storage (e.g. HDDs) can result in decreased read performance due to fragmentation (OpenZFS Wiki) -- with mechanical hard drives, please consider using a dedicated SSD as ZIL rather than setting the option below. In addition, setting this for non-database file systems, or for pools with configured log devices, can also negatively impact the performance, so beware:

These can also be done at file system creation time, for example:

Please note: these kinds of tuning parameters are ideal for specialized applications like RDBMSes. You can easily hurt ZFS's performance by setting these on a general-purpose file system such as your /home directory.

If you would like to use ZFS to store your /tmp directory, which may be useful for storing arbitrarily-large sets of files or simply keeping your RAM free of idle data, you can generally improve performance of certain applications writing to /tmp by disabling file system sync. This causes ZFS to ignore an application's sync requests (eg, with fsync or O_SYNC) and return immediately. While this has severe application-side data consistency consequences (never disable sync for a database!), files in /tmp are less likely to be important and affected. Please note this does not affect the integrity of ZFS itself, only the possibility that data an application expects on-disk may not have actually been written out following a crash.

Additionally, for security purposes, you may want to disable setuid and devices on the /tmp file system, which prevents some kinds of privilege-escalation attacks or the use of device nodes:

Combining all of these for a create command would be as follows:

Please note, also, that if you want /tmp on ZFS, you will need to mask (disable) systemd's automatic tmpfs-backed /tmp (tmp.mount, else ZFS will be unable to mount your dataset at boot-time or import-time.

It is possible to pipe ZFS snapshots to an arbitrary target by pairing zfs send and zfs recv. This is done through standard output, which allows the data to be sent to any file, device, across the network, or manipulated mid-stream by incorporating additional programs in the pipe.

Below are examples of common scenarios:

First, create a snapshot of some ZFS filesystem:

Now send the snapshot to a new location on a different zpool:

The contents of zpool0/archive/books@snap are now live at zpool4/library

First, create a snapshot of some ZFS filesystem:

Write the snapshot to a gzip file:

Now restore the snapshot from the file:

First, create a snapshot of some ZFS filesystem:

Next we pipe our "send" traffic over an ssh session running "recv":

The -v flag prints information about the datastream being generated. If you are using a passphrase or passkey, you will be prompted to enter it.

You may wish update a previously sent ZFS filesystem without retransmitting all of the data over again. Alternatively, it may be necessary to keep a filesystem online during a lengthy transfer and it is now time to send writes that were made since the initial snapshot.

First, create a snapshot of some ZFS filesystem:

Next we pipe our "send" traffic over an ssh session running "recv":

Once changes are written, make another snapshot:

The following will send the differences that exist locally between zpool1/filestore@initial and zpool1/filestore@snap2 and create an additional snapshot for the remote filesystem coldstore/backups:

Now both zpool1/filestore and coldstore/backups have the @initial and @snap2 snapshots.

On the remote host, you may now promote the latest snapshot to become the active filesystem:

ZFS pools and datasets can be further adjusted using parameters.

To retrieve the current pool parameter status:

To retrieve the current dataset parameter status:

To disable access time (atime), which is enabled by default:

To disable access time (atime) on a particular dataset:

An alternative to turning off atime completely, relatime is available. This brings the default ext4/XFS atime semantics to ZFS, where access time is only updated if the modified time or changed time changes, or if the existing access time has not been updated within the past 24 hours. It is a compromise between atime=off and atime=on. This property only takes effect if atime is on:

Compression is just that, transparent compression of data. ZFS supports a few different algorithms, presently lz4 is the default, gzip is also available for seldom-written yet highly-compressible data; consult the OpenZFS Wiki for more details.

To enable compression:

To reset a property of a pool and/or dataset to its default state, use zfs inherit:

Whenever data is read and ZFS encounters an error, it is silently repaired when possible, rewritten back to disk and logged so you can obtain an overview of errors on your pools. There is no fsck or equivalent tool for ZFS. Instead, ZFS supports a feature known as scrubbing. This traverses through all the data in a pool and verifies that all blocks can be read.

To cancel a running scrub:

From the Oracle blog post Disk Scrub - Why and When?:

In the ZFS Administration Guide by Aaron Toponce, he advises to scrub consumer disks once a week.

Using a systemd timer/service it is possible to automatically scrub pools.

To perform scrubbing monthly on a particular pool:

Enable/start zfs-scrub@pool-to-scrub.timer unit for monthly scrubbing the specified zpool.

To quickly query your vdevs TRIM support, you can include trimming information in zpool status with -t.

ZFS is capable of trimming supported vdevs either on-demand or periodically via the autotrim property.

Manually performing a TRIM operation on a zpool:

Enabling periodic trimming on all supported vdevs in a pool:

To perform a full zpool trim monthly on a particular pool using a systemd timer/service:

Enable/start zfs-trim@pool-to-trim.timer unit for monthly trimming of the specified zpool.

If your pool has no configured log devices, ZFS reserves space on the pool's data disks for its intent log (the ZIL, also called SLOG). If your data disks are slow (e.g. HDD) it is highly recommended to configure the ZIL on solid state drives for better write performance and also to consider a layer 2 adaptive replacement cache (L2ARC). The process to add them is very similar to adding a new VDEV.

All of the below references to device-id are the IDs from /dev/disk/by-id/*.

To add a mirrored ZIL:

Or to add a single device ZIL (unsafe):

Because the ZIL device stores data that has not been written to the pool, it is important to use devices that can finish writes when power is lost. It is also important to use redundancy, since a device failure can cause data loss. In addition, the ZIL is only used for sync writes, so may not provide any performance improvement when your data drives are as fast as your ZIL drive(s).

L2ARC is only a read cache, so redundancy is unnecessary. Since ZFS version 2.0.0, L2ARC is persisted across reboots.[8]

L2ARC is generally only useful in workloads where the amount of hot data is bigger than system memory, but small enough to fit into L2ARC. The L2ARC is indexed by the ARC in system memory, consuming 70 bytes per record (default 128KiB). Thus, the equation for RAM usage is:

Because of this, L2ARC can, in certain workloads, harm performance as it takes memory away from ARC.

ZFS volumes (ZVOLs) can suffer from the same block size-related issues as RDBMSes, but it is worth noting that the default recordsize for ZVOLs is 8 KiB already. If possible, it is best to align any partitions contained in a ZVOL to your recordsize (current versions of fdisk and gdisk by default automatically align at 1MiB segments, which works), and file system block sizes to the same size. Other than this, you might tweak the recordsize to accommodate the data inside the ZVOL as necessary (though 8 KiB tends to be a good value for most file systems, even when using 4 KiB blocks on that level).

Each block of a ZVOL gets its own parity disks, and if you have physical media with logical block sizes of 4096B, 8192B, or so on, the parity needs to be stored in whole physical blocks, and this can drastically increase the space requirements of a ZVOL, requiring 2× or more physical storage capacity than the ZVOL's logical capacity. Setting the recordsize to 16k or 32k can help reduce this footprint drastically.

See OpenZFS issue #1807 for details.

While ZFS is expected to work well with modern schedulers including, mq-deadline, and none, experimenting with manually setting the I/O scheduler on ZFS disks may yield performance gains. The ZFS recomendation is "[...] users leave the default scheduler “unless you’re encountering a specific problem, or have clearly measured a performance improvement for your workload”"[9]

If the following error occurs then it can be fixed.

One reason this can occur is because ZFS expects pool creation to take less than 1 second[10][11]. This is a reasonable assumption under ordinary conditions, but in many situations it may take longer. Each drive will need to be cleared again before another attempt can be made.

The factual accuracy of this article or section is disputed.

A brute force creation can be attempted over and over again, and with some luck the ZPool creation will take less than 1 second. One cause for creation slowdown can be slow burst read writes on a drive. By reading from the disk in parallel to ZPool creation, it may be possible to increase burst speeds.

This can be done with multiple drives by saving the above command for each drive to a file on separate lines and running

Then run ZPool creation at the same time.

By default, ZFS caches file operations (ARC) using up to half of available system memory on the host. To adjust the ARC size, add the following to the Kernel parameters list:

In case that the default value of zfs_arc_min (1/32 of system memory) is higher than the specified zfs_arc_max it is needed to add also the following to the Kernel parameters list:

You may also want to increase zfs_arc_sys_free instead (in this example to 8GiB):

For a more detailed description, as well as other configuration options, see Gentoo:ZFS#ARC.

ZFS should release ARC as applications reserve more RAM, but some applications still get confused, and reported free RAM is always wrong. But in case all your applications work as intended and you have no problems, there is no need to change ARC settings.

The following error will occur when attempting to create a zfs filesystem,

The way to overcome this is to use -f with the zfs create command.

An error that occurs at boot with the following lines appearing before initscript output:

This warning occurs because the ZFS module does not have access to the spl hosted. There are two solutions, for this. Either place the spl hostid in the kernel parameters in the boot loader. For example, adding spl.spl_hostid=0x00bab10c.

The other solution is to make sure that there is a hostid in /etc/hostid, and then regenerate the initramfs image. Which will copy the hostid into the initramfs image.

In case you are booting a SAS/SCSI based, you might occassionally get boot problems where the pool you are trying to boot from cannot be found. A likely reason for this is that your devices are initialized too late into the process. That means that zfs cannot find any devices at the time when it tries to assemble your pool.

In this case you should force the scsi driver to wait for devices to come online before continuing. You can do this by putting this into /etc/modprobe.d/zfs.conf:

Afterwards, regenerate the initramfs.

This works because the zfs hook will copy the file at /etc/modprobe.d/zfs.conf into the initcpio which will then be used at build time.

If the new installation does not boot because the zpool cannot be imported, chroot into the installation and properly export the zpool. See #Emergency chroot repair with archzfs.

Once inside the chroot environment, load the ZFS module and force import the zpool,

To see the available pools, use,

It is necessary to export a pool because of the way ZFS uses the hostid to track the system the zpool was created on. The hostid is generated partly based on the network setup. During the installation in the archiso the network configuration could be different generating a different hostid than the one contained in the new installation. Once the zfs filesystem is exported and then re-imported in the new installation, the hostid is reset. See Re: Howto zpool import/export automatically? - msg#00227.

If ZFS complains about "pool may be in use" after every reboot, properly export pool as described above, and then regenerate the initramfs in normally booted system.

Double check that the pool is properly exported. Exporting the zpool clears the hostid marking the ownership. So during the first boot the zpool should mount correctly. If it does not there is some other problem.

Reboot again, if the zfs pool refuses to mount it means the hostid is not yet correctly set in the early boot phase and it confuses zfs. Manually tell zfs the correct number, once the hostid is coherent across the reboots the zpool will mount correctly.

Boot using zfs_force and write down the hostid. This one is just an example.

This number have to be added to the kernel parameters as spl.spl_hostid=0x0a0af0f8. Another solution is writing the hostid inside the initram image, see the installation guide explanation about this.

Users can always ignore the check adding zfs_force=1 in the kernel parameters, but it is not advisable as a permanent solution.

Once a drive has become faulted it should be replaced A.S.A.P. with an identical drive.

but in this instance, the following error is produced:

ZFS uses the ashift option to adjust for physical block size. When replacing the faulted disk, ZFS is attempting to use ashift=12, but the faulted disk is using a different ashift (probably ashift=9) and this causes the resulting error.

For Advanced Format disks with 4 KiB block size, an ashift of 12 is recommended for best performance. See OpenZFS FAQ: Performance Considerations and ZFS and Advanced Format disks.

Use zdb to find the ashift of the zpool: zdb , then use the -o argument to set the ashift of the replacement drive:

Check the zpool status for confirmation:

According to ZFS issue #840, this is a known issue since 2012 with ZFS-ZED which causes the resilvering process to constantly restart, sometimes get stuck and be generally slow for some hardware. The simplest mitigation is to stop zfs-zed.service until the resilver completes.

Your boot time can be significantly impacted if you update your intitramfs (eg when doing a kernel update) when you have additional but non-permanently attached pools imported because these pools will get added to your initramfs zpool.cache and ZFS will attempt to import these extra pools on every boot, regardless of whether you have exported it and removed it from your regular zpool.cache.

If you notice ZFS trying to import unavailable pools at boot, first run:

To check your zpool.cache for pools you do not want imported at boot. If this command is showing (a) additional, currently unavailable pool(s), run:

To clear the zpool.cache of any pools other than the pool named zroot. Sometimes there is no need to refresh your zpool.cache, but instead all you need to do is regenerate the initramfs.

ZFS logs changes to a pool's structure natively as a log of executed commands in a ring buffer (which cannot be turned off). The log may be helpful when restoring a degraded or failed pool.

Follow the Archiso steps for creating a fully functional Arch Linux live CD/DVD/USB image. To include ZFS support in the image, you can either build your choice of PKGBUILDs from the AUR or include prebuilt packages from one of the unofficial user repositories.

Build the ZFS packages you want by following the normal procedures. If you are unsure, zfs-dkmsAUR and zfs-utilsAUR are likely to be compatible with the widest range of other modifications to the Archiso image you may wish to perform. Proceed to set up a custom local repository. Include the resulting repository in the Pacman configuration of your new profile.

Include the built packages in the list of packages to be installed. The example below presumes you want to include the libunwind,zfs-dkmsAUR, and zfs-utilsAUR packages.

If you include any DKMS packages, make sure you also include headers for any kernels you are including in the ISO (for example, for the default linux kernel this would be linux-headers. Other kernels have their own respective headers packages).

Add the archzfs unofficial user repository to pacman.conf in your new Archiso profile.

Add the archzfs group to the list of packages to be installed (the archzfs repository provides packages for the x86_64 architecture only) as well as required dependencies.

Regardless of where you source your ZFS packages from, you should finish by building the ISO.

The zreplAUR package provides a ZFS automatic replication service, which could also be used as a snapshotting service much like snapper.

For details on how to configure the zrepl daemon, see the zrepl documentation. The configuration file should be located at /etc/zrepl/zrepl.yml. Then, run zrepl configcheck to make sure that the syntax of the config file is correct. Finally, enable zrepl.service.

sanoidAUR is a policy-driven tool for taking snapshots. Sanoid also includes syncoid, which is for replicating snapshots. It comes with systemd services and a timer.

Sanoid only prunes snapshots on the local system. To prune snapshots on the remote system, run sanoid there as well with prune options. Either use the --prune-snapshots command line option or use the --cron command line option together with the autoprune = yes and autosnap = no configuration options.

The zfs-auto-snapshot-gitAUR package provides a shell script to automate the management of snapshots, with each named by date and label (hourly, daily, etc), giving quick and convenient snapshotting of all ZFS datasets. The package also installs cron tasks for quarter-hourly, hourly, daily, weekly, and monthly snapshots. Optionally adjust the --keep parameter from the defaults depending on how far back the snapshots are to go (the monthly script by default keeps data for up to a year).

To prevent a dataset from being snapshotted at all, set com.sun:auto-snapshot=false on it. Likewise, set more fine-grained control as well by label, if, for example, no monthlies are to be kept on a snapshot, for example, set com.sun:auto-snapshot:monthly=false.

Once the package has been installed, enable and start the selected timers (zfs-auto-snapshot-{frequent,daily,weekly,monthly}.timer).

ZFS has support for creating shares by NFS or SMB.

Make sure NFS has been installed/configured, note there is no need to edit the /etc/exports file. For sharing over NFS the services nfs-server.service and zfs-share.service should be started.

To make a pool available on the network:

To make a dataset available on the network:

To enable read/write access for a specific ip-range(s):

To check if the dataset is exported successfully:

To view the current loaded exports state in more detail, use:

To view the current NFS share list by ZFS:

When sharing through SMB, using usershares in /etc/samba/smb.conf will allow ZFS to setup and create the shares. See Samba#Enable Usershares for details.

Create and set permissions on the user directory as root

To make a pool available on the network:

To make a dataset available on the network:

To check if the dataset is exported successfully:

To view the current SMB share list by ZFS:

Before OpenZFS version 0.8.0, ZFS did not support encryption directly (See #Native encryption). Instead, zpools can be created on dm-crypt block devices. Since the zpool is created on the plain-text abstraction, it is possible to have the data encrypted while having all the advantages of ZFS like deduplication, compression, and data robustness. Furthermore, utilizing dm-crypt will encrypt the zpools metadata, which the native encryption can inherently not provide.[12]

dm-crypt, possibly via LUKS, creates devices in /dev/mapper and their name is fixed. So you just need to change zpool create commands to point to that names. The idea is configuring the system to create the /dev/mapper block devices and import the zpools from there. Since zpools can be created in multiple devices (raid, mirroring, striping, ...), it is important all the devices are encrypted otherwise the protection might be partially lost.

For example, an encrypted zpool can be created using plain dm-crypt (without LUKS) with:

In the case of a root filesystem pool, the mkinitcpio.conf HOOKS line will enable the keyboard for the password, create the devices, and load the pools. It will contain something like:

Since the /dev/mapper/enc name is fixed no import errors will occur.

Creating encrypted zpools works fine. But if you need encrypted directories, for example to protect your users' homes, ZFS loses some functionality.

ZFS will see the encrypted data, not the plain-text abstraction, so compression and deduplication will not work. The reason is that encrypted data has always high entropy making compression ineffective and even from the same input you get different output (thanks to salting) making deduplication impossible. To reduce the unnecessary overhead it is possible to create a sub-filesystem for each encrypted directory and use eCryptfs on it.

For example to have an encrypted home: (the two passwords, encryption and login, must be the same)

To get into the ZFS filesystem from live system for maintenance, there are two options:

To start the recovery, load the ZFS kernel modules:

Mount the boot partition and EFI system partition (if any):

Chroot into the ZFS filesystem:

Check the kernel version:

uname will show the kernel version of the archiso. If they are different, run depmod (in the chroot) with the correct kernel version of the chroot installation:

This will load the correct kernel modules for the kernel version installed in the chroot installation.

Regenerate the initramfs. There should be no errors.

Here a bind mount from /mnt/zfspool to /srv/nfs4/music is created. The configuration ensures that the zfs pool is ready before the bind mount is created.

See systemd.mount(5) for more information on how systemd converts fstab into mount unit files with systemd-fstab-generator(8).

See ZED: The ZFS Event Daemon for more information.

An email forwarder, such as S-nail, is required to accomplish this. Test it to be sure it is working correctly.

Uncomment the following in the configuration file:

Update 'root' in ZED_EMAIL_ADDR="root" to the email address you want to receive notifications at.

If you are keeping your mailrc in your home directory, you can tell mail to get it from there by setting MAILRC:

This works because ZED sources this file, so mailx sees this environment variable.

If you want to receive an email no matter the state of your pool, you will want to set ZED_NOTIFY_VERBOSE=1. You will need to do this temporary to test.

Start and enable zfs-zed.service.

With ZED_NOTIFY_VERBOSE=1, you can test by running a scrub as root: zpool scrub <pool-name>.

Since it is so cheap to make a snapshot, we can use this as a measure of security for sensitive commands such as system and package upgrades. If we make a snapshot before, and one after, we can later diff these snapshots to find out what changed on the filesystem after the command executed. Furthermore we can also rollback in case the outcome was not desired.

A utility that automates the creation of pre and post snapshots around a shell command is znp.

and you would get snapshots created before and after the supplied command, and also output of the commands logged to file for future reference so we know what command created the diff seen in a pair of pre/post snapshots.

As of PR #261, archzfs supports SSH unlocking of natively-encrypted ZFS datasets. This section describes how to use this feature, and is largely based on dm-crypt/Specialties#Busybox based initramfs (built with mkinitcpio).

By default, mkinitcpio-tinyssh and mkinitcpio-dropbear listen on port 22. You may wish to change this.

For TinySSH, copy /usr/lib/initcpio/hooks/tinyssh to /etc/initcpio/hooks/tinyssh, and find/modify the following line in the run_hook() function:

For Dropbear, copy /usr/lib/initcpio/hooks/dropbear to /etc/initcpio/hooks/dropbear, and find/modify the following line in the run_hook() function:

Regenerate the initramfs.

First, we need to use puttygen.exe to import and convert the OpenSSH key generated earlier into PuTTY's .ppk private key format. We will call it zfs_unlock.ppk for this example.

The mkinitcpio-netconf process above does not setup a shell (nor do we need need one). However, because there is no shell, PuTTY will immediately close after a successful connection. This can be disabled in the PuTTY SSH configuration (Connection > SSH > [X] Do not start a shell or command at all), but it still does not allow us to see stdout or enter the encryption passphrase. Instead, we use plink.exe with the following parameters:

The plink command can be put into a batch script for ease of use.

To use cp --reflink and other commands needing bclone support, it is necessary to upgrade the feature flags if coming from a version prior to 2.2.2. This will allow the pool to have support for bclone. This is done with zpool upgrade, if the status of the pool show this is possible.

It is also required to enable a module parameter, otherwise userspace apps will not be able to use this feature. You can do this by putting this into /etc/modprobe.d/zfs.conf:

Check that is working, and how much space is being saved with the command: zpool get all POOLNAME | grep clon

**Examples:**

Example 1 (unknown):
```unknown
zpool status
```

Example 2 (unknown):
```unknown
zfs-import.target
```

Example 3 (unknown):
```unknown
zfs-import-cache.service
```

Example 4 (unknown):
```unknown
zfs-import-cache.service
```

---

## Securely wipe disk

**URL:** https://wiki.archlinux.org/title/Securely_wipe_disk

**Contents:**
- Common use cases
  - Wipe all data left on the device
  - Preparations for block device encryption
- Data remanence
  - Operating system, programs and filesystem
  - Hardware-specific issues
    - Flash memory
    - Marked Bad Sectors
    - Residual magnetism
- Select a target

Wiping a disk is done by writing new data over every single bit.

The most common usecase for completely and irrevocably wiping a device is when the device is going to be given away or sold. There may be (unencrypted) data left on the device and you want to protect against simple forensic investigation that is mere child's play with for example File recovery software.

If you want to quickly wipe everything from the disk, /dev/zero or simple patterns allow maximum performance while adequate randomness can be advantageous in some cases that should be covered up in #Data remanence.

Every overwritten bit means to provide a level of data erasure not allowing recovery with normal system functions (like standard ATA/SCSI commands) and hardware interfaces. Any file recovery software mentioned above then would need to be specialized on proprietary storage-hardware features.

In case of a HDD, data recreation will not be possible without at least undocumented drive commands or tinkering with the device's controller or firmware to make them read out for example reallocated sectors (bad blocks that S.M.A.R.T. retired from use).

There are different wiping issues with different physical storage technologies. Most notably, all Flash memory based devices and older magnetic storage (old HDDs, floppy disks, tape).

To prepare a drive for block device encryption inside the wiped area afterwards, it is recommended to use #Random data generated by a cryptographically strong random number generator (referred to as RNG in this article from now on).

See also Wikipedia:Random number generation.

See also Wikipedia:Data remanence. The representation of data may remain even after attempts have been made to remove or erase the data.

The operating system, executed programs or journaling file systems may copy your unencrypted data throughout the block device. When writing to plain disks, this should only be relevant in conjunction with one of the above.

If the data can be exactly located on the disk and was never copied anywhere else, wiping with pseudorandom data can be thoroughgoing and impressively quick.

A good example is cryptsetup using /dev/urandom for wiping the LUKS keyslots.

Write amplification and other characteristics make Flash memory, including SSDs, a stubborn target for reliable wiping. As there is a lot of transparent abstraction in between data as seen by a device's controller chip and the operating system, sight data is never overwritten in place and wiping particular blocks or files is not reliable.

Other "features" like transparent compression (all SandForce SSDs) can compress your zeros or repetitive patterns, so if wiping is fast beyond belief this might be the cause.

Disassembling Flash memory devices, unsoldering the chips and analyzing data content without the controller in between is feasible without difficulty using simple hardware. Data recovery companies do it for cheap money.

For more information see:

If a hard drive marks a sector as bad, it cordons it off, and the section becomes impossible to write to via software. Thus a full overwrite would not reach it. However because of block sizes, these sections would only amount to a few theoretically recoverable KiB.

A single, full overwrite with zeros or random data does not lead to any recoverable data on a modern high-density storage device. Note that repeating the operation should not be necessary nowadays. [1] Indications otherwise refer to single residual bits; reconstruction of byte patterns is generally not feasible.[2] See also [3], [4] and [5].

Use fdisk to locate all read/write devices the user has read access to.

Check the output for lines that start with devices such as /dev/sdX.

This is an example for a HDD formatted to boot a linux system:

Or another example with the Arch Linux image written to a 4GB USB thumb drive:

If you are worried about unintentional damage of important data on the primary computer, consider using an isolated environment such as a virtual environment (VirtualBox, VMWare, QEMU, etc...) with direct connected disk drives to it or a single computer only with a storage disk(s) that need to be wiped booted from a Live Media (USB, CD, PXE, etc...) or use a script to prevent wiping mounted partitions by typo.

To wipe sensitive data, one can use any data pattern matching the needs.

Overwriting with /dev/zero or simple patterns is considered secure in most situations. With today's HDDs, it is deemed appropriate and fast for disk wiping.

However, a drive that is abnormally fast in writing patterns or zeroing could be doing transparent compression. It is obviously presumable not all blocks get wiped this way. Some #Flash memory devices do "feature" that.

To setup block device encryption afterwards, one should wipe the area with random data (see next section) to avoid weakening the encryption.

/dev/urandom can be used as a fast and secure source of cryptographically secure pseudorandom data from the Linux kernel. For more details about sources of random and pseudorandom data, see Random number generation.

In the past when the kernel's random number generator was slow, a common alternative for pseudorandom data generation was to use an encrypted datastream, such as by encrypting /dev/zero with a random key. While this should in theory be secure, it no longer presents any advantages over the kernel's new, faster random number generator, and there is a risk that the temporary key may accidentally be saved someplace.

See also Wikipedia:Dd (Unix)#Block size, blocksize io-limits.

If you have an Advanced Format hard drive it is recommended that you specify a block size larger than the default 512 bytes. To speed up the overwriting process choose a block size matching your drive's physical geometry by appending the block size option to the dd command (i.e. bs=4096 for 4 KiB).

fdisk prints physical and logical sector size for every disk. Alternatively sysfs does expose information:

Block storage devices are divided in sectors, and the size of a single sector can be used to calculate the size of the entire device in bytes. To do so, multiply the number of sectors by the drive sector size.

As an example we use the parameters with the dd command to wipe a partition:

Here, to illustrate with a practical example, we will show the output of the fdisk command on the partition /dev/sdX:

To wipe partition /dev/sdX1, the example parameters with logical sectors would be used like follows.

with Start=2048, End=3839711231 and BytesInSector=512.

with LogicalSectors=3839709184.

Or, to wipe the whole disk by using physical sectors:

with AllDiskPhysicalSectors=488378646 and PhysicalSectorSizeBytes=4096.

You can choose from several utilities to overwrite a drive. If you only want to wipe a single file, Securely wipe disk/Tips and tricks#Wipe a single file has considerations in addition to the utilities mentioned below.

The redirected output can be used to create files, rewrite free space on the partition, and to wipe the whole device or a single partition on it. The examples here use /dev/zero to zero the device, but /dev/urandom may be substituted if a random wipe is desired.

The following examples show how to rewrite the partition or a block device by redirecting stdout from other utilities:

See also dd and Securely wipe disk/Tips and tricks#Wipe a single file.

Zero-fill the disk by writing a zero byte to every addressable location on the disk using the /dev/zero stream.

Or the /dev/urandom stream:

The process is finished when dd reports No space left on device and returns control back:

To speed up wiping a large drive, see also:

The file copy command cp(1) can also be used to rewrite the device, because it ignores the type of the destination:

Using pv will show a progress bar, the time spent and the estimated time till completion. Pass the selected data source to pv(1) and use the -o/--output option to specify the disk which will be written to. For example, to fill the disk /dev/sdX with /dev/zero:

A program specialized on wiping files. It is available as part of the wipe package. To make a quick wipe of a destination, you can use something like:

See also wipe(1). The tool was last updated in 2009. Its SourceForge page suggests that it is currently unmaintained.

shred (from the coreutils package) is a Unix command that can be used to securely delete individual files or full devices so that they can be recovered only with great difficulty with specialised hardware, if at all. By default shred uses three passes, writing pseudo-random data to the device during each pass. This can be reduced or increased.

The following command invokes shred with its default settings and displays the progress.

Shred can also be used on a single partition, e.g. to wipe the first partition use shred -v /dev/sdX1.

Alternatively, shred can be instructed to do only one pass, with entropy from e.g. /dev/urandom, and a final overwrite with zeros.

scrub iteratively writes patterns on files or disk devices to make retrieving the data more difficult.

The following command invokes scrub with the default settings, in mode 1, overwriting the target device using patterns compliant with NNSA Policy Letter NAP-14.x. This is the most effective method.

The following command invokes scrub with the default settings, in mode 2, overwriting the target file using patterns compliant with NNSA Policy Letter NAP-14.x, rounding the bytes written up to fill out the last file system block. Note that there are caveats for this mode, see the manual for further details.

The following command invokes scrub with the default settings, in mode 3, creating a directory and filling it with files until the file system is full. The files are then scrubbed using patterns compliant with NNSA Policy Letter NAP-14.x, rounding the bytes written up to fill out the last file system block. Note that there are caveats for this mode, see the manual for further details.

For further usage and information, see the manual.

The tool badblocks from e2fsprogs is able to perform destructive read-write test, effectively wiping the device. By default, it performs four passes and can take a long time.

hdparm supports ATA Secure Erase, which is functionally equivalent to zero-filling a disk. It is however handled by the hard drive firmware itself, and includes "hidden data areas". As such, it can be seen as a modern-day "low-level format" command. SSD drives reportedly achieve factory performance after issuing this command, but may not be sufficiently wiped (see #Flash memory).

Some drives support Enhanced Secure Erase, which uses distinct patterns defined by the manufacturer. If the output of hdparm -I for the device indicates a many-fold time advantage for the Enhanced erasure, the device probably has a hardware encryption feature and the wipe will be performed to the encryption keys only.

For detailed instructions on using ATA Secure Erase, see Solid state drive/Memory cell clearing and the Linux ATA wiki.

See Solid state drive/Memory cell clearing#Common method with blkdiscard

**Examples:**

Example 1 (unknown):
```unknown
/dev/urandom
```

Example 2 (unknown):
```unknown
Disk /dev/sda: 250.1 GB, 250059350016 bytes, 488397168 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00ff784a

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048      206847      102400   83  Linux
/dev/sda2          206848   488397167   244095160   83  Linux
```

Example 3 (unknown):
```unknown
Disk /dev/sdb: 4075 MB, 4075290624 bytes, 7959552 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x526e236e

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           0      802815      401408   17  Hidden HPFS/NTFS
```

Example 4 (unknown):
```unknown
/dev/urandom
```

---

## LLVM

**URL:** https://wiki.archlinux.org/title/LLVM_toolchain

**Contents:**
- Toolchain
- See also

This article or section needs expansion.

---

## FAT

**URL:** https://wiki.archlinux.org/title/FAT32

**Contents:**
- File system creation
- Kernel configuration
- Writing to FAT32 as normal user
- Detecting FAT type
- See also

From Wikipedia:File Allocation Table:

To create a FAT filesystem, install dosfstools.

mkfs.fat supports creating FAT12, FAT16 and FAT32, see Wikipedia:File Allocation Table#Types for an explanation on their differences. mkfs.fat will select the FAT type based on the partition size, to explicitly create a certain type of FAT filesystem use the -F option. See mkfs.fat(8) for more information.

Format a partition to FAT32:

Here is an example of the default mount configuration in the kernel:

A short description of the options:

If the partition type detected by mount is VFAT then it will run the /usr/bin/mount.vfat script.

To write on a FAT32 partition, you must make a few changes to the fstab file.

The user option means that any user (even non-root) can mount and unmount the partition /dev/sdxY (mount(8) § Non-superuser mounts). rw gives read-write access.

For example, if your FAT32 partition is on /dev/sda9, and you wish to mount it to /mnt/fat32, then you would use:

Now, any user can mount it with:

Note that FAT does not support Linux file permissions. Each file will also appear to be executable. You may want to use the showexec option to only mark Windows executables (com, exe, bat) as executable. See mount(8) § Mount options for fat for more options.

If you need to know which type of FAT file system a partition uses, use the file command:

Alternatively you can use minfo from the mtools package:

**Examples:**

Example 1 (unknown):
```unknown
# mkfs.fat -F 32 /dev/partition
```

Example 2 (unknown):
```unknown
$ zgrep -e FAT -e DOS /proc/config.gz | sort -r
```

Example 3 (unknown):
```unknown
# DOS/FAT/NT Filesystems
CONFIG_FAT_FS=m
CONFIG_MSDOS_PARTITION=y
CONFIG_FAT_FS=m
CONFIG_MSDOS_FS=m
CONFIG_VFAT_FS=m
CONFIG_FAT_DEFAULT_CODEPAGE=437
CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"
CONFIG_NCPFS_SMALLDOS=y
```

Example 4 (unknown):
```unknown
CONFIG_FAT_DEFAULT_CODEPAGE
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/GUID_Partition_Table

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## fdisk

**URL:** https://wiki.archlinux.org/title/Fdisk

**Contents:**
- Installation
- List partitions
- Backup and restore partition table
- Create a partition table and partitions
  - Create new table
  - Create partitions
    - Partition type
    - Partition number
    - First and last sector
  - Change partition type

util-linux fdisk is a dialogue-driven command-line utility that creates and manipulates partition tables and partitions on a hard disk. Hard disks are divided into partitions and this division is described in the partition table.

This article covers fdisk(8) and its related sfdisk(8) utility.

fdisk and its associated utilities are provided by the util-linux package, which is a dependency of the base meta package.

To list partition tables and partitions on a block device, you can run the following, where device is a name like /dev/sda, /dev/nvme0n1, /dev/mmcblk0, etc.:

Before making changes to a hard disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

For both GPT and MBR you can use sfdisk to save the partition layout of your device to a file with the -d/--dump option. Run the following command for device /dev/sda:

The file should look something like this for a single ext4 partition that is 1 GiB in size:

To later restore this layout you can run:

The first step to partitioning a disk is making a partition table. After that, the actual partitions are created according to the desired partition scheme. See the partition table article to help decide whether to use MBR or GPT.

Before beginning, you may wish to backup your current partition table and scheme.

fdisk performs partition alignment automatically on a 2048 512-byte sector (1 MiB) block size base which should be compatible with all Advanced Format HDDs and the vast majority of SSDs if not all. This means that the default settings will give you proper alignment.

To use fdisk, run the program with the name of the block device you want to change/edit. This example uses /dev/sda:

This opens the fdisk dialogue where you can type in commands.

To create a new partition table and clear all current partition data type g at the prompt for a GUID Partition Table (GPT) or o for an MBR partition table. Skip this step if the table you require has already been created.

Create a new partition with the n command. You must enter a partition number, starting sector, and an ending sector. If formatting with MBR, it may also require a partition type.

When using MBR, fdisk will ask for the MBR partition type. Specify it, type p to create a primary partition or e to create an extended one. There may be up to four primary partitions.

fdisk does not ask for the partition type ID and uses 'Linux filesystem' by default; you can change it later.

A partition number is the number assigned to a partition, e.g. a partition with number 1 on a disk /dev/sda would be /dev/sda1, /dev/nvme0n1p1 on /dev/nvme0n1 and /dev/mmcblk0p1 on /dev/mmcblk0. See Device file#Partition for details on the naming scheme. Partition numbers may not always match the order of partitions on disk, in which case they can be sorted.

It is advised to choose the default number suggested by fdisk.

The first sector must be specified in absolute terms using sector numbers. The last sector can be specified using the absolute position in sector numbers or as positions measured in kibibytes (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P);

The position of the last sector can be specified in:

Pressing the Enter key with no input specifies the default value, which is the start of the largest available block for the first sector and the end of the same block for the last sector.

Repeat this procedure until you have the partitions you desire.

Each partition is associated with a type. MBR uses partition IDs; GPT uses Partition type GUIDs.

Press t to change the type of a partition. You can use an alias for common partition types:

You can make an MBR partition bootable (a.k.a. active) by typing a.

To create a file system on the new partition, see File systems#Create a file system.

In order to move a partition, you need to have free space available where the partition will be moved. If necessary, you can make room by shrinking your partitions and the filesystems on them. See Parted#Shrinking partitions. To relocate a partition:

Where sectors is the number of sectors to move the partition (the + indicates moving it forward), device is the device that holds the partition, and number is the partition number. Note that if you add a new partition in the middle or at the beginning of your disk, you will likely want to renumber the partitions. See #Sort partitions or the "extra functionality" mode of fdisk.

This applies for when a new partition is created in the space between two partitions or a partition is deleted. /dev/sda is used in this example.

After sorting the partitions if you are not using Persistent block device naming, it might be required to adjust the /etc/fstab and/or the /etc/crypttab configuration files.

**Examples:**

Example 1 (unknown):
```unknown
/dev/nvme0n1
```

Example 2 (unknown):
```unknown
/dev/mmcblk0
```

Example 3 (unknown):
```unknown
# fdisk -l /dev/sda
```

Example 4 (unknown):
```unknown
/proc/partitions
```

---

## Ext4

**URL:** https://wiki.archlinux.org/title/Ext4

**Contents:**
- Create a new ext4 filesystem
  - Bytes-per-inode ratio
  - Reserved blocks
- Migrating from ext2/ext3 to ext4
  - Mounting ext2/ext3 partitions as ext4 without converting
    - Rationale
    - Procedure
  - Converting ext2/ext3 partitions to ext4
    - Rationale
    - Procedure

From Ext4 - Linux Kernel Newbies:

To format a partition do:

See mke2fs(8) for more options.

Creating a new file, directory, symlink etc. requires at least one free inode. If the inode count is too low, no file can be created on the filesystem even though there is still space left on it.

Because it is not possible to change either the bytes-per-inode ratio or the inode count after the filesystem is created, mkfs.ext4 uses by default a rather low ratio of one inode every 16384 bytes (16 KiB) to avoid this situation.

However, for partitions with size in the hundreds or thousands of GB and average file size in the megabyte range, this usually results in a much too large inode number because the number of files created never reaches the number of inodes.

This results in a waste of disk space, because all those unused inodes each take up 256 bytes on the filesystem (this is also set in /etc/mke2fs.conf but should not be changed). 256 * several millions = quite a few gigabytes wasted in unused inodes.

This situation can be evaluated by comparing the Use% and IUse% figures provided by df and df -i:

To specify a different bytes-per-inode ratio, use the -T usage-type option which hints at the expected usage of the filesystem using types defined in /etc/mke2fs.conf. Among those types are the bigger largefile and largefile4 which offer more relevant ratios of one inode every 1 MiB and 4 MiB respectively. It can be used as such:

The bytes-per-inode ratio can also be set directly via the -i option: e.g. use -i 2097152 for a 2 MiB ratio and -i 6291456 for a 6 MiB ratio.

By default, 5% of the filesystem blocks will be reserved for the super-user, to avoid fragmentation and "allow root-owned daemons to continue to function correctly after non-privileged processes are prevented from writing to the filesystem" (from mke2fs(8)).

For modern high-capacity disks, this is higher than necessary if the partition is used as a long-term archive or not crucial to system operations (like /home). See this email for the opinion of ext4 developer Ted Ts'o on reserved blocks and this superuser answer for general background on this topic.

It is generally safe to reduce the percentage of reserved blocks to free up disk space when the partition is either:

The -m option of ext4-related utilities allows to specify the percentage of reserved blocks.

To totally prevent reserving blocks upon filesystem creation, use:

To change it to 1% afterwards, use:

To set the number of reserved block space to an absolute size in gigabytes, use -r:

blocksize is the block size of the filesystem in bytes. This is almost always 4096; check to be sure:

The $(()) syntax is for math expansion. This syntax works in bash and zsh, but it will not work in fish. For fish, this is the syntax:

These commands can be applied to currently-mounted filesystems and changes will take effect immediately. Use findmnt(8) to find the device name:

To query the current number of reserved blocks:

This is the number of blocks, so this has to be multiplied by the filesystem's block size to get the number of bytes or gigabytes: 2975334 * 4096 / 1024**3 = 11.34 GiB.

A compromise between fully converting to ext4 and simply remaining with ext2/ext3 is to mount the partitions as ext4.

To experience the benefits of ext4, an irreversible conversion process must be completed.

These instructions were adapted from Kernel documentation and an BBS thread.

In the following steps /dev/sdxX denotes the path to the partition to be converted, such as /dev/sda1.

The ext4 file system records information about when a file was last accessed and there is a cost associated with recording it. See fstab#atime options for the noatime and related options.

The sync interval for data and metadata can be increased by providing a higher time delay to the commit option.

The default 5 sec means that if the power is lost, one will lose as much as the latest 5 seconds of work. It forces a full sync of all data/journal to physical media every 5 seconds. The filesystem will not be damaged though, thanks to the journaling. The following fstab illustrates the use of commit:

Ext4 enables write barriers by default. It ensures that file system metadata is correctly written and ordered on disk, even when write caches lose power. This goes with a performance cost especially for applications that use fsync heavily or create and delete many small files. For disks that have a write cache that is battery-backed in one way or another, disabling barriers may safely improve performance.

To turn barriers off, add the option barrier=0 to the desired filesystem. For example:

Disabling the journal with ext4 can be done with the following command on an unmounted disk:

The Fast commits for ext4 article introduction summarizes succinctly why and how the mount options data=journal or data=writeback speed up overall ext4 performance, compared to the default data=ordered operation mode. In addition, the journaling itself can be sped up by adding the journal_async_commit mount option.

A further option is to to use a newer journal format, see #Enabling fast_commit.

If using the non-default data= options, a dedicated device for the journal may also speed up file operations in some cases. For example, when a relatively slow device is used for the data itself and another (faster but smaller) device for the journal. To set up a separate journal device:

To assign journal_device as the journal of ext4_device, use:

Replace tune2fs with mkfs.ext4 if wanting to make a new filesystem on ext4_device.

Add the journal_device as a dependency of the ext4_device using the x-systemd.requires mount option in /etc/fstab:

This prevents issues if journal_device needs any setup (e.g. it is encrypted).

Ignore the saved devnum and force loading of the journal by path using the journal_path mount option:

e2fsck will look up the journal device using the UUID and fix the saved devnum if it goes out of sync. However, it will consider this as corruption and trigger an unnecessary full filesystem scan [5]. This can be disabled in e2fsck's config file:

Since Linux 4.1, ext4 natively supports file encryption, see the fscrypt article. Encryption is applied at the directory level, and different directories can use different encryption keys. This is different from both dm-crypt, which is block-device level encryption, and from eCryptfs, which is a stacked cryptographic filesystem.

When a filesystem has been created with e2fsprogs 1.43 (2016) or later, metadata checksums are enabled by default. Existing filesystems may be converted to enable metadata checksum support.

To read more about metadata checksums, see the ext4 wiki.

First the partition needs to be checked and optimized using e2fsck:

Convert the filesystem to 64-bit:

Finally enable checksums support:

The e2scrub tool checks metadata of the ext4 filesystem, if it is used in LVM logical volumes. The volume group must have 256MiB unallocated space for this check, because the tool creates a snapshot to check. As noted by the e2scrub(8) manual the tool does not repair errors, but report them and marks the filesystem to require an e2fsck (see e2fsck(8)) run prior to the next mount.

The check can be automated, for example by enabling the packaged e2scrub_all.timer unit.

If the minimum 256MiB unallocated space is missing, see LVM#Resizing the logical volume and file system in one go.

The ext4 "fast commits" feature introduces a new, lighter-weight journaling method. It is expected to significantly increase the performance of the ext4 filesystem,[6]

To enable on the feature on a new filesystem, include fast_commit in the -O file system options argument.

To enable the feature on an existing file system, run:

To query the current configuration:

To disable the feature on an existing file system, run:

ext4 can be used in case-insensitive mode, which can increase the performance of applications and games running in Wine. This feature does not affect the entire file system, only directories that have the case-insensitive attribute enabled.

First, enable the feature in the file system:

Enable the case-insensitive attribute in any directory:

Note that the directory must be empty, and moving subdirectories from elsewhere will not cause them to inherit the attribute, so plan ahead accordingly.

**Examples:**

Example 1 (unknown):
```unknown
# mkfs.ext4 /dev/partition
```

Example 2 (unknown):
```unknown
/etc/mke2fs.conf
```

Example 3 (unknown):
```unknown
/etc/mke2fs.conf
```

Example 4 (unknown):
```unknown
$ df -h /home
```

---

## Bcachefs

**URL:** https://wiki.archlinux.org/title/Bcachefs

**Contents:**
- Installation
- Setup
  - Single drive
  - Multiple drives
  - Encrypted root filesystem
  - SSD caching
  - Mounting
- Configuration
  - Changing a device's group
  - Adding a device

This article or section is out of date.

Bcachefs is a copy on write (CoW) file system with support for multiple devices, RAID, compression, checksumming and encryption. It aims to provide modern features similar to those of Btrfs and ZFS.

It is built upon Bcache and is mainly developed by Kent Overstreet.

In-tree kernel module was removed at Linux 6.18.

Install bcachefs-tools and bcachefs-dkms.

Bcachefs stripes data by default, similar to RAID0. Redundancy is handled via the replicas option. 2 drives with --replicas=2 is equivalent to RAID1, 4 drives with --replicas=2 is equivalent to RAID10, etc.

Heterogeneous drives are supported. If they are different sizes, larger stripes will be used on some, so that they all fill up at the same rate. If they are different speeds, reads for replicated data will be sent to the ones with the lowest IO latency. If some are more reliable than others (a hardware raid device, for example) you can set --durability=2 device to count each copy of data on that device as 2 replicas.

Bcachefs uses a self-rolled whole filesystem encryption using ChaCha20Poly1305. To format an encrypted filesystem:

In the case of a root filesystem add bcachefs to the HOOKS array in the /etc/mkinitcpio.conf configuration to prompt for filesystem unlock at boot or resuming from hibernate.

Bcachefs has four storage targets: metadata, background, foreground, and promote. Writes to the filesystem prioritize the foreground drives, which are then moved to the background over time. Reads are cached on the promote drives. The metadata target is usually leveraged with ultra-low read-latency NVME drives like Intel Optane.

A recommended configuration is to use an ssd group for the foreground and promote, and an hdd group for the background (a writeback cache).

For a writethrough cache, do the same as above, but set --durability=0 device on each of the ssd devices. For a writearound cache, foreground target to the hdd group, and promote target to the ssd group.

The default way of mounting is to specify every device in the mount directive.

The mount.bcachefs command supports mounting a filesystem by UUID, which is displayed by bcachefs format on filesystem creation.

To mount a single or multi-device on boot, add bcachefs to the HOOKS array in /etc/mkinitcpio.conf and regenerate the initramfs.

This article or section needs expansion.

Most options can be set

Mount options override those set by the other methods, which save them to the filesystem's superblock.

Examples of some available options are:

More options can be found in the bcachefs documentation.

The following can also be set on a per directory or per file basis with bcachefs setattr file --option=value. It will propagate options recursively if you set it on a directory.

To check what options are active you can do getfattr -d -m 'bcachefs_effective\.' directory/file

The group of a device can be changed through the sysfs.

If this is the first drive in a group, you will need to change the target settings to make use of it. This example is for adding a cache drive.

First make sure there are at least 2 metadata replicas (Evacuate does not appear to work for metadata). If your data and metadata are already replicated, you may skip this step.

Setting state ro meaning read-only.

To remove the device:

Metadata and data replication levels in Bcachefs can be configured independently to control redundancy and durability. The following options define both the synchronous (immediate) replication, which is performed atomically at write time to ensure data integrity, and the eventual replication target, which is fulfilled asynchronously in the background to improve redundancy and fault tolerance:

Compression is set with the --compression= option. It is also possible to set the compression level. As an example to set zstd compression level 5, you can use --compression=zstd:5.

Bcachefs supports subvolumes and snapshots with a similar userspace interface as Btrfs. A new subvolume may be created empty, or it may be created as a snapshot of another subvolume. Snapshots are writeable and may be snapshot-ted again, creating a tree of snapshots.

Snapshots are very cheap to create: they’re not based on cloning of COW btrees as with Btrfs, but instead are based on versioning of individual keys in the btrees. Many thousands or millions of snapshots can be created, with the only limitation being disk space.

To create a new, empty subvolume:

To delete an existing subvolume or snapshot:

To create a snapshot of an existing subvolume:

A subvolume can also be deleting with a normal rmdir after deleting all the contents, as with rm -rf.

Features including recursive snapshot creation and a method for recursively listing subvolume are still to be implemented.

This article or section needs expansion.

Check the journal for more useful error messages.

Some bcachefs format flags are set based upon their argument order and only affect drives that come after the flag is toggled. For example, if you want SSDs to have --durability=0 and enable --discard while HDDs use defaults, make sure arguments are passed in the following order:

It is possible to set replica count after format using set-fs-option.

Afterwards you'll need to tell bcachefs to ensure that all files have a replica with:

Some 32-bit programs may fail to retrieve contents of directories in Bcachefs, due to incompatibility of data returned by the filesystem when a readdir(3) syscall is performed. [3]

This can be worked around by temporarily using a different filesystem, such as tmpfs, for such a program to read and write from.

Bcachefs does not currently support swapfiles.

There is currently a bug in systemd that does not make it possible for it to mount a multi-device bcachefs filesystem at boot using devices separated by colons in fstab. It will work when doing mount -a, but will not mount at boot. However since bcachefs-tools version 1.7.0 it is possible to mount a multi-device array using one device node; this allows the use of the normal UUID specifier.

The filesystem UUID / External UUID can be found by either using:

When the mounting of a device created with the --encrypted option fails after bcachefs unlock /dev/sdXY with

It can be worked-around by manually linking the keys to the session[4]:

The renewed entry of the passphrase queried by mount is not necessary (pressing Enter suffices).

**Examples:**

Example 1 (unknown):
```unknown
# bcachefs format /dev/sdX
# mount -t bcachefs /dev/sdX /mnt
```

Example 2 (unknown):
```unknown
--replicas=2
```

Example 3 (unknown):
```unknown
--replicas=2
```

Example 4 (unknown):
```unknown
# bcachefs format /dev/sdX /dev/sdY --replicas=n
# mount -t bcachefs /dev/sdX:/dev/sdY /mnt
```

---

## LVM

**URL:** https://wiki.archlinux.org/title/LVM2

**Contents:**
- Background
  - LVM building blocks
  - Advantages
  - Disadvantages
- Installation
- Volume operations
  - Physical volumes
    - Creating
    - Growing
    - Shrinking

From Wikipedia:Logical Volume Manager (Linux):

Logical Volume Management utilizes the kernel's device-mapper feature to provide a system of partitions independent of underlying disk layout. With LVM you abstract your storage and have "virtual partitions", making extending/shrinking easier (subject to potential filesystem limitations).

Virtual partitions allow addition and removal without worry of whether you have enough contiguous space on a particular disk, getting caught up fdisking a disk in use (and wondering whether the kernel is using the old or new partition table), or, having to move other partitions out of the way.

Basic building blocks of LVM:

LVM gives you more flexibility than just using normal hard drive partitions:

Make sure the lvm2 package is installed.

If you have LVM volumes not activated via the initramfs, enable lvm2-monitor.service, which is provided by the lvm2 package.

To create a PV on /dev/sda1, run:

You can check the PV is created using the following command:

After extending or prior to reducing the size of a device that has a physical volume on it, you need to grow or shrink the PV using pvresize(8).

To expand the PV on /dev/sda1 after enlarging the partition, run:

This will automatically detect the new size of the device and extend the PV to its maximum.

To shrink a physical volume prior to reducing its underlying device, add the --setphysicalvolumesize size parameters to the command, e.g.:

The above command may leave you with this error:

Indeed pvresize will refuse to shrink a PV if it has allocated extents after where its new end would be. One needs to run pvmove beforehand to relocate these elsewhere in the volume group if there is sufficient free space.

Before freeing up physical extents at the end of the volume, one must run pvdisplay -v -m to see them. An alternative way to view segments in a tabular form is pvs --segments -v.

In the below example, there is one physical volume on /dev/sdd1, one volume group vg1 and one logical volume backup.

One can observe FREE space are split across the volume. To shrink the physical volume, we must first move all used segments to the beginning.

Here, the first free segment is from 0 to 153600 and leaves us with 153601 free extents. We can now move this segment number from the last physical extent to the first extent. The command will thus be:

Once all your free physical segments are on the last physical extents, run vgdisplay with root privileges and see your free PE.

Then you can now run again the command:

Last, you need to shrink the partition with your favorite partitioning tool.

To create a VG MyVolGroup with an associated PV /dev/sdb1, run:

You can check the VG MyVolGroup is created using the following command:

You can bind multiple PVs when creating a VG like this:

By default, this will reactivate the volume group when applicable. For example, if you had a drive failure in a mirror and you swapped the drive; and ran (1) pvcreate, (2) vgextend and (3) vgreduce --removemissing --force.

To start the rebuilding process of the degraded mirror array in this example, you would run:

You can monitor the rebuilding process (Cpy%Sync Column output) with:

This will deactivate the volume group and allow you to unmount the container it is stored in.

Use the vgrename(8) command to rename an existing volume group.

Either of the following commands renames the existing volume group MyVolGroup to my_volume_group

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the renamed volume group.

You first create a new physical volume on the block device you wish to use, then extend your volume group

This of course will increase the total number of physical extents on your volume group, which can be allocated by logical volumes as you see fit.

If you created a logical volume on the partition, remove it first.

All of the data on that partition needs to be moved to another partition. Fortunately, LVM makes this easy:

If you want to have the data on a specific physical volume, specify that as the second argument to pvmove:

Then the physical volume needs to be removed from the volume group:

Or remove all empty physical volumes:

For example: if you have a bad disk in a group that cannot be found because it has been removed or failed:

And lastly, if you want to use the partition for something else, and want to avoid LVM thinking that the partition is a physical volume:

To create a LV homevol in a VG MyVolGroup with 300 GiB of capacity, run:

or, to create a LV homevol in a VG MyVolGroup with the rest of capacity, run:

To create the LV while restricting it to specific PVs within the VG, append them to the command:

The new LV will appear as /dev/MyVolGroup/homevol. Now you can format the LV with an appropriate file system.

You can check the LV is created using the following command:

To rename an existing logical volume, use the lvrename(8) command.

Either of the following commands renames logical volume old_vol in volume group MyVolGroup to new_vol.

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the renamed logical volume.

Extend the logical volume mediavol in MyVolGroup by 10 GiB and resize its file system all at once:

Set the size of logical volume mediavol in MyVolGroup to 15 GiB and resize its file system all at once:

If you want to fill all the free space on a volume group, use the following command:

See lvresize(8) for more detailed options.

For file systems not supported by fsadm(8) will need to use the appropriate utility to resize the file system before shrinking the logical volume or after expanding it.

To extend logical volume mediavol within volume group MyVolGroup by 2 GiB without touching its file system:

Now expand the file system (ext4 in this example) to the maximum size of the underlying logical volume:

For Btrfs, btrfs-filesystem(8) expects the mountpoint instead of the device, the equivalent is:

To reduce the size of logical volume mediavol in MyVolGroup by 500 MiB, first calculate the resulting file system size and shrink the file system (Ext4 in this example) to the new size:

Unlike Ext4, Btrfs supports online shrinking (again, a mountpoint should be specified) e.g.:

When the file system is shrunk, reduce the size of logical volume:

To calculate the exact logical volume size for ext2, ext3, ext4 file systems, use a simple formula: LVM_EXTENTS = FS_BLOCKS × FS_BLOCKSIZE ÷ LVM_EXTENTSIZE.

Passing --resizefs will confirm that the correctness.

See lvresize(8) for more detailed options.

First, find out the name of the logical volume you want to remove. You can get a list of all logical volumes with:

Next, look up the mountpoint of the chosen logical volume:

Then unmount the filesystem on the logical volume:

Finally, remove the logical volume:

Confirm by typing in y.

Make sure to update all configuration files (e.g. /etc/fstab or /etc/crypttab) that reference the removed logical volume.

You can verify the removal of the logical volume by typing lvs as root again (see first step of this section).

LVM supports CoW (Copy-on-Write) snapshots. A CoW snapshot initially points to the original data. When data blocks are overwritten, the original copy is left intact and the new blocks are written elsewhere on-disk. This has several desirable properties:

LVM snapshots are at the block level. They make a new block device, with no apparent relationship to the original except when dealing with the LVM tools. Therefore, deleting files in the original copy does not free space in the snapshots. If you need filesystem-level snapshots, you rather need btrfs, ZFS or bcachefs.

You create snapshot logical volumes just like normal ones.

With that volume, you may modify less than 100 MiB of data, before the snapshot volume fills up.

Reverting the modified lvol logical volume to the state when the snap01vol snapshot was taken can be done with

In case the origin logical volume is active, merging will occur on the next reboot (merging can be done even from a LiveCD).

Also multiple snapshots can be taken and each one can be merged with the origin logical volume at will.

A snapshot provides a frozen copy of a file system to make backups. For example, a backup taking two hours provides a more consistent image of the file system than directly backing up the partition.

The snapshot can be mounted and backed up with dd or tar. The size of the backup file done with dd will be the size of the files residing on the snapshot volume. To restore just create a snapshot, mount it, and write or extract the backup to it. And then merge it with the origin.

See Create root filesystem snapshots with LVM for automating the creation of clean root file system snapshots during system startup for backup and rollback.

This article or section needs expansion.

See dm-crypt/Encrypting an entire system#LUKS on LVM and dm-crypt/Encrypting an entire system#LVM on LUKS for the possible schemes of combining LUKS with LVM.

This article or section needs expansion.

Convert your fast disk (/dev/fastdisk) to PV and add to your existing VG (MyVolGroup):

Create a cache pool with automatic meta data on /dev/fastdisk and convert the existing LV MyVolGroup/rootvol to a cached volume, all in one step:

Cachemode has two possible options:

If a specific --cachemode is not indicated, the system will assume writethrough as default.

If you ever need to undo the one step creation operation above:

This commits any pending writes still in the cache back to the origin LV, then deletes the cache. Other options are available and described in lvmcache(7).

LVM may be used to create a software RAID. It is a good choice if the user does not have hardware RAID and was planning on using LVM anyway. From lvmraid(7):

LVM RAID supports RAID 0, RAID 1, RAID 4, RAID 5, RAID 6 and RAID 10. See Wikipedia:Standard RAID levels for details on each level.

Create physical volumes:

Create volume group on the physical volumes:

Create logical volumes using lvcreate --type raidlevel, see lvmraid(7) and lvcreate(8) for more options.

Please mind how the examples below each specify the physical volumes. This can make sense in some situations to have LVM use a specific subset of devices for your new logical volume. But generally speaking, this is not necessary.

will create a 70 GiB striped (raid0) logical volume named "myraid1vol" in VolGroup00. Stripes will be spread over /dev/nvme1n1p1 and /dev/nvme0n1p1. Stripesize is set to be 64K.

will create a 20 GiB mirrored logical volume named "myraid1vol" in VolGroup00 on /dev/sda2 and /dev/sdb2.

RAID5 requires at least three drives (number of --stripes plus one parity device). Data and parity blocks are stored on each device, typically in a rotating pattern.

will create a 40 GiB striped logical volume named "myraid5vol" in VolGroup00 on /dev/sda2, /dev/sdb2 and /dev/sdc2. On each disk, the RAID5 will occupy about 20 GiB.

RAID6 requires at least five drives (number of --stripes plus two parity devices). As with RAID5, data and parity blocks are stored on each device, typically in a rotating pattern.

will create a 60 GiB striped logical volume named "myraid6vol" in VolGroup00 on /dev/sda2, /dev/sdb2, /dev/sdc2 and /dev/sdd2. On each disk, the RAID6 will occupy about 20 GiB.

will create a 100 GiB RAID10 logical volume named "myraid1vol" in VolGroup00 on /dev/sdd1, /dev/sdc1, /dev/sdb1, and /dev/sda5.

You can convert easily a non-RAID (e.g. linear) volume to pretty much any other raid configuration provided that you have enough physical devices to meet the RAID requirements. Some of them will require you to go through intermediate steps which lvconvert will inform you about and prompt you to agree. raid10 below can be replaced with raid0, raid1, raid5 etc.

You can keep track of the progress of conversion with:

Here is the classic use case. Suppose you want to start your own VPS service, initially hosting about 100 VPSes on a single PC with a 930 GiB hard drive. Hardly any of the VPSes will actually use all of the storage they are allotted, so rather than allocate 9 GiB to each VPS, you could allow each VPS a maximum of 30 GiB and use thin provisioning to only allocate as much hard drive space to each VPS as they are actually using. Suppose the 930 GiB hard drive is /dev/sdb. Here is the setup.

Prepare the volume group, MyVolGroup.

Create the thin pool LV, MyThinPool. This LV provides the blocks for storage.

The thin pool is composed of two sub-volumes, the data LV and the metadata LV. This command creates both automatically. But the thin pool stops working if either fills completely, and LVM currently does not support the shrinking of either of these volumes. This is why the above command allows for 5% of extra space, in case you ever need to expand the data or metadata sub-volumes of the thin pool.

For each VPS, create a thin LV. This is the block device exposed to the user for their root partition.

The block device /dev/MyVolGroup/SomeClientsRoot may then be used by a VirtualBox instance as the root partition.

Thin snapshots are much more powerful than regular snapshots, because they are themselves thin LVs. See Red Hat's guide [4] for a complete list of advantages thin snapshots have.

Instead of installing Linux from scratch every time a VPS is created, it is more space-efficient to start with just one thin LV containing a basic installation of Linux:

Then create snapshots of it for each VPS:

This way, in the thin pool there is only one copy the data common to all VPSes, at least initially. As an added bonus, the creation of a new VPS is instantaneous.

Since these are thin snapshots, a write operation to GenericRoot only causes one COW operation in total, instead of one COW operation per snapshot. This allows you to update GenericRoot more efficiently than if each VPS were a regular snapshot.

There are applications of thin provisioning outside of VPS hosting. Here is how you may use it to grow the effective capacity of an already-mounted file system without having to unmount it. Suppose, again, that the server has a single 930 GiB hard drive. The setup is the same as for VPS hosting, only there is only one thin LV and the LV's size is far larger than the thin pool's size.

This extra virtual space can be filled in with actual storage at a later time by extending the thin pool.

Suppose some time later, a storage upgrade is needed, and a new hard drive, /dev/sdc, is plugged into the server. To upgrade the thin pool's capacity, add the new hard drive to the VG:

Now, extend the thin pool:

Since this thin LV's size is 16 TiB, you could add another 15.09 TiB of hard drive space before finally having to unmount and resize the file system.

Some customisation is available by editing /etc/lvm/lvm.conf. You may find it useful to customize the output of lvs and pvs which by default does not include the % sync (useful to see progress of conversion between e.g. linear and raid type) and type of logical volume:

The dm_mod module should be automatically loaded. In case it does not, explicitly load the module at boot.

If you are trying to mount existing logical volumes, but they do not show up in lvscan, you can use the following commands to activate them:

Cause: removing an external LVM drive without deactivating the volume group(s) first. Before you disconnect, make sure to:

Fix: assuming you already tried to activate the volume group with vgchange -ay vg, and are receiving the Input/output errors:

Unplug the external drive and wait a few minutes:

The factual accuracy of this article or section is disputed.

In order for LVM to work properly with removable media – like an external USB drive – the volume group of the external drive needs to be deactivated before suspend. If this is not done, you may get buffer I/O errors on the dm device (after resume). For this reason, it is not recommended to mix external and internal drives in the same volume group.

To automatically deactivate the volume groups with external USB drives, tag each volume group with the sleep_umount tag in this way:

Once the tag is set, use the following unit file for systemd to properly deactivate the volumes before suspend. On resume, they will be automatically activated by LVM.

Finally, enable the unit.

If trying to extend a logical volume errors with:

The reason is that the logical volume was created with an explicit contiguous allocation policy (options -C y or --alloc contiguous) and no further adjacent contiguous extents are available.[5]

To fix this, prior to extending the logical volume, change its allocation policy with lvchange --alloc inherit logical_volume. If you need to keep the contiguous allocation policy, an alternative approach is to move the volume to a disk area with sufficient free extents. See [6].

Make sure to remove snapshot volumes before generating grub.cfg.

With a large number of snapshots, thin_check runs for a long enough time so that waiting for the root device times out. To compensate, add the rootdelay=60 kernel boot parameter to your boot loader configuration. Or, make thin_check skip checking block mappings (see [7]) and regenerate the initramfs:

If you use RAID, snapshots or thin provisioning and experience a delay on shutdown, make sure lvm2-monitor.service is started. See FS#50420.

See Power management/Suspend and hibernate#Hibernation into a thinly-provisioned LVM volume.

**Examples:**

Example 1 (unknown):
```unknown
Physical disks

  Disk1 (/dev/sda):
    ┌──────────────────────────────────────┬─────────────────────────────────────┐
    │ Partition1  50 GiB (Physical volume) │ Partition2 80 GiB (Physical volume) │
    │ /dev/sda1                            │ /dev/sda2                           │
    └──────────────────────────────────────┴─────────────────────────────────────┘

  Disk2 (/dev/sdb):
    ┌──────────────────────────────────────┐
    │ Partition1 120 GiB (Physical volume) │
    │ /dev/sdb1                            │
    └──────────────────────────────────────┘
```

Example 2 (unknown):
```unknown
LVM logical volumes

  Volume Group1 (/dev/MyVolGroup/ = /dev/sda1 + /dev/sda2 + /dev/sdb1):
    ┌─────────────────────────┬─────────────────────────┬──────────────────────────┐
    │ Logical volume1 15 GiB  │ Logical volume2 35 GiB  │ Logical volume3 200 GiB  │
    │ /dev/MyVolGroup/rootvol │ /dev/MyVolGroup/homevol │ /dev/MyVolGroup/mediavol │
    └─────────────────────────┴─────────────────────────┴──────────────────────────┘
```

Example 3 (unknown):
```unknown
/dev/VolumeGroupName/LogicalVolumeName
```

Example 4 (unknown):
```unknown
/dev/mapper/VolumeGroupName-LogicalVolumeName
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/GPT

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## Timeshift

**URL:** https://wiki.archlinux.org/title/Timeshift

**Contents:**
- Installation
- Configuration
- Usage
- Configuring btrfs snapshots
  - Making a supported Btrfs layout during installation
  - Converting an installed system to the compatible Btrfs layout
  - Excluding directories from Btrfs snapshots
  - GRUB entries for btrfs snapshots
- Troubleshooting
  - Timeshift GUI not launching on Wayland

Timeshift is a tool originally created by Tony George, that is now part of the Xapp project.

Timeshift helps create incremental snapshots of the file system at regular intervals, which can then be restored at a later date to undo all changes to the system.

It supports rsync snapshots for all filesystems, and uses the built-in snapshot features for Btrfs drives configured to use the @ and @home subvolume layout for root and home directories respectively.

Install the timeshift package and enable/start your chosen cron scheduler (see cron#Configuration). This will ensure that snapshots scheduled within the Timeshift application run as intended.

Alternatively, timeshift-systemd-timerAUR can be installed instead of using a cron scheduler.

Timeshift can be fully configured using the timeshift-gtk graphical user interface, but if running graphical applications is not an option, its configuration file can be edited directly. Copy the template file /etc/timeshift/default.json to /etc/timeshift/timeshift.json and edit settings you want to change.

Here is an example of a rsync-based configuration with three weekly snapshots and rules to exclude the /var/cache, /var/tmp and /home/archie directories, while including the /home/archie/.config directory and its content into the snapshots:

Snapshots can be managed through the timeshift-gtk graphical user interface, as well as the timeshift command-line user interface tool.

Restoring a snapshot:

Timeshift requires a flat Btrfs layout with subvolumes for / and optionally /home being named as /@ and /@home.

The instruction below assumes that you are following the installation guide.

Right after the Btrfs filesystem is created and mounted to /mnt, create subvolumes named /mnt/@ and /mnt/@home. Unmount /mnt and mount the subvolumes using the subvol parameter:

Proceed with the installation as normal.

The following instructions assume that the system is installed in the top-level (ID=5) subvolume, you may need to adapt these depending on your configuration.

Start by creating a snapshot of your root named /@ and mount it to /mnt:

Create the /@home subvolume, move the user data into it and mount it at /mnt/home:

Mount your EFI system partition to /mnt/esp if you have one. Chroot into /mnt, reinstall and reconfigure the boot loader. For an amd64 EFI system with GRUB, just running:

would be enough, however if you use any other bootloader that has no automatic configuration, you need to manually add rootflags=subvol=@ to the kernel options (see Kernel parameters#Boot loader configuration).

Edit the fstab file so that the entry for / contains subvol=@ mount option, and add an entry for /home with subvol=@home mount option. Example of how it may look like:

Exit the chroot, reboot and confirm with the mount command that everything is done correctly. Mount the toplevel using mount -o subvolid=5 /dev/root-partition /mnt and cleanup the old root.

Btrfs mode does not support the exclusion of individual files and directories from snapshots. However, it is possible to work around this to some extent by creating additional subvolumes at the top-level and mounting them in place of directories, which will effectively exclude them.

Here is an example of how to exclude the /var/log directory, to prevent the system logs from rolling back and make it easy to inspect them after a system breakage:

Start by mounting the top-level and create the subvolume inside of it:

Add a new entry for it to fstab:

To add snapshots to the GRUB menu each time GRUB configuration is generated, install the grub-btrfs package. It comes with the grub-btrfsd.service, which can be enabled to automatically update the GRUB configuration whenever a new snapshot is created.

To make grub-btrfsd work with Timeshift, edit the service by running:

After saving the changes, restart the service.

Xwayland will only allow the user who started the X server to connect clients to it (see Running GUI applications as root#Wayland).

Due to Timeshift requiring root permissions, attempting to launch the Timeshift GUI via an application launcher or a terminal with the command timeshift-launcher will result in an error containing xhost: command not found.

Users encountering this error may also be presented with their authentication agent prompting for a password, only to find that the Timeshift GUI does not launch after entering the password. [1][dead link 2025-03-15—HTTP 404] This is because the command timeshift-launcher requires the xorg-xhost package: install it.

If GTK cannot open your display and you get a warning message in the terminal, it means that the root user need the access to the graphical X server (Display :0, :1, etc.)

Normally only the user who started the graphical session can open new windows in your compositor and since your need to execute timeshift with the root user, you are not able to open the GUI

If the delete button silently fails in GUI and timeshift --delete --snapshot snapshot results in

this means the snapshot contains one or more nested subvolumes and those need to be removed manually. In order to do so, you need to mount the toplevel subvolume and see the subvolume list:

If you see any subvolumes located inside the snapshot, make sure they do not contain anything you would like to copy first and remove them by running:

And remove the snapshot using timeshift as normal. Alternatively, you can remove the whole snapshot and all the nested subvolumes by running rm -rf /mnt/timeshift-btrfs/snapshots/snapshot.

Typically, this issue occurs because systemd-nspawn creates /var/lib/machines and /var/lib/portables subvolumes automatically. You can avoid this by creating them as directories in advance [2]

**Examples:**

Example 1 (unknown):
```unknown
timeshift-gtk
```

Example 2 (unknown):
```unknown
/etc/timeshift/default.json
```

Example 3 (unknown):
```unknown
/etc/timeshift/timeshift.json
```

Example 4 (unknown):
```unknown
/home/archie
```

---

## Solid state drive

**URL:** https://wiki.archlinux.org/title/TRIM

**Contents:**
- Usage
  - TRIM
    - Periodic TRIM
    - Continuous TRIM
    - Trim an entire device
    - LVM
    - dm-crypt
    - swap
  - Maximizing performance
    - SSD memory cell clearing

This article covers special topics for operating solid state drives (SSDs) and other flash-memory based storage devices.

If you want to partition an SSD for a specific purpose, it may be useful to consider the List of file systems optimized for flash memory.

For general usage, simply choose your preferred file system and enable #TRIM.

Compared to hard drives, where deleting a file is only handled at the file system level[1], SSDs benefit from informing the disk controller when blocks of memory are free to be reused. Since the flash cells they are made of are worn out a little with each write operation, the disk controllers use algorithms to share the write operations on all the cells: this process is called wear leveling. Without the NVMe DEALLOCATE, SAS UNMAP or ATA_TRIM command (supported by most SSDs), the disk controller takes more time to do a write operation as soon as there is no empty memory blocks, as it has to shuffle data around to erase a cell before writing to it (see Wikipedia:Write amplification): a TechSpot benchmark shows the performance impact before and after filling an SSD with data.

As of Linux kernel version 3.8 onwards, support for TRIM was continually added for the different file systems. See the following table for an indicative overview:

To verify TRIM support, run:

And check the values of DISC-GRAN (discard granularity) and DISC-MAX (discard max bytes) columns. Non-zero values indicate TRIM support.

For SATA SSDs only, the hdparm package can detect TRIM support via hdparm -I /dev/sda | grep TRIM as the root user. hdparm does however not support NVMe SSDs.

The util-linux package provides fstrim.service and fstrim.timer systemd unit files. Enabling the timer will activate the service weekly. The service executes fstrim(8) on all mounted file systems on devices that support the discard operation.

The timer relies on the timestamp of /var/lib/systemd/timers/stamp-fstrim.timer (which it will create upon first invocation) to know whether a week has elapsed since it last ran. Therefore there is no need to worry about too frequent invocations, in an anacron-like fashion.

To query the units activity and status, see journalctl. To change the periodicity of the timer or the command run, edit the provided unit files.

Instead of issuing TRIM commands once in a while (by default once a week if using fstrim.timer), it is also possible to issue TRIM commands each time files are deleted instead. The latter is known as the continuous TRIM.

Using the discard option for a mount in /etc/fstab enables continuous TRIM in device operations. For example:

On the ext4 file system, the discard flag can also be set as a default mount option using tune2fs:

Using the default mount options instead of an entry in /etc/fstab is particularly useful for external drives, because such partition will be mounted with the default options also on other machines. This way, there is no need to edit /etc/fstab on every machine.

If you want to trim your entire SSD at once, e.g. for a new install or if you want to sell the drive, you can use the blkdiscard command.

TRIM requests that get passed from the file system to the logical volume are automatically passed to the physical volume(s). No additional configuration is necessary.

No LVM operations (lvremove, lvreduce and all others) issue TRIM requests to physical volume(s) by default. This is done to allow restoring previous volume group configuration with vgcfgrestore(8). The setting issue_discards in /etc/lvm/lvm.conf controls whether discards are sent to a logical volume's underlying physical volumes when the logical volume is no longer using the physical volumes' space.

Follow the instructions in dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD) to enable discard support for LUKS and plain dm-crypt devices.

To enable discard for swap space, either add the discard option to a swap device's entry in fstab or pass --discard when calling swapon.

Discard is not automatically enabled for swap partitions when using GPT partition automounting.

See swapon(8) for discussion on when swap is discarded: discard=once or discard=pages. If discard is specified without a specific mode, the default is to enable both.

Follow the tips in Improving performance#Storage devices to maximize the performance of your drives.

On occasion, users may wish to completely reset an SSD's cells to the same virgin state they were at the time the device was installed, thus restoring it to its factory default write performance. Write performance is known to degrade over time even on SSDs with native TRIM support: TRIM only safeguards against file deletes, not replacements such as an incremental save.

The reset can be accomplished by following the appropriate procedure denoted in Solid state drive/Memory cell clearing, either for SATA or NVMe SSDs.

Some motherboard firmware issue a ATA SECURITY FREEZE LOCK command to SATA devices on initialization, setting the drive to frozen mode which transitions it to SEC2 state (security disabled, not locked, frozen). Likewise some SSD (and HDD) are set to this state in the factory already. This can be seen in hdparm and smartctl output:

Operations like formatting the device or installing operating systems are not affected by the frozen mode.

The above hdparm output shows the device is not locked by an HDD-password on boot and the frozen state safeguards the device against malwares which may try to lock it by setting a password to it at runtime.

If you intend to set a password to a "frozen" device yourself, a motherboard BIOS with support for it is required. A lot of notebooks have support, because it is required for hardware encryption, but support may not be trivial for a desktop/server board. For the Intel DH67CL/BL motherboard, for example, the motherboard has to be set to "maintenance mode" by a physical jumper to access the settings.[10]

If you intend to erase the SSD, see Securely wipe disk#hdparm and /Memory cell clearing.

When waking up from S3 sleep, the SATA SSD will most likely have reverted to SEC1 state (security disabled, not locked, not frozen), leaving it vulnerable to ATA SECURITY ERASE UNIT commands like those described in /Memory cell clearing.

In order to prevent this issue, a script can be run after waking up from sleep:

If the system has multiple storage devices and/or portable USB-drives, another option is to adapt Hdparm#Persistent configuration using udev rule to issue a --security-freeze for all drives (incl. HDD).

As noted in #Frozen mode, setting a password for a storage device (SSD/HDD) in the BIOS may also initialize the hardware encryption of devices supporting it. If the device also conforms to the OPAL standard, this may also be achieved without a respective BIOS feature to set the passphrase. See Self-encrypting drives.

It is possible that the issue you are encountering is a firmware bug which is not Linux specific, so before trying to troubleshoot an issue affecting the SSD device, you should first check if updates are available for:

Even if it is a firmware bug it might be possible to avoid it, so if there are no updates to the firmware or you hesitant on updating firmware then the following might help.

Some SSDs and SATA chipsets do not work properly with Linux Native Command Queueing (NCQ). The tell-tale errors in the journal look like:

To disable NCQ on boot, add libata.force=noncq to the kernel command line in the boot loader configuration. To disable NCQ only for disk 0 on port 9 use: libata.force=9.00:noncq

Alternatively, you may disable NCQ for a specific drive without rebooting via sysfs:

If this (and also updating the firmware) does not resolve the problem or causes other issues, then file a bug report.

Some SSDs (e.g. Transcend MTS400 or Crucial M550 SSDs) are failing with certain SATA controllers when SATA Active Link Power Management (ALPM), is enabled.

ALPM is enabled by default since linux-4.16, or may be enabled at runtime by a power saving daemon (e.g. TLP, Laptop Mode Tools). See Power management#SATA Active Link Power Management for more on this.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Several USB-to-SATA bridge chips (like VL715, VL716 etc.) and also USB-to-PCIe bridge chips (like the JMicron JMS583 used in external NVMe enclosures like IB-1817M-C31) support TRIM-like commands that can be sent through the USB Attached SCSI driver (named "uas" under Linux).

But the kernel may not automatically detect this capability, and therefore might not use it. Assuming your block device in question is /dev/sdX, you can find out whether that is the case by using the command from sg3_utils:

If in its output you find a line stating Logical block provisioning: lbpme=0 then you know that the kernel assumes the device does not support "Logical Block Provisioning Management" because the (LBPME) bit is not set.

If this is the case, then you should next find out whether the "Vital Product Data" (VPD) page on "Logical Block Provisioning" of your device tells of supported mechanisms for unmapping data. You can do this using the command:

Look for lines in the output that look like this:

This example would tell you the device supports the "UNMAP" command.

Have a look at the output of

If the kernel did not detect the capability of your device to unmap data, then this will likely return "full". Apart from "full", the kernel SCSI storage driver currently knows the following values for provisioning_mode:

For the example above, you could now write "unmap" to "provisioning_mode" to ask the kernel to use that:

This should immediately enable you to use tools like blkdiscard on /dev/sdX or fstrim on file systems mounted on /dev/sdX.

If you want to enable a "provisioning_mode" automatically when an external device of a certain vendor/product is attached, this can be automated via the "udev" mechanism. First find the USB Vendor and Product IDs:

Then create or append to a udev rule file (example here using idVendor 152d and idProduct 0583):

(You can also use the lsusb command to look for the relevant idVendor/idProduct.)

If supported by the device vendor, it is recommended to update firmware using the fwupd utility.

To check your current firmware version:

Updating SSD firmware under Linux is not supported by ADATA. A Windows-only utility called SSD ToolBox is provided by ADATA through their support page and through their ADATA XPG support page to monitor, TRIM, benchmark and update ADATA SSD firmware.

Crucial provides an option for updating the firmware with an ISO image. These images can be found after selecting the product on their SSD support page and downloading the "Manual Boot File."

Owners of an M4 Crucial model, may check if a firmware upgrade is needed with smartctl.

Users seeing this warning are advised to backup all sensible data and consider upgrading immediately. Check this instructions to update Crucial MX100 firmware by using the ISO image and Grub.

Besides the bootable ISO, micron-storage-executive-cliAUR is a command-line tool for flashing firmwares and also offers additional SSD information.

Intel has a Linux live system based Firmware Update Tool for operating systems that are not compatible with its Windows Intel® Memory and Storage Tool (GUI) software.

There is also a newer Linux command-line utility that can reflash firmware called the Intel Memory and Storage (MAS) Tool available as intel-mas-cli-toolAUR. There is a PDF user guide available.

An example for checking the firmware status is:

-intelssd 0 can be omitted if there is only one Intel SSD in the system, or 1 passed for the second SSD, and so on.

If an update is available, it is performed by running intelmas load -intelssd 0. The PDF user guide suggests that this procedure needs to be performed twice in Linux, with a power cycle in between. The latest firmware for all devices is distributed as part of the MAS Tool itself, so does not need to be downloaded separately.

KFU tool is available for the Sandforce based drives, kingston_fw_updaterAUR.

The lesser known Mushkin brand solid state drives also use Sandforce controllers, and have a Linux utility (nearly identical to Kingston's) to update the firmware.

OCZ has a Command Line Online Update Tool (CLOUT) available for Linux. The existing packages are ocz-ssd-utilityAUR, ocztoolboxAUR and oczcloutAUR.

Although Samsung deems firmware update methods outside of their Magician software as "unsupported", they still can work. The Magician software can create a bootable USB drive containing the firmware update, however Samsung no longer provides the software for consumer SSDs. Samsung also provides pre-made bootable ISO images that can be used to update the firmware. Another option is to use Samsung's magician utility provided by samsung_magician-consumer-ssdAUR. Magician only supports Samsung-branded SSDs; those manufactured by Samsung for OEMs (e.g., Lenovo) are not supported.

Users preferring to run the firmware update from a live USB created under Linux (without using Samsung's Magician software under Microsoft Windows) can refer to [11] for more details. Note that this blog post details creating a bootable USB drive with Master Boot Record (MBR) that some newer motherboards, e.g. Intel NUC no longer support.

The SSD firmware can be updated natively (without making a bootable USB stick) as shown below. First visit the Samsung downloads page, go to the "Samsung SSD Firmware" section, and download the latest firmware for your SSD—it should be an ISO image.

Extract the initrd Linux image from the ISO image:

Extract root/fumagician/. This directory contains the firmware update files:

Finally, run root/fumagician/fumagician with root privileges and reboot your system (if the firmware was successfully updated).

If after reboot the firmware version does not change, run root/fumagician/fumagician 2> log and search for errors in the log file. For example, if the log shows 'unzip is not available', install unzip or extract it from the initrd.

Some of the SSD firmware ISO images contain a FreeDOS image instead of an initrd Linux image, so the steps needed to update the SSD firmware differ from above. The following table lists these SSDs (and relevant paths):

First, extract the FreeDOS image from the ISO image:

Mount the FreeDOS image to /mnt/:

Get the disk number of the SSD under Disk Number from the Magician SSD management utility:

Update the SSD firmware for the specified disk by providing the firmware package path:

Finally, verify whether the firmware was successfully updated by checking the version under Firmware from the output of magician --list (with root privileges). Reboot your system if so.

SanDisk makes ISO firmware images to allow SSD firmware update on operating systems that are unsupported by their SanDisk SSD Toolkit.

One must choose the firmware for the correct SSD model, and the correct capacity that it has (e.g. 60GB, or 256GB). After burning the ISO firmware image, simply restart the PC to boot with the newly created CD/DVD boot disk (may work from a USB stick).

The iso images just contain a linux kernel and an initrd. Extract them to /boot partition and boot them with GRUB or Syslinux to update the firmware.

**Examples:**

Example 1 (unknown):
```unknown
$ lsblk --discard
```

Example 2 (unknown):
```unknown
hdparm -I /dev/sda | grep TRIM
```

Example 3 (unknown):
```unknown
fstrim.service
```

Example 4 (unknown):
```unknown
fstrim.timer
```

---

## GPT fdisk

**URL:** https://wiki.archlinux.org/title/Gdisk

**Contents:**
- Installation
- List partitions
- Backup and restore partition table
- Create a partition table and partitions
  - Create new table
  - Create partitions
    - Partition number
    - First and last sector
    - Partition type
  - Write changes to disk

GPT fdisk—consisting of the gdisk, cgdisk, sgdisk, and fixparts programs—is a set of text-mode partitioning tools made by Rod Smith. They work on Globally Unique Identifier (GUID) Partition Table (GPT) disks, rather than on the older (and once more common) Master Boot Record (MBR) partition tables.

gdisk, cgdisk and sgdisk all have the same functionality but provide different user interfaces. gdisk is text-mode interactive, sgdisk is command-line, and cgdisk has a curses-based interface. This article covers gdisk(8) and sgdisk(8) utilities.

Install the gptfdisk package.

To list partition tables and partitions on a block device, you can run the following, where device is a name like /dev/sda, /dev/nvme0n1, /dev/mmcblk0, etc.:

or alternatively the same action using sgdisk:

Before making changes to a disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

Using sgdisk you can create a binary backup consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table. The example below will save the partition table of /dev/sda to a file sgdisk-sda.bin:

You can later restore the backup by running:

If you want to clone your current device's partition layout (/dev/sda in this case) to another drive (/dev/sdc) run:

If both drives will be in the same computer, you need to randomize the disk and partition GUIDs:

The first step to partitioning a disk is making a partition table. After that, the actual partitions are created according to the desired partition scheme.

Before beginning, you may wish to backup your current partition table and scheme.

The following shows how to use gdisk to perform both the creation of a partition table and the creation of the actual partitions. Alternatively, you may use the curses-based version called cgdisk; however, the following instructions do not apply to it. See cgdisk(8) for its usage.

gdisk performs partition alignment automatically on a 2048 512-byte sector (1 MiB) block size base which should be compatible with all Advanced Format HDDs and the vast majority of SSDs if not all.

To use gdisk, run the program with the name of the block device you want to change/edit. This example uses /dev/sda:

To create a new GUID Partition Table and clear all current partition data, type o at the prompt. Skip this step if the table you require has already been created.

Create a new partition with the n command. You must enter the partition number, first sector, last sector and the partition type.

A partition number is the number assigned to a partition, e.g. a partition with number 1 on a disk /dev/sda would be /dev/sda1, /dev/nvme0n1p1 on /dev/nvme0n1 and /dev/mmcblk0p1 on /dev/mmcblk0. See Device file#Partition for details on the naming scheme. Partition numbers may not always match the order of partitions on disk, in which case they can be sorted.

It is advised to choose the default number suggested by gdisk.

The first and last sectors of the partition can be specified in sector numbers or as positions measured in kibibytes (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P);

The position can be specified in:

Pressing the Enter key with no input specifies the default value, which is the start of the largest available block for the first sector and the end of the same block for the last sector.

Select the partition's type by entering gdisk's internal type code or specifying the partition type GUID manually. The default, Linux filesystem (GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4, gdisk's internal code 8300), should be fine for most use cases.

Repeat this procedure until you have the partitions you desire.

Write the table to disk and exit via the w command.

gdisk, sgdisk and cgdisk have the ability to convert MBR and BSD disklabels to GPT without data loss. Upon conversion, all the MBR primary partitions and the logical partitions become GPT partitions with the correct partition type GUIDs and Unique partition GUIDs created for each partition.

After conversion, the boot loader will need to be reinstalled to configure it to boot from GPT.

This article or section needs expansion.

To convert an MBR partition table to GPT using sgdisk, use the -g/--mbrtogpt option:

To convert GPT to MBR use the -m/--gpttombr option. Note that it is not possible to convert more than four partitions from GPT to MBR.

This applies for when a new partition is created in the space between two partitions or a partition is deleted. /dev/sda is used in this example.

After sorting the partitions if you are not using Persistent block device naming, it might be required to adjust the /etc/fstab and/or the /etc/crypttab configuration files.

In case main GPT header or backup GPT header gets damaged, you can recover one from the other with gdisk. /dev/sda is used in this example.

choose r for recovery and transformation options (experts only). From there choose either

When done write the table to disk and exit via the w command.

After enlarging a disk (e.g. in hardware RAID or a virtual machine disk) the newly added free space will not be immediately usable since GPT keeps data at the end of the disk. You must relocate the backup GPT header to the new end of the disk.

Run sgdisk with the option -e/--move-second-header, e.g.:

Afterwards print the partition table; the total free space should now be increased.

systemd-gpt-auto-generator(8) will automount partitions following the Discoverable Partitions Specification. Sometimes that may not be desirable.

The automounting can be disabled by setting the partition attribute 63 "do not automount" on the partition.

Press p to print the partition table and take note of the partition number(s) of the for which you want to disable automounting.

Press x extra functionality (experts only).

Press a set attributes. Input the partition number and set the attribute 63. Under Set fields are: it should now show 63 (do not automount). Press Enter to end attribute changing. Repeat this for all partitions you want to prevent from automounting.

When done write the table to disk and exit via the w command.

Alternatively using sgdisk, the attribute can be set using the -A/--attributes= option; see sgdisk(8) for usage. For example, to set partition attribute 63 "do not automount" on /dev/sda2 run:

This article or section is out of date.

There is no package for the EFI version of gdisk, but Rod Smith provides a prebuilt gdisk-1.04 EFI binary on SourceForge. Download gdisk-efi-*.zip and extract the archive. To use it, copy gdisk_x64.efi to the EFI system partition and launch it from your boot loader or UEFI Shell.

gdisk_x64.efi allows you to edit the partition table before the operating system is even booted. It is used the same way as the gdisk binary on Linux.

See README-efi.txt for more information.

**Examples:**

Example 1 (unknown):
```unknown
/dev/nvme0n1
```

Example 2 (unknown):
```unknown
/dev/mmcblk0
```

Example 3 (unknown):
```unknown
# gdisk -l /dev/sda
```

Example 4 (unknown):
```unknown
# sgdisk -p /dev/sda
```

---

## RAID

**URL:** https://wiki.archlinux.org/title/Mdadm

**Contents:**
- RAID levels
  - Standard RAID levels
  - Nested RAID levels
  - RAID level comparison
  - LINEAR
- Implementation
  - Which type of RAID do I have?
- Installation
  - Prepare the devices
  - Partition the devices

Redundant Array of Independent Disks (RAID) is a storage technology that combines multiple disk drive components—typically disk drives or partitions thereof—into a logical unit. Depending on the RAID implementation, this logical unit can be a file system or an additional transparent layer that can hold several partitions.

Data is distributed across the drives in one of several ways called #RAID levels, depending on the level of redundancy and performance required. The RAID level chosen can thus prevent data loss in the event of a hard disk failure, increase performance or be a combination of both.

This article explains how to create and manage a software RAID array using mdadm(8).

Despite redundancy implied by most RAID levels, RAID does not guarantee that data is safe. A RAID will not protect data if there is a fire, the computer is stolen or multiple hard drives fail at once. Furthermore, installing a system with RAID is a complex process that may destroy data.

There are many different levels of RAID; listed below are the most common.

Best; on par with RAID0 but redundant

* Where n is standing for the number of dedicated disks.

LINEAR allows to map two or more devices into a single device, without parallel accesses like RAID0 but allowing to fully use disks from different sizes. To create a pseudo RAID using this mode without mdadm, one can either use the low-level dmsetup(8) utility, the high-level LVM framework or the Btrfs filesystem.

The RAID devices can be managed in different ways:

Since software RAID is implemented by the user, the type of RAID is easily known to the user.

However, discerning between FakeRAID and true hardware RAID can be more difficult. As stated, manufacturers often incorrectly distinguish these two types of RAID and false advertising is always possible. The best solution in this instance is to run the lspci command and looking through the output to find the RAID controller. Then do a search to see what information can be located about the RAID controller. Hardware RAID controllers appear in this list, but FakeRAID implementations do not. Also, true hardware RAID controllers are often rather expensive, so if someone customized the system, then it is very likely that choosing a hardware RAID setup made a very noticeable change in the computer's price.

Install mdadm. mdadm is used for administering pure software RAID using plain block devices: the underlying hardware does not provide any RAID logic, just a supply of disks. mdadm will work with any collection of block devices. Even if unusual. For example, one can thus make a RAID array from a collection of thumb drives.

If the device is being reused or re-purposed from an existing array, erase any old RAID configuration information:

or if a particular partition on a drive is to be deleted:

It is highly recommended to partition the disks to be used in the array. Since most RAID users are selecting disk drives larger than 2 TiB, GPT is required and recommended. See Partitioning for more information on partitioning and the available partitioning tools.

For those creating partitions on HDDs with a MBR partition table, the partition types IDs available for use are:

See Linux Raid Wiki:Partition Types for more information.

Use mdadm to build the array. See mdadm(8) for supported options. Several examples are given below.

The following example shows building a 2-device RAID1 array:

The following example shows building a RAID5 array with 4 active devices and 1 spare device:

The following example shows building a RAID10,far2 array with 2 devices:

The array is created under the virtual device /dev/mdX, assembled and ready to use (in degraded mode). One can directly start using it while mdadm resyncs the array in the background. It can take a long time to restore parity. Check the progress with:

By default, most of mdadm.conf is commented out, and it contains just the following:

This directive tells mdadm to examine the devices referenced by /proc/partitions and assemble as many arrays as possible. This is fine if you really do want to start all available arrays and are confident that no unexpected superblocks will be found (such as after installing a new storage device). A more precise approach is to explicitly add the arrays to /etc/mdadm.conf:

This results in something like the following:

This also causes mdadm to examine the devices referenced by /proc/partitions. However, only devices that have superblocks with a UUID of 27664… are assembled in to active arrays.

See mdadm.conf(5) for more information.

Once the configuration file has been updated the array can be assembled using mdadm:

The array can now be formatted with a file system like any other partition, just keep in mind that:

Two parameters are required to optimise the filesystem structure to fit optimally within the underlying RAID structure: the stride and stripe width. These are derived from the RAID chunk size, the filesystem block size, and the number of "data disks".

The chunk size is a property of the RAID array, decided at the time of its creation. mdadm's current default is 512 KiB. It can be found with mdadm:

The block size is a property of the filesystem, decided at its creation. The default for many filesystems, including ext4, is 4 KiB. See /etc/mke2fs.conf for details on ext4.

The number of "data disks" is the minimum number of devices in the array required to completely rebuild it without data loss. For example, this is N for a raid0 array of N devices and N-1 for raid5.

Once you have these three quantities, the stride and the stripe width can be calculated using the following formulas:

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 2*128 so the stripe width = 256.

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 3*128 so the stripe width = 384.

For more on stride and stripe width, see: RAID Math.

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 2*128 so the stripe width = 256.

Users wanting to mount the RAID partition from a Live CD, use:

If your RAID 1 that is missing a disk array was wrongly auto-detected as RAID 1 (as per mdadm --detail /dev/mdnumber) and reported as inactive (as per cat /proc/mdstat), stop the array first:

You should create the RAID array between the Partitioning and formatting steps of the Installation Procedure. Instead of directly formatting a partition to be your root file system, it will be created on a RAID array. Follow the section #Installation to create the RAID array. Then continue with the installation procedure until the pacstrap step is completed. When using UEFI boot, also read EFI system partition#ESP on software RAID1.

After the base system is installed the default configuration file, mdadm.conf, must be updated like so:

Always check the mdadm.conf configuration file using a text editor after running this command to ensure that its contents look reasonable.

Continue with the installation procedure until you reach the step Installation guide#Initramfs, then follow the next section.

Install mdadm and add mdadm_udev to the HOOKS array of the mkinitcpio.conf to add support for mdadm into the initramfs image:

Then regenerate the initramfs.

Point the root parameter to the mapped device. E.g.:

If booting from a software raid partition fails using the kernel device node method above, an alternative way is to use one of the methods from Persistent block device naming, for example:

Since version 5.3.4 of the Linux kernel, you need to explicitly tell the kernel which RAID0 layout should be used: RAID0_ORIG_LAYOUT (1) or RAID0_ALT_MULTIZONE_LAYOUT (2).[1] You can do this by providing the kernel parameter as follows:

The correct value depends upon the kernel version that was used to create the raid array: use 1 if created using kernel 3.14 or earlier, use 2 if using a more recent version of the kernel. One way to check this is to look at the creation time of the raid array:

Here we can see that this raid array was created on September 24, 2015. The release date of Linux Kernel 3.14 was March 30, 2014, and as such this raid array is most likely created using a multizone layout (2).

It is good practice to regularly run data scrubbing to check for and fix errors. Depending on the size/configuration of the array, a scrub may take multiple hours to complete.

To initiate a data scrub:

The check operation scans the drives for bad sectors and automatically repairs them. If it finds good sectors that contain bad data (i.e. a mismatch, the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below). This "do nothing" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

As with many tasks/items relating to mdadm, the status of the scrub can be queried by reading /proc/mdstat.

To stop a currently running data scrub safely:

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

It is a good idea to set up a cron job as root to schedule a periodic scrub. See raid-checkAUR which can assist with this. To perform a periodic scrub using systemd timers instead of cron, See raid-check-systemdAUR which contains the same script along with associated systemd timer unit files.

Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy. These non-0 counts will only exist in transient data areas where they do not pose a problem. However, we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem. This fact is a source of false positives for RAID1 and RAID10 arrays. It is however still recommended to scrub regularly in order to catch and correct any bad sectors that might be present in the devices.

One can remove a block device from the array after marking it as faulty:

Now remove it from the array:

If the device has not failed entirely, but you would like to replace it, e.g. because it looks like it is dying, you can actually handle replacement more gracefully by first adding a new drive and then telling mdadm to replace it.

For example, with /dev/sdc1 as the new one and /dev/sdb1 as the failing one:

The --with /dev/sdc1 part is optional, but more explicit. See [2] for more details.

To remove a device permanently (for example, to use it individually from now on), follow the steps above (fail/remove or add/replace) and then run:

Adding new devices with mdadm can be done on a running system with the devices mounted. Partition the new device using the same layout as one of those already in the arrays as discussed above.

Assemble the RAID array if it is not already assembled:

Add the new device to the array:

This should not take long for mdadm to do.

This article or section needs expansion.

Depending on the type of RAID (for example, with RAID1), mdadm may add the device as a spare without syncing data to it. You can increase the number of disks the RAID uses by using --grow with the --raid-devices option. For example, to increase an array to four disks:

You can check the progress with:

Check that the device has been added with the command:

This is because the above commands will add the new disk as a "spare" but RAID0 does not have spares. If you want to add a device to a RAID0 array, you need to "grow" and "add" in the same command, as demonstrated below:

If larger disks are installed in a RAID array or partition size has been increased, it may be desirable to increase the size of the RAID volume to fill the larger available space. This process may be begun by first following the above sections pertaining to replacing disks. Once the RAID volume has been rebuilt onto the larger disks it must be "grown" to fill the space.

Next, partitions present on the RAID volume /dev/md0 may need to be resized. See Partitioning for details. Finally, the filesystem on the above mentioned partition will need to be resized. If partitioning was performed with gparted this will be done automatically. If other tools were used, unmount and then resize the filesystem manually.

Syncing can take a while. If the machine is not needed for other tasks the speed limit can be increased.

In the above example, it would seem the max speed is limited to approximately 238 M/sec.

Check the current speed limit (in kibibytes per second, KiB/s):

Set a new maximum speed of raid resyncing operations using sysctl:

Then check out the syncing speed and estimated finish time.

To improve RAID5 performance for fast storage (e.g. NVMe), increase /sys/block/mdx/md/group_thread_cnt to more threads. For example, to use 8 threads to operate on a RAID5 device:

See git kernel commit 851c30c9badf.

To update the RAID superblock, you need to first unmount the array and then stop the array with the following command:

Then you can update certain parameters by reassembling the array. For example, to update the homehost:

See the arguments of --update for details.

A simple one-liner that prints out the status of the RAID devices:

Or preferably using tmux:

The iotop package displays the input/output stats for processes. Use this command to view the IO for raid threads.

The iostat utility from sysstat package displays the input/output statistics for devices and partitions.

mdadm provides the systemd service mdmonitor.service which can be useful for monitoring the health of your raid arrays and notifying you if anything goes wrong.

This service is special in that it cannot be manually activated like a regular service; mdadm will take care of activating it via udev upon assembling your arrays on system startup, but it will only do so if an email address and/or program has been configured for its notifications (see below).

To enable this functionality, edit /etc/mdadm.conf and define the email address:

Then, to verify that everything is working as it should, run the following command:

If the test is successful and the email is delivered, then you are done; the next time your arrays are reassembled, mdmonitor.service will begin monitoring them for errors.

Like Email notification above, edit /etc/mdadm.conf and edit the line:

The argument for PROGRAM is the script you want to run for any event. Which then interact with proper network monitoring agents. Or even IM clients or push notification services like ntfy.sh for home users.

Test in the same way as for email notification above.

If you are getting error when you reboot about "invalid raid superblock magic" and you have additional hard drives other than the ones you installed to, check that your hard drive order is correct. During installation, your RAID devices may be hdd, hde and hdf, but during boot they may be hda, hdb and hdc. Adjust your kernel line accordingly. This is what happened to me anyway.

If you suddenly (after reboot, changed BIOS settings) experience Error messages like:

It does not necessarily mean that a drive is broken. You often find panic links on the web which go for the worst. In a word, No Panic. Maybe you just changed APIC or ACPI settings within your BIOS or Kernel parameters somehow. Change them back and you should be fine. Ordinarily, turning ACPI and/or ACPI off should help.

When an md array is started, the superblock will be written, and resync may begin. To start read-only set the kernel module md_mod parameter start_ro. When this is set, new arrays get an 'auto-ro' mode, which disables all internal io (superblock updates, resync, recovery) and is automatically switched to 'rw' when the first write request arrives.

To set the parameter at boot, add md_mod.start_ro=1 to your kernel line.

Or set it at module load time by Kernel module#Using modprobe.d or from directly from /sys/:

You might get the above mentioned error also when one of the drives breaks for whatever reason. In that case you will have to force the raid to still turn on even with one disk short. Type this (change where needed):

Now you should be able to mount it again with something like this (if you had it in fstab):

Now the raid should be working again and available to use, however with one disk short. So, to add that one disc partition it the way like described above in #Prepare the devices. Once that is done you can add the new disk to the raid by doing:

you probably see that the raid is now active and rebuilding.

You also might want to update your configuration (see: #Update configuration file).

There are several tools for benchmarking a RAID. The most notable improvement is the speed increase when multiple threads are reading from the same RAID volume.

bonnie++ tests database type access to one or more files, and creation, reading, and deleting of small files which can simulate the usage of programs such as Squid, INN, or Maildir format e-mail. The enclosed ZCAV program tests the performance of different zones of a hard drive without writing any data to the disk.

hdparm should not be used to benchmark a RAID, because it provides very inconsistent results.

**Examples:**

Example 1 (unknown):
```unknown
mdadm --grow
```

Example 2 (unknown):
```unknown
# mdadm --misc --zero-superblock /dev/drive
```

Example 3 (unknown):
```unknown
# mdadm --misc --zero-superblock /dev/partition
```

Example 4 (unknown):
```unknown
A19D880F-05FC-4D3B-A006-743F0F84911E
```

---

## GPT fdisk

**URL:** https://wiki.archlinux.org/title/Sgdisk

**Contents:**
- Installation
- List partitions
- Backup and restore partition table
- Create a partition table and partitions
  - Create new table
  - Create partitions
    - Partition number
    - First and last sector
    - Partition type
  - Write changes to disk

GPT fdisk—consisting of the gdisk, cgdisk, sgdisk, and fixparts programs—is a set of text-mode partitioning tools made by Rod Smith. They work on Globally Unique Identifier (GUID) Partition Table (GPT) disks, rather than on the older (and once more common) Master Boot Record (MBR) partition tables.

gdisk, cgdisk and sgdisk all have the same functionality but provide different user interfaces. gdisk is text-mode interactive, sgdisk is command-line, and cgdisk has a curses-based interface. This article covers gdisk(8) and sgdisk(8) utilities.

Install the gptfdisk package.

To list partition tables and partitions on a block device, you can run the following, where device is a name like /dev/sda, /dev/nvme0n1, /dev/mmcblk0, etc.:

or alternatively the same action using sgdisk:

Before making changes to a disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

Using sgdisk you can create a binary backup consisting of the protective MBR, the main GPT header, the backup GPT header, and one copy of the partition table. The example below will save the partition table of /dev/sda to a file sgdisk-sda.bin:

You can later restore the backup by running:

If you want to clone your current device's partition layout (/dev/sda in this case) to another drive (/dev/sdc) run:

If both drives will be in the same computer, you need to randomize the disk and partition GUIDs:

The first step to partitioning a disk is making a partition table. After that, the actual partitions are created according to the desired partition scheme.

Before beginning, you may wish to backup your current partition table and scheme.

The following shows how to use gdisk to perform both the creation of a partition table and the creation of the actual partitions. Alternatively, you may use the curses-based version called cgdisk; however, the following instructions do not apply to it. See cgdisk(8) for its usage.

gdisk performs partition alignment automatically on a 2048 512-byte sector (1 MiB) block size base which should be compatible with all Advanced Format HDDs and the vast majority of SSDs if not all.

To use gdisk, run the program with the name of the block device you want to change/edit. This example uses /dev/sda:

To create a new GUID Partition Table and clear all current partition data, type o at the prompt. Skip this step if the table you require has already been created.

Create a new partition with the n command. You must enter the partition number, first sector, last sector and the partition type.

A partition number is the number assigned to a partition, e.g. a partition with number 1 on a disk /dev/sda would be /dev/sda1, /dev/nvme0n1p1 on /dev/nvme0n1 and /dev/mmcblk0p1 on /dev/mmcblk0. See Device file#Partition for details on the naming scheme. Partition numbers may not always match the order of partitions on disk, in which case they can be sorted.

It is advised to choose the default number suggested by gdisk.

The first and last sectors of the partition can be specified in sector numbers or as positions measured in kibibytes (K), mebibytes (M), gibibytes (G), tebibytes (T), or pebibytes (P);

The position can be specified in:

Pressing the Enter key with no input specifies the default value, which is the start of the largest available block for the first sector and the end of the same block for the last sector.

Select the partition's type by entering gdisk's internal type code or specifying the partition type GUID manually. The default, Linux filesystem (GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4, gdisk's internal code 8300), should be fine for most use cases.

Repeat this procedure until you have the partitions you desire.

Write the table to disk and exit via the w command.

gdisk, sgdisk and cgdisk have the ability to convert MBR and BSD disklabels to GPT without data loss. Upon conversion, all the MBR primary partitions and the logical partitions become GPT partitions with the correct partition type GUIDs and Unique partition GUIDs created for each partition.

After conversion, the boot loader will need to be reinstalled to configure it to boot from GPT.

This article or section needs expansion.

To convert an MBR partition table to GPT using sgdisk, use the -g/--mbrtogpt option:

To convert GPT to MBR use the -m/--gpttombr option. Note that it is not possible to convert more than four partitions from GPT to MBR.

This applies for when a new partition is created in the space between two partitions or a partition is deleted. /dev/sda is used in this example.

After sorting the partitions if you are not using Persistent block device naming, it might be required to adjust the /etc/fstab and/or the /etc/crypttab configuration files.

In case main GPT header or backup GPT header gets damaged, you can recover one from the other with gdisk. /dev/sda is used in this example.

choose r for recovery and transformation options (experts only). From there choose either

When done write the table to disk and exit via the w command.

After enlarging a disk (e.g. in hardware RAID or a virtual machine disk) the newly added free space will not be immediately usable since GPT keeps data at the end of the disk. You must relocate the backup GPT header to the new end of the disk.

Run sgdisk with the option -e/--move-second-header, e.g.:

Afterwards print the partition table; the total free space should now be increased.

systemd-gpt-auto-generator(8) will automount partitions following the Discoverable Partitions Specification. Sometimes that may not be desirable.

The automounting can be disabled by setting the partition attribute 63 "do not automount" on the partition.

Press p to print the partition table and take note of the partition number(s) of the for which you want to disable automounting.

Press x extra functionality (experts only).

Press a set attributes. Input the partition number and set the attribute 63. Under Set fields are: it should now show 63 (do not automount). Press Enter to end attribute changing. Repeat this for all partitions you want to prevent from automounting.

When done write the table to disk and exit via the w command.

Alternatively using sgdisk, the attribute can be set using the -A/--attributes= option; see sgdisk(8) for usage. For example, to set partition attribute 63 "do not automount" on /dev/sda2 run:

This article or section is out of date.

There is no package for the EFI version of gdisk, but Rod Smith provides a prebuilt gdisk-1.04 EFI binary on SourceForge. Download gdisk-efi-*.zip and extract the archive. To use it, copy gdisk_x64.efi to the EFI system partition and launch it from your boot loader or UEFI Shell.

gdisk_x64.efi allows you to edit the partition table before the operating system is even booted. It is used the same way as the gdisk binary on Linux.

See README-efi.txt for more information.

**Examples:**

Example 1 (unknown):
```unknown
/dev/nvme0n1
```

Example 2 (unknown):
```unknown
/dev/mmcblk0
```

Example 3 (unknown):
```unknown
# gdisk -l /dev/sda
```

Example 4 (unknown):
```unknown
# sgdisk -p /dev/sda
```

---

## Partitioning

**URL:** https://wiki.archlinux.org/title/Partition_table

**Contents:**
- Partition table
  - Master Boot Record
    - Master Boot Record (bootstrap code)
    - Master Boot Record (partition table)
  - GUID Partition Table
  - Choosing between GPT and MBR
  - Partitionless disk
    - Btrfs partitioning
- Partition scheme
  - Single root partition

An entire disk may be allocated to a single partition, or multiple ones for cases such as dual-booting, maintaining a swap partition, or to logically separate data such as audio and video files. The partitioning scheme is stored in a partition table such as Master Boot Record (MBR) or GUID Partition Table (GPT).

Partition tables are created and modified using one of many partitioning tools. The tools available for Arch Linux are listed in the #Partitioning tools section.

Partitions usually contain a file system directly which is accomplished by creating a file system on (a.k.a. formatting) the partition. Alternatively, partitions can contain LVM, block device encryption or RAID, which ultimately provide device files on which a file system can be placed (or the devices can be stacked further).

Any block device (e.g. disk, partition, LUKS device, LVM logical volume or RAID array) that directly contains a mountable file system is called a volume.

There are two main types of partition table available. These are described below in the #Master Boot Record (MBR) and #GUID Partition Table (GPT) sections along with a discussion on how to choose between the two. A third, less common alternative is using a partitionless disk, which is also discussed.

Use a partitioning tool to view the partition table of a block device.

The Master Boot Record (MBR) is the first 512 bytes of a storage device. It contains an operating system boot loader and the storage device's partition table. It plays an important role in the boot process under BIOS systems. See Wikipedia:Master boot record#Disk partitioning for the MBR structure.

The first 440 bytes of MBR are the bootstrap code area. On BIOS systems it usually contains the first stage of the boot loader. The bootstrap code can be backed up, restored from backup or erased using dd.

In the MBR partition table (also known as DOS or MS-DOS partition table) there are 3 types of partitions:

Primary partitions can be bootable and are limited to four partitions per disk or RAID volume. If the MBR partition table requires more than four partitions, then one of the primary partitions needs to be replaced by an extended partition containing logical partitions within it.

Extended partitions can be thought of as containers for logical partitions. A hard disk can contain no more than one extended partition. The extended partition is also counted as a primary partition so if the disk has an extended partition, only three additional primary partitions are possible (i.e. three primary partitions and one extended partition). The number of logical partitions residing in an extended partition is unlimited. A system that dual boots with Windows will require for Windows to reside in a primary partition.

The customary numbering scheme is to create primary partitions sda1 through sda3 followed by an extended partition sda4. The logical partitions on sda4 are numbered sda5, sda6, etc.

GUID Partition Table (GPT) is a partitioning scheme that is part of the Unified Extensible Firmware Interface specification; it uses globally unique identifiers (GUIDs), or UUIDs in the Linux world, to define partitions and partition types. It is designed to succeed the Master Boot Record partitioning scheme method.

At the start of a GUID Partition Table disk there is a protective Master Boot Record (PMBR) to protect against GPT-unaware software. This protective MBR just like an ordinary MBR has a bootstrap code area which can be used for BIOS/GPT booting with boot loaders that support it.

GUID Partition Table (GPT) is an alternative, contemporary, partitioning style; it is intended to replace the old Master Boot Record (MBR) system. GPT has several advantages over MBR which has quirks dating back to MS-DOS times. With the recent developments to the formatting tools, it is equally easy to get good dependability and performance for GPT or MBR.

Some points to consider when choosing:

Some advantages of GPT over MBR are:

The section on #Partitioning tools contains a table indicating which tools are available for creating and modifying GPT and MBR tables.

This article or section needs expansion.

Partitionless disk a.k.a. superfloppy refers to a storage device without a partition table, having one file system occupying the whole storage device. The boot sector present on a partitionless device is called a volume boot record (VBR).

Btrfs can occupy an entire data storage device and replace the MBR or GPT partitioning schemes. See the Btrfs#Partitionless Btrfs disk instructions for details.

This article or section needs expansion.

There are no strict rules for partitioning a hard drive, although one may follow the general guidance given below. A disk partitioning scheme is determined by various issues such as desired flexibility, speed, security, as well as the limitations imposed by available disk space. It is essentially personal preference. If you would like to dual boot Arch Linux and a Windows operating system please see Dual boot with Windows.

This scheme is the simplest, most flexible and should be enough for most use cases given the increase in storage size of consumer grade devices. A swap file can be created and easily resized as needed. It usually makes sense to start by considering a single / partition and then separate out others based on specific use cases like RAID, encryption, a shared media partition, etc… See #Discrete partitions for a description of some common to uncommon dedicated partitions.

The suggested minimum size is 23–32 GiB for a single root partition. More space may be needed for user files and when using a swap file. A bare minimal installation requires about 2 GiB. As examples, a simple server can fit under 4 GiB while a full KDE Plasma installation uses 10 GiB. Both examples require frequent purges of the package cache.

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

Separating out a path as a partition allows for the choice of a different filesystem and mount options. In some cases like a media partition, they can also be shared between operating systems.

Below are some example layouts that can be used when partitioning, and the following subsections detail a few of the directories which can be placed on their own separate partition and then mounted at mount points under /. See file-hierarchy(7) for a full description of the contents of these directories.

The root directory is the top of the hierarchy, the point where the primary filesystem is mounted and from which all other filesystems stem. All files and directories appear under the root directory /, even if they are stored on different physical devices. The contents of the root filesystem must be adequate to boot, restore, recover, and/or repair the system. Therefore, certain directories under / are not candidates for separate partitions.

The / partition or root partition is necessary and it is the most important. The other partitions can be replaced by it.

/ traditionally contains the /usr directory, which can grow significantly depending upon how much software is installed. 15–20 GiB should be sufficient for most users with modern hard disks. If you plan to store a swap file here and do not plan on using a separate /var, you might need a larger partition size (i.e. adding the size of your RAM to be able to hibernate and an additional 8–12 GiB for /var).

A GPT partition should have the "Linux root (x86-64)" type GUID 4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709 (8304 for gdisk). An MBR partition should have the default "Linux" type ID 83.

The /boot directory contains the vmlinuz and initramfs images as well as the boot loader configuration file and boot loader stages. It also stores data that is used before the kernel begins executing user-space programs. /boot is not required for normal system operation, but only during boot and kernel upgrades (when regenerating the initial ramdisk).

See Arch boot process#Boot loader for more information on boot loader requirements and capabilities.

When using an EFI system partition as /boot, the requirements are as described in the EFI system partition article—the correct partition type must be set.

In other cases, it is recommended to set the partition type to Extended Boot Loader (XBOOTLDR) Partition which is GPT partition type GUID BC13C2FF-59E6-4262-A352-B275FD6F7172 (ea00 type for gdisk, xbootldr type for fdisk) or MBR partition type ID ea.

In both cases the suggested size for the partition is 1 GiB, which should give enough space to house multiple kernels. If still in doubt, 4 GiB ought to be enough for anybody.

The /home directory contains user-specific configuration files, caches, application data and media files.

Separating out /home allows / to be re-partitioned separately, but note that you can still reinstall Arch with /home untouched even if it is not separate—the other top-level directories just need to be removed, and then pacstrap can be run.

You should not share home directories between users on different distributions, because they use incompatible software versions and patches. Instead, consider sharing a media partition or at least using different home directories on the same /home partition. The size of this partition varies.

A GPT partition should have the "Linux home" type GUID 933AC7E1-2EB4-4F13-B844-0E14E2AEF915 (8302 type for gdisk, home type for fdisk). An MBR partition should have the default "Linux" type ID 83.

A swap is a file or partition that provides disk space used as virtual memory. Swap files and swap partitions are equally performant, but swap files are much easier to resize as needed. A swap partition can potentially be shared between operating systems, but not if hibernation is used.

Since computers have gained memory capacities superior to a gibibit, the previous "twice the amount of physical RAM" rule has become outdated. A sane default size is 4 GiB.

To use hibernation (a.k.a. suspend to disk) it is advised to create the swap partition at the size of RAM. Although the kernel will try to compress the suspend-to-disk image to fit the swap space there is no guarantee it will succeed if the used swap space is significantly smaller than RAM. See Power management/Suspend and hibernate#Hibernation for more information.

A GPT partition should have the "Linux swap" type with GUID 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (8200 type for gdisk, swap type for fdisk). An MBR partition should have the "Linux swap" type ID 82.

One can consider mounting a "data" partition to cover various files to be shared by all users. Using the /home partition for this purpose is fine as well. The size of this partition varies.

A GPT partition should have the default "Linux filesystem" type GUID 0FC63DAF-8483-4772-8E79-3D69D8477DE4. An MBR partition should have the default "Linux" type ID 83.

The /var directory stores variable data such as spool directories and files, administrative and logging data, pacman's cache, etc. It is used, for example, for caching and logging, and hence frequently read or written. Keeping it in a separate partition avoids running out of disk space due to flunky logs, etc.

It exists to make it possible to mount /usr as read-only. Everything that historically went into /usr that is written to during system operation (as opposed to installation and software maintenance) must reside under /var.

/var will contain, among other data, the pacman cache. Retaining these packages is helpful in case a package upgrade causes instability, requiring a downgrade to an older, archived package. The pacman cache will grow as the system is expanded and updated, but it can be safely cleared if space becomes an issue.

8–12 GiB on a desktop system should be sufficient for /var, depending on how much software will be installed. For users of NVIDIA, Wayland and GDM, consider adding to this partition size as to have enough free space to fit your whole video memory.

A GPT partition should have the "Linux variable data" a.k.a. "Linux /var" type GUID 4D21B016-B534-45C2-A9FB-5C16E091FD2D (8310 type for gdisk). An MBR partition should have the default "Linux" type ID 83.

This article or section needs expansion.

The following examples use /dev/sda as the example disk with /dev/sda1 as the first partition. The block device naming scheme will differ if you are partitioning a NVMe disk (e.g. /dev/nvme0n1 with partitions starting from /dev/nvme0n1p1) or an SD card or eMMC disk (e.g. /dev/mmcblk0 with partitions starting from /dev/mmcblk0p1). See Device file#Block device names for more information.

The following programs are used to create and/or manipulate device partition tables and partitions. See the linked articles for the exact commands to be used.

This table will help you to choose utility for your needs:

The rule of thumb is to align a partition's start and size to mebibytes. See Advanced Format#Partition alignment.

The CONFIG_EFI_PARTITION option in the kernel config enables GPT support in the kernel (despite the name, EFI PARTITION which looks close to EFI system partition). This option must be built in the kernel and not compiled as a loadable module. This option is required even if GPT disks are used only for data storage and not for booting. This option is enabled by default in all Arch's officially supported kernels. In case of a custom kernel, enable this option by doing CONFIG_EFI_PARTITION=y.

Some old BIOSes (from before year 2010) attempt to parse the boot sector and refuse to boot it if it does not contain a bootable MBR partition. This is a problem if one wants to use GPT on this disk, because, from the BIOS viewpoint, it contains only one, non-bootable, MBR partition of type ee (i.e., the protective MBR partition). One can mark the protective MBR entry as bootable using fdisk -t mbr /dev/sda, and it will work on some BIOSes. However, the UEFI specification prohibits the protective MBR partition entry from being bootable, and UEFI-based boards do care about this, even in the legacy boot mode. So, this matters if one wants to create a GPT-based USB flash drive that is supposed to boot both on modern UEFI-based boards and also on old BIOSes that insist on finding a bootable MBR partition. It is not possible to solve this problem using traditional tools such as fdisk or gdisk, but it is possible to create a fake MBR partition entry suitable for both kinds of BIOSes manually as a sequence of bytes.

The command below will overwrite the second MBR partition slot and add a bootable partition there of type 0 (i.e. unused), covering only the first sector of the device. It will not interfere with the GPT or with the first MBR partition entry which normally contains a protective MBR partition.

The end result will look like this:

If a SATA or NVMe drive is visible in firmware setup, but not to Linux (e.g. fdisk -l does not list it), it is possible that the controller is in firmware RAID mode.

For NVMe, the journal should show something like:

The solution is to enter firmware setup and disable NVMe RAID mode and change the SATA controller operation mode from RAID to AHCI. Mind that the setting may have a different name (e.g. "Intel Rapid Storage Technology", "Intel RST", "Intel VMD controller" or "VMD") and it could also be per-controller or per-port.

**Examples:**

Example 1 (unknown):
```unknown
parted /dev/sdX print
```

Example 2 (unknown):
```unknown
fdisk -l /dev/sdX
```

Example 3 (unknown):
```unknown
/dev/nvme0n1
```

Example 4 (unknown):
```unknown
/dev/mmcblk0
```

---

## NTFS-3G

**URL:** https://wiki.archlinux.org/title/NTFS-3G

**Contents:**
- Installation
- Manual mounting
- Formatting
- Configuring
  - Default settings
  - Linux compatible permissions
  - Allowing group/user
  - Basic NTFS-3G options
  - Allowing user to mount
- Resizing NTFS partition

NTFS-3G is an open source implementation of Microsoft NTFS that includes read and write support. NTFS-3G developers use the FUSE file system to facilitate development and to help with portability.

Install the ntfs-3g package.

Two options exist when manually mounting NTFS partitions. The traditional:

The mount type ntfs-3g does not need to be explicitly specified in Arch. The mount command by default will use /usr/bin/mount.ntfs which is symlinked to /usr/bin/ntfs-3g after the ntfs-3g package is installed.

The second option is to call ntfs-3g directly:

See ntfs-3g(8) for the available options.

Your NTFS partition(s) can be setup to mount automatically, or pre-configured to be able to mount in a certain way when you would like them to be mounted. This configuration can be done in the static filesystem configuration (fstab) or by the use of udev rules.

Using the default settings will mount the NTFS partition(s) at boot. With this method, if the parent folder that it is mounted upon has the proper user or group permissions (e.g. /run/media/username/), then that user or group will be able to read and write on that partition(s).

Permissions on a Linux system are normally set to 755 for folders and 644 for files. It is recommended to keep these permissions in use for the NTFS partition as well if you use the partition on a regular basis. The following example assigns the above permissions to a normal user:

Alternatively, if the Windows permissions do matter to you, you can use the ntfsusermap(8) command to map Windows users to Linux ones. ntfs-3g will handle the translation of these permissions.

First, you need to know the SID of the desired Windows user. You can determine this either using the ntfsusermap wizard to guess off of file paths, or by executing wmic useraccount get on the Windows system to get a definitive list of users. Then, reorder your UserMapping file such that the Windows user SID is above the service account SIDs.

In /etc/fstab you can also specify other options like those who are allowed to access (read) the partition. For example, for you to allow people in the groupid group to have access:

By default, the above line will enable write support for root only. To enable user writing, you have to specify the user who should be granted write permissions. Use the uid parameter together with your user id to enable user writing:

If you are running on a single user machine, you may like to own the file system yourself and grant all possible permissions:

For most, the above settings should suffice. Here are a few other options that are general common options for various Linux filesystems. For a complete list, see ntfs-3g(8) § OPTIONS.

The following option is specific to ntfs-3g only:

By default, ntfs-3g requires root rights to mount the filesystem if it is a block device, even with the user option in /etc/fstab. See ntfs-3g-faq for details. The user option in the fstab is still required.

For non-blockfiles like normal images, ntfs-3g on the command-line should work out-of-the-box with normal user privileges as the underlying FUSE calls are redirected to the setuid-root fusermount when direct kernel interaction is unavailable.

Most systems that are purchased already have Windows installed on it, and some people would prefer not wipe it off completely when doing an Arch Linux installation. For this reason, among others, it is useful to resize the existing Windows partition to make room for a Linux partition or two. This is often accomplished with a Live CD or bootable USB thumb drive.

For Live CDs the typical procedure is to download an ISO file, burn it to a CD, and then boot from it. InfraRecorder is a free (as in GPL3) CD/DVD burning application for Windows which fits the bill nicely. If you would rather use a bootable USB media instead, see USB flash installation media for methods to create bootable USB stick.

There are a number of bootable CD/USB images available. This list is not exhaustive, but is a good place to start:

Note that the important programs for resizing NTFS partitions include ntfs-3g and a utility like (G)parted or fdisk, provided by the util-linux package. Unless you are an "advanced" user it is advisable to use a tool like GParted to perform any resize operations to minimize the chance of data loss due to user error.

If you already have Arch Linux installed on your system and simply want to resize an existing NTFS partition, you can use the parted and ntfs-3g packages to do it. Optionally, you can use the GParted GUI after installing the GParted package. At the core of the resizing is the ntfsresize(8) command.

When mounting an NTFS filesystem for Windows 10, and reading files or directories, you may

The reason for this are NTFS reparse points, used by Microsoft to extend the file system. NTFS-3G does not support some types of reparse points by default. NTFS-3G plugins may be used to provide compatibility with a part of the features defined by the following reparse points:

See this page for further details, and archive.org for downloads.

If an NTFS filesystem has errors on it, NTFS-3G will mount it as read-only. To fix an NTFS filesystem, load Windows and run its disk checking program, chkdsk.

Note that ntfsfix can only repair some errors. If it fails, chkdsk will probably succeed.

To fix the NTFS file system, the device must already be unmounted. For example, to fix an NTFS partition residing in /dev/sda2:

If all went well, the volume will now be writable.

See Character encoding#Incorrect mount encoding.

When dual booting with Windows 8 or 10, trying to mount a partition that is visible to Windows may yield the following error:

The problem is due to a feature introduced in Windows 8 called "fast startup". When fast startup is enabled, part of the metadata of all mounted partitions are restored to the state they were at the previous closing down. As a consequence, changes made on Linux may be lost. This can happen to any NTFS partition when selecting "Shut down" or "Hibernate" under Windows 8 or 10. Leaving Windows by selecting "Restart", however, is apparently safe.

To enable writing to the partitions on other operating systems, be sure fast startup is disabled. This can be achieved by issuing as an administrator the command:

You can check the current settings on Control Panel > Hardware and Sound > Power Options > System Setting > Choose what the power buttons do. The box Turn on fast startup should either be disabled or missing.

As an alternative to above clean shutdown method, there is a way to completely destroy NTFS metadata that was saved after hibernating. This method is only feasible if you are not able or unwilling to boot into Windows and shut it down completely. This is by running ntfsfix provided by ntfs-3g.

If you cannot mount your NTFS partition even when following this guide, try using the UUID instead of device name in /etc/fstab for all NTFS partitions. See fstab#File system UUIDs for an example.

Windows will not recognize a NTFS partition that does not have a corresponding partition type. A common pitfall when creating an NTFS partition to work with Windows is forgetting to set the partition type as NTFS. See fdisk or one of the partitioning tools.

This article or section is being considered for removal.

There is a web page[dead link 2024-10-19—SSL error] on "advanced features", maintained by Jean-Pierre André, one of the NTFS-3G authors. It provides:

Information provided in the documentation apply to the Tuxera version (2017.3.23) too. The system-compression and dedupe plugins work with the Tuxera version, but the onedrive plugin requires a tweak of the plugin-loading system only available in advanced releases.

Since August 30, 2021, NTFS-3G AR has been merged back to the mainline NTFS-3G, which has moved to GitHub and restarted active development. The plugin source code has not been merged, however.

**Examples:**

Example 1 (unknown):
```unknown
# mount /dev/your_NTFS_partition /mount/point
```

Example 2 (unknown):
```unknown
/usr/bin/mount.ntfs
```

Example 3 (unknown):
```unknown
/usr/bin/ntfs-3g
```

Example 4 (unknown):
```unknown
# ntfs-3g /dev/your_NTFS_partition /mount/point
```

---

## RAID

**URL:** https://wiki.archlinux.org/title/RAID

**Contents:**
- RAID levels
  - Standard RAID levels
  - Nested RAID levels
  - RAID level comparison
  - LINEAR
- Implementation
  - Which type of RAID do I have?
- Installation
  - Prepare the devices
  - Partition the devices

Redundant Array of Independent Disks (RAID) is a storage technology that combines multiple disk drive components—typically disk drives or partitions thereof—into a logical unit. Depending on the RAID implementation, this logical unit can be a file system or an additional transparent layer that can hold several partitions.

Data is distributed across the drives in one of several ways called #RAID levels, depending on the level of redundancy and performance required. The RAID level chosen can thus prevent data loss in the event of a hard disk failure, increase performance or be a combination of both.

This article explains how to create and manage a software RAID array using mdadm(8).

Despite redundancy implied by most RAID levels, RAID does not guarantee that data is safe. A RAID will not protect data if there is a fire, the computer is stolen or multiple hard drives fail at once. Furthermore, installing a system with RAID is a complex process that may destroy data.

There are many different levels of RAID; listed below are the most common.

Best; on par with RAID0 but redundant

* Where n is standing for the number of dedicated disks.

LINEAR allows to map two or more devices into a single device, without parallel accesses like RAID0 but allowing to fully use disks from different sizes. To create a pseudo RAID using this mode without mdadm, one can either use the low-level dmsetup(8) utility, the high-level LVM framework or the Btrfs filesystem.

The RAID devices can be managed in different ways:

Since software RAID is implemented by the user, the type of RAID is easily known to the user.

However, discerning between FakeRAID and true hardware RAID can be more difficult. As stated, manufacturers often incorrectly distinguish these two types of RAID and false advertising is always possible. The best solution in this instance is to run the lspci command and looking through the output to find the RAID controller. Then do a search to see what information can be located about the RAID controller. Hardware RAID controllers appear in this list, but FakeRAID implementations do not. Also, true hardware RAID controllers are often rather expensive, so if someone customized the system, then it is very likely that choosing a hardware RAID setup made a very noticeable change in the computer's price.

Install mdadm. mdadm is used for administering pure software RAID using plain block devices: the underlying hardware does not provide any RAID logic, just a supply of disks. mdadm will work with any collection of block devices. Even if unusual. For example, one can thus make a RAID array from a collection of thumb drives.

If the device is being reused or re-purposed from an existing array, erase any old RAID configuration information:

or if a particular partition on a drive is to be deleted:

It is highly recommended to partition the disks to be used in the array. Since most RAID users are selecting disk drives larger than 2 TiB, GPT is required and recommended. See Partitioning for more information on partitioning and the available partitioning tools.

For those creating partitions on HDDs with a MBR partition table, the partition types IDs available for use are:

See Linux Raid Wiki:Partition Types for more information.

Use mdadm to build the array. See mdadm(8) for supported options. Several examples are given below.

The following example shows building a 2-device RAID1 array:

The following example shows building a RAID5 array with 4 active devices and 1 spare device:

The following example shows building a RAID10,far2 array with 2 devices:

The array is created under the virtual device /dev/mdX, assembled and ready to use (in degraded mode). One can directly start using it while mdadm resyncs the array in the background. It can take a long time to restore parity. Check the progress with:

By default, most of mdadm.conf is commented out, and it contains just the following:

This directive tells mdadm to examine the devices referenced by /proc/partitions and assemble as many arrays as possible. This is fine if you really do want to start all available arrays and are confident that no unexpected superblocks will be found (such as after installing a new storage device). A more precise approach is to explicitly add the arrays to /etc/mdadm.conf:

This results in something like the following:

This also causes mdadm to examine the devices referenced by /proc/partitions. However, only devices that have superblocks with a UUID of 27664… are assembled in to active arrays.

See mdadm.conf(5) for more information.

Once the configuration file has been updated the array can be assembled using mdadm:

The array can now be formatted with a file system like any other partition, just keep in mind that:

Two parameters are required to optimise the filesystem structure to fit optimally within the underlying RAID structure: the stride and stripe width. These are derived from the RAID chunk size, the filesystem block size, and the number of "data disks".

The chunk size is a property of the RAID array, decided at the time of its creation. mdadm's current default is 512 KiB. It can be found with mdadm:

The block size is a property of the filesystem, decided at its creation. The default for many filesystems, including ext4, is 4 KiB. See /etc/mke2fs.conf for details on ext4.

The number of "data disks" is the minimum number of devices in the array required to completely rebuild it without data loss. For example, this is N for a raid0 array of N devices and N-1 for raid5.

Once you have these three quantities, the stride and the stripe width can be calculated using the following formulas:

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 2*128 so the stripe width = 256.

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 3*128 so the stripe width = 384.

For more on stride and stripe width, see: RAID Math.

Example formatting to ext4 with the correct stripe width and stride:

stride = chunk size / block size. In this example, the math is 512/4 so the stride = 128.

stripe width = # of physical data disks * stride. In this example, the math is 2*128 so the stripe width = 256.

Users wanting to mount the RAID partition from a Live CD, use:

If your RAID 1 that is missing a disk array was wrongly auto-detected as RAID 1 (as per mdadm --detail /dev/mdnumber) and reported as inactive (as per cat /proc/mdstat), stop the array first:

You should create the RAID array between the Partitioning and formatting steps of the Installation Procedure. Instead of directly formatting a partition to be your root file system, it will be created on a RAID array. Follow the section #Installation to create the RAID array. Then continue with the installation procedure until the pacstrap step is completed. When using UEFI boot, also read EFI system partition#ESP on software RAID1.

After the base system is installed the default configuration file, mdadm.conf, must be updated like so:

Always check the mdadm.conf configuration file using a text editor after running this command to ensure that its contents look reasonable.

Continue with the installation procedure until you reach the step Installation guide#Initramfs, then follow the next section.

Install mdadm and add mdadm_udev to the HOOKS array of the mkinitcpio.conf to add support for mdadm into the initramfs image:

Then regenerate the initramfs.

Point the root parameter to the mapped device. E.g.:

If booting from a software raid partition fails using the kernel device node method above, an alternative way is to use one of the methods from Persistent block device naming, for example:

Since version 5.3.4 of the Linux kernel, you need to explicitly tell the kernel which RAID0 layout should be used: RAID0_ORIG_LAYOUT (1) or RAID0_ALT_MULTIZONE_LAYOUT (2).[1] You can do this by providing the kernel parameter as follows:

The correct value depends upon the kernel version that was used to create the raid array: use 1 if created using kernel 3.14 or earlier, use 2 if using a more recent version of the kernel. One way to check this is to look at the creation time of the raid array:

Here we can see that this raid array was created on September 24, 2015. The release date of Linux Kernel 3.14 was March 30, 2014, and as such this raid array is most likely created using a multizone layout (2).

It is good practice to regularly run data scrubbing to check for and fix errors. Depending on the size/configuration of the array, a scrub may take multiple hours to complete.

To initiate a data scrub:

The check operation scans the drives for bad sectors and automatically repairs them. If it finds good sectors that contain bad data (i.e. a mismatch, the data in a sector does not agree with what the data from another disk indicates that it should be, for example the parity block + the other data blocks would cause us to think that this data block is incorrect), then no action is taken, but the event is logged (see below). This "do nothing" allows admins to inspect the data in the sector and the data that would be produced by rebuilding the sectors from redundant information and pick the correct data to keep.

As with many tasks/items relating to mdadm, the status of the scrub can be queried by reading /proc/mdstat.

To stop a currently running data scrub safely:

When the scrub is complete, admins may check how many blocks (if any) have been flagged as bad:

It is a good idea to set up a cron job as root to schedule a periodic scrub. See raid-checkAUR which can assist with this. To perform a periodic scrub using systemd timers instead of cron, See raid-check-systemdAUR which contains the same script along with associated systemd timer unit files.

Due to the fact that RAID1 and RAID10 writes in the kernel are unbuffered, an array can have non-0 mismatch counts even when the array is healthy. These non-0 counts will only exist in transient data areas where they do not pose a problem. However, we cannot tell the difference between a non-0 count that is just in transient data or a non-0 count that signifies a real problem. This fact is a source of false positives for RAID1 and RAID10 arrays. It is however still recommended to scrub regularly in order to catch and correct any bad sectors that might be present in the devices.

One can remove a block device from the array after marking it as faulty:

Now remove it from the array:

If the device has not failed entirely, but you would like to replace it, e.g. because it looks like it is dying, you can actually handle replacement more gracefully by first adding a new drive and then telling mdadm to replace it.

For example, with /dev/sdc1 as the new one and /dev/sdb1 as the failing one:

The --with /dev/sdc1 part is optional, but more explicit. See [2] for more details.

To remove a device permanently (for example, to use it individually from now on), follow the steps above (fail/remove or add/replace) and then run:

Adding new devices with mdadm can be done on a running system with the devices mounted. Partition the new device using the same layout as one of those already in the arrays as discussed above.

Assemble the RAID array if it is not already assembled:

Add the new device to the array:

This should not take long for mdadm to do.

This article or section needs expansion.

Depending on the type of RAID (for example, with RAID1), mdadm may add the device as a spare without syncing data to it. You can increase the number of disks the RAID uses by using --grow with the --raid-devices option. For example, to increase an array to four disks:

You can check the progress with:

Check that the device has been added with the command:

This is because the above commands will add the new disk as a "spare" but RAID0 does not have spares. If you want to add a device to a RAID0 array, you need to "grow" and "add" in the same command, as demonstrated below:

If larger disks are installed in a RAID array or partition size has been increased, it may be desirable to increase the size of the RAID volume to fill the larger available space. This process may be begun by first following the above sections pertaining to replacing disks. Once the RAID volume has been rebuilt onto the larger disks it must be "grown" to fill the space.

Next, partitions present on the RAID volume /dev/md0 may need to be resized. See Partitioning for details. Finally, the filesystem on the above mentioned partition will need to be resized. If partitioning was performed with gparted this will be done automatically. If other tools were used, unmount and then resize the filesystem manually.

Syncing can take a while. If the machine is not needed for other tasks the speed limit can be increased.

In the above example, it would seem the max speed is limited to approximately 238 M/sec.

Check the current speed limit (in kibibytes per second, KiB/s):

Set a new maximum speed of raid resyncing operations using sysctl:

Then check out the syncing speed and estimated finish time.

To improve RAID5 performance for fast storage (e.g. NVMe), increase /sys/block/mdx/md/group_thread_cnt to more threads. For example, to use 8 threads to operate on a RAID5 device:

See git kernel commit 851c30c9badf.

To update the RAID superblock, you need to first unmount the array and then stop the array with the following command:

Then you can update certain parameters by reassembling the array. For example, to update the homehost:

See the arguments of --update for details.

A simple one-liner that prints out the status of the RAID devices:

Or preferably using tmux:

The iotop package displays the input/output stats for processes. Use this command to view the IO for raid threads.

The iostat utility from sysstat package displays the input/output statistics for devices and partitions.

mdadm provides the systemd service mdmonitor.service which can be useful for monitoring the health of your raid arrays and notifying you if anything goes wrong.

This service is special in that it cannot be manually activated like a regular service; mdadm will take care of activating it via udev upon assembling your arrays on system startup, but it will only do so if an email address and/or program has been configured for its notifications (see below).

To enable this functionality, edit /etc/mdadm.conf and define the email address:

Then, to verify that everything is working as it should, run the following command:

If the test is successful and the email is delivered, then you are done; the next time your arrays are reassembled, mdmonitor.service will begin monitoring them for errors.

Like Email notification above, edit /etc/mdadm.conf and edit the line:

The argument for PROGRAM is the script you want to run for any event. Which then interact with proper network monitoring agents. Or even IM clients or push notification services like ntfy.sh for home users.

Test in the same way as for email notification above.

If you are getting error when you reboot about "invalid raid superblock magic" and you have additional hard drives other than the ones you installed to, check that your hard drive order is correct. During installation, your RAID devices may be hdd, hde and hdf, but during boot they may be hda, hdb and hdc. Adjust your kernel line accordingly. This is what happened to me anyway.

If you suddenly (after reboot, changed BIOS settings) experience Error messages like:

It does not necessarily mean that a drive is broken. You often find panic links on the web which go for the worst. In a word, No Panic. Maybe you just changed APIC or ACPI settings within your BIOS or Kernel parameters somehow. Change them back and you should be fine. Ordinarily, turning ACPI and/or ACPI off should help.

When an md array is started, the superblock will be written, and resync may begin. To start read-only set the kernel module md_mod parameter start_ro. When this is set, new arrays get an 'auto-ro' mode, which disables all internal io (superblock updates, resync, recovery) and is automatically switched to 'rw' when the first write request arrives.

To set the parameter at boot, add md_mod.start_ro=1 to your kernel line.

Or set it at module load time by Kernel module#Using modprobe.d or from directly from /sys/:

You might get the above mentioned error also when one of the drives breaks for whatever reason. In that case you will have to force the raid to still turn on even with one disk short. Type this (change where needed):

Now you should be able to mount it again with something like this (if you had it in fstab):

Now the raid should be working again and available to use, however with one disk short. So, to add that one disc partition it the way like described above in #Prepare the devices. Once that is done you can add the new disk to the raid by doing:

you probably see that the raid is now active and rebuilding.

You also might want to update your configuration (see: #Update configuration file).

There are several tools for benchmarking a RAID. The most notable improvement is the speed increase when multiple threads are reading from the same RAID volume.

bonnie++ tests database type access to one or more files, and creation, reading, and deleting of small files which can simulate the usage of programs such as Squid, INN, or Maildir format e-mail. The enclosed ZCAV program tests the performance of different zones of a hard drive without writing any data to the disk.

hdparm should not be used to benchmark a RAID, because it provides very inconsistent results.

**Examples:**

Example 1 (unknown):
```unknown
mdadm --grow
```

Example 2 (unknown):
```unknown
# mdadm --misc --zero-superblock /dev/drive
```

Example 3 (unknown):
```unknown
# mdadm --misc --zero-superblock /dev/partition
```

Example 4 (unknown):
```unknown
A19D880F-05FC-4D3B-A006-743F0F84911E
```

---

## CDemu

**URL:** https://wiki.archlinux.org/title/CDemu

**Contents:**
- Installation
  - GUI
- Examples

CDemu is a software suite designed to emulate an optical drive and disc (including CD-ROMs and DVD-ROMs). It enables you to use other disk image formats that contain more than just the standard ISO-9660 filesystem, for instance .bin/.cue, .nrg, or .ccd images. mount can directly handle only .iso disc images (which contain a single filesystem), but many images contain multiple sessions, mixed data/audio tracks… In short, cdemu enables you to mount nearly any kind of image file with ease.

CDemu can be installed with the package cdemu-client. This package pulls cdemu-daemon as its dependency, which provides a cdemu-daemon.service that can be enabled and started. Mind this is a user service. If you are using a custom kernel, instead of the normal vhba kernel module package (vhba-module) you must use the DKMS variant of the package: vhba-module-dkms.

Since systemd does not automatically load drivers for CD/DVD drives, you need to do it manually:

There are several GUIs available:

Loading a single image to first device:

Loading multiple-file image to first device:

Loading a text-based image in non-ASCII/non-Unicode encoding:

Loading an encrypted image with password provided as an argument:

Unloading first device:

Displaying device status:

Displaying device mapping information:

Setting daemon debug mask for the first device:

Obtaining library debug mask for the first device:

Disabling DPM emulation on all devices:

Enabling transfer rate emulation on first device:

Changing device ID of first device:

Enumerating supported parsers:

Enumerating supported fragments:

Enumerating supported daemon debug masks:

Enumerating supported library debug masks:

Displaying daemon and library version:

Enabling support for CSS encryption on drive 0 (For when a DVD video playback is choppy)

**Examples:**

Example 1 (unknown):
```unknown
cdemu-daemon.service
```

Example 2 (unknown):
```unknown
# modprobe -a sg sr_mod vhba
```

Example 3 (unknown):
```unknown
$ cdemu load 0 ~/image.mds
```

Example 4 (unknown):
```unknown
$ cdemu load 0 ~/session1.toc ~/session2.toc ~/session3.toc
```

---

## udisks

**URL:** https://wiki.archlinux.org/title/Udiskie

**Contents:**
- Installation
- Configuration
  - Permissions
  - Default mount options
- Usage
- Tips and tricks
  - Mount helpers
    - udevadm monitor
  - Mount to /media
  - Mount loop devices

udisks provides a daemon udisksd, that implements D-Bus interfaces used to query and manipulate storage devices, and a command-line tool udisksctl, used to query and use the daemon.

Install the udisks2 package.

udisksd(8) is started on-demand by D-Bus and should not be enabled explicitly. It can be controlled through the command-line with udisksctl(1).

Actions a user can perform using udisks are restricted with polkit. If the user session is not activated or present (for example, when controlling udisks from a systemd/User service), adjust polkit rules accordingly.

See https://github.com/coldfix/udiskie/wiki/Permissions for common udisks permissions for the storage group, and [1] for a more restrictive example. If you are using Dolphin, you may see [2].

It is possible to define default mount options in /etc/udisks2/mount_options.conf. Create the file if it does not already exist. The built-in defaults and some examples can be seen in /etc/udisks2/mount_options.conf.example.[3]

The options can target specific filesystem types. For example, mount btrfs filesystems with zstd compression enabled:

To manually mount a removable drive, for example /dev/sdc:

See udisksctl help for more.

The automatic mounting of devices is easily achieved with udisks wrappers. See also List of applications/Utilities#Mount tools.

You may use udevadm monitor to monitor block events and mount drives when a new block device is created. Stale mount points are automatically removed by udisksd, such that no special action is required on deletion.

By default, udisks2 mounts removable drives under the ACL controlled directory /run/media/$USER/. If you wish to mount to /media instead, use this rule:

Since /media, unlike /run, is not mounted by default as a tmpfs, you may also wish to create a tmpfiles.d snippet to clean stale mountpoints at every boot:

To easily mount ISO images, use the following command:

This will create a read only loop device and show the ISO image ready to mount. Remove the -r flag to be able to write to it. The name of the created loop device is output by the above loop-setup command.

You can unmount, and remount, the image as long as the specific loop device is in place. When done working with the specific loop device, use

to delete it. Substitute /dev/loop0 with the name of the specific loop device.

Loop devices are cheap. Therefore, many loop devices can be created in practice without worrying about a denial of service issue. See [4].

If you wish to prevent certain partitions or drives appearing on the desktop, you can create a udev rule, for example /etc/udev/rules.d/10-local.rules:

shows all partitions with the exception of sda1 and sda2 on your desktop.

Because block device names can change between reboots, it is also possible to use UUIDs to hide partitions or whole devices. Matching by UUID is only possible after /usr/lib/udev/rules.d/60-persistent-storage.rules has been processed, so make sure to choose a file name that will be ordered after it. For example:

The above line is also useful to hide multi device btrfs filesystems, as all the devices from a single btrfs filesystem will share the same UUID across the devices but will have different SUB_UUID for each individual device.

At start-up and when a drive is connected, udisksd will apply configuration stored in the file /etc/udisks2/IDENTIFIER.conf where IDENTIFIER is the value of the Drive:Id property for the drive. Currently ATA settings are supported. See udisks(8) for available options. These settings have essentially the same effect as those of hdparm, but they are persistent as long as the udisks daemon is autostarted.

For example, to set standby timeout to 240 (20 minutes) for a drive, add the following:

To obtain the DriveId for your drive, use udevadm info --query=all --name=sdx | grep ID_SERIAL | sed "s/_/-/g"

Alternatively, use a GUI utility to manage the configuration file, such as gnome-disk-utility.

If most of the devices mounted with Udisks are flash memories, like USB sticks and SD cards, configuring Udisks to not update files' access time may be beneficial. It causes additional and unexpected writes, despite the memory has apparently only been read. The default relatime mount option limits excessive writes for main storage. It does not prevent updates if the access time is older than 24 hours, which is often the case on removable media. To set noatime as the default for all Udisks mounts, add:

This option may be overridden later for specific mounts that do require atime: either in mount-specific /etc/udisks2/mount_options.conf section or through a udev rule setting ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="relatime".

Udisks2 hides certain devices from the user by default. If this is undesired or otherwise problematic, copy /usr/lib/udev/rules.d/80-udisks2.rules to /etc/udev/rules.d/80-udisks2.rules and remove the following section in the copy:

The udisks daemon polls S.M.A.R.T. data from drives regularly. Hard drives with a longer standby timeout than the polling interval may fail to enter standby. Drives that are already spun down are usually not affected. There seems no way to disable polling or change the interval as for udisks2 by now. See [5], [6].

However, Standby timeout applied by udisks2 seems to be unaffected. To set standby timeout via udisks, see #Apply ATA settings.

Other possible workarounds could be setting the timeout below the polling interval (10 minutes) or forcing a manual spindown using hdparm -y /dev/sdx.

The factual accuracy of this article or section is disputed.

If mounting a ntfs partition fails with the error:

and in the kernel log with journalctl/dmesg ran as root:

The problem is (as of udisks 2.10), the default is using the NTFS-3G driver, and there are 2 solutions for this:

1: Install NTFS-3G, and restart your machine.

2: Configure udisks2. By default, udisks2 is not configured on an Arch system, and no defaults are defined for non-native filesystems. The easiest way to do so, is to copy /etc/udisks2/mount.options.conf.example to /etc/udisks2/mount.options.conf and uncomment the following lines:

and restart the udisk2 daemon, or restart your machine.

udisks 2.8.2 introduced a breaking change by adding windows_names to NTFS mount options, preventing creation of Win32-incompatible filenames such as nul, screenshot 23-08-21 19:22.jpg. Among other things, this causes Steam Proton to stop initializing. To revert this behavior, use:

Bad filenames generally do not cause issues in Windows unless accessed. chkdsk will treat these names as errors and move the renamed files to found.nnn folders under filesystem root.

If an external HDD is not powered off properly at system shutdown, it may be desirable to fix the issue.

Enable udisks2.service.

A service to invoke our script might look like so:

Enable handle_external_hdds.service

Do a systemd daemon-reload to apply the new setting.

Reboot or restart graphical.target to check if works.

An example script to handle an arbitrary amount of partitions on a single disk looks like so:

uuid_list is a list of space delimited UUIDs corresponding to partitions of the device to check, e.g. "uuid_1" "uuid_2".

Even if nothing seems to be written to a USB stick, memory card, or other removable media, file access times may still be updated. This is a change that needs to be flushed to the device. If that is of concern, consider setting the noatime option for all Udisks mounts.

**Examples:**

Example 1 (unknown):
```unknown
/etc/udisks2/mount_options.conf
```

Example 2 (unknown):
```unknown
/etc/udisks2/mount_options.conf.example
```

Example 3 (unknown):
```unknown
/etc/udisks2/mount_options.conf
```

Example 4 (unknown):
```unknown
[defaults]
btrfs_defaults=compress=zstd
```

---
