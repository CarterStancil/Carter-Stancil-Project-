import threading
from queue import Queue
from producers.producer_stancil import producer
from consumers.consumer_stancil import consumer
from analyzer import analyze

if __name__ == "__main__":
    q = Queue()
    stop_signal = "__STOP__"

    
    t1 = threading.Thread(target=producer, args=("data/players_stats_by_season_full_details.csv", q, 0.1, stop_signal))
    t2 = threading.Thread(target=consumer, args=(q, "db.sqlite3", stop_signal))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
    analyze("db.sqlite3")