from collections.abc import Iterable
from .domain import TodoItem

_PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}

def by_priority(items: Iterable[TodoItem], priority: str) -> list[TodoItem]:
    value = priority.title()
    return [item for item in items if item.priority == value]

def pending(items: Iterable[TodoItem]) -> list[TodoItem]:
    return [item for item in items if not item.completed]

def prioritize(items: Iterable[TodoItem]) -> list[TodoItem]:
    """Return pending work ordered by urgency without mutating the input."""
    values = [item for item in items if not item.completed]
    return sorted(values, key=lambda item: _PRIORITY_ORDER.get(item.priority, 99))
