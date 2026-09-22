from todo_core.domain import TodoItem
from todo_core.workload import workload_summary


def test_workload_summary_counts_and_weights_pending_items():
    items = [
        TodoItem("Ship", priority="High"),
        TodoItem("Review", priority="Medium"),
        TodoItem("Done", priority="High", completed=True),
    ]
    assert workload_summary(items) == {"pending": 2, "completed": 1, "urgency": 5}


def test_workload_summary_handles_empty_input():
    assert workload_summary([]) == {"pending": 0, "completed": 0, "urgency": 0}
