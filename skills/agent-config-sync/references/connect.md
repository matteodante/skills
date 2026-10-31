# Reaching the other machine

Read this when the other machine is not the one the agent runs on. A remote UI does not count: a desktop client attached to another machine's server, or a phone running remote control, still runs every tool on the server. Check where tools actually run before planning.

Use one path below. Prefer a private network such as Tailscale or a LAN, and never open SSH to the internet for this.

## Check what already works

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 USER@HOST 'whoami'
```

A timeout means nothing is listening, or a firewall drops the connection. `Permission denied (publickey…)` means the server is running and the key is not authorized yet.

## macOS as the SSH server

Remote Login may already be on: `nc -z 127.0.0.1 22` succeeds. If it is off, the user enables it in System Settings → General → Sharing → Remote Login. `systemsetup -setremotelogin on` needs sudo and Full Disk Access, so ask the user to do it in the UI. Then add the client's public key to `~/.ssh/authorized_keys`, or log in with the account password.

## Windows as the SSH server

OpenSSH Server is a Windows optional feature. The user runs these commands in an **elevated** PowerShell. From a normal one, `Start-Process powershell -Verb RunAs` opens an elevated window.

```powershell
# Only if `Get-Service sshd` reports that the service does not exist:
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service sshd -StartupType Automatic
$f = "C:\ProgramData\ssh\administrators_authorized_keys"
Add-Content $f "ssh-ed25519 AAAA... client-key-comment"
icacls $f /inheritance:r /grant "*S-1-5-32-544:F" /grant "*S-1-5-18:F"
Get-Service sshd   # should show Running
```

Pitfalls seen in practice:

- **Not elevated.** You get `Access denied` or "elevated privileges required" on every line. The service may already be installed, so check `Get-Service sshd` before reinstalling it.
- **Mangled capability name.** Chat renderers can turn `~~~~` into strikethrough. A pasted `OpenSSH.Server0.0.1.0` means the tildes were lost. If you can, avoid sending that line at all.
- **Localized group names.** "Administrators" is translated on some Windows languages, so grant by SID as shown above.
- **Which key file.** Accounts in the Administrators group read `administrators_authorized_keys`. Standard accounts read `%USERPROFILE%\.ssh\authorized_keys`.
- **If the feature install hangs**, use the Win64 MSI from the PowerShell/Win32-OpenSSH releases.

## Linux as the SSH server

Install and start the distribution's `openssh-server` package, then add the key to `~/.ssh/authorized_keys`.

## Running commands on Windows over SSH

The default remote shell is `cmd.exe`, and nested quoting through it breaks quickly. Write a `.ps1` script locally, copy it, run it, then delete it:

```bash
scp -q script.ps1 USER@HOST:script.ps1
ssh USER@HOST 'powershell -NoProfile -ExecutionPolicy Bypass -File script.ps1 & del script.ps1'
```

- On Windows, `bash` in PATH can resolve to `C:\Windows\System32\bash.exe`, which is WSL, not Git Bash. Use the full Git Bash path when testing scripts, for example `"C:\Program Files\Git\bin\bash.exe"`. Claude Code itself runs hook and status line commands through Git Bash.
- Archives made on macOS carry `._*` AppleDouble files. Create them with `COPYFILE_DISABLE=1 tar …`, or delete `._*` after extracting.
- Interactive logins started over SSH (`railway login`, OAuth flows) often fail or open a browser nobody can see. Leave logins to the user on that machine.
