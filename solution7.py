"""Extra runs conceded per team in the year 2016"""

import matplotlib.pyplot as plt
from match_file_reader import data_matches
from delivery_file_reader import data_delivery


def calculate(deliveries, matches):
    """Calculating extra runs conceded per team in 2016"""
    result = {}
    id_2016 = set()
    for match in matches():
        if int(match["season"]) == 2016:
            id_2016.add(match["id"])

    for delivery in deliveries():
        if delivery["match_id"] in id_2016:
            team_name = delivery["batting_team"]
            extra_runs = int(delivery["extra_runs"])
            if team_name in result:
                result[team_name] += extra_runs
            else:
                result[team_name] = extra_runs
    team_names = result.keys()
    extra_runs = result.values()
    return team_names, extra_runs

def plot(name, runs):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12,7))
    plt.title("Extra runs conceded per team in the year 2016", fontsize=14, fontweight="bold")
    plt.bar(name, runs, color="steelblue", edgecolor="black")
    plt.xlabel("Team name", fontsize=12)
    plt.ylabel("Runs", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution7.png", dpi=300)
    plt.show()

def execute(delivery, match):
    """Executing the calculation and plotting of data in bar chart"""
    teams, run = calculate(delivery, match)
    plot(teams, run)

execute(data_delivery, data_matches)
