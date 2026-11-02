#!/usr/bin/env bash
# Agent Superpowers: Universal Installer for macOS and Linux
# Author: Gabriele Dattile (https://github.com/GabrieleDattile)
# Repository: https://github.com/GabrieleDattile/agent-superpowers

set -e

BOLD="\033[1m"
GREEN="\033[32m"
CYAN="\033[36m"
YELLOW="\033[33m"
RESET="\033[0m"

echo -e "${BOLD}${CYAN}⚡ Agent Superpowers: Installing suite across AI platforms on Unix...${RESET}"

TARGET="${1:-all}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || echo "")"

# 1. Resolve source directory (Local clone OR Remote download)
LOCAL_SOURCE=""
if [ -n "$SCRIPT_DIR" ] && [ -d "$SCRIPT_DIR/skills" ]; then
    LOCAL_SOURCE="$SCRIPT_DIR"
elif [ -d "./skills" ]; then
    LOCAL_SOURCE="$(pwd)"
fi

TEMP_DIR="/tmp/agent-superpowers-install"
if [ -z "$LOCAL_SOURCE" ]; then
    echo -e "${YELLOW}⬇ Downloading latest Agent Superpowers package from GitHub...${RESET}"
    rm -rf "$TEMP_DIR"
    mkdir -p "$TEMP_DIR"
    
    DOWNLOAD_URL="https://github.com/GabrieleDattile/agent-superpowers/archive/refs/heads/main.tar.gz"
    curl -fsSL "$DOWNLOAD_URL" | tar -xz -C "$TEMP_DIR"
    
    if [ -d "$TEMP_DIR/agent-superpowers-main" ]; then
        LOCAL_SOURCE="$TEMP_DIR/agent-superpowers-main"
    else
        LOCAL_SOURCE="$(find "$TEMP_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
    fi
fi

echo -e "${GREEN}📦 Source package verified at:${RESET} $LOCAL_SOURCE"

# 2. Deploy Global Suite Installation to ~/.agent-superpowers
GLOBAL_DEST="$HOME/.agent-superpowers"
mkdir -p "$GLOBAL_DEST"
cp -R "$LOCAL_SOURCE/cli" "$GLOBAL_DEST/"
cp -R "$LOCAL_SOURCE/skills" "$GLOBAL_DEST/"
cp -R "$LOCAL_SOURCE/mcp" "$GLOBAL_DEST/"
cp -R "$LOCAL_SOURCE/bin" "$GLOBAL_DEST/"

# Create executable launcher in ~/.local/bin if directory exists
if [ -d "$HOME/.local/bin" ]; then
    cat << 'EOF' > "$HOME/.local/bin/superpowers"
#!/usr/bin/env bash
python3 "$HOME/.agent-superpowers/cli/superpowers.py" "$@"
EOF
    chmod +x "$HOME/.local/bin/superpowers" 2>/dev/null || true
fi

# Helper to deploy skills
deploy_skills() {
    local dest="$1"
    mkdir -p "$dest"
    find "$LOCAL_SOURCE/skills" -type f -name "SKILL.md" | while read -r skill_file; do
        skill_dir="$(dirname "$skill_file")"
        skill_name="$(basename "$skill_dir")"
        mkdir -p "$dest/$skill_name"
        cp -R "$skill_dir/"* "$dest/$skill_name/"
    done
}

# 3. Google Antigravity & Gemini CLI
if [ "$TARGET" = "antigravity" ] || [ "$TARGET" = "all" ]; then
    AG_DEST="$HOME/.gemini/antigravity/skills"
    AG_CONFIG_DEST="$HOME/.gemini/config/skills"
    deploy_skills "$AG_DEST"
    deploy_skills "$AG_CONFIG_DEST"
    echo -e "${GREEN}✔ Installed into Antigravity:${RESET} $AG_DEST and $AG_CONFIG_DEST"
fi

# 4. Claude Code
if [ "$TARGET" = "claude" ] || [ "$TARGET" = "all" ]; then
    CLAUDE_DEST="$HOME/.claude/skills"
    deploy_skills "$CLAUDE_DEST"
    echo -e "${GREEN}✔ Installed into Claude Code:${RESET} $CLAUDE_DEST"
fi

# 5. Cursor (Workspace rules)
if [ "$TARGET" = "cursor" ] || [ "$TARGET" = "all" ]; then
    CURSOR_DEST="$(pwd)/.cursor/rules"
    mkdir -p "$CURSOR_DEST"
    RULE_SRC="$LOCAL_SOURCE/.cursor/rules/agent-superpowers.mdc"
    RULE_DST="$CURSOR_DEST/agent-superpowers.mdc"
    if [ -f "$RULE_SRC" ] && [ "$RULE_SRC" != "$RULE_DST" ]; then
        cp -f "$RULE_SRC" "$RULE_DST"
        echo -e "${GREEN}✔ Installed into Cursor rules:${RESET} $RULE_DST"
    fi
fi

# 6. Windsurf
if [ "$TARGET" = "windsurf" ] || [ "$TARGET" = "all" ]; then
    WINDSURF_SRC="$LOCAL_SOURCE/.windsurfrules"
    WINDSURF_DST="$(pwd)/.windsurfrules"
    if [ -f "$WINDSURF_SRC" ] && [ "$WINDSURF_SRC" != "$WINDSURF_DST" ]; then
        cp -f "$WINDSURF_SRC" "$WINDSURF_DST"
        echo -e "${GREEN}✔ Installed into Windsurf:${RESET} .windsurfrules"
    fi
fi

# 7. OpenAI Codex
if [ "$TARGET" = "codex" ] || [ "$TARGET" = "all" ]; then
    CODEX_DEST="$(pwd)/.codex"
    mkdir -p "$CODEX_DEST"
    CODEX_SRC="$LOCAL_SOURCE/.codex/INSTALL.md"
    CODEX_DST="$CODEX_DEST/INSTALL.md"
    if [ -f "$CODEX_SRC" ] && [ "$CODEX_SRC" != "$CODEX_DST" ]; then
        cp -f "$CODEX_SRC" "$CODEX_DST"
        echo -e "${GREEN}✔ Configured for Codex:${RESET} $CODEX_DEST"
    fi
fi

# Cleanup
rm -rf "$TEMP_DIR" 2>/dev/null || true

echo -e "\n================================================================="
echo -e "${BOLD}${GREEN}✔ 11 Agent Superpowers & Python scripts installed successfully!${RESET}"
echo -e "  Location: $GLOBAL_DEST"
echo -e "  To launch CLI: python3 \"$GLOBALDEST/cli/superpowers.py\" list"
echo -e "  To launch Dashboard: python3 \"$GLOBALDEST/cli/superpowers.py\" dashboard"
echo -e "================================================================="
