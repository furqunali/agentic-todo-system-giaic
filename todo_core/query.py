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
