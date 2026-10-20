[CmdletBinding()]
param(
    [ValidateSet('Global','User','Project')]
    [string]$Scope = 'Global',
    [ValidateSet('Codex','Claude','Both')]
    [string]$Target = 'Codex',
    [string]$ProjectPath = (Get-Location).Path,
    [string]$Only = '',
    [switch]$Force
)
$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot 'skills'
if (-not (Test-Path -LiteralPath $source -PathType Container)) { throw 'Diretorio skills nao encontrado.' }
$folders = @(Get-ChildItem -LiteralPath $source -Directory)
if ($Only) {
    $folders = @($folders | Where-Object { $_.Name -eq $Only })
    if ($folders.Count -eq 0) { throw "Skill desconhecida: $Only" }
}
$targets = if ($Target -eq 'Both') { @('Codex','Claude') } else { @($Target) }
foreach ($agent in $targets) {
    $root = if ($Scope -eq 'Project') { $ProjectPath } else { $HOME }
    $directory = if ($agent -eq 'Codex') { '.agents\skills' } else { '.claude\skills' }
    $destination = Join-Path $root $directory
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    foreach ($folder in $folders) {
        $skillFile = Join-Path $folder.FullName 'SKILL.md'
        if (-not (Test-Path -LiteralPath $skillFile -PathType Leaf)) { throw "SKILL.md ausente: $($folder.Name)" }
        $targetPath = Join-Path $destination $folder.Name
        if (Test-Path -LiteralPath $targetPath) {
            if (-not $Force) {
                Write-Warning "Ja existe; ignorado: $targetPath (use -Force para atualizar)"
                continue
            }
            $backup = "$targetPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
            if (Test-Path -LiteralPath $backup) { throw "Backup ja existe: $backup" }
            Move-Item -LiteralPath $targetPath -Destination $backup
            Write-Host "Backup criado: $backup"
        }
        Copy-Item -LiteralPath $folder.FullName -Destination $targetPath -Recurse -ErrorAction Stop
        if (-not (Test-Path -LiteralPath (Join-Path $targetPath 'SKILL.md') -PathType Leaf)) {
            throw "Falha na verificacao da instalacao: $targetPath"
        }
        Write-Host "Instalado em $agent : $targetPath"
    }
}
Write-Host 'Concluido. Reinicie a sessao do Codex ou Claude Code para conferir as skills.'
