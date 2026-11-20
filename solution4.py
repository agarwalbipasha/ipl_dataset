# Stacked chart of matches played by team by season
# Plot a stacked bar chart of ...
#
# number of games played
# by team
# by season

from match_file_reader import data_matches

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





calculate(data_matches)
