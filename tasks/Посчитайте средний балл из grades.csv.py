import csv

grade_list = []

with open("grades.csv", "r", encoding="utf-8") as grades_csv:
    reader = csv.DictReader(grades_csv, dialect="excel", delimiter=":")
    for data in reader:
        grade_list.append(int(data["Оценка"]))

print(f"Средний балл: {int(sum(grade_list) / len(grade_list))}, (Оценки: {grade_list})")