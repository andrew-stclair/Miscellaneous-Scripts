# git gpg signing using an OpenPGP card within WSL

This guide will step you through setting up gpg4win and using it from git within WSL.

This guide assumes you already have a private key on an OpenPGP card and have imported your public key to github (or other git repository).

Also, i may have missed something from when i set this up as i am writing this guide months after actually getting it to work.

## Using gpg4win inside WSL

1. Download and install GPG4Win as normal from [gpg4win.org](https://www.gpg4win.org/get-gpg4win.html).
2. Download and install WSL2 by following [these instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
3. Using your favorite flavor of linux running inside WSL, setup a symlink somewhere in your $path to override the installed gpg tool with the version installed with gpg4win. I chose to install my symlink in `~/bin/gpg` using the command `mkdir -p ~/bin; ln -s '/mnt/c/Program Files (x86)/GnuPG/bin/gpg.exe' '~/bin/gpg'`.

## Setting up git commit signing

These instrictions assume you are configuring your global config. If not, just drop `--global` from all relevant git commands.

1. Import your public key into Kleopatra and insert your OpenPGP card.

2. Get your gpg key fingerprint using `gpg --list-secret-keys --keyid-format LONG`.
The string you want will be a 40 character long hexadecimal string listed just below a line starting with `sec>`.
your email you setup with the key should be listed just below the card serial number in the same block.

3. Copy your key's fingerprint to git using `git config --global user.signingkey <All 40 characters or last 16 or 8 characters>`.

4. If you put your gpg symlink somewhere outside of $path or before the existing gpg executable, use `git config --global gpg.program /path/to/gpg` to set the path to the symlink.
This is only neccesary if running gpg still executes the existing gpg executable, and not the symlink.

5. Set git's user.name and user.email values to match your account on github (or other git repository).
```
git config --global user.name "John Smith"
git config --global user.email "j.smith@example.com"
```

6. You are all done, you should now be able to sign any commits inside of WSL. I suggest setting up a dummy repository and testing commit signing to check it everything worked.

## What does this achieve?

If, like me, you store your private gpg key on an OpenPGP Card, this will allow you to sign git commits inside of WSL using your private gpg key stored on the OpenPGP Card.

This means you do not need to keep a digital copy of your private key within WSL, which defeats the main purpose of using a physical OpenPGP Card.