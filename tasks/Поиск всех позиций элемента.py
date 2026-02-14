spisok = [1, 5, 7, 3, 5, 9]
five_elem = []

for i, elem in enumerate(spisok):
    if elem == 5:
        five_elem.append(i)

print(f"Все индексы чисел 5 в списке: {five_elem}")