import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        name TEXT,
        phone TEXT,
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_request(user_id, username, name, phone, created_at):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO requests (user_id, username, name, phone, created_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, username, name, phone, created_at)
    )
    conn.commit()
    conn.close()

def get_last_requests(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, phone, created_at FROM requests ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows