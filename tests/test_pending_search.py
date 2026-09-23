from todo_core.domain import TodoItem
from todo_core.query import pending_search

def test_pending_search_excludes_completed_items():
    items = [
        TodoItem("Ship API", "release", "High", "Work", False),
        TodoItem("Ship docs", "release", "Low", "Work", True),
    ]
    assert [item.title for item in pending_search(items, "release")] == ["Ship API"]
