import json 

input_data = {
    "theme": "dark",
    "font_size": 12,
    "language": "ru"
}

with open("settings.json", "w", encoding="utf-8") as settings_json:
    json.dump(input_data, settings_json, ensure_ascii=False, indent=4)