# Arch-Wiki - Hardware

**Pages:** 41

---

## OpenGL

**URL:** https://wiki.archlinux.org/title/OpenGL

**Contents:**
- Installation
- Verification
- Switching between drivers
  - Mesa
- OpenGL over Vulkan (Zink)
- Troubleshooting
  - Lenovo GPU Graphics Mesa Error

From Wikipedia:OpenGL:

Learn more at Khronos.

Development of OpenGL ceased in 2017 in favour of Vulkan, the "next generation" API which offers higher performance on newer hardware.

To run applications that use OpenGL, you will need to install the correct driver(s) for your hardware (either GPUs or CPUs).

Mesa is an open-source OpenGL implementation, continually updated to support the latest OpenGL specification. It has a collection of open-source drivers for Intel graphics, AMD (formerly ATI) and NVIDIA GPUs. Mesa also provides software rasterizers, such as llvmpipe.

There are two Mesa packages, each with a distinct set of drivers:

To verify your OpenGL installation, you can use mesa-utils eglinfo, which should display output like this (with different values depending on your setup, of course):

On X11 platform, glxinfo works as well.

From the same package, you can also use eglgears_x11 or glxgears (on X11) or eglgears_wayland (on Wayland) as a basic OpenGL test. You should see 3 rotating gears when running the program.

For Hybrid graphics, see PRIME.

You can override the driver used for an application with the following environment variable:

By default, Mesa searches for drivers in /lib/dri/. You can view the list of installed drivers with

driver in driver_dri.so is the actual name of the driver. If Mesa failed to find the specified driver, it will fall back to llvmpipe.

You can also use an OpenGL software rasterizer by setting the following environment variables:

driver can be either softpipe, llvmpipe, or swr.

From the Mesa documentation:

If you are experiencing issues in your default OpenGL drivers (a bug in RadeonSI, Iris, etc.), you could try using the Zink driver.

According to this Phoronix benchmark, the average FPS might be lower in some applications compared to RadeonSI.

Note that Zink no longer works out-of-the-box on X systems that use the AMD or Intel DDX drivers (xf86-video-amdgpu and xf86-video-intel, respectively). Upstream developers recommend use of the generic modesetting(4) DDX driver. [1] Alternatively, to bypass this issue, you can use the following environment variables:

To use Zink on the proprietary NVIDIA driver, use this command or similar:

Mesa was using CPU (llvmpipe) for rendering, which crashed some GUI software. Fixed this by going to BIOS settings and choosing Dynamic Graphics over Discrete Graphics (If using another computer, choose the option that lets you switch between GPUs than disabling the integrated GPU). This will happen if main GPU driver is not installed but you expect the integrated one to work. [2]

**Examples:**

Example 1 (unknown):
```unknown
nouveau_vieux
```

Example 2 (unknown):
```unknown
$ eglinfo -B
```

Example 3 (unknown):
```unknown
Wayland platform:
EGL API version: 1.5
EGL vendor string: Mesa Project
EGL version string: 1.5
EGL client APIs: OpenGL OpenGL_ES
OpenGL core profile vendor: Intel
OpenGL core profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL core profile version: 4.6 (Core Profile) Mesa 25.1.3-arch1.3
OpenGL core profile shading language version: 4.60
OpenGL compatibility profile vendor: Intel
OpenGL compatibility profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL compatibility profile version: 4.6 (Compatibility Profile) Mesa 25.1.3-arch1.3
OpenGL compatibility profile shading language version: 4.60
OpenGL ES profile vendor: Intel
OpenGL ES profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL ES profile version: OpenGL ES 3.2 Mesa 25.1.3-arch1.3
OpenGL ES profile shading language version: OpenGL ES GLSL ES 3.20

X11 platform:
EGL API version: 1.5
EGL vendor string: Mesa Project
EGL version string: 1.5
EGL client APIs: OpenGL OpenGL_ES
OpenGL core profile vendor: Intel
OpenGL core profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL core profile version: 4.6 (Core Profile) Mesa 25.1.3-arch1.3
OpenGL core profile shading language version: 4.60
OpenGL compatibility profile vendor: Intel
OpenGL compatibility profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL compatibility profile version: 4.6 (Compatibility Profile) Mesa 25.1.3-arch1.3
OpenGL compatibility profile shading language version: 4.60
OpenGL ES profile vendor: Intel
OpenGL ES profile renderer: Mesa Intel(R) UHD Graphics (CML GT2)
OpenGL ES profile version: OpenGL ES 3.2 Mesa 25.1.3-arch1.3
OpenGL ES profile shading language version: OpenGL ES GLSL ES 3.20
```

Example 4 (unknown):
```unknown
eglgears_x11
```

---

## Laptop/Toshiba

**URL:** https://wiki.archlinux.org/title/Laptop/Toshiba

**Contents:**
- Satellite
- Portege

**Examples:**

Example 1 (unknown):
```unknown
ath5k.nohwcrypt=1
```

Example 2 (unknown):
```unknown
i915_enable_rc6
```

Example 3 (unknown):
```unknown
i915_enable_fbc
```

---

## Power management/Suspend and hibernate

**URL:** https://wiki.archlinux.org/title/Power_management/Suspend_and_hibernate

**Contents:**
- Kernel interface (swsusp)
- High level interface (systemd)
- Changing suspend method
- Hibernation
  - About swap partition/file size
  - Configure the initramfs
  - Pass hibernate location to initramfs
    - Manually specify hibernate location
      - Acquire swap file offset
  - Change the image compression algorithm for hibernation

There are multiple methods of suspending available, notably:

The kernel provides basic functionality, and some high level interfaces provide tweaks to handle problematic hardware drivers/kernel modules (e.g. video card re-initialization).

It is possible to directly inform the in-kernel software suspend code (swsusp) to enter a suspended state; the exact method and state depends on the level of hardware support. On modern kernels, writing appropriate strings to /sys/power/state is the primary mechanism to trigger this suspend.

See kernel documentation for details.

systemd provides native commands for suspend, hibernate and a hybrid suspend. This is the default interface used in Arch Linux.

systemctl suspend should work out of the box. For systemctl hibernate to work on your system you might need to follow the instructions at #Hibernation.

There are also two modes combining suspend and hibernate:

See #Sleep hooks for additional information on configuring suspend/hibernate hooks. Also see systemctl(1), systemd-sleep(8), and systemd.special(7).

On systems where S0ix suspension does not provide the same energy savings as the regular S3 sleep, or when conserving energy is preferred to a quick resume time, changing the default suspend method is possible.

Run the following command to see all suspend methods hardware advertises support for (current method is shown in square brackets[1]):

If your hardware does not advertise the deep sleep status, check first if your UEFI advertises some settings for it, generally under Power or Sleep state or similar wording, with options named Windows 10, Windows and Linux or S3/Modern standby support for S0ix, and Legacy, Linux, Linux S3 or S3 enabled for S3 sleep. Failing that, you can keep using s2idle, consider using hibernation or try to patch the DSDT tables (or find a patched version online).

Confirm that your hardware does not exhibit issues with S3 sleep by testing a few sleep cycles after changing the sleep method:

If no issues have been found, you can make the change permanent through the MemorySleepMode directive in systemd-sleep.conf(5):

or through the mem_sleep_default=deep kernel parameter.

In some opposite situations, faulty firmware advertises support for deep sleep, while only s2idle is supported. In this case, an alternative method for using s2idle is available through the SuspendState setting:

In order to use hibernation, you must create a swap partition or file, configure the initramfs so that the resume process will be initiated in early userspace, and specify the location of the swap space in a way that is available to the initramfs, e.g. HibernateLocation EFI variable defined by systemd or resume= kernel parameter. These three steps are described in detail below.

Even if your swap partition is smaller than RAM, you still have a good chance of hibernating successfully. See "image_size" in the kernel documentation for information on the image_size sysfs(5) pseudo-file.

You may either decrease the value of /sys/power/image_size to make the suspend image as small as possible (for small swap partitions), or increase it to possibly speed up the hibernation process. For systems with a large amount of RAM, smaller values may drastically increase the speed of resuming a hibernating system. systemd#systemd-tmpfiles - temporary files can be used to make this change persistent:

The suspend image cannot span multiple swap partitions and/or swap files. It must fully fit in one swap partition or one swap file.[2]

When the system hibernates, the memory image is dumped to the swap space, which also includes the state of mounted file systems. Therefore, the hibernate location must be made available to the initramfs, i.e. before the root file system is mounted for resuming from hibernate to work.

When the system is running on UEFI, systemd-sleep(8) will automatically pick a suitable swap space to hibernate into, and the information of the used swap space is stored in HibernateLocation EFI variable. Upon next boot, systemd-hibernate-resume(8) reads the location off the EFI variable and the system resumes. This means the following steps are not necessary unless the system is using legacy BIOS or you want to choose a different swap space from the automatically-selected one.

The kernel parameter resume=swap_device can be used, where swap_device follows the persistent block device naming. For example:

The kernel parameters will only take effect after rebooting. To hibernate right away, obtain the volume's major and minor device numbers from lsblk and echo them in format major:minor to /sys/power/resume.

For example, if the swap device is 8:3:

If using a swap file, additionally follow the procedures in #Acquire swap file offset.

When using a swap file for hibernation, the block device on which the file system lies should be specified in resume=, and additionally the physical offset of swap file must be specified through resume_offset= kernel parameter. [3]

On file systems other than Btrfs, the value of resume_offset= can be obtained by running filefrag -v swap_file. The output is in a table format and the required value is in the first row of the physical_offset column.

In the example the value of resume_offset= is the first 38912.

Alternatively, to directly acquire the offset value:

For Btrfs, do not try to use the filefrag tool, since the "physical" offset you get from filefrag is not the real physical offset on disk; there is a virtual disk address space in order to support multiple devices.[4] Instead, use the btrfs-inspect-internal(8) command. E.g.:

In this example, the kernel parameter would be resume_offset=198122980.

To apply the change immediately (without rebooting), echo the resume offset to /sys/power/resume_offset. For example, if the offset is 38912:

Starting with Linux 6.9[5], the image compression algorithm for hibernation can be changed. The default compression algorithm is selected based on the compile time option CONFIG_HIBERNATION_DEF_COMP, but it can be overridden at boot time and runtime.

Different compression algorithms have different characteristics and hibernation may benefit when it uses any of these algorithms, especially when a secondary algorithm (LZ4) offers better decompression speeds over a default algorithm (LZO), which in turn reduces hibernation image restore time.

You can override the default algorithm in two ways:

1) Passing hibernate.compressor as a kernel parameter:

2) Specifying the algorithm at runtime:

Currently lzo and lz4 are the supported algorithms with LZO being the default.

It is possible to solve the hibernation problem with zram RAM-only swap by maintaining two or more swap spaces at the same time. systemd will always ignore zram block devices before triggering hibernation [6], therefore keeping both spaces enabled should work without further intervention.

After configuring the swap file, follow the zram page. Make sure zram has the higher swap priority (e.g. pri=100).

Hibernation into a thinly-provisioned LVM volume is possible, but you have to make sure that the volume is fully allocated. Otherwise resuming from it will fail, see FS#50703.

You can fully allocate the LVM volume by simply filling it with zeros. E.g.:

To verify the volume is fully allocated, you can use:

A fully allocated volume will show up as having 100% data usage.

In Linux 6.8, zswap gained a per-cgroup option to disable writeback. By using systemd unit setting MemoryZSwapWriteback (see systemd.resource-control(5) § Memory Accounting and Control) in all possible unit types, zswap writeback can be effectively disabled entirely. This allows to use zswap just like zram with the added benefit of supporting hibernation.

To avoid having to manually create twelve top level per-type drop-in files (for system and user scope, service, slice, socket, mount, swap units types), install zswap-disable-writebackAUR. Enable zswap and reboot for the settings to take effect.

Try to perform memory intensive tasks and confirm that zswap has not written anything to disk:

systemd starts suspend.target, hibernate.target, hybrid-sleep.target, or suspend-then-hibernate.target for each sleep state, respectively. All the aforementioned targets pull in sleep.target. Any of the targets can be used to invoke custom units before or after suspend/hibernate. Separate files should be created for user actions and root/system actions. Examples:

Enable user-suspend@user.service and/or user-resume@user.service for the change to take effect.

For root/system actions:

With the combined unit file, a single hook does all the work for different phases (sleep/resume) and for different targets.

Example and explanation:

systemd-sleep runs all executables in /usr/lib/systemd/system-sleep/, passing two arguments to each of them:

An environment variable called SYSTEMD_SLEEP_ACTION will be set and contain the sleep action that is processing. This is primarily helpful for suspend-then-hibernate where the value of the variable will be suspend, hibernate, or suspend-after-failed-hibernate in cases where hibernation has failed.

The output of any custom script will be logged by systemd-suspend.service, systemd-hibernate.service or systemd-hybrid-sleep.service. You can see its output in systemd's journalctl:

An example of a custom sleep script:

Do not forget to make your script executable.

When resuming, you can automatically unlock your system if it is connected to certain devices or trusted Wi-Fi networks.

Configure your desktop environment so that it locks on resume, and then create a sleep hook that runs the above script after resuming. You also need to install wireless_tools to read the connected Wi-Fi SSID. If you also want to test for connected USB devices, uncomment the lsusb -d ... line in the script and fill in the ID of your trusted device. You can get the ID of your device by running lsusb.

When using a device as e.g a server, suspending/hibernating might not be needed or it could even be undesired. Each sleep state can be disabled through systemd-sleep.conf(5):

Intel Rapid Start Technology is a firmware method of hibernation that allows hibernating from sleep after a predefined interval or according to battery state. This should be faster and more reliable than regular hibernation as it is done by firmware instead of at the operating system level. Generally it must enabled in the firmware, and the firmware also provides support for setting the duration after suspend/battery event triggering hibernation. However, some devices–despite supporting IRST in the firmware–only allow it to be configured via Intel's Windows drivers. In such cases the intel-rst kernel module described below should be able to configure the events under Linux.

With Intel Rapid Start Technology (IRST) enabled, resuming from a deep sleep takes "a few seconds longer than resuming from S3 but is far faster than resuming from hibernation".

Many Intel-based systems have firmware support for IRST but require a special partition on an SSD (rather than an HDD). OEM deployments of Windows may have a pre-existing IRST partition which can be retained during the Arch Linux installation process (rather than wiping and re-partitioning the whole SSD). It should show up as an unformatted partition equal in size to the system's RAM.

If you intend to wipe and re-partition the whole drive (or have already done so), then the IRST partition must be recreated if you also plan on using the technology. This can be done by creating an empty partition equal in size to the system's RAM and by setting its partition type to GUID D3BFE2DE-3DAF-11DF-BA40-E3A556D89593 for a GPT partition or ID 0x84 for an MBR partition. You may also need to enable support for IRST in your system's firmware settings.

The duration of the IRST hibernation process (i.e., copying the "entire contents of RAM to a special partition") is dependent on the system's RAM size and SSD speed and can thus take 20–60 seconds. Some systems may indicate the process's completion with an LED indicator, e.g., when it stops blinking.

Configuring IRST hibernation events in the Linux kernel requires CONFIG_INTEL_RST built-in or as a module. Once loaded via modprobe intel_rst, it should create the files wakeup_events and wakeup_time under /sys/bus/acpi/drivers/intel_rapid_start/*/ that can be used for further configuration. This module is tersely documented, see the source drivers/platform/x86/intel/rst.c for more details.

See also the general Q&A and user guides for Intel Rapid Start Technology.

To measure power consumption in suspend states use Batenergy script to log battery changes to the system journal. This allows to compare power consumption in S3 / S0x states or check after BIOS and kernel updates for regressions and fixes. The script needs bc to be installed for calculation.

You might want to tweak your DSDT table to make it work. See DSDT.

The factual accuracy of this article or section is disputed.

There have been many reports about the screen going black without easily viewable errors or the ability to do anything when going into and coming back from suspend and/or hibernate. These problems have been seen on both laptops and desktops. This is not an official solution, but switching to an older kernel, especially the LTS-kernel, will probably fix this.

A problem may arise when using the hardware watchdog timer (disabled by default, see RuntimeWatchdogSec= in systemd-system.conf(5) § OPTIONS). A buggy watchdog timer may reset the computer before the system finishes creating the hibernation image.

Sometimes the screen goes black due to device initialization from within the initramfs. Removing any modules you might have in Mkinitcpio#MODULES, removing the kms hook and rebuilding the initramfs can possibly solve this issue, in particular with graphics drivers for early KMS. Initializing such devices before resuming can cause inconsistencies that prevents the system resuming from hibernation. This does not affect resuming from RAM. Also, check the blog article best practices to debug suspend issues.

Moving from the ATI video driver to the newer AMDGPU driver could also help to make the hibernation and awakening process successful.

With NVIDIA cards, the VRAM contents are saved to disk when suspending.[8] Make sure that you have enough disk space, otherwise you might get a blank screen when resuming. Another cause for this could be fixed by blacklisting the module nvidiafb. [9]

Laptops with an Intel CPU that load the intel_lpss_pci module for a touchpad may face kernel panic on resume (blinking caps lock) [10]. The module needs to be added to initramfs as:

Then regenerate the initramfs.

System may fail to suspend because of a USB device. You might see the following error:

lspci may give you more information on the failing device:

Try disconnecting devices on that port.

If Wake-on-LAN is active, the network interface card will consume power even if the computer is hibernated.

See Wakeup triggers#Instantaneous wakeup after suspending.

When you hibernate your system, the system should power off (after saving the state on the disk). On some firmware the S4 sleeping state does not work reliably. For example, instead of powering off, the system might reboot or stay on but unresponsive. If that happens, it might be instructive to set the HibernateMode to shutdown in sleep.conf.d(5):

With the above configuration, if everything else is set up correctly, on invocation of a systemctl hibernate the machine will shut down, saving state to disk as it does so.

This can happen when the boot disk is an external disk, and seems to be caused by a BIOS/firmware limitation. The BIOS/firmware tries to boot from an internal disk, while hibernation was done from an OS on an external (or other) disk.

Set HibernateMode=shutdown as shown in #System does not power off when hibernating to solve the problem permanently. If you have already locked yourself out, you can try rebooting your system 4 times (wait for the error to appear each time), which on some BIOS'es forces a normal boot procedure.

If the swap file is in /home/, systemd-logind will not be able to access it, giving the Call to Hibernate failed: No such file or directory warning message and resulting in a need for authentication on systemctl hibernate. This setup should be avoided, as it is considered unsupported upstream. See systemd issue 15354 for two workarounds.

On some motherboards with A520i and B550i chipsets, the system will not completely enter the sleep state or come out of it. Symptoms include the system entering sleep and the monitor turning off while internal LEDs on the motherboard or the power LED stay on. Subsequently, the system will not come back from this state and require a hard power off. If you have similar issues with AMD, first make sure your system is fully updated and check whether the AMD microcode package is installed.

Verify the line starting with GPP0 has the enabled status:

If that is enabled, you can run the following command to disable it:

Now test by running systemctl suspend and let the system go to sleep. Then try to wake the system after a few seconds. If it works, you can make the workaround permanent. Create a systemd unit file:

Do a daemon-reload and start/enable the newly created unit.

Alternatively, you can create a udev rule. Assuming GPP0’s sysfs node is pci:0000:00:01.1 like in the example, run udevadm info -a -p /sys/bus/pci/devices/0000\:00\:01.1 to get the relevant information and create a udev rule like this one:

The udev daemon is already watching for changes in your system by default. If needed you can reload the rules manually.

If, regardless of the setting in logind.conf, the sleep button does not work (pressing it does not even produce a message in syslog), then logind is probably not watching the keyboard device. [11] Do:

You might see something like this:

Notice no keyboard device. List keyboard devices as follows:

Now obtain ATTRS{name} for the parent keyboard device [12]. As an example, on the above list this keyboard device has event6 as device input event, it can be used to search its respective attribute name:

Now write a custom udev rule to add the "power-switch" tag:

After reloading the udev rules and restarting systemd-logind.service, you should see Watching system buttons on /dev/input/event6 in the journal of logind.

Since systemd v256, systemd freezes user.slice before sleeping. This process can fail due to kernel bugs, particularly when KVM is in use.[13][14]

Messages in the logs will contain Failed to freeze unit 'user.slice' before sleep. When such an issue occurs, trying to login (start another session) would fail with:

To temporarily revert back to the old behavior, edit systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, and systemd-suspend-then-hibernate.service with the following drop-in:

However, this drop-in can itself prevent the system from going to sleep.[15]

If you are running a multi boot system (including but not limited to dual boot with Windows) and want to be able to boot into your other system while your main Arch Linux is hibernated, you must take extra caution not to mount filesystems that are still in use by the hibernated system. Before attempting to mount such filesystem within another system, you must make sure to unmount this filesystem before hibernating the system. This can be achieved with sleep hooks.

This issue is particularly relevant for the EFI system partition, because the ESP is expected to be shared across multiple systems. Check the matching section in EFI system partition for mitigation strategies, which can be adapted to other filesystems as well.

**Examples:**

Example 1 (unknown):
```unknown
/sys/power/state
```

Example 2 (unknown):
```unknown
systemctl suspend
```

Example 3 (unknown):
```unknown
systemctl hibernate
```

Example 4 (unknown):
```unknown
systemctl hybrid-sleep
```

---

## Laptop/Samsung

**URL:** https://wiki.archlinux.org/title/Laptop/Samsung

**Contents:**
- Model list

This article or section needs expansion.

**Examples:**

Example 1 (unknown):
```unknown
modprobe.blacklist=viafb
```

Example 2 (unknown):
```unknown
i915.enable_dpcd_backlight=3
```

Example 3 (unknown):
```unknown
/etc/modules-load.d/ohci_hcd.conf
```

Example 4 (unknown):
```unknown
acpi_osi=! acpi_osi="Windows 2022"
```

---

## Nouveau

**URL:** https://wiki.archlinux.org/title/Nouveau

**Contents:**
- Installation
  - Using the Mesa NVK Vulkan Driver
- Loading
  - Early KMS
- Tips and tricks
  - Keep NVIDIA driver installed
  - Installing the latest development packages
  - Dual head
  - Setting console resolution
  - Power management

This article covers the reverse-engineered open-source Nouveau driver for NVIDIA graphics cards. For information about the upstream proprietary nvidia and open-source nvidia-open drivers, see NVIDIA.

Find your card's code name (a more detailed list is available on Wikipedia), and compare it with the feature matrix for supported features.

This article or section is out of date.

Install the mesa package, which provides the DRI driver for 3D acceleration.

See also Hardware video acceleration.

NVK is an open-source Vulkan driver based on Nouveau for Kepler and newer NVIDIA cards.

Using NVK requires Kernel version 6.7 or newer and mesa version 24.1 or newer.

Before enabling NVK you must uninstall any of the following packages (and/or their lib32 and DKMS variants):

If you are using a hybrid laptop or a dual GPU system ensure you do not have Nouveau blacklisted by a GPU manager in /etc/modprobe.d/.

Then install vulkan-nouveau (and if it is required, lib32-vulkan-nouveau).

Add nouveau.config=NvGspRm=1 as a kernel parameter if required. It is enabled by default on Ada Lovelace and newer cards. See note in the documentation.

Finally reboot your system.

To verify everything is working vulkaninfo from vulkan-tools can be used. It should report the NVIDIA GPU in your system as using the NVK driver.

The Nouveau kernel module should load automatically on system boot. If it does not happen, then:

Kernel mode setting (KMS) is supported by the nouveau driver and is enabled early since mkinitcpio v32, as the kms hook is included by default. For other setups, see Kernel mode setting#Early KMS start for instructions on how to enable KMS as soon as possible at the boot process.

The factual accuracy of this article or section is disputed.

If you want to keep the proprietary NVIDIA driver installed (and are not using OpenGL), but want to use the Nouveau driver, follow the steps below:

Comment out nouveau blacklisting in /etc/modprobe.d/nouveau_blacklist.conf or /usr/lib/modprobe.d/nvidia-utils.conf, modifying it as follows:

You may also need to comment out other configuration files that prioritize the proprietary driver, e.g. systemd-modules-load's /usr/lib/modules-load.d/nvidia-utils.conf and udev's /usr/lib/udev/rules.d/60-nvidia.rules. Check what files the driver has installed with the following command:

Then, ensure that you have disabled nvidia--prefixed services that might call nvidia-modprobe to load the module on boot. For example:

And if you are using Xorg, tell Xorg to load nouveau instead of NVIDIA:

Reboot to make effects. And check that it loaded fine by looking at kernel messages:

To get the latest Nouveau improvements

Multiple monitors can be setup with RandR, see Multihead#RandR.

You can pass the resolution to nouveau with the video= kernel line option (see KMS).

The lack of proper power management in the nouveau driver is one of the most important causes of performance issues, since most cards will remain in their lower power state with lower clocks during their use. Experimental support for GPU reclocking is available for some cards (see the Nouveau PowerManagement page) and since kernel 4.5 can be controlled through a debugfs interface located at /sys/kernel/debug/dri/*/pstate.

For example, to check the available power states and the current setting for the first card in your system, run:

It is also possible to manually set/force a certain power state by writing to said interface:

If it is implemented for your card, you can configure fan control via /sys.

pwm1_enable can be set to 0, 1 or 2 meaning NONE, MANUAL and AUTO fan control. If set to manual fan control, you can set pwm1 manually, for example to 40 for 40%.

You can also set it by an udev rule:

You have two solutions to use Optimus on a laptop (aka hybrid graphics, when you have two GPUs on your laptop): bumblebee and PRIME

This article or section is out of date.

Xorg compositors are prone to show issues with Nouveau. Unlike most of them, Picom offers lots of options to tweak for a smoother and tearing free result. A configuration which is expected to deliver a good result would be the following:

Add drm.debug=14 and log_buf_len=16M to your kernel parameters to turn on video debugging:

Create verbose Xorg log:

View loaded video module parameters and values:

If you are still having problems loading the module or starting the X server, append nouveau.config=NvMSI=0 to your Kernel parameters.

Source: https://bugs.freedesktop.org/show_bug.cgi?id=78441

It is possible for the nouveau driver to detect "phantom" outputs. For example, both VGA-1 and LVDS-1 are shown as connected but only LVDS-1 is present.

This causes display problems and/or prevent suspending on lid closure.

The problem can be overcome by disabling the phantom output (VGA-1 in the examples given) with Kernel parameters:

The nouveau kernel module also has an option to disable TV-out detection [2]:

The phantom output can be disabled in Xorg by adding the following to /etc/X11/xorg.conf.d/20-nouveau.conf:

Source: https://web.archive.org/web/20170118202740/http://gentoo-en.vfose.ru/wiki/Nouveau#Phantom_and_unpopulated_output_connector_issues

Xrandr can disable the output:

This can be added to the xinit configuration.

Specific NVIDIA chips with Nouveau may give random system lockups and more commonly throw many kernel messages, seen with dmesg. Try adding the nouveau.noaccel=1 kernel parameter. See Fedora:Common kernel problems#Systems with nVidia adapters using the nouveau driver lock up randomly for more information.

Note that using nouveau.noaccel=1 kernel parameter might cause ~%100 CPU usage on Wayland when there is no iGPU or disabled iGPU by factory. You can switch to X11 session or prefer adding LIBGL_ALWAYS_SOFTWARE=1 environment variable for wayland to disable OpenGL hardware acceleration completely.

As an alternative, you can also use the QT_XCB_FORCE_SOFTWARE_OPENGL=1 environment variable to disable OpenGL acceleration in Qt applications.

NVIDIA graphics cards with recent chipsets can cause startup issues - this includes X11 being unable to start and lspci freezing indefinitely[3][4][5][6][7].

This can break live distributions/installation media. This can be detected either by running lspci, or checking the systemd journal for the error:

The system may start if the Nouveau driver is disabled by passing the following kernel parameters:

The Nouveau driver can then be loaded using

The system should then function correctly. If you have another NVIDIA graphics card, or just want to be safe, you can disable the offending card using:

**Examples:**

Example 1 (unknown):
```unknown
/etc/modprobe.d/
```

Example 2 (unknown):
```unknown
nouveau.config=NvGspRm=1
```

Example 3 (unknown):
```unknown
$ vulkaninfo
```

Example 4 (unknown):
```unknown
...
GPU id : 0 (NVIDIA GeForce RTX 3050 Ti Laptop GPU (NVK GA107)):
       Surface type = VK_KHR_wayland_surface
       Formats: count = 8
...
```

---

## Professional audio

**URL:** https://wiki.archlinux.org/title/Pro_audio

**Contents:**
- Getting started
- Choosing a sound server
  - PipeWire-only
  - PipeWire-as-JACK-Client
  - JACK-only
- JACK parameters
- Latency verification
  - Latency sources
  - Conversion latency
  - Measuring latency

This article describes how to configure your system for multitrack recording, mixing and playing back audio as well as using it to synthesize and generate sounds. Those activities are subsumed under the term professional audio (pro audio) and typically require low latency performance.

Most applications do not need as much high-end hardware, compared to video production or gaming. For more information, refer to The Right Computer System for Digital Audio.

Advanced Linux Sound Architecture (ALSA) is part of the Linux kernel and used for drivers and low-level interface on Arch Linux as the default sound system. ALSA should work out of the box with a default Arch Linux installation. If this is not the case, you must solve the problem before going any further.

Have I set up sound properly?

A vanilla Arch Linux kernel is sufficient for low latency operation in most use cases. #Optimizing system configuration will be necessary only if you are experiencing audio drop-outs (also known as glitches) or if you need (or want) to reach ultra-low latency operations.

To finish with optimizations, these ultra low latency operations may require you to set up a #Realtime kernel.

Although some pro audio software can work with ALSA directly, most of the #Applications mentioned later are JACK Audio Connection Kit or JACK clients. Therefore, you will need to install and setup one of the available sound servers which are outlined soon.

Sound hardware cannot play back sound from more than one application simultaneously. While ALSA can theoretically be configured to mix applications in software this is typically left to a sound server.

As ALSA alone cannot achieve low latencies easily and cannot synchronise multiple audio applications to play on time, starting all at the same time, at the same tempo, etc., and as it can not share audio flux between applications simply by connecting all its clients together, you need not just any sound server, but professional audio class one:

The sound server setup strongly depends on the use case as well as on the workflow and capabilities of some application interaction. JACK was designed to share audio between applications and access an audio device simultaneously by providing the synchronous execution of clients while maintaining constant low latency. Its PipeWire replacement provides a sufficient server for most of the use cases.

This layout illustrates a layer model of the sound server setups to be discussed:

The newer PipeWire framework replaces JACK as well as other sound servers for the sake of simplicity. Thus, it is recommended to first go for a PipeWire-only setup implementing support for JACK clients by installing pipewire-jack and using the vanilla Arch Linux kernel.

For pro audio use, you also have to select the Pro Audio profile installing and using pavucontrol, PulseAudio's mixer.

PipeWire can also be used as a JACK client by installing pipewire-jack-client. This is explained in PipeWire#Run PipeWire on top of native JACK.

The principle of versatility allows you to employ JACK and the #Realtime kernel with #Optimizing system configuration to achieve low latencies for advanced use cases known as JACK-only setup. Using JACK as the only sound server requires any software, that is intended for interaction and audio device access, to run as a JACK client.

Unfortunately, popular desktop applications such as Firefox or most games either dropped JACK support or never implemented it. For that reason this setup should be used for a dedicated pro audio system where non-JACK software can be neglected. If you still need to use software that cannot connect to JACK, refer to Professional audio/Examples#Advanced sound server setups after following the setup described here. Before installing and running JACK you should ensure it can access your audio device.

Is PulseAudio or something else grabbing my device?

If your audio device is not listed, it may be used by PulseAudio (which was probably installed as dependency of another application). Remove those alongside PulseAudio, if you are not intending to use Professional audio/Examples#PulseAudio+JACK in order to make PulseAudio release your audio device.

As JACK version 1 is planned to be "slowly phased out" [1], does not support Symmetric Multiprocessing (SMP), lacks D-Bus and systemd integration, you would want to use version 2 which is available as the jack2 package. If you are going to use a JACK control GUI or a systemd user service for starting the audio graph, also install jack2-dbus.

The article on JACK describes a GUI-based and a shell-based example setup as a point of reference for your own scenario. Parameter values of JACK are discussed in detail in the #JACK parameters section and may depend on other system factors covered by the #Optimizing system configuration section below.

The aim here is to find the best possible combination of buffer size and periods, given the hardware you have. Frames/Period = 256 is a sane starter. For onboard and USB devices, try Periods/Buffer = 3 before lowering both values. Commonly used values are: 256/3, 256/2, 128/3, 128/2.

Also, the sample rate must match the hardware sample rate. To check what sample and bit rates your device supports:

Replace card0 and codec#0 depending on what you have. You will be looking for rates or VRA in Extended ID. A common sample rate across many of today's devices is 48000 Hz. Others common rates include 44100 Hz, 96000 Hz and 192000 Hz.

Almost always, when recording or sequencing with external gear is concerned, realtime is a must. Also, you may like to set maximum priority (at least 10 lower than system limits defined in /etc/security/limits.d/99-realtime-privileges.conf; the highest is for the device itself).

Start jack with the options you just found out:

qjackctl, cadenceAUR, patchageAUR and studio-controls-gitAUR can all be used to as GUIs to monitor JACK's status and simplify its configuration.

JACK parameters are most significant for controlling the round-trip delay (RTD). In the context of this article that is the overall time it takes for an audio signal to be recorded, processed and played back. The next subsection deals with theoretical background on the sources of latency adding up to the RTD. If you are already familiar with that, you can go to #Measuring latency to verify your RTD or skip this section completely.

Consider a typical recording situation of a singer performance. The voice is being captured with a microphone as it propagates trough the air with the speed of sound. An analog-to-digital-conversion enables the electrical signal to be recorded by a computer for digital signal processing. Finally, a digital-to-analog conversion returns the signal to be played back at the singer's headphones for monitoring similar to stage monitor system usage.

In that voice recording situation there are five significant latency sources constructing the RTD and occuring in the following order:

The first and last latency source is hard to change as a particular distance is technically necessary to create an intended sound during recording or playback, respectively. Additionally, when using closer miking for capturing and headphones for monitoring both sound propagation latencies are typically within the range of a few microseconds which is not noticeable by humans. Thus, an objective for RTD minimization is to reduce the other sources of latency.

In theory JACK maintains a constant low latency by using fixed values (frames, periods, sample rate) for sampling and buffering of audio to be converted analog-to-digital and vice versa. The latency occurring in the capturing process is described by the following equation:

Lc: Capture latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), f: Sample rate in Hertz (Hz).

The playback latency is also employing the periods value:

Lp: Playback latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), p: Periods, f: Sample rate in Hertz (Hz).

As already stated before, the capabilities of the audio interface define working combinations. You have to trial and error to find a setup. Sure, it is a trade-off between xrun prevention and achieving low latency, but recent audio interfaces can be used at high sample rates (up to 192 kHz) to deal with that requirement. The audio flux of JACK clients in the digital domain is about zero and thus, negligible for latency measurements [2].

Once you have set up #JACK parameters you might want to verify the RTD described above. For example, using a frames or buffer size of n = 128, a periods value of p = 2, and a sample rate of f = 48000 results in a capture latency of about Lc = 2,666... ms and a playback latency of about Lp = 5,333... ms summing up to a total round-trip delay of RTD = 8 ms.

The jack_delay utility by Fons Adriaensen measures RTD by emitting test tones out a playback channel and capturing them again at a capture channel for measuring the phase differences to estimate the round-trip time the signal has taken through the whole chain. Use an appropriate cable to connect an input and output channel of your audio device or put a speaker close to a microphone as described by JACK Latency tests.

For example, running jack_delay for a JACK-only setup using a cable connection between the ports playback_1 and capture_1 (the description may differ depending on your hardware) to close the loop, as well as the values discussed before yields the following insights:

As the output indicates further optimization of JACK can be done by using the parameters -I 19 and -O 19 to compensate for the reported extra loopback latency in the chain:

This article or section needs expansion.

"Realtime" in the context of an operating system is defined that the results of a computation are available within a fixed period of time. Only in a broader sense does it mean "time running simultaneously with reality", for example, that a sound is produced immediately in response to musical user input. The latter is called "low latency" and its setup is one of the main goals of this article.

Since a while ago, the stock Linux kernel (with CONFIG_PREEMPT=y, default in Arch Linux vanilla kernel) has proven to be adequate for low latency operation. Latency in an operating system context is the time between the moment an interrupt occurs in hardware, and the moment the corresponding interrupt-thread gets running. Unfortunately, some device drivers can introduce higher latencies. So depending on your hardware, drivers, and requirements, you might want a kernel with hard realtime capabilities.

The RT_PREEMPT patch by Ingo Molnar and Thomas Gleixner is an interesting option for hard and firm realtime applications, reaching from professional audio to industrial control. Most audio-specific Linux distributions ships with this patch applied. A realtime-preemptible kernel will also make it possible to tweak priorities of IRQ handling threads and help ensure smooth audio almost regardless of the load.

Install either the linux-rt or linux-rt-lts package.

If you are going to compile your own kernel as a realtime kernel, remember that removing modules/options does not equate to a "leaner and meaner" kernel. It is true that the size of the kernel image is reduced, but in today's systems it is not as much of an issue as it was back in 1995.

In any way, you should also ensure that:

If you truly want a slim system, we suggest you go your own way and deploy one with static /devs. You should, however, set your CPU architecture. Selecting "Core 2 Duo" for appropriate hardware will allow for a good deal of optimisation, but not so much as you go down the scale.

General issue(s) with (realtime) kernels:

You may want to consider the following system optimizations:

You may also want to maximize the PCI latency timer of the PCI sound card and raise the latency timer of all other PCI peripherals (default is 64).

E.g. SOUND_CARD_PCI_ID=03:00.0.

The SOUND_CARD_PCI_ID can be obtained like so:

Arch Linux provides the package group pro-audio holding all relevant (semi-) professional applications. All applications in the pro-audio package group are JACK clients. Also lv2-plugins, ladspa-plugins, dssi-plugins, vst-plugins and clap-plugins are subgroups of the pro-audio group.

An overview and brief information on some applications is found in List of applications/Multimedia#Audio. Especially the categories Digital audio workstations, Audio effects and Music trackers, as well as Audio synthesis environments and Sound generators provide examples of pro audio software for recording, mixing, mastering, and sound design. Other categories include Scorewriters, Audio editors, Audio converters, and DJ software.

Packages not (yet) in the official repositories can be found in proaudio. Browse the list of packages to find the application you need or request packaging of your desired applications via GitHub.

The majority of sound cards and audio devices will work with no extra configuration or packages, simply set JACK to use the desired one.

This is not true for all devices, have a look at the Category:Sound, /Hardware as well as Envy24control#Supported cards for those special cases.

**Examples:**

Example 1 (unknown):
```unknown
$ speaker-test
```

Example 2 (unknown):
```unknown
#PipeWire-only       #PipeWire-as-JACK-Client       #JACK-only
┌──────────────┐          ┌──────────────┐        ┌──────────────┐
│ Applications │          │ Applications │        │ Applications │
├──────────────┤          ├──────────────┤        ├──────────────┤
│   PipeWire   │          │ PipeWire+JACK│        │     JACK     │
├──────────────┤          ├──────────────┤        ├──────────────┤
│     ALSA     │          │     ALSA     │        │     ALSA     │
└──────────────┘          └──────────────┘        └──────────────┘
```

Example 3 (unknown):
```unknown
$ lsof +c 0 /dev/snd/pcm* /dev/dsp*
```

Example 4 (unknown):
```unknown
$ fuser -fv /dev/snd/pcm* /dev/dsp*
```

---

## NVIDIA

**URL:** https://wiki.archlinux.org/title/NVIDIA

**Contents:**
- Installation
  - Custom kernel
  - DRM kernel mode setting
    - Early loading
      - pacman hook
  - Hardware accelerated video decoding
  - Hardware accelerated video encoding with NVENC
- Wayland configuration
  - Basic support
    - modeset

This article covers the official NVIDIA graphics card drivers. For the community open-source driver, see Nouveau. If you have a laptop with hybrid graphics, see also NVIDIA Optimus.

First, find the family of your card (e.g. NV110, NVC0, etc.) on nouveau wiki's code names page corresponding to its model/official name obtained with:

Then, install the appropriate driver for your card:

For 32-bit application support, also install the corresponding lib32 package from the multilib repository (e.g. lib32-nvidia-utils).

The nvidia-utils package contains a file which blacklists the nouveau module once you reboot. Optionally, you can also remove kms from the HOOKS array in /etc/mkinitcpio.conf and regenerate the initramfs. This will prevent the initramfs from containing the nouveau module making sure the kernel cannot load it during early boot.

Once the driver has been installed, continue to #Xorg configuration or #Wayland configuration.

Ensure your kernel has CONFIG_DRM_SIMPLEDRM=y, and if using CONFIG_DEBUG_INFO_BTF then this is needed in the PKGBUILD (since kernel 5.16):

If your kernel is compiled with CONFIG_NOVA_CORE enabled, you may need to prevent the new NVIDIA GPU driver Nova from loading. nvidia-utils adds it to the blacklist by default. You can check this by running systemd-analyze. If you have installed a different version of the driver, you may need to blacklist the nova_core and nova_drm modules manually.

Since NVIDIA does not support automatic KMS late loading, enabling DRM (Direct Rendering Manager) kernel mode setting is required to make Wayland compositors function properly.

Starting from nvidia-utils 560.35.03-5, DRM defaults to enabled.[1] For older drivers, set the modeset=1 kernel module parameter for the nvidia_drm module.

To verify that DRM is actually enabled, execute the following:

Which should now return Y, and not N.

For basic functionality, just adding the kernel parameter should suffice. If you want to ensure it is loaded as early as possible, or you are noticing startup issues (such as the nvidia kernel module being loaded after the display manager), you can add nvidia, nvidia_modeset, nvidia_uvm and nvidia_drm to the initramfs. See Kernel module#Early module loading to learn how to configure your initramfs generator. mkinitcpio users may also need to regenerate the initramfs image every time there is a nvidia driver update. See #pacman hook to automate these steps.

To avoid the possibility of forgetting to update initramfs after an NVIDIA driver upgrade, you may want to use a pacman hook:

Accelerated video decoding with VDPAU is supported on GeForce 8 series cards and newer. Accelerated video decoding with NVDEC is supported on Fermi (~400 series) cards and newer. See Hardware video acceleration for details.

NVENC requires the nvidia_uvm module and the creation of related device nodes under /dev.

The latest driver package provides a udev rule which creates device nodes automatically, so no further action is required.

If you are using an old driver (e.g. nvidia-340xx-dkmsAUR), you need to create device nodes. Invoking the nvidia-modprobe utility automatically creates them. You can create /etc/udev/rules.d/70-nvidia.rules to run it automatically:

Regarding Xwayland take a look at Wayland#Xwayland.

For further configuration options, take a look at the wiki pages or documentation of the respective compositor.

There are two kernel parameters for the nvidia_drm module to be considered: modeset and fbdev. Both are enabled by default when using the nvidia-utils package. NVIDIA also plans to enable them by default in a future release.

Enabling modeset is necessary for all Wayland configurations to function properly.

For unsupported drivers, where modeset needs to be enabled manually, see #DRM kernel mode setting, and Wayland#Requirements for more information.

This article or section is out of date.

Enabling fbdev is necessary for some Wayland configurations.

It is specifically a hard requirement on Linux 6.11 and later, but it is currently unclear whether this is intended behavior or a bug, see [2] for more details.

It can be set the same way as the modesetting parameter, with the difference that executing:

Will return a missing file error if it is not set at all, instead of N.

Wayland suspend can suffer from the defaults more than X does, see /Tips and tricks#Preserve video memory after suspend for details.

If you use GDM, also see GDM#Wayland and the proprietary NVIDIA driver.

Some wayland compositors will consume a large quantity of VRAM by default if the GLVidHeapReuseRatio application profile key is not applied against their process name. For example, niri users can free up to ~2.5GiB of idle vram consumption with the following:

The proprietary NVIDIA graphics card driver does not need any Xorg server configuration file. You can start X to see if the Xorg server will function correctly without a configuration file. However, it may be required to create a configuration file (prefer /etc/X11/xorg.conf.d/20-nvidia.conf over /etc/X11/xorg.conf) in order to adjust various settings. This configuration can be generated by the NVIDIA Xorg configuration tool, or it can be created manually. If created manually, it can be a minimal configuration (in the sense that it will only pass the basic options to the Xorg server), or it can include a number of settings that can bypass Xorg's auto-discovered or pre-configured options.

The NVIDIA package includes an automatic configuration tool to create an Xorg server configuration file (xorg.conf) and can be run by:

This command will auto-detect and create (or edit, if already present) the /etc/X11/xorg.conf configuration according to present hardware.

Double-check your /etc/X11/xorg.conf to make sure your default depth, horizontal sync, vertical refresh, and resolutions are acceptable.

The nvidia-settings tool lets you configure many options using either CLI or GUI. Running nvidia-settings without any options launches the GUI, for CLI options see nvidia-settings(1).

You can run the CLI/GUI as a non-root user and save the settings to ~/.nvidia-settings-rc by using the option Save Current Configuration under nvidia-settings Configuration tab.

To load the ~/.nvidia-settings-rc for the current user:

See Autostarting to start this command on every boot.

Several tweaks (which cannot be enabled automatically or with nvidia-settings) can be performed by editing your configuration file. The Xorg server will need to be restarted before any changes are applied.

See NVIDIA Accelerated Linux Graphics Driver README and Installation Guide for additional details and options.

A basic configuration block in 20-nvidia.conf (or deprecated in xorg.conf) would look like this:

If you are using an old driver (nvidia-340xx-dkmsAUR), you may want to disable the NVIDIA logo splash screen that is displayed at X startup. Add the "NoLogo" option under section Device:

The "ConnectedMonitor" option under section Device allows overriding monitor detection when X server starts, which may save a significant amount of time at start up. The available options are: "CRT" for analog connections, "DFP" for digital monitors and "TV" for televisions.

The following statement forces the NVIDIA driver to bypass startup checks and recognize the monitor as DFP:

This article or section is out of date.

Add to kernel parameters:

Alternatively, add the following under section Device:

If brightness control still does not work with this option, try installing nvidia-bl-dkmsAUR.

This article or section is out of date.

Taken from the NVIDIA driver's README Appendix B: This option controls the configuration of SLI rendering in supported configurations. A "supported configuration" is a computer equipped with an SLI-Certified Motherboard and 2 or 3 SLI-Certified GeForce GPUs.

Find the first GPU's PCI Bus ID using lspci:

Add the BusID (3 in the previous example) under section Device:

Add the desired SLI rendering mode value under section Screen:

The following table presents the available rendering modes.

Alternatively, you can use the nvidia-xconfig utility to insert these changes into xorg.conf with a single command:

To verify that SLI mode is enabled from a shell:

If this configuration does not work, you may need to use the PCI Bus ID provided by nvidia-settings,

and comment out the PrimaryGPU option in your xorg.d configuration,

Using this configuration may also solve any graphical boot issues.

See Multihead for more general information.

The nvidia-settings tool can configure multiple monitors.

For CLI configuration, first get the CurrentMetaMode by running:

Save everything after the :: to the end of the attribute (in this case: DPY-1: 2880x1620 @2880x1620 +0+0 {ViewPortIn=2880x1620, ViewPortOut=2880x1620+0+0}) and use to reconfigure your displays with nvidia-settings --assign "CurrentMetaMode=your_meta_mode".

This article or section is out of date.

If the driver does not properly detect a second monitor, you can force it to do so with ConnectedMonitor.

The duplicated device with Screen is how you get X to use two monitors on one card without TwinView. Note that nvidia-settings will strip out any ConnectedMonitor options you have added.

This article or section is out of date.

You want only one big screen instead of two. Set the TwinView argument to 1. This option should be used if you desire compositing. TwinView only works on a per-card basis, when all participating monitors are connected to the same card.

Example configuration:

Device option information.

If you have multiple cards that are SLI capable, it is possible to run more than one monitor attached to separate cards (for example: two cards in SLI with one monitor attached to each). The "MetaModes" option in conjunction with SLI Mosaic mode enables this. Below is a configuration which works for the aforementioned example and runs GNOME flawlessly.

If you are using TwinView and vertical sync (the Sync to VBlank option in nvidia-settings), you will notice that only one screen is being properly synced, unless you have two identical monitors. Although nvidia-settings does offer an option to change which screen is being synced (the Sync to this display device option), this does not always work. A solution is to add the following environment variables at startup, for example append in /etc/profile:

You can change DFP-0 with your preferred screen (DFP-0 is the DVI port and CRT-0 is the VGA port). You can find the identifier for your display from nvidia-settings in the X Server XVideoSettings section.

In case you want to play full-screen games when using TwinView, you will notice that games recognize the two screens as being one big screen. While this is technically correct (the virtual X screen really is the size of your screens combined), you probably do not want to play on both screens at the same time.

To correct this behavior for SDL 1.2, try:

For OpenGL, add the appropriate Metamodes to your xorg.conf in section Device and restart X:

Another method that may either work alone or in conjunction with those mentioned above is starting games in a separate X server.

Mosaic mode is the only way to use more than 2 monitors across multiple graphics cards with compositing. Your window manager may or may not recognize the distinction between each monitor. Mosaic mode requires a valid SLI configuration. Even if using Base mode without SLI, the GPUs must still be SLI capable/compatible.

Base Mosaic mode works on any set of Geforce 8000 series or higher GPUs. It cannot be enabled from within the nvidia-setting GUI. You must either use the nvidia-xconfig command line program or edit xorg.conf by hand. Metamodes must be specified. The following is an example for four DFPs in a 2x2 configuration, each running at 1920x1024, with two DFPs connected to two cards:

If you have an SLI configuration and each GPU is a Quadro FX 5800, Quadro Fermi or newer, then you can use SLI Mosaic mode. It can be enabled from within the nvidia-settings GUI or from the command line with:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

For systems with NVswitch, like H100x8 on AWS, the following is need.

With the fabricmanager, pytorch would report no GPU is found.

To install the fabric manager:

To get the matching kernel driver:

finally, systemctl enable nvidia-fabricmanager and systemctl start nvidia-fabricmanager, then pytorch should work.

See NVIDIA/Tips and tricks.

See NVIDIA/Troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -k -d ::03xx
```

Example 2 (unknown):
```unknown
NVreg_EnableGpuFirmware=0
```

Example 3 (unknown):
```unknown
/etc/mkinitcpio.conf
```

Example 4 (unknown):
```unknown
CONFIG_DRM_SIMPLEDRM=y
```

---

## Laptop/Framework

**URL:** https://wiki.archlinux.org/title/Laptop/Framework

**Contents:**
- Laptop 13
- Laptop 16
- Laptop 12
- Expansion Cards

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

**Examples:**

Example 1 (unknown):
```unknown
MODULES=(pinctrl_tigerlake soc_button_array)
```

Example 2 (unknown):
```unknown
/etc/mkinitcpio.d/99-framework-12.conf
```

---

## NVIDIA/Troubleshooting

**URL:** https://wiki.archlinux.org/title/NVIDIA/Troubleshooting

**Contents:**
- Failure to start
  - System will not boot after driver was installed
  - Xorg fails to load or Red Screen of Death
  - Black screen at X startup / Machine poweroff at X shutdown
  - Screen(s) found, but none have a usable configuration
  - X fails with "Failing initialization of X screen"
  - Xorg fails during boot, but otherwise starts fine
  - Black screen on systems with integrated GPU
  - X fails with "no screens found" when using Multiple GPUs
  - Modprobe Error: "Could not insert 'nvidia': No such device" on linux >=4.8

If after installing the NVIDIA driver your system becomes stuck before reaching the display manager, try to disable kernel mode setting.

If you get a red screen and use GRUB, disable the GRUB framebuffer by editing /etc/default/grub and uncomment GRUB_TERMINAL_OUTPUT=console. For more information see GRUB/Tips and tricks#Disable framebuffer.

If you have installed an update of NVIDIA and your screen stays black after launching Xorg, or if shutting down Xorg causes a machine poweroff, try the below workarounds:

Sometimes NVIDIA and X have trouble finding the active screen. If your graphics card has multiple outputs try plugging your monitor into the other ones. On a laptop it may be because your graphics card has VGA/TV out. Xorg.0.log will provide more info.

Another thing to try is adding an invalid Option "ConnectedMonitor" to Section "Device" to force Xorg throw an error and show you how to correct it. See the documentation for more information about the ConnectedMonitor setting.

After re-run X see Xorg.0.log to get valid CRT-x,DFP-x,TV-x values.

nvidia-xconfig --query-gpu-info could be helpful.

If /var/log/Xorg.0.log says X server fails to initialize screen

and nvidia-smi says No running processes found

The solution is at first reinstall latest nvidia-utils, and then copy /usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf to /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf, and then edit /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf and add the line Option "PrimaryGPU" "yes". Restart the computer. The problem will be fixed.

On very fast booting systems, systemd may attempt to start the display manager before the NVIDIA driver has fully initialized. You will see a message like the following in your logs only when Xorg runs during boot.

In this case you will need to establish an ordering dependency from the display manager to the DRI device. First create device units for DRI devices by creating a new udev rules file.

Then create dependencies from the display manager to the device(s).

If you have additional cards needed for the desktop then list them in Wants and After seperated by spaces.

If you have a system with an integrated GPU (e.g. Intel HD 4000, VIA VX820 Chrome 9 or AMD Cezanne) and have installed the nvidia package, you may experience a black screen on boot, when changing virtual terminal, or when exiting an X session. This may be caused by a conflict between the graphics modules. This is solved by blacklisting the relevant GPU modules. Create the file /etc/modprobe.d/blacklist.conf and prevent the relevant modules from loading on boot:

In situations where you might have multiple GPUs on a system and X fails to start with:

then you need to add your discrete card's BusID to your X configuration. This can happen on systems with an Intel CPU and an integrated GPU or if you have more than one NVIDIA card connected. Find your BusID:

Then you fix it by adding it to the card's Device section in your X configuration. In my case:

In the example above 01:00.0 is stripped to be written as 1:0:0, however some conversions can be more complicated. lspci output is in hex format, but in configuration files the BusID's are in decimal format! This means that in cases where the BusID is greater than 9 you will need to convert it to decimal!

ie: 5e:00.0 from lspci becomes PCI:94:0:0.

With linux 4.8, one can get the following errors when trying to use the discrete card:

This problem is caused by bad commits pertaining to PCIe power management in the Linux Kernel (as documented in this NVIDIA DevTalk thread).

The workaround is to add pcie_port_pm=off to your kernel parameters. Note that this disables PCIe power management for all devices.

What you see in the log:

A possible solution based on [1]:

Run this command to get the version string:

Add the acpi_osi=! "acpi_osi=version" kernel parameter to your boot loader configuration.

Another possible cause to the issue could be the use of the nvidia-open package, as described here:

If experiencing black screen issues and logs containing:

You need to enable the NVIDIA suspend, hibernate and sleep services as explained in NVIDIA/Tips and tricks#Preserve video memory after suspend.

This bug is present only for new games that depend on them, like Final Fantasy VII Rebirth. This is reflected in the absence of environments when using NVIDIA GPUs even with latest beta drivers. [2]

However, pyroveil, recently developed, allows you to get around the problem with SPIR-V, while waiting for a fix from NVIDIA.

You need to compile and install the tool by following the tutorial on GitHub, then run the game with the PYROVEIL=1 and PYROVEIL_CONFIG=/path/to/pyroveil/hacks/ffvii-rebirth-nvidia/pyroveil.json environment variables.

If you are using a recent CPU (Intel Sandy Bridge (2011) and later or AMD Zen (2017) and later) it has a micro operations cache. Using a micro op cache can lead to problems with NVIDIA's driver in OpenGL due to Cache Aliasing [3]. You usually are able to disable the micro op cache in your systems BIOS, but this comes at the cost of performance [4]. Disabling the micro op cache also helps with the most severe graphical glitches in Xwayland applications, although it does not solve the problem fully [5].

This is a known bug that is present in the NVIDIA 550 series drivers. [6] As of yet the cause is unknown however it only appears to affect laptops. See BBS#293400 for more details.

To workaround this issue, switch to nvidia-open-dkms if supported by the hardware, otherwise use nvidia-535xx-dkmsAUR instead.

The use of the GSP firmware, enabled by default since version 555 of the NVIDIA driver released in June 2024, is known to cause a range of issues including Vulkan failures and system crashes.

To disable it, use the NVreg_EnableGpuFirmware=0 module parameter for the nvidia kernel module. This only works with the proprietary NVIDIA driver: see NVIDIA#Installation if switching from the open source driver.

Do not forget to regenerate the initramfs if needed. To have this new kernel module option take effect, reboot.

Tearing can be avoided by forcing a full composition pipeline, regardless of the compositor you are using. To test whether this option will work, run:

Or click on the Advanced button that is available on the X Server Display Configuration menu option. Select either Force Composition Pipeline or Force Full Composition Pipeline and click on Apply.

In order to make the change permanent, it must be added to the "Screen" section of the Xorg configuration file. When making this change, TripleBuffering should be enabled and AllowIndirectGLXProtocol should be disabled in the driver configuration as well. See example configuration below:

If you do not have an Xorg configuration file, you can create one for your present hardware using nvidia-xconfig (see NVIDIA#Automatic configuration) and move it from /etc/X11/xorg.conf to the preferred location /etc/X11/xorg.conf.d/20-nvidia.conf.

For multi-monitor setup you will need to specify ForceCompositionPipeline=On for each display. For example:

Without doing this, the nvidia-settings command will disable your secondary display.

You can get the current screen names and offsets using --query:

The above line is for two 3840x2160 monitors connected to DP-2 and DP-4. You will need to read the correct CurrentMetaMode by exporting xorg.conf and append ForceCompositionPipeline to each of your displays. Setting ForceCompositionPipeline only affects the targeted display.

This also applies if an external monitor does not wake up after suspend or hibernation.

See NVIDIA/Tips and tricks#Preserve video memory after suspend

A corruption after suspend bug when using GDM service was solved as of driver version 515.43.04 [7].

For some users, using GeForce GT 100M's, the screen gets corrupted after X starts, divided into 6 sections with a resolution limited to 640x480. The same problem has been reported with Quadro 2000 and hi-res displays.

To solve this problem, enable the Validation Mode NoTotalSizeCheck in section Device:

An update of GTK4 brought an issue for users relying on the nvidia-470 driver for legacy cards. After the update text and icons randomly disappear and re-appear only after hovering with the mouse over the windows.[8]

See the forum for work-arounds.

If you are facing strange fonts and/or having weird graphical glitches in GNOME Shell when resuming from sleep, try setting the following kernel parameter to enable power management:

More info: https://download.nvidia.com/XFree86/Linux-x86_64/575.64/README/dynamicpowermanagement.html

If the system freezes or crashes right after the desktop environment turns off the display (DPMS) or when resuming from suspend, and dmesg/journal shows a GSP timeout like:

the GPU may be dropping to an unstable low clock state during these power transitions.

Workaround: lock a higher minimum GPU/memory clock with nvidia-smi.

Enable/start the nvidia-persistenced.service.

Find supported clock values (use these to pick valid min/max pairs):

Set minimum clocks (example values; adjust to your GPU’s max supported clocks):

Permanent configuration (systemd) Create a unit such as nvidia-clocks.service:

You can adjust the minimum clock so they are lower than the 800 mentioned earlier to lower idle power consumption; just be aware that setting them to low will cause the issue to occur again.

Then enable/start nvidia-clocks.service.

The factual accuracy of this article or section is disputed.

If FPS have dropped in comparison with older drivers, check if direct rendering is enabled (glxinfo is included in mesa-utils):

If the command prints:

A possible solution could be to regress to the previously installed driver version and rebooting afterwards.

The factual accuracy of this article or section is disputed.

A common issue with Mutter is that animations, video playback and gaming cause extreme desktop lag on Xorg.

See NVIDIA/Tips and tricks#Preserve video memory after suspend.

This should resolve this issue, however if it did not, you are most likely out of luck. One way you can remedy this issue is by adding these options:

turning Sync to VBlank and Allow flipping off within NVIDIA Settings, and configuring NVIDIA Settings to launch on startup using the flag --load-config-only. This will still result in a laggy desktop behavior, in particular on an eventual second (or third) monitor, but it should be much better.

If you are experiencing intermittent CPU spikes with a 400 series card, it may be caused by PowerMizer constantly changing the GPU's clock frequency. Switching PowerMizer's setting from Adaptive to Performance, add the following to the Device section of your Xorg configuration:

The factual accuracy of this article or section is disputed.

On executing an application that require Vulkan acceleration, if you get this error

try to delete the ~/.nv or ~/.cache/nvidia directory.

Sometimes NVIDIA HDMI audio devices are not shown when you do

On some new machines, the audio chip on the NVIDIA GPU is disabled at boot. Read more on NVIDIA's website and a forum post.

You need to reload the NVIDIA device with audio enabled. In order to do that make sure that your GPU is on (in case of laptops/Bumblebee) and that you are not running X on it, because it is going to reset:

If you are running your TTY on NVIDIA, put the lines in a script so you do not end up with no screen.

By default, DPMS should turn off backlight with the timeouts set or by running xset. However, probably due to a bug in the proprietary NVIDIA drivers the result is a blank screen with no powersaving whatsoever. To workaround it, until the bug has been fixed you can use the vbetool as root.

Install the vbetool package.

Turn off your screen on demand and then by pressing a random key backlight turns on again:

Alternatively, xrandr is able to disable and re-enable monitor outputs without requiring root.

This article or section needs expansion.

Proprietary driver 415 includes a new feature called HardDPMS. This is reported by some users to solve the issues with suspending monitors connected over DisplayPort. It is enabled by default since 440.26. If you are using an older driver, the HardDPMS option can be set in the Device or Screen sections. For example:

HardDPMS will trigger on screensaver settings like BlankTime. The following ServerFlags will set your monitor(s) to suspend after 10 minutes of inactivity:

If you are trying to configure a WQHD monitor such as DELL U2515H using xrandr and xrandr --addmode gives you the error X Error of failed request: BadMatch, it might be because the proprietary NVIDIA driver clips the pixel clock maximum frequency of HDMI output to 225 MHz or lower. To set the monitor to maximum resolution you have to install nouveau drivers. You can force nouveau to use a specific pixel clock frequency by setting nouveau.hdmimhz=297 (or 330) in your Kernel parameters.

Alternatively, it may be that your monitor's EDID is incorrect. See #Override EDID.

Another reason could be that by default current NVIDIA drivers will only allow modes explicitly reported by EDID, but sometimes refresh rates and/or resolutions are desired which are not reported by the monitor (although the EDID information is correct; it is just that current NVIDIA drivers are too restrictive).

If this happens, you may want to add an option to xorg.conf to allow non-EDID modes:

This can be set per-output. See README - Appendix B. X Config Options for more information.

See Kernel mode setting#Forcing modes and EDID, Xrandr#Troubleshooting and Qnix QX2710#Fixing X11 with Nvidia.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Workaround is to use nvidia-settings CLI to query and set certain variables after enabling overclocking (as explained in NVIDIA/Tips and tricks#Enabling overclocking in nvidia-settings, see nvidia-settings(1) for more information).

Example to query all variables:

Example to set PowerMizerMode to prefer performance mode:

Example to set fan speed to fixed 21%:

Example to set multiple variables at once (overclock GPU by 50MHz, overclock video memory by 50MHz, increase GPU voltage by 100mV):

If you are running Xorg as a non-root user and trying to overclock your NVIDIA GPU, you will get an error similar to this one:

To avoid this issue, Xorg has to be run as the root user. See Xorg#Rootless Xorg for details.

This article or section needs expansion.

If power save is configured on the kernel module:

The binary NVIDIA driver will not adhere to the Mesa environment variable LIBGL_ALWAYS_SOFTWARE=1 but you can direct libglvnd and EGL to use Mesa by setting the following environment variables:

which will result in the Mesa libgl being used for GLX and EGL and result in software GL to see whether a bug is related to the NVIDIA GL library.

Newer versions of the driver (after 550xx) seem to waste bandwidth on 8bpc outputs, likely pushing the signal above specification limits and the result is a failure to apply modes with higher refresh rates that otherwise would be within the specification of the output. Add nvidia-modeset.hdmi_deepcolor=0 to the kernel parameters or set the option via modprobe Notice that deep color will however be required for HDR monitors.

In some cases (like using a HDMI cable with a 1660 Super Graphics Card with 60hz), the driver seems to wrongly assume the color space for the output. This leads to the colors looking darker than normal. Because of there being no easy way to explicitly set the color space on Wayland, as a workaround you can add nvidia-modeset.debug_force_color_space=2 to the kernel parameters or set the option via modprobe.

**Examples:**

Example 1 (unknown):
```unknown
/etc/default/grub
```

Example 2 (unknown):
```unknown
GRUB_TERMINAL_OUTPUT=console
```

Example 3 (unknown):
```unknown
xrandr --auto
```

Example 4 (unknown):
```unknown
rcutree.gp_init_delay=1
```

---

## Laptop/Other

**URL:** https://wiki.archlinux.org/title/Laptop/Other

**Contents:**
- Avell
- Casper
- Chuwi
- Clevo
- Colorful
- Cube
- Eve/Dough
- Fujitsu
  - Suspend issue
- Gateway

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

dual accelerometer does not work*

The Fujitsu Lifebook U9311 and other Tiger Lake/Alder Lake Fujitsu laptops face a long-standing BIOS bug related to Intel graphics since 2021. See Fujitsu Lifebook U9311#Suspend.

Macro keys have to be defined using the windows application.

Default NVME drive (ESR512GTLG-E6GBTNB4) has a very fragile firmware. If issued any NVME or S.M.A.R.T command, all filesystems fail to mount. The only known fix is to reboot. Also does not support any kind of namespace manipulation.

**Examples:**

Example 1 (unknown):
```unknown
pnpacpi=off
```

Example 2 (unknown):
```unknown
11n_disable=1
```

Example 3 (unknown):
```unknown
bmc150_accel_i2c
```

Example 4 (unknown):
```unknown
serio_raw serio atkbd psmouse i8042
```

---

## Advanced Linux Sound Architecture/Troubleshooting

**URL:** https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture/Troubleshooting

**Contents:**
- Volume
  - Output is muted after reboot
  - Volume is too low
  - Volume is still too low
  - Random lack of sound on startup
- Microphone
  - No microphone input
  - Setting the default microphone/capture device
  - Internal microphone not working
- Audio quality

The alsa-utils package contains the alsa-info.sh script, which can be used to gather detailed data on the ALSA state.

See also SoundcardTesting.

Run the following command:

If the problem persists, verify that the Auto-Mute option in alsamixer(1) is set to Disabled.

Run alsamixer and try to increase the value of the sliders, unmuting channels if necessary. Note that if you have many sliders, you may have to scroll to the right to see any missing sliders.

If all the sliders are maxed out, and the volume is still too low, you can try running the following script to reset your codec settings:

Close the analyzer, and when prompted as to whether you want to reset the codecs, say "yes".

If the volume is still too low, run alsamixer again: resetting the codecs may have caused new sliders to become enabled and some of them may be set to a low value.

If you are facing low volume even after maxing out your speakers/headphones, you can give the softvol plugin a try. Add the following to /etc/asound.conf:

After the changes are loaded successfully, you will see a Pre-Amp section in alsamixer. You can adjust the levels there.

You can quickly test sound by running speaker-test. If there is no sound, you may see something similar to:

If you have no sound on startup, this may be because your system has multiple sound cards, and their order may sometimes change on startup. If this is the case, try setting the default sound card.

If you use MPD and the above configuration tips do not work, try following https://mpd.wikia.com/wiki/Configuration#ALSA_MPD_software_volume_control.

In alsamixer(1), make sure that all the volume levels are up under recording, and that CAPTURE is toggled active on the microphone (e.g. Mic, Internal Mic) and/or on Capture (in alsamixer, select these items and press Space). Try making positive Mic Boost and raising Capture and Digital levels higher; this may make static or distortion, but then you can adjust them back down once you are hearing something when you record.

As the PulseAudio wrapper is shown as "default" in alsamixer, you may have to press F6 to select your actual sound card first. You may also need to enable and increase the volume of Line-in in the Playback section.

To test the microphone, run these commands (see arecord(1) for further information):

Alternatively, you can run this command:

alongside alsamixer to easily identify channel which you should select and unmute.

To test a particular device, use the --device parameter followed by the hardware PCM name in the form hw:C,D for card C device D, or plughw:C,D for plugged hardware. For instance:

If all fails, you may want to eliminate hardware failure by testing the microphone with a different device.

For at least some computers, muting a microphone (MM) simply means its input does not go immediately to the speakers. It still receives input.

Some programs use try to use OSS as the main input software. If you have enabled the snd_pcm_oss, snd_mixer_oss or snd_seq_oss kernel modules previously (they are not loaded by default), try unloading them.

Some applications (Pidgin, Adobe Flash) do not provide an option to change the capture device. It becomes a problem if your microphone is on a separate device (e.g. USB webcam or microphone) than your internal sound card. To change only the default capture device, leaving the default playback device as is, you can modify your ~/.asoundrc file to include the following:

Replace U0x46d0x81d with your capture device's card name in ALSA. You can use arecord -L to list all the capture devices detected by ALSA.

First make sure the volume is enabled under the Capture view in alsamixer. In some cases, the "Internal Microphone" is not displayed in the capture list available when pressing F4. If so, specifying the card number given by aplay -l to start alsamixer (for example alsamixer -c 0 ) can make it appear.

Following Advanced Linux Sound Architecture#Simultaneous output might lead to crackling sound through headphones or external speakers. This can be fixed by muting or setting the volume to 0% on Mic. Use alsamixer(1) or amixer(1):

You might hear a popping sound after resuming the computer from suspension. This can be fixed by editing /etc/pm/sleep.d/90alsa and removing the line that says aplay -d 1 /dev/zero

Run alsamixer, and if channels exist for nonexistent output devices then disable them (e.g. alsamixer showing a center speaker but you not having one).

If you experience poor sound quality, try setting the PCM volume (in alsamixer) to a level such that gain is 0.

If snd_usb_audio driver has been loaded, you could try to enable softvol:

Some modules (e.g. snd_hda_intel) can power off your sound card when it is not used. This might cause audible click noises—like a crack/pop/scratch—at each power-down/up depending on the device (sometimes even when moving the volume slider or opening and closing windows on some desktop environments).

For more information, see Power management#Audio and #Power saving.

For more information, see Module snd-hda-intel and the output of modinfo --field=parm snd_hda_intel | column --separator=':' --table.

Power saving is enabled by default and might cause the following issues:

To completely disable the power-saving mode for the snd_hda_intel module, use the following kernel module parameters:

A codec is a hardware component of an HD Audio sound card. One card might incorporate more than one codec, one codec might correspond to more than one ALSA device.

A codec slot is a number (it begins from zero) identifying the codec on a given sound card. You can get the codec slot number from /proc/asound/cardi/codec#s file and /sys/class/sound/hwCiDs/ directory names—here i is a card index, and s is a codec slot.

To disable a codec—and subsequently all of the related ALSA devices—use the probe_mask option of the snd_hda_intel module.

Wrong model autodetection might cause the following issues:

See HD-Audio Codec-Specific Models for possible model strings for a given sound card chip.

The sound card chip can be found in:

To force, use the model option of the snd_hda_intel module.

Whether Message Signaled Interrupts (MSI) should be enabled or not hardly depends on the hardware. In the case of wrong autodetection different kinds of bad things could happen:

To check the MSI capability status, run lspci -vv -nn -d ::0403 with root user privileges.

MSI on HD Audio cards are controlled by the enable_msi option of the snd_hda_intel module.

Click noises (crackling, popping) on input and/or output of an HD Audio card might be caused by DMA position problem. Try to change the position_fix option of the snd_hda_intel module.

If the mappings to your audio pins(plugs) do not correspond but ALSA works fine, you could try HDA Analyzer -- a pyGTK2 GUI for HD-audio control can be found at the ALSA wiki. Try tweaking the Widget Control section of the PIN nodes, to make microphones IN and headphone jacks OUT. Referring to the Config Defaults heading is a good idea.

Check the contents of /proc/asound/cardC/pcmPp/subS/hw_params, where C, P, and S are system dependent. In order to find this file, execute the following command chain while outputting something via ALSA:

Here is an example output for audio with a bit depth of 24 bits and a sampling frequency of 44.1 kilohertz:

For more information see the Proc asound documentation.

S/PDIF (IEC958) utilizes two modes:

ALSA should detect appropriate mode automatically, but if it fails, you can force the mode with iecset(1) (on—audio, off—non-audio):

For more information, see DigitalOut.

This article or section is a candidate for merging with ALSA.

The procedure described below can be used to test HDMI audio. Before proceeding, make sure you have enabled and unmuted the output with alsamixer.

Connect your PC to the Display via HDMI cable and enable the display with xrandr.

Use aplay -l to discover the card and device number. For example:

Send sound to the device. Following the example in the previous step, you would send sound to card 1, device 3:

If aplay does not output any errors, but still no sound is heard, "reboot" the receiver, monitor or tv set. Since the HDMI interface executes a handshake on connection, it might have noticed before that there was no audio stream embedded, and disabled audio decoding. If you are using a standalone window manager, you may need to have sound playing while plugging in the HDMI cable.

mplay and other application could be configured to use special HDMI device as audio output. But flashplugin could only use default device. The following method is used to override default device. But you need to change it back when your TV is disconnected from HDMI port.

If the test is successful, create or edit your ~/.asoundrc file to set HDMI as the default audio device.

Or if the above configuration does not work try:

Or if you alternatively succeed with

for your HDMI or DisplayPort port the following configuration will work (successfully tested on Lenovo ThinkPad T430s):

Sound can be redirected to the intended speakers using ALSA's remap function.

If you get no sound using SDL based applications, try setting the environment variable SDL_AUDIODRIVER to alsa.

OpenAL defaults to PulseAudio. To instruct it to try ALSA first:

For other applications who insist on their own audio setup, e.g., XMMS or MPlayer, you would need to set their specific options.

For MPlayer or mpv, add the following line to the respective configuration file:

Eg. for XMMS2, go into their options and make sure the sound driver is set to ALSA, not oss.

For applications which do not provide a ALSA output, you can use aoss from the alsa-oss package. To use aoss, when you run the program, prefix it with aoss, e.g.:

pcm.!default{ ... } doesnt work for me anymore. but this does:

If you are having problems with simultaneous playback, and if PulseAudio is installed, its default configuration is set to "hijack" the soundcard. Some users of ALSA may not want to use PulseAudio and are quite content with their current ALSA settings. One fix is to edit /etc/asound.conf and comment out the following lines:

Commenting the following out also may help:

This may be a much simpler solution than completely uninstalling PulseAudio.

Effectively, here is an example of a working /etc/asound.conf:

The alsa-utils package provides alsa-store.service which automatically stores the current ALSA state to /var/lib/alsa/asound.state upon system shutdown. This can be problematic for users who are trying to reset their current ALSA state as the asound.state file will be recreated with the current state upon every shutdown (e.g., attempting to remove user-defined channels from the mixer). The alsa-store.service service may be temporarily disabled by creating the following empty file:

The presence of state-daemon.conf prevents alsa-store.service from saving asound.state during shutdown. After disabling this service, the asound.state file may be removed as such:

After rebooting, the previous ALSA state should be lost and the current state should be reset to defaults. Re-enable alsa-store.service by deleting the condition file we created:

On the next shutdown, the asound.state file should be recreated with ALSA defaults. The file may also be generated immediately using:

If you want to clean ALSA state without rebooting, you can use rmmod to remove the sound driver module, then manually delete the unwanted entries in asound.state, and then use modprobe to reinstall the sound driver module.

You might find that only one user can use the dmixer at a time. This is probably ok for most, but for those who run mpd as a separate user this poses a problem. When mpd is playing a normal user cannot play sounds though the dmixer. While it is quite possible to just run mpd under a user's login account, another solution has been found. Adding the line ipc_key_add_uid 0 to the pcm.dmixer block disables this locking. The following is a snippet from asound.conf, the rest is the same as above.

Check if you have i8kutilsAUR installed and if anything (e.g. i8kmon.service) is reading or writing to the interface exposed by the module, as i8kutils BIOS system calls block the kernel for a moment on some systems. See warning in Fan speed control#Dell laptops for more details.

**Examples:**

Example 1 (unknown):
```unknown
alsa-info.sh
```

Example 2 (unknown):
```unknown
# alsactl restore
```

Example 3 (unknown):
```unknown
$ wget -O hda-analyzer.py https://git.alsa-project.org/?p=alsa.git;a=blob_plain;f=hda-analyzer/run.py
```

Example 4 (unknown):
```unknown
/etc/asound.conf
```

---

## Professional audio

**URL:** https://wiki.archlinux.org/title/Pro-audio

**Contents:**
- Getting started
- Choosing a sound server
  - PipeWire-only
  - PipeWire-as-JACK-Client
  - JACK-only
- JACK parameters
- Latency verification
  - Latency sources
  - Conversion latency
  - Measuring latency

This article describes how to configure your system for multitrack recording, mixing and playing back audio as well as using it to synthesize and generate sounds. Those activities are subsumed under the term professional audio (pro audio) and typically require low latency performance.

Most applications do not need as much high-end hardware, compared to video production or gaming. For more information, refer to The Right Computer System for Digital Audio.

Advanced Linux Sound Architecture (ALSA) is part of the Linux kernel and used for drivers and low-level interface on Arch Linux as the default sound system. ALSA should work out of the box with a default Arch Linux installation. If this is not the case, you must solve the problem before going any further.

Have I set up sound properly?

A vanilla Arch Linux kernel is sufficient for low latency operation in most use cases. #Optimizing system configuration will be necessary only if you are experiencing audio drop-outs (also known as glitches) or if you need (or want) to reach ultra-low latency operations.

To finish with optimizations, these ultra low latency operations may require you to set up a #Realtime kernel.

Although some pro audio software can work with ALSA directly, most of the #Applications mentioned later are JACK Audio Connection Kit or JACK clients. Therefore, you will need to install and setup one of the available sound servers which are outlined soon.

Sound hardware cannot play back sound from more than one application simultaneously. While ALSA can theoretically be configured to mix applications in software this is typically left to a sound server.

As ALSA alone cannot achieve low latencies easily and cannot synchronise multiple audio applications to play on time, starting all at the same time, at the same tempo, etc., and as it can not share audio flux between applications simply by connecting all its clients together, you need not just any sound server, but professional audio class one:

The sound server setup strongly depends on the use case as well as on the workflow and capabilities of some application interaction. JACK was designed to share audio between applications and access an audio device simultaneously by providing the synchronous execution of clients while maintaining constant low latency. Its PipeWire replacement provides a sufficient server for most of the use cases.

This layout illustrates a layer model of the sound server setups to be discussed:

The newer PipeWire framework replaces JACK as well as other sound servers for the sake of simplicity. Thus, it is recommended to first go for a PipeWire-only setup implementing support for JACK clients by installing pipewire-jack and using the vanilla Arch Linux kernel.

For pro audio use, you also have to select the Pro Audio profile installing and using pavucontrol, PulseAudio's mixer.

PipeWire can also be used as a JACK client by installing pipewire-jack-client. This is explained in PipeWire#Run PipeWire on top of native JACK.

The principle of versatility allows you to employ JACK and the #Realtime kernel with #Optimizing system configuration to achieve low latencies for advanced use cases known as JACK-only setup. Using JACK as the only sound server requires any software, that is intended for interaction and audio device access, to run as a JACK client.

Unfortunately, popular desktop applications such as Firefox or most games either dropped JACK support or never implemented it. For that reason this setup should be used for a dedicated pro audio system where non-JACK software can be neglected. If you still need to use software that cannot connect to JACK, refer to Professional audio/Examples#Advanced sound server setups after following the setup described here. Before installing and running JACK you should ensure it can access your audio device.

Is PulseAudio or something else grabbing my device?

If your audio device is not listed, it may be used by PulseAudio (which was probably installed as dependency of another application). Remove those alongside PulseAudio, if you are not intending to use Professional audio/Examples#PulseAudio+JACK in order to make PulseAudio release your audio device.

As JACK version 1 is planned to be "slowly phased out" [1], does not support Symmetric Multiprocessing (SMP), lacks D-Bus and systemd integration, you would want to use version 2 which is available as the jack2 package. If you are going to use a JACK control GUI or a systemd user service for starting the audio graph, also install jack2-dbus.

The article on JACK describes a GUI-based and a shell-based example setup as a point of reference for your own scenario. Parameter values of JACK are discussed in detail in the #JACK parameters section and may depend on other system factors covered by the #Optimizing system configuration section below.

The aim here is to find the best possible combination of buffer size and periods, given the hardware you have. Frames/Period = 256 is a sane starter. For onboard and USB devices, try Periods/Buffer = 3 before lowering both values. Commonly used values are: 256/3, 256/2, 128/3, 128/2.

Also, the sample rate must match the hardware sample rate. To check what sample and bit rates your device supports:

Replace card0 and codec#0 depending on what you have. You will be looking for rates or VRA in Extended ID. A common sample rate across many of today's devices is 48000 Hz. Others common rates include 44100 Hz, 96000 Hz and 192000 Hz.

Almost always, when recording or sequencing with external gear is concerned, realtime is a must. Also, you may like to set maximum priority (at least 10 lower than system limits defined in /etc/security/limits.d/99-realtime-privileges.conf; the highest is for the device itself).

Start jack with the options you just found out:

qjackctl, cadenceAUR, patchageAUR and studio-controls-gitAUR can all be used to as GUIs to monitor JACK's status and simplify its configuration.

JACK parameters are most significant for controlling the round-trip delay (RTD). In the context of this article that is the overall time it takes for an audio signal to be recorded, processed and played back. The next subsection deals with theoretical background on the sources of latency adding up to the RTD. If you are already familiar with that, you can go to #Measuring latency to verify your RTD or skip this section completely.

Consider a typical recording situation of a singer performance. The voice is being captured with a microphone as it propagates trough the air with the speed of sound. An analog-to-digital-conversion enables the electrical signal to be recorded by a computer for digital signal processing. Finally, a digital-to-analog conversion returns the signal to be played back at the singer's headphones for monitoring similar to stage monitor system usage.

In that voice recording situation there are five significant latency sources constructing the RTD and occuring in the following order:

The first and last latency source is hard to change as a particular distance is technically necessary to create an intended sound during recording or playback, respectively. Additionally, when using closer miking for capturing and headphones for monitoring both sound propagation latencies are typically within the range of a few microseconds which is not noticeable by humans. Thus, an objective for RTD minimization is to reduce the other sources of latency.

In theory JACK maintains a constant low latency by using fixed values (frames, periods, sample rate) for sampling and buffering of audio to be converted analog-to-digital and vice versa. The latency occurring in the capturing process is described by the following equation:

Lc: Capture latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), f: Sample rate in Hertz (Hz).

The playback latency is also employing the periods value:

Lp: Playback latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), p: Periods, f: Sample rate in Hertz (Hz).

As already stated before, the capabilities of the audio interface define working combinations. You have to trial and error to find a setup. Sure, it is a trade-off between xrun prevention and achieving low latency, but recent audio interfaces can be used at high sample rates (up to 192 kHz) to deal with that requirement. The audio flux of JACK clients in the digital domain is about zero and thus, negligible for latency measurements [2].

Once you have set up #JACK parameters you might want to verify the RTD described above. For example, using a frames or buffer size of n = 128, a periods value of p = 2, and a sample rate of f = 48000 results in a capture latency of about Lc = 2,666... ms and a playback latency of about Lp = 5,333... ms summing up to a total round-trip delay of RTD = 8 ms.

The jack_delay utility by Fons Adriaensen measures RTD by emitting test tones out a playback channel and capturing them again at a capture channel for measuring the phase differences to estimate the round-trip time the signal has taken through the whole chain. Use an appropriate cable to connect an input and output channel of your audio device or put a speaker close to a microphone as described by JACK Latency tests.

For example, running jack_delay for a JACK-only setup using a cable connection between the ports playback_1 and capture_1 (the description may differ depending on your hardware) to close the loop, as well as the values discussed before yields the following insights:

As the output indicates further optimization of JACK can be done by using the parameters -I 19 and -O 19 to compensate for the reported extra loopback latency in the chain:

This article or section needs expansion.

"Realtime" in the context of an operating system is defined that the results of a computation are available within a fixed period of time. Only in a broader sense does it mean "time running simultaneously with reality", for example, that a sound is produced immediately in response to musical user input. The latter is called "low latency" and its setup is one of the main goals of this article.

Since a while ago, the stock Linux kernel (with CONFIG_PREEMPT=y, default in Arch Linux vanilla kernel) has proven to be adequate for low latency operation. Latency in an operating system context is the time between the moment an interrupt occurs in hardware, and the moment the corresponding interrupt-thread gets running. Unfortunately, some device drivers can introduce higher latencies. So depending on your hardware, drivers, and requirements, you might want a kernel with hard realtime capabilities.

The RT_PREEMPT patch by Ingo Molnar and Thomas Gleixner is an interesting option for hard and firm realtime applications, reaching from professional audio to industrial control. Most audio-specific Linux distributions ships with this patch applied. A realtime-preemptible kernel will also make it possible to tweak priorities of IRQ handling threads and help ensure smooth audio almost regardless of the load.

Install either the linux-rt or linux-rt-lts package.

If you are going to compile your own kernel as a realtime kernel, remember that removing modules/options does not equate to a "leaner and meaner" kernel. It is true that the size of the kernel image is reduced, but in today's systems it is not as much of an issue as it was back in 1995.

In any way, you should also ensure that:

If you truly want a slim system, we suggest you go your own way and deploy one with static /devs. You should, however, set your CPU architecture. Selecting "Core 2 Duo" for appropriate hardware will allow for a good deal of optimisation, but not so much as you go down the scale.

General issue(s) with (realtime) kernels:

You may want to consider the following system optimizations:

You may also want to maximize the PCI latency timer of the PCI sound card and raise the latency timer of all other PCI peripherals (default is 64).

E.g. SOUND_CARD_PCI_ID=03:00.0.

The SOUND_CARD_PCI_ID can be obtained like so:

Arch Linux provides the package group pro-audio holding all relevant (semi-) professional applications. All applications in the pro-audio package group are JACK clients. Also lv2-plugins, ladspa-plugins, dssi-plugins, vst-plugins and clap-plugins are subgroups of the pro-audio group.

An overview and brief information on some applications is found in List of applications/Multimedia#Audio. Especially the categories Digital audio workstations, Audio effects and Music trackers, as well as Audio synthesis environments and Sound generators provide examples of pro audio software for recording, mixing, mastering, and sound design. Other categories include Scorewriters, Audio editors, Audio converters, and DJ software.

Packages not (yet) in the official repositories can be found in proaudio. Browse the list of packages to find the application you need or request packaging of your desired applications via GitHub.

The majority of sound cards and audio devices will work with no extra configuration or packages, simply set JACK to use the desired one.

This is not true for all devices, have a look at the Category:Sound, /Hardware as well as Envy24control#Supported cards for those special cases.

**Examples:**

Example 1 (unknown):
```unknown
$ speaker-test
```

Example 2 (unknown):
```unknown
#PipeWire-only       #PipeWire-as-JACK-Client       #JACK-only
┌──────────────┐          ┌──────────────┐        ┌──────────────┐
│ Applications │          │ Applications │        │ Applications │
├──────────────┤          ├──────────────┤        ├──────────────┤
│   PipeWire   │          │ PipeWire+JACK│        │     JACK     │
├──────────────┤          ├──────────────┤        ├──────────────┤
│     ALSA     │          │     ALSA     │        │     ALSA     │
└──────────────┘          └──────────────┘        └──────────────┘
```

Example 3 (unknown):
```unknown
$ lsof +c 0 /dev/snd/pcm* /dev/dsp*
```

Example 4 (unknown):
```unknown
$ fuser -fv /dev/snd/pcm* /dev/dsp*
```

---

## Laptop/ASUS

**URL:** https://wiki.archlinux.org/title/Laptop/ASUS

**Contents:**
- ASUS Linux
- Battery charge threshold
  - Include required module in initramfs
  - TLP
  - bat
  - GNOME extension
  - udev rule
  - Persist after hibernation
- Model list
  - Vivobook

See also Wikipedia:Asus.

Advanced power management (Laptop Power Profile selection, battery charge limit and Panel Overdrive) and many other functions from recent laptops need the ASUS Linux stack installed and running.

Kernel 5.4 brought the ability to set the battery charge threshold for some Asus laptops, by modifying the charge_control_end_threshold variable exposed under /sys/class/power_supply/BAT0/[1][2].

By default this value is set to 100 and reset on every power cycle[3].

The effect of its change can be demonstrated as follows:

To work around cases of configuration failing to apply at boot because the required asus_wmi kernel module has not yet been loaded[5], configure early module loading for it.

TLP gained with version 1.4 the ability to set battery charge thresholds for laptops other than Thinkpads: see upstream documentation and config example.

Another (more simple) way to force the charging threshold is by using bat-asus-battery-binAUR, which provides a bat-boot.service systemd service and an intuitive terminal interface to change the threshold by typing bat-asus-battery threshold value.

gnome-shell-extension-battery-health-charging-gitAUR is a GNOME extension that "provides a graphical user interface for setting a laptop’s charging limit (charging threshold) within a Gnome environment". It supports ASUS laptops and many other brands. See its official website for details and screenshots.

The battery's charge_control_end_threshold power supply class attribute does not initially exist. It is added to the sysfs(5) directory by the asus-nb-wmi kernel module. Create a udev rule for asus-nb-wmi to set the battery's charge threshold:

While this setting will persist after suspending to RAM, it will be reset when resuming from hibernation. In order to re-execute the service after hibernation, use one of the methods described in Power management/Suspend and hibernate#Sleep hooks.

If creating a script as described in Power management/Suspend and hibernate#Hooks in /usr/lib/systemd/system-sleep, use something similar to:

Do not forget to make the script executable.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Use the pcie_aspm=force and pcie_aspm.policy=powersupersave kernel module parameters along with a power management tool to match the battery life of this device when running Windows.

The Function keys default behavior is F1,F2,etc… and must be unset by using Fn+Esc to use alternative functions.

rog-control-centerAUR works great.

Add amd_iommu=off idle=nomwait amdgpu.gpu_recovery=1 to your kernel command line.

The factual accuracy of this article or section is disputed.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Some laptops with only an NVIDIA GPU and no integrated GPU may fail to resume properly from suspend, especially when the system only supports s2idle. To fix that enable S0ix support on NVIDIA Proprietary driver

You can check if S0ix is currently enabled for the NVIDIA GPU by running:

Look for this section:

Then S0ix is not currently active.

To enable S0ix support, ensure you're using NVIDIA driver version 515 or newer. Then, configure the kernel module option:

Create a modprobe configuration file:

Rebuild the initramfs:

After rebooting, re-check:

Confirm that the line now reads:

This indicates that S0ix is now active.

Additionally, enable NVIDIA suspend/resume services:

These services help properly transition the GPU into and out of low-power states during suspend/resume.

Boot with nouveau disabled: use nouveau.modset=0 on the kernel command line. Need to edit bumblebee service to boot : https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-450749984.

Some fixes are needed: see https://bugzilla.redhat.com/show_bug.cgi?id=1543769.

Regular "Blur" works fine.

No sound on the internal speakers or the headphones jack.

Sound works on displays over HDMI or USB-C, and on bluetooth headphones.

**Examples:**

Example 1 (unknown):
```unknown
charge_control_end_threshold
```

Example 2 (unknown):
```unknown
/sys/class/power_supply/BAT0/
```

Example 3 (unknown):
```unknown
$ cat /sys/class/power_supply/BAT0/status
Charging
$ cat /sys/class/power_supply/BAT0/capacity
74
# echo 60 > /sys/class/power_supply/BAT0/charge_control_end_threshold
$ cat /sys/class/power_supply/BAT0/status
Not charging
```

Example 4 (unknown):
```unknown
bat-boot.service
```

---

## Laptop/Sony

**URL:** https://wiki.archlinux.org/title/Laptop/Sony

**Contents:**
- Model list
- Troubleshooting

If you encounter issues with power management, in particular regarding suspend and hibernate, you might have to add the kernel parameter acpi_sleep=nonvs to your boot loader.

**Examples:**

Example 1 (unknown):
```unknown
config=NvBios=PLATFORM
```

Example 2 (unknown):
```unknown
/sys/devices/platform/sony-laptop
```

Example 3 (unknown):
```unknown
i8042.direct i8042.dumbkbd
```

Example 4 (unknown):
```unknown
acpi_backlight=video
```

---

## Display Power Management Signaling

**URL:** https://wiki.archlinux.org/title/Display_Power_Management_Signaling

**Contents:**
- Linux console
- Xorg
  - Configuration
  - Runtime settings
- See also

This article or section needs expansion.

VESA Display Power Management Signaling (DPMS) enables power saving behaviour of monitors when the computer is not in use. The time of inactivity before the monitor enters into a given saving power level—standby, suspend or off—can be set as described in DPMSSetTimeouts(3).

To alter the terminal, use the setterm command. Its syntax (where 0 disables):

Some commands just write the terminal sequences to the current terminal device, whether that be in screen, a remote ssh terminal, console mode, serial consoles, etc.

To see the escape codes used, pipe the output as follows:

To modify a specific terminal, redirect the escape codes to it (with write permission):

To fully disable DPMS and screen blanking on the X Window System, create configuration files:

If you simply want to adjust the delays, change the duration (in minutes):

It is possible to turn off your monitor with the xset command which is provided by the xorg-xset package.

To query the current settings:

See xset(1) for all available commands.

**Examples:**

Example 1 (unknown):
```unknown
$ setterm --blank [0-60|force|poke]
$ setterm --powersave [on|vsync|hsync|powerdown|off]
$ setterm --powerdown [0-60]
```

Example 2 (unknown):
```unknown
setterm --powerdown
```

Example 3 (unknown):
```unknown
APM_DISPLAY_BLANK
```

Example 4 (unknown):
```unknown
consoleblank
```

---

## Advanced Linux Sound Architecture

**URL:** https://wiki.archlinux.org/title/ALSA

**Contents:**
- Installation
  - Firmware
  - ALSA utilities
  - ALSA and systemd
  - User privileges
  - OSS emulation
- Unmuting the channels
  - Unmute with amixer
  - Unmute with alsamixer
  - Unmute 5.1/7.1 sound

The Advanced Linux Sound Architecture (ALSA) provides kernel driven sound card drivers. It replaces the original Open Sound System (OSS).

Besides the sound device drivers, ALSA also bundles a user space driven library for application developers. They can then use those ALSA drivers for high level API development. This enables direct (kernel) interaction with sound devices through ALSA libraries.

The ALSA drivers are part of the Linux kernel. The ALSA library (alsa-lib) is usually installed as a dependency. Therefore, manual installation is not necessary.

udev will automatically detect your hardware and select needed drivers at boot time, therefore, your sound should already be working.

However, your sound may be initially muted. If it is, see #Unmuting the channels.

The Sound Open Firmware (SOF) (sof-firmware) is usually required for laptops—they tend to utilize Cadence Tensilica Xtensa architecture DSPs, see the list of the supported platforms. In case of the missing firmware the journal will provide messages such as:

For more SOF troubleshooting information, see Overview of Intel hardware platforms.

The linux-firmware-cirrus package is needed for laptops with Cirrus Logic smart amplifiers. See also:

The linux-firmware-intel package is needed for some Intel audio devices.

The alsa-firmware package contains firmware that may be required for certain sound cards.

See also #Cards and modules and Linux firmware.

Install the alsa-utils package. This contains (among other utilities) the alsamixer(1) and amixer(1) utilities. amixer is a shell command to change audio settings, while alsamixer provides a more intuitive ncurses based interface for audio device configuration.

The alsa-utils package comes with systemd unit configuration files alsa-restore.service and alsa-state.service by default.

These are automatically installed and activated during installation (via package provided symlink to sound.target). The options are as follows:

Evidently, both methods are mutually exclusive. You can decide for one of the two approaches depending on your requirements. To edit these units, see systemd#Editing provided units. You can check their status using systemctl.

For further information, see alsactl(1).

Local users have permission to play audio and change mixer levels. To allow remote users to use ALSA, you need to add those users to the audio group.

OSS emulation is the ability to intercept OSS calls and reroute them through ALSA instead. This emulation layer is useful e.g. for legacy applications which try to open /dev/dsp and write sound data to them directly. Without OSS or the emulation library, /dev/dsp will be missing, and the application will not produce any sound.

If you want OSS applications to work with dmix, install the alsa-oss package as well.

Load the snd_pcm_oss and snd_seq_oss kernel modules. Configure them to load at boot.

By default, ALSA has all channels muted. Those have to be unmuted manually.

Unmuting the sound card's master volume can be done by using amixer:

Unmuting the sound card can be done using alsamixer:

The MM label below a channel indicates that the channel is muted, and OO indicates that it is open.

Scroll to the Master and PCM channels with the Left and Right keys and unmute them by pressing the m key.

Use the Up key to increase the volume and obtain a value of 0 dB gain. The gain can be found in the upper left next to the Item: field.

To get full 5.1 or 7.1 surround sound, you will likely need to unmute other channels such as Front, Surround, Center, LFE (subwoofer) and Side. (Those are channel names with Intel HD Audio; they may vary with different hardware)

To enable your microphone, switch to the Capture tab with F4 and enable a channel with Space. See /Troubleshooting#Microphone if microphone does not work.

Next, test to see if sound works:

Change -c to fit your speaker setup. Use -c 8 for 7.1, for instance:

If audio is being outputted to the wrong device, try manually specifying it with the argument -D.

-D accepts PCM channel names as values, which can be retrieved by running the following:

For more information, see Advanced Linux Sound Architecture - Driver Configuration guide.

To reload ALSA driver configuration you have to reload corresponding modules. Before doing this, all processes using the corresponding ALSA driver—such as PipeWire—must be stopped. To identify processes using sound device files, utilize fuser(1):

Run lspci -k -nn -d ::0403 to identify the modules in use for PCI devices.

Run lsusb --verbose --tree | grep --after-context=1 'Class=Audio' for USB devices.

Run lsmod | grep '^snd' to get a full list of loaded sound modules.

Run cat /proc/asound/cards to get the list of your sound cards with their corresponding indexes (card numbers).

Run cat /proc/asound/modules to get the card indexes with their corresponding module names.

If you want to change your sound card order (or if your sound card order changes on boot, and you want to make it permanent), reserve the index for the given driver with the slots option of the snd module. See also Kernel module#Setting module options.

The following sample assumes you want your USB sound card always be the first (i.e. with index 0), no matter when the module is loaded (e.g. the card could be unplugged on boot):

When a module name is prepended with an exclamation mark (!), the corresponding index will be given for any modules but that name. For example, reserve the first index (0) for any modules but snd_usb_audio to avoid USB sound cards from getting it:

You can also provide an index of -2 to instruct ALSA to never use a card as the primary one: negative value is interpreted as a bitmask of permissible indexes. The alternative to the previous sample using the index option of the specific module:

If several sound cards use the same module, and their order is always the same, you can change the order with just index option. The following sample assumes there are two audio cards using the HD Audio module (e.g. an integrated audio card and HDMI output of non-integrated video card), and you want to swap their indexes:

The slots option can be combined with the index one as long as they do not conflict:

To disable all cards controlled by a given kernel module, prevent the module from loading using install or module_blacklist approach.

To select which card should be disabled, use the enable option of a kernel module. For example, disable the second card operated by a module:

See also /Troubleshooting#Codec probing for an HD Audio card codec disabling.

The system configuration file is /etc/asound.conf, and the per-user configuration file is ~/.asoundrc.

The syntax of library configuration—i.e. whitespace, line continuation, comments, including configuration files, punctuators (separators), assignments, compound assignments, operation modes—is explained in Configuration files.

ALSA library configuration is loaded for each instance of the library, so to reload it, all you have to do is restart the programs that are using it.

For more information, see:

There are different operation modes for parsing nodes, the default mode is merge and create. If operation mode is either merge/create or merge, type checking is done. Only same type assignments can be merged, so strings cannot be merged with integers. Trying to define a simple assignment in default operation mode to a compound (and vice versa) will also not work.

Prefixes of operation modes:

Using override operation mode, when done correctly, is usually safe; however, one should bear in mind that there might be other necessary keys in a node for proper functioning.

Sometimes, it may be useful and even easier to read using nesting in configuration.

Assuming that "defaults" node is set in /usr/share/alsa/alsa.conf, where "defaults.pcm.card" and its "ctl" counterpart have assignment values "0" (type integer), user wants to set default pcm and control device to (third) sound card "2" or "SB" for an Azalia sound card.

Using double quotes here automatically sets values data type to string, so in the above example, setting defaults.pcm.!card "2" would result in retaining last default device, in this case card 0. Using double quotes for strings is not mandatory as long as no special characters are used, which ideally should never be the case. This may be irrelevant in other assignments.

Putting the previous example regarding defaults.pcm.card and defaults.pcm.device into practice, assuming we have 2 cards with index 0 and 1 respectively and wish to simply change the default card to index 1, would lead to the following configuration in /etc/asound.conf or the user-specific ~/.asoundrc to change both the playback and the mixer control card.

Probably, it is enough to set ALSA_CARD to the name of the device. First, get the names with aplay -l, then set ALSA_CARD to the name which comes after the colon and before the bracket; e.g. if you have

then set ALSA_CARD=HDMI.

Other variables are also checked in the default global configuration /usr/share/alsa/alsa.conf. By looking there for constructs of the form vars [ ... ], the following table emerges:

Alternatively, you can override the behavior in your own configuration file, preferably the global one (/etc/asound.conf). Add:

In this case as well, replace Audigy2 with the name of your device. You can get the names with aplay -l or you can also use PCMs like surround51. But if you need to use the microphone, it is a good idea to select full-duplex PCM as default.

Now, you can select the sound card when starting programs by just changing the environment variable ALSAPCM. It works fine for all programs that do not allow to select the card; for the others, ensure you keep the default card. For example, assuming you wrote a downmix PCM called mix51to20, you can use it with mplayer using the commandline ALSAPCM=mix51to20 mplayer example_6_channel.wav

First, you will have to find out the card and device id that you want to set as the default:

For example, the last entry in this list has the card index (card number) 2, card ID strings Audio and the device ID 0. To set this card as the default, you can either use the system-wide file /etc/asound.conf or the user-specific file ~/.asoundrc. You may have to create the file if it does not exist. Then insert the following options with the corresponding card.

It is recommended to use sound card ID strings instead of number references to overcome the boot order problem.

pcm.dmixer and pcm.dsnooper are spares for applications which does not support without mixing.

The factual accuracy of this article or section is disputed.

For example, chromium -alsa-output-device=pcm.dmixer -alsa-input-device=pcm.dsnooper enables mixing for Chromium tempolary.

The pcm options affect which card and device will be used for audio playback while the ctl option affects which card is used by control utilities like alsamixer.

The changes should take effect as soon as you (re-)start an application (e.g. MPlayer). You can also test with a command like aplay:

If you receive an error regarding your asound configuration, check the upstream documentation for possible changes to the configuration file format.

Install the alsa-plugins package if you need to enable #Upmixing, #Downmixing, #High quality resampling and other advanced features.

For more information, see PCM (digital audio) plugins.

Mixing enables multiple applications to output sound at the same time. Most discrete sound cards support hardware mixing, which is enabled by default if available. Integrated motherboard sound cards (such as Intel HD Audio), usually do not support hardware mixing. On such cards, software mixing is done by an ALSA plugin called dmix. This feature is enabled automatically if hardware mixing is unavailable.

To manually enable dmix, add the following to your ALSA configuration file:

In order for stereo sources like music to be able to saturate a 5.1 or 7.1 sound system, you need to use upmixing. In darker days, this used to be tricky and error prone, but nowadays, plugins exist to easily take care of this task. We will use the upmix plugin, included in the alsa-plugins package.

Then add the following to your ALSA configuration file of choice (either /etc/asound.conf or ~/.asoundrc):

You can easily change this example for 7.1 upmixing to 5.1 or 4.0.

The following example adds a new PCM channel that you can use for upmixing. If you want all sound sources to go through this channel, add it as a default below the previous definition like so:

The plugin automatically allows multiple sources to play through it without problems so setting is as a default is actually a safe choice. If this is not working, you have to setup your own dmixer for the upmixing PCM like this:

and use "dmix6" instead of "surround71". If you experience skipping or distorted sound, consider increasing the buffer_size (to 32768, for example) or use a high quality resampler.

If you want to downmix sources to stereo because you, for instance, want to watch a movie with 5.1 sound on a stereo system, use the vdownmix plugin, included in the alsa-plugins package.

Again, in your configuration file, add this:

mbeq is part of Steve Harris' LADSPA plugin suite.

Install the alsa-plugins, ladspa and swh-plugins packages if you do not already have them.

If you have not already created either an ~/.asoundrc or a /etc/asound.conf file, then create either one and insert the following:

Install the alsaequalAUR package.

After installing the package, add the following to your ALSA configuration file:

To change your equalizer settings, run

Note that the equalizer configuration is different for each user (until not specified else). It is saved in ~/.alsaequal.bin. So if you want to use ALSAEqual with mpd or another software running under different user, you can configure it using

or for example, you can make a symlink to your .alsaequal.bin in their home directory.

If you wish to apply an equalizer to a specific output device only (for example your speakers connected to the S/PDIF output, but not your headphones connected to the headphone jack), but also want be able to output from multiple applications and to both output devices simultaneously, you need to create two dmix devices that feed into their respective devices (slave.pcm) directly. The following works for stereo output and maintains a regular stereo input, applying the equalizer to the S/PDIF output only.

Install the alsaequal-mgrAUR package.

Configure the equalizer as usual with

When you are satisfied with the state, you may give it a name (foo in this example) and save it:

The state "foo" can then be restored at a later time with

This, however, only restores ~/.alsaequal.bin. You then have to update the equalizer by alsamixer -D equal.

You can thus create different equalizer states for games, movies, music genres, VoIP apps, etc. and reload them as necessary.

See the project page and the help message for more options.

When #Software mixing is enabled, ALSA is forced to resample everything to the same frequency (48 kHz by default when supported). By default, it will try to use the speexrate converter to do so, and fallback to low-quality linear interpolation if it is not available. Thus, if you are getting poor sound quality due to bad resampling, the problem can be solved by simply installing the alsa-plugins package.

For even higher quality resampling, you can change the default rate converter to speexrate_medium or speexrate_best. Both perform well enough that in practice it does not matter which one you choose, so using the best converter is usually not worth the extra CPU cycles it requires.

To change the default converter, place the following contents in your ~/.asoundrc or /etc/asound.conf:

Auto-Mute Mode can be configured on startup with amixer. For example, to disable it:

Alternatively, the ncurses based interface can be utilized through alsamixer. In order to save any modifications, use:

See also #ALSA and systemd.

See Writing Udev rules for ALSA.

You might want to play music via external speakers connected via mini jack and internal speakers simultaneously. This can be done by unmuting Auto-Mute item using alsamixer or amixer:

and then unmuting other required items, such as Headphones, Speaker, Bass Speaker...

Map the following commands to your volume keys: XF86AudioRaiseVolume, XF86AudioLowerVolume, XF86AudioMute.

To toggle mute/unmute of the volume:

You might want a jack alternative to create a virtual recording or play device in order to mix different sources, using the snd_aloop module:

List your new virtual devices using:

now you can for example using ffmpeg:

In the hw:R,W,N phrase, R is your virtual card device number. W should be set to 1 for recording devices, or 0 for playing. N is your sub device. You can use all the virtual devices available and play/stop using applications like mplayer:

Another thing you could do with this approach is using festival to generate a voice into a recording stream using a script like this:

The alsa-tools package contains the hdajackretask tool, which can be used (on Intel HDA cards) to reconfigure the sound card input/output ports; for instance, to turn a microphone jack into a headphone jack.

apulseAUR provides an alternative partial implementation of the PulseAudio API. It lets you use ALSA for applications that support only PulseAudio for sound. Usage is simply:

**Examples:**

Example 1 (unknown):
```unknown
error: sof firmware file is missing
error: failed to load DSP firmware -2
error: sof_probe_work failed err: -2
```

Example 2 (unknown):
```unknown
alsa-restore.service
```

Example 3 (unknown):
```unknown
alsa-state.service
```

Example 4 (unknown):
```unknown
alsa-restore.service
```

---

## Dell XPS 15 (9560)

**URL:** https://wiki.archlinux.org/title/Dell_XPS_15_(9560)

**Contents:**
- Installation
- Power management
  - Suspend and hibernate
  - Fan and temperature monitoring and control
  - Sensor kernel module and configuration
- Power saving
  - Disable discrete GPU
    - bbswitch method
    - acpi_call method
  - Standard power saving configuration

This article or section does not follow the Laptop page guidelines.

This page contains recommendations for running Arch Linux on the Dell XPS 15 9560 (late 2016). With some configuration almost all the hardware is well-supported. Exceptions are the fingerprint reader, occasional locks on resuming from suspend experienced by some users, and the lack of support for PRIME render offload to the discrete GPU in the NVIDIA proprietary driver.

Before installing, it is necessary to modify some UEFI Settings. They can be accessed by pressing the F2 key repeatedly when booting.

Installation of Arch Linux can proceed normally. Refer to the Installation guide for more information.

Suspend and hibernate work out of the box, although some users have reported occasional system hangs on resuming from suspend, more commonly on kernels since 4.10.

The suspend function key is not printed on the keyboard, but it is actually mapped to Fn+Insert.

Many of the thermometers can be read with lm_sensors.

Fan speeds can be monitored with i8kctl from i8kutils-gitAUR. This laptop is not in the supported list so it is necessary to load the i8k kernel module with the force=1 module option. See Kernel modules#Setting module options. It is also possible to manually control fan speeds (at your own risk) however with manual control only a subset of the possible speeds are available (0rpm, 2500rpm, 4800rpm) instead of (0rpm, 2500rpm, 3200rpm, 3700rpm, 4800rpm, and 5100rpm) in the firmware's automatic control. See Fan speed control#Dell laptops.

The built-in fan modes can also be controlled directly by editing the setting in the bios. The libsmbios package provides many tools for reading and modifying certain settings on the computer. The smbios-thermal-ctl command can be used with the --set-thermal-mode flag to change the fan between modes performance, cool-bottom, quiet and balanced. For example:

this changes the fan mode to quiet, which makes the fan curve less aggressive.

The thermometer on the discrete NVIDIA GPU can be monitored with the nvidia-smi utility, which is part of nvidia-utils.

One avenue worth investigating is the use of the native kernel module dell-smm-hwmon:

If the module does not load, try the passing the option ignore_dmi=1 when running modprobe:

Upon successfully loading it you should see the following in your kernel logs and/or dmesg:

Now the sensors command should be able to display some useful data:

You can make these settings permanent by adding the following to /etc/modprobe.d/dell.conf:

And also by making the HWMON_MODULES variable appears like so in /etc/conf.d/lm_sensors:

The discrete NVIDIA GTX 1050 GPU is on by default and cannot be disabled in the UEFI settings. Even when idle, it uses a significant amount of power (about 7W). To disable it when not in use it is necessary to install bbswitch and bumblebee, add acpi_rev_override=1 to the kernel parameters, enable bumblebeed.service, and reboot (you may need to reboot twice for the firmware to notice acpi_rev_override).

An alternative set of steps, not requiring bbswitch or bumblebee is as follows:

It is a good idea to install a tool to tune common settings to save power. See Power management#Userspace tools.

Disabling the touchscreen can be done in the UEFI settings and results in significant power savings. If touchscreen is required it can be placed into autosuspend by TLP by adding 04f3:24a1 to USB_WHITELIST in tlp config file. The USB_AUTOSUSPEND must be set to 1 for this to have an effect. This will leave touchscreen enabled for usage and will consume much less battery.

Starting from linux 4.11, NVMe APST is supported and enabled by default, allowing NVMe SSDs to be switched to lower power states when idle, achieving significant power savings. See Solid state drive/NVMe#Allow drive to enter low-power states (APST). Depending on the specific SSD, it may also be necessary to adjust the default_ps_max_latency_us parameter to the nvme_core module in order to make ASPT work. This is necessary with the Toshiba THNSN5512GPUK for example.

Passing the following options to the i915 kernel module results in significant power savings: enable_fbc=1 enable_psr=1 disable_power_well=0. Some users with the HD matte screen have reported that these parameters cause screen flickering. Frame buffer compression (enable_fbc=1) is enabled by default starting from kernel 4.11.

For the Precision 5520 which has an Intel 8265 Wi-Fi card, the power_save option for the iwlwifi kernel module can be set from 1 to 5 with potential power savings. See Kernel modules#Setting module options. Bluetooth and Wi-Fi can separately be disabled with rfkill. See Wireless network configuration#Rfkill caveat.

It is possible to reduce the voltage supplied to the CPU and integrated intel GPU in order to reduce their power consumption. Usually some reduction is possible without any instability, depending on the specific system. Often the first signs of instability come during suspend, resume, and transitions between load and idle, not necessarily during extended periods of high load. See intel-undervolt and linux-intel-undervolt-toolAUR which can automate the process of undervolting on each boot/resume.

The integrated Intel HD 630 GPU works well out of the box. Optionally you may install xf86-video-intel but this is no longer recommended, since the built-in kernel modesetting driver is more reliable. If you do not want to use the discrete NVIDIA GPU, no extra setup is necessary. Otherwise, there are a few options. All of the display outputs are connected to the integrated GPU, so there is no need to set up output from the discrete GPU. It may be necessary to compile a custom kernel as described in #Power saving.

See #Disable discrete GPU above.

With this setup it is possible to use the integrated GPU by default and to offload GPU intensive applications to the discrete GPU by the use of the DRI_PRIME environment variable. See PRIME for details. Note that the open source NVIDIA driver Nouveau currently does not support power management on Pascal GPUs such as the GTX 1050, so performance is very poor with this driver. See Nouveau#Power management.

With this setup the integrated GPU is used by default, but some applications can be rendered on the discrete GPU with the optirun or primusrun launchers. See Bumblebee for detailed instructions. The lack of proper v-sync support means that with this method applications rendered on the discrete GPU exhibit tearing. There is also some overhead introduced as a result of moving data inefficiently between the discrete and integrated GPUs, but the NVIDIA GPU performs much better than it does with Nouveau.

With this setup the discrete GPU is used for all rendering and the integrated GPU is used only to display the rendered output. Power consumption is much higher during light usage because the discrete GPU cannot be disabled. Performance for graphics intensive applications is significantly better than with Bumblebee, and v-sync works due to PRIME Synchronization so tearing is eliminated. Remove bumblebee and follow the instructions in NVIDIA Optimus, NVIDIA README, or PRIME Synchronization thread using PCI:1:0:0 as the BusID. Add the modeset=1 parameter to the nvidia_drm kernel module (on boot, not with modprobe) to enable PRIME synchronization and remove tearing (see Kernel modules#Setting module options).

The Synaptics Touchpad's basic functionality works out of the box.

Depending on which package handles your touchpad input, the methods to extend the functionality varies.

The full documentation for libinput seemed to work quite well for this touchpad. While the driver already contains logic to process advanced multitouch events like swipe and pinch gestures, the desktop environment or window manager might not have implemented actions for all of them yet.

To get some three and four-touch gestures to work you may need to use the documentation at libinput-gestures and install the libinput-gesturesAUR package.

You can use synclient to list the touchpad's capabilities and change them for the session.

The touchpad has a big click zone in the bottom that can be disabled or configured for 1, 2 or 3 buttons. For example, to have most of the touchpad seen as "button 1" but the middle lower zone (middle button) and the right lower zone (right button), create /etc/X11/xorg.conf.d/50-synaptics.conf with content:

With the recent deprecation of synaptics, it is possible to use existing GUI (for instance, GNOME Tweak Tool) to change the behavior. Using gnome-tweaks, under Keyboard & Mouse section, Mouse Click Emulation is set by default to "Fingers". Changing it to the "Area" option, which uses the bottom right of the touchpad for a right click, fixes the problem.

TB16 works fine if either Thunderbolt security is disabled in the BIOS or using bolt to temporarily authorize or permanently enroll Thunderbolt devices with Thunderbolt security activated. Various quirks are detailed on the Dell TB16 page.

Some Dell docks (tested with the D6000) experience behavior whereby the displays periodically disconnect. Unplugging and plugging the dock back in again causes the displays to come back to life, but the displays will disconnect again. The more permanent fix for this is to comment out the following line in PulseAudio configuration:

A discussion around this issue can be found here, including the discussion around fixes.

Firmware updates are provided by Dell and can be installed with fwupd.

Alternatively, firmware images can be found at Dell support page as XPS_15_9560_X.Y.Z.exe files. In order to install:

The process will take about five minutes, during which the system will have some reboots and push fans at maximum speed. Finally, the system will reboot normally.

The fingerprint reader support was added as of libfprint v1.92.0. To setup and configure the fingerprint reader, see instructions in fprint.

If Xorg freezes as soon as it starts, even before printing any logs, and you are trying to use the Intel card with the NVIDIA one disabled, you need to add kernel parameter acpi_rev_override=1 as explained in #Disable discrete GPU above.

If audio output through the headphone jack suddenly stops working and restarting the computer does not help, try suspending/resuming it. It may be necessary to unplug headphones before suspending and then plug them in after the computer fully wakes up (based off of this AskUbuntu answer and users experience on Arch). If headphone audio seems permanently missing even after suspend/resume tricks and plugging/unplugging the cable, alsactl restore can bring it back. The last suggested thing to try is booting to Windows and muting/unmuting audio with headphones connected.

If audio volume is low through the speakers/headphones, you may need to reboot into Windows and increase the volume in Windows. Then reboot into Linux and your speakers/headphones should be louder.

If no audio devices are detected after updating the kernel to 6.7.0 or later, this may be due to the snd_soc_avs module (See thread for more information). Check the output of pactl list cards. If the line for driver name shows alsa.driver_name = "snd_soc_avs_probe", try blacklisting the module from the kernel.

One way to do this is to create the file /etc/modprobe.d/blacklist.conf and add the line blacklist snd_soc_avs. After rebooting, the module snd_hda_intel should be loaded and the audio devices detected successfully.

If you have an NVMe disk and depending on your BIOS version (but even with 1.5.0 from October 2017), you may have a lot of system error logs like:

This can be corrected with the kernel boot option pcie_aspm=off which appears to have minimal to no effect on power consumption. If that does not work, try pci=nommconf (see here for explanation).

The NVIDIA/nouveau driver may cause any runs of lspci, starting an X server, or otherwise poking the graphics card to cause at least one CPU core to lock up, as well as seeming to completely lock up PCIe access, for instance to the NVMe SSD. The kernel parameter nouveau.modeset=0 may fix this. This is also related to the X freezes on startup (some machines may require lspci/startx to be run twice so they freeze after nouveau is taken care of); the solution in that case is to also set acpi_rev_override=1. [1]

If you experience a large degradation of general performance and responsiveness it may be due to the CPU getting stuck throttled at 800Mhz. This also happens for other similar XPS models like the XPS15 9550 and might be because of non-OEM power adapters. To check, run watch -n1 'lscpu | grep MHz' and perform some tasks. If the CPU frequency is stuck at 800Mhz the whole time, then you have this problem.

To fix, there are three options:

After restarting run the same command to check the CPU frequency again and it should be back to normal. [2]

It can be a problem in some cases when devices attached to the USB-C port:

It caused by Dell firmware not initializing them during POST by default. But it can be turned on in BIOS setup (System Configuration > Thunderbolt Adapter Configuration > Enable Thunderbolt Adapter Boot Support).

A regression was introduced in kernel 6.4.11 and 6.1.46LTS related to the card reader rtsx driver that subsequently prevents the system from recognizing NVMe drives and booting normally.

A workaround is to blacklists the offending drivers (rtsx_pci and rtsx_pci_sdmmc) then regenerate the initramfs, until the kernel issue is fixed.

This will disable the card reader and the system will boot normally.

See FS#79439 for more details.

**Examples:**

Example 1 (unknown):
```unknown
smbios-thermal-ctl
```

Example 2 (unknown):
```unknown
--set-thermal-mode
```

Example 3 (unknown):
```unknown
# smbios-thermal-ctl --set-thermal-mode quiet
```

Example 4 (unknown):
```unknown
$ modinfo dell-smm-hwmon | grep '^description'
description:    Dell laptop SMM BIOS hwmon driver
```

---

## Power management/Wakeup triggers

**URL:** https://wiki.archlinux.org/title/Power_management/Wakeup_triggers

**Contents:**
- Wakeup trigger interfaces
  - /proc/acpi/wakeup
  - /sys/module/acpi/parameters/ec_no_wakeup
  - /sys/devices/
  - /sys/class/wakeup/*
- Persistent settings
  - One-time with systemd
  - Event-driven with udev
- Troubleshooting
  - List device and/or bus trees

Wakeup triggers are event sources that can wake the system from any of the hardware power-saving states. The obvious example is the power or suspend button, the Wake-on-LAN functionality or the lid switch in laptop systems. Wakeup triggers can be controlled through various kernel interfaces listed below. There is no unified interface covering all possible triggers.

Reading the /proc/acpi/wakeup file yields list of ACPI-registered wakeup sources with corresponding sysfs IDs where available. Writing an entry from the Device column to the file toggles its state. For example, to disable waking on opening the laptop lid, run:

This file represents the value of ACPI kernel module option ec_no_wakeup, which controls passing the wakeup triggers from embedded controller when the system is in the suspend-to-idle (s2idle) power state [1]. On modern laptops embedded controller wakeups can cause excessive battery drain in some cases.

Each sysfs device that supports wakeup contains the file wakeup in a device's power subdirectory. The file contains wakeup trigger's status and can be written to as well. Bus controllers as well as endpoint devices can be capable of waking up the system. For example, to disable wakeups from the first USB controller (bus), run:

An endpoint device should be able to wake the device if the trigger is enabled regardless of the controller's setting, however this might be hardware-dependent.

Program PowerTOP interfaces with sysfs, but it only lists wakeup triggers of networking and USB devices by reading /sys/class/net/ and /sys/bus/usb/devices/ (containing symlinks to /sys/devices/).

Almost all wakeup triggers can be found in the /sys/class/wakeup directory, which contains symlinks to all relevant devices. This is useful for finding possible wakeup triggers by going through subdirectories. Some of the triggers can correspond to virtual devices while hardware-related wakeup triggers are the ones that contain at least one of these files:

Some of wakeup triggers in /sys/class/wakeup also provide a link to the cryptic /proc/acpi/wakeup names where the following file is present:

The one-time methods should suffice for setting the /proc/acpi/wakeup states and acpi.ec_no_wakeup kernel parameter while the event-driven approach with udev is the reliable way to configure the sysfs devices.

The ec_no_wakeup ACPI kernel module option can be set at boot as described in the article. The standard solution to set the sysfs values at boot are systemd services such as in this troubleshooting case. Another systemd-based manager for /proc/acpi/wakeup is wakeup-triggersAUR.

Some systems can override some of the ACPI wakeup triggers upon power state transition(s) in what is more of a bug rather than a feature. If the hardware is overriding triggers at predictable times that can still be solved with appropriately crafted systemd units. The sleep.target is a generic target covering all different suspended states that might be helpful in this case, but there is no generic wakeup.target [2].

This method only works reliably with sysfs devices that are connected all the time.

Setting the wakeup trigger status with udev rules is an event-driven method that works reliably any time the devices with wakeup triggers are connected. The key is to detect an addition of a new device (ACTION=="add") in a rule and set the wakeup trigger status with ATTR{power/wakeup}="disabled". If the hardware is resetting this setting, udev can try to circumvent it by reapplying rules upon every device change (ACTION=="add|change"). A device tree with possible parameters for matching a particular device found in sysfs can be obtained with udevadm info -q all -a /sys/devices/....

A representative common example here would be a Logitech Unifying USB receiver. Its wakeup trigger should be enabled by default and if that is not desired, a solution could be a udev rule, as follows:

The reverse case to enable the necessary trigger(s) is described in the udev article.

udev triggers so early in the device enumeration that disabling wakeup trigger with the method above causes (some?) disabled triggers to not be listed in /sys/class/wakeup. That might be dependent on whether the device was already present at boot and needs further clarification.

These auxiliary commands can be helpful when trying to understand all wakeup triggers of a certain system, to aid with udev rule writing or general wakeup source troubleshooting:

The information on which wakeup source was the reason for the last device wakeup is unfortunately platform-specific. On x86 machines dmidecode can be used:

However for some computers it always reports "Power Switch" regardless of the real cause, e.g. for any of the USB keyboard, laptop keyboard, the power switch and the mouse.

For some Intel Haswell systems with the LynxPoint and LynxPoint-LP chipset, instantaneous wakeups after suspending are reported. They are linked to erroneous BIOS ACPI implementations and how the xhci_hcd module interprets it during boot. As a work-around reported affected systems are added to a denylist (named XHCI_SPURIOUS_WAKEUP) by the kernel case-by-case [3].

Wakeup may happen, for example, if a USB device is plugged during suspending and ACPI wakeup triggers are enabled. A viable workaround for such a system is to disable the relevant wakeup triggers. An example to disable wakeup through USB is described as follows [4].

To view the current configuration:

The relevant devices are EHC1, EHC2 and XHC (for USB 3.0). To toggle their state you have to echo the device name to the file as root:

This should result in suspension working again. However, this settings are only temporary and need to be set at every boot. To automate this, see systemd-tmpfiles or BBS thread for possible solutions.

On some Gigabyte motherboards, the GPP bridge to the NVMe drive may cause premature wakeups from suspend.

Known boards affected:

Setting the status of GPP0 to disabled may fix the issue:

Same as the Haswell solution above, this setting is only temporary. An example of automating the fix can be found in this BBS thread.

For some Gigabyte motherboards, disabling everything in /proc/acpi/wakeup including GPP0 does not prevent an instantaneous wakeup from suspension. If this is the case, your motherboard may have issues with ACPI in Linux.

Known boards affected:

Apply the following to your kernel parameters:

Certain ASRock motherboards for the AM5 platform may instantly wake from sleep also. This is due to the USB xHCI controller.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:

This behaviour has been noticed on the B850M Pro RS model (and will presumably also extend to the very similar B850M Pro RS WiFi.)

Certain MSI motherboards for the AM5 platform may also be affected by the premature wakeups from suspend because of the GPP bridge to the NVME drive.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:

This behaviour has been noticed on the X870 Tomahawk model.

For some newer AMD Ryzen 7000 Series systems, instantaneous wakeups after suspending, or wake up from s2idle when plugging in the AC adapter or by closing the lid, may occur. It is due to the redundant IRQ interrupt from the GPIO controller in AMDI0030:00. [5][6]

The current workaround is to configure the kernel to ignore the interrupt from the problematic GPIO pins. Add the following to your kernel parameters:

Multiple GPIO pins can be appended to the ignore list in the format of AMDI0030:00@N. However, the corresponding GPIO pins that cause the system to wake up is depended to the device model. You may find the pin number from the dmesg log after enabling debug messages from the system suspend/hibernation infrastructure:

Perform a suspend/resume cycle, you may find the following lines in dmesg log.

Usually GPIO 2, 3 and 4 would be the one response to this issue. Then, you may mount the debugfs to /sys/kernel/debug to trace the state of the GPIOs.

Look for the lines in /sys/kernel/debug/gpio with data in S0i3 and S3 columns.

Ignore the corresponding GPIO pins in gpiolib_acpi.ignore_interrupt, regenerate the initramfs image, and reboot.

Installing NVIDIA proprietary drivers might render suspension and hibernation not possible. In that case the system log might include:

See NVIDIA/Tips and tricks#Preserve video memory after suspend.

If the nouveau driver is used, the reason for instantaneous wakeups may be a bug in the driver, which sometimes prevents GPU from suspending. A possible workaround is unloading the nouveau kernel module right before going to sleep and loading it back after wakeup. To do this, create the following script:

The first echo line unbinds nouveaufb from the framebuffer console driver (fbcon). Usually it is vtcon1 as in this example, but it may also be another vtcon*. See /sys/class/vtconsole/vtcon*/name which one of them is a frame buffer device [7].

The Logitech Bolt receiver is a dongle with a yellow hexagon that has a lightning bolt shape cut out of it. It can cause immediate wakeup after suspending. See Logitech Unifying Receiver#PC wakes immediately from sleep.

**Examples:**

Example 1 (unknown):
```unknown
/proc/acpi/wakeup
```

Example 2 (unknown):
```unknown
# echo "LID" > /proc/acpi/wakeup
```

Example 3 (unknown):
```unknown
ec_no_wakeup
```

Example 4 (unknown):
```unknown
# echo "disabled" > /sys/bus/usb/devices/usb1/power/wakeup
```

---

## Bluetooth

**URL:** https://wiki.archlinux.org/title/Bluetooth

**Contents:**
- Installation
  - Front-ends
    - Console
    - Graphical
- Pairing
  - Dual boot pairing
    - Setup
    - For Windows
      - Extracting on Windows
      - Extracting on Linux

Bluetooth is a standard for the short-range wireless interconnection of cellular phones, computers, and other electronic devices. In Linux, the canonical implementation of the Bluetooth protocol stack is BlueZ.

The following packages allow for a graphical interface to customize Bluetooth.

This section describes directly configuring bluez via the bluetoothctl(1) command line tool, which might not be necessary if you are using an alternative front-end tool (such as GNOME Bluetooth).

The exact procedure depends on the devices involved and their input functionality. What follows is a general outline of pairing a device using bluetoothctl.

Start the bluetoothctl interactive command. Input help to get a list of available commands.

An example session may look this way:

For dual booting Linux systems, as shown in #Saving the configuration simply ensure all files from /var/lib/bluetooth/BT-Adapter-MAC-address are identical on each installation, either by copying or symlinking them.

With Windows or macOS, to pair devices on dual boot setups you need to change the pairing keys on your Linux install to match.

This page only describes the manual method of doing so. To automate the process, see the bt-dualboot project (does not support Bluetooth Low Energy) and the related repositories. For a semi-automated process, use the bluetooth-dualboot script which does not edit any files, but it helps you run the right commands and cut-and-paste the correct values.

To do this, first pair your device on your Arch Linux install. Then reboot into the other OS and pair the device. Now you need to extract the pairing keys, but first switch off the Bluetooth devices to prevent any connection attempts.

You can extract your Bluetooth keys on either Linux or Windows:

First, boot into Windows.

The registry key containing the link keys may only be accessed by the SYSTEM account, which cannot be logged into. Therefore, you will need Microsoft's PsExec tool from the official Windows Sysinternals site in order to run regedit.exe as SYSTEM.

Download PsTools, and extract PsExec64.exe.

In an administrator instance of a command shell, from the location of the extracted EXE, launch the registry editor:

In the registry editor, navigate to the following registry key:

Within this registry key is one subkey per Bluetooth adapter, named by MAC address. If there are multiple subkeys, and you are unsure of which to use, follow this guide to find the MAC address for the desired Bluetooth adapter.

In the desired adapter's registry key, there is a name-value pair for each paired device, with the name being its MAC address. Additionally, you might see some subkeys named by MAC addresses, each containing name-value pairs with names like LTK or IRK. These subkeys (if any) are for Bluetooth 5.1 devices. If the device you're trying to share has a subkey, it is a Bluetooth 5.1 device. If it does not have a subkey, only a name-value pair, it is not a Bluetooth 5.1 device.

Right click on the adapter's registry key and export it as a .reg file. This is a text file that you can copy keys from. As mentioned, it contains pairing keys in name-value pairs for non-Bluetooth 5.1 devices, and pairing keys (and some other information) in per-device subkeys for Bluetooth 5.1 devices. Make this file available to your Linux installation and reboot into it.

If the device you want to share is not a Bluetooth 5.1 device, jump to #Saving the configuration. If it is a Bluetooth 5.1 device, you need to make some modifications to the pairing keys and the associated information before finishing up. Refer to #Preparing Bluetooth 5.1 Keys to see how.

Boot into Arch. Install chntpw. Mount your windows system drive. Change to the registry hive directory and start chntpw on the SYSTEM hive:

Inside the chntpw environment, run:

Instead of CurrentControlSet, you may see ControlSet00X (check using ls); use this instead:

There will probably be just one subkey, whose name is your Bluetooth adapter's MAC address. Show it with ls and cd into it:

The subkey names under that adapter are the MAC addresses of the devices the adapter is paired to. Show them with ls, then cd into each of those you want to dual-pair:

If this is not a Bluetooth 5.1 device, you will only see the pairing key:

If so, show a hexdump of your device's key using hex:

The "XX"s are the pairing key. Make note of which keys map to which MAC addresses.

If this is a Bluetooth 5.1 device, then you will see several keys corresponding to the one device:

Refer to #Preparing Bluetooth 5.1 Keys to see how to use these, using hex value_name to obtain the requested values.

Finally, to import the key(s) into your Linux installation, proceed to #Saving the configuration.

The ~/.bt_keys.txt file now contains the established Bluetooth keys. For older versions of macOS (High Sierra and older) you will have to reverse the keys before proceeding. For example, 98 54 2f aa bb cc dd ee ff gg hh ii jj kk ll mm becomes MM LL KK JJ GG FF EE DD CC BB AA 2F 54 98.

If this is a Bluetooth 5.1 device, then there will be more than one key corresponding to one device. Refer to #Preparing Bluetooth 5.1 Keys to see how to use these.

Finally, to import the key(s) into your Linux installation, reboot into Linux and proceed to #Saving the configuration.

This article or section needs expansion.

If you observed the presence of Bluetooth 5.1 keys while following #For Windows or #For macOS, you must apply certain transformations to their values before importing them into Linux. Create the requested files with their appropriate contents, for installation in #Saving the configuration. This process will depend on the device, and some of the values have to be manipulated; code utilities for doing so are provided below.

For an example of the general case:

Now that you have the keys change user to root, then continue with:

Here you will find folders for each paired Bluetooth device. For each device you want to pair with Arch and your dual boot, do the following:

If you have a pairing key (i.e. this is not a Bluetooth 5.1 device), then edit the info file and change the key under [LinkKey]. E.g.:

If you have several keys, as in Bluetooth 5.1, edit the info file and substitute all applicable keys with their recorded values. E.g. for an Xbox One S Wireless Controller:

Then restart bluetooth.service and pulseaudio (with pulseaudio -k && pulseaudio --start).

You should be able to connect to your device now.

To force Bluetooth controller to use older Bluetooth transport protocol (e.g. because its simpler to setup dual boot pairing for 3.0 device, than for 5.x BLE device), set ControllerMode=bredr in /etc/bluetooth/main.conf in the [General] section:

Default value is ControllerMode=dual i.e. both BR/EDR and LE enabled.

As of bluez 5.65, BlueZ' default behavior is to power on all Bluetooth adapters when starting the service or resuming from suspend. [2]

If you would like the adapter to not be automatically enabled (e.g. on a portable device where you wish to save battery), set AutoEnable=false in /etc/bluetooth/main.conf in the [Policy] section:

The adapter can still be turned on manually by running power on as described in #Pairing.

If the device should always be visible and directly connectable:

To allow Bluetooth keyboards, mice, etc. to wake the system from suspend. First, check the bios settings and make sure that wake from USB is not disabled. In many cases, Bluetooth from the motherboard is a USB device.

Add a new udev rule for Bluetooth adapter(s) (USB Wireless Controller Base Class, Bluetooth Programming Interface Protocol) to enable wake from suspend:

To automatically re-configure your Bluetooth keyboard after wakeups to e.g. have a different keymap or key press repeat rate (for details, see Xorg/Keyboard configuration#Adjusting typematic delay and rate and xmodmap), create an executable script:

Then create an additional udev rule like above:

The Bluez stack keeps new, potentially buggy features behind the D-Bus experimental and kernel experimental options. The functionality included under these varies over time, as experimental features are determined to be stable and no longer require the option (as an example: enabling D-Bus experimental interfaces currently allows to report battery level for old headsets). To enable these, uncomment the corresponding line in the configuration:

Alternatively, you can edit the bluetooth.service to add the --experimental or --kernel flag, like this drop-in file:

Either way, you must then restart the bluetooth.service.

You will typically need to take an additional step to integrate the audio server with Bluetooth. This is detailed in the below sections.

See the Bluetooth headset page for more information about Bluetooth audio and Bluetooth headsets.

In order to be able to use audio equipment like Bluetooth headphones or speakers, you need to install the additional pulseaudio-bluetooth package. Make sure to restart PulseAudio to make the installation take effect: pulseaudio -k. With a default PulseAudio installation (specifically, using a user instance with the packaged default.pa) you should immediately be able to stream audio from a Bluetooth device to your speakers. [3]

If you have a system-wide PulseAudio setup make sure the user running the daemon (usually pulse) is in the lp group and you load the Bluetooth modules in your PulseAudio config:

Optionally, add load-module module-switch-on-connect if you want to auto-switch all audio to the Bluetooth device.

PipeWire as of v0.3.19 enables its Bluetooth support by default.

First, ensure that your Bluetooth audio device is correctly paired and connected to the system.

Then, install bluez-alsa-gitAUR, start (and enable) the bluealsa service, and add your user to the audio group.

Run the following command to check if everything is working as intended (replace XX:XX:XX:XX:XX:XX and FILE.wav below):

Finally, add the following lines to your ~/.asoundrc:

You can now use the bluealsa device to reach your Bluetooth audio device. Volume management is conducted normally via alsamixer with the option -D bluealsa.

To get Bluetooth serial communication working on Bluetooth-to-Serial modules (HC-05, HC-06) do the following steps:

Pair your Bluetooth device using bluetoothctl as described above.

Install bluez-deprecated-tools, as it provides certain functionality which is missing from newer tools.

Bind paired device MAC address to tty terminal:

Now you can open /dev/rfcomm0 for serial communication:

This article or section is out of date.

In order to debug, first stop bluetooth.service.

And then start it with the -d parameter:

Another option is via the btmon tool.

Eight BlueZ tools were deprecated and removed from bluez-utils, although not all of them were superseded by newer tools. The bluez-deprecated-tools package now provides these deprecated tools.

bluetooth.service only requires the directory /sys/class/bluetooth to exist, which should be created by kernel module bluetooth, which is only autoloaded by systemd-udev if it actually finds a working Bluetooth hardware device.

If your /sys/class/bluetooth does not exist, check if your kernel Bluetooth module is loaded by lsmod. If not, and you believe you have a Bluetooth device, you can try manually starting them by loading the Bluetooth module and restarting bluetooth.service.

You should also load your corresponding kernel Bluetooth driver when loading the bluetooth module, most likely btusb, but can also be btrtl,btintel,btbcm,bnep,btusb etc.

Check bluetooth.service's unit status to see whether it started.

See also Debian Bug report logs - #853207.

If bluetooth.service started successfully, there is a chance that you still cannot use Bluetooth normally (e.g. bluetoothctl says something like org.Bluez.Error.NotReady when you scan on). If this happens, try rebooting your computer, and double-check: whether directory /sys/class/bluetooth exists; whether lsmod includes correct Bluetooth modules; log messages in the journal; etc. systemd-udev should pickup your Bluetooth hardware automatically without manual changes again.

On systems capable of suspend-to-idle/S2idle/S0ix/Modern Standby, Bluetooth controllers will stay enabled during sleep. This will usually cause the system to wake up immediately after going to sleep if any Bluetooth device is connected.

To prevent this, you can disable Bluetooth completely before going to sleep - install bluez-utils and create this file:

Enable this service and check if Bluetooth devices disconnect when going to sleep, and whenever Bluetooth goes back up after waking up the system.

If this workaround is in use, waking up the system with a Bluetooth mouse/keyboard will not work.

This can have various causes:

There is a bug with some motherboard bluetooth controllers. To see if this might be the issue, run journalctl | grep hci. If there are entries like "command tx timeout" or "Reading Intel version command failed", then power off your pc and physically unplug the power cable for a few seconds. This forces the controller to reload the firmware (while a standard reboot will not). See bug report here.

Make sure the device is not being blocked by rfkill.

If using USBGuard, make sure it does not block the device. See USBGuard#Allow Bluetooth controllers.

It might also happen with some intel cards (such as the 8260) to not be picked up correctly by the Bluetooth service. In some cases, using the deprecated bluez-deprecated-tools in lieu of bluez-utils have reportedly fixed the issue.

This might also be caused by power saving measures, in which case adding the kernel parameter btusb.enable_autosuspend=n is a potential solution. See also Red Hat Bugzilla – Bug 1573562.

Sometimes unloading and loading btusb without options helps to get the controller back:

It may also occur when the dongle is a CSR clone.

If your device still soft blocked and you run ConnMan, try this:

If you are using a USB dongle, you should check that your Bluetooth dongle is recognized. You can do that by running journalctl -f as root when you have plugged in the USB dongle (or inspecting /var/log/messages.log). It should look something like the following (look out for hci):

If you only get the first two lines, you may see that it found the device but you need to bring it up. Example:

To verify that the device was detected you can use btmgmt which is part of the bluez-utils. You can get a list of available devices and their identifiers and their MAC address by issuing:

It is possible to check the Bluetooth version as mapped to the HCI version according to the table in the official specification. For example, in the previous output, HCI version 6 is Bluetooth version 4.0.

More detailed information about the device can be retrieved by using the deprecated hciconfig. (bluez-deprecated-tools)

If other devices share the same USB host, they can interrupt communication with audio devices. Make sure it is the only device attached to its bus. For example:

The device ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode) has a regression bug, and currently only works in the kernel version 5.17 and < 6.0. For more information, see Kernel Bug 60824.

There are Logitech dongles (ex. Logitech MX5000) that can work in two modes: Embedded and HCI. In embedded mode dongle emulates a USB device so it seems to your PC that you are using a normal USB mouse/keyoard.

If you hold the little red Button on the USB BT mini-receiver it will enable the other mode. Hold the red button on the BT dongle and plug it into the computer, and after 3-5 seconds of holding the button, the Bluetooth icon will appear in the system tray. Discussion

Alternatively, you can install the bluez-hid2hci package. When you connect your Logitech dongle it will automatically switch.

Some of these devices require the firmware to be flashed into the device at boot.

Some firmware is available when searching for broadcom on the AUR, a notable package being broadcom-bt-firmwareAUR, which provides the files for multiple cards.

Alternatively, the firmware can be converted from a Microsoft Windows .hex file into a .hcd using hex2hcd (which is installed with bluez-utils).

In order to get the right .hex file, try searching the device vendor:product code obtained with lsusb, for example:

Alternatively, boot into Windows (a virtual machine installation will suffice) and get the firmware name from the Device Manager utility. If you want to know the model of your device but cannot see it in lsusb, you might see it in lsusb -v as iProduct.

The .hex file can be extracted from the downloaded Windows driver without having to run Windows for it. Download the right driver, for example Bluetooth Widcomm[dead link 2023-09-16—domain name not resolved]. Depending on the format, extracting the files might need unrar or cabextract. To find out which of the many .hex files is the right one for you, look in the file Win32/bcbtums-win7x86-brcm.inf and search for [RAMUSBE031.CopyList], where E031 should be replaced with the product code (the second hex number in lsusb) of your device in upper-case. Underneath you should see the file name of the right .hex file.

Once you have the .hcd file, copy it into /lib/firmware/brcm/BCM.hcd - this filename is suggested by dmesg and it may change in your case so check your dmesg output in order to verify. Then reload the btusb module:

The device should now be available. See BBS#162688 for information on making these changes persistent.

See Wireless network configuration#Bluetooth coexistence.

On dual boot systems, if Bluetooth firmware versions are different for Windows and Linux, the Bluetooth adapter is not working after rebooting to Windows.

The best way to prevent this is updating the Bluetooth drivers (especially firmware) with latest version for each OS.

If you cannot find the latest version driver (or firmware) for Windows, you can copy the latest firmware file /usr/lib/firmware/mediatek/BT_RAM_CODE_MT7961_1_2_hdr.bin.xz from Arch Linux and extract to Windows (e.g. C:\WINDOWS\system32\DRIVERS\, you can find the firmware file path in the device manager on Windows).

First, find vendor and product ID of the adapter. For example:

In this case, the vendor ID is 8087 and the product ID is 0025.

Then, use usb_modeswitch to reset the adapter:

Enable discoverable mode if your computer cannot be discovered from your phone:

Verify that discoverable mode is on:

If the computer still does not show up, try changing the device class in /etc/bluetooth/main.conf as follows:

A user reported that this was the only solution to make their computer visible for their phone. LG TVs (and some others) are discoverable from their audio devices, so using 000414 (the soundbar class) will make such devices appear.

See https://bluetooth-pentest.narod.ru/software/bluetooth_class_of_device-service_generator.html to generate Bluetooth device/service classes.

If you see messages like the following in the journal, and your device fails to connect or disconnects shortly after connecting:

This may be because you have already paired the device with another operating system using the same Bluetooth adapter (e.g., dual-booting). Some devices cannot handle multiple pairings associated with the same MAC address (i.e., Bluetooth adapters). Follow instructions on #Dual boot pairing for solving this issue.

Some devices using Bluetooth low energy do not appear when scanning with bluetoothctl, for example the Logitech MX Master. You can use transport le to scan it.

Another way to connect them is by installing bluez-deprecated-tools, then start bluetooth.service and do:

Wait until your device shows up, then Ctrl+c hcitool. bluetoothctl should now see your device and pair normally.

It seems that BLE passive scan is broken on this device. See upstream bug report for more details.

You may notice that you cannot automatically reconnect to a device after it goes to sleep, or after the computer wakes from suspend.

You would for example notice the following errors in your logs:

This could be because the device is not marked as trusted. See #Pairing.

See Bluetooth mouse#Troubleshooting.

A Bluetooth audio device will fail to connect if pipewire (rather than pulseaudio-bluetooth) is being used, but an instance of pipewire is not running. Start the pipewire.service user unit or play some audio to start the pipewire daemon, then try to connect the audio device again.

If you experience audio stuttering while using a Bluetooth mouse and keyboard simultaneously, you can try the following as referenced in #23 https://bugs.launchpad.net/ubuntu/+source/bluez/+bug/424215

Use the settings below:

Then restart the bluetooth.service.

You can see relevant discussion on xpadneo but the xpadneo driver is not needed.

If you see this when trying to enable receiving files in bluetooth-properties:

Then make sure that the XDG user directories exist.

If incoming file transfers fail on an an otherwise functional Bluetooth connection, the problem may be due to symlinks in your file transfer path. Logs like this would appear in the journal:

If the path shown in the error message contains a symlink, then obexd by default will not accept it. The behavior can be overridden on initialization using a drop-in file for the obex.service user service:

Then reload the systemd manager configuration of the calling user and restart the obex.service user unit.

**Examples:**

Example 1 (unknown):
```unknown
bluetooth.service
```

Example 2 (unknown):
```unknown
obex.service
```

Example 3 (unknown):
```unknown
echo -e "command1\ncommand2\n" | bluetoothctl
```

Example 4 (unknown):
```unknown
bluetoothctl -- command
```

---

## Hybrid graphics

**URL:** https://wiki.archlinux.org/title/Hybrid_graphics

**Contents:**
- Dynamic switching
  - Fully power down discrete GPU
    - Using BIOS/UEFI
    - Using udev rules
    - Using bbswitch
    - Using acpi_call
      - Turning off the GPU automatically
        - At boot
        - After X server initialization
  - System76

Hybrid-graphics is a concept involving two graphics cards on same computer. Laptop manufacturers have developed technologies involving two graphics cards with different abilities and power consumption on a single computer. Hybrid-graphics has been developed to support both high performance and power saving use cases by keeping the Dedicated/Discrete Graphics Processor inactive unless its 3D rendering performance is needed over the Integrated Graphics Processor.

There are a variety of technologies and each manufacturer developed its own solution to this problem. This technology is well supported on Windows but it is still rough around the edges with Linux distributions. This article will try to explain a little about each approach and describe some community solutions to the lack of GNU/Linux systems support by vendors.

Most of the new Hybrid-graphics technologies involve two graphics cards: the dedicated and integrated cards are plugged to a framebuffer and there is no hardware multiplexer. The integrated card is always on and the dedicated card is switched on/off when there is a need in power-save or performance-rendering. In most cases there is no way to use only the dedicated card and all the switching and rendering is controlled by software. At startup, the Linux kernel starts using a video mode and setting up low-level graphic drivers which will be used by the applications. Most of the Linux distributions then use X.org to create a graphical environment. Finally, a few other softwares are launched, first a login manager and then a window manager, and so on. This hierarchical system has been designed to be used in most of cases on a single graphics card.

You may want to turn off the high-performance graphics processor to save battery power.

Some laptop manufacturers provide a toggle in the BIOS or UEFI to fully deactivate the dedicated card.

Ensure any display manager config for NVIDIA is removed.

Blacklist the nouveau drivers by creating

Reboot and run lspci to see if your NVIDIA GPU is still listed.

Check power usage to ensure your GPU is not drawing power, if it does #Using acpi_call may be another option to fully power it down.

With an NVIDIA GPU, this can be more safely done using bbswitch, which consists of a kernel package that automatically issues the correct ACPI calls to disable the discrete GPU when not needed, or automatically at boot.

Otherwise, and for GPUs not supported by bbswitch, the same can be done manually installing the acpi_call package.

Once installed load the kernel module:

With the kernel module loaded, execute the script at /usr/share/acpi_call/examples/turn_off_gpu.sh

The script will go through all the known data buses and attempt to turn them off. You will get an output similar to the following:

See the "works"? This means the script found a bus which your GPU sits on and it has now turned off the chip. To confirm this, your battery time remaining should have increased.

Currently, the chip will turn back on with the next reboot. To get around this, load the module at boot:

To turn off the GPU at boot it is possible to use systemd-tmpfiles.

The configuration above will be loaded at boot by systemd. What it does is write the specific OFF signal to the /proc/acpi/call file. Obviously, replace the \_SB.PCI0.PEG0.PEGP._OFF with the one which works on your system (please note that you need to escape the backslash).

On some systems, turning off the discrete GPU before the X server is initialized may hang the system. In such cases, it may be better to disable the GPU after X server initialization, which is possible with some display managers. In LightDM, for instance, the display-setup-script seat configuration parameter could be used to execute a script as root that disables the GPU. If you use SDDM then you can add the line echo "\_SB.PCI0.PEG0.PEGP._OFF" > /proc/acpi/call to either /usr/share/sddm/scripts/wayland-session or /usr/share/sddm/scripts/Xsession depending if you use Wayland or Xorg, replacing \_SB.PCI0.PEG0.PEGP._OFF with the one which works on your system.

Some System76 laptops (like the Oryx Pro) have their own unique hybrid graphics option. To make use of it, install system76-powerAUR, enable system76-power.service, and run system76-power graphics hybrid.

First ensure you are using integrated graphics mode by running system76-power graphics integrated and rebooting. Once in integrated mode, to power down the discrete graphics card run system76-power graphics power off. This command is not persistent and will need to be run after each boot.

This article or section is a candidate for merging with Vulkan.

When invoked, Vulkan attempts to initialize the Installable Client Driver (ICD) specified in /usr/share/vulkan/icd.d/nvidia_icd.json. The package nvidia-utils configures this file to reference the libGLX_nvidia driver, providing Vulkan with information about the GPU driver's path. However, if the GPU is disabled, initialization of this driver will fail, causing certain applications (e.g., those based on Chromium/Electron) to undergo delayed startup until a 30-second timeout is reached. To prevent Vulkan from attempting to load the driver in the first place and thus mitigate this timeout, you can override the location of the ICD JSON file using the VK_DRIVER_FILES environment variable. To unset it, use:

If after disabling the dedicated GPU bus #Using acpi_call the power draw is still high, check if the nouveau kernel module is loaded with lsmod. If it is not then make sure it is installed, that any entries in .conf files that blacklist Nouveau in /etc/modprobe.d/ are removed and that the Nouveau kernel module is automatically loaded at boot. After rebooting the power draw should be lower.

**Examples:**

Example 1 (unknown):
```unknown
/etc/modprobe.d/blacklist-nouveau.conf
```

Example 2 (unknown):
```unknown
blacklist nouveau
options nouveau modeset=0
```

Example 3 (unknown):
```unknown
/etc/udev/rules.d/00-remove-nvidia.rules
```

Example 4 (unknown):
```unknown
# Remove NVIDIA USB xHCI Host Controller devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c0330", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA USB Type-C UCSI devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x0c8000", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA Audio devices, if present
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x040300", ATTR{power/control}="auto", ATTR{remove}="1"

# Remove NVIDIA VGA/3D controller devices
ACTION=="add", SUBSYSTEM=="pci", ATTR{vendor}=="0x10de", ATTR{class}=="0x03[0-9]*", ATTR{power/control}="auto", ATTR{remove}="1"
```

---

## PulseAudio/Troubleshooting

**URL:** https://wiki.archlinux.org/title/PulseAudio/Troubleshooting

**Contents:**
- Getting debug output from PulseAudio
- Volume
  - Auto-Mute Mode
  - Muted audio device
  - Output stuck muted while Master is toggled
  - Muted application
  - Volume adjustment does not work properly
  - Per-application volumes change when the Master volume is adjusted
  - Volume gets louder every time a new application is started
  - Sound output is only mono on M-Audio Audiophile 2496 sound card

It can be useful to stop the pulseaudio.socket and pulseaudio.service user units, and start manually in a terminal during debugging:

Add vs to increase verbosity.

Here you will find some hints on volume issues and why you may not hear anything.

Auto-Mute Mode is a configurable setting from amixer. For more information, see ALSA#Disabling auto mute on startup.

If one experiences no audio output via any means while using ALSA, attempt to unmute the sound card. To do this, launch alsamixer and make sure each column has a green 00 under it (this can be toggled by pressing m):

To troubleshoot via CLI only, install pamixer and check the output of the following command:

If the output says muted, run pamixer -u to unmute. If it displays a low percentage value, you can run pamixer -i 10 several times to turn up the volume gradually.

In setups with multiple outputs (e.g. 'Headphone' and 'Speaker'), using plain amixer to toggle Master can trigger PulseAudio to mute the active output too, but it does not necessarily unmute it when Master is toggled back to be unmuted. [1] To resolve this, amixer must have the device flag set to pulse (requires pulseaudio-alsa):

This will cause amixer to ask PulseAudio to do the toggling rather than toggling it directly. Because of this, PulseAudio will correctly unmute Master as well as any applicable output.

If a specific application is muted or low while all else seems to be in order, it may be due to individual sink-input settings. With the offending application playing audio, run:

Find and make note of the index of the corresponding sink input. The properties: application.name and application.process.binary, among others, should help here. Ensure sane settings are present, specifically those of muted and volume.

If the sink input is muted, it can be unmuted by:

If the volume needs adjusting, it can be set to 100% by:

Check /usr/share/pulseaudio/alsa-mixer/paths/analog-output.conf.common.

If the volume does not appear to increment/decrement properly using alsamixer or amixer, it may be due to PulseAudio having a larger number of increments (65537 to be exact). Try using larger values when changing volume (e.g. amixer set Master 655+).

This is because your PulseAudio configuration uses flat volumes, instead of relative volumes, relative to an absolute master volume. If this is found to be inconvenient, asinine, or otherwise undesireable, relative volumes can be enabled by disabling flat volumes in the PulseAudio daemon's configuration file:

and then restarting PulseAudio by executing

Per default, it seems as if changing the volume in an application sets the global system volume to that level instead of only affecting the respective application. Applications setting their volume on startup will therefore cause the system volume to "jump".

Fix this by disabling flat volumes, as demonstrated in the previous section. When PulseAudio comes back after a few seconds, applications will not alter the global system volume anymore but have their own volume level again.

Known issue (will not fix): https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/223133

If sound does not play when PulseAudio's volume is set below a certain level, or if you hear clipping on output even at low volume (including Bluetooth devices), try setting ignore_dB=1 in /etc/pulse/default.pa:

However, be aware that it may cause another bug preventing PulseAudio to unmute speakers when headphones or other audio devices are unplugged.

If you experience low volume on internal notebook microphone, try setting:

If changing the volume in specific applications or simply running an application changes the master output volume, this is likely due to flat volumes mode of PulseAudio. Before disabling it, KDE users should try lowering the volume in System Settings > Sound > Notification Sounds to something reasonable. Changing the Event Sounds volume in KMix or another volume mixer application will not help here. This should make the flat-volumes mode work out as intended, if it does not work, some other application is likely requesting 100% volume when its playing something. If all else fails, you can try to disable flat-volumes:

Then restart the PulseAudio daemon:

If audio generally works, but stops after resume from suspend, try "reloading" PulseAudio by executing:

This is better than completely killing and restarting it (pulseaudio -k followed by pulseaudio --start), because it does not break already running applications.

If the above fixes your problem, you may wish to automate it, by creating a systemd service file.

Create the template service file in

Do a daemon-reload and enable this service for your user account (i.e. resume-fix-pulseaudio@username.service)

If when you unplug your headphones or plug them in the audio remains muted in alsamixer on the wrong channel due to it being set to 0%, you may be able to fix it by opening /etc/pulse/default.pa and commenting out the line:

Then restart the pulseaudio.service user unit.

Install alsa-tools and use hdajackretask:

More info about this problem: [2].

If you added the ignore_dB=1 option earlier to the load-module module-udev-detect line in your /etc/pulse/default.pa, try removing it.

Edit /etc/pulse/daemon.conf and set enable-deferred-volume = no. This might cause some sound crackles when changing volume, in that case you might want to leave that option enabled and tweak the deferred-volume-safety-margin-usec and deferred-volume-extra-delay-usec options instead.

Determine the card and device number of your microphone:

In hw:CARD,DEVICE notation, you would specify the above device as hw:0,0.

Then, edit /etc/pulse/default.pa and insert a load-module line specifying your device as follows:

Finally, restart PulseAudio to apply the new settings:

If everything worked correctly, you should now see your microphone show up when running pavucontrol (under the Input Devices tab).

If PulseAudio uses the wrong microphone, and changing the Input Device with pavucontrol did not help, take a look at alsamixer. It seems that pavucontrol does not always set the input source correctly.

Press F6 and choose your sound card, e.g. HDA Intel. Now press F5 to display all items. Try to find the item: Input Source. With the up/down arrow keys you are able to change the input source.

Now try if the correct microphone is used for recording.

Unmute and maximize the volume of the "Internal Mic".

Once you see the device with:

you might still need to adjust the settings. The microphone and the audio jack are duplexed. Set the configuration of the internal audio in pavucontrol to Analog Stereo Duplex.

Install and run pavucontrol, unlink the microphone channels and turn down the volume of one of the channels (which one depends on the device) to 0.

Some applications can change microphone levels causing the same issue. Try disabling volume adjustment in the application settings. For example, in Chromium, open chrome://flags and set Allow WebRTC to adjust the input volume to Disabled. If the application does not have such an option, a workaround is to remap stereo input to mono and use the remapped device as default.

If we are getting static noise in recordings, then the sound card sampling rate might be incorrect. To fix this, we need to set the sampling rate in the daemon.conf configuration file for the sound hardware.

48000 is disabled and needs to be changed to 44100:

Now hopefully, there is no static noise in microphone recording anymore.

Another possible cause is that your microphone has two channels but only one channel can provide a valid sound signal. Some information can be found here. The solution is to remap the stereo input to a mono input:

Now arecord hopefully works.

Try plugging it into a different port—e.g. ports at the back rather than front.

When you set enable-remixing = no on /etc/pulse/daemon.conf you may find that your microphone has stopped working on certain applications like Steam. This happens because these applications capture the microphone as mono only and because remixing is disabled, PulseAudio will no longer remix your stereo microphone to mono.

To fix this you need to tell PulseAudio to do this for you:

1. Find the name of the source

Example output edited for brevity, the name you need is in bold:

2. Add a remap rule to /etc/pulse/default.pa, use the name you found with the previous command, here we will use alsa_input.pci-0000_00_14.2.analog-stereo as an example:

3. Restart PulseAudio

If your microphone volume creeps up automatically and causes the sound to be distorted, you can fix it by disabling mic boost:

In all files /usr/share/pulseaudio/alsa-mixer/paths/analog-input*.conf,

including all variations such as [Element Headphone Mic Boost] and [Element Mic Boost (+20dB)]

Then restart PulseAudio:

Sometimes ALC892 chips have crackling sound while recording using a microphone. Some PulseAudio configuration changes may help:

and add the use_ucm option to

then restart PulseAudio.

If you are unsure about your microphone setup, you can hear the input from the microphone in real-time by enabling the loopback module (source):

The module will show up in the Recording tab of the pavucontrol program, where the source and volume can be configured. While latency should be low, it should be sufficient to get a feeling of the sound quality as you will hear yourself speak in the microphone. To make the change permanent, add the following PulseAudio configuration:

Watch out for feedback! Be ready to lower all volumes in case the microphone picks up the output from the loudspeakers. Naturally, it is better to run such a test with headphones.

The newer implementation of the PulseAudio sound server uses timer-based audio scheduling instead of the traditional, interrupt-driven approach.

Timer-based scheduling may expose issues in some ALSA drivers. On the other hand, other drivers might have a tendency to experience buffer underruns without it on, so check to see what works on your system.

To turn timer-based scheduling off, add tsched=0 in /etc/pulse/default.pa:

Then restart the PulseAudio server:

Do the reverse to enable timer-based scheduling, if not already enabled by default.

If you are using Intel's IOMMU and experience buffer underruns, add intel_iommu=igfx_off to your kernel command line.

If you experience buffer underruns because of kernel page locking or late scheduling, see Gaming#Tweaking kernel parameters for response time consistency.

Time-based scheduling may be causing this, disable it as explained in #Troubleshooting buffer underruns (glitches, skips, crackling).

Another reason you are encountering static noise in your headphone jack could be ALSA's loopback mixing.

Make sure you have alsa-utils installed, launch alsamixer, then select your audio device (pressing F6), navigate all the way left using the left arrow, and stop on Loopback, if Enabled disable it using the down arrow. This should not impact audio playback or microphone recording negatively, unless you require loopback mixing.

Some notebook models, like Dell XPS 13 9360, suffer from continuous hissing sound when a headphone is plugged in.

Yet another reason for this symptom could be the power-saving mode of your audio device.[3] If you followed Power management#Audio, revert the changes and check if it solves the problem.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

By default, PulseAudio uses timer-based scheduling. In this mode, fixed-size fragments are not used at all, and so the default-fragments and default-fragment-size-msec parameters are ignored. To turn timer-based scheduling off, add tsched=0 in /etc/pulse/default.pa:

Instructions below will cause PulseAudio to use a fixed size and number for audio fragments. These settings directly affect latency and power consumption. The latency is determined as default-fragments * default-fragment-size-msec, and the interrupt rate (i.e. how often the application is notified that some sound has indeed been played) is 1000 / default-fragment-size-msec. The considerations are:

If one does not care about excessive power consumption, then 2 or 3 fragments, 5 ms each, are a reasonable choice.

Restart the pulseaudio.service user unit.

Run your applications, listen to the sounds they produce, inspect the journal.

If the buffer underruns are occasional and mostly correlated to the system being highly loaded: this is a scheduler problem, the latency needs to be increased.

If there is metallic sound with the wrong speed from all applications: the most common reason is that you are trying to configure the fragment size which is way too small, like 1 ms. Do not do this.

If some, but not all, applications experience buffer underruns: this is an application that assumes a low-latency setup. So the fragment size must be decreased so that the application request becomes valid.

Try to enable LFE remixing as described in PulseAudio/Examples#LFE remixing.

This issue is due to incorrect buffer sizes. First verify that the variables default-fragments and default-fragment-size-msec are not being set to non default values in the file /etc/pulse/daemon.conf. If the issue is still present, try setting them to the following values:

This can result from an incorrectly set sample rate. Try the following setting:

and restart the PulseAudio server.

If one experiences choppy sound in applications using OpenAL, change the sample rate in /etc/openal/alsoft.conf:

Setting the PCM volume above 0 dB can cause clipping. Running alsamixer will allow you to see if this is the problem and if so fix it. Note that ALSA may not correctly export the dB information to PulseAudio. Try the following:

and restart the PulseAudio server. See also #No sound below a volume cutoff or Clipping on a particular output device.

When streaming over Wi-Fi using module-native-protocol-tcp, you can experience periodic sound stuttering with buffer underruns. As a workaround, you can try to use the rtp protocol. Install pulseaudio-rtp on both sides. On the sender side, create an rtp sink:

On the receiver side, load the rtp module:

PulseAudio can suspend sinks after a period of inactivity. This can make an audible noise (like a crack/pop/scratch). Sometimes even when move the slider volume, or open and close windows. This behavior is enabled in default configuration files:

Commenting that line in relevant file fixes that issue. A better solution is to add the following file:

For some devices (eg. Bose Quietcomfort 35 II), setting high enough volume of the device (usually via physical buttons or a slider) eliminates the audible noise after stopping playback.

The monitor is connected via HDMI/DisplayPort, and the audio jack is plugged in the headphone jack of the monitor, but PulseAudio insists that it is unplugged:

This leads to no sound coming from HDMI output. A workaround for this is to switch to another VT and back again. If that does not work, try: turn off your monitor, switch to another VT, turn on your monitor, and switch back. This problem has been reported by ATI/Nvidia/Intel users.

Another workaround could be to disable the switch-on-port-available module by commenting it in /etc/pulse/default.pa [4]:

You might want to use HDMI audio with your a/v receiver but no display. HDMI requires a video signal, which we have from the virtual terminal.

When the video signal turns off, the audio sink gets lost as well, so make sure that console blanking is disabled. See Display Power Management Signaling#Linux console for details.

If PulseAudio starts, run pacmd list. If no cards are reported, make sure that the ALSA devices are not in use:

Make sure any applications using the pcm or dsp files are shut down before restarting PulseAudio.

If you have trouble with some applications (such as TeamSpeak or Mumble) interrupting sound output of already running applications (such as DeaDBeeF), you can solve this by commenting out the line load-module module-role-cork in /etc/pulse/default.pa like shown below:

Then restart PulseAudio:

If the only playback device is the Dummy Output, PulseAudio cannot access your sound devices. It is possible there is an issue with logind giving permissions, see General troubleshooting#Session permissions for more information.

An application might also not have been configured to work with PulseAudio. This happens with FluidSynth for example. To see which application is responsible for a direct access to the sound card via ALSA, run the following command:

Try to close these applications. PulseAudio, if running, should take again precedence over these applications and all the applications relying on PulseAudio should work again like expected.

If the above does not work, try to restart pulseaudio.service.

Restarting pulseaudio.service can also be useful if PulseAudio fails to detect any hardware after resuming from hibernate or suspend.

If you are unable to select 5/7.1 channel output for a working HDMI device, then turning off "stream device reading" in /etc/pulse/default.pa might help.

See #Fallback device is not respected.

If you do not have any output sound and receive dozens of error messages related to a suspended sink from running journalctl -b as root, then backup first and then delete your user-specific PulseAudio folders:

Simultaneous output to two different devices can be very useful. For example, being able to send audio to your A/V receiver via your graphics card's HDMI output, while also sending the same audio through the analogue output of your motherboard's built-in audio. This is much less hassle than it used to be (in this example, we are using GNOME desktop).

Using paprefs, simply select Add virtual output device for simultaneous output on all local sound cards from under the Simultaneous Output tab. Then, under GNOME's sound settings, select the simultaneous output you have just created.

If this does not work, try adding the following to ~/.asoundrc:

This can be useful for users who have multiple sound sources and want to play them on different sinks/outputs. An example use-case for this would be if you play music and also voice chat and want to output music to speakers (in this case Digital S/PDIF) and voice to headphones. (Analog)

This is sometimes auto detected by PulseAudio but not always. If you know that your sound card can output to both Analog and S/PDIF at the same time and PulseAudio does not have this option in its profiles in pavucontrol or veromix, then you probably need to create a configuration file for your sound card.

More in detail you need to create a profile-set for your specific sound card. This is done in two steps mostly.

Create a PulseAudio udev rule.

Now, create a configuration file. If you bother, you can start from scratch and make it saucy. However you can also use the default configuration file, rename it, and then add your profile there that you know works. Less pretty but also faster.

To enable multiple sinks for Asus Xonar Essence STX, you only need to add this in.

This will auto-profile your Asus Xonar Essence STX with default profiles and add your own profile so you can have multiple sinks.

You need to create another profile in the configuration file if you want to have the same functionality with AC3 Digital 5.1 output.

See PulseAudio article about profiles

Some profiles like IEC-958 (i.e. S/PDIF) may not be enabled by default on the selected sink. Each time the system starts up, the card profile is disabled and the pulseaudio daemon cannot select it. You have to add the profile selection to you default.pa file. Verify the card and profile name with:

Then edit the configuration to add the profile

PulseAudio will add this profile the pool of available profiles

This might happen if PulseAudio use the wrong output device. Firstly, set up proper card profile:

Replace alsa_card.pci-0000_00_1f.3 with your card, and output:analog-stereo or output:analog-stereo+input:analog-stereo with your profile, remember to choose the profile with analog. Using shell auto completion could help you a lot. One could also use check available cards and profiles with:

One might also need to set sink port by:

Check available sink ports with:

To keep these setting, add them to PulseAudio's configuration file default.pa.

Although not related to PulseAudio, it is also possible that the card is not powered properly by its USB port, or that it does not provide enough bandwidth.

Try connecting the USB DAC directly to your computer's USB ports, avoiding any hubs or docks.

See Bluetooth headset#Troubleshooting 2.

When starting Audacity, you may find that your headphones no longer work. This can be because Audacity is trying to use them as a recording device. To fix this, open Audacity, then set its recording device to pulse:Internal Mic:0.

Under some circumstances, playback may be distorted, very fast, or freeze, as explained upstream, start Audacity with:

If the solution above does not fix this issue, one may wish to temporarily disable PulseAudio while running Audacity by using the pasuspender command:

Then, be sure to select the appropriate ALSA input and output devices in Audacity.

See also #Some applications do not appear in pavucontrol or play sound and #Setting the default fragment number and buffer size in PulseAudio.

Some games may prevent you from switching the output device. Trying to move the sink with pactl gives the following error:

OpenAL needs to be configured to allow moving the sink:

Check your daemon.conf file for the following options:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

For me, I have my default sample rate changed from 44.1Khz to 384Khz. After that, firefox starts to having problems playing from netflix, hbo max and paramount+ sites. However, spotify is not affected.

If you have the alternate-sample-rate set to the default 48000, firefox will try to send audio in that sample rate. That triggers a pulseaudio to not resample the audio and send it directly to the audio card, which causes problems of playback.

If you set the alternate-sample-rate to the same as the default sample rate, it will trigger pulseaudio to resample the audio from firefox. Then everything works correctly.

Finally, opera or other chromium based browsers were not affected by this issue since it seems that they always re-sample to match what pulseaudio's default sample rate. Firefox in that regard is trying to be more bit-perfect in playback, which is a good thing. But unfortunately run into this bug/issue with pulseaudio.

To work with PulseAudio, some applications require pulseaudio-alsa. This provides the pulse:... playback and recording devices. See PulseAudio#ALSA for details.

pavucontrol is a handy GUI utility for configuring PulseAudio. Under its Configuration tab, you can select different profiles for each of your sound devices e.g. analogue stereo, digital output (IEC958), HDMI 5.1 Surround etc.

However, you may run into an instance where selecting a different profile for a card results in the PulseAudio daemon crashing and auto restarting without the new selection "sticking". If this occurs, use the other useful GUI tool, paprefs, to check under the Simultaneous Output tab for a virtual simultaneous device. If this setting is active (checked), it will prevent you changing any card's profile in pavucontrol. Uncheck this setting, then adjust your profile in pavucontrol prior to re-enabling simultaneous output in paprefs.

PulseAudio usually overwrites the ALSA settings — for example set with alsamixer — at start-up, even when the ALSA daemon is loaded. Since there seems to be no other way to restrict this behaviour, a workaround is to restore the ALSA settings again after PulseAudio has started. Add the following command to .xinitrc or .bash_profile or any other autostart file:

Try resetting PulseAudio:

See also man pages for pax11publish(1) and pulseaudio(1) for more details.

If the pax11publish -d shows error like:

then run pax11publish -r command then could be also good to logout and login again.

If the pulseaudio -vvvv command shows error like:

This can be resolved temporary by:

For permanent use save settings in the 99-sysctl.conf file:

On some systems, PulseAudio may be started multiple times. journalctl will report:

Make sure to use only one method of autostarting applications. pulseaudio includes these files:

Also check user autostart files and directories, such as xinitrc, ~/.config/autostart/ etc.

Known issue: https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/494099

To fix this, enable LFE remixing as described in PulseAudio/Examples#LFE remixing.

If you are unable to set 5.1 surround output in pavucontrol because it only shows "Analog Surround 4.0 Output", open the ALSA mixer and change the output configuration there to 6 channels. Then restart PulseAudio, and pavucontrol will list many more options.

If rtkit does not work, you can manually set up your system to run PulseAudio with real-time scheduling, which can help performance. To do this, add the following lines to /etc/security/limits.conf:

Afterwards, you need to add your user to the pulse-rt group.

PulseAudio does not have a true default device. Instead it uses a "fallback", which only applies to new sound streams. This means previously run applications are not affected by the newly set fallback device.

gnome-control-center, mate-media and paswitchAUR handle this gracefully. Alternatively:

In some cases, the default configuration might flood the network with UDP packets.[5] To fix this problem, launch paprefs and disable Multicast/RTP Sender.[6]

Example scenario: Restarting, stopping, fast forwarding a Youtube video on Firefox 68.0.1 on KDE + Arch might set the "sink" associated with it in PulseAudio to a blank state, and then output sound over laptop speakers. Inconsistently reproducible on Dell 9360.

Fix seems to be to kill and restart PulseAudio.

**Examples:**

Example 1 (unknown):
```unknown
pulseaudio.socket
```

Example 2 (unknown):
```unknown
pulseaudio.service
```

Example 3 (unknown):
```unknown
$ pulseaudio -v
```

Example 4 (unknown):
```unknown
$ alsamixer -c 0
```

---

## Advanced Linux Sound Architecture/Configuration examples

**URL:** https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture/Configuration_examples

**Contents:**
- Upmixing of stereo sources to 7.1 using dmix while saturated sources do not get upmixed
- Surround51 incl. upmix stereo & dmix, swap L/R, bad speaker position in room
- Loopback interface with dmix external interface

The following should serve as a guide for more advanced ALSA setups. The configuration takes place in /etc/asound.conf as mentioned in the main article. None of the following configurations are guaranteed to work.

Bad practice but works fine for almost everything without additional per-program/file customization:

Used to control which output goes to external, loopback, or both. Others have reported working setups without specifying format [1]

**Examples:**

Example 1 (unknown):
```unknown
/etc/asound.conf
```

Example 2 (unknown):
```unknown
# 2008-11-15
#
# This .asoundrc will allow the following:
#
# - upmix stereo files to 7.1 speakers.
# - playback real 7.1 sounds, on 7.1 speakers,
# - allow the playback of both stereo (upmixed) and surround(7.1) sources at the same time.
# - use the 6th and 7th channel (side speakers) as a separate soundcard, i.e. for headphones
#   (This is called the "alternate" output throughout the file, device names prefixed with 'a')
# - play mono sources in stereo (like ekiga) on the alterate output
#
# Make sure you have "8 Channels" and NOT "6 Channels" selected in alsamixer!
#
# Please try the following commands, to make sure everything is working as it should.
#
# To test stereo upmix :      speaker-test -c2 -Ddefault -twav
# To test surround(5.1):      speaker-test -c6 -Dplug:dmix6 -twav
# To test surround(7.1):      speaker-test -c6 -Dplug:dmix8 -twav
# To test alternative output: speaker-test -c2 -Daduplex -twav
# To test mono upmix:         speaker-test -c1 -Dmonoduplex -twav
#
#
# It may not work out of the box for all cards. If it doesnt work for you, read the comments throughout the file.
# The basis of this file was written by wishie of #alsa, and then modified with info from various sources by 
# squisher. Svenstaro modified it for 7.1 output support.

#Define the soundcard to use
pcm.snd_card {
    type hw
    card 0
    device 0
}

# 8 channel dmix - output whatever audio, to all 8 speakers
pcm.dmix8 {
    type dmix
    ipc_key 1024
    ipc_key_add_uid false
    ipc_perm 0660
    slave {
        pcm "snd_card"
        rate 48000
        channels 8
        period_time 0
        period_size 1024
        buffer_time 0
        buffer_size 5120
    }

# Some cards, like the "nforce" variants require the following to be uncommented. 
# It routes the audio to the correct speakers.
#    bindings {
#        0 0
#        1 1
#        2 4
#        3 5
#        4 2
#        5 3
#        6 6
#        7 7
#    }
}

# upmixing - duplicate stereo data to all 8 channels
pcm.ch71dup {
    type route
    slave.pcm dmix8
    slave.channels 8
    ttable.0.0 1
    ttable.1.1 1
    ttable.0.2 1
    ttable.1.3 1
    ttable.0.4 0.5
    ttable.1.4 0.5
    ttable.0.5 0.5
    ttable.1.5 0.5
    ttable.0.6 1
    ttable.1.7 1
}

# this creates a six channel soundcard
# and outputs to the eight channel one
# i.e. for usage in mplayer I had to define in ~/.mplayer/config:
#   ao=alsa:device=dmix6
#   channels=6
pcm.dmix6 {
    type route
    slave.pcm dmix8
    slave.channels 8
    ttable.0.0 1
    ttable.1.1 1
    ttable.2.2 1
    ttable.3.3 1
    ttable.4.4 1
    ttable.5.5 1
    ttable.6.6 1
    ttable.7.7 1
}

# share the microphone, i.e. because virtualbox grabs it by default
pcm.microphone {
    type dsnoop
    ipc_key 1027
    slave {
        pcm "snd_card"
    }
}

# rate conversion, needed i.e. for wine
pcm.2chplug {
    type plug
    slave.pcm "ch71dup"
}
pcm.a2chplug {
    type plug
    slave.pcm "dmix8"
}

# routes the channel for the alternative
# 2 channel output, which becomes the 7th and 8th channel 
# on the real soundcard
#pcm.alt2ch {
#    type route
#    slave.pcm "a2chplug"
#    slave.channels 8
#    ttable.0.6    1
#    ttable.1.7    1
#}

# ekiga is only mono, so route left channel to the right channel
# note: this gets routed to the alternative 2 channels
pcm.mono_playback {
    type route
    slave.pcm "a2chplug"
    slave.channels 8
    # Send audio channel 0 to the L and R speakers at full volume
    #ttable.0.6    1
    #ttable.0.7    1
}

# 'full-duplex' device for use with aoss
pcm.duplex {
    type asym
    playback.pcm "2chplug"
    capture.pcm "microphone"
}

#pcm.aduplex {
#    type asym
#    playback.pcm "alt2ch"
#    capture.pcm "microphone"
#}

pcm.monoduplex {
    type asym
    playback.pcm "mono_playback"
    capture.pcm "microphone"
}

# for aoss
pcm.dsp0 "duplex"
ctl.mixer0 "duplex"

# softvol manages volume in ALSA
# i.e. wine likes this
pcm.mainvol {
    type softvol
    slave.pcm "duplex"
    control {
        name "2ch-Upmix Master"
        card 0
    }
}

#pcm.!default "mainvol"

# set the default device according to the environment
# variable ALSA_DEFAULT_PCM and default to mainvol
pcm.!default {
    @func refer
    name { @func concat 
           strings [ "pcm."
                     { @func getenv
                       vars [ ALSA_DEFAULT_PCM ]
                       default "mainvol"
                     }
           ]
         }
}

# uncomment the following if you want to be able to control
# the mixer device through environment variables as well
#ctl.!default {
#    @func refer
#    name { @func concat 
#           strings [ "ctl."
#                     { @func getenv
#                       vars [ ALSA_DEFAULT_CTL
#                              ALSA_DEFAULT_PCM
#                       ]
#                       default "duplex"
#                     }
#           ]
#         }
#}
```

Example 3 (javascript):
```javascript
pcm.!default {
    type route
## forwards to the mixer pcm defined below
    slave.pcm dmix51
    slave.channels 6

## "Native Channels" stereo, swap left/right
    ttable.0.1 1
    ttable.1.0 1
## original normal left/right commented out
#    ttable.0.0 1
#    ttable.1.1 1

## route "native surround" so it still works but weaken signal (+ RL/RF swap) 
## because my rear speakers are more like random than really behind me
    ttable.2.3 0.7
    ttable.3.2 0.7
    ttable.4.4 0.7
    ttable.5.5 0.7

## stereo => quad speaker "upmix" for "rear" speakers + swap L/R
    ttable.0.3 1
    ttable.1.2 1

## stereo L+R => join to Center & Subwoofer 50%/50%
    ttable.0.4 0.5
    ttable.1.4 0.5
    ttable.0.5 0.5
    ttable.1.5 0.5
## to test: "$ speaker-test -c6 -twav" and: "$ speaker-test -c2 -twav"
}

pcm.dmix51 {
	type dmix
	ipc_key 1024
# let multiple users share
	ipc_key_add_uid false 
# IPC permissions (octal, default 0600)
# I think changing this fixed something - but I'm not sure what.
	ipc_perm 0660 # 
	slave {
## this is specific to my hda_intel. Often hd:0 is just allready it; To find: $ aplay -L 
		pcm surround51 
# this rate makes my soundcard crackle
#		rate 44100
# this rate stops flash in firefox from playing audio, but I do not need that
       rate 48000
       channels 6
## Any other values in the 4 lines below seem to make my soundcard crackle, too
       period_time 0
       period_size 1024
       buffer_time 0
       buffer_size 4096
	}
}
```

Example 4 (unknown):
```unknown
# Use this to output to external
pcm.dmixerout {
 type dmix
 ipc_key 1024
 ipc_key_add_uid false
 slave {
  pcm "hw:CARDNAME,0"
  channels 2
  period_time 0
  period_size 1024
  buffer_size 4096
  rate 44100
 }
 bindings {
  0 0
  1 1
 }
}

# Use this to output to loopback
pcm.dmixerloop {
 type dmix
 ipc_key 2048
 ipc_key_add_uid false
 slave {
  pcm "hw:Loopback,0,0"
  channels 2
  period_time 0
  period_size 1024
  buffer_size 4096
  # If format is absent ALSA gives me slave PCM not usable, but it works w/o it for others
  format S32_LE
  rate 44100
 }
 bindings {
  0 0
  1 1
 }
}

# Sends to the two dmix interfaces
pcm.quad {
 type multi
 # Necessary to have both slaves be dmix; both as hw doesn't give errors, but wouldn't 
 slaves.a.pcm "dmixerout"
 slaves.a.channels 2
 slaves.b.pcm "dmixerloop"
 slaves.b.channels 2
 bindings {
  0 { slave a; channel 0; }
  1 { slave a; channel 1; }
  2 { slave b; channel 0; }
  3 { slave b; channel 1; }
 }
}

# Duplicates to quad, use this to output to loopback & external
pcm.stereo2quad {
 type route
 slave.pcm "quad"
 # ttable.A.B G
 # where A - input channel
 #       B - output channel
 #       G - volume gain (1.0 = original)
 ttable.0.0 1
 ttable.1.1 1
 ttable.0.2 1
 ttable.1.3 1
}

# Listens to loopback
# trying to play to stereo2quad when something is already listening gives me slave PCM not usable
# but listening when something is already playing on stereo2quad works
# and so does starting to listen, then playing to dmixerloop
pcm.loopin {
 type dsnoop
 ipc_key 1111
 ipc_key_add_uid false
 slave.pcm "hw:Loopback,1"
}

pcm.!default {
 type asym
 playback.pcm "plug:stereo2quad"
 capture.pcm "plug:loopin"
}
```

---

## Professional audio

**URL:** https://wiki.archlinux.org/title/Professional_audio

**Contents:**
- Getting started
- Choosing a sound server
  - PipeWire-only
  - PipeWire-as-JACK-Client
  - JACK-only
- JACK parameters
- Latency verification
  - Latency sources
  - Conversion latency
  - Measuring latency

This article describes how to configure your system for multitrack recording, mixing and playing back audio as well as using it to synthesize and generate sounds. Those activities are subsumed under the term professional audio (pro audio) and typically require low latency performance.

Most applications do not need as much high-end hardware, compared to video production or gaming. For more information, refer to The Right Computer System for Digital Audio.

Advanced Linux Sound Architecture (ALSA) is part of the Linux kernel and used for drivers and low-level interface on Arch Linux as the default sound system. ALSA should work out of the box with a default Arch Linux installation. If this is not the case, you must solve the problem before going any further.

Have I set up sound properly?

A vanilla Arch Linux kernel is sufficient for low latency operation in most use cases. #Optimizing system configuration will be necessary only if you are experiencing audio drop-outs (also known as glitches) or if you need (or want) to reach ultra-low latency operations.

To finish with optimizations, these ultra low latency operations may require you to set up a #Realtime kernel.

Although some pro audio software can work with ALSA directly, most of the #Applications mentioned later are JACK Audio Connection Kit or JACK clients. Therefore, you will need to install and setup one of the available sound servers which are outlined soon.

Sound hardware cannot play back sound from more than one application simultaneously. While ALSA can theoretically be configured to mix applications in software this is typically left to a sound server.

As ALSA alone cannot achieve low latencies easily and cannot synchronise multiple audio applications to play on time, starting all at the same time, at the same tempo, etc., and as it can not share audio flux between applications simply by connecting all its clients together, you need not just any sound server, but professional audio class one:

The sound server setup strongly depends on the use case as well as on the workflow and capabilities of some application interaction. JACK was designed to share audio between applications and access an audio device simultaneously by providing the synchronous execution of clients while maintaining constant low latency. Its PipeWire replacement provides a sufficient server for most of the use cases.

This layout illustrates a layer model of the sound server setups to be discussed:

The newer PipeWire framework replaces JACK as well as other sound servers for the sake of simplicity. Thus, it is recommended to first go for a PipeWire-only setup implementing support for JACK clients by installing pipewire-jack and using the vanilla Arch Linux kernel.

For pro audio use, you also have to select the Pro Audio profile installing and using pavucontrol, PulseAudio's mixer.

PipeWire can also be used as a JACK client by installing pipewire-jack-client. This is explained in PipeWire#Run PipeWire on top of native JACK.

The principle of versatility allows you to employ JACK and the #Realtime kernel with #Optimizing system configuration to achieve low latencies for advanced use cases known as JACK-only setup. Using JACK as the only sound server requires any software, that is intended for interaction and audio device access, to run as a JACK client.

Unfortunately, popular desktop applications such as Firefox or most games either dropped JACK support or never implemented it. For that reason this setup should be used for a dedicated pro audio system where non-JACK software can be neglected. If you still need to use software that cannot connect to JACK, refer to Professional audio/Examples#Advanced sound server setups after following the setup described here. Before installing and running JACK you should ensure it can access your audio device.

Is PulseAudio or something else grabbing my device?

If your audio device is not listed, it may be used by PulseAudio (which was probably installed as dependency of another application). Remove those alongside PulseAudio, if you are not intending to use Professional audio/Examples#PulseAudio+JACK in order to make PulseAudio release your audio device.

As JACK version 1 is planned to be "slowly phased out" [1], does not support Symmetric Multiprocessing (SMP), lacks D-Bus and systemd integration, you would want to use version 2 which is available as the jack2 package. If you are going to use a JACK control GUI or a systemd user service for starting the audio graph, also install jack2-dbus.

The article on JACK describes a GUI-based and a shell-based example setup as a point of reference for your own scenario. Parameter values of JACK are discussed in detail in the #JACK parameters section and may depend on other system factors covered by the #Optimizing system configuration section below.

The aim here is to find the best possible combination of buffer size and periods, given the hardware you have. Frames/Period = 256 is a sane starter. For onboard and USB devices, try Periods/Buffer = 3 before lowering both values. Commonly used values are: 256/3, 256/2, 128/3, 128/2.

Also, the sample rate must match the hardware sample rate. To check what sample and bit rates your device supports:

Replace card0 and codec#0 depending on what you have. You will be looking for rates or VRA in Extended ID. A common sample rate across many of today's devices is 48000 Hz. Others common rates include 44100 Hz, 96000 Hz and 192000 Hz.

Almost always, when recording or sequencing with external gear is concerned, realtime is a must. Also, you may like to set maximum priority (at least 10 lower than system limits defined in /etc/security/limits.d/99-realtime-privileges.conf; the highest is for the device itself).

Start jack with the options you just found out:

qjackctl, cadenceAUR, patchageAUR and studio-controls-gitAUR can all be used to as GUIs to monitor JACK's status and simplify its configuration.

JACK parameters are most significant for controlling the round-trip delay (RTD). In the context of this article that is the overall time it takes for an audio signal to be recorded, processed and played back. The next subsection deals with theoretical background on the sources of latency adding up to the RTD. If you are already familiar with that, you can go to #Measuring latency to verify your RTD or skip this section completely.

Consider a typical recording situation of a singer performance. The voice is being captured with a microphone as it propagates trough the air with the speed of sound. An analog-to-digital-conversion enables the electrical signal to be recorded by a computer for digital signal processing. Finally, a digital-to-analog conversion returns the signal to be played back at the singer's headphones for monitoring similar to stage monitor system usage.

In that voice recording situation there are five significant latency sources constructing the RTD and occuring in the following order:

The first and last latency source is hard to change as a particular distance is technically necessary to create an intended sound during recording or playback, respectively. Additionally, when using closer miking for capturing and headphones for monitoring both sound propagation latencies are typically within the range of a few microseconds which is not noticeable by humans. Thus, an objective for RTD minimization is to reduce the other sources of latency.

In theory JACK maintains a constant low latency by using fixed values (frames, periods, sample rate) for sampling and buffering of audio to be converted analog-to-digital and vice versa. The latency occurring in the capturing process is described by the following equation:

Lc: Capture latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), f: Sample rate in Hertz (Hz).

The playback latency is also employing the periods value:

Lp: Playback latency in milliseconds (ms), n: Frames or buffer (multiples of 2, starting at 16), p: Periods, f: Sample rate in Hertz (Hz).

As already stated before, the capabilities of the audio interface define working combinations. You have to trial and error to find a setup. Sure, it is a trade-off between xrun prevention and achieving low latency, but recent audio interfaces can be used at high sample rates (up to 192 kHz) to deal with that requirement. The audio flux of JACK clients in the digital domain is about zero and thus, negligible for latency measurements [2].

Once you have set up #JACK parameters you might want to verify the RTD described above. For example, using a frames or buffer size of n = 128, a periods value of p = 2, and a sample rate of f = 48000 results in a capture latency of about Lc = 2,666... ms and a playback latency of about Lp = 5,333... ms summing up to a total round-trip delay of RTD = 8 ms.

The jack_delay utility by Fons Adriaensen measures RTD by emitting test tones out a playback channel and capturing them again at a capture channel for measuring the phase differences to estimate the round-trip time the signal has taken through the whole chain. Use an appropriate cable to connect an input and output channel of your audio device or put a speaker close to a microphone as described by JACK Latency tests.

For example, running jack_delay for a JACK-only setup using a cable connection between the ports playback_1 and capture_1 (the description may differ depending on your hardware) to close the loop, as well as the values discussed before yields the following insights:

As the output indicates further optimization of JACK can be done by using the parameters -I 19 and -O 19 to compensate for the reported extra loopback latency in the chain:

This article or section needs expansion.

"Realtime" in the context of an operating system is defined that the results of a computation are available within a fixed period of time. Only in a broader sense does it mean "time running simultaneously with reality", for example, that a sound is produced immediately in response to musical user input. The latter is called "low latency" and its setup is one of the main goals of this article.

Since a while ago, the stock Linux kernel (with CONFIG_PREEMPT=y, default in Arch Linux vanilla kernel) has proven to be adequate for low latency operation. Latency in an operating system context is the time between the moment an interrupt occurs in hardware, and the moment the corresponding interrupt-thread gets running. Unfortunately, some device drivers can introduce higher latencies. So depending on your hardware, drivers, and requirements, you might want a kernel with hard realtime capabilities.

The RT_PREEMPT patch by Ingo Molnar and Thomas Gleixner is an interesting option for hard and firm realtime applications, reaching from professional audio to industrial control. Most audio-specific Linux distributions ships with this patch applied. A realtime-preemptible kernel will also make it possible to tweak priorities of IRQ handling threads and help ensure smooth audio almost regardless of the load.

Install either the linux-rt or linux-rt-lts package.

If you are going to compile your own kernel as a realtime kernel, remember that removing modules/options does not equate to a "leaner and meaner" kernel. It is true that the size of the kernel image is reduced, but in today's systems it is not as much of an issue as it was back in 1995.

In any way, you should also ensure that:

If you truly want a slim system, we suggest you go your own way and deploy one with static /devs. You should, however, set your CPU architecture. Selecting "Core 2 Duo" for appropriate hardware will allow for a good deal of optimisation, but not so much as you go down the scale.

General issue(s) with (realtime) kernels:

You may want to consider the following system optimizations:

You may also want to maximize the PCI latency timer of the PCI sound card and raise the latency timer of all other PCI peripherals (default is 64).

E.g. SOUND_CARD_PCI_ID=03:00.0.

The SOUND_CARD_PCI_ID can be obtained like so:

Arch Linux provides the package group pro-audio holding all relevant (semi-) professional applications. All applications in the pro-audio package group are JACK clients. Also lv2-plugins, ladspa-plugins, dssi-plugins, vst-plugins and clap-plugins are subgroups of the pro-audio group.

An overview and brief information on some applications is found in List of applications/Multimedia#Audio. Especially the categories Digital audio workstations, Audio effects and Music trackers, as well as Audio synthesis environments and Sound generators provide examples of pro audio software for recording, mixing, mastering, and sound design. Other categories include Scorewriters, Audio editors, Audio converters, and DJ software.

Packages not (yet) in the official repositories can be found in proaudio. Browse the list of packages to find the application you need or request packaging of your desired applications via GitHub.

The majority of sound cards and audio devices will work with no extra configuration or packages, simply set JACK to use the desired one.

This is not true for all devices, have a look at the Category:Sound, /Hardware as well as Envy24control#Supported cards for those special cases.

**Examples:**

Example 1 (unknown):
```unknown
$ speaker-test
```

Example 2 (unknown):
```unknown
#PipeWire-only       #PipeWire-as-JACK-Client       #JACK-only
┌──────────────┐          ┌──────────────┐        ┌──────────────┐
│ Applications │          │ Applications │        │ Applications │
├──────────────┤          ├──────────────┤        ├──────────────┤
│   PipeWire   │          │ PipeWire+JACK│        │     JACK     │
├──────────────┤          ├──────────────┤        ├──────────────┤
│     ALSA     │          │     ALSA     │        │     ALSA     │
└──────────────┘          └──────────────┘        └──────────────┘
```

Example 3 (unknown):
```unknown
$ lsof +c 0 /dev/snd/pcm* /dev/dsp*
```

Example 4 (unknown):
```unknown
$ fuser -fv /dev/snd/pcm* /dev/dsp*
```

---

## tp_smapi

**URL:** https://wiki.archlinux.org/title/Tp_smapi

**Contents:**
- Supported laptops
- Installation
- Features
  - Control battery charging
    - General way
    - Check whether settings were accepted
  - Protect the hard disk from drops
- Workaround for partially supported laptops
  - 1st option, custom script
  - 2nd option, tpacpi-bat

tp_smapi is a set of kernel modules that retrieves information from and conveys commands to the hardware of many ThinkPad laptops before Ivy Bridge processors.

This information is presented through the /sys/devices/platform/smapi filesystem. Much like the /proc filesystem, you can read and write information to these files to get information about and send commands to the hardware. tp_smapi is highly recommended if you are using a supported ThinkPad laptop.

First check whether your laptop is supported. Thinkwiki has a comprehensive list of all supported Thinkpads. In case your TP does not support stop_threshold but only start_threshold please go here #Workaround for partially supported laptops for a decent workaround.

If you are installing on a recent Thinkpad that has an Ivy Bridge processor or later (any of the *30, *40 or *50 models), tp_smapi will not work: use tpacpi-batAUR.

Install the tp_smapi package for linux or tp_smapi-lts for linux-lts. For all other kernels (e.g., linux-zen), consider using tp_smapi-dkmsAUR.

tp_smapi (and its variations) provide the following kernel modules:

After a reboot, tp_smapi and its dependencies will get autoloaded and the sysfs interface under /sys/devices/platform/smapi/ should be fully functional.

Here are a couple of useful things you can do using tp_smapi.

It is bad for most laptop batteries to hold a full charge for long periods of time. [1] You should try to keep your battery in the 40-80% charged range, unless you need the battery life for extended periods of time.

tp_smapi lets you control the start and stop charging threshold to do just that. Run these commands to set these to good values:

This will cause the battery to begin charging when it falls below 40% charge and stop charging once it exceeds 80% charge. This will extend the lifetime of your battery.

Note that when you remove and re-insert the battery, these thresholds may be reset to their default values. To work around this, create a script to set these values, and make this script run both at startup and when a battery is inserted. More specific instructions follow.

Make it executable. With this script to set a battery threshold is very simple, just type (if set_battery_thresholds is the name of the script):

Or run it with no arguments to default to BAT0, and thresholds of 40% and 80%.

Let systemd execute the script at startup. Thus, create the tp_smapi_set_battery_thresholds.service unit and enable/start it afterwards:

You can also make it run when a battery is inserted. This requires that acpid is installed and running. Edit /etc/acpi/handler.sh:

To check whether your settings were accepted check the output of the following:

tp_smapi includes a driver to read the accelerometer in your laptop to detect drops and other events that could cause damage to your hard drive. See the HDAPS page for more information on this useful feature.

For partially supported laptops you can still gain control over your battery. First check what is actually supported:

If start_charge_thresh is supported but not stop_charge_thresh but you still want to have your computer stop charging your battery you might have other options.

Note: None of the first two options works on T42p. The third one works on E540.

Now copy the following script, make it executable, adjust the values to your liking and run it every couple of minutes as a root cron.

To control the battery charging thresholds, install the Perl script tpacpi-batAUR.

Manually set the thresholds by calling

The example values 40 and 80 given here are in percent of the full battery capacity. Adjust them to your own needs. You may also want to add these lines to a systemd tmpfile to set them at startup.

The manual setting of thresholds via the command tpacpi-bat is not permanent. To set the thresholds permanently, edit the start and end thresholds accordingly in /etc/conf.d/tpacpi.

Kernel 4.17 added the option to adjust battery charging thresholds for ThinkPads directly.

Note that if you try to display the values, you will get only the last one set (start in the example), with 128 added to it. This is a known issue, but the true value is really set, as you can see from battery behaviour. Other interesting parameters can be found under /sys/class/power_supply/BAT0/.

**Examples:**

Example 1 (unknown):
```unknown
/sys/devices/platform/smapi
```

Example 2 (unknown):
```unknown
/sys/devices/platform/smapi/
```

Example 3 (unknown):
```unknown
# echo 40 > /sys/devices/platform/smapi/BAT0/start_charge_thresh
# echo 80 > /sys/devices/platform/smapi/BAT0/stop_charge_thresh
```

Example 4 (unknown):
```unknown
/usr/sbin/set_battery_thresholds
```

---

## Laptop/Dell

**URL:** https://wiki.archlinux.org/title/Laptop/Dell

**Contents:**
- Software
- Model list
  - Alienware
  - Inspiron
  - Latitude
  - Precision
  - Studio
  - Vostro
  - XPS
  - G3

Dell offers in-house Linux support for a subset of hardware, contributing to the dell-smm-hwmon kernel module (refer to it's documentation here[1]) and providing native Linux utilities to control hardware on supported devices. These utilities include:

ACPI platform_profiles are natively supported on newer kernels which enables setting thermal modes without Dell specific software.[2]

Dell also makes firmware updates for some devices available via the Linux Vendor firmware Service (LVFS).

CPU would sometimes get stuck at minimum frequency, fixed with Lenovo ThinkPad T480#CPU stuck at minimum frequency

**Examples:**

Example 1 (unknown):
```unknown
dell-smm-hwmon
```

Example 2 (unknown):
```unknown
smbios-battery-ctl
```

Example 3 (unknown):
```unknown
smbios-keyboard-ctl
```

Example 4 (unknown):
```unknown
smbios-lcd-brightness
```

---

## Power management

**URL:** https://wiki.archlinux.org/title/Power_management

**Contents:**
- Userspace tools
  - Console
  - Graphical
- ACPI events
  - Power managers
  - xss-lock
- Power saving
  - Print power settings
  - Processors with Intel Hardware P-state support
  - Audio

Power management is a feature that turns off the power or switches system components to a low-power state when inactive.

In Arch Linux, power management consists of two main parts:

These tools allow you to change a lot of settings without the need to edit config files by hand. Only run one of these tools to avoid possible conflicts as they all work more or less similarly. Have a look at the power management category to get an overview on what power management options exist in Arch Linux.

These are the more popular scripts and tools designed to help power saving:

systemd handles some power-related ACPI events, whose actions can be configured in /etc/systemd/logind.conf or /etc/systemd/logind.conf.d/*.conf — see logind.conf(5). On systems with no dedicated power manager, this may replace the acpid daemon which is usually used to react to these ACPI events.

The specified action for each event can be one of ignore, poweroff, reboot, halt, suspend, hibernate, hybrid-sleep, suspend-then-hibernate, lock or kexec. In case of hibernation and suspension, they must be properly set up. If an event is not configured, systemd will use a default action.

To apply changes, reload systemd-logind.service.

Some desktop environments include power managers which inhibit (temporarily turn off) some or all of the systemd ACPI settings. If such a power manager is running, then the actions for ACPI events can be configured in the power manager alone. Changes to /etc/systemd/logind.conf or /etc/systemd/logind.conf.d/*.conf need be made only if you wish to configure behaviour for a particular event that is not inhibited by the power manager.

Note that if the power manager does not inhibit systemd for the appropriate events you can end up with a situation where systemd suspends your system and then when the system is woken up the other power manager suspends it again. The power managers of GNOME, MATE, Plasma and Xfce issue the necessary inhibited commands. If the inhibited commands are not being issued, such as when using acpid or others to handle ACPI events, set the Handle options to ignore. See also systemd-inhibit(1).

xss-lock subscribes to the systemd-events suspend, hibernate, lock-session, and unlock-session with appropriate actions (run locker and wait for user to unlock or kill locker). xss-lock also reacts to DPMS events and runs or kills the locker in response.

Autostarting the following for example:

This section is a reference for creating custom scripts and power saving settings such as by udev rules. Make sure that the settings are not managed by some other utility to avoid conflicts.

Almost all of the features listed here are worth using whether or not the computer is on AC or battery power. Most have negligible performance impact and are just not enabled by default because of commonly broken hardware/drivers. Reducing power usage means reducing heat, which can even lead to higher performance on a modern Intel or AMD CPU, thanks to dynamic overclocking.

This script prints power settings and a variety of other properties for USB and PCI devices. Note that root permissions are needed to see all settings.

This article or section is a candidate for merging with CPU frequency scaling.

The available energy preferences of an Intel Hardware P-state (HWP) supported processor are default, performance, balance_performance, balance_power, power.

This can be validated by running

To conserve more energy, you can edit the configuration by creating the following file:

See the x86_energy_perf_policy(8) man page for more details on energy-performance policy in Intel processors. Also see systemd-tmpfiles(8) and tmpfiles.d(5) man pages for temporary files/directories details.

Whether power saving is turned on by default depends on a given driver, e.g. it is on for HD Audio. Identify the module in use, then run

and look for a kernel module parameter (like power_save) that adjusts or disables power-saving feature.

To disable Bluetooth completely, blacklist the btusb and bluetooth modules.

Alternatively, create the following udev rules:

To turn off Bluetooth only temporarily, use rfkill(8):

If you will not use integrated web camera then blacklist the uvcvideo module.

This section uses configurations in /etc/sysctl.d/, which is "a drop-in directory for kernel sysctl parameters." See The New Configuration Files and more specifically sysctl.d(5) for more information.

This article or section needs expansion.

The NMI watchdog is a debugging feature to catch hardware hangs that cause a kernel panic. On some systems it can generate a lot of interrupts, causing a noticeable increase in power usage. To list these interrupts per CPU core since last boot, you can use:

To turn the hardlockup detector off, use:

or add nmi_watchdog=0 to the kernel line.

Alternatively add nowatchdog to the kernel line to disable both hard and soft lockup detectors. See [3]

Increasing the virtual memory dirty writeback time helps to aggregate disk I/O together, thus reducing spanned disk writes, and increasing power saving. To set the value to 60 seconds (default is 5 seconds):

To do the same for journal commits on supported filesystems (e.g. ext4, btrfs...), use commit=60 as an option in fstab.

Note that this value is modified as a side effect of the Laptop Mode setting below. See also sysctl#Virtual memory for other parameters affecting I/O performance and power saving.

See the kernel documentation on the laptop mode "knob" - "A sensible value for the knob is 5 seconds".

Wake-on-LAN can be a useful feature, but if you are not making use of it then it is simply draining extra power waiting for a magic packet while in suspend. You can adapt the Wake-on-LAN#udev rule to disable the feature for all ethernet interfaces. To enable powersaving with iw on all wireless interfaces:

The name of the configuration file is important. With the use of persistent device names in systemd, the above network rule, named lexicographically after 80-net-setup-link.rules, is applied after the device is renamed with a persistent name e.g. wlan0 renamed wlp3s0. Be aware that the RUN command is executed after all rules have been processed and must anyway use the persistent name, available in $name for the matched device.

Additional power saving functions of Intel wireless cards with iwlwifi driver can be enabled by passing the correct parameters to the kernel module. Making them persistent can be achieved by adding the lines below to the /etc/modprobe.d/iwlwifi.conf file:

This option will probably increase your median latency:

On kernels < 5.4 you can use this option, but it will probably decrease your maximum throughput:

Depending on your wireless card one of these two options will apply.

You can check which one is relevant by checking which of these modules is running using

Keep in mind that these power saving options are experimental and can cause an unstable system.

If using iwd, power-saving can be disabled for all Wi-Fi devices with the following config file:

You can also replace * with a specific driver name, see iwd.config(5) § SETTINGS.

If using NetworkManager, power-saving can be disabled globally for every connection with a config file, for example:

At boot, the BIOS enables or disables ASPM based on hardware support. To check for support:

Fetch available ASPM policies and the current system default using the following:

ASPM might be disabled for the following reasons [4]:

If you believe that your hardware has support for ASPM despite the above, it can be force-enabled for the kernel to handle with the pcie_aspm=force kernel parameter.

As long as ASPM is supported and enabled, it is possible to select a desired policy for the current session. For example, switch to powersupersave for the current session by doing the following:

To configure a specific ASPM state to enable upon system boot (using powersupersave as an example), add pcie_aspm.policy=powersupersave as a kernel parameter.

The rule above powers down unused devices.

Some devices will not wake up again. To allow runtime power management only for devices that are known to work, use simple matching against vendor and device IDs (use lspci -nn to get these values):

Alternatively, to blacklist devices that are not working with PCI runtime power management and enable it for all other devices:

The Linux kernel can automatically suspend USB devices when they are not in use. This can sometimes save quite a bit of power, however some USB devices are not compatible with USB power saving and start to misbehave (common for USB mice/keyboards). udev rules based on whitelist or blacklist filtering can help to mitigate the problem.

The example is enabling autosuspend for all USB devices except for keyboards and mice:

To allow autosuspend only for devices that are known to work, use simple matching against vendor and product IDs (use lsusb to get these values):

Alternatively, to blacklist devices that are not working with USB autosuspend and enable it for all other devices:

The default autosuspend idle delay time is controlled by the autosuspend parameter of the usbcore built-in kernel module. To set the delay to 5 seconds instead of the default 2 seconds, add the following kernel parameter for your boot loader.

Similarly to power/control, the delay time can be fine-tuned per device by setting the power/autosuspend attribute. This means, alternatively, autosuspend can be disabled by setting power/autosuspend to -1 (i.e., never autosuspend):

See the Linux kernel documentation for more information on USB power management.

The current setting can be read from or written to /sys/class/scsi_host/host*/link_power_management_policy as follows:

You can configure link_power_management_policy settings persistently by adding a udev rules file, for example:

See hdparm#Power management configuration for drive parameters that can be set.

Power saving is not effective when too many programs are frequently writing to the disk. Tracking all programs, and how and when they write to disk is the way to limit disk usage. Use iotop to see which programs use the disk frequently. See Improving performance#Storage devices for other tips.

Small adjustments such as setting the noatime option can also help. If enough RAM is available, consider disabling or limiting swappiness as it has the possibility to limit a good number of disk writes.

For Seagate drives with PowerChoice technology, tricks setting APM via hdparm will not work due to the EPC (Extended Power Conditions) feature. Rather than setting APM, you can install openseachestAUR and fully disable EPC like so (replace X with actual drive letter):

Last invocation will give the following summary:

Zeroes in the first column confirm that parking and spindown were disabled successfully

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

This article or section is a candidate for merging with Laptop#Power management.

Since systemd users can suspend and hibernate through systemctl suspend or systemctl hibernate and handle acpi events with /etc/systemd/logind.conf, it might be interesting to remove pm-utils and acpid. There is just one thing systemd cannot do (as of systemd-204): power management depending on whether the system is running on AC or battery. To fill this gap, you can create a single udev rule that runs a script when the AC adapter is plugged and unplugged:

Examples of powersave scripts:

The above udev rule should work as expected, but if your power settings are not updated after a suspend or hibernate cycle, you should add a script in /usr/lib/systemd/system-sleep/ with the following contents:

Do not forget to make it executable!

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The suspend, poweroff and hibernate button presses and lid close events are handled by logind as described in #ACPI events.

If you are using polkit, users with non-remote session can issue power-related commands as long as the session is not broken.

To check if your session is active:

The user can then use systemctl commands in the command line, or add them to menus:

Other commands can be used as well, including systemctl suspend and systemctl hibernate. See the System Commands section in systemctl(1).

Install sudo, and configure it to give the user root privileges. The user will then be able to use the sudo systemctl commands (e.g. sudo systemctl poweroff, sudo systemctl reboot, sudo systemctl suspend and sudo systemctl hibernate). See the System Commands section in systemctl(1)

If users should only be allowed to use shutdown commands, but not have other privileges, add the following to the end of /etc/sudoers using the visudo command as root. Substitute user for your username and hostname for the machine's hostname.

Now your user can shutdown with sudo systemctl poweroff, and reboot with sudo systemctl reboot. Users wishing to power down a system can also use sudo systemctl halt. Use the NOPASSWD: tag only if you do not want to be prompted for your password.

**Examples:**

Example 1 (unknown):
```unknown
/etc/systemd/logind.conf
```

Example 2 (unknown):
```unknown
/etc/systemd/logind.conf.d/*.conf
```

Example 3 (unknown):
```unknown
hybrid-sleep
```

Example 4 (unknown):
```unknown
suspend-then-hibernate
```

---

## Hardware video acceleration

**URL:** https://wiki.archlinux.org/title/Hardware_video_acceleration

**Contents:**
- Installation
  - Intel
    - VA-API
    - Vulkan Video
    - Intel Video Processing Library (Intel VPL)
  - NVIDIA
  - AMD/ATI
  - Translation layers
- Verification
  - Verifying VA-API

Hardware video acceleration makes it possible for the video card to decode/encode video, thus offloading the CPU and saving power.

There are several ways to achieve this on Linux:

For comprehensive overview of driver and application support see #Comparison tables.

Intel graphics open-source drivers support VA-API:

Also see VAAPI supported hardware and features.

ANV open-source vulkan driver provides Vulkan Video support via vulkan-intel.

For Intel VPL, install the base library libvpl, and at least one of the following runtime implementations:

Nouveau open-source driver supports both VA-API and VDPAU:

NVIDIA proprietary driver supports via nvidia-utils:

AMD and ATI open-source drivers support both VA-API and VDPAU via mesa:

RADV open-source vulkan driver provides Vulkan Video support via vulkan-radeon.

AMDGPU PRO proprietary driver is built on top of AMDGPU driver and supports both VA-API and VDPAU in addition to AMF.

Your system may work perfectly out-of-the-box without needing any configuration. Therefore it is a good idea to start with this section to see that it is the case.

Verify the settings for VA-API by running vainfo, which is provided by libva-utils:

VAEntrypointVLD means that your card is capable to decode this format, VAEntrypointEncSlice means that you can encode to this format.

In this example the i965 driver is used, as you can see in this line:

If the following error is displayed when running vainfo:

You need to configure the correct driver, see #Configuring VA-API.

Install vdpauinfo to verify if the VDPAU driver is loaded correctly and retrieve a full report of the configuration:

Install vulkan-tools and use vulkaninfo to verify if the video processing extensions are available:

Although the video driver should automatically enable hardware video acceleration support for both VA-API and VDPAU, it may be needed to configure VA-API/VDPAU manually. Only continue to this section if you went through #Verification.

The default driver names, used if there is no other configuration present, are guessed by the system. However, they are often hacked together and may not work. The guessed value will be printed in the Xorg log file, which is ~/.local/share/xorg/Xorg.0.log if rootless, or /var/log/Xorg.0.log if Xorg is running as root. To search the log file for the values of interest:

In this case radeonsi is the default for both VA-API and VDPAU.

This does not represent the configuration however. The values above will not change even if you override them.

You can override the driver for VA-API by using the LIBVA_DRIVER_NAME environment variable:

You can override the driver for VDPAU by using the VDPAU_DRIVER environment variable.

The correct driver name depends on your setup:

Note that some older GPU models do not have Vulkan Video support in Mesa. Force-enabling Vulkan Video support on such GPUs may result in crashes with some applications (for example, mpv).

Multimedia frameworks:

Multimedia recording/streaming:

You need to set VDPAU_DRIVER variable to point to correct driver. See #Configuring VDPAU.

An error along the lines of libva: /usr/lib/dri/i965_drv_video.so init failed is encountered. This can happen because of improper detection of Wayland. One solution is to unset $DISPLAY so that mpv, MPlayer, VLC, etc. do not assume it is X11. Another mpv-specific solution is to add the parameter --gpu-context=wayland.

This error can also occur if you installed the wrong VA-API driver for your hardware.

When experiencing video decoding corruption or distortion with AMDGPU driver, set allow_rgb10_configs=false as an environment variable. [4]

If you encounter the following error:

Try installing the intel-media-driver-legacyAUR instead of the non-legacy one, which works with intel-compute-runtime-legacyAUR. [5]

**Examples:**

Example 1 (unknown):
```unknown
mpv --hwdec=auto video_filename
```

Example 2 (unknown):
```unknown
intel_gpu_top
```

Example 3 (unknown):
```unknown
intel_gpu_top
```

Example 4 (unknown):
```unknown
libva info: VA-API version 0.39.4
libva info: va_getDriverName() returns 0
libva info: Trying to open /usr/lib/dri/i965_drv_video.so
libva info: Found init function __vaDriverInit_0_39
libva info: va_openDriver() returns 0
vainfo: VA-API version: 0.39 (libva 1.7.3)
vainfo: Driver version: Intel i965 driver for Intel(R) Skylake - 1.7.3
vainfo: Supported profile and entrypoints
      VAProfileMPEG2Simple            :	VAEntrypointVLD
      VAProfileMPEG2Simple            :	VAEntrypointEncSlice
      VAProfileMPEG2Main              :	VAEntrypointVLD
      VAProfileMPEG2Main              :	VAEntrypointEncSlice
      VAProfileH264ConstrainedBaseline:	VAEntrypointVLD
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSlice
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSliceLP
      VAProfileH264Main               :	VAEntrypointVLD
      VAProfileH264Main               :	VAEntrypointEncSlice
      VAProfileH264Main               :	VAEntrypointEncSliceLP
      VAProfileH264High               :	VAEntrypointVLD
      VAProfileH264High               :	VAEntrypointEncSlice
      VAProfileH264High               :	VAEntrypointEncSliceLP
      VAProfileH264MultiviewHigh      :	VAEntrypointVLD
      VAProfileH264MultiviewHigh      :	VAEntrypointEncSlice
      VAProfileH264StereoHigh         :	VAEntrypointVLD
      VAProfileH264StereoHigh         :	VAEntrypointEncSlice
      VAProfileVC1Simple              :	VAEntrypointVLD
      VAProfileVC1Main                :	VAEntrypointVLD
      VAProfileVC1Advanced            :	VAEntrypointVLD
      VAProfileNone                   :	VAEntrypointVideoProc
      VAProfileJPEGBaseline           :	VAEntrypointVLD
      VAProfileJPEGBaseline           :	VAEntrypointEncPicture
      VAProfileVP8Version0_3          :	VAEntrypointVLD
      VAProfileVP8Version0_3          :	VAEntrypointEncSlice
      VAProfileHEVCMain               :	VAEntrypointVLD
      VAProfileHEVCMain               :	VAEntrypointEncSlice
```

---

## Laptop/MSI

**URL:** https://wiki.archlinux.org/title/Laptop/MSI

**Contents:**
- Model list
- Tips and tricks
  - BisonCam
  - Embedded Controller
  - Intel Management Engine
  - Advanced UEFI settings

Advanced UEFI settings needed to disable the dGPU

Models with a BisonCam integrated webcam just need to activate it with Fn+F6.

Some models are supported by a community developed driver.

If you need the added functionality, you can install it with msi-ec-dkms-gitAUR or msi-ec-gitAUR.

Intel ME firmware needs to be updated from Windows.

See Windows PE/Tips and tricks#Update Intel Management Engine firmware with the files provided by MSI on their BIOS Update webpage.

It may still reported as vulnerable after update. Intel ME may be disabled in the advanced UEFI settings.

An unlocked version of the UEFI settings is available on most MSI laptops since 2019. To access it, press Alt+RCtrl+RShift then F2 once inside the UEFI.

**Examples:**

Example 1 (unknown):
```unknown
Alt+RCtrl+RShift
```

---

## PipeWire/Examples

**URL:** https://wiki.archlinux.org/title/PipeWire/Examples

**Contents:**
- Surround sound systems
  - Splitting front/rear
- Echo cancellation
- Mixing additional audio into the microphone's audio

When using PipeWire as a PulseAudio/JACK replacement, you can set up PipeWire to replicate the PulseAudio example for splitting front/rear. Doing this allows you to send audio streams using PulseAudio to a separate sink for speakers or headphones.

Connect speakers to the line-out port and headphones to the rear port. In pavucontrol set the soundcard used to Analog Surround 4.0 Output. Then using the following commands, make new sinks for the speakers and for the headphones, link the speakers to the front channels and link the headphones to the rear channels:

object.linger=1 keeps the sinks alive after the creating client disconnects. You can name sink_name whatever you want.

In order to unload module, you can use pw-cli destroy ID, where ID is output of pactl load-module command. Unloading individual modules through pactl unload-module is not currently supported [1]. However, you may use it to unload all module-null-sink modules using pactl unload-module module-null-sink.

Using jack_connect, connect the monitors of the new sinks to the sound card's playback ports. Find out the name of the channels by running pw-link -iol[2].

To individually control the volumes, one option is to use ALSA utilities—such as amixer(1)—to control Front and Rear/Surround (ALSA naming) channels. A script to automatically do that depending on what is your currently default PulseAudio sink can be found here.

PipeWire can remove your speakers' sounds from your microphone in real time, which makes it possible to attend audio chats without having to use headphones, even while other applications are playing audio.

Usually, voice chat applications do cancel out feedback, but they are only aware of audio that goes through them. As an example, if another voice chat attendant talks on your speakers, the chat application "knows" about it and is able to selectively erase this noise from your microphone, which would otherwise be repeated back into the voice chat as an annoying echo. The problems with this approach tend to start when other applications are playing to your speakers, because this audio the voice chat does not know about, and the other participants may hear it and complain. Example situations:

This is the problem that system-wide echo cancellation solves; instead of having the voice chat app suppress the echo – and fail in the above situations – you make PipeWire do that, which innately "knows about" all audio that is played on the speakers.

Assuming a blank PipeWire configuration, system-wide echo cancellation can be enabled by creating a world-readable configuration file in /etc/pipewire/pipewire.conf.d/ whose name ends with ".conf", for example 60-echo-cancel.conf:

Default values for "aec.args" can be found here, just search for "webrtc." in the "aec-webrtc.cpp".

Configuration changes such as these require a PipeWire restart (i.e. the pipewire.service and pipewire-pulse.service user unit) to become effective.

The echo cancellation example above can be extended to provide a virtual sink that copies audio into your microphone.

It is a re-creation of PulseAudio/Examples#Mixing additional audio into the microphone's audio and solves the same use-case.

To achieve this you additionally load two instances of the "Combine stream" module, as shown below.

Currently, after each reboot or PipeWire restart the setup requires manual user action in e.g. Helvum to complete it; see the "TODO" comment in the configuration example.

**Examples:**

Example 1 (unknown):
```unknown
pavucontrol
```

Example 2 (unknown):
```unknown
pactl load-module module-null-sink sink_name=speakers object.linger=1 media.class=Audio/Sink channel_map=FL,FR
 pactl load-module module-null-sink sink_name=headphones object.linger=1 media.class=Audio/Sink channel_map=RL,RR
```

Example 3 (unknown):
```unknown
object.linger=1
```

Example 4 (unknown):
```unknown
pw-cli destroy ID
```

---

## Advanced Linux Sound Architecture

**URL:** https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture

**Contents:**
- Installation
  - Firmware
  - ALSA utilities
  - ALSA and systemd
  - User privileges
  - OSS emulation
- Unmuting the channels
  - Unmute with amixer
  - Unmute with alsamixer
  - Unmute 5.1/7.1 sound

The Advanced Linux Sound Architecture (ALSA) provides kernel driven sound card drivers. It replaces the original Open Sound System (OSS).

Besides the sound device drivers, ALSA also bundles a user space driven library for application developers. They can then use those ALSA drivers for high level API development. This enables direct (kernel) interaction with sound devices through ALSA libraries.

The ALSA drivers are part of the Linux kernel. The ALSA library (alsa-lib) is usually installed as a dependency. Therefore, manual installation is not necessary.

udev will automatically detect your hardware and select needed drivers at boot time, therefore, your sound should already be working.

However, your sound may be initially muted. If it is, see #Unmuting the channels.

The Sound Open Firmware (SOF) (sof-firmware) is usually required for laptops—they tend to utilize Cadence Tensilica Xtensa architecture DSPs, see the list of the supported platforms. In case of the missing firmware the journal will provide messages such as:

For more SOF troubleshooting information, see Overview of Intel hardware platforms.

The linux-firmware-cirrus package is needed for laptops with Cirrus Logic smart amplifiers. See also:

The linux-firmware-intel package is needed for some Intel audio devices.

The alsa-firmware package contains firmware that may be required for certain sound cards.

See also #Cards and modules and Linux firmware.

Install the alsa-utils package. This contains (among other utilities) the alsamixer(1) and amixer(1) utilities. amixer is a shell command to change audio settings, while alsamixer provides a more intuitive ncurses based interface for audio device configuration.

The alsa-utils package comes with systemd unit configuration files alsa-restore.service and alsa-state.service by default.

These are automatically installed and activated during installation (via package provided symlink to sound.target). The options are as follows:

Evidently, both methods are mutually exclusive. You can decide for one of the two approaches depending on your requirements. To edit these units, see systemd#Editing provided units. You can check their status using systemctl.

For further information, see alsactl(1).

Local users have permission to play audio and change mixer levels. To allow remote users to use ALSA, you need to add those users to the audio group.

OSS emulation is the ability to intercept OSS calls and reroute them through ALSA instead. This emulation layer is useful e.g. for legacy applications which try to open /dev/dsp and write sound data to them directly. Without OSS or the emulation library, /dev/dsp will be missing, and the application will not produce any sound.

If you want OSS applications to work with dmix, install the alsa-oss package as well.

Load the snd_pcm_oss and snd_seq_oss kernel modules. Configure them to load at boot.

By default, ALSA has all channels muted. Those have to be unmuted manually.

Unmuting the sound card's master volume can be done by using amixer:

Unmuting the sound card can be done using alsamixer:

The MM label below a channel indicates that the channel is muted, and OO indicates that it is open.

Scroll to the Master and PCM channels with the Left and Right keys and unmute them by pressing the m key.

Use the Up key to increase the volume and obtain a value of 0 dB gain. The gain can be found in the upper left next to the Item: field.

To get full 5.1 or 7.1 surround sound, you will likely need to unmute other channels such as Front, Surround, Center, LFE (subwoofer) and Side. (Those are channel names with Intel HD Audio; they may vary with different hardware)

To enable your microphone, switch to the Capture tab with F4 and enable a channel with Space. See /Troubleshooting#Microphone if microphone does not work.

Next, test to see if sound works:

Change -c to fit your speaker setup. Use -c 8 for 7.1, for instance:

If audio is being outputted to the wrong device, try manually specifying it with the argument -D.

-D accepts PCM channel names as values, which can be retrieved by running the following:

For more information, see Advanced Linux Sound Architecture - Driver Configuration guide.

To reload ALSA driver configuration you have to reload corresponding modules. Before doing this, all processes using the corresponding ALSA driver—such as PipeWire—must be stopped. To identify processes using sound device files, utilize fuser(1):

Run lspci -k -nn -d ::0403 to identify the modules in use for PCI devices.

Run lsusb --verbose --tree | grep --after-context=1 'Class=Audio' for USB devices.

Run lsmod | grep '^snd' to get a full list of loaded sound modules.

Run cat /proc/asound/cards to get the list of your sound cards with their corresponding indexes (card numbers).

Run cat /proc/asound/modules to get the card indexes with their corresponding module names.

If you want to change your sound card order (or if your sound card order changes on boot, and you want to make it permanent), reserve the index for the given driver with the slots option of the snd module. See also Kernel module#Setting module options.

The following sample assumes you want your USB sound card always be the first (i.e. with index 0), no matter when the module is loaded (e.g. the card could be unplugged on boot):

When a module name is prepended with an exclamation mark (!), the corresponding index will be given for any modules but that name. For example, reserve the first index (0) for any modules but snd_usb_audio to avoid USB sound cards from getting it:

You can also provide an index of -2 to instruct ALSA to never use a card as the primary one: negative value is interpreted as a bitmask of permissible indexes. The alternative to the previous sample using the index option of the specific module:

If several sound cards use the same module, and their order is always the same, you can change the order with just index option. The following sample assumes there are two audio cards using the HD Audio module (e.g. an integrated audio card and HDMI output of non-integrated video card), and you want to swap their indexes:

The slots option can be combined with the index one as long as they do not conflict:

To disable all cards controlled by a given kernel module, prevent the module from loading using install or module_blacklist approach.

To select which card should be disabled, use the enable option of a kernel module. For example, disable the second card operated by a module:

See also /Troubleshooting#Codec probing for an HD Audio card codec disabling.

The system configuration file is /etc/asound.conf, and the per-user configuration file is ~/.asoundrc.

The syntax of library configuration—i.e. whitespace, line continuation, comments, including configuration files, punctuators (separators), assignments, compound assignments, operation modes—is explained in Configuration files.

ALSA library configuration is loaded for each instance of the library, so to reload it, all you have to do is restart the programs that are using it.

For more information, see:

There are different operation modes for parsing nodes, the default mode is merge and create. If operation mode is either merge/create or merge, type checking is done. Only same type assignments can be merged, so strings cannot be merged with integers. Trying to define a simple assignment in default operation mode to a compound (and vice versa) will also not work.

Prefixes of operation modes:

Using override operation mode, when done correctly, is usually safe; however, one should bear in mind that there might be other necessary keys in a node for proper functioning.

Sometimes, it may be useful and even easier to read using nesting in configuration.

Assuming that "defaults" node is set in /usr/share/alsa/alsa.conf, where "defaults.pcm.card" and its "ctl" counterpart have assignment values "0" (type integer), user wants to set default pcm and control device to (third) sound card "2" or "SB" for an Azalia sound card.

Using double quotes here automatically sets values data type to string, so in the above example, setting defaults.pcm.!card "2" would result in retaining last default device, in this case card 0. Using double quotes for strings is not mandatory as long as no special characters are used, which ideally should never be the case. This may be irrelevant in other assignments.

Putting the previous example regarding defaults.pcm.card and defaults.pcm.device into practice, assuming we have 2 cards with index 0 and 1 respectively and wish to simply change the default card to index 1, would lead to the following configuration in /etc/asound.conf or the user-specific ~/.asoundrc to change both the playback and the mixer control card.

Probably, it is enough to set ALSA_CARD to the name of the device. First, get the names with aplay -l, then set ALSA_CARD to the name which comes after the colon and before the bracket; e.g. if you have

then set ALSA_CARD=HDMI.

Other variables are also checked in the default global configuration /usr/share/alsa/alsa.conf. By looking there for constructs of the form vars [ ... ], the following table emerges:

Alternatively, you can override the behavior in your own configuration file, preferably the global one (/etc/asound.conf). Add:

In this case as well, replace Audigy2 with the name of your device. You can get the names with aplay -l or you can also use PCMs like surround51. But if you need to use the microphone, it is a good idea to select full-duplex PCM as default.

Now, you can select the sound card when starting programs by just changing the environment variable ALSAPCM. It works fine for all programs that do not allow to select the card; for the others, ensure you keep the default card. For example, assuming you wrote a downmix PCM called mix51to20, you can use it with mplayer using the commandline ALSAPCM=mix51to20 mplayer example_6_channel.wav

First, you will have to find out the card and device id that you want to set as the default:

For example, the last entry in this list has the card index (card number) 2, card ID strings Audio and the device ID 0. To set this card as the default, you can either use the system-wide file /etc/asound.conf or the user-specific file ~/.asoundrc. You may have to create the file if it does not exist. Then insert the following options with the corresponding card.

It is recommended to use sound card ID strings instead of number references to overcome the boot order problem.

pcm.dmixer and pcm.dsnooper are spares for applications which does not support without mixing.

The factual accuracy of this article or section is disputed.

For example, chromium -alsa-output-device=pcm.dmixer -alsa-input-device=pcm.dsnooper enables mixing for Chromium tempolary.

The pcm options affect which card and device will be used for audio playback while the ctl option affects which card is used by control utilities like alsamixer.

The changes should take effect as soon as you (re-)start an application (e.g. MPlayer). You can also test with a command like aplay:

If you receive an error regarding your asound configuration, check the upstream documentation for possible changes to the configuration file format.

Install the alsa-plugins package if you need to enable #Upmixing, #Downmixing, #High quality resampling and other advanced features.

For more information, see PCM (digital audio) plugins.

Mixing enables multiple applications to output sound at the same time. Most discrete sound cards support hardware mixing, which is enabled by default if available. Integrated motherboard sound cards (such as Intel HD Audio), usually do not support hardware mixing. On such cards, software mixing is done by an ALSA plugin called dmix. This feature is enabled automatically if hardware mixing is unavailable.

To manually enable dmix, add the following to your ALSA configuration file:

In order for stereo sources like music to be able to saturate a 5.1 or 7.1 sound system, you need to use upmixing. In darker days, this used to be tricky and error prone, but nowadays, plugins exist to easily take care of this task. We will use the upmix plugin, included in the alsa-plugins package.

Then add the following to your ALSA configuration file of choice (either /etc/asound.conf or ~/.asoundrc):

You can easily change this example for 7.1 upmixing to 5.1 or 4.0.

The following example adds a new PCM channel that you can use for upmixing. If you want all sound sources to go through this channel, add it as a default below the previous definition like so:

The plugin automatically allows multiple sources to play through it without problems so setting is as a default is actually a safe choice. If this is not working, you have to setup your own dmixer for the upmixing PCM like this:

and use "dmix6" instead of "surround71". If you experience skipping or distorted sound, consider increasing the buffer_size (to 32768, for example) or use a high quality resampler.

If you want to downmix sources to stereo because you, for instance, want to watch a movie with 5.1 sound on a stereo system, use the vdownmix plugin, included in the alsa-plugins package.

Again, in your configuration file, add this:

mbeq is part of Steve Harris' LADSPA plugin suite.

Install the alsa-plugins, ladspa and swh-plugins packages if you do not already have them.

If you have not already created either an ~/.asoundrc or a /etc/asound.conf file, then create either one and insert the following:

Install the alsaequalAUR package.

After installing the package, add the following to your ALSA configuration file:

To change your equalizer settings, run

Note that the equalizer configuration is different for each user (until not specified else). It is saved in ~/.alsaequal.bin. So if you want to use ALSAEqual with mpd or another software running under different user, you can configure it using

or for example, you can make a symlink to your .alsaequal.bin in their home directory.

If you wish to apply an equalizer to a specific output device only (for example your speakers connected to the S/PDIF output, but not your headphones connected to the headphone jack), but also want be able to output from multiple applications and to both output devices simultaneously, you need to create two dmix devices that feed into their respective devices (slave.pcm) directly. The following works for stereo output and maintains a regular stereo input, applying the equalizer to the S/PDIF output only.

Install the alsaequal-mgrAUR package.

Configure the equalizer as usual with

When you are satisfied with the state, you may give it a name (foo in this example) and save it:

The state "foo" can then be restored at a later time with

This, however, only restores ~/.alsaequal.bin. You then have to update the equalizer by alsamixer -D equal.

You can thus create different equalizer states for games, movies, music genres, VoIP apps, etc. and reload them as necessary.

See the project page and the help message for more options.

When #Software mixing is enabled, ALSA is forced to resample everything to the same frequency (48 kHz by default when supported). By default, it will try to use the speexrate converter to do so, and fallback to low-quality linear interpolation if it is not available. Thus, if you are getting poor sound quality due to bad resampling, the problem can be solved by simply installing the alsa-plugins package.

For even higher quality resampling, you can change the default rate converter to speexrate_medium or speexrate_best. Both perform well enough that in practice it does not matter which one you choose, so using the best converter is usually not worth the extra CPU cycles it requires.

To change the default converter, place the following contents in your ~/.asoundrc or /etc/asound.conf:

Auto-Mute Mode can be configured on startup with amixer. For example, to disable it:

Alternatively, the ncurses based interface can be utilized through alsamixer. In order to save any modifications, use:

See also #ALSA and systemd.

See Writing Udev rules for ALSA.

You might want to play music via external speakers connected via mini jack and internal speakers simultaneously. This can be done by unmuting Auto-Mute item using alsamixer or amixer:

and then unmuting other required items, such as Headphones, Speaker, Bass Speaker...

Map the following commands to your volume keys: XF86AudioRaiseVolume, XF86AudioLowerVolume, XF86AudioMute.

To toggle mute/unmute of the volume:

You might want a jack alternative to create a virtual recording or play device in order to mix different sources, using the snd_aloop module:

List your new virtual devices using:

now you can for example using ffmpeg:

In the hw:R,W,N phrase, R is your virtual card device number. W should be set to 1 for recording devices, or 0 for playing. N is your sub device. You can use all the virtual devices available and play/stop using applications like mplayer:

Another thing you could do with this approach is using festival to generate a voice into a recording stream using a script like this:

The alsa-tools package contains the hdajackretask tool, which can be used (on Intel HDA cards) to reconfigure the sound card input/output ports; for instance, to turn a microphone jack into a headphone jack.

apulseAUR provides an alternative partial implementation of the PulseAudio API. It lets you use ALSA for applications that support only PulseAudio for sound. Usage is simply:

**Examples:**

Example 1 (unknown):
```unknown
error: sof firmware file is missing
error: failed to load DSP firmware -2
error: sof_probe_work failed err: -2
```

Example 2 (unknown):
```unknown
alsa-restore.service
```

Example 3 (unknown):
```unknown
alsa-state.service
```

Example 4 (unknown):
```unknown
alsa-restore.service
```

---

## NVIDIA Optimus

**URL:** https://wiki.archlinux.org/title/NVIDIA_Optimus

**Contents:**
- Available methods
- Use integrated graphics only
  - Use CUDA without switching the rendering provider
- Use NVIDIA graphics only
  - Display managers
    - LightDM
    - SDDM
    - GDM
  - Checking 3D
  - Further information

This article or section needs expansion.

NVIDIA Optimus is a technology that allows an integrated GPU and discrete NVIDIA GPU to be built into and accessed by a laptop. As a prerequisite, install the relevant GPU driver for both cards.

There are several methods available:

If you only care to use a certain GPU without switching, check the options in your system's BIOS. There should be an option to disable one of the cards. Some laptops only allow disabling of the discrete card, or vice-versa, but it is worth checking if you only plan to use just one of the cards.

If your BIOS does not allow to disable Nvidia graphics, you can disable it from the Linux kernel itself. See Hybrid graphics#Fully power down discrete GPU.

You can use CUDA without switching rendering to the Nvidia graphics. All you need to do is ensure that the Nvidia card is powered on before starting a CUDA application, see Hybrid graphics#Fully power down discrete GPU for details.

Now when you start a CUDA application, it will automatically load all necessary kernel modules. Before turning off the Nvidia card after using CUDA, the nvidia kernel modules have to be unloaded first:

The proprietary NVIDIA driver can be configured to be the primary rendering provider. It also has notable screen-tearing issues unless you enable prime sync by enabling NVIDIA#DRM kernel mode setting, see [1] for further information. It does allow use of the discrete GPU and has (as of January 2017) a marked edge in performance over the nouveau driver.

First, install the NVIDIA driver and xorg-xrandr. Then, configure /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf the options of which will be combined with the package provided /usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf to provide compatibility with this setup.

Next, add the following two lines to the beginning of your ~/.xinitrc:

Now reboot to load the drivers, and X should start.

If your display dpi is not correct add the following line:

If you get a black screen when starting X, make sure that there are no ampersands after the two xrandr commands in ~/.xinitrc. If there are ampersands, it seems that the window manager can run before the xrandr commands finish executing, leading to a black screen.

If you are using a display manager then you will need to create or edit a display setup script for your display manager instead of using ~/.xinitrc.

For the LightDM display manager:

Make the script executable.

Now configure lightdm to run the script by editing the [Seat:*] section in /etc/lightdm/lightdm.conf:

Now reboot and your display manager should start.

For the SDDM display manager (SDDM is the default DM for KDE):

For the GDM display manager create two new .desktop files:

Make sure that GDM use X as default backend.

You can check if the NVIDIA graphics are being used by installing mesa-utils and running

For more information, look at NVIDIA's official page on the topic [2].

This is the official NVIDIA method to support switchable graphics.

See PRIME#PRIME render offload for details.

See PRIME for graphics switching and nouveau for open-source NVIDIA driver.

See PRIME#GNOME integration.

See Optimus-manager upstream documentation. It covers both installation and configuration in Arch Linux systems.

See EnvyControl upstream documentation. It covers both installation and usage instructions.

See NVidia-eXec upstream documentation. It covers both installation and usage instructions.

See nvidia-switch upstream documentation. It covers both installation and usage instructions.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Enable DRM kernel mode setting, which will in turn enable the PRIME synchronization and fix the tearing.

You can read the official forum thread for details.

Add rcutree.gp_init_delay=1 to the kernel parameters. Original topic can be found in [3] and [4].

This is due to the NVIDIA driver not detecting the EDID for the display. You need to manually specify the path to an EDID file or provide the same information in a similar way.

To provide the path to the EDID file edit the Device Section for the NVIDIA card in Xorg.conf, adding these lines and changing parts to reflect your own system:

If Xorg will not start try swapping out all references of CRT to DFB. card0 is the identifier for the Intel card to which the display is connected via LVDS. The edid binary is in this directory. If the hardware arrangement is different, the value for CustomEDID might vary but yet this has to be confirmed. The path will start in any case with /sys/class/drm.

Alternatively you can generate your edid with tools like read-edid and point the driver to this file. Even modelines can be used, but then be sure to change UseEDID and IgnoreEDID.

Using nvidia-xconfig, incorrect information might be generated in xorg.conf and in particular wrong monitor refresh rates that restrict the possible resolutions. Try commenting out the HorizSync/VertRefresh lines. If this helps, you can probably also remove everything else not mentioned in this article.

Symptoms: lspci hangs, system suspend fails, shutdown hangs, optirun hangs.

Applies to: newer laptops with GTX 965M or alike when bbswitch (e.g. via Bumblebee) or nouveau is in use.

When the dGPU power resource is turned on, it may fail to do so and hang in ACPI code (kernel bug 156341).

When using nouveau, disabling runtime power-management stops it from changing the power state, thus avoiding this issue. To disable runtime power-management, add nouveau.runpm=0 to the kernel parameters.

For known model-specific workarounds, see this issue. In other cases you can try to boot with acpi_osi="!Windows 2015" or acpi_osi=! acpi_osi="Windows 2009" added to your Kernel parameters. (Consider reporting your laptop to that issue.)

Check if the output is something similar to:

NVIDIA drivers now offer Optimus support since 319.12 Beta [5] with kernels above and including 3.9.

Another solution is to install the Intel driver to handle the screens, then if you want 3D software you should run them through Bumblebee to tell them to use the NVIDIA card.

Using the proprietary drivers on a setup with an integrated AMD card and with the dedicated NVIDIA card set as the only one in use, users report freezes for up to 10 seconds, with the following errors in the Xorg logs:

While this is not root-caused yet, it seems linked to a conflict in how the integrated and dedicated cards interact with Xorg.

The workaround is to use switchable graphics, see PRIME#PRIME render offload for details.

There are cases where lspci will show the PCI domain as first output column, making optimus-manager generated files break while trying to map BusID on multiple laptop models.

If you face a black screen that never ends to load your GUI, GUI partially loading with console artifacts or Xorg crashing with (EE) - No Devices detected, the workaround and bug reports are available at the upstream GitHub.

A workaround for the issue is to uninstall the Xorg driver of the iGPU (e.g. xf86-video-amdgpu or xf86-video-intel) [6]. This should work as long as the external monitor port (HDMI/DP/USB-C) is connected directly to the Nvidia dGPU.

Since the 530.41 driver version, cases of cards locked at low power consumption limits appeared (see GitHub issue 483). The NVIDIA driver has disabled the ability to manually set the power limit using nvidia-smi command, so many laptops are stuck with low power usage and bad performance.

To workaround this problem (for the Ampere generation or newer), see NVIDIA/Tips and tricks#Dynamic Boost.

Some processes may keep your NVIDIA GPU on due to their way of interacting with the GPU. This causes significantly increased power usage, lower battery life, and higher temperatures.

You can check if your GPU is in an active state or suspended by running the following command:

If the state is active, you are probably running a process that keeps your GPU alive.

If you use a thermal monitor that is probing your GPU temperature, it typically calls nvidia-smi to get this temperature, which will wake up your GPU and keep it in an active state.

You can use nvtop to check if a process (such as Xorg) is using the NVIDIA GPU, but this method does not work in all cases. For example, if you have a Ollama server running, it will always keep your GPU on but will not show in nvtop or invoke nvidia-smi.

Remember to check the articles related to your specific chosen method for troubleshooting as well.

**Examples:**

Example 1 (unknown):
```unknown
# rmmod nvidia_uvm
# rmmod nvidia
```

Example 2 (unknown):
```unknown
/etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
```

Example 3 (unknown):
```unknown
/usr/share/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
```

Example 4 (unknown):
```unknown
/etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf
```

---

## Backlight

**URL:** https://wiki.archlinux.org/title/Backlight

**Contents:**
- Hardware interfaces
  - ACPI
    - Kernel command-line options
    - Udev rule
  - setpci
  - External monitors
- Switch off the backlight
- Save and restore functionality
- Backlight utilities
  - xbacklight

Screen brightness might be tricky to control. On some machines physical hardware switches are missing and software solutions may not work well. However, it is generally possible to find a functional method for a given hardware. This article aims to summarize all possible ways to adjust the backlight.

There are many ways to control brightness of a monitor, laptop or integrated panel (such as the iMac). According to these discussions and this wiki page the control method can be divided into these categories:

The brightness of the screen backlight is adjusted by setting the power level of the backlight LEDs or cathodes. The power level can often be controlled using the ACPI kernel module for video. An interface to this module is provided via a sysfs(5) directory at /sys/class/backlight/.

The name of the directory depends on the graphics card model.

In this case, the backlight is managed by an ATI graphics card. In the case of an Intel card, the directory is called intel_backlight. In the following examples, acpi_video0 is used. If you use an Intel card, simply replace acpi_video0 with intel_backlight in the examples.

The directory contains the following files related to brightness:

The maximum brightness can be read from max_brightness, like this:

The brightness can be set by writing a number to brightness. However, its value often differs from actual_brightness, and it's device dependent. (See also #Recent_(2025)_AMD_changes.)

Attempting to set a brightness greater than the maximum results in an error. By default, only root can change the brightness by this method. To allow users in the video group to change the brightness, a udev rule such as the following can be used (Logging out/Rebooting may be necessary to changes take effects):

The factual accuracy of this article or section is disputed.

Sometimes ACPI does not work well due to different motherboard implementations and ACPI quirks. This results in, for instance, inaccurate brightness notifications. This includes some laptops with dual graphics (e.g., NVIDIA/AMD dedicated GPU with Intel/AMD integrated GPU). Additionally, ACPI sometimes needs to register its own acpi_video0 backlight even if one already exists (such as intel_backlight), which can be done by adding one of the following kernel parameters:

If the ACPI interface is available, the backlight level can be set at boot using a udev rule:

In some cases (e.g. Intel Mobile 945GME [1]), it is possible to set the register of the graphics card to adjust the backlight. It means you adjust the backlight by manipulating the hardware directly, which can be risky and generally is not a good idea. Not all of the graphics cards support this method.

When using this method, you need to use lspci first to find out where your graphics card is.

Display Data Channel Command Interface (DDC/CI) can be used to communicate with external monitors implementing Monitor Control Command Set (MCCS) over I2C. DDC can control brightness, contrast, inputs, etc on supported monitors. Settings available via the On-Screen Display (OSD) panel can usually also be managed via DDC. The kernel module i2c-dev may need to be loaded if the /dev/i2c-* devices do not exist.

ddcutil can be used to query and set brightness settings:

Alternatively, one may use ddcci-driver-linux-dkmsAUR to expose external monitors in sysfs. Then, after loading the ddcci kernel module, one can use any backlight utility.

This article or section is a candidate for merging with DPMS.

Switching off the backlight (for example when one locks a notebook) can be useful to conserve battery energy. Ideally the following command should work for any Xorg graphical session:

The backlight should switch on again on mouse movement or keyboard input. Alternately, xset s could be used for a similar effect.

If the previous commands do not work, there is a chance that vbetool may work. Note, however, that in this case the backlight must be manually activated again. The command is as follows:

To activate the backlight again:

For example, this can be put to use when closing the notebook lid using acpid.

The systemd package includes the service systemd-backlight@.service, which is enabled by default and "static". It saves the backlight brightness level at shutdown and restores it at boot. The service uses the ACPI method described in #ACPI, generating services for each folder found in /sys/class/backlight/. For example, if there is a folder named acpi_video0, it generates a service called systemd-backlight@backlight:acpi_video0.service. When using other methods of setting the backlight at boot, it is recommended to stop systemd-backlight from restoring the backlight by setting the kernel parameters parameter systemd.restore_state=0. See systemd-backlight@.service(8) for details.

Additionally, the brilloAUR and lightAUR utilities support save and restore functionality. These two may be more useful if one wishes to restore the screen brightness on a per-user basis, however no systemd units are provided to accomplish this.

This article or section is being considered for removal.

Brightness can be set using the xorg-xbacklight package.

To set brightness to 50% of maximum:

Increments can be used instead of absolute values, for example to increase or decrease brightness by 10%:

If you get the "No outputs have backlight property" error, it is because xrandr/xbacklight does not choose the right directory in /sys/class/backlight. You can specify the directory by setting the Backlight option of the device section in /etc/X11/xorg.conf.d/20-video.conf. For instance, if the name of the directory is intel_backlight and using the Intel driver, the device section may be configured as follows:

See FS#27677 and https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=651741 for details.

If you have enabled Intel Fastboot you might also get the No outputs have backlight property error. In this case, trying the above method may cause Xorg to crash on start up. You should disable it to fix the issue. It is known to cause issues with brightness control.

Install lightAUR and add your user to the video user group.

Increase backlight brightness by 5 percent:

Decrease backlight brightness by 5 percent:

Set backlight brightness to 100 percent:

Brightness can also be adjusted as the GNOME controls do. Changes are reflected in the GNOME UI using this method.

Steps in brightness for keyboard control can be implemented with this method as well.

See https://userbase.kde.org/KDE_Connect/Tutorials/Useful_commands#Brightness_settings.

This article or section needs expansion.

Color correction does not change the backlight power, it just modifies the video lookup table: this means that your battery life will be unaffected by the change. Nevertheless, it could be useful when no backlight control is available (desktop PCs or laptops with OLED screens).

Redshift does not support Wayland (although a patchset exists). But it is possible to apply the desired temperature in tty before starting a compositor. For example:

Otherwise some compositors can apply color correction during runtime:

xrandr may be used to adjust the perceived brightness.

To adjust perceived brightness above its maximum level (the same caveats mentioned above for Nvidia apply):

This should roughly double luma in the image. It will sacrifice color quality for brightness, nevertheless it is particularly suited for situations where the ambient light is very bright (e.g. sunlight).

This can also be used to reduce perceived brightness in a dark room by specifying some value less than 1 (e.g. 0.5), this is useful when no backlight control is available (e.g. desktop PC).

The output name of the connected device may be determined by calling xrandr:

Users may find it convenient to implement this as an alias:

To automatically call xrandr when a backlight file changes, oled_shmoledAUR can be used like so:

Users of NVIDIA's proprietary drivers can change display brightness via the nvidia-settings utility under "X Server Color Correction." However, note that this has absolutely nothing to do with backlight (intensity), it merely adjusts the color output. (Reducing brightness this way is a power-inefficient last resort when all other options fail; increasing brightness spoils your color output completely, in a way similar to overexposed photos.)

This article or section needs expansion.

Laptops with LED backlight are known to have screen flicker sometimes. This is because the most efficient way of controlling LED backlight brightness is by turning the LED's on and off very quickly varying the amount of time they are on.

However, the frequency of the switching, so-called PWM (pulse-width modulation) frequency, may not be high enough for the eye to perceive it as a single brightness and instead see flickering. This causes some people to have symptoms such as headaches and eyestrain.

If you have an Intel i915 GPU, then it may be possible to adjust PWM frequency to eliminate flicker.

Period of PWM (inverse to frequency) is stored in 2 higher bytes of 0xC8254 register (if you are using the Intel GM45 chipset use address 0x61254 instead). To manipulate registers values, install the intel-gpu-tools package.

To increase the frequency, period must be reduced. For example:

Then to double PWM frequency divide 2 higher bytes (4 higher hex digits) by 2 and write back resulting value, keeping lower bytes unchanged:

You can use online calculator to calculate desired value https://devbraindom.blogspot.com/2013/03/eliminate-led-screen-flicker-with-intel.html[dead link 2025-03-15—HTTP 404]

To set new frequency automatically, consider writing an udev rule or install intelpwm-udevAUR.

This problem may be solved by adding i915.invert_brightness=1 to the list of kernel parameters.

Embedded Display Port (eDP) v1.2 introduced a new display panel control protocol for backlight and other controls that works through the AUX channel [6]

By default the i915 driver tries to use PWM to control backlight brightness, which might not work.

To set the backlight through writes to DPCD registers using the AUX channel set i915.enable_dpcd_backlight=1 as a kernel parameter.

On some systems, the brightness hotkeys on your keyboard correctly modify the values of the acpi interface in /sys/class/backlight/acpi_video0/actual_brightness but the brightness of the screen is not changed. Brightness applets from desktop environments may also show changes to no effect.

If you have tested the recommended kernel parameters and only xbacklight works, then you may be facing an incompatibility between your BIOS and kernel driver.

In this case the only solution is to wait for a fix either from the BIOS or GPU driver manufacturer.

A workaround is to use the inotify kernel api to trigger xbacklight each time the value of /sys/class/backlight/acpi_video0/actual_brightness changes.

First install inotify-tools. Then create a script around inotify that will be launched upon each boot or through autostart.

check dmesg if you have seen like this :

i915 0000:00:02.0: [drm] *ERROR* [CONNECTOR:114:DSI-1] Failed to get the SoC PWM chip

Change /etc/mkinitcpio.conf to match the following:

Then regenerate the initramfs.

Make sure the mate-power-manager package is installed.

Some Notebook Models e.g. Razer Blade 14, Lenovo Yoga Slim 7, Lenovo IdeaPad Gaming 3 and Acer AN517-41 have issues with backlight control, pass acpi_backlight=video and/or amdgpu.backlight=0 as kernel parameters.

In xfce4, the Xfce4 Power Manager handles the brightness keys.

In some installations of Xfce, the "Handle display brightness keys" setting may be turned off by default.

To activate the brightness keys again, open the Xfce Power Manager dialog and toggle on "Handle display brightness keys":

Depending on the video card installed, sometimes xbacklight from xorg-xbacklight returns the message "No outputs have backlight property". Installing acpilightAUR provides an alternative xbacklight that may work as expected.

Due to a bug introduced recently in the amdgpu driver, the backlight's actual_brightness value is reported as a 16-bit integer, which is outside the 8-bit range specified in max_brightness. This causes the systemd-backlight service to attempt to restore, at boot time, a value that is too large and ends being truncated to maximum brightness (255).

While the bug is not addressed, one possible workaround is to modify the stored brightness to within the correct range before it is restored. This can be accomplished with a script and a service unit:

On certain systems, the backlight level reported by the driver is in the correct range [0, 255], but systemd still fails to restore the correct value. This is probably due to a race in the kernel. In this case, truncating the brightness level will not help since it is already in the correct range. Instead, saving the brightness level to systemd before shutting down could work as a workaround. This can be accomplished by the following script and service unit:

According to systemd-backlight@.service(8), if the udev property ID_BACKLIGHT_CLAMP is not set to false, the brightness is clamped to a value of at least 1 or 5% of maximum brightness, whichever is greater. This restriction will be removed when the kernel allows user space to reliably set a brightness value which does not turn off the display.

To allow <5% brightness to persist on reboot, create udev rule:

This article or section needs expansion.

In 2025 there were two changes for AMD laptops, affecting kernel 6.16 and backported to 6.15.5. First, the previous max brightness was <= 255, but it is now <= 65535. [7] Notice this means using backlight values defined before this change results in a lower brightness.

Second is the relation of brightness and actual_brightness, found under /sys/class/backlight/amdgpu_bl0 or so. Both in the former and the new kernels, these two values are not identical. In the new behavior, actual brightness changes according to the firmware setting. [8] [9] This is because the brightness curve in the firmware possibly better reflects the characteristics of the panel.

To disable this firmware curve, set the following kernel parameter: amdgpu.dcdebugmask=0x40000

**Examples:**

Example 1 (unknown):
```unknown
/sys/class/backlight
```

Example 2 (unknown):
```unknown
/sys/class/backlight/
```

Example 3 (unknown):
```unknown
$ ls /sys/class/backlight/
```

Example 4 (unknown):
```unknown
acpi_video0
```

---

## PRIME

**URL:** https://wiki.archlinux.org/title/PRIME

**Contents:**
- PRIME GPU offloading
  - For open source drivers - PRIME
  - Note about Windows games
  - PRIME render offload
    - PCI-Express Runtime D3 (RTD3) Power Management
      - Open-source drivers
      - NVIDIA
    - Configure applications to render using GPU
    - GNOME integration
    - Troubleshooting

PRIME is a technology used to manage hybrid graphics found on recent desktops and laptops (Optimus for NVIDIA, AMD Dynamic Switchable Graphics for Radeon). PRIME GPU offloading and Reverse PRIME are an attempt to support muxless hybrid graphics in the Linux kernel.

We want to render applications on the more powerful card and send the result to the card which has display connected.

The command xrandr --setprovideroffloadsink provider sink can be used to make a render offload provider send its output to the sink provider (the provider which has a display connected). The provider and sink identifiers can be numeric (0x7d, 0x56) or a case-sensitive name (Intel, radeon).

You may also use provider index instead of provider name:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To use your discrete card for the applications who need it the most (for example games, 3D modellers...), prepend the DRI_PRIME=1 environment variable:

Other applications will still use the less power-hungry integrated card. These settings are lost once the X server restarts, you may want to make a script and auto-run it at the startup of your desktop environment (alternatively, put it in /etc/X11/xinit/xinitrc.d/). This may reduce your battery life and increase heat though.

See Gentoo:AMDGPU#Identifying_which_graphics_card_is_in_use for more information.

For DRI_PRIME to work on Vulkan applications vulkan-mesa-layers needs to be installed, as well as lib32-vulkan-mesa-layers for 32 bit applications.

This article or section is a candidate for merging with DXVK.

When running Windows DirectX games under Wine or Proton, you need to instruct DXVK directly using:

Get the card name from vulkaninfo; DXVK uses substring match.

NVIDIA driver since version 435.17 supports this method. The modesetting, xf86-video-amdgpu (450.57), and xf86-video-intel (455.38) are officially supported as iGPU drivers.

To run a program on the NVIDIA card you can use the prime-run script provided by nvidia-prime:

Kernel PCI power management turns off the GPU when not used with PRIME offloading or reverse PRIME. This feature is supported by modesetting, xf86-video-amdgpu, xf86-video-intel, xf86-video-nouveau drivers.

The following command can be used to check current [1] power state of each GPU:

For Turing generation cards with Intel Coffee Lake or above CPUs as well as some Ryzen CPUs like the 5800H, it is possible to fully power down the GPU when not in use.

The following udev rules are needed, as recommended by NVIDIA:

Some users also reported that the following additional lines are necessary too:

Also, add the following module parameters:

Alternatively, you can install nvidia-prime-rtd3pmAUR which provides these two configuration files.

After you setup the udev rules and the module parameter either manually or using the AUR package, you will need to restart your Laptop.

To check if the NVIDIA GPU is turned off you can use this command:

You will see either suspended or running, if suspended is displayed, the GPU is turned off. Now the power draw will be 0 Watts, making the battery last longer.

In some cases, such as the NVIDIA RTX A1000, none of the options above might be listed and instead the result will be active. This alone does not mean that the GPU is in the running state. In this case you can check the state using this command:

While the GPU is in suspended state, the counter will be incrementing every time you run the command. When the GPU's state becomes running it will stop incrementing.

If you notice that the runtime_suspended_time is not incrementing, you can check your D3 Status with this command.

If it says Runtime D3 status: Not supported, you may need to follow the steps in this forum post to disable. One user noted disabling the GpuFirmware only works on the closed source driver, not on nvidia-open.

We also need to enable nvidia-persistenced.service to avoid the kernel tearing down the device state whenever the NVIDIA device resources are no longer in use. [4]

This article or section is a candidate for merging with External GPU#Xorg rendered on iGPU, PRIME render offload to eGPU.

Even without enabling Dynamic Power Management, offload rendering of applications is required [5].

To run an application offloaded to the NVIDIA GPU with Dynamic Power Management enabled, add the following environment variables: [6]

When using on a Steam game, the launcher command line can be set to:

For GNOME integration, install switcheroo-control and enable switcheroo-control.service.

GNOME will respect the PrefersNonDefaultGPU property in the desktop entry. Alternatively, you can launch applications with GPU by right clicking on the icon and choosing Launch using Discrete Graphics Card.

If you have bumblebee installed, you should remove it because it blacklists the nvidia_drm driver which is required to load the NVIDIA driver by X server for offloading.

When using PRIME, the primary GPU renders the screen content / applications, and passes it to the secondary GPU for display. Quoting an NVIDIA thread, "Traditional vsync can synchronize the rendering of the application with the copy into system memory, but there needs to be an additional mechanism to synchronize the copy into system memory with the iGPU’s display engine. Such a mechanism would have to involve communication between the dGPU’s and the iGPU’s drivers, unlike traditional vsync."

This synchronization is achieved using PRIME sync. To check if PRIME synchronization is enabled for your display, check the output of xrandr --prop.

This article or section needs expansion.

If the second GPU has outputs that are not accessible by the primary GPU, you can use Reverse PRIME to make use of them. This will involve using the primary GPU to render the images, and then pass them off to the second GPU.

It may work out of the box, however if not, please go through the following steps.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

First, identify integrated GPU BusID

In the above example Intel card has 00:02.0 which translates to PCI:0:2:0.

Set up your xorg.conf as follows and adjust BusID.

The command xrandr --setprovideroutputsource provider source sets the provider as output for the source. For example:

When this is done, the discrete card's outputs should be available in xrandr, and you could do something like:

to configure both internal as well as external displays.

If after reboot you only have one provider, it might be because when Xorg starts, the nvidia module is not loaded yet. You need to enable early module loading. See NVIDIA#Early loading for details.

The factual accuracy of this article or section is disputed.

Delete/move /etc/X11/xorg.conf file and any other files relating to GPUs in /etc/X11/xorg.conf.d/. Restart the X server after this change.

If the video driver is blacklisted in /etc/modprobe.d/ or /usr/lib/modprobe.d/, load the module and restart X. This may be the case if you use the bbswitch module for NVIDIA GPUs.

Another possible problem is that Xorg might try to automatically assign monitors to your second GPU. Check the logs:

To solve this add the ServerLayout section with inactive device to your xorg.conf:

In some cases PRIME needs a composite manager to properly work. If your window manager does not handle compositing, you can use a compositor on top of it.

If you use Xfce, you can go to Menu > Settings > Window Manager Tweaks > Compositor and enable compositing, then try again your application.

Currently there are issues with GL-based compositors and PRIME offloading. While Xrender-based compositors (xcompmgr, xfwm, compton's default backend, cairo-compmgr, and a few others) will work without issue, GL-based compositors (Mutter/muffin, Compiz, compton with GLX backend, Kwin's OpenGL backend, etc) will initially show a black screen, as if there was no compositor running. While you can force an image to appear by resizing the offloaded window, this is not a practical solution as it will not work for things such as full screen Wine applications. This means that desktop environments such as GNOME3 and Cinnamon have issues with using PRIME offloading.

Additionally if you are using an Intel IGP you might be able to fix the GL Compositing issue by running the IGP as UXA instead of SNA, however this may cause issues with the offloading process (ie, xrandr --listproviders may not list the discrete GPU).

For details see FDO Bug #69101.

One other way to approach this issue is by enabling DRI3 in the Intel driver. See the below issue for a sample configuration.

You may find that disabling fullscreen undirect allows PRIME offloading to work correctly for full-screen applications.

Using DRI3 WITH a configuration file for the integrated card seems to fix this issue.

To enable DRI3, you need to create a configuration for the integrated card adding the DRI3 option:

After this you can use DRI_PRIME=1 WITHOUT having to run xrandr --setprovideroffloadsink radeon Intel as DRI3 will take care of the offloading.

This problem can affect users when not using a composite manager, such as with i3. [9]

If you experience this problem under Gnome, then a possible fix is to set some environment variables in /etc/environment [10]

This error is given when the power management in the kernel driver is running. You can overcome this error by appending radeon.runpm=0 to the kernel parameters in the boot loader.

Some Vulkan applications (particularly ones using VK_PRESENT_MODE_FIFO_KHR and/or VK_PRESENT_MODE_FIFO_RELAXED_KHR, including Windows games ran with DXVK) will cause the GPU to lockup constantly (~5-10 seconds freezed, ~1 second working fine)[11] when ran on a system using reverse PRIME.

A GPU lockup will render any input unusable (this includes switching TTYs and using SysRq functions).

There is no known fix for this NVIDIA bug, but a few workarounds exist:

You can verify if your configuration is affected by the issue simply by running vkcube from the vulkan-tools package.

If you have RTD3 working (from #NVIDIA), when using Wayland you will experience some delay when some programs open. Depending on the application, this can be caused by two sources: Vulkan, or OpenGL, but the mechanism causing the delay is the same. Both will have to determine which device to defer to. This decision is made based on configuration files. For OpenGL, the configurations are located in /usr/share/glvnd/egl_vendor.d/, while for Vulkan they are located in /usr/share/vulkan/icd.d/. The actual delay itself is caused by the determination of a candidate requiring iteration over all potential rendering configurations. Even if the preferred configuration appears before the other (i.e. has a lower number, igpu before external), it will still iterate through all available options. While trying the configuration for the sleeping (external) GPU, it is woken up (which it takes ~1 second or more) before deferring to open the program, wasting time and battery life. This is an NVIDIA driver problem. More details here.

One solution is to make sure the dedicated GPU is not started is to make sure it is not iterated. This can be done by explicitly setting the configurations as environment variables. These can be passed either directly when running a program, or set globally (for example in your /etc/environment file). Do note that setting it globally requires you to un-set this variable (or set it to the nvidia files respectively) when deliberately trying to run a program with the external GPU.

When using PRIME offload, encountering the Major opcode of failed request: 156 (NV-GLX) is a known problem. The only known workaround is to start X session entirely on NVIDIA GPU. A user friendly way to switching between NVIDIA only and PRIME offload method is the optimus-manager utility or write some automation scripts yourself.

**Examples:**

Example 1 (unknown):
```unknown
xrandr --setprovideroffloadsink provider sink
```

Example 2 (unknown):
```unknown
xf86-video-*
```

Example 3 (unknown):
```unknown
$ xrandr --setprovideroffloadsink radeon Intel
```

Example 4 (unknown):
```unknown
$ xrandr --setprovideroffloadsink 1 0
```

---

## AMDGPU

**URL:** https://wiki.archlinux.org/title/AMDGPU

**Contents:**
- Selecting the right driver
- Installation
  - Experimental
  - Enable Southern Islands (SI) and Sea Islands (CIK) support
    - Load amdgpu driver
      - Set module parameters in kernel command line
    - Specify the correct module order
      - Set kernel module parameters
      - Compile kernel which supports amdgpu driver
  - ACO compiler

AMDGPU is the open source graphics driver for AMD Radeon graphics cards since the Graphics Core Next family.

Depending on the card you have, find the right driver in Xorg#AMD. This driver supports Southern Islands (GCN 1, released in 2012) cards and later. AMD has no plans to support pre-GCN GPUs.

Owners of unsupported GPUs may use the open source ATI driver.

Install the mesa package, which provides both the DRI driver for 3D acceleration and VA-API/VDPAU drivers for accelerated video decoding.

It may be worthwhile for some users to use the upstream experimental build of mesa.

Install the mesa-gitAUR package, which provides the DRI driver for 3D acceleration.

Officially supported kernels enable AMDGPU support for cards of the Southern Islands (GCN 1, released in 2012) and Sea Islands (GCN 2, released in 2013). The amdgpu kernel driver needs to be loaded before the radeon one. You can check which kernel driver is loaded by running lspci -k. It should be like this:

If the amdgpu driver is not in use, follow instructions in the next section.

The module parameters of both amdgpu and radeon modules are cik_support= and si_support=.

They need to be set as kernel parameters or in a modprobe configuration file, and depend on the cards GCN version.

You can use both parameters if you are unsure which kernel card you have.

Set one of the following kernel parameters:

Furthermore, if you are using an AMD A10 APU with an integrated Sea Island (GCN 1.1) card, you may have to disable Radeon Dynamic Power Management to get a proper boot. This is a feature that dynamically re-clocks the graphics core in order to keep the APU cooler and quieter, however this feature may put you in an infinite restart loop. To disable it, following the instructions above, add radeon.dpm=0 to the boot options.

Make sure amdgpu has been set as first module in the Mkinitcpio#MODULES array, e.g. MODULES=(amdgpu radeon).

For Southern Islands (SI) use the si_support=1 kernel module parameter, for Sea Islands (CIK) use cik_support=1:

Make sure modconf is in the HOOKS array in /etc/mkinitcpio.conf and regenerate the initramfs.

When building or compiling a kernel, CONFIG_DRM_AMDGPU_SI=Y and/or CONFIG_DRM_AMDGPU_CIK=Y should be set in the config.

The ACO compiler is an open source shader compiler created and developed by Valve Corporation to directly compete with the LLVM compiler, as well as Windows 10. It offers lesser compilation time and also performs better while gaming than LLVM.

Some benchmarks can be seen on GitHub and Phoronix [1] [2].

Since mesa version 20.2 ACO is the default shader compiler.

The amdgpu kernel module is supposed to load automatically on system boot.

It is possible it loads, but late, after the X server requires it. In this case see Kernel mode setting#Early KMS start.

Xorg will automatically load the driver and it will use your monitor's EDID to set the native resolution. Configuration is only required for tuning the driver.

If you want manual configuration, create /etc/X11/xorg.conf.d/20-amdgpu.conf, and add the following:

Using this section, you can enable features and tweak the driver settings, see amdgpu(4) first before setting driver options.

TearFree controls tearing prevention using the hardware page flipping mechanism. By default, TearFree will be on for rotated outputs, outputs with RandR transforms applied, and for RandR 1.4 slave outputs, and off for everything else. Or you can configure it to be always on or always off with true or false respectively.

You can also enable TearFree temporarily with xrandr:

Where output should look like DisplayPort-0 or HDMI-A-0 and can be acquired by running xrandr -q.

DRI sets the maximum level of DRI to enable. Valid values are 2 for DRI2 or 3 for DRI3. The default is 3 for DRI3 if the Xorg version is >= 1.18.3, otherwise DRI2 is used:

See Variable refresh rate.

Newer AMD cards support 10bpc color, but the default is 24-bit color and 30-bit color must be explicitly enabled. Enabling it can reduce visible banding/artifacts in gradients, if the applications support this too. To check if your monitor supports it search for "EDID" in your Xorg log file (e.g. /var/log/Xorg.0.log or ~/.local/share/xorg/Xorg.0.log):

To check whether it is currently enabled search for "Depth"):

With the default configuration it will instead say the depth is 24, with 24 bits stored in 4 bytes.

To check whether 10-bit works, exit Xorg if you have it running and run Xorg -retro which will display a black and white grid, then press Ctrl-Alt-F1 and Ctrl-C to exit X, and run Xorg -depth 30 -retro. If this works fine, then 10-bit is working.

To launch in 10-bit via startx, use startx -- -depth 30. To permanently enable it, create or add to:

If you want to minimize latency you can disable page flipping and tear free:

See Gaming#Reducing DRI latency to further reduce latency.

See Hardware video acceleration#AMD/ATI.

Monitoring your GPU is often used to check the temperature and also the P-states of your GPU.

To check your GPU's P-states, execute:

To monitor your GPU, execute:

To check your GPU utilization, execute:

To check your GPU frequency, execute:

To check your GPU temperature, execute:

To check your VRAM frequency, execute:

To check your VRAM usage, execute:

To check your VRAM size, execute:

Since Linux 4.17, once you have enabled the features at boot below, it is possible to adjust clocks and voltages of the graphics card via /sys/class/drm/card0/device/pp_od_clk_voltage.

It is required to unlock access to adjust clocks and voltages in sysfs by appending the Kernel parameter amdgpu.ppfeaturemask=0xffffffff.

Not all bits are defined, and new features may be added over time. Setting all 32 bits may enable unstable features that cause problems such as screen flicker or broken resume from suspend. It should be sufficient to set the PP_OVERDRIVE_MASK bit, 0x4000, in combination with the default ppfeaturemask. To compute a reasonable parameter for your system, execute:

For in-depth information on all possible options, read the kernel documentation for amdgpu thermal control.

To enable manual overclocking, select the manual performance level as described in #Performance levels.

To set the GPU clock for the maximum P-state 7 on e.g. a Polaris GPU to 1209MHz and 900mV voltage, run:

The same procedure can be applied to the VRAM, e.g. maximum P-state 2 on Polaris 5xx series cards:

To check if it worked out, read out clocks and voltage under 3D load:

You can reset to the default values using:

It is also possible to forbid the driver from switching to certain P-states, e.g. to workaround problems with deep powersaving P-states, such as flickering artifacts or stutter. To force the highest VRAM P-state on a card, while still allowing the GPU itself to run with lower clocks, first find the highest possible P-state, then set it:

Allow only the three highest GPU P-states:

To set the allowed maximum power consumption of the GPU to e.g. 50 Watts, run:

If you are not inclined to fully manually overclock your GPU, there are some overclocking tools that are offered by the community to assist you to overclock and monitor your AMD GPU.

One way is to use systemd units, if you want your settings to apply automatically upon boot, consider looking at this Reddit thread to configure and apply your settings on boot.

Another way is to use udev rules for some of the values, for example, to set a low performance level to save energy:

AMDGPU offers several performance levels, the file power_dpm_force_performance_level is used for this, it is possible to select between these levels:

To set the AMDGPU device to use a low performance level, the following command can be executed:

AMDGPU offers several optimizations via power profiles, one of the most commonly used is the compute mode for OpenCL intensive applications. Available power profiles can be listed with:

To use a specific power profile you should first enable manual control over them with:

Then to select a power profile by writing the NUM field associated with it, e.g. to enable COMPUTE run:

The exact values and limits of power profiles is managed through the powerplay table system. Use upliftpowerplayAUR to modify the table for supported models (Polaris to Navi2x; Navi3x and Navi4x are bugged on kernel side).

This article or section is a candidate for merging with xrandr.

To avoid the usage of the scaler which is built in the display, and use the GPU own scaler instead, when not using the native resolution of the monitor, execute:

Possible values for "scaling mode" are: None, Full, Center, Full aspect.

AMDGPU offers GPU accelerated virtual monitors for headless setups without the use of a dummy plug. This is useful for RDP and game streaming software such as sunshineAUR.

Choose the AMD GPU to use:

Add the virtual_display=1234:56:78.9,x kernel module parameter for the amdgpu module, where 1234:56:78.9 is the PCI address of the GPU and x is the number of crtc (virtual monitors) to expose. Using this parameter also disables physical outputs. [3]

Multiple GPUs can also be used by separating PCI address with a semicolon (;) as shown below:

The AMDGPU driver supports user queues, which allow job submission directly to the GPU hardware without going through the kernel driver’s command submission ioctl. Enabling this can reduce latency and improve efficiency by bypassing some kernel driver overhead.

To enable user queues, set the following environment variable:

The amdgpu module stashes several config parameters (modinfo amdgpu | grep mask) in masks that are only documented in the kernel sources.

Setting the screen's depth under Xorg to 16 or 32 will cause problems/crash. To avoid that, you should use a standard screen depth of 24 by adding this to your "screen" section:

Dynamic power management may cause screen artifacts to appear when displaying to monitors at higher frequencies (anything above 60Hz) due to issues in the way GPU clock speeds are managed[4][5].

A workaround [6] is to set the high or low performance level as described in #Performance levels.

Changing the kernel version can also help eliminate this issue. For example, it appears to be fixed in 6.12.9.

If you see artifacts in Chromium, forcing the vulkan-based backend might help. Go to chrome://flags and enable #ignore-gpu-blocklist and #enable-vulkan.

If you experience issues [7] with a AMD R9 390 series graphics card, set radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1 as kernel parameters to force the use of amdgpu driver instead of radeon.

If it still does not work, disabling DPM might help, add radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 to the kernel parameters.

If you experience freezes and kernel crashes during a GPU intensive task with the kernel error " [drm] IP block:gmc_v8_0 is hung!" [8], a workaround is to set amdgpu.vm_update_mode=3 as kernel parameters to force the GPUVM page tables update to be done using the CPU. Downsides are listed here [9].

When you change resolution or connect to an external monitor, if the screen flickers or stays white, add amdgpu.sg_display=0 as a kernel parameter.

Dynamic power management may cause a complete system freeze whilst gaming due to issues in the way GPU clock speeds are managed. [10] A workaround is to set the high performance level as described in #Performance levels.

Artifacts and other anomalies may present themselves (e.g. inability to select extension options) when WebRenderer is force enabled by the user. Workaround is to fall back to OpenGL compositing.

This is sometimes caused by a communication issue between an AMDGPU device and a 4K display connected over HDMI. A possible workaround is to enable HDR or "Ultra HD Deep Color" via the display's built-in settings. On many Android based TVs, this means setting this to "Standard" instead of "Optimal".

If you encounter issues where the kernel driver is loaded, but the discrete graphics card still is not available for games or becomes disabled during use (similar to [11]), you can workaround the issue by setting the kernel parameter amdgpu.runpm=0, which prevents the dGPU from being powered down dynamically at runtime.

A bug in the amdgpu driver may stop the display from updating [12]. It is suggested to append the amdgpu.dcdebugmask=0x10 or amdgpu.dcdebugmask=0x12 kernel parameter as a workaround.

In the system journal or the kernel message keyring a critical level error message

may appear. If you are not planning to use Radeon Open Compute, this can be safely ignored. It is not supported in TOPAZ, as they are old GPUs. [13] [14]

On high resolutions and refresh rates, the MCLK (vram / memory clock) may be locked at the highest clock rate (1000MHz) [15] [16] causing higher GPU idle power draw. On Linux kernel 6.4.x, MCLK clocks at the lowest (96MHz), causing low performance in games [17] [18].

This is likely due to a monitor not using Coordinated Video Timings (CVT) with a low V-Blank value for the affected resolutions and refresh rates, see this gist for a workaround.

The amdgpu kernel module tries to buffer VRAM in RAM when the system enters S3 to prevent memory loss through VRAM decay which is not sufficiently refreshed.

If you are using a lot of VRAM and are short on free RAM this can fail despite sufficient SWAP memory would be available, because the IO subsystem might have been suspended before.

You will see something like:

As a workaround, a userspace service can ensure to allocate enough RAM for the VRAM to be buffered by swapping out enough RAM before the system is suspended.

The factual accuracy of this article or section is disputed.

There is a bug in the amdgpu module, due to which the video core frequencies can be higher than those declared by the manufacturer, which can cause system instability during the game, when exiting sleep, when rebooting.

The problem has been noticed on RDNA 3 GPUs (7XXX Models) [20] [21] [22].

In dmesg you can see logs like theese:

If you have similar problems, check the maximum frequency of the video core in the system with what is stated by the manufacturer. To decrease maximum frequency, refer to #Overclocking.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

As an example, the ASUS G14 2022 laptop which as has AMD CPU and dedicated AMD GPU. The most successful approach requires to use armor crate on Windows to enforce dGPU Ultimate power options. It's switching GPU order and laptop internal power policies. Since that change HDMI should be working but user is going to experience separate rendering for integrated GPU (which SDDM and Wayland somehow pick by default) and dedicated GPU. User can obviously add DRI_PRIME=0 it this case before launching any application but its not convenient. Extending configuration to presented one allows flawless experience in expense of shorter battery life when running on battery.

Additionally kernel command line should be extended with

Power-saving applications such as power-profiles-daemon and tuned have started to enable a feature known as Panel Power Savings (PPS).

PPS is a featured supported on Laptops in which the laptop's GPU is instructed to have a lower color accuracy in the name of saving power. This, however, leads to washed out colors whenever selecting more aggressive power-saving modes on the aforementioned power-profiles-daemon and tuned. Therefore, there is interest in disabling this feature entirely.

It can be done by setting the following kernel parameter to zero:

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -k -d ::03xx
```

Example 2 (unknown):
```unknown
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Curacao PRO [Radeon R7 370 / R9 270/370 OEM]
	Subsystem: Gigabyte Technology Co., Ltd Device 226c
	Kernel driver in use: amdgpu
	Kernel modules: radeon, amdgpu
```

Example 3 (unknown):
```unknown
cik_support=
```

Example 4 (unknown):
```unknown
si_support=
```

---

## nvidia-xrun

**URL:** https://wiki.archlinux.org/title/Nvidia-xrun

**Contents:**
- Installation
- Configuration
  - Setting the right bus id
  - External GPU setup
  - Automatically run window manager
  - Use bbswitch to manage the NVIDIA card
- Usage
  - Start at boot
- Troubleshooting
  - NVIDIA GPU fails to switch off or is set to be default

nvidia-xrun is a utility that allows NVIDIA Optimus-enabled laptops to run X server with discrete NVIDIA graphics on demand. This solution offers full GPU utilization, compatibility and better performance than Bumblebee.

X server can only be used with integrated graphics or discrete NVIDIA graphics, but not both, so the user might want to switch to a separate virtual console and start another X server using different graphics from what was used for the first X server.

Find your display device bus id:

It might return something similar to 01:00.0. Then create a file (for example /etc/X11/nvidia-xorg.conf.d/30-nvidia.conf) to set the proper bus id:

Also this way you can adjust some NVIDIA settings if you encounter issues:

You can also use this in an external GPU setup. Make sure to load the nvidia-modeset and nvidia-drm modules and add the option Option "AllowExternalGpus" "true" to the "Device" section.

Change the auto-generated configuration to use the internal display on devices with multiple NVIDIA cards:

Remember to set the bus id to the correct graphics card.

For convenience you can create an $XDG_CONFIG_HOME/X11/nvidia-xinitrc file with your favorite window manager. (if using nvidia-xrun < v.0.3.79 create $HOME/.nvidia-xinitrc)

With it you do not need to specify the app and can simply execute:

Since this method starts an isolated X server, it is also a good idea to get a copy of all the other configurations files that you have located at /etc/X11/xorg.conf.d/, except for your prior standard integrated GPU configurations.

When the NVIDIA card is not needed, bbswitch can be used to turn it off. The nvidia-xrun script will automatically take care of running a window manager and waking up the NVIDIA card. To achieve that, you need to:

Load the bbswitch module on boot:

Disable the nvidia module on boot:

After a reboot, the NVIDIA card will be off. This can be seen by querying bbswitch's status:

To force the card to turn on/off respectively run:

For more about bbswitch see Bumblebee-Project/bbswitch.

Enable nvidia-xrun-pm.service - this shuts down the NVIDIA card during boot.

Once the system boots, from the virtual console, login to your user, and run nvidia-xrun application.

If above does not work, switch to unused virtual console and try again.

As mentioned before, running applications directly with nvidia-xrun application does not work well, so it is best to create an nvidia-xinitrc file as outlined earlier, and use nvidia-xrun to launch your window manager.

See #Use bbswitch to manage the NVIDIA card.

If NVIDIA GPU still fails to switch off, or is somehow set to be default whenever you use or not nvidia-xrun, then you might likely need to blacklist specific modules (which were previously blacklisted by Bumblebee). Create this file and restart your system:

There seems to be a race condition between nvidia-xrun-pm.service and systemd-modules-load.service which loads the nvidia modules. If the latter runs first, nvidia-xrun-pm will hang (actually the tee command) during device removal. If on the other hand nvidia-xrun-pm runs first then it will succeed, and later the modules will fail to load with an error (which is harmless but ugly). For this reason it might be better to always blacklist the above modules.

DRM kernel mode setting should be enabled for PRIME synchronization to work (for example on muxless devices where only the Intel GPU is connected to outputs). However, consider disabling it in case there is an issue. See NVIDIA#DRM kernel mode setting

On certain hardware, the NVIDIA GPU exposes two devices on the PCI bus: a 3D controller and an audio device. In this case, both devices need to be removed from the bus in order for the GPU to fully power down. This can be done by simply adding a line for the audio device bus id in /etc/default/nvidia-xrun, and the corresponding line in the function turn_off_gpu in /usr/bin/nvidia-xrun to remove the second device.

**Examples:**

Example 1 (unknown):
```unknown
nvidia-xrun application
```

Example 2 (unknown):
```unknown
/etc/X11/nvidia-xorg.conf
```

Example 3 (unknown):
```unknown
nvidia-xorg.conf
```

Example 4 (unknown):
```unknown
"PCI:59:0:0"
```

---

## Bumblebee

**URL:** https://wiki.archlinux.org/title/Bumblebee

**Contents:**
- Bumblebee: Optimus for Linux
- Installation
- Usage
  - Test
  - General usage
- Configuration
  - Optimizing speed
    - Using VirtualGL as bridge
    - Primusrun
    - Pvkrun

From Bumblebee's FAQ:

Optimus Technology is a hybrid graphics implementation without a hardware multiplexer. The integrated GPU manages the display while the dedicated GPU manages the most demanding rendering and ships the work to the integrated GPU to be displayed. When the laptop is running on battery supply, the dedicated GPU is turned off to save power and prolong the battery life. It has also been tested successfully with desktop machines with Intel integrated graphics and an nVidia dedicated graphics card.

Bumblebee is a software implementation comprising two parts:

It tries to mimic the Optimus technology behavior; using the dedicated GPU for rendering when needed and power it down when not in use. The present releases only support rendering on-demand, automatically starting a program with the discrete video card based on workload is not implemented.

Before installing Bumblebee, check your BIOS and activate Optimus (older laptops call it "switchable graphics") if possible (BIOS does not have to provide this option). If neither "Optimus" or "switchable" is in the BIOS, still make sure both GPUs will be enabled and that the integrated graphics (igfx) is initial display (primary display). The display should be connected to the onboard integrated graphics, not the discrete graphics card. If integrated graphics had previously been disabled and discrete graphics drivers installed, be sure to remove /etc/X11/xorg.conf or the conf file in /etc/X11/xorg.conf.d related to the discrete graphics card.

For 32-bit application support, enable the multilib repository and install:

In order to use Bumblebee, it is necessary to add your regular user to the bumblebee group:

Also enable bumblebeed.service. Reboot your system and follow #Usage.

Install mesa-utils and use glxgears to test if Bumblebee works with your Optimus system:

If it fails, try the following command (from virtualgl):

If the window with animation shows up, Optimus with Bumblebee is working.

For example, start Windows applications with Optimus:

For another example, open NVIDIA Settings panel with Optimus:

For a list of all available options, see optirun(1).

You can configure the behaviour of Bumblebee to fit your needs. Fine tuning like speed optimization, power management and other stuff can be configured in /etc/bumblebee/bumblebee.conf

One disadvantage of the offscreen rendering methods is performance. The following table gives a raw overview of a Lenovo ThinkPad T480 in an eGPU setup with NVIDIA GTX 1060 6GB and unigine-heavenAUR benchmark (1920x1080, max settings, 8x AA):

Bumblebee renders frames for your Optimus NVIDIA card in an invisible X Server with VirtualGL and transports them back to your visible X Server. Frames will be compressed before they are transported - this saves bandwidth and can be used for speed-up optimization of bumblebee:

To use another compression method for a single application:

The method of compress will affect performance in the GPU/CPU usage. Compressed methods will mostly load the CPU. However, uncompressed methods will mostly load the GPU.

Uncompressed methods:

Here is a performance table tested with ASUS N550JV laptop and benchmark app unigine-heavenAUR:

To use a standard compression for all applications, set the VGLTransport to compress-method in /etc/bumblebee/bumblebee.conf:

You can also play with the way VirtualGL reads back the pixels from your graphics card. Setting VGL_READBACK environment variable to pbo should increase the performance. Compare the following:

PBO should be faster:

The default value is sync:

primusrun (from primus) is becoming the default choice, because it consumes less power and sometimes provides better performance than optirun/virtualgl. It may be run separately, but it does not accept options as optirun does. Setting primus as the bridge for optirun provides more flexibility.

For 32-bit applications support on 64-bit machines, install lib32-primus (multilib must be enabled).

You can either run it separately:

Or as a bridge for optirun. The default configuration sets virtualgl as the bridge. Override that on the command line:

Alternatively, set Bridge=primus in /etc/bumblebee/bumblebee.conf and you will not have to specify it on the command line.

pvkrun from the package primus_vk is a drop-in replacement for primusrun that enables to run Vulkan-based applications. A quick check can be done with vulkaninfo from vulkan-tools.

This article or section is a candidate for merging with Hybrid graphics#Using bbswitch.

The goal of the power management feature is to turn off the NVIDIA card when it is not used by Bumblebee any more. If bbswitch (for linux) or bbswitch-dkms (for linux-lts or custom kernels) is installed, it will be detected automatically when the Bumblebee daemon starts. No additional configuration is necessary. However, bbswitch is for Optimus laptops only and will not work on desktop computers. So, Bumblebee power management is not available for desktop computers, and there is no reason to install bbswitch on a desktop. (Nevertheless, the other features of Bumblebee do work on some desktop computers.)

To manually turn the card on or off using bbswitch, write into /proc/acpi/bbswitch:

The default behavior of bbswitch is to leave the card power state unchanged. bumblebeed does disable the card when started, so the following is only necessary if you use bbswitch without bumblebeed.

Set load_state and unload_state kernel module parameters according to your needs (see bbswitch documentation).

To run bbswitch without bumblebeed on system startup, do not forget to add bbswitch to /etc/modules-load.d, as explained in Kernel module#systemd.

On some laptops, the NVIDIA card may not correctly initialize during boot if the card was powered off when the system was last shutdown. Therefore the Bumblebee daemon will power on the GPU when stopping the daemon (e.g. on shutdown) due to the (default) setting TurnCardOffAtExit=false in /etc/bumblebee/bumblebee.conf. Note that this setting does not influence power state while the daemon is running, so if all optirun or primusrun programs have exited, the GPU will still be powered off.

When you stop the daemon manually, you might want to keep the card powered off while still powering it on on shutdown. To achieve the latter, add the following systemd service (if using bbswitch):

Then enable the nvidia-enable.service unit.

The bumblebee daemon may fail to activate the graphics card after suspending. A possible fix involves setting bbswitch as the default method for power management:

If the above fix fails, try the following command:

To rescan the PCI bus automatically after a suspend, create a script as described in Power management/Suspend and hibernate#Hooks in /usr/lib/systemd/system-sleep.

If the port (DisplayPort/HDMI/VGA) is wired to the Intel chip, you can set up multiple monitors with xorg.conf. Set them to use the Intel card, but Bumblebee can still use the NVIDIA card. One example configuration is below for two identical screens with 1080p resolution and using the HDMI out.

You need to probably change the BusID for both the Intel and the NVIDIA card.

The BusID is 0:2:0. Note that lspci outputs hexadecimal values, but Xorg expects decimal values.

On some notebooks, the digital Video Output (HDMI or DisplayPort) is hardwired to the NVIDIA chip. If you want to use all the displays on such a system simultaneously, the easiest solution is to use intel-virtual-output, a tool provided in the xf86-video-intel driver set, as of v2.99. It will allow you to extend the existing X session onto other screens, leveraging virtual outputs to work with the discrete graphics card. Usage is as follows:

If this command alone does not work, you can try running it with optirun to enable the discrete graphics and allow it to detect the outputs accordingly. This is known to be necessary on Lenovo's Legion Y720.

If no target displays are parsed on the commandline, intel-virtual-output will attempt to connect to any local display. The detected displays will be manageable via any desktop display manager such as xrandr or KDE Display. The tool will also start bumblebee (which may be left as default install). See the Bumblebee wiki page for more information.

When run in a terminal, intel-virtual-output will daemonize itself unless the -f switch is used. Games can be run on the external screen by first exporting the display export DISPLAY=:8, and then running the game with optirun game_bin, however, cursor and keyboard are not fully captured. Use export DISPLAY=:0 to revert back to standard operation.

If intel-virtual-output does not detect displays, or if a no VIRTUAL outputs on ":0" message is obtained, then create:

which does exist by default, and:

See [3] for further configurations to try. If the laptop screen is stretched and the cursor is misplaced while the external monitor shows only the cursor, try killing any running compositing managers.

If you do not want to use intel-virtual-output, another option is to configure Bumblebee to leave the discrete GPU on and directly configure X to use both the screens, as it will be able to detect them.

As a last resort, you can run 2 X Servers. The first will be using the Intel driver for the notebook's screen. The second will be started through optirun on the NVIDIA card, to show on the external display. Make sure to disable any display/session manager before manually starting your desktop environment with optirun. Then, you can log in the integrated-graphics powered one.

You can disable screen blanking when using intel-virtual-output with xset by setting the DISPLAY environment variable appropriately (see DPMS for more info):

If you have multiple NVIDIA graphics cards (eg. when using an eGPU with a laptop with another built in NVIDIA graphics card) or NVIDIA Optimus, you need to make a minor edit to /etc/bumblebee/xorg.conf.nvidia. If this change is not made the daemon may default to using the internal NVIDIA card.

First, determine the BusID of the external card:

In this case, the BusID is 0b:00.0.

Now edit /etc/bumblebee/xorg.conf.nvidia and add the following line to Section "Device":

There is a known problem with some wine applications that fork and kill the parent process without keeping track of it (for example the free to play online game "Runes of Magic").

This is a known problem with VirtualGL. As of bumblebee 3.1, so long as you have it installed, you can use Primus as your render bridge:

If this does not work, an alternative walkaround for this problem is:

If using NVIDIA drivers a fix for this problem is to edit /etc/bumblebee/xorg.conf.nvidia and change Option ConnectedMonitor to CRT-0.

If you tried to install the NVIDIA driver from NVIDIA website, this is not going to work.

In some instances, running optirun will return:

In this case, you will need to move the file /etc/X11/xorg.conf.d/20-intel.conf to somewhere else, restart the bumblebeed daemon and it should work. If you do need to change some features for the Intel module, a workaround is to merge /etc/X11/xorg.conf.d/20-intel.conf to /etc/X11/xorg.conf.

It could be also necessary to comment the driver line in /etc/X11/xorg.conf.d/10-monitor.conf.

If you are using the nouveau driver you could try switching to the nvidia driver.

You might need to define the NVIDIA card somewhere (e.g. file /etc/bumblebee/xorg.conf.nvidia), using the correct BusID according to lspci output:

Observe that the format of lspci output is in HEX, while in xorg it is in decimals. So if the output of lspci is, for example, 0a:00.0 the BusID should be PCI:10:0:0.

If the console output is:

If the following line in /etc/bumblebee/xorg.conf.nvidia does not exist, you can add it to the "Device" section:

If it does already exist, you can try changing it to:

After that, restart the Bumblebee service to apply these changes.

Add rcutree.rcu_idle_gp_delay=1 to the kernel parameters of the boot loader configuration (see also the original BBS post for a configuration example).

You might encounter an issue when after resume from sleep, primusrun or optirun command does not work anymore. there are two ways to fix this issue - reboot your system or execute the following command:

And try to test if primusrun or optirun works.

If the above command did not help, try finding your NVIDIA card's bus ID:

For example, above command showed 01:00.0 so we use following commands with this bus ID:

If the console output is:

and if you try to load the nvidia module:

This could be because the nvidia driver is out of sync with the Linux kernel, for example if you installed the latest nvidia driver and have not updated the kernel in a while. A full system update , followed by a reboot into the updated kernel, might resolve the issue. If the problem persists you should try manually compiling the nvidia packages against your current kernel, for example with nvidia-dkms or by compiling nvidia from the ABS.

Consider switching to the official nvidia driver. As commented here, nouveau driver has some issues with some cards and bumblebee.

Set the "AutoAddDevices" option to "true" in /etc/bumblebee/xorg.conf.nvidia (see here):

This could be worked around by appending following lines in /etc/bumblebee/xorg.conf.nvidia (see here):

You probably want to start a 32-bit application with bumblebee on a 64-bit system. See the "For 32-bit..." section in #Installation. If the problem persists or if it is a 64-bit application, try using the primus bridge.

Change KeepUnusedXServer in /etc/bumblebee/bumblebee.conf from false to true. Your program forks into background and bumblebee do not know anything about it.

Video tearing is a somewhat common problem on Bumblebee. To fix it, you need to enable vsync. It should be enabled by default on the Intel card, but verify that from Xorg logs. To check whether or not it is enabled for NVIDIA, make sure nvidia-settings is installed and run:

X Server XVideo Settings -> Sync to VBlank and OpenGL Settings -> Sync to VBlank should both be enabled. The Intel card has in general less tearing, so use it for video playback. Especially use VA-API for video decoding (e.g. mplayer-vaapi and with -vsync parameter).

Refer to Intel graphics#Tearing on how to fix tearing on the Intel card.

If it is still not fixed, try to disable compositing from your desktop environment. Try also disabling triple buffering.

You might get something like:

If you are already in the bumblebee group (groups | grep bumblebee), you may try removing the socket /var/run/bumblebeed.socket.

Another reason for this error could be that you have not actually turned on both GPUs in your BIOS, and as a result, the Bumblebee daemon is in fact not running. Check the BIOS settings carefully and be sure Intel graphics (integrated graphics - may be abbreviated in BIOS as something like igfx) has been enabled or set to auto, and that it is the primary GPU. Your display should be connected to the onboard integrated graphics, not the discrete graphics card.

If you mistakenly had the display connected to the discrete graphics card and Intel graphics was disabled, you probably installed Bumblebee after first trying to run NVIDIA alone. In this case, be sure to remove the /etc/X11/xorg.conf or /etc/X11/xorg.conf.d/20-nvidia.conf configuration files. If Xorg is instructed to use NVIDIA in a configuration file, X will fail.

See Xorg#Rootless Xorg.

In some instances, using primusrun instead of optirun will result in a segfault. This is caused by an issue in code auto-detecting faster upload method, see FS#58933.

The workaround is skipping auto-detection by manually setting PRIMUS_UPLOAD environment variable to either 1 or 2, depending on which one is faster on your setup.

For primusrun, VSYNC is enabled by default and as a result, it could make mouse input delay lag or even slightly decrease performance. Test primusrun with VSYNC disabled:

If you are satisfied with the above setting, create an alias (e.g. alias primusrun="vblank_mode=0 primusrun").

Performance comparison:

Tested with ASUS N550JV notebook and benchmark app unigine-heavenAUR.

Since compositing hurts performance, invoking primus when a compositing WM is active is not recommended.[4] If you need to use primus with compositing and see flickering or bad performance, synchronizing primus' display thread with the application's rendering thread may help:

This makes primus display the previously rendered frame.

In some systems, it can happens that the nvidia module is loaded after resuming from standby. One possible solution for this is to install the acpi_call and acpi package.

Users are reporting that in some cases, even though Bumblebee was installed correctly, running

gives no output at all, and the glxgears window does not appear. Any programs that need 3d acceleration crashes:

Apparently it is a bug of some versions of virtualgl. So a workaround is to use #Primusrun instead. See this forum post for more information.

This article or section is a candidate for merging with Hybrid graphics#Using bbswitch.

If you have a newer laptop (BIOS date 2015 or newer), then Linux 4.8 might break bbswitch (bbswitch issue 140) since bbswitch does not support the newer, recommended power management method. As a result, the GPU may fail to power on, fail to power off or worse.

As a workaround, add pcie_port_pm=off to your Kernel parameters.

Alternatively, if you are only interested in power saving (and perhaps use of external monitors), remove bbswitch and rely on Nouveau runtime power-management (which supports the new method).

See NVIDIA Optimus#Lockup issue (lspci hangs) for an issue that affects new laptops with a GTX 965M (or alike).

Add acpi_osi=Linux to your Kernel parameters. See [6] and [7] for more information.

Modify the configuration as follows:

If Bumblebee starts/works in a random manner, check that you have set your Network configuration#Local network hostname resolution (details here).

Make sure nvidia-persistenced.service is disabled and not currently active. It is intended to keep the nvidia driver running at all times [8], which prevents the card being turned off.

If the discrete card is activated by some program (e.g. mpv with its GPU backend), it might stays on. The problem might be libglvnd which is loading the nvidia drivers and activating the card.

To disable this set environment variable __EGL_VENDOR_LIBRARY_FILENAMES (see documentation) to only load mesa configuration file:

nvidia-utils (and its branches) is installing the configuration file at /usr/share/glvnd/egl_vendor.d/10_nvidia.json which has priority and causes libglvnd to load the nvidia drivers and enable the card.

The other solution is to avoid installing the configuration file provided by nvidia-utils.

With the nvidia 440.36 driver, the DPMS setting is enabled by default resulting in a timeout after a fixed period of time (e.g. 10 minutes) which causes the frame rate to throttle down to 1 FPS. To work around this, add the following line to the "Device" section in /etc/bumblebee/xorg.conf.nvidia

Using Bumblebee, applications cannot access the screen to identify and record it. This happens, for example, using obs-studio with NVENC activated. To solve this, disable the bridging mode with optirun -b none command.

**Examples:**

Example 1 (unknown):
```unknown
/etc/X11/xorg.conf
```

Example 2 (unknown):
```unknown
/etc/X11/xorg.conf.d
```

Example 3 (unknown):
```unknown
# gpasswd -a user bumblebee
```

Example 4 (unknown):
```unknown
bumblebeed.service
```

---

## Hardware video acceleration

**URL:** https://wiki.archlinux.org/title/Video_acceleration

**Contents:**
- Installation
  - Intel
    - VA-API
    - Vulkan Video
    - Intel Video Processing Library (Intel VPL)
  - NVIDIA
  - AMD/ATI
  - Translation layers
- Verification
  - Verifying VA-API

Hardware video acceleration makes it possible for the video card to decode/encode video, thus offloading the CPU and saving power.

There are several ways to achieve this on Linux:

For comprehensive overview of driver and application support see #Comparison tables.

Intel graphics open-source drivers support VA-API:

Also see VAAPI supported hardware and features.

ANV open-source vulkan driver provides Vulkan Video support via vulkan-intel.

For Intel VPL, install the base library libvpl, and at least one of the following runtime implementations:

Nouveau open-source driver supports both VA-API and VDPAU:

NVIDIA proprietary driver supports via nvidia-utils:

AMD and ATI open-source drivers support both VA-API and VDPAU via mesa:

RADV open-source vulkan driver provides Vulkan Video support via vulkan-radeon.

AMDGPU PRO proprietary driver is built on top of AMDGPU driver and supports both VA-API and VDPAU in addition to AMF.

Your system may work perfectly out-of-the-box without needing any configuration. Therefore it is a good idea to start with this section to see that it is the case.

Verify the settings for VA-API by running vainfo, which is provided by libva-utils:

VAEntrypointVLD means that your card is capable to decode this format, VAEntrypointEncSlice means that you can encode to this format.

In this example the i965 driver is used, as you can see in this line:

If the following error is displayed when running vainfo:

You need to configure the correct driver, see #Configuring VA-API.

Install vdpauinfo to verify if the VDPAU driver is loaded correctly and retrieve a full report of the configuration:

Install vulkan-tools and use vulkaninfo to verify if the video processing extensions are available:

Although the video driver should automatically enable hardware video acceleration support for both VA-API and VDPAU, it may be needed to configure VA-API/VDPAU manually. Only continue to this section if you went through #Verification.

The default driver names, used if there is no other configuration present, are guessed by the system. However, they are often hacked together and may not work. The guessed value will be printed in the Xorg log file, which is ~/.local/share/xorg/Xorg.0.log if rootless, or /var/log/Xorg.0.log if Xorg is running as root. To search the log file for the values of interest:

In this case radeonsi is the default for both VA-API and VDPAU.

This does not represent the configuration however. The values above will not change even if you override them.

You can override the driver for VA-API by using the LIBVA_DRIVER_NAME environment variable:

You can override the driver for VDPAU by using the VDPAU_DRIVER environment variable.

The correct driver name depends on your setup:

Note that some older GPU models do not have Vulkan Video support in Mesa. Force-enabling Vulkan Video support on such GPUs may result in crashes with some applications (for example, mpv).

Multimedia frameworks:

Multimedia recording/streaming:

You need to set VDPAU_DRIVER variable to point to correct driver. See #Configuring VDPAU.

An error along the lines of libva: /usr/lib/dri/i965_drv_video.so init failed is encountered. This can happen because of improper detection of Wayland. One solution is to unset $DISPLAY so that mpv, MPlayer, VLC, etc. do not assume it is X11. Another mpv-specific solution is to add the parameter --gpu-context=wayland.

This error can also occur if you installed the wrong VA-API driver for your hardware.

When experiencing video decoding corruption or distortion with AMDGPU driver, set allow_rgb10_configs=false as an environment variable. [4]

If you encounter the following error:

Try installing the intel-media-driver-legacyAUR instead of the non-legacy one, which works with intel-compute-runtime-legacyAUR. [5]

**Examples:**

Example 1 (unknown):
```unknown
mpv --hwdec=auto video_filename
```

Example 2 (unknown):
```unknown
intel_gpu_top
```

Example 3 (unknown):
```unknown
intel_gpu_top
```

Example 4 (unknown):
```unknown
libva info: VA-API version 0.39.4
libva info: va_getDriverName() returns 0
libva info: Trying to open /usr/lib/dri/i965_drv_video.so
libva info: Found init function __vaDriverInit_0_39
libva info: va_openDriver() returns 0
vainfo: VA-API version: 0.39 (libva 1.7.3)
vainfo: Driver version: Intel i965 driver for Intel(R) Skylake - 1.7.3
vainfo: Supported profile and entrypoints
      VAProfileMPEG2Simple            :	VAEntrypointVLD
      VAProfileMPEG2Simple            :	VAEntrypointEncSlice
      VAProfileMPEG2Main              :	VAEntrypointVLD
      VAProfileMPEG2Main              :	VAEntrypointEncSlice
      VAProfileH264ConstrainedBaseline:	VAEntrypointVLD
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSlice
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSliceLP
      VAProfileH264Main               :	VAEntrypointVLD
      VAProfileH264Main               :	VAEntrypointEncSlice
      VAProfileH264Main               :	VAEntrypointEncSliceLP
      VAProfileH264High               :	VAEntrypointVLD
      VAProfileH264High               :	VAEntrypointEncSlice
      VAProfileH264High               :	VAEntrypointEncSliceLP
      VAProfileH264MultiviewHigh      :	VAEntrypointVLD
      VAProfileH264MultiviewHigh      :	VAEntrypointEncSlice
      VAProfileH264StereoHigh         :	VAEntrypointVLD
      VAProfileH264StereoHigh         :	VAEntrypointEncSlice
      VAProfileVC1Simple              :	VAEntrypointVLD
      VAProfileVC1Main                :	VAEntrypointVLD
      VAProfileVC1Advanced            :	VAEntrypointVLD
      VAProfileNone                   :	VAEntrypointVideoProc
      VAProfileJPEGBaseline           :	VAEntrypointVLD
      VAProfileJPEGBaseline           :	VAEntrypointEncPicture
      VAProfileVP8Version0_3          :	VAEntrypointVLD
      VAProfileVP8Version0_3          :	VAEntrypointEncSlice
      VAProfileHEVCMain               :	VAEntrypointVLD
      VAProfileHEVCMain               :	VAEntrypointEncSlice
```

---

## Laptop

**URL:** https://wiki.archlinux.org/title/Laptop

**Contents:**
- Power management
  - Battery state
    - ACPI
    - Hibernate on low battery level
      - udev
        - Testing events
      - UPower
  - Suspend and hibernate
  - Hard drive spin down problem
  - Wakeup triggers

This Laptop main page contains links to articles (sections) needed for configuring a laptop for the best experience. Setting up a laptop is in many ways the same as setting up a desktop. However, there are a few key differences. Arch Linux provides all the tools and programs necessary to take complete control of your laptop. These programs and utilities are highlighted below, with appropriate tips tutorials.

If there are laptop model specific instructions, the respective article is crosslinked in the first column of the vendor subpages. In case the model is not listed in the vendor table, existing instructions of similar models via the Category:Laptops vendor subcategory may help.

Power management is very important for anyone who wishes to make good use of their battery capacity. The following tools and programs help to increase battery life and keep your laptop cool and quiet.

Reading battery state can be done in multiple ways. Classical method is some daemon periodically polling battery level using ACPI interface. On some systems, the battery sends events to udev whenever it (dis)charges by 1%, this event can be connected to some action using a udev rule.

Battery can be checked directly from the kernel using:

BAT0 could also have vendor name. For example, wacom_battery_0 for Wacom stylus pen.

Alternatively, you can use the upower abstraction utility:

Battery state can be read using ACPI utilities from the terminal. ACPI command line utilities are provided via the acpi package. See ACPI modules for more information.

If your battery sends events to udev whenever it (dis)charges by 1%, you can use this udev rule to automatically hibernate the system when battery level is critical, and thus prevent all unsaved work from being lost. Alternatively, upower can also take action when battery level is at a configurable critical level if upower.service is enabled.

This rule will be repeated whenever the condition is set. As such, when resuming from hibernate when the battery is critical, the computer will hibernate directly. Some laptops do not boot beyond a certain battery level, so the rule could be adjusted accordingly.

If you have more than one battery or if you are using a battery powered peripheral device, the rule could be triggered unexpectedly by another battery discharging; this can be fixed by obtaining another attribute/value pair to add to your udev rule that specifically match the main battery, for example model_name. Such new attribute/value pair can be obtained for example by checking /sys/class/power_supply/nameOfMainBattery/attributesAndOtherDirectories, or by running udevadm monitor --property and waiting for battery events.

Batteries can jump to a lower value instead of discharging continuously, therefore a udev string matching pattern for all capacities 0 through 5 is used.

To shutdown the system instead of hibernating, use /usr/bin/systemctl poweroff. The -i flag can be used to ignore shutdown inhibitors, see systemctl(1) § OPTIONS. Other rules can be added to perform different actions depending on power supply status and/or capacity.

If your system has no or missing ACPI events, frequently run the following script which uses acpi:

If you have more than one battery or if you are using a battery powered peripheral device, you should modify the second line of the script by adding grep to monitor the correct battery like so: acpi -b | grep "Battery 0" | awk -F'[,:%]' '{print $2, $3}' | {. Replace Battery 0 with your required battery as reported by acpi -b.

One way to test udev rules is to have them create a file when they are run. For example:

This creates a file at /home/archie/discharging when the laptop charger is unplugged. You can test whether the rule worked by unplugging your laptop and looking for this file. For more advanced udev rule testing, see Udev#Testing rules before loading.

Configure UPower, for example:

Enable and start upower.service afterwards.

Manually suspending the operating system, either to memory (standby) or to disk (hibernate) sometimes provides the most efficient way to optimize battery life, depending on the usage pattern of the laptop.

See the main article Suspend and hibernate.

To prevent your laptop hard drive from spinning down too often, set less aggressive power management as described in hdparm#Power management configuration. Even the default values may be too aggressive.

Wakeup sources/events/triggers wake the system from any of the hardware power-saving states. To find and configure these see wakeup triggers.

To get your touchpad working properly, see the libinput page. Touchpad Synaptics is the older input driver, which is currently in maintenance mode and is no longer updated.

If a touchpad device is not detected and shown as a device at all, a possible solution might be using one or more of these kernel parameters:

If an Elantech Touchpad is not being detected and the following line appears in your journal:

it is related to an issue with the psmouse module trying to use a secondary bus for the touchpad device, and elan_i2c failing to do so. The fix is to force it to use the primary one. Create the file below and reload the psmouse module or reboot:

See Fingerprint-gui, fprint and ThinkFinger (for ThinkPads).

There are several laptops from different vendors featuring shock protection capabilities. As manufacturers have refused to support open source development of the required software components so far, Linux support for shock protection varies considerably between different hardware implementations.

Currently, two projects, named HDAPS and Hpfall, support this kind of protection. HDAPS is for IBM/Lenovo Thinkpads and hpfall for HP/Compaq laptops.

The laptop manufacturers developed new technologies involving two graphic cards in a single computer, enabling both high performance and power saving usages. These laptops usually use an Intel chip for display by default, so an Intel graphics driver is needed first. Then you can choose methods to utilize the second graphics chip.

Use of hardware decoding and encoding can lead to a higher battery life. See Video acceleration.

On laptops using Intel HD Audio, the user may need to manually specify the codec model in order to get the audio mute LED to work. First, check if your laptop uses Intel HD Audio; the following command will produce output if so:

Next, you will need to find your audio codec model:

Now you need to find their codec in the list of available model names. If you cannot find a codec for your specific model, you may be able to find one that works through trial and error.

In order to tell the kernel module which model-specific options to load, specify the model= kernel module parameter. For example:

To test whether or not this worked, the kernel module must be reloaded. You can do this by rebooting.

If you need to test a large number of codecs, it may be more efficient to avoid rebooting by first bringing the system to a state where no processes are using the kernel module, and then reloading the module with the new parameters. This can be done by logging out of all graphical and console sessions, and stopping the display manager if using one. Upon logging back in at a console, run the following commands:

The module will now be using the new codec specified in model_name.

For a laptop, it may be a good idea to use Chrony as an alternative to NTPd, OpenNTPD or systemd-timesyncd to sync your clock over the network. Chrony is designed to work well even on systems with no permanent network connection (such as laptops), and is capable of much faster time synchronisation than standard ntp. Chrony has several advantages when used in systems running on virtual machines, such as a larger range for frequency correction to help correct quickly drifting clocks, and better response to rapid changes in the clock frequency. It also has a smaller memory footprint and no unnecessary process wakeups, improving power efficiency.

See Help:Laptop page guidelines if you want to create or modify any laptop page.

Pages specific to certain laptop types

**Examples:**

Example 1 (unknown):
```unknown
$ cat /sys/class/power_supply/BAT0/capacity
```

Example 2 (unknown):
```unknown
wacom_battery_0
```

Example 3 (unknown):
```unknown
$ for BAT_PATH in $(upower -e | grep BAT); do upower -i "$BAT_PATH"; done
```

Example 4 (unknown):
```unknown
upower.service
```

---

## Powertop

**URL:** https://wiki.archlinux.org/title/Powertop

**Contents:**
- Installation
- Usage
  - Generate reports
  - Apply settings
- Troubleshooting
  - Error: Cannot load from file
  - Calibration to prevent inaccurate measurement
  - Display power estimation
- See also

Powertop is a tool provided by Intel to enable various powersaving modes in userspace, kernel and hardware. It is possible to monitor processes and show which of them are utilizing the CPU and wake it from its Idle-States, allowing to identify applications with particular high power demands.

Install the powertop package.

Powertop's interactive mode can be invoked with:

In interactive mode, you can modify recommended settings in the Tunables and WakeUp tabs. This allows you to change settings and monitor how they affect your power consumption in the Overview tab. However this does not persist any settings and the changes will be lost on reboot.

Powertop can generate reports in either CSV or HTML format. The HTML export is an interactive document that shows recommended settings. Make sure to reboot to revert to system defaults before generating a report!

You can also extract the recommended parameters by following these steps:

Newer versions of Powertop include the --auto-tune-dump option which will output the commands Powertop's --auto-tune would have run. This is useful for including in a script in case you do not want to run all of Powertop's recommendations.

There are two ways to automatically apply the suggested settings:

You can also add this line to the [Service] section in order to prevent your plugged-in USB input devices from getting disconnected on boot:

If you receive an error like the following when starting powertop, it is likely that powertop has not collected enough measurement data yet. To fix this, keep powertop running for a certain time connected to battery power only.

If you experience inaccurate measurement, then it is likely that you need to calibrate powertop first. This can be done by running powertop with the --calibrate parameter.

Prior to displaying the power usage estimation column, powertop needs to run 270 measurements. Each one lasts 20 seconds, which means you need to let powertop run for 1h30 in total.

**Examples:**

Example 1 (unknown):
```unknown
# powertop --html=powerreport.html
```

Example 2 (unknown):
```unknown
$ awk -F '</?td ?>' '/tune/ { print $4 }' powerreport.html
```

Example 3 (unknown):
```unknown
--auto-tune-dump
```

Example 4 (unknown):
```unknown
--auto-tune
```

---

## Laptop/Apple

**URL:** https://wiki.archlinux.org/title/Laptop/Apple

**Contents:**
- Model list
- Troubleshooting
  - MacBook2,1 Mid 2007
    - Boot loader
    - Rebooting
    - Microphone
  - MacBookAir1,1 Early 2008
  - MacBookAir2,1 Mid 2009
  - MacBookPro6,2 Mid 2010
  - MacBookPro7,1 Mid 2010

The factual accuracy of this article or section is disputed.

See UEFI#UEFI firmware bitness: this machine runs a 32-bit EFI. This means you should make sure the boot loader you choose supports mixed mode booting (i.e. a 64-bit OS on a 32-bit UEFI). For GRUB, use i386-efi as the target.

The MacBook will not reboot properly by default. It needs the reboot=pci kernel parameter.

This article or section is a candidate for merging with PulseAudio/Troubleshooting.

If your microphone is not working, you have probably run into a driver bug which makes PulseAudio think the digital microphone is always plugged in, disabling the normal microphone.

To work around it, disable the PulseAudio plug detector with this patch:

Since this model has only one USB port, you may find it easiest to install Arch with a powered USB hub. Plug a USB network adapter (wireless or ethernet adapter to plug into a USB port) and your Arch installation media into the USB hub.

See Mac/Troubleshooting#Wi-Fi. If you cannot get any result by scanning wireless network after boot, unload modules b43 and ssb and load them again:

There is a good chance you will find what's wrong with DMA from the dmesg log.

Even if you can scan wireless networks after reloading the modules, it is still possible that you will only be able to connect to some networks, but not all of them. According to a more detailed discussion here: https://crunchbang.org/forums/viewtopic.php?id=17368, adding pio=1,qos=0 options to the b43 module can solve this problem.

See Mac/Troubleshooting#Wi-Fi. Append options b43 pio=1 qos=0 to /etc/modprobe.d/b43.conf.

Heat issues solved with mbpfan-gitAUR.

On this model only the nouveau driver can be installed when booting in UEFI mode, nvidia-340xx-dkmsAUR causes a black blank screen when Xorg loads.

Booting the installation media, you might encounter the following error:

To fix this problem, boot with the option: acpi=off. After chrooting, add MODULES=(ata_generic) to /etc/mkinitcpio.conf and regenerate the initramfs, see Installation guide#Configure the system.

If you have issues with waking from sleep while in X11 such as a black screen or showing the console with a frozen mouse cursor then remove xf86-input-synaptics and install xf86-input-mtrack-gitAUR. This fixed errors such as

and backtraces that causes X11 to crash. This might apply to Version 5,2 assuming they use the same trackpad.

Unless you have a local repository on a USB disk, you need a USB to Ethernet adapter or a USB wireless adapter supported natively by the kernel to easily install Arch Linux, since you have to install the broadcom-wl-dkms package to make the internal wireless card work.

rEFInd uses 30 seconds to start booting, following Mac/Troubleshooting#Avoid long EFI wait before booting stops rEFInd from loading and it has to be re-installed.

The brcmfmac driver is working as of 2015-11-20, with newer firmware necessary for working 5GHz support (see here.)

Then check whether PCI runtime power management is enabled on the device, and disable it if so.

Haptic feedback works out of the box due to the trackpad's built-in firmware.

There are several drivers available that provide multitouch support. The following have been confirmed working with the MacBookPro12,1.

For xf86-input-libinput the following configuration emulates some features from the macOS functionality. For more options see libinput(4).

For xf86-input-synaptics the following configuration is necessary to make the touchpad work fully.

See MacBookPro11,x#Graphics to enable the integrated graphics. See PRIME for details on handling hybrid graphics.

If you are experiencing flickering issues with Xorg, you can set i915.enable_rc6=0 as a kernel parameter, which will disable the power savings for the Intel graphics.

Internal keyboard, trackpad, Touch Bar (if your model has one), Wi-fi, and Bluetooth will not work unless you have necessary kernel modules and firmwares. You should follow the guide on https://wiki.t2linux.org/distributions/arch/installation/ for hardware support.

It seems the amdgpu driver has problems to set the native 5k resolution. If the display gets corrupted during boot when the amdgpu driver module is loaded, try forcing a lower resolution. Add e.g. video=2560x1440@60 to your kernel parameters.

**Examples:**

Example 1 (unknown):
```unknown
snd_hda_intel model=mb5
```

Example 2 (unknown):
```unknown
brcmfmac.feature_disable=0x82000
```

Example 3 (unknown):
```unknown
--- a/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf
+++ b/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf
@@ -23,6 +23,8 @@

 [Jack Mic]
 required-any = any
+state.plugged = unknown
+state.unplugged = unknown

 [Jack Mic Phantom]
 required-any = any
@@ -31,6 +33,8 @@

 [Jack Mic - Input]
 required-any = any
+state.plugged = unknown
+state.unplugged = unknown

 [Element Capture]
 switch = mute
```

Example 4 (unknown):
```unknown
# rmmod ssb
# rmmod b43
# modprobe b43
```

---

## Power management/Wakeup triggers

**URL:** https://wiki.archlinux.org/title/Wakeup_triggers

**Contents:**
- Wakeup trigger interfaces
  - /proc/acpi/wakeup
  - /sys/module/acpi/parameters/ec_no_wakeup
  - /sys/devices/
  - /sys/class/wakeup/*
- Persistent settings
  - One-time with systemd
  - Event-driven with udev
- Troubleshooting
  - List device and/or bus trees

Wakeup triggers are event sources that can wake the system from any of the hardware power-saving states. The obvious example is the power or suspend button, the Wake-on-LAN functionality or the lid switch in laptop systems. Wakeup triggers can be controlled through various kernel interfaces listed below. There is no unified interface covering all possible triggers.

Reading the /proc/acpi/wakeup file yields list of ACPI-registered wakeup sources with corresponding sysfs IDs where available. Writing an entry from the Device column to the file toggles its state. For example, to disable waking on opening the laptop lid, run:

This file represents the value of ACPI kernel module option ec_no_wakeup, which controls passing the wakeup triggers from embedded controller when the system is in the suspend-to-idle (s2idle) power state [1]. On modern laptops embedded controller wakeups can cause excessive battery drain in some cases.

Each sysfs device that supports wakeup contains the file wakeup in a device's power subdirectory. The file contains wakeup trigger's status and can be written to as well. Bus controllers as well as endpoint devices can be capable of waking up the system. For example, to disable wakeups from the first USB controller (bus), run:

An endpoint device should be able to wake the device if the trigger is enabled regardless of the controller's setting, however this might be hardware-dependent.

Program PowerTOP interfaces with sysfs, but it only lists wakeup triggers of networking and USB devices by reading /sys/class/net/ and /sys/bus/usb/devices/ (containing symlinks to /sys/devices/).

Almost all wakeup triggers can be found in the /sys/class/wakeup directory, which contains symlinks to all relevant devices. This is useful for finding possible wakeup triggers by going through subdirectories. Some of the triggers can correspond to virtual devices while hardware-related wakeup triggers are the ones that contain at least one of these files:

Some of wakeup triggers in /sys/class/wakeup also provide a link to the cryptic /proc/acpi/wakeup names where the following file is present:

The one-time methods should suffice for setting the /proc/acpi/wakeup states and acpi.ec_no_wakeup kernel parameter while the event-driven approach with udev is the reliable way to configure the sysfs devices.

The ec_no_wakeup ACPI kernel module option can be set at boot as described in the article. The standard solution to set the sysfs values at boot are systemd services such as in this troubleshooting case. Another systemd-based manager for /proc/acpi/wakeup is wakeup-triggersAUR.

Some systems can override some of the ACPI wakeup triggers upon power state transition(s) in what is more of a bug rather than a feature. If the hardware is overriding triggers at predictable times that can still be solved with appropriately crafted systemd units. The sleep.target is a generic target covering all different suspended states that might be helpful in this case, but there is no generic wakeup.target [2].

This method only works reliably with sysfs devices that are connected all the time.

Setting the wakeup trigger status with udev rules is an event-driven method that works reliably any time the devices with wakeup triggers are connected. The key is to detect an addition of a new device (ACTION=="add") in a rule and set the wakeup trigger status with ATTR{power/wakeup}="disabled". If the hardware is resetting this setting, udev can try to circumvent it by reapplying rules upon every device change (ACTION=="add|change"). A device tree with possible parameters for matching a particular device found in sysfs can be obtained with udevadm info -q all -a /sys/devices/....

A representative common example here would be a Logitech Unifying USB receiver. Its wakeup trigger should be enabled by default and if that is not desired, a solution could be a udev rule, as follows:

The reverse case to enable the necessary trigger(s) is described in the udev article.

udev triggers so early in the device enumeration that disabling wakeup trigger with the method above causes (some?) disabled triggers to not be listed in /sys/class/wakeup. That might be dependent on whether the device was already present at boot and needs further clarification.

These auxiliary commands can be helpful when trying to understand all wakeup triggers of a certain system, to aid with udev rule writing or general wakeup source troubleshooting:

The information on which wakeup source was the reason for the last device wakeup is unfortunately platform-specific. On x86 machines dmidecode can be used:

However for some computers it always reports "Power Switch" regardless of the real cause, e.g. for any of the USB keyboard, laptop keyboard, the power switch and the mouse.

For some Intel Haswell systems with the LynxPoint and LynxPoint-LP chipset, instantaneous wakeups after suspending are reported. They are linked to erroneous BIOS ACPI implementations and how the xhci_hcd module interprets it during boot. As a work-around reported affected systems are added to a denylist (named XHCI_SPURIOUS_WAKEUP) by the kernel case-by-case [3].

Wakeup may happen, for example, if a USB device is plugged during suspending and ACPI wakeup triggers are enabled. A viable workaround for such a system is to disable the relevant wakeup triggers. An example to disable wakeup through USB is described as follows [4].

To view the current configuration:

The relevant devices are EHC1, EHC2 and XHC (for USB 3.0). To toggle their state you have to echo the device name to the file as root:

This should result in suspension working again. However, this settings are only temporary and need to be set at every boot. To automate this, see systemd-tmpfiles or BBS thread for possible solutions.

On some Gigabyte motherboards, the GPP bridge to the NVMe drive may cause premature wakeups from suspend.

Known boards affected:

Setting the status of GPP0 to disabled may fix the issue:

Same as the Haswell solution above, this setting is only temporary. An example of automating the fix can be found in this BBS thread.

For some Gigabyte motherboards, disabling everything in /proc/acpi/wakeup including GPP0 does not prevent an instantaneous wakeup from suspension. If this is the case, your motherboard may have issues with ACPI in Linux.

Known boards affected:

Apply the following to your kernel parameters:

Certain ASRock motherboards for the AM5 platform may instantly wake from sleep also. This is due to the USB xHCI controller.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:

This behaviour has been noticed on the B850M Pro RS model (and will presumably also extend to the very similar B850M Pro RS WiFi.)

Certain MSI motherboards for the AM5 platform may also be affected by the premature wakeups from suspend because of the GPP bridge to the NVME drive.

This can be fixed by disabling wakeup on this device, in line with the Gigabyte instructions above:

This behaviour has been noticed on the X870 Tomahawk model.

For some newer AMD Ryzen 7000 Series systems, instantaneous wakeups after suspending, or wake up from s2idle when plugging in the AC adapter or by closing the lid, may occur. It is due to the redundant IRQ interrupt from the GPIO controller in AMDI0030:00. [5][6]

The current workaround is to configure the kernel to ignore the interrupt from the problematic GPIO pins. Add the following to your kernel parameters:

Multiple GPIO pins can be appended to the ignore list in the format of AMDI0030:00@N. However, the corresponding GPIO pins that cause the system to wake up is depended to the device model. You may find the pin number from the dmesg log after enabling debug messages from the system suspend/hibernation infrastructure:

Perform a suspend/resume cycle, you may find the following lines in dmesg log.

Usually GPIO 2, 3 and 4 would be the one response to this issue. Then, you may mount the debugfs to /sys/kernel/debug to trace the state of the GPIOs.

Look for the lines in /sys/kernel/debug/gpio with data in S0i3 and S3 columns.

Ignore the corresponding GPIO pins in gpiolib_acpi.ignore_interrupt, regenerate the initramfs image, and reboot.

Installing NVIDIA proprietary drivers might render suspension and hibernation not possible. In that case the system log might include:

See NVIDIA/Tips and tricks#Preserve video memory after suspend.

If the nouveau driver is used, the reason for instantaneous wakeups may be a bug in the driver, which sometimes prevents GPU from suspending. A possible workaround is unloading the nouveau kernel module right before going to sleep and loading it back after wakeup. To do this, create the following script:

The first echo line unbinds nouveaufb from the framebuffer console driver (fbcon). Usually it is vtcon1 as in this example, but it may also be another vtcon*. See /sys/class/vtconsole/vtcon*/name which one of them is a frame buffer device [7].

The Logitech Bolt receiver is a dongle with a yellow hexagon that has a lightning bolt shape cut out of it. It can cause immediate wakeup after suspending. See Logitech Unifying Receiver#PC wakes immediately from sleep.

**Examples:**

Example 1 (unknown):
```unknown
/proc/acpi/wakeup
```

Example 2 (unknown):
```unknown
# echo "LID" > /proc/acpi/wakeup
```

Example 3 (unknown):
```unknown
ec_no_wakeup
```

Example 4 (unknown):
```unknown
# echo "disabled" > /sys/bus/usb/devices/usb1/power/wakeup
```

---
