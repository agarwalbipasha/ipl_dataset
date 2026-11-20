# Number of matches won per team per year in IPL.

from match_file_reader import data_matches

def calculate(matches):
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

    sorted_result = {year: dict(sorted(record.items())) for year, record in sorted(result.items())}
    print(sorted_result)

calculate(data_matches)
