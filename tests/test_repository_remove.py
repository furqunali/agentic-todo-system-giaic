from todo_core.domain import TodoItem
from todo_core.repository import TodoRepository

def test_remove_returns_task_and_removes_it_case_insensitively():
    item = TodoItem("Prepare release")
    repository = TodoRepository([item])
    assert repository.remove("PREPARE RELEASE") == item
    assert repository.get(item.title) is None

def test_remove_unknown_task_returns_none():
    assert TodoRepository().remove("missing") is None
