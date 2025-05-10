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

3. **PythonREPL Integration**:
   - Seamless integration with Python's REPL for dynamic code execution

4. **Flexible Graph Orchestration**:
   - Customizable workflow design with directed graph structure

### Architecture Overview

- Implements a directed graph structure for information processing

<img src='https://www.mermaidchart.com/raw/4ae51c3c-fee7-499f-8bb7-a7abbfccff61?theme=light&version=v0.1&format=svg' width=800, height=600></img>

### Dynamic Code Generation and Execution

The agent employs a sophisticated ReAct (Reasoning and Acting) pattern for dynamic code generation and execution, specifically designed for financial data analysis:

1. **Code Generation Process**:
   - Analyzes user requirements and data context
   - Generates Python code for specific analysis tasks
   - Implements best practices for financial data analysis

2. **Self-Reflection Mechanism**:
   - Ensures all analysis requirements are met
   - Iteratively refines code based on execution results

3. **Execution Flow**:
   - Uses PythonREPL for safe code execution
   - Implements error handling and recovery

4. **Analysis Requirements Coverage**:
   - Technical Analysis (Moving averages, RSI, etc.)
   - Statistical Analysis (Descriptive statistics, distributions)
   - Risk Metrics (Sharpe ratio, volatility)
   - Performance Metrics (Returns, volume analysis)

5. **Quality Assurance**:
   - Code review before execution
   - Result validation after execution
   - Performance optimization
   - Documentation generation

### Challenges and Solutions

During the development of this agent, several significant challenges were encountered and addressed:

1. **State Management in ReAct Pattern**:
   - **Challenge**: The ReAct pattern's limitation in passing state between reasoning and tool execution
   - **Solution**: 
     - Utilized environment variables for state persistence across tool executions
     - Implemented a centralized state management using dotenv
     - Ensured state consistency through environment variable synchronization

2. **Visualization and Email Integration**:
   - **Challenge**: Difficulty in rendering visualizations in email HTML format
   - **Solution**:
     - Defined specific Python code generation in agent prompts for AWS integration
     - Implemented automatic image upload to AWS S3 for URL generation
     - Used generated URLs in email HTML for visualization rendering

3. **Graph Debugging and Error Tracing**:
   - **Challenge**: Complex graph structure making it difficult to identify failure points
   - **Solution**:
     - Implemented detailed logging at each node
     - Created a visual graph representation using Mermaid
     - Added state tracking and validation at each transition
     - Developed a step-by-step execution mode for debugging

4. **Tool Integration Complexity**:
   - **Challenge**: Managing multiple tools with different input/output requirements
   - **Solution**:
     - Standardized tool interfaces using TypedDict
     - Implemented input validation and type checking
     - Created a tool registry for easy management and updates

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
