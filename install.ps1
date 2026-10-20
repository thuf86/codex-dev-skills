[CmdletBinding()]
param(
    [ValidateSet('Global','User','Project')]
    [string]$Scope = 'Global',
    [string]$ProjectPath = (Get-Location).Path,
    [string]$Only = '',
    [switch]$Force
)
$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot 'skills'
if (-not (Test-Path -LiteralPath $source -PathType Container)) { throw 'Missing skills directory.' }
$destination = if ($Scope -eq 'Project') {
    Join-Path $ProjectPath '.agents\skills'
} else {
    Join-Path $HOME '.agents\skills'
}
$folders = @(Get-ChildItem -LiteralPath $source -Directory)
if ($Only) {
    $folders = @($folders | Where-Object { $_.Name -eq $Only })
    if ($folders.Count -eq 0) { throw "Unknown skill: $Only" }
}
New-Item -ItemType Directory -Path $destination -Force | Out-Null
foreach ($folder in $folders) {
    $skillFile = Join-Path $folder.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillFile -PathType Leaf)) { throw "Missing SKILL.md: $($folder.Name)" }
    $target = Join-Path $destination $folder.Name
    if (Test-Path -LiteralPath $target) {
        if (-not $Force) {
            Write-Warning "Already installed, skipped: $target (use -Force to update)"
            continue
        }
        $backup = "$target.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
        if (Test-Path -LiteralPath $backup) { throw "Backup path already exists: $backup" }
        Move-Item -LiteralPath $target -Destination $backup
        Write-Host "Backed up existing skill to $backup"
    }
    Copy-Item -LiteralPath $folder.FullName -Destination $target -Recurse -ErrorAction Stop
    if (-not (Test-Path -LiteralPath (Join-Path $target 'SKILL.md'))) { throw "Install verification failed: $target" }
    Write-Host "Installed $($folder.Name) -> $target"
}
Write-Host "Installation scope: $Scope"
Write-Host 'Global scope is per Windows user and works across VS Code projects.'
Write-Host 'Restart Codex to discover installed skills.'
