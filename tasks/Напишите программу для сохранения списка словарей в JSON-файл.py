import json

user_list = []

for i in range(3):
    user_list.append({
    "name": f"Name{i}",
    "age": i
    })

with open("users.json", "w", encoding="utf-8") as users_json:
    json.dump(user_list, users_json, ensure_ascii=False, indent=4)