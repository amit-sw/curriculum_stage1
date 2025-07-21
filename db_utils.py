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
                response TEXT,
                topic_expansion TEXT,
                session_duration REAL
            )
            """
        )
        conn.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_curriculum_topic ON curriculum(topic)"
        )
        # Ensure new columns exist if upgrading an old DB
        try:
            conn.execute("ALTER TABLE curriculum ADD COLUMN topic_expansion TEXT")
        except Exception:
            pass
        try:
            conn.execute("ALTER TABLE curriculum ADD COLUMN session_duration REAL")
        except Exception:
            pass
        conn.commit()

def insert_curriculum(topic_sentence, topic, prompt, response, topic_expansion=None, session_duration=None):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            """
            INSERT INTO curriculum (topic_sentence, topic, prompt, response, topic_expansion, session_duration)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(topic) DO UPDATE SET
                topic_sentence=excluded.topic_sentence,
                prompt=excluded.prompt,
                response=excluded.response,
                topic_expansion=excluded.topic_expansion,
                session_duration=excluded.session_duration
            """,
            (topic_sentence, topic, prompt, response, topic_expansion, session_duration)
        )
        conn.commit()

def get_all_curriculums():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute("SELECT * FROM curriculum")
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        return columns, rows

def get_all_topics():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute("SELECT id, topic FROM curriculum ORDER BY topic")
        return cur.fetchall()

def get_curriculum_by_topic(topic):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute("SELECT * FROM curriculum WHERE topic=?", (topic,))
        row = cur.fetchone()
        if not row:
            return None
        columns = [desc[0] for desc in cur.description]
        return dict(zip(columns, row))

def update_curriculum(curriculum_id, topic_sentence, topic, prompt, topic_expansion=None, session_duration=None):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "UPDATE curriculum SET topic_sentence=?, topic=?, prompt=?, topic_expansion=?, session_duration=? WHERE id=?",
            (topic_sentence, topic, prompt, topic_expansion, session_duration, curriculum_id),
        )
        conn.commit()

def update_response(curriculum_id, response):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "UPDATE curriculum SET response=? WHERE id=?",
            (response, curriculum_id),
        )
        conn.commit()