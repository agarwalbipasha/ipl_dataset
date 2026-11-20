# Stacked chart of matches played by team by season
# Plot a stacked bar chart of ...
#
# number of games played
# by team
# by season

from match_file_reader import data_matches
import matplotlib.pyplot as plt

def calculate(matches):
    result = {}
    for match in matches():
        year = int(match["season"])
        for team in ["team1", "team2"]:
            if year in result:
                if match[team] in result[year]:
                    result[year][match[team]] += 1
                else:
                    result[year][match[team]] = 1
            else:
                result[year] = {match[team]: 1}

    matches_team_season = {year: dict(sorted(team.items())) for year, team in sorted(result.items())}

    return matches_team_season

def plot(match):
    years = match.keys()
    teams = sorted({team for season_data in match.values() for team in season_data})
    bottom_heights = [0] * len(years)
    plt.figure(figsize=(12,7))
    for team in teams:
        team_wins = [match[year].get(team, 0) for year in years]
        plt.bar(years, team_wins, bottom = bottom_heights, label=team)
        bottom_heights = [current + added for current, added in zip(bottom_heights, team_wins)]
    plt.title("Stacked chart of matches played by team by season", fontsize=14, fontweight="bold")
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Number of matches", fontsize=12)
    plt.legend(title="Teams", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("output/solution4.png", dpi=300)
    plt.show()

def execute(match):
    matches = calculate(match)
    plot(matches)

execute(data_matches)
