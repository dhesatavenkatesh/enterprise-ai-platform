# Enterprise AI Platform for BlackRoth

## Project Overview

The Enterprise AI Platform is an AI-powered enterprise application developed for BlackRoth. The platform enables employees to securely access AI services based on their roles and permissions. It integrates authentication, Role-Based Access Control (RBAC), Retrieval-Augmented Generation (RAG), AI agents, monitoring, audit logging, and an administrative dashboard.

---

# Sprint 1

Sprint 1 focuses on building the project foundation, including:

- Project Initialization
- FastAPI Backend
- PostgreSQL Database
- JWT Authentication
- RBAC Foundation
- Admin APIs
- Audit Logging
- API Documentation
- Enterprise Architecture Documentation

---

# Features

## Authentication

- JWT Authentication
- Secure Login
- Logout
- Refresh Token
- Password Hashing using bcrypt
- Token Expiration

---

## User Management

- User Registration
- User Management APIs
- Role Management
- Permission Management

---

## Role-Based Access Control (RBAC)

Supported Roles:

- Admin
- HR
- Manager
- Employee
- Support

Role-based authorization ensures users only access resources permitted by their assigned role.

---

## AI Platform Components

- AI Chat
- Retrieval-Augmented Generation (RAG)
- Multi-Agent System
- MCP Tool Integration
- Enterprise Knowledge Search

---

## Monitoring

- Health Check API
- Audit Logs
- Request Monitoring

---

## Admin Dashboard APIs

- Get Users
- Create User
- Update User
- Delete User
- Get Roles
- Get Permissions

---

# Technology Stack

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- PostgreSQL

## Authentication

- JWT
- python-jose
- Passlib (bcrypt)

## ORM

- SQLAlchemy

## API Documentation

- Swagger UI
- OpenAPI

## Version Control

- Git
- GitHub

---

# Project Structure

```text
enterprise-ai-platform/

backend/
frontend/
gateway/
agents/
rag/
mcp/
security/
monitoring/
database/
docker/
kubernetes/
docs/
tests/
scripts/
```

---

# Backend Structure

```text
backend/

authentication/
chat/
rag/
agents/
users/
audit/
settings/

main.py
config.py
database.py
models.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/enterprise-ai-platform.git
```

---

## Open Project

```bash
cd enterprise-ai-platform
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib[bcrypt] python-multipart python-dotenv
```

---

## Start Server

```bash
cd backend

uvicorn main:app --reload
```

---

# API URLs

Home

```
GET /
```

Health Check

```
GET /health
```

Swagger Documentation

```
GET /docs
```

Authentication

```
POST /login

POST /logout

POST /refresh-token
```

Admin

```
GET /users

POST /users

PUT /users/{id}

DELETE /users/{id}
```

Roles

```
GET /roles
```

Permissions

```
GET /permissions
```

---

# Database

Database Name

```
enterprise_ai
```

Main Tables

- users
- roles
- permissions
- audit_logs

---

# Security Features

- Password Hashing
- JWT Tokens
- Secure Authentication
- Token Expiry
- RBAC Authorization
- Middleware Protection

---

# Documentation

Project documentation is available in the **docs** folder.

- api_documentation.md
- enterprise_architecture.md

---

# Sprint 1 Deliverables

- Project Repository
- Folder Structure
- FastAPI Backend
- PostgreSQL Database
- JWT Authentication
- RBAC Foundation
- Admin APIs
- Audit Logging
- Swagger Documentation
- Enterprise Architecture Documentation

---

# Future Enhancements (Sprint 2)

- AI Chatbot
- RAG Implementation
- ChromaDB / FAISS Integration
- Multi-Agent System
- MCP Tool Integration
- Monitoring Dashboard
- Docker Deployment
- Kubernetes Deployment

---

# Author

**Name:** Dhesata Venkatesh

**Project:** Enterprise AI Platform for BlackRoth

**Sprint:** Sprint 1

---

# License

This project is developed for educational and enterprise learning purposes.