from collections.abc import Iterable
from .domain import TodoItem

def capacity_plan(items: Iterable[TodoItem], capacity: int) -> dict[str, object]:
    """Choose pending tasks within a count-based capacity, highest priority first."""
    if isinstance(capacity, bool) or not isinstance(capacity, int):
        raise TypeError("capacity must be an integer")
    if capacity < 0:
        raise ValueError("capacity cannot be negative")
    rank = {"High": 0, "Medium": 1, "Low": 2}
    pending = [item for item in items if not item.completed]
    ordered = sorted(pending, key=lambda item: (rank.get(item.priority, 99), item.title.casefold()))
    selected = ordered[:capacity]
    return {"selected": tuple(selected), "deferred": tuple(ordered[capacity:]), "selected_count": len(selected), "deferred_count": max(0, len(ordered) - capacity)}
