import json

with open("settings.json", "r", encoding="utf-8") as settings_json:
    data = json.load(settings_json)

data["font_size"] = 14

with open("settings.json", "w", encoding="utf-8") as settings_json:
    json.dump(data, settings_json, ensure_ascii=False, indent=4)