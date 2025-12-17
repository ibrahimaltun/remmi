from dataclasses import dataclass
from db import get_conn


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_time: str
    interval_minutes: int
    done: int


class TaskRepository:
    def list(self):
        with get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM tasks ORDER BY id DESC").fetchall()
            return [Task(**dict(r)) for r in rows]

    def create(self, title, desc, due_time, interval):
        with get_conn() as conn:
            conn.execute("INSERT INTO tasks(title,description,due_time,interval_minutes) VALUES(?,?,?,?)",
                         (title, desc, due_time, interval))

    def update(self, task_id, title, desc, due_time, interval):
        with get_conn() as conn:
            conn.execute("UPDATE tasks SET title=?,description=?,due_time=?,interval_minutes=? WHERE id=?",
                         (title, desc, due_time, interval, task_id))

    def delete(self, task_id):
        with get_conn() as conn:
            conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
