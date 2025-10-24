# smolagents Setup TODO

## Environment Setup
1. Check if smolagents is already installed
   - The repository was cloned fresh but installation status is unknown.
   - Running examples without installation will fail with import errors.
   - Verifying first avoids redundant installation attempts.

2. Check Python version compatibility (requires >=3.10)
   - smolagents pyproject.toml specifies requires-python = ">=3.10".
   - Running on incompatible Python will cause cryptic errors.
   - Better to fail fast with clear version mismatch than debug later.

3. Identify required environment variables (HF_TOKEN, etc)
   - Many examples use InferenceClientModel which needs HF_TOKEN for API access.
   - Without proper tokens, agent runs will fail at model initialization.
   - Knowing requirements upfront prevents mid-execution failures.

4. Install smolagents with toolkit extras if needed
   - The [toolkit] extra includes WebSearchTool and other default tools.
   - Examples in documentation assume these tools are available.
   - Installing editable mode (-e) allows testing changes to the codebase.

5. Test import of smolagents core modules
   - Confirms installation worked and dependencies are satisfied.
   - Identifies missing system dependencies before running complex examples.
   - Validates the Python environment can load the package structure.

## Basic Examples
6. Run simplest possible agent example (no tools, just code)
   - Tests the minimal viable agent setup without external dependencies.
   - Validates that the code execution engine works in isolation.
   - Provides baseline understanding before adding complexity.

7. Test CodeAgent with basic math task (Fibonacci)
   - The Fibonacci example appears in multiple documentation sections.
   - Tests the agent's ability to write and execute Python code autonomously.
   - Small task means fast feedback on whether core functionality works.

8. Test with HF InferenceClientModel
   - This is the default model type used in most documentation examples.
   - Uses HuggingFace Inference API which requires only HF_TOKEN.
   - Confirms we can connect to external LLM providers successfully.

9. Test with local model if available
   - Removes dependency on external API calls and tokens.
   - Tests TransformersModel or MLXModel integration if system supports it.
   - Useful for understanding latency and capability differences.

10. Run web search tool example
    - WebSearchTool is part of the default toolkit and commonly demonstrated.
    - Tests tool calling mechanism end-to-end with real external service.
    - Validates that agent can successfully invoke tools and process results.

## Tool System
11. Create custom tool from scratch using @tool decorator
    - The @tool decorator is the recommended simple way to create tools.
    - Tests whether we understand the tool metadata requirements (inputs, outputs, descriptions).
    - Validates that custom tools integrate seamlessly with agents.

12. Create custom tool by subclassing Tool
    - Subclassing gives more control for complex tools with initialization logic.
    - Tests the full Tool class API and lifecycle management.
    - Shows the difference between decorator and class-based approaches.

13. Test loading tool from Hub
    - smolagents emphasizes sharing tools via HuggingFace Hub as Spaces.
    - Validates the Tool.from_hub() and load_tool() mechanisms work.
    - Tests trust_remote_code security model for external tools.

14. Test MCP integration with smolagents
    - Both SkogAI and smolagents support MCP servers as tool sources.
    - This is the most obvious integration point between the systems.
    - Validates ToolCollection.from_mcp() and MCPClient work correctly.

## Multi-Agent
15. Test multi-agent hierarchy (manager + managed agents)
    - Multi-agent systems are core to smolagents' value proposition per their docs.
    - Tests the managed_agents parameter and agent-as-tool pattern.
    - Validates whether this pattern aligns with SkogAI's orchestration approach.

16. Run the web browser multi-agent example
    - The web browser example is well-documented and shows real hierarchy.
    - Combines ToolCallingAgent (for web) with CodeAgent (for manager).
    - Demonstrates specialization through separate tool sets and memories.

## Execution Environments
17. Test local executor (default)
    - The LocalPythonExecutor is the default and requires no setup.
    - Tests the custom AST-based interpreter with import restrictions.
    - Establishes baseline performance and security characteristics.

18. Test Docker executor if available
    - Docker is locally available and requires no external accounts.
    - Tests containerized execution for isolation without cloud dependencies.
    - Validates the executor_type="docker" parameter works as documented.

19. Test E2B executor if account exists
    - E2B is the primary recommended sandboxing solution in the docs.
    - Tests remote execution environment with proper isolation.
    - Requires E2B_API_KEY which may not be available yet.

20. Test WebAssembly executor
    - WebAssembly via Pyodide+Deno is the newest execution option.
    - Tests browser-like sandboxing without containers or cloud services.
    - Validates executor_type="wasm" works if Deno is installed.

## Examples Directory
21. Run examples from smolagents/examples/ directory
    - The examples/ directory contains real working code not just docs.
    - Shows actual usage patterns and integration approaches.
    - Identifies which examples work out-of-box vs need configuration.

22. Test gradio_ui.py
    - GradioUI provides interactive web interface for agent interaction.
    - Tests whether the UI components work with the agent system.
    - Useful for understanding how to expose agents to end users.

23. Test text_to_sql.py
    - Demonstrates agents solving structured query generation tasks.
    - Tests complex tool usage and domain-specific problems.
    - Shows how agents handle data transformation workflows.

24. Test rag_using_chromadb.py
    - RAG is a common pattern for augmenting agent knowledge.
    - Tests integration with vector databases and retrieval systems.
    - Validates whether agents can effectively use retrieved context.

## Integration
25. Document all successful runs
    - Successful runs show what actually works in the current environment.
    - Creates reference material for future integration decisions.
    - Helps identify patterns that translate well to SkogAI workflows.

26. Document all failures and errors
    - Failures reveal dependencies, constraints, and edge cases.
    - Error messages guide troubleshooting and configuration needs.
    - Prevents repeating the same failed approaches later.

27. Identify integration points with SkogAI
    - smolagents and SkogAI likely have overlapping capabilities.
    - Finding natural boundaries prevents redundant implementations.
    - MCP support is already a known common interface.

28. Create minimal working example for SkogAI context
    - A simple working example serves as proof of concept.
    - Demonstrates concrete value before investing in deep integration.
    - Provides template for how SkogAI could invoke smolagents capabilities.
