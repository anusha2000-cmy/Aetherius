"""
sentry.py — Sentry Agent

This LlmAgent is the first responder in the Aetherius pipeline.

Responsibilities (to be implemented):
  - Receives raw disaster telemetry events from the orchestrator.
  - Calls the MCP geospatial tool (get_disaster_coordinates) to enrich events
    with geographic coordinates.
  - Performs a first-pass threat classification (fire / flood / earthquake …).
  - Passes structured, enriched incident data downstream to the Critic Agent.

Example system prompt (placeholder):
    "You are a first-responder analyst.  Given a disaster telemetry event,
     retrieve its coordinates via the MCP tool and classify its severity."
"""

from google.adk.agents import LlmAgent  # noqa: F401  (will be used in implementation)

# ---------------------------------------------------------------------------
# Agent definition will be added here
# ---------------------------------------------------------------------------
