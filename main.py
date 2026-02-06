import typer
from sqlmodel import SQLModel, Session, create_engine, select
from models import Todo
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url)

def init_db():
    SQLModel.metadata.create_all(engine)

@app.command()
def add(title: str, description: str = None):
    with Session(engine) as session:
        new_todo = Todo(title=title, description=description)
        session.add(new_todo)
        session.commit()
        console.print(f"[green]Added task:[/green] {title}")

@app.command()
def list():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        table = Table(title="Todo List")
        table.add_column("ID", style="cyan")
        table.add_column("Title", style="magenta")
        table.add_column("Status", style="green")
        
        for todo in todos:
            status = "✅" if todo.is_completed else "⏳"
            table.add_row(str(todo.id), todo.title, status)
        console.print(table)

@app.command()
def complete(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            console.print("[red]Task not found[/red]")
            return
        todo.is_completed = True
        session.add(todo)
        session.commit()
        console.print(f"[green]Task {todo_id} marked as complete![/green]")

@app.command()
def delete(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            console.print("[red]Task not found[/red]")
            return
        session.delete(todo)
        session.commit()
        console.print(f"[red]Deleted task {todo_id}[/red]")

if __name__ == "__main__":
    init_db()
    app()
