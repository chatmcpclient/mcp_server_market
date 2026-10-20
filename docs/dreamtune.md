# Dreamtune

[Dreamtune](https://dreamtunelabs.com) exposes model requests, tool runs, GPU compute and run inspection through MCP.

## Setup in ChatMCP

1. Install Node.js **22.20 or newer**, including `npx`, and make it available to ChatMCP. Restart ChatMCP after changing its PATH.
2. Add the `dreamtune` entry from `mcp_server_market.json`.
3. Replace `<YOUR_DREAMTUNE_API_KEY>` with your Dreamtune workspace API key in your private client configuration. Keep the production API origin and timeout from the entry.
4. Connect the server in ChatMCP and refresh its tool list.

The entry launches `dreamtune-mcp` from the version-pinned `@dreamtune/sdk@0.1.2` package using stdio. Node diagnostics go to stderr; stdout is reserved for the protocol. Keep real API keys out of public JSON files and Git commits.

## Verify the connection

Initialization and tool discovery list the available definitions without executing a model request, paid tool run or compute job. After connecting, use the schemas in the tool list and the [MCP tool reference](https://docs.dreamtunelabs.com/reference/mcp-tools) when requesting an operation.

Calls use the scopes and workspace of your key. Model requests, paid tool runs and compute jobs can incur charges, and compute may continue billing until stopped. Operations that require an idempotency key should reuse a saved key only for identical intended work.

For optional local GPU access configuration, see [local MCP setup](https://docs.dreamtunelabs.com/connect/local-mcp). If you prefer Streamable HTTP, the separate [hosted setup guide](https://docs.dreamtunelabs.com/connect/mcp) documents the required custom authentication header.
