@echo off
:: Agent Superpowers: Windows Polyglot Hook Runner for Claude Code
:: Author: Gabriele Dattile (https://github.com/GabrieleDattile)

setlocal EnableDelayedExpansion

:: Check for Git Bash
if exist "C:\Program Files\Git\bin\bash.exe" (
    "C:\Program Files\Git\bin\bash.exe" "%~dp0session-start"
    exit /b %ERRORLEVEL%
)

:: Fallback direct Windows Console output
echo.
echo =========================================================================
echo   ⚡ AGENT SUPERPOWERS v1.2.0 ACTIVE  [9 autonomous skills loaded]
echo =========================================================================
echo   >> Directives: Worktree isolation - TDD Red-Green - Red-Team Audit
echo   Type "Tell me about your superpowers" to inspect active capabilities.
echo.

exit /b 0
