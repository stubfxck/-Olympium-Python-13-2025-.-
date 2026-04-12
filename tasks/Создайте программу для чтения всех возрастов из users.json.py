import json

age_list = []

with open("users.json", "r", encoding="utf-8") as users_json:
    data = json.load(users_json)
    for user_age in data:
        age_list.append(user_age["age"])

print(age_list)