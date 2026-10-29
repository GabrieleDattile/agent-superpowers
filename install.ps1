# Agent Superpowers: Universal Installer for Windows PowerShell
# Author: Gabriele Dattile (https://github.com/GabrieleDattile)

param(
    [string]$Target = "all"
)

Write-Host "⚡ Agent Superpowers: Installing across platforms on Windows..." -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# 1. Claude Code
if ($Target -eq "claude" -or $Target -eq "all") {
    $ClaudeDest = Join-Path $env:USERPROFILE ".claude\skills"
    New-Item -ItemType Directory -Force -Path $ClaudeDest | Out-Null
    Copy-Item -Recurse -Force "$ScriptDir\skills\*" $ClaudeDest
    Write-Host "✔ Installed into Claude Code: $ClaudeDest" -ForegroundColor Green
}

# 2. Cursor
if ($Target -eq "cursor" -or $Target -eq "all") {
    $CursorDest = Join-Path (Get-Location) ".cursor\rules"
    New-Item -ItemType Directory -Force -Path $CursorDest | Out-Null
    if (Test-Path "$ScriptDir\.cursor\rules\agent-superpowers.mdc") {
        Copy-Item -Force "$ScriptDir\.cursor\rules\agent-superpowers.mdc" $CursorDest
    }
    Write-Host "✔ Installed into Cursor: $CursorDest" -ForegroundColor Green
}

# 3. Google Antigravity
if ($Target -eq "antigravity" -or $Target -eq "all") {
    $AgDest = Join-Path $env:USERPROFILE ".gemini\antigravity\skills"
    New-Item -ItemType Directory -Force -Path $AgDest | Out-Null
    Copy-Item -Recurse -Force "$ScriptDir\skills\*" $AgDest
    Write-Host "✔ Installed into Antigravity: $AgDest" -ForegroundColor Green
}

# 4. OpenAI Codex
if ($Target -eq "codex" -or $Target -eq "all") {
    $CodexDest = Join-Path (Get-Location) ".codex"
    New-Item -ItemType Directory -Force -Path $CodexDest | Out-Null
    if (Test-Path "$ScriptDir\.codex\INSTALL.md") {
        Copy-Item -Force "$ScriptDir\.codex\INSTALL.md" $CodexDest
    }
    Write-Host "✔ Configured for Codex: $CodexDest" -ForegroundColor Green
}

Write-Host "`n✔ Agent Superpowers successfully deployed across selected platforms!" -ForegroundColor Green
Write-Host "Run `python cli/superpowers.py list` to verify active capabilities." -ForegroundColor Yellow
