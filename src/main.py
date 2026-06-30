"""
main.py — Aetherius Orchestrator Entry Point

This module wires together all three LlmAgents (Sentry → Critic → Strategist)
into a single Google ADK SequentialAgent and runs it via the ADK Runner.

High-level flow (to be implemented):
  1. Load configuration from .env (GOOGLE_API_KEY, model name, MCP server URL).
  2. Instantiate each agent:
       sentry_agent    — enriches & classifies raw telemetry.
       critic_agent    — audits for prompt-injection / spoofing.
       strategist_agent — produces the final response plan.
  3. Compose them into a SequentialAgent so output of each step becomes
     input context for the next.
  4. Create an ADK Runner bound to the SequentialAgent.
  5. Accept a disaster telemetry event (CLI arg or stdin) and run the pipeline.
  6. Print / persist the Strategist's final response plan.

Usage (placeholder):
    python -m src.main --sector SECTOR_42
"""

import asyncio

# from google.adk.agents import SequentialAgent   # uncomment when implementing
# from google.adk.runners import Runner           # uncomment when implementing
# from src.agents.sentry     import sentry_agent
# from src.agents.critic     import critic_agent
# from src.agents.strategist import strategist_agent


async def main() -> None:
    """Entry-point coroutine — pipeline wiring goes here."""
    raise NotImplementedError("Orchestrator not yet implemented.")


if __name__ == "__main__":
    asyncio.run(main())
