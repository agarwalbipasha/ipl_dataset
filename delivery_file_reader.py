"""Reading the deliveries.csv file for further calculation"""

import csv

def data_delivery():
    """Yield delivery records as dictionaries from CSV file"""
    with open("deliveries.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))
        yield from records

data_delivery()
