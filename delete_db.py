# delete_db.py
import os

db_path = "db.sqlite3"
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Removed {db_path}")
else:
    print(f"No DB to remove at {db_path}")