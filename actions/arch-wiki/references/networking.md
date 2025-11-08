# Arch-Wiki - Networking

**Pages:** 33

---

## OpenSSH

**URL:** https://wiki.archlinux.org/title/X11_forwarding

**Contents:**
- Installation
- Client usage
  - Configuration
- Server usage
  - Configuration
  - Daemon management
    - Socket activation
  - Protection
    - Force public key authentication
    - Two-factor authentication and public keys

OpenSSH (OpenBSD Secure Shell) is a set of computer programs providing encrypted communication sessions over a computer network using the Secure Shell (SSH) protocol. It was created as an open source alternative to the proprietary Secure Shell software suite offered by SSH Communications Security. OpenSSH is developed as part of the OpenBSD project, which is led by Theo de Raadt.

OpenSSH is occasionally confused with the similarly-named OpenSSL; however, the projects have different purposes and are developed by different teams, the similar name is drawn only from similar goals.

Install the openssh package.

To connect to a server, run:

If the server only allows public-key authentication, follow SSH keys.

This article or section needs expansion.

The client can be configured to store common options and hosts. All options can be declared globally or restricted to specific hosts. For example:

With such a configuration, the following commands are equivalent

See ssh_config(5) for more information.

Some options do not have command line switch equivalents, but you can specify configuration options on the command line with -o. For example -oKexAlgorithms=+diffie-hellman-group1-sha1.

This article or section needs expansion.

sshd is the OpenSSH server daemon, configured with /etc/ssh/sshd_config and managed by sshd.service. Whenever changing the configuration, use sshd in test mode before restarting the service to ensure it will be able to start cleanly. Valid configurations produce no output.

To allow access only for some users, add this line:

To allow access only for some groups:

To add a nice welcome message (e.g. from the /etc/issue file), configure the Banner option:

Public and private host keys are automatically generated in /etc/ssh by the sshdgenkeys service and regenerated if missing even if HostKeyAlgorithms option in sshd_config allows only some. Three key pairs are provided based on the algorithms ed25519, ecdsa and rsa. To have sshd use a particular key, specify the following option:

If the server is to be exposed to the WAN, it is recommended to change the default port from 22 to a random higher one like this:

Start/enable sshd.service. It will keep the SSH daemon permanently active and fork for each incoming connection.

openssh 8.0p1-3 removed sshd.socket that used systemd's socket activation due to it being susceptible to denial of service. See FS#62248 for details. If sshd.socket is enabled when updating to openssh 8.0p1-3, the sshd.socket and sshd@.service units will be copied to /etc/systemd/system/ and reenabled. This is only done to not break existing setups; users are still advised to migrate to sshd.service.

Using sshd.socket negates the ListenAddress setting, so it will allow connections over any address. To achieve the effect of setting ListenAddress, you must specify the port and IP for ListenStream (e.g. ListenStream=192.168.1.100:22) by editing sshd.socket. You must also add FreeBind=true under [Socket] or else setting the IP address will have the same drawback as setting ListenAddress: the socket will fail to start if the network is not up in time.

When using socket activation, a transient instance of sshd@.service will be started for each connection (with different instance names). Therefore, neither sshd.socket nor the daemon's regular sshd.service allow to monitor connection attempts in the log. The logs of socket-activated instances of SSH can be seen by running journalctl -u "sshd@*" as root or by running journalctl /usr/bin/sshd as root.

Allowing remote log-on through SSH is good for administrative purposes, but can pose a threat to your server's security. Often the target of brute force attacks, SSH access needs to be limited properly to prevent third parties gaining access to your server.

ssh-audit offers an automated analysis of server and client configuration. Several other good guides and tools are available on the topic, for example:

If a client cannot authenticate through a public key, by default, the SSH server falls back to password authentication, thus allowing a malicious user to attempt to gain access by brute-forcing the password. One of the most effective ways to protect against this attack is to disable password logins entirely, and force the use of SSH keys. This can be accomplished by setting the following options in the daemon configuration file:

SSH can be set up to require multiple ways of authentication; you can tell which authentication methods are required using the AuthenticationMethods option. This enables you to use public keys as well as a two-factor authorization.

See Google Authenticator to set up Google Authenticator.

For Duo, install duo_unixAUR which will supply the pam_duo.so module. Read the Duo Unix documentation for instructions on how to setup the necessary Duo credentials (Integration Key, Secret Key, API Hostname).

The factual accuracy of this article or section is disputed.

To use PAM with OpenSSH, edit the following files:

Then you can log in with either a publickey or the user authentication as required by your PAM setup.

If, on the other hand, you want to authenticate the user on both a publickey and the user authentication as required by your PAM setup, use a comma instead of a space to separate the AuthenticationMethods:

With required pubkey and pam authentication, you may wish to disable the password requirement:

Brute forcing is a simple concept: one continuously tries to log in to a webpage or server log-in prompt like SSH with a high number of random username and password combinations.

See ufw#Rate limiting with ufw or Simple stateful firewall#Bruteforce attacks for iptables.

Since 9.8 a basic protection similar to fail2ban is implemented: the option PerSourcePenalties is set with reasonable default values. Penalties for various conditions are enforced against a client on its source address, resulting in a refused connection for a time period.

Alternatively, you can protect yourself from brute force attacks by using an automated script that blocks anybody trying to brute force their way in.

This article or section is out of date.

It is generally considered bad practice to allow the root user to log in without restraint over SSH. There are two methods by which SSH root access can be restricted for increased security.

Sudo selectively provides root rights for actions requiring these without requiring authenticating against the root account. This allows locking the root account against access via SSH and potentially functions as a security measure against brute force attacks, since now an attacker must guess the account name in addition to the password.

SSH can be configured to deny remote logins with the root user by editing the "Authentication" section in the daemon configuration file. Simply set PermitRootLogin to no:

Next, restart the SSH daemon.

You will now be unable to log in through SSH under root, but will still be able to log in with your normal user and use su or sudo to do system administration.

Some automated tasks such as remote, full-system backup require full root access. To allow these in a secure way, instead of disabling root login via SSH, it is possible to only allow root logins for selected commands. This can be achieved by editing ~root/.ssh/authorized_keys, by prefixing the desired key, e.g. as follows:

This will allow any login with this specific key only to execute the command specified between the quotes.

The increased attack surface created by exposing the root user name at login can be compensated by adding the following to sshd_config:

This setting will not only restrict the commands which root may execute via SSH, but it will also disable the use of passwords, forcing use of public key authentication for the root account.

A slightly less restrictive alternative will allow any command for root, but makes brute force attacks infeasible by enforcing public key authentication. For this option, set:

If, for whatever reason, you think that the user in question should not be able to add or change existing keys, you can prevent them from manipulating the file.

On the server, make the authorized_keys file read-only for the user and deny all other permissions:

To prevent the user from simply changing the permissions back, set the immutable bit on the authorized_keys file. To prevent the user from renaming the ~/.ssh directory and creating a new ~/.ssh directory and authorized_keys file, set the immutable bit on the ~/.ssh directory too. To add or remove keys, you will have to remove the immutable bit from authorized_keys and make it writable temporarily.

While common SSH keys and manual fingerprint verification may be easy to use with a handful of hosts that are managed by a single administrator, this method of authentication does not scale at all. When a number of servers need to be accessed through SSH by several users, manually verifying ssh public key fingerprints of every host becomes nearly impossible to do securely and reliably.

The solution for this is to use SSH certificates that provide automatic verification of public key identities through a chain of trust that scales significantly better than the default trust-on-first-use approach of SSH. SSH certificates are basically nothing else than normal public SSH keys, but with an additional signature from a trusted certificate authority that verifies the key identity.

The private certificate authority key should be stored securely, ideally on a smartcard or hardware token that prevents key extraction like the Nitrokey or YubiKey.

Copy the public server key to your local system containing the private certificate authority key to sign it:

The generated certificate ssh_host_ed25519_key-cert.pub should be copied to the server at /etc/ssh/.

Depending on the number of users and method of deployment, SSH User keys can also be used with Certificates. For organizations with many ssh users, this is strongly advised to manage User key deployment securely.

The deployment of user certificates works basically the same as for server identities. More details and instructions can be found at Wikibooks:OpenSSH/Cookbook/Certificate-based Authentication.

Automated deployment of SSH certificates can be provided by a number of open source tools. Popular examples are:

The Secure Shell fingerprint record (SSHFP) is an optional resource record in the domain name system that associates SSH keys to a host name. It can be used to verify the SSH fingerprint on public servers by using DNSSEC instead of deploying trusted CA certificates, which allows even unmanaged clients to verify the validity of key fingerprints.

To generate the required hexadecimal key fingerprint to be stored in the DNS record, create the hash on the target server.

This will read all available SSH keys for the specified domain and output valid SSHFP records that can then be stored in the DNS entries of the affected domain.

In order to automatically retrieve and trust SSH key fingerprints stored as SSHFP records, add the following to your ssh client configuration file:

If the target host has a valid SSHFP record and this record is verified with a valid DNSSEC signature, the fingerprint is automatically accepted without prompting the user to verify the hosts identity. In case the DNS record is not verified by DNSSEC, the user will be prompted to verify the fingerprint instead.

To determine the SSH fingerprint of a specific domain, use ssh-keyscan to retrieve the ssh fingerprints in a valid DNS record format. (Note that by default fingerprints for every available key type is provided as both SHA1 and SHA256.)

Since the SSHFP record stores the key fingerprints as hexadecimal values while the common output for SSH fingerprints is the base64 encoded SHA256 hash of the public key, it is necessary to convert the record back to the base64 format in order to compare it with values in the known_hosts file or other documentation that commonly stores fingerprints as SHA256.

Example for github.com using the hex value for the sha256 fingerprint of the key type ed25519

Compare with known_hosts entries:

This can be useful for laptop users connect to unsafe wireless connections. The only requirement is an SSH server running at a somewhat secure location, like your home or at work. It might be useful to use a dynamic DNS service like DynDNS so you do not have to remember your IP address.

The N flag disables the interactive prompt, and the D flag specifies the local port on which to listen on (you can choose any port number). The T flag disables pseudo-tty allocation.

Perhaps add the verbose (-v) flag, to verify the connection.

The above step is useful only in combination with a web browser or another program. Since SSH supports both SOCKS v4 and SOCKS v5, you can use either.

This is more complicated initially, but results in you not having to manually configure every application to use the SOCKS proxy. It requires setting up a local TUN interface and routing traffic through it.

See VPN over SSH#Set up badvpn and tunnel interface.

X11 forwarding is a mechanism that allows graphical interfaces of X11 programs running on a remote system to be displayed on a local client machine. For X11 forwarding the remote host does not need to have a full X11 system installed; however, it needs at least to have xauth installed. xauth is a utility that maintains Xauthority configurations used by server and client for authentication of X11 session (source).

Log on to the remote machine normally, specifying the -X switch if ForwardX11 was not enabled in the client's configuration file:

If you receive errors trying to run graphical applications, try ForwardX11Trusted instead:

Given the output X11 forwarding request failed, redo the setup for your remote machine. Once the X11 forwarding request succeeds, you can start any X program on the remote server, and it will be forwarded to your local session:

Error output containing Can't open display indicates that DISPLAY is improperly set.

Be careful with some applications as they check for a running instance on the local machine. Firefox is an example: either close the running Firefox instance or use the following start parameter to start a remote instance on the local machine:

If you get "X11 forwarding request failed on channel 0" when you connect (and the server /var/log/errors.log shows "Failed to allocate internet-domain X11 display socket"), make sure package xorg-xauth is installed. If its installation is not working, try to either:

Setting it to inet may fix problems with Ubuntu clients on IPv4.

For running X applications as another user on the SSH server, you need to xauth add the authentication line taken from xauth list of the SSH logged in user.

In addition to SSH's built-in support for X11, it can also be used to securely tunnel any TCP connection, by use of local forwarding or remote forwarding.

Local forwarding opens a port on the local machine, connections to which will be forwarded to the remote host and from there on to a given destination. Very often, the forwarding destination will be the same as the remote host, thus providing a secure shell and, e.g. a secure VNC connection, to the same machine. Local forwarding is accomplished by means of the -L switch and it is accompanying forwarding specification in the form of <tunnel port>:<destination address>:<destination port>.

will use SSH to login to and open a shell on 192.168.0.100, and will also create a tunnel from the local machine's TCP port 1000 to mail.google.com on port 25. Once established, connections to localhost:1000 will connect to the Gmail SMTP port. To Google, it will appear that any such connection (though not necessarily the data conveyed over the connection) originated from 192.168.0.100, and such data will be secure between the local machine and 192.168.0.100, but not between 192.168.0.100 and Google, unless other measures are taken.

will allow connections to localhost:2000 which will be transparently sent to the remote host on port 6001. The preceding example is useful for VNC connections using the vncserver utility--part of the tightvnc package--which, though very useful, is explicit about its lack of security.

Remote forwarding allows the remote host to connect to an arbitrary host via the SSH tunnel and the local machine, providing a functional reversal of local forwarding, and is useful for situations where, e.g., the remote host has limited connectivity due to firewalling. It is enabled with the -R switch and a forwarding specification in the form of <tunnel port>:<destination address>:<destination port>.

