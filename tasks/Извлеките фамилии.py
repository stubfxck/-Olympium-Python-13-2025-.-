
import re

with open("names.txt", "w", encoding="utf-8-sig") as namesfile:
    print("Иванов И.И., Петрова А.Б., Сидоров В.В.", file=namesfile)

with open("names.txt", "r", encoding="utf-8-sig") as namesfile:
    pattern = r".+ов|.+ова"
    names = namesfile.read().split()
    for name in names:
        match = re.match(pattern, name)
        if match:
            print(match.group())
    # Ожидаемый вывод: Иванов, Петрова, Сидоров
    