# SSH Keys

## TL;DR

- SSH keys enable secure authentication to remote servers and Git hosting services.
- A key pair consists of a **private key** (secret) and a **public key** (shared with the service).
- **Ed25519** is a good default for generating new keys.
- Protect private keys with a passphrase and never commit them to Git repositories.

## How SSH Keys Work

SSH (Secure Shell) establishes an encrypted connection between a client and a remote system. With public-key authentication, the client proves possession of a private key, while the server verifies it using the corresponding public key.

| File | Purpose |
|---|---|
| `id_ed25519` | Private key — keep secret |
| `id_ed25519.pub` | Public key — register with the remote service |
| `known_hosts` | Records server host keys |

## Generate an SSH Key

Generate a new Ed25519 key pair:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Follow the prompts and set a strong passphrase. By default, the keys are saved in `~/.ssh/`.

Check existing keys before generating a new pair to avoid overwriting credentials you still need.

## Use SSH with GitHub

Display your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Add it under **GitHub → Settings → SSH and GPG keys → New SSH key**.

Test the connection:

```bash
ssh -T git@github.com
```

Clone a repository using SSH:

```bash
git clone git@github.com:OWNER/REPOSITORY.git
```

For an existing repository, switch from HTTPS to SSH:

```bash
git remote set-url origin git@github.com:OWNER/REPOSITORY.git
```

## SSH Agent

The SSH agent manages loaded private keys so you do not need to enter the passphrase for every authentication attempt.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l  # List loaded keys
```

Agent setup varies by operating system; macOS can also integrate SSH keys with Keychain.

## Connect to a Remote Server

If `ssh-copy-id` is available, install your public key on a server:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@server.example.com
```

Connect using:

```bash
ssh username@server.example.com
```

For multiple servers or keys, configure `~/.ssh/config`:

```sshconfig
Host research-server
    HostName server.example.com
    User researcher
    IdentityFile ~/.ssh/id_ed25519_work
    IdentitiesOnly yes
```

Then connect with `ssh research-server`.

## Security Best Practices

- **Never share or commit private keys.**
- Protect private keys with a strong passphrase.
- Use separate keys for different environments when appropriate.
- Verify server host-key fingerprints before trusting a new connection.
- Store CI/CD private keys in a secrets manager, not in source code or container images.
- Revoke compromised or unused keys on every service where they are authorized.

Restrict file permissions on Unix-like systems:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

If a private key is compromised, revoke its public key, generate a replacement, and update all dependent systems.

## Troubleshooting

| Error | Possible solution |
|---|---|
| `Permission denied (publickey)` | Check that the public key is registered and the correct account is used. |
| `Could not open a connection to your authentication agent` | Start or reconnect to the SSH agent. |
| `Too many authentication failures` | Specify the intended key and use `IdentitiesOnly yes`. |
| Host identification warning | Verify the server's identity before modifying `known_hosts`. |

For detailed diagnostics:

```bash
ssh -vT git@github.com
```

## Related Topics

- Git and version control
- Secrets management
- Authentication
- CI/CD and deployment