will bring up a shell on 192.168.0.200, and connections from 192.168.0.200 to itself on port 3000 (the remote host's localhost:3000) will be sent over the tunnel to the local machine and then on to irc.libera.chat on port 6667, thus, in this example, allowing the use of IRC programs on the remote host to be used, even if port 6667 would normally be blocked to it.

Both local and remote forwarding can be used to provide a secure "gateway", allowing other computers to take advantage of an SSH tunnel, without actually running SSH or the SSH daemon by providing a bind-address for the start of the tunnel as part of the forwarding specification, e.g. <tunnel address>:<tunnel port>:<destination address>:<destination port>. The <tunnel address> can be any address on the machine at the start of the tunnel. The address localhost allows connections via the localhost or loopback interface, and an empty address or * allow connections via any interface. By default, forwarding is limited to connections from the machine at the "beginning" of the tunnel, i.e. the <tunnel address> is set to localhost. Local forwarding requires no additional configuration; however, remote forwarding is limited by the remote server's SSH daemon configuration. See the GatewayPorts option in sshd_config(5) and -L address option in ssh(1) for more information about remote forwarding and local forwarding, respectively.

In certain scenarios, there might not be a direct connection to your target SSH daemon, and the use of a jump server (or bastion server) is required. Thus, we attempt to connect together two or more SSH tunnels, and assuming your local keys are authorized against each server in the chain. This is possible using SSH agent forwarding (-A) and pseudo-terminal allocation (-t) which forwards your local key with the following syntax:

This can be automated with the ProxyCommand option:

An easier and more secure way to do this is using the ProxyJump option with the -J flag:

Multiple hosts in the -J directive can be separated with a comma; they will be connected to in the order listed. The user...@ part is not required, but can be used. The host specifications for -J use the ssh configuration file, so specific per-host options can be set there, if needed.

The main difference between the ProxyCommand and ProxyJump options is that the later does not require a shell on the jumphost. Consequently, this also means that the jumpserver does not require access to the users login credentials or SSH agent forwarding. With the ProxyJump option, the ssh client connects through the jumpserver directly to the target server, establishing an end-to-end encrypted channel between client and target server.

An equivalent of the -J flag in the configuration file is the ProxyJump option; see ssh_config(5) for details.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The idea is that the client connects to the server via another relay while the server is connected to the same relay using a reverse SSH tunnel. This is useful when the server is behind a NAT, and the relay is a publicly accessible SSH server used as a proxy to which the user has access. Therefore, the prerequisite is that the client's keys are authorized against both the relay and the server, and the server needs to be authorized against the relay as well for the reverse SSH connection.

The following configuration example assumes that user1 is the user account used on client, user2 on relay and user3 on server. First, assuming we will use port 2222, the server needs to establish the reverse tunnel with:

Which can also be automated with a startup script, systemd service, autossh or sidedoorAUR.

At the client side, the connection is established with:

The remote command to establish the connection to reverse tunnel can also be defined in relay's authorized_keys file by including the command field as follows:

In this case the connection is established with:

Alternatively, you can add an entry to your ssh configuration that specifies both RemoteCommand and RequestTTY:

Which will reduce connecting to:

The SSH daemon usually listens on port 22. However, it is common practice for many public internet hotspots to block all traffic that is not on the regular HTTP/S ports (80 and 443, respectively), thus effectively blocking SSH connections. The immediate solution for this is to have sshd listen additionally on one of the whitelisted ports:

However, it is likely that port 443 is already in use by a web server serving HTTPS content, in which case it is possible to use a multiplexer, such as sslh, which listens on the multiplexed port and can intelligently forward packets to many services.

There are several client configuration options which can speed up connections either globally or for specific hosts. See ssh_config(5) for full descriptions of these options.

Please refer to the SSHFS article to mount a SSH-accessible remote system to a local directory, so you will be able to do any operation on the mounted files with any tool (copy, rename, edit with vim, etc.). sshfs is generally preferred over shfs, the latter has not been updated since 2004.

By default, the SSH session automatically logs out if it has been idle for a certain time. To keep the session up, the client can send a keep-alive signal to the server if no data has been received for some time, or symmetrically the server can send messages at regular intervals if it has not heard from the client.

systemd can automatically start SSH connections on boot/login and restart them when they fail. This makes it a useful tool for maintaining SSH tunnels.

The following service can start an SSH tunnel on login using the connection settings in your ssh configuration. If the connection closes for any reason, it waits 10 seconds before restarting it:

Then enable and start the user unit. See #Keep alive for how to prevent the tunnel from timing out. If you wish to start the tunnel on boot, you might want to rewrite the unit as a system service.

When a session or tunnel cannot be kept alive, for example due to bad network conditions causing client disconnections, you can use autossh to automatically restart them.

Connecting through a SOCKS-proxy set by Proxy settings:

With the -f option autossh can be made to run as a background process. Running it this way however means the passphrase cannot be entered interactively.

The session will end once you type exit in the session, or the autossh process receives a SIGTERM, SIGINT of SIGKILL signal.

If you want to automatically start autossh, you can create a systemd unit file:

Here AUTOSSH_GATETIME=0 is an environment variable specifying how long ssh must be up before autossh considers it a successful connection, setting it to 0 autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot. Other environment variables are available at autossh(1). Of course, you can make this unit more complex if necessary (see the systemd documentation for details), and obviously you can use your own options for autossh, but note that the -f implying AUTOSSH_GATETIME=0 does not work with systemd.

Remember to start and/or enable the service afterwards.

You may also need to disable ControlMaster:

For remote or headless servers which rely exclusively on SSH, a failure to start the SSH daemon (e.g., after a system upgrade) may prevent administration access. systemd offers a simple solution via OnFailure option.

Let us suppose the server runs sshd and telnet is the fail-safe alternative of choice. Create a file as follows. Do not enable telnet.socket!

That's it. Telnet is not available when sshd is running. Should sshd fail to start, a telnet session can be opened for recovery.

To better distinguish when you are on different hosts, you can set a different background color based on the kind of host.

This solution works, but is not universal (ZSH only).

You can use host configuration specific to the network you are connected to using a Match exec.

For example, when using nmcli(1), and the connection is configured (manually or through DHCP) to use a search-domain:

Another example for Match host ... exec "...": Consider that connecting to internal.example.com requires a bastion/proxy (via ProxyJump) unless you are already connected via VPN. The fragment !exec "host internal.example.com" applies only when internal.example.com cannot be looked up via DNS. Various alternatives are discussed at [3].

Because different servers on different networks are likely to share a common private IP address, you might want to handle them differently.

The factual accuracy of this article or section is disputed.

The best solution is to use the #Network specific configuration to use a different UserKnownHostsFile depending on the network you are on. The second solution, best used as default when you are working on new/prototype networks, would be to simply ignore hostkeys for private networks:

The factual accuracy of this article or section is disputed.

If you are using an interactive session, there are multiple ways to execute a command on login:

SSH agent forwarding allows you to use your local keys when connected to a server. It is recommended to only enable agent forwarding for selected hosts.

Next, configure an SSH agent and add your local key with ssh-add.

If you now connect to a remote server you will be able to connect to other services using your local keys.

New server private keys can be generated by:

You may want to run sshd as non-privileged user in containers, or for testing, etc.

Since non-privileged user cannot read host keys in /etc/ssh, new host keys must be generated:

Create an sshd_config file. The example below uses a port higher than 1024, provides a new path to the host keys and disables PAM:

Run sshd with the created config. The -D flag disables daemon mode and -e redirects output to stderr to allow easy monitoring.

Check these simple issues before you look any further.

If you are behind a NAT mode/router (which is likely unless you are on a VPS or publicly addressed host), make sure that your router is forwarding incoming ssh connections to your machine. Find the server's internal IP address with ip addr and set up your router to forward TCP on your SSH port to that IP. portforward.com can help with that.

The ss utility shows all the processes listening to a TCP port with the following command line:

If the above command do not show the system is listening to the port ssh, then SSH is not running: check the journal for errors etc.

Iptables may be blocking connections on port 22. Check this with:

and look for rules that might be dropping packets on the INPUT chain. Then, if necessary, unblock the port with a command like:

For more help configuring firewalls, see firewalls.

Start a traffic dump on the computer you are having problems with:

This should show some basic information, then wait for any matching traffic to happen before displaying it. Try your connection now. If you do not see any output when you attempt to connect, then something outside of your computer is blocking the traffic (e. g., hardware firewall, NAT router etc.).

In some cases, your ISP might block the default port (SSH port 22) so whatever you try (opening ports, hardening the stack, defending against flood attacks, et al) ends up useless. To confirm this, create a server on all interfaces (0.0.0.0) and connect remotely.

If you get an error message comparable to this:

That means the port is not being blocked by the ISP, but the server does not run SSH on that port (See security through obscurity).

However, if you get an error message comparable to this:

That means that something is rejecting your TCP traffic on port 22. Basically that port is stealth, either by your firewall or 3rd party intervention (like an ISP blocking and/or rejecting incoming traffic on port 22). If you know you are not running any firewall on your computer, and you know that Gremlins are not growing in your routers and switches, then your ISP is blocking the traffic.

To double check, you can run Wireshark on your server and listen to traffic on port 22. Since Wireshark is a Layer 2 Packet Sniffing utility, and TCP/UDP are Layer 3 and above (see IP Network stack), if you do not receive anything while connecting remotely, a third party is most likely to be blocking the traffic on that port to your server.

Install either tcpdump or Wireshark with the wireshark-cli package.

where interface is the network interface for a WAN connection (see ip a to check). If you are not receiving any packets while trying to connect remotely, you can be very sure that your ISP is blocking the incoming traffic on port 22.

The solution is just to use some other port that the ISP is not blocking. Open the /etc/ssh/sshd_config and configure the file to use different ports. For example, add:

Also make sure that other "Port" configuration lines in the file are commented out. Just commenting "Port 22" and putting "Port 1234" will not solve the issue because then sshd will only listen on port 1234. Use both lines to run the SSH server on both ports.

Restart the server sshd.service and you are almost done. You still have to configure your client(s) to use the other port instead of the default port. There are numerous solutions to that problem, but let us cover two of them here.

Recent versions of OpenSSH sometimes fail with the above error message when connecting to older ssh servers. This can be worked around by setting various client options for that host. See ssh_config(5) for more information about the following options.

The problem could be the ecdsa-sha2-nistp*-cert-v01@openssh elliptical host key algorithms. These can be disabled by setting HostKeyAlgorithms to a list excluding those algorithms. On the client side, the HostKeyAlgorithms that the client wants to use can also be set by preceding the HostKeyAlgorithms list with a - to remove the specified algorithms (including wildcards) from the default set (see ssh_config(5)). You can check the actually used host key algorithm with ssh -v server_to_connect_to in the line that contains kex: host key algorithm:.

If that does not work, it could be that the list of ciphers is too long. Set the Ciphers option to a shorter list (fewer than 80 characters should be enough). Similarly, you can also try shortening the list of MACs.

See also the discussion on the OpenSSH bug forum.

One possible cause for this is the need of certain SSH clients to find an absolute path (one returned by whereis -b [your shell], for instance) in $SHELL, even if the shell's binary is located in one of the $PATH entries.

If you receive the above errors upon logging in, this means the server does not recognize your terminal. ncurses applications like nano may fail with the message Error opening terminal.

The correct solution is to install the client terminal's terminfo file on the server. This tells console programs on the server how to correctly interact with your terminal. You can get info about current terminfo using infocmp and then find out which package owns it.

If you cannot install it normally, you can copy your terminfo to your home directory on the server:

After logging in and out from the server the problem should be fixed.

Alternatively, you can simply set TERM=xterm in your environment on the server (e.g. in .bash_profile). This will silence the error and allow ncurses applications to run again, but you may experience strange behavior and graphical glitches unless your terminal's control sequences exactly match xterm's.

If you are seeing this error in your sshd logs, make sure you have set a valid HostKey:

Since OpenSSH 8.8, scp uses SFTP as the default protocol for data transfers by requesting the subsystem named sftp. If you run scp in verbose mode, scp -v, you can determine which subsystem your client is using (e.g. Sending subsystem: <subsystem-name>). Errors such as subsystem request failed on channel 0 may be fixed by configuring the server's Subsystem settings: sshd_config(5) § Subsystem. The server configuration should resemble the example below.

OpenSSH 7.0 deprecated DSA public keys for security reasons and OpenSSH 9.8 is built without support for DSA keys by default. The first OpenSSH release of 2025 will remove DSA support entirely. For now, if you absolutely must use them, you will need to rebuild openssh while passing --enable-dsa-keys to configure.[4]

OpenSSH 7.0 deprecated the diffie-hellman-group1-sha1 key algorithm because it is weak and within theoretical range of the so-called Logjam attack (see https://www.openssh.com/legacy.html). If the key algorithm is needed for a particular host, ssh will produce an error message like this:

The best resolution for these failures is to upgrade/configure the server to not use deprecated algorithms. If that is not possible, you can force the client to reenable the algorithm with the client option KexAlgorithms +diffie-hellman-group1-sha1.

If your processes get killed at the end of the session, it is possible that you are using socket activation and it gets killed by systemd when it notices that the SSH session process exited. In that case there are two solutions. One is to avoid using socket activation by using ssh.service instead of ssh.socket. The other is to set KillMode=process in the Service section of ssh@.service.

The KillMode=process setting may also be useful with the classic ssh.service, as it avoids killing the SSH session process or the screen or tmux processes when the server gets stopped or restarted.

SSH responds to flow control commands XON and XOFF. It will freeze/hang/stop responding when you hit Ctrl+s. Use Ctrl+q to resume your session.

If you attempt to create a connection which results in a Broken pipe response for packet_write_wait, you should reattempt the connection in debug mode and see if the output ends in error:

The send packet line above indicates that the reply packet was never received. So, it follows that this is a QoS issue. To decrease the likely-hood of a packet being dropped, set IPQoS:

The reliability (0x04) type-of-service should resolve the issue, as well as 0x00 and throughput (0x08).

If a client session is no longer responding and cannot be terminated by instructing the running program (e.g. shell), you can still terminate the session by pressing Enter, ~ and . one after another in that order.

The ~ is a pseudo-terminal escape character (see ssh(1) § ESCAPE CHARACTERS), which can be added multiple times depending on the client session to terminate. For example, if you connected from A to B and then from B to C and the session from B to C freezes, you can terminate it by pressing Enter and typing ~~., which will leave you in a working session on B.

If the client warns that the key of an ssh server has changed, you should verify that the newly offered key really belongs to the server operator via an authenticated (not necessarily encrypted) channel. Then remove the old key from the known_hosts file with ssh-keygen -R $SSH_HOST and accept the new key as if it was a new server.

When connecting to hosts that do not have a terminfo entry for your terminal, for example, when using a terminal emulator whose terminfo entry is not shipped with ncurses (e.g. kitty and rxvt-unicode), or when connecting to hosts with a limited terminfo database (e.g. systems running OpenWrt), various issues will occur with software that relies on terminfo(5).

A proper solution is to place the appropriate terminfo entry on the host. If that is not feasible, an alternative is to set TERM to a value that is both supported by the remote host and compatible with the terminal.

Since OpenSSH 8.7, a custom TERM environment variable can be passed to remote hosts with a simple configuration snippet:

If you do not have the SHELL environment variable set to a full valid path (on the jump server), connection will fail with an error message simmilar to this one:

You can simply solve this by setting your SHELL to a full path name of a shell that will also be valid on the jump server or by setting a specific SHELL variable for each server in your ~/.ssh/config file.

This article or section is being considered for removal.

A hang during connection setup can be caused by MTU/fragmentation problem. Either try to find the wrong configured router/firewall, or reduce MTU size step by step on client side (poor workaround). Another workaround is to reduce initial ssh payload, by specifying only a reduced number of settings for e.g. KexAlgorithms, HostKeyAlgorithms, Ciphers, MACs.

**Examples:**

Example 1 (unknown):
```unknown
$ ssh -p port user@server-address
```

Example 2 (unknown):
```unknown
Include /etc/ssh/ssh_config.d/*.conf
```

Example 3 (unknown):
```unknown
/etc/ssh/ssh_config
```

Example 4 (unknown):
```unknown
~/.ssh/config
```

---

## Category:Virtual Private Network

**URL:** https://wiki.archlinux.org/title/VPN

A Virtual Private Network (VPN) is a security concept to create a secure communication channel between hosts over another (public) network connection.

This category contains general VPN software, provider-specific software belongs to Category:VPN providers.

See also List of applications/Internet#VPN clients.

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Network_interface

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/DHCP

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## Network Debugging

**URL:** https://wiki.archlinux.org/title/Network_Debugging

**Contents:**
- Ping & Tracepath/Traceroute
- Tcpdump

This article or section is a candidate for merging with Network Configuration.

This article or section is a candidate for merging with Network configuration#Ping.

The ping command can help test connectivity towards a specific host.

The first step would be verifying connectivity towards the default gateway (replace the ip address with your own default gateway):

When erasing the "-c4" parameter, the ping will continue endlessly. It can be aborted by hitting "Control-C".

The output above indicated the default gateway is reachable. When instead a "Destination Host Unreachable" message is displayed, doublecheck the ip address, netmask and default gateway config. This message can also be displayed when ICMP traffic is not permitted towards the default gateway (blocked by a firewall, router,...).

The next step is verifying connectivity towards the configured dns server(s). When no reply is received, tracepath or traceroute can be used to verify the routing towards said server and get an idea of where the issue lies.

Traceroute also used ICMP to determine the path and hence there can be "no reply" answers as well when ICMP traffic is blocked.

tcpdump, and its underlying library libpcap, are multi-platform user space interfaces to the packets on the network. It should be emphasized they do see, they can capture, any inbound packets that reach the local NIC. No matter if the local software firewall is blocking those packets, or not. On the other hand, they can only see outbound packets the firewall passes through: [1]

A short, unintimidating introduction to tcpdump, with examples, is at: [2]

**Examples:**

Example 1 (unknown):
```unknown
$ ping -c4 192.168.1.1
```

Example 2 (unknown):
```unknown
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_req=1 ttl=64 time=0.193 ms
64 bytes from 192.168.1.1: icmp_req=2 ttl=64 time=0.190 ms
64 bytes from 192.168.1.1: icmp_req=3 ttl=64 time=0.192 ms
64 bytes from 192.168.1.1: icmp_req=4 ttl=64 time=0.189 ms

--- 192.168.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2999ms
rtt min/avg/max/mdev = 0.165/0.184/0.193/0.014 ms
```

Example 3 (unknown):
```unknown
Destination Host Unreachable
```

Example 4 (unknown):
```unknown
$ traceroute 8.8.4.4
```

---

## DNS over HTTPS servers

**URL:** https://wiki.archlinux.org/title/DNS_over_HTTPS_servers

**Contents:**
- DoH server/proxy software configuration
  - coreDNS
  - dns-over-https
    - Stub resolver
    - DoH proxy
  - doh-proxy
  - python-doh-proxy
    - Stub resolver
    - DoH proxy
    - DoH proxy

This article or section needs expansion.

DNS, since its inception, has been unencrypted on UDP/53, and later TCP/53, making it susceptible to snooping attacks. For additional information on the available protocols that can be used to address this vulnerability, see Domain name resolution#Privacy and security. This article covers two of the three available protocols for DNS servers with the necessary proxy configuration to provide both DNS over HTTPS (DoH) and DNS over TLS (DoT). Multiple DoH utilities are available in the AUR including corednsAUR, dns-over-https, doh-proxyAUR, and python-doh-proxyAUR. Which of the available solutions is appropriate, depends on the needs of your network.

corednsAUR provides both a caching, non-authoritative DNS server, and DoH services (citation needed).

dns-over-https, doh-proxyAUR, and python-doh-proxyAUR all provide an HTTP listener for proxying behind your existing HTTPS server, and a stub resolver to forward regular queries on UDP/53 to a secure DNS server. Additionally, both doh-proxyAUR and python-doh-proxyAUR provide a standalone HTTPS/2 server.

This article or section is a candidate for merging with CoreDNS#Configuration.

Install the corednsAUR package.

You can use coreDNS as DoH/DoT/gRPC DNS server and/or DoT proxy. Default configuration file should be located at /etc/coredns/Corefile.

The example of simple configuration file looks like this:

First string is listener, you can use next protocols: dns:// for plain DNS protocol, http:// for DNS over HTTPS, tls:// for DNS over TLS and grpc:// for gRPC (see [1]). If you leave protocol empty (e.g. example.com:53), dns:// will be choose as default. The domain is for matching queried domains, you can use specific one (e.g. dns: //example.com: 53) or use . (e.g. dns: //.: 53) to match all domains. And by :port you can set listening port, you can leave it empty and will be chosen 53 port.

forward string is for where DNS query will be forward. Use . for domain to match all domains. In forward_to set upstream DNS server where to send queries, you can specify tls:// protocol for DoT server. If you using upstream DoT server, you need to set tls_servername for TLS negotiation.

tls string mandatory if you use DoH, DoT or gRPC protocols. Put here certificate and private key paths in given order.

Example of configuration simple DoT proxy listening 53 port and using Cloudflare DoT server

Also, you can use several instances and forward plugins:

Start/enable the coredns.service unit.

This article or section is a candidate for merging with DNS-over-HTTPS.

At first, install dns-over-https and after setting will not forget to enable and start needed service.

You can start using it right after install with default settings. Defaults ports for listening is 53 and 5380, if one of them is already binded, it will be ignored. Start/enable doh-client.service.

Configuration file locate at /etc/dns-over-https/doh-client.conf. You can change desired ports at section listen. There are many included third-parted DoH servers in configuration file, you need just uncomment one you needed or write unspecified. You can use several resolvers as well. One of them will be chosen randomly for each request. To force dns-over-https use resolvers in the required order set upstream_selector to weighted_round_robin or lvs_weighted_round_robin and change weight value at resolvers in use.

Configuration file for use as doh server locate at /etc/dns-over-https/doh-server.conf. At upstream section can set desired upstream resolver and its protocol for use. You can use dns-over-https as standalone service or together with HTTPS services like nginx or apache.

For standalone use you need to set port to 443 and specify proper cert and key:

If you want use HTTP server for caching or using along with other HTTPS services leave empty cert and key strings in doh-server.conf and use next examples for configuration desired HTTP server. Note that there using default dns-over-https port.

After setting up, start/enable doh-server.service.

This article or section needs expansion.

This article or section is being considered for removal.

Install python-doh-proxyAUR.

If you intend to provide encrypted queries to your local network for legacy applications, configure the stub resolver:

If you do not have a way to provide a secure forward DNS lookoup to your real DNS server, you should configure both DOMAIN and NS to use one of the upstream providers (CloudFlare, OpenDNS, etc., instead of localhost). If you only need to provide lookups to localhost, this is fine. If you need to provide them for the entire network, the you could listen on 53 directly if you do not have a local caching or authoritative DNS server - you would also want to use the real IP address instead of the loopback adapter in this case.

If you have an existing HTTP server and wish to proxy DNS lookups with it, setup the HTTP proxy to listen on port 8080:

Optionally, you can utilize either the doh-proxy service or an upstream DoH provider to forward queries.

If you do not have an existing http server, you can configure the HTTPS/2 lisener:

Again, adjust as necessary, but be certain that the upstream server has a way to perform secure queries, or you will be creating a loop.

This article or section is a candidate for merging with BIND#Configuration.

BIND 9.18 natively supports serving both DNS over HTTPS and DNS over TLS. See BIND#Configuration for details.

Typical: If using ISC bind as the current DNS provider, and you will be providing both forwarding services for legacy clients and DoH to modern clients, you will likely want to configure named to forward all non-local queries to your stub resolver, comment out any forwarding lines an forward to the stub resolver (omit forward only if you would like to fall back to roots):

This article or section is out of date.

If you want to forward to an external TLS proxy (via stunnel), do the same but use only TCP/54 (see stunnel configuration below):

Optional: If using ISC bind as the current DNS provider, and you will be providing both forwarding services for legacy clients and DoH to modern clients, you might want to configure named to listen on an alternate port, for example TCP|UDP/54, rather than the default of 53 so that your stub resolver will listen on the standard port. Comment out any existing 'listen' lines and add the following (omit the v6 line if not needed):

This article or section is a candidate for merging with Unbound#Configuration.

You can easily set up DoT server by adding to your configuration file port 853 to listening and specify certificate and key paths:

DoH server setup is same as DoT, but needed port is 443:

Configure a proxy in your primary httpd.conf or appropriate vhost listening on 443:

With Nginx stream module you can setup proxy to upstream DNS. Note that you can use local dns as well as third parties.

For DoH implementation you need for use additional NJS scripts. You need to get it from this GitHub's page, put it to /etc/nginx/njs.d/ and be sure package nginx-mod-njs is installed.

At first you need to setup stream service, which will be get DNS request from nginx's HTTP/2 service, process it with js_filter to find DNS packets and pass it to upstream DNS server.

Then, setup HTTP/2 service to listen DNS requests at URI /dns-query and relay them to stream service. Note that to a need change certificates to valid

You can use both DoT and DoH services at same time, caching and multiple upstream DNS. For more examples see these configuration files

This article or section is a candidate for merging with stunnel#DNS over TLS.

Configure stunnel to listen on TCP/853 for TLS connections, and forward to your local DNS provider:

Configure stunnel to listen on TCP/54 and forward to an upstream secure provider:

See https://hub.docker.com/r/satishweb/doh-server.

**Examples:**

Example 1 (unknown):
```unknown
/etc/coredns/Corefile
```

Example 2 (unknown):
```unknown
/etc/coredns/Corefile
```

Example 3 (unknown):
```unknown
protocol://domain:port {
    forward domain forward_to
    tls_servername domain_of_dot_server
    tls cert_path key_path
}
```

Example 4 (unknown):
```unknown
tls_servername
```

---

## Broadcom wireless

**URL:** https://wiki.archlinux.org/title/Broadcom_wireless

**Contents:**
- History
- Driver selection
- Installation
  - brcm80211
    - BCM43602 802.11ac Wireless LAN SoC
  - b43
  - broadcom-wl
- Known issues
  - Ethernet card is not detected
  - Older Broadcom drivers not allowing connections

This article details how to install and setup a Broadcom wireless network device.

Broadcom has a noted history with its support for Wi-Fi devices regarding GNU/Linux. For a good portion of its initial history, Broadcom devices were either entirely unsupported or required the user to tinker with the firmware. The limited set of wireless devices that were supported were done so by a reverse-engineered driver. The reverse-engineered b43 driver was introduced in the 2.6.24 kernel.

In August 2008, Broadcom released the 802.11 Linux STA driver officially supporting Broadcom wireless devices on GNU/Linux. This is a restrictively licensed driver and it does not work with hidden ESSIDs, but Broadcom promised to work towards a more open approach in the future.

In September 2010, Broadcom released a fully open source driver. The brcm80211 driver was introduced in the 2.6.37 kernel and in the 2.6.39 kernel it was sub-divided into the brcmsmac and brcmfmac drivers.

The types of available drivers are:

To know what driver(s) are operable on the computer's Broadcom wireless network device, the device ID and chipset name will need to be detected. Cross-reference them with the driver list of devices supported by the brcm80211 and b43 drivers.

Check if your device is supported by the builtin kernel driver brcm80211 first before resorting to other drivers.

The kernel contains two built-in open-source drivers: brcmfmac for native FullMAC and brcmsmac for mac80211-based SoftMAC. They should be automatically loaded when booting.

Chips supported by the brcm80211 driver can be found in [1].

BCM43602 needs the brcmfmac.feature_disable=0x82000 kernel parameter as tested with PCI Device ID 14e4:43ba (see BBS#298025).

Two reverse-engineered open-source drivers are built-in to the kernel: b43 and b43legacy. b43 supports most newer Broadcom chipsets, while the b43legacy driver only supports the early BCM4301 and BCM4306 rev.2 chipsets. To avoid erroneous detection of your Wi-Fi cards chipset, blacklist the unused driver.

Both of these drivers require non-free firmware to function. Install b43-firmwareAUR, b43-firmware-classicAUR, or b43legacy-firmwareAUR depending on the chipset.

The b43 should be loaded automatically, but you may need to explicitly load the module at boot.

There are two variants of the restrictively licensed driver:

Broadcom wireless module has a history of conflicting with Broadcom Ethernet module.

Due to conflicts between wl (wireless module) and tg3 (Ethernet module), tg3 is now blacklisted as of broadcom-wl-dkms 6.30.223.271-27[2]. See also FS#70476.

This also affects broadcom-wl as it is built based on broadcom-wl-dkms.

Broadcom chips BCM4360 or lower do not support modern security connection methods such as WPA3. WPA2 or alternative security methods are necessary for certain network connections to handshake.

Monitor mode is used to capture 802.11 frames over the air. This can be useful for diagnosing issues on a network or testing the security of your wireless network. Often, monitor mode is required to capture certain frames for wireless penetration testing, but it may be unethical or even illegal to capture frames on any network you do not own, manage or have permission to perform penetration testing against.

To set broadcom-wl in monitor mode you have to set 1 to /proc/brcm_monitor0:

It will create a new network interface called prism0.

To work in monitor mode, use this newly created network interface.

Since the 3.3.1 kernel the bcma module was introduced. If using a brcm80211 driver be sure it has not been blacklisted. It should be blackisted if using a b43 driver.

If you are using broadcom-wl, uninstall and reinstall it after upgrading your kernel or switch to broadcom-wl-dkms package.

Be sure the correct modules are blacklisted and occasionally it may be necessary to blacklist the brcm80211 drivers if accidentally detected before the wl driver is loaded. Furthermore, update the modules dependencies depmod -a, verify the wireless interface with ip addr, kernel upgrades will require an upgrade of the non-DKMS package.

Append the following kernel parameter:

You may continuously get some verbose and annoying messages during the boot, similar to

To disable those messages, increase the loglevel of printk messages that get through to the console - see Silent boot#sysctl.

This device will not display with either lspci nor lsusb; there is no known solution yet.

As per the driver page it may be necessary to copy the efi vars before the driver will operate correctly. However the expected path depends on your system.

Write the efi vars into the referenced location, e.g. on a thinkpad tablet:

If no other approaches help, install linux-lts, or use a previous driver version.

Issue appears to be linked to a channel issue. Changing the wireless channel to a lower channel number (like 40 or, if your router show MHz instead of channel numbers, like 5200 MHz or 5280 MHz) seems to allow connection to 5GHz bands. If your router has the same SSID for the 2.4GHZ and 5GHZ, this can fix problems with your wireless connection being unstable or very slow.

In some cases (e.g. using BCM4331 and b43-firmwareAUR), Wi-Fi connection works intermittently. One way to fix this is to check if the card is hard-blocked or soft-blocked by kernel, and if it is, unblock it with rfkill.

The b43-firmwareAUR driver has been observed hanging in ssh sessions with BCM4331. Installing broadcom-wl and removing b43 solves it.

If you have a brcm43430 connected via SDIO, you are unable to see the device after booting the installation ISO, because in the delivered image is missing a default parameter file for the device: brcmfmac43430-sdio.txt.

To overcome the problem, you have to download brcmfmac43430-sdio.txt on another machine, and copy it on a different pendrive.

After booting the install ISO you need to copy the file to the /lib/firmware/brcm/ directory. Then follow these steps in order to activate it:

After that you can start iwctl that now should find your device, and proceed with the installation as usual.

After completing the installation, do not forget to copy the file to the target disk to the same location.

If you are using the kernel driver along with certain Broadcom laptop Wi-Fi cards, you may experience extremely slow or even unusable internet speeds. This can be fixed by installing #broadcom-wl and rebooting

Some users report that systems using the brcmfmac driver (notably the Broadcom 4352 chipset on MacBookPro12,1 and similar hardware) experience Wi-Fi failures after suspending. Symptoms may include:

This appears to be a race condition during suspend, where the driver is not properly unloaded before power state changes occur.

A workaround is unloading the brcmfmac module before suspend and reload it after resume by systemd service:

**Examples:**

Example 1 (unknown):
```unknown
$ lspci -vnn -d 14e4:
```

Example 2 (unknown):
```unknown
brcmfmac.feature_disable=0x82000
```

Example 3 (unknown):
```unknown
Loading firmware b43/ucode4.fw
```

Example 4 (unknown):
```unknown
Loading firmware b43legacy/ucode4.fw
```

---

## Wireless bonding

**URL:** https://wiki.archlinux.org/title/Wireless_bonding

**Contents:**
- Network Interface Bonding with Removable Device Support
- DHCP configuration
- Static Network configuration
- wpa_supplicant configuration
- Slave configuration
- Master configuration
- Enabling/Installing the Service Units
- Testing the result

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

This article or section needs expansion.

The Linux bonding driver provides a method for aggregating multiple network interfaces into a single logical "bonded" interface. Linux Ethernet Bonding Driver HOWTO

The Linux kernel bonding driver can be used to provide parallel network connections to maximize throughput, or to allow redundant network connections to maximize network availability. Here is an example of using the kernel bonding driver to maximize availability, by allowing network connections to "failover" between a primary network device and any number of secondary devices, or alternatively, by selecting the highest speed connection available. This approach provides Automatic Wired and Wireless Network Configuration with Removable Device Support, using only the kernel bonding module in "active-backup" mode, the sysfs, the iproute2 commands, and systemd "template" Unit files, without using systemd-networkd.

This example will run wpa_supplicant continuously on any interface, as needed, and DHCP client on a virtual "bond0" interface. This is useful, for instance, with a portable computer when you want to use the wired interface for speed and/or security when available, and the wireless interface when the wired interface is not available. The basic idea is to have two "always active" wired and wireless interfaces, then "bond" or "enslave" them to a virtual interface "master", and then let the kernel bonding module handle switching between the interfaces. Of course, this scheme can be applied to any other type of network interface, and extended to more than two physical or virtual network interfaces.

Note that host networking is managed directly with systemd, and that no other "connection manager" is used here, providing a more basic approach. But then also, wpa_supplicant itself can still be managed directly using wpa_gui from wpa_supplicant_guiAUR, to scan for, select, and connect to new wireless access points/base stations.

In this example, there are six systemd service unit files used, along with five associated configuration files, for the kernel bonding module, wpa_supplicant, dhclient, and for static network configuration and specifying the primary slave network interface name. The six unit files are essentially generic service unit files which do not contain configuration data, and no modification is needed. The various service units may be stopped, started, and restarted individually without ordering errors or failed states. Any network interface device, such as typically a wired or wireless PC Card, may be removed and replaced, and reconfiguration will be automatic.

If you also run a DHCPv6 client, make sure that the DHCP Client Identifier and the DHCPv6 Client Identifier are the same DUID. The DHCP Server, dnsmasq for instance, can be configured to give fixed IP addresses based upon multiple MAC addresses, or provided hostname, or provided Client Identifier.

There is a particular issue to address. When starting kernel bonding, where the only working interface is the non-primary slave - for instance, starting with only a wireless interface available when the wired interface is the primary - then dhclient will quickly start and adopt the MAC address of the initial primary slave, and use that MAC address when attempting to communicate with the DHCP server. When the wireless interface, some short time later, is authenticated, associated, and authorized with the access point/base station, establishing a connection to the network, the bonding driver will make the wireless interface the new active interface, and change the active MAC address on the bond0 interface, to match the wireless MAC address. Because dhclient will continue to use the MAC address from the wired interface, and that MAC address is no longer accepted by the bond0 interface, all DHCP communication will fail. If there is no saved lease file in /var/lib/dhclient/dhclient.leases, then no IPv4 address will be configured, and no IPv4 traffic will be possible. It can also be seen that when dhclient starts quickly, it can read the primary slave's firmware MAC address, rather than any MAC address assigned to the device interface. If the firmware MAC address is "null", then dhclient assigns a random MAC address. BOOTP/DHCP packets using these firmware or random MAC addresses may "succeed" in gaining a reply on the primary slave device and fail on the non-primary slave device. That can be confusing and annoying.

These are only issues with dhclient and IPv4. Fortunately, on a dhclient DHCP request, after the lease expires, dhclient "does the right thing". dhclient will function properly no matter on which slave interface it was started.

This problem cannot be solved by configuring the bonding driver with the default fail_over_mac=none. Almost all network interface devices will not pass traffic with a MAC address which is not their own. An example of this kind of warning can be seen here. Strange network behavior will be the result, where broadcast packets will pass, but ping/icmp packets will only pass in some circumstances and not others.

Ideally, dhclient would re-determine the bonding interface MAC address each time it initially retried contacting the DHCP server. Without that, a different approach is to simply delay the start of dhclient until after the kernel bonding driver has configured an active slave. If the active slave is to be the wireless interface, then wpa_supplicant will first have authenticated, associated, and authorized with the access point/base station, and dhclient will adopt the correct MAC address. If the active slave is the primary slave, again dhclient will adopt the correct MAC address. This delay is imposed with the simple ExecStartPre= /usr/bin/sleep 8 line in the dhclient service unit file, a conservatively long delay between the time systemd starts dhclient and the supplicant and the bonding driver selects the active interface. This selection time is longest during system boot, when many processes are starting. On faster hardware, a shorter delay, perhaps sleep 4, may still be effective.

Here, for instance, a static private IPv4 address will be assigned to the bonding interface as a "fail-safe", were the DHCP server to fail or be otherwise inaccessible. The primary slave interface is also specified in this file.

Of course, static network configuration may be used as an alternative to, or in addition to, dynamic network configuration, or not at all.

Be careful with the actual protocol configuration in the wpa_supplicant configuration file. Using protocols incompatible with the base station can result in unstable and otherwise difficult to troubleshoot wireless connections. Pre-compute the PSK with wpa_passphrase ssid passphrase. wpa_gui can overwrite this file. Note that wpa_supplicant can be run on any wired or wireless interface, as needed.

The supplicants and the DHCP client are ordered relative to the network-pre.target on shutdown. The supplicants must not be stopped before the DHCP client releases the address lease.

Remember that the iw commands do not work with the wired interface drivers or with older wireless drivers which rely upon the Wireless Extensions user-space driver, and will be ignored in those cases.

There is a "trick" which will be used here, in the naming of the slave service template unit files. Two environment variables are to be passed to the slave unit files, the name of the network interface, and the name of the bonding interface. Notice that there are two particular environment variables passed into a systemd unit file, %p/%P and %i/%I, these being the strings before and after the "@" character in the name of a template unit file. Here, the bonding interface name is specified in that portion of the unit file name after the "@" character, and the network interface name is passed in that portion before the "@" character. This allows two network interface names to be specified arbitrarily on the command line, without modifying the unit files themselves.

This "slave@.service" unit file will be hard linked to files having the same name as the network interfaces, such as "wlp2s0@.service" and "enp3s0@.service". Note that symbolic links cannot be used here, since systemd would then set %p/%P to the target file name "slave", instead of the desired network interface name.

Of course, "Environment=" could be used here instead of the Environment file, if static network configuration is not used, and then the Environment file could be avoided. Settings from Environment files override settings made with "Environment=".

This master service unit file supports creation of a bonding master or a bridging master network interface. The type of master interface created is determined by the name of the interface. A bridging master is created when the interface name includes the character string "br", and a bonding master is created otherwise.

The RequiredBy dependencies are only here to activate the stop ordering of static or dynamic network configuration units during master stop and restart. The network configurations must be taken-down and that process completed before the slave interfaces are freed and the master interface is deleted.

Enable/Install a bonding master unit or bridging master unit only when the master interface is also an IP interface for the host, which is to say, when there is a static or dynamic network configuration unit Enabled/Installed on that master interface. If the bonding master or bridging master is not also an IP interface, then the master service unit should not be Enabled/Installed, since it will be started manually, or will be started by the slave service units, on boot, or when a network device is plugged.

With those preliminaries, the interface names must be specified on the command line.

Whenever a unit file is edited, afterward run a daemon-reload.

Next, observe the available network interface names, after inserting any removable devices:

For each interface which will be enslaved, hard link "slave@.service" to "interface_name@.service":

Now, determine which network interface devices will need a supplicant to access the network. Typically this will just be the wireless interface. Start/enable the supplicant@.service unit for each interface, as needed (e.g. supplicant@wlp2s0.service)

Then, enable the slave and master units, using any desired interface name. (Here, "bond0" is used: enp3s0@bond0.service wlp2s0@bond0.service master@bond0.service)

Explicitly enable only the desired network configuration, specifying the interface name(here again, bond0: dhclient@bond0.service static@bond0.serice)

And finally, activate the bonding interface, the DHCP client, and any static network configuration, by starting master@bond0.service

The master and supplicant units will be started automatically when any configured slave device appears, and in particular, when the system boots. Were any of the DHCP, or slave units to be started independently, the master unit would also be started, but normally these units will have already been started at boot.

Using the wired ethernet interface,

Using the wireless interface,

To tear-down the bonding interface and shutdown the master, slave, and DHCP units, simply stop master@bond0.service.

The supplicant units can be stopped independently with supplicant@interface_name.service.

This approach to bonded wireless networking leaves wpa_supplicant running continuously on whatever interfaces it is started. By running htop, it can be seen that wpa_supplicant, and the DHCP client daemon, seem to behave well, and do not use any noticeable CPU time.

Still, a hardware switch or rfkill can be used to actually disable the radio when desired.

Notice that the various service units are quite independent except for the ordering dependencies that have been explicitly configured. So, for instance, a dhclient configured IPv4 address may be removed without disturbing any other network configuration or functionality by stoping dhclient@bond0.service.

Similarly, an address may be released and a new address acquired with a restart of dhclient@bond0.service.

And a static address or default gateway may be changed by stopping the static service unit (static@bond0.service), editing the network.conf file, and then starting the static@bond0.service unit again

Also, wpa_supplicant could be temporarily disabled when only the wired interface is being used, and then started again later.

This bonding interface will function properly even with only one interface available, for instance, when only a wired interface is being used. And then, simply inserting a configured wireless network card, this new wireless interface will be automatically added to the bonded interface pool, and wpa_supplicant started. Removing this wireless card again will remove the slave interface and stop wpa_supplicant.

Check that the Ethernet cable is actually plugged-in when wired networking is preferred. And use, for instance, wpa_cli status or iwconfig to verify a connection to the correct Service Set Identifier/SSID when wireless networking is used.

**Examples:**

Example 1 (unknown):
```unknown
/etc/dhclient.conf
```

Example 2 (unknown):
```unknown
# These time-outs are aggressively short, supposing a sparsely populated network.
initial-interval 2;
reboot 5;
timeout 10;
retry 20;

# RFC 4361          Node-specific Identifiers for DHCPv4     February 2006
send dhcp-client-identifier 00:02:00:02:2e:2d:01:bd:c3:92:9a:44:2a:c4 ;
send host-name "laptop";
```

Example 3 (unknown):
```unknown
/etc/systemd/system/dhclient@.service
```

Example 4 (unknown):
```unknown
[Unit]
Description= ISC dhclient on interface %I
Documentation= man:dhclient(8) man:dhclient.conf(5)

Wants= network.target
Before= network.target
After= network-pre.target

BindsTo= sys-subsystem-net-devices-%i.device

[Service]
ExecStartPre= /usr/bin/sleep 8
ExecStart= /usr/bin/dhclient -d -pf /run/dhclient-%i -i %I

# Release the current lease and ensure that dhclient has actually stopped.
ExecStop= /usr/bin/dhclient -r -pf /run/dhclient-%i
ExecStop= /usr/bin/sleep 1

Restart= on-abnormal

[Install]
WantedBy= sys-subsystem-net-devices-%i.device
```

---

## Network configuration/Ethernet

**URL:** https://wiki.archlinux.org/title/Network_configuration/Ethernet

**Contents:**
- Device driver
  - Check the status
  - Load the module
- Tips and tricks
  - ifplugd for laptops
  - Reduce link speed
- Troubleshooting
  - Swapping computers on the cable modem
  - Explicit Congestion Notification
  - Broadcom BCM57780

This article describes Ethernet specifics, general network configuration is covered in Network configuration.

udev should detect your network interface controller (NIC) and automatically load the necessary kernel module at startup. Check the output of lspci -knnd ::0200 (where ::0200 means the "Ethernet controller" subclass of the "Network controller" PCI device class) . It should tell you which kernel module contains the driver for your network device. For example:

Next, check that the driver was loaded by running dmesg | grep module_name as root. For example:

Skip the next section if the driver was loaded successfully. Otherwise, you will need to know which module is needed for your particular model.

Search the internet for the right module/driver for your chipset. Some common modules are 8139too for cards with a Realtek chipset, or sis900 for cards with a SiS chipset. Once you know which module to use, try to load it manually. If you get an error saying that the module was not found, verify first if you recently upgraded the kernel (see General troubleshooting#Cannot use some peripherals after kernel upgrade). Alternatively, it is possible that the driver is not included in the Arch kernel. You may search the AUR for the module name.

If udev is not detecting and loading the proper module automatically during bootup, you can explicitly load the module at boot.

ifplugd is a daemon which will automatically configure your Ethernet device when a cable is plugged in and automatically unconfigure it if the cable is pulled. This is useful on laptops with onboard network adapters, since it will only configure the interface when a cable is really connected. Another use is when you just need to restart the network but do not want to restart the computer or do it from the shell.

By default it is configured to work for the eth0 device. This and other settings like delays can be configured in /etc/ifplugd/ifplugd.conf.

The factual accuracy of this article or section is disputed.

Forcing 100Mbps or 10Mbps full-duplex speed on a gigabit ethernet NIC can save a lot of power (~1W) on most network workloads. This also reduces components temperature.

Using ethtool -s eth0 autoneg off speed 100 on every boot is inconvenient.

Boot time initialization of lower ethernet NIC speed is possible through systemd.link files. The actual setup is performed by the net_setup_link udev builtin. Add the AutoNegotiation option to the network link file:

Also see systemd.link(5) for more information.

Some cable ISPs (Vidéotron for example) have the cable modem configured to recognize only one client PC, by the MAC address of its network interface. Once the cable modem has learned the MAC address of the first PC or equipment that talks to it, it will not respond to another MAC address in any way. Thus if you swap one PC for another (or for a router), the new PC (or router) will not work with the cable modem, because the new PC (or router) has a MAC address different from the old one. To reset the cable modem so that it will recognise the new PC, you must power the cable modem off and on again. Once the cable modem has rebooted and gone fully online again (indicator lights settled down), reboot the newly connected PC so that it makes a DHCP request, or manually make it request a new DHCP lease.

If this method does not work, you will need to clone the MAC address of the original machine. See also MAC address spoofing.

Explicit Congestion Notification (ECN) may cause traffic problems with old/bad routers [1]. As of systemd 240, it is enabled for incoming connections that request it (kernel default).

To enable ECN for both incoming and outgoing connections:

To enable ECN only when requested by incoming connections (the reasonably safe, kernel default):

To disable ECN completely (to e.g. test whether ECN was causing problems):

See also the kernel documentation.

This Broadcom chipset sometimes does not behave well unless you specify the order of the modules to be loaded. The modules are broadcom and tg3, the former needing to be loaded first.

These steps should help if your computer has this chipset:

Users with Realtek 8168 8169 8101 8111(C) 8156B based NICs (cards / and on-board) may notice a problem where the NIC seems to be disabled on boot and has no Link light. This can usually be found on a dual boot system where Windows is also installed. It seems that using the official Realtek drivers (dated anything after May 2007) under Windows is the cause. These newer drivers disable the Wake-On-LAN feature by disabling the NIC at Windows shutdown time, where it will remain disabled until the next time Windows boots. You will be able to notice if this problem is affecting you if the Link light remains off until Windows boots up; during Windows shutdown the Link light will switch off. Normal operation should be that the link light is always on as long as the system is on, even during POST. This problem will also affect other operating systems without newer drivers (eg. Live CDs). Here are a few fixes for this problem.

Follow Network configuration#Enabling and disabling network interfaces to enable the interface.

You can roll back your Windows NIC driver to the Microsoft provided one (if available), or roll back/install an official Realtek driver pre-dating May 2007 (may be on the CD that came with your hardware).

Probably the best and the fastest fix is to change this setting in the Windows driver. This way it should be fixed system-wide and not only under Arch (eg. live CDs, other operating systems). In Windows, under Device Manager, find your Realtek network adapter and double-click it. Under the "Advanced" tab, change "Wake-on-LAN after shutdown" to "Enable".

It appears that setting Integrated Peripherals > Onboard LAN Boot ROM > Enabled in BIOS/CMOS reactivates the Realtek LAN chip on system boot-up, despite the Windows driver disabling it on OS shutdown.

When using power saving features, specifically USB autosuspend, the device can fail to load correctly, resulting in a NO-CARRIER state (tested with RT8156B), and no established link.

To resolve, see Power management#USB autosuspend for details on blacklisting a device for USB autosuspend manually, or TLP documentation on USB devices if using TLP; then reconnect the device.

The adapter should be recognized by the r8169 module. However, with some chip revisions the connection may go off and on all the time. The alternative r8168AUR should be used for a reliable connection in this case. Blacklist r8169, if r8168AUR is not automatically loaded by udev, you can explicitly load the module at boot.

The factual accuracy of this article or section is disputed.

Another fault in the drivers for some revisions of this adapter is poor IPv6 support. IPv6#Disable functionality can be helpful if you encounter issues such as hanging webpages and slow speeds.

With motherboards such as the Gigabyte GA-990FXA-UD3, booting with IOMMU off (which can be the default) will cause the network interface to be unreliable, often failing to connect or connecting but allowing no throughput. This will apply to the onboard NIC and to any other pci-NIC in the box because the IOMMU setting affects the entire network interface on the board. Enabling IOMMU and booting with the install media will throw AMD I-10/xhci page faults for a second, but then boots normally, resulting in a fully functional onboard NIC (even with the r8169 module).

When configuring the boot process for your installation, add iommu=soft as a kernel parameter to eliminate the error messages on boot and restore USB3.0 functionality.

With motherboards such as the "MicroStar B450M MORTAR TITANIUM", unpluging/pluging Ethernet cables or restarting router's DHCP server would cause r8169 to enter a downshifted status, and downgrade the 1000 Mbit/s Ethernet speed to 100 Mbit/s. The kernel log will show:

In this case, restart the adapter (set it down and up). For example:

USB Network Adapters with the following controller will often hang and stop transmit until its link is reset. This is accompanied with Tx status -2 or Tx status -71 errors in the kernel log. This can be fixed by setting USB_QUIRK_NO_LPM.

The quirk can be set at boot by adding the kernel parameter usbcore.quirks=2357:0601:k. It can also be set immediately via the sysfs by

Note that 2357:0601 should be replaced with your own device's USB ID which can be found using lsusb.

**Examples:**

Example 1 (unknown):
```unknown
lspci -knnd ::0200
```

Example 2 (unknown):
```unknown
$ lspci -knnd ::0200
```

Example 3 (unknown):
```unknown
01:00.1 Ethernet controller [0200]: Intel Corporation 82599ES 10-Gigabit SFI/SFP+ Network Connection [8086:10fb] (rev 01)
	Subsystem: Intel Corporation Ethernet Server Adapter X520-2 [8086:000c]
	Kernel driver in use: ixgbe
	Kernel modules: ixgbe
```

Example 4 (unknown):
```unknown
dmesg | grep module_name
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Network_configuration

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## NetworkManager

**URL:** https://wiki.archlinux.org/title/NetworkManager

**Contents:**
- Installation
  - Enable NetworkManager
  - Additional interfaces
  - Mobile broadband support
  - PPPoE / DSL support
  - VPN support
- Usage
  - nmcli examples
  - Edit a connection
  - nmtui

NetworkManager is a program for providing detection and configuration for systems to automatically connect to networks.

NetworkManager can be useful for both wireless and wired networks. For wireless networks, NetworkManager prefers known wireless networks and has the ability to switch to the most reliable network. NetworkManager-aware applications can switch from online and offline mode.

NetworkManager also prefers wired connections over wireless ones, has support for modem connections and certain types of VPN.

NetworkManager can be installed with the package networkmanager, which contains a daemon, a command line interface (nmcli) and a curses‐based interface (nmtui).

After installation, you should start/enable NetworkManager.service. Once the NetworkManager daemon is started, it will automatically connect to any available "system connections" that have already been configured. Any "user connections" or unconfigured connections will need nmcli or an applet to configure and connect.

NetworkManager uses ModemManager for mobile broadband connection support.

Install modemmanager and usb_modeswitch. Afterwards enable and start ModemManager.service.

It may be necessary to restart NetworkManager.service for it to detect ModemManager. After you restart it, re-plug the modem again and it should be recognized.

Add connections from a front-end (e.g. nm-connection-editor) and select mobile broadband as the connection type. After selecting your ISP and billing plan, APN and other settings should be filled in automatically using information from mobile-broadband-provider-info.

Install ppp package for PPPoE / DSL connection support. To actually add PPPoE connection, use nm-connection-editor and add new DSL/PPPoE connection.

NetworkManager since version 1.16 has native support for WireGuard, all it needs is the wireguard kernel module. Read the WireGuard in NetworkManager blog post for details.

Support for other VPN types is based on a plug-in system. They are provided in the following packages:

NetworkManager comes with nmcli(1) and nmtui(1).

List nearby Wi-Fi networks:

Connect to a Wi-Fi network:

Connect to a hidden Wi-Fi network:

Connect to a Wi-Fi on the wlan1 interface:

Disconnect an interface:

Get a list of connections with their names, UUIDs, types and backing devices:

Activate a connection (i.e. connect to a network with an existing profile):

See a list of network devices and their state:

For a comprehensive list of settings, see nm-settings(5).

Firstly, you need to get a list of connections:

Here you can use the first column as connection-id used later. In this example, we pick Wired connection 2 as a connection-id.

You have three methods to configure a connection Wired connection 2 after it has been created:

To remove a setting, pass an empty field ("") to it like this:

NetworkManager ships a text user interface (TUI) for managing connections, the system hostname and radio switches. It can be launched by running nmtui.

To provide integration with a desktop environment, most users will want to install an applet. This not only provides easy access to network selection and configuration, but also provides the agent necessary for securely storing secrets. Various desktop environments have their own applet; otherwise, you can use #nm-applet.

GNOME has a built-in tool, accessible from the Network settings.

Install the plasma-nm package. After that, add it to the KDE taskbar via the Panel options > Add widgets > Networks menu.

network-manager-applet is a GTK 3 front-end which works under Xorg environments with a systray.

To store connection secrets install and configure an application which implements the Secret Service D-Bus API such as GNOME/Keyring, KDE Wallet, or KeePassXC.

Be aware that after enabling the tick-box option Make available to other users for a connection, NetworkManager stores the password in plain-text, though the respective file is accessible only to root (or other users via nm-applet). See #Encrypted Wi-Fi passwords.

In order to run nm-applet without a systray, you can use trayerAUR or stalonetray. For example, you can add a script like this one in your path:

When you close the stalonetray window, it closes nm-applet too, so no extra memory is used once you are done with network settings.

The applet can show notifications for events such as connecting to or disconnecting from a Wi-Fi network. For these notifications to display, ensure that you have a notification server installed - see Desktop notifications. If you use the applet without a notification server, you might see some messages in stdout/stderr, and the applet might hang. See [2].

In order to run nm-applet with such notifications disabled, start the applet with the following command:

As of version 1.18.0 Appindicator support is available in the official network-manager-applet package. To use nm-applet in an Appindicator environment start the applet with the following command:

Alternatively there is networkmanager-dmenu-gitAUR which is a small script to manage NetworkManager connections with dmenu or rofi instead of nm-applet. It provides all essential features such as connection to existing NetworkManager Wi-Fi or wired connections, connect to new Wi-Fi connections, requests passphrase if required, connect to existing VPN connections, enable/disable networking, launch nm-connection-editor GUI, connect to Bluetooth networks.

Pantheon's switchboard offers a desktop environment-agnostic way to configure NetworkManager when combined with switchboard-plug-network and nm-connection-editor. It can be ran with the following command:

NetworkManager will require some additional steps to be able run properly. Make sure you have configured /etc/hosts as described in Network configuration#Set the hostname section.

NetworkManager has a global configuration file at /etc/NetworkManager/NetworkManager.conf. Additional configuration files can be placed in /etc/NetworkManager/conf.d/. Usually no configuration needs to be done to the global defaults.

After editing a configuration file, the changes can be applied by running:

Enabling NetworkManager.service also enables NetworkManager-wait-online.service, which is a oneshot system service that waits for the network to be configured. The latter has WantedBy=network-online.target, so it will finish only when network-online.target itself is enabled or pulled in by some other unit. See also systemd#Running services after the network is up.

By default, NetworkManager-wait-online.service waits for NetworkManager startup to complete, rather than waiting for network connectivity specifically (see nm-online(1)). If NetworkManager-wait-online.service finishes before the network is really up, resulting in failed services on boot, extend the unit to remove the -s from the ExecStart line:

Be aware that this can cause other issues.

In some cases, the service will still fail to start successfully on boot due to the timeout setting being too short. Edit the service to change NM_ONLINE_TIMEOUT from 60 to a higher value.

By default, all users in active local sessions are allowed to change most network settings without a password. See General troubleshooting#Session permissions to check your session type. In most cases, everything should work out of the box.

Some actions (such as changing the system hostname) require an administrator password. In this case, you need to add yourself to the wheel group and run a Polkit authentication agent which will prompt for your password.

For remote sessions (e.g. headless VNC), you have several options for obtaining the necessary privileges to use NetworkManager:

NetworkManager does support some proxy settings. While they can not be directly modified using nmtui, nm-applet and nmcli support those. See the proxy settings in nm-settings-nmcli(5).

Additionally, custom proxy commands can always be run using dispatcher scripts, see #Dispatcher examples.

See also Proxy settings.

NetworkManager can try to reach a webserver after connecting to a network in order to determine if it is e.g behind a captive portal. The default host (configured in /usr/lib/NetworkManager/conf.d/20-connectivity.conf) is ping.archlinux.org (a CNAME alias of redirect.archlinux.org). To use a different webserver or to disable connectivity checking, create /etc/NetworkManager/conf.d/20-connectivity.conf, see NetworkManager.conf(5) § CONNECTIVITY SECTION. Below is an example of using GNOME servers (it does not require the use of GNOME):

To disable NetworkManager's connectivity check, use the following configuration. This can be useful when connected to a VPN that blocks connectivity checks.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

For those behind a captive portal, the desktop manager may automatically open a window asking for credentials. If your desktop does not, you can use capnet-assist package (however, it currently has a broken NetworkManager dispatcher script). Alternatively, you can create a NetworkManager dispatcher script with the following content:

Make the script executable. But that script assumes you use X and simply opens http page. It might not work for everyone.

You will need to restart NetworkManager.service or reboot for this to start working. Once you do, the dispatcher script should open a login window once it detects you are behind a captive portal.

Simple solution is captive-portal-sh - shell script that obtains captive portal URL and opens it in your default browser (for Wayland users only).

Another solution is captive-browser-gitAUR based on Google Chrome.

Some older Wi-Fi chips (e.g. Broadcom BCM4360) require the proprietary wl driver, which lacks support for the OWE/Elliptic-Curve handshake that many captive-portal hotspots use before presenting a login page. By switching NetworkManager’s Wi-Fi backend to iwd (see #Using iwd as the Wi-Fi backend), which implements the full OWE key exchange in userspace over the existing driver, you can complete the encrypted association, obtain a DHCP lease, and trigger the portal “PORTAL” state. Once that is done, any dispatcher script or browser-launcher will reliably pop up the login page on hardware that otherwise could never fully connect.

By default NetworkManager uses its internal DHCP client. The internal DHCPv4 plugin is based on the nettools' n-dhcp4 library, while the internal DHCPv6 plugin is made from code based on systemd-networkd.

To use a different DHCP client install one of the alternatives:

To change the DHCP client backend, set the option main.dhcp=dhcp_client_name with a configuration file in /etc/NetworkManager/conf.d/. E.g.:

Do not enable the systemd units shipped with the dhclient and dhcpcd packages. They will conflict with NetworkManager, see the note in #Installation for details.

NetworkManager's DNS management is described in the GNOME project's wiki page—Projects/NetworkManager/DNS.

NetworkManager has a plugin to enable DNS caching and conditional forwarding (previously called "split DNS" in NetworkManager's documentation) using dnsmasq or systemd-resolved. The advantages of this setup is that DNS lookups will be cached, shortening resolve times, and DNS lookups of VPN hosts will be routed to the relevant VPN's DNS servers. This is especially useful if you are connected to more than one VPN.

Make sure dnsmasq has been installed. Then set main.dns=dnsmasq with a configuration file in /etc/NetworkManager/conf.d/:

Now run nmcli general reload as root. NetworkManager will automatically start dnsmasq and add 127.0.0.1 to /etc/resolv.conf. The original DNS servers can be found in /run/NetworkManager/no-stub-resolv.conf. You can verify dnsmasq is being used by doing the same DNS lookup twice with drill example.com and verifying the server and query times.

Custom configurations can be created for dnsmasq by creating configuration files in /etc/NetworkManager/dnsmasq.d/. For example, to change the size of the DNS cache (which is stored in RAM):

You can check the configuration file syntax with:

See dnsmasq(8) for all available options.

The factual accuracy of this article or section is disputed.

Enabling dnsmasq in NetworkManager may break IPv6-only DNS lookups (i.e. drill -6 [hostname]) which would otherwise work. In order to resolve this, creating the following file will configure dnsmasq to also listen to the IPv6 loopback:

In addition, dnsmasq also does not prioritize upstream IPv6 DNS. Unfortunately NetworkManager does not do this (Ubuntu Bug). A workaround would be to disable IPv4 DNS in the NetworkManager config, assuming one exists.

The dnsmasq instance started by NetworkManager by default will not validate DNSSEC. To enable DNSSEC validation, thus breaking DNS resolution with name servers that do not support it, create the following configuration file:

This article or section needs expansion.

NetworkManager can use systemd-resolved as a DNS resolver and cache. Make sure that systemd-resolved is properly configured and that systemd-resolved.service is started before using it.

systemd-resolved will be used automatically if /etc/resolv.conf is a symlink to /run/systemd/resolve/stub-resolv.conf, /run/systemd/resolve/resolv.conf or /usr/lib/systemd/resolv.conf.

You can enable it explicitly by setting main.dns=systemd-resolved with a configuration file in /etc/NetworkManager/conf.d/:

If openresolv has a subscriber for your local DNS resolver, set up the subscriber and configure NetworkManager to use openresolv.

Because NetworkManager advertises a single "interface" to resolvconf, it is not possible to implement conditional forwarding between two NetworkManager connections. See NetworkManager issue 153.

This can be partially mitigated if you set private_interfaces="*" in /etc/resolvconf.conf[6]. Any queries for domains that are not in search domain list will not get forwarded. They will be handled according to the local resolver's configuration, for example, forwarded to another DNS server or resolved recursively from the DNS root.

To set DNS servers for all connections, specify them in NetworkManager.conf(5) using the syntax servers=serveripaddress1,serveripaddress2,serveripaddress3 in a section named [global-dns-domain-*]. For example:

Setup will depend on the type of front-end used; the process usually involves right-clicking on the applet, editing (or creating) a profile, and then choosing DHCP type as Automatic (specify addresses). The DNS addresses will need to be entered and are usually in this form: 127.0.0.1, DNS-server-one, ....

To setup DNS Servers per connection, you change the ipv4.dns and ipv6.dns settings (and their associated dns-search and dns-options) in the connection settings.

If method is set to auto (when you use DHCP/RA), you need to set ignore-auto-dns to yes.

To use DNS over TLS (requires systemd-resolved), specify the DNS servers using the syntax dns=ip.address#servername; and additionally set the connection.dns-over-tls setting to 2. For example, to use Quad9:

NetworkManager's /etc/resolv.conf management mode is configured with the main.rc-manager setting. networkmanager sets it to symlink as opposed to the upstream default auto. The setting and its values are documented in the NetworkManager.conf(5) man page.

NetworkManager also offers hooks via so called dispatcher scripts that can be used to alter the /etc/resolv.conf after network changes. See #Network services with NetworkManager dispatcher and NetworkManager(8) for more information.

To stop NetworkManager from touching /etc/resolv.conf, set main.dns=none with a configuration file in /etc/NetworkManager/conf.d/:

After that /etc/resolv.conf might be a broken symlink that you will need to remove. Then, just create a new /etc/resolv.conf file.

To configure NetworkManager to use openresolv, set main.rc-manager=resolvconf with a configuration file in /etc/NetworkManager/conf.d/:

You can assign a firewalld zone based on your current connection. For example a restrictive firewall when at work, and a less restrictive one when at home.

This can also be done with NetworkManager dispatcher.

There are quite a few network services that you will not want running until NetworkManager brings up an interface. NetworkManager has the ability to start services when you connect to a network and stop them when you disconnect (e.g. when using NFS, SMB and NTPd).

To activate the feature you need to enable and start the NetworkManager-dispatcher.service.

Once the service is active, scripts can be added to the /etc/NetworkManager/dispatcher.d directory.

Scripts must be owned by root, otherwise the dispatcher will not execute them. For added security, set group ownership to root as well:

Make sure the file is executable.

The scripts will be run in alphabetical order at connection time, and in reverse alphabetical order at disconnect time. To ensure what order they come up in, it is common to use numerical characters prior to the name of the script (e.g. 10-portmap or 30-netfs (which ensures that the portmapper is up before NFS mounts are attempted).

Scripts will receive the following arguments:

If the above is working, then this section is not relevant. However, there is a general problem related to running dispatcher scripts which take longer to be executed. Initially an internal timeout of three seconds only was used. If the called script did not complete in time, it was killed. Later the timeout was extended to about 20 seconds (see the Bugtracker for more information). If the timeout still creates the problem, a work around may be to use a drop-in file for the NetworkManager-dispatcher.service to remain active after exit:

Now start and enable the modified NetworkManager-dispatcher service.

Create a NetworkManager dispatcher script and make it executable:

Alternatively, the tool tzupdateAUR automatically sets the timezone based on the geolocation of the IP address. This comparison of the most popular IP geolocation apis may be helpful in deciding which API to use in production.

As the script is run in a very restrictive environment, you have to export SSH_AUTH_SOCK in order to connect to your SSH agent. There are different ways to accomplish this, see this message for more information. The example below works with GNOME Keyring, and will ask you for the password if not unlocked already. In case NetworkManager connects automatically on login, it is likely gnome-keyring has not yet started and the export will fail (hence the sleep). The UUID to match can be found with the command nmcli connection status or nmcli connection list.

Some SMB shares are only available on certain networks or locations (e.g. at home). You can use the dispatcher to only mount SMB shares that are present at your current location.

The following script will check if we connected to a specific network and mount shares accordingly:

The following script will unmount all SMB shares before a software initiated disconnect from a specific network:

The following script will attempt to unmount all SMB shares following an unexpected disconnect from a specific network:

An alternative is to use the script as seen in NFS#Using a NetworkManager dispatcher:

Create a symlink inside /etc/NetworkManager/dispatcher.d/pre-down/ to catch the pre-down events:

See NFS#Using a NetworkManager dispatcher.

The idea is to only turn Wi-Fi on when the LAN cable is unplugged (for example when detaching from a laptop dock), and for Wi-Fi to be automatically disabled, once a LAN cable is plugged in again.

Create the following dispatcher script[7], replacing Your_Ethernet_Interface with your ethernet interface's device name.

Remember to make the script executable. You can verify that it works by restarting NetworkManager.service, running ip a, and checking that wlp3s0 (or whatever your Wi-Fi interface is called) is in state DOWN. If you encounter unexpected behavior, check the journal of NetworkManager-dispatcher.service.

In this example we want to connect automatically to a previously defined VPN connection after connecting to a specific Wi-Fi network. First thing to do is to create the dispatcher script that defines what to do after we are connected to the network.

The factual accuracy of this article or section is disputed.

If you would like to attempt to automatically connect to VPN for all Wi-Fi networks, you can use the following definition of the ESSID: ESSID=$(iwgetid -r). Remember to set the script's permissions accordingly.

Trying to connect with the above script may still fail with NetworkManager-dispatcher.service complaining about 'no valid VPN secrets', because of the way VPN secrets are stored. Fortunately, there are different options to give the above script access to your VPN password.

1: One of them requires editing the VPN connection configuration file to make NetworkManager store the secrets by itself rather than inside a keyring that will be inaccessible for root: open up /etc/NetworkManager/system-connections/name of your VPN connection.nmconnection and change the password-flags and secret-flags from 1 to 0.

If that alone does not work, you may have to create a passwd-file in a safe location with the same permissions and ownership as the dispatcher script, containing the following:

The script must be changed accordingly, so that it gets the password from the file:

2: Alternatively, change the password-flags and put the password directly in the configuration file adding the section vpn-secrets:

Many commercial VPN providers support only IPv4. That means all IPv6 traffic bypasses the VPN and renders it virtually useless. To avoid this, dispatcher can be used to disable all IPv6 traffic for the time a VPN connection is up.

As an alternative, dispatcher can be used to temporarily set the IPv6 mode of the device used by the VPN connection to link-local. This will avoid NetworkManager log spam about IPv6 being disabled. This script will not work if multiple devices or connections provide IPv6 connectivity, but could be adapted to iterate over multiple devices. Note that any change to the connection (using nmcli(1) or a desktop environment) will reapply the entire connection to the device and re-enable IPv6 (if it is enabled in the connection).

See OpenNTPD#Using NetworkManager dispatcher.

When roaming between different networks (e.g. a company's LAN, Wi-Fi at home, various other Wi-Fi now and then) you might want to set the NTP server(s) used by timesyncd to those provided by DHCP. However, NetworkManager itself is not capable to communicate with systemd-timesyncd to set the NTP server(s).

The dispatcher can work around it.

Create the overlay directory for your systemd-timesyncd configuration /etc/systemd/timesyncd.conf.d if it does not already exist. Inside /etc/NetworkManager/dispatcher.d, put the following:

Every time NetworkManager sets up a new network connection (ACTION=up) or gets some update for an existing connection (ACTION=dhcp4-change or ACTION=dhcp6-change) and the provided connection data contains information about NTP server(s) (DHCP4_NTP_SERVERS), a connection specific overlay configuration file is written to /etc/systemd/timesyncd.conf.d, containing the provided NTP server(s). Whenever a connection is taken down (ACTION=down) the connection specific overlay file is removed. After each change to the configuration of systemd-timesyncd, this service is restarted to pick up the updated configuration. The use of connection specific configuration files is intentional so that when two or more connections are managed by NetworkManager in parallel the different NTP server names in the configuration are not overwritten as up, dhcp4-change, dhcp6-change and down actions might come in an arbitrary order.

NetworkManager applets are designed to load upon login so no further configuration should be necessary for most users. If you have already disabled your previous network settings and disconnected from your network, you can now test if NetworkManager will work. The first step is to start NetworkManager.service.

Some applets will provide you with a .desktop file so that the NetworkManager applet can be loaded through the application menu. If it does not, you are going to either have to discover the command to use or logout and login again to start the applet. Once the applet is started, it will likely begin polling network connections with for auto-configuration with a DHCP server.

To start the GNOME applet in non-xdg-compliant window managers like awesome:

For static IP addresses, you will have to configure NetworkManager to understand them. The process usually involves right-clicking the applet and selecting something like 'Edit Connections'.

By default, NetworkManager stores passwords in clear text in the connection files at /etc/NetworkManager/system-connections/. To print the stored passwords, use the following command:

The passwords are accessible to the root user in the filesystem and to users with access to settings via the GUI (e.g. nm-applet).

It is preferable to save the passwords in encrypted form in a keyring instead of clear text. The downside to this is that the connections have to be set up for each user.

In order to read and write to the keyring, there must be a secret agent available. This can be one of:

If you make neither of these available, then authentication will fail with the error no secrets: No agents were available for this request.

The keyring daemon has to be started and the keyring needs to be unlocked for the following to work.

Furthermore, NetworkManager needs to be configured not to store the password for all users. Using GNOME's network-manager-applet, run nm-connection-editor from a terminal, select a network connection, click Edit, select the Wi-Fi Security tab and click on the right icon of password and check Store the password only for this user.

Using KDE's plasma-nm, click the applet, click on the top right Settings icon, click on a network connection, in the General configuration tab, untick All users may connect to this network. If the option is ticked, the passwords will still be stored in clear text, even if a keyring daemon is running.

If the option was selected previously and you un-tick it, you may have to use the reset option first to make the password disappear from the file. Alternatively, delete the connection first and set it up again.

You can share your internet connection (e.g. 3G or wired) with a few clicks. Please note that a firewall may interfere with internet sharing.

You will need a Wi-Fi card which supports AP mode, see Software access point#Wi-Fi device must support AP mode for details.

Install the dnsmasq package to be able to actually share the connection. Note that NetworkManager starts its own instance of dnsmasq, independent of dnsmasq.service, as a DHCP server. See #dnsmasq for the caveats.

Create the shared connection:

The connection will be saved and remain stored for the next time you need it.

Scenario: your device has internet connection over Wi-Fi and you want to share the internet connection to other devices over Ethernet.

Now you should have a new option "Shared Internet" under the Wired connections in NetworkManager.

This article or section is out of date.

Some cron jobs require networking to be up to succeed. You may wish to avoid running these jobs when the network is down. To accomplish this, add an if test for networking that queries NetworkManager's nm-tool and checks the state of networking. The test shown here succeeds if any interface is up, and fails if they are all down. This is convenient for laptops that might be hardwired, might be on wireless, or might be off the network.

This is useful for a cron.hourly script that runs fpupdate for the F-Prot virus scanner signature update, as an example. Another way it might be useful, with a little modification, is to differentiate between networks using various parts of the output from nm-tool; for example, since the active wireless network is denoted with an asterisk, you could grep for the network name and then grep for a literal asterisk.

By default, NetworkManager will not connect to networks requiring a secret automatically on boot. This is because it locks such connections to the user who makes it by default, only connecting after they have logged in. To change this, do the following:

Log out and log back in to complete.

While you may type both values at connection time, plasma-nm 0.9.3.2-1 and above are capable of retrieving OpenConnect username and password directly from KWallet.

Open "KDE Wallet Manager" and look up your OpenConnect VPN connection under "Network Management|Maps". Click "Show values" and enter your credentials in key "VpnSecrets" in this form (replace username and password accordingly):

Next time you connect, username and password should appear in the "VPN secrets" dialog box.

Sometimes it may be desired that NetworkManager ignores specific devices and does not try to configure addresses and routes for them. You can quickly and easily ignore devices by MAC or interface-name by using the following in /etc/NetworkManager/conf.d/unmanaged.conf:

After editing the file, run nmcli general reload as root. Afterwards you should be able to configure interfaces without NetworkManager altering what you have set.

This article or section is a candidate for merging with NetworkManager/Privacy#MAC Randomization.

MAC randomization can be used for increased privacy by not disclosing your real MAC address to the network.

NetworkManager supports two types MAC Address Randomization: randomization during scanning, and for network connections. Both modes can be configured by modifying /etc/NetworkManager/NetworkManager.conf or by creating a separate configuration file in /etc/NetworkManager/conf.d/ which is recommended since the aforementioned configuration file may be overwritten by NetworkManager.

Randomization during Wi-Fi scanning is enabled by default, but it may be disabled by adding the following lines to /etc/NetworkManager/NetworkManager.conf or a dedicated configuration file under /etc/NetworkManager/conf.d:

MAC randomization for network connections can be set to different modes for both wireless and ethernet interfaces. See the GNOME blog post for more details on the different modes.

In terms of MAC randomization the most important modes are stable and random. stable generates a random MAC address when you connect to a new network and associates the two permanently. This means that you will use the same MAC address every time you connect to that network. In contrast, random will generate a new MAC address every time you connect to a network, new or previously known. You can configure the MAC randomization by adding the desired configuration under /etc/NetworkManager/conf.d:

To configure MAC randomization for a specific connection (for example, if the network does not like random MAC addresses), edit the connection to set 802-11-wireless.cloned-mac-address to one of the modes (e.g. stable or random).

See the following GNOME blog post for more details.

See IPv6#NetworkManager.

The DHCPv6 Unique Identifier (DUID) is a value used by the DHCPv6 client to identify itself to DHCPv6 servers. NetworkManager supports 3 types of DUID:

If the internal NetworkManager's DHCP client is in use (the default) it will identify itself with a global and permanent DUID-UUID generated from the machine-id (/etc/machine-id). This means that all connections share the same UUID, which may be a privacy breach.

Fortunately, NetworkManager is able to provide unique DUIDs per connection, derived from the connection's stable-id and a per-host unique key. You can enable that by adding the following configuration under /etc/NetworkManager/conf.d:

The stable-ll and stable-llt values are also supported. For further information read the description for dhcp-duid in nm-settings(5) § ipv6 setting.

By default, NetworkManager generates a connection profile for each wired ethernet connection it finds. At the point when generating the connection, it does not know whether there will be more Ethernet adapters available. Hence, it calls the first wired connection "Wired connection 1". You can avoid generating this connection, by configuring no-auto-default (see NetworkManager.conf(5)), or by simply deleting it. Then NetworkManager will remember not to generate a connection for this interface again.

You can also edit the connection (and persist it to disk) or delete it. NetworkManager will not re-generate a new connection. Then you can change the name to whatever you want. You can use something like nm-connection-editor for this task.

To enable the experimental iwd backend, first install iwd and then create the following configuration file:

Alternatively, you can install networkmanager-iwdAUR, a modified package configured to build NetworkManager working exclusively with iwd, with the main difference being that iwd is required and wpa_supplicant can be uninstalled after building.

If you would like to run NetworkManager inside a network namespace (e.g., to manage a specific device which should be used by selected applications), bring the device down before moving it to the namespace:

otherwise NetworkManager will later fail to establish the connection with a device is strictly unmanaged error.

NetworkManager can be set to automatically connect to a VPN when connecting to the internet, on a per network basis. The VPN connection itself can be added in GNOME's NetworkManager front-end, but to make it automatically use the VPN nmcli must be used. Other front-ends might not have this limitation.

First, make sure to make the VPN connection available to all users. In the GNOME this is a matter of checking a box under the details tab. Under the Identity tab, in the password field, click the icon on the right side in the field, and set it to Store the password for all users.

Then find the UUID of the VPN connection, and add that to connection.secondaries of the Internet connection:

Now when NetworkManager is restarted and you connect to the Internet connection you have configured, you should automatically get connected to the VPN.

When trying to connect to a secured Wi-Fi network, no prompt for a password is shown and no connection is established. This happens when no keyring package is installed. An easy solution is to install gnome-keyring. If you want the passwords to be stored in encrypted form, follow GNOME Keyring to set up the gnome-keyring-daemon.

When NetworkManager shuts down but the pid (state) file is not removed, you will see a Network management disabled message. If this happens, remove the file manually:

If you have problems with getting an IP address using the internal DHCP client, consider using another DHCP client, see #DHCP client for instructions. This workaround might solve problems in big wireless networks like eduroam.

If you have problems with getting an IP address via DHCP, try to add the following to your /etc/dhclient.conf:

Where aa:bb:cc:dd:ee:ff is the MAC address of this NIC. The MAC address can be found using the ip link show interface command from the iproute2 package.

See Mobile broadband modem#NetworkManager.

Sometimes NetworkManager will not work when you disable your Wi-Fi adapter with a switch on your laptop and try to enable it again afterwards. This is often a problem with rfkill. To check if the driver notifies rfkill about the wireless adapter's status, use:

If one identifier stays blocked after you switch on the adapter you could try to manually unblock it with (where X is the number of the identifier provided by the above output):

This article or section is out of date.

Due to an unresolved bug, when changing default connections to a static IP address, nm-applet may not properly store the configuration change, and will revert to automatic DHCP.

To work around this issue you have to edit the default connection (e.g. "Auto eth0") in nm-applet, change the connection name (e.g. "my eth0"), uncheck the "Available to all users" checkbox, change your static IP address settings as desired, and click Apply. This will save a new connection with the given name.

Next, you will want to make the default connection not connect automatically. To do so, run nm-connection-editor (not as root). In the connection editor, edit the default connection (e.g. "Auto eth0") and uncheck "Connect automatically". Click Apply and close the connection editor.

See #Set up PolicyKit permissions.

Since hidden networks are not displayed in the selection list of the Wireless view, they cannot be forgotten (removed) with the GUI. You can delete one with the following command:

This also works for any other connection.

When setting up OpenConnect or vpnc connections in NetworkManager while using GNOME, you will sometimes never see the dialog box pop up and the following error appears in /var/log/errors.log:

This is caused by the GNOME NetworkManager Applet expecting dialog scripts to be at /usr/lib/gnome-shell, when NetworkManager's packages put them in /usr/lib/networkmanager. As a "temporary" fix (this bug has been around for a while now), make the following symlink(s):

This may need to be done for any other NetworkManager VPN plugins as well, but these are the two most common.

WLAN chips are shipped with a default regulatory domain. If your access point does not operate within these limitations, you will not be able to connect to the network. Fixing this is easy:

The problem occurs when the system (i.e. NetworkManager running as the root user) tries to establish a VPN connection, but the password is not accessible because it is stored in the GNOME Keyring of a particular user.

A solution is to keep the password to your VPN in plaintext, as described in step (2.) of #Use dispatcher to connect to a VPN after a network connection is established.

You do not need to use the dispatcher described in step (1.) to auto-connect anymore, if you use the new "auto-connect VPN" option from the nm-applet GUI.

Over time the log files (/var/log/journal) can become very large. This can have a big impact on boot performance when using NetworkManager, see: systemd#Boot time increasing over time.

NetworkManager does a scan every 2 minutes.

Some Wi-Fi drivers have issues when scanning for base stations whilst connected/associated. Symptoms include VPN disconnects/reconnects and lost packets, web pages failing to load and then refresh fine.

Running journalctl -f as root will indicate that this is taking place, messages like the following will be contained in the logs at regular intervals.

If roaming is not important, the periodic scanning behavior can be disabled by locking the BSSID of the access point in the Wi-Fi connection profile.

There is an issue with the ideapad_laptop module on some Lenovo models due to the Wi-Fi driver incorrectly reporting a soft block. The card can still be manipulated with netctl, but managers like NetworkManager break. You can verify that this is the problem by checking the output of rfkill list after toggling your hardware switch and seeing that the soft block persists.

The factual accuracy of this article or section is disputed.

Unloading the ideapad_laptop module should fix this. (warning: this may disable the laptop keyboard and touchpad also!).

NetworkManager by default sends the hostname to the DHCP server.

To disable sending your hostname to the DHCP server globally, set the ipv4.dhcp-send-hostname=0 and ipv6.dhcp-send-hostname=0 options with a configuration file in /etc/NetworkManager/conf.d/. E.g.:

To disable sending your hostname to the DHCP server for a specific connection (or alternatively, enable it for a connection if it is disabled globally), add the following to your network connection file:

If you use the xfce4-notifyd.service for notifications you must edit the unit and add the following:

After reloading the daemons restart xfce4-notifyd.service. Exit i3 and start it back up again and the applet should show on the tray.

If systemd-resolved.service is not started, NetworkManager will try to start it using D-Bus and fail:

This is because NetworkManager will try to send DNS information to systemd-resolved regardless of the main.dns= setting in NetworkManager.conf(5).[10]

This can be disabled with a configuration file in /etc/NetworkManager/conf.d/:

If you received the following error when attempting to connect to a network:

This error can have numerous causes and you should read the journal (filter it with -u NetworkManager). For example, if NetworkManager took too long to establish connection, it will believe that the password is incorrect:

You can try deleting the connection profile and creating a new one:

You can also try disabling MAC address randomization:

If you try to connect to an WPA Enterprise network like 'eduroam' with NetworkManager with the iwd backend then you will get the following error from NetworkManager:

This is because NetworkManager can not configure a WPA Enterprise network. Therefore you have to configure it using an iwd configuration file /var/lib/iwd/essid.8021x like described in iwd#WPA Enterprise.

If you get this error:

It is either because the password is empty or you have to set up PolicyKit permissions.

This article or section is being considered for removal.

The package networkmanager-openvpn requires libnma-gtk4 and optionally libnma (Gtk3) when integrated within the GNOME-Shell. If libnma is required but not installed a message will be printed to the system log:

Since openssl was updated to version 3, certificates generated with legacy cryptographic algorithms are rejected by default. Attempting to use networkmanager-openvpn with such a setup can result in the following error in the logs:

The correct approach is to have the OpenVPN server administrator generate and re-issue more secure certificates. However, as an immediate work-around, OpenVPN requires tls-cipher "DEFAULT:@SECLEVEL=0". This may not be possible through the plugin GUI, but it is possible with nmcli. Separately, you will also need to enable the legacy provider in OpenSSL.

Firstly, obtain the name of the VPN connection with the issue, from the output of the following:

Assuming the connection name is vpn.example.com, use nmcli like so:

The change should instantly be reflected in /etc/NetworkManager/system-connections/vpn.example.com.nmconnection.

As for OpenSSL, edit /etc/ssl/openssl.cnf as described on the OpenSSL wiki.

Specifically, at the end of the [provider_sect] section add legacy = legacy_sect. Under [default_sect] uncomment activate = 1. Lastly, add a new section [legacy_sect] that also contains the line activate = 1. Excluding most other preexisting configuration sections, the end result will look something like:

Finally, restart the NetworkManager.service to have the new OpenSSL configuration take effect.

Since openssl was updated to version 3, "SSL 3, TLS 1.0, TLS 1.1, and DTLS 1.0 only work at security level 0" by default. Attempting to authenticate to a Wi-Fi network only supporting older standards results in the following error in the logs:

The correct approach is to convince the institution's administrator to upgrade the encrypted networking tunnel protocol to TLS 1.3 and optionally drop support for deprecated security standards, including TLS 1.0/1.1, DTLS 1.0 and SSL 1-3. However, as an immediate workaround, there are multiple ways to allow TLS 1.0 and/or 1.1 by default. One way would be to manually patch or revert the breaking changes in OpenSSL ([11]). As this also lowers security for all other programs using OpenSSL level 1, it is not recommended. Instead, one can directly set the level used by wpa_supplicant, like described in BBS#286417. To only change the affected connection, it is possible to set phase1-auth-flags=32 or phase1-auth-flags=64 in the [802-1x] section of the connection's configuration file. This may not be possible through GUIs, but it is possible with nmcli.

Firstly, obtain the name of the Wi-Fi connection with the issue, from the output of the following:

Assuming the connection uses TLS 1.0 and its name is Example Wi-Fi, use nmcli like so:

And for a TLS 1.1 connection, type "64" instead:

The change should instantly be reflected in /etc/NetworkManager/system-connections/Example Wi-Fi.nmconnection.

Finally, restart the NetworkManager.service to have the new OpenSSL configuration take effect.

**Examples:**

Example 1 (unknown):
```unknown
NetworkManager.service
```

Example 2 (unknown):
```unknown
systemctl --type=service
```

Example 3 (unknown):
```unknown
ModemManager.service
```

Example 4 (unknown):
```unknown
NetworkManager.service
```

---

## Simple stateful firewall

**URL:** https://wiki.archlinux.org/title/Simple_stateful_firewall

**Contents:**
- Prerequisites
- Firewall for a single machine
  - Creating necessary chains
  - The FORWARD chain
  - The OUTPUT chain
  - The INPUT chain
  - Resulting iptables.rules file
  - The TCP and UDP chains
    - Opening ports to incoming connections
    - Port knocking

This page explains how to set up a stateful firewall using iptables. It also explains what the rules mean and why they are needed. For simplicity, it is split into two major sections. The first section deals with a firewall for a single machine, the second sets up a NAT gateway in addition to the firewall from the first section.

First, install the userland utilities iptables or verify that they are already installed.

This article assumes that there are currently no iptables rules set. To check the current ruleset and verify that there are currently no rules run the following:

If there are rules, you may be able to reset the rules by loading a default rule set:

Otherwise, see Iptables#Resetting rules.

For this basic setup, we will create two user-defined chains that we will use to open up ports in the firewall.

The chains can of course have arbitrary names. We pick these just to match the protocols we want handle with them in the later rules, which are specified with the protocol options, e.g. -p tcp, always.

If you want to set up your machine as a NAT gateway, please look at #Setting up a NAT gateway. For a single machine, however, we simply set the policy of the FORWARD chain to DROP and move on:

The OUTPUT chain can be a powerful tool for filtering outbound traffic, especially for servers and other devices which do not run web browsers or peer-to-peer tools that need to connect to arbitrary destinations on the internet. However, properly setting up an OUTPUT chain requires information about the intended use of the system. A secure set of rules for a desktop system, laptop system, cloud server and home/on-prem server would all be very different.

In this simple example, we will allow all outbound traffic by setting the default policy for the OUTPUT chain to ACCEPT. This is less secure, but is highly compatible with many systems.

Similar to the previous chains, we set the default policy for the INPUT chain to DROP in case something somehow slips by our rules. Dropping all traffic and specifying what is allowed is the best way to make a secure firewall.

Every packet that is received by any network interface will pass the INPUT chain first, if it is destined for this machine. In this chain, we make sure that only the packets that we want are accepted. For a simplified ASCII art showing how packets traverse those builtin chains, see How Packets Traverse The Filters.

The first rule added to the INPUT chain will allow traffic that belongs to established connections, or new valid traffic that is related to these connections such as ICMP errors, or echo replies (the packets a host returns when pinged). ICMP stands for Internet Control Message Protocol. Some ICMP messages are very important and help to manage congestion and MTU, and are accepted by this rule:

The connection state ESTABLISHED implies that either another rule previously allowed the initial (--ctstate NEW) connection attempt or the connection was already active (for example an active remote SSH connection).

The second rule will accept all traffic from the "loopback" (lo) interface, which is necessary for many applications and services.

The third rule will drop all traffic with an "INVALID" state match. Traffic can fall into four "state" categories: NEW, ESTABLISHED, RELATED or INVALID and this is what makes this a "stateful" firewall rather than a less secure "stateless" one. States are tracked using the "nf_conntrack_*" kernel modules which are loaded automatically by the kernel as you add rules.

The next rule will accept all new incoming ICMP echo requests, also known as pings. Only the first packet will count as NEW, the others will be handled by the RELATED, ESTABLISHED rule. Since the computer is not a router, no other ICMP traffic with state NEW needs to be allowed.

Now we attach the TCP and UDP chains to the INPUT chain to handle all new incoming connections. Once a connection is accepted by either TCP or UDP chain, it is handled by the RELATED/ESTABLISHED traffic rule. The TCP and UDP chains will either accept new incoming connections, or politely reject them. New TCP connections must be started with SYN packets.

We reject TCP connections with TCP RESET packets and UDP streams with ICMP port unreachable messages if the ports are not opened. This imitates default Linux behavior (RFC compliant), and it allows the sender to quickly close the connection and clean up.

For other protocols, we add a final rule to the INPUT chain to reject all remaining incoming traffic with icmp protocol unreachable messages. This imitates Linux's default behavior.

Example of iptables.rules file after running all the commands from above:

This file can be generated and saved with:

and can be used to continue with the following sections. If you are setting up the firewall remotely via SSH, append the following rule to allow new SSH connections before continuing (adjust port as required):

The TCP and UDP chains contain rules for accepting new incoming TCP connections and UDP streams to specific ports.

To accept incoming TCP connections on port 80 for a web server:

To accept incoming TCP connections on port 443 for a web server (HTTPS):

To allow remote SSH connections (on port 22):

To accept incoming TCP/UDP requests for a DNS server (port 53):

See iptables(8) for more advanced rules, like matching multiple ports.

Port knocking is a method to externally open ports that, by default, the firewall keeps closed. It works by requiring connection attempts to a series of predefined closed ports. When the correct sequence of port "knocks" (connection attempts) is received, the firewall opens certain port(s) to allow a connection. See Port knocking for more information.

Blocking reserved local addresses incoming from the internet or local network is normally done through setting rp_filter (Reverse Path Filter) in sysctl to 1. To do so, add the following line to your /etc/sysctl.d/90-firewall.conf file (see sysctl for details) to enable source address verification which is built into Linux kernel itself. The verification by the kernel will handle spoofing better than individual iptables rules for each case.

This can be done with netfilter instead if statistics (and better logging) are desired:

For niche setups where asymmetric routing is used, the rp_filter=2 sysctl option needs to be used instead. Passing the --loose switch to the rpfilter module will accomplish the same thing with netfilter.

If you are running a desktop machine, it might be a good idea to block some incoming requests.

A 'Ping' request is an ICMP packet sent to the destination address to ensure connectivity between the devices. If your network works well, you can safely block all ping requests. It is important to note that this does not actually hide your computer — any packet sent to you is rejected, so you will still show up in a simple nmap "ping scan" of an IP range.

This is rudimentary "protection" and makes life difficult when debugging issues in the future. This should only be done for educational purposes.

To block echo requests, add the following line to your /etc/sysctl.d/90-firewall.conf file (see sysctl for details):

More information in iptables(8), or reading the docs and examples on the webpage http://www.snowman.net/projects/ipt_recent/

Port scans are used by attackers to identify open ports on your computer. This allows them to identify and fingerprint your running services and possibly launch exploits against them.

The INVALID state rule will take care of every type of port scan except UDP, ACK and SYN scans (-sU, -sA and -sS in nmap respectively).

ACK scans are not used to identify open ports, but to identify ports filtered by a firewall. Due to the SYN check for all TCP connections with the state NEW, every single packet sent by an ACK scan will be correctly rejected by a TCP RESET packet. Some firewalls drop these packets instead, and this allows an attacker to map out the firewall rules.

The recent module can be used to trick the remaining two types of port scans. The recent module is used to add hosts to a "recent" list which can be used to fingerprint and stop certain types of attacks. Current recent lists can be viewed in /proc/net/xt_recent/.

In a SYN scan, the port scanner sends a SYN (synchronization) packet to every port to initiate a TCP connection. Closed ports return a TCP RESET packet, or get dropped by a strict firewall, while open ports return a SYN ACK packet.

The recent module can be used to keep track of hosts with rejected connection attempts and return a TCP RESET for any SYN packet they send to open ports as if the port was closed. If an open port is the first to be scanned, a SYN ACK will still be returned, so running applications such as ssh on non-standard ports is required for this to work consistently.

First, insert a rule at the top of the TCP chain. This rule responds with a TCP RESET to any host that got onto the TCP-PORTSCAN list in the past sixty seconds. The --update switch causes the recent list to be updated, meaning the 60 second counter is reset.

Next, the rule for rejecting TCP packets need to be modified to add hosts with rejected packets to the TCP-PORTSCAN list.

UDP port scans are similar to TCP SYN scans except that UDP is a "connectionless" protocol. There are no handshakes or acknowledgements. Instead, the scanner sends UDP packets to each UDP port. Closed ports should return ICMP port unreachable messages, and open ports do not return a response. Since UDP is not a "reliable" protocol, the scanner has no way of knowing if packets were lost, and has to do multiple checks for each port that does not return a response.

The Linux kernel sends out ICMP port unreachable messages very slowly, so a full UDP scan against a Linux machine would take over 10 hours. However, common ports could still be identified, so applying the same countermeasures against UDP scans as SYN scans is a good idea.

First, add a rule to reject packets from hosts on the UDP-PORTSCAN list to the top of the UDP chain.

Next, modify the reject packets rule for UDP:

If either or both of the portscanning tricks above were used, the final default rule is no longer the last rule in the INPUT chain. It needs to be the last rule, or it would intercept the trick port scanner rules you just added, rendering them useless. Simply delete (-D) the rule, then add it again using append (-A), which will place it at the end of the chain.

See the sysctl#TCP/IP stack hardening for relevant kernel parameters.

Unfortunately, bruteforce attacks on services accessible via an external IP address are common. One reason for this is that the attacks are easy to perform with the many tools available. Fortunately, there are a number of ways to protect the services against them. One is the use of appropriate iptables rules which activate and blacklist an IP after a set number of packets attempt to initiate a connection. Another is the use of specialised daemons that monitor the logfiles for failed attempts and blacklist accordingly.

Two packages that ban IPs after too many password failures are Fail2ban or, for sshd in particular, Sshguard. These two applications update iptables rules to reject temporarily or permanently future connections from attackers.

The following rules give an example configuration to mitigate SSH bruteforce attacks using iptables.

Most of the rules should be self-explanatory: the first one allows for a maximum of three connection packets in ten seconds and drops further attempts from this IP. The next rule adds a quirk by allowing a maximum of four hits in 30 minutes. This is done because some bruteforce attacks are actually performed slow and not in a burst of attempts. The rules employ a number of additional options. To read more about them, check the original reference for this example in compilefailure.blogspot.com. The LOG_AND_DROP chain is used for logging dropped connections.

The above rules can be used to protect any service, though the SSH daemon is probably the most often required one.

In terms of order, one must ensure that -A INPUT -p tcp --dport ssh -m conntrack --ctstate NEW -j IN_SSH is at the right position in the iptables sequence: it should come before the TCP chain is attached to INPUT in order to catch new SSH connections first. If all the previous steps of this wiki have been completed, the following positioning works:

If you do not use IPv6, you can consider disabling it, otherwise follow these steps to enable the IPv6 firewall rules.

Copy the IPv4 rules used in this example as a base, and change any IPs from IPv4 format to IPv6 format:

A few of the rules in this example have to be adapted for use with IPv6. The ICMP protocol has been updated in IPv6, replacing the ICMP protocol for use with IPv4. Hence, the reject error return codes --reject-with icmp-port-unreachable and --reject-with icmp-proto-unreachable have to be converted to ICMPv6 codes.

The available ICMPv6 error codes are listed in RFC 4443, which specifies that connection attempts blocked by a firewall rule should use --reject-with icmp6-adm-prohibited. Doing so will basically inform the remote system that the connection was rejected by a firewall, rather than a listening service.

If it is preferred not to explicitly inform about the existence of a firewall filter, the packet may also be rejected without the message:

The above will reject with the default return error of --reject-with icmp6-port-unreachable. You should note though, that identifying a firewall is a basic feature of port scanning applications and most will identify it regardless.

This article or section needs expansion.

In the next step make sure the protocol and extension are changed to be IPv6 appropriate for the rule regarding all new incoming ICMP echo requests (pings):

Netfilter conntrack does not appear to track ICMPv6 Neighbor Discovery Protocol (the IPv6 equivalent of ARP), so we need to allow ICMPv6 traffic regardless of state for all directly attached subnets. The following should be inserted after dropping --ctstate INVALID, but before any other DROP or REJECT targets, along with a corresponding line for each directly attached subnet:

If you want to enable DHCPv6, you need to accept incoming connections on UDP port 546:

Since there is no kernel reverse path filter for IPv6, you may want to enable one in ip6tables with the following:

The rule sets are now finished and should be saved to a file so that they can be loaded on every boot.

Save the IPv4 and IPv6 rules with these commands:

Example of ip6tables.rules file after running all the commands from above:

Then enable and start iptables.service and the ip6tables.service. Check the status of the services to make sure the rules are loaded correctly.

This section of the guide deals with NAT gateways. It is assumed that you already read the first part of the guide and set up the INPUT, OUTPUT, TCP and UDP chains like described above. All rules so far have been created in the filter table. In this section, we will also have to use the nat table. There is an ASCII art of the situation at Controlling What To NAT.

In our setup, we will create two new chains in the filter table, fw-interfaces and fw-open, using the following commands:

Setting up the FORWARD chain is similar to the INPUT chain in the first section.

Now we set up a rule with the conntrack match, identical to the one in the INPUT chain:

The next step is to enable forwarding for trusted interfaces and to make all packets pass the fw-open chain.

The remaining packets are denied with an ICMP message:

The meaning of the fw-interfaces and fw-open chains is explained later, when we deal with the POSTROUTING and PREROUTING chains in the nat table, respectively.

All over this section, we assume that the outgoing interface (the one with the public internet IP) is ppp0. Keep in mind that you have to change the name in all following rules if your outgoing interface has another name.

Now, we have to define who is allowed to connect to the internet. Let us assume we have the subnet 192.168.0.0/24 (which means all addresses that are of the form 192.168.0.*) on eth0. We first need to accept the machines on this interface in the FORWARD table, that is why we created the fw-interfaces chain above:

Now, we have to alter all outgoing packets so that they have our public IP address as the source address, instead of the local LAN address. To do this, we use the MASQUERADE target:

Do not forget the -o ppp0 parameter above. If you omit it, your network will be screwed up.

Let us assume we have another subnet, 10.3.0.0/16 (which means all addresses 10.3.*.*), on the interface eth1. We add the same rules as above again:

The last step is to enable packet forwarding (if it is not already enabled).

Machines from these subnets can now use your new NAT machine as their gateway. Note that you may want to set up a DNS and DHCP server to simplify network settings on the client machines. This is not the topic of this guide.

Sometimes, we want to change the address of an incoming packet from the gateway to a LAN machine. To do this, we use the fw-open chain defined above, as well as the PREROUTING chain in the nat table in the following two simple examples.

First, we want to change all incoming SSH packets (port 22) to the ssh server of the machine 192.168.0.5:

The second example will show you how to change packets to a different port than the incoming port. We want to change any incoming connection on port 8000 to our web server on 192.168.0.6, port 80:

The same setup also works with udp packets.

This assumes that you have followed the steps above to enable the iptables systemd service.

**Examples:**

Example 1 (unknown):
```unknown
# iptables-save
```

Example 2 (unknown):
```unknown
# Generated by iptables-save v1.4.19.1 on Thu Aug  1 19:28:53 2013
*filter
:INPUT ACCEPT [50:3763]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [30:3472]
COMMIT
# Completed on Thu Aug  1 19:28:53 2013
```

Example 3 (unknown):
```unknown
# iptables -nvL --line-numbers
```

Example 4 (unknown):
```unknown
Chain INPUT (policy ACCEPT 156 packets, 12541 bytes)
num   pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
num   pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 82 packets, 8672 bytes)
num   pkts bytes target     prot opt in     out     source               destination
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Network_management

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## DNSSEC

**URL:** https://wiki.archlinux.org/title/DNSSEC

**Contents:**
- Install a DNSSEC-validating resolver
  - Test the local validating resolver
    - From a terminal
    - From a web browser
- Recursive query with DNSSEC validation
- Enable DNSSEC in specific software
- See also

This article or section needs expansion.

From the DNSSEC Wikipedia article:

To ensure DNSSEC is validated system-wide, setup a local DNS server that validates DNSSEC records and configure resolv.conf(5) to use it so that all DNS lookups go through it. See Domain name resolution#DNS servers for available validating resolvers. Note that some DNS servers require specific options to enable DNSSEC validation.

If you attempt to visit a site with a bogus (spoofed) IP address, the validating resolver will prevent you from receiving the invalid DNS data and your browser (or other application) will be told there is no such host. Since all DNS lookups go through the validating resolver, you do not need software that has DNSSEC support built-in when using this option.

To test if your local resolver properly validates DNSSEC, use a DNS lookup utility that supports setting the DO ("DNSSEC OK") bit, such as drill(1).

Test if the resolver does not return an answer for a domain with an invalid signature such as badsig.test.dnscheck.tools, rhybar.cz or dnssec-failed.org:

The return code should be SERVFAIL (server failure), the answer section should be empty and flags should not contain ad (authenticated data).

Next, test a domain with a valid signature:

The query should return successfully and contain the ad (authenticated data) flag.

Multiple websites provide tests that check if your DNS resolver validates DNSSEC:

To validate DNSSEC for a domain without involving a recursive resolver, use a DNS lookup utility that can trace a domain starting from a the DNS root. E.g. drill(1) (from ldns) or dig(1) (from bind).

With drill, use the -D option to set the DO (DNSSEC OK) bit and the -T option to trace from the root name servers down to the domain being resolved:

Replace example.com with a domain name for which you want to preform DNSSEC validation.

For a domain with an invalid DNSSEC signature, the result should end with the following lines:

For a domain with a trusted signature, the result should end with the following lines:

This article or section is being considered for removal.

If you choose not to #Install a DNSSEC-validating resolver, you need to use software that has DNSSEC support builtin. Often this means you must patch the software yourself. Hopefully, a full list of several patched applications will eventually (Dec 2020) be found at [1]. Additionally, some web browsers, some of them mentioned at [2], have extensions or add-ons that can be installed to implement DNSSEC without patching the program.

**Examples:**

Example 1 (unknown):
```unknown
$ drill -D badsig.test.dnscheck.tools
```

Example 2 (unknown):
```unknown
;; ->>HEADER<<- opcode: QUERY, rcode: SERVFAIL, id: 5610
;; flags: qr rd ra ; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; badsig.test.dnscheck.tools.    IN      A

;; ANSWER SECTION:

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 44 msec
;; EDNS: version 0; flags: do ; udp: 1232
; EDE: 6 (DNSSEC Bogus): 49 37 34 56 (I74V)
;; SERVER: 127.0.0.1
...
```

Example 3 (unknown):
```unknown
$ drill -D test.dnscheck.tools
```

Example 4 (unknown):
```unknown
;; ->>HEADER<<- opcode: QUERY, rcode: NOERROR, id: 20952
;; flags: qr rd ra ad ; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; QUESTION SECTION:
;; test.dnscheck.tools.   IN      A

;; ANSWER SECTION:
test.dnscheck.tools.      5       IN      A       116.203.95.251
...

;; AUTHORITY SECTION:

;; ADDITIONAL SECTION:

;; Query time: 45 msec
;; EDNS: version 0; flags: do ; udp: 1232
;; SERVER: 127.0.0.1
...
```

---

## PowerDNS

**URL:** https://wiki.archlinux.org/title/PowerDNS

**Contents:**
- Installation
- Backends
  - PostgreSQL backend
  - MySQL backend
  - SQLite backend
- Startup
- Zone Management
- DNSSEC
- Tips and Tricks
  - Bind address and/or port

PowerDNS is a DNS server, written in C++ and licensed under the GPL. PowerDNS features a large number of different backends ranging from simple BIND style zonefiles to relational databases and load balancing/failover algorithms.

Install the powerdns package.

Next you can review the configuration file located at /etc/powerdns/pdns.conf.

To configure PowerDNS to use specific backend you will need to set the launch option in configuration file. Also depending on particular backend you use, you will have to configure it.

For PostgreSQL, MySQL and SQLite you can find database table creation SQL files located at /usr/share/doc/powerdns.

Firstly you will need to create a user and database where PowerDNS can store data, then import the schema:

And finally update configuration file to use the backend:

Install and run a MySQL server. Create a new user, and a new database and import the schema into the db:

Then, configure Powerdns to use MySQL:

You could also use localhost instead of 127.0.0.1, but this causes PowerDNS to use the socket file. As PowerDNS runs in a chroot by default, the socket file is not available.

Configure Powerdns to use sqlite:

Start/enable pdns.service.

PowerDNS comes with pdnsutil(1) utility to easily manage hosted zones.

Create a new, empty zone:

Upon saving and quitting the editor, you will be asked for confirmation to commit the changes. Carefully read the shown diff and only press a when you're certain that the change is correct. If you keep SOA record unchanged, you'll also be asked whether to increase serial number or not. In most cases, you can simply reply with y, which bumps the number.

When you want to no longer serve the zone, you can remove it from the backend:

PowerDNS has easy-to-use facilities to serve DNSSEC-signed zone with minimal administrative overhead. It takes advantage of online signing architecture, which generates signatures on-demand when queries come from Internet.

For most cases, turning existing insecure zone into DNSSEC-signed one is as simply as:

This will sign the zone with single (CSK) ECDSA 256-bit (algorithm 13) key with NSEC denial-of-existence.

For more flexibility on key generation, pdnsutil add-zone-key command can be used instead. For example, to generate traditional KSK/ZSK split ECDSA 256-bit keys:

To view DS records (and other zone information):

Submit DS to the parent zone (e.g. by filling the web form on your registrar).

The default /etc/powerdns/pdns.conf binds to 0.0.0.0:53 (all IP addresses). This will conflict with any other process bound to port 53, for example systemd-resolved uses 127.0.0.53:53. This will result in an error:

This can be resolved in a number of ways, for example changing either/both local-address or local-port options:

By default, zones in PowerDNS are native, which means that zone replication is handled by the backend. It is only make sense for MySQL and PostgreSQL backends as they have database replication facility.

You can also configure PowerDNS in classical primary/secondary setup. First, enable appropriate mode in /etc/powerdns/pdns.conf.

where 10.20.30.40 and 10.20.30.50 are IP addresses of primary and secondary, respectively.

Restart pdns.service.

Set the zone type on primary as primary zone:

On secondary, create the secondary zone, specifying primary's IP address to retrieve from:

The zone will be transferred after a while.

You can also authenticate zone transfers with TSIG keys.

On primary, generate hmac-sha256 key:

Enable the key for primary zone's outgoing transfer:

On secondary, import the key:

Enable the key for secondary zone's transfer request:

**Examples:**

Example 1 (unknown):
```unknown
/etc/powerdns/pdns.conf
```

Example 2 (unknown):
```unknown
/usr/share/doc/powerdns
```

Example 3 (unknown):
```unknown
$ psql -U <user> -d <database name> -a -f /usr/share/doc/powerdns/schema.pgsql.sql
```

Example 4 (unknown):
```unknown
/etc/powerdns/pdns.conf
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Hostname

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## ConnMan

**URL:** https://wiki.archlinux.org/title/ConnMan

**Contents:**
- Installation
  - Front-ends
- Usage
  - Wi-Fi
    - Enabling and disabling Wi-Fi
    - Connecting to an open access point
    - Connecting to a protected access point
    - Using iwd instead of wpa_supplicant
  - Settings
  - Technologies

ConnMan is a command-line network manager designed for use with embedded devices and fast resolve times. It is modular through a plugin architecture, but has native DHCP and NTP support.[1]

Install the connman package. wpa_supplicant, bluez, and openvpn are optional dependencies required for Wi-Fi, Bluetooth, and VPN functionality respectively.

Before enabling connman.service, ensure any existing network configuration is disabled.

ConnMan comes with the connmanctl(1) CLI, there are various #Front-ends available.

This article or section needs expansion.

ConnMan comes with the connmanctl command-line interface, see connmanctl(1). If you do not provide any commands connmanctl starts as an interactive shell.

ConnMan automatically handles wired connections.

To check if Wi-Fi is enabled you can run connmanctl technologies and check for the line that says Powered: True/False. To power the Wi-Fi on you can run connmanctl enable wifi or if you need to disable it you can run connmanctl disable wifi. Other ways to enable Wi-Fi could include using the Fn keys on the laptop to turn it on or running ip link set interface up.

To scan the network connmanctl accepts simple names called technologies. To scan for nearby Wi-Fi networks:

To list the available networks found after a scan run (example output):

To connect to an open network, use the second field beginning with wifi_:

You should now be connected to the network. Check using connmanctl state or ip addr.

For protected access points you will need to provide some information to the ConnMan daemon, at the very least a password or a passphrase.

The commands in this section show how to run connmanctl in interactive mode, it is required for running the agent command. To start interactive mode simply type:

You then proceed almost as above, first scan for any Wi-Fi technologies:

Now you need to register the agent to handle user requests. The command is:

You now need to connect to one of the protected services. To do this easily, just use tab completion for the wifi_ service. If you were connecting to OtherNET in the example above you would type:

The agent will then ask you to provide any information the daemon needs to complete the connection. The information requested will vary depending on the type of network you are connecting to. The agent will also print additional data about the information it needs as shown in the example below.

Provide the information requested, in this example the passphrase, and then type:

If the information you provided is correct you should now be connected to the protected access point.

ConnMan can use iwd to connect to wireless networks. As connman will start wpa_supplicant when it finds it, it is recommended to uninstall wpa_supplicant.

This article or section is out of date.

Note that ConnMan is probably unnecessary for IWD users, as IWD can handle its own network configuration, in which case connmand should be stopped.

Currently the -i-option of iwd seems to cause that the Wi-Fi interface gets hidden from connman.

Create the following service file which should cause connman to use iwd to connect to wireless networks, regardless if wpa_supplicant is installed.

Then enable/start the connman_iwd service.

Advantage of using iwd instead of wpa_supplicant is, that the ping times seem to be much more consistent and the connection seems to be more reliable.

Settings and profiles are automatically created for networks the user connects to often. They contain fields for the passphrase, essid and other information. Profile settings are stored in directories under /var/lib/connman/ by their service name. To view all network profiles run:

Various hardware interfaces are referred to as Technologies by ConnMan.

To list available technologies run:

To get just the types by their name one can use this one liner:

To interact with them one must refer to the technology by type. Technologies can be toggled on/off with:

For example to toggle off Wi-Fi:

By default, ConnMan changes the transient hostname (see hostnamectl(1)) on a per network basis. This can create problems with X authority: If ConnMan changes your hostname to something else than the one used to generate the xauth magic cookie, then it will become impossible to create new windows. Symptoms are error messages like No protocol specified and Can't open display: :0.0. Manually resetting the host name fixes this, but a permanent solution is to prevent ConnMan from changing your host name in the first place. This can be accomplished by adding the following to /etc/connman/main.conf:

Make sure to restart the connman.service after changing this file.

For testing purposes it is recommended to watch the systemd journal and plug the network cable a few times to see the action.

By default ConnMan does not prefer Ethernet over wireless, which can lead to it deciding to stick with a slow wireless network even when ethernet is available. You can tell connman to prefer Ethernet adding the following to /etc/connman/main.conf:

ConnMan allows you to be connected to both Ethernet and wireless at the same time. This can be useful as it allows programs that established a connection over Wi-Fi to stay connected even after you connect to ethernet. But some people prefer to have only a single unambiguous connection active at a time. That behavior can be activated by adding the following to /etc/connman/main.conf:

WPA2 Enterprise networks such as eduroam require a separate configuration file before connecting to the network. For example, create /var/lib/connman/eduroam.config:

Restart wpa_supplicant.service and connman.service to connect to the new network.

For more information, see connman-service.config(5) and Wireless network configuration#eduroam.

If you are running a local DNS server, it will likely have problems binding to port 53 (TCP and/or UDP) after installing Connman. This is because Connman includes its own DNS proxy which also tries to bind to those ports. If you see log messages from BIND or dnsmasq like

this could be the problem. To verify which application is listening on the ports, you can execute ss -tulpn as root.

To fix this connmand can be started with the options -r or --nodnsproxy by overriding the systemd service file. Create the folder /etc/systemd/system/connman.service.d/ and add the file disable_dns_proxy.conf:

Make sure to reload the systemd daemon and restart the connman.service, and your DNS proxy, after adding this file.

If you want to know the DNS servers received from DHCP while keeping a custom /etc/resolv.conf, then append RuntimeDirectory=connman to the above file (clear the ExecStart lines if not needed). Now connman will write them to /var/run/connman/resolv.conf instead.

ConnMan has systemd-resolved support, which replaces its internal DNS proxy with a module that configures systemd-resolved with the correct DNS servers and search domains for the interface whenever it connects to a network. Using systemd-resolved is known to improve compatibility with Tailscale since ConnMan's internal proxy and Tailscale can fight over /etc/resolv.conf, which is better mediated by both talking to resolved instead.

To use this support, ConnMan needs to be rebuilt: checkout the package using the Arch build system, set the configure flag --with-dns-backend=systemd-resolved, rebuild the package, and install the modified version. After installing the modified package, set up the stub resolver as /etc/resolv.conf then restart connman.service, systemd-resolved.service, and (if using it) tailscale.service.

If something like Docker is creating virtual interfaces Connman may attempt to connect to one of these instead of your physical adapter if the connection drops. A simple way of avoiding this is to blacklist the interfaces you do not want to use. Connman will by default blacklist interfaces starting with vmnet, vboxnet, virbr and ifb, so those need to be included in the new blacklist as well.

Blacklisting interface names is also useful to avoid a race condition where connman may access eth# or wlan# before systemd/udev can change it to use a Predictable Network Interface Names like enp4s0. Blacklisting the conventional (and unpredictable) interface prefixes makes connman wait until they are renamed.

If it does not already exist, create /etc/connman/main.conf:

Once connman.service has been restarted this will also hide all the veth####### interfaces from GUI tools like Econnman.

Currently, connman does not support scanning for Wi-Fi networks with iwd, at the moment this functionality is available with wpa_supplicant only (see [4]). To connect to Wi-Fi with iwd, enable/start iwd.service and then either follow instructions in Iwd to connect to the Wi-Fi or you can also use any of the #Front-ends. In order to have Wi-Fi scanning support from within connman, install wpa_supplicant and then restart connman.service after you stop iwd.service.

You have enabled your Wi-Fi with:

If wireless scanning leads to above error, this may be due to an unresolved bug. If it does not resolve even though wireless preconditions[dead link 2023-09-16—domain name not resolved] are met, try again after disabling competing network managers and rebooting.

This may also simply be caused by the wireless interface being blocked by rfkill, which can occur after restarting wpa_supplicant. Use rfkill list to check.

When issuing commands, you may see errors like the following:

From a connmanctl prompt:

These errors are produced because the agent is not running. Start the agent from a connmanctl prompt with agent on, and try again.

connman can fail to set hostname or domainname due to lack of CAP_SYS_ADMIN.

You will need to edit connman.service (and other like connman-vpn.service , etc ...) to modify the CapabilityBoundingSet line to add CAP_SYS_ADMIN.

See EPERM under sethostname(2) § ERRORS or setdomainname(2) § ERRORS for more details.

A log entry for an unknown route appears each time a connect is done. For example:

It likely is Connman performing a connectivity check to the ipv4.connman.net host (which resolves to the IP address 82.165.8.211 at current).[5] See the Connman README for more information on why and what - apart from the connecting IP - it transmits. This behaviour can be prevented by adding the following to /etc/connman/main.conf:

This setting will cause that the default device will not switch to ONLINE, but stay in READY state.connman.conf(5) However, the connection will still be functional.

The connection itself is also functional (unless behind a captive portal) if the check is blocked by a firewall rule:

If you see this in your error log it is caused by bug in connman [6] and can be ignored.Bug Report

**Examples:**

Example 1 (unknown):
```unknown
connman.service
```

Example 2 (unknown):
```unknown
connmanctl technologies
```

Example 3 (unknown):
```unknown
Powered: True/False
```

Example 4 (unknown):
```unknown
connmanctl enable wifi
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Network_manager

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## SSH keys

**URL:** https://wiki.archlinux.org/title/SSH_keys

**Contents:**
- Background
- Generating an SSH key pair
  - Choosing the authentication key type
    - Ed25519
    - ECDSA
    - RSA
    - FIDO/U2F
      - resident
      - no-touch-required
  - Choosing the key location and passphrase

This article or section needs expansion.

SSH keys can serve as a means of identifying yourself to an SSH server using public-key cryptography and challenge-response authentication. The major advantage of key-based authentication is that, in contrast to password authentication, it is not prone to brute-force attacks, and you do not expose valid credentials if the server has been compromised (see RFC 4251 9.4.4).

Furthermore, SSH key authentication can be more convenient than the more traditional password authentication. When used with a program known as an SSH agent, SSH keys can allow you to connect to a server, or multiple servers, without having to remember or enter your password for each system.

Key-based authentication is not without its drawbacks and may not be appropriate for all environments, but in many circumstances it can offer some strong advantages. A general understanding of how SSH keys work will help you decide how and when to use them to meet your needs.

This article assumes you already have a basic understanding of the Secure Shell protocol and have installed the openssh package.

SSH keys are always generated in pairs with one known as the private key and the other as the public key. The private key is known only to you and it should be safely guarded. By contrast, the public key can be shared freely with any SSH server to which you wish to connect.

If an SSH server has your public key on file and sees you requesting a connection, it uses your public key to construct and send you a challenge. This challenge is an encrypted message and it must be met with the appropriate response before the server will grant you access. What makes this coded message particularly secure is that it can only be understood by the private key holder. While the public key can be used to encrypt the message, it cannot be used to decrypt that very same message. Only you, the holder of the private key, will be able to correctly understand the challenge and produce the proper response.

This challenge-response phase happens behind the scenes and is invisible to the user. As long as you hold the private key, which is typically stored in the ~/.ssh/ directory, your SSH client should be able to reply with the appropriate response to the server.

A private key is a guarded secret and as such it is advisable to store it on disk in an encrypted form. When the encrypted private key is required, a passphrase must first be entered in order to decrypt it. While this might superficially appear as though you are providing a login password to the SSH server, the passphrase is only used to decrypt the private key on the local system. The passphrase is not transmitted over the network.

An SSH key pair can be generated by running the ssh-keygen command, see the ssh-keygen(1) man page for what is "generally considered sufficient" and should be compatible with virtually all clients and servers:

The randomart image was introduced in OpenSSH 5.1 as an easier means of visually identifying the key fingerprint.

You can also add an optional comment field to the public key with the -C switch, to more easily identify it in places such as ~/.ssh/known_hosts, ~/.ssh/authorized_keys and ssh-add -L output. For example:

will add a comment saying which user created the key on which machine and when.

OpenSSH supports several signing algorithms (for authentication keys) which can be divided in two groups depending on the mathematical properties they exploit:

Elliptic curve cryptography (ECC) algorithms are a more recent addition to public key cryptosystems. One of their main advantages is their ability to provide the same level of security with smaller keys, which makes for less computationally intensive operations (i.e. faster key creation, encryption and decryption) and reduced storage and transmission requirements.

DSA keys are deprecated due to their security weaknesses and most SSH implementations do not support them anymore. Dropbear 2022.83 disabled DSA key support while OpenSSH 10.0 and libssh 0.11.0 removed support for DSA keys entirely. Therefore the choice of cryptosystem lies within RSA or one of the two types of ECC.

The default Ed25519 will give you the best security and good performance. ECDSA is slower than Ed25519, but faster than RSA; concerns exist about its security (see below). RSA keys will give you the greatest compatibility with old servers, but it requires a larger key size to provide sufficient security.

Ed25519 was introduced in OpenSSH 6.5 of January 2014: "Ed25519 is an elliptic curve signature scheme that offers better security than ECDSA and DSA and good performance". Its main strengths are its speed, its constant-time run time (and resistance against side-channel attacks), and its lack of nebulous hard-coded constants.[1] See also this blog post by a Mozilla developer on how it works.

It is implemented in many applications and libraries and is the default key type in ssh-keygen(1) and dropbearkey(1).

ssh-keygen(1) defaults to Ed25519 therefore there is no need to specify it with the -t ed25519 option. The key pairs can be simply generated with:

There is no need to set the key size, as all Ed25519 keys are 256 bits.

Keep in mind that ancient SSH clients and servers may not support these keys.

The Elliptic Curve Digital Signature Algorithm (ECDSA) was the preferred algorithm for authentication (key exchange algorithm) from OpenSSH 5.7 (2011-01-24) to OpenSSH 6.5 (2014-01-30).

There are two sorts of concerns with it:

Both of those concerns are best summarized in libssh curve25519 introduction. Although the political concerns will always be subject to debate, there is a clear consensus that #Ed25519 is technically superior and should therefore be preferred.

ECDSA key pairs can be generated with:

Three elliptic curve sizes are supported for ECDSA keys: 256, 384 and 521 bits. The default is 256 bits. If you wish to generate a stronger ECDSA key pair, simply specify the -b option:

RSA provides the best compatibility of all algorithms but requires the key size to be larger to provide sufficient security. Minimum key size is 1024 bits, default is 3072 (see ssh-keygen(1)) and maximum is 16384.

RSA key pairs can be generated with:

If you wish to generate a stronger RSA key pair (e.g. to guard against cutting-edge or unknown attacks and more sophisticated attackers), simply specify the -b option with a higher bit value than the default:

Be aware though that there are diminishing returns in using longer keys.[2][3] The GnuPG FAQ reads: "If you need more security than RSA-2048 offers, the way to go would be to switch to elliptical curve cryptography — not to continue using RSA."[4]

On the other hand, the latest iteration of the NSA Fact Sheet Suite B Cryptography suggests a minimum 3072-bit modulus for RSA while "[preparing] for the upcoming quantum resistant algorithm transition".[5]

FIDO/U2F hardware authenticator support was added in OpenSSH version 8.2 for both of the elliptic curve signature schemes mentioned above. It allows for a hardware token attached via USB or other means to act a second factor alongside the private key.

The libfido2 is required for hardware token support.

After attaching a compatible FIDO key, a key pair may be generated with:

You will usually be required to enter your PIN and/or tap your token to confirm the generation.

By default, the generated SSH key consist of two parts: a key handle on disk, and a private key that is unique for each security key. To easily move your FIDO key between machines, generate a key with the ssh-keygen(1) § resident option, -O resident. This indicates "that the key handle should be stored on the FIDO authenticator itself." [6]

Afterwards, on a new machine, the key can be downloaded using ssh-keygen(1) § K

Connecting to a server will usually require tapping your token unless the -O no-touch-required command line option is used during generation and the sshd(8) § no-touch-required authorized_keys option is set on the server.

To create keys that do not require touch events, generate a key pair with the no-touch-required option. For example:

Additionally, sshd rejects no-touch-required keys by default. To allow keys generated with this option, either enable it for an individual key in the authorized_keys file:

Or for the whole system by editing /etc/ssh/sshd_config with:

An ECDSA-based keypair may also be generated with the ecdsa-sk keytype, but the relevant concerns in the #ECDSA section above still apply.

Upon issuing the ssh-keygen command, you will be prompted for the desired name and location of your private key. By default, keys are stored in the ~/.ssh/ directory and named according to the type of encryption used. You are advised to accept the default name and location in order for later code examples in this article to work properly.

When prompted for a passphrase, choose something that will be hard to guess if you have the security of your private key in mind. A longer, more random password will generally be stronger and harder to crack should it fall into the wrong hands.

It is also possible to create your private key without a passphrase. While this can be convenient, you need to be aware of the associated risks. Without a passphrase, your private key will be stored on disk in an unencrypted form. Anyone who gains access to your private key file will then be able to assume your identity on any SSH server to which you connect using key-based authentication. Furthermore, without a passphrase, you must also trust the root user, as they can bypass file permissions and will be able to access your unencrypted private key file at any time.

If the originally chosen SSH key passphrase is undesirable or must be changed, one can use the ssh-keygen command to change the passphrase without changing the actual key. This can also be used to change the password encoding format to the new standard.

If you have multiple SSH identities, you can set different keys to be used for different hosts or remote users by using the Host and IdentityFile directives in your configuration:

See ssh_config(5) for full description of these options.

SSH keys can also be stored on a security token like a smart card or a USB token. This has the advantage that the private key is stored securely on the token instead of being stored on disk. When using a security token the sensitive private key is also never present in the RAM of the PC; the cryptographic operations are performed on the token itself. A cryptographic token has the additional advantage that it is not bound to a single computer; it can easily be removed from the computer and carried around to be used on other computers.

Examples of hardware tokens are described in:

This article or section needs expansion.

Once you have generated a key pair, you will need to copy the public key to the remote server so that it will use SSH key authentication. The public key file shares the same name as the private key except that it is appended with a .pub extension. Note that the private key is not shared and remains on the local machine.

If your key file is ~/.ssh/id_rsa.pub you can simply enter the following command.

If your username differs on remote machine, be sure to prepend the username followed by @ to the server name.

If your public key filename is anything other than the default of ~/.ssh/id_rsa.pub you will get an error stating /usr/bin/ssh-copy-id: ERROR: No identities found. In this case, you must explicitly provide the location of the public key.

If the ssh server is listening on a port other than default of 22, be sure to include it within the host argument.

By default, for OpenSSH, the public key needs to be concatenated with ~/.ssh/authorized_keys. Begin by copying the public key to the remote server.

The above example copies the public key (id_ecdsa.pub) to your home directory on the remote server via scp. Do not forget to include the : at the end of the server address. Also note that the name of your public key may differ from the example given.

On the remote server, you will need to create the ~/.ssh directory if it does not yet exist and append your public key to the authorized_keys file.

The last two commands remove the public key file from the server and set the permissions on the authorized_keys file such that it is only readable and writable by you, the owner.

If your private key is encrypted with a passphrase, this passphrase must be entered every time you attempt to connect to an SSH server using public-key authentication. Each individual invocation of ssh or scp will need the passphrase in order to decrypt your private key before authentication can proceed.

An SSH agent is a program which caches your decrypted private keys and provides them to SSH client programs on your behalf. In this arrangement, you must only provide your passphrase once, when adding your private key to the agent's cache. This facility can be of great convenience when making frequent SSH connections.

An agent is typically configured to run automatically upon login and persist for the duration of your login session. A variety of agents, front-ends, and configurations exist to achieve this effect. This section provides an overview of a number of different solutions which can be adapted to meet your specific needs.

ssh-agent is the default agent included with OpenSSH. It can be used directly or serve as the back-end to a few of the front-end solutions mentioned later in this section. When ssh-agent is run, it forks to background and prints necessary environment variables. E.g.

To make use of these variables, run the command through the eval command. Use ssh-agent -c instead if using the fish shell.

Once ssh-agent is running, you will need to add your private key to its cache:

If your private key is encrypted, ssh-add will prompt you to enter your passphrase. Once your private key has been successfully added to the agent you will be able to make SSH connections without having to enter your passphrase.

In order to start the agent automatically and make sure that only one ssh-agent process runs at a time, touch $XDG_RUNTIME_DIR/ssh-agent.env and add the following to your ~/.bashrc:

This will run an ssh-agent process if there is not one already, and save the output thereof. If there is one running already, we retrieve the cached ssh-agent output and evaluate it which will set the necessary environment variables. The lifetime of the unlocked keys is set to 1 hour.

There also exist a number of front-ends to ssh-agent and alternative agents described later in this section which avoid this problem.

If you would like your ssh agent to run when you are logged in, regardless of whether X is running, a handy ssh-agent.service is included in openssh since the version 9.4p1-3, which can be enabled as a user unit.

Then set the environment variable SSH_AUTH_SOCK to $XDG_RUNTIME_DIR/ssh-agent.socket.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

When forwarding a local ssh-agent to remote (e.g., through command-line argument ssh -A remote or through ForwardAgent yes in the configuration file), it is important for the remote machine not to overwrite the environment variable SSH_AUTH_SOCK. So if the remote machine uses a systemd unit shown previously to start the agent, SSH_AUTH_SOCK must not be set in the environment when a user is logged in through SSH. Otherwise, the forwarding may fail, and you may see errors (for example: The agent has no identities) when checking the existing keys with ssh-add -l on the remote machine.

For example, if using bash, the .bashrc could be something like:

In this way, SSH_AUTH_SOCK is only set when the current session is not an SSH login. And when this is a SSH session, SSH_AUTH_SOCK on the remote machine is then set by the local machine to make the forwarding work.

An alternative way to start ssh-agent (with, say, each X session) is described in this ssh-agent tutorial by UC Berkeley Labs. A basic use case is if you normally begin X with the startx command, you can instead prefix it with ssh-agent like so:

And so you do not even need to think about it you can put an alias in your .bash_aliases file or equivalent:

Doing it this way avoids the problem of having extraneous ssh-agent instances floating around between login sessions. Exactly one instance will live and die with the entire X session.

See the notes on using x11-ssh-askpass with ssh-add for an idea on how to immediately add your key to the agent.

This ssh-agent specializes on OpenPGP card integration. It uses private keys that are stored in OpenPGP card authentication slots.

Install openpgp-card-ssh-agent and enable and start the openpgp-card-ssh-agent.socket user unit.

Afterwards add the relevant environment variable for this agent:

The user PIN for the OpenPGP card is persisted via an org.freedesktop.secrets provider (such as GNOME Keyring, KeePassXC or KDE Wallet) by default. The PIN storage backend is configurable and extendable.

The user PIN needs to be persisted only once for each OpenPGP card. Prior to the first SSH connection with this agent, list the available SSH public keys and add their respective card identifiers:

The gpg-agent has OpenSSH Agent protocol emulation. See GnuPG#SSH agent for necessary configuration.

Keychain is a program designed to help you easily manage your SSH keys with minimal user interaction. It is implemented as a shell script which drives both ssh-agent and ssh-add. A notable feature of Keychain is that it can maintain a single ssh-agent process across multiple login sessions. This means that you only need to enter your passphrase once each time your local machine is booted.

Install the keychain package.

Add a line similar to the following to your shell configuration file, e.g. if using Bash:

In the above example,

Multiple keys can be specified on the command line, as shown in the example. By default keychain will look for key pairs in the ~/.ssh/ directory, but absolute path can be used for keys in non-standard location. You may also use the --confhost option to inform keychain to look in ~/.ssh/config for IdentityFile settings defined for particular hosts, and use these paths to locate keys.

See keychain --help or keychain(1) for details on setting keychain for other shells.

To test Keychain, simply open a new terminal emulator or log out and back in your session. It should prompt you for the passphrase of the specified private key(s) (if applicable), either using the program set in $SSH_ASKPASS or on the terminal.

Because Keychain reuses the same ssh-agent process on successive logins, you should not have to enter your passphrase the next time you log in or open a new terminal. You will only be prompted for your passphrase once each time the machine is rebooted.

The x11-ssh-askpass package provides a graphical dialog for entering your passhrase when running an X session. x11-ssh-askpass depends only on the libx11 and libxt libraries, and the appearance of x11-ssh-askpass is customizable. While it can be invoked by the ssh-add program, which will then load your decrypted keys into ssh-agent, the following instructions will, instead, configure x11-ssh-askpass to be invoked by the aforementioned Keychain script.

Install the keychain and x11-ssh-askpass packages.

Edit your ~/.xinitrc file to include the following lines, replacing the name and location of your private key if necessary. Be sure to place these commands before the line which invokes your window manager.

In the above example, the first line invokes keychain and passes the name and location of your private key. If this is not the first time keychain was invoked, the following two lines load the contents of $HOSTNAME-sh and $HOSTNAME-sh-gpg, if they exist. These files store the environment variables of the previous instance of keychain.

The ssh-add manual page specifies that, in addition to needing the DISPLAY or WAYLAND_DISPLAY variable defined, you also need SSH_ASKPASS set to the name of your askpass program (in this case x11-ssh-askpass). It bears keeping in mind that the default Arch Linux installation places the x11-ssh-askpass binary in /usr/lib/ssh/, which will not be in most people's PATH. This is a little annoying, not only when declaring the SSH_ASKPASS variable, but also when theming. You have to specify the full path everywhere. Both inconveniences can be solved simultaneously by symlinking:

This is assuming that ~/bin is in your PATH. So now in your .xinitrc, before calling your window manager, one just needs to export the SSH_ASKPASS environment variable:

and your X resources will contain something like:

Doing it this way works well with the above method on using ssh-agent as a wrapper program. You start X with ssh-agent startx and then add ssh-add to your window manager's list of start-up programs.

The appearance of the x11-ssh-askpass dialog can be customized by setting its associated X resources. Some examples are the .ad files at https://github.com/sigmavirus24/x11-ssh-askpass. See x11-ssh-askpass(1) for full details.

There are other passphrase dialog programs which can be used instead of x11-ssh-askpass. The following list provides some alternative solutions.

The pam_ssh project exists to provide a Pluggable Authentication Module (PAM) for SSH private keys. This module can provide single sign-on behavior for your SSH connections. On login, your SSH private key passphrase can be entered in place of, or in addition to, your traditional system password. Once you have been authenticated, the pam_ssh module spawns ssh-agent to store your decrypted private key for the duration of the session.

To enable single sign-on behavior at the tty login prompt, install the unofficial pam_sshAUR package.

Create a symlink to your private key file and place it in ~/.ssh/login-keys.d/. Replace the id_rsa in the example below with the name of your own private key file.

Edit the /etc/pam.d/login configuration file to include the text highlighted in bold in the example below. The order in which these lines appear is significiant and can affect login behavior.

In the above example, login authentication initially proceeds as it normally would, with the user being prompted to enter their user password. The additional auth authentication rule added to the end of the authentication stack then instructs the pam_ssh module to try to decrypt any private keys found in the ~/.ssh/login-keys.d directory. The try_first_pass option is passed to the pam_ssh module, instructing it to first try to decrypt any SSH private keys using the previously entered user password. If the user's private key passphrase and user password are the same, this should succeed and the user will not be prompted to enter the same password twice. In the case where the user's private key passphrase user password differ, the pam_ssh module will prompt the user to enter the SSH passphrase after the user password has been entered. The optional control value ensures that users without an SSH private key are still able to log in. In this way, the use of pam_ssh will be transparent to users without an SSH private key.

If you use another means of logging in, such as an X11 display manager like SLiM or XDM and you would like it to provide similar functionality, you must edit its associated PAM configuration file in a similar fashion. Packages providing support for PAM typically place a default configuration file in the /etc/pam.d/ directory.

Further details on how to use pam_ssh and a list of its options can be found in the pam_ssh(8) man page.

If you want to unlock the SSH keys or not depending on whether you use your key's passphrase or the (different!) login password, you can modify /etc/pam.d/system-auth to

For an explanation, see [8].

Work on the pam_ssh project is infrequent and the documentation provided is sparse. You should be aware of some of its limitations which are not mentioned in the package itself.

As an alternative to pam_ssh you can use pam_exec-ssh-gitAUR. It is a shell script that uses pam_exec. Help for configuration can be found upstream.

The GNOME Keyring tool can act as a wrapper around ssh-agent, providing GUI and/or automatic key unlocking. See GNOME Keyring#SSH keys for further details.

For instructions on how to use kwallet to store your SSH keys, see KDE Wallet#Using the KDE Wallet to store ssh key passphrases.

KeeAgent is a plugin for KeePass that allows SSH keys stored in a KeePass database to be used for SSH authentication by other programs.

See KeePass#Plugin installation in KeePass or install the keepass-plugin-keeagent package.

This agent can be used directly, by matching KeeAgent socket: KeePass -> Tools -> Options -> KeeAgent -> Agent mode socket file -> %XDG_RUNTIME_DIR%/keeagent.socket and environment variable: export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR"'/keeagent.socket'.

The KeePassXC fork of KeePass can act as a client for an existing SSH agent. SSH keys stored in its database can be automatically (or manually) added to the agent. It is also compatible with KeeAgent's database format.

If your private key requires a password (or, for instance, you have a hardware key with a PIN) but ssh-agent is not provided with one, ssh will fail:

One potential cause for this is ssh-agent being unable to prompt for a password. Ensure that ssh-agent has access to either a display server (via the DISPLAY environment variable) or a TTY. For some graphical environments you might only need to install x11-ssh-askpass, for other setups also follow #x11-ssh-askpass instructions.

Another cause, if using a hardware authenticator, could be the key malfunctioning or being unplugged.

There is currently an open bug that triggers with the "agent refused operation" error when using authenticator keys like ED25519-sk and ECDSA-SK that were created with the option -O verify-required. To avoid this issue, use the -o IdentityAgent=none -o IdentitiesOnly=yes option for the ssh command or add it to your ssh_config file for the relevant hosts:

**Examples:**

Example 1 (unknown):
```unknown
$ ssh-keygen
```

Example 2 (unknown):
```unknown
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/username/.ssh/id_ed25519):
Created directory '/home/username/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/username/.ssh/id_ed25519
Your public key has been saved in /home/username/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:RLy4JBv7jMK5qYhRKwHB3af0rpMKYwE2PBhALCBV3G8 username@hostname
The key's randomart image is:
+--[ED25519 256]--+
|%oooo. ..        |
|== ..o.o.        |
|==  . +o..       |
|+ o o.ooE        |
|...  *.oS        |
| o..o ..         |
|o=.. +o          |
|+o*..+o          |
|+.o+. .          |
+----[SHA256]-----+
```

Example 3 (unknown):
```unknown
~/.ssh/known_hosts
```

Example 4 (unknown):
```unknown
~/.ssh/authorized_keys
```

---

## dnscrypt-proxy

**URL:** https://wiki.archlinux.org/title/Dnscrypt-proxy

**Contents:**
- Installation
- Configuration
  - Startup
  - Select resolver
  - Modify resolv.conf and coordinate with other local domain name resolvers
    - Disable any services bound to port 53
  - Start systemd service
  - Check if dnscrypt-proxy is working
- Tips and tricks
  - Enabling, downloading and auto-updating filter lists / block lists

This article or section needs expansion.

dnscrypt-proxy is a DNS proxy client with support for the encrypted DNS protocols DNS over HTTPS and DNSCrypt, which can be used to prevent man-in-the-middle attacks and eavesdropping. dnscrypt-proxy is also compatible with DNSSEC.

Install the dnscrypt-proxy package.

The default configuration file referred to is at /etc/dnscrypt-proxy/dnscrypt-proxy.toml.

The service can be started in two mutually exclusive ways (i.e. only one of the two may be enabled):

By leaving server_names commented out in the configuration file, dnscrypt-proxy will choose the fastest server from the sources already configured under [sources] [3]. The lists will be downloaded, verified, and automatically updated [4]. Thus, configuring a specific set of servers is optional.

To manually set which server is used, uncomment the server_names variable in the configuration file and select one or more of the servers. For example, to use Cloudflare's servers:

A full list of resolvers is located at the upstream page or Github. If dnscrypt-proxy has run successfully on the system before, /var/cache/dnscrypt-proxy/public-resolvers.md will also contain a list. Look at the description for servers note which validate DNSSEC, do not log, and are uncensored. These requirements can be configured globally with the require_dnssec, require_nolog, require_nofilter options.

Modify the resolv.conf file and replace the current set of resolver addresses with the loopback IP addresses and options[5]:

Next, existing services doing domain name resolution must be configured not to overwrite the settings. See resolv.conf#Overwriting of /etc/resolv.conf for details. They can be used, if they are configured to bind to different addresses than localhost and forward DNS requests to localhost port 53. For example, systemd-resolved uses address 127.0.0.53 by default.

To see if any programs are using port 53, run:

If the output contains more than the first line of column names, you need to disable whatever service is using port 53. For example, NetworkManager may try to activate a resolver automatically, but other network managers may have analogous components. You are ready to proceed once the above command outputs nothing more than the header line:

Finally, start/enable the dnscrypt-proxy.service unit or dnscrypt-proxy.socket, depending on which method you chose above.

Open the browser and head to DnsLeakTest and do an extended test, if the results show servers that you have set in the configuration files it means that dnscrypt-proxy is working, otherwise something is wrong.

This article or section is being considered for removal.

Configure filter list sources in /usr/share/dnscrypt-proxy/utils/generate-domains-blocklist/domains-blocklist.conf. For example:

Create a service to download & combine filter lists. /etc/systemd/system/dnscrypt-filterlist-update.service:

Create a time to run on boot but also every 5 hours. /etc/systemd/system/dnscrypt-filterlist-update.timer:

Configure DNSCrypt to apply the created filter rules. /etc/dnscrypt-proxy/dnscrypt-proxy.toml:

It is recommended to run dnscrypt-proxy as a forwarder for a local DNS cache if not using dnscrypt-proxy's cache feature; otherwise, every single query will make a round-trip to the upstream resolver. Any local DNS caching program should work. In addition to setting up dnscrypt-proxy, you must setup your local DNS cache program.

In order to forward queries from a local DNS cache, dnscrypt-proxy should listen on a port different from the default 53, since the DNS cache itself needs to listen on 53 and query dnscrypt-proxy on a different port. Port number 54 is used as an example in this section.

There are two methods for changing the default port:

Edit dnscrypt-proxy.socket with the following contents:

When queries are forwarded from the local DNS cache to 54, dnscrypt-proxy.socket will start dnscrypt-proxy.service.

Edit the listen_addresses option in /etc/dnscrypt-proxy/dnscrypt-proxy.toml with the following:

The following configurations should work with dnscrypt-proxy and assume that it is listening on port 54.

Configure Unbound to your liking (in particular, see Unbound#Local DNS server) and add the following lines to the end of the server section in /etc/unbound/unbound.conf:

Restart unbound.service to apply the changes.

Configure dnsmasq as a local DNS cache. The basic configuration to work with dnscrypt-proxy:

If you configured dnscrypt-proxy to use a resolver with enabled DNSSEC validation, make sure to enable it also in dnsmasq:

Restart dnsmasq.service to apply the changes.

Install pdnsd. A basic configuration to work with dnscrypt-proxy is:

Restart pdnsd.service to apply the changes.

This article or section needs expansion.

Extension Mechanisms for DNS that, among other things, allows a client to specify how large a reply over UDP can be.

Add the following line to your /etc/resolv.conf:

This article or section is out of date.

Make use of the DNS Reply Size Test Server, use the drill command line tool to issue a TXT query for the name rs.dns-oarc.net:

With EDNS0 supported, the "answer section" of the output should look similar to this:

Set the correct ownership of /var/cache/dnscrypt-proxy, usually dnscrypt-proxy:dnscrypt-proxy.

**Examples:**

Example 1 (unknown):
```unknown
/etc/dnscrypt-proxy/dnscrypt-proxy.toml
```

Example 2 (unknown):
```unknown
dnscrypt-proxy.service
```

Example 3 (unknown):
```unknown
listen_addresses
```

Example 4 (unknown):
```unknown
listen_addresses = ['127.0.0.1:53', '[::1]:53']
```

---

## Network Debugging

**URL:** https://wiki.archlinux.org/title/Tcpdump

**Contents:**
- Ping & Tracepath/Traceroute
- Tcpdump

This article or section is a candidate for merging with Network Configuration.

This article or section is a candidate for merging with Network configuration#Ping.

The ping command can help test connectivity towards a specific host.

The first step would be verifying connectivity towards the default gateway (replace the ip address with your own default gateway):

When erasing the "-c4" parameter, the ping will continue endlessly. It can be aborted by hitting "Control-C".

The output above indicated the default gateway is reachable. When instead a "Destination Host Unreachable" message is displayed, doublecheck the ip address, netmask and default gateway config. This message can also be displayed when ICMP traffic is not permitted towards the default gateway (blocked by a firewall, router,...).

The next step is verifying connectivity towards the configured dns server(s). When no reply is received, tracepath or traceroute can be used to verify the routing towards said server and get an idea of where the issue lies.

Traceroute also used ICMP to determine the path and hence there can be "no reply" answers as well when ICMP traffic is blocked.

tcpdump, and its underlying library libpcap, are multi-platform user space interfaces to the packets on the network. It should be emphasized they do see, they can capture, any inbound packets that reach the local NIC. No matter if the local software firewall is blocking those packets, or not. On the other hand, they can only see outbound packets the firewall passes through: [1]

A short, unintimidating introduction to tcpdump, with examples, is at: [2]

**Examples:**

Example 1 (unknown):
```unknown
$ ping -c4 192.168.1.1
```

Example 2 (unknown):
```unknown
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_req=1 ttl=64 time=0.193 ms
64 bytes from 192.168.1.1: icmp_req=2 ttl=64 time=0.190 ms
64 bytes from 192.168.1.1: icmp_req=3 ttl=64 time=0.192 ms
64 bytes from 192.168.1.1: icmp_req=4 ttl=64 time=0.189 ms

--- 192.168.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 2999ms
rtt min/avg/max/mdev = 0.165/0.184/0.193/0.014 ms
```

Example 3 (unknown):
```unknown
Destination Host Unreachable
```

Example 4 (unknown):
```unknown
$ traceroute 8.8.4.4
```

---

## ipset

**URL:** https://wiki.archlinux.org/title/Ipset

**Contents:**
- Installation
- Configuration
  - Blocking a list of networks
  - Blocking a list of IP addresses
  - Making ipset persistent
  - Blocking with PeerGuardian and other blocklists
- Other commands
- Optimization

ipset is a companion application for the iptables Linux firewall. It allows you to setup rules to quickly and easily block a set of IP addresses, among other things.

The iptables successor nftables has a built-in infrastructure for using sets. The ipset-translate tool can be used to transform "ipsets" (for iptables) into nftables sets, see Moving from ipset to nftables for details.

Install the ipset package.

Start by creating a new "set" of network addresses. This creates a new "hash" set of "net" network addresses named "myset".

Add any IP address that you would like to block to the set.

Finally, configure iptables to block any address in that set. This command will add a rule to the top of the "INPUT" chain to "-m" match the set named "myset" from ipset (--match-set) when it is a "src" packet and "DROP", or block, it.

Start by creating a new "set" of ip addresses. This creates a new "hash" set of "ip" addresses named "myset-ip".

Add any IP address that you would like to block to the set.

Finally, configure iptables to block any address in that set.

The ipset you have created is stored in memory and will be gone after reboot. To make the ipset persistent you have to do the followings:

First, save the ipset to /etc/ipset.conf:

Then enable ipset.service, which works similarly to iptables.service for restoring iptables rules.

The pg2ipset-gitAUR tool by the author of Maeyanie.com, coupled with the ipset-update.sh script, can be used with cron to automatically update various blocklists. Currently, by default, blocking of: country, tor exit node and Bluetack pg2 list are implemented.

Please see the ipset(8) for further information.

The iprangeAUR tool can help to reduce entries in ipset.conf by merging adjacent ranges or eliminating overlapped ranges. This can improve the router/firewall performance if the table size is huge. This tool can also convert a list of hostnames to IPs.

Although ipset is designed to be able to scale well, that does not mean infinitely. In particular, some nations have very large IP address spaces, which will cause geoblocking to be inefficient.

**Examples:**

Example 1 (unknown):
```unknown
# ipset create myset hash:net
```

Example 2 (unknown):
```unknown
# ipset -N myset nethash
```

Example 3 (unknown):
```unknown
# ipset add myset 14.144.0.0/12
# ipset add myset 27.8.0.0/13
# ipset add myset 58.16.0.0/15
# ipset add myset 1.1.1.0/24
```

Example 4 (unknown):
```unknown
# iptables -I INPUT -m set --match-set myset src -j DROP
```

---

## SSHFS

**URL:** https://wiki.archlinux.org/title/SSHFS

**Contents:**
- Installation
- Usage
  - Mounting
  - Unmounting
- Options
  - User ID mapping
  - allow_root or allow_other
  - Change ownership of mountpoint
- Tips and tricks
  - Chrooting

SSHFS is a FUSE-based file system client for mounting remote directories over a Secure Shell connection.

Install the sshfs package.

In order to be able to mount a directory the SSH user needs to be able to access it. Invoke sshfs to mount a remote directory:

Here -p 9876 specifies the port number and -C enables compression. For more options see the #Options section.

When not specified, the remote path defaults to the remote user home directory. Default user names and options can be predefined on a host-by-host basis in ~/.ssh/config to simplify the sshfs usage. For more information see OpenSSH#Client usage.

SSH will ask for the password, if needed. If you do not want to type in the password multiple times a day, see SSH keys.

To unmount the remote system:

A complete list of options can be found in sshfs(1) and mount.fuse(8).

sshfs can automatically convert between local and remote user IDs. Use the idmap=user option to translate the UID of the connecting user to the remote user myuser (GID remains unchanged):

If you need more control over UID and GID translation, look at the options idmap=file, uidfile and gidfile.

allow_root and allow_other are mutually exclusive. Additionally you want to edit /etc/fuse.conf and uncomment the string user_allow_other to enable all users to use these options.

You may want to restrict a specific user to a specific directory on the remote system. This can be done by editing /etc/ssh/sshd_config:

See also SFTP chroot. For more information check the sshd_config(5) man page for Match, ChrootDirectory and ForceCommand.

Similar to other file system mounts see systemd.mount(5) and possibly systemd.automount(5). Because of the FUSE system and its mechanics you should use user units. Setup SSH with public key authentication.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Place the foo.mount inside ${XDG_CONFIG_HOME}/systemd/user/.

Start the unit as usual with the --user option.

See SSH keys#Start ssh-agent with systemd user.

This article or section is being considered for removal.

Create an entry in /etc/fstab with at least _netdev, x-systemd.automount is only necessary if you need automount functionality.

All the generated files are after the daemon-reload command in /run/systemd/generator/. For user units you can copy the files you need and remove the fstab line and reload systemd

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

You will need to write two systemd units: a mount unit and an optional automount unit. Enabling the automount unit and keeping the mount unit itself disabled will not block startup and only mount once trying to access the file system. These files need to be named exactly like the mountpoint with "-" signs separating the folders within the path.

Mount unit, needs to be named exactly like the mountpoint (here, /mnt/data becomes mnt-data):

The automount unit file also needs to be named exactly like the mountpoint:

The factual accuracy of this article or section is disputed.

Automounting can happen on boot, or on demand (when accessing the directory). For both, the setup happens in the fstab.

To let the root user use an SSH key of a normal user, specify its full path in the IdentityFile option.

And most importantly, use each sshfs mount at least once manually while root on the client machine so the host's signature is added to the client's /root/.ssh/known_hosts file. This can also be done manually by appending one or more of the SSH server's public host keys (the /etc/ssh/ssh_host_*key.pub files) to /root/.ssh/known_hosts.

With systemd, on-demand mounting is possible using /etc/fstab entries.

The important mount options here are x-systemd.automount,_netdev.

See also fstab#Automount with systemd.

An example on how to use sshfs to mount a remote file system through /etc/fstab

Take for example the fstab line

The above will work automatically if you are using an SSH key for the user that is not password-protected. See Using SSH Keys.

If you want to use sshfs with multiple users, add the following option:

In order to ensure the network is available before trying to mount, it is not only important to set the _netdev mount option, but also to add either --any or a specific --interface to the appropriate wait-online service for your network manager.

The factual accuracy of this article or section is disputed.

When automounting via fstab, the file system will generally be mounted by root. By default, this produces undesireable results if you wish access as an ordinary user and limit access to other users.

An example mountpoint configuration:

See #allow_root or allow_other for the explanation of the options used.

Read OpenSSH#Checklist first. Further issues to check are:

If you receive this message directly after attempting to use sshfs:

To get verbose debugging output, add the following to the mount options:

To be able to run mount -av and see the debug output, remove the following:

sshfs by default does not support symlinks. If those directories happened to be symlinks, use:

If you see old content on remote, consider using option dir_cache=no:

If you observe transfer speed that is lower than your network capabilities and high CPU usage on the party where files are copied from, disable compression (remove -C option or set -o compression=no).

**Examples:**

Example 1 (unknown):
```unknown
$ sshfs [user@]host:[dir] mountpoint [options]
```

Example 2 (unknown):
```unknown
$ sshfs myuser@mycomputer:/remote/path /local/path -C -p 9876
```

Example 3 (unknown):
```unknown
~/.ssh/config
```

Example 4 (unknown):
```unknown
$ fusermount3 -u mountpoint
```

---

## Category:Firewalls

**URL:** https://wiki.archlinux.org/title/Firewall

Arch Linux comes with two options for managing a firewall, neither of which is enabled automatically. The stock Linux kernel includes the netfilter packet filtering framework which can be managed by either of the following:

---

## dnsmasq

**URL:** https://wiki.archlinux.org/title/Dnsmasq

**Contents:**
- Installation
- Configuration
  - DNS server
    - DNS addresses file and forwarding
      - openresolv
      - Manual forwarding
    - Adding a custom domain
    - Test
  - DHCP server
    - Proxy DHCP

dnsmasq provides a DNS server, a DHCP server with support for DHCPv6 and PXE, and a TFTP server. It is designed to be lightweight and have a small footprint, suitable for resource constrained routers and firewalls. dnsmasq can also be configured to cache DNS queries for improved DNS lookup speeds to previously visited sites.

Install the dnsmasq package. Then start/enable dnsmasq.service.

The network will also need to be restarted so the DHCP client can create a new /etc/resolv.conf.

To configure dnsmasq, edit /etc/dnsmasq.conf. The file contains comments explaining the options. For all available options see dnsmasq(8).

If dnsmasq will not be used as a local DNS resolver, you may also want to edit dnsmasq.service so that it does not pull in nss-lookup.target:

To set up dnsmasq as a DNS caching daemon on a single computer specify a listen-address directive, adding in the localhost IP address:

To use this computer to listen on its LAN IP address for other computers on the network. It is recommended that you use a static LAN IP in this case. E.g.:

You may alternatively assign a network interface:

Set the number of cached domain names with cache-size=size (the default is 150):

To validate DNSSEC load the DNSSEC trust anchors provided by the dnsmasq package and set the option dnssec:

See dnsmasq(8) for more options you might want to use.

After configuring dnsmasq, you need to add the localhost addresses as the only nameservers in /etc/resolv.conf. This causes all queries to be sent to dnsmasq.

Since dnsmasq is a stub resolver not a recursive resolver you must set up forwarding to an external DNS server. This can be done automatically by using openresolv or by manually specifying the DNS server address in dnsmasq's configuration.

If your network manager supports resolvconf, instead of directly altering /etc/resolv.conf, you can use openresolv to generate configuration files for dnsmasq.

Edit /etc/resolvconf.conf and add the loopback addresses as name servers, and configure openresolv to write out dnsmasq configuration:

Run resolvconf -u so that the configuration files get created. If the files do not exist dnsmasq.service will fail to start.

Edit dnsmasq's configuration file to use openresolv's generated configuration[1]:

First you must set localhost addresses as the only nameservers in /etc/resolv.conf:

Make sure to protect /etc/resolv.conf from modification as described in Domain name resolution#Overwriting of /etc/resolv.conf.

This article or section is a candidate for merging with NetworkManager#Setting custom DNS servers in a connection (nmcli / connection file).

Alternatively, NetworkManager may be configured to automatically generate the /etc/resolv.conf file for a specific connection with the following commands:

Then restart NetworkManager.service.

The upstream DNS server addresses must then be specified in dnsmasq's configuration file as server=server_address. Also add no-resolv so dnsmasq does not needlessly read /etc/resolv.conf which only contains the localhost addresses of itself.

Now DNS queries will be resolved with dnsmasq, only checking external servers if it cannot answer the query from its cache.

You can assign a domain simply by adding:

Alternatively, if you continue to use add a custom domain to hosts in your (local) network:

In this example it is possible to ping a host/device (e.g. defined in your /etc/hosts file) as hostname.home.arpa.

Uncomment expand-hosts to add the custom domain to hosts entries:

Without this setting, you will have to add the domain to entries of /etc/hosts.

To do a lookup speed test choose a website that has not been visited since dnsmasq has been started (drill is part of the ldns package):

Running the command again will use the cached DNS IP and result in a faster lookup time if dnsmasq is setup correctly:

To test if DNSSEC validation is working see DNSSEC#Test the local validating resolver.

This article or section needs expansion.

By default dnsmasq has the DHCP functionality turned off, if you want to use it you must turn it on. Here are the important settings:

See dnsmasq(8) for more options.

In case there is already a DHCP server running on the network and you want to interoperate with it, dnsmasq can be set to behave as a "proxy DHCP", therefore only serving the #PXE server specific information to the client. This mode is only available with IPv4. Use the following syntax, providing the existing DHCP server address:

From a computer that is connected to the one with dnsmasq on it, configure it to use DHCP for automatic IP address assignment, then attempt to log into the network normally.

If you inspect the /var/lib/misc/dnsmasq.leases file on the server, you should be able to see the lease.

dnsmasq has built-in TFTP server.

To use it, create a root directory for TFTP (e.g. /srv/tftp) to put transferable files in.

For increased security it is advised to use dnsmasq's TFTP secure mode. In secure mode only files owned by the dnsmasq user will be served over TFTP. You will need to chown TFTP root and all files in it to dnsmasq user to use this feature.

See dnsmasq(8) for more options.

PXE requires a DHCP and a TFTP server; both can be provided by dnsmasq. To setup the PXE server, follow these steps:

To simply send one file:

To send a file depending on client architecture:

In case pxe-service does not work to identify the architecture (especially for UEFI-based clients), combination of dhcp-match and dhcp-boot can be used. See RFC 4578 2.1 for more client-arch numbers for use with dhcp boot protocol.

See dnsmasq(8) for more options.

The rest is up to the boot loader.

To prevent OpenDNS from redirecting all Google queries to their own search server, add to /etc/dnsmasq.conf:

In some cases, such as when operating a captive portal, it can be useful to resolve specific domains names to a hard-coded set of addresses. This is done with the address config:

Furthermore, it is possible to return a specific address for all domain names that are not answered from /etc/hosts or DHCP by using a special wildcard:

If we want two or more dnsmasq servers works per interface(s).

To do this staticly, server per interface, use interface and bind-interfaces options. This enforce start second dnsmasq.

In this case we can exclude per interface and bind any others:

To blocklist domains, i.e. answer queries for them with NXDOMAIN, use the address option without specifying the IP address:

Wildcards are also supported. Add a * to the start of the pattern:

Some specific subdomains can be unblocked using # as the server address:

For ease of use place the blocklist in a separate file, e.g. /etc/dnsmasq.d/blocklist.conf and load it from /etc/dnsmasq.conf with conf-file=/etc/dnsmasq.d/blocklist.conf or conf-dir=/etc/dnsmasq.d/,*.conf.

Cache statistics can be queried using chaos requests, using the drill utility from the ldns package:

The output will respectively contain the number of cache misses and hits:

Other options are cachesize.bind, insertions.bind, evictions.bind, auth.bind and servers.bind.

**Examples:**

Example 1 (unknown):
```unknown
dnsmasq.service
```

Example 2 (unknown):
```unknown
/etc/resolv.conf
```

Example 3 (unknown):
```unknown
/etc/dnsmasq.conf
```

Example 4 (unknown):
```unknown
dnsmasq.service
```

---

## SSH keys

**URL:** https://wiki.archlinux.org/title/Using_SSH_Keys

**Contents:**
- Background
- Generating an SSH key pair
  - Choosing the authentication key type
    - Ed25519
    - ECDSA
    - RSA
    - FIDO/U2F
      - resident
      - no-touch-required
  - Choosing the key location and passphrase

This article or section needs expansion.

SSH keys can serve as a means of identifying yourself to an SSH server using public-key cryptography and challenge-response authentication. The major advantage of key-based authentication is that, in contrast to password authentication, it is not prone to brute-force attacks, and you do not expose valid credentials if the server has been compromised (see RFC 4251 9.4.4).

Furthermore, SSH key authentication can be more convenient than the more traditional password authentication. When used with a program known as an SSH agent, SSH keys can allow you to connect to a server, or multiple servers, without having to remember or enter your password for each system.

Key-based authentication is not without its drawbacks and may not be appropriate for all environments, but in many circumstances it can offer some strong advantages. A general understanding of how SSH keys work will help you decide how and when to use them to meet your needs.

This article assumes you already have a basic understanding of the Secure Shell protocol and have installed the openssh package.

SSH keys are always generated in pairs with one known as the private key and the other as the public key. The private key is known only to you and it should be safely guarded. By contrast, the public key can be shared freely with any SSH server to which you wish to connect.

If an SSH server has your public key on file and sees you requesting a connection, it uses your public key to construct and send you a challenge. This challenge is an encrypted message and it must be met with the appropriate response before the server will grant you access. What makes this coded message particularly secure is that it can only be understood by the private key holder. While the public key can be used to encrypt the message, it cannot be used to decrypt that very same message. Only you, the holder of the private key, will be able to correctly understand the challenge and produce the proper response.

This challenge-response phase happens behind the scenes and is invisible to the user. As long as you hold the private key, which is typically stored in the ~/.ssh/ directory, your SSH client should be able to reply with the appropriate response to the server.

A private key is a guarded secret and as such it is advisable to store it on disk in an encrypted form. When the encrypted private key is required, a passphrase must first be entered in order to decrypt it. While this might superficially appear as though you are providing a login password to the SSH server, the passphrase is only used to decrypt the private key on the local system. The passphrase is not transmitted over the network.

An SSH key pair can be generated by running the ssh-keygen command, see the ssh-keygen(1) man page for what is "generally considered sufficient" and should be compatible with virtually all clients and servers:

The randomart image was introduced in OpenSSH 5.1 as an easier means of visually identifying the key fingerprint.

You can also add an optional comment field to the public key with the -C switch, to more easily identify it in places such as ~/.ssh/known_hosts, ~/.ssh/authorized_keys and ssh-add -L output. For example:

will add a comment saying which user created the key on which machine and when.

OpenSSH supports several signing algorithms (for authentication keys) which can be divided in two groups depending on the mathematical properties they exploit:

Elliptic curve cryptography (ECC) algorithms are a more recent addition to public key cryptosystems. One of their main advantages is their ability to provide the same level of security with smaller keys, which makes for less computationally intensive operations (i.e. faster key creation, encryption and decryption) and reduced storage and transmission requirements.

DSA keys are deprecated due to their security weaknesses and most SSH implementations do not support them anymore. Dropbear 2022.83 disabled DSA key support while OpenSSH 10.0 and libssh 0.11.0 removed support for DSA keys entirely. Therefore the choice of cryptosystem lies within RSA or one of the two types of ECC.

The default Ed25519 will give you the best security and good performance. ECDSA is slower than Ed25519, but faster than RSA; concerns exist about its security (see below). RSA keys will give you the greatest compatibility with old servers, but it requires a larger key size to provide sufficient security.

Ed25519 was introduced in OpenSSH 6.5 of January 2014: "Ed25519 is an elliptic curve signature scheme that offers better security than ECDSA and DSA and good performance". Its main strengths are its speed, its constant-time run time (and resistance against side-channel attacks), and its lack of nebulous hard-coded constants.[1] See also this blog post by a Mozilla developer on how it works.

It is implemented in many applications and libraries and is the default key type in ssh-keygen(1) and dropbearkey(1).

ssh-keygen(1) defaults to Ed25519 therefore there is no need to specify it with the -t ed25519 option. The key pairs can be simply generated with:

There is no need to set the key size, as all Ed25519 keys are 256 bits.

Keep in mind that ancient SSH clients and servers may not support these keys.

The Elliptic Curve Digital Signature Algorithm (ECDSA) was the preferred algorithm for authentication (key exchange algorithm) from OpenSSH 5.7 (2011-01-24) to OpenSSH 6.5 (2014-01-30).

There are two sorts of concerns with it:

Both of those concerns are best summarized in libssh curve25519 introduction. Although the political concerns will always be subject to debate, there is a clear consensus that #Ed25519 is technically superior and should therefore be preferred.

ECDSA key pairs can be generated with:

Three elliptic curve sizes are supported for ECDSA keys: 256, 384 and 521 bits. The default is 256 bits. If you wish to generate a stronger ECDSA key pair, simply specify the -b option:

RSA provides the best compatibility of all algorithms but requires the key size to be larger to provide sufficient security. Minimum key size is 1024 bits, default is 3072 (see ssh-keygen(1)) and maximum is 16384.

RSA key pairs can be generated with:

If you wish to generate a stronger RSA key pair (e.g. to guard against cutting-edge or unknown attacks and more sophisticated attackers), simply specify the -b option with a higher bit value than the default:

Be aware though that there are diminishing returns in using longer keys.[2][3] The GnuPG FAQ reads: "If you need more security than RSA-2048 offers, the way to go would be to switch to elliptical curve cryptography — not to continue using RSA."[4]

On the other hand, the latest iteration of the NSA Fact Sheet Suite B Cryptography suggests a minimum 3072-bit modulus for RSA while "[preparing] for the upcoming quantum resistant algorithm transition".[5]

FIDO/U2F hardware authenticator support was added in OpenSSH version 8.2 for both of the elliptic curve signature schemes mentioned above. It allows for a hardware token attached via USB or other means to act a second factor alongside the private key.

The libfido2 is required for hardware token support.

After attaching a compatible FIDO key, a key pair may be generated with:

You will usually be required to enter your PIN and/or tap your token to confirm the generation.

By default, the generated SSH key consist of two parts: a key handle on disk, and a private key that is unique for each security key. To easily move your FIDO key between machines, generate a key with the ssh-keygen(1) § resident option, -O resident. This indicates "that the key handle should be stored on the FIDO authenticator itself." [6]

Afterwards, on a new machine, the key can be downloaded using ssh-keygen(1) § K

Connecting to a server will usually require tapping your token unless the -O no-touch-required command line option is used during generation and the sshd(8) § no-touch-required authorized_keys option is set on the server.

To create keys that do not require touch events, generate a key pair with the no-touch-required option. For example:

Additionally, sshd rejects no-touch-required keys by default. To allow keys generated with this option, either enable it for an individual key in the authorized_keys file:

Or for the whole system by editing /etc/ssh/sshd_config with:

An ECDSA-based keypair may also be generated with the ecdsa-sk keytype, but the relevant concerns in the #ECDSA section above still apply.

Upon issuing the ssh-keygen command, you will be prompted for the desired name and location of your private key. By default, keys are stored in the ~/.ssh/ directory and named according to the type of encryption used. You are advised to accept the default name and location in order for later code examples in this article to work properly.

When prompted for a passphrase, choose something that will be hard to guess if you have the security of your private key in mind. A longer, more random password will generally be stronger and harder to crack should it fall into the wrong hands.

It is also possible to create your private key without a passphrase. While this can be convenient, you need to be aware of the associated risks. Without a passphrase, your private key will be stored on disk in an unencrypted form. Anyone who gains access to your private key file will then be able to assume your identity on any SSH server to which you connect using key-based authentication. Furthermore, without a passphrase, you must also trust the root user, as they can bypass file permissions and will be able to access your unencrypted private key file at any time.

If the originally chosen SSH key passphrase is undesirable or must be changed, one can use the ssh-keygen command to change the passphrase without changing the actual key. This can also be used to change the password encoding format to the new standard.

If you have multiple SSH identities, you can set different keys to be used for different hosts or remote users by using the Host and IdentityFile directives in your configuration:

See ssh_config(5) for full description of these options.

SSH keys can also be stored on a security token like a smart card or a USB token. This has the advantage that the private key is stored securely on the token instead of being stored on disk. When using a security token the sensitive private key is also never present in the RAM of the PC; the cryptographic operations are performed on the token itself. A cryptographic token has the additional advantage that it is not bound to a single computer; it can easily be removed from the computer and carried around to be used on other computers.

Examples of hardware tokens are described in:

This article or section needs expansion.

Once you have generated a key pair, you will need to copy the public key to the remote server so that it will use SSH key authentication. The public key file shares the same name as the private key except that it is appended with a .pub extension. Note that the private key is not shared and remains on the local machine.

If your key file is ~/.ssh/id_rsa.pub you can simply enter the following command.

If your username differs on remote machine, be sure to prepend the username followed by @ to the server name.

If your public key filename is anything other than the default of ~/.ssh/id_rsa.pub you will get an error stating /usr/bin/ssh-copy-id: ERROR: No identities found. In this case, you must explicitly provide the location of the public key.

If the ssh server is listening on a port other than default of 22, be sure to include it within the host argument.

By default, for OpenSSH, the public key needs to be concatenated with ~/.ssh/authorized_keys. Begin by copying the public key to the remote server.

The above example copies the public key (id_ecdsa.pub) to your home directory on the remote server via scp. Do not forget to include the : at the end of the server address. Also note that the name of your public key may differ from the example given.

On the remote server, you will need to create the ~/.ssh directory if it does not yet exist and append your public key to the authorized_keys file.

The last two commands remove the public key file from the server and set the permissions on the authorized_keys file such that it is only readable and writable by you, the owner.

If your private key is encrypted with a passphrase, this passphrase must be entered every time you attempt to connect to an SSH server using public-key authentication. Each individual invocation of ssh or scp will need the passphrase in order to decrypt your private key before authentication can proceed.

An SSH agent is a program which caches your decrypted private keys and provides them to SSH client programs on your behalf. In this arrangement, you must only provide your passphrase once, when adding your private key to the agent's cache. This facility can be of great convenience when making frequent SSH connections.

An agent is typically configured to run automatically upon login and persist for the duration of your login session. A variety of agents, front-ends, and configurations exist to achieve this effect. This section provides an overview of a number of different solutions which can be adapted to meet your specific needs.

ssh-agent is the default agent included with OpenSSH. It can be used directly or serve as the back-end to a few of the front-end solutions mentioned later in this section. When ssh-agent is run, it forks to background and prints necessary environment variables. E.g.

To make use of these variables, run the command through the eval command. Use ssh-agent -c instead if using the fish shell.

Once ssh-agent is running, you will need to add your private key to its cache:

If your private key is encrypted, ssh-add will prompt you to enter your passphrase. Once your private key has been successfully added to the agent you will be able to make SSH connections without having to enter your passphrase.

In order to start the agent automatically and make sure that only one ssh-agent process runs at a time, touch $XDG_RUNTIME_DIR/ssh-agent.env and add the following to your ~/.bashrc:

This will run an ssh-agent process if there is not one already, and save the output thereof. If there is one running already, we retrieve the cached ssh-agent output and evaluate it which will set the necessary environment variables. The lifetime of the unlocked keys is set to 1 hour.

There also exist a number of front-ends to ssh-agent and alternative agents described later in this section which avoid this problem.

If you would like your ssh agent to run when you are logged in, regardless of whether X is running, a handy ssh-agent.service is included in openssh since the version 9.4p1-3, which can be enabled as a user unit.

Then set the environment variable SSH_AUTH_SOCK to $XDG_RUNTIME_DIR/ssh-agent.socket.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

When forwarding a local ssh-agent to remote (e.g., through command-line argument ssh -A remote or through ForwardAgent yes in the configuration file), it is important for the remote machine not to overwrite the environment variable SSH_AUTH_SOCK. So if the remote machine uses a systemd unit shown previously to start the agent, SSH_AUTH_SOCK must not be set in the environment when a user is logged in through SSH. Otherwise, the forwarding may fail, and you may see errors (for example: The agent has no identities) when checking the existing keys with ssh-add -l on the remote machine.

For example, if using bash, the .bashrc could be something like:

In this way, SSH_AUTH_SOCK is only set when the current session is not an SSH login. And when this is a SSH session, SSH_AUTH_SOCK on the remote machine is then set by the local machine to make the forwarding work.

An alternative way to start ssh-agent (with, say, each X session) is described in this ssh-agent tutorial by UC Berkeley Labs. A basic use case is if you normally begin X with the startx command, you can instead prefix it with ssh-agent like so:

And so you do not even need to think about it you can put an alias in your .bash_aliases file or equivalent:

Doing it this way avoids the problem of having extraneous ssh-agent instances floating around between login sessions. Exactly one instance will live and die with the entire X session.

See the notes on using x11-ssh-askpass with ssh-add for an idea on how to immediately add your key to the agent.

This ssh-agent specializes on OpenPGP card integration. It uses private keys that are stored in OpenPGP card authentication slots.

Install openpgp-card-ssh-agent and enable and start the openpgp-card-ssh-agent.socket user unit.

Afterwards add the relevant environment variable for this agent:

The user PIN for the OpenPGP card is persisted via an org.freedesktop.secrets provider (such as GNOME Keyring, KeePassXC or KDE Wallet) by default. The PIN storage backend is configurable and extendable.

The user PIN needs to be persisted only once for each OpenPGP card. Prior to the first SSH connection with this agent, list the available SSH public keys and add their respective card identifiers:

The gpg-agent has OpenSSH Agent protocol emulation. See GnuPG#SSH agent for necessary configuration.

Keychain is a program designed to help you easily manage your SSH keys with minimal user interaction. It is implemented as a shell script which drives both ssh-agent and ssh-add. A notable feature of Keychain is that it can maintain a single ssh-agent process across multiple login sessions. This means that you only need to enter your passphrase once each time your local machine is booted.

Install the keychain package.

Add a line similar to the following to your shell configuration file, e.g. if using Bash:

In the above example,

Multiple keys can be specified on the command line, as shown in the example. By default keychain will look for key pairs in the ~/.ssh/ directory, but absolute path can be used for keys in non-standard location. You may also use the --confhost option to inform keychain to look in ~/.ssh/config for IdentityFile settings defined for particular hosts, and use these paths to locate keys.

See keychain --help or keychain(1) for details on setting keychain for other shells.

To test Keychain, simply open a new terminal emulator or log out and back in your session. It should prompt you for the passphrase of the specified private key(s) (if applicable), either using the program set in $SSH_ASKPASS or on the terminal.

Because Keychain reuses the same ssh-agent process on successive logins, you should not have to enter your passphrase the next time you log in or open a new terminal. You will only be prompted for your passphrase once each time the machine is rebooted.

The x11-ssh-askpass package provides a graphical dialog for entering your passhrase when running an X session. x11-ssh-askpass depends only on the libx11 and libxt libraries, and the appearance of x11-ssh-askpass is customizable. While it can be invoked by the ssh-add program, which will then load your decrypted keys into ssh-agent, the following instructions will, instead, configure x11-ssh-askpass to be invoked by the aforementioned Keychain script.

Install the keychain and x11-ssh-askpass packages.

Edit your ~/.xinitrc file to include the following lines, replacing the name and location of your private key if necessary. Be sure to place these commands before the line which invokes your window manager.

In the above example, the first line invokes keychain and passes the name and location of your private key. If this is not the first time keychain was invoked, the following two lines load the contents of $HOSTNAME-sh and $HOSTNAME-sh-gpg, if they exist. These files store the environment variables of the previous instance of keychain.

The ssh-add manual page specifies that, in addition to needing the DISPLAY or WAYLAND_DISPLAY variable defined, you also need SSH_ASKPASS set to the name of your askpass program (in this case x11-ssh-askpass). It bears keeping in mind that the default Arch Linux installation places the x11-ssh-askpass binary in /usr/lib/ssh/, which will not be in most people's PATH. This is a little annoying, not only when declaring the SSH_ASKPASS variable, but also when theming. You have to specify the full path everywhere. Both inconveniences can be solved simultaneously by symlinking:

This is assuming that ~/bin is in your PATH. So now in your .xinitrc, before calling your window manager, one just needs to export the SSH_ASKPASS environment variable:

and your X resources will contain something like:

Doing it this way works well with the above method on using ssh-agent as a wrapper program. You start X with ssh-agent startx and then add ssh-add to your window manager's list of start-up programs.

The appearance of the x11-ssh-askpass dialog can be customized by setting its associated X resources. Some examples are the .ad files at https://github.com/sigmavirus24/x11-ssh-askpass. See x11-ssh-askpass(1) for full details.

There are other passphrase dialog programs which can be used instead of x11-ssh-askpass. The following list provides some alternative solutions.

The pam_ssh project exists to provide a Pluggable Authentication Module (PAM) for SSH private keys. This module can provide single sign-on behavior for your SSH connections. On login, your SSH private key passphrase can be entered in place of, or in addition to, your traditional system password. Once you have been authenticated, the pam_ssh module spawns ssh-agent to store your decrypted private key for the duration of the session.

To enable single sign-on behavior at the tty login prompt, install the unofficial pam_sshAUR package.

Create a symlink to your private key file and place it in ~/.ssh/login-keys.d/. Replace the id_rsa in the example below with the name of your own private key file.

Edit the /etc/pam.d/login configuration file to include the text highlighted in bold in the example below. The order in which these lines appear is significiant and can affect login behavior.

In the above example, login authentication initially proceeds as it normally would, with the user being prompted to enter their user password. The additional auth authentication rule added to the end of the authentication stack then instructs the pam_ssh module to try to decrypt any private keys found in the ~/.ssh/login-keys.d directory. The try_first_pass option is passed to the pam_ssh module, instructing it to first try to decrypt any SSH private keys using the previously entered user password. If the user's private key passphrase and user password are the same, this should succeed and the user will not be prompted to enter the same password twice. In the case where the user's private key passphrase user password differ, the pam_ssh module will prompt the user to enter the SSH passphrase after the user password has been entered. The optional control value ensures that users without an SSH private key are still able to log in. In this way, the use of pam_ssh will be transparent to users without an SSH private key.

If you use another means of logging in, such as an X11 display manager like SLiM or XDM and you would like it to provide similar functionality, you must edit its associated PAM configuration file in a similar fashion. Packages providing support for PAM typically place a default configuration file in the /etc/pam.d/ directory.

Further details on how to use pam_ssh and a list of its options can be found in the pam_ssh(8) man page.

If you want to unlock the SSH keys or not depending on whether you use your key's passphrase or the (different!) login password, you can modify /etc/pam.d/system-auth to

For an explanation, see [8].

Work on the pam_ssh project is infrequent and the documentation provided is sparse. You should be aware of some of its limitations which are not mentioned in the package itself.

As an alternative to pam_ssh you can use pam_exec-ssh-gitAUR. It is a shell script that uses pam_exec. Help for configuration can be found upstream.

The GNOME Keyring tool can act as a wrapper around ssh-agent, providing GUI and/or automatic key unlocking. See GNOME Keyring#SSH keys for further details.

For instructions on how to use kwallet to store your SSH keys, see KDE Wallet#Using the KDE Wallet to store ssh key passphrases.

KeeAgent is a plugin for KeePass that allows SSH keys stored in a KeePass database to be used for SSH authentication by other programs.

See KeePass#Plugin installation in KeePass or install the keepass-plugin-keeagent package.

This agent can be used directly, by matching KeeAgent socket: KeePass -> Tools -> Options -> KeeAgent -> Agent mode socket file -> %XDG_RUNTIME_DIR%/keeagent.socket and environment variable: export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR"'/keeagent.socket'.

The KeePassXC fork of KeePass can act as a client for an existing SSH agent. SSH keys stored in its database can be automatically (or manually) added to the agent. It is also compatible with KeeAgent's database format.

If your private key requires a password (or, for instance, you have a hardware key with a PIN) but ssh-agent is not provided with one, ssh will fail:

One potential cause for this is ssh-agent being unable to prompt for a password. Ensure that ssh-agent has access to either a display server (via the DISPLAY environment variable) or a TTY. For some graphical environments you might only need to install x11-ssh-askpass, for other setups also follow #x11-ssh-askpass instructions.

Another cause, if using a hardware authenticator, could be the key malfunctioning or being unplugged.

There is currently an open bug that triggers with the "agent refused operation" error when using authenticator keys like ED25519-sk and ECDSA-SK that were created with the option -O verify-required. To avoid this issue, use the -o IdentityAgent=none -o IdentitiesOnly=yes option for the ssh command or add it to your ssh_config file for the relevant hosts:

**Examples:**

Example 1 (unknown):
```unknown
$ ssh-keygen
```

Example 2 (unknown):
```unknown
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/username/.ssh/id_ed25519):
Created directory '/home/username/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/username/.ssh/id_ed25519
Your public key has been saved in /home/username/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:RLy4JBv7jMK5qYhRKwHB3af0rpMKYwE2PBhALCBV3G8 username@hostname
The key's randomart image is:
+--[ED25519 256]--+
|%oooo. ..        |
|== ..o.o.        |
|==  . +o..       |
|+ o o.ooE        |
|...  *.oS        |
| o..o ..         |
|o=.. +o          |
|+o*..+o          |
|+.o+. .          |
+----[SHA256]-----+
```

Example 3 (unknown):
```unknown
~/.ssh/known_hosts
```

Example 4 (unknown):
```unknown
~/.ssh/authorized_keys
```

---

## pdnsd

**URL:** https://wiki.archlinux.org/title/Pdnsd

**Contents:**
- Installation
- Configuration
  - Format
  - DNS servers
    - DNS servers with DHCP connections
  - OpenDNS
  - Testing
  - System setup
- Tips and tricks
  - Performance settings for home broadband users

pdnsd is a DNS server designed for local caching of DNS information. Correctly configured, it can significantly increase browsing speed on a broadband connection. Compared to BIND or dnsmasq it can remember its cache after a reboot; "p" stands for persistent. See Domain name resolution#DNS servers for comparison with other DNS servers.

Install the pdnsd package.

The package comes with a sample configuration file at /usr/share/doc/pdnsd/pdnsd.conf. The customized configuration file should be created at /etc/pdnsd.conf.

The pdnsd.conf file uses a fairly simple format, but it has some differences from most other configuration files you have likely encountered. It has a collection of sections of various types. A section is started with the name of the type of section and an opening curly bracket ({) and is ended by a closing curly bracket (}). Sections cannot be nested.

Inside each block is a series of options of the following format:

Notice the semicolon at the end; unlike some formats, it is not optional.

Comments are started with either # or /*. The former goes to the end of the line, the latter continues until it reaches */.

pdnsd needs to know the address of at least one DNS server to collect DNS information from. This part of the setup differs depending on whether you have a broadband connection or dial-up. Broadband users should use the first server section as a starting point, dial-up users the second, leaving the other server sections commented out.

The rest of the server section will work without any more changes. For details on all the available options, see the pdnsd manual.

When netctl is installed, pdnsd can be notified of the ip addresses of the name servers by openresolv and the notifications become dynamic when you use Automatic switching of profiles.

To configure this feature, remove the broadband server section and update the dial-up server section with the following changes:

Edit /etc/resolvconf.conf to configure openresolv with pdnsd as one of its subscribers:

And run resolvconf -u to update /etc/pdnsd-resolv.conf with the addresses of the name servers (ignore the error message saying that the pdnsd socket cannot be accessed). This updating is only needed once before starting manually pdnsd.

The pdnsd.conf file comes with OpenDNS settings built in; you can simply remove (or comment out) the dialup and broadband sections above it (being careful not to remove the necessary global setup at the very top of the file), and then uncomment it to use OpenDNS resolution.

However, OpenDNS does some weird things to Google. You need to deny results from OpenDNS that return one of OpenDNS’s Google-proxy machines if you want to avoid this behaviour (for many people, it can increase Google requests from, say, 15ms, to 75ms+). The exact servers’ IPs change, but you can run a drill www.google.com @208.67.222.222 (provided by ldns) to find the current IPs. You will know if the query is being proxied, because the server’s name will resolve to something like google.navigation.opendns.com. On one try, these addresses were 208.67.216.230 and 208.67.216.231.

Once you know the IPs, you can replace the pdnsd.conf’s already-existant rejected IPs inside the OpenDNS server { …} declaration. Make sure you retain the prefixes.

OpenNIC is a reliable alternative to OpenDNS.

You should now have a working pdnsd daemon. Start it.

Test that it is now working.

For the second time you look up any address using 127.0.0.1, query time should be under 1 ms.

Make sure to enable pdnsd.service.

It starts right after network.target, as services that use the network rely on a working DNS, i.e. network-online.target (see the upstream explanation).

For any PC with two or more NICs to have pdnsd operational for any wired and wireless connection please configure separate profile for each NIC in pdnsd.conf by specifying correct interface.

Many users have broadband connections where the DNS server is slow or unreliable, and would like to use pdnsd as a caching server to minimize the number of DNS queries that need to be made. After doing the setup detailed above, the following settings in the /etc/pdnsd.conf will help improve the performance in this role:

Under global settings:

Under server settings:

The neg_rrs_pol=on; policy means that when a negative response comes back for a query, pdnsd server will still cache the result even if the response is not "authoritative". This is important since watching DNS queries will reveal that there are many requests for AAAA records (DNS queries for IPv6) which will never return results since many domains are not using IPv6, as well as MX records since not every domain has an MX record. Without the negative caching, these requests will be sent even after a domain name has been cached, and in this role you do not want the extra DNS requests being made. It is important to use this option in conjunction with the proxy_only=on; option to minimize the number of queries coming out of the system.

The par_queries=1; option is useful if you specify more than one DNS server in your "server" section below. It specifies an increment of how many parallel queries will be made at once. For example, if four DNS servers are listed in the "server" section, and par_queries=2; (the default), then the first 2 servers will be queried simultaneously, and if both of the first two servers fail, pdnsd will move on to the next two and query them simultaneously. The setting used above means that one DNS server at a time gets queried, so you can list two or more DNS servers in the "server" section, and the second one will only be queried if the first one fails. This helps minimize traffic, but if the first server fails you will have to wait through the timeout before the second server will be queried. Tweak this setting for your own preferences, and if you only specify one server in the "server" section then you do not need to worry about it.

The proxy_only=on; setting is mentioned below in the FAQ and is important for home broadband users since you generally are using only one or two DNS servers instead of trying to do the full-blown hierarchical name resolution that a full DNS server would do. This setting will prevent pdnsd from resolving all the way back to the "authoritative" name server, and instead accept the results of the DNS servers that were already specified in the "server" section. Once again, this reduces the number of DNS queries you need to make, improving performance.

The purge_cache=off; setting tells pdnsd not to remove cache entries even if they have outlived the DNS record's time-to-live metric. This can be very useful when your ISP's DNS server goes down and you want to be able to access name lookups for domains you frequently use despite the outage. Records will still be bumped out of the cache based on age once the cache becomes full (see pdnsd.conf(5) on how to set the size of the cache).

Each DNS resource record returned from a server includes a maximum time-to-live, or TTL. This tells the recipient how long to store the record and when to do a new lookup on it. Many DNS records have relatively short TTLs, such as 3600 (one hour). This means that after one hour, pdnsd will attempt a new lookup on this entry, regardless of whether it has a cached record for it available. It will improve performance to override this default TTL by setting a global minimum TTL, causing fewer lookups to be performed. The disadvantage to using a minimum TTL that is too long is that a cached record may be out of date (the IP address of the host may be changed, but your client will not know this because it will receive the cached address). However, most IP addresses do not change hourly or even daily.

Times are specified in seconds by default, or you may append an "m", "h", "d", or "w" to the time to specify minutes, hours, days, or weeks.

min_ttl in the global settings sets a minimum TTL for cached records, causing pdnsd to ignore the default TTL in the record received from the server. On a slow connection or with a slow DNS server, you may want to set this to several hours to reduce the number of lookups (eg min_ttl=6h;).

neg_ttl in the global settings sets a minimum TTL for non-existent domains. If a server tells pdnsd that a domain does not exist, it will not try to lookup that domain again until this amount of time has elapsed.

Setting shorter timeouts means that pdnsd will give up on an entire query or a given server query more quickly, resulting in faster performance. The disadvantage to setting timeouts too short is that pdnsd might return an error on a lookup simply because the server was not given enough time to respond.

timeout in the global settings determines when pdnsd gives up on an entire query and returns an error to your browser or other client. Setting the global timeout option makes it possible to specify quite short timeout intervals in the server sections (see below). This will have the effect that pdnsd will start querying additional servers fairly quickly if the first servers are slow to respond (but will still continue to listen for responses from the first ones). (If you use query_method=tcp_udp it is recommended that you make the global timeout at least twice as large as the largest server timeout, otherwise pdnsd may not have time to try a UDP query if a TCP connection times out.)

tcp_qtimeout in the global settings determines how long a TCP query connection may be left open.

timeout in the server settings determines how long pdnsd will wait for a response from each server. Setting this to a shorter time means that pdnsd will give up on a non-responsive server more quickly and will move on to the next available server, sometimes resulting in a faster overall response time. On a fast connection, setting this to 4 or 5 seconds is not unreasonable.

To see what servers pdnsd is using for a particular lookup, how timeouts are working, and what default TTLs are being used by domains, turn debug on in the global settings:

Restart pdnsd and monitor the pdnsd.service for changes with the systemd journal:

Be sure to turn debug off for general use as leaving it on may degrade performance.

By default, pdnsd will automatically create authoritative records for all entries in /etc/hosts. If you have a lot of entries, for example if you are using it for ad blocking, the default maximum cache size provided by /etc/pdnsd.conf may not be large enough, resulting in DNS requests not being cached for their expected amount of time.

To increase the cache size, edit the perm_cache line in the 'global settings' section of configuration file (size in kB).

Alternatively, you can prevent pdnsd from preemptively sourcing your hosts file by adding the option authrec=off to the 'source' section. If, for whatever reason, setting authrec to off does not work, an easy workaround is to create a separate hosts file (eg /etc/hosts-pdnsd) with only your system information and point your 'source' section to that instead, while leaving your original hosts file intact. This way, pdnsd will reference /etc/hosts only when performing lookups. So for example:

If you have several computers on your network, you may want to make pdnsd the DNS server for them all. This allows your entire network to share a single DNS cache, making repeated lookups much faster. To allow this, simply set server_ip in the global section to the name of your network interface (usually eth0). If you have set up a firewall, tell it to allow connections to port 53 from any address on your network.

Now you can configure the other computers on your network to use the computer running pdns as their primary dns server.

pdnsd allows you to specify hosts or domains that it should never return results for. This allows you to use it as a primitive ad or content blocker, among other things. Create a new neg section in pdnsd.conf. neg sections have two main options. name is the name of the host or domain you want to block. types can be set to domain to block all hosts in the given domain. The default pdnsd.conf gives an example that blocks all ads from doubleclick.net.

Since there can only be one domain set per block, this does not scale well for blocking ads, trackers or malicious content directly in pdnsd.conf. You may want to create separate configuration files specifically for these lists, e.g., /etc/pdnsd.d/spam_domains and add an include section in pdnsd.conf like

Alternatively, it is possible to add a source section (additional to the existing one that loads /etc/hosts), that loads a file in /etc/hosts format that binds domains to the special IP-Address 0.0.0.0 – but this will not block subdomains since /etc/hosts does not allow wildcards. Doing this is equivalent to adding the rules to /etc/hosts but it avoids having a huge /etc/hosts which can break some applications.

From pdnsd-ctl(8) § DESCRIPTION:

To do that, include the option

in the global section of the /etc/pdnsd.conf.

If you changed the cache directory in /etc/pdnsd.conf, you will have to run pdnsd-ctl with the -c option:

A couple of useful commands to get you started...

pdnsd can be used with DNSCrypt. DNSCrypt encrypts the domain name lookup. pdnsd then queries DNSCrypt when necessary. An example configuration is found in DNSCrypt#pdnsd.

You can successfully ping your ISP's dynamic DNS server, even though the log shows the following:

Check the interface configured in /etc/pdnsd.conf global section exists:

or the one in the server section:

The correct name can be found by running: ifconfig.

**Examples:**

Example 1 (unknown):
```unknown
/usr/share/doc/pdnsd/pdnsd.conf
```

Example 2 (unknown):
```unknown
/etc/pdnsd.conf
```

Example 3 (unknown):
```unknown
option_name=option_value;
```

Example 4 (unknown):
```unknown
/etc/resolv.conf
```

---

## OpenSSH

**URL:** https://wiki.archlinux.org/title/OpenSSH

**Contents:**
- Installation
- Client usage
  - Configuration
- Server usage
  - Configuration
  - Daemon management
    - Socket activation
  - Protection
    - Force public key authentication
    - Two-factor authentication and public keys

OpenSSH (OpenBSD Secure Shell) is a set of computer programs providing encrypted communication sessions over a computer network using the Secure Shell (SSH) protocol. It was created as an open source alternative to the proprietary Secure Shell software suite offered by SSH Communications Security. OpenSSH is developed as part of the OpenBSD project, which is led by Theo de Raadt.

OpenSSH is occasionally confused with the similarly-named OpenSSL; however, the projects have different purposes and are developed by different teams, the similar name is drawn only from similar goals.

Install the openssh package.

To connect to a server, run:

If the server only allows public-key authentication, follow SSH keys.

This article or section needs expansion.

The client can be configured to store common options and hosts. All options can be declared globally or restricted to specific hosts. For example:

With such a configuration, the following commands are equivalent

See ssh_config(5) for more information.

Some options do not have command line switch equivalents, but you can specify configuration options on the command line with -o. For example -oKexAlgorithms=+diffie-hellman-group1-sha1.

This article or section needs expansion.

sshd is the OpenSSH server daemon, configured with /etc/ssh/sshd_config and managed by sshd.service. Whenever changing the configuration, use sshd in test mode before restarting the service to ensure it will be able to start cleanly. Valid configurations produce no output.

To allow access only for some users, add this line:

To allow access only for some groups:

To add a nice welcome message (e.g. from the /etc/issue file), configure the Banner option:

Public and private host keys are automatically generated in /etc/ssh by the sshdgenkeys service and regenerated if missing even if HostKeyAlgorithms option in sshd_config allows only some. Three key pairs are provided based on the algorithms ed25519, ecdsa and rsa. To have sshd use a particular key, specify the following option:

If the server is to be exposed to the WAN, it is recommended to change the default port from 22 to a random higher one like this:

Start/enable sshd.service. It will keep the SSH daemon permanently active and fork for each incoming connection.

openssh 8.0p1-3 removed sshd.socket that used systemd's socket activation due to it being susceptible to denial of service. See FS#62248 for details. If sshd.socket is enabled when updating to openssh 8.0p1-3, the sshd.socket and sshd@.service units will be copied to /etc/systemd/system/ and reenabled. This is only done to not break existing setups; users are still advised to migrate to sshd.service.

Using sshd.socket negates the ListenAddress setting, so it will allow connections over any address. To achieve the effect of setting ListenAddress, you must specify the port and IP for ListenStream (e.g. ListenStream=192.168.1.100:22) by editing sshd.socket. You must also add FreeBind=true under [Socket] or else setting the IP address will have the same drawback as setting ListenAddress: the socket will fail to start if the network is not up in time.

When using socket activation, a transient instance of sshd@.service will be started for each connection (with different instance names). Therefore, neither sshd.socket nor the daemon's regular sshd.service allow to monitor connection attempts in the log. The logs of socket-activated instances of SSH can be seen by running journalctl -u "sshd@*" as root or by running journalctl /usr/bin/sshd as root.

Allowing remote log-on through SSH is good for administrative purposes, but can pose a threat to your server's security. Often the target of brute force attacks, SSH access needs to be limited properly to prevent third parties gaining access to your server.

ssh-audit offers an automated analysis of server and client configuration. Several other good guides and tools are available on the topic, for example:

If a client cannot authenticate through a public key, by default, the SSH server falls back to password authentication, thus allowing a malicious user to attempt to gain access by brute-forcing the password. One of the most effective ways to protect against this attack is to disable password logins entirely, and force the use of SSH keys. This can be accomplished by setting the following options in the daemon configuration file:

SSH can be set up to require multiple ways of authentication; you can tell which authentication methods are required using the AuthenticationMethods option. This enables you to use public keys as well as a two-factor authorization.

See Google Authenticator to set up Google Authenticator.

For Duo, install duo_unixAUR which will supply the pam_duo.so module. Read the Duo Unix documentation for instructions on how to setup the necessary Duo credentials (Integration Key, Secret Key, API Hostname).

The factual accuracy of this article or section is disputed.

To use PAM with OpenSSH, edit the following files:

Then you can log in with either a publickey or the user authentication as required by your PAM setup.

If, on the other hand, you want to authenticate the user on both a publickey and the user authentication as required by your PAM setup, use a comma instead of a space to separate the AuthenticationMethods:

With required pubkey and pam authentication, you may wish to disable the password requirement:

Brute forcing is a simple concept: one continuously tries to log in to a webpage or server log-in prompt like SSH with a high number of random username and password combinations.

See ufw#Rate limiting with ufw or Simple stateful firewall#Bruteforce attacks for iptables.

Since 9.8 a basic protection similar to fail2ban is implemented: the option PerSourcePenalties is set with reasonable default values. Penalties for various conditions are enforced against a client on its source address, resulting in a refused connection for a time period.

Alternatively, you can protect yourself from brute force attacks by using an automated script that blocks anybody trying to brute force their way in.

This article or section is out of date.

It is generally considered bad practice to allow the root user to log in without restraint over SSH. There are two methods by which SSH root access can be restricted for increased security.

Sudo selectively provides root rights for actions requiring these without requiring authenticating against the root account. This allows locking the root account against access via SSH and potentially functions as a security measure against brute force attacks, since now an attacker must guess the account name in addition to the password.

SSH can be configured to deny remote logins with the root user by editing the "Authentication" section in the daemon configuration file. Simply set PermitRootLogin to no:

Next, restart the SSH daemon.

You will now be unable to log in through SSH under root, but will still be able to log in with your normal user and use su or sudo to do system administration.

Some automated tasks such as remote, full-system backup require full root access. To allow these in a secure way, instead of disabling root login via SSH, it is possible to only allow root logins for selected commands. This can be achieved by editing ~root/.ssh/authorized_keys, by prefixing the desired key, e.g. as follows:

This will allow any login with this specific key only to execute the command specified between the quotes.

The increased attack surface created by exposing the root user name at login can be compensated by adding the following to sshd_config:

This setting will not only restrict the commands which root may execute via SSH, but it will also disable the use of passwords, forcing use of public key authentication for the root account.

A slightly less restrictive alternative will allow any command for root, but makes brute force attacks infeasible by enforcing public key authentication. For this option, set:

If, for whatever reason, you think that the user in question should not be able to add or change existing keys, you can prevent them from manipulating the file.

On the server, make the authorized_keys file read-only for the user and deny all other permissions:

To prevent the user from simply changing the permissions back, set the immutable bit on the authorized_keys file. To prevent the user from renaming the ~/.ssh directory and creating a new ~/.ssh directory and authorized_keys file, set the immutable bit on the ~/.ssh directory too. To add or remove keys, you will have to remove the immutable bit from authorized_keys and make it writable temporarily.

While common SSH keys and manual fingerprint verification may be easy to use with a handful of hosts that are managed by a single administrator, this method of authentication does not scale at all. When a number of servers need to be accessed through SSH by several users, manually verifying ssh public key fingerprints of every host becomes nearly impossible to do securely and reliably.

The solution for this is to use SSH certificates that provide automatic verification of public key identities through a chain of trust that scales significantly better than the default trust-on-first-use approach of SSH. SSH certificates are basically nothing else than normal public SSH keys, but with an additional signature from a trusted certificate authority that verifies the key identity.

The private certificate authority key should be stored securely, ideally on a smartcard or hardware token that prevents key extraction like the Nitrokey or YubiKey.

Copy the public server key to your local system containing the private certificate authority key to sign it:

The generated certificate ssh_host_ed25519_key-cert.pub should be copied to the server at /etc/ssh/.

Depending on the number of users and method of deployment, SSH User keys can also be used with Certificates. For organizations with many ssh users, this is strongly advised to manage User key deployment securely.

The deployment of user certificates works basically the same as for server identities. More details and instructions can be found at Wikibooks:OpenSSH/Cookbook/Certificate-based Authentication.

Automated deployment of SSH certificates can be provided by a number of open source tools. Popular examples are:

The Secure Shell fingerprint record (SSHFP) is an optional resource record in the domain name system that associates SSH keys to a host name. It can be used to verify the SSH fingerprint on public servers by using DNSSEC instead of deploying trusted CA certificates, which allows even unmanaged clients to verify the validity of key fingerprints.

To generate the required hexadecimal key fingerprint to be stored in the DNS record, create the hash on the target server.

This will read all available SSH keys for the specified domain and output valid SSHFP records that can then be stored in the DNS entries of the affected domain.

In order to automatically retrieve and trust SSH key fingerprints stored as SSHFP records, add the following to your ssh client configuration file:

If the target host has a valid SSHFP record and this record is verified with a valid DNSSEC signature, the fingerprint is automatically accepted without prompting the user to verify the hosts identity. In case the DNS record is not verified by DNSSEC, the user will be prompted to verify the fingerprint instead.

To determine the SSH fingerprint of a specific domain, use ssh-keyscan to retrieve the ssh fingerprints in a valid DNS record format. (Note that by default fingerprints for every available key type is provided as both SHA1 and SHA256.)

Since the SSHFP record stores the key fingerprints as hexadecimal values while the common output for SSH fingerprints is the base64 encoded SHA256 hash of the public key, it is necessary to convert the record back to the base64 format in order to compare it with values in the known_hosts file or other documentation that commonly stores fingerprints as SHA256.

Example for github.com using the hex value for the sha256 fingerprint of the key type ed25519

Compare with known_hosts entries:

This can be useful for laptop users connect to unsafe wireless connections. The only requirement is an SSH server running at a somewhat secure location, like your home or at work. It might be useful to use a dynamic DNS service like DynDNS so you do not have to remember your IP address.

The N flag disables the interactive prompt, and the D flag specifies the local port on which to listen on (you can choose any port number). The T flag disables pseudo-tty allocation.

Perhaps add the verbose (-v) flag, to verify the connection.

The above step is useful only in combination with a web browser or another program. Since SSH supports both SOCKS v4 and SOCKS v5, you can use either.

This is more complicated initially, but results in you not having to manually configure every application to use the SOCKS proxy. It requires setting up a local TUN interface and routing traffic through it.

See VPN over SSH#Set up badvpn and tunnel interface.

X11 forwarding is a mechanism that allows graphical interfaces of X11 programs running on a remote system to be displayed on a local client machine. For X11 forwarding the remote host does not need to have a full X11 system installed; however, it needs at least to have xauth installed. xauth is a utility that maintains Xauthority configurations used by server and client for authentication of X11 session (source).

Log on to the remote machine normally, specifying the -X switch if ForwardX11 was not enabled in the client's configuration file:

If you receive errors trying to run graphical applications, try ForwardX11Trusted instead:

Given the output X11 forwarding request failed, redo the setup for your remote machine. Once the X11 forwarding request succeeds, you can start any X program on the remote server, and it will be forwarded to your local session:

Error output containing Can't open display indicates that DISPLAY is improperly set.

Be careful with some applications as they check for a running instance on the local machine. Firefox is an example: either close the running Firefox instance or use the following start parameter to start a remote instance on the local machine:

If you get "X11 forwarding request failed on channel 0" when you connect (and the server /var/log/errors.log shows "Failed to allocate internet-domain X11 display socket"), make sure package xorg-xauth is installed. If its installation is not working, try to either:

Setting it to inet may fix problems with Ubuntu clients on IPv4.

For running X applications as another user on the SSH server, you need to xauth add the authentication line taken from xauth list of the SSH logged in user.

In addition to SSH's built-in support for X11, it can also be used to securely tunnel any TCP connection, by use of local forwarding or remote forwarding.

Local forwarding opens a port on the local machine, connections to which will be forwarded to the remote host and from there on to a given destination. Very often, the forwarding destination will be the same as the remote host, thus providing a secure shell and, e.g. a secure VNC connection, to the same machine. Local forwarding is accomplished by means of the -L switch and it is accompanying forwarding specification in the form of <tunnel port>:<destination address>:<destination port>.

will use SSH to login to and open a shell on 192.168.0.100, and will also create a tunnel from the local machine's TCP port 1000 to mail.google.com on port 25. Once established, connections to localhost:1000 will connect to the Gmail SMTP port. To Google, it will appear that any such connection (though not necessarily the data conveyed over the connection) originated from 192.168.0.100, and such data will be secure between the local machine and 192.168.0.100, but not between 192.168.0.100 and Google, unless other measures are taken.

will allow connections to localhost:2000 which will be transparently sent to the remote host on port 6001. The preceding example is useful for VNC connections using the vncserver utility--part of the tightvnc package--which, though very useful, is explicit about its lack of security.

Remote forwarding allows the remote host to connect to an arbitrary host via the SSH tunnel and the local machine, providing a functional reversal of local forwarding, and is useful for situations where, e.g., the remote host has limited connectivity due to firewalling. It is enabled with the -R switch and a forwarding specification in the form of <tunnel port>:<destination address>:<destination port>.

will bring up a shell on 192.168.0.200, and connections from 192.168.0.200 to itself on port 3000 (the remote host's localhost:3000) will be sent over the tunnel to the local machine and then on to irc.libera.chat on port 6667, thus, in this example, allowing the use of IRC programs on the remote host to be used, even if port 6667 would normally be blocked to it.

Both local and remote forwarding can be used to provide a secure "gateway", allowing other computers to take advantage of an SSH tunnel, without actually running SSH or the SSH daemon by providing a bind-address for the start of the tunnel as part of the forwarding specification, e.g. <tunnel address>:<tunnel port>:<destination address>:<destination port>. The <tunnel address> can be any address on the machine at the start of the tunnel. The address localhost allows connections via the localhost or loopback interface, and an empty address or * allow connections via any interface. By default, forwarding is limited to connections from the machine at the "beginning" of the tunnel, i.e. the <tunnel address> is set to localhost. Local forwarding requires no additional configuration; however, remote forwarding is limited by the remote server's SSH daemon configuration. See the GatewayPorts option in sshd_config(5) and -L address option in ssh(1) for more information about remote forwarding and local forwarding, respectively.

In certain scenarios, there might not be a direct connection to your target SSH daemon, and the use of a jump server (or bastion server) is required. Thus, we attempt to connect together two or more SSH tunnels, and assuming your local keys are authorized against each server in the chain. This is possible using SSH agent forwarding (-A) and pseudo-terminal allocation (-t) which forwards your local key with the following syntax:

This can be automated with the ProxyCommand option:

An easier and more secure way to do this is using the ProxyJump option with the -J flag:

Multiple hosts in the -J directive can be separated with a comma; they will be connected to in the order listed. The user...@ part is not required, but can be used. The host specifications for -J use the ssh configuration file, so specific per-host options can be set there, if needed.

The main difference between the ProxyCommand and ProxyJump options is that the later does not require a shell on the jumphost. Consequently, this also means that the jumpserver does not require access to the users login credentials or SSH agent forwarding. With the ProxyJump option, the ssh client connects through the jumpserver directly to the target server, establishing an end-to-end encrypted channel between client and target server.

An equivalent of the -J flag in the configuration file is the ProxyJump option; see ssh_config(5) for details.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

The idea is that the client connects to the server via another relay while the server is connected to the same relay using a reverse SSH tunnel. This is useful when the server is behind a NAT, and the relay is a publicly accessible SSH server used as a proxy to which the user has access. Therefore, the prerequisite is that the client's keys are authorized against both the relay and the server, and the server needs to be authorized against the relay as well for the reverse SSH connection.

The following configuration example assumes that user1 is the user account used on client, user2 on relay and user3 on server. First, assuming we will use port 2222, the server needs to establish the reverse tunnel with:

Which can also be automated with a startup script, systemd service, autossh or sidedoorAUR.

At the client side, the connection is established with:

The remote command to establish the connection to reverse tunnel can also be defined in relay's authorized_keys file by including the command field as follows:

In this case the connection is established with:

Alternatively, you can add an entry to your ssh configuration that specifies both RemoteCommand and RequestTTY:

Which will reduce connecting to:

The SSH daemon usually listens on port 22. However, it is common practice for many public internet hotspots to block all traffic that is not on the regular HTTP/S ports (80 and 443, respectively), thus effectively blocking SSH connections. The immediate solution for this is to have sshd listen additionally on one of the whitelisted ports:

However, it is likely that port 443 is already in use by a web server serving HTTPS content, in which case it is possible to use a multiplexer, such as sslh, which listens on the multiplexed port and can intelligently forward packets to many services.

There are several client configuration options which can speed up connections either globally or for specific hosts. See ssh_config(5) for full descriptions of these options.

Please refer to the SSHFS article to mount a SSH-accessible remote system to a local directory, so you will be able to do any operation on the mounted files with any tool (copy, rename, edit with vim, etc.). sshfs is generally preferred over shfs, the latter has not been updated since 2004.

By default, the SSH session automatically logs out if it has been idle for a certain time. To keep the session up, the client can send a keep-alive signal to the server if no data has been received for some time, or symmetrically the server can send messages at regular intervals if it has not heard from the client.

systemd can automatically start SSH connections on boot/login and restart them when they fail. This makes it a useful tool for maintaining SSH tunnels.

The following service can start an SSH tunnel on login using the connection settings in your ssh configuration. If the connection closes for any reason, it waits 10 seconds before restarting it:

Then enable and start the user unit. See #Keep alive for how to prevent the tunnel from timing out. If you wish to start the tunnel on boot, you might want to rewrite the unit as a system service.

When a session or tunnel cannot be kept alive, for example due to bad network conditions causing client disconnections, you can use autossh to automatically restart them.

Connecting through a SOCKS-proxy set by Proxy settings:

With the -f option autossh can be made to run as a background process. Running it this way however means the passphrase cannot be entered interactively.

The session will end once you type exit in the session, or the autossh process receives a SIGTERM, SIGINT of SIGKILL signal.

If you want to automatically start autossh, you can create a systemd unit file:

Here AUTOSSH_GATETIME=0 is an environment variable specifying how long ssh must be up before autossh considers it a successful connection, setting it to 0 autossh also ignores the first run failure of ssh. This may be useful when running autossh at boot. Other environment variables are available at autossh(1). Of course, you can make this unit more complex if necessary (see the systemd documentation for details), and obviously you can use your own options for autossh, but note that the -f implying AUTOSSH_GATETIME=0 does not work with systemd.

Remember to start and/or enable the service afterwards.

You may also need to disable ControlMaster:

For remote or headless servers which rely exclusively on SSH, a failure to start the SSH daemon (e.g., after a system upgrade) may prevent administration access. systemd offers a simple solution via OnFailure option.

Let us suppose the server runs sshd and telnet is the fail-safe alternative of choice. Create a file as follows. Do not enable telnet.socket!

That's it. Telnet is not available when sshd is running. Should sshd fail to start, a telnet session can be opened for recovery.

To better distinguish when you are on different hosts, you can set a different background color based on the kind of host.

This solution works, but is not universal (ZSH only).

You can use host configuration specific to the network you are connected to using a Match exec.

For example, when using nmcli(1), and the connection is configured (manually or through DHCP) to use a search-domain:

Another example for Match host ... exec "...": Consider that connecting to internal.example.com requires a bastion/proxy (via ProxyJump) unless you are already connected via VPN. The fragment !exec "host internal.example.com" applies only when internal.example.com cannot be looked up via DNS. Various alternatives are discussed at [3].

Because different servers on different networks are likely to share a common private IP address, you might want to handle them differently.

The factual accuracy of this article or section is disputed.

The best solution is to use the #Network specific configuration to use a different UserKnownHostsFile depending on the network you are on. The second solution, best used as default when you are working on new/prototype networks, would be to simply ignore hostkeys for private networks:

The factual accuracy of this article or section is disputed.

If you are using an interactive session, there are multiple ways to execute a command on login:

SSH agent forwarding allows you to use your local keys when connected to a server. It is recommended to only enable agent forwarding for selected hosts.

Next, configure an SSH agent and add your local key with ssh-add.

If you now connect to a remote server you will be able to connect to other services using your local keys.

New server private keys can be generated by:

You may want to run sshd as non-privileged user in containers, or for testing, etc.

Since non-privileged user cannot read host keys in /etc/ssh, new host keys must be generated:

Create an sshd_config file. The example below uses a port higher than 1024, provides a new path to the host keys and disables PAM:

Run sshd with the created config. The -D flag disables daemon mode and -e redirects output to stderr to allow easy monitoring.

Check these simple issues before you look any further.

If you are behind a NAT mode/router (which is likely unless you are on a VPS or publicly addressed host), make sure that your router is forwarding incoming ssh connections to your machine. Find the server's internal IP address with ip addr and set up your router to forward TCP on your SSH port to that IP. portforward.com can help with that.

The ss utility shows all the processes listening to a TCP port with the following command line:

If the above command do not show the system is listening to the port ssh, then SSH is not running: check the journal for errors etc.

Iptables may be blocking connections on port 22. Check this with:

and look for rules that might be dropping packets on the INPUT chain. Then, if necessary, unblock the port with a command like:

For more help configuring firewalls, see firewalls.

Start a traffic dump on the computer you are having problems with:

This should show some basic information, then wait for any matching traffic to happen before displaying it. Try your connection now. If you do not see any output when you attempt to connect, then something outside of your computer is blocking the traffic (e. g., hardware firewall, NAT router etc.).

In some cases, your ISP might block the default port (SSH port 22) so whatever you try (opening ports, hardening the stack, defending against flood attacks, et al) ends up useless. To confirm this, create a server on all interfaces (0.0.0.0) and connect remotely.

If you get an error message comparable to this:

That means the port is not being blocked by the ISP, but the server does not run SSH on that port (See security through obscurity).

However, if you get an error message comparable to this:

That means that something is rejecting your TCP traffic on port 22. Basically that port is stealth, either by your firewall or 3rd party intervention (like an ISP blocking and/or rejecting incoming traffic on port 22). If you know you are not running any firewall on your computer, and you know that Gremlins are not growing in your routers and switches, then your ISP is blocking the traffic.

To double check, you can run Wireshark on your server and listen to traffic on port 22. Since Wireshark is a Layer 2 Packet Sniffing utility, and TCP/UDP are Layer 3 and above (see IP Network stack), if you do not receive anything while connecting remotely, a third party is most likely to be blocking the traffic on that port to your server.

Install either tcpdump or Wireshark with the wireshark-cli package.

where interface is the network interface for a WAN connection (see ip a to check). If you are not receiving any packets while trying to connect remotely, you can be very sure that your ISP is blocking the incoming traffic on port 22.

The solution is just to use some other port that the ISP is not blocking. Open the /etc/ssh/sshd_config and configure the file to use different ports. For example, add:

Also make sure that other "Port" configuration lines in the file are commented out. Just commenting "Port 22" and putting "Port 1234" will not solve the issue because then sshd will only listen on port 1234. Use both lines to run the SSH server on both ports.

Restart the server sshd.service and you are almost done. You still have to configure your client(s) to use the other port instead of the default port. There are numerous solutions to that problem, but let us cover two of them here.

Recent versions of OpenSSH sometimes fail with the above error message when connecting to older ssh servers. This can be worked around by setting various client options for that host. See ssh_config(5) for more information about the following options.

The problem could be the ecdsa-sha2-nistp*-cert-v01@openssh elliptical host key algorithms. These can be disabled by setting HostKeyAlgorithms to a list excluding those algorithms. On the client side, the HostKeyAlgorithms that the client wants to use can also be set by preceding the HostKeyAlgorithms list with a - to remove the specified algorithms (including wildcards) from the default set (see ssh_config(5)). You can check the actually used host key algorithm with ssh -v server_to_connect_to in the line that contains kex: host key algorithm:.

If that does not work, it could be that the list of ciphers is too long. Set the Ciphers option to a shorter list (fewer than 80 characters should be enough). Similarly, you can also try shortening the list of MACs.

See also the discussion on the OpenSSH bug forum.

One possible cause for this is the need of certain SSH clients to find an absolute path (one returned by whereis -b [your shell], for instance) in $SHELL, even if the shell's binary is located in one of the $PATH entries.

If you receive the above errors upon logging in, this means the server does not recognize your terminal. ncurses applications like nano may fail with the message Error opening terminal.

The correct solution is to install the client terminal's terminfo file on the server. This tells console programs on the server how to correctly interact with your terminal. You can get info about current terminfo using infocmp and then find out which package owns it.

If you cannot install it normally, you can copy your terminfo to your home directory on the server:

After logging in and out from the server the problem should be fixed.

Alternatively, you can simply set TERM=xterm in your environment on the server (e.g. in .bash_profile). This will silence the error and allow ncurses applications to run again, but you may experience strange behavior and graphical glitches unless your terminal's control sequences exactly match xterm's.

If you are seeing this error in your sshd logs, make sure you have set a valid HostKey:

Since OpenSSH 8.8, scp uses SFTP as the default protocol for data transfers by requesting the subsystem named sftp. If you run scp in verbose mode, scp -v, you can determine which subsystem your client is using (e.g. Sending subsystem: <subsystem-name>). Errors such as subsystem request failed on channel 0 may be fixed by configuring the server's Subsystem settings: sshd_config(5) § Subsystem. The server configuration should resemble the example below.

OpenSSH 7.0 deprecated DSA public keys for security reasons and OpenSSH 9.8 is built without support for DSA keys by default. The first OpenSSH release of 2025 will remove DSA support entirely. For now, if you absolutely must use them, you will need to rebuild openssh while passing --enable-dsa-keys to configure.[4]

OpenSSH 7.0 deprecated the diffie-hellman-group1-sha1 key algorithm because it is weak and within theoretical range of the so-called Logjam attack (see https://www.openssh.com/legacy.html). If the key algorithm is needed for a particular host, ssh will produce an error message like this:

The best resolution for these failures is to upgrade/configure the server to not use deprecated algorithms. If that is not possible, you can force the client to reenable the algorithm with the client option KexAlgorithms +diffie-hellman-group1-sha1.

If your processes get killed at the end of the session, it is possible that you are using socket activation and it gets killed by systemd when it notices that the SSH session process exited. In that case there are two solutions. One is to avoid using socket activation by using ssh.service instead of ssh.socket. The other is to set KillMode=process in the Service section of ssh@.service.

The KillMode=process setting may also be useful with the classic ssh.service, as it avoids killing the SSH session process or the screen or tmux processes when the server gets stopped or restarted.

SSH responds to flow control commands XON and XOFF. It will freeze/hang/stop responding when you hit Ctrl+s. Use Ctrl+q to resume your session.

If you attempt to create a connection which results in a Broken pipe response for packet_write_wait, you should reattempt the connection in debug mode and see if the output ends in error:

The send packet line above indicates that the reply packet was never received. So, it follows that this is a QoS issue. To decrease the likely-hood of a packet being dropped, set IPQoS:

The reliability (0x04) type-of-service should resolve the issue, as well as 0x00 and throughput (0x08).

If a client session is no longer responding and cannot be terminated by instructing the running program (e.g. shell), you can still terminate the session by pressing Enter, ~ and . one after another in that order.

The ~ is a pseudo-terminal escape character (see ssh(1) § ESCAPE CHARACTERS), which can be added multiple times depending on the client session to terminate. For example, if you connected from A to B and then from B to C and the session from B to C freezes, you can terminate it by pressing Enter and typing ~~., which will leave you in a working session on B.

If the client warns that the key of an ssh server has changed, you should verify that the newly offered key really belongs to the server operator via an authenticated (not necessarily encrypted) channel. Then remove the old key from the known_hosts file with ssh-keygen -R $SSH_HOST and accept the new key as if it was a new server.

When connecting to hosts that do not have a terminfo entry for your terminal, for example, when using a terminal emulator whose terminfo entry is not shipped with ncurses (e.g. kitty and rxvt-unicode), or when connecting to hosts with a limited terminfo database (e.g. systems running OpenWrt), various issues will occur with software that relies on terminfo(5).

A proper solution is to place the appropriate terminfo entry on the host. If that is not feasible, an alternative is to set TERM to a value that is both supported by the remote host and compatible with the terminal.

Since OpenSSH 8.7, a custom TERM environment variable can be passed to remote hosts with a simple configuration snippet:

If you do not have the SHELL environment variable set to a full valid path (on the jump server), connection will fail with an error message simmilar to this one:

You can simply solve this by setting your SHELL to a full path name of a shell that will also be valid on the jump server or by setting a specific SHELL variable for each server in your ~/.ssh/config file.

This article or section is being considered for removal.

A hang during connection setup can be caused by MTU/fragmentation problem. Either try to find the wrong configured router/firewall, or reduce MTU size step by step on client side (poor workaround). Another workaround is to reduce initial ssh payload, by specifying only a reduced number of settings for e.g. KexAlgorithms, HostKeyAlgorithms, Ciphers, MACs.

**Examples:**

Example 1 (unknown):
```unknown
$ ssh -p port user@server-address
```

Example 2 (unknown):
```unknown
Include /etc/ssh/ssh_config.d/*.conf
```

Example 3 (unknown):
```unknown
/etc/ssh/ssh_config
```

Example 4 (unknown):
```unknown
~/.ssh/config
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Networking

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## Category:Firewalls

**URL:** https://wiki.archlinux.org/title/Firewalls

Arch Linux comes with two options for managing a firewall, neither of which is enabled automatically. The stock Linux kernel includes the netfilter packet filtering framework which can be managed by either of the following:

---

## VPN over SSH

**URL:** https://wiki.archlinux.org/title/VPN_over_SSH

**Contents:**
- Using badvpn's tun2socks
  - Start SSH dynamic SOCKS proxy
  - Set up badvpn and tunnel interface
  - Get traffic into the tunnel
- OpenSSH's built in tunneling
  - Enable forwarding for the TUN device
  - Create tun interfaces using systemd-networkd
    - Creating interfaces in SSH command
  - Start SSH
  - Troubleshooting

There are several ways to set up a Virtual Private Network through SSH. Note that, while this may be useful from time to time, it may not be a full replacement for a regular VPN. See for example [1].

badvpn is a collection of utilities for various VPN-related use cases.

First, we will set up a normal SSH dynamic socks proxy like usual:

Afterwards, we can go ahead with setting up the TUN.

Now you have a working local tun0 interface which routes all traffic going into it through the SOCKS proxy you set up earlier.

All that's left to do now is to set up a local route to get some traffic into it. Let us set up a route that routes all traffic into it. We will need three routes:

The idea behind setting the metrics specifically is because we need to ensure that the route picked to the SSH server is always direct because otherwise it would go back into the SSH tunnel which would cause a loop and we would lose the SSH connection as a result. Apart from that, we need to set an explicit DNS route because tun2socks does not tunnel UDP (required for DNS). We also need a new default route with a lower metric than your old default route so that traffic goes into the tunnel at all. With all of that said, let us get to work:

Now all traffic (except for DNS and the SSH server itself) should go through tun0.

OpenSSH has built-in TUN/TAP support using -w<local-tun-number>:<remote-tun-number>. Here, a layer 3/point-to-point/ TUN tunnel is described. It is also possible to create a layer 2/ethernet/TAP tunnel.

To enable forwarding for the TUN device, edit /etc/ssh/sshd_config and set PermitTunnel to yes, point-to-point or ethernet. Setting yes enables forwarding for both point-to-point and ethernet tunnels. See sshd_config(5) for details.

Then reload sshd.service.

Once these files are created, enable them by restarting systemd-networkd.service.

Also, you may manage tun interfaces with ip tunnel command.

SSH creates both interfaces automatically, but IP and routing should be configured after the connection is established.

or you may add keep-alive options if you are behind a NAT.

pppd can easily be used to create a tunnel through an SSH server:

When the VPN is established, you can route traffic through it. To get access to an internal network:

To route all Internet traffic through the tunnel, for example, to protect your communication on an unencrypted network, first add a route to the SSH server through your regular gateway:

Next, replace the default route with the tunnel

pvpn (package pvpnAUR) is a wrapper script around pppd over SSH.

**Examples:**

Example 1 (unknown):
```unknown
$ ssh -TND 4711 <your_user>@<SSH_server>
```

Example 2 (unknown):
```unknown
# ip tuntap add dev tun0 mode tun user <your_local_user>
# ip addr replace 10.0.0.1/24 dev tun0
# badvpn-tun2socks --tundev tun0 --netif-ipaddr 10.0.0.2 --netif-netmask 255.255.255.0 --socks-server-addr localhost:4711
```

Example 3 (unknown):
```unknown
# ip route add <IP_of_SSH_server> via <IP_of_original_gateway> metric 5
# ip route add <IP_of_DNS_server> via <IP_of_original_gateway> metric 5
# ip route add default via 10.0.0.2 metric 6
```

Example 4 (unknown):
```unknown
-w<local-tun-number>:<remote-tun-number>
```

---

## Network configuration

**URL:** https://wiki.archlinux.org/title/Ping

**Contents:**
- Check the connection
  - Ping
- Network management
  - Manual
    - iproute2
    - Static IP address
    - IP addresses
    - Routing table
  - Automatic
    - Network managers

This article describes how to configure network connections on OSI layer 3 and above. Medium-specifics are handled in the /Ethernet and /Wireless subpages.

This article or section needs expansion.

To troubleshoot a network connection, go through the following conditions and ensure that you meet them:

ping is used to test if you can reach a host.

For every reply received, the ping utility will print a line like the above until you interrupt (Ctrl+c) it interactively. For more information see the ping(8) manual. Note that computers can be configured not to respond to ICMP echo requests. [1]

If you receive an error message (see ping error indications) or no reply, this may be related to incomplete configuration, but also your default gateway or your Internet Service Provider (ISP). You can run a traceroute to further diagnose the route to the host.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

To set up a network connection, go through the following steps:

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

iproute2 is a dependency of the base meta package and provides the ip(8) command-line interface, used to manage network interfaces, IP addresses and the routing table. Be aware that configuration made using ip will be lost after a reboot. For persistent configuration, you can automate ip commands using scripts and systemd units. Also note that ip commands can generally be abbreviated, for clarity they are however spelled out in this article.

A static IP address can be configured with most standard network managers and also dhcpcd.

To manually configure a static IP address, add an IP address as described in #IP addresses, set up your routing table and configure your DNS servers.

IP addresses are managed using ip-address(8).

Add an IP address to an interface:

Delete an IP address from an interface:

Delete all addresses matching a criteria, e.g. of a specific interface:

The routing table is used to determine if you can reach an IP address directly or what gateway (router) you should use. If no other route matches the IP address, the default gateway is used.

The routing table is managed using ip-route(8).

PREFIX is either a CIDR notation or default for the default gateway.

This article or section needs expansion.

Automatic network configuration is accomplished using Dynamic Host Configuration Protocol (DHCP). The network's DHCP server provides IP address(es), the default gateway IP address(es) and optionally also DNS name servers upon request from the DHCP client.

See Router#DNS and DHCP for a DHCP server comparison table.

A network manager lets you manage network connection settings in so called network profiles to facilitate switching networks.

Network interfaces are managed by udev and configured by systemd.link(5) files. The default configuration assigns names to your network interface controllers using Predictable Network Interface Names, which prefixes interfaces names with en (wired/Ethernet), wl (wireless/WLAN), or ww (mobile broadband/WWAN). See systemd.net-naming-scheme(7).

Both wired and wireless interface names can be found via ls /sys/class/net or ip link. Note that lo is the virtual loopback interface and not used in making network connections.

Wireless device names can also be retrieved using iw dev. See also /Wireless#Get the name of the interface.

If your network interface is not listed, make sure your device driver was loaded successfully. See /Ethernet#Device driver or /Wireless#Device driver.

Network interfaces can be enabled or disabled using ip link set interface up|down, see ip-link(8).

To check the status of the interface enp2s0:

The UP in <BROADCAST,MULTICAST,UP,LOWER_UP> is what indicates the interface is up, not the later state DOWN.

This article or section needs expansion.

You can change the device name by defining the name manually with a systemd.link(5) file. The file must be ordered lexicographically before 99-default.link, for example:

Alternatively, a udev rule can be used:

These rules will be applied automatically at boot. To apply the change immediately, do a manual trigger of the udev rule on the net subsystem:

If you want to run a test on the changes made, udevadm --debug test /sys/class/net/* can be of help.

If the network card has a dynamic MAC, you can use Path (which can be checked using networkctl status interface_name):

Or, use a udev rule with DEVPATH:

To get the DEVPATH of all currently-connected devices, see where the symlinks in /sys/class/net/ lead. For example:

The device path should match both the new and old device name, since the rule may be executed more than once on bootup. For example, in the given rule, "/devices/pci*/*1c.0/*/net/en*" would be wrong since it will stop matching once the name is changed to net1. Only the system-default rule will fire the second time around, causing the name to be changed back.

If you are using a USB network device (e.g. Android phone tethering) that has a dynamic MAC address and you want to be able to use different USB ports, you could use a rule that matched depending on vendor and model ID instead:

If you would prefer to retain traditional interface names such as eth0, Predictable Network Interface Names can be disabled by changing the default NamePolicy for udev's net_setup_link built-in:

Alternatively, net_setup_link can be completely disabled by masking the corresponding udev rule:

or by adding net.ifnames=0 to the kernel parameters.

The factual accuracy of this article or section is disputed.

You can change the device MTU and queue length by defining manually with a systemd.link(5) config. For example:

Or through a udev rule:

MTUBytes: Using a value larger than 1500 (so called jumbo frames) can significantly speed up your network transfers. Note that all network interfaces, including switches in the local network, must support the same MTU in order to use jumbo frames. For PPPoE, the MTU should not be larger than 1492. You can also set MTU via systemd.netdev(5).

TransmitQueueLength: Small value for slower devices with a high latency like modem links and ISDN. High value is recommended for server connected over the high-speed internet connections that perform large data transfers.

A hostname is a unique name created to identify a machine on a network, configured in /etc/hostname—see hostname(5) and hostname(7) for details. The file can contain the system's domain name, if any. To set the hostname, edit /etc/hostname to include a single line with yourhostname:

Alternatively, using hostnamectl(1):

To temporarily set the hostname (until reboot), use hostname(1) from inetutils:

To set the "pretty" hostname and other machine metadata, see machine-info(5).

To make your machine accessible in your LAN via its hostname you can:

See netctl or systemd-networkd, or Wireless bonding.

IP aliasing is the process of adding more than one IP address to a network interface. With this, one node on a network can have multiple connections to a network, each serving a different purpose. Typical uses are virtual hosting of Web and FTP servers, or reorganizing servers without having to update any other machines (this is especially useful for nameservers).

To manually set an alias, for some NIC, use iproute2 to execute

To remove a given alias execute

Packets destined for a subnet will use the primary alias by default. If the destination IP is within a subnet of a secondary alias, then the source IP is set respectively. Consider the case where there is more than one NIC, the default routes can be listed with ip route.

Toggling promiscuous mode will make a (wireless) NIC forward all traffic it receives to the OS for further processing. This is opposite to "normal mode" where a NIC will drop frames it is not intended to receive. It is most often used for advanced network troubleshooting and packet sniffing.

If you want to enable promiscuous mode on interface enp2s0, enable promiscuous@enp2s0.service.

ss is a utility to investigate network ports and is part of the iproute2 package. It has a similar functionality to the deprecated netstat utility.

Common usage includes:

Display all TCP Sockets with service names:

Display all TCP Sockets with port numbers:

Display all UDP Sockets:

For more information see ss(8).

TCP packets contain a "window" value in their headers indicating how much data the other host may send in return. This value is represented with only 16 bits, hence the window size is at most 64KiB. TCP packets are cached for a while (they have to be reordered), and as memory is (or used to be) limited, one host could easily run out of it.

Back in 1992, as more and more memory became available, RFC:1323 was written to improve the situation: Window Scaling. The "window" value, provided in all packets, will be modified by a Scale Factor defined once, at the very beginning of the connection. That 8-bit Scale Factor allows the Window to be up to 32 times higher than the initial 64KiB.

It appears that some broken routers and firewalls on the Internet are rewriting the Scale Factor to 0 which causes misunderstandings between hosts. The Linux kernel 2.6.17 introduced a new calculation scheme generating higher Scale Factors, virtually making the aftermaths of the broken routers and firewalls more visible.

The resulting connection is at best very slow or broken.

First of all, let us make it clear: this problem is odd. In some cases, you will not be able to use TCP connections (HTTP, FTP, ...) at all and in others, you will be able to communicate with some hosts (very few).

When you have this problem, the output from dmesg is okay, logs are clean and ip addr will report normal status... and actually everything appears normal.

If you cannot browse any website, but you can ping some random hosts, chances are great that you are experiencing this problem: ping uses ICMP and is not affected by TCP problems.

You can try to use Wireshark. You might see successful UDP and ICMP communications but unsuccessful TCP communications (only to foreign hosts).

To fix it the bad way, you can change the tcp_rmem value, on which Scale Factor calculation is based. Although it should work for most hosts, it is not guaranteed, especially for very distant ones.

Simply disable Window Scaling. Since Window Scaling is a nice TCP feature, it may be uncomfortable to disable it, especially if you cannot fix the broken router. There are several ways to disable Window Scaling, and it seems that the most bulletproof way (which will work with most kernels) is to add the following line to /etc/sysctl.d/99-disable_window_scaling.conf (see also sysctl):

This problem is caused by broken routers/firewalls, so let us change them. Some users have reported that the broken router was their very own DSL router.

This section is based on the LWN article TCP window scaling and broken routers and an archived Kernel Trap article: Window Scaling on the Internet.

There are also several relevant threads on the LKML.

nss-myhostname(8) (an NSS module provided by systemd and enabled by default in /etc/nsswitch.conf) provides localhost and the local hostname resolution to an IP address. Some software may, however, still instead read /etc/hosts directly; see [4] [5] for examples.

To prevent such software from unsafely resolving the local hostname over the network, add an entry for it to the hosts(5) file:

For a system with a permanent IP address, replace 127.0.1.1 with that permanent IP address. For a system with a fully qualified domain name, insert the fully qualified domain name before the hostname (see the following link for the reasoning). For example:

**Examples:**

Example 1 (unknown):
```unknown
archlinux.org
```

Example 2 (unknown):
```unknown
$ ping www.example.com
```

Example 3 (unknown):
```unknown
PING www.example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=1 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=2 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34 (93.184.216.34): icmp_seq=3 ttl=56 time=10.683 ms
...
```

Example 4 (unknown):
```unknown
$ ip address show
```

---

## Knot Resolver

**URL:** https://wiki.archlinux.org/title/Knot_Resolver

**Contents:**
- Installation
- Configuration
  - Knot Resolver and dnsmasq
- See also

Knot Resolver (a.k.a. kresd) is a full (recursive), caching DNS resolver. It is designed to scale from small home-office networks to providing DNS servers at the scale of ISPs. Knot Resolver supports DNSSEC validation, which is enabled by default.

Install the knot-resolver package.

Start/enable kresd@1.service.

To use Knot Resolver as the local resolver, configure 127.0.0.1 and ::1 as your nameservers in resolv.conf(5). For example:

By default, the resolver will listen on 127.0.0.1 and ::1, ports 53 and 853 (DNS over TLS). If the resolver should be accessible from other hosts, configure other network interfaces in /etc/knot-resolver/kresd.conf with net.listen(). Refer to Knot Resolver documentation for more information.

If the resolver should respect entries from the /etc/hosts file, add a hints.add_hosts() line to /etc/knot-resolver/kresd.conf.

If dnsmasq is used for managing DHCP, then advertising a kresd instance works like any other external DNS server would: By adding an dhcp-option=option:dns-server,<Server Address> line to the dnsmasq configuration file.

Note that a default configuration of dnsmasq will clash with the default configuration of kresd, since both will attempt to use port 53. Disable the dnsmasq DNS functionality (port=0), or assign a different port to either service.

**Examples:**

Example 1 (unknown):
```unknown
kresd@1.service
```

Example 2 (unknown):
```unknown
/etc/resolv.conf
```

Example 3 (unknown):
```unknown
nameserver ::1
nameserver 127.0.0.1
options edns0 trust-ad
```

Example 4 (unknown):
```unknown
/etc/knot-resolver/kresd.conf
```

---
