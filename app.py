import os
import asyncio
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
if not OPENAI_KEY:
    raise ValueError("Set OPENAI_API_KEY in .env")

async def main():
    mcp_tools = MCPTools(
        command="python mcp_server.py",
        transport="stdio"
    )
    await mcp_tools.connect()

    agent = Agent(
        name="RepoMind",
        role="Answer questions about GitHub repos using tooling.",
        model=OpenAIChat(id="gpt-5-nano", api_key=OPENAI_KEY),
        tools=[mcp_tools],
        show_tool_calls=True,
        debug_mode=True
    )

    while True:
        q = input("\nAsk about the repo (type 'exit' to quit):\n> ")
        if q.lower() == "exit":
            break
        await agent.aprint_response(q)

    mcp_tools.close()

if __name__ == "__main__":
    asyncio.run(main())
