import requests

response = requests.get("https://api.github.com")

for value in response.headers.values():
    print(value)