#!/usr/bin/env bash
# Agent Superpowers: Universal Installer for macOS and Linux
# Author: Gabriele Dattile (https://github.com/GabrieleDattile)

set -e

BOLD="\033[1m"
GREEN="\033[32m"
CYAN="\033[36m"
YELLOW="\033[33m"
RESET="\033[0m"

echo -e "${BOLD}${CYAN}⚡ Agent Superpowers: Installing across platforms...${RESET}"

TARGET="${1:-all}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Claude Code
if [ "$TARGET" = "claude" ] || [ "$TARGET" = "all" ]; then
    CLAUDE_DEST="$HOME/.claude/skills"
    mkdir -p "$CLAUDE_DEST"
    cp -R "$SCRIPT_DIR/skills/"* "$CLAUDE_DEST/" 2>/dev/null || true
    echo -e "${GREEN}✔ Installed into Claude Code:${RESET} $CLAUDE_DEST"
fi

# 2. Cursor
if [ "$TARGET" = "cursor" ] || [ "$TARGET" = "all" ]; then
    CURSOR_DEST="$(pwd)/.cursor/rules"
    mkdir -p "$CURSOR_DEST"
    if [ -f "$SCRIPT_DIR/.cursor/rules/agent-superpowers.mdc" ]; then
        cp "$SCRIPT_DIR/.cursor/rules/agent-superpowers.mdc" "$CURSOR_DEST/"
    fi
    echo -e "${GREEN}✔ Installed into Cursor:${RESET} $CURSOR_DEST"
fi

# 3. Google Antigravity
if [ "$TARGET" = "antigravity" ] || [ "$TARGET" = "all" ]; then
    AG_DEST="$HOME/.gemini/antigravity/skills"
    mkdir -p "$AG_DEST"
    cp -R "$SCRIPT_DIR/skills/"* "$AG_DEST/" 2>/dev/null || true
    echo -e "${GREEN}✔ Installed into Antigravity:${RESET} $AG_DEST"
fi

# 4. OpenAI Codex
if [ "$TARGET" = "codex" ] || [ "$TARGET" = "all" ]; then
    CODEX_DEST="$(pwd)/.codex"
    mkdir -p "$CODEX_DEST"
    if [ -f "$SCRIPT_DIR/.codex/INSTALL.md" ]; then
        cp "$SCRIPT_DIR/.codex/INSTALL.md" "$CODEX_DEST/"
    fi
    echo -e "${GREEN}✔ Configured for Codex:${RESET} $CODEX_DEST"
fi

echo -e "\n${BOLD}${GREEN}✔ Agent Superpowers successfully installed!${RESET}"
echo -e "Run ${CYAN}python cli/superpowers.py list${RESET} to verify."
