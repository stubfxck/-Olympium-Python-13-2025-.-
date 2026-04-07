with open("output.txt", "w", encoding="utf-8-sig") as output:
    print("Текст\nЕще текст", file=output)

# Проверка
# with open("output.txt", "r", encoding="utf-8-sig") as output:
#     text = output.readlines()
#     [print(line.strip()) for line in text]