import re

with open("tags.txt", "w", encoding="utf-8-sig") as tagsfile:
    print("[python] [regex] [data]", file=tagsfile)

with open("tags.txt", "r", encoding="utf-8-sig") as tagsfile:
    pattern = r"\[|\]"
    content = tagsfile.read()
    clear = re.sub(pattern, "", content)
    print("Слова внутри квадратных скобок:", clear)