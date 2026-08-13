# Agentic To-Do System

An **agentic task-management system** built with Flask that goes beyond a plain to-do list: tasks are
interpreted and managed with the help of an AI agent, backed by a persistent database. Built as part of
the GIAIC Agentic AI program.

## What it does
- Create, track, and manage tasks through a Flask web app.
- An agent layer interprets task intent and helps organise / prioritise work.
- Persists all tasks in a local database so state survives restarts.

## Architecture
| File | Role |
|------|------|
| `app.py` | Flask application entry point and routes. |
| `main.py` | App bootstrap / runner. |
| `models.py` | Data models for tasks and persistence. |
| `database.db` | SQLite database storing tasks. |
| `specs/` | Feature specifications for the system. |
| `requirements.txt` | Python dependencies. |

## Tech stack
Python · Flask · SQLite · agentic task handling

## Getting started
```bash
git clone https://github.com/furqunali/agentic-todo-system-giaic.git
cd agentic-todo-system-giaic
python -m venv venv
venv\Scripts\activate        # Windows  (source venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
python app.py
```
Then open the local URL shown in the terminal (usually http://127.0.0.1:5000).

## Roadmap
- Natural-language task entry ("remind me to invoice ACME on Friday")
- Agent-driven prioritisation and daily summaries
- Auth + multi-user support

---
Built by **Furqan Ali** — AI Engineer & Agent Architect · [LinkedIn](https://linkedin.com/in/furqan-ali-08b030255)
