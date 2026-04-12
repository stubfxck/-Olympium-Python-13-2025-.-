import csv

result = []

with open("grades.csv", "r", encoding="utf-8") as grades_csv:
    reader = csv.reader(grades_csv, "excel", delimiter=":")
    next(reader)
    for name, grade in reader:
        result.append(grade)

print(f"Количество учеников с пятерками: {result.count('5')}")