# Agentic To-Do System

A Flask-based task-management project with reusable todo-domain logic, persistence, workload analytics, and an agent-oriented application layer.

## Install

Requires Python 3.11+.

```bash
python -m pip install -r requirements.txt
python -m pip install -e ".[dev]"
```

## Run

```bash
python app.py
```

Then open the local URL shown in the terminal.

## Test

```bash
pytest
```

## Architecture

- `app.py` — Flask application entry point and routes
- `main.py` — application bootstrap
- `todo_core/` — reusable domain, validation, filtering, prioritization, persistence, and workload logic
- `specs/` — feature specifications
- SQLite — local persistence

## Public API

The `todo_core` package is usable independently of Flask. It exposes:

- task creation and validation through `TodoItem`
- search and multi-criteria filtering
- category, priority, and status reports
- prioritization and workload summaries
- validated dictionary snapshots through `todo_to_dict` / `todo_from_dict`

This separation keeps business rules testable and makes the domain layer reusable by future CLI, API, or agent interfaces.

## Roadmap

- Natural-language task entry
- Agent-driven prioritisation and daily summaries
- Authentication and multi-user support
- HTTP API for external clients
