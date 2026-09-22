from todo_core.domain import TodoItem
from todo_core.query import by_category, search

def test_search_matches_description():
    items = [TodoItem("Deploy API", "production release"), TodoItem("Write docs")]
    assert search(items, "production")[0].title == "Deploy API"

def test_category_filter_is_case_insensitive():
    item = TodoItem("Deploy", category="Engineering")
    assert by_category([item], "engineering") == [item]
