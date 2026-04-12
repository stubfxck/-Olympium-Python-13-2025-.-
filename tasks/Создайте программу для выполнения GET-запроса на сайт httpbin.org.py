import requests

response = requests.get("https://httpbin.org/get")

print(f"Код ответа {response.status_code}")