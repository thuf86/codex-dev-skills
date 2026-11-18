# Instagram Video Pro

Skill profissional para Claude Code e Codex CLI: roteiro, direção, storyboard, identidade visual, slides gráficos editáveis, renderização local FFmpeg e validação FFprobe.

## Instalação
Use o instalador do repositório pai no PowerShell:
```powershell
.\install.ps1 -Target Both -Scope Global -Only instagram-video-pro
```
Reinicie os agentes. O instalador existente copia o diretório completo para ~/.agents/skills e ~/.claude/skills.

## Gerar vídeo
Requer Python, FFmpeg/FFprobe e Pillow:
```bash
python -m pip install -r skills/instagram-video-pro/requirements.txt
python skills/instagram-video-pro/scripts/render.py --project skills/instagram-video-pro/templates/project.example.json --output exemplo.mp4
python skills/instagram-video-pro/scripts/validate_video.py exemplo.mp4 --json
python -m unittest discover -s skills/instagram-video-pro/tests -v
```

## Prompt de exemplo
Use a skill instagram-video-pro para produzir um Reel educativo de 30 segundos sobre phishing em pt-BR. Aplique visual NULL TRACE, gere storyboard, roteiro, arte, legenda e um MP4 editável. Valide a exportação. Não publique.

## Limites reais
O motor incluído cria slides gráficos, não cenas cinematográficas de IA. Voz natural, vídeo generativo, Remotion e publicação são integrações opcionais dependentes de ferramentas externas autorizadas. O exemplo gera um vídeo sem áudio. Ao usar áudio, forneça arquivos locais legalmente licenciados. A verificação automática não substitui revisão visual, auditiva, jurídica e factual.

Para o feed NULL TRACE, carrosséis estáticos continuam com exatamente sete imagens 1080×1350, separados do formato Reel.
