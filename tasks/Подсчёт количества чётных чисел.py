spisok = [1, 2, 3, 4, 5, 6, 7, 8]
result = 0

for char in spisok:
    if char % 2 != 0:
        result += 1

print(result)