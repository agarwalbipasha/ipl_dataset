import csv

def data_umpires():
    with open("ipl_umpires_countries.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))

    for umpire in records:
        yield umpire

data_umpires()
