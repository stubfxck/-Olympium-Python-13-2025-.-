import json

# Пример содержания: 
#
# with open("student.json", "w", encoding="utf-8") as student_json:
#     info = {
#         "Name": "Петя",
#         "Age": 19
#     }
#     json.dump(info, student_json, indent=4, ensure_ascii=False)

with open("student.json", "r", encoding="utf-8") as student_json:
    data = json.load(student_json)
    print("Имя ученика:", data["Name"])