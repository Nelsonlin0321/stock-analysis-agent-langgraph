# Stock Analysis Agent

A sophisticated stock analysis agent built using LangGraph and LangChain, designed to analyze stock market data and provide insights.

## Architecture and Framework

### Chosen Framework
This project utilizes LangGraph as the primary agent framework, which provides a robust foundation for building complex, stateful agent workflows. The architecture is built on top of LangChain, leveraging its extensive tooling and integration capabilities.

### Architecture Overview
- **State Management**: Uses LangGraph's `StateGraph` for managing agent state and message flow
- **LLM Integration**: Implements DeepSeek's language model for natural language understanding and generation
- **Tool Integration**: Combines multiple specialized tools for stock analysis and data processing

## Agent Operation

### Planning and Execution
1. **Task Planning**:
   - The agent receives user queries and breaks them down into actionable steps
   - Uses LangGraph's state management to track progress and maintain context

2. **Tool Selection**:
   - Dynamically selects appropriate tools based on the task requirements
   - Available tools include:
     - Stock data fetching (yfinance)
     - Data analysis (pandas)
     - News aggregation
     - Technical analysis

3. **Information Flow**:
   - Implements a directed graph structure for information processing
   - Maintains state between operations for context preservation
   - Uses message passing for inter-tool communication

### Dynamic Code Generation
- Generates analysis code based on user requirements
- Implements error handling and retry mechanisms
- Supports multiple analysis types:
  - Technical analysis
  - Fundamental analysis
  - News sentiment analysis

## Error Handling and Reliability

### Error Management
1. **Retry Mechanism**:
   - Implements exponential backoff for API calls
   - Maximum retry attempts for failed operations
   - Graceful degradation when services are unavailable

2. **Data Validation**:
   - Input validation for all user queries
   - Data integrity checks for stock information
   - Format verification for generated outputs

3. **Fallback Strategies**:
   - Alternative data sources when primary sources fail
   - Caching mechanisms for frequently accessed data
   - Graceful error messages for user feedback

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


