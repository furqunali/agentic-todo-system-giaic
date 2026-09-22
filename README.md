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
- `todo_core/` — reusable domain, validation, filtering, prioritization, and workload logic
- `specs/` — feature specifications
- SQLite — local persistence

## Public API

Supported domain functions are exported from `todo_core`, so the core can be reused independently of Flask.

## Roadmap

- Natural-language task entry
- Agent-driven prioritisation and daily summaries
- Authentication and multi-user support
