import requests

response = requests.get("https://yandex.ru")

print(f"Длинна текста ответа {len(response.text)}")