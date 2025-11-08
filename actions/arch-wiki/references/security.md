# Arch-Wiki - Security

**Pages:** 13

---

## GnuPG

**URL:** https://wiki.archlinux.org/title/GPG

**Contents:**
- Installation
- Configuration
  - Home directory
  - Configuration files
  - Default options for new users
- Usage
  - Create a key pair
  - List keys
  - Export your public key
  - Import a public key

According to the official website:

Install the gnupg package.

This will also install pinentry, a collection of simple PIN or passphrase entry dialogs which GnuPG uses for passphrase entry. The shell script /usr/bin/pinentry determines which pinentry dialog is used, in the order described at #pinentry.

If you want to use a graphical frontend or program that integrates with GnuPG, see List of applications/Security#Encryption, signing, steganography.

The GnuPG home directory is where the GnuPG suite stores its keyrings and private keys, and reads configurations from. By default, the path used is ~/.gnupg. There are two ways to override this:

By default, the home directory has its permissions set to 700 and the files it contains have their permissions set to 600. Only the owner of the directory has permission to read, write, and access the files. This is for security purposes and should not be changed. In case this directory or any file inside it does not follow this security measure, you will get warnings about unsafe file and home directory permissions.

All of GnuPG's behavior is configurable via command line arguments. For arguments you would like to be the default, you can add them to the respective configuration file:

These two configuration files cover the common usecases, but there are more auxiliary programs in the GnuPG suite with their own options. See the GnuPG manual for a comprehensive list.

Create the desired file(s), and set their permissions to 600 as discussed in #Home directory.

Add to these files any long options you want. Do not write the two dashes, but simply the name of the option and required arguments. For example, to make GnuPG always use a keyring at a specific path, as if it was invoked as gpg --no-default-keyring --keyring keyring-path ...:

Other examples are found in #See also.

Additionally, pacman uses a different set of configuration files for package signature verification. See Pacman/Package signing for details.

If you want to setup some default options for new users, put configuration files in /etc/skel/.gnupg/. When the new user is added in system, files from here will be copied to its GnuPG home directory. There is also a simple script called addgnupghome which you can use to create new GnuPG home directories for existing users:

This will add the respective /home/user1/.gnupg/ and /home/user2/.gnupg/ and copy the files from the skeleton directory to it. Users with existing GnuPG home directory are simply skipped.

Generate a key pair by typing in a terminal:

Also add the --expert option to the command line to access more ciphers and in particular some newer elliptic curves like Curve448.

The command will prompt for answers to several questions. For general use most people will want:

To list keys in your public key ring:

To list keys in your secret key ring:

GnuPG's main usage is to ensure confidentiality of exchanged messages via public-key cryptography. With it each user distributes the public key of their keyring, which can be used by others to encrypt messages to the user. The private key must always be kept private, otherwise confidentiality is broken. See Wikipedia:Public-key cryptography for examples about the message exchange.

So, in order for others to send encrypted messages to you, they need your public key.

To generate an ASCII version of a user's public key to file public-key.asc (e.g. to distribute it by e-mail):

Alternatively, or in addition, you can use a keyserver to share your key.

In order to encrypt messages to others, as well as verify their signatures, you need their public key. To import a public key with file name public-key.asc to your public key ring:

Alternatively, try retrieving their public key via WKD (in case the domain of their email address supports it) or using a keyserver.

If you wish to import a key ID to install a specific Arch Linux package, see pacman/Package signing#Managing the keyring and Makepkg#Signature checking.

You can register your key with a public PGP key server, so that others can retrieve it without having to contact you directly:

To find out details of a key on the keyserver, without importing it, do:

To import a key from a key server:

To refresh/update the keychain with the latest version from a key server:

See OpenPGP#Keyserver for a general overview of OpenPGP keyservers and their features.

An alternative key server can be specified with the keyserver option in one of the configuration files, for instance:

A temporary use of another server is handy when the regular one does not work as it should. It can be achieved by, for example,

See OpenPGP#Web Key Directory for a general overview.

When encrypting to an email address (e.g. user@example.org), if it is not already in the local keyring, GnuPG, by default, will retrieve the public OpenPGP key using the Web Key Directory protocol (i.e. GnuPG will download the key via HTTPS from the example.org web server). For example:

To retrieve a public key and import it into your keyring, use the --locate-keys or --locate-external-keys options. The former will not do anything if the key already exists in the local keyring, while the later will always refresh the key. For example:

If you control the domain of your email address yourself and have a web server that provides HTTPS with a trusted TLS certificate, you can follow this guide to enable WKD for your domain.

You need to import a public key of a user before encrypting (option -e/--encrypt) a file or message to that recipient (option -r/--recipient). Additionally you need to create a key pair if you have not already done so.

To encrypt a file with the name doc, use:

To decrypt (option -d/--decrypt) a file with the name doc.gpg encrypted with your public key, use:

gpg will prompt you for your passphrase and then decrypt and write the data from doc.gpg to doc. If you omit the -o/--output option, gpg will write the decrypted data to stdout.

Symmetric encryption does not require the generation of a key pair and can be used to simply encrypt data with a passphrase. Simply use -c/--symmetric to perform symmetric encryption:

The following example:

To decrypt a symmetrically encrypted doc.gpg using a passphrase and output decrypted contents into the same directory as doc do:

Encrypting/decrypting a directory can be done with gpgtar(1).

To backup your private key do the following:

If the private key is protected by a passphrase, the exported key file will be protected by the same one.

GnuPG may ask you to enter the passphrase for the key. This is required, because the internal protection method of the secret key is different from the one specified by the OpenPGP protocol.[5]

To import the backup of your private key:

Revocation certificates are automatically generated for newly generated keys. These are by default located in ~/.gnupg/openpgp-revocs.d/. The filename of the certificate is the fingerprint of the key it will revoke. The revocation certificates can also be generated manually by the user later using:

This certificate can be used to revoke a key if it is ever lost or compromised. The backup will be useful if you have no longer access to the secret key and are therefore not able to generate a new revocation certificate with the above command. It is short enough to be printed out and typed in by hand if necessary.

Running the gpg --edit-key user-id command will present a menu which enables you to do most of your key management related tasks.

Type help in the edit key sub menu to show the complete list of commands. Some useful ones:

If you plan to use the same key across multiple devices, you may want to strip out your master key and only keep the bare minimum encryption subkey on less secure systems.

First, find out which subkey you want to export.

Select only that subkey to export.

At this point you could stop, but it is most likely a good idea to change the passphrase as well. Import the key into a temporary folder.

At this point, you can now use /tmp/tmp.XXXXXXXXXX/subkey.altpass.asc on your other devices.

It is good practice to set an expiration date on your subkeys, so that if you lose access to the key (e.g. you forget the passphrase) the key will not continue to be used indefinitely by others. When the key expires, it is relatively straight-forward to extend the expiration date:

You will be prompted for a new expiration date, as well as the passphrase for your secret key, which is used to sign the new expiration date.

Repeat this for any further subkeys that have expired:

Finally, save the changes and quit:

Update it to a keyserver.

Alternatively, if you use this key on multiple computers, you can export the public key (with new signed expiration dates) and import it on those machines:

There is no need to re-export your secret key or update your backups: the master secret key itself never expires, and the signature of the expiration date left on the public key and subkeys is all that is needed.

Alternatively, if you prefer to stop using subkeys entirely once they have expired, you can create new ones. Do this a few weeks in advance to allow others to update their keyring.

Create new subkey (repeat for both signing and encrypting key)

