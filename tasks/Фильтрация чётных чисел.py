spisok = [1, 2, 3, 4, 5, 6, 7, 8]
result = []

for num in spisok:
    
    if num % 2 == 0:
        result.append(num)


print(f"Чётные числа из списка: {str(result)[1:-1]}")