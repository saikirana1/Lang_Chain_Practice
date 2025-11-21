# LangChain Practice - Copilot Instructions

## Project Overview

This is a **LangChain experimentation repository** focused on building and testing AI agent systems using the ReAct (Reasoning + Acting) framework. The project demonstrates integration of LLMs with external tools for autonomous decision-making.

## Architecture & Key Components

### Core Stack

- **LLM**: OpenAI's GPT-4o via `langchain_openai.ChatOpenAI`
- **Agent Framework**: LangChain 1.0+ `create_agent` with built-in tool-calling loop
- **Tools**: Custom and community-provided tools that agents can invoke
  - `TavilySearchResults`: Web search capability (from `langchain_community.tools`)
  - `get_system_time`: Custom tool example showing time formatting

### Data Flow

1. Agent receives a user query
2. LLM analyzes the query and decides which tools to use
3. Tools execute and return results
4. Agent reflects on results and decides next action
5. Process continues until agent reaches conclusion

## Essential Patterns

### Tool Definition

Custom tools use the `@tool` decorator from `langchain_core.tools`:

```python
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current date and time in the specified format"""
    # Implementation here
    return formatted_time
```

**Key**: Tool docstrings are critical—agents parse these to understand tool purpose and parameters.

### Agent Initialization

LangChain 1.0+ uses `create_agent` from `langchain.agents`:

```python
from langchain.agents import create_agent
from langchain_core.tools import tool

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant with access to web search and system time tools."
)
agent.invoke({"input": "Your query here"})
```

**Key**: The agent runs a tool-calling loop automatically—the LLM decides when to use tools and when to return final answers.

## Development Workflow

### Environment Setup

- **Python Version**: 3.12+ (set in `.python-version`)
- **Package Manager**: `uv` (faster replacement for pip)
- **Virtual Environment**: `.venv/` (standard location)

### Running Code

```bash
# Using Python directly (venv activated)
python simple_model_run.py

# Via uv (recommended, activates venv automatically)
uv run simple_model_run.py
```

### Configuration

- Environment variables loaded via `python-dotenv` from `.env` file
- **Required**: `OPENAI_API_KEY` for ChatOpenAI
- **Optional**: `TAVILY_API_KEY` for TavilySearchResults (web search)

## Project-Specific Conventions

1. **Tool Docstrings**: Always include clear docstrings—they're your tool's "interface contract" with the agent
2. **System Prompts**: Provide a clear system prompt when creating agents—it guides LLM behavior
3. **Input Format**: Agent input is a dict: `{"input": "query"}`, not a raw string
4. **Tool Parameters**: Use type hints in tool functions—LangChain passes these to the LLM for better decisions

## Key Files

- `simple_model_run.py`: Complete agent implementation example with search + time tools
- `main.py`: Placeholder entry point
- `pyproject.toml`: Dependencies and Python version constraint

## Common Tasks

**Add a new tool**: Create function with `@tool` decorator, add to `tools` list, ensure docstring describes parameters.

**Test agent behavior**: Use `verbose=True` to see the agent's internal reasoning chain—this reveals if the LLM understands your tools correctly.

**Debug API issues**: Check `.env` file has `OPENAI_API_KEY`; use `load_dotenv()` before any LangChain initialization.
