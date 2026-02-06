from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy.orm import registry

# Registry check to prevent "InvalidRequestError" during reloads
mapper_registry = registry()

class Todo(SQLModel, table=True):
    __table_args__ = {'extend_existing': True} # This fixes the error
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    priority: str = Field(default="Medium")
    category: str = Field(default="General")
    is_completed: bool = Field(default=False)
