"""
server.py — Aetherius Geospatial MCP Server

A FastMCP server that exposes geospatial disaster-data tools to ADK agents
over the Model Context Protocol (MCP).

Exposed tools (to be implemented):
  get_disaster_coordinates(sector_id: str) -> dict
      Looks up the given sector_id in tests/mock_disaster_data.json and
      returns a dict containing:
        - lat   (float)  : latitude of the disaster event centroid.
        - lon   (float)  : longitude of the disaster event centroid.
        - type  (str)    : disaster category (fire | flood | earthquake …).
        - severity (str) : low | medium | high | critical.
      Raises a ToolError if the sector_id is not found in the mock data.

Running the server (placeholder):
    python -m mcp_geospatial.server
    # or via FastMCP CLI:
    fastmcp run mcp_geospatial/server.py

Notes:
  - In production the JSON mock will be replaced by a live geospatial API
    (e.g., GDACS, NASA EONET).
  - Transport: stdio (default) — swap to SSE for networked deployments.
"""

from pathlib import Path

from fastmcp import FastMCP  # noqa: F401

# ---------------------------------------------------------------------------
# Server instantiation and tool definitions will be added here
# ---------------------------------------------------------------------------

DATA_FILE = Path(__file__).parent.parent / "tests" / "mock_disaster_data.json"

mcp = FastMCP(
    name="aetherius-geospatial",
    instructions="Provides geospatial coordinates for disaster sectors.",
)


# @mcp.tool()
# async def get_disaster_coordinates(sector_id: str) -> dict:
#     """Implementation goes here."""
#     raise NotImplementedError


if __name__ == "__main__":
    mcp.run()
