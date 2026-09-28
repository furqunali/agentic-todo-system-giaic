from todo_core.domain import TodoItem
from todo_core.query import completed_search

def test_completed_search_returns_only_completed_matches():
    items = [
        TodoItem("Ship API", "release", "High", "Work", False),
        TodoItem("Ship docs", "release", "Low", "Work", True),
    ]
    assert [item.title for item in completed_search(items, "release")] == ["Ship docs"]
