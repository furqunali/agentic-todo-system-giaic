from todo_core.domain import TodoItem
from todo_core.query import ranked_search

def test_ranked_search_prefers_exact_and_prefix_title_matches():
    exact = TodoItem("Deploy")
    prefix = TodoItem("Deploy API", priority="Low")
    description = TodoItem("Release notes", "deploy checklist", priority="High")
    assert ranked_search([description, prefix, exact], "deploy") == [exact, prefix, description]

def test_ranked_search_returns_empty_for_blank_query():
    assert ranked_search([TodoItem("Deploy")], "  ") == []


from todo_core.domain import TodoItem
from todo_core.query import pending_search
def test_pending_search_excludes_completed_items():
    items=[TodoItem("Ship API","release","High","Work",False),TodoItem("Ship docs","release","Low","Work",True)]
    assert [item.title for item in pending_search(items,"release")] == ["Ship API"]
