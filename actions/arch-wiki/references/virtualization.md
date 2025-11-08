# Arch-Wiki - Virtualization

**Pages:** 5

---

## QEMU

**URL:** https://wiki.archlinux.org/title/QEMU

**Contents:**
- Installation
  - QEMU variants
  - Details on packages available in Arch Linux
- Graphical front-ends for QEMU
- Creating a new virtualized system
  - Creating a hard disk image
    - Overlay storage images
    - Resizing an image
      - Shrinking an image
    - Converting an image

According to the QEMU about page:

QEMU can use other hypervisors like Xen or KVM to use CPU extensions (HVM) for virtualization. When used as a virtualizer, QEMU achieves near native performance by executing the guest code directly on the host CPU.

Install the qemu-full package (or qemu-base for the version without GUI and qemu-desktop for the version with only x86_64 emulation by default) and below optional packages for your needs:

Alternatively, qemu-user-static exists as a usermode and static variant.

QEMU is offered in several variants suited for different use cases.

As a first classification, QEMU is offered in full-system and usermode emulation modes:

QEMU is offered in dynamically-linked and statically-linked variants:

In the case of Arch Linux, full-system emulation is offered as:

Note that headless and non-headless versions install commands with the same name (e.g. qemu-system-x86_64) and thus cannot be both installed at the same time.

Unlike other virtualization programs such as VirtualBox and VMware, QEMU does not provide a GUI to manage virtual machines (other than the window that appears when running a virtual machine), nor does it provide a way to create persistent virtual machines with saved settings. All parameters to run a virtual machine must be specified on the command line at every launch, unless you have created a custom script to start your virtual machine(s).

Libvirt provides a convenient way to manage QEMU virtual machines. See list of libvirt clients for available front-ends.

The factual accuracy of this article or section is disputed.

To run QEMU you will need a hard disk image, unless you are booting a live system from CD-ROM or the network (and not doing so to install an operating system to a hard disk image). A hard disk image is a file which stores the contents of the emulated hard disk.

A hard disk image can be raw, so that it is literally byte-by-byte the same as what the guest sees, and will always use the full capacity of the guest hard drive on the host. This method provides the least I/O overhead, but can waste a lot of space, as not-used space on the guest cannot be used on the host.

