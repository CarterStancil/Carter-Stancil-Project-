"""

producer_stancil.py

"""


#####################################
# Import Modules
#####################################

import csv
import time

def producer(file_path, q, delay=0.05, stop_signal="__STOP__"):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            q.put(row)
            time.sleep(delay)  
    q.put(stop_signal)  