import requests
from html import unescape

response = requests.get("https://novkrp.ru/raspisanie.htm")

data = unescape(response.text)

with open("response.htm", "w", encoding="utf-8") as response_htm:
    response_htm.write(data)
