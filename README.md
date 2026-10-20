<div align="center">

# 🧩 CODEX DEV SKILLS

**Skills especializadas para desenvolvimento, testes, segurança e otimização de contexto**

![Versão](https://img.shields.io/badge/VERS%C3%83O-1.2-65c600?style=for-the-badge)
![Plataforma](https://img.shields.io/badge/PLATAFORMA-WINDOWS-0078d4?style=for-the-badge)
![Codex](https://img.shields.io/badge/OPENAI_CODEX-COMPAT%C3%8DVEL-111827?style=for-the-badge)
![Claude](https://img.shields.io/badge/CLAUDE_CODE-COMPAT%C3%8DVEL-111827?style=for-the-badge)
![Licença](https://img.shields.io/badge/LICEN%C3%87A-N%C3%83O_DEFINIDA-f0b400?style=for-the-badge)

</div>

---

## ⭐ Apoie o projeto deixe uma ⭐

Se este repositório for útil ao seu ambiente de desenvolvimento, considere deixar uma estrela. Compartilhe melhorias por meio de issues e pull requests.

---

## 🤖 Codex Dev Skills

O **Codex Dev Skills** reúne **11 skills personalizadas** para OpenAI Codex e Claude Code, organizadas em um único repositório. O objetivo é padronizar tarefas de frontend, Android, backend, bancos de dados, testes, segurança e planejamento, com **ativação sob demanda** e boas práticas de economia de contexto.

**Autor:** [thuf86](https://github.com/thuf86)

---

## 📌 Visão geral

Este projeto oferece:

- Instalação global para o usuário Windows, válida em diferentes projetos.
- Compatibilidade com **Codex** e **Claude Code**, com diretórios separados.
- Instalação individual ou conjunta das 11 skills.
- Atualizações seguras com backup das skills anteriores.
- Metadados `SKILL.md` e instruções de ativação por contexto.
- Validação estrutural via PowerShell e GitHub Actions.
- Documentação e instruções em português brasileiro.

> As skills são instruções para agentes, não substituem dependências como Playwright, Android SDK ou navegadores. As cinco skills adicionais são implementações personalizadas, não cópias oficiais. A economia de tokens não é garantida.

---

## ✨ Principais recursos

| Skill | Especialidade |
|---|---|
| `frontend-uiux` | Interfaces web, responsividade e acessibilidade |
| `android-apk` | Kotlin, Compose, Gradle e APK |
| `backend-apis` | APIs, autenticação e integrações |
| `database-engineering` | SQL, migrações e desempenho |
| `quality-security` | Testes, revisão de segurança e CI |
| `context-token-efficiency` | Leitura seletiva, patches mínimos e checkpoints |
| `playwright-browser` | Testes automatizados de navegador |
| `playwright-interactive-browser` | Investigação interativa quando suportada |
| `openai-api-docs` | Consulta à documentação oficial de APIs OpenAI |
| `screenshot-review` | Análise de capturas e regressão visual |
| `implementation-plan` | Planejamento em fases e critérios de aceitação |

`skill-creator` e `skill-installer` são skills de sistema em instalações compatíveis do Codex; veja [a documentação](docs/system-skills.md). Não são sobrescritas.

---

## 🖥️ Instalação no Windows / PowerShell

Clone o repositório privado com uma conta GitHub autorizada:

```powershell
git clone https://github.com/thuf86/codex-dev-skills.git
cd codex-dev-skills
.\validate.ps1
```

### Instalar globalmente no Codex

```powershell
.\install.ps1 -Target Codex -Scope Global
```

Destino: `$HOME\.agents\skills`.

### Instalar globalmente no Claude Code

```powershell
.\install.ps1 -Target Claude -Scope Global
```

Destino: `$HOME\.claude\skills`. O Claude Code reconhece skills pessoais nesse diretório. [Documentação oficial](https://code.claude.com/docs/en/skills).

### Instalar globalmente nos dois

```powershell
.\install.ps1 -Target Both -Scope Global
```

A instalação global é **por usuário Windows**, não para todas as contas da máquina. Reinicie a sessão do agente após instalar.

### Atualizar skills instaladas

```powershell
git pull --ff-only
.\validate.ps1
.\install.ps1 -Target Both -Scope Global -Force
```

O parâmetro `-Force` cria um backup datado antes de substituir cada skill existente. Sem ele, pastas existentes são preservadas.

### Instalação seletiva ou por projeto

```powershell
.\install.ps1 -Target Claude -Scope Global -Only frontend-uiux
.\install.ps1 -Target Codex -Scope Project -ProjectPath 'C:\Projetos\MeuApp'
```

Para uso no Claude Code, verifique as skills com `/skills` ou invoque pelo nome quando disponível.

---

## 🧠 Ativação sob demanda e economia de contexto

O agente deve selecionar apenas a skill relevante. Para projetos grandes, combine uma skill técnica com `context-token-efficiency` quando necessário. Evite carregar todos os arquivos do repositório, imprimir logs extensos ou executar testes irrelevantes.

Use [AGENTS.example.md](AGENTS.example.md) como modelo de instruções do Codex. Para Claude Code, use [CLAUDE.example.md](CLAUDE.example.md) como modelo de `CLAUDE.md`, sem sobrescrever configurações existentes.

---

## 🧪 Validação e limitações

```powershell
.\validate.ps1
```

O validador verifica a presença e a estrutura das 11 skills. O workflow do GitHub Actions executa essa verificação no Windows. A publicação do workflow **não comprova** que a execução remota passou ou que os agentes reconheceram as skills.

---

## 🔐 Segurança e licença

Nunca inclua chaves de API, senhas, tokens ou credenciais de assinatura no repositório. Preserve contratos e funcionalidades dos projetos. A licença de redistribuição ainda não foi definida: não presuma uma licença open source apenas porque o repositório está no GitHub.

---

## 📂 Estrutura

```text
codex-dev-skills/
├── skills/                  # 11 skills com SKILL.md
├── docs/                    # Orientações de compatibilidade
├── .github/workflows/       # Validação automatizada
├── install.ps1              # Instalador Codex / Claude / Ambos
├── validate.ps1             # Validador estrutural
├── AGENTS.example.md        # Instruções para Codex
├── CLAUDE.example.md        # Instruções para Claude Code
└── README.md
```
