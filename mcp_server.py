from dotenv import load_dotenv
import os
import requests
from fastmcp import FastMCP

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("Please set GITHUB_TOKEN in .env")

# Initialize FastMCP server
mcp = FastMCP("RepoMind MCP 🚀")

# -------------------------
# Define tools
# -------------------------

@mcp.tool()
def list_files(path: str = ".") -> list:
    """List all files in a given directory"""
    import os
    return os.listdir(path)

@mcp.tool()
def count_lines(file_path: str) -> int:
    """Count lines in a file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

@mcp.tool()
def github_repo_info(repo: str) -> dict:
    """Fetch GitHub repo info"""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    url = f"https://api.github.com/repos/{repo}"
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        return {"error": f"{resp.status_code} - {resp.text}"}
    
    data = resp.json()
    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "description": data["description"]
    }

# -------------------------
# Start server
# -------------------------
if __name__ == "__main__":
    print("Starting MCP server on http://127.0.0.1:8000 ...")
    mcp.run()
