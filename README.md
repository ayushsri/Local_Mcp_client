This project demonstrates how to build a fully local AI agent using the **Model Context Protocol (MCP)** with:

- 🧠 LlamaIndex FunctionCallingAgent
- 🗃️ SQLite for persistent key-value storage
- 🧰 Custom MCP tools for interacting with SQLite
- 🤖 Locally served LLM (via Ollama or mocked for demo)

## 📦 Requirements
```bash
pip install llama-index mcp sqlite3
```

If using a local LLM like DeepSeek-R1 via Ollama:
```bash
brew install ollama   # or follow instructions from https://ollama.com/
ollama run deepseek
```

## 🚀 How to Run
```bash
# 1. Start the MCP Server (runs SQLite tools)
python mcp_server.py

# 2. In another terminal, start the agent CLI
python main.py
```

## 🧪 Sample Queries
```
User: Add "name" as "Ayush"
User: Fetch value for key "name"
```

## 🛠️ File Structure
```
.
├── agent.py         # LlamaIndex agent with MCP tools
├── mcp_server.py    # MCP server with SQLite-backed tools
├── main.py          # CLI loop to interact with agent
└── README.md
```

## 📚 Reference
Based on the "100% Local MCP Client" project from [dailydoseofds.com](https://www.dailydoseofds.com/p/building-a-100-local-mcp-client/)

---
Happy Hacking 🚀
