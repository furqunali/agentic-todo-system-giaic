import streamlit as st
from sqlmodel import Session, create_engine, select, or_, SQLModel
from models import Todo

# Database Setup
sqlite_url = "sqlite:///todo_v2.db"
engine = create_engine(sqlite_url)

# Database Table Creation
def init_db():
    SQLModel.metadata.create_all(engine)

st.set_page_config(page_title="GIAIC AI Todo Evolution", layout="wide")
st.title("🚀 Agentic Todo System - Phase 2")

# Initialize DB on start
init_db()

# Sidebar for adding tasks
with st.sidebar:
    st.header("Add New Task")
    title = st.text_input("Task Title")
    desc = st.text_area("Description")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    category = st.text_input("Category", "General")
    if st.button("Add Task"):
        if title:
            with Session(engine) as session:
                new_todo = Todo(title=title, description=desc, priority=priority, category=category)
                session.add(new_todo)
                session.commit()
                st.success("Task Added!")
        else:
            st.error("Please enter a title")

# Main Screen - List and Filter
col1, col2 = st.columns(2)
with col1:
    search = st.text_input("🔍 Search Tasks")
with col2:
    filter_prio = st.multiselect("Filter by Priority", ["High", "Medium", "Low"])

with Session(engine) as session:
    statement = select(Todo)
    if search:
        statement = statement.where(or_(Todo.title.contains(search), Todo.category.contains(search)))
    if filter_prio:
        statement = statement.where(Todo.priority.in_(filter_prio))
    
    results = session.exec(statement).all()
    
    if not results:
        st.info("No tasks found. Add your first task from the sidebar!")
    
    for todo in results:
        with st.expander(f"{'✅' if todo.is_completed else '⏳'} {todo.title} - [{todo.priority}]"):
            st.write(f"**Category:** {todo.category}")
            st.write(f"**Description:** {todo.description}")
