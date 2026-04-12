import csv

with open("products.csv", "w", encoding="utf-8", newline='') as products_csv:
    writer = csv.writer(products_csv, "excel", delimiter=",")

    writer.writerows([
        ["Название", "Цена"],
        ["Хлеб", 79],
        ["Молоко", 135],
        ["Сыр", 270]
    ])

# with open("products.csv", "r", encoding="utf-8") as products_csv:
#     reader = csv.reader(products_csv, "excel", delimiter=",")
#     for row in reader:
#         print(row)