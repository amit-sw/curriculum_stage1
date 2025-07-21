# db_utils.py
import sqlite3
from config import DB_FILE

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS curriculum (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_sentence TEXT,
            topic TEXT,
            prompt TEXT,
            response TEXT
        )
        """)
        conn.commit()

def insert_curriculum(topic_sentence, topic, prompt, response):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO curriculum (topic_sentence, topic, prompt, response) VALUES (?, ?, ?, ?)",
            (topic_sentence, topic, prompt, response)
        )
        conn.commit()

def get_all_curriculums():
    with sqlite3.connect(DB_FILE) as conn:
        return conn.execute("SELECT * FROM curriculum").fetchall()