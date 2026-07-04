# BlackRoth Enterprise AI Platform

BlackRoth is a full-stack Enterprise AI Platform providing secure AI
chat, enterprise knowledge retrieval, AI agents, workflow automation,
analytics, governance, and administration. The platform combines a
FastAPI backend with a React and TypeScript frontend.

------------------------------------------------------------------------

## Project Status

-   Sprint 1 --- Completed
-   Sprint 2 --- Completed
-   Sprint 3 --- Completed
-   Sprint 4 --- Completed
-   Sprint 5 --- Completed
-   Sprint 5 Bonus Challenge --- Completed

------------------------------------------------------------------------

# Technology Stack

## Backend

-   Python
-   FastAPI
-   Uvicorn
-   PostgreSQL
-   SQLAlchemy
-   JWT Authentication
-   Role-Based Access Control (RBAC)
-   Sentence Transformers
-   ChromaDB
-   BM25
-   Cross-Encoder Re-ranking
-   Docker

## Frontend

-   React
-   TypeScript
-   Vite
-   Tailwind CSS
-   Shadcn/UI
-   React Router
-   TanStack Query
-   Axios
-   Zustand
-   Recharts
-   Lucide React

------------------------------------------------------------------------

# Sprint 1 --- Enterprise AI Foundation

Sprint 1 established the secure backend foundation.

## Main Features

-   JWT-based authentication
-   Password hashing
-   Role-Based Access Control
-   PostgreSQL database integration
-   User and role management
-   Permission checks
-   Audit logging
-   Security middleware
-   Docker support

## Security Pipeline

``` text
User Request
    ↓
Authentication
    ↓
Authorization
    ↓
Security Validation
    ↓
Business Logic
    ↓
Audit Logging
    ↓
Response
```

------------------------------------------------------------------------

# Sprint 2 --- Enterprise RAG System

Sprint 2 implemented enterprise document processing and semantic
knowledge retrieval.

## Main Features

-   Document ingestion
-   Text extraction
-   Document chunking
-   Embedding generation
-   ChromaDB vector storage
-   Semantic search APIs
-   Metadata filtering
-   Enterprise knowledge retrieval

## RAG Pipeline

``` text
Document
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Generation
    ↓
Vector Database
    ↓
Semantic Search
    ↓
Relevant Context
```

------------------------------------------------------------------------

# Sprint 3 --- Advanced Enterprise AI Chat

Sprint 3 built an advanced Retrieval-Augmented Generation and enterprise
chat system.

## Main Features

-   Hybrid Search
-   Semantic Search
-   BM25 Keyword Search
-   Cross-Encoder Re-ranking
-   Query Rewriting
-   Conversation Memory
-   Context Builder
-   Multi-turn Chat
-   Source Citations
-   Hallucination Detection
-   Retrieval Evaluation
-   Response Quality Metrics
-   Cost Tracking

## Advanced RAG Pipeline

``` text
User Question
    ↓
Query Rewriting
    ↓
Hybrid Search
    ↓
Semantic Search + BM25
    ↓
Cross-Encoder Re-ranking
    ↓
Context Builder
    ↓
LLM Response
    ↓
Citation Engine
    ↓
Hallucination Detection
    ↓
Final Response
```

------------------------------------------------------------------------

# Sprint 4 --- Enterprise AI Agents and Workflow Automation

Sprint 4 introduced intelligent AI agents, enterprise tools, workflow
automation, and human approvals.

## AI Agent Orchestrator

-   Intent Detection
-   Agent Routing
-   Workflow Planning
-   Tool Selection
-   Result Aggregation
-   Error Recovery

## Supported Agents

-   HR Agent
-   Payroll Agent
-   Knowledge Agent
-   Project Management Agent
-   Analytics Agent
-   Customer Support Agent

## MCP Integration

-   Tool Discovery
-   Tool Health Checks
-   Tool Authentication
-   Tool Versioning
-   Retry Logic

## Enterprise Tools

-   Employee Tool
-   Leave Tool
-   Payroll Tool
-   Project Tool
-   Email Tool
-   Calendar Tool
-   Notification Tool

## Workflow Engine

