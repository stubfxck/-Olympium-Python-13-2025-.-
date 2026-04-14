import json
import os

data = {
    "name": "Иван",
    "city": "Москва"
}

if not os.path.exists("info.json"):
    with open("info.json", "w", encoding="utf-8") as info_json_w:
        json.dump(data, info_json_w, ensure_ascii=False, indent=4)

with open("info.json", "r", encoding="utf-8") as info_json_r:
    data_r = json.load(info_json_r)
    print(data["city"])