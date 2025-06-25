# MCP Server Market
The MCP Server Market is a centralized repository for discovering and utilizing Model Context Protocol (MCP) servers. This repository contains a JSON configuration file (mcp_server_market.json) that lists various MCP server implementations, enabling seamless integration with the chatmcp chatbot/MCP-client application. The chatmcp application parses this JSON file to allow users to interact with different MCP servers. Additionally, this repository provides a platform for other developers to share their own MCP server implementations.

## ChatMCP Project URL
https://github.com/daodao97/chatmcp

## Purpose
The MCP Server Market aims to:

Provide a curated list of MCP server configurations for easy integration with MCP-compatible clients like chatmcp.
Enable developers to contribute their own MCP server implementations to the market.
Simplify the process of discovering and using MCP servers for various data sources and protocols.

## Getting Started
### Prerequisites
To use the MCP Server Market with the chatmcp application, ensure you have the following:

The chatmcp application installed and configured.
The required runtime environments for the MCP servers you wish to use (e.g., Python for uvx, Node.js for npx).
Necessary credentials or access tokens for servers that require authentication (e.g., GitHub personal access token).

### Using the MCP Server Market

Clone or Download the Repository:
git clone https://github.com/chatmcpclient/mcp_server_market.git


Access the JSON Configuration:The mcp_server_market.json file contains a list of available MCP servers with their respective configurations. The chatmcp application automatically parses this file to connect to the specified servers.

### Integrate with chatmcp:

Ensure the mcp_server_market.json file is accessible to your chatmcp application.
Configure chatmcp to point to the JSON file or include it in your project directory as required.
The chatmcp application will use the JSON to display and connect to available MCP servers.


Run an MCP Server:Each server in the mcp_server_market.json file specifies a command, args, and optional env variables. For example, to run the sqlite MCP server:
uvx mcp-server-sqlite --db-path /path/to/test.db



## JSON Configuration
The mcp_server_market.json file defines the available MCP servers with the following structure:

Key: The name of the MCP server (e.g., sqlite, github, Turkiye-Legal-MCP).
command: The executable command to run the server (e.g., uvx, npx).
args: An array of command-line arguments for the server.
env (optional): Environment variables required for the server (e.g., access tokens).

Example entry:
```json
{
    "mcpServers": {
        "sqlite": {
            "command": "uvx",
            "args": [
                "mcp-server-sqlite",
                "--db-path",
                "/path/to/test.db"
            ]
        }
    }
}
```

## Available MCP Servers
The current mcp_server_market.json includes the following servers:

* **sqlite***: Connects to an SQLite database.
* **fetch**: A basic fetch-based MCP server.
* **filesystem**: Accesses local filesystem data.
* **git**: Interacts with a Git repository.
* **github**: Connects to GitHub repositories (requires a personal access token).
* **postgres**: Connects to a PostgreSQL database.
* **Turkiye-Legal-MCP**: A custom MCP server for legal data, hosted at git+https://github.com/saidsurucu/yargi-mcp.

## Contributing
We welcome contributions to the MCP Server Market! To add your own MCP server:

### Fork this repository.
Add your server configuration to the mcp_server_market.json file.
Ensure your server is publicly accessible or provide clear instructions for setup.
Submit a pull request with a clear description of your MCP server and its use case.

Guidelines for Adding Servers

Use a unique key for your server in the mcpServers object.
Specify the correct command and args for running your server.
Include any required env variables, clearly indicating placeholders for sensitive data (e.g., <YOUR_TOKEN>).
Test your server with the chatmcp application to ensure compatibility.
Provide documentation for your server, including setup instructions and dependencies.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
## Contact
For questions or support, please open an issue on this repository or contact the maintainers.
