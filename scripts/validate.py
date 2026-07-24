#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "coreader"
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
FORBIDDEN_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\b(?:sk|ghp|gho|github_pat)_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bservice_role\b.{0,40}\beyJ", re.IGNORECASE),
)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as error:
        raise AssertionError(f"{path.relative_to(ROOT)} is not valid JSON: {error}") from error


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate() -> None:
    codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
    codex_market = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude_market = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    mcp = load_json(PLUGIN / ".mcp.json")

    versions = {
        codex.get("version"),
        claude.get("version"),
        claude_market.get("metadata", {}).get("version"),
        claude_market.get("plugins", [{}])[0].get("version"),
    }
    require(len(versions) == 1, f"manifest versions differ: {sorted(str(v) for v in versions)}")
    version = next(iter(versions))
    require(isinstance(version, str) and VERSION_RE.fullmatch(version) is not None, "version must be strict SemVer")

    require(codex.get("name") == "coreader", "Codex plugin name must be coreader")
    require(claude.get("name") == "coreader", "Claude plugin name must be coreader")
    require(codex_market.get("name") == "coreader", "Codex marketplace name must be coreader")
    require(claude_market.get("name") == "coreader", "Claude marketplace name must be coreader")

    server = mcp.get("mcpServers", {}).get("coreader", {})
    require(server.get("type") == "http", "Coreader MCP transport must be http")
    require(server.get("url") == "https://mcp.coreader.dev/mcp", "Coreader MCP URL is incorrect")

    interface = codex.get("interface", {})
    for key in ("composerIcon", "logo", "logoDark"):
        value = interface.get(key)
        require(isinstance(value, str) and value.startswith("./assets/"), f"{key} must reference ./assets")
        require((PLUGIN / value[2:]).is_file(), f"missing asset: {value}")

    skill = PLUGIN / "skills" / "coreader" / "SKILL.md"
    require(skill.is_file(), "missing Coreader Skill")
    skill_text = skill.read_text(encoding="utf-8")
    require(skill_text.startswith("---\n"), "Skill must include YAML frontmatter")
    require("paste a Coreader API token" in skill_text, "Skill must prohibit pasted tokens")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in FORBIDDEN_PATTERNS:
            require(pattern.search(text) is None, f"possible secret in {path.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        validate()
    except AssertionError as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("Coreader plugin repository validation passed.")
