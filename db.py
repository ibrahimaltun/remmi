import sqlite3
from pathlib import Path

DB_PATH = Path("tasks.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_time TEXT,
            interval_minutes INTEGER,
            done INTEGER DEFAULT 0
        )
        """)
