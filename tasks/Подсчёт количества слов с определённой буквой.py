spisok = ["дом", "дорога", "лист", "дерево"]
result = 0

userinput = input("Введите букву: ")

for word in spisok:
    for letter in word:
        if letter == userinput:
            result += 1
            break

print(result)