-   Sequential Workflows
-   Parallel Workflows
-   Conditional Branching
-   Rollback on Failure

## Human Approval System

-   Leave Approval
-   Expense Approval
-   Payroll Approval
-   Policy Approval
-   Document Approval
-   Pending Queue
-   Approval History
-   Escalation Rules
-   Auto Reminders
-   Audit Trail

## Multi-Agent Collaboration

``` text
User
    ↓
Research Agent
    ↓
Planner Agent
    ↓
Executor Agent
    ↓
Validator Agent
    ↓
Final Response
```

## Workflow APIs

-   `POST /workflow/start`
-   `GET /workflow/history`
-   `GET /workflow/{id}`
-   `POST /workflow/cancel`
-   `POST /workflow/retry`

------------------------------------------------------------------------

# Sprint 5 --- Enterprise Frontend Development and End-to-End Integration

Sprint 5 delivered the complete frontend workspace and connected the
platform modules into one enterprise application.

## Task 1 --- Project Initialization

Created the React and TypeScript frontend using Vite, Tailwind CSS,
Shadcn/UI, React Router, TanStack Query, Axios, Zustand, and Recharts.

## Task 2 --- Authentication Module

-   Login
-   Forgot Password
-   Reset Password
-   MFA Verification
-   JWT Authentication
-   Protected Routes
-   Session Handling
-   Logout
-   Role-Based Navigation

## Task 3 --- Enterprise Dashboard

### Dashboard Widgets

-   Active AI Sessions
-   Active Users
-   Running Agents
-   Knowledge Base Size
-   Today's Queries
-   Average Response Time
-   Token Usage
-   Workflow Status

### Analytics

-   Daily Requests
-   AI Usage Trends
-   Cost Analytics
-   Retrieval Performance

## Task 4 --- AI Chat Interface

-   Multi-turn Chat UI
-   Chat History
-   Typing Indicator
-   Suggested Questions
-   Copy Response
-   Feedback Buttons
-   Source Citations
-   Enterprise RAG API Integration

## Task 5 --- Knowledge Base UI

-   Document Upload
-   Search
-   Department Filtering
-   Tags
-   Document Status
-   Version History
-   Preview Actions
-   Download Actions
-   Delete Actions
-   Approval Queue
-   Admin Approval

Supported formats: PDF, DOCX, TXT, and Markdown.

## Task 6 --- AI Agent Dashboard

-   Active Agents
-   Running Tasks
-   Agent Health
-   Tool Usage
-   Active Sessions
-   Agent Logs
-   Execution History
-   Start Agent
-   Stop Agent
-   Restart Agent
-   View Agent Memory

## Task 7 --- Workflow Management UI

-   Workflow List
-   Workflow Status
-   Workflow Progress
-   Approval Queue
-   Retry Failed Workflow
-   Workflow Timeline
-   Workflow Logs

## Task 8 --- Admin Console

### User Management

-   Create User
-   View Users
-   Delete User
-   Assign Roles

### Role Management

-   Admin
-   HR
-   Manager
-   Employee

### AI Settings

-   Model Selection
-   Temperature Control
-   Token Limits
-   Prompt Templates

### Audit Logs

-   User Actions
-   Tool Calls
-   Security Events

## Task 9 --- Analytics Dashboard

-   AI Requests
-   Cost Tracking
-   Agent Performance
-   RAG Accuracy
-   Hallucination Rate
-   API Response Time
-   Top Knowledge Sources
-   User Satisfaction
-   CSV Export
-   PDF Export Integration Point

## Task 10 --- End-to-End Integration

-   Shared Axios API Client
-   JWT Request Interceptor
-   Authentication Error Handling
-   FastAPI CORS Integration
-   TanStack Query
-   Automatic Retry Logic
-   Loading State Support
-   Offline Detection
-   Frontend and Backend Integration

------------------------------------------------------------------------

# Sprint 5 Bonus --- Enterprise AI Workspace

The bonus challenge transformed all frontend modules into one unified
enterprise workspace.

## Workspace Navigation

-   Dashboard
-   AI Chat
-   Knowledge
-   Agents
-   Workflows
-   Analytics
-   Admin
-   Settings
-   Profile

