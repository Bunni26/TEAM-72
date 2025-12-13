🤖 AI-Powered Customer Support Automation System
RAG + n8n Workflow Orchestration
📌 Overview

This project is an AI-driven, autonomous customer support system that goes beyond traditional chatbots by combining:

Large Language Models (LLMs)

Retrieval-Augmented Generation (RAG)

Workflow automation using n8n

The system can answer customer queries using enterprise documents, automatically execute workflows such as ticket creation and email notifications, and provide explainable, auditable responses suitable for real-world enterprise use.

🚩 Problem Statement

Customer support teams handle a large number of repetitive queries and operational requests such as refunds, policy clarifications, delivery issues, and account updates. Existing customer support chatbots are largely rule-based and limited to predefined flows, making them unable to understand unstructured documents or automate complex workflows. This leads to high manual effort, slow response times, increased operational costs, and poor customer experience.

There is a need for an intelligent, autonomous customer support system that can retrieve accurate information from enterprise documents, reason over user intent, automate operational workflows, and provide transparent, auditable decisions.

🎯 Solution

This project introduces an AI-Powered Customer Support Automation System that:

Retrieves accurate answers from company documents using RAG

Reasons over customer intent using LLMs

Executes real-world actions via n8n workflows

Provides citations and explanations

Logs every interaction for auditability

Handles failures with retry and escalation mechanisms

🏗️ Architecture Overview
User
 ↓
Frontend (React Chat UI)
 ↓
Backend API (FastAPI)
 ↓
Intent Detection + AI Agent
 ↓
RAG Pipeline (Embeddings + Vector DB)
 ↓
LLM Reasoning
 ↓
n8n Workflow Orchestration
 ↓
Actions (Ticket, Email, Escalation)
 ↓
Simple Memory

🤖 Core Components
1. AI Agent

Interprets user intent

Decides whether to answer or trigger an action

Uses tools (workflows, APIs)

Maintains short-term conversation memory

2. Retrieval-Augmented Generation (RAG)

Prevents hallucinations

Retrieves answers strictly from documents

Provides citations for transparency

3. Workflow Automation (n8n)

Ticket creation

Email notifications

Human escalation

Retry & failure handling

Integration with external systems


⚙️ Tech Stack
AI & NLP

OpenAI GPT (LLM)

OpenAI Embeddings

Retrieval-Augmented Generation (RAG)

Backend

FastAPI (Python)

REST APIs

Workflow Automation

n8n

Data & Storage

Vector Database: Pinecone / Chroma

PostgreSQL (audit logs)

Frontend

React (minimal chat UI)

DevOps

Docker

Docker Compose

✨ Features

✅ Document-based answers with citations

✅ Automated ticket creation

✅ Email & notification workflows

✅ Explainable AI decisions

✅ Full audit trail

✅ Retry & error handling

✅ Production-oriented architecture

📁 Repository Structure
.
├── backend/
│   ├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   └── Dockerfile
├── n8n/
│   └── workflow.json
├── sample_docs/
│   ├── refund_policy.pdf
│   └── faq.pdf
├── docker-compose.yml
└── README.md

📄 Document Ingestion (RAG)

Documents are ingested once, not during chat.

Ingestion Flow:

PDF / Text → Chunking → Embeddings → Vector DB


These documents are later queried during chat to generate grounded responses.

🚀 Installation & Setup
Prerequisites

Docker & Docker Compose

OpenAI API key

Vector DB API key (Pinecone or Chroma)

1️⃣ Clone Repository
git clone https://github.com/your-username/ai-support-automation
cd ai-support-automation

2️⃣ Environment Variables

Create a .env file in the backend directory:

OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
DATABASE_URL=postgresql://user:pass@postgres:5432/supportdb

3️⃣ Start Services
docker-compose up -d

4️⃣ Access Services

Backend API: http://localhost:8000

n8n UI: http://localhost:5678

Frontend UI: http://localhost:3000

5️⃣ Import n8n Workflow

Open n8n UI

Import n8n/workflow.json

Configure credentials

Activate workflow

🧪 Testing
Functional Testing

Knowledge query → RAG answer with citation

Action request → ticket creation + email

Follow-up query → contextual answer

Failure Testing

Simulate API failure

Verify retry logic

Confirm escalation & logging

🎥 Demo Flow

Ask a policy question → answer with citation

Request refund → ticket created automatically

Email confirmation sent

Audit log recorded

📊 Use Cases

SaaS customer support

E-commerce issue resolution

Ed-tech student queries

Telecom service requests

🏁 Conclusion

This project demonstrates how AI + RAG + workflow automation can transform customer support into an intelligent, autonomous, and explainable system suitable for enterprise deployment.

👤 Author

Developed as a hackathon project focused on AI automation, explainable systems, and real-world applicability.
