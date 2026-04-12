import csv

with open("products.csv", "r", encoding="utf-8", newline='') as products_csv:
    reader = csv.reader(products_csv, "excel", delimiter=",")
    next(reader)
    for product, price in reader:
        if int(price) >= 50:
            print(product, price)