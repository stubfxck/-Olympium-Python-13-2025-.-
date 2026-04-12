import requests
import json

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=demo")

with open("headers.json", "w", encoding="utf-8") as headers_json:

    data = {}

    for key, value in response.headers.items():
        data[key] = value

    json.dump(data, headers_json, ensure_ascii=False, indent=4) 