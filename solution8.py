"""Top 10 economical bowlers in the year 2015"""

import matplotlib.pyplot as plt

from delivery_file_reader import data_delivery
from match_file_reader import data_matches


def calculate(deliveries, matches):
    """Calculating top 10 economical bowlers in 2015"""
    economical_result = {}
    result = {}
    id_2015 = set()
    for match in matches():
        if int(match["season"]) == 2015:
            id_2015.add(match["id"])

    for delivery in deliveries():
        if delivery["match_id"] in id_2015:
            bowler = delivery["bowler"]
            runs_conceeded = (
                int(delivery["total_runs"])
                - int(delivery["bye_runs"])
                - int(delivery["legbye_runs"])
            )
            if bowler in result:
                result[bowler]["runs"] += runs_conceeded
                result[bowler]["balls"] += 1
            else:
                result[bowler] = {"runs": runs_conceeded, "balls": 1}

    for key, values in result.items():
        economical_rate = round(values["runs"] * 6 / values["balls"], 2)
        economical_result[key] = economical_rate

    sorted_economical_result = dict(
        sorted(economical_result.items(), key=lambda item: item[1])[:10]
    )
    economical_bowlers = sorted_economical_result.keys()
    economy_rate_bowler = sorted_economical_result.values()
    return list(economical_bowlers), list(economy_rate_bowler)


def plot(name, rate):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title(
        "Top 10 economical bowlers in the year 2015", fontsize=14, fontweight="bold"
    )
    plt.bar(name, rate, color="green", edgecolor="black")
    plt.xlabel("Bowler name", fontsize=12)
    plt.ylabel("Economy rate", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution8.png", dpi=300)
    plt.show()


def execute(delivery, match):
    """Executing the calculation and plotting of data in bar chart"""
    bowler, economy_rate = calculate(delivery, match)
    plot(bowler, economy_rate)


if __name__ == "__main__":
    execute(data_delivery, data_matches)
