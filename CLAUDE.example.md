# Instruções do projeto para Claude Code

Use as skills instaladas em `~/.claude/skills` ou `.claude/skills` apenas quando a tarefa corresponder à descrição da skill. Prefira uma skill de domínio por tarefa e, se necessário, `context-token-efficiency`.

As skills cobrem frontend, Android, backend, bancos de dados, qualidade/segurança, Playwright, documentação OpenAI, capturas de tela e planejamento.

Preserve contratos de API, sessão de autenticação e funcionamento existente. Leia apenas arquivos relevantes, evite logs excessivos e não invente testes concluídos. Use dados sintéticos, não exponha segredos e peça autorização antes de mudanças destrutivas.

Este arquivo é um modelo: revise antes de copiar para `CLAUDE.md` em um projeto real.
