import re

with open("english.txt", "w", encoding="utf-8-sig") as englishfile:
    print("Welcome to Python programming. John and alice joined us.", file=englishfile)

with open("english.txt", "r", encoding="utf-8-sig") as englishfile:
    pattern = r"[A-Z][a-z]+"
    text = englishfile.read()
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)