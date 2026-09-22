from collections.abc import Iterable
from .domain import TodoItem

def by_priority(items: Iterable[TodoItem], priority: str) -> list[TodoItem]:
    value = priority.title()
    return [item for item in items if item.priority == value]

def pending(items: Iterable[TodoItem]) -> list[TodoItem]:
    return [item for item in items if not item.completed]
