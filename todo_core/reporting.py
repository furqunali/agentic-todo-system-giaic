from collections.abc import Iterable
from .domain import TodoItem

def status_report(items: Iterable[TodoItem]) -> dict[str, int]:
    """Return deterministic counts suitable for dashboards and agent summaries."""
    pending = completed = 0
    for item in items:
        if item.completed: completed += 1
        else: pending += 1
    return {"total": pending + completed, "pending": pending, "completed": completed}
