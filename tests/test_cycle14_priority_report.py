from todo_core.domain import TodoItem
from todo_core.reporting import priority_report

def test_priority_report_counts_priorities():
    values = [TodoItem("A", "", "High", "General", False), TodoItem("B", "", "Low", "General", True)]
    assert priority_report(values) == {"High": 1, "Medium": 0, "Low": 1}
