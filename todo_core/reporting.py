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
    """Count tasks by normalized category, merging case/whitespace variants."""
    counts: dict[str, int] = {}
    for item in items:
        category = item.category.strip() or "General"
        normalized = category.casefold()
        counts[normalized] = counts.get(normalized, 0) + 1
    return dict(sorted(counts.items()))

def priority_report(items: Iterable[TodoItem]) -> dict[str, int]:
    """Count tasks by canonical priority, including completed items."""
    counts = {"High": 0, "Medium": 0, "Low": 0, "Other": 0}
    for item in items:
        priority = item.priority.title()
        counts[priority if priority in {"High", "Medium", "Low"} else "Other"] += 1
    return counts
