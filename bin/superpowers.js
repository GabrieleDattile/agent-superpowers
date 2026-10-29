#!/usr/bin/env node
/**
 * Agent Superpowers: Node.js / NPX CLI Bridge
 * Author: Gabriele Dattile (https://github.com/GabrieleDattile)
 */

import { spawn } from "child_process";
import { fileURLToPath } from "url";
import { dirname, join } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const rootDir = join(__dirname, "..");
const pythonScript = join(rootDir, "cli", "superpowers.py");

const args = process.argv.slice(2);
const pythonCmd = process.platform === "win32" ? "python" : "python3";

const child = spawn(pythonCmd, [pythonScript, ...args], {
  cwd: rootDir,
  stdio: "inherit"
});

child.on("error", (err) => {
  console.error("Failed to start Agent Superpowers CLI:", err.message);
  process.exit(1);
});

child.on("close", (code) => {
  process.exit(code ?? 0);
});
