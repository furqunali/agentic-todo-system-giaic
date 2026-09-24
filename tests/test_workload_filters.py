from todo_core.domain import TodoItem
from todo_core.workload_filters import overdue_candidates

def test_overdue_candidates_excludes_completed_and_future_items():
    items = [
        TodoItem("Late", "", "High", "Work", False),
        TodoItem("Done", "", "High", "Work", True),
    ]
    assert overdue_candidates(items, "2026-01-01") == []
