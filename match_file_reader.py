import csv

def data_matches():
    with open("matches.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))

    for match in records:
        yield match

data_matches()
