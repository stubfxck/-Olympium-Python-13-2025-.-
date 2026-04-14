import os
import json
import requests
from datetime import datetime

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

if not os.path.exists(date_str):
    os.mkdir(date_str)

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()

report_data = {
    "date": date_str,
    "fact": data["fact"],
    "length": data["length"]
}

with open(f"{date_str}/report.json", "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=4)

with open(f"{date_str}/report.txt", "w", encoding="utf-8") as f:
    f.write(f"Дата: {date_str}\n")
    f.write(f"Факт о коте: {data['fact']}\n")
    f.write(f"Длина факта: {data['length']}\n")

print("Отчёт сохранён в папке:", date_str)