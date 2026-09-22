from collections.abc import Iterable

from .domain import TodoItem

_PRIORITY = {"High": 3, "Medium": 2, "Low": 1}


def workload_summary(items: Iterable[TodoItem]) -> dict[str, int]:
    """Summarize pending/completed work and weighted pending urgency."""
    pending = completed = urgency = 0
    for item in items:
        if item.completed:
            completed += 1
        else:
            pending += 1
            urgency += _PRIORITY.get(item.priority, 0)
    return {"pending": pending, "completed": completed, "urgency": urgency}
