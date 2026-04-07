num = int(input("Введите число: "))

nums = [3, 8, 1, 7, 5]
result = []

for i in nums:
    if i > num:
        result.append(str(i))

print(f"Результат: {', '.join(result)}")