import re

with open("dates.txt", "w", encoding="utf-8-sig") as dates:
    print("Сегодня 21.05.2023, а завтра 22.05.2023.", "Вчера было 20.05.2023.", sep="\n", file=dates)

with open("dates.txt", "r", encoding="utf-8-sig") as dates:
    content = dates.read()
    pattern = r"\d{2}\.\d{2}\.\d{4}"
    a = re.findall(pattern, content)
    print(f"Кол-во дат: {len(a)}")