# Agent Superpowers: Universal Installer for Windows PowerShell
# Author: Gabriele Dattile (https://github.com/GabrieleDattile)
# Repository: https://github.com/GabrieleDattile/agent-superpowers

param(
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"

Write-Host "Agent Superpowers: Installing suite across AI platforms on Windows..." -ForegroundColor Cyan

# 1. Resolve source directory (Local clone OR Remote download)
$LocalSource = $null
if ($PSScriptRoot -and (Test-Path (Join-Path $PSScriptRoot "skills"))) {
    $LocalSource = $PSScriptRoot
} elseif (Test-Path ".\skills") {
    $LocalSource = (Get-Location).Path
}

$TempDir = Join-Path $env:TEMP "agent-superpowers-install"
if (-not $LocalSource) {
    Write-Host "Downloading latest Agent Superpowers package from GitHub..." -ForegroundColor Yellow
    if (Test-Path $TempDir) {
        Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
    }
    New-Item -ItemType Directory -Force -Path $TempDir | Out-Null
    
    $ZipPath = Join-Path $TempDir "package.zip"
    $DownloadUrl = "https://github.com/GabrieleDattile/agent-superpowers/archive/refs/heads/main.zip"
    
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $DownloadUrl -OutFile $ZipPath -UseBasicParsing
    
    Expand-Archive -Path $ZipPath -DestinationPath $TempDir -Force
    $ExtractedFolder = Join-Path $TempDir "agent-superpowers-main"
    if (Test-Path $ExtractedFolder) {
        $LocalSource = $ExtractedFolder
    } else {
        $LocalSource = (Get-ChildItem -Path $TempDir -Directory | Select-Object -First 1).FullName
    }
}

Write-Host "Source package verified at: $LocalSource" -ForegroundColor Green

# 2. Deploy Global Suite Installation to ~/.agent-superpowers
$GlobalDest = Join-Path $env:USERPROFILE ".agent-superpowers"
New-Item -ItemType Directory -Force -Path $GlobalDest | Out-Null
Copy-Item -Recurse -Force (Join-Path $LocalSource "cli") $GlobalDest
Copy-Item -Recurse -Force (Join-Path $LocalSource "skills") $GlobalDest
Copy-Item -Recurse -Force (Join-Path $LocalSource "mcp") $GlobalDest
Copy-Item -Recurse -Force (Join-Path $LocalSource "bin") $GlobalDest

# Create cmd launcher in ~/.agent-superpowers/bin
$CmdLauncher = Join-Path $GlobalDest "bin\superpowers.cmd"
"@echo off`r`npython `"$GlobalDest\cli\superpowers.py`" %*" | Set-Content -Path $CmdLauncher -Encoding Ascii

# Helper to deploy skills flattened by skill name
function Deploy-Skills([string]$DestinationDir) {
    New-Item -ItemType Directory -Force -Path $DestinationDir | Out-Null
    $skillFiles = Get-ChildItem -Path (Join-Path $LocalSource "skills") -Recurse -Filter "SKILL.md"
    foreach ($sf in $skillFiles) {
        $skillFolder = $sf.Directory
        $targetPath = Join-Path $DestinationDir $skillFolder.Name
        Copy-Item -Recurse -Force $skillFolder.FullName $targetPath
    }
}

# 3. Google Antigravity & Gemini CLI
if ($Target -eq "antigravity" -or $Target -eq "all") {
    $AgDest = Join-Path $env:USERPROFILE ".gemini\antigravity\skills"
    $AgConfigDest = Join-Path $env:USERPROFILE ".gemini\config\skills"
    Deploy-Skills -DestinationDir $AgDest
    Deploy-Skills -DestinationDir $AgConfigDest
    Write-Host "Installed into Antigravity: $AgDest and $AgConfigDest" -ForegroundColor Green
}

# 4. Claude Code
if ($Target -eq "claude" -or $Target -eq "all") {
    $ClaudeDest = Join-Path $env:USERPROFILE ".claude\skills"
    Deploy-Skills -DestinationDir $ClaudeDest
    Write-Host "Installed into Claude Code: $ClaudeDest" -ForegroundColor Green
}

# 5. Cursor (Workspace rules)
if ($Target -eq "cursor" -or $Target -eq "all") {
    $CursorDest = Join-Path (Get-Location) ".cursor\rules"
    New-Item -ItemType Directory -Force -Path $CursorDest | Out-Null
    $RuleSrc = Join-Path $LocalSource ".cursor\rules\agent-superpowers.mdc"
    $RuleDst = Join-Path $CursorDest "agent-superpowers.mdc"
    if (Test-Path $RuleSrc) {
        $srcPath = (Resolve-Path $RuleSrc).Path
        $dstPath = if (Test-Path $RuleDst) { (Resolve-Path $RuleDst).Path } else { $null }
        if ($srcPath -ne $dstPath) {
            Copy-Item -Force $RuleSrc $RuleDst
        }
        Write-Host "Installed into Cursor rules: $RuleDst" -ForegroundColor Green
    }
}

# 6. Windsurf
if ($Target -eq "windsurf" -or $Target -eq "all") {
    $WindsurfSrc = Join-Path $LocalSource ".windsurfrules"
    $WindsurfDst = Join-Path (Get-Location) ".windsurfrules"
    if (Test-Path $WindsurfSrc) {
        $srcPath = (Resolve-Path $WindsurfSrc).Path
        $dstPath = if (Test-Path $WindsurfDst) { (Resolve-Path $WindsurfDst).Path } else { $null }
        if ($srcPath -ne $dstPath) {
            Copy-Item -Force $WindsurfSrc $WindsurfDst
        }
        Write-Host "Installed into Windsurf: .windsurfrules" -ForegroundColor Green
    }
}

# 7. OpenAI Codex
if ($Target -eq "codex" -or $Target -eq "all") {
    $CodexDest = Join-Path (Get-Location) ".codex"
    New-Item -ItemType Directory -Force -Path $CodexDest | Out-Null
    $CodexSrc = Join-Path $LocalSource ".codex\INSTALL.md"
    $CodexDst = Join-Path $CodexDest "INSTALL.md"
    if (Test-Path $CodexSrc) {
        $srcPath = (Resolve-Path $CodexSrc).Path
        $dstPath = if (Test-Path $CodexDst) { (Resolve-Path $CodexDst).Path } else { $null }
        if ($srcPath -ne $dstPath) {
            Copy-Item -Force $CodexSrc $CodexDst
        }
        Write-Host "Configured for Codex: $CodexDest" -ForegroundColor Green
    }
}

# Cleanup temporary download
if (Test-Path $TempDir) {
    Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "SUCCESS: 11 Agent Superpowers and Python scripts installed!" -ForegroundColor Green
Write-Host "  Location: $GlobalDest" -ForegroundColor Gray
Write-Host "  To launch CLI: python `"$GlobalDest\cli\superpowers.py`" list" -ForegroundColor Yellow
Write-Host "  To launch Dashboard: python `"$GlobalDest\cli\superpowers.py`" dashboard" -ForegroundColor Yellow
Write-Host "=================================================================" -ForegroundColor Cyan
