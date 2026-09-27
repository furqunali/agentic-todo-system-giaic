from todo_core.domain import TodoItem
from todo_core.planning import capacity_plan

def test_capacity_plan_selects_high_priority_first():
    items = [TodoItem("Low", "", "Low", "General", False), TodoItem("Urgent", "", "High", "General", False)]
    plan = capacity_plan(items, 1)
    assert [item.title for item in plan["selected"]] == ["Urgent"]
    assert plan["deferred_count"] == 1
