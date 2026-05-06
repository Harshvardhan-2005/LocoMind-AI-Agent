# 🧠 LocoMind — Local AI Agent with RAG & Toolformer Capabilities

LocoMind is a modular AI agent system built using LangGraph and LangChain that combines:

- Local LLM inference using Ollama
- Tool calling and orchestration
- Retrieval-Augmented Generation (RAG)
- Local vector embeddings
- Web search integration
- File system operations

The project demonstrates how modern AI agents can reason, retrieve information, and execute tools autonomously using graph-based workflows.

---

# 🚀 Features

## ✅ Modular Tool Architecture
Each capability is separated into independent tools for scalability and maintainability.

## ✅ LangGraph Workflow Orchestration
Uses LangGraph DAGs for agent execution flow and conditional routing.

## ✅ Retrieval-Augmented Generation (RAG)
Supports:
- document ingestion
- chunking
- embedding generation
- vector similarity search
- context-aware answering

## ✅ Local Embeddings with Ollama
Uses:
- `nomic-embed-text`

for fully local embedding generation.

## ✅ Hybrid AI Pipeline
Combines:
- Local inference (Ollama)
- Cloud generation (Gemini)

for optimized performance and reliability.

## ✅ Real-Time Web Search
DuckDuckGo-powered internet search tool.

## ✅ File System Tools
Supports:
- file creation
- writing content to files

## ✅ Arithmetic Tools
Basic arithmetic execution tools:
- addition
- subtraction
- multiplication

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Agent Framework | LangGraph |
| LLM Framework | LangChain |
| Local LLM | Ollama |
| Embeddings | nomic-embed-text |
| Vector Database | ChromaDB |
| Cloud LLM | Gemini 2.5 Flash |
| Search Engine | DuckDuckGo |
| Language | Python |

---

# 📂 Project Structure

```bash
agentic-ai/
│
├── Agents/
│   ├── main.py
│   │
│   └── tools/
│       ├── __init__.py
│       ├── add.py
│       ├── subtract.py
│       ├── multiply.py
│       ├── create_file.py
│       ├── write_file.py
│       ├── search_duckduckgo.py
│       └── rag_tools.py
│
├── requirements.txt
├── .gitignore
└── README.md