## Bonus Features

-   Responsive Sidebar
-   Mobile Navigation
-   Dark Mode Control
-   Real-Time Notification Interface
-   Ctrl + K Command Palette
-   Keyboard Navigation
-   Global Workspace Navigation
-   Offline Detection
-   Responsive Design
-   Accessibility Labels

## Workspace Architecture

``` text
Login
    ↓
Protected Route
    ↓
Enterprise Workspace
    ↓
Sidebar Navigation
    ↓
────────────────────────────────
Dashboard | Chat | Knowledge
Agents | Workflows | Analytics
Admin | Settings | Profile
────────────────────────────────
    ↓
Axios + TanStack Query
    ↓
FastAPI Backend
    ↓
Enterprise AI Platform
```

------------------------------------------------------------------------

# Complete Platform Architecture

``` text
User
    ↓
React + TypeScript Frontend
    ↓
JWT Authentication
    ↓
FastAPI Backend
    ↓
Security and RBAC
    ↓
────────────────────────────────
AI Chat
Enterprise RAG
AI Agents
Workflow Engine
MCP Tools
Knowledge Base
Analytics
Admin Console
────────────────────────────────
    ↓
PostgreSQL + ChromaDB
    ↓
Audit Logging and Monitoring
```

------------------------------------------------------------------------

# Project Structure

``` text
enterprise-ai-platform/
├── backend/
│   ├── agents/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── mcp/
│   ├── monitoring/
│   ├── rag/
│   ├── security/
│   ├── tools/
│   ├── workflows/
│   └── main.py
├── frontend/
│   └── src/
│       ├── api/
│       ├── assets/
│       ├── components/
│       ├── hooks/
│       ├── layouts/
│       ├── pages/
│       │   ├── admin/
│       │   ├── agents/
│       │   ├── analytics/
│       │   ├── auth/
│       │   ├── chat/
│       │   ├── dashboard/
│       │   ├── knowledge/
│       │   ├── profile/
│       │   ├── settings/
│       │   └── workflows/
│       ├── services/
│       ├── store/
│       ├── types/
│       └── utils/
├── docs/
├── docker/
├── kubernetes/
├── tests/
├── scripts/
└── README.md
```

------------------------------------------------------------------------

# Running the Backend

From the project root:

``` bash
python -m uvicorn backend.main:app --reload
```

Backend API: `http://127.0.0.1:8000`

Swagger documentation: `http://127.0.0.1:8000/docs`

------------------------------------------------------------------------

# Running the Frontend

Open another terminal:

``` bash
cd frontend
npm.cmd run dev
```

Frontend: `http://localhost:5173`

------------------------------------------------------------------------

# Security Features

-   JWT Authentication
-   Password Hashing
-   Role-Based Access Control
-   Protected Frontend Routes
-   API Authorization Headers
-   Input Validation
-   Output Validation
-   Audit Logging
-   Security Event Tracking
-   Human Approval Workflows
-   Tool Authentication
-   Offline Detection
-   Session Expiration Handling

------------------------------------------------------------------------

# Enterprise Capabilities

-   Secure Enterprise AI Chat
-   Retrieval-Augmented Generation
-   Hybrid Search
-   Source Citations
-   Hallucination Detection
-   Conversation Memory
-   AI Agent Routing
-   Multi-Agent Collaboration
-   MCP Integration
-   Enterprise Tool Calling
-   Workflow Automation
-   Human-in-the-Loop Approval
-   Role-Based Access
-   Knowledge Management
-   Monitoring
-   Analytics
-   Cost Tracking
-   Audit Logging

------------------------------------------------------------------------

# Final Result

The BlackRoth Enterprise AI Platform now provides a complete enterprise
AI ecosystem combining secure authentication, Enterprise RAG, AI chat,
AI agents, workflow automation, human approval, MCP tool integration,
knowledge management, analytics, administration, a full React workspace,
and end-to-end frontend/backend integration.

All Sprint 1 through Sprint 5 requirements and the Sprint 5 Bonus
Challenge have been completed.

# Author

**D. Venkatesh**
