with open("numbers.txt", "w", encoding="utf-8-sig") as numbers_file:
    print("У меня 3 яблока, 2.5 груши и 100 бананов.", file=numbers_file)

with open("numbers.txt", "r", encoding="utf-8-sig") as numbers_file:
    import re
    pattern = r"\d+\.\d+|\d+"
    result = re.findall(pattern, numbers_file.read())
    s = ""
    print(f"Результат: {", ".join(result)}")