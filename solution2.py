"""Top batsman for Royal Challengers Bangalore.Plot only top 10 batsmen by runs scored"""

import matplotlib.pyplot as plt

from delivery_file_reader import data_delivery


def calculate(data):
    """Calculating the runs scored by batsman of RCB"""
    result = {}
    for record in data():
        team = record["batting_team"]
        if team == "Royal Challengers Bangalore":
            batsman = record["batsman"]
            runs = int(record["total_runs"])
            if batsman not in result:
                result[batsman] = runs
            else:
                result[batsman] += runs
    result_topten = dict(
        sorted(result.items(), key=lambda item: item[1], reverse=True)[:10]
    )
    top_batsman = result_topten.keys()
    runs_batsman = result_topten.values()
    return list(top_batsman), list(runs_batsman)


def plot(name, run):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title(
        "Top batsman for Royal Challengers Bangalore", fontsize=14, fontweight="bold"
    )
    plt.bar(name, run, color="steelblue", edgecolor="black")
    plt.xlabel("Batsman name", fontsize=12)
    plt.ylabel("Total runs", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution2.png", dpi=300)
    plt.show()


def execute(record):
    """Executing the calculation and plotting of data in bar chart"""
    name, run = calculate(record)
    plot(name, run)


if __name__ == "__main__":
    execute(data_delivery)
