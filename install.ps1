param([ValidateSet('User','Project')][string]$Scope='User',[string]$ProjectPath=(Get-Location).Path,[string]$Only='',[switch]$Force)
$ErrorActionPreference='Stop'
$source=Join-Path $PSScriptRoot 'skills'
if(!(Test-Path $source)){throw 'Missing skills directory'}
$dest=if($Scope -eq 'User'){Join-Path $HOME '.agents\skills'}else{Join-Path $ProjectPath '.agents\skills'}
New-Item -ItemType Directory -Force -Path $dest | Out-Null
$folders=@(Get-ChildItem -LiteralPath $source -Directory)
if($Only){$folders=@($folders | Where-Object Name -eq $Only);if(!$folders.Count){throw "Unknown skill: $Only"}}
foreach($folder in $folders){$target=Join-Path $dest $folder.Name;if(Test-Path $target){if(!$Force){Write-Warning "Skipped existing $target";continue};Remove-Item -LiteralPath $target -Recurse -Force};Copy-Item -LiteralPath $folder.FullName -Destination $target -Recurse;Write-Host "Installed $target"}
Write-Host 'Restart Codex to refresh skill discovery.'
