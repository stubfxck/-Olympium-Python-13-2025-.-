import json

# Непонятная формулировка "построчно печатая", так же ни примеров ни даже примерного содержимого "student_updated.json"

with open("student_updated.json", "r", encoding="utf-8") as student_updated_json:
    data = json.load(student_updated_json)
    for row_key, row_value in data.items():
        print(f"Ключ: {row_key}, Значение: {row_value}")