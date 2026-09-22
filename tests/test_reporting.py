from todo_core.domain import TodoItem
from todo_core.reporting import status_report

def test_status_report_counts_total_pending_and_completed():
    items = [TodoItem("A", "", "High", "General", False), TodoItem("B", "", "Low", "General", True)]
    assert status_report(items) == {"total": 2, "pending": 1, "completed": 1}
