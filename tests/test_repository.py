import pytest
from todo_core.domain import TodoItem
from todo_core.repository import TodoRepository

def test_repository_add_get_and_filter():
    item = TodoItem("Ship release", priority="High")
    repo = TodoRepository([item])
    assert repo.get("ship release") is item
    assert repo.list(completed=False) == [item]

def test_duplicate_title_is_rejected():
    repo = TodoRepository([TodoItem("Write docs")])
    with pytest.raises(ValueError):
        repo.add(TodoItem("write docs"))