And answer the following questions it asks (see #Create a key pair for suggested settings).

Update it to a keyserver.

You will also need to export a fresh copy of your secret keys for backup purposes. See #Backup your private key for details on how to do this.

Key revocation should be performed if the key is compromised, superseded, no longer used, or you forget your passphrase. This is done by merging the key with the revocation certificate of the key.

If you have no longer access to your keypair, first import a public key to import your own key.

Then, to revoke the key, import the file saved in #Backup your revocation certificate:

Now the revocation needs to be made public. Use a keyserver to send the revoked key to a public PGP server if you used one in the past, otherwise, export the revoked key to a file and distribute it to your communication partners.

Signatures certify and timestamp documents. If the document is modified, verification of the signature will fail. Unlike encryption which uses the recipient public key to encrypt a document, signatures are created with the sender's private key. The recipient of a signed document then verifies the signature using the sender's public key.

To sign a file use the -s/--sign flag:

doc.sig contains both the compressed content of the original file doc and the signature in a binary format, but the file is not encrypted. However, you can combine signing with encrypting.

To sign a file without compressing it into binary format use:

Here both the content of the original file doc and the signature are stored in human-readable form in doc.sig.

To create a separate signature file to be distributed separately from the document or file itself, use the --detach-sig flag:

Here the signature is stored in doc.sig, but the contents of doc are not stored in it. This method is often used in distributing software projects to allow users to verify that the program has not been modified by a third party.

To verify a signature use the --verify flag:

where doc.sig is the signed file containing the signature you wish to verify.

If you are verifying a detached signature, both the signed data file and the signature file must be present when verifying. For example, to verify Arch Linux's latest iso you would do:

where archlinux-version.iso must be located in the same directory.

You can also specify the signed data file with a second argument:

If a file has been encrypted in addition to being signed, simply decrypt the file and its signature will also be verified.

This article or section needs expansion.

gpg-agent is mostly used as daemon to request and cache the password for the keychain. This is useful if GnuPG is used from an external program like a mail client. gnupg comes with systemd user sockets which are enabled by default. These sockets are gpg-agent.socket, gpg-agent-extra.socket, gpg-agent-browser.socket, gpg-agent-ssh.socket, and dirmngr.socket.

gpg-agent can be configured via ~/.gnupg/gpg-agent.conf file. The configuration options are listed in gpg-agent(1). For example you can change cache ttl for unused keys:

where XXXXX is the keygrip. You can get its value when running gpg --with-keygrip --list-secret-keys. The passphrase will be stored until gpg-agent is restarted. If you set up default-cache-ttl value, it will take precedence.

After changing the configuration, reload the agent using gpg-connect-agent:

The command should print OK.

However in some cases only the restart may not be sufficient, like when keep-screen has been added to the agent configuration. In this case you firstly need to kill the ongoing gpg-agent process and then you can restart it as was explained above.

gpg-agent can be configured via the pinentry-program stanza to use a particular pinentry user interface when prompting the user for a passphrase. For example:

There are other pinentry programs that you can choose from - see pacman -Ql pinentry | grep /usr/bin/. You may need to install the relevant optional dependencies for your chosen pinentry program.

Remember to reload the agent after making changes to the configuration.

max-cache-ttl and default-cache-ttl defines how many seconds gpg-agent should cache the passwords. To enter a password once a session, set them to something very high, for instance:

For password caching in SSH emulation mode, set default-cache-ttl-ssh and max-cache-ttl-ssh instead, for example:

Starting with GnuPG 2.1.0 the use of gpg-agent and pinentry is required, which may break backwards compatibility for passphrases piped in from STDIN using the --passphrase-fd 0 commandline option. In order to have the same type of functionality as the older releases two things must be done:

First, edit the gpg-agent configuration to allow loopback pinentry mode:

Reload the agent if it is running to let the change take effect.

Second, either the application needs to be updated to include a commandline parameter to use loopback mode like so:

...or if this is not possible, add the option to the configuration:

gpg-agent has OpenSSH agent emulation. If you already use the GnuPG suite, you might consider using its agent to also cache your SSH keys. Additionally, some users may prefer the PIN entry dialog GnuPG agent provides as part of its passphrase management.

Using gpg-agent in place of ssh-agent will not work if you use coreutils-uutilsAUR. It will always say Communication with agent failed

Set the following variables to communicate with gpg-agent instead of the default ssh-agent.

Alternatively, depend on Bash. This works for non-standard socket locations as well:

Also set the GPG_TTY and refresh the TTY in case user has switched into an X session as stated in gpg-agent(1). For example:

If you use multiple terminals simultaneously and want gpg-agent to ask for passphrase via pinentry-curses from the same terminal where the ssh command was run, add the following to the SSH configuration file. This will make the TTY to be refreshed every time an ssh command is run [11]:

Note that GPG_TTY environment variable has to be set for this to work.

Once gpg-agent is running you can use ssh-add to approve keys, following the same steps as for ssh-agent. The list of approved keys is stored in the ~/.gnupg/sshcontrol file.

Once your key is approved, you will get a pinentry dialog every time your passphrase is needed. For password caching see #Cache passwords.

You can also use your PGP key as an SSH key. This requires a key with the Authentication capability (see #Custom capabilities). There are various benefits gained by using a PGP key for SSH authentication, including:

To retrieve the public key part of your GPG/SSH key, run gpg --export-ssh-key gpg-key. If your key is authentication-capable but this command still fails with "Unusable public key", add a ! suffix ([12]).

Unless you have your GPG key on a keycard, you need to add your key to $GNUPGHOME/sshcontrol to be recognized as a SSH key. If your key is on a keycard, its keygrip is added to sshcontrol implicitly. If not, get the keygrip of your key this way:

Then edit sshcontrol like this. Adding the keygrip is a one-time action; you will not need to edit the file again, unless you are adding additional keys.

This article or section needs expansion.

It is possible to forward one's gpg-agent to a remote machine by forwarding gpg sockets to the remote machine, as explained by the GnuPG wiki.

First, add the following line to /etc/ssh/sshd_config on the remote machine to enable automatic removal of stale sockets on connect. Without this, the socket(s) on the remote machine will need to removed manually before connecting with forwarding enabled for agent forwarding to work:

On the client, use the RemoteForward SSH directive to forward traffic destined for a remote port, to a port on your local host. As described in ssh_config(5) § RemoteForward, this directive's parameters are the listening socket path on the remote, and then the destination socket path on the local host. Your configuration should look something like this:

The first line configures gpg-agent forwarding:

The second line is optional. It configures ssh-agent forwarding:

So, with the default paths, it would be:

With this configuration in place, invoking ssh remote_name should automatically forward the gpg-agent to the remote, and allow the use of your gpg key(s) for both decryption/signing (and allows the use of ssh-agent with gpg if the second RemoteForward line is included).

This article or section needs expansion.

GnuPG uses scdaemon as an interface to your smartcard reader, please refer to the man page scdaemon(1) for details.

GnuPG's gpg-card tool can be used to configure scdaemon and serves as front-end for smartcard configuration, see gpg-card(1) for details.

If you do not plan to use other cards but those based on GnuPG, you should check the reader-port parameter in ~/.gnupg/scdaemon.conf. The value '0' refers to the first available serial port reader and a value of '32768' (default) refers to the first USB reader.

pcscd(8) is a daemon which handles access to smartcard (SCard API). In earlier versions, if GnuPG's scdaemon failed to connect to the smartcard directly (e.g. by using its integrated CCID support), it fell back and tried to find a smartcard using the PCSC Lite driver. Since version 2.4 however, you will have to add the disable-ccid option in ~/.gnupg/scdaemon.conf, to be able to use pcscd.

To use pscsd install pcsclite and ccid. Then start and/or enable pcscd.service. Alternatively start and/or enable pcscd.socket to activate the daemon when needed.

If you are using any smartcard with an opensc driver (e.g.: ID cards from some countries) you should pay some attention to GnuPG configuration. Out of the box you might receive a message like this when using gpg --card-status

By default, scdaemon will try to connect directly to the device. This connection will fail if the reader is being used by another process. For example: the pcscd daemon used by OpenSC. To cope with this situation we should use the same underlying driver as opensc so they can work well together. In order to point scdaemon to use pcscd you should remove reader-port from ~/.gnupg/scdaemon.conf, specify the location to libpcsclite.so library and disable ccid so we make sure that we use pcscd:

Please check scdaemon(1) if you do not use OpenSC.

GnuPG scdaemon is the only popular pcscd client that uses PCSC_SHARE_EXCLUSIVE flag when connecting to pcscd. Other clients like OpenSC PKCS#11 that are used by browsers and programs listed in Electronic identification are using PCSC_SHARE_SHARED that allows simultaneous access to single smartcard. pcscd will not give exclusive access to smartcard while there are other clients connected. This means that to use GnuPG smartcard features you must before have to close all your open browser windows or do some other inconvenient operations.

Starting from version 2.2.28 LTS and 2.3.0 you can enable shared access by modifying your scdaemon.conf file and adding the line pcsc-shared to the end of it. Keep in mind that scdaemon(1) § --pcsc-shared describes this flag as a "somewhat dangerous option" due to "certain information being cached from the card".

When using YubiKeys or other multi applet USB dongles with OpenSC PKCS#11 may run into problems where OpenSC switches your Yubikey from OpenPGP to PIV applet, breaking the scdaemon.

You can hack around the problem by forcing OpenSC to also use the OpenPGP applet. Open /etc/opensc.conf file, search for Yubikey and change the driver = "PIV-II"; line to driver = "openpgp";. If there is no such entry, use opensc-tool --atr provided by opensc. Search for the Answer to Reset ATR: 12 34 56 78 90 AB CD .... Then create a new card_atr block referencing your device ATR within the app block.

After that you can test with pkcs11-tool -O --login that the OpenPGP applet is selected by default. Other PKCS#11 clients like browsers may need to be restarted for that change to be applied.

If for example you log into a machine via SSH or share a smart card to WSL via usbipd-win and try to use an attached device via pcscd, you will notice errors such as:

This is due to Polkit restricting access to local clients. To fix this, you can add a rule to allow certain users in all cases. The below rule allows all users in the wheel group to access devices via pcscd:

After creating the file, make sure to restart polkit.service.

GnuPG started out as an implementation of the OpenPGP format. Currently, the project is based on RFC 4880 and does not support RFC 9580 (which supersedes RFC 4880).

However, beginning with version 2.4.0 (from December 2022) GnuPG has opted to roll out changes and extensions to the format outside of the IETF process (see draft-koch-librepgp).

Most of the GnuPG-proprietary formats (which diverge from the OpenPGP standard) carry "version 5" (this version is not used in the IETF OpenPGP standard) and introduce incompatibilities:

External reviews have raised concerns about the soundness of the format extensions by GnuPG (see A Summary of Known Security Issues in LibrePGP).

See A Critique on "A Critique on the OpenPGP Updates" for a more in-depth discussion of concerns with regard to the GnuPG-specific format changes and "Comparison of RFC 9580 and LibrePGP" for a detailed technical comparison.

Arch Linux's position is to prefer compatibility with the OpenPGP standard. To this end patches such as the one for reverting RFC4880bis by default are applied to the gnupg package. This ensures the longterm compatibility with other OpenPGP implementations and avoids vendor lock-in by default.

With gnupg 2.4, gpg generates keys, which advertise support for a GnuPG specific AEAD encryption mechanism (based on OCB). However, this flavor of AEAD is not supported by other OpenPGP implementations!

Although many downstreams attempt to remove this new default by patching the GnuPG sources, when using --full-gen-key the OCB based custom AEAD encryption mechanism is nonetheless set for the new key.

Whether GnuPG's custom AEAD is set for a key can be inspected with the help of gpg itself:

This mechanism can be disabled:

You may want to use stronger algorithms:

In the latest version of GnuPG, the default algorithms used are SHA256 and AES, both of which are secure enough for most people. However, if you are using a version of GnuPG older than 2.1, or if you want an even higher level of security, then you should follow the above step.

It can be useful to encrypt some password, so it will not be written in clear on a configuration file. A good example is your email password.

First create a file with your password. You need to leave one empty line after the password, otherwise gpg will return an error message when evaluating the file.

-e is for encrypt, -a for armor (ASCII output), -r for recipient user ID.

You will be left with a new your_password_file.asc file.

By default GnuPG uses the Web of Trust as the trust model. You can change this to Trust on first use by adding --trust-model=tofu when adding a key or adding this option to your GnuPG configuration file. More details are in this email to the GnuPG list.

By default the recipient's key ID is in the encrypted message. This can be removed at encryption time for a recipient by using hidden-recipient user-id. To remove it for all recipients add throw-keyids to your configuration file. This helps to hide the receivers of the message and is a limited countermeasure against traffic analysis (i.e. using a little social engineering, anyone who is able to decrypt the message can check whether one of the other recipients is the one they suspect). On the receiving side, it may slow down the decryption process because all available secret keys must be tried (e.g. with --try-secret-key user-id).

To allow users to validate keys on the keyservers and in their keyrings (i.e. make sure they are from whom they claim to be), PGP/GPG uses the Web of Trust. Keysigning parties allow users to get together at a physical location to validate keys. The Zimmermann-Sassaman key-signing protocol is a way of making these very effective. Here you will find a how-to article.

For an easier process of signing keys and sending signatures to the owners after a keysigning party, you can use the tool caff. It can be installed from the AUR with the package caff-gitAUR.

To send the signatures to their owners you need a working MTA. If you do not have already one, install msmtp.

To always show long key ID's add keyid-format 0xlong to your configuration file. To always show full fingerprints of keys, add with-fingerprint to your configuration file.

For further customization also possible to set custom capabilities to your keys. The following capabilities are available:

It is possible to specify the capabilities of the primary key, by running:

And select an option that allows you to set your own capabilities.

Comparably, to specify custom capabilities for subkeys, add the --expert flag to gpg --edit-key, see #Edit your key for more information.

When using pinentry, you must have the proper permissions of the terminal device (e.g. /dev/tty1) in use. However, with su (or sudo), the ownership stays with the original user, not the new one. This means that pinentry will fail with a Permission denied error, even as root. If this happens when attempting to use ssh, an error like sign_and_send_pubkey: signing failed: agent refused operation will be returned. The fix is to change the permissions of the device at some point before the use of pinentry (i.e. using gpg with an agent). If doing gpg as root, simply change the ownership to root right before using gpg:

and then change it back after su (or sudo) terminated.

If the pinentry program is /usr/bin/pinentry-gnome3, it needs a DBus session bus to run properly. See General troubleshooting#Session permissions for details.

Alternatively, you can use a variety of different options described in #pinentry.

There have been issues with kgpg being able to access the ~/.gnupg/ options. One issue might be a result of a deprecated options file, see the bug report.

For Wayland sessions, gnome-session sets SSH_AUTH_SOCK to the standard gnome-keyring socket, $XDG_RUNTIME_DIR/keyring/ssh. This overrides any value set elsewhere.

See GNOME/Keyring#Disabling on how to disable this behavior.

Mutt might not use gpg-agent correctly, you need to set an environment variable GPG_AGENT_INFO (the content does not matter) when running mutt. Be also sure to enable password caching correctly, see #Cache passwords.

See this forum thread.

When gpg --list-keys fails to show keys that used to be there, and applications complain about missing or invalid keys, some keys may not have been migrated to the new format.

Please read GnuPG invalid packet workaround. Basically, it says that there is a bug with keys in the old pubring.gpg and secring.gpg files, which have now been superseded by the new pubring.kbx file and the private-keys-v1.d/ subdirectory and files. Your missing keys can be recovered with the following commands:

If gpg hanged with a certain keyserver when trying to receive keys, you might need to kill dirmngr in order to get access to other keyservers which are actually working, otherwise it might keeping hanging for all of them.

Your user might not have the permission to access the smartcard which results in a card error to be thrown, even though the card is correctly set up and inserted.

One possible solution is to add a new group scard including the users who need access to the smartcard.

Then use udev rules, similar to the following:

One needs to adapt VENDOR and MODEL according to the lsusb output, the above example is for a YubikeyNEO.

This warning appears if gnupg is upgraded and the old gpg-agent is still running. Restart the user's gpg-agent.socket (i.e., use the --user flag when restarting).

Make sure gpg-agent and dirmngr are not running with killall gpg-agent dirmngr and the $GNUPGHOME/crls.d/ folder has permission set to 700.

By default, the gnupg package uses the directory /run/user/$UID/gnupg/ for sockets. GnuPG documentation states this is the preferred directory (not all file systems are supported for sockets). Validate that your agent-socket configuration specifies a path that has an appropriate file system. You can find your path settings for agent-socket by running gpgconf --list-dirs agent-socket.

Test that gpg-agent starts successfully with gpg-agent --daemon.

In June 2019, an unknown attacker spammed several high-profile PGP certificates with tens of thousands (or hundreds of thousands) of signatures (CVE-2019-13050) and uploaded these signatures to keyservers. The existence of these poisoned certificates in a keyring causes gpg to hang with the following message:

Possible mitigation involves removing the poisoned certificate as per this blog post.

The default pinentry program is /usr/bin/pinentry-gtk-2. If gtk2AUR is unavailable, pinentry falls back to /usr/bin/pinentry-curses and causes signing to fail:

You need to set the GPG_TTY environment variable for the pinentry programs /usr/bin/pinentry-tty and /usr/bin/pinentry-curses.

If you get an error like this when trying to import keys

it is because GnuPG will not create its home directory if it does not yet exist. Simply create it manually

In some cases creating a subkey with a custom set of capabilities results in the subkey marked as "Restricted". This happens in the addkey command with option 7 or 8 ("set your own capabilities") when the capabilities are toggled in the interactive prompt. A workaround is to enter the desired capability set directly as a string instead of toggling individual capabilities, when prompted with the capability selection. For example, enter "=A" to create a subkey with only the Authentication capability.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/pinentry
```

Example 2 (unknown):
```unknown
$ gpg --homedir path/to/dir
```

Example 3 (unknown):
```unknown
gnupg_home/gpg.conf
```

Example 4 (unknown):
```unknown
/etc/gnupg/gpg.conf
```

---

## List of applications/Security

**URL:** https://wiki.archlinux.org/title/Password_manager

**Contents:**
- Network security
- Firewall management
- Threat and vulnerability detection
- File security
- Anti malware
- Screen lockers
- Password auditing
- Password managers
  - Console
  - Graphical

For detailed guides, see the main ArchWiki page, Security.

See also Wikipedia:Comparison of packet analyzers.

See iptables#Front-ends and nftables#Front-ends.

This article or section is a candidate for merging with Session lock#By environment.

See also Session lock.

See Data-at-rest encryption.

---

## List of applications/Security

**URL:** https://wiki.archlinux.org/title/List_of_Applications/Security

**Contents:**
- Network security
- Firewall management
- Threat and vulnerability detection
- File security
- Anti malware
- Screen lockers
- Password auditing
- Password managers
  - Console
  - Graphical

For detailed guides, see the main ArchWiki page, Security.

See also Wikipedia:Comparison of packet analyzers.

See iptables#Front-ends and nftables#Front-ends.

This article or section is a candidate for merging with Session lock#By environment.

See also Session lock.

See Data-at-rest encryption.

---

## Arch Security Team

**URL:** https://wiki.archlinux.org/title/Arch_Security_Team

**Contents:**
- Mission
- Contribute
- Procedure
  - Information sharing and investigation phase
  - Upstream situation and bug reporting
  - Tracking and publishing
- Resources
  - RSS
  - Mailing lists
  - Other distributions

The Arch Security Team is a group of volunteers whose goal is to track security issues with Arch Linux packages. All issues are tracked on the Arch Linux security tracker. The team was formerly known as the Arch CVE Monitoring Team.

The mission of the Arch Security Team is to contribute to the improvement of the security of Arch Linux.

The most important duty of the team is to find and track issues assigned a Common Vulnerabilities and Exposure (CVE). A CVE is public, it is identified by a unique ID of the form CVE-YYYY-number.

They publish ASAs (Arch Linux Security Advisory) which is an Arch-specific warning disseminated to Arch users. ASAs are scheduled in the tracker for peer-review, and need two acknowledgments from team members before being published.

The Arch Linux security tracker is a platform used by the Arch Security Team to track packages, add CVEs and generate advisory text.

To get involved in the identification of the vulnerabilities, it is recommended to:

The procedure to follow whenever a security vulnerability has been found in a software packaged within the Arch Linux official repositories is the following:

Two situations may arise:

The following tasks must be performed by team members:

Also consider following the mailing lists for specific packages, such as LibreOffice, X.org, Puppetlabs, ISC, etc.

Resources of other distributions (to look for CVE, patch, comments etc.):

NVD and Mitre do not necessarily fill their CVE entry immediately after attribution, so it is not always relevant for Arch. The CVE-ID and the "Date Entry Created" fields do not have particular meaning. CVE are attributed by CVE Numbering Authorities (CNA), and each CNA obtain CVE blocks from Mitre when needed/asked, so the CVE ID is not linked to the attribution date. The "Date Entry Created" field often only indicates when the CVE block was given to the CNA, nothing more.

For more resources, please see the OpenWall's Open Source Software Security Wiki.

The current members of the Arch Security Team are:

**Examples:**

Example 1 (unknown):
```unknown
!pingsec Message to the Arch Security Team
```

---

## Transport Layer Security

**URL:** https://wiki.archlinux.org/title/TLS

**Contents:**
- Implementations
- Certificate authorities
  - An overview of mechanisms for loading a default set of CA certificates
- Trust management
  - List trust store items
  - Add a certificate to a trust store
  - Remove a certificate from a trust store
  - Override default trust
- Obtaining a certificate
- Server-side recommendations

According to Wikipedia:

This article or section needs expansion.

There are multiple TLS implementations available. OpenSSL should already be installed on your system as it is an indirect dependency of the base meta package (base > coreutils > openssl). GnuTLS might already be installed on your system as it is required by many packages.

With TLS one of a set of certificate authorities (CAs) checks and signs for the authenticity of a public key certificate from a server. A client connecting to the server via TLS may verify its certificate's authenticity by relying on a digital signature of CA. To check the digital signature a client must have a public key of CA, obtained via a separate path and stored as a self-signed certificate. On Arch Linux the default set of CA certificates is provided by the ca-certificates package.

Arch Linux provides a centralized system-wide interface for managing CA certificates. This interface is the library /usr/lib/pkcs11/p11-kit-trust.so from the libp11-kit package, which provides PKCS #11 API for certificates, stored in /usr/share/ca-certificates/trust-source/ (the token "Default Trust") and /etc/ca-certificates/trust-source/ (the token "System Trust").

For using the interface from a command line, the p11-kit package provides the trust(1) utility.

For libraries, that have not been ported to PKCS #11 and use a custom logic for managing CA certificates, the package ca-certificates-utils provides the update-ca-trust(8) script. It copies CA certificates obtained through the centralized interface to /etc/ca-certificates/extracted/ and /etc/ssl/certs/.

For trust management the trust(1) utility is provided. The utility operates on a list of PKCS #11 modules with the trust-policy: yes setting, sorted by the priority: setting. See pkcs11.conf(5) for details about configuration of modules.

The certificate should be in the persistence, DER or PEM format (including the OpenSSL-specific trusted certificate format). This command stores the certificate in the first writable token found by querying the list of modules.

The default trust store p11-kit-trust.so includes a blocklist directory at /etc/ca-certificates/trust-source/blocklist/ and certificates in it will be treated as distrusted for all purposes.

The token representing certificates in /usr/share/ca-certificates/trust-source/ is always write-protected. To distrust a default certificate authority it can be extracted to the system's blocklist:

Alternatively, an already extracted certificate may also be copied to the blocklist from the /etc/ca-certificates/extracted/cadir/ path. See update-ca-trust(8) § SOURCE CONFIGURATION for further information.

The first step is to generate a private key. Before generating the key, set a restrictive file mode creation mask with umask (for example 077). This ensures that the keys written by openssl are read-protected.

Keys can use either elliptic curve or RSA algorithms.

Elliptic curves are newer algorithms and are becoming increasingly adopted for modern systems. A 256-bit elliptic curve key is expected to provide sufficient security through the year 2030 [5]. Curve25519 is an elliptic curve algorithm which has good security and performance properties.

RSA is an older cryptosystem and has higher compatibility, especially with clients that do not support recent versions of TLS. However, RSA relies on factorization, which is an area of cryptography which may be becoming weaker due to the development of faster factorization algorithms [6]. A 2048-bit RSA private key is expected to provide security through most of the 2020s [7]. A 4096-bit RSA private key is expected to provide security for longer (barring major advancements in factorization), but has a very large performance impact. The performance difference can be benchmarked with openssl speed rsa2048 rsa4096 [8].

After the key is generated, a certificate can be obtained from a certificate authority with a Certificate Signing Request (CSR), or a certificate may be self-signed. While self-signed certificates can be generated easily, clients will reject them by default, meaning that every client needs to be configured to trust the self-signed certificate.

For the actual generation commands refer to the article of the used implementation:

Because there are various attacks against TLS the best practices should be considered:

Programs to check TLS:

Websites to check TLS:

The Automated Certificate Management Environment (ACME) protocol lets you request valid X.509 certificates from certificate authorities, like Let's Encrypt.

See also List of ACME clients.

The Online Certificate Status Protocol (OCSP) is supported by Firefox. Chromium has its own mechanism[9].

See also ocsptool(1) by GnuTLS and ocsp(1ssl) by OpenSSL.

The HTTP Strict Transport Security (HSTS) mechanism is supported by Firefox, Chromium and wget (~/.wget-hsts).

See Wikipedia:DNS Certification Authority Authorization.

**Examples:**

Example 1 (unknown):
```unknown
/usr/lib/pkcs11/p11-kit-trust.so
```

Example 2 (unknown):
```unknown
/usr/share/ca-certificates/trust-source/
```

Example 3 (unknown):
```unknown
/etc/ca-certificates/trust-source/
```

Example 4 (unknown):
```unknown
/etc/ca-certificates/extracted/
```

---

## List of applications/Security

**URL:** https://wiki.archlinux.org/title/List_of_applications/Security

**Contents:**
- Network security
- Firewall management
- Threat and vulnerability detection
- File security
- Anti malware
- Screen lockers
- Password auditing
- Password managers
  - Console
  - Graphical

For detailed guides, see the main ArchWiki page, Security.

See also Wikipedia:Comparison of packet analyzers.

See iptables#Front-ends and nftables#Front-ends.

This article or section is a candidate for merging with Session lock#By environment.

See also Session lock.

See Data-at-rest encryption.

---

## GnuPG

**URL:** https://wiki.archlinux.org/title/GnuPG

**Contents:**
- Installation
- Configuration
  - Home directory
  - Configuration files
  - Default options for new users
- Usage
  - Create a key pair
  - List keys
  - Export your public key
  - Import a public key

According to the official website:

Install the gnupg package.

This will also install pinentry, a collection of simple PIN or passphrase entry dialogs which GnuPG uses for passphrase entry. The shell script /usr/bin/pinentry determines which pinentry dialog is used, in the order described at #pinentry.

If you want to use a graphical frontend or program that integrates with GnuPG, see List of applications/Security#Encryption, signing, steganography.

The GnuPG home directory is where the GnuPG suite stores its keyrings and private keys, and reads configurations from. By default, the path used is ~/.gnupg. There are two ways to override this:

By default, the home directory has its permissions set to 700 and the files it contains have their permissions set to 600. Only the owner of the directory has permission to read, write, and access the files. This is for security purposes and should not be changed. In case this directory or any file inside it does not follow this security measure, you will get warnings about unsafe file and home directory permissions.

All of GnuPG's behavior is configurable via command line arguments. For arguments you would like to be the default, you can add them to the respective configuration file:

These two configuration files cover the common usecases, but there are more auxiliary programs in the GnuPG suite with their own options. See the GnuPG manual for a comprehensive list.

Create the desired file(s), and set their permissions to 600 as discussed in #Home directory.

Add to these files any long options you want. Do not write the two dashes, but simply the name of the option and required arguments. For example, to make GnuPG always use a keyring at a specific path, as if it was invoked as gpg --no-default-keyring --keyring keyring-path ...:

Other examples are found in #See also.

Additionally, pacman uses a different set of configuration files for package signature verification. See Pacman/Package signing for details.

If you want to setup some default options for new users, put configuration files in /etc/skel/.gnupg/. When the new user is added in system, files from here will be copied to its GnuPG home directory. There is also a simple script called addgnupghome which you can use to create new GnuPG home directories for existing users:

This will add the respective /home/user1/.gnupg/ and /home/user2/.gnupg/ and copy the files from the skeleton directory to it. Users with existing GnuPG home directory are simply skipped.

Generate a key pair by typing in a terminal:

Also add the --expert option to the command line to access more ciphers and in particular some newer elliptic curves like Curve448.

The command will prompt for answers to several questions. For general use most people will want:

To list keys in your public key ring:

To list keys in your secret key ring:

GnuPG's main usage is to ensure confidentiality of exchanged messages via public-key cryptography. With it each user distributes the public key of their keyring, which can be used by others to encrypt messages to the user. The private key must always be kept private, otherwise confidentiality is broken. See Wikipedia:Public-key cryptography for examples about the message exchange.

So, in order for others to send encrypted messages to you, they need your public key.

To generate an ASCII version of a user's public key to file public-key.asc (e.g. to distribute it by e-mail):

Alternatively, or in addition, you can use a keyserver to share your key.

In order to encrypt messages to others, as well as verify their signatures, you need their public key. To import a public key with file name public-key.asc to your public key ring:

Alternatively, try retrieving their public key via WKD (in case the domain of their email address supports it) or using a keyserver.

If you wish to import a key ID to install a specific Arch Linux package, see pacman/Package signing#Managing the keyring and Makepkg#Signature checking.

You can register your key with a public PGP key server, so that others can retrieve it without having to contact you directly:

To find out details of a key on the keyserver, without importing it, do:

To import a key from a key server:

To refresh/update the keychain with the latest version from a key server:

See OpenPGP#Keyserver for a general overview of OpenPGP keyservers and their features.

An alternative key server can be specified with the keyserver option in one of the configuration files, for instance:

A temporary use of another server is handy when the regular one does not work as it should. It can be achieved by, for example,

See OpenPGP#Web Key Directory for a general overview.

When encrypting to an email address (e.g. user@example.org), if it is not already in the local keyring, GnuPG, by default, will retrieve the public OpenPGP key using the Web Key Directory protocol (i.e. GnuPG will download the key via HTTPS from the example.org web server). For example:

To retrieve a public key and import it into your keyring, use the --locate-keys or --locate-external-keys options. The former will not do anything if the key already exists in the local keyring, while the later will always refresh the key. For example:

If you control the domain of your email address yourself and have a web server that provides HTTPS with a trusted TLS certificate, you can follow this guide to enable WKD for your domain.

You need to import a public key of a user before encrypting (option -e/--encrypt) a file or message to that recipient (option -r/--recipient). Additionally you need to create a key pair if you have not already done so.

To encrypt a file with the name doc, use:

To decrypt (option -d/--decrypt) a file with the name doc.gpg encrypted with your public key, use:

gpg will prompt you for your passphrase and then decrypt and write the data from doc.gpg to doc. If you omit the -o/--output option, gpg will write the decrypted data to stdout.

Symmetric encryption does not require the generation of a key pair and can be used to simply encrypt data with a passphrase. Simply use -c/--symmetric to perform symmetric encryption:

The following example:

To decrypt a symmetrically encrypted doc.gpg using a passphrase and output decrypted contents into the same directory as doc do:

Encrypting/decrypting a directory can be done with gpgtar(1).

To backup your private key do the following:

If the private key is protected by a passphrase, the exported key file will be protected by the same one.

GnuPG may ask you to enter the passphrase for the key. This is required, because the internal protection method of the secret key is different from the one specified by the OpenPGP protocol.[5]

To import the backup of your private key:

Revocation certificates are automatically generated for newly generated keys. These are by default located in ~/.gnupg/openpgp-revocs.d/. The filename of the certificate is the fingerprint of the key it will revoke. The revocation certificates can also be generated manually by the user later using:

This certificate can be used to revoke a key if it is ever lost or compromised. The backup will be useful if you have no longer access to the secret key and are therefore not able to generate a new revocation certificate with the above command. It is short enough to be printed out and typed in by hand if necessary.

Running the gpg --edit-key user-id command will present a menu which enables you to do most of your key management related tasks.

Type help in the edit key sub menu to show the complete list of commands. Some useful ones:

If you plan to use the same key across multiple devices, you may want to strip out your master key and only keep the bare minimum encryption subkey on less secure systems.

First, find out which subkey you want to export.

Select only that subkey to export.

At this point you could stop, but it is most likely a good idea to change the passphrase as well. Import the key into a temporary folder.

At this point, you can now use /tmp/tmp.XXXXXXXXXX/subkey.altpass.asc on your other devices.

It is good practice to set an expiration date on your subkeys, so that if you lose access to the key (e.g. you forget the passphrase) the key will not continue to be used indefinitely by others. When the key expires, it is relatively straight-forward to extend the expiration date:

You will be prompted for a new expiration date, as well as the passphrase for your secret key, which is used to sign the new expiration date.

Repeat this for any further subkeys that have expired:

Finally, save the changes and quit:

Update it to a keyserver.

Alternatively, if you use this key on multiple computers, you can export the public key (with new signed expiration dates) and import it on those machines:

There is no need to re-export your secret key or update your backups: the master secret key itself never expires, and the signature of the expiration date left on the public key and subkeys is all that is needed.

Alternatively, if you prefer to stop using subkeys entirely once they have expired, you can create new ones. Do this a few weeks in advance to allow others to update their keyring.

Create new subkey (repeat for both signing and encrypting key)

And answer the following questions it asks (see #Create a key pair for suggested settings).

Update it to a keyserver.

You will also need to export a fresh copy of your secret keys for backup purposes. See #Backup your private key for details on how to do this.

Key revocation should be performed if the key is compromised, superseded, no longer used, or you forget your passphrase. This is done by merging the key with the revocation certificate of the key.

If you have no longer access to your keypair, first import a public key to import your own key.

Then, to revoke the key, import the file saved in #Backup your revocation certificate:

Now the revocation needs to be made public. Use a keyserver to send the revoked key to a public PGP server if you used one in the past, otherwise, export the revoked key to a file and distribute it to your communication partners.

Signatures certify and timestamp documents. If the document is modified, verification of the signature will fail. Unlike encryption which uses the recipient public key to encrypt a document, signatures are created with the sender's private key. The recipient of a signed document then verifies the signature using the sender's public key.

To sign a file use the -s/--sign flag:

doc.sig contains both the compressed content of the original file doc and the signature in a binary format, but the file is not encrypted. However, you can combine signing with encrypting.

To sign a file without compressing it into binary format use:

Here both the content of the original file doc and the signature are stored in human-readable form in doc.sig.

To create a separate signature file to be distributed separately from the document or file itself, use the --detach-sig flag:

Here the signature is stored in doc.sig, but the contents of doc are not stored in it. This method is often used in distributing software projects to allow users to verify that the program has not been modified by a third party.

To verify a signature use the --verify flag:

where doc.sig is the signed file containing the signature you wish to verify.

If you are verifying a detached signature, both the signed data file and the signature file must be present when verifying. For example, to verify Arch Linux's latest iso you would do:

where archlinux-version.iso must be located in the same directory.

You can also specify the signed data file with a second argument:

If a file has been encrypted in addition to being signed, simply decrypt the file and its signature will also be verified.

This article or section needs expansion.

gpg-agent is mostly used as daemon to request and cache the password for the keychain. This is useful if GnuPG is used from an external program like a mail client. gnupg comes with systemd user sockets which are enabled by default. These sockets are gpg-agent.socket, gpg-agent-extra.socket, gpg-agent-browser.socket, gpg-agent-ssh.socket, and dirmngr.socket.

gpg-agent can be configured via ~/.gnupg/gpg-agent.conf file. The configuration options are listed in gpg-agent(1). For example you can change cache ttl for unused keys:

where XXXXX is the keygrip. You can get its value when running gpg --with-keygrip --list-secret-keys. The passphrase will be stored until gpg-agent is restarted. If you set up default-cache-ttl value, it will take precedence.

After changing the configuration, reload the agent using gpg-connect-agent:

The command should print OK.

However in some cases only the restart may not be sufficient, like when keep-screen has been added to the agent configuration. In this case you firstly need to kill the ongoing gpg-agent process and then you can restart it as was explained above.

gpg-agent can be configured via the pinentry-program stanza to use a particular pinentry user interface when prompting the user for a passphrase. For example:

There are other pinentry programs that you can choose from - see pacman -Ql pinentry | grep /usr/bin/. You may need to install the relevant optional dependencies for your chosen pinentry program.

Remember to reload the agent after making changes to the configuration.

max-cache-ttl and default-cache-ttl defines how many seconds gpg-agent should cache the passwords. To enter a password once a session, set them to something very high, for instance:

For password caching in SSH emulation mode, set default-cache-ttl-ssh and max-cache-ttl-ssh instead, for example:

Starting with GnuPG 2.1.0 the use of gpg-agent and pinentry is required, which may break backwards compatibility for passphrases piped in from STDIN using the --passphrase-fd 0 commandline option. In order to have the same type of functionality as the older releases two things must be done:

First, edit the gpg-agent configuration to allow loopback pinentry mode:

Reload the agent if it is running to let the change take effect.

Second, either the application needs to be updated to include a commandline parameter to use loopback mode like so:

...or if this is not possible, add the option to the configuration:

gpg-agent has OpenSSH agent emulation. If you already use the GnuPG suite, you might consider using its agent to also cache your SSH keys. Additionally, some users may prefer the PIN entry dialog GnuPG agent provides as part of its passphrase management.

Using gpg-agent in place of ssh-agent will not work if you use coreutils-uutilsAUR. It will always say Communication with agent failed

Set the following variables to communicate with gpg-agent instead of the default ssh-agent.

Alternatively, depend on Bash. This works for non-standard socket locations as well:

Also set the GPG_TTY and refresh the TTY in case user has switched into an X session as stated in gpg-agent(1). For example:

If you use multiple terminals simultaneously and want gpg-agent to ask for passphrase via pinentry-curses from the same terminal where the ssh command was run, add the following to the SSH configuration file. This will make the TTY to be refreshed every time an ssh command is run [11]:

Note that GPG_TTY environment variable has to be set for this to work.

Once gpg-agent is running you can use ssh-add to approve keys, following the same steps as for ssh-agent. The list of approved keys is stored in the ~/.gnupg/sshcontrol file.

Once your key is approved, you will get a pinentry dialog every time your passphrase is needed. For password caching see #Cache passwords.

You can also use your PGP key as an SSH key. This requires a key with the Authentication capability (see #Custom capabilities). There are various benefits gained by using a PGP key for SSH authentication, including:

To retrieve the public key part of your GPG/SSH key, run gpg --export-ssh-key gpg-key. If your key is authentication-capable but this command still fails with "Unusable public key", add a ! suffix ([12]).

Unless you have your GPG key on a keycard, you need to add your key to $GNUPGHOME/sshcontrol to be recognized as a SSH key. If your key is on a keycard, its keygrip is added to sshcontrol implicitly. If not, get the keygrip of your key this way:

Then edit sshcontrol like this. Adding the keygrip is a one-time action; you will not need to edit the file again, unless you are adding additional keys.

This article or section needs expansion.

It is possible to forward one's gpg-agent to a remote machine by forwarding gpg sockets to the remote machine, as explained by the GnuPG wiki.

First, add the following line to /etc/ssh/sshd_config on the remote machine to enable automatic removal of stale sockets on connect. Without this, the socket(s) on the remote machine will need to removed manually before connecting with forwarding enabled for agent forwarding to work:

On the client, use the RemoteForward SSH directive to forward traffic destined for a remote port, to a port on your local host. As described in ssh_config(5) § RemoteForward, this directive's parameters are the listening socket path on the remote, and then the destination socket path on the local host. Your configuration should look something like this:

The first line configures gpg-agent forwarding:

The second line is optional. It configures ssh-agent forwarding:

So, with the default paths, it would be:

With this configuration in place, invoking ssh remote_name should automatically forward the gpg-agent to the remote, and allow the use of your gpg key(s) for both decryption/signing (and allows the use of ssh-agent with gpg if the second RemoteForward line is included).

This article or section needs expansion.

GnuPG uses scdaemon as an interface to your smartcard reader, please refer to the man page scdaemon(1) for details.

GnuPG's gpg-card tool can be used to configure scdaemon and serves as front-end for smartcard configuration, see gpg-card(1) for details.

If you do not plan to use other cards but those based on GnuPG, you should check the reader-port parameter in ~/.gnupg/scdaemon.conf. The value '0' refers to the first available serial port reader and a value of '32768' (default) refers to the first USB reader.

pcscd(8) is a daemon which handles access to smartcard (SCard API). In earlier versions, if GnuPG's scdaemon failed to connect to the smartcard directly (e.g. by using its integrated CCID support), it fell back and tried to find a smartcard using the PCSC Lite driver. Since version 2.4 however, you will have to add the disable-ccid option in ~/.gnupg/scdaemon.conf, to be able to use pcscd.

To use pscsd install pcsclite and ccid. Then start and/or enable pcscd.service. Alternatively start and/or enable pcscd.socket to activate the daemon when needed.

If you are using any smartcard with an opensc driver (e.g.: ID cards from some countries) you should pay some attention to GnuPG configuration. Out of the box you might receive a message like this when using gpg --card-status

By default, scdaemon will try to connect directly to the device. This connection will fail if the reader is being used by another process. For example: the pcscd daemon used by OpenSC. To cope with this situation we should use the same underlying driver as opensc so they can work well together. In order to point scdaemon to use pcscd you should remove reader-port from ~/.gnupg/scdaemon.conf, specify the location to libpcsclite.so library and disable ccid so we make sure that we use pcscd:

Please check scdaemon(1) if you do not use OpenSC.

GnuPG scdaemon is the only popular pcscd client that uses PCSC_SHARE_EXCLUSIVE flag when connecting to pcscd. Other clients like OpenSC PKCS#11 that are used by browsers and programs listed in Electronic identification are using PCSC_SHARE_SHARED that allows simultaneous access to single smartcard. pcscd will not give exclusive access to smartcard while there are other clients connected. This means that to use GnuPG smartcard features you must before have to close all your open browser windows or do some other inconvenient operations.

Starting from version 2.2.28 LTS and 2.3.0 you can enable shared access by modifying your scdaemon.conf file and adding the line pcsc-shared to the end of it. Keep in mind that scdaemon(1) § --pcsc-shared describes this flag as a "somewhat dangerous option" due to "certain information being cached from the card".

When using YubiKeys or other multi applet USB dongles with OpenSC PKCS#11 may run into problems where OpenSC switches your Yubikey from OpenPGP to PIV applet, breaking the scdaemon.

You can hack around the problem by forcing OpenSC to also use the OpenPGP applet. Open /etc/opensc.conf file, search for Yubikey and change the driver = "PIV-II"; line to driver = "openpgp";. If there is no such entry, use opensc-tool --atr provided by opensc. Search for the Answer to Reset ATR: 12 34 56 78 90 AB CD .... Then create a new card_atr block referencing your device ATR within the app block.

After that you can test with pkcs11-tool -O --login that the OpenPGP applet is selected by default. Other PKCS#11 clients like browsers may need to be restarted for that change to be applied.

If for example you log into a machine via SSH or share a smart card to WSL via usbipd-win and try to use an attached device via pcscd, you will notice errors such as:

This is due to Polkit restricting access to local clients. To fix this, you can add a rule to allow certain users in all cases. The below rule allows all users in the wheel group to access devices via pcscd:

After creating the file, make sure to restart polkit.service.

GnuPG started out as an implementation of the OpenPGP format. Currently, the project is based on RFC 4880 and does not support RFC 9580 (which supersedes RFC 4880).

However, beginning with version 2.4.0 (from December 2022) GnuPG has opted to roll out changes and extensions to the format outside of the IETF process (see draft-koch-librepgp).

Most of the GnuPG-proprietary formats (which diverge from the OpenPGP standard) carry "version 5" (this version is not used in the IETF OpenPGP standard) and introduce incompatibilities:

External reviews have raised concerns about the soundness of the format extensions by GnuPG (see A Summary of Known Security Issues in LibrePGP).

See A Critique on "A Critique on the OpenPGP Updates" for a more in-depth discussion of concerns with regard to the GnuPG-specific format changes and "Comparison of RFC 9580 and LibrePGP" for a detailed technical comparison.

Arch Linux's position is to prefer compatibility with the OpenPGP standard. To this end patches such as the one for reverting RFC4880bis by default are applied to the gnupg package. This ensures the longterm compatibility with other OpenPGP implementations and avoids vendor lock-in by default.

With gnupg 2.4, gpg generates keys, which advertise support for a GnuPG specific AEAD encryption mechanism (based on OCB). However, this flavor of AEAD is not supported by other OpenPGP implementations!

Although many downstreams attempt to remove this new default by patching the GnuPG sources, when using --full-gen-key the OCB based custom AEAD encryption mechanism is nonetheless set for the new key.

Whether GnuPG's custom AEAD is set for a key can be inspected with the help of gpg itself:

This mechanism can be disabled:

You may want to use stronger algorithms:

In the latest version of GnuPG, the default algorithms used are SHA256 and AES, both of which are secure enough for most people. However, if you are using a version of GnuPG older than 2.1, or if you want an even higher level of security, then you should follow the above step.

It can be useful to encrypt some password, so it will not be written in clear on a configuration file. A good example is your email password.

First create a file with your password. You need to leave one empty line after the password, otherwise gpg will return an error message when evaluating the file.

-e is for encrypt, -a for armor (ASCII output), -r for recipient user ID.

You will be left with a new your_password_file.asc file.

By default GnuPG uses the Web of Trust as the trust model. You can change this to Trust on first use by adding --trust-model=tofu when adding a key or adding this option to your GnuPG configuration file. More details are in this email to the GnuPG list.

By default the recipient's key ID is in the encrypted message. This can be removed at encryption time for a recipient by using hidden-recipient user-id. To remove it for all recipients add throw-keyids to your configuration file. This helps to hide the receivers of the message and is a limited countermeasure against traffic analysis (i.e. using a little social engineering, anyone who is able to decrypt the message can check whether one of the other recipients is the one they suspect). On the receiving side, it may slow down the decryption process because all available secret keys must be tried (e.g. with --try-secret-key user-id).

To allow users to validate keys on the keyservers and in their keyrings (i.e. make sure they are from whom they claim to be), PGP/GPG uses the Web of Trust. Keysigning parties allow users to get together at a physical location to validate keys. The Zimmermann-Sassaman key-signing protocol is a way of making these very effective. Here you will find a how-to article.

For an easier process of signing keys and sending signatures to the owners after a keysigning party, you can use the tool caff. It can be installed from the AUR with the package caff-gitAUR.

To send the signatures to their owners you need a working MTA. If you do not have already one, install msmtp.

To always show long key ID's add keyid-format 0xlong to your configuration file. To always show full fingerprints of keys, add with-fingerprint to your configuration file.

For further customization also possible to set custom capabilities to your keys. The following capabilities are available:

It is possible to specify the capabilities of the primary key, by running:

And select an option that allows you to set your own capabilities.

Comparably, to specify custom capabilities for subkeys, add the --expert flag to gpg --edit-key, see #Edit your key for more information.

When using pinentry, you must have the proper permissions of the terminal device (e.g. /dev/tty1) in use. However, with su (or sudo), the ownership stays with the original user, not the new one. This means that pinentry will fail with a Permission denied error, even as root. If this happens when attempting to use ssh, an error like sign_and_send_pubkey: signing failed: agent refused operation will be returned. The fix is to change the permissions of the device at some point before the use of pinentry (i.e. using gpg with an agent). If doing gpg as root, simply change the ownership to root right before using gpg:

and then change it back after su (or sudo) terminated.

If the pinentry program is /usr/bin/pinentry-gnome3, it needs a DBus session bus to run properly. See General troubleshooting#Session permissions for details.

Alternatively, you can use a variety of different options described in #pinentry.

There have been issues with kgpg being able to access the ~/.gnupg/ options. One issue might be a result of a deprecated options file, see the bug report.

For Wayland sessions, gnome-session sets SSH_AUTH_SOCK to the standard gnome-keyring socket, $XDG_RUNTIME_DIR/keyring/ssh. This overrides any value set elsewhere.

See GNOME/Keyring#Disabling on how to disable this behavior.

Mutt might not use gpg-agent correctly, you need to set an environment variable GPG_AGENT_INFO (the content does not matter) when running mutt. Be also sure to enable password caching correctly, see #Cache passwords.

See this forum thread.

When gpg --list-keys fails to show keys that used to be there, and applications complain about missing or invalid keys, some keys may not have been migrated to the new format.

Please read GnuPG invalid packet workaround. Basically, it says that there is a bug with keys in the old pubring.gpg and secring.gpg files, which have now been superseded by the new pubring.kbx file and the private-keys-v1.d/ subdirectory and files. Your missing keys can be recovered with the following commands:

If gpg hanged with a certain keyserver when trying to receive keys, you might need to kill dirmngr in order to get access to other keyservers which are actually working, otherwise it might keeping hanging for all of them.

Your user might not have the permission to access the smartcard which results in a card error to be thrown, even though the card is correctly set up and inserted.

One possible solution is to add a new group scard including the users who need access to the smartcard.

Then use udev rules, similar to the following:

One needs to adapt VENDOR and MODEL according to the lsusb output, the above example is for a YubikeyNEO.

This warning appears if gnupg is upgraded and the old gpg-agent is still running. Restart the user's gpg-agent.socket (i.e., use the --user flag when restarting).

Make sure gpg-agent and dirmngr are not running with killall gpg-agent dirmngr and the $GNUPGHOME/crls.d/ folder has permission set to 700.

By default, the gnupg package uses the directory /run/user/$UID/gnupg/ for sockets. GnuPG documentation states this is the preferred directory (not all file systems are supported for sockets). Validate that your agent-socket configuration specifies a path that has an appropriate file system. You can find your path settings for agent-socket by running gpgconf --list-dirs agent-socket.

Test that gpg-agent starts successfully with gpg-agent --daemon.

In June 2019, an unknown attacker spammed several high-profile PGP certificates with tens of thousands (or hundreds of thousands) of signatures (CVE-2019-13050) and uploaded these signatures to keyservers. The existence of these poisoned certificates in a keyring causes gpg to hang with the following message:

Possible mitigation involves removing the poisoned certificate as per this blog post.

The default pinentry program is /usr/bin/pinentry-gtk-2. If gtk2AUR is unavailable, pinentry falls back to /usr/bin/pinentry-curses and causes signing to fail:

You need to set the GPG_TTY environment variable for the pinentry programs /usr/bin/pinentry-tty and /usr/bin/pinentry-curses.

If you get an error like this when trying to import keys

it is because GnuPG will not create its home directory if it does not yet exist. Simply create it manually

In some cases creating a subkey with a custom set of capabilities results in the subkey marked as "Restricted". This happens in the addkey command with option 7 or 8 ("set your own capabilities") when the capabilities are toggled in the interactive prompt. A workaround is to enter the desired capability set directly as a string instead of toggling individual capabilities, when prompted with the capability selection. For example, enter "=A" to create a subkey with only the Authentication capability.

**Examples:**

Example 1 (unknown):
```unknown
/usr/bin/pinentry
```

Example 2 (unknown):
```unknown
$ gpg --homedir path/to/dir
```

Example 3 (unknown):
```unknown
gnupg_home/gpg.conf
```

Example 4 (unknown):
```unknown
/etc/gnupg/gpg.conf
```

---

## Firejail

**URL:** https://wiki.archlinux.org/title/Firejail

**Contents:**
- Installation
- Configuration
- Usage
  - Using Firejail by default
  - Use with hardened_malloc
  - Enable AppArmor support
  - Verifying Firejail is being used
- Creating custom profiles
  - Whitelists and blacklists
  - Profile writing

Firejail is an easy to use Setuid sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces, seccomp-bpf and Linux capabilities.

Install the firejail package. A GUI application for use with Firejail is also available, firetools.

Most users will not require any custom configuration and can proceed to #Usage.

Firejail uses profiles to set the security protections for each of the applications executed inside of it - you can find the default profiles in /etc/firejail/application.profile. Should you require custom profiles for applications not included, or wish to modify the defaults, you may place new rules or copies of the defaults in the ~/.config/firejail directory. You may have multiple custom profile files for a single application, and you may share the same profile file among several applications.

If firejail does not have a profile for a particular application, it uses its restrictive system-wide default profile. This can result in the application not functioning as desired, without first creating a custom and less restrictive profile.

Refer to firejail-profile(5).

To execute an application using firejail's default protections for that application (the default profile), execute the following:

One-time additions to the default profile can be added as command line options (see firejail(1)). For example, to execute okular with seccomp protection, execute the following:

You may define multiple non-default profiles for a single program. Once you create your profile file, you can use it by executing:

To use Firejail by default for all applications for which it has profiles, run the firecfg tool with sudo:

This creates symbolic links in /usr/local/bin/ pointing to /usr/bin/firejail for programs for which Firejail has default or self-created profiles. Note that firecfg(1) only symlinks the programs listed in /etc/firejail/firecfg.config. Certain CLI programs are absent, such as: tar, curl, and git. These need to be symlinked manually. See Profiles not in firecfg #2507 for why they are not included. firecfg additionally adds the current user to Firejail user access database and checks the /usr/share/applications/*.desktop files if they contain the full path to the respective executable, removes the full path and copies them to ~/.local/share/applications/. This ensures that the symlinks in /usr/local/bin/ will be used, which prevents Firejail getting bypassed. If sudo is not installed on your system, you should execute:

as user in order to fix the .desktop files.

There may be cases for which you need to manually modify the Exec= line of the .desktop file in ~/.local/share/applications/ to explicitly call Firejail.

To manually map individual applications, execute:

hardened_mallocAUR is a hardened implementation of glibc's malloc() allocator, originally written for Android but extended for use on the desktop. While not integrated into glibc yet, it can be used selectively with LD_PRELOAD. The proper way to launch an application within firejail using hardened_malloc is demonstrated below. To make it permanent, you would need to create your own entry in /usr/local/bin/ for the desired application.

Alternatively, add the following to a custom profile:

Profiles that have private-lib will need the following in custom profiles:

The various environment variables and settings that can be used to tune hardened_malloc can be found on its github page.

Since 0.9.60-1, Firejail has supported more direct integration with AppArmor through a generic AppArmor profile. During installation, the profile, firejail-default, is placed in /etc/apparmor.d directory, and needs to be loaded into the kernel by running the following command as root:

See firejail(1) § APPARMOR.

Local customizations of the apparmor profile are supported by editing the file /etc/apparmor.d/local/firejail-local

AppArmor is already enabled for a large number of Firejail profiles. There are several ways to enable AppArmor confinement on top of a Firejail security profile:

Note that enabling AppArmor by above methods always means that /etc/apparmor.d/firejail-default is used. If you rather want to use a specific AppArmor profile for an application, you have to use the above mentioned ignore apparmor command. However, that is not recommended, as using both Firejail and AppArmor for the same applications often creates problems.

A more comprehensive output is produced by

Blacklists deny access to a specific file or directory. All other files and directories, which are not added to the blacklist, are not changed.

The order in which they appear in a profile is important: noblacklist directives must be added above blacklist directives.

Whitelists block everything under the same "top directory", that is not explicitly whitelisted. This means that if you whitelist for example /etc/something, this file will be accessible, but for example if there's another file /etc/something_else, that will not be accessible. In Firejail, a "top directory" means, if the whitelisted file's path is for example /etc/somedir/somefile, then the top directory would be /etc. All other top directories like /opt, /usr and so on, haven't changed, so all files there are still accessible, unless a file or directory inside them is also whitelisted.

The order in which they appear in a profile is important: nowhitelist directives must be added above whitelist directives.

The basic process is:

If you want to create a whitelisted profile (i.e. a profile which contains whitelist directives), you can build a whitelist of permitted locations by executing

Keep in mind that a whitelisted profile is problematic for applications that need to access random locations (like text editors or file managers).

The standard profile layout includes the capability to make persistent local customisations through the inclusion of .local files[3]. Basically, each officially supported profile contains the lines include ProgramName.local and include globals.local. These *.local files might be located in /etc/firejail/ or in ~/.config/firejail/. Since the order of precedence is determined by which is read first, this makes for a very powerful way of making local customisations. For example, with reference this firejail question, to globally enable Apparmor and disable Internet connectivity, one could simply create/edit /etc/firejail/globals.local to include the lines

Then, to allow, for example, "curl" to connect to the internet, yet still maintain its apparmor confinement, one would create/edit /etc/firejail/curl.local to include the lines.

Since curl.local is read before globals.local, ignore net overrides net none, and, as a bonus, the above changes would be persistent across future updates.

In order to test and audit a Firejail profile, you may find the following to be useful:

The factual accuracy of this article or section is disputed.

On Xorg any program can listen to all keyboard input and record all screens. The purpose of sandboxing X11 is to restrict this behavior, which is especially problematic for complex programs working with potentially malicious input like browsers.

Xephyr and Xpra allow you to sandbox Xorg. Although Xpra provides full clipboard support, it is recommended to use Xephyr due to the very notable and permanent lag with nested X11 sessions.

For a complete setup with (not ideal) clipboard support (clipboard is still always shared), see Sakaki's Gentoo guide, especially the section about the clipboard and automatic rescaling.

Alternatively, if clipboard support is not needed but windows need to be managed, install a standalone window manager such as Openbox.

xephyr-screen WidthxHeight can be set in /etc/firejail/firejail.config where Width and Height are in pixels and based on your screen resolution.

device is your active network interface, which is needed to ensure that DNS works. Then right click and select your applications to run.

See the Firejail Wordpress site for a simpler guide.

According to the guide:

Note that the statement:

is incorrect, xserverrc can be edited to -nolisten local, which disables the abstract sockets of X11 and helps isolate it.

Openbox can be configured to start a certain browser at startup. program.profile is the respective profile contained in /etc/firejail, and --startup "command" is the command line used to start the program. For example, to start Chromium in the sandbox:

You can control the size of the screen with the parameter:

The security risk of Firejail being a SUID executable can be mitigated by adding the line

to /etc/firejail/firejail.config. However, this can break specific applications. On Arch Linux, VirtualBox doesn't start anymore. With the linux-hardened kernel Wireshark and Chromium-based browsers are also affected.

Further hardening measures include creating a special firejail group with adding the user to that group and changing the file mode for the firejail executable. For details see here.

Make sure to create the firejail group and add your user to it.

If you need to reference, whitelist, or blacklist a directory within a custom profile, such as with palemoonAUR, you must do so using the absolute path, without encapsulation or escapes:

Firejail also includes a one time private mode, in which no mounts are made in the chroots to your home directory. In doing this, you can execute applications without performing any changes to disk. For example, to execute okular in private mode, do the following:

Some of the Firejail developers recognized issues with the tools it ships with and made their own, improved versions of them.

Firejail can be hard to debug. The symptoms of a misconfigured or otherwise unfitting setup range from random segmentation faults and hangs in the applications to simple error messages.

Some applications are harder to sandbox than others. For example web browsers and Electron applications tend to need more troubleshooting than others since there is much that can go wrong. It is crucial to check the FAQ and open issues first, since debugging can take quite some time.

To remove Firejail created symbolic links (e.g. reset to default):

If you do not want to use Firejail for a specific application (e.g., because you prefer to rather confine it with AppArmor), you have to manually remove the related symbolic link:

As a subsequent execution of firecfg would re-add the removed symlinks, the respective applications should be commented in /etc/firejail/firecfg.config.

Verify if any leftovers of Desktop entries are still overruled by Firejail.

If Firejail causes PulseAudio issues with sandboxed applications [4], the following command may be used:

This commands creates a custom ~/.config/pulse/client.conf file for the current user with enable-shm = no and possible other workarounds.

If the system uses the hidepid kernel parameter, Firemon can only be run as root. This, among other things, will cause problems with the Firetools GUI incorrectly reporting "Capabilities", "Protocols" and the status of "Seccomp"[5].

Some users report problems when using Firejail and proprietary graphic drivers from NVIDIA (e.g. [6], [7] or [8]). This can often be solved by disabling the noroot Firejail option in the application's profile file.

There is a bug on firejail 0.5.96 with linux >= 4.20.0, see [9] and [10]

Example error message:

This article or section is a candidate for merging with #Enable AppArmor support.

For some applications (e.g. Firefox) starting with Firejail may result in warnings like:

When running the suggested command you might see:

This means that AppArmor is not enabled as a kernel parameter, so you have to set it according to AppArmor#Installation.

This means the PKGBUILD uses patch with the -i argument so a whitelist for $SRCDEST in /etc/makepkg.conf is needed.

Create the override patch.local with the value of your $SRCDEST:

Changing the PKGBUILD to use stdin also works:

There is a known issue that prevents processes from daemonizing. There is currently no solution to this except not using Firejail to sandbox the affected application. Because it is a bug within Firejail, no configuration can solve this issue. Fortunately the applications mentioned in the issue usually do not have a large attack surface, so the risks of running them without a sandbox are comparatively low.

**Examples:**

Example 1 (unknown):
```unknown
/etc/firejail/firefox.profile
```

Example 2 (unknown):
```unknown
/mnt/btrfs/@some-snapshot/$HOME/.ssh
```

Example 3 (unknown):
```unknown
/etc/firejail/application.profile
```

Example 4 (unknown):
```unknown
~/.config/firejail
```

---

## Data-at-rest encryption

**URL:** https://wiki.archlinux.org/title/Encryption

**Contents:**
- Why use encryption?
  - System data encryption
- Preparation
  - Choosing a setup
  - Preparing the disk
  - Available methods
    - Stacked filesystem encryption
      - Cloud-storage optimized
    - Block device encryption
  - Block device vs stacked filesystem encryption

This article discusses data-at-rest encryption software, which on-the-fly encrypts / decrypts data written to / read from a block device, disk partition or directory. Examples for block devices are hard drives, flash drives and DVDs.

Data-at-rest encryption should only be viewed as an adjunct to the existing security mechanisms of the operating system - focused on securing physical access, while relying on other parts of the system to provide things like network security and user-based access control.

Data-at-rest encryption ensures that files are always stored on disk in an encrypted form. The files only become available to the operating system and applications in readable form while the system is running and unlocked by a trusted user (data in use or in transit). An unauthorized person looking at the disk contents directly, will only find garbled random-looking data instead of the actual files.

For example, this can prevent unauthorized viewing of the data when the computer or hard-disk is:

In addition, data-at-rest encryption can also be used to add some security against unauthorized attempts to tamper with your operating system – for example, the installation of keyloggers or Trojan horses by attackers who can gain physical access to the system while you are away.

You will still be vulnerable to:

Data-at-rest encryption also will not protect you against someone simply wiping your disk. Regular backups are recommended to keep your data safe.

A very strong disk encryption setup (e.g. full system encryption with authenticity checking and no plaintext boot partition) is required to stand a chance against professional attackers who are able to tamper with your system before you use it. And even then it cannot prevent all types of tampering (e.g. hardware keyloggers). The best remedy might be hardware-based full-disk encryption and Trusted Computing.

While encrypting only the user data itself (often located within the home directory, or on removable media like a data DVD), is the simplest and least intrusive method, it has some significant drawbacks. In modern computer systems, there are many background processes that may cache and store information about user data or parts of the data itself in non-encrypted areas of the hard drive, like:

The solution is to encrypt both system and user data, preventing unauthorized physical access to private data that may be cached by the system. This however comes with the disadvantage that unlocking of the encrypted parts of the disk has to happen at boot time. Another benefit of system data encryption is that it complicates the installation of malware like keyloggers or rootkits for someone with physical access.

Which encryption setup is appropriate for you will depend on your goals (please read #Why use encryption? above) and system parameters.

Among other things, you will need to answer the following questions:

Then you can go on to make the required technical choices (see #Available methods and #How the encryption works below), regarding:

Before setting up encryption on a (part of a) disk, consider securely wiping it first. This consists of overwriting the entire drive or partition with a stream of zero bytes or random bytes, and is done for one or both of the following reasons:

Disk encryption does not change the fact that individual sectors are only overwritten on demand, when the file system creates or modifies the data those particular sectors hold (see #How the encryption works below). Sectors which the filesystem considers "not currently used" are not touched, and may still contain remnants of data from previous filesystems. The only way to make sure that all data which you previously stored on the drive can not be recovered, is to manually erase it. For this purpose it does not matter whether zero bytes or random bytes are used (although wiping with zero bytes will be much faster).

Ideally, the whole encrypted part of the disk should be indistinguishable from uniformly random data. This way, no unauthorized person can know which and how many sectors actually contain encrypted data - which may be a desirable goal in itself (as part of true confidentiality), and also serves as an additional barrier against attackers trying to break the encryption. In order to satisfy this goal, wiping the disk using high-quality random bytes is crucial.

The second goal only makes sense in combination with block device encryption, because in the case of stacked filesystem encryption the encrypted data can easily be located anyways (in the form of distinct encrypted files in the host filesystem). Also note that even if you only intend to encrypt a particular folder, you will have to erase the whole partition if you want to get rid of files that were previously stored in that folder in unencrypted form (due to disk fragmentation). If there are other folders on the same partition, you will have to back them up and move them back afterwards.

Once you have decided which kind of disk erasure you want to perform, refer to the Securely wipe disk article for technical instructions.

This article or section needs expansion.

All data-at-rest encryption methods operate in such a way that even though the disk actually holds encrypted data, the operating system and applications "see" it as the corresponding normal readable data as long as the cryptographic container (i.e. the logical part of the disk that holds the encrypted data) has been "unlocked" and mounted.

For this to happen, some "secret information" (usually in the form of a keyfile and/or passphrase) needs to be supplied by the user, from which the actual encryption key can be derived (and stored in the kernel keyring for the duration of the session).

If you are completely unfamiliar with this sort of operation, please also read the #How the encryption works section below.

The available data-at-rest encryption methods can be separated into two types by their layer of operation:

Stacked filesystem encryption solutions are implemented as a layer that stacks on top of an existing filesystem, causing all files written to an encryption-enabled folder to be encrypted on-the-fly before the underlying filesystem writes them to disk, and decrypted whenever the filesystem reads them from disk. This way, the files are stored in the host filesystem in encrypted form (meaning that their contents, and usually also their file/folder names, are replaced by random-looking data of roughly the same length), but other than that they still exist in that filesystem as they would without encryption, as normal files / symlinks / hardlinks / etc.

The way it is implemented, is that to unlock the folder storing the raw encrypted files in the host filesystem ("lower directory"), it is mounted (using a special stacked pseudo-filesystem) onto itself or optionally a different location ("upper directory"), where the same files then appear in readable form - until it is unmounted again, or the system is turned off.

Available solutions in this category include eCryptfs and EncFS, or one of the cloud-ready options below.

If you are deploying stacked filesystem encryption to achieve zero-knowledge synchronization with third-party-controlled locations such as cloud-storage services, you may want to consider alternatives to eCryptfs and EncFS, since these are not optimized for transmission of files over the Internet. There are some solutions designed for this purpose instead:

Note that some cloud-storage services offer zero-knowledge encryption directly through their own client applications.

Block device encryption methods, on the other hand, operate below the filesystem layer and make sure that everything written to a certain block device (i.e. a whole disk, or a partition, or a file acting as a loop device) is encrypted. This means that while the block device is offline, its whole content looks like a large blob of random data, with no way of determining what kind of filesystem and data it contains. Accessing the data happens, again, by mounting the protected container (in this case the block device) to an arbitrary location in a special way.

The following "block device encryption" solutions are available in Arch Linux:

For practical implications of the chosen layer of operation, see the #Block device vs stacked filesystem encryption below, as well as the general write up for eCryptfs. See Category:Encryption for the available content of the methods compared below, as well as other tools not included in the table.

This article or section needs expansion.

The column "dm-crypt +/- LUKS" denotes features of dm-crypt for both LUKS ("+") and plain ("-") encryption modes. If a specific feature requires using LUKS, this is indicated by "(with LUKS)". Likewise "(without LUKS)" indicates usage of LUKS is counter-productive to achieve the feature and plain mode should be used.

with systemd and /etc/crypttab

AES-Twofish, AES-Twofish-Serpent, Serpent-AES, Serpent-Twofish-AES, Twofish-Serpent

In practice, it could turn out something like:

Many other combinations are of course possible. You should carefully plan what kind of setup will be appropriate for your system.

This section is intended as a high-level introduction to the concepts and processes which are at the heart of usual disk encryption setups.

It does not go into technical or mathematical details (consult the appropriate literature for that), but should provide a system administrator with a rough understanding of how different setup choices (especially regarding key management) can affect usability and security.

For the purposes of disk encryption, each blockdevice (or individual file in the case of stacked filesystem encryption) is divided into sectors of equal length, for example 512 bytes (4096 bits). The encryption/decryption then happens on a per-sector basis, so the n'th sector of the blockdevice/file on disk will store the encrypted version of the n'th sector of the original data.

Whenever the operating system or an application requests a certain fragment of data from the blockdevice/file, the whole sector (or sectors) that contains the data will be read from disk, decrypted on-the-fly, and temporarily stored in memory:

Similarly, on each write operation, all sectors that are affected must be re-encrypted completely (while the rest of the sectors remain untouched).

In order to be able to de/encrypt data, the disk encryption system needs to know the unique secret "key" associated with it. Whenever the encrypted block device or folder in question is to be mounted, its corresponding key (called henceforth its "master key") must be supplied.

The entropy of the key is of utmost importance for the security of the encryption. A randomly generated byte string of a certain length, for example 32 bytes (256 bits), has desired properties but is not feasible to remember and apply manually during the mount.

For that reason two techniques are used as aides. The first is the application of cryptography to increase the entropic property of the master key, usually involving a separate human-friendly passphrase. For the different types of encryption the #Comparison table lists respective features. The second method is to create a keyfile with high entropy and store it on a medium separate from the data drive to be encrypted.

See also Wikipedia:Authenticated encryption.

The following are examples how to store and cryptographically secure a master key with a keyfile:

Simply storing the master key in a file (in readable form) is the simplest option. The file - called a "keyfile" - can be placed on a USB stick that you keep in a secure location and only connect to the computer when you want to mount the encrypted parts of the disk (e.g. during boot or login).

The master key (and thus the encrypted data) can be protected with a secret passphrase, which you will have to remember and enter each time you want to mount the encrypted block device or folder. See #Cryptographic metadata below for details.

In some cases, e.g. when encrypting swap space or a /tmp partition, it is not necessary to keep a persistent master key at all. A new throwaway key can be randomly generated for each session, without requiring any user interaction. This means that once unmounted, all files written to the partition in question can never be decrypted again by anyone - which in those particular use-cases is perfectly fine.

Frequently the encryption techniques use cryptographic functions to enhance the security of the master key itself. On mount of the encrypted device the passphrase or keyfile is passed through these and only the result can unlock the master key to decrypt the data.

A common setup is to apply so-called "key stretching" to the passphrase (via a "key derivation function"), and use the resulting enhanced passphrase as the mount key for decrypting the actual master key (which has been previously stored in encrypted form):

The key derivation function (e.g. PBKDF2 or scrypt) is deliberately slow (it applies many iterations of a hash function, e.g. 1000 iterations of HMAC-SHA-512), so that brute-force attacks to find the passphrase are rendered infeasible. For the normal use-case of an authorized user, it will only need to be calculated once per session, so the small slowdown is not a problem. It also takes an additional blob of data, the so-called "salt", as an argument - this is randomly generated once during set-up of the disk encryption and stored unprotected as part of the cryptographic metadata. Because it will be a different value for each setup, this makes it infeasible for attackers to speed up brute-force attacks using precomputed tables for the key derivation function.

The encrypted master key can be stored on disk together with the encrypted data. This way, the confidentiality of the encrypted data depends completely on the secret passphrase.

Additional security can be attained by instead storing the encrypted master key in a keyfile on e.g. a USB stick. This provides two-factor authentication: Accessing the encrypted data now requires something only you know (the passphrase), and additionally something only you have (the keyfile).

Another way of achieving two-factor authentication is to augment the above key retrieval scheme to mathematically "combine" the passphrase with byte data read from one or more external files (located on a USB stick or similar), before passing it to the key derivation function.The files in question can be anything, e.g. normal JPEG images, which can be beneficial for #Plausible deniability. They are still called "keyfiles" in this context, though.

After it has been derived, the master key is securely stored in memory (e.g. in a kernel keyring), for as long as the encrypted block device or folder is mounted.

It is usually not used for de/encrypting the disk data directly, though. For example, in the case of stacked filesystem encryption, each file can be automatically assigned its own encryption key. Whenever the file is to be read/modified, this file key first needs to be decrypted using the main key, before it can itself be used to de/encrypt the file contents:

In a similar manner, a separate key (e.g. one per folder) may be used for the encryption of file names in the case of stacked filesystem encryption.

In the case of block device encryption one master key is used per device and, hence, all data. Some methods offer features to assign multiple passphrases/keyfiles for the same device and others not. Some use above mentioned functions to secure the master key and others give the control over the key security fully to the user. Two examples are explained by the cryptographic parameters used by dm-crypt in plain or LUKS modes.

When comparing the parameters used by both modes one notes that dm-crypt plain mode has parameters relating to how to locate the keyfile (e.g. --keyfile-size, --keyfile-offset). The dm-crypt LUKS mode does not need these, because each blockdevice contains a header with the cryptographic metadata at the beginning. The header includes the used cipher, the encrypted master-key itself and parameters required for its derivation for decryption. The latter parameters in turn result from options used during initial encryption of the master-key (e.g. --iter-time, --use-random).

For the dis-/advantages of the different techniques, please refer back to #Comparison table or browse the specific pages.

The actual algorithm used for translating between pieces of unencrypted and encrypted data (so-called "plaintext" and "ciphertext") which correspond to each other with respect to a given encryption key, is called a "cipher".

Disk encryption employs "block ciphers", which operate on fixed-length blocks of data, e.g. 16 bytes (128 bits). At the time of this writing, the predominantly used ones are:

Encrypting/decrypting a sector (see above) is achieved by dividing it into small blocks matching the cipher's block-size, and following a certain rule-set (a so-called "mode of operation") for how to consecutively apply the cipher to the individual blocks.

Simply applying it to each block separately without modification (dubbed the "electronic codebook (ECB)" mode) would not be secure, because if the same 16 bytes of plaintext always produce the same 16 bytes of ciphertext, an attacker could easily recognize patterns in the ciphertext that is stored on disk.

The most basic (and common) mode of operation used in practice is "cipher-block chaining (CBC)". When encrypting a sector with this mode, each block of plaintext data is combined in a mathematical way with the ciphertext of the previous block, before encrypting it using the cipher. For the first block, since it has no previous ciphertext to use, a special pre-generated data block stored with the sector's cryptographic metadata and called an "initialization vector (IV)" is used:

When decrypting, the procedure is reversed analogously.

One thing worth noting is the generation of the unique initialization vector for each sector. The simplest choice is to calculate it in a predictable fashion from a readily available value such as the sector number. However, this might allow an attacker with repeated access to the system to perform a so-called watermarking attack. To prevent that, a method called "Encrypted salt-sector initialization vector (ESSIV)" can be used to generate the initialization vectors in a way that makes them look completely random to a potential attacker.

There are also a number of other, more complicated modes of operation available for disk encryption, which already provide built-in security against such attacks (and hence do not require ESSIV). One of them is XTS, which is preferred over ESSIV since cryptsetup 2.7.0. Some can also additionally guarantee authenticity of the encrypted data (i.e. confirm that it has not been modified/corrupted by someone who does not have access to the key).

Stream ciphers work in streams and do not need such thing as a "mode of operation". Nevertheless, properties required for disk encryption (e.g. "wide-block") mean that layers need to be added on top of them. As far as disk encryption on Linux is concerned, the main example is XChaCha12 in the Adiantum configuration, xchacha12,aes-adiantum, intended for low-end systems where the hardware has no AES acceleration. Adiantum is fast on such hardware. It also guarantees authenticity of the encrypted data.

See Wikipedia:Plausible deniability and Wikipedia:Deniable Encryption.

Make a backup of the user data to protect against data loss. In general the backup of your encrypted data should be encrypted as well.

There are multiple options; you can back up the disk block device where the encryption container resides as an image, e.g. /dev/sdx, or you can back up the filesystem inside of the encrypted container, e.g. /dev/mapper/dm_name, or you can back up the files, e.g. with rsync. The following sections list the advantages and disadvantages of each option.

A backup of the disk block device is:

A backup of the filesystem or files is:

If using LUKS it is possible to make a backup of the LUKS headers: it can make sense to periodically check and synchronize those backups, especially if passphrases have been revoked.

If however you have a backup of the data, and want to restore it, you can recreate the LUKS encrypted partition from scratch with cryptsetup and then restore the data, therefore backing up the LUKS header is less important than backing up the data.

**Examples:**

Example 1 (unknown):
```unknown
/var/lib/plocate/plocate.db
```

Example 2 (unknown):
```unknown
~/.volume.img
```

Example 3 (unknown):
```unknown
╔═══════╗
  sector 1 ║"???.."║
           ╠═══════╣         ╭┈┈┈┈┈╮
  sector 2 ║"???.."║         ┊ key ┊
           ╠═══════╣         ╰┈┈┬┈┈╯
           :       :            │
           ╠═══════╣            ▼             ┣┉┉┉┉┉┉┉┫
  sector n ║"???.."║━━━━━━(decryption)━━━━━━━▶┋"abc.."┋ sector n
           ╠═══════╣                          ┣┉┉┉┉┉┉┉┫
           :       :
           ╚═══════╝

           encrypted                          unencrypted
      blockdevice or                          data in RAM
        file on disk
```

Example 4 (unknown):
```unknown
╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮                         ╭┈┈┈┈┈┈┈┈┈┈┈╮
 ┊ mount passphrase ┊━━━━⎛key derivation⎞━━━━▶┊ mount key ┊
 ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯ ,──⎝   function   ⎠     ╰┈┈┈┈┈┬┈┈┈┈┈╯
 ╭──────╮            ╱                              │
 │ salt │───────────´                               │
 ╰──────╯                                           │
 ╭──────────────────────╮                           ▼         ╭┈┈┈┈┈┈┈┈┈┈┈┈╮
 │ encrypted master key │━━━━━━━━━━━━━━━━━━━━(decryption)━━━━▶┊ master key ┊
 ╰──────────────────────╯                                     ╰┈┈┈┈┈┈┈┈┈┈┈┈╯
```

---

## Stateless OpenPGP

**URL:** https://wiki.archlinux.org/title/Stateless_OpenPGP

**Contents:**
- Installation
- Features
  - Hardware device support
- Tips and tricks
  - Create a private key
  - Extract certificate
  - Create detached signature
  - Verify detached signature
  - Encrypt a message
  - Decrypt a message

Stateless OpenPGP (SOP) is a standard for command line interface (CLI) tools to perform OpenPGP operations. It is defined in a dedicated IETF draft outlining its features and syntax.

SOP is a lean approach to signing/verification and encryption/decryption operations on messages. Certificates and/or keys for all operations must be explicitly specified.

Usually private key operations use software keys. However, private key material on hardware security devices can also be used with some SOP implementations.

Many SOP implementations exist and are cross-tested in an interoperability test suite.

Although implementations provide executables of differing names, they all have the same CLI and the core functionality can be used interchangeably.

Several implementations are available for installation:

While SOP offers a uniform interface, implementations are free to support different subsets of the cryptographic mechanisms that OpenPGP specifies. Different versions of the format as well as hardware backed keys may be supported.

When using hardware security devices, SOP parameters that usually specify private key material instead only specify public key material.

This public key material serves as an explicit reference to locate and use a hardware device that provides the corresponding private key material.

The below examples assume, that the name of the SOP executable (e.g. gosop, rsop, rsop-oct or sqop) is stored in the environment variable $SOP.

To create an OpenPGP transferable secret key (aka. private key) with the User ID <archie@example.org> use:

To extract the certificate (aka. public key) from the created transferable secret key use:

To create a detached signature for a message use:

To verify the detached signature, provide the original message, the signature as well as the OpenPGP certificate:

Messages can be encrypted by providing the message and the OpenPGP certificate of the recipient:

Recipients of encrypted messages can decrypt them by providing the encrypted message and their transferable secret key:

Cleartext signed messages can be created by providing the message and the signer's transferable secret key:

**Examples:**

Example 1 (unknown):
```unknown
<archie@example.org>
```

Example 2 (unknown):
```unknown
$ $SOP generate-key "<archie@example.org>" > archie.tsk
```

Example 3 (unknown):
```unknown
$ $SOP extract-cert > archie.cert < archie.tsk
```

Example 4 (unknown):
```unknown
$ echo "Hello world" | $SOP sign archie.tsk > msg.sig
```

---

## Data-at-rest encryption

**URL:** https://wiki.archlinux.org/title/Data-at-rest_encryption

**Contents:**
- Why use encryption?
  - System data encryption
- Preparation
  - Choosing a setup
  - Preparing the disk
  - Available methods
    - Stacked filesystem encryption
      - Cloud-storage optimized
    - Block device encryption
  - Block device vs stacked filesystem encryption

This article discusses data-at-rest encryption software, which on-the-fly encrypts / decrypts data written to / read from a block device, disk partition or directory. Examples for block devices are hard drives, flash drives and DVDs.

Data-at-rest encryption should only be viewed as an adjunct to the existing security mechanisms of the operating system - focused on securing physical access, while relying on other parts of the system to provide things like network security and user-based access control.

Data-at-rest encryption ensures that files are always stored on disk in an encrypted form. The files only become available to the operating system and applications in readable form while the system is running and unlocked by a trusted user (data in use or in transit). An unauthorized person looking at the disk contents directly, will only find garbled random-looking data instead of the actual files.

For example, this can prevent unauthorized viewing of the data when the computer or hard-disk is:

In addition, data-at-rest encryption can also be used to add some security against unauthorized attempts to tamper with your operating system – for example, the installation of keyloggers or Trojan horses by attackers who can gain physical access to the system while you are away.

You will still be vulnerable to:

Data-at-rest encryption also will not protect you against someone simply wiping your disk. Regular backups are recommended to keep your data safe.

A very strong disk encryption setup (e.g. full system encryption with authenticity checking and no plaintext boot partition) is required to stand a chance against professional attackers who are able to tamper with your system before you use it. And even then it cannot prevent all types of tampering (e.g. hardware keyloggers). The best remedy might be hardware-based full-disk encryption and Trusted Computing.

While encrypting only the user data itself (often located within the home directory, or on removable media like a data DVD), is the simplest and least intrusive method, it has some significant drawbacks. In modern computer systems, there are many background processes that may cache and store information about user data or parts of the data itself in non-encrypted areas of the hard drive, like:

The solution is to encrypt both system and user data, preventing unauthorized physical access to private data that may be cached by the system. This however comes with the disadvantage that unlocking of the encrypted parts of the disk has to happen at boot time. Another benefit of system data encryption is that it complicates the installation of malware like keyloggers or rootkits for someone with physical access.

Which encryption setup is appropriate for you will depend on your goals (please read #Why use encryption? above) and system parameters.

Among other things, you will need to answer the following questions:

Then you can go on to make the required technical choices (see #Available methods and #How the encryption works below), regarding:

Before setting up encryption on a (part of a) disk, consider securely wiping it first. This consists of overwriting the entire drive or partition with a stream of zero bytes or random bytes, and is done for one or both of the following reasons:

Disk encryption does not change the fact that individual sectors are only overwritten on demand, when the file system creates or modifies the data those particular sectors hold (see #How the encryption works below). Sectors which the filesystem considers "not currently used" are not touched, and may still contain remnants of data from previous filesystems. The only way to make sure that all data which you previously stored on the drive can not be recovered, is to manually erase it. For this purpose it does not matter whether zero bytes or random bytes are used (although wiping with zero bytes will be much faster).

Ideally, the whole encrypted part of the disk should be indistinguishable from uniformly random data. This way, no unauthorized person can know which and how many sectors actually contain encrypted data - which may be a desirable goal in itself (as part of true confidentiality), and also serves as an additional barrier against attackers trying to break the encryption. In order to satisfy this goal, wiping the disk using high-quality random bytes is crucial.

The second goal only makes sense in combination with block device encryption, because in the case of stacked filesystem encryption the encrypted data can easily be located anyways (in the form of distinct encrypted files in the host filesystem). Also note that even if you only intend to encrypt a particular folder, you will have to erase the whole partition if you want to get rid of files that were previously stored in that folder in unencrypted form (due to disk fragmentation). If there are other folders on the same partition, you will have to back them up and move them back afterwards.

Once you have decided which kind of disk erasure you want to perform, refer to the Securely wipe disk article for technical instructions.

This article or section needs expansion.

All data-at-rest encryption methods operate in such a way that even though the disk actually holds encrypted data, the operating system and applications "see" it as the corresponding normal readable data as long as the cryptographic container (i.e. the logical part of the disk that holds the encrypted data) has been "unlocked" and mounted.

For this to happen, some "secret information" (usually in the form of a keyfile and/or passphrase) needs to be supplied by the user, from which the actual encryption key can be derived (and stored in the kernel keyring for the duration of the session).

If you are completely unfamiliar with this sort of operation, please also read the #How the encryption works section below.

The available data-at-rest encryption methods can be separated into two types by their layer of operation:

Stacked filesystem encryption solutions are implemented as a layer that stacks on top of an existing filesystem, causing all files written to an encryption-enabled folder to be encrypted on-the-fly before the underlying filesystem writes them to disk, and decrypted whenever the filesystem reads them from disk. This way, the files are stored in the host filesystem in encrypted form (meaning that their contents, and usually also their file/folder names, are replaced by random-looking data of roughly the same length), but other than that they still exist in that filesystem as they would without encryption, as normal files / symlinks / hardlinks / etc.

The way it is implemented, is that to unlock the folder storing the raw encrypted files in the host filesystem ("lower directory"), it is mounted (using a special stacked pseudo-filesystem) onto itself or optionally a different location ("upper directory"), where the same files then appear in readable form - until it is unmounted again, or the system is turned off.

Available solutions in this category include eCryptfs and EncFS, or one of the cloud-ready options below.

If you are deploying stacked filesystem encryption to achieve zero-knowledge synchronization with third-party-controlled locations such as cloud-storage services, you may want to consider alternatives to eCryptfs and EncFS, since these are not optimized for transmission of files over the Internet. There are some solutions designed for this purpose instead:

Note that some cloud-storage services offer zero-knowledge encryption directly through their own client applications.

Block device encryption methods, on the other hand, operate below the filesystem layer and make sure that everything written to a certain block device (i.e. a whole disk, or a partition, or a file acting as a loop device) is encrypted. This means that while the block device is offline, its whole content looks like a large blob of random data, with no way of determining what kind of filesystem and data it contains. Accessing the data happens, again, by mounting the protected container (in this case the block device) to an arbitrary location in a special way.

The following "block device encryption" solutions are available in Arch Linux:

For practical implications of the chosen layer of operation, see the #Block device vs stacked filesystem encryption below, as well as the general write up for eCryptfs. See Category:Encryption for the available content of the methods compared below, as well as other tools not included in the table.

This article or section needs expansion.

The column "dm-crypt +/- LUKS" denotes features of dm-crypt for both LUKS ("+") and plain ("-") encryption modes. If a specific feature requires using LUKS, this is indicated by "(with LUKS)". Likewise "(without LUKS)" indicates usage of LUKS is counter-productive to achieve the feature and plain mode should be used.

with systemd and /etc/crypttab

AES-Twofish, AES-Twofish-Serpent, Serpent-AES, Serpent-Twofish-AES, Twofish-Serpent

In practice, it could turn out something like:

Many other combinations are of course possible. You should carefully plan what kind of setup will be appropriate for your system.

This section is intended as a high-level introduction to the concepts and processes which are at the heart of usual disk encryption setups.

It does not go into technical or mathematical details (consult the appropriate literature for that), but should provide a system administrator with a rough understanding of how different setup choices (especially regarding key management) can affect usability and security.

For the purposes of disk encryption, each blockdevice (or individual file in the case of stacked filesystem encryption) is divided into sectors of equal length, for example 512 bytes (4096 bits). The encryption/decryption then happens on a per-sector basis, so the n'th sector of the blockdevice/file on disk will store the encrypted version of the n'th sector of the original data.

Whenever the operating system or an application requests a certain fragment of data from the blockdevice/file, the whole sector (or sectors) that contains the data will be read from disk, decrypted on-the-fly, and temporarily stored in memory:

Similarly, on each write operation, all sectors that are affected must be re-encrypted completely (while the rest of the sectors remain untouched).

In order to be able to de/encrypt data, the disk encryption system needs to know the unique secret "key" associated with it. Whenever the encrypted block device or folder in question is to be mounted, its corresponding key (called henceforth its "master key") must be supplied.

The entropy of the key is of utmost importance for the security of the encryption. A randomly generated byte string of a certain length, for example 32 bytes (256 bits), has desired properties but is not feasible to remember and apply manually during the mount.

For that reason two techniques are used as aides. The first is the application of cryptography to increase the entropic property of the master key, usually involving a separate human-friendly passphrase. For the different types of encryption the #Comparison table lists respective features. The second method is to create a keyfile with high entropy and store it on a medium separate from the data drive to be encrypted.

See also Wikipedia:Authenticated encryption.

The following are examples how to store and cryptographically secure a master key with a keyfile:

Simply storing the master key in a file (in readable form) is the simplest option. The file - called a "keyfile" - can be placed on a USB stick that you keep in a secure location and only connect to the computer when you want to mount the encrypted parts of the disk (e.g. during boot or login).

The master key (and thus the encrypted data) can be protected with a secret passphrase, which you will have to remember and enter each time you want to mount the encrypted block device or folder. See #Cryptographic metadata below for details.

In some cases, e.g. when encrypting swap space or a /tmp partition, it is not necessary to keep a persistent master key at all. A new throwaway key can be randomly generated for each session, without requiring any user interaction. This means that once unmounted, all files written to the partition in question can never be decrypted again by anyone - which in those particular use-cases is perfectly fine.

Frequently the encryption techniques use cryptographic functions to enhance the security of the master key itself. On mount of the encrypted device the passphrase or keyfile is passed through these and only the result can unlock the master key to decrypt the data.

A common setup is to apply so-called "key stretching" to the passphrase (via a "key derivation function"), and use the resulting enhanced passphrase as the mount key for decrypting the actual master key (which has been previously stored in encrypted form):

The key derivation function (e.g. PBKDF2 or scrypt) is deliberately slow (it applies many iterations of a hash function, e.g. 1000 iterations of HMAC-SHA-512), so that brute-force attacks to find the passphrase are rendered infeasible. For the normal use-case of an authorized user, it will only need to be calculated once per session, so the small slowdown is not a problem. It also takes an additional blob of data, the so-called "salt", as an argument - this is randomly generated once during set-up of the disk encryption and stored unprotected as part of the cryptographic metadata. Because it will be a different value for each setup, this makes it infeasible for attackers to speed up brute-force attacks using precomputed tables for the key derivation function.

The encrypted master key can be stored on disk together with the encrypted data. This way, the confidentiality of the encrypted data depends completely on the secret passphrase.

Additional security can be attained by instead storing the encrypted master key in a keyfile on e.g. a USB stick. This provides two-factor authentication: Accessing the encrypted data now requires something only you know (the passphrase), and additionally something only you have (the keyfile).

Another way of achieving two-factor authentication is to augment the above key retrieval scheme to mathematically "combine" the passphrase with byte data read from one or more external files (located on a USB stick or similar), before passing it to the key derivation function.The files in question can be anything, e.g. normal JPEG images, which can be beneficial for #Plausible deniability. They are still called "keyfiles" in this context, though.

After it has been derived, the master key is securely stored in memory (e.g. in a kernel keyring), for as long as the encrypted block device or folder is mounted.

It is usually not used for de/encrypting the disk data directly, though. For example, in the case of stacked filesystem encryption, each file can be automatically assigned its own encryption key. Whenever the file is to be read/modified, this file key first needs to be decrypted using the main key, before it can itself be used to de/encrypt the file contents:

In a similar manner, a separate key (e.g. one per folder) may be used for the encryption of file names in the case of stacked filesystem encryption.

In the case of block device encryption one master key is used per device and, hence, all data. Some methods offer features to assign multiple passphrases/keyfiles for the same device and others not. Some use above mentioned functions to secure the master key and others give the control over the key security fully to the user. Two examples are explained by the cryptographic parameters used by dm-crypt in plain or LUKS modes.

When comparing the parameters used by both modes one notes that dm-crypt plain mode has parameters relating to how to locate the keyfile (e.g. --keyfile-size, --keyfile-offset). The dm-crypt LUKS mode does not need these, because each blockdevice contains a header with the cryptographic metadata at the beginning. The header includes the used cipher, the encrypted master-key itself and parameters required for its derivation for decryption. The latter parameters in turn result from options used during initial encryption of the master-key (e.g. --iter-time, --use-random).

For the dis-/advantages of the different techniques, please refer back to #Comparison table or browse the specific pages.

The actual algorithm used for translating between pieces of unencrypted and encrypted data (so-called "plaintext" and "ciphertext") which correspond to each other with respect to a given encryption key, is called a "cipher".

Disk encryption employs "block ciphers", which operate on fixed-length blocks of data, e.g. 16 bytes (128 bits). At the time of this writing, the predominantly used ones are:

Encrypting/decrypting a sector (see above) is achieved by dividing it into small blocks matching the cipher's block-size, and following a certain rule-set (a so-called "mode of operation") for how to consecutively apply the cipher to the individual blocks.

Simply applying it to each block separately without modification (dubbed the "electronic codebook (ECB)" mode) would not be secure, because if the same 16 bytes of plaintext always produce the same 16 bytes of ciphertext, an attacker could easily recognize patterns in the ciphertext that is stored on disk.

The most basic (and common) mode of operation used in practice is "cipher-block chaining (CBC)". When encrypting a sector with this mode, each block of plaintext data is combined in a mathematical way with the ciphertext of the previous block, before encrypting it using the cipher. For the first block, since it has no previous ciphertext to use, a special pre-generated data block stored with the sector's cryptographic metadata and called an "initialization vector (IV)" is used:

When decrypting, the procedure is reversed analogously.

One thing worth noting is the generation of the unique initialization vector for each sector. The simplest choice is to calculate it in a predictable fashion from a readily available value such as the sector number. However, this might allow an attacker with repeated access to the system to perform a so-called watermarking attack. To prevent that, a method called "Encrypted salt-sector initialization vector (ESSIV)" can be used to generate the initialization vectors in a way that makes them look completely random to a potential attacker.

There are also a number of other, more complicated modes of operation available for disk encryption, which already provide built-in security against such attacks (and hence do not require ESSIV). One of them is XTS, which is preferred over ESSIV since cryptsetup 2.7.0. Some can also additionally guarantee authenticity of the encrypted data (i.e. confirm that it has not been modified/corrupted by someone who does not have access to the key).

Stream ciphers work in streams and do not need such thing as a "mode of operation". Nevertheless, properties required for disk encryption (e.g. "wide-block") mean that layers need to be added on top of them. As far as disk encryption on Linux is concerned, the main example is XChaCha12 in the Adiantum configuration, xchacha12,aes-adiantum, intended for low-end systems where the hardware has no AES acceleration. Adiantum is fast on such hardware. It also guarantees authenticity of the encrypted data.

See Wikipedia:Plausible deniability and Wikipedia:Deniable Encryption.

Make a backup of the user data to protect against data loss. In general the backup of your encrypted data should be encrypted as well.

There are multiple options; you can back up the disk block device where the encryption container resides as an image, e.g. /dev/sdx, or you can back up the filesystem inside of the encrypted container, e.g. /dev/mapper/dm_name, or you can back up the files, e.g. with rsync. The following sections list the advantages and disadvantages of each option.

A backup of the disk block device is:

A backup of the filesystem or files is:

If using LUKS it is possible to make a backup of the LUKS headers: it can make sense to periodically check and synchronize those backups, especially if passphrases have been revoked.

If however you have a backup of the data, and want to restore it, you can recreate the LUKS encrypted partition from scratch with cryptsetup and then restore the data, therefore backing up the LUKS header is less important than backing up the data.

**Examples:**

Example 1 (unknown):
```unknown
/var/lib/plocate/plocate.db
```

Example 2 (unknown):
```unknown
~/.volume.img
```

Example 3 (unknown):
```unknown
╔═══════╗
  sector 1 ║"???.."║
           ╠═══════╣         ╭┈┈┈┈┈╮
  sector 2 ║"???.."║         ┊ key ┊
           ╠═══════╣         ╰┈┈┬┈┈╯
           :       :            │
           ╠═══════╣            ▼             ┣┉┉┉┉┉┉┉┫
  sector n ║"???.."║━━━━━━(decryption)━━━━━━━▶┋"abc.."┋ sector n
           ╠═══════╣                          ┣┉┉┉┉┉┉┉┫
           :       :
           ╚═══════╝

           encrypted                          unencrypted
      blockdevice or                          data in RAM
        file on disk
```

Example 4 (unknown):
```unknown
╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮                         ╭┈┈┈┈┈┈┈┈┈┈┈╮
 ┊ mount passphrase ┊━━━━⎛key derivation⎞━━━━▶┊ mount key ┊
 ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯ ,──⎝   function   ⎠     ╰┈┈┈┈┈┬┈┈┈┈┈╯
 ╭──────╮            ╱                              │
 │ salt │───────────´                               │
 ╰──────╯                                           │
 ╭──────────────────────╮                           ▼         ╭┈┈┈┈┈┈┈┈┈┈┈┈╮
 │ encrypted master key │━━━━━━━━━━━━━━━━━━━━(decryption)━━━━▶┊ master key ┊
 ╰──────────────────────╯                                     ╰┈┈┈┈┈┈┈┈┈┈┈┈╯
```

---

## Vault

**URL:** https://wiki.archlinux.org/title/Vault

**Contents:**
- Installation
- Configuration
  - Development mode
  - Production configuration
    - Storage configuration
    - Listener configuration
    - UI configuration
    - API and cluster addresses
    - Security considerations
    - Audit logging configuration

Vault is an open-source tool from HashiCorp for securely managing secrets and protecting sensitive data. It provides encryption as a service, access control, and detailed audit logging.

Install the vault package.

Vault can be run in development mode for testing or configured as a production server with enhanced security settings. The configuration is defined in a file using the "Hashicorp Command Language" (HCL) format.

For testing, Vault can be run in development mode, which starts with an in-memory storage backend and automatically unseals itself.

To start Vault in development mode, run the following command:

To set up a production-ready Vault server, create a configuration file:

Then, add your desired configuration settings to /etc/vault/config.hcl.

Vault supports multiple storage backends. For a simple file-based backend, use:

For high-availability or heavy usage environments, consider using consul, dynamodbAUR, or other supported storage solutions that offer scalability and reliability.

Vault listens on a TCP port for API requests. For basic configurations without TLS, use:

If TLS is required for secure communication, configure it as follows:

To enable the Vault web interface, add:

Set the API and cluster addresses for proper networking:

By default, Vault locks memory to prevent sensitive data from being swapped to disk. This enhances security by ensuring that secrets do not end up in the swap space, where they could be accessed by unauthorized users or forensic tools.

However, using mlock requires ensuring that the system has sufficient memory and allows unlimited memory locking. If the system lacks adequate RAM or has restrictive memory limits, enabling mlock could cause Vault to fail unexpectedly. To safely use mlock, ensure:

If your system does not meet these requirements, you may need to disable mlock. To do so (not recommended for production environments):

Vault uses audit devices to log client requests and responses for security and troubleshooting purposes. The audit logs help track access patterns, detect anomalies, and ensure compliance.

To enable a file-based audit log, configure an audit device in Vault:

This will log audit events to /var/log/vault-audit.log in JSON format, making it easier to parse and analyze.

To ensure Vault can write to the audit log securely, set the correct permissions:

Vault supports multiple audit logging backends besides files, For a full list of supported audit devices and advanced configuration options, refer to the official documentation.

Vault provides logging capabilities to help monitor its operations, troubleshoot issues, and analyze system behavior. By default, logs are sent to stdout, but they can also be written to a file.

To configure Vault to log to a file, specify the log file path and log level in the configuration:

To ensure Vault can write logs properly, adjust file permissions:

Below is a complete example combining the above settings:

Optionally, Vault can be run as a systemd service to ensure it starts automatically at boot, restarts upon failure, and integrates well with process management on Linux. This approach is particularly useful in production environments where Vault needs to remain available without manual intervention.

Next, enable/start the vault.service.

Set the environment variable to specify the Vault address. This ensures that Vault commands interact with the correct server instance without requiring the address to be manually specified each time.

To make this persistent across reboots:

Vault encrypts and protects secrets, requiring an "unsealing" process to decrypt and access them after a restart. When initialized, Vault generates multiple unseal keys, and a minimum threshold of these keys is needed to unseal the Vault. This ensures that no single person has full access, adding an extra layer of security.

To initialize Vault, run:

This will output 5 unseal keys and an initial root token. Save these securely!

Vault can be configured to auto-unseal using cloud-based KMS services (such as AWS KMS, GCP KMS) or hardware security modules (HSMs). This eliminates the need for manual key entry upon startup. For more info refer to the official Vault auto-unseal documentation.

For manual unsealing, Vault must be unsealed with at least three different keys:

Open http://127.0.0.1:8200 in your browser.

You will see a login screen where you can use your root token to access the Vault UI.

**Examples:**

Example 1 (unknown):
```unknown
$ vault server -dev
```

Example 2 (unknown):
```unknown
# mkdir /etc/vault
# touch /etc/vault/config.hcl
```

Example 3 (unknown):
```unknown
/etc/vault/config.hcl
```

Example 4 (unknown):
```unknown
storage "file" {
    path = "/opt/vault/data"
}
```

---

## Security

**URL:** https://wiki.archlinux.org/title/Security

**Contents:**
- Concepts
- Passwords
  - Choosing secure passwords
  - Maintaining passwords
  - Password hashes
  - Enforcing strong passwords with pam_pwquality
- CPU
  - Microcode
  - Hardware vulnerabilities
    - Simultaneous multithreading (hyper-threading)

This article contains recommendations and best practices for hardening an Arch Linux system.

Passwords are key to a secure system. They secure your user accounts, encrypted filesystems, and SSH/GPG keys. They are the main way a computer chooses to trust the person using it, so a big part of security is just about picking secure passwords and protecting them.

Passwords must be complex enough to not be easily guessed from e.g. personal information, or cracked using methods like social engineering or brute-force attacks. The tenets of strong passwords are based on length and randomness. In cryptography the quality of a password is often referred to as its entropy.

Insecure passwords include those containing or those using as a base before substitution/variation:

The best choice for a password is something long (the longer, the better) and generated from a random source. It is important to use a long password. Weak hash algorithms allow an 8-character password hash to be compromised in just a few hours.

Tools like pwgen or apgAUR can generate random passwords. However, these passwords can be difficult to memorize. One memorization technique (for ones often typed) is to generate a long password and memorize a minimally secure number of characters, temporarily writing down the full generated string. Over time, increase the number of characters typed - until the password is ingrained in muscle memory and need not be remembered. This technique is more difficult, but can provide confidence that a password will not turn up in wordlists or "intelligent" brute force attacks that combine words and substitute characters.

Apart from password management, keepassxc offers password/passphrase generation. It is possible to customize the generation in a GUI. Dictionary based passphrases are also supported.

One technique for memorizing a password is to use a mnemonic phrase, where each word in the phrase reminds you of the next character in the password. Take for instance “the girl is walking down the rainy street” could be translated to t6!WdtR5 or, less simply, t&6!RrlW@dtR,57. This approach could make it easier to remember a password, but note that the various letters have very different probabilities of being found at the start of words (Wikipedia:Letter frequency).

Another effective technique can be to write randomly generated passwords down and store them in a safe place, such as in a wallet, purse, or document safe. Most people do a generally good job of protecting their physical valuables from attack, and it is easier for most people to understand physical security best practices compared to digital security practices.

It is also very effective to combine the mnemonic and random technique by saving long randomly generated passwords with a password manager, which will be in turn accessed with a memorable "master password"/primary password that must be used only for that purpose. The master password must be memorized and never saved. This requires the password manager to be installed on a system to easily access the password (which could be seen as an inconvenience or a security feature, depending on the situation). Some password managers also have smartphone apps which can be used to display passwords for manual entry on systems without that password manager installed (if that is a common use case, you could still use easily typeable but secure passwords for each service instead of completely random ones, see below). Note that a password manager introduces a single point of failure if you ever forget the master password. Some password managers compute the contained passwords based on the master password and the service name where you want to log in instead of encrypting them, making it possible to use it on a new system without syncing any data.

It can be effective to use a memorable long series of unrelated words as a password. The theory is that if a sufficiently long phrase is used, the gained entropy from the password's length can counter the lost entropy from the use of dictionary words. This xkcd comic demonstrates the entropy tradeoff of this method, taking into account the limited set of possible words for each word in the passphrase. If the set of words you choose from is large (multiple thousand words) and you choose 5-7 or even more random words from it, this method provides great entropy, even assuming the attacker knows the set of possible words chosen from and the number of words chosen. The number of possible passphrases after settling on a set of words and number of words is: (number of words in the set of words to select from) to the power of (the number of words chosen for the passphrase). See e.g. Diceware for more.

See The passphrase FAQ or Wikipedia:Password strength for some additional background.

Once you pick a strong password, be sure to keep it safe. Watch out for keyloggers (software and hardware), screen loggers, social engineering, shoulder surfing, and avoid reusing passwords so insecure servers cannot leak more information than necessary. Password managers can help manage large numbers of complex passwords: if you are copy-pasting the stored passwords from the manager to the applications that need them, make sure to clear the copy buffer every time, and ensure they are not saved in any kind of log (e.g. do not paste them in plain terminal commands, which would store them in files like .bash_history). Note that password managers that are implemented as browser extensions may be vulnerable to side channel attacks. These can be mitigated by using password managers that run as separate applications.

As a rule, do not pick insecure passwords just because secure ones are harder to remember. Passwords are a balancing act. It is better to have an encrypted database of secure passwords, guarded behind a key and one strong master password, than it is to have many similar weak passwords. Writing passwords down is perhaps equally effective [1], avoiding potential vulnerabilities in software solutions while requiring physical security.

Another aspect of the strength of the passphrase is that it must not be easily recoverable from other places.

If you use the same passphrase for disk encryption as you use for your login password (useful e.g. to auto-mount the encrypted partition or folder on login), make sure that /etc/shadow ends up on an encrypted partition or/and uses a strong key derivation function (i.e. yescrypt/argon2 or sha512 with PBKDF2, but not md5 or low iterations in PBKDF2) for the stored password hash (see SHA password hashes for more information).

If you are backing up your password database, make sure that each copy is not stored behind any other passphrase which in turn is stored in it, e.g. an encrypted drive or an authenticated remote storage service, or you will not be able to access it in case of need; a useful trick is to protect the drives or accounts where the database is backed up using a simple cryptographic hash of the master password. Maintain a list of all the backup locations: if one day you fear that the master passphrase has been compromised you will have to change it immediately on all the database backups and the locations protected with keys derived from the master password.

Version-controlling the database in a secure way can be very complicated: if you choose to do it, you must have a way to update the master password of all the database versions. It may not always be immediately clear when the master password is leaked: to reduce the risk of somebody else discovering your password before you realize that it leaked, you may choose to change it on a periodical basis. If you fear that you have lost control over a copy of the database, you will need to change all the passwords contained in it within the time that it may take to brute-force the master password, according to its entropy.

A hash is a one-way function, i.e. it is designed to make it impossible to deduct the input without computing the hash function with it (example: MD5, SHA).

A password-hash function is designed to make deducting a user-input (password) impossible without computing the hash function with it (example: bcrypt). A key derivation function (KDF; examples: yescrypt, scrypt, PBKDF2) is a cryptographic algorithm designed to derive secret keys (e.g. an AES key, a password hash) from an input (a master key, a password). Hence, a KDF can serve multiple applications, including those of a password-hash function.

By default, Arch stores the hashed user passwords in the root-only-readable /etc/shadow file, separated from the other user parameters stored in the world-readable /etc/passwd file, see Users and groups#User database. See also #Restricting root.

Passwords are set with the passwd command, which stretches them with the system's crypt function and then saves them in /etc/shadow. The passwords are also salted in order to defend them against rainbow table attacks. See also How are passwords stored in Linux (Understanding hashing with shadow utils).

Since password hashes follow a defined format, the method and parameter can be configured for subsequent new invocations of the passwd command. Hence, the individual hashes stored in the /etc/shadow file can be a heterogeneous mix of the hash functions supported by the system.

See crypt(5) for more information on the format, hashing methods and parameters.

The /etc/login.defs file configures the default password hashing method ENCRYPT_METHOD YESCRYPT and its parameter YESCRYPT_COST_FACTOR.

For example, an increment of the default YESCRYPT_COST_FACTOR parameter will lead to a logarithmic increase of the compute time required to deduce the hash from a password. This applies, likewise, to a third-party trying to obtain the password secret, and the system to authenticate a user log-in.

In contrast, the compute time for the SHA-512 hash function is configured by a parameter with a linear influence. See SHA password hashes for information on the previous Arch default. Note the yescrypt algorithm internally uses SHA-256, HMAC and PBKDF2 to compute its password-hash. The main reason is to combine positive attributes of these widely used and tested functions for an enhanced resistance to attacks. For example, the usability of SHA for various purposes has resulted in hardware support for the function, i.e. the performance to compute a pure SHA hash has accelerated considerably, making its application as a password-hash function more and more derelict.

pam_pwquality provides protection against Dictionary attacks and helps configure a password policy that can be enforced throughout the system. It is based on pam_cracklib, so it is backwards compatible with its options.

Install the libpwquality package.

If for example you want to enforce this policy:

Edit the /etc/pam.d/passwd file to read as:

The password required pam_unix.so use_authtok instructs the pam_unix module to not prompt for a password but rather to use the one provided by pam_pwquality.

You can refer to the pam_pwquality(8) and pam_unix(8) man pages for more information.

See microcode for information on how to install important security updates for your CPU's microcode.

Some CPUs contain hardware vulnerabilities. See the kernel documentation on hardware vulnerabilities for a list of these vulnerabilities, as well as mitigation selection guides to help customize the kernel to mitigate these vulnerabilities for specific usage scenarios.

To check if you are affected by a known vulnerability, run the following:

In most cases, updating the kernel and microcode will mitigate vulnerabilities.

Simultaneous multithreading (SMT), also called hyper-threading on Intel CPUs, is a hardware feature that may be a source of L1 Terminal Fault and Microarchitectural Data Sampling vulnerabilities. The Linux kernel and microcode updates contain mitigations for known vulnerabilities, but disabling SMT may still be required on certain CPUs if untrusted virtualization guests are present.

SMT can often be disabled in your system's firmware. Consult your motherboard or system documentation for more information. You can also disable SMT in the kernel by adding the following kernel parameter:

hardened_mallocAUR is a hardened replacement for glibc's malloc(). The project was originally developed for integration into Android's Bionic and musl by Daniel Micay, of GrapheneOS, but he has also built in support for standard Linux distributions on the x86_64 architecture.

While hardened_malloc is not yet integrated into glibc (assistance and pull requests welcome) it can be used easily with LD_PRELOAD. In testing so far, it only causes issues with a handful of applications if enabled globally in /etc/ld.so.preload. Since hardened_malloc has a performance cost, you may want to decide which implementation to use on a case-by-case basis based on attack surface and performance needs.

The factual accuracy of this article or section is disputed.

To try it out in a standalone manner, use the hardened-malloc-preload wrapper script, or manually start an application with the proper preload value:

Proper usage with Firejail can be found on its wiki page, and some configurable build options for hardened_malloc can be found on the github repo.

Data-at-rest encryption, preferably full-disk encryption with a strong passphrase, is the only way to guard data against physical recovery. This provides data confidentiality when the computer is turned off or the disks in question are unmounted.

Once the computer is powered on and the drive is mounted, however, its data becomes just as vulnerable as an unencrypted drive. It is therefore best practice to unmount data partitions as soon as they are no longer needed.

You may also encrypt a drive with the key stored in a TPM, although it has had vulnerabilites in the past and the key can be extracted by a bus sniffing attack.

Certain programs, like dm-crypt, allow the user to encrypt a loop file as a virtual volume. This is a reasonable alternative to full-disk encryption when only certain parts of the system need to be secure.

While the block-device or filesystem-based encryption types compared in the data-at-rest encryption article are useful at protecting data on physical media, most can not be used to protect data on a remote system that you can not control (such as cloud storage). In some cases, individual file encryption will be useful.

These are some methods to encrypt files:

The kernel now prevents security issues related to hardlinks and symlinks if the fs.protected_hardlinks and fs.protected_symlinks sysctl switches are enabled, so there is no longer a major security benefit from separating out world-writable directories.

File systems containing world-writable directories can still be kept separate as a coarse way of limiting the damage from disk space exhaustion. However, filling /var or /tmp is enough to take down services. More flexible mechanisms for dealing with this concern exist (like quotas), and some file systems include related features themselves (Btrfs has quotas on subvolumes).

Following the principle of least privilege, file systems should be mounted with the most restrictive mount options possible (without losing functionality).

Relevant mount options are:

File systems used for data should always be mounted with nodev, nosuid and noexec.

Potential file system mounts to consider:

When utilizing file system snapshots, e.g. with Btrfs, LVM, or ZFS, it is essential to be aware that snapshots may retain sensitive information that users expect to be deleted. This is especially true when automatic snapshotting tools like Snapper are configured, as they can capture snapshots at regular intervals or in response to system events. Here are some examples of how sensitive information in /home/ can persist within snapshots:

If this is supported, consider excluding such directories from snapshots altogether. For example, if using Btrfs, you can create subvolumes for example .cache/, .config/, .local/, .var/ or any other directory according to your use-case.

The factual accuracy of this article or section is disputed.

The default file permissions allow read access to almost everything and changing the permissions can hide valuable information from an attacker who gains access to a non-root account such as the http or nobody users. You can use chmod to take away all permissions from the group and others:

Some paths to consider are:

The default umask 0022 can be changed to improve security for newly created files. The NSA RHEL5 Security Guide suggests a umask of 0077 for maximum security, which makes new files not readable by users other than the owner. To change this, see Umask#Set the mask value. If you use sudo, consider configuring it to use the default root umask.

It is important to be aware of any files with the Setuid or Setgid bit. Examples of relevant files with the SUID bit set:

The prominent risks of such executable files include privilege escalation vulnerabilities, see e.g Wikipedia:Setuid#Security impact.[5][6][7]

Files with the SUID bit set and not owned by root, or files with the SGID bit set typically have less potential impact but can theoretically still do decent damage if vulnerable. It is usually possible to avoid using SUID or SGID by assigning Capabilities instead.

To search for files with either the SUID or SGID bit:

This article or section is a candidate for merging with System backup.

Regularly create backups of important data. Regularly test the integrity of the backups. Regularly test that the backups can be restored.

Make sure that at least one copy of the data is stored offline, i.e. not connected to the system under threat in any way. Ransomware and other destructive attacks may also attack any connected backup systems.

See Solid state drive#Setting the SATA SSD state to frozen mode after waking up from sleep.

Following the principle of least privilege, do not use the root user for daily use. Create a non-privileged user account for each person using the system. See List of applications/Security#Privilege elevation for ways of temporarily gaining privileged access.

Add the following line to /etc/pam.d/system-login to add a delay of at least 4 seconds between failed login attempts:

4000000 is the time in microseconds to delay.

In particular, both pam_unix and pam_faillock set a minimum delay of 2 seconds by default. In order to completely remove this delay, you need to add the nodelay parameter to any auth lines of these modules, e.g.

Since pambase 20200721.1-2, pam_faillock.so is enabled by default to lock out users for 10 minutes after 3 failed login attempts in a 15 minute period (see FS#67644). The lockout only applies to password authentication (e.g. login and sudo), public key authentication over SSH is still accepted. To prevent complete denial-of-service, this lockout is disabled for the root user by default.

To unlock a user, do:

By default, the lock mechanism is a file per-user located at /run/faillock/. Deleting or emptying the file unlocks that user—the directory is owned by root, but the file is owned by the user, so the faillock command only empties the file, therefore does not require root.

The module pam_faillock.so can be configured with the file /etc/security/faillock.conf. The lockout parameters:

By default, all user locks are lost after reboot. If your attacker can reboot the machine, it is more secure if locks persist. To make locks persist, change the dir parameter in /etc/security/faillock.conf to /var/lib/faillock.

No restart is required for changes to take effect. See faillock.conf(5) for further configuration options, such as enabling lockout for the root account, disabling for centralized login (e.g. LDAP), etc.

On systems with many, or untrusted users, it is important to limit the number of processes each can run at once, therefore preventing fork bombs and other denial of service attacks. The /etc/security/limits.conf configuration determines how many processes each user, or group can have open, and is empty (except for useful comments) by default. Adding the following lines to this file will limit all users to 100 active processes, unless they use the prlimit command to explicitly raise their maximum to 200 for that session. These values can be changed according to the appropriate number of processes a user should have running, or the hardware of the box you are administrating.

The current number of threads for each user can be found with ps --no-headers -Leo user | sort | uniq --count. This may help with determining appropriate values for the users' limits; see also limits.conf.

Prefer using Wayland over Xorg. Xorg's design predates modern security practices and is considered insecure by many. For example, Xorg applications may record keystrokes while inactive.

If you must run Xorg, it is recommended to avoid running it as root. Within Wayland, the Xwayland compatibility layer will automatically use rootless Xorg.

The root user is, by definition, the most powerful user on a system. It is also difficult to audit the root user account. It is therefore important to restrict usage of the root user account as much as possible. There are a number of ways to keep the power of the root user while limiting its ability to cause harm.

This article or section is a candidate for merging with sudo.

Using sudo for privileged access is preferable to su for a number of reasons.

Or, individual commands can be allowed for all users. To mount Samba shares from a server as a regular user:

This allows all users who are members of the group users to run the commands /sbin/mount.cifs and /sbin/umount.cifs from any machine (ALL).

Exporting EDITOR=nano visudo is regarded as a severe security risk since everything can be used as an EDITOR.

See Sudo#Editing files. Alternatively, you can use an editor like rvim or rnano which has restricted capabilities in order to be safe to run as root.

Once sudo is properly configured, full root access can be heavily restricted or denied without losing much usability. To disable root, but still allowing to use sudo, you can use passwd(1) with passwd --lock root.

The PAM pam_wheel.so lets you allow only users in the group wheel to login using su. See su#su and wheel.

Even if you do not wish to deny root login for local users, it is always good practice to deny root login via SSH. The purpose of this is to add an additional layer of security before a user can completely compromise your system remotely.

When someone attempts to log in with PAM, /etc/security/access.conf is checked for the first combination that matches their login properties. Their attempt then fails or succeeds based on the rule for that combination.

Rules can be set for specific groups and users. In this example, the user archie is allowed to login locally, as are all users in the wheel and adm groups. All other logins are rejected:

Read more at access.conf(5)

Mandatory access control (MAC) is a type of security policy that differs significantly from the discretionary access control (DAC) used by default in Arch and most Linux distributions. MAC essentially means that every action a program could perform that affects the system in any way is checked against a security ruleset. This ruleset, in contrast to DAC methods, cannot be modified by users. Using virtually any mandatory access control system will significantly improve the security of your computer, although there are differences in how it can be implemented.

Pathname-based access control is a simple form of access control that offers permissions based on the path of a given file. The downside to this style of access control is that permissions are not carried with files if they are moved around the system. On the positive side, pathname-based MAC can be implemented on a much wider range of filesystems, unlike labels-based alternatives.

Labels-based access control means the extended attributes of a file are used to govern its security permissions. While this system is arguably more flexible in its security offerings than pathname-based MAC, it only works on filesystems that support these extended attributes.

Access Control Lists (ACLs) are an alternative to attaching rules directly to the filesystem in some way. ACLs implement access control by checking program actions against a list of permitted behavior.

The linux-hardened package uses a basic kernel hardening patch set and more security-focused compile-time configuration options than the linux package. A custom build can be made to choose a different compromise between security and performance than the security-leaning defaults.

However, it should be noted that several packages will not work when using this kernel. For example throttled.

If you use an out-of-tree driver such as NVIDIA, you may need to switch to its DKMS package.

The linux-hardened package provides an improved implementation of Address Space Layout Randomization for userspace processes. The paxtest command can be used to obtain an estimate of the provided entropy:

Setting kernel.kptr_restrict to 1 will hide kernel symbol addresses in /proc/kallsyms from regular users without CAP_SYSLOG, making it more difficult for kernel exploits to resolve addresses/symbols dynamically. This will not help that much on a pre-compiled Arch Linux kernel, since a determined attacker could just download the kernel package and get the symbols manually from there, but if you are compiling your own kernel, this can help mitigating local root exploits. This will break some perf commands when used by non-root users (but many perf features require root access anyway). See FS#34323 for more information.

Setting kernel.kptr_restrict to 2 will hide kernel symbol addresses in /proc/kallsyms regardless of privileges.

BPF is a system used to load and execute bytecode within the kernel dynamically during runtime. It is used in a number of Linux kernel subsystems such as networking (e.g. XDP, tc), tracing (e.g. kprobes, uprobes, tracepoints) and security (e.g. seccomp). It is also useful for advanced network security, performance profiling and dynamic tracing.

BPF was originally an acronym of Berkeley Packet Filter since the original classic BPF was used for packet capture tools for BSD. This eventually evolved into Extended BPF (eBPF), which was shortly afterwards renamed to just BPF (not an acronym). BPF should not be confused with packet filtering tools like iptables or netfilter, although BPF can be used to implement packet filtering tools.

BPF code may be either interpreted or compiled using a Just-In-Time (JIT) compiler. The Arch kernel is built with CONFIG_BPF_JIT_ALWAYS_ON which disables the BPF interpreter and forces all BPF to use JIT compilation. This makes it harder for an attacker to use BPF to escalate attacks that exploit SPECTRE-style vulnerabilities. See the kernel patch which introduced CONFIG_BPF_JIT_ALWAYS_ON for more details.

The kernel includes a hardening feature for JIT-compiled BPF which can mitigate some types of JIT spraying attacks at the cost of performance and the ability to trace and debug many BPF programs. It may be enabled by setting net.core.bpf_jit_harden to 1 (to enable hardening of unprivileged code) or 2 (to enable hardening of all code).

See the net.core.bpf_* settings in the kernel documentation for more details.

The ptrace(2) syscall provides a means by which one process (the "tracer") may observe and control the execution of another process (the "tracee"), and examine and change the tracee's memory and registers. ptrace is commonly used by debugging tools including gdb, strace, perf, reptyr and other debuggers. However, it also provides a means by which a malicious process can read data from and take control of other processes.

Arch enables the Yama LSM by default, which provides a kernel.yama.ptrace_scope kernel parameter. This parameter is set to 1 (restricted) by default which prevents tracers from performing a ptrace call on traces outside of a restricted scope unless the tracer is privileged or has the CAP_SYS_PTRACE capability. This is a significant improvement in security compared to the classic permissions. Without this module, there is no separation between processes running as the same user (in the absence of additional security layers such as pid_namespaces(7)).

If you do not need to use debugging tools, consider setting kernel.yama.ptrace_scope to 2 (admin-only) or 3 (no ptrace possible) to harden the system.

This article or section needs expansion.

The factual accuracy of this article or section is disputed.

The kernel has the ability to hide other users' processes, normally accessible via /proc, from unprivileged users by mounting the proc filesystem with the hidepid= and gid= options documented in https://docs.kernel.org/filesystems/proc.html.

This greatly complicates an intruder's task of gathering information about running processes, whether some daemon runs with elevated privileges, whether other user runs some sensitive program, whether other users run any program at all, makes it impossible to learn whether any user runs a specific program (given the program does not reveal itself by its behaviour), and, as an additional bonus, poorly written programs passing sensitive information via program arguments are now protected against local eavesdroppers.

The proc group, provided by the filesystem package, acts as a whitelist of users authorized to learn other users' process information. If users or services need access to /proc/<pid> directories beyond their own, add them to the group.

For example, to hide process information from other users except those in the proc group:

For user sessions to work correctly, an exception needs to be added for systemd-logind:

The default Arch kernel has CONFIG_MODULE_SIG_ALL enabled, which signs all kernel modules built as part of the linux package. This allows the kernel to only load modules signed with a valid key, i.e. out-of-tree modules compiled locally or provided by packages such as virtualbox-host-modules-arch cannot be loaded.

Kernel module loading can be restricted by setting the module.sig_enforce=1 kernel parameter. More information can be found in the kernel documentation.

Further, unneeded individual modules can be blacklisted, see secureblue for examples.

Kexec allows replacing the current running kernel.

Since Linux 5.4 the kernel has gained an optional lockdown feature, intended to strengthen the boundary between UID 0 (root) and the kernel. When enabled some applications may cease to work which rely on low-level access to either hardware or the kernel.

To use lockdown, its LSM must be initialized and a lockdown mode must be set.

All officially supported kernels initialize the LSM, but none of them enforce any lockdown mode.

Lockdown has two modes of operation:

It is recommended to use integrity, unless your specific threat model dictates otherwise.

To enable kernel lockdown at runtime, run:

To enable kernel lockdown on boot, use the kernel parameter lockdown=mode.

See also kernel_lockdown(7).

LKRG (lkrg-dkmsAUR) is a kernel module which performs integrity checking of the kernel and detection of exploit attempts.

The factual accuracy of this article or section is disputed.

The emergency shell is used to interactively troubleshoot the machine during the boot process. However, it is also a gadget that an attacker can use to access secure resources such as the TPM. See this article for a practical example. The difficulty of attacks can be increased by disabling the emergency shell, at the tradeoff of removing a tool to troubleshoot early boot failures.

To disable the emergency shell, See systemd#Disable emergency mode on remote machine.

See also Wikipedia:Sandbox (computer security).

To improve the security of systemd service units, see systemd/Sandboxing.

To mitigate this, either:

Note that this can break applications such as nsjail. Chromium based applications need SUID bit for chrome-sandbox to work with this setting.

Firejail is an easy to use tool for sandboxing applications and servers alike. It was originally created for browsers and internet facing applications, but supports a large number of applications by now. To establish a sandboxed environment with a variety of features, it is installed as a suid binary and builds a sandboxed runtime environment for the target application based on black and white lists.

bubblewrap is a sandbox application developed for unprivileged container tools like Flatpak with a significantly smaller resource footprint and complexity than Firejail. While it lacks certain features such as file path whitelisting, bubblewrap does offer bind mounts as well as the creation of user/IPC/PID/network/cgroup namespaces and can support both simple and complex sandboxes. For the linux-hardened kernel you will need to to use bubblewrap-suid.

Bubblejail sandbox is based on bubblewrap and provides a resource oriented permission model with a graphical interface to tweak permissions.

Portable is a sandboxing framework which utilizes bubblewrap and many other tools to lockdown running applications. It is designed to be simple for packagers and efficient for users, yet cuts off security holes and monitors background processes by default.

See portable-arch for a repository of applications sandboxed by portable.

If a sandboxed application does not utilize the Portal file chooser, portable can pass files to the sandbox (by passing --actions share-files).

Portable is fully functional on GNOME, while other desktops may lack small amounts of features like advanced background monitoring and ScreenShot portal.

Manual chroot jails can also be constructed to build sandboxed process environments. It is much more limited than other sandboxing technologies; the extent of its sandboxing is file path isolation.

Linux Containers are another good option when you need more separation than the other options (short of full system virtualization) provide. LXC is run on top of the existing kernel in a pseudo-chroot with their own virtual hardware.

Using full virtualization options such as VirtualBox, KVM, Xen or Qubes OS (based on Xen) can also improve isolation and security in the event you plan on running risky applications or browsing dangerous websites.

While the stock Arch kernel is capable of using Netfilter's iptables and nftables, the services are not enabled by default. It is highly recommended to set up some form of firewall to protect the services running on the system. Many resources (including ArchWiki) do not state explicitly which services are worth protecting, so enabling a firewall is a good precaution.

This article or section needs language, wiki syntax or style improvements. See Help:Style for reference.

Some services listen for inbound traffic on open network ports. It is important to only bind these services to the addresses and interfaces that are strictly necessary. It may be possible for a remote attacker to exploit flawed network protocols to access exposed services. This can even happen with processes bound to localhost.

In general, if a service only needs to be accessible to the local system, bind to a Unix domain socket (unix(7)) or a loopback address such as localhost instead of a non-loopback address like 0.0.0.0/0.

If a service needs to be accessible to other systems via the network, control the access with strict firewall rules and configure authentication, authorization and encryption whenever possible.

You can list all current open ports with ss -l. To show all listening processes and their numeric tcp and udp port numbers:

See ss(8) for more options.

Kernel parameters which affect networking can be set using Sysctl. For how to do this, see Sysctl#TCP/IP stack hardening.

To mitigate brute-force attacks it is recommended to enforce key-based authentication. For OpenSSH see OpenSSH#Protection for more recommendations. Alternatively Fail2ban or Sshguard offer lesser forms of protection by monitoring logs and writing firewall rules but open up the potential for a denial of service, since an attacker can spoof packets as if they came from the administrator after identifying their address. Spoofing IP has lines of defense, such as by reverse path filtering and disabling ICMP redirects.

You may want to harden authentication even more by using two-factor authentication. Google Authenticator provides a two-step authentication procedure using one-time passcodes (OTP).

Denying root login is also a good practice, both for tracing intrusions and adding an additional layer of security before root access. For OpenSSH, see OpenSSH#Deny.

Mozilla publishes an OpenSSH configuration guide which configures more verbose audit logging and restricts ciphers.

The default domain name resolution (DNS) configuration is highly compatible but has security weaknesses. See DNS privacy and security for more information.

Proxies are commonly used as an extra layer between applications and the network, sanitizing data from untrusted sources. The attack surface of a small proxy running with lower privileges is significantly smaller than a complex application running with the end user privileges.

For example the DNS resolver is implemented in glibc, that is linked with the application (that may be running as root), so a bug in the DNS resolver might lead to a remote code execution. This can be prevented by installing a DNS caching server, such as dnsmasq, which acts as a proxy. [13]

See TLS#Trust management.

Physical access to a computer is root access given enough time and resources. However, a high practical level of security can be obtained by putting up enough barriers.

An attacker can gain full control of your computer on the next boot by simply attaching a malicious IEEE 1394 (FireWire), Thunderbolt or PCI Express device as they are given full memory access by default.[14] For Thunderbolt, you can restrict the direct memory access completely or to known devices, see Thunderbolt#User device authorization. For Firewire and PCI Express, there is little you can do from preventing this, or modification of the hardware itself - such as flashing malicious firmware onto a drive. However, the vast majority of attackers will not be this knowledgeable and determined.

#Data-at-rest encryption will prevent access to your data if the computer is stolen, but malicious firmware can be installed to obtain this data upon your next log in by a resourceful attacker.

Adding a password to the BIOS prevents someone from booting into removable media, which is basically the same as having root access to your computer. You should make sure your drive is first in the boot order and disable the other drives from being bootable if you can.

It is highly important to protect your boot loader. An unprotected boot loader can bypass any login restrictions, e.g. by setting the init=/bin/sh kernel parameter to boot directly to a shell.

Syslinux supports password-protecting your boot loader. It allows you to set either a per-menu-item password or a global boot loader password.

GRUB supports boot loader passwords as well. See GRUB/Tips and tricks#Password protection of GRUB menu for details. It also has support for encrypted /boot, which only leaves some parts of the boot loader code unencrypted. GRUB's configuration, kernel and initramfs are encrypted.

systemd-boot disables editing of kernel parameters when #Secure Boot is enabled. Alternatively, see systemd-boot#Kernel parameters editor with password protection for a more traditional password-based option.

Secure Boot is a feature of UEFI that allows authentication of the files your computer boots. This helps preventing some evil maid attacks such as replacing files inside the boot partition. Normally computers come with keys that are enrolled by vendors (OEM). However these can be removed and allow the computer to enter Setup Mode which allows the user to enroll and manage their own keys.

The secure boot page guides you through how to set secure boot up by using your own keys.

TPMs are hardware microprocessors which have cryptographic keys embedded. This forms the fundamental root of trust of most modern computers and allows end-to-end verification of the boot chain. They can be used as internal smartcards, attest the firmware running on the computer and allow users to insert secrets into a tamper-proof and brute-force resistant store.

One popular idea is to place the boot partition on a flash drive in order to render the system unbootable without it. Proponents of this idea often use full-disk encryption alongside, and some also use detached encryption headers placed on the boot partition.

This method can also be merged with encrypting /boot.

If you are using Bash or Zsh, you can set TMOUT for an automatic logout from shells after a timeout.

For example, the following will automatically log out from virtual consoles (but not terminal emulators in X11):

If you really want EVERY Bash/Zsh prompt (even within X) to timeout, use:

Note that this will not work if there is some command running in the shell (eg.: an SSH session or other shell without TMOUT support). But if you are using VC mostly for restarting frozen GDM/Xorg as root, then this is very useful.

The kernel has settings to deactivate USB ports to protect your computer against rogue USB devices (a.k.a. BadUSB, PoisonTap or LanTurtle). They can be set at runtime and automated via sysctl.

For more control install USBGuard, which is a software framework implementing basic whitelisting and blacklisting capabilities based on device attributes.

A computer that is powered on may be vulnerable to volatile data collection. It is a best practice to turn a computer completely off at times it is not necessary for it to be on, or if the computer's physical security is temporarily compromised (e.g. when passing through a security checkpoint).

Attacks on package managers are possible without proper use of package signing, and can affect even package managers with proper signature systems. Arch uses package signing by default and relies on a web of trust from 5 trusted master keys. See Pacman-key for details.

It is important to regularly upgrade the system.

Subscribe to the Common Vulnerabilities and Exposure (CVE) Security Alert updates, made available by National Vulnerability Database, and found on the NVD Download webpage. The Arch Linux Security Tracker serves as a particularly useful resource in that it combines Arch Linux Security Advisory (ASA), Arch Linux Vulnerability Group (AVG) and CVE data sets in tabular format. The tool arch-audit can be used to check for vulnerabilities affecting the running system. A graphical system tray, arch-audit-gtk, can also be used. See also Arch Security Team.

You should also consider subscribing to the release notifications for software you use, especially if you install software through means other than the main repositories or AUR. Some software have mailing lists you can subscribe to for security notifications. Source code hosting sites often offer RSS feeds for new releases.

Packages can be rebuilt and stripped of undesired functions and features as a means to reduce attack surface. For example, bzip2 can be rebuilt without bzip2recover in an attempt to circumvent CVE-2016-3189. Custom hardening flags can also be applied either manually or via a wrapper.

This article or section is a candidate for merging with Arch package guidelines/Security.

The factual accuracy of this article or section is disputed.

**Examples:**

Example 1 (unknown):
```unknown
k1araj0hns0n
```

Example 2 (unknown):
```unknown
photocopyhauntbranchexpose
```

Example 3 (unknown):
```unknown
Ph0toc0pyh4uN7br@nch3xp*se
```

Example 4 (unknown):
```unknown
t&6!RrlW@dtR,57
```

---
