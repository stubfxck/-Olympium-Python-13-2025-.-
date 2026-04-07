import json

with open("new_student.json", "w", encoding="utf-8") as new_student_json:
    data = {
        "name": "Иван",
        "age": 15,
        "grades": [4, 5, 4]
    }
    json.dump(data, new_student_json, indent=4, ensure_ascii=False)

# Прочитать:
#
# with open("new_student.json", "r", encoding="utf-8") as new_student_json:
#     data = json.load(new_student_json)
#     print(data)