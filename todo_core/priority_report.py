from collections.abc import Iterable
from .domain import TodoItem

def priority_report(items: Iterable[TodoItem]) -> dict[str, int]:
    """Count tasks by priority in a stable, explicit order."""
    counts = {"High": 0, "Medium": 0, "Low": 0, "Other": 0}
    for item in items:
        key = item.priority if item.priority in {"High", "Medium", "Low"} else "Other"
        counts[key] += 1
    return counts
