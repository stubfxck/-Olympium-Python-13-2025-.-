with open("numbers.txt", "w", encoding="utf-8") as numbers_txt:
    for i in range(1, 11):
        print(i, file=numbers_txt)