import sqlite3
import matplotlib.pyplot as plt

def analyze(db_name="db.sqlite3"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT season, total_fouls FROM fouls ORDER BY season")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No data found in database.")
        return

    seasons = [r[0] for r in rows]
    fouls = [r[1] for r in rows]

    plt.figure(figsize=(12,6))
    plt.plot(seasons, fouls, marker="o", linewidth=2)
    plt.title("Total Personal Fouls per NBA Season")
    plt.xlabel("Season")
    plt.ylabel("Total Personal Fouls")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()