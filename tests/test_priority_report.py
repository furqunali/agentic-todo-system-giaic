from todo_core.domain import TodoItem
from todo_core.reporting import category_report, priority_report

def test_category_report_merges_case_and_space_variants():
    items = [TodoItem("A", category=" Work "), TodoItem("B", category="work")]
    assert category_report(items) == {"work": 2}

def test_priority_report_counts_canonical_priorities():
    items = [TodoItem("A", priority="High"), TodoItem("B", priority="Low")]
    assert priority_report(items) == {"High": 1, "Medium": 0, "Low": 1, "Other": 0}
