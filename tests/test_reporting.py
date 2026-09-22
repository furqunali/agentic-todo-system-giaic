from todo_core.domain import TodoItem
from todo_core.reporting import category_report, status_report

def test_status_report_counts_total_pending_and_completed():
    items = [TodoItem("A", "", "High", "General", False), TodoItem("B", "", "Low", "General", True)]
    assert status_report(items) == {"total": 2, "pending": 1, "completed": 1}

def test_category_report_is_case_stable_and_sorted():
    items = [TodoItem("A", category="Work"), TodoItem("B", category="home"), TodoItem("C", category="Work")]
    assert category_report(items) == {"home": 1, "Work": 2}
