import csv

grades = []

with open("subjects.csv", "r", encoding="utf-8", newline='') as subjects_csv:
    data = csv.DictReader(subjects_csv, delimiter=",")
    for row in data:
        grades.append(int(row["Математика"]))

print(f"Средний балл: {int(sum(grades) / len(grades))}")