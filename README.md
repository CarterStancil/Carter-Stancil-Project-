# Carter-Stancil-Project

## File Summary

- producers/producer.py – Reads NBA data, groups by season, and computes total fouls, rebounds, blocks, and steals. Emits these results as messages or events.
- consumers/consumer.py – Receives messages from the producer and writes the results into an SQLite database.
- analyzer.py – Loads stored data and generates line charts showing per-season trends in fouls, rebounds, blocks, and steals.
- main.py – Orchestrates the pipeline by running producer and consumer concurrently, then triggering the analyzer once data ingestion is complete.
- delete_db.py – Utility for deleting or resetting the SQLite database before a new run.
- requirements.txt – Lists Python dependencies.
- LICENSE.txt – Project license (MIT).

## Installation and Setup
Prerequisites
Python 3.8+
Recommended: virtual environment (venv or conda)

All dependencies listed in requirements.txt

## Installation Steps

### Clone the repository

git clone https://github.com/CarterStancil/Carter-Stancil-Project-.git
cd Carter-Stancil-Project-

### Set up a virtual environment (optional)

python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

### Install dependencies

pip install -r requirements.txt

### (Optional) Reset database

python delete_db.py

### Run the full pipeline

python main.py

## How It Works

### Producer

- Reads NBA data from a CSV file.
- Groups records by season.
- Calculates total fouls, rebounds, blocks, and steals for each season.
- Sends aggregated data to the consumer.

### Consumer

- Listens for messages from the producer.
- Stores the received season-level statistics in an SQLite database.

### Analyzer

- Reads data from the database.
- Produces line charts comparing how fouls, rebounds, blocks, and steals change across seasons.
- Optionally saves the plots as image files or displays them interactively.

### Main

- Launches the producer and consumer (often in separate threads).
- Waits for both to complete, then runs the analyzer automatically.

Example Output

After running main.py, the analyzer will generate charts with:

- X-axis: NBA Seasons (e.g. 2017–2018, 2018–2019, etc.)
- Y-axis: Totals for fouls, rebounds, blocks, and steals.

Each metric will appear as a separate line, allowing quick comparison of performance trends over time.

## Extending the Project

Potential areas for improvement:

- Add more advanced statistics (e.g., assists, turnovers, points per game).
- Break down metrics by team or player.
- Use a real-time message broker (Kafka, RabbitMQ) for streaming data.
- Expand analyzer visuals with interactive dashboards (Plotly, Dash).
- Introduce automated testing and logging for production readiness.

## Dependencies

Listed in requirements.txt. Typical dependencies include:

- pandas – for data loading and aggregation
- matplotlib – for visualization
- sqlite3 (built-in) – for local database storage
- threading (built-in) – for concurrent producer/consumer execution
