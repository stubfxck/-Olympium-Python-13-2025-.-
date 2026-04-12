import csv

with open("subjects.csv", "w", encoding="utf-8", newline="") as subjects_csv:
    data = csv.writer(subjects_csv, "excel", delimiter=",")
    data.writerows([
        ["Имя", "Математика", "Русский", "Английский"],
        ["Анна", 5, 4, 3],
        ["Дмитрий", 3, 4, 5]
    ])

# with open("subjects.csv", "r", encoding="utf-8", newline="") as subjects_csv:
#     data = csv.reader(subjects_csv, "excel", delimiter=",")
#     for row in data:
#         print(row)