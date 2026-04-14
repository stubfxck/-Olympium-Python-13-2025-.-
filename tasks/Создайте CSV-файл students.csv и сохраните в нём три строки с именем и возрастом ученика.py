import csv

with open("students.csv", "w", encoding="utf-8", newline="") as students_csv:
    data = csv.writer(students_csv, "excel", delimiter=",")
    data.writerows([
        ["Имя", "Возраст"],
        ["Иван", "19"],
        ["Дарья", "18"],
        ["Дмитрий", "19"]
    ])

with open("students.csv", "r", encoding="utf-8") as students_csv:
    data = csv.reader(students_csv, "excel", delimiter=",")
    for item in data:
        print(item)