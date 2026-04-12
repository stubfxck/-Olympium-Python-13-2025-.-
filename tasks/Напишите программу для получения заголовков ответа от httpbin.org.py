import requests

response = requests.get("https://httpbin.org/get")

print(f"Заголовки: {response.headers}")