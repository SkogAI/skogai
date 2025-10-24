# smolagents Architecture Analysis

## Project Overview

**smolagents** is HuggingFace's lightweight library for code-based agents (~11.7k LOC, ~1k in core agents.py). It emphasizes simplicity while supporting sophisticated agentic patterns. Core philosophy: agents write Python code to call tools or orchestrate other agents.

**Key Differentiator**: Instead of traditional JSON/dictionary-based tool calling, agents generate and execute Python code snippets, leading to 30% fewer steps and higher performance on benchmarks.

---

## Core Architecture

### 1. High-Level Data Flow (ReAct Loop)

```
User Task
    ↓
agent.memory (conversation history)
    ↓
agent.model (LLM generates code)
    ↓
Parse code action from LLM output
    ↓
Execute code (tool calls as Python functions)
    ↓
Capture observations (print outputs)
    ↓
Loop or call final_answer() to exit
```

### 2. Module Organization (by responsibility)

**agents.py (1,776 LOC)** - Core orchestration and ReAct loop
- `MultiStepAgent` (ABC): Base class with ReAct framework, memory management, step execution
- `CodeAgent`: Generates Python code actions (PRIMARY AGENT TYPE)
- `ToolCallingAgent`: Traditional JSON/text tool calling (ALTERNATIVE)
- `RunResult`: Structured output with full execution history
- `ActionOutput`, `ToolOutput`: Intermediate result types

**models.py (2,011 LOC)** - LLM abstractions
- `Model` (ABC): Base class with standard interface
- `TransformersModel`: Local transformers/ollama
- `OpenAIModel`: OpenAI and compatible servers (Together, OpenRouter, etc.)
- `LiteLLMModel`: 100+ LLM providers via LiteLLM
- `InferenceClientModel`: HuggingFace Hub inference providers
- `VLLMModel`, `MLXModel`: Specialized serving
- `AzureOpenAIModel`, `AmazonBedrockModel`: Cloud providers
- Chat message types, tool calling protocol, response parsing

**tools.py (1,422 LOC)** - Tool abstraction and management
- `BaseTool` (ABC): Minimal interface (just `__call__`)
- `Tool`: Rich abstraction with JSON schema, inputs/outputs, Hub integration
- `PipelineTool`: Wraps HF Hub pipeline models as tools
- `ToolCollection`: Manages multiple tools, discovers from MCP, LangChain, Hub
- Tool validation, schema generation, Hub push/pull
- `@tool` decorator: Simplifies tool creation from functions

**local_python_executor.py (1,671 LOC)** - Safe Python code execution
- `PythonExecutor` (ABC): Base executor interface
- `LocalPythonExecutor`: In-process safe interpreter with sandboxing
- `evaluate_python_code()`: AST-based code evaluation with security constraints
- Authorized imports, safe builtins, loop/function support
- Handles print capture, return values, final_answer detection
- Fix for final_answer formatting

**remote_executors.py (915 LOC)** - Sandboxed execution options
- `RemotePythonExecutor` (ABC): Base for remote execution
- `E2BExecutor`: E2B.dev sandbox (browser-based)
- `ModalExecutor`: Modal.com cloud execution
- `DockerExecutor`: Docker container sandboxing
- `WasmExecutor`: Pyodide + Deno WebAssembly (browser)

**memory.py (316 LOC)** - Execution history and state
- `MemoryStep`, `ActionStep`, `TaskStep`, `PlanningStep`, `FinalAnswerStep`
- `AgentMemory`: Manages conversation history, tool calls, observations
- `ToolCall`: Represents individual tool invocation
- Serialization to JSON, conversion to chat messages for LLM context

**default_tools.py (658 LOC)** - Built-in tools
- `FinalAnswerTool`: Special tool to signal answer and exit ReAct loop
- `PythonInterpreterTool`: Evaluates Python code (for ToolCallingAgent)
- `PreTool`, `TOOL_MAPPING`: Tool registration system

**agent_types.py (284 LOC)** - Output type abstractions
- `AgentType` (ABC): Base for multimodal outputs
- `AgentText`, `AgentImage`, `AgentAudio`: Type wrappers with:
  - Lazy loading (path/tensor/bytes)
  - Notebook display support (`_ipython_display_`)
  - Conversion to/from multiple formats (PIL, torch, numpy)

**monitoring.py (265 LOC)** - Logging and telemetry
- `Monitor`: Token usage, timing tracking
- `AgentLogger`: Formatted console output (via rich)
- `LogLevel`: Verbosity control
- `Timing`, `TokenUsage`: Telemetry dataclasses
- OpenTelemetry integration for observability

