# Netscaler.MCP.server

<img width="724" alt="image" src="https://github.com/user-attachments/assets/64df900a-c7d6-4a96-86dc-0cbf894e01a3"/>


This project is an **MCP( Model Context Protocol ) server** designed to interact with Netscaler devices using the **NITRO API (REST)**. It provides a set of tools to manage Netscaler objects such as lbvserver,csvserver, service, server. The server is implemented using the `FastMCP` framework and exposes functionalities for creating, updating, listing, and deleting Netscaler objects.

## Features

- **Tool-Based API**: The project defines tools (`list_tool`, `create_tool`, `update_tool`, `bind_tool`, `delete_tool`) that encapsulate operations on Netscaler devices.
- **REST API Integration**: Uses Python's `requests` library to communicate with Netscaler devices via the NITRO API (REST).
- **Environment Configuration**: Sensitive information like IP addresses and authorization strings are managed through environment variables loaded from a `.env` file.
- **Extensibility**: Modular design allows additional tools or functionalities to be added easily.
- **Transport Support**: The server runs using the `stdio` transport, making it compatible with various client integrations.

### Key Files

- **`NetscalerMCPserver.py`**: The main server file that initializes the MCP server and defines the tools.
- **`Tools/NetscalerObject.py`**: A utility class for performing CRUD operations on Netscaler objects.

The repo also contains an example of the Claude desktop app config file.

### `It was tested with the Claude Desktop app. The MCP server was hosted in Windows WSL.`

<img width="362" alt="image" src="https://github.com/user-attachments/assets/c8e63a6e-c968-47ea-842f-173baf08d7b2"/>

### Credits
This was written by Mihai Cziraki
