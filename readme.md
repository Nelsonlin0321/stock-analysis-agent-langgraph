# Stock Analysis Agent

A sophisticated stock analysis agent built using LangGraph and LangChain, designed to analyze stock market data and provide insights.

## Architecture and Framework

### Chosen Framework

This project leverages the powerful combination of LangGraph and LangChain, chosen specifically for their robust implementation of the ReAct (Reasoning and Acting) agent pattern and advanced error handling capabilities.

#### Why LangChain + LangGraph?

1. **ReAct Pattern Implementation**:

   - Enables the agent to reason about problems and take actions in a structured way
   - Combines reasoning (thinking) and acting (doing) in a single loop
   - Allows the agent to:
     - Plan its approach to complex stock analysis tasks
     - Execute actions based on its reasoning
     - Learn from outcomes and adjust its strategy
     - Handle multi-step analysis workflows efficiently

2. **Self-Error Handling**:
   - Built-in retry mechanisms with exponential backoff
   - Automatic error recovery and state management
   - Graceful degradation when services are unavailable
   - Ability to:
     - Detect and recover from API failures
     - Handle data inconsistencies
     - Maintain state during error recovery
     - Provide meaningful error feedback

### Architecture Overview

- **State Management**: Uses LangGraph's `StateGraph` for managing agent state and message flow
- **LLM Integration**: Implements DeepSeek's language model for natural language understanding and generation
- **Tool Integration**: Combines multiple specialized tools for stock analysis and data processing

## Agent Operation

### Planning and Execution

- Implements a directed graph structure for information processing

<img src='https://www.mermaidchart.com/raw/6a579ff6-aa7e-48b7-ae0e-264de058370b?theme=light&version=v0.1&format=svg' width=800, height=600></img>

### Dynamic Code Generation

- Generates analysis code based on user requirements
- Implements error handling and retry mechanisms

## Error Handling and Reliability

### Error Management

1. **Retry Mechanism**:
   - Implements exponential backoff for API calls
   - Maximum retry attempts for failed operations
   - Graceful degradation when services are unavailable

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Virtual environment tool (venv)
- UV package manager

### Installation

```shell
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Initialize UV and install dependencies
uv init
uv pip install -r pyproject.toml
```

### Environment Setup

1. Create a `.env` file in the project root
2. Add required API keys:
   ```
    DEEPSEEK_API_KEY=
    SERPER_API_KEY=
    GMAIL=
    GMAIL_APP_PASSWORD=
   ```

### Running the Agent

```shell
# Run the main agent
main.ipynb
```

## Project Structure

```
stock-analysis-agent-langgraph/
├── src/
│   ├── utils.py
│   ├── utils_stock.py    # Stock data processing utilities
│   ├── utils_news.py    # email sending utilities
│   └── utils_news.py     # News aggregation utilities
├── data/                 # Data storage directory
├── main.ipynb              # Main agent implementation in jupyter notebook
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

## Dependencies

Key dependencies include:

- langgraph: Agent framework
- langchain: Core agent functionality
- yfinance: Stock data fetching
- pandas: Data analysis
- tabulate: Data presentation
- python-dotenv: Environment management
