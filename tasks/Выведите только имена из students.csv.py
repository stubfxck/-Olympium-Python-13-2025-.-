import csv

# Пример содержания students.csv:
#
# with open("students.csv", "w", encoding="utf-8", newline='') as students_csv:
#     writer = csv.writer(students_csv, dialect="excel", delimiter=":")
#     writer.writerows([
#         ["Петя", "21", "11В"],
#         ["Катя", "20", "11А"]
#     ])

with open("students.csv", "r", encoding="utf-8", newline='') as students_csv:
    reader = csv.reader(students_csv, dialect="excel", delimiter=":")
    result = []
    for row in reader:
        result.append(row[0])

print(result)