# Spotify MCP server only (stdio). mlx-whisper is Apple-Silicon-only, so it's left out.
FROM python:3.12-slim
RUN pip install --no-cache-dir "mcp==2.3.0" "spotipy==2.26.0"
WORKDIR /app
COPY tools/spotify_mcp.py tools/
ENTRYPOINT ["python", "tools/spotify_mcp.py"]
