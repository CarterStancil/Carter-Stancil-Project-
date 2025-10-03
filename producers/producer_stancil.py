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
    fouls_per_season = defaultdict(int)

    
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["League"] != "NBA" or row["Stage"] != "Regular_Season":
                continue

            season = row["Season"].strip()
            try:
                fouls = int(row["PF"])
            except ValueError:
                fouls = 0
            fouls_per_season[season] += fouls

   
    for season, total_fouls in fouls_per_season.items():
        message = {"season": season, "fouls": total_fouls}
        q.put(message)
        print(f"[Producer] Produced: {message}")
        time.sleep(delay)

    q.put(stop_signal)  