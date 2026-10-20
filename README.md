# Codex Dev Skills

Six task-activated custom skills for Codex on Windows/VS Code: frontend UI/UX, Android/APK, backend APIs, databases, quality/security, and context/token efficiency.

## Install globally for all projects (Windows PowerShell)

Clone this private repository using your authenticated GitHub credentials:

```powershell
git clone https://github.com/thuf86/codex-dev-skills.git
cd codex-dev-skills
.\validate.ps1
.\install.ps1 -Scope Global
```

The **global user installation** places each skill at `$HOME\.agents\skills\<skill-name>\SKILL.md` (typically `C:\Users\<username>\.agents\skills`). It applies across projects opened in VS Code by the same Windows user. It is not machine-wide for other Windows accounts. Restart Codex after installing.

### Update an existing global installation

```powershell
git pull --ff-only
.\validate.ps1
.\install.ps1 -Scope Global -Force
```

The `-Force` option first moves each existing skill folder to a timestamped backup before replacing it. Without `-Force`, existing folders are skipped. Do not install duplicate copies under both `~/.codex/skills` and `~/.agents/skills` unless you know how your Codex version handles duplicates.

### Optional commands

```powershell
# Install only one skill globally
.\install.ps1 -Scope Global -Only context-token-efficiency
# Install only in a particular project
.\install.ps1 -Scope Project -ProjectPath 'C:\work\my-project'
# Inspect global skill files
Get-ChildItem "$HOME\.agents\skills" -Directory | Select-Object Name
```

`-Scope User` is retained as an alias for `-Scope Global` for backward compatibility.

## Included skills

| Skill | Purpose |
| --- | --- |
| `frontend-uiux` | Web UI, responsiveness, accessibility and design systems |
| `android-apk` | Android Kotlin/Compose/XML, Gradle and APK packaging |
| `backend-apis` | API contracts, authentication, integrations and error handling |
| `database-engineering` | SQL, migrations, transactions and query tuning |
| `quality-security` | Testing, secure reviews and CI quality gates |
| `context-token-efficiency` | Scoped reads, targeted patches and concise checkpoints |

## Coverage versus previously suggested skills

This repository includes **six original custom skills**, not all third-party or official skills previously discussed. `playwright`, `playwright-interactive`, `openai-docs`, `screenshot`, and `create-plan` are not bundled here. `skill-creator` and `skill-installer` are built-in system skills in supported Codex versions; do not copy or overwrite them. Install optional official/community skills separately after reviewing their sources and compatibility.

## Activation and validation

Each skill has YAML `name` and `description` metadata. Codex discovers skills and loads detailed instructions when relevant. Mention a skill explicitly to request it. The `AGENTS.example.md` file is a template, not automatically installed as global instructions.

`validate.ps1` checks the six skill files and expected sections; GitHub Actions runs the structural check on pushes and pull requests. Structural checks are not a substitute for an actual Codex discovery test or Android/web build.

## Safety

Do not commit API keys, passwords, tokens or signing credentials. Preserve existing project functionality unless a change is explicitly authorized and tested.
