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
            matches.append(
                (
                    title != needle,
                    not title.startswith(needle),
                    priority_rank.get(item.priority, 99),
                    title,
                    item,
                )
            )
    matches.sort(key=lambda value: value[:-1])
    return [value[-1] for value in matches]


def completed_search(items: Iterable[TodoItem], text: str) -> list[TodoItem]:
    """Search only completed tasks while preserving relevance ranking."""
    return [item for item in ranked_search(items, text) if item.completed]


def pending_search(items: Iterable[TodoItem], text: str) -> list[TodoItem]:
    """Search only incomplete tasks while preserving relevance ranking."""
    return [item for item in ranked_search(items, text) if not item.completed]


def filter_tasks(
    items: Iterable[TodoItem],
    *,
    text: str | None = None,
    category: str | None = None,
    priority: str | None = None,
    completed: bool | None = None,
) -> list[TodoItem]:
    """Filter tasks by any combination of search, category, priority, and status.

    Filters are applied as an AND expression and the original item order is
    preserved. A missing filter (None) does not restrict the result.
    """
    values = list(items)

    if text is not None:
        needle = str(text).strip().casefold()
        if not needle:
            return []
        values = [
            item
            for item in values
            if needle in item.title.casefold() or needle in item.description.casefold()
        ]

    if category is not None:
        category_value = str(category).strip().casefold()
        values = [item for item in values if item.category.casefold() == category_value]

    if priority is not None:
        priority_value = str(priority).strip().title()
        values = [item for item in values if item.priority == priority_value]

    if completed is not None:
        values = [item for item in values if item.completed is completed]

    return values
