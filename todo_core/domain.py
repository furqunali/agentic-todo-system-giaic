from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class TodoItem:
    title: str
    description: str = ""
    priority: str = "Medium"
    category: str = "General"
    completed: bool = False
    created_at: datetime = datetime.now(timezone.utc)

    def __post_init__(self):
        self.title = self.title.strip()
        self.description = self.description.strip()
        self.category = self.category.strip() or "General"
        self.priority = self.priority.title()
        if not self.title:
            raise ValueError("title is required")
        if self.priority not in {"High", "Medium", "Low"}:
            raise ValueError("priority must be High, Medium, or Low")

    def complete(self):
        self.completed = True
        return self

    def reopen(self):
        self.completed = False
        return self
