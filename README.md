# LocoMind — Local AI Agent with RAG & Toolformer Capabilities

LocoMind is a modular AI agent system built using LangGraph and LangChain that combines:

- Local LLM inference using Ollama
- Tool orchestration and execution
- Retrieval-Augmented Generation (RAG)
- Local vector embeddings
- Web search integration
- File system operations

The project demonstrates how AI agents can reason, retrieve information, and execute tools autonomously using graph-based workflows.

---

# Features

## Modular Tool Architecture

Each capability is separated into independent tools for scalability and maintainability.

## LangGraph Workflow Orchestration

Uses LangGraph DAGs for agent execution flow and conditional routing.

## Retrieval-Augmented Generation (RAG)

Supports:
- document ingestion
- text chunking
- embedding generation
- vector similarity retrieval
- context-aware answering

## Local Embeddings with Ollama

Uses `nomic-embed-text` for local embedding generation.

## Hybrid AI Pipeline

Combines:
- Local inference using Ollama
- Cloud generation using Gemini

for optimized performance and reliability.

## Real-Time Web Search

DuckDuckGo-powered internet search tool.

## File System Tools

Supports:
- file creation
- writing content to files

## Arithmetic Tools

Provides:
- addition
- subtraction
- multiplication

---

# Tech Stack

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

# Project Structure

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
```

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/LocoMind-AI-Agent.git
cd LocoMind-AI-Agent
```

## Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

## Install Dependencies

```bash
uv pip install -r requirements.txt
```

## Setup Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

## Pull Ollama Models

```bash
ollama pull qwen3:4b
ollama pull nomic-embed-text
```

---

# Running the Project

```bash
python Agents/main.py
```

---

# Example Queries

## Arithmetic Tool

```python
What is 12 multiplied by 7?
```

## Web Search Tool

```python
Search latest AI news
```

## File Creation Tool

```python
Create a file named notes
and write hello world into it
```

## RAG Document Ingestion

```python
ingest_document('sample.txt')
```

## RAG Question Answering

```python
ask_rag('What is LangGraph?')
```

---

# RAG Pipeline

```text
Document
   ↓
Chunking
   ↓
Embeddings (Ollama)
   ↓
ChromaDB Storage
   ↓
Similarity Retrieval
   ↓
Gemini Context Generation
   ↓
Final Answer
```

---

# Agent Workflow Architecture

```text
User Query
     ↓
LangGraph Agent
     ↓
Qwen (Ollama)
     ↓
Tool Selection
     ↓
┌──────────────┬──────────────┬──────────────┐
│ Math Tools   │ Search Tool  │ RAG Tools    │
└──────────────┴──────────────┴──────────────┘
                                     ↓
                           Ollama Embeddings
                                     ↓
                                ChromaDB
                                     ↓
                            Retrieved Context
                                     ↓
                              Gemini 2.5 Flash
                                     ↓
                              Final Answer
```

---

# Future Improvements

- Multi-agent collaboration
- Memory persistence
- Browser automation tools
- Streaming frontend UI
- Voice assistant integration
- Autonomous task planning
- Async tool execution
- Docker deployment

---

# Author

Harshvardhan Kumar

---

# Project Highlights

- Built a hybrid local-cloud AI agent architecture
- Integrated RAG with local embeddings
- Implemented modular tool execution
- Used LangGraph for workflow orchestration
- Combined local inference with Gemini generation
