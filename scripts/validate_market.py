#!/usr/bin/env python3
"""Validate the MCP server market without third-party dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


class MarketValidationError(ValueError):
    """Raised when the market file cannot be loaded safely."""


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise MarketValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_market(path: Path) -> dict[str, Any]:
    """Load a market file while rejecting duplicate JSON keys."""
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as error:
        raise MarketValidationError(str(error)) from error

    try:
        value = json.loads(raw, object_pairs_hook=_reject_duplicate_keys)
    except json.JSONDecodeError as error:
        raise MarketValidationError(
            f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}"
        ) from error

    if not isinstance(value, dict):
        raise MarketValidationError("market root must be an object")
    return value


def _require_string(value: Any, path: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise MarketValidationError(f"{path} must be a non-empty string")


def validate_market(market: dict[str, Any]) -> None:
    """Validate the market structure consumed by ChatMCP."""
    if set(market) != {"mcpServers"}:
        raise MarketValidationError("market root must contain only mcpServers")

    servers = market["mcpServers"]
    if not isinstance(servers, dict) or not servers:
        raise MarketValidationError("mcpServers must be a non-empty object")

    for name, config in servers.items():
        _require_string(name, "server name")
        if not isinstance(config, dict):
            raise MarketValidationError(f"mcpServers.{name} must be an object")

        _require_string(config.get("command"), f"mcpServers.{name}.command")

        args = config.get("args", [])
        if not isinstance(args, list) or not all(
            isinstance(argument, str) for argument in args
        ):
            raise MarketValidationError(
                f"mcpServers.{name}.args must be an array of strings"
            )

        environment = config.get("env", {})
        if not isinstance(environment, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in environment.items()
        ):
            raise MarketValidationError(
                f"mcpServers.{name}.env must map strings to strings"
            )


def main(arguments: list[str]) -> int:
    if len(arguments) != 2:
        sys.stderr.write("usage: validate_market.py <market.json>\n")
        return 2

    try:
        market = load_market(Path(arguments[1]))
        validate_market(market)
    except MarketValidationError as error:
        sys.stderr.write(f"market validation failed: {error}\n")
        return 1

    sys.stdout.write(f"validated {len(market['mcpServers'])} MCP servers\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
