from collections.abc import Iterable
from .domain import TodoItem

def search(items: Iterable[TodoItem], text: str) -> list[TodoItem]:
    needle = str(text).strip().casefold()
    if not needle:
        return []
    return [i for i in items if needle in i.title.casefold() or needle in i.description.casefold()]

def by_category(items: Iterable[TodoItem], category: str) -> list[TodoItem]:
    value = str(category).strip().casefold()
    return [i for i in items if i.category.casefold() == value]

def ranked_search(items: Iterable[TodoItem], text: str) -> list[TodoItem]:
    needle = str(text).strip().casefold()
    if not needle:
        return []
    priority_rank = {"High": 0, "Medium": 1, "Low": 2}
    matches = []
    for item in items:
        title, description = item.title.casefold(), item.description.casefold()
        if needle in title or needle in description:
            matches.append((title != needle, not title.startswith(needle), priority_rank.get(item.priority, 99), title, item))
    matches.sort(key=lambda value: value[:-1])
    return [value[-1] for value in matches]

def pending_search(items: Iterable[TodoItem], text: str) -> list[TodoItem]:
    """Search only incomplete tasks while preserving relevance ranking."""
    return [item for item in ranked_search(items, text) if not item.completed]
