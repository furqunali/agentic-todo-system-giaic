from todo_core.domain import TodoItem
from todo_core.query import by_category, search
from todo_core.filters import prioritize

def test_search_matches_description():
    items = [TodoItem("Deploy API", "production release"), TodoItem("Write docs")]
    assert search(items, "production")[0].title == "Deploy API"

def test_category_filter_is_case_insensitive():
    item = TodoItem("Deploy", category="Engineering")
    assert by_category([item], "engineering") == [item]

def test_prioritize_pending_work():
    low = TodoItem("Cleanup", priority="Low")
    high = TodoItem("Fix outage", priority="High")
    done = TodoItem("Already done", priority="High", completed=True)
    assert [item.title for item in prioritize([low, done, high])] == ["Fix outage", "Cleanup"]
