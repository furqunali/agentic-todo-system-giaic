from datetime import datetime

from .domain import TodoItem


def todo_to_dict(item: TodoItem) -> dict[str, object]:
    """Return a JSON-compatible snapshot of a validated todo item."""
    if not isinstance(item, TodoItem):
        raise TypeError("item must be a TodoItem")
    return {
        "title": item.title,
        "description": item.description,
        "priority": item.priority,
        "category": item.category,
        "completed": item.completed,
        "created_at": item.created_at.isoformat(),
    }


def todo_from_dict(data: dict) -> TodoItem:
    """Restore and validate a todo item from a JSON-compatible snapshot."""
    if not isinstance(data, dict):
        raise TypeError("todo snapshot must be a dictionary")

    required = {"title", "description", "priority", "category", "completed", "created_at"}
    missing = required - data.keys()
    if missing:
        raise ValueError(f"todo snapshot is missing {sorted(missing)[0]}")

    if not isinstance(data["completed"], bool):
        raise TypeError("completed must be a boolean")
    if not isinstance(data["created_at"], str):
        raise TypeError("created_at must be an ISO datetime string")

    try:
        created_at = datetime.fromisoformat(data["created_at"])
    except ValueError as exc:
        raise ValueError("created_at must be a valid ISO datetime") from exc

    return TodoItem(
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        category=data["category"],
        completed=data["completed"],
        created_at=created_at,
    )
