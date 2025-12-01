# Meeting Atmosphere MCP Service

Meeting Atmosphere MCP is a collection of tools designed to improve the atmosphere of meetings and team activities. The service provides various functions including generating ice-breaking games and providing casual jokes, aiming to help teams establish better communication atmosphere and enhance team cohesion.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) - Python package manager
- Node.js (optional, for npx deployment)

## Installation

Install the required dependencies using uv:

```bash
uv sync
```

## Running the Server

### Method 1: Using uv (Recommended)

1. Install dependencies:
```bash
uv sync
```

2. Run the service:
```bash
uv run python server.py
```

### Method 2: Using npx for Quick Deployment (Requires Node.js)

```bash
npx meeting-atmosphere-mcp
```

By default, this will start the server with SSE transport on port 8080 which is suitable for local development.

## Available Tools

This service includes the following tools:

1. **ice_breaking_game** - Generate ice-breaking games based on the number of participants
2. **jokes** - Get a list of jokes

## Technical Architecture

This service is built on the FastMCP framework and developed using Python. By integrating large language models, it can intelligently generate content that meets requirements.

## Customization

You can modify the following configurations as needed:
- Modify model configuration in [config.py](file:///Users/lcs/code/mcp_test/config.py)
- Set environment variables to use custom API keys