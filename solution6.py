"""Number of matches won per team per year in IPL"""

import matplotlib.pyplot as plt

from match_file_reader import data_matches


def calculate(matches):
    """Calculating the number of matches won per team per year"""
    result = {}
    for match in matches():
        year = int(match["season"])
        winner = match["winner"]
        if year in result:
            if winner in result[year]:
                result[year][winner] += 1
            else:
                result[year][winner] = 1
        else:
            result[year] = {winner: 1}

    sorted_result = {
        year: dict(sorted(record.items())) for year, record in sorted(result.items())
    }
    return sorted_result


def plot(match):
    """Plotting the result in the stacked bar chart"""
    years = match.keys()
    teams = sorted({team for season_data in match.values() for team in season_data})
    bottom_heights = [0] * len(years)
    plt.figure(figsize=(12, 7))
    for team in teams:
        team_wins = [match[year].get(team, 0) for year in years]
        plt.bar(years, team_wins, bottom=bottom_heights, label=team)
        bottom_heights = [
            current + added for current, added in zip(bottom_heights, team_wins)
        ]
    plt.title(
        "Stacked chart of number of matches won per team per year",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Number of matches", fontsize=12)
    plt.legend(title="Teams", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution6.png", dpi=300)
    plt.show()


def execute(match):
    """Executing the calculation and plotting of data in stacked bar chart"""
    matches = calculate(match)
    plot(matches)


if __name__ == "__main__":
    execute(data_matches)
