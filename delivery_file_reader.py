import csv

def data_delivery():
    with open("deliveries.csv", mode="r", encoding="utf-8") as csv_file:
        records = list(csv.DictReader(csv_file))

    for delivery in records:
        yield delivery

data_delivery()
