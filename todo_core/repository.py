from collections.abc import Iterable
from .domain import TodoItem

class TodoRepository:
    def __init__(self, items: Iterable[TodoItem] = ()):
        self._items: dict[str, TodoItem] = {}
        for item in items:
            self.add(item)

    def add(self, item: TodoItem) -> TodoItem:
        key = item.title.casefold()
        if key in self._items:
            raise ValueError("todo title already exists")
        self._items[key] = item
        return item

    def list(self, completed: bool | None = None) -> list[TodoItem]:
        items = list(self._items.values())
        if completed is None:
            return items
        return [item for item in items if item.completed is completed]

    def get(self, title: str) -> TodoItem | None:
        return self._items.get(title.strip().casefold())
