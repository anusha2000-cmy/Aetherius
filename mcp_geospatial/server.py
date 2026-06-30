"""
server.py — Aetherius Geospatial MCP Server

A FastMCP server that exposes geospatial disaster-data tools to ADK agents
over the Model Context Protocol (MCP).

Running the server:
    python -m mcp_geospatial.server
    # or via FastMCP CLI:
    fastmcp run mcp_geospatial/server.py
"""

import os

from dotenv import load_dotenv
from fastmcp import FastMCP

from mcp_geospatial.validator import DualTokenValidator

load_dotenv()

HOST = os.getenv("MCP_SERVER_HOST", "localhost")
PORT = int(os.getenv("MCP_SERVER_PORT", 8000))
TRANSPORT = os.getenv("MCP_TRANSPORT", "stdio")

mcp = FastMCP("Aetherius Geospatial Server")

_validator = DualTokenValidator()

_RESOURCE_REGISTRY = {
    "boat_01": {"max_capacity": 8, "current_load": 0, "status": "available"},
    "boat_03": {"max_capacity": 6, "current_load": 6, "status": "at_capacity"},
    "heli_02": {"max_capacity": 4, "current_load": 1, "status": "available"},
}


@mcp.tool()
def get_incident_context(lat: float, lon: float, radius_km: float) -> dict:
    """Returns terrain, hazard polygons, road status, and nearest staging
    points for a location. Called by Ingestion Sentry to enrich raw reports."""
    return {
        "location": {"lat": lat, "lon": lon},
        "terrain_type": "urban_floodplain",
        "hazard_polygons": ["flood_zone_b", "road_closure_highway_7"],
        "road_network_status": "partially_passable",
        "nearest_staging_points": [
            {"id": "staging_north", "distance_km": 2.1, "type": "medical"},
            {"id": "staging_harbor", "distance_km": 4.7, "type": "boat_dock"},
        ],
    }


@mcp.tool()
def check_corroboration(
    incident_id: str,
    lat: float,
    lon: float,
    incident_type: str,
    report_timestamp: str,
    raw_text: str,
) -> dict:
    """The Dual-Token security gate. Cross-references incident against
    two independent sources. Called exclusively by Triage Critic. Logistical
    Strategist may NOT act on any incident that returns is_validated=False."""
    return _validator.validate(
        incident_id=incident_id,
        lat=lat,
        lon=lon,
        incident_type=incident_type,
        report_timestamp=report_timestamp,
        raw_text=raw_text,
    )


@mcp.tool()
def compute_route_feasibility(
    origin_lat: float,
    origin_lon: float,
    dest_lat: float,
    dest_lon: float,
    vehicle_type: str,
) -> dict:
    """Returns route viability for a vehicle type accounting for
    current flood/hazard layers. Called by Logistical Strategist."""
    return {
        "route_exists": True,
        "vehicle_type": vehicle_type,
        "estimated_eta_minutes": 18,
        "hazards_on_route": ["flood_zone_b"],
        "confidence": "high",
        "data_freshness": "simulated_historic",
    }


@mcp.tool()
def query_resource_proximity(
    incident_lat: float, incident_lon: float, resource_type: str
) -> dict:
    """Returns available resources ranked by travel time (not straight-line
    distance). Called by Logistical Strategist."""
    return {
        "resource_type": resource_type,
        "ranked_resources": [
            {
                "id": "boat_01",
                "eta_minutes": 12,
                "status": "available",
                "capacity": 8,
            },
            {
                "id": "boat_03",
                "eta_minutes": 24,
                "status": "available",
                "capacity": 6,
            },
        ],
    }


@mcp.tool()
def get_capacity_constraints(resource_id: str) -> dict:
    """Returns current load vs capacity to prevent double-allocation.
    Called by Logistical Strategist before finalizing any dispatch."""
    if resource_id not in _RESOURCE_REGISTRY:
        return {"error": "resource_not_found"}
    return _RESOURCE_REGISTRY[resource_id]


if __name__ == "__main__":
    if TRANSPORT == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport=TRANSPORT, host=HOST, port=PORT)
