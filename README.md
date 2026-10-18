# 🤖 LangGraph Agentic SDLC & BRD Generation Pipeline

> **Stateful Multi-Agent Workflow Orchestrating RFP Analysis, Vector Knowledge Retrieval & Automated Business Requirements Document (BRD) Synthesis**

[![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agents-10b981?style=flat-square&logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)

---

## 🏛️ Architectural Overview

Manual requirements engineering from dense Request for Proposal (RFP) documents is slow and prone to compliance omissions. This repository demonstrates how to architect a **stateful multi-agent system using LangGraph** that parses unstructured requirements, injects corporate architectural governance via RAG, and produces formal Business Requirement Documents (BRDs).

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                    LANGGRAPH MULTI-AGENT SDLC TOPOLOGY                           │
└──────────────────────────────────────────────────────────────────────────────────┘
    [Raw RFP Document]
            │
            ▼
   [RFP Parser Node]  ──► Extracts requirement items, priorities & categories
            │
            ▼
  [Router Conditional Edge]
            │
      ┌─────┴────────────────────────────────┐
      ▼ (Security / Infra)                   ▼ (Standard Functional)
[Knowledge Retrieval Node]                   │
(Injects OIDC, DB, Caching guidelines)       │
      │                                      │
      └──────────────────┬───────────────────┘
                         ▼
             [BRD Synthesizer Node]
                         │
                         ▼
             [Compliance Verifier Gate]
                         │
                         ▼
        [Final Structured BRD Specification]
```

---

## 📁 Repository Structure

```
langgraph-agentic-sdlc/
├── langgraph_agent/
│   ├── state.py              # TypedDict graph state definitions
│   ├── graph.py              # Compiled state graph & orchestration engine
│   └── nodes/
│       ├── rfp_parser.py     # Token-aware requirement extractor
│       ├── router.py         # Conditional edge routing logic
│       ├── retriever_node.py # Architectural standards retrieval
│       ├── brd_synthesizer.py# Section drafting agent
│       └── verifier_node.py  # Quality gate & validation checks
├── api/
│   └── main.py               # FastAPI REST endpoint
├── sample_rfps/
│   └── enterprise_banking_rfp.md # Demo RFP input
├── tests/
│   └── test_graph.py         # Multi-agent execution test suite
├── Dockerfile                # Production container deployment
└── requirements.txt
```

---

## 🚀 Quickstart & Usage

### 1. Run the Multi-Agent Pipeline Test
```bash
python3 tests/test_graph.py
```

### 2. Launch FastAPI Service
```bash
uvicorn api.main:app --reload --port 8000
# OpenAPI Docs: http://localhost:8000/docs
```

### 3. Generate BRD via API
```bash
curl -X POST "http://localhost:8000/api/v1/sdlc/generate-brd" \
     -H "Content-Type: application/json" \
     -d '{
       "rfp_title": "Enterprise Cloud Migration",
       "rfp_content": "- 1. Must use Okta OIDC PKCE authentication.\n- 2. High-availability PostgreSQL database required."
     }'
```

---

## 👤 Author
**Rajat Patle** — Senior Software Engineer & AI Architect
- **Interactive Portfolio:** [rajat-dev-new.github.io](https://rajat-dev-new.github.io)
- **GitHub:** [@rajat-dev-new](https://github.com/rajat-dev-new)
- **Email:** [patlerajat94@gmail.com](mailto:patlerajat94@gmail.com)
