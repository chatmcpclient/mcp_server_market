from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_market import MarketValidationError, load_market, validate_market


class ValidateMarketTest(unittest.TestCase):
    def test_repository_market_is_valid(self) -> None:
        validate_market(load_market(ROOT / "mcp_server_market.json"))

    def test_duplicate_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "market.json"
            path.write_text(
                '{"mcpServers":{"same":{"command":"one"},'
                '"same":{"command":"two"}}}',
                encoding="utf-8",
            )

            with self.assertRaisesRegex(MarketValidationError, "duplicate JSON key"):
                load_market(path)

    def test_invalid_server_shape_is_rejected(self) -> None:
        with self.assertRaisesRegex(MarketValidationError, "array of strings"):
            validate_market(
                {"mcpServers": {"broken": {"command": "uvx", "args": [1]}}}
            )


if __name__ == "__main__":
    unittest.main()
