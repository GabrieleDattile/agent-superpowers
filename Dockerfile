FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies for CLI and skill engines
RUN pip install --no-cache-dir pyyaml pydantic rich requests

# Copy codebase
COPY . /app

# Run MCP server with unbuffered stdio
ENTRYPOINT ["python", "-u", "mcp/server.py"]
