# Phase 1 Spec: Core Todo CLI
## Data Model
- id: int (Primary Key)
- title: string
- description: string (optional)
- is_completed: boolean (default: False)

## Commands
- `add`: Accepts a title and optional description.
- `list`: Displays all tasks in a 'rich' table.
- `complete`: Marks a task ID as done.
- `delete`: Removes a task by ID.
