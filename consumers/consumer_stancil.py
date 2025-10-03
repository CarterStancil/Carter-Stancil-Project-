import sqlite3

def setup_db(db_name="db.sqlite3"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fouls (
            season TEXT PRIMARY KEY,
            total_fouls INTEGER
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

        cur.execute("""
            INSERT OR REPLACE INTO fouls (season, total_fouls)
            VALUES (?, ?)
        """, (season, fouls))

        conn.commit()
        print(f"[Consumer] Stored in DB: {message}")

    conn.close()