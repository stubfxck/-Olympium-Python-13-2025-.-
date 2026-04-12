import csv

with open("grades.csv", "a", encoding="utf-8", newline="") as grades_csv:
    writer = csv.writer(grades_csv, dialect="excel", delimiter=":")

    writer.writerows([
        ["Имя", "Оценка"],
        ["Анна", 5],
        ["Дмитрий", 2],
        ["Владислав", 4]
    ])

# Проверка:
#
# with open("grades.csv", "r", encoding="utf-8", newline="") as grades_csv:
#     reader = csv.reader(grades_csv, dialect="excel", delimiter=":")

#     for row in reader:
#         print(row)