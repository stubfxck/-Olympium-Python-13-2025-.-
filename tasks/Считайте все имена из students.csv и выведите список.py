import csv

names_list = []

with open("students.csv", "r", encoding="utf-8") as students_csv:
    reader = csv.DictReader(students_csv, dialect="excel", delimiter=":")

    for data in reader:
        names_list.append(data["Имя"])


print(names_list)