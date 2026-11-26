"""Foreign umpire analysis"""

import matplotlib.pyplot as plt

from match_file_reader import data_matches
from umpire_file_reader import data_umpires


def calculate(data, umpires):
    """Finding the count of foreign umpires country wise"""
    result = {}
    umpire_list = set()
    for match in data():
        for element in ["umpire1", "umpire2", "umpire3"]:
            umpire_list.add(match[element])
    for umpire in umpires():
        country = umpire["country"]
        umpire_name = umpire["umpire"]
        if country != "India" and umpire_name in umpire_list:
            if country not in result:
                result[country] = 1
            else:
                result[country] += 1

    country_names = result.keys()
    country_count = result.values()
    return country_names, country_count


def plot(countries, count):
    """Plotting the result in the bar chart"""
    plt.figure(figsize=(12, 7))
    plt.title("Foreign umpire analysis", fontsize=14, fontweight="bold")
    plt.bar(countries, count, color="steelblue", edgecolor="black")
    plt.xlabel("Country name", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution3.png", dpi=300)
    plt.show()


def execute(record, umpire):
    """Executing the calculation and plotting of data in bar chart"""
    country, count = calculate(record, umpire)
    plot(country, count)


if __name__ == "__main__":
    execute(data_matches, data_umpires)
