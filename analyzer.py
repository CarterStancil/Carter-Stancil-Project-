import matplotlib.pyplot as plt
from collections import defaultdict

def live_analyze(q, stop_signal="__STOP__"):
    fouls_per_season = defaultdict(int)

    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 6))
    line, = ax.plot([], [], marker="o", linewidth=2)

    ax.set_title("Rolling Personal Fouls per NBA Season (Live Stream)")
    ax.set_xlabel("Season")
    ax.set_ylabel("Cumulative Fouls")
    ax.grid(True, linestyle="--", alpha=0.6)

    while True:
        row = q.get()
        if row == stop_signal:
            break

        # Only count NBA Regular Season rows
        if row["League"] != "NBA":
            continue
        if row["Stage"] != "Regular_Season":
            continue

        season = row["Season"].strip()
        try:
            fouls = int(row["PF"])
        except ValueError:
            fouls = 0

        fouls_per_season[season] += fouls

        
        seasons = sorted(fouls_per_season.keys())
        fouls_vals = [fouls_per_season[s] for s in seasons]

        x_vals = list(range(len(seasons)))  

        line.set_xdata(x_vals)
        line.set_ydata(fouls_vals)

        ax.set_xticks(x_vals)
        ax.set_xticklabels(seasons, rotation=45)

        ax.relim()
        ax.autoscale_view()

        plt.draw()
        plt.pause(0.01)

    plt.ioff()
    plt.show()