import json
from datetime import datetime, timezone

import pytest

from todo_core import TodoItem, todo_from_dict, todo_to_dict


def test_todo_snapshot_round_trips_through_json():
    item = TodoItem(
        "Ship API",
        "Release the public API",
        "High",
        "Work",
        True,
        datetime(2026, 10, 1, 12, 30, tzinfo=timezone.utc),
    )

    snapshot = todo_to_dict(item)
    restored = todo_from_dict(json.loads(json.dumps(snapshot)))

    assert restored == item
    assert restored.created_at == item.created_at


def test_todo_snapshot_is_json_compatible():
    item = TodoItem("Write docs")

    encoded = json.dumps(todo_to_dict(item))

    assert isinstance(encoded, str)


def test_todo_snapshot_rejects_malformed_data():
    with pytest.raises(TypeError):
        todo_from_dict([])

    with pytest.raises(ValueError):
        todo_from_dict({"title": "Missing fields"})

    with pytest.raises(TypeError):
        todo_from_dict(
            {
                "title": "A",
                "description": "",
                "priority": "Low",
                "category": "General",
                "completed": "false",
                "created_at": "2026-10-01T12:30:00+00:00",
            }
        )

    with pytest.raises(ValueError):
        todo_from_dict(
            {
                "title": "A",
                "description": "",
                "priority": "Low",
                "category": "General",
                "completed": False,
                "created_at": "not-a-date",
            }
        )
