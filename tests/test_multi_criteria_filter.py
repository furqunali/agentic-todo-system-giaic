from todo_core.domain import TodoItem
from todo_core.query import filter_tasks


def test_filter_tasks_combines_multiple_criteria():
    items = [
        TodoItem("Deploy API", "production", "High", "Work"),
        TodoItem("Deploy docs", "release", "Medium", "Work", True),
        TodoItem("Plan API", "production", "High", "Personal"),
    ]

    result = filter_tasks(
        items,
        text="api",
        category="work",
        priority="high",
        completed=False,
    )

    assert [item.title for item in result] == ["Deploy API"]


def test_filter_tasks_preserves_input_order():
    items = [
        TodoItem("First", priority="Low"),
        TodoItem("Second", priority="High"),
        TodoItem("Third", priority="High"),
    ]

    assert [item.title for item in filter_tasks(items, priority="high")] == [
        "Second",
        "Third",
    ]


def test_filter_tasks_ignores_unset_filters():
    items = [TodoItem("A"), TodoItem("B", completed=True)]

    assert filter_tasks(items) == items


def test_filter_tasks_rejects_empty_text_filter():
    items = [TodoItem("A")]

    assert filter_tasks(items, text="   ") == []
