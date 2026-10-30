FROM python:3.11-slim

WORKDIR /app

# Copy codebase
COPY . /app

# Run MCP server with unbuffered stdio
ENTRYPOINT ["python", "-u", "mcp/server.py"]
