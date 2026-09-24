from collections.abc import Iterable
from .domain import TodoItem

def overdue_candidates(items: Iterable[TodoItem], today: str) -> list[TodoItem]:
    """Return pending tasks with due dates earlier than an ISO date string."""
    if not isinstance(today, str) or len(today) != 10:
        raise ValueError("today must be an ISO date (YYYY-MM-DD)")
    try:
        from datetime import date
        cutoff = date.fromisoformat(today)
    except ValueError as exc:
        raise ValueError("today must be a valid ISO date") from exc
    result = []
    for item in items:
        due = getattr(item, "due_date", None)
        if item.completed or not due:
            continue
        try:
            due_date = date.fromisoformat(str(due))
        except ValueError:
            continue
        if due_date < cutoff:
            result.append(item)
    return result