**utils.py (581 LOC)** - Utility functions
- Exception hierarchy: `AgentError`, `AgentGenerationError`, `AgentParsingError`, etc.
- Code extraction/parsing: `extract_code_from_text()`, `parse_code_blobs()`
- Hub integration: `push_to_hub()`, `pull_from_hub()`
- Content handling: `truncate_content()`, multimodal input prep
- Gradio app template generation

**cli.py (164 LOC)** - Command-line interface
- `smolagent`: Generic agent CLI with tool selection
- `webagent`: Vision-based web browser agent
- Argument parsing, environment variable handling

**mcp_client.py (171 LOC)** - Model Context Protocol integration
- `MCPClient`: Discovers tools from MCP servers
- Converts MCP tool definitions to smolagents tools

**tool_validation.py (263 LOC)** - Tool descriptor validation
- Type hint parsing and conversion to JSON schema
- Validation of tool inputs/outputs

**_function_type_hints_utils.py (431 LOC)** - Type introspection
- Extract type hints from function signatures
- Convert Python types to JSON Schema
- Handle complex types (Union, Optional, List, Dict, etc.)

**gradio_ui.py (509 LOC)** - Gradio interface generation
- `launch_gradio_demo()`: Auto-generates UI for tools
- Web interface for agent interaction

**vision_web_browser.py (247 LOC)** - Vision-based web browser
- `VisionWebBrowser`: Selenium-based browser with vision understanding
- Tool for agents to browse web with visual feedback

### 3. Data Flow: Agent Execution

```
1. USER → agent.run(task, stream=False)
   ↓
2. MEMORY SETUP
   - Create TaskStep(task), reset if needed
   - Inject additional_args into state
   ↓
3. PYTHON EXECUTOR INIT (if code agent)
   - send_variables(state): Pass user data to executor
   - send_tools({tools, managed_agents}): Register callable tools
   ↓
4. REACT LOOP via _run_stream()
   a. build_messages_list() → ChatMessage[] for LLM input
   b. model.get_chat_completion(messages) → LLM output (code blob)
   c. parse_action() → Extract code from LLM output
   d. python_executor.run_code(code) → Execute and capture result
   e. If final_answer() called → Exit loop
      Else → Append observations to memory, loop
   ↓
5. OUTPUT
   - Extract output from FinalAnswerStep
   - If return_full_result: RunResult (with all steps, token usage)
   - Else: Just final answer value
```

### 4. Key Relationships

```
Agent ← Model (LLM backend)
   ↓
   ├→ Tools (callable functions with schema)
   │   └→ ToolCollection (groups, Hub integration)
   │
   ├→ Memory (history of steps)
   │   └→ MemoryStep[] (Task, Action, FinalAnswer)
   │
   ├→ PythonExecutor (runs code)
   │   └→ RemotePythonExecutor variants (E2B, Modal, Docker, Wasm)
   │
   ├→ Monitor (logs, token usage)
   │   └→ AgentLogger (console output)
   │
   └→ Managed Agents (for hierarchies)
       └→ Agents calling agents
```

### 5. Agent Types and Selection

**CodeAgent** (Preferred)
- Generates Python code snippets
- Tool calls: `result = tool_name(arg1=value1, arg2=value2)`
- Execution: Via PythonExecutor (safe interpreter or remote sandbox)
- Advantages: Fewer steps, cleaner code, better performance
- Risk: Code execution (mitigated by sandboxing options)

**ToolCallingAgent** (Traditional)
- Generates JSON/text tool calls
- Follows LLM's native tool_call protocol
- Simpler, no code execution risk
- Less efficient than code agents

---

## Development Build/Test Commands

**From Makefile:**
```bash
make quality    # ruff check + format check
make style      # ruff fix + ruff format
make test       # pytest ./tests/
```

**From pyproject.toml:**
```bash
pip install -e ".[dev]"        # Full dev environment
pytest ./tests/                # Run all tests
ruff check src tests examples  # Code quality
ruff format src tests examples # Auto-format
```

**Available test groups:**
- `tests/` (24 test files covering all modules)
- Fixtures in `tests/fixtures/` (agents, tools)
- Integration markers for optional dependencies

---

## Important Development Patterns

### 1. Tool Definition Pattern
```python
@tool
def my_tool(arg1: str, arg2: int) -> str:
    """Tool description. 
    
    Args:
        arg1: what it is
        arg2: what it is
    """
    return f"result: {arg1}, {arg2}"
```
- Decorator infers schema from type hints
- Description extracted from docstring
- Inputs/output_type auto-detected

