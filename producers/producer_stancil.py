"""

producer_stancil.py

"""


#####################################
# Import Modules
#####################################

import csv
import time
from collections import defaultdict

def producer(file_path, q, delay=0.1, stop_signal="__STOP__"):
    stats_per_season = defaultdict(lambda: {"fouls": 0, "rebounds": 0, "steals": 0, "blocks": 0})

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["League"] != "NBA" or row["Stage"] != "Regular_Season":
                continue

            season = row["Season"].strip()

            try:
                fouls = int(row["PF"])
                rebounds = int(row["REB"])
                steals = int(row["STL"])
                blocks = int(row["BLK"])
            except ValueError:
                fouls = rebounds = steals = blocks = 0

            stats_per_season[season]["fouls"] += fouls
            stats_per_season[season]["rebounds"] += rebounds
            stats_per_season[season]["steals"] += steals
            stats_per_season[season]["blocks"] += blocks

    for season, totals in stats_per_season.items():
        message = {
            "season": season,
            "fouls": totals["fouls"],
            "rebounds": totals["rebounds"],
            "steals": totals["steals"],
            "blocks": totals["blocks"],
        }
        q.put(message)
        print(f"[Producer] Produced: {message}")
        time.sleep(delay)

    q.put(stop_signal)