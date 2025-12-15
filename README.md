🤖 AI-Powered Customer Support Automation System
Ollama-Based Reasoning · n8n Workflow Orchestration
📌 Overview

This project is an AI-powered customer support automation system built using a locally hosted LLM via Ollama and workflow orchestration with n8n.

The system intelligently understands customer queries, decides whether to respond or take action, and automatically executes real-world workflows such as ticket creation and notifications — all without using cloud LLMs or external embedding services.

The design focuses on local inference, automation, and practical backend orchestration, making it suitable for self-hosted and privacy-sensitive environments.

🚀 Key Advantages

Fully local AI using Ollama
Uses a locally hosted LLM (via Ollama) for reasoning and response generation, ensuring data privacy and zero dependency on cloud AI services.

Intent-aware decision making
Interprets customer intent using LLM reasoning to determine whether to answer a query or trigger an operational workflow.

Automated workflow execution
Integrates with n8n to automatically perform actions such as ticket creation, email notifications, and escalation.

End-to-end support automation
Handles both conversational responses and operational requests within a single system.

Auditable and traceable actions
All interactions and triggered workflows can be logged, enabling transparency and monitoring.

Modular and extensible architecture
Clean separation between frontend, AI reasoning, and workflow orchestration allows easy future enhancements.



Privacy-friendly design
No user data is sent to third-party AI APIs; all AI inference runs locally.
User
 ↓
Frontend (Chat UI)
 ↓
Backend API (n8n Webhook)
 ↓
LLM Reasoning (Ollama)
 ↓
Intent-Based Routing
 ↓
n8n Workflow Orchestration
 ↓
Actions (Ticket, Email, Escalation)

🤖 Core Components
LLM Reasoning (Ollama)

Uses a locally running LLM (e.g., Phi, Llama-family models)

Interprets user queries

Generates natural language responses

Determines whether an action is required

Workflow Automation (n8n)

Acts as the orchestration backbone

Handles:

Ticket creation

Email notifications

Audit logging

Conditional branching

Integrates with external systems via HTTP/Webhooks

Frontend

Simple chat-style interface

Displays user queries and AI responses

Communicates with backend via HTTP requests

⚙️ Tech Stack
AI

LLM Runtime: Ollama (local inference)

Models: Phi / Llama-family models (CPU-based)

Backend & Automation

n8n (self-hosted)

Webhooks & HTTP Request nodes

Frontend

React (Vite)

Tailwind CSS

Chat-style UI

DevOps

Docker

Docker Compose

✨ Features

✅ Local AI inference using Ollama

✅ Intent-based query handling

✅ Automated ticket creation

✅ Email / notification workflows

✅ Workflow-driven architecture

✅ Privacy-first, self-hosted setup


.
├── frontend/
│   ├── src/
│   └── Dockerfile
├── n8n/
│   └── workflow.json
├── docker-compose.yml
└── README.md


🚀 Setup & Run
Prerequisites

Docker & Docker Compose

Ollama installed locally

1️⃣ Start Ollama
ollama serve
ollama pull phi3:mini

2️⃣ Start n8n
docker-compose up -d


🧪 Example Interaction

User:

I want a refund for order #12345

System Actions:

LLM interprets intent as a refund request

n8n workflow is triggered

Ticket is created automatically

Confirmation response is returned to the user

📊 Use Cases

Customer support automation

Internal helpdesk systems

Privacy-sensitive applications

Workflow-driven AI assistants

🏁 Conclusion

This project demonstrates how local LLMs combined with workflow orchestration can be used to build an intelligent, automated customer support system without relying on cloud AI services.

It highlights a practical approach to AI + automation using open-source tools and self-hosted infrastructure.

👤 Author

Developed as a hackathon / portfolio project focused on:

Local AI inference

Workflow automation

Practical system design

Privacy-first architectures


Output : 


<img width="1911" height="1182" alt="image" src="https://github.com/user-attachments/assets/b39c1c29-f923-42c5-8032-234bcfbbcb78" />
<img width="1919" height="1193" alt="image" src="https://github.com/user-attachments/assets/1d2f2f94-161a-4f14-a5af-dba0b013a836" />
<img width="1916" height="1189" alt="image" src="https://github.com/user-attachments/assets/809bb2f7-18a3-479e-bbf5-3df0edaa1663" />
<img width="1891" height="1185" alt="image" src="https://github.com/user-attachments/assets/dfb48db1-d723-4d71-bea8-9199323fc057" />