### 2. Agent Setup Pattern
```python
model = SomeModel(model_id="...", api_key=...)
agent = CodeAgent(
    tools=[tool1, tool2],
    model=model,
    max_steps=5,
    verbosity_level=2
)
result = agent.run("task description")
```
- Simple composition: model + tools + config
- Stream support: `agent.run(..., stream=True)` yields steps
- Full result: `agent.run(..., return_full_result=True)` returns RunResult

### 3. Tool Collection Pattern
```python
tools = ToolCollection.from_hub(...)  # Load from Hub
tools = ToolCollection.from_mcp(...)  # Load from MCP server
agent = CodeAgent(tools=list(tools.values()))
```

### 4. Code Execution Safety
Three tiers:
- **LocalPythonExecutor**: AST-based in-process (safer than exec)
- **RemotePythonExecutor**: Sandboxed (E2B/Modal/Docker/Wasm)
- No sandbox: Risky, avoid in production

### 5. Memory/History Access
```python
agent.run(...)
# After run:
agent.memory.steps → list[MemoryStep]
agent.memory.get_messages() → list[ChatMessage]
```

### 6. Managed Agents (Hierarchies)
```python
manager_agent = CodeAgent(
    tools=[tool1, tool2],
    managed_agents=[worker_agent1, worker_agent2]
)
```
- Sub-agents appear as callable tools
- Each gets its own memory
- Orchestrated by parent

---

## File Structure

```
smolagents/
├── src/smolagents/
│   ├── agents.py              # Core: MultiStepAgent, CodeAgent, ToolCallingAgent
│   ├── models.py              # LLM backends: OpenAI, Transformers, etc.
│   ├── tools.py               # Tool abstraction and ToolCollection
│   ├── memory.py              # Execution history tracking
│   ├── local_python_executor.py  # Safe code execution
│   ├── remote_executors.py    # Sandboxed execution (E2B, Modal, Docker, Wasm)
│   ├── default_tools.py       # FinalAnswerTool, PythonInterpreterTool
│   ├── agent_types.py         # Multimodal output types (Text, Image, Audio)
│   ├── monitoring.py          # Logging, telemetry, token tracking
│   ├── cli.py                 # CLI interface
│   ├── gradio_ui.py           # Gradio UI generation
│   ├── vision_web_browser.py  # Web browser tool
│   ├── mcp_client.py          # Model Context Protocol integration
│   ├── tool_validation.py     # Tool schema validation
│   ├── _function_type_hints_utils.py  # Type introspection
│   ├── utils.py               # Utilities, exceptions, Hub integration
│   ├── __init__.py            # Public API exports
│   └── prompts/               # Prompt templates (YAML)
│       ├── code_agent.yaml
│       ├── toolcalling_agent.yaml
│       └── structured_code_agent.yaml
├── tests/
│   ├── test_agents.py         # Agent behavior
│   ├── test_tools.py          # Tool system
│   ├── test_models.py         # Model backends
│   ├── test_local_python_executor.py  # Code execution
│   ├── test_memory.py         # History tracking
│   ├── test_monitoring.py     # Logging
│   ├── test_remote_executors.py  # Sandboxed execution
│   ├── conftest.py            # Fixtures, markers
│   └── fixtures/
│       ├── agents.py
│       └── tools.py
├── examples/
│   ├── hello_world.py         # Simple demo
│   ├── multiple_tools.py      # Tool usage
│   ├── text_to_sql.py         # Advanced patterns
│   ├── sandboxed_execution.py # Executor options
│   └── ...
├── pyproject.toml             # Dependencies, build config
├── Makefile                   # Quality, test, style commands
├── CONTRIBUTING.md            # Contribution guidelines
├── AGENTS.md                  # Contributor guidelines
├── README.md                  # User documentation
└── SECURITY.md                # Security policy
```

---

## Key Entry Points for Integration

### For Creating Custom Agents
```python
from smolagents import CodeAgent, Tool, LiteLLMModel

# 1. Define tools (inherit from Tool or use @tool decorator)
# 2. Select model (any from models.py)
# 3. Instantiate agent
# 4. Call run()
```

### For Adding New Executors
- Inherit from `RemotePythonExecutor` in `remote_executors.py`
- Implement `run_code_raise_errors(code: str) → CodeOutput`
- Register in agent initialization

### For New Models
- Inherit from `Model` in `models.py`
- Implement `get_chat_completion(messages, stop_sequences)`
- Return `ChatMessage` or stream `ChatMessageStreamDelta`

### For Hub Integration
```python
agent.push_to_hub("username/repo_name")
agent = CodeAgent.from_hub("username/repo_name")
```

---

## Testing Patterns

**Fixtures** (tests/fixtures/):
- `agents.py`: Pre-configured agent instances
- `tools.py`: Sample tools for testing

