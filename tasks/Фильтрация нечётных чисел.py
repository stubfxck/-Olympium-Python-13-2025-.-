spisok = [1, 2, 3, 4, 5, 6, 7, 8]

for num in spisok:
    
    if num % 2 == 0:
        spisok.remove(num)


print(f"Чётные числа из списка: {str(spisok)[1:-1]}")