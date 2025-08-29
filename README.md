# RepoSage 🤖

An AI-powered tool to analyze and answer questions about GitHub repositories using GPT and custom tooling.

## Features

- Interactive CLI interface to ask questions about repositories
- GitHub repository analysis (stars, forks, description, etc.)
- File system operations (listing files, counting lines)
- Powered by GPT through OpenAI API
- MCP (Message Control Program) server for tool orchestration

## Prerequisites

- Python 3.x
- OpenAI API key
- GitHub personal access token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RepoMind.git
cd RepoMind
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```
OPENAI_KEY=your_openai_api_key
GITHUB_TOKEN=your_github_token
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Enter your questions about GitHub repositories when prompted
3. Type 'exit' to quit the application

## Architecture

- `app.py`: Main application entry point with the interactive CLI
- `mcp_server.py`: Tool server implementing various utilities:
  - Repository information fetching
  - File system operations
  - Line counting functionality

## Tools Available

- `list_files`: Lists all files in a given directory
- `count_lines`: Counts the number of lines in a specified file
- `github_repo_info`: Fetches repository information including stars, forks, and description

## Dependencies

- agno: Agent framework for tool orchestration
- openai: OpenAI API client
- mcp: Message Control Program implementation
- python-dotenv: Environment variable management
- requests: HTTP client for GitHub API calls

## License

MIT License

## Security Note

Never commit your `.env` file containing API keys to version control. The `.gitignore` file is configured to prevent this.