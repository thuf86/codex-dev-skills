# Skills de sistema e compatibilidade

As skills `skill-creator` e `skill-installer` são fornecidas pelo próprio Codex em ambientes compatíveis. Este repositório não as copia nem sobrescreve. Solicite sua execução no Codex e verifique a disponibilidade na instalação utilizada.

As cinco skills adicionais (`playwright-browser`, `playwright-interactive-browser`, `openai-api-docs`, `screenshot-review` e `implementation-plan`) são **implementações personalizadas**, não cópias das distribuições oficiais.

## Claude Code

O Claude Code aceita skills com arquivo `SKILL.md` e metadados YAML `name` e `description`. A instalação pessoal usa `~/.claude/skills/<nome>/SKILL.md`; a instalação por projeto usa `.claude/skills/<nome>/SKILL.md`.

Execute `.\install.ps1 -Target Claude -Scope Global` para instalar as 11 skills para o usuário atual. Para instalar nos dois agentes: `.\install.ps1 -Target Both -Scope Global`.

A compatibilidade estrutural não significa que Playwright ou ferramentas externas estejam instalados. Recursos interativos dependem do ambiente do agente.

Documentação oficial: https://code.claude.com/docs/en/skills