**Test Organization**:
- `test_*.py` files mirror src module names
- Use pytest markers for optional dependencies
- `conftest.py` provides common fixtures

**Run subset**: `pytest tests/test_agents.py -v`

---

## Important Non-Obvious Patterns

1. **Code Format Consistency**: The same code format (```python ... ```) must match:
   - System prompt template (YAML)
   - Parser (agents.py)
   - Executor (local_python_executor.py)
   - Changing format requires updates in all three places

2. **Tool Auto-Registration**: Tools are discovered via:
   - Explicit list: `tools=[tool1, tool2]`
   - `@tool` decorator with auto-schema inference
   - Hub pull: `ToolCollection.from_hub(...)`
   - MCP servers: `ToolCollection.from_mcp(...)`
   - Each method produces Tool instances with identical interface

3. **Memory as First-Class Abstraction**: Unlike many frameworks, memory is:
   - Structured (typed steps, not just chat messages)
   - Serializable (dict conversion)
   - Replayable (can reconstruct message history)
   - Observable (token counts, timings, errors)

4. **Executor as Execution Runtime**: Code execution is abstracted:
   - Local: Direct Python interpreter (suitable for safe code)
   - Remote: Any sandboxed environment (E2B, Modal, Docker, Wasm)
   - Same interface: `run_code() → CodeOutput`
   - Tool sending happens before execution: `send_tools()` registers callables

5. **Streaming is Generator-Based**: Stream mode returns generator:
   - Each yield is a MemoryStep
   - Caller must iterate to trigger execution
   - Enables real-time monitoring/UI feedback

6. **Multimodal I/O via AgentType Wrappers**:
   - Input: Converted via `handle_agent_input_types()`
   - Output: Wrapped via `handle_agent_output_types()`
   - Lazy loading: Deferred until needed
   - Notebook-aware: Has `_ipython_display_()` for rich output

7. **Managed Agents as Callable Tools**: Sub-agents:
   - Added to agent's tools dict at runtime
   - Automatically wrapped with tool schema
   - Each maintains own memory
   - Enable hierarchical decomposition

---

## Build/Quality/Test Commands Summary

| Task | Command |
|------|---------|
| Check code quality | `make quality` or `ruff check src tests examples` |
| Auto-format code | `make style` or `ruff check --fix && ruff format` |
| Run tests | `make test` or `pytest ./tests/` |
| Install dev deps | `pip install -e ".[dev]"` |
| Install all extras | `pip install -e ".[all]"` |
| Specific extras | `pip install -e ".[docker,e2b,modal]"` |

---

## Dependency Organization

**Core** (always):
- huggingface-hub, requests, rich, jinja2, pillow, python-dotenv, pip

**Optional by feature**:
- `torch`: For local model support
- `litellm`: For 100+ LLM providers
- `openai`: For OpenAI API
- `transformers`: For local models
- `docker`: For Docker executor
- `e2b`, `modal`: For sandboxed execution
- `gradio`: For UI generation
- `mcp`: For Model Context Protocol
- `toolkit`: For web search tools
- `vision`: For web browser automation
- `audio`: For audio I/O
- `test`: Full test suite (includes all)

---

## Prompt Templates (YAML)

Located in `src/smolagents/prompts/`, three main templates:

1. **code_agent.yaml**: For CodeAgent
   - System prompt with Thought/Code/Observation cycle
   - Examples with notional tools
   - Emphasizes print() for observation capture

2. **toolcalling_agent.yaml**: For ToolCallingAgent
   - Traditional ReAct template
   - JSON tool call format

3. **structured_code_agent.yaml**: Experimental
   - For structured output support

---

## Contribution Guidelines (from AGENTS.md)

- Follow OOP principles
- Be Pythonic: idiomatic Python patterns
- Write unit tests for new functionality

---

## Assessment: Ready for Custom CLAUDE.md

**Strengths for Documentation**:
- Clear separation of concerns
- Well-defined abstractions (Model, Tool, Executor, Agent)
- Extensive type hints throughout
- Comprehensive test coverage
- Simple core logic (~1k LOC in agents.py)

**Key Concepts for CLAUDE.md**:
- ReAct loop with code-based actions
- Tool system (decoration, schema, Hub integration)
- Multiple executor options (safety spectrum)
- Memory as structured history (not just chat)
- Type-based multimodal I/O
- Streaming for real-time feedback
- Managed agents for hierarchies

**Should Emphasize**:
- Code execution safety (multiple options)
- Tool discovery (decorator vs collection vs Hub)
- Memory structure (key for understanding debugging)
- Executor selection (matches security/latency tradeoff)
- Streaming patterns (for UI integration)
