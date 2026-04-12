import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=demo")

print(f"Код ответа: {response.status_code}")