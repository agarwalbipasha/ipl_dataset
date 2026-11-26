"""Number of matches played per year for all the years in IPL"""

import matplotlib.pyplot as plt

from match_file_reader import data_matches


def calculate(records):
    """Calculating the number of matches played per year"""
    result = {}
    for match in records():
        year = match["season"]
        if year not in result:
            result[year] = 1
        else:
            result[year] += 1
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    years = result.keys()
    count = result.values()
    return list(years), list(count)


def plot(year, counts):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Number of matches played per year", fontsize=14, fontweight="bold")
    plt.bar(year, counts, color="steelblue", edgecolor="black")
    plt.xlabel("Season (year)", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution5.png", dpi=300)
    plt.show()


def execute(match):
    """Executing the calculation and plotting of data in bar chart"""
    year, count = calculate(match)
    plot(year, count)


if __name__ == "__main__":
    execute(data_matches)
