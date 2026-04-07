import json

with open("student.json", "r", encoding="utf-8") as student_json:
    data = json.load(student_json)

result = data | {"City": "Москва"}

with open("student.json", "w", encoding="utf-8") as student_json:
    json.dump(result, student_json, indent=4, ensure_ascii=False)