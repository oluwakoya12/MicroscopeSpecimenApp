import sqlite3
from .config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            microscope_size REAL NOT NULL,
            actual_size REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_record(username, microscope_size, actual_size):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO specimens (username, microscope_size, actual_size)
        VALUES (?, ?, ?)
    """, (username, microscope_size, actual_size))
    conn.commit()
    conn.close()

def get_all_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM specimens")
    results = cursor.fetchall()
    conn.close()
    return results
