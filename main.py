import threading
from queue import Queue
from producers.producer_stancil import producer
from analyzer import live_analyze

if __name__ == "__main__":
    q = Queue()
    stop_signal = "__STOP__"

    # Producer thread
    t1 = threading.Thread(target=producer, args=("data/players_stats_by_season_full_details.csv", q, 0.05))
    t1.start()

    # Analyzer runs in main thread
    live_analyze(q, stop_signal)

    t1.join()