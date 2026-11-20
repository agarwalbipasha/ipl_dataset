"""Reading the ipl_umpires_countries.csv file for further calculation"""
import csv

def data_umpires():
    """Yield umpire records as dictionaries from CSV file"""
    with open("ipl_umpires_countries.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))
        yield from records


data_umpires()