Alternatively, the hard disk image can be in a format such as qcow2 which only allocates space to the image file when the guest operating system actually writes to those sectors on its virtual hard disk. The image appears as the full size to the guest operating system, even though it may take up only a very small amount of space on the host system. This image format also supports QEMU snapshotting functionality (see #Creating and managing snapshots via the monitor console for details). However, using this format instead of raw will likely affect performance.

QEMU provides the qemu-img command to create hard disk images. For example to create a 4 GiB image in the raw format:

You may use -f qcow2 to create a qcow2 disk instead.

You can create a storage image once (the 'backing' image) and have QEMU keep mutations to this image in an overlay image. This allows you to revert to a previous state of this storage image. You could revert by creating a new overlay image at the time you wish to revert, based on the original backing image.

To create an overlay image, issue a command like:

After that you can run your QEMU virtual machine as usual (see #Running a virtualized system):

The backing image will then be left intact and mutations to this storage will be recorded in the overlay image file.

When the path to the backing image changes, repair is required.

Make sure that the original backing image's path still leads to this image. If necessary, make a symbolic link at the original path to the new path. Then issue a command like:

At your discretion, you may alternatively perform an 'unsafe' rebase where the old path to the backing image is not checked:

The qemu-img executable has the resize option, which enables easy resizing of a hard drive image. It works for both raw and qcow2. For example, to increase image space by 10 GiB, run:

After enlarging the disk image, you must use file system and partitioning tools inside the virtual machine to actually begin using the new space.

When shrinking a disk image, you must first reduce the allocated file systems and partition sizes using the file system and partitioning tools inside the virtual machine and then shrink the disk image accordingly. For a Windows guest, this can be performed from the "create and format hard disk partitions" control panel.

Then, to decrease image space by 10 GiB, run:

You can convert an image to other formats using qemu-img convert. This example shows how to convert a raw image to qcow2:

This will not remove the original input file.

To install an operating system into your disk image, you need the installation medium (e.g. optical disc, USB-drive, or ISO image) for the operating system. The installation medium should not be mounted because QEMU accesses the media directly.

This is the first time you will need to start the emulator. To install the operating system on the disk image, you must attach both the disk image and the installation media to the virtual machine, and have it boot from the installation media.

For example on i386 guests, to install from a bootable ISO file as CD-ROM and a raw disk image:

See qemu(1) for more information about loading other media types (such as floppy, disk images or physical drives) and #Running a virtualized system for other useful options.

After the operating system has finished installing, the QEMU image can be booted directly (see #Running a virtualized system).

In many cases, it is not necessary or desired to manually install your own operating system, for instance in a cloud environment. Luckily, many pre-made images are available for download from different providers.

For Arch Linux, we have the arch-boxes project with weekly image releases.

There are similar images available for Fedora and Debian.

qemu-system-* binaries (for example qemu-system-i386 or qemu-system-x86_64, depending on guest's architecture) are used to run the virtualized guest. The usage is:

Options are the same for all qemu-system-* binaries, see qemu(1) for documentation of all options.

Usually, if an option has many possible values, you can use

to list all possible values. If it supports properties, you can use

to list all available properties.

You can use these methods and the qemu(1) documentation to understand the options used in the following sections.

By default, QEMU will show the virtual machine's video output in a window. One thing to keep in mind: when you click inside the QEMU window, the mouse pointer is grabbed. To release it, press Ctrl+Alt+g.

KVM (Kernel-based Virtual Machine) full virtualization must be supported by your Linux kernel and your hardware, and necessary kernel modules must be loaded. See KVM for more information.

To start QEMU in KVM mode, append -accel kvm to the additional start options. To check if KVM is enabled for a running virtual machine, enter the #QEMU monitor and type info kvm.

First enable IOMMU, see PCI passthrough via OVMF#Setting up IOMMU.

Add -device intel-iommu to create the IOMMU device:

The default firmware used by QEMU is SeaBIOS, which is a Legacy BIOS implementation. QEMU uses /usr/share/qemu/bios-256k.bin (provided by the seabios package) as a default read-only (ROM) image. You can use the -bios argument to select another firmware file. However, UEFI requires writable memory to work properly, so you need to emulate PC System Flash instead.

OVMF is a TianoCore project to enable UEFI support for Virtual Machines. It can be installed with the edk2-ovmf package.

There are two ways to use OVMF as a firmware. The first is to copy /usr/share/edk2/x64/OVMF.4m.fd, make it writable and use as a pflash drive:

All changes to the UEFI settings will be saved directly to this file.

Another and more preferable way is to split OVMF into two files. The first one will be read-only and store the firmware executable, and the second one will be used as a writable variable store. The advantage is that you can use the firmware file directly without copying, so it will be updated automatically by pacman.

Use /usr/share/edk2/x64/OVMF_CODE.4m.fd as a first read-only pflash drive. Copy /usr/share/edk2/x64/OVMF_VARS.4m.fd, make it writable and use as a second writable pflash drive:

To enable Secure Boot, you must use OVMF firmware files that have Secure Boot keys installed, which is not provided by the upstream project[1].

Unlike some other Linux distributions (e.g., Fedora), Arch Linux does not yet provide its own firmware files that are pre-enrolled with Secure Boot enabled:

Although the firmware file /usr/share/edk2/x64/OVMF_VARS.secboot.4m.fd exists and appears to support Secure Boot, it does not. Using it will result in a non-bootable virtual system until you swap it with another firmware file to make it bootable again.

A simple workaround is to use Fedora's version by installing the edk2-ovmf-fedora package from the AUR:

With that, Secure Boot is now enabled on your VMs!

Alternatively, you can provide your own OVMF_VARS and manually enroll it with your own keys. See KVM#Secure Boot on how to do this.

QEMU can emulate Trusted Platform Module, which is required by some systems such as Windows 11 (which requires TPM 2.0).

Install the swtpm package, which provides a software TPM implementation. Create some directory for storing TPM data (/path/to/mytpm will be used as an example). Run this command to start the emulator:

/path/to/mytpm/swtpm-sock will be created by swtpm: this is a UNIX socket to which QEMU will connect. You can put it in any directory.

By default, swtpm starts a TPM version 1.2 emulator. The --tpm2 option enables TPM 2.0 emulation.

Finally, add the following options to QEMU:

and TPM will be available inside the virtual machine. After shutting down the virtual machine, swtpm will be automatically terminated.

See the QEMU documentation for more information.

If guest OS still does not recognize the TPM device, try to adjust CPU Models and Topology options. It might cause problem.

Data can be shared between the host and guest OS using any network protocol that can transfer files, such as NFS, SMB, NBD, HTTP, FTP, or SSH, provided that you have set up the network appropriately and enabled the appropriate services.

The default SLIRP-based user-mode networking allows the guest to access the host OS at the IP address 10.0.2.2. Any servers that you are running on your host OS, such as a SSH server or SMB server, will be accessible at this IP address. So on the guests, you can mount directories exported on the host via SMB or NFS, or you can access the host's HTTP server, etc. It will not be possible for the host OS to access servers running on the guest OS, but this can be done with other network configurations (see #Tap networking with QEMU).

QEMU can forward ports from the host to the guest to enable e.g. connecting from the host to an SSH server running on the guest.

For example, to bind port 60022 on the host with port 22 (SSH) on the guest, start QEMU with a command like:

Make sure the sshd is running on the guest and connect with:

You can use SSHFS to mount the guest's file system at the host for shared read and write access.

To forward several ports, you just repeat the hostfwd in the -nic argument, e.g. for VNC's port:

A secure and convenient way to connect to the VM is to use SSH over vsock(7). Your VM needs to be systemd-based for this to work out of the box.

First, launch QEMU with a special device:

The cid needs to be picked by the user to be a valid 32-bit number (see vsock(7)). When systemd detects the VM has been launched with a vhost-vsock device, it will automatically launch an SSH server via systemd-ssh-generator.

You can then connect to the VM like this:

This works because of /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf which tells your SSH client to use systemd-ssh-proxy to allow SSH to use vsock.

Furthermore, using systemd.system-credentials(7) we can inject an authorized keys file for the root user which is very convenient in case we are trying to run a downloaded image. This can be done like so:

The public key line has to be provided as a base64-encoded string. This can be done like so:

The same mechanism via -smbios type=11,value=io.systemd... can be used to inject a variety of other magical variables that will get acted on by systemd. See also systemd docs: System and Service Credentials.

QEMU's documentation says it has a "built-in" SMB server, but actually it just starts up Samba on the host with an automatically generated smb.conf file located in /tmp/qemu-smb.random_string and makes it accessible to the guest at a different IP address (10.0.2.4 by default). This only works for user networking, and is useful when you do not want to start the normal Samba service on the host, which the guest can also access if you have set up shares on it.

Only a single directory can be set as shared with the option smb=, but adding more directories (even while the virtual machine is running) could be as easy as creating symbolic links in the shared directory if QEMU configured SMB to follow symbolic links. It does not do so, but the configuration of the running SMB server can be changed as described below.

Samba must be installed on the host. To enable this feature, start QEMU with a command like:

where shared_dir_path is a directory that you want to share between the guest and host.

Then, in the guest, you will be able to access the shared directory on the host 10.0.2.4 with the share name "qemu". For example, in Windows Explorer you would go to \\10.0.2.4\qemu.

One way to share multiple directories and to add or remove them while the virtual machine is running, is to share an empty directory and create/remove symbolic links to the directories in the shared directory. For this to work, the configuration of the running SMB server can be changed with the following script, which also allows the execution of files on the guest that are not set executable on the host:

This can be applied to the running server started by qemu only after the guest has connected to the network drive the first time. An alternative to this method is to add additional shares to the configuration file like so:

This share will be available on the guest as \\10.0.2.4\myshare.

See the QEMU documentation.

virtiofsd is shipped with the virtiofsd package. It is a modern and high-performance way to conveniently share files between host and guest. See the online documentation or /usr/share/doc/virtiofsd/README.md for a full list of available options.

You can choose to either run virtiofsd as root or as a regular user.

First, make sure that there is a subuid(5) and subgid(5) configuration entry for the user that will execute virtiofsd. See also the relevant section in the Podman article.

Then, start virtiofsd:

Add the user that runs QEMU to the kvm user group, because it needs to access the virtiofsd socket. You might have to logout for change to take effect.

Start virtiofsd as root:

Add the following configuration options when starting the virtual machine:

You may also boot a rootfs directly via virtiofsd. In addition to the above arguments, append:

Once logged into the guest as root, you can simply mount the share on any modern distribution:

This directory should now be shared between host and guest.

See relevant Windows section.

It can be useful to mount a drive image under the host system, it can be a way to transfer files in and out of the guest. This should be done when the virtual machine is not running.

The procedure to mount the drive on the host depends on the type of qemu image, raw or qcow2. We detail thereafter the steps to mount a drive in the two formats in #Mounting a partition from a raw image and #Mounting a partition from a qcow2 image. For the full documentation see Wikibooks:QEMU/Images#Mounting an image on the host.

It is possible to mount partitions that are inside a raw disk image file by setting them up as loopback devices.

One way to mount a disk image partition is to mount the disk image at a certain offset using a command like the following:

The offset=32256 option is actually passed to the losetup program to set up a loopback device that starts at byte offset 32256 of the file and continues to the end. This loopback device is then mounted. You may also use the sizelimit option to specify the exact size of the partition, but this is usually unnecessary.

Depending on your disk image, the needed partition may not start at offset 32256. Run fdisk -l disk_image to see the partitions in the image. fdisk gives the start and end offsets in 512-byte sectors, so multiply by 512 to get the correct offset to pass to mount.

The Linux loop driver actually supports partitions in loopback devices, but it is disabled by default. To enable it, do the following:

Set up your image as a loopback device:

Then, if the device created was /dev/loop0, additional devices /dev/loop0pX will have been automatically created, where X is the number of the partition. These partition loopback devices can be mounted directly. For example:

To mount the disk image with udisksctl, see Udisks#Mount loop devices.

kpartx from the multipath-tools package can read a partition table on a device and create a new device for each partition. For example:

This will setup the loopback device and create the necessary partition(s) device(s) in /dev/mapper/.

We will use qemu-nbd, which lets us use the NBD (network block device) protocol to share the disk image.

First, we need the nbd module loaded:

Then, we can share the disk and create the device entries:

Discover the partitions:

fdisk can be used to get information regarding the different partitions in nbd0:

Then mount any partition of the drive image, for example the partition 2:

After the usage, it is important to unmount the image and reverse previous steps, i.e. unmount the partition and disconnect the nbd device:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The performance of virtual networking should be better with tap devices and bridges than with user-mode networking or vde because tap devices and bridges are implemented in-kernel.

In addition, networking performance can be improved by assigning virtual machines a virtio network device rather than the default emulation of an e1000 NIC. See #Using virtio drivers for more information.

By giving the -net nic argument to QEMU, it will, by default, assign a virtual machine a network interface with the link-level address 52:54:00:12:34:56. However, when using bridged networking with multiple virtual machines, it is essential that each virtual machine has a unique link-level (MAC) address on the virtual machine side of the tap device. Otherwise, the bridge will not work correctly, because it will receive packets from multiple sources that have the same link-level address. This problem occurs even if the tap devices themselves have unique link-level addresses because the source link-level address is not rewritten as packets pass through the tap device.

Make sure that each virtual machine has a unique link-level address, but it should always start with 52:54:. Use the following option, replace X with arbitrary hexadecimal digit:

Generating unique link-level addresses can be done in several ways:

In a script, you can use for example:

By default, without any -netdev arguments, QEMU will use SLIRP-based user-mode networking with a built-in DHCP server. Your virtual machines will be assigned an IP address when they run their DHCP client, and they will be able to access the physical host's network through IP masquerading done by QEMU.

This default configuration allows your virtual machines to easily access the Internet, provided that the host is connected to it, but the virtual machines will not be directly visible on the external network, nor will virtual machines be able to talk to each other if you start up more than one concurrently.

QEMU's user-mode networking can offer more capabilities such as built-in TFTP or SMB servers, redirecting host ports to the guest (for example to allow SSH connections to the guest) or attaching guests to VLANs so that they can talk to each other. See the QEMU documentation on the -net user flag for more details.

However, SLIRP-based user-mode networking has limitations in both utility and performance. More advanced network configurations require the use of tap devices or other methods.

Users can choose to use passt-based user-mode networking. passt has several advantages over SLIRP such as better performance, full IPv6 support (including ICMPv6), better security, and more control.

To get started, install passt. There are two ways to launch it: Either via socket-based communication or via shared vhost-user. The latter method has better performance.

For the socket-based way, first launch passt:

Then, for your QEMU command, add these parameters:

For the vhost-user way, launch passt with --vhost-user

Then, for your QEMU command, add these parameters:

Notice the memory sizes of -m 4G and size=4G have to match exactly.

Tap devices are a Linux kernel feature that allows you to create virtual network interfaces that appear as real network interfaces. Packets sent to a tap interface are delivered to a userspace program, such as QEMU, that has bound itself to the interface.

QEMU can use tap networking for a virtual machine so that packets sent to the tap interface will be sent to the virtual machine and appear as coming from a network interface (usually an Ethernet interface) in the virtual machine. Conversely, everything that the virtual machine sends through its network interface will appear on the tap interface.

Tap devices are supported by the Linux bridge drivers, so it is possible to bridge together tap devices with each other and possibly with other host interfaces such as eth0. This is desirable if you want your virtual machines to be able to talk to each other, or if you want other machines on your LAN to be able to talk to the virtual machines.

As indicated in the user-mode networking section, tap devices offer higher networking performance than user-mode. If the guest OS supports virtio network driver, then the networking performance will be increased considerably as well. Supposing the use of the tap0 device, that the virtio driver is used on the guest, and that no scripts are used to help start/stop networking, next is part of the qemu command one should see:

But if already using a tap device with virtio networking driver, one can even boost the networking performance by enabling vhost, like:

See [3] for more information.

If the bridge is given an IP address and traffic destined for it is allowed, but no real interface (e.g. eth0) is connected to the bridge, then the virtual machines will be able to talk to each other and the host system. However, they will not be able to talk to anything on the external network, provided that you do not set up IP masquerading on the physical host. This configuration is called host-only networking by other virtualization software such as VirtualBox.

If you do not give the bridge an IP address and add an iptables rule to drop all traffic to the bridge in the INPUT chain, then the virtual machines will be able to talk to each other, but not to the physical host or to the outside network. This configuration is called internal networking by other virtualization software such as VirtualBox. You will need to either assign static IP addresses to the virtual machines or run a DHCP server on one of them.

By default iptables would drop packets in the bridge network. You may need to use such iptables rule to allow packets in a bridged network:

This method does not require a start-up script and readily accommodates multiple taps and multiple bridges. It uses /usr/lib/qemu/qemu-bridge-helper binary, which allows creating tap devices on an existing bridge.

First, create a configuration file containing the names of all bridges to be used by QEMU:

Make sure /etc/qemu/ has 755 permissions. QEMU issues and GNS3 issues may arise if this is not the case.

Now start the virtual machine; the most basic usage to run QEMU with the default network helper and default bridge br0:

Using the bridge br1 and the virtio driver:

If you need more control over your virtual machine's networking or you have very specific needs that arent covered in the previous setctions, see QEMU/Advanced networking.

If you are using QEMU with various networking options a lot, you probably have created a lot of -netdev and -device argument pairs, which gets quite repetitive. You can instead use the -nic argument to combine -netdev and -device together, so that, for example, these arguments:

Notice the lack of network IDs, and that the device was created with model=. The first half of the -nic parameters are -netdev parameters, whereas the second half (after model=) are related with the device. The same parameters (for example, smb=) are used. To completely disable the networking use -nic none.

See QEMU networking documentation for more information on parameters you can use.

QEMU can emulate a standard graphics card text mode using -display curses command line option. This allows to type text and see text output directly inside a text terminal. Alternatively, -nographic serves a similar purpose.

QEMU can emulate several types of VGA card. The card type is passed in the -vga type command line option and can be std, qxl, vmware, virtio, cirrus or none.

With -vga std you can get a resolution of up to 2560 x 1600 pixels without requiring guest drivers. This is the default since QEMU 2.2.

QXL is a paravirtual graphics driver with 2D support. To use it, pass the -vga qxl option and install drivers in the guest. You may want to use #SPICE for improved graphical performance when using QXL.

On Linux guests, the qxl and bochs_drm kernel modules must be loaded in order to gain a decent performance.

Default VGA memory size for QXL devices is 16M which is sufficient to drive resolutions approximately up to QHD (2560x1440). To enable higher resolutions, increase vga_memmb.

Although it is a bit buggy, it performs better than std and cirrus. Install the VMware drivers xf86-video-vmwareAUR and xf86-input-vmmouse for Arch Linux guests.

virtio-vga / virtio-gpu is a paravirtual 3D graphics driver based on virgl. It's mature, currently supporting only Linux guests with mesa compiled with the option gallium-drivers=virgl.

To enable 3D acceleration on the guest system, select this vga with -device virtio-vga-gl and enable the OpenGL context in the display device with -display sdl,gl=on or -display gtk,gl=on for the SDL and GTK display output respectively. Successful configuration can be confirmed looking at the kernel log in the guest:

To enable Vulkan support in the guest, use options like -device virtio-vga-gl,hostmem=2G,blob=true,venus=true and install the vulkan-virtio in the guest system [4].

The cirrus graphical adapter was the default before 2.2. It should not be used on modern systems.

This is like a PC that has no VGA card at all. You would not even be able to access it with the -vnc option. Also, this is different from the -nographic option which lets QEMU emulate a VGA card, but disables the SDL display.

The SPICE project aims to provide a complete open source solution for remote access to virtual machines in a seamless way.

The following is an example of booting with SPICE as the remote desktop protocol, including the support for copy and paste from host:

The parameters have the following meaning:

A SPICE client is necessary to connect to the guest. In Arch, the following clients are available:

For clients that run on smartphone or on other platforms, refer to the Other clients section in spice-space download.

One way of connecting to a guest listening on Unix socket /tmp/vm_spice.socket is to manually run the SPICE client using $ remote-viewer spice+unix:///tmp/vm_spice.socket or $ spicy --uri="spice+unix:///tmp/vm_spice.socket", depending on the desired client. Since QEMU in SPICE mode acts similarly to a remote desktop server, it may be more convenient to run QEMU in daemon mode with the -daemonize parameter.

This example connects spicy to the local port 5999 which is forwarded through SSH to the guest's SPICE server located at the address my.domain.org, port 5930. Note the -f option that requests ssh to execute the command sleep 10 in the background. This way, the ssh session runs while the client is active and auto-closes once the client ends.

QEMU can automatically start a SPICE client with an appropriate socket, if the display is set to SPICE with the -display spice-app parameter. This will use the system's default SPICE client as the viewer, determined by your mimeapps.list files.

For Arch Linux guests, for improved support for multiple monitors or clipboard sharing, the following packages should be installed:

For guests under other operating systems, refer to the Guest section in spice-space download.

If you want to enable password authentication with SPICE you need to remove disable-ticketing from the -spice argument and instead add password=yourpassword. For example:

Your SPICE client should now ask for the password to be able to connect to the SPICE server.

You can also configure TLS encryption for communicating with the SPICE server. First, you need to have a directory which contains the following files (the names must be exactly as indicated):

An example of generation of self-signed certificates with your own generated CA for your server is shown in the Spice User Manual.

Afterwards, you can run QEMU with SPICE as explained above but using the following -spice argument: -spice tls-port=5901,password=yourpassword,x509-dir=/path/to/pki_certs, where /path/to/pki_certs is the directory path that contains the three needed files shown earlier.

It is now possible to connect to the server using virt-viewer:

Keep in mind that the --spice-host-subject parameter needs to be set according to your server-cert.pem subject. You also need to copy ca-cert.pem to every client to verify the server certificate.

The equivalent spice-gtk command is:

One can add the -vnc :X option to have QEMU redirect the VGA display to the VNC session. Substitute X for the number of the display (0 will then listen on 5900, 1 on 5901...).

An example is also provided in the #Starting QEMU virtual machines on boot section.

An access password can be setup easily by using the password option. The password must be indicated in the QEMU monitor and connection is only possible once the password is provided.

In the QEMU monitor, password is set using the command change vnc password and then indicating the password.

The following command line directly runs vnc with a password:

The -audiodev flag sets the audio backend driver on the host and its options.

To list availabe audio backend drivers:

Their optional settings are detailed in the qemu(1) man page.

At the bare minimum, one need to choose an audio backend and set an id, for PulseAudio for example:

For Intel HD Audio emulation, add both controller and codec devices. To list the available Intel HDA Audio devices:

Add the audio controller:

Also, add the audio codec and map it to a host audio backend id:

For AC97 emulation just add the audio card device and map it to a host audio backend id:

VirtIO sound is also available since QEMU 8.2.0. The usage is:

More information can be found in QEMU documentation.

QEMU offers guests the ability to use paravirtualized block and network devices using the virtio drivers, which provide better performance and lower overhead.

To use virtio devices after an Arch Linux guest has been installed, the following modules must be loaded in the guest: virtio, virtio_pci, virtio_blk, virtio_net, and virtio_ring. For 32-bit guests, the specific "virtio" module is not necessary.

If you want to boot from a virtio disk, the initial ramdisk must contain the necessary modules. By default, this is handled by mkinitcpio's autodetect hook. Otherwise use the MODULES array in /etc/mkinitcpio.conf to include the necessary modules and rebuild the initial ramdisk.

Virtio disks are recognized with the prefix v (e.g. vda, vdb, etc.); therefore, changes must be made in at least /etc/fstab and /boot/grub/grub.cfg when booting from a virtio disk.

Further information on paravirtualization with KVM can be found here.

You might also want to install qemu-guest-agent to implement support for QMP commands that will enhance the hypervisor management capabilities.

In order to allow the guest's memory foot print to shrink as seen from the host, it needs to report to the host which pages are not needed anymore by the guest. The kernel has an API for that called Free Page Reporting and since it is built-in, it is as easy as starting QEMU like this:

After this, you should see the guest memory increasing and then shrinking again after running workloads in it.

However, while this parameter will indeed take care of shrinking the guest's memory usage from the host's perspective when pages are freed, it will not be able to automatically make use of memory that the guest is using for cache. This is an important consideration as a guest is likely to eventually use its entire unused memory for caching, making free-page-reporting=on useless. Read the next section to mitigate this problem.

You might want to rely on the host's page cache instead of the guest's in order to allow for more efficient memory usage. Coupled with KSM, this allows you to make your virtual machines quite memory efficient, duplicating only few pages.

One way to achieve this is to use a file-mapped virtio pmem device. Add this config to your QEMU:

whereby virtio_pmem.img is a local file on the host that will serve as our memory backend in side the guest. The -m part is important here: Set the maxmem parameter so that it is regular memory + memory-backend-file size. In this case: 64G + 32G = 96G.

Start the guest with those options. Inside the guest, you will find a new device at /dev/pmem0 which we will need to format with a DAX-compatible filesystem such as ext4 (btrfs is not supported):

Any files you write into /mnt will then bypass the guest's page cache.

It's also possible to have the whole root filesystem DAX-enabled in this way.

Windows does not come with the virtio drivers. The latest and stable versions of the drivers are regularly built by Fedora, details on downloading the drivers are given on virtio-win on GitHub. In the following sections we will mostly use the stable ISO file provided here: virtio-win.iso. Alternatively, use virtio-winAUR.

The drivers need to be loaded during installation, the procedure is to load the ISO image with the virtio drivers in a cdrom device along with the primary disk device and the Windows ISO install media:

During the installation, at some stage, the Windows installer will ask "Where do you want to install Windows?", it will give a warning that no disks are found. Follow the example instructions below (based on Windows Server 2012 R2 with Update).

You should now see your virtio disk(s) listed here, ready to be selected, formatted and installed to.

Modifying an existing Windows guest for booting from virtio disk requires that the virtio driver is loaded by the guest at boot time. We will therefore need to teach Windows to load the virtio driver at boot time before being able to boot a disk image in virtio mode.

To achieve that, first create a new disk image that will be attached in virtio mode and trigger the search for the driver:

Run the original Windows guest with the boot disk still in IDE mode, the fake disk in virtio mode and the driver ISO image.

Windows will detect the fake disk and look for a suitable driver. If it fails, go to Device Manager, locate the SCSI drive with an exclamation mark icon (should be open), click Update driver and select the virtual CD-ROM. Do not navigate to the driver folder within the CD-ROM, simply select the CD-ROM drive and Windows will find the appropriate driver automatically (tested for Windows 7 SP1).

Request Windows to boot in safe mode next time it starts up. This can be done using the msconfig.exe tool in Windows. In safe mode all the drivers will be loaded at boot time including the new virtio driver. Once Windows knows that the virtio driver is required at boot it will memorize it for future boot.

Once instructed to boot in safe mode, you can turn off the virtual machine and launch it again, now with the boot disk attached in virtio mode:

You should boot in safe mode with virtio driver loaded, you can now return to msconfig.exe disable safe mode boot and restart Windows.

Using virtio network drivers is a bit easier, simply add the -nic argument.

Windows will detect the network adapter and try to find a driver for it. If it fails, go to the Device Manager, locate the network adapter with an exclamation mark icon (should be open), click Update driver and select the virtual CD-ROM. Do not forget to select the checkbox which says to search for directories recursively.

If you want to track your guest memory state (for example via virsh command dommemstat) or change guest's memory size in runtime (you still will not be able to change memory size, but can limit memory usage via inflating balloon driver) you will need to install guest balloon driver.

For this you will need to go to Device Manager, locate PCI standard RAM Controller in System devices (or unrecognized PCI controller from Other devices) and choose Update driver. In opened window you will need to choose Browse my computer... and select the CD-ROM (and do not forget the Include subdirectories checkbox). Reboot after installation. This will install the driver and you will be able to inflate the balloon (for example via hmp command balloon memory_size, which will cause balloon to take as much memory as possible in order to shrink the guest's available memory size to memory_size). However, you still will not be able to track guest memory state. In order to do this you will need to install Balloon service properly. For that open command line as administrator, go to the CD-ROM, Balloon directory and deeper, depending on your system and architecture. Once you are in amd64 (x86) directory, run blnsrv.exe -i which will do the installation. After that virsh command dommemstat should be outputting all supported values.

Before you progress in this section, make sure you followed the section about setting up host file sharing with virtiofsd first.

First, follow the upstream instructions. Once configured, Windows will have the Z: drive mapped automatically with shared directory content.

Your Windows 11 guest system is properly configured if it has:

If the above installed and Z: drive is still not listed, try repairing "Virtio-win-guest-tools" in Windows Add/Remove programs.

Install the emulators/virtio-kmod port if you are using FreeBSD 8.3 or later up until 10.0-CURRENT where they are included into the kernel. After installation, add the following to your /boot/loader.conf file:

Then modify your /etc/fstab by doing the following:

And verify that /etc/fstab is consistent. If anything goes wrong, just boot into a rescue CD and copy /etc/fstab.bak back to /etc/fstab.

While QEMU is running, a monitor console is provided in order to provide several ways to interact with the virtual machine running. The QEMU monitor offers interesting capabilities such as obtaining information about the current virtual machine, hotplugging devices, creating snapshots of the current state of the virtual machine, etc. To see the list of all commands, run help or ? in the QEMU monitor console or review the relevant section of the official QEMU documentation.

When using the std default graphics option, one can access the QEMU monitor by pressing Ctrl+Alt+2 or by clicking View > compatmonitor0 in the QEMU window. To return to the virtual machine graphical view either press Ctrl+Alt+1 or click View > VGA.

However, the standard method of accessing the monitor is not always convenient and does not work in all graphic outputs QEMU supports.

To enable telnet, run QEMU with the -monitor telnet:127.0.0.1:port,server,nowait parameter. When the virtual machine is started you will be able to access the monitor via telnet:

Run QEMU with the -monitor unix:socketfile,server,nowait parameter. Then you can connect with either socat, nmap or openbsd-netcat.

For example, if QEMU is run via:

It is possible to connect to the monitor with:

Alternatively with nmap:

You can expose the monitor over TCP with the argument -monitor tcp:127.0.0.1:port,server,nowait. Then connect with openbsd-netcat by running:

It is possible to access the monitor automatically from the same terminal QEMU is being run by running it with the argument -monitor stdio.

Some combinations of keys may be difficult to perform on virtual machines due to the host intercepting them instead in some configurations (a notable example is the Ctrl+Alt+F* key combinations, which change the active tty). To avoid this problem, the problematic combination of keys may be sent via the monitor console instead. Switch to the monitor and use the sendkey command to forward the necessary keypresses to the virtual machine. For example:

It is sometimes desirable to save the current state of a virtual machine and having the possibility of reverting the state of the virtual machine to that of a previously saved snapshot at any time. The QEMU monitor console provides the user with the necessary utilities to create snapshots, manage them, and revert the machine state to a saved snapshot.

It is possible to run a virtual machine in a frozen state so that all changes will be discarded when the virtual machine is powered off just by running QEMU with the -snapshot parameter. When the disk image is written by the guest, changes will be saved in a temporary file in /tmp and will be discarded when QEMU halts.

However, if a machine is running in frozen mode it is still possible to save the changes to the disk image if it is afterwards desired by using the monitor console and running the following command:

If snapshots are created when running in frozen mode they will be discarded as soon as QEMU is exited unless changes are explicitly commited to disk, as well.

Some operations of a physical machine can be emulated by QEMU using some monitor commands:

Screenshots of the virtual machine graphic display can be obtained in the PPM format by running the following command in the monitor console:

The QEMU machine protocol (QMP) is a JSON-based protocol which allows applications to control a QEMU instance. Similarly to the #QEMU monitor it offers ways to interact with a running machine and the JSON protocol allows to do it programmatically. The description of all the QMP commands can be found in qmp-commands.

The usual way to control the guest using the QMP protocol, is to open a TCP socket when launching the machine using the -qmp option. Here it is using for example the TCP port 4444:

Then one way to communicate with the QMP agent is to use netcat:

At this stage, the only command that can be recognized is qmp_capabilities, so that QMP enters into command mode. Type:

Now, QMP is ready to receive commands, to retrieve the list of recognized commands, use:

It is possible to merge a running snapshot into its parent by issuing a block-commit command. In its simplest form the following line will commit the child into its parent:

Upon reception of this command, the handler looks for the base image and converts it from read only to read write mode and then runs the commit job.

Once the block-commit operation has completed, the event BLOCK_JOB_READY will be emitted, signalling that the synchronization has finished. The job can then be gracefully completed by issuing the command block-job-complete:

Until such a command is issued, the commit operation remains active. After successful completion, the base image remains in read write mode and becomes the new active layer. On the other hand, the child image becomes invalid and it is the responsibility of the user to clean it up.

To create a new snapshot out of a running image, run the command:

This creates an overlay file named new_snapshot_name.qcow2 which then becomes the new active layer.

There are a number of techniques that you can use to improve the performance of the virtual machine. For example:

See https://www.linux-kvm.org/page/Tuning_KVM for more information.

Sometimes, you may wish to use one of your system partitions from within QEMU. Using a raw partition for a virtual machine will improve performance, as the read and write operations do not go through the file system layer on the physical host. Such a partition also provides a way to share data between the host and guest.

In Arch Linux, device files for raw partitions are, by default, owned by root and the disk group. If you would like to have a non-root user be able to read and write to a raw partition, you must either change the owner of the partition's device file to that user, add that user to the disk group, or use ACL for more fine-grained access control.

After doing so, you can attach the partition to a QEMU virtual machine as a virtual disk.

However, things are a little more complicated if you want to have the entire virtual machine contained in a partition. In that case, there would be no disk image file to actually boot the virtual machine since you cannot install a boot loader to a partition that is itself formatted as a file system and not as a partitioned device with an MBR. Such a virtual machine can be booted either by: #Specifying kernel and initramfs manually, #Simulating a virtual disk with MBR, #Using the device-mapper, #Using a linear RAID or #Using a Network Block Device.

QEMU supports loading Linux kernels and initial RAM file systems directly, thereby circumventing boot loaders such as GRUB. It then can be launched with the physical partition containing the root file system as the virtual disk, which will not appear to be partitioned. This is done by issuing a command similar to the following:

In the above example, the physical partition being used for the guest's root file system is /dev/sda3 on the host, but it shows up as /dev/sda on the guest.

You may, of course, specify any kernel and initramfs that you want, and not just the ones that come with Arch Linux.

When there are multiple kernel parameters to be passed to the -append option, they need to be quoted using single or double quotes. For example:

A more complicated way to have a virtual machine use a physical partition, while keeping that partition formatted as a file system and not just having the guest partition the partition as if it were a disk, is to simulate an MBR for it so that it can boot using a boot loader such as GRUB.

For the following, suppose you have a plain, unmounted /dev/hdaN partition with some file system on it you wish to make part of a QEMU disk image. The trick is to dynamically prepend a master boot record (MBR) to the real partition you wish to embed in a QEMU raw disk image. More generally, the partition can be any part of a larger simulated disk, in particular a block device that simulates the original physical disk but only exposes /dev/hdaN to the virtual machine.

A virtual disk of this type can be represented by a VMDK file that contains references to (a copy of) the MBR and the partition, but QEMU does not support this VMDK format. For instance, a virtual disk created by

will be rejected by QEMU with the error message

Note that VBoxManage creates two files, file.vmdk and file-pt.vmdk, the latter being a copy of the MBR, to which the text file file.vmdk points. Read operations outside the target partition or the MBR would give zeros, while written data would be discarded.

A method that is similar to the use of a VMDK descriptor file uses the device-mapper to prepend a loop device attached to the MBR file to the target partition. In case we do not need our virtual disk to have the same size as the original, we first create a file to hold the MBR:

Here, a 1 MiB (2048 * 512 bytes) file is created in accordance with partition alignment policies used by modern disk partitioning tools. For compatibility with older partitioning software, 63 sectors instead of 2048 might be required. The MBR only needs a single 512 bytes block, the additional free space can be used for a BIOS boot partition and, in the case of a hybrid partitioning scheme, for a GUID Partition Table. Then, we attach a loop device to the MBR file:

In this example, the resulting device is /dev/loop0. The device mapper is now used to join the MBR and the partition:

The resulting /dev/mapper/qemu is what we will use as a QEMU raw disk image. Additional steps are required to create a partition table (see the section that describes the use of a linear RAID for an example) and boot loader code on the virtual disk (which will be stored in /path/to/mbr).

The following setup is an example where the position of /dev/hdaN on the virtual disk is to be the same as on the physical disk and the rest of the disk is hidden, except for the MBR, which is provided as a copy:

The table provided as standard input to dmsetup has a similar format as the table in a VMDK descriptor file produced by VBoxManage and can alternatively be loaded from a file with dmsetup create qemu --table table_file. To the virtual machine, only /dev/hdaN is accessible, while the rest of the hard disk reads as zeros and discards written data, except for the first sector. We can print the table for /dev/mapper/qemu with dmsetup table qemu (use udevadm info -rq name /sys/dev/block/major:minor to translate major:minor to the corresponding /dev/blockdevice name). Use dmsetup remove qemu and losetup -d $loop to delete the created devices.

A situation where this example would be useful is an existing Windows XP installation in a multi-boot configuration and maybe a hybrid partitioning scheme (on the physical hardware, Windows XP could be the only operating system that uses the MBR partition table, while more modern operating systems installed on the same computer could use the GUID Partition Table). Windows XP supports hardware profiles, so that that the same installation can be used with different hardware configurations alternatingly (in this case bare metal vs. virtual) with Windows needing to install drivers for newly detected hardware only once for every profile. Note that in this example the boot loader code in the copied MBR needs to be updated to directly load Windows XP from /dev/hdaN instead of trying to start the multi-boot capable boot loader (like GRUB) present in the original system. Alternatively, a copy of the boot partition containing the boot loader installation can be included in the virtual disk the same way as the MBR.

You can also do this using software RAID in linear mode (you need the linear.ko kernel driver) and a loopback device:

First, you create some small file to hold the MBR:

Here, a 16 KiB (32 * 512 bytes) file is created. It is important not to make it too small (even if the MBR only needs a single 512 bytes block), since the smaller it will be, the smaller the chunk size of the software RAID device will have to be, which could have an impact on performance. Then, you setup a loopback device to the MBR file:

Let us assume the resulting device is /dev/loop0, because we would not already have been using other loopbacks. Next step is to create the "merged" MBR + /dev/hdaN disk image using software RAID:

The resulting /dev/md0 is what you will use as a QEMU raw disk image (do not forget to set the permissions so that the emulator can access it). The last (and somewhat tricky) step is to set the disk configuration (disk geometry and partitions table) so that the primary partition start point in the MBR matches the one of /dev/hdaN inside /dev/md0 (an offset of exactly 16 * 512 = 16384 bytes in this example). Do this using fdisk on the host machine, not in the emulator: the default raw disc detection routine from QEMU often results in non-kibibyte-roundable offsets (such as 31.5 KiB, as in the previous section) that cannot be managed by the software RAID code. Hence, from the host:

Press X to enter the expert menu. Set number of 's'ectors per track so that the size of one cylinder matches the size of your MBR file. For two heads and a sector size of 512, the number of sectors per track should be 16, so we get cylinders of size 2x16x512=16k.

Now, press R to return to the main menu.

Press P and check that the cylinder size is now 16k.

Now, create a single primary partition corresponding to /dev/hdaN. It should start at cylinder 2 and end at the end of the disk (note that the number of cylinders now differs from what it was when you entered fdisk.

Finally, 'w'rite the result to the file: you are done. You now have a partition you can mount directly from your host, as well as part of a QEMU disk image:

You can, of course, safely set any boot loader on this disk image using QEMU, provided the original /dev/hdaN partition contains the necessary tools.

With Network Block Device, Linux can use a remote server as one of its block device. You may use nbd-server (from the nbd package) to create an MBR wrapper for QEMU.

Assuming you have already set up your MBR wrapper file like above, rename it to wrapper.img.0. Then create a symbolic link named wrapper.img.1 in the same directory, pointing to your partition. Then put the following script in the same directory:

The .0 and .1 suffixes are essential; the rest can be changed. After running the above script (which you may need to do as root to make sure nbd-server is able to access the partition), you can launch QEMU with:

If a virtual machine is set up with libvirt, it can be configured with virsh autostart or through the virt-manager GUI to start at host boot by going to the Boot Options for the virtual machine and selecting "Start virtual machine on host boot up".

To run QEMU virtual machines on boot, you can use following systemd unit and config.

Then create per-VM configuration files, named /etc/conf.d/qemu.d/vm_name, with the variables args and haltcmd set. Example configs:

The description of the variables is the following:

To set which virtual machines will start on boot-up, enable the qemu@vm_name.service systemd unit.

To prevent the mouse from being grabbed when clicking on the guest operating system's window, add the options -usb -device usb-tablet. This means QEMU is able to report the mouse position without having to grab the mouse. This also overrides PS/2 mouse emulation when activated. For example:

If that does not work, try using -vga qxl parameter, also look at the instructions QEMU/Troubleshooting#Mouse cursor is jittery or erratic.

It is possible to access the physical device connected to a USB port of the host from the guest. The first step is to identify where the device is connected, this can be found running the lsusb command. For example:

The outputs in bold above will be useful to identify respectively the host_bus and host_addr or the vendor_id and product_id.

In qemu, the idea is to emulate an EHCI (USB 2) or XHCI (USB 1.1 USB 2 USB 3) controller with the option -device usb-ehci,id=ehci or -device qemu-xhci,id=xhci respectively and then attach the physical device to it with the option -device usb-host,... We will consider that controller_id is either ehci or xhci for the rest of this section.

Then, there are two ways to connect to the USB of the host with qemu:

See QEMU/USB emulation for more information.

When using #SPICE it is possible to redirect USB devices from the client to the virtual machine without needing to specify them in the QEMU command. It is possible to configure the number of USB slots available for redirected devices (the number of slots will determine the maximum number of devices which can be redirected simultaneously). The main advantages of using SPICE for redirection compared to the previously-mentioned -usbdevice method is the possibility of hot-swapping USB devices after the virtual machine has started, without needing to halt it in order to remove USB devices from the redirection or adding new ones. This method of USB redirection also allows us to redirect USB devices over the network, from the client to the server. In summary, it is the most flexible method of using USB devices in a QEMU virtual machine.

We need to add one EHCI/UHCI controller per available USB redirection slot desired as well as one SPICE redirection channel per slot. For example, adding the following arguments to the QEMU command you use for starting the virtual machine in SPICE mode will start the virtual machine with three available USB slots for redirection:

See SPICE/usbredir for more information.

Both spicy from spice-gtk (Input > Select USB Devices for redirection) and remote-viewer from virt-viewer (File > USB device selection) support this feature. Please make sure that you have installed the necessary SPICE Guest Tools on the virtual machine for this functionality to work as expected (see the #SPICE section for more information).

Normally, forwarded devices must be available at the boot time of the virtual machine to be forwarded. If that device is disconnected, it will not be forwarded anymore.

You can use udev rules to automatically attach a device when it comes online. Create a hostdev entry somewhere on disk. chown it to root to prevent other users modifying it.

Then create a udev rule which will attach/detach the device:

Source and further reading.

Kernel Samepage Merging (KSM) is a feature of the Linux kernel that allows for an application to register with the kernel to have its pages merged with other processes that also register to have their pages merged. The KSM mechanism allows for guest virtual machines to share pages with each other. In an environment where many of the guest operating systems are similar, this can result in significant memory savings.

To make it permanent, use systemd's temporary files:

If KSM is running, and there are pages to be merged (i.e. at least two similar virtual machines are running), then /sys/kernel/mm/ksm/pages_shared should be non-zero. See https://docs.kernel.org/admin-guide/mm/ksm.html for more information.

The Linux QXL driver supports four heads (virtual screens) by default. This can be changed via the qxl.heads=N kernel parameter.

The default VGA memory size for QXL devices is 16M (VRAM size is 64M). This is not sufficient if you would like to enable two 1920x1200 monitors since that requires 2 × 1920 × 4 (color depth) × 1200 = 17.6 MiB VGA memory. This can be changed by replacing -vga qxl by -vga none -device qxl-vga,vgamem_mb=32. If you ever increase vgamem_mb beyond 64M, then you also have to increase the vram_size_mb option.

A custom display resolution can be set with -device VGA,edid=on,xres=1280,yres=720 (see EDID and display resolution).

One way to share the clipboard between the host and the guest is to enable the SPICE remote desktop protocol and access the client with a SPICE client. One needs to follow the steps described in #SPICE. A guest run this way will support copy paste with the host.

QEMU provides its own implementation of the spice vdagent chardev called qemu-vdagent. It interfaces with the spice-vdagent guest service and allows the guest and host share a clipboard.

To access this shared clipboard with QEMU's GTK display, you will need to compile QEMU from source with the --enable-gtk-clipboard configure parameter. It is sufficient to replace the installed qemu-ui-gtk package.

Add the following QEMU command line arguments:

These arguments are also valid if converted to libvirt form.

On linux guests, you may start the spice-vdagent.service user unit manually. On Windows guests, set the spice-agent startup type to automatic.

QEMU can run any version of Windows from Windows 95 through Windows 11.

It is possible to run Windows PE in QEMU.

For Windows 8 (or later) guests it is better to disable "Turn on fast startup (recommended)" from the Power Options of the Control Panel as explained in the following forum page, as it causes the guest to hang during every other boot.

Fast Startup may also need to be disabled for changes to the -smp option to be properly applied.

If you use a MS Windows guest, you might want to use RDP to connect to your guest virtual machine. If you are using a VLAN or are not in the same network as the guest, use:

Then connect with either rdesktop or freerdp to the guest. For example:

By default, Windows assumes the firmware clock is set to local time, but this is usually not the case when using QEMU. To remedy this you can configure Windows to use UTC after the installation, or you can set the virtual clock to localtime by adding -rtc base=localtime to your command line.

Linux system installed on physical equipment can be cloned for running on a QEMU virtual machine. See Clone Linux system from hardware for QEMU virtual machine

Sometimes it is easier to work directly on a disk image instead of the real ARM based device. This can be achieved by mounting an SD card/storage containing the root partition and chrooting into it.

Another use case for an ARM chroot is building ARM packages on an x86_64 machine. Here, the chroot environment can be created from an image tarball from Arch Linux ARM - see [5] for a detailed description of this approach.

Either way, from the chroot it should be possible to run pacman and install more packages, compile large libraries etc. Since the executables are for the ARM architecture, the translation to x86 needs to be performed by QEMU.

Install qemu-user-static on the x86_64 machine/host, and qemu-user-static-binfmt to register the qemu binaries to binfmt service.

qemu-user-static is used to allow the execution of compiled programs from other architectures. This is similar to what is provided by qemu-emulators-full, but the "static" variant is required for chroot. Examples:

These two lines execute the ls command compiled for 32-bit ARM and 64-bit ARM respectively. Note that this will not work without chrooting, because it will look for libraries not present in the host system.

qemu-user-static-binfmt allows automatically prefixing the ARM executable with qemu-arm-static or qemu-aarch64-static.

Make sure that the ARM executable support is active:

Each executable must be listed.

If it is not active, restart systemd-binfmt.service.

Mount the SD card to /mnt/sdcard (the device name may be different).

Mount boot partition if needed (again, use the suitable device name):

Finally chroot into the SD card root as described in Change root#Using chroot:

Alternatively, you can use arch-chroot from arch-install-scripts, as it will provide an easier way to get network support:

You can also use systemd-nspawn to chroot into the ARM environment:

--bind-ro=/etc/resolv.conf is optional and gives a working network DNS inside the chroot

If you install sudo in the chroot and receive the following error when trying to use it:

then you may need to modify the binfmt flags, for example for aarch64:

and add a C at the end of this file:

Then restart systemd-binfmt.service and check that the changes have taken effect (note the C on the flags line):

See the "flags" section of the kernel binfmt documentation for more information.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Tablet mode has side effect of not grabbing mouse input in QEMU window:

It works with several -vga backends one of which is virtio.

See QEMU/Troubleshooting.

**Examples:**

Example 1 (unknown):
```unknown
qemu-system-target_architecture
```

Example 2 (unknown):
```unknown
qemu-system-x86_64
```

Example 3 (unknown):
```unknown
qemu-system-i386
```

Example 4 (unknown):
```unknown
qemu-system-arm
```

---

## Codecs and containers

**URL:** https://wiki.archlinux.org/title/Codecs

**Contents:**
- Requirements
- List of codecs
  - Audio
    - Lossless audio codecs
    - Lossy audio codecs
      - AAC
  - Image codecs
  - Video codecs
- Container format tools
- Backends

From Wikipedia, "a codec is a device or computer program capable of encoding and/or decoding a digital data stream or signal."

In general, codecs are utilized by multimedia applications to encode or decode audio or video streams. In order to play encoded streams, users must ensure an appropriate codec is installed.

This article deals only with codecs and application backends; see List of applications/Multimedia for a list of media players (MPlayer, mpv and VLC are popular choices).

Playing multimedia content requires two components:

It is not always necessary to explicitly install codecs if you have installed a media player. For example, MPlayer pulls in a large number of codecs as dependencies, and also has codecs built in.

See also Wikipedia:Comparison of audio coding formats.

See also Wikipedia:Comparison of video codecs.

See also Wikipedia:Comparison of video container formats.

From https://gstreamer.freedesktop.org/:

Simply, GStreamer is a backend or framework utilized by many media applications. See GStreamer article.

From https://sourceforge.net/projects/xine/:

As an alternative to GStreamer, many media players can be configured to utilize the xine backend provided by xine-lib.

Note that the xine project itself provides a capable video player, xine-ui.

libavcodec is part of the FFmpeg project. It includes a large number of video and audio codecs. The libavcodec codecs are included with media players such as MPlayer and VLC, so you may not need to install the ffmpeg package itself.

If you see the "The H264 plugin is missing" warning with Totem media player, install gst-libav.

If you see the "Parole needs H.264 decoder to play this file" warning with Parole media player, install gst-libav.

If you see the warning VLC could not decode the format "h264" (H264 - MPEG-4 AVC (part 10)) install vlc-plugin-ffmpeg.

**Examples:**

Example 1 (unknown):
```unknown
VLC could not decode the format "h264" (H264 - MPEG-4 AVC (part 10))
```

---

## KVM

**URL:** https://wiki.archlinux.org/title/KVM

**Contents:**
- Checking support for KVM
  - Hardware support
  - Kernel support
- Para-virtualization with Virtio
  - Kernel support
  - List of para-virtualized devices
- How to use KVM
- Tips and tricks
  - Nested virtualization
  - Enabling huge pages

KVM, Kernel-based Virtual Machine, is a hypervisor built into the Linux kernel. It is similar to Xen in purpose but much simpler to get running. Unlike native QEMU, which uses emulation, KVM is a special operating mode of QEMU that uses CPU extensions (HVM) for virtualization via a kernel module.

Using KVM, one can run multiple virtual machines running unmodified GNU/Linux, Windows, or any other operating system. (See Guest Support Status for more information.) Each virtual machine has private virtualized hardware: a network card, disk, graphics card, etc.

Differences between KVM and Xen, VMware, or QEMU can be found at the KVM FAQ.

This article does not cover features common to multiple emulators using KVM as a backend. You should see related articles for such information.

KVM requires that the virtual machine host's processor has virtualization support (named VT-x for Intel processors and AMD-V for AMD processors). You can check whether your processor supports hardware virtualization with the following command:

If nothing is displayed after running either command, then your processor does not support hardware virtualization, and you will not be able to use KVM.

Arch Linux kernels provide the required kernel modules to support KVM.

The module is available only if it is set to either y or m.

If the command returns nothing, the module needs to be loaded manually; see Kernel modules#Manual module handling.

Para-virtualization provides a fast and efficient means of communication for guests to use devices on the host machine. KVM provides para-virtualized devices to virtual machines using the Virtio API as a layer between the hypervisor and guest.

All Virtio devices have two parts: the host device and the guest driver.

Use the following command inside the virtual machine to check if the VIRTIO modules are available in the kernel:

Then, check if the kernel modules are automatically loaded with the command:

In case the above commands return nothing, you need to load the kernel modules manually.

See the main article: QEMU.

Nested virtualization enables existing virtual machines to be run on third-party hypervisors and on other clouds without any modifications to the original virtual machines or their networking.

On host, enable nested feature for kvm_intel:

To make it permanent (see Kernel modules#Setting module options):

Verify that feature is activated:

Enable the "host passthrough" mode to forward all CPU features to the guest system:

Boot the virtual machine and check if the vmx flag is present:

This article or section is a candidate for merging with QEMU.

You may also want to enable hugepages to improve the performance of your virtual machine. With an up to date Arch Linux and a running KVM, you probably already have everything you need. Check if you have the directory /dev/hugepages. If not, create it. Now we need the right permissions to use this directory. The default permission is root's uid and gid with 0755, but we want anyone in the kvm group to have access to hugepages.

Add to your /etc/fstab:

Instead of specifying the group name directly, with gid=kvm, you can of course specify the gid as a number, but it must match the kvm group. The mode of 1770 allows anyone in the group to create files but not unlink or rename each other's files. Make sure /dev/hugepages is mounted properly:

Now you can calculate how many hugepages you need. Check how large your hugepages are:

Normally that should be 2048 kB ≙ 2 MB. Let us say you want to run your virtual machine with 1024 MB. 1024 / 2 = 512. Add a few extra so we can round this up to 550. Now tell your machine how many hugepages you want:

If you had enough free memory, you should see:

If the number is smaller, close some applications or start your virtual machine with less memory (number_of_pages x 2):

Note the -mem-path parameter. This will make use of the hugepages.

Now you can check, while your virtual machine is running, how many pages are used:

Now that everything seems to work, you can enable hugepages by default if you like. Add to your /etc/sysctl.d/40-hugepage.conf:

This article or section is a candidate for merging with QEMU#Enabling Secure Boot.

KVM Secure boot has a few requirements before it can be enabled:

To enable UEFI with secure boot support, install edk2-ovmf and set your virtual machine to use the secure boot enabled UEFI. If you are using libvirt, you can do this by adding the following to the XML configuration of your virtual machine.

Next you need to enroll some keys. In this example we will enroll Microsoft and Redhat's secure boot keys. Install virt-firmware and run the following. Replace vm_name with the name of your virtual machine.

Then edit the libvirt XML configuration of your virtual machine to point to the new VARS file.

After this secure boot should automatically be enabled. You can double check by entering the virtual machine's BIOS by pressing F2 when you see the UEFI boot logo.

**Examples:**

Example 1 (unknown):
```unknown
$ LC_ALL=C.UTF-8 lscpu | grep Virtualization
```

Example 2 (unknown):
```unknown
$ grep -E --color=auto 'vmx|svm|0xc0f' /proc/cpuinfo
```

Example 3 (unknown):
```unknown
$ zgrep CONFIG_KVM= /proc/config.gz
```

Example 4 (unknown):
```unknown
$ lsmod | grep kvm
```

---

## PhpVirtualBox

**URL:** https://wiki.archlinux.org/title/PhpVirtualBox

**Contents:**
- Installation
  - VirtualBox web service
  - VirtualBox web interface (phpvirtualbox)
- Configuration
  - Web service
  - Web interface
- Running
- Debugging
- See also

phpVirtualBox is an open source, AJAX implementation of the VirtualBox user interface written in PHP. As a modern web interface, it allows you to access and control remote VirtualBox instances. Much of its verbage and some of its code is based on the (inactive) vboxweb project. phpVirtualBox was designed to allow users to administer VirtualBox in a headless environment - mirroring the VirtualBox GUI through its web interface.

To remotely control virtual machine you need two components: VirtualBox web service, running in the same OS with virtual machine, and web interface, written in PHP and therefore dependent on PHP-capable web server. Communication between them, based on SOAP protocol is currently unencrypted, so it is recommended to install both on the same machine if you do not want your username and password to be send via network as clear text.

To use the web console, you must install the virtualbox-ext-oracleAUR package.

Install the phpvirtualbox package. You will also need a PHP-capable web server of your choice (Apache HTTP Server is suitable choice).

From here on out, it is assumed that you have a web server (with root at /srv/http) and php functioning properly.

In the virtual machine settings, enable the remote desktop access and specify a port different with other virtual machines.

Every time you need to make machine remotely available execute something like this:

As user whose account you want the service to be running from (--host option is not necessary if you enabled association with localhost in the /etc/host.conf).

virtualbox provides the vboxweb.service for systemd.

To start vboxweb from non-root user you must:

Edit /etc/php/php.ini, uncomment the following line:

Edit the example configuration file /usr/share/webapps/phpvirtualbox/config.php-example appropriately (it is well-commented and does not need explanations). Copy that file into /etc/webapps/phpvirtualbox/config.php and symlink to /usr/share/webapps/phpvirtualbox/config.php.

Then, edit /etc/php/php.ini, find open_basedir and append the configuration path /etc/webapps/ at the end. It will look like the follows:

If you are running Apache as webserver, you can copy /etc/webapps/phpvirtualbox/apache.example.conf into /etc/httpd/conf/extra/phpvirtualbox.conf. If you are running Apache 2.4, due to the syntax of ACL changes, edit that file to replace the follows

Next, add following line into /etc/httpd/conf/httpd.conf:

Edit /etc/webapps/phpvirtualbox/.htaccess and remove the following line.

Do not forget to restart the webserver (e.g. for Apache, restart httpd.service).

If everything works fine, visit http://YourVboxWebInterfaceHost/phpvirtualbox and it should show a login box. The initial username and password are both "admin", after login change them from the web interface (File -> change password). If you set $noAuth=true in the web interface config.php, you should immediately see the phpvirtualbox web interface.

If you encounter a login problem, and you have upgraded virtualbox from 3.2.x to 4.0.x, you should run the following command to update you websrvauthlibrary in you virtualbox configuration file which has been changed from VRDPAuth.so to VBOXAuth.so.

If you encounter a login problem with an error message that contains

Then you may want to edit /etc/webapps/phpvirtualbox/config.php variable location to use localhost rather than 127.0.0.1. See this forum post for further information.

If you are still unable to login into the interface, you can try to disable webauth by

on virtualization server and set username and password to empty strings and set $noAuth=true in /etc/webapps/phpvirtualbox/config.php on web server. By doing this, you should immediatelly access the web interface without login process. And then, maybe you can try some apache access control.

**Examples:**

Example 1 (unknown):
```unknown
vboxwebsrv -b --logfile path/to/log/file --pidfile /run/vbox/vboxwebsrv.pid --host 127.0.0.1
```

Example 2 (unknown):
```unknown
/etc/host.conf
```

Example 3 (unknown):
```unknown
vboxweb.service
```

Example 4 (unknown):
```unknown
vboxweb_mod.service
```

---

## VirtualBox

**URL:** https://wiki.archlinux.org/title/VirtualBox

**Contents:**
- Installation steps for Arch Linux hosts
  - Install the core packages
  - Sign modules
  - Load the VirtualBox kernel modules
  - Accessing host USB devices in guest
  - Guest additions
  - Extension pack
  - Front-ends
- Installation steps for Arch Linux guests
- Virtual disks management

VirtualBox is a hypervisor used to run operating systems in a special environment, called a virtual machine, on top of the existing operating system. VirtualBox is in constant development and new features are implemented continuously. It comes with a Qt graphical user interface, as well as headless and SDL command-line tools for managing and running virtual machines.

In order to integrate functions of the host system to the guests, including shared folders and clipboard, video acceleration and a seamless window integration mode, guest additions are provided for some guest operating systems.

For more information, see the official documentation.

In order to launch VirtualBox virtual machines on your Arch Linux box, follow these installation steps.

Install the virtualbox package. You will also need to choose a package to provide host modules:

To compile the VirtualBox modules provided by virtualbox-host-dkms, it will also be necessary to install the appropriate headers package(s) for your installed kernel(s) (e.g. linux-rt-headers for linux-rt). [1] When either VirtualBox or the kernel is updated, the kernel modules will be automatically recompiled thanks to the DKMS pacman hook.

When using a custom kernel with CONFIG_MODULE_SIG_FORCE option enabled, you must sign your modules with a key generated during kernel compilation.

You can sign the modules by executing the following command as root:

If you experience an error such as the following:

Then run the command cd /lib/modules/$(uname -r)/build to navigate to your kernel tree folder and check if the certs folder actually has a signing_key.pem file. If not, create a file somewhere on your system (doesn't have to be in the kernel tree folder) named x509.genkey with the following contents (based on [2]):

Then run openssl req -new -nodes -utf8 -sha512 -days 36500 -batch -x509 -config x509.genkey -outform DER -out signing_key.x509 -keyout signing_key.pem in the directory you created the x509.genkey file and move the resulting files to the certs directory in the kernel tree folder. You should then be able to rerun the signing command without an error.

virtualbox-host-modules-arch and virtualbox-host-dkms use systemd-modules-load.service to load VirtualBox modules automatically at boot time. For the modules to be loaded after installation, either reboot or load the modules once manually; the list of modules can be found in /usr/lib/modules-load.d/virtualbox-host-modules-arch.conf, /usr/lib/modules-load.d/virtualbox-host-modules-lts.conf or /usr/lib/modules-load.d/virtualbox-host-dkms.conf.

Among the kernel modules VirtualBox uses, there is a mandatory module named vboxdrv, which must be loaded before any virtual machines can run.

To load the module manually, run:

The following modules are only required in advanced configurations:

To use the USB ports of your host machine in your virtual machines, add users that will be authorized to use this feature to the vboxusers user group.

It is also recommended to install the virtualbox-guest-iso package on the host running VirtualBox. This package will act as a disc image that can be used to install the guest additions onto guest systems other than Arch Linux. The .iso file will be located at /usr/lib/virtualbox/additions/VBoxGuestAdditions.iso, and may have to be mounted manually inside the virtual machine. Once mounted, you can run the guest additions installer inside the guest. For Arch Linux guest also see VirtualBox/Install Arch Linux as a guest#Install the Guest Additions.

The Oracle VM VirtualBox Extension Pack provides additional features and is released under a non-free license only available for personal use. To install it, the virtualbox-ext-oracleAUR package is available, and a prebuilt version can be found in the seblu repository.

If you prefer to use the traditional and manual way: download the extension pack manually and install it via the GUI (File > Tools > Extension Pack Manager) or via VBoxManage extpack install <.vbox-extpack>, make sure you have a toolkit like Polkit to grant privileged access to VirtualBox. The installation of extension pack requires root access.

You can also install the extension pack without using Polkit via the following command:

One of the non-free extension pack features is support for the Remote Desktop Protocol (RDP). This part of functionality can also be obtained with the open source VNC Extension Pack, by installing the virtualbox-ext-vnc package.

VirtualBox comes with four front-ends:

Refer to the VirtualBox manual to learn how to create virtual machines.

A security feature in Wayland (i.e. when using GDM) disallows VirtualBox to grab all keyboard input. This is annoying when you want to pass window manager shortcuts to your guest operating system. It can be bypassed by whitelisting VirtualBox:

The first command will show if any other applications are already whitelisted. If so, add VirtualBox Machine to that list, rather than having it as the only one.

See VirtualBox/Install Arch Linux as a guest.

See also #Import/export VirtualBox virtual machines from/to other hypervisors.

VirtualBox supports the following virtual disk formats:

VBoxManage clonehd can be used to convert between VDI, VMDK, VHD and RAW.

For example to convert VDI to VMDK:

VirtualBox does not support QEMU's QCOW2 disk image format. To use a QCOW2 disk image with VirtualBox you therefore need to convert it, which you can do with qemu-img. qemu-img can convert QCOW to / from VDI, VMDK, VHDX, RAW and various other formats (which you can see by running qemu-img --help).

For example to convert QCOW2 to VDI:

There are two revisions of QCOW2: 0.10 and 1.1. You can specify the revision to use with -o compat=revision.

Mounting VDI images only works with fixed size images (a.k.a. static images); dynamic (dynamically size allocating) images are not easily mountable.

The offset of the partition (within the VDI) is needed, then add the value of offData to 32256 (e.g. 69632 + 32256 = 101888):

The storage can now be mounted with:

For VDI disks with more partitions you can also use losetup:

After this you should find the partitions under /dev/loop* (e.g. /dev/loop0p1). Then you can mount them as usual (e.g. mount mount /dev/loop0p1 /mnt/).

You can also use mount.vdi script that, which you can use as (install script itself to /usr/bin/):

Alternately you can use the nbd kernel module and qemu-nbd from qemu-img[3]:

If the partition nodes are not propagated try using partprobe /dev/nbd0; otherwise, a VDI partition can be mapped directly to a node by: qemu-nbd -P 1 -c /dev/nbd0 storage.vdi.

Like VDI, VHD images can be mounted with QEMU's nbd module:

Compacting virtual disks only works with .vdi files and basically consists of the following steps.

Boot your virtual machine and remove all bloat manually or by using cleaning tools like bleachbit which is available for Windows systems too.

Wiping free space with zeroes can be achieved with several tools:

Once the free disk space have been wiped, shut down your virtual machine.

The next time you boot your virtual machine, it is recommended to do a filesystem check.

Now, remove the zeros from the .vdi file with VBoxManage modifyhd:

VirtualBox offers simulation of TRIM in VDI files via an experimental "discard" attachment option. This option is undocumented and can be accessed by commandline or .vbox file editing. When enabled, TRIM commands from the guest operating system causes the corresponding part of the VDI file to be compacted away.

If you are running out of space due to the small hard drive size you selected when you created your virtual machine, the solution adviced by the VirtualBox manual is to use VBoxManage modifyhd. However this command only works for VDI and VHD disks and only for the dynamically allocated variants. If you want to resize a fixed size virtual disk disk too, read on this trick which works either for a Windows or UNIX-like virtual machine.

First, create a new virtual disk next to the one you want to increase:

where size is in MiB, in this example 10000MiB ~= 10GiB, and new.vdi is name of new hard drive to be created.

Next, the old virtual disk needs to be cloned to the new one which this may take some time:

Detach the old hard drive and attach new one, replace all mandatory italic arguments by your own:

To get the storage controller name and the port number, you can use the command VBoxManage showvminfo virtual_machine_name. Among the output you will get such a result (what you are looking for is in italic):

Download GParted live image and mount it as a virtual CD/DVD disk file, boot your virtual machine, increase/move your partitions, umount GParted live and reboot.

Finally, unregister the virtual disk from VirtualBox and remove the file:

If your disk is a VDI one, run:

Then jump back to the Gparted step, to increase the size of the partition on the virtual disk.

If you think that editing a simple XML file is more convenient than playing with the GUI or with VBoxManage and you want to replace (or add) a virtual disk to your virtual machine, in the .vbox configuration file corresponding to your virtual machine, simply replace the GUID, the file location and the format to your needs:

then in the <AttachedDevice> sub-tag of <StorageController>, replace the GUID by the new one.

The information about path to harddisks and the snapshots is stored between <HardDisks> .... </HardDisks> tags in the file with the .vbox extension. You can edit them manually or use this script where you will need change only the path or use defaults, assumed that .vbox is in the same directory with a virtual harddisk and the snapshots folder. It will print out new configuration to stdout.

UUIDs are widely used by VirtualBox. Each virtual machines and each virtual disk of a virtual machine must have a different UUID. When you launch a virtual machine in VirtualBox, VirtualBox will keep track of all UUIDs of your virtual machine instance. See the VBoxManage list to list the items registered with VirtualBox.

If you cloned a virtual disk manually by copying the virtual disk file, you will need to assign a new UUID to the cloned virtual drive if you want to use the disk in the same virtual machine or even in another (if that one has already been opened, and thus registered, with VirtualBox).

You can use this command to assign a new UUID to a virtual disk:

If you plan to use your virtual machine on another hypervisor or want to import in VirtualBox a virtual machine created with another hypervisor, you might be interested in reading the following steps.

Guest additions are available in most hypervisor solutions: VirtualBox comes with the Guest Additions, VMware with the VMware Tools, Parallels with the Parallels Tools, etc. These additional components are designed to be installed inside a virtual machine after the guest operating system has been installed. They consist of device drivers and system applications that optimize the guest operating system for better performance and usability by providing these features.

If you have installed the additions to your virtual machine, please uninstall them first. Your guest, especially if it is using an operating system from the Windows family, might behave weirdly, crash or even might not boot at all if you are still using the specific drivers in another hypervisor.

This step will depend on the ability to convert the virtual disk image directly or not.

Some companies provide tools which offer the ability to create virtual machines from a Windows or GNU/Linux operating system located either in a virtual machine or even in a native installation. With such a product, you do not need to apply this and the following steps and can stop reading here.

First, familiarize yourself with the formats supported by VirtualBox and those supported by third-party hypervisors.

Each hypervisor have their own virtual machine configuration file: .vbox for VirtualBox, .vmx for VMware, a config.pvs file located in the virtual machine bundle (.pvm file), etc. You will have thus to recreate a new virtual machine in your new destination hypervisor and specify its hardware configuration as close as possible as your initial virtual machine.

Pay a close attention to the firmware interface (BIOS or UEFI) used to install the guest operating system. While an option is available to choose between these 2 interfaces on VirtualBox and on Parallels solutions, on VMware, you will have to add manually the following line to your .vmx file.

Finally, ask your hypervisor to use the existing virtual disk you have converted and launch the virtual machine.

Find hereafter the implementation details of a systemd service that will be used to consider a virtual machine as a service.

Enable the vboxvmservice@your_virtual_machine_name systemd unit in order to launch the virtual machine at next boot. To launch it directly, simply start the systemd unit.

VirtualBox 4.2 introduces a new way for UNIX-like systems to have virtual machines started automatically, other than using a systemd service.

It can be useful to start virtual machines directly with a keyboard shortcut instead of using the VirtualBox interface (GUI or CLI). For that, you can simply define key bindings in .xbindkeysrc. Please refer to Xbindkeys for more details.

Example, using the Fn key of a laptop with an unused battery key (F3 on the computer used in this example):

If the device that you are looking for does not show up on any of the menus in the section above and you have tried all three USB controller options, boot up your virtual machine three separate times. Once using the USB 1.1 controller, another using the USB 2.0 controller, etc. Leave the virtual machine running for at least 5 minutes after startup. Sometimes Windows will autodetect the device for you. Be sure you filter any devices that are not a keyboard or a mouse so they do not start up at boot. This ensures that Windows will detect the device at start-up.

To access Apache server on a Virtual Machine from the host machine only, simply execute the following lines on the host:

where 8888 is the port the host should listen on and 80 is the port the virtual machine will send Apache's signal on.

To use a port lower than 1024 on the host machine, changes need to be made to the firewall on that host machine. This can also be set up to work with SSH or any other services by changing "Apache" to the corresponding service and ports.

To communicate between the VirtualBox guest and host using ssh, the server port must be forwarded under Settings > Network. When connecting from the client/host, connect to the IP address of the client/host machine, as opposed to the connection of the other machine. This is because the connection will be made over a virtual adapter.

Recent versions of VirtualBox have support for accelerating OpenGL inside guests. This can be enabled with a simple checkbox in the machine's settings, right below where video ram is set, and installing the VirtualBox guest additions. However, most Windows games use Direct3D (part of DirectX), not OpenGL, and are thus not helped by this method. However, it is possible to gain accelerated Direct3D in your Windows guests by borrowing the d3d libraries from Wine, which translate d3d calls into OpenGL, which is then accelerated. These libraries are now part of VirtualBox guest additions.

After enabling OpenGL acceleration as described above, reboot the guest into safe mode (press F8 before the Windows screen appears but after the VirtualBox screen disappears), and install VirtualBox guest additions, during install enable checkbox Direct3D support. Reboot back to normal mode and you should have accelerated Direct3D.

When using VirtualBox on a USB key, for example to start an installed machine with an ISO image, you will manually have to create VMKDs from the existing drives. However, once the new VMDKs are saved and you move on to another machine, you may experience problems launching an appropriate machine again. To get rid of this issue, you can use the following script to launch VirtualBox. This script will clean up and unregister old VMDK files and it will create new, proper VMDKs for you:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Note that your user has to be added to the "disk" group to create VMDKs out of existing drives.

If you have a dual boot system between Arch Linux and another operating system, it can become tedious to switch back and forth if you need to work in both. You may also experience performance or compatibility issues when using a virtual machine, which can impact your ability to do certain tasks.

This guide will let you reuse, in a virtual machine, your native Arch Linux installation when you are running your second operating system. This way, you keep the ability to run each operating system natively, but have the option to run your Arch Linux installation inside a virtual machine.

Depending on your hard drive setup, device files representing your hard drives may appear differently when you will run your Arch Linux installation natively or in virtual machine. This problem occurs when using FakeRAID for example. The fake RAID device will be mapped in /dev/mapper/ when you run your GNU/Linux distribution natively, while the devices are still accessible separately. However, in your virtual machine, it can appear without any mapping in /dev/sdaX for example, because the drivers controlling the fake RAID in your host operating system (e.g. Windows) are abstracting the fake RAID device.

To circumvent this problem, we will need to use an addressing scheme that is persistent to both systems. This can be achieved using UUIDs. Make sure your boot loader and fstab file is using UUIDs, otherwise fix this issue. Read fstab and Persistent block device naming.

Make sure your mkinitcpio configuration uses the HOOK block:

If it is not present, add it and regenerate the initramfs.

Now, we need to create a new virtual machine which will use a RAW disk as virtual drive, for that we will use a ~ 1Kio VMDK file which will be mapped to a physical disk. Unfortunately, VirtualBox does not have this option in the GUI, so we will have to use the console and use an internal command of VBoxManage.

Boot the host which will use the Arch Linux virtual machine. The command will need to be adapted according to the host you have.

There are 3 ways to achieve this: login as root, changing the access right of the device with chmod, adding your user to the disk group. The latter way is the more elegant, let us proceed that way:

Apply the new group settings with:

Now, you can use the command:

Adapt the above command to your need, especially the path and filename of the VMDK location and the raw disk location to map which contain your Arch Linux installation.

Open a command prompt must be run as administrator.

On Windows, as the disk filename convention is different from UNIX, use this command to determine what drives you have in your Windows system and their location:

In this example, as the Windows convention is \\.\PhysicalDriveX where X is a number from 0, \\.\PHYSICALDRIVE1 could be analogous to /dev/sdb from the Linux disk terminology.

To use the VBoxManage command on Windows, you can either, change the current directory to your VirtualBox installation folder first with cd C:\Program Files\Oracle\VirtualBox\

or use the absolute path name:

There are other limitations regarding the aforementioned command when used in other operating systems like OS X, please thus read carefully the manual page, if you are concerned.

After, we need to create a new machine (replace the virtual_machine_name to your convenience) and register it with VirtualBox.

Then, the newly raw disk needs to be attached to the machine. This will depend if your computer or actually the root of your native Arch Linux installation is on an IDE or a SATA controller.

If you need an IDE controller:

While you continue using the CLI, it is recommended to use the VirtualBox GUI, to personalise the virtual machine configuration. Indeed, you must specify its hardware configuration as close as possible as your native machine: turning on the 3D acceleration, increasing video memory, setting the network interface, etc.

Finally, you may want to seamlessly integrate your Arch Linux with your host operating system and allow copy pasting between both operating systems. Please refer to VirtualBox/Install Arch Linux as a guest#Install the Guest Additions for that, since this Arch Linux virtual machine is basically an Arch Linux guest.

In some cases it may be useful to install a native Arch Linux system while running another operating system: one way to accomplish this is to perform the installation through VirtualBox on a raw disk. If the existing operating system is Linux based, you may want to consider following Install from existing Linux instead.

This scenario is very similar to #Run a native Arch Linux installation inside VirtualBox, but will follow those steps in a different order: start by #Create a raw disk VMDK image, then #Create the virtual machine configuration file.

Now, you should have a working virtual machine configuration whose virtual VMDK disk is tied to a real disk. The installation process is exactly the same as the steps described in VirtualBox/Install Arch Linux as a guest, but #Make sure you have a persistent naming scheme and #Make sure your mkinitcpio image is correct.

After completing the installation, boot your computer natively with an GNU/Linux installation media (whether it be Arch Linux or not), chroot into your installed Arch Linux installation and install and configure a boot loader.

Before starting the virtual machine, run the following commands on the host machine [4]:

If you use an AMD processor and the first boot gets stuck, you also have to run

If you are attempting to install Mojave, after doing the aforementioned steps, the installer will load up but you might not be able to send keyboard or mouse input. The reason seems to be that Mojave no longer supports the USB 1.1 controllers and in order to fix the issue you need to emulating USB 3.0. To do that first install the extension pack.

Then go to Machine > Settings > USB and select USB 3.0. Input should work from this point onwards.

If the installer is unable to properly format the bootable drive during installation and you end up in an UEFI shell, enter the following:

You will now be brought to couple of obscure PCI paths. The first one is the one that you just attempted to boot from and it did not work. The second (or third) one should be the one with the MacOS recovery partition that you need to load to continue the installation. Click the second Entry. If it is empty, press Esc to go back and select the third entry. Once you get one with folders click though the folders. It should be something like macOS Install Data > Locked Files > Boot Files > boot.efi. Once you click enter on the boot.efi you should boot into the MacOS installer and resume installation. Note that some of the subdirectories might be missing. Remember that you need to get to a boot.efi.[5]

If you want to migrate an existing native Windows installation to a virtual machine which will be used with VirtualBox on GNU/Linux, this use case is for you. This section only covers native Windows installation using the MSDOS/Intel partition scheme. Your Windows installation must reside on the first MBR partition for this operation to success. Operation for other partitions are available but have been untested (see #Known limitations for details).

A couple of tasks are required to be done inside your native Windows installation first, then on your GNU/Linux host.

The first three following points comes from this outdated VirtualBox wiki page, but are updated here.

Boot into Windows, clean up the installation (with CCleaner for example), use disk2vhd tool to create a VHD image. Include a reserved system partition (if present) and the actual Windows partition (usually disk C:). The size of Disk2vhd-created image will be the sum of the actual files on the partition (used space), not the size of a whole partition. If all goes well, the image should just boot in a virtual machine and you will not have to go through the hassle with MBR and Windows boot loader, as in the case of cloning an entire partition.

If your Windows virtual machine refuses to boot, you may need to apply the following modifications to your virtual machine.

In some cases, it is useful to be able to dual boot with Windows and access the partition in a virtual machine. This process is significantly different from #Move a native Windows installation to a virtual machine in several ways:

A VirtualBox virtual machine must be manually created. As of now do not add any storage device any disk to the virtual machine, it will be done manually later.

Configure the virtual machine with the following settings (settings panel can be opened by clicking the "Settings" button in the main toolbar):

Optionally you can enable also the following settings:

To access the Windows partitions, create a raw VMDK file pointing to the relevant Windows partitions (root privileges are required to read disk partition table):

Replace capitalized placeholder strings as follow:

The command will also create an extra file inside the virtual machine folder, "windows-pt.vmdk", that will be just ignored.

Partition numbers can be found also by running this command and looking at the MIN column:

Now change the virtual disk owner to give access the user and group running VirtualBox.

Replace VIRTUALBOX_RUNNING_USER and VIRTUALBOX_RUNNING_GROUP with the user and the group that will run VirtualBox, which most likely will be your user.

VirtualBox must have raw disk access in order to run a Windows partition. Normally, this would require VirtualBox to be run with full root privileges, but more elegant options are available.

Here udev is configured to restrict the access to partitions Windows partitions to the vboxusers group, and then the user running VirtualBox is added to the group.

Assigning the disks to the vboxusers group can be done automatically by creating the following file:

WINDOWS_DISK_ID_PART_TABLE_UUID must be replaced with the value obtained from udevadm info /dev/WINDOWS_DISK (replace WINDOWS_DISK with the disk containing Windows partitions). The UUIDs in these rules correspond to particular GPT partition types while the other capitalized strings are supposed to be written that way, so those does not have to be replaced.

Then the user running VirtualBox must be added to the vboxusers group. This can be done with the following command:

Replace VIRTUALBOX_RUNNING_USER and with the user that will run VirtualBox, which most likely will be your user.

To be able to add the VMDK file in VirtualBox Virtual Media Manager without running VirtualBox as root, the user running VirtualBox need to be in vboxusers and disk groups.

Replace VIRTUALBOX_RUNNING_USER and with the user that will run VirtualBox, which most likely will be your user.

Virtual machine EFI boot files will refer to different disks than the ones in the physical EFI system partition, so VirtualBox must not make use of the latter but instead of an EFI system partition inside a dedicated virtual disk. This disk can be created with the following command:

Replace VM_DIRECTORY with the folder containing the virtual machine being built.

Configure the virtual machine storage devices (Settings panel - Storage) as following:

Now start the virtual machine and it should automatically boot from Windows installation disk. After choosing the installation locales click on the "Repair your computer" link, then choose "Troubleshoot" and then " Command Prompt" in order to launch a command prompt from the install media.

Enter the following commands to create a new GPT table in the esp.vmdk disk and install the Windows boot loader onto it using configuration from the existing Windows partition:

List all disks identified by the system:

The esp.vmkd disk should be labeled as disk 0 due to the fact that was attached to the SATA port 0, ~512 MiB in size and unpartitioned. The windows.vmdk disk should be labeled as disk 1; note that the column "Size" displays the disk size, not the partition one.

Select the esp.vmdk disk:

Now create a GPT partition table, an EFI system partition, big as the whole disk, and assign to it a label and drive letter:

Check that the partition has been correctly created:

Our newly created EFI system partition will be labeled as "SYSTEM" with letter as "S".

Take note of the Windows installation volume letter because it will be used in next steps. Usually its D but it could be different: you can infer it from its label and its size. The size is the same as the Windows installation partition size on your physical hard disk.

Install the Windows boot loader into the EFI system partition.

Now close the command prompt, power off the virtual machine and detach the Windows installation disk (from "Preferences > Devices" remove the optical disk). The virtual machine should now boot from the newly installed boot partition and load the physical Windows installation. It may show some UEFI related errors on the top of the virtual machine window and the first boot may take a while, but if everything has been done correctly you will be able to access your windows installation.

This works the same way as #Run a native Windows installation inside VirtualBox but the vmdk will contain the entire disk rather than one partition, and so you will not need to create a separate ESP or MBR partition as the one in the physical disk will be used.

Then follow the same method as in #Run a native Windows installation inside VirtualBox for the configuration and virtual disk attachement.

Typically after installing Guest Additions, a fullscreen Arch guest running X will be set to the optimal resolution for your display; however, the virtual console's framebuffer will be set to a standard, often smaller, resolution detected from VirtualBox's custom VESA driver.

To use the virtual consoles at optimal resolution, Arch needs to recognize that resolution as valid, which in turn requires VirtualBox to pass this information along to the guest OS.

First, check if your desired resolution is not already recognized by running the command (hwinfo need to be installed):

If the optimal resolution does not show up, then you will need to run the VBoxManage tool on the host machine and add "extra resolutions" to your virtual machine (on a Windows host, go to the VirtualBox installation directory to find VBoxManage.exe). For example:

The parameters "Arch Linux" and "1360x768x24" in the example above should be replaced with your virtual machine name and the desired framebuffer resolution. Incidentally, this command allows for defining up to 16 extra resolutions ("CustomVideoMode1" through "CustomVideoMode16"). Recommended resolutions are 1280x720, 1920x1080, 2048x1080, 2560x1440, 3840x2160, 1280x800, 1280x1024, 1440x900, 1600x900.

Afterwards, restart the virtual machine and run hwinfo --framebuffer once more to verify that the new resolutions have been recognized by your guest system (which does not guarantee they will all work, depending on your hardware limitations).

Finally, add a video=resolution kernel parameter to set the framebuffer to the new resolution, for example:

Additionally you may want to configure your boot loader to use the same resolution. If you use GRUB, see GRUB/Tips and tricks#Setting the framebuffer resolution.

The network tab of the virtual machine settings contains, in "Advanced", a tool to create port forwarding. It is possible to use it to forward the Guest ssh port 22 to a Host port, e.g. 3022 :

will establish a connection from Host to Guest.

Using this port forwarding and SSHFS it is straightforward to mount the Guest filesystem onto the Host one:

and then transfer files between both.

This means your virtual machine has captured the input of your keyboard and your mouse. Simply press the right Ctrl key and your input should control your host again.

To control transparently your virtual machine with your mouse going back and forth your host, without having to press any key, and thus have a seamless integration, install the guest additions inside the guest. Read from VirtualBox/Install Arch Linux as a guest#Install the Guest Additions if your guest is Arch Linux, otherwise read the official VirtualBox help.

When launching a virtual machine client, and no 64-bit options are available, make sure your CPU virtualization capabilities (usually named VT-x) are enabled in the BIOS.

If you are using a Windows host, you may need to disable Hyper-V, as it prevents VirtualBox from using VT-x. [6]

See Uniform look for Qt and GTK applications for information about theming Qt-based applications like VirtualBox.

Your guest operating system is a GNU/Linux distribution and you want to open a new TTY shell by hitting Ctrl+Alt+F2 or exit your current X session with Ctrl+Alt+Backspace. If you type these keyboard shortcuts without any adaptation, the guest will not receive any input and the host (if it is a GNU/Linux distribution too) will intercept these shortcut keys. To send Ctrl+Alt+F2 to the guest for example, simply hit your Host Key (usually the right Ctrl key) and press F2 simultaneously.

Your user must be in the vboxusers group and you need to install the extension pack if you want USB 2 support. Then you will be able to enable USB 2 in the virtual machine settings and add one or several filters for the devices you want to access from the guest operating system.

If VBoxManage list usbhost does not show any USB devices even if run as root, make sure that there is no old udev rules (from VirtualBox 4.x) in /etc/udev/rules.d/. VirtualBox 5.0 installs udev rules to /usr/lib/udev/rules.d/. You can use command like pacman -Qo /usr/lib/udev/rules.d/60-vboxdrv.rules to determine if the udev rule file is outdated.

Sometimes, on old Linux hosts, the USB subsystem is not auto-detected resulting in an error Could not load the Host USB Proxy service: VERR_NOT_FOUND or in a not visible USB drive on the host, even when the user is in the vboxusers group. This problem is due to the fact that VirtualBox switched from usbfs to sysfs in version 3.0.8. If the host does not understand this change, you can revert to the old behaviour by defining the following environment variable in any file that is sourced by your shell (e.g. your ~/.bashrc if you are using bash):

Then make sure, the environment has been made aware of this change (reconnect, source the file manually, launch a new shell instance or reboot).

Also make sure that your user is a member of the storage group.

If you have a USB modem which is being used by the guest operating system, killing the guest operating system can cause the modem to become unusable by the host system. Killing and restarting VBoxSVC should fix this problem.

If attaching a USB device to the guest causes a crash or any other erroneous behavior, try switching the USB controller from USB 2 (EHCI) to USB 3 (xHCI) or vice versa.

Generally, such issues are observed after upgrading VirtualBox or Linux kernel. Downgrading them to the previous versions of theirs might solve the problem.

If the audio input from an analog microphone is working correctly on the host, but no sound seems to get through to the guest, despite the microphone device apparently being detected normally, installing a sound server such as PulseAudio on the host might fix the problem.

If after installing PulseAudio the microphone still refuses to work, setting Host Audio Driver (under VirtualBox > Machine > Settings > Audio) to ALSA Audio Driver might help.

Some image formats cannot be reliably converted to ISO. For instance, ccd2iso ignores .ccd and .sub files, which can result in disk images with broken files.

In this case, you will either have to use CDemu for Linux inside VirtualBox or any other utility used to mount disk images.

Make sure all required kernel modules are loaded. See #Load the VirtualBox kernel modules.

If all required kernel modules are loaded and you are still unable to create the host-only adapter, navigate to File > Host Network Manager and click the Create button to add the network interface.

When you get the following error when trying to load modules:

Sign your modules or disable CONFIG_MODULE_SIG_FORCE in your kernel config.

This can occur if a virtual machine is exited ungracefully. Run the following command:

This error might appear if extension pack has not been updated and becomes incompatible with a newly released VirtualBox version.

This error also happens sometimes when selecting QCOW/QCOW2/QED disk format when creating a new virtual disk.

If you encounter this message the first time you start the virtual machine:

Exit VirtualBox, delete all files of the new machine and from VirtualBox configuration file remove the last line in MachineRegistry menu (or the offending machine you are creating):

While OpenBSD is reported to work fine on other hypervisors without virtualisation instructions (VT-x AMD-V) enabled, an OpenBSD virtual machine running on VirtualBox without these instructions will be unusable, manifesting with a bunch of segmentation faults. Starting VirtualBox with the -norawr0 argument may solve the problem. You can do it like this:

This error message may appear when running an .exe file which requires administrator privileges from a shared folder in windows guests. [7]

As a workaround, copy the file to the virtual drive or use UNC paths (\\vboxsvr). See [8] for more information.

If you get this error code while booting, even if you choose operating system type Win 8, try to enable the CMPXCHG16B CPU instruction:

Update the virtual machine's settings by going to Settings > Storage > Controller:SATA and check Use Host I/O Cache.

If you are running at 16-bit color depth, then the icons may appear fuzzy/choppy. However, upon attempting to change the color depth to a higher level, the system may restrict you to a lower resolution or simply not enable you to change the depth at all. To fix this, run regedit in Windows and add the following key to the Windows XP virtual machine's registry:

Then update the color depth in the "desktop properties" window. If nothing happens, force the screen to redraw through some method (i.e. Host+f to redraw/enter full screen).

VirtualBox > 4.3.14 has a regression in which Windows guests with 3D acceleration flicker. Since r120678 a patch has been implemented to recognize an environment variable setting, launch VirtualBox like this:

Make sure no VirtualBox services are still running. See VirtualBox bug 13653.

This problem is caused by Qt detecting Wayland (e.g., if XDG_SESSION_TYPE=wayland), while VirtualBox does not work on Wayland yet. See FS#58761 and the upstream bug.

The Qt platform detection can be disabled and X11 forced over Wayland by setting the environment variable QT_QPA_PLATFORM=xcb. To not affect the other Qt applications (which usually work well with Wayland), QT_QPA_PLATFORM=xcb should only be set when launching VirtualBox.

If starting through the desktop entry, follow the instructions in Desktop entries#Modify environment variables and change the lines starting with Exec=VirtualBox ... to Exec=env QT_QPA_PLATFORM=xcb VirtualBox .... If starting from the shell, alias (Bash#Aliases) virtualbox to env QT_QPA_PLATFORM=xcb virtualbox.

With Intel CPU and graphics, allocating more processors for the guest can lower render performance, thus cause random freezing. Allocating less processors can help.

Disable the Mini Toolbar by selecting Machine > Settings, select the User Interface tab and uncheck the Mini Toolbar checkbox

Disable split lock detection by adding split_lock_detect=off to the kernel parameters.

Details are described in VirtualBox's Ticket #20180.

In VirtualBox 7.0.0, enabling Secure Boot in a virtual machine that was created in a previous VirtualBox version will fail with a nondescript error (FS#76234):

The solution is to click the Reset Keys to Default button right below the Enable Secure Boot checkbox.

KVM and VirtualBox kernel modules can be loaded but not used simultaneously. Android Studio emulator is a QEMU emulator, which uses KVM for acceleration. So Android Studio emulator and VirtualBox machine (if hardware acceleration is enabled) cannot run at the same time. We have to use one after the other stopped completely.

Sometimes, VirtualBox kernel module can still be used unexpectedly by some process, and keep all VirtualBox machines failing to start, the error message on VirtualBox GUI is "A critical error has occurred".

At this time, we can check and reload VirtualBox kernel modules using vboxreload as root. If it saying some modules is still be in use, you need to manually kill related process and rerun the command.

On some configurations of Kvantum (kvantum) with third party themes, some UI elements such as toolbars and menus are rendered black or improperly. This seems to be limited to translucent windows being enabled. See Kvantum's issue #418.

To fix this behavior, do one of:

By default, VirtualBox should auto-select the best audio driver. However, on PipeWire systems this often falls back to ALSA (see Pipewire issue).

It could cause journal records like these:

The solution is to configure VirtualBox to use the PulseAudio backend (which PipeWire will handle via pipewire-pulse):

**Examples:**

Example 1 (unknown):
```unknown
CONFIG_MODULE_SIG_FORCE
```

Example 2 (unknown):
```unknown
# find "/lib/modules/$(uname -r)/" '(' -name 'vboxdrv.ko*' -o -name 'vboxnetadp.ko*' -o -name 'vboxnetflt.ko*' ')' -exec /lib/modules/$(uname -r)/build/scripts/sign-file sha256 /lib/modules/$(uname -r)/build/certs/signing_key.pem /lib/modules/$(uname -r)/build/certs/signing_key.x509 {} ';'
```

Example 3 (unknown):
```unknown
At main.c:171:
- SSL error:FFFFFFFF80000002:system library::No such file or directory: crypto/bio/bss_file.c:67
- SSL error:10000080:BIO routines::no such file: crypto/bio/bss_file.c:75
sign-file: certs/signing_key.pem
```

Example 4 (unknown):
```unknown
cd /lib/modules/$(uname -r)/build
```

---
