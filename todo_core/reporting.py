from collections.abc import Iterable
from .domain import TodoItem

def status_report(items: Iterable[TodoItem]) -> dict[str, int]:
    """Return deterministic counts suitable for dashboards and agent summaries."""
    pending = completed = 0
    for item in items:
        if item.completed: completed += 1
        else: pending += 1
    return {"total": pending + completed, "pending": pending, "completed": completed}

def category_report(items: Iterable[TodoItem]) -> dict[str, int]:
    """Count tasks by normalized category in deterministic order."""
    counts: dict[str, int] = {}
    for item in items:
        category = item.category.strip() or "General"
        counts[category] = counts.get(category, 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: pair[0].casefold()))
