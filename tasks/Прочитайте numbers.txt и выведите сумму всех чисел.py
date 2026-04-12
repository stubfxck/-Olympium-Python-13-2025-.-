result = 0

with open("numbers.txt", "r", encoding="utf-8") as numbers_txt:
    data = numbers_txt.readlines()
    for item in data:
        result += int(item.strip())

print(result)