# Codex Dev Skills

Six task-activated skills for Codex in VS Code on Windows: frontend UI/UX, Android/APK, backend APIs, databases, quality/security and context/token efficiency.

## Install (PowerShell)

Clone this private repository using your authenticated GitHub account, then run:

```powershell
.\validate.ps1
.\install.ps1 -Scope User
# or project-local:
.\install.ps1 -Scope Project -ProjectPath 'C:\path\to\repo'
# install one skill:
.\install.ps1 -Scope User -Only context-token-efficiency
```

User target: `$HOME\.agents\skills`. Project target: `<project>\.agents\skills`. Existing skill folders are preserved unless `-Force` is specified. Restart the Codex session after installing.

## Activation

Codex discovers each `SKILL.md` by its YAML name and description. Request the relevant task or mention the skill by name. Do not load every skill on every turn. Use `AGENTS.example.md` as a template for repository-level instructions, reviewing any existing `AGENTS.md` first.

## Validation

`validate.ps1` checks all six skill files and their required metadata/sections. GitHub Actions runs the structural check on pushes and pull requests. This does not establish functional Codex compatibility, Android builds or guaranteed token savings.

## Safety

Never commit secrets, credentials or private keys. Keep production behavior unchanged unless explicitly requested and tested.
