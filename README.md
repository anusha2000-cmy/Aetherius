# Aetherius — Multi-Agent Disaster-Response System

> **Status:** Skeleton / scaffold — logic not yet implemented.

Aetherius is a multi-agent disaster-response platform built with
[Google ADK](https://google.github.io/adk-docs/) and
[FastMCP](https://github.com/jlowin/fastmcp).

Three specialised LLM agents work sequentially to transform raw disaster
telemetry into a prioritised, human-readable response plan:

```
Raw Telemetry
     │
     ▼
┌─────────────┐
│  Sentry     │  — Enriches events with geospatial data, classifies threats
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Critic     │  — Audits for prompt-injection / spoofing, scores trust
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Strategist  │  — Synthesises a prioritised response plan for operators
└─────────────┘
```

The **MCP Geospatial Server** (`mcp_geospatial/server.py`) runs as a
side-car FastMCP process exposing the `get_disaster_coordinates` tool that
the Sentry Agent calls over MCP.

---

## Project Structure

```
aetherius/
├── src/
│   ├── __init__.py
│   ├── main.py                  # ADK Runner + SequentialAgent orchestrator
│   └── agents/
│       ├── __init__.py
│       ├── sentry.py            # LlmAgent — threat classification
│       ├── critic.py            # LlmAgent — injection detection
│       └── strategist.py        # LlmAgent — response planning
├── mcp_geospatial/
│   ├── __init__.py
│   └── server.py                # FastMCP server — geospatial tools
├── tests/
│   ├── __init__.py
│   └── mock_disaster_data.json  # Mock telemetry (valid + spoof incidents)
├── docs/
│   └── README.md                # Architecture diagrams (TBD)
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Quick Start

```bash
# 1. Create & activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy and populate the environment file
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 4. Start the MCP geospatial server
python -m mcp_geospatial.server

# 5. Run the orchestrator (in a separate terminal)
python -m src.main --sector SECTOR_42
```

## Requirements

- Python ≥ 3.11
- Google ADK (`google-adk`)
- FastMCP (`fastmcp`)
- A valid Gemini API key

## License

MIT
