from todo_core.domain import TodoItem
from todo_core.query import pending_search

def test_pending_search_excludes_completed_tasks():
    items = [TodoItem("Deploy API"), TodoItem("Deploy docs", completed=True)]
    assert [item.title for item in pending_search(items, "deploy")] == ["Deploy API"]
