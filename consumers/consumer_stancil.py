import sqlite3
import os

def setup_db(db_name="db.sqlite3"):
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fouls (
            season TEXT PRIMARY KEY,
            total_fouls INTEGER,
            total_rebounds INTEGER,
            total_steals INTEGER,
            total_blocks INTEGER
        )
    """)
    conn.commit()
    return conn

def consumer(q, db_name="db.sqlite3", stop_signal="__STOP__"):
    conn = setup_db(db_name)
    cur = conn.cursor()

    while True:
        message = q.get()
        if message == stop_signal:
            break

        season = message["season"]
        fouls = message["fouls"]
        rebounds = message["rebounds"]
        steals = message["steals"]
        blocks = message["blocks"]

        cur.execute("""
            INSERT OR REPLACE INTO fouls (season, total_fouls, total_rebounds, total_steals, total_blocks)
            VALUES (?, ?, ?, ?, ?)
        """, (season, fouls, rebounds, steals, blocks))

        conn.commit()
        print(f"[Consumer] Stored in DB: {message}")

    conn.close()