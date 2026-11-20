"""Reading the matches.csv file for further calculation"""
import csv

def data_matches():
    """Yield match records as dictionaries from CSV file"""
    with open("matches.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))
        yield from records

data_matches()
