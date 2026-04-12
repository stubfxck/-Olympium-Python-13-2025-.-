import csv
import json

names_list = []

with open("students.csv", "r", encoding="utf-8") as students_csv:
    reader = csv.DictReader(students_csv, dialect="excel", delimiter=":")

    for data in reader:
        names_list.append(data["Имя"])


with open("names.json", "w", encoding="utf-8") as names_json:
    json.dump(names_list, names_json, ensure_ascii=False, indent=4)