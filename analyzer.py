import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def analyze(db_name="db.sqlite3"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Create correlations table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS correlations (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            corr_fouls_rebounds REAL,
            corr_fouls_steals REAL,
            corr_fouls_blocks REAL
        )
    """)

    # --- Fetch data ---
    cur.execute("""
        SELECT season, total_fouls, total_rebounds, total_steals, total_blocks
        FROM fouls
        ORDER BY season
    """)
    rows = cur.fetchall()

    if not rows:
        print("No data found in database.")
        conn.close()
        return

    seasons = [r[0] for r in rows]
    fouls = np.array([r[1] for r in rows])
    rebounds = np.array([r[2] for r in rows])
    steals = np.array([r[3] for r in rows])
    blocks = np.array([r[4] for r in rows])

    # --- Plot total fouls per season ---
    plt.figure(figsize=(12, 5))
    plt.plot(seasons, fouls, marker="o", linewidth=2, label="Fouls")
    plt.title("Total Personal Fouls per NBA Season")
    plt.xlabel("Season")
    plt.ylabel("Total Fouls")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # --- Scatter plots ---
    fig, ax = plt.subplots(1, 3, figsize=(16, 5))

    ax[0].scatter(rebounds, fouls, color="blue")
    ax[0].set_xlabel("Total Rebounds")
    ax[0].set_ylabel("Total Fouls")
    ax[0].set_title("Fouls vs Rebounds")

    ax[1].scatter(steals, fouls, color="green")
    ax[1].set_xlabel("Total Steals")
    ax[1].set_ylabel("Total Fouls")
    ax[1].set_title("Fouls vs Steals")

    ax[2].scatter(blocks, fouls, color="purple")
    ax[2].set_xlabel("Total Blocks")
    ax[2].set_ylabel("Total Fouls")
    ax[2].set_title("Fouls vs Blocks")

    plt.tight_layout()
    plt.show()

    # --- Compute correlations ---
    corr_rebounds = np.corrcoef(fouls, rebounds)[0,1]
    corr_steals = np.corrcoef(fouls, steals)[0,1]
    corr_blocks = np.corrcoef(fouls, blocks)[0,1]

    print("Correlation Analysis:")
    print(f"Fouls vs Rebounds: {corr_rebounds:.3f}")
    print(f"Fouls vs Steals:   {corr_steals:.3f}")
    print(f"Fouls vs Blocks:   {corr_blocks:.3f}")

    for name, corr in [("Rebounds", corr_rebounds), ("Steals", corr_steals), ("Blocks", corr_blocks)]:
        if corr > 0:
            print(f"→ More {name.lower()} tend to come with more fouls.")
        else:
            print(f"→ More {name.lower()} tend to come with fewer fouls.")

    # --- Save results into correlations table ---
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("""
        INSERT INTO correlations (timestamp, corr_fouls_rebounds, corr_fouls_steals, corr_fouls_blocks)
        VALUES (?, ?, ?, ?)
    """, (timestamp, float(corr_rebounds), float(corr_steals), float(corr_blocks)))
    conn.commit()
    conn.close()

    print(f"\n Correlation results saved to 'correlations' table at {timestamp}.")