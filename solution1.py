"""Plot a chart of the total runs scored by each teams over the history of IPL."""

import matplotlib.pyplot as plt

from delivery_file_reader import data_delivery


def calculate(data):
    """Calculating the total runs scored by each team"""
    result = {}
    for record in data():
        runs = int(record["total_runs"])
        team = record["batting_team"]
        if team not in result:
            result[team] = runs
        else:
            result[team] += runs

    team_names = result.keys()
    total_runs = result.values()
    # print(team_names, total_runs)
    return list(team_names), list(total_runs)


def plot(name, run):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Total runs scored by team", fontsize=14, fontweight="bold")
    plt.bar(name, run, color="steelblue", edgecolor="black")
    plt.xlabel("Team name", fontsize=12)
    plt.ylabel("Total runs", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution1.png", dpi=300)
    plt.show()


def execute(records):
    """Executing the calculation and plotting of data in bar chart"""
    team, runs = calculate(records)
    plot(team, runs)


if __name__ == "__main__":
    execute(data_delivery)
