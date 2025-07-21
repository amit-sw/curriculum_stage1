# db_utils.py
import sqlite3
import os
from config import DB_FILE

def init_db():
    """Initialize the database and create the schema if needed."""
    # Ensure the path to the DB file exists and create an empty DB if missing
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        open(DB_FILE, "a").close()

    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS curriculum (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_sentence TEXT,
                topic TEXT,
                prompt TEXT,
                response TEXT
            )
            """
        )
        conn.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_curriculum_topic ON curriculum(topic)"
        )
        conn.commit()

def insert_curriculum(topic_sentence, topic, prompt, response):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            INSERT INTO curriculum (topic_sentence, topic, prompt, response)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(topic) DO UPDATE SET
                topic_sentence=excluded.topic_sentence,
                prompt=excluded.prompt,
                response=excluded.response
            """,
            (topic_sentence, topic, prompt, response)
        )
        conn.commit()

def get_all_curriculums():
    with sqlite3.connect(DB_FILE) as conn:
        return conn.execute("SELECT * FROM curriculum").fetchall()
