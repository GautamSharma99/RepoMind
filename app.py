from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.tools.mcp import MCPTools
import asyncio
import os

load_dotenv()
api_key = os.getenv("OPENAI_KEY")
MCP_SERVER_URL = {
    "SERVER_URL": "http://mcp-gateway-github:8080"
}

async def main():
    MCP_TOOLKIT = MCPTools(url=MCP_SERVER_URL["SERVER_URL"], transport="streamable-http")
    await MCP_TOOLKIT.connect()

    agent = Agent(
        name="Github Repo Summarizer",
        role="You are a github repository agent that can answer questions about a repository and its codebase. you can perform tasks like summarizing the repository, finding specific code snippets, and explaining code functionality.",
        tools=[
            MCP_TOOLKIT
        ],
        model=OpenAIChat(
            model="gpt-5-mini",
            api_key=api_key,
            
        ),
        show_tool_calls=True,
        debug_mode=True,
        add_datetime_to_instructions=True
    )

    while True:
        query = input("\nEnter your query (type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Exiting...")
            break
        
        await agent.aprint_response(query)
    MCP_TOOLKIT.close()

if __name__ == "__main__":
    asyncio.run(main())