with open("data.txt", "w", encoding="utf-8-sig") as data:
    print("Текст\nЕще текст", file=data)

with open("data.txt", "r", encoding="utf-8-sig") as data:
    text = data.read()
    print(text